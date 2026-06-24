"""
Protocolo ADA - Etapa 06: Validacao Final dos Dados Finais

Finalidade:
- Ler somente os arquivos finais em dados/finais/.
- Validar existencia, leitura, estrutura, chaves, relacionamentos, calendario,
  campos sensiveis, nulos preservados e pontos de atencao para Power BI.
- Gerar relatorios/06_relatorio_validacao_dados_finais.md.

Regras de seguranca:
- Este script nao altera dados brutos.
- Este script nao altera dados tratados.
- Este script nao altera dados finais.
- Este script nao cria KPIs finais complexos.
- Este script nao cria dashboard.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
import re

import pandas as pd

from ada_relatorios import (
    escrever_relatorio_preservando_validacao,
    montar_secao_validacao_humana,
)


PASTA_RAIZ = Path(__file__).resolve().parents[1]
PASTA_FINAIS = PASTA_RAIZ / "dados" / "finais"
PASTA_RELATORIOS = PASTA_RAIZ / "relatorios"
RELATORIO_SAIDA = PASTA_RELATORIOS / "06_relatorio_validacao_dados_finais.md"

ARQUIVOS_FINAIS = [
    "dim_clientes.csv",
    "dim_rotas.csv",
    "dim_caminhoes.csv",
    "fato_cargas.csv",
    "fato_viagens.csv",
    "fato_eventos_entrega.csv",
    "fato_abastecimentos.csv",
    "dim_calendario.csv",
]

CHAVES_DIMENSOES = {
    "dim_clientes.csv": "customer_id",
    "dim_rotas.csv": "route_id",
    "dim_caminhoes.csv": "truck_id",
    "dim_calendario.csv": "data",
}

CHAVES_FATOS = {
    "fato_cargas.csv": "load_id",
    "fato_viagens.csv": "trip_id",
    "fato_eventos_entrega.csv": "event_id",
    "fato_abastecimentos.csv": "fuel_purchase_id",
}

RELACIONAMENTOS = [
    ("fato_cargas.csv", "customer_id", "dim_clientes.csv", "customer_id"),
    ("fato_cargas.csv", "route_id", "dim_rotas.csv", "route_id"),
    ("fato_viagens.csv", "load_id", "fato_cargas.csv", "load_id"),
    ("fato_viagens.csv", "truck_id", "dim_caminhoes.csv", "truck_id"),
    ("fato_eventos_entrega.csv", "trip_id", "fato_viagens.csv", "trip_id"),
    ("fato_abastecimentos.csv", "trip_id", "fato_viagens.csv", "trip_id"),
    ("fato_abastecimentos.csv", "truck_id", "dim_caminhoes.csv", "truck_id"),
]

NULOS_OPERACIONAIS = [
    ("fato_viagens.csv", "driver_id"),
    ("fato_viagens.csv", "truck_id"),
    ("fato_viagens.csv", "trailer_id"),
    ("fato_abastecimentos.csv", "driver_id"),
    ("fato_abastecimentos.csv", "truck_id"),
    ("fato_eventos_entrega.csv", "actual_datetime"),
]

CAMPOS_RISCO_AGREGACAO = [
    ("fato_viagens.csv", "average_mpg", "Media operacional; usar media ponderada ou regra validada, nunca soma simples."),
    ("fato_abastecimentos.csv", "price_per_gallon", "Preco unitario; usar media ponderada por galoes ou regra validada."),
    ("dim_rotas.csv", "base_rate_per_mile", "Taxa por milha; nao representa valor total da rota."),
    ("dim_rotas.csv", "fuel_surcharge_rate", "Taxa/percentual; confirmar escala e formatacao no Power BI."),
]

CAMPOS_DATA_FATOS = [
    ("fato_cargas.csv", "load_date"),
    ("fato_viagens.csv", "dispatch_date"),
    ("fato_eventos_entrega.csv", "scheduled_datetime"),
    ("fato_eventos_entrega.csv", "actual_datetime"),
    ("fato_abastecimentos.csv", "purchase_date"),
]


def ler_csv(caminho: Path) -> tuple[pd.DataFrame | None, str]:
    """Le um CSV final sem alterar o arquivo."""
    try:
        return pd.read_csv(caminho, low_memory=False), ""
    except Exception as erro:  # noqa: BLE001 - erro deve aparecer no relatorio
        return None, f"{type(erro).__name__}: {erro}"


def formatar_valor(valor: Any) -> str:
    """Formata valores para tabelas Markdown."""
    if pd.isna(valor):
        return ""
    if isinstance(valor, float):
        return f"{valor:.2f}"
    return str(valor).replace("\n", " ").replace("|", "\\|")


def formatar_tabela(linhas: list[dict[str, Any]], colunas: list[str]) -> str:
    """Cria tabela Markdown simples."""
    if not linhas:
        return "Sem registros para exibir."

    cabecalho = "| " + " | ".join(colunas) + " |"
    separador = "| " + " | ".join("---" for _ in colunas) + " |"
    corpo = []
    for linha in linhas:
        corpo.append("| " + " | ".join(formatar_valor(linha.get(coluna, "")) for coluna in colunas) + " |")
    return "\n".join([cabecalho, separador, *corpo])


def percentual(parte: int, total: int) -> str:
    """Calcula percentual formatado evitando divisao por zero."""
    if total == 0:
        return "0.00%"
    return f"{parte / total * 100:.2f}%"


def status_prioritario(statuses: list[str]) -> str:
    """Resume varios status em um status geral."""
    if "Crítico" in statuses:
        return "Crítico"
    if "Atenção" in statuses:
        return "Atenção"
    return "OK"


def carregar_arquivos() -> tuple[dict[str, pd.DataFrame], list[dict[str, Any]]]:
    """Confirma existencia e leitura dos arquivos finais esperados."""
    tabelas: dict[str, pd.DataFrame] = {}
    resultados = []

    for nome in ARQUIVOS_FINAIS:
        caminho = PASTA_FINAIS / nome
        existe = caminho.exists()
        tabela, erro = (None, "arquivo ausente")
        if existe:
            tabela, erro = ler_csv(caminho)
        if tabela is not None:
            tabelas[nome] = tabela

        status = "OK" if existe and tabela is not None else "Crítico"
        resultados.append(
            {
                "arquivo": nome,
                "caminho": f"dados/finais/{nome}",
                "existe": "Sim" if existe else "Não",
                "leitura": "OK" if tabela is not None else "Falhou",
                "linhas": len(tabela) if tabela is not None else "",
                "colunas": len(tabela.columns) if tabela is not None else "",
                "erro": erro,
                "status": status,
            }
        )

    return tabelas, resultados


def estrutura_arquivos(tabelas: dict[str, pd.DataFrame]) -> list[dict[str, Any]]:
    """Registra linhas, colunas e nomes de colunas dos arquivos finais."""
    linhas = []
    for nome in ARQUIVOS_FINAIS:
        tabela = tabelas.get(nome)
        if tabela is None:
            continue
        linhas.append(
            {
                "arquivo": nome,
                "linhas": len(tabela),
                "colunas": len(tabela.columns),
                "nomes das colunas": ", ".join(tabela.columns),
                "status": "OK",
            }
        )
    return linhas


def validar_chave_unica(tabela: pd.DataFrame, arquivo: str, chave: str, escopo: str) -> dict[str, Any]:
    """Valida nulos e duplicidades em uma chave."""
    if chave not in tabela.columns:
        return {
            "escopo": escopo,
            "arquivo": arquivo,
            "chave": chave,
            "linhas": len(tabela),
            "nulos": "",
            "duplicidades": "",
            "valores únicos": "",
            "status": "Crítico",
            "observação": "Coluna de chave ausente.",
        }

    nulos = int(tabela[chave].isna().sum())
    duplicidades = int(tabela.duplicated(subset=[chave], keep=False).sum())
    unicos = int(tabela[chave].nunique(dropna=True))
    status = "OK" if nulos == 0 and duplicidades == 0 else "Crítico"
    return {
        "escopo": escopo,
        "arquivo": arquivo,
        "chave": chave,
        "linhas": len(tabela),
        "nulos": nulos,
        "duplicidades": duplicidades,
        "valores únicos": unicos,
        "status": status,
        "observação": "Chave sem nulos e sem duplicidades." if status == "OK" else "Chave exige correção antes do modelo.",
    }


def validar_chaves(tabelas: dict[str, pd.DataFrame]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Valida chaves das dimensoes e duplicidades relevantes nas fatos."""
    dimensoes = []
    fatos = []

    for arquivo, chave in CHAVES_DIMENSOES.items():
        tabela = tabelas.get(arquivo)
        if tabela is not None:
            dimensoes.append(validar_chave_unica(tabela, arquivo, chave, "dimensão"))

    for arquivo, chave in CHAVES_FATOS.items():
        tabela = tabelas.get(arquivo)
        if tabela is not None:
            fatos.append(validar_chave_unica(tabela, arquivo, chave, "fato"))

    return dimensoes, fatos


def validar_relacionamentos(tabelas: dict[str, pd.DataFrame]) -> list[dict[str, Any]]:
    """Valida relacionamentos esperados por intersecao de chaves."""
    resultados = []
    for origem, coluna_origem, destino, coluna_destino in RELACIONAMENTOS:
        tabela_origem = tabelas.get(origem)
        tabela_destino = tabelas.get(destino)
        if tabela_origem is None or tabela_destino is None:
            resultados.append(
                {
                    "origem": origem,
                    "coluna origem": coluna_origem,
                    "destino": destino,
                    "coluna destino": coluna_destino,
                    "valores origem": "",
                    "sem correspondência": "",
                    "nulos origem": "",
                    "status": "Crítico",
                    "observação": "Tabela de origem ou destino ausente/ilegível.",
                }
            )
            continue
        if coluna_origem not in tabela_origem.columns or coluna_destino not in tabela_destino.columns:
            resultados.append(
                {
                    "origem": origem,
                    "coluna origem": coluna_origem,
                    "destino": destino,
                    "coluna destino": coluna_destino,
                    "valores origem": "",
                    "sem correspondência": "",
                    "nulos origem": "",
                    "status": "Crítico",
                    "observação": "Coluna de relacionamento ausente.",
                }
            )
            continue

        serie_origem = tabela_origem[coluna_origem]
        valores_origem = set(serie_origem.dropna().astype(str))
        valores_destino = set(tabela_destino[coluna_destino].dropna().astype(str))
        sem_correspondencia = len(valores_origem - valores_destino)
        nulos = int(serie_origem.isna().sum())
        status = "OK" if sem_correspondencia == 0 else "Atenção"
        resultados.append(
            {
                "origem": origem,
                "coluna origem": coluna_origem,
                "destino": destino,
                "coluna destino": coluna_destino,
                "valores origem": len(valores_origem),
                "sem correspondência": sem_correspondencia,
                "nulos origem": nulos,
                "status": status,
                "observação": "Nulos preservados foram ignorados na correspondência." if nulos else "Sem nulos na chave de origem.",
            }
        )
    return resultados


def validar_campos_sensiveis(tabelas: dict[str, pd.DataFrame]) -> list[dict[str, Any]]:
    """Valida remocao ou mascaramento de campos sensiveis nos dados finais."""
    resultados = []

    dim_caminhoes = tabelas.get("dim_caminhoes.csv")
    vin_existe = dim_caminhoes is not None and "vin" in dim_caminhoes.columns
    resultados.append(
        {
            "arquivo": "dim_caminhoes.csv",
            "campo": "vin",
            "regra": "não deve existir nos dados finais",
            "resultado": "Existe" if vin_existe else "Ausente",
            "status": "Crítico" if vin_existe else "OK",
        }
    )

    fato_abastecimentos = tabelas.get("fato_abastecimentos.csv")
    fuel_card_existe = fato_abastecimentos is not None and "fuel_card_number" in fato_abastecimentos.columns
    resultados.append(
        {
            "arquivo": "fato_abastecimentos.csv",
            "campo": "fuel_card_number",
            "regra": "não deve existir nos dados finais",
            "resultado": "Existe" if fuel_card_existe else "Ausente",
            "status": "Crítico" if fuel_card_existe else "OK",
        }
    )

    dim_clientes = tabelas.get("dim_clientes.csv")
    if dim_clientes is None or "customer_name" not in dim_clientes.columns:
        resultados.append(
            {
                "arquivo": "dim_clientes.csv",
                "campo": "customer_name",
                "regra": "se existir, deve estar mascarado",
                "resultado": "Coluna ausente",
                "status": "OK",
            }
        )
    else:
        serie = dim_clientes["customer_name"].dropna().astype(str)
        padrao_mascara = re.compile(r"^Cliente_\d{3,}$")
        fora_padrao = int((~serie.str.match(padrao_mascara)).sum())
        resultados.append(
            {
                "arquivo": "dim_clientes.csv",
                "campo": "customer_name",
                "regra": "se existir, deve estar mascarado",
                "resultado": f"{fora_padrao} valores fora do padrão Cliente_###",
                "status": "OK" if fora_padrao == 0 else "Crítico",
            }
        )

    return resultados


def validar_nulos_operacionais(tabelas: dict[str, pd.DataFrame]) -> list[dict[str, Any]]:
    """Registra nulos preservados em campos operacionais importantes."""
    resultados = []
    for arquivo, coluna in NULOS_OPERACIONAIS:
        tabela = tabelas.get(arquivo)
        if tabela is None:
            continue
        if coluna not in tabela.columns:
            resultados.append(
                {
                    "arquivo": arquivo,
                    "coluna": coluna,
                    "linhas": len(tabela),
                    "nulos": "",
                    "percentual": "",
                    "status": "Atenção",
                    "observação": "Campo operacional esperado não encontrado.",
                }
            )
            continue
        nulos = int(tabela[coluna].isna().sum())
        resultados.append(
            {
                "arquivo": arquivo,
                "coluna": coluna,
                "linhas": len(tabela),
                "nulos": nulos,
                "percentual": percentual(nulos, len(tabela)),
                "status": "Atenção" if nulos > 0 else "OK",
                "observação": "Nulos preservados; validar interpretação no Power BI." if nulos else "Sem nulos observados.",
            }
        )
    return resultados


def validar_campos_agregacao(tabelas: dict[str, pd.DataFrame]) -> list[dict[str, Any]]:
    """Lista campos que exigem cuidado de agregacao no Power BI."""
    resultados = []
    for arquivo, campo, cuidado in CAMPOS_RISCO_AGREGACAO:
        tabela = tabelas.get(arquivo)
        existe = tabela is not None and campo in tabela.columns
        resultados.append(
            {
                "arquivo": arquivo,
                "campo": campo,
                "existe": "Sim" if existe else "Não",
                "risco": cuidado,
                "status": "Atenção" if existe else "Crítico",
            }
        )
    return resultados


def menor_maior_data(serie: pd.Series) -> tuple[str, str, int]:
    """Converte uma serie em datas e retorna menor, maior e invalidos."""
    datas = pd.to_datetime(serie, errors="coerce").dt.normalize()
    invalidos = int(serie.notna().sum() - datas.notna().sum())
    if not datas.notna().any():
        return "", "", invalidos
    return str(datas.min().date()), str(datas.max().date()), invalidos


def validar_calendario(tabelas: dict[str, pd.DataFrame]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Valida a dimensao calendario e sua cobertura das datas das fatos."""
    calendario = tabelas.get("dim_calendario.csv")
    resumo = []
    cobertura = []

    if calendario is None:
        resumo.append(
            {
                "checagem": "existência da dim_calendario.csv",
                "resultado": "arquivo ausente ou ilegível",
                "status": "Crítico",
            }
        )
        return resumo, cobertura

    if "data" not in calendario.columns:
        resumo.append({"checagem": "coluna de data", "resultado": "coluna data ausente", "status": "Crítico"})
        return resumo, cobertura

    datas_cal = pd.to_datetime(calendario["data"], errors="coerce").dt.normalize()
    invalidas = int(calendario["data"].notna().sum() - datas_cal.notna().sum())
    duplicadas = int(calendario.duplicated(subset=["data"], keep=False).sum())
    menor = str(datas_cal.min().date()) if datas_cal.notna().any() else ""
    maior = str(datas_cal.max().date()) if datas_cal.notna().any() else ""

    resumo.extend(
        [
            {"checagem": "coluna de data", "resultado": "coluna data encontrada", "status": "OK"},
            {"checagem": "datas inválidas", "resultado": invalidas, "status": "OK" if invalidas == 0 else "Atenção"},
            {"checagem": "datas duplicadas", "resultado": duplicadas, "status": "OK" if duplicadas == 0 else "Crítico"},
            {"checagem": "período mínimo", "resultado": menor, "status": "OK" if menor else "Crítico"},
            {"checagem": "período máximo", "resultado": maior, "status": "OK" if maior else "Crítico"},
        ]
    )

    datas_cal_set = set(datas_cal.dropna())
    for arquivo, coluna in CAMPOS_DATA_FATOS:
        tabela = tabelas.get(arquivo)
        if tabela is None or coluna not in tabela.columns:
            cobertura.append(
                {
                    "arquivo": arquivo,
                    "coluna": coluna,
                    "menor data": "",
                    "maior data": "",
                    "datas fora do calendário": "",
                    "datas inválidas": "",
                    "status": "Atenção",
                }
            )
            continue

        datas = pd.to_datetime(tabela[coluna], errors="coerce").dt.normalize()
        invalidas_fato = int(tabela[coluna].notna().sum() - datas.notna().sum())
        fora = int((~datas.dropna().isin(datas_cal_set)).sum())
        menor_fato, maior_fato, _ = menor_maior_data(tabela[coluna])
        status = "OK" if fora == 0 and invalidas_fato == 0 else "Atenção"
        cobertura.append(
            {
                "arquivo": arquivo,
                "coluna": coluna,
                "menor data": menor_fato,
                "maior data": maior_fato,
                "datas fora do calendário": fora,
                "datas inválidas": invalidas_fato,
                "status": status,
            }
        )

    return resumo, cobertura


def contar_status(linhas: list[dict[str, Any]]) -> dict[str, int]:
    """Conta status OK/Atenção/Crítico em uma lista de resultados."""
    contagem = {"OK": 0, "Atenção": 0, "Crítico": 0}
    for linha in linhas:
        status = linha.get("status")
        if status in contagem:
            contagem[status] += 1
    return contagem


def combinar_contagens(conjuntos: list[list[dict[str, Any]]]) -> dict[str, int]:
    """Combina contagens de status."""
    total = {"OK": 0, "Atenção": 0, "Crítico": 0}
    for linhas in conjuntos:
        parcial = contar_status(linhas)
        for status, quantidade in parcial.items():
            total[status] += quantidade
    return total


def gerar_relatorio() -> tuple[int, dict[str, int]]:
    """Executa validacoes e gera relatorio Markdown."""
    PASTA_RELATORIOS.mkdir(parents=True, exist_ok=True)

    tabelas, existencia = carregar_arquivos()
    estrutura = estrutura_arquivos(tabelas)
    chaves_dimensoes, chaves_fatos = validar_chaves(tabelas)
    relacionamentos = validar_relacionamentos(tabelas)
    calendario_resumo, calendario_cobertura = validar_calendario(tabelas)
    sensiveis = validar_campos_sensiveis(tabelas)
    nulos = validar_nulos_operacionais(tabelas)
    agregacao = validar_campos_agregacao(tabelas)

    temas = {
        "existência e leitura dos arquivos finais": existencia,
        "estrutura dos arquivos finais": estrutura,
        "chaves das dimensões": chaves_dimensoes,
        "duplicidades nas tabelas fato": chaves_fatos,
        "relacionamentos esperados": relacionamentos,
        "dimensão calendário": calendario_resumo,
        "cobertura temporal das fatos": calendario_cobertura,
        "campos sensíveis": sensiveis,
        "nulos operacionais preservados": nulos,
        "campos com risco de agregação indevida": agregacao,
    }
    matriz = [
        {
            "tema": tema,
            "status": status_prioritario([linha.get("status", "OK") for linha in linhas]),
        }
        for tema, linhas in temas.items()
    ]
    contagem = combinar_contagens(list(temas.values()))
    arquivos_validados = sum(1 for nome in ARQUIVOS_FINAIS if nome in tabelas)

    recomendacao = (
        "Avançar para documentação de KPIs e modelagem no Power BI com ressalvas de atenção aos nulos "
        "operacionais e aos campos que não devem ser somados diretamente."
        if contagem["Crítico"] == 0
        else "Não avançar antes de corrigir os itens críticos identificados."
    )

    partes = [
        "# Relatório da Etapa 06 — Validação Final dos Dados Finais",
        "",
        f"Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## 1. Objetivo da Etapa 06",
        "",
        "Validar os arquivos finais já criados para uso no Power BI, sem alterar nenhum CSV e sem criar KPIs finais complexos.",
        "",
        "Python gera evidências. IA interpreta hipóteses. Humano valida decisões.",
        "",
        "## 2. Confirmação de segurança",
        "",
        "* dados brutos não foram lidos nem alterados;",
        "* dados tratados não foram lidos nem alterados;",
        "* dados finais foram apenas lidos em `dados/finais/`;",
        "* nenhum CSV final foi alterado;",
        "* nenhum KPI final complexo foi criado;",
        "* nenhum dashboard foi criado.",
        "",
        "## 3. Arquivos finais validados",
        "",
        formatar_tabela(existencia, ["arquivo", "caminho", "existe", "leitura", "linhas", "colunas", "erro", "status"]),
        "",
        "## 4. Estrutura dos arquivos finais",
        "",
        formatar_tabela(estrutura, ["arquivo", "linhas", "colunas", "nomes das colunas", "status"]),
        "",
        "## 5. Validação de chaves",
        "",
        "### Chaves únicas nas dimensões",
        "",
        formatar_tabela(chaves_dimensoes, ["escopo", "arquivo", "chave", "linhas", "nulos", "duplicidades", "valores únicos", "status", "observação"]),
        "",
        "### Duplicidades em chaves relevantes das tabelas fato",
        "",
        formatar_tabela(chaves_fatos, ["escopo", "arquivo", "chave", "linhas", "nulos", "duplicidades", "valores únicos", "status", "observação"]),
        "",
        "## 6. Validação de relacionamentos",
        "",
        formatar_tabela(relacionamentos, ["origem", "coluna origem", "destino", "coluna destino", "valores origem", "sem correspondência", "nulos origem", "status", "observação"]),
        "",
        "## 7. Validação da dimensão calendário",
        "",
        "### Estrutura e período",
        "",
        formatar_tabela(calendario_resumo, ["checagem", "resultado", "status"]),
        "",
        "### Compatibilidade com datas das tabelas fato",
        "",
        formatar_tabela(calendario_cobertura, ["arquivo", "coluna", "menor data", "maior data", "datas fora do calendário", "datas inválidas", "status"]),
        "",
        "## 8. Validação de campos sensíveis",
        "",
        formatar_tabela(sensiveis, ["arquivo", "campo", "regra", "resultado", "status"]),
        "",
        "## 9. Nulos e pontos de atenção",
        "",
        "Nulos operacionais foram preservados como evidência; esta etapa não aplica imputação, remoção de linhas ou correção automática.",
        "",
        formatar_tabela(nulos, ["arquivo", "coluna", "linhas", "nulos", "percentual", "status", "observação"]),
        "",
        "## 10. Campos com risco de agregação indevida no Power BI",
        "",
        formatar_tabela(agregacao, ["arquivo", "campo", "existe", "risco", "status"]),
        "",
        "## 11. Matriz geral de status",
        "",
        formatar_tabela(matriz, ["tema", "status"]),
        "",
        "## 12. Limitações da validação",
        "",
        "* A validação é estrutural e relacional; não substitui validação de regras de negócio pelo usuário.",
        "* A etapa não recalcula KPIs finais, métricas gerenciais ou medidas DAX.",
        "* A etapa não avalia layout, performance ou interações do Power BI.",
        "* A dimensão calendário foi validada por cobertura geral das datas disponíveis, sem calendário fiscal ou feriados.",
        "* Nulos operacionais foram apenas registrados, não corrigidos.",
        "",
        "## 13. Recomendação para avanço",
        "",
        recomendacao,
        "",
        montar_secao_validacao_humana(
            "## 14. Decisão da Etapa 06",
            "Status da Etapa 06:\n\n* [ ] Aprovada\n* [ ] Aprovada com ressalvas\n* [ ] Reprovada para avanço\n\nObservações da validação humana:\n\n* A preencher.",
        ),
        "",
        "## 15. Confirmações finais",
        "",
        "* Etapa 06 concluída como validação final dos dados finais;",
        f"* arquivos finais validados: {arquivos_validados} de {len(ARQUIVOS_FINAIS)};",
        f"* alertas OK: {contagem['OK']};",
        f"* alertas Atenção: {contagem['Atenção']};",
        f"* alertas Crítico: {contagem['Crítico']};",
        "* nenhum dado bruto, tratado ou final foi alterado;",
        "* nenhum dashboard foi criado;",
        "* nenhum KPI final complexo foi criado.",
        "",
    ]

    escrever_relatorio_preservando_validacao(
        RELATORIO_SAIDA,
        "\n".join(partes),
        "## 14. Decisão da Etapa 06",
    )
    return arquivos_validados, contagem


def main() -> None:
    """Ponto de entrada da Etapa 06."""
    arquivos_validados, contagem = gerar_relatorio()

    print("Etapa 06 concluída: validação final dos dados finais.")
    print(f"Arquivos finais validados: {arquivos_validados}")
    print(f"Alertas OK: {contagem['OK']}")
    print(f"Alertas Atenção: {contagem['Atenção']}")
    print(f"Alertas Crítico: {contagem['Crítico']}")
    print(f"Relatório gerado: {RELATORIO_SAIDA.relative_to(PASTA_RAIZ)}")


if __name__ == "__main__":
    main()
