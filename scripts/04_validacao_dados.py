"""
Protocolo ADA - Etapa 04: Validação dos Dados Tratados

Finalidade:
- Ler os arquivos tratados gerados na Etapa 03.
- Comparar arquivos tratados com seus brutos correspondentes.
- Auditar mascaramento, datas, nulos, tipos, relações, duplicidades e métricas.
- Gerar relatorio/04_relatorio_validacao_dados_tratados.md.

Regras principais:
- Este script não altera dados brutos.
- Este script não altera dados tratados.
- Este script não cria dados finais.
- Este script não aplica novas transformações, KPIs ou dashboards.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
import re
import unicodedata

import pandas as pd

from ada_relatorios import (
    escrever_relatorio_preservando_validacao,
    montar_secao_validacao_humana,
)


PASTA_DADOS_BRUTOS = Path("dados/brutos")
PASTA_DADOS_TRATADOS = Path("dados/tratados")
PASTA_RELATORIOS = Path("relatorios")
RELATORIO = PASTA_RELATORIOS / "04_relatorio_validacao_dados_tratados.md"

REFERENCIAS = [
    PASTA_RELATORIOS / "01_relatorio_inspecao_dados.md",
    PASTA_RELATORIOS / "02_plano_tratamento_dados.md",
    PASTA_RELATORIOS / "03_relatorio_tratamento_padronizacao.md",
]

ARQUIVOS = {
    "customers_tratado.csv": "customers.csv",
    "loads_tratado.csv": "loads.csv",
    "trips_tratado.csv": "trips.csv",
    "delivery_events_tratado.csv": "delivery_events.csv",
    "routes_tratado.csv": "routes.csv",
    "fuel_purchases_tratado.csv": "fuel_purchases.csv",
    "trucks_tratado.csv": "trucks.csv",
}

MASCARAS = {
    "customers_tratado.csv": ("customer_name", r"^Cliente_\d{3,}$"),
    "fuel_purchases_tratado.csv": ("fuel_card_number", r"^CARTAO_MASCARADO_\d{3,}$"),
    "trucks_tratado.csv": ("vin", r"^VIN_MASCARADO_\d{3,}$"),
}

DATAS = {
    "customers_tratado.csv": ["contract_start_date"],
    "loads_tratado.csv": ["load_date"],
    "trips_tratado.csv": ["dispatch_date"],
    "delivery_events_tratado.csv": ["scheduled_datetime", "actual_datetime"],
    "fuel_purchases_tratado.csv": ["purchase_date"],
    "trucks_tratado.csv": ["acquisition_date"],
}

NULOS_RELEVANTES = {
    "trips_tratado.csv": ["driver_id", "truck_id", "trailer_id"],
    "fuel_purchases_tratado.csv": ["driver_id", "truck_id"],
}

RELACIONAMENTOS = [
    ("loads_tratado.csv", "load_id", "trips_tratado.csv", "load_id"),
    ("trips_tratado.csv", "trip_id", "delivery_events_tratado.csv", "trip_id"),
    ("loads_tratado.csv", "customer_id", "customers_tratado.csv", "customer_id"),
    ("loads_tratado.csv", "route_id", "routes_tratado.csv", "route_id"),
    ("trips_tratado.csv", "truck_id", "trucks_tratado.csv", "truck_id"),
    ("fuel_purchases_tratado.csv", "trip_id", "trips_tratado.csv", "trip_id"),
    ("fuel_purchases_tratado.csv", "truck_id", "trucks_tratado.csv", "truck_id"),
]

CHAVES = {
    "customers_tratado.csv": "customer_id",
    "loads_tratado.csv": "load_id",
    "trips_tratado.csv": "trip_id",
    "delivery_events_tratado.csv": "event_id",
    "routes_tratado.csv": "route_id",
    "fuel_purchases_tratado.csv": "fuel_purchase_id",
    "trucks_tratado.csv": "truck_id",
}

CATEGORICOS = {
    "customers_tratado.csv": ["customer_type", "account_status", "primary_freight_type"],
    "loads_tratado.csv": ["load_type", "load_status", "booking_type"],
    "trips_tratado.csv": ["trip_status"],
    "delivery_events_tratado.csv": ["event_type", "location_state"],
    "routes_tratado.csv": ["origin_state", "destination_state"],
    "trucks_tratado.csv": ["make", "fuel_type", "status", "home_terminal"],
}

METRICAS = {
    "customers_tratado.csv": ["annual_revenue_potential"],
    "loads_tratado.csv": ["weight_lbs", "pieces", "revenue", "fuel_surcharge", "accessorial_charges"],
    "trips_tratado.csv": ["actual_distance_miles", "actual_duration_hours", "fuel_gallons_used", "average_mpg", "idle_time_hours"],
    "delivery_events_tratado.csv": ["detention_minutes"],
    "routes_tratado.csv": ["typical_distance_miles", "typical_transit_days", "base_rate_per_mile", "fuel_surcharge_rate"],
    "fuel_purchases_tratado.csv": ["gallons", "price_per_gallon", "total_cost"],
    "trucks_tratado.csv": ["acquisition_mileage", "tank_capacity_gallons"],
}

TAXAS = {
    "routes_tratado.csv": ["fuel_surcharge_rate", "base_rate_per_mile"],
    "fuel_purchases_tratado.csv": ["price_per_gallon"],
}


def padronizar_nome_coluna(nome: str) -> str:
    """Replica a padronização da Etapa 03 para comparar colunas."""
    sem_acentos = unicodedata.normalize("NFKD", nome)
    sem_acentos = "".join(caractere for caractere in sem_acentos if not unicodedata.combining(caractere))
    minusculo = sem_acentos.lower().strip()
    snake_case = re.sub(r"[^a-z0-9]+", "_", minusculo)
    return snake_case.strip("_")


def status_prioritario(statuses: list[str]) -> str:
    """Resume vários status em um status geral."""
    if "Crítico" in statuses:
        return "Crítico"
    if "Atenção" in statuses:
        return "Atenção"
    return "OK"


def formatar_tabela(linhas: list[dict[str, Any]], colunas: list[str]) -> str:
    """Cria tabela Markdown simples."""
    if not linhas:
        return "Sem registros para exibir."
    cabecalho = "| " + " | ".join(colunas) + " |"
    separador = "| " + " | ".join("---" for _ in colunas) + " |"
    corpo = []
    for linha in linhas:
        valores = []
        for coluna in colunas:
            valor = "" if pd.isna(linha.get(coluna, "")) else str(linha.get(coluna, ""))
            valores.append(valor.replace("\n", " ").replace("|", "\\|"))
        corpo.append("| " + " | ".join(valores) + " |")
    return "\n".join([cabecalho, separador, *corpo])


def ler_csv(caminho: Path) -> tuple[pd.DataFrame | None, str]:
    """Lê um CSV sem alterar o arquivo."""
    try:
        return pd.read_csv(caminho, low_memory=False), ""
    except Exception as erro:  # noqa: BLE001 - registrar no relatório
        return None, f"{type(erro).__name__}: {erro}"


def carregar_tabelas() -> tuple[dict[str, pd.DataFrame], dict[str, pd.DataFrame], list[dict[str, Any]]]:
    """Carrega brutos e tratados para validação."""
    brutos: dict[str, pd.DataFrame] = {}
    tratados: dict[str, pd.DataFrame] = {}
    existencia = []

    for tratado, bruto in ARQUIVOS.items():
        caminho_tratado = PASTA_DADOS_TRATADOS / tratado
        encontrado = caminho_tratado.exists()
        tabela_tratada, erro_tratado = (None, "arquivo ausente")
        if encontrado:
            tabela_tratada, erro_tratado = ler_csv(caminho_tratado)
        tabela_bruta, erro_bruto = ler_csv(PASTA_DADOS_BRUTOS / bruto)

        if tabela_tratada is not None:
            tratados[tratado] = tabela_tratada
        if tabela_bruta is not None:
            brutos[bruto] = tabela_bruta

        status = "OK" if encontrado and tabela_tratada is not None and not erro_bruto else "Crítico"
        existencia.append(
            {
                "arquivo esperado": str(caminho_tratado),
                "encontrado": "Sim" if encontrado else "Não",
                "sucesso de leitura": "Sim" if tabela_tratada is not None else "Não",
                "linhas": len(tabela_tratada) if tabela_tratada is not None else "",
                "colunas": len(tabela_tratada.columns) if tabela_tratada is not None else "",
                "erro": erro_tratado or erro_bruto,
                "status": status,
                "observação": "Arquivo tratado lido com sucesso." if status == "OK" else "Risco crítico: arquivo ausente ou ilegível.",
            }
        )

    return brutos, tratados, existencia


def validar_linhas_colunas(brutos: dict[str, pd.DataFrame], tratados: dict[str, pd.DataFrame]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Compara linhas e colunas entre bruto e tratado."""
    linhas = []
    colunas = []
    for tratado, bruto in ARQUIVOS.items():
        if tratado not in tratados or bruto not in brutos:
            continue
        tabela_bruta = brutos[bruto]
        tabela_tratada = tratados[tratado]
        colunas_brutas = [padronizar_nome_coluna(coluna) for coluna in tabela_bruta.columns]
        colunas_tratadas = list(tabela_tratada.columns)
        ausentes = sorted(set(colunas_brutas) - set(colunas_tratadas))
        novas = sorted(set(colunas_tratadas) - set(colunas_brutas))
        diff_linhas = len(tabela_tratada) - len(tabela_bruta)
        diff_colunas = len(colunas_tratadas) - len(colunas_brutas)
        linhas.append(
            {
                "arquivo": tratado,
                "linhas no bruto": len(tabela_bruta),
                "linhas no tratado": len(tabela_tratada),
                "diferença": diff_linhas,
                "status": "OK" if diff_linhas == 0 else "Crítico",
            }
        )
        colunas.append(
            {
                "arquivo": tratado,
                "colunas no bruto": len(colunas_brutas),
                "colunas no tratado": len(colunas_tratadas),
                "diferença": diff_colunas,
                "colunas ausentes": ", ".join(ausentes) or "nenhuma",
                "colunas novas": ", ".join(novas) or "nenhuma",
                "status": "OK" if diff_colunas == 0 and not ausentes and not novas else "Atenção",
            }
        )
    return linhas, colunas


def validar_mascaras(tratados: dict[str, pd.DataFrame]) -> list[dict[str, Any]]:
    """Valida padrões de mascaramento sem expor valores originais."""
    linhas = []
    for arquivo, (coluna, padrao) in MASCARAS.items():
        tabela = tratados.get(arquivo)
        if tabela is None or coluna not in tabela.columns:
            linhas.append({"tabela": arquivo, "coluna": coluna, "existe": "Não", "padrão": padrao, "distintos": "", "nulos": "", "status": "Crítico", "observação": "Coluna ou arquivo ausente."})
            continue
        serie = tabela[coluna].dropna().astype(str)
        segue_padrao = serie.str.match(padrao).all() if not serie.empty else True
        linhas.append(
            {
                "tabela": arquivo,
                "coluna": coluna,
                "existe": "Sim",
                "padrão": padrao,
                "distintos": tabela[coluna].nunique(dropna=True),
                "nulos": int(tabela[coluna].isna().sum()),
                "status": "OK" if segue_padrao else "Crítico",
                "observação": "Máscara validada sem expor valores originais." if segue_padrao else "Há valores fora do padrão de máscara.",
            }
        )
    return linhas


def validar_datas(tratados: dict[str, pd.DataFrame]) -> list[dict[str, Any]]:
    """Valida legibilidade de datas sem alterar formato."""
    linhas = []
    for arquivo, colunas in DATAS.items():
        tabela = tratados.get(arquivo)
        if tabela is None:
            continue
        for coluna in colunas:
            if coluna not in tabela.columns:
                continue
            datas = pd.to_datetime(tabela[coluna], errors="coerce")
            nulos = int(tabela[coluna].isna().sum())
            invalidos = int(tabela[coluna].notna().sum() - datas.notna().sum())
            linhas.append(
                {
                    "tabela": arquivo,
                    "coluna": coluna,
                    "nulos": nulos,
                    "menor data": datas.min() if datas.notna().any() else "",
                    "maior data": datas.max() if datas.notna().any() else "",
                    "valores inválidos aparentes": invalidos,
                    "status": "OK" if invalidos == 0 else "Atenção",
                }
            )
    return linhas


def validar_nulos(tratados: dict[str, pd.DataFrame]) -> list[dict[str, Any]]:
    """Registra nulos preservados em campos operacionais relevantes."""
    linhas = []
    for arquivo, colunas in NULOS_RELEVANTES.items():
        tabela = tratados.get(arquivo)
        if tabela is None:
            continue
        for coluna in colunas:
            if coluna not in tabela.columns:
                continue
            nulos = int(tabela[coluna].isna().sum())
            percentual = (nulos / len(tabela)) * 100 if len(tabela) else 0
            linhas.append(
                {
                    "tabela": arquivo,
                    "coluna": coluna,
                    "nulos": nulos,
                    "percentual de nulos": f"{percentual:.2f}%",
                    "status": "Atenção" if nulos > 0 else "OK",
                    "interpretação pendente": "Nulos preservados; validar significado antes da Etapa 05.",
                }
            )
    return linhas


def papel_esperado(coluna: str) -> str:
    """Resume papel técnico esperado."""
    if coluna.endswith("_id"):
        return "ID como texto"
    if coluna in {"contract_start_date", "load_date", "dispatch_date", "scheduled_datetime", "actual_datetime", "purchase_date", "acquisition_date"}:
        return "data legível"
    if coluna in {"on_time_flag"}:
        return "booleano/flag"
    if coluna in {"annual_revenue_potential", "revenue", "fuel_surcharge", "accessorial_charges", "base_rate_per_mile", "total_cost", "price_per_gallon"}:
        return "numérico financeiro"
    if coluna in {"weight_lbs", "pieces", "actual_distance_miles", "actual_duration_hours", "fuel_gallons_used", "average_mpg", "idle_time_hours", "detention_minutes", "typical_distance_miles", "typical_transit_days", "gallons", "acquisition_mileage", "tank_capacity_gallons"}:
        return "métrica operacional numérica"
    return "evidência técnica"


def validar_tipos(tratados: dict[str, pd.DataFrame]) -> list[dict[str, Any]]:
    """Registra tipos lidos pelo pandas como evidência técnica."""
    linhas = []
    for arquivo, tabela in tratados.items():
        for coluna in tabela.columns:
            esperado = papel_esperado(coluna)
            tipo = str(tabela[coluna].dtype)
            status = "OK"
            if esperado == "ID como texto" and not (pd.api.types.is_string_dtype(tabela[coluna]) or tipo == "object"):
                status = "Atenção"
            if "numérica" in esperado or "financeiro" in esperado:
                status = "OK" if pd.api.types.is_numeric_dtype(tabela[coluna]) else "Atenção"
            linhas.append({"tabela": arquivo, "coluna": coluna, "tipo técnico lido": tipo, "papel esperado": esperado, "status": status})
    return linhas


def cardinalidade_observada(origem: pd.Series, destino: pd.Series) -> str:
    """Calcula cardinalidade observada sem definir cardinalidade conceitual."""
    dup_origem = origem.dropna().duplicated().any()
    dup_destino = destino.dropna().duplicated().any()
    if not dup_origem and not dup_destino:
        return "1:1 observado"
    if dup_origem and not dup_destino:
        return "N:1 observado"
    if not dup_origem and dup_destino:
        return "1:N observado"
    return "N:N observado"


def validar_relacionamentos(tratados: dict[str, pd.DataFrame]) -> list[dict[str, Any]]:
    """Valida relacionamentos candidatos por interseção de chaves, sem joins permanentes."""
    linhas = []
    for origem, col_origem, destino, col_destino in RELACIONAMENTOS:
        if origem not in tratados or destino not in tratados:
            continue
        tabela_origem = tratados[origem]
        tabela_destino = tratados[destino]
        if col_origem not in tabela_origem.columns or col_destino not in tabela_destino.columns:
            continue
        valores_origem = set(tabela_origem[col_origem].dropna())
        valores_destino = set(tabela_destino[col_destino].dropna())
        sem_destino = valores_origem - valores_destino
        percentual = (len(sem_destino) / len(valores_origem)) * 100 if valores_origem else 0
        linhas.append(
            {
                "tabela origem": origem,
                "coluna origem": col_origem,
                "tabela destino": destino,
                "coluna destino": col_destino,
                "valores na origem": len(valores_origem),
                "sem correspondência": len(sem_destino),
                "percentual sem correspondência": f"{percentual:.2f}%",
                "cardinalidade observada": cardinalidade_observada(tabela_origem[col_origem], tabela_destino[col_destino]),
                "status": "OK" if len(sem_destino) == 0 else "Atenção",
                "observação": "Validação por conjuntos de chaves; não define cardinalidade conceitual.",
            }
        )
    return linhas


def validar_duplicidades(tratados: dict[str, pd.DataFrame]) -> list[dict[str, Any]]:
    """Valida duplicidades em chaves principais prováveis."""
    linhas = []
    for arquivo, chave in CHAVES.items():
        tabela = tratados.get(arquivo)
        if tabela is None or chave not in tabela.columns:
            continue
        total = len(tabela)
        unicos = int(tabela[chave].nunique(dropna=True))
        duplicados = total - unicos
        linhas.append({"tabela": arquivo, "chave": chave, "total de registros": total, "valores únicos": unicos, "duplicados": duplicados, "status": "OK" if duplicados == 0 else "Crítico"})
    return linhas


def validar_dominios(tratados: dict[str, pd.DataFrame]) -> list[dict[str, Any]]:
    """Registra domínios categóricos principais sem padronizar valores."""
    linhas = []
    for arquivo, colunas in CATEGORICOS.items():
        tabela = tratados.get(arquivo)
        if tabela is None:
            continue
        for coluna in colunas:
            if coluna not in tabela.columns:
                continue
            principais = tabela[coluna].value_counts(dropna=False).head(5)
            valores = ", ".join(str(indice) for indice in principais.index)
            linhas.append({"tabela": arquivo, "coluna": coluna, "valores distintos": tabela[coluna].nunique(dropna=True), "principais valores": valores, "status": "OK"})
    return linhas


def stats_numericas(tabela: pd.DataFrame, arquivo: str, campos: list[str]) -> list[dict[str, Any]]:
    """Calcula estatísticas básicas para métricas, sem remover outliers."""
    linhas = []
    for campo in campos:
        if campo not in tabela.columns:
            continue
        serie = pd.to_numeric(tabela[campo], errors="coerce")
        negativos = int((serie < 0).sum())
        zeros = int((serie == 0).sum())
        status = "Atenção" if negativos > 0 else "OK"
        observacao = "Possíveis pontos de atenção registrados; nenhum valor alterado." if status == "Atenção" else "Sem alerta simples de valores negativos."
        linhas.append(
            {
                "tabela": arquivo,
                "campo": campo,
                "mínimo": serie.min(),
                "máximo": serie.max(),
                "média": serie.mean(),
                "mediana": serie.median(),
                "valores negativos": negativos,
                "zeros": zeros,
                "status": status,
                "observação": observacao,
            }
        )
    return linhas


def validar_metricas(tratados: dict[str, pd.DataFrame]) -> list[dict[str, Any]]:
    """Valida métricas financeiras e operacionais."""
    linhas = []
    for arquivo, campos in METRICAS.items():
        tabela = tratados.get(arquivo)
        if tabela is not None:
            linhas.extend(stats_numericas(tabela, arquivo, campos))
    return linhas


def validar_taxas(tratados: dict[str, pd.DataFrame]) -> list[dict[str, Any]]:
    """Valida percentuais, taxas e preços unitários sem alterar escala."""
    linhas = []
    for arquivo, campos in TAXAS.items():
        tabela = tratados.get(arquivo)
        if tabela is None:
            continue
        for campo in campos:
            if campo not in tabela.columns:
                continue
            serie = pd.to_numeric(tabela[campo], errors="coerce")
            acima_1 = int((serie > 1).sum())
            if campo == "fuel_surcharge_rate":
                interpretacao = "percentual/taxa; escala precisa de validação humana"
            elif campo == "base_rate_per_mile":
                interpretacao = "taxa monetária por milha, não percentual"
            else:
                interpretacao = "preço por galão, não percentual"
            linhas.append(
                {
                    "tabela": arquivo,
                    "campo": campo,
                    "mínimo": serie.min(),
                    "máximo": serie.max(),
                    "média": serie.mean(),
                    "mediana": serie.median(),
                    "valores acima de 1": acima_1,
                    "interpretação provável": interpretacao,
                    "status": "Atenção" if campo == "fuel_surcharge_rate" and acima_1 > 0 else "OK",
                }
            )
    return linhas


def contar_status(linhas: list[dict[str, Any]]) -> dict[str, int]:
    """Conta status OK/Atenção/Crítico."""
    contagem = {"OK": 0, "Atenção": 0, "Crítico": 0}
    for linha in linhas:
        status = linha.get("status")
        if status in contagem:
            contagem[status] += 1
    return contagem


def gerar_relatorio() -> tuple[int, dict[str, int]]:
    """Executa validações e gera relatório."""
    PASTA_RELATORIOS.mkdir(parents=True, exist_ok=True)
    brutos, tratados, existencia = carregar_tabelas()
    linhas_comp, colunas_comp = validar_linhas_colunas(brutos, tratados)
    mascaras = validar_mascaras(tratados)
    datas = validar_datas(tratados)
    nulos = validar_nulos(tratados)
    tipos = validar_tipos(tratados)
    relacionamentos = validar_relacionamentos(tratados)
    duplicidades = validar_duplicidades(tratados)
    dominios = validar_dominios(tratados)
    metricas = validar_metricas(tratados)
    taxas = validar_taxas(tratados)

    temas = {
        "arquivos encontrados": existencia,
        "leitura dos arquivos": existencia,
        "preservação de linhas": linhas_comp,
        "preservação de colunas": colunas_comp,
        "mascaramento": mascaras,
        "datas": datas,
        "nulos": nulos,
        "tipos técnicos": tipos,
        "relacionamentos": relacionamentos,
        "duplicidades": duplicidades,
        "domínios categóricos": dominios,
        "métricas": metricas,
        "taxas/percentuais": taxas,
    }
    matriz = [{"tema": tema, "status": status_prioritario([linha.get("status", "OK") for linha in linhas])} for tema, linhas in temas.items()]

    contagem_total = {"OK": 0, "Atenção": 0, "Crítico": 0}
    for linhas in temas.values():
        parcial = contar_status(linhas)
        for chave, valor in parcial.items():
            contagem_total[chave] += valor

    referencias = [str(caminho) for caminho in REFERENCIAS if caminho.exists()]
    arquivos_lidos = [arquivo for arquivo in ARQUIVOS if arquivo in tratados]

    partes = [
        "# Relatório da Etapa 04 — Validação dos Dados Tratados",
        "",
        f"Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## 1. Objetivo da etapa",
        "",
        "Esta etapa valida os dados tratados antes da criação dos dados finais para Power BI, sem aplicar novas transformações.",
        "",
        "Python gera evidências. IA interpreta hipóteses. Humano valida decisões.",
        "",
        "## 2. Confirmação de segurança",
        "",
        "- Dados brutos não foram alterados.\n- Dados tratados não foram alterados.\n- Nenhum dado final foi criado.\n- Nenhum KPI final foi criado.\n- Nenhum dashboard foi gerado.\n- Nenhuma transformação foi aplicada.",
        "",
        "## 3. Fontes utilizadas",
        "",
        f"- Arquivos tratados lidos: {', '.join(f'`{arquivo}`' for arquivo in arquivos_lidos)}.\n- Relatórios de referência: {', '.join(f'`{ref}`' for ref in referencias)}.",
        "",
        "## 4. Existência e leitura dos arquivos tratados",
        "",
        formatar_tabela(existencia, ["arquivo esperado", "encontrado", "sucesso de leitura", "linhas", "colunas", "erro", "status", "observação"]),
        "",
        "## 5. Preservação de linhas e colunas",
        "",
        formatar_tabela(linhas_comp, ["arquivo", "linhas no bruto", "linhas no tratado", "diferença", "status"]),
        "",
        formatar_tabela(colunas_comp, ["arquivo", "colunas no bruto", "colunas no tratado", "diferença", "colunas ausentes", "colunas novas", "status"]),
        "",
        "## 6. Validação de mascaramento",
        "",
        formatar_tabela(mascaras, ["tabela", "coluna", "existe", "padrão", "distintos", "nulos", "status", "observação"]),
        "",
        "## 7. Validação de datas",
        "",
        formatar_tabela(datas, ["tabela", "coluna", "nulos", "menor data", "maior data", "valores inválidos aparentes", "status"]),
        "",
        "## 8. Validação de nulos preservados",
        "",
        formatar_tabela(nulos, ["tabela", "coluna", "nulos", "percentual de nulos", "status", "interpretação pendente"]),
        "",
        "## 9. Validação de tipos técnicos",
        "",
        "Os tipos lidos pelo pandas são evidência técnica, não verdade definitiva de banco de dados.",
        "",
        formatar_tabela(tipos, ["tabela", "coluna", "tipo técnico lido", "papel esperado", "status"]),
        "",
        "## 10. Validação de relacionamentos candidatos",
        "",
        formatar_tabela(relacionamentos, ["tabela origem", "coluna origem", "tabela destino", "coluna destino", "valores na origem", "sem correspondência", "percentual sem correspondência", "cardinalidade observada", "status", "observação"]),
        "",
        "## 11. Validação de duplicidades",
        "",
        formatar_tabela(duplicidades, ["tabela", "chave", "total de registros", "valores únicos", "duplicados", "status"]),
        "",
        "## 12. Validação de domínios categóricos",
        "",
        formatar_tabela(dominios, ["tabela", "coluna", "valores distintos", "principais valores", "status"]),
        "",
        "## 13. Validação de métricas e outliers simples",
        "",
        formatar_tabela(metricas, ["tabela", "campo", "mínimo", "máximo", "média", "mediana", "valores negativos", "zeros", "status", "observação"]),
        "",
        "## 14. Validação de percentuais, taxas e preços unitários",
        "",
        formatar_tabela(taxas, ["tabela", "campo", "mínimo", "máximo", "média", "mediana", "valores acima de 1", "interpretação provável", "status"]),
        "",
        "## 15. Matriz geral de status",
        "",
        formatar_tabela(matriz, ["tema", "status"]),
        "",
        "## 16. Pendências para a Etapa 05",
        "",
        "- Relacionamentos aceitos.\n- Granularidade das tabelas finais.\n- Quais fatos e dimensões serão criados.\n- Tratamento de nulos.\n- Uso ou não de registros sem correspondência.\n- Regras de agregação.\n- Escala de percentuais.\n- Campos mascarados que seguem para dados finais.\n- Criação de dimensão calendário.",
        "",
        montar_secao_validacao_humana(
            "## 17. Decisão da Etapa 04",
            "Status da Etapa 04:\n\n- [ ] Aprovada\n- [ ] Aprovada com ressalvas\n- [ ] Reprovada para avanço\n\nObservações da validação humana:\n\n- A preencher.",
        ),
        "",
        "## 18. Confirmações finais",
        "",
        "- Dados brutos preservados.\n- Dados tratados preservados.\n- Dados finais não criados.\n- KPIs finais não criados.\n- Dashboard não criado.",
        "",
    ]

    escrever_relatorio_preservando_validacao(
        RELATORIO,
        "\n".join(partes),
        "## 17. Decisão da Etapa 04",
    )
    return len(arquivos_lidos), contagem_total


def main() -> None:
    """Ponto de entrada da validação."""
    print("Etapa 04 - Validação dos Dados Tratados")
    print("Nenhum dado bruto ou tratado será alterado.")

    total_validados, contagem = gerar_relatorio()

    print("\nRelatório criado:")
    print(f"- {RELATORIO}")
    print("\nResumo da validação:")
    print(f"- Arquivos tratados validados: {total_validados}")
    print(f"- Alertas OK: {contagem['OK']}")
    print(f"- Alertas Atenção: {contagem['Atenção']}")
    print(f"- Alertas Crítico: {contagem['Crítico']}")
    print("- Confirmação: nenhum dado foi alterado.")


if __name__ == "__main__":
    main()
