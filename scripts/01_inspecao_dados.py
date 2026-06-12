"""
Protocolo ADA - Etapa 01: Inspeção Segura dos Dados Brutos

Finalidade:
- Ler arquivos CSV da pasta dados/brutos/.
- Gerar um relatório inicial de inspeção em relatorios/01_relatorio_inspecao_dados.md.
- Preservar integralmente os arquivos originais.

Regras principais:
- Este script não altera, move, limpa, sobrescreve ou transforma arquivos em dados/brutos/.
- O relatório contém hipóteses iniciais, não decisões finais.
- Amostras de dados são limitadas a no máximo 3 linhas por tabela.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd


PASTA_DADOS_BRUTOS = Path("dados/brutos")
PASTA_RELATORIOS = Path("relatorios")
CAMINHO_RELATORIO = PASTA_RELATORIOS / "01_relatorio_inspecao_dados.md"
CAMINHO_SCHEMA = PASTA_DADOS_BRUTOS / "DATABASE_SCHEMA.txt"


def normalizar_nome_coluna(nome_coluna: str) -> str:
    """Padroniza o nome da coluna apenas para facilitar buscas por palavras-chave."""
    return nome_coluna.strip().lower()


def separar_partes_nome(nome_coluna: str) -> list[str]:
    """Divide o nome da coluna em partes simples, usando sublinhado como separador."""
    return [parte for parte in normalizar_nome_coluna(nome_coluna).split("_") if parte]


def eh_possivel_id(nome_coluna: str) -> bool:
    """
    Identifica possíveis IDs por regra restrita.

    A regra evita falsos positivos como idle_time_hours e average_idle_hours,
    que contêm as letras "id", mas não representam identificadores.
    """
    nome = normalizar_nome_coluna(nome_coluna)
    return nome == "id" or nome.endswith("_id") or nome in {"codigo", "código", "code"}


def eh_possivel_data_hora(nome_coluna: str) -> bool:
    """
    Identifica possíveis datas/horas sem usar a palavra genérica "time".

    Isso evita classificar campos como on_time_flag, idle_time_hours,
    average_idle_hours e downtime_hours como datas.
    """
    nome = normalizar_nome_coluna(nome_coluna)
    partes = separar_partes_nome(nome_coluna)

    if "timestamp" in nome or "datetime" in nome:
        return True

    return any(parte in {"date", "data", "hora"} for parte in partes)


def eh_possivel_booleano_por_nome(nome_coluna: str) -> bool:
    """Identifica possíveis booleanos pelo nome da coluna."""
    nome = normalizar_nome_coluna(nome_coluna)
    partes = separar_partes_nome(nome_coluna)

    return (
        nome.endswith("_flag")
        or nome.startswith("is_")
        or nome.startswith("has_")
        or "flag" in partes
        or "ativo" in partes
        or "inativo" in partes
    )


def eh_possivel_financeiro(nome_coluna: str) -> bool:
    """
    Identifica possíveis campos financeiros por termos específicos.

    A regra não usa termos genéricos que poderiam classificar customer_id,
    customer_name ou customer_type como financeiros.
    """
    nome = normalizar_nome_coluna(nome_coluna)
    partes = separar_partes_nome(nome_coluna)

    termos_por_parte = {
        "cost",
        "price",
        "revenue",
        "charge",
        "charges",
        "amount",
        "valor",
        "custo",
        "preco",
        "preço",
        "receita",
        "surcharge",
    }

    return "rate_per" in nome or any(parte in termos_por_parte for parte in partes)


def eh_possivel_percentual_ou_taxa(nome_coluna: str) -> bool:
    """Identifica possíveis percentuais, razões ou taxas."""
    nome = normalizar_nome_coluna(nome_coluna)
    partes = separar_partes_nome(nome_coluna)

    return (
        "rate" in partes
        or "ratio" in partes
        or "percent" in partes
        or "percentage" in partes
        or nome.endswith("_rate")
        or nome.endswith("_ratio")
        or nome.endswith("_percent")
        or nome.endswith("_percentage")
    )


def eh_possivel_pessoal_ou_sensivel(nome_coluna: str) -> bool:
    """
    Identifica possíveis dados pessoais/sensíveis por nomes específicos.

    Campos operacionais como facility_name não são classificados como pessoais
    apenas por conterem a palavra "name".
    """
    nome = normalizar_nome_coluna(nome_coluna)
    termos_exatos = {
        "first_name",
        "last_name",
        "driver_name",
        "customer_name",
        "email",
        "phone",
        "cpf",
        "rg",
        "address",
        "birth",
        "date_of_birth",
        "license_number",
    }

    return nome in termos_exatos


def eh_possivel_metrica_tempo(nome_coluna: str) -> bool:
    """Identifica possíveis métricas de tempo, duração ou permanência."""
    nome = normalizar_nome_coluna(nome_coluna)
    partes = separar_partes_nome(nome_coluna)

    termos_tempo = {"duration", "hours", "minutes", "days"}
    exemplos_compostos = {
        "downtime_hours",
        "idle_time_hours",
        "average_idle_hours",
        "detention_minutes",
        "typical_transit_days",
    }

    return nome in exemplos_compostos or any(parte in termos_tempo for parte in partes)


def tentar_ler_csv(caminho_csv: Path) -> tuple[pd.DataFrame | None, str | None]:
    """
    Tenta ler um CSV sem alterar o arquivo original.

    Alguns arquivos podem ter codificações diferentes. Por isso, o script tenta
    algumas opções comuns e registra erro caso nenhuma funcione.
    """
    codificacoes = ["utf-8", "utf-8-sig", "latin1"]
    ultimo_erro = "Erro não identificado."

    for codificacao in codificacoes:
        try:
            tabela = pd.read_csv(caminho_csv, encoding=codificacao, low_memory=False)
            return tabela, None
        except Exception as erro:  # noqa: BLE001 - erro registrado no relatório
            ultimo_erro = f"{type(erro).__name__}: {erro}"

    return None, ultimo_erro


def detectar_colunas_booleanas(tabela: pd.DataFrame) -> list[str]:
    """Identifica campos que parecem booleanos pelo tipo, nome ou valores simples."""
    colunas_booleanas: list[str] = []
    valores_booleanos_texto = {"true", "false", "sim", "não", "nao", "yes", "no", "0", "1"}

    for coluna in tabela.columns:
        serie = tabela[coluna].dropna()

        if pd.api.types.is_bool_dtype(tabela[coluna]):
            colunas_booleanas.append(coluna)
            continue

        if eh_possivel_booleano_por_nome(coluna):
            colunas_booleanas.append(coluna)
            continue

        if serie.empty:
            continue

        valores_unicos = {str(valor).strip().lower() for valor in serie.unique()[:20]}
        if valores_unicos and valores_unicos.issubset(valores_booleanos_texto):
            colunas_booleanas.append(coluna)

    return colunas_booleanas


def detectar_colunas_categoricas(tabela: pd.DataFrame) -> list[str]:
    """Identifica possíveis campos categóricos sem aplicar transformação."""
    colunas_categoricas: list[str] = []
    nomes_categoricos = {"status", "type", "state", "city"}
    limite_unicos = max(20, int(len(tabela) * 0.05))

    for coluna in tabela.columns:
        serie = tabela[coluna]
        nome = normalizar_nome_coluna(coluna)
        partes = separar_partes_nome(coluna)

        nome_sugere_categoria = (
            nome in nomes_categoricos
            or nome.endswith("_type")
            or nome.endswith("_status")
            or any(parte in nomes_categoricos for parte in partes)
        )

        if pd.api.types.is_object_dtype(serie) or isinstance(serie.dtype, pd.CategoricalDtype):
            quantidade_unicos = serie.nunique(dropna=True)
            if quantidade_unicos <= limite_unicos or nome_sugere_categoria:
                colunas_categoricas.append(coluna)

    return colunas_categoricas


def formatar_lista(valores: list[str]) -> str:
    """Formata listas para Markdown, mantendo uma mensagem clara quando vazias."""
    if not valores:
        return "Nenhum campo identificado automaticamente."
    return "\n".join(f"- `{valor}`" for valor in valores)


def formatar_tabela_markdown(linhas: list[dict[str, Any]], colunas: list[str]) -> str:
    """Cria uma tabela Markdown simples sem depender de bibliotecas extras."""
    if not linhas:
        return "Sem linhas para exibir."

    cabecalho = "| " + " | ".join(colunas) + " |"
    separador = "| " + " | ".join("---" for _ in colunas) + " |"
    corpo = []

    for linha in linhas:
        valores = []
        for coluna in colunas:
            valor = linha.get(coluna, "")
            texto = "" if pd.isna(valor) else str(valor)
            texto = texto.replace("\n", " ").replace("|", "\\|")
            valores.append(texto)
        corpo.append("| " + " | ".join(valores) + " |")

    return "\n".join([cabecalho, separador, *corpo])


def gerar_tabela_nulos(tabela: pd.DataFrame) -> str:
    """Gera tabela com quantidade e percentual de valores nulos por coluna."""
    total_linhas = len(tabela)
    linhas = []

    for coluna in tabela.columns:
        quantidade_nulos = int(tabela[coluna].isna().sum())
        percentual_nulos = 0 if total_linhas == 0 else (quantidade_nulos / total_linhas) * 100
        linhas.append(
            {
                "Coluna": coluna,
                "Valores nulos": quantidade_nulos,
                "Percentual nulo": f"{percentual_nulos:.2f}%",
            }
        )

    return formatar_tabela_markdown(linhas, ["Coluna", "Valores nulos", "Percentual nulo"])


def gerar_tabela_tipos(tabela: pd.DataFrame) -> str:
    """Gera tabela com os tipos identificados pelo pandas."""
    linhas = [{"Coluna": coluna, "Tipo pandas": str(tipo)} for coluna, tipo in tabela.dtypes.items()]
    return formatar_tabela_markdown(linhas, ["Coluna", "Tipo pandas"])


def gerar_amostra_controlada(tabela: pd.DataFrame) -> str:
    """Gera uma amostra limitada a 3 linhas para reduzir exposição de dados."""
    amostra = tabela.head(3)
    linhas = amostra.fillna("").to_dict(orient="records")
    return formatar_tabela_markdown(linhas, list(tabela.columns))


def inspecionar_tabela(caminho_csv: Path, tabela: pd.DataFrame) -> dict[str, Any]:
    """Coleta informações iniciais sobre uma tabela CSV sem transformar dados."""
    colunas = list(tabela.columns)
    colunas_booleanas = detectar_colunas_booleanas(tabela)

    campos_numericos = [
        coluna
        for coluna in colunas
        if pd.api.types.is_numeric_dtype(tabela[coluna]) and coluna not in colunas_booleanas
    ]

    return {
        "nome_arquivo": caminho_csv.name,
        "quantidade_linhas": len(tabela),
        "quantidade_colunas": len(colunas),
        "colunas": colunas,
        "tabela_tipos": gerar_tabela_tipos(tabela),
        "tabela_nulos": gerar_tabela_nulos(tabela),
        "linhas_duplicadas": int(tabela.duplicated().sum()),
        "possiveis_ids": [coluna for coluna in colunas if eh_possivel_id(coluna)],
        "possiveis_datas": [coluna for coluna in colunas if eh_possivel_data_hora(coluna)],
        "possiveis_numericos": campos_numericos,
        "possiveis_categoricos": detectar_colunas_categoricas(tabela),
        "possiveis_booleanos": colunas_booleanas,
        "possiveis_financeiros": [coluna for coluna in colunas if eh_possivel_financeiro(coluna)],
        "possiveis_percentuais_taxas": [coluna for coluna in colunas if eh_possivel_percentual_ou_taxa(coluna)],
        "possiveis_sensiveis": [coluna for coluna in colunas if eh_possivel_pessoal_ou_sensivel(coluna)],
        "possiveis_metricas_tempo": [coluna for coluna in colunas if eh_possivel_metrica_tempo(coluna)],
        "amostra": gerar_amostra_controlada(tabela),
        "nulos_por_coluna": tabela.isna().sum().to_dict(),
    }


def resumir_schema() -> str:
    """
    Registra a existência do DATABASE_SCHEMA.txt.

    O conteúdo é lido apenas para confirmar que há uma documentação estrutural.
    O script não usa esse arquivo como fonte única para decidir tipos ou regras.
    """
    if not CAMINHO_SCHEMA.exists():
        return "- `DATABASE_SCHEMA.txt` não foi encontrado em `dados/brutos/`."

    try:
        conteudo = CAMINHO_SCHEMA.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        conteudo = CAMINHO_SCHEMA.read_text(encoding="latin1")
    except Exception as erro:  # noqa: BLE001 - erro registrado no relatório
        return f"- `DATABASE_SCHEMA.txt` foi encontrado, mas não pôde ser lido. Erro: `{type(erro).__name__}: {erro}`."

    total_linhas = len(conteudo.splitlines())
    total_caracteres = len(conteudo)
    return (
        "- `DATABASE_SCHEMA.txt` foi encontrado e lido apenas para confirmar a "
        f"existência de documentação estrutural da base. Linhas: {total_linhas}. "
        f"Caracteres: {total_caracteres}. O script não depende exclusivamente dele "
        "para decidir tipos ou regras."
    )


def gerar_observacoes_privacidade(possiveis_sensiveis: list[str], colunas: list[str]) -> str:
    """Gera observações iniciais de privacidade sem concluir risco final."""
    observacoes = []

    if not possiveis_sensiveis:
        observacoes.append("Nenhum campo sensível ou pessoal foi identificado automaticamente pelo nome da coluna.")
    else:
        observacoes.append(
            "Foram identificadas colunas com nomes que podem indicar dados pessoais ou sensíveis. "
            "Essa é uma hipótese inicial e exige validação humana antes de uso, exposição ou compartilhamento."
        )

    if "facility_name" in [normalizar_nome_coluna(coluna) for coluna in colunas]:
        observacoes.append(
            "`facility_name` foi registrado como dado operacional de instalação, não como dado pessoal."
        )

    return " ".join(observacoes)


def gerar_secao_arquivo(resultado: dict[str, Any]) -> str:
    """Monta a seção Markdown de um arquivo CSV inspecionado."""
    return f"""
### Arquivo: `{resultado["nome_arquivo"]}`

**Quantidade de linhas:** {resultado["quantidade_linhas"]}

**Quantidade de colunas:** {resultado["quantidade_colunas"]}

**Lista de colunas:**

{formatar_lista(resultado["colunas"])}

**Tipos de dados identificados pelo pandas:**

{resultado["tabela_tipos"]}

**Valores nulos por coluna:**

{resultado["tabela_nulos"]}

**Quantidade de linhas duplicadas:** {resultado["linhas_duplicadas"]}

**Possíveis colunas de identificação:**

{formatar_lista(resultado["possiveis_ids"])}

**Possíveis colunas de data/hora:**

{formatar_lista(resultado["possiveis_datas"])}

**Possíveis campos numéricos:**

{formatar_lista(resultado["possiveis_numericos"])}

**Possíveis campos categóricos:**

{formatar_lista(resultado["possiveis_categoricos"])}

**Possíveis campos booleanos:**

{formatar_lista(resultado["possiveis_booleanos"])}

**Possíveis campos financeiros:**

{formatar_lista(resultado["possiveis_financeiros"])}

**Possíveis campos percentuais ou taxas:**

{formatar_lista(resultado["possiveis_percentuais_taxas"])}

**Possíveis métricas de tempo/duração:**

{formatar_lista(resultado["possiveis_metricas_tempo"])}

**Possíveis campos sensíveis ou pessoais:**

{formatar_lista(resultado["possiveis_sensiveis"])}

**Observações iniciais sobre riscos de privacidade:**

{gerar_observacoes_privacidade(resultado["possiveis_sensiveis"], resultado["colunas"])}

**Amostra controlada de até 3 linhas:**

{resultado["amostra"]}
""".strip()


def gerar_recomendacoes_iniciais(resultados: list[dict[str, Any]]) -> str:
    """Gera recomendações preliminares como hipóteses, sem aplicar tratamento."""
    linhas = [
        "## Recomendações iniciais do Agente ADA",
        "",
        "As recomendações abaixo são hipóteses automáticas preliminares. Elas não são decisões finais e exigem validação humana antes de qualquer tratamento.",
        "",
    ]

    if not resultados:
        linhas.append("- Nenhum arquivo CSV foi inspecionado com sucesso.")
        return "\n".join(linhas)

    for resultado in resultados:
        arquivo = resultado["nome_arquivo"]
        colunas_com_nulos = [
            coluna
            for coluna, quantidade in resultado["nulos_por_coluna"].items()
            if quantidade > 0
        ]

        linhas.append(f"### `{arquivo}`")
        linhas.append("")
        linhas.append(f"- Colunas que provavelmente precisam ser avaliadas para conversão de data/hora: {', '.join(resultado['possiveis_datas']) or 'nenhuma identificada automaticamente'}.")
        linhas.append(f"- Colunas que provavelmente devem ser tratadas como texto/ID: {', '.join(resultado['possiveis_ids']) or 'nenhuma identificada automaticamente'}.")
        linhas.append(f"- Colunas que provavelmente são métricas numéricas: {', '.join(resultado['possiveis_numericos']) or 'nenhuma identificada automaticamente'}.")
        linhas.append(f"- Colunas que provavelmente são valores financeiros: {', '.join(resultado['possiveis_financeiros']) or 'nenhuma identificada automaticamente'}.")
        linhas.append(f"- Colunas que provavelmente são percentuais ou taxas e exigem validação da escala antes do uso no Power BI: {', '.join(resultado['possiveis_percentuais_taxas']) or 'nenhuma identificada automaticamente'}.")
        linhas.append(f"- Colunas que provavelmente são métricas de tempo/duração: {', '.join(resultado['possiveis_metricas_tempo']) or 'nenhuma identificada automaticamente'}.")
        linhas.append(f"- Colunas que exigem atenção por valores ausentes: {', '.join(colunas_com_nulos) or 'nenhuma identificada automaticamente'}.")
        linhas.append(f"- Colunas com possível risco de privacidade: {', '.join(resultado['possiveis_sensiveis']) or 'nenhuma identificada automaticamente'}.")
        linhas.append("- Pontos que exigem validação humana antes de qualquer tratamento: tipos de dados, regras de negócio, tratamento de nulos, duplicidades, campos sensíveis, escala de taxas/percentuais e critérios de uso em relatórios.")
        linhas.append("")

    return "\n".join(linhas).strip()


def gerar_confirmacoes_seguranca() -> str:
    """Declara as confirmações de segurança da etapa."""
    return """
## Confirmações de segurança

- Dados brutos não foram alterados.
- Nenhuma transformação foi aplicada.
- Nenhum KPI foi criado.
- Nenhuma conclusão analítica foi tomada.
- Relatório gerado apenas para inspeção inicial.
""".strip()


def gerar_relatorio() -> tuple[int, int]:
    """Inspeciona arquivos CSV e salva o relatório Markdown."""
    PASTA_RELATORIOS.mkdir(parents=True, exist_ok=True)

    arquivos_csv = sorted(PASTA_DADOS_BRUTOS.glob("*.csv"))
    resultados: list[dict[str, Any]] = []
    erros: list[str] = []

    partes_relatorio = [
        "# Relatório de Inspeção Segura dos Dados Brutos",
        "",
        f"Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "Este relatório foi gerado por leitura dos arquivos em `dados/brutos/`, sem alteração dos arquivos originais.",
        "",
        "Todas as classificações automáticas são hipóteses iniciais e precisam de validação humana antes de qualquer tratamento.",
        "",
        "## Documentação de estrutura da base",
        "",
        resumir_schema(),
        "",
        "## Arquivos CSV inspecionados",
        "",
    ]

    if not arquivos_csv:
        partes_relatorio.append("Nenhum arquivo `.csv` foi encontrado em `dados/brutos/`.")

    for caminho_csv in arquivos_csv:
        tabela, erro = tentar_ler_csv(caminho_csv)

        if erro is not None or tabela is None:
            erros.append(f"- `{caminho_csv.name}`: `{erro}`")
            continue

        resultado = inspecionar_tabela(caminho_csv, tabela)
        resultados.append(resultado)
        partes_relatorio.append(gerar_secao_arquivo(resultado))
        partes_relatorio.append("")

    partes_relatorio.extend(
        [
            "## Erros de leitura",
            "",
            "\n".join(erros) if erros else "Nenhum erro de leitura foi registrado.",
            "",
            gerar_recomendacoes_iniciais(resultados),
            "",
            gerar_confirmacoes_seguranca(),
            "",
        ]
    )

    CAMINHO_RELATORIO.write_text("\n".join(partes_relatorio), encoding="utf-8")
    return len(resultados), len(erros)


def main() -> None:
    """Ponto de entrada da inspeção segura."""
    print("Etapa 01 - Inspeção Segura dos Dados Brutos")
    print("Nenhuma alteração será feita em dados/brutos/.")

    total_inspecionados, total_erros = gerar_relatorio()

    print("\nArquivos criados ou alterados:")
    print(f"- {CAMINHO_RELATORIO}")
    print("- scripts/01_inspecao_dados.py")

    print("\nComando para executar o script:")
    print("python scripts/01_inspecao_dados.py")

    print("\nCaminho do relatório gerado:")
    print(CAMINHO_RELATORIO)

    print("\nResumo da execução:")
    print(f"- Arquivos CSV inspecionados com sucesso: {total_inspecionados}")
    print(f"- Arquivos CSV com erro de leitura: {total_erros}")
    print("- Confirmação: nenhum dado bruto foi alterado.")


if __name__ == "__main__":
    main()
