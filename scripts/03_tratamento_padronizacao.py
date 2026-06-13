"""
Protocolo ADA - Etapa 03: Tratamento e Padronização dos Dados

Finalidade:
- Aplicar apenas os tratamentos aprovados na Etapa 02.
- Criar arquivos tratados somente em dados/tratados/.
- Gerar relatório técnico em relatorios/03_relatorio_tratamento_padronizacao.md.

Regras principais:
- Os dados brutos nunca são alterados.
- Nenhum arquivo é criado em dados/finais/.
- Nenhuma linha é removida.
- Nenhum valor ausente é preenchido automaticamente.
- Nenhum KPI final ou dashboard é criado.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
import re
import unicodedata

import pandas as pd


PASTA_DADOS_BRUTOS = Path("dados/brutos")
PASTA_DADOS_TRATADOS = Path("dados/tratados")
PASTA_RELATORIOS = Path("relatorios")
RELATORIO_ETAPA_03 = PASTA_RELATORIOS / "03_relatorio_tratamento_padronizacao.md"

RELATORIOS_REFERENCIA = [
    PASTA_RELATORIOS / "01_relatorio_inspecao_dados.md",
    PASTA_RELATORIOS / "02_plano_tratamento_dados.md",
]

ARQUIVOS_ESCOPO = {
    "customers.csv": "customers_tratado.csv",
    "loads.csv": "loads_tratado.csv",
    "trips.csv": "trips_tratado.csv",
    "delivery_events.csv": "delivery_events_tratado.csv",
    "routes.csv": "routes_tratado.csv",
    "fuel_purchases.csv": "fuel_purchases_tratado.csv",
    "trucks.csv": "trucks_tratado.csv",
}

ARQUIVOS_FORA_ESCOPO = {
    "drivers.csv": "contém dados pessoais/identificáveis e ficou fora do núcleo V1.",
    "driver_monthly_metrics.csv": "tabela agregada mensal por motorista; fase futura.",
    "truck_utilization_metrics.csv": "tabela agregada mensal por caminhão; fase futura.",
    "maintenance_records.csv": "manutenção ficou como escopo complementar.",
    "safety_incidents.csv": "incidentes envolvem risco operacional e baixa ocorrência.",
    "trailers.csv": "dimensão complementar de equipamento.",
    "facilities.csv": "dimensão complementar de instalações.",
}

IDS = {
    "customer_id",
    "load_id",
    "trip_id",
    "route_id",
    "truck_id",
    "trailer_id",
    "driver_id",
    "event_id",
    "facility_id",
    "fuel_purchase_id",
}

DATAS_POR_TABELA = {
    "customers.csv": ["contract_start_date"],
    "loads.csv": ["load_date"],
    "trips.csv": ["dispatch_date"],
    "delivery_events.csv": ["scheduled_datetime", "actual_datetime"],
    "fuel_purchases.csv": ["purchase_date"],
    "trucks.csv": ["acquisition_date"],
}

CAMPOS_FINANCEIROS = {
    "annual_revenue_potential",
    "revenue",
    "fuel_surcharge",
    "accessorial_charges",
    "base_rate_per_mile",
    "total_cost",
    "price_per_gallon",
}

CAMPOS_TAXAS_PREC_UNITARIOS = {
    "fuel_surcharge_rate",
    "base_rate_per_mile",
    "price_per_gallon",
}

METRICAS_OPERACIONAIS = {
    "weight_lbs",
    "pieces",
    "actual_distance_miles",
    "actual_duration_hours",
    "fuel_gallons_used",
    "average_mpg",
    "idle_time_hours",
    "detention_minutes",
    "typical_distance_miles",
    "typical_transit_days",
    "gallons",
    "acquisition_mileage",
    "tank_capacity_gallons",
}

CATEGORICOS = {
    "customer_type",
    "primary_freight_type",
    "account_status",
    "load_type",
    "load_status",
    "booking_type",
    "trip_status",
    "event_type",
    "location_city",
    "location_state",
    "origin_city",
    "origin_state",
    "destination_city",
    "destination_state",
    "make",
    "fuel_type",
    "status",
    "home_terminal",
}

BOOLEANOS = {"on_time_flag"}

MASCARAMENTOS = {
    "customers.csv": {"customer_name": "Cliente"},
    "trucks.csv": {"vin": "VIN_MASCARADO"},
    "fuel_purchases.csv": {"fuel_card_number": "CARTAO_MASCARADO"},
}

NULOS_RELEVANTES = {
    "trips.csv": ["driver_id", "truck_id", "trailer_id"],
    "fuel_purchases.csv": ["driver_id", "truck_id"],
}


def padronizar_nome_coluna(nome: str) -> str:
    """Converte nome de coluna para minúsculas, snake_case e sem acentos."""
    sem_acentos = unicodedata.normalize("NFKD", nome)
    sem_acentos = "".join(caractere for caractere in sem_acentos if not unicodedata.combining(caractere))
    minusculo = sem_acentos.lower().strip()
    snake_case = re.sub(r"[^a-z0-9]+", "_", minusculo)
    return snake_case.strip("_")


def formatar_tabela(linhas: list[dict[str, Any]], colunas: list[str]) -> str:
    """Cria uma tabela Markdown simples."""
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


def mascarar_serie(serie: pd.Series, prefixo: str) -> tuple[pd.Series, int]:
    """Mascara valores mantendo consistência: mesmo valor original recebe mesmo código."""
    valores_unicos = [valor for valor in serie.dropna().drop_duplicates()]
    largura = max(3, len(str(len(valores_unicos))))
    mapa = {
        valor: f"{prefixo}_{indice:0{largura}d}"
        for indice, valor in enumerate(valores_unicos, start=1)
    }
    return serie.map(mapa).astype("string"), len(mapa)


def converter_data_segura(serie: pd.Series) -> tuple[pd.Series, int, int, int]:
    """Converte datas com errors='coerce' e retorna contagens de controle."""
    validos_antes = int(serie.notna().sum())
    convertida = pd.to_datetime(serie, errors="coerce")
    convertidos = int(convertida.notna().sum())
    nao_convertidos = max(validos_antes - convertidos, 0)
    return convertida, validos_antes, convertidos, nao_convertidos


def contar_nulos(tabela: pd.DataFrame, colunas: list[str]) -> dict[str, int]:
    """Conta nulos apenas para colunas existentes."""
    return {coluna: int(tabela[coluna].isna().sum()) for coluna in colunas if coluna in tabela.columns}


def tratar_tabela(nome_arquivo: str) -> tuple[pd.DataFrame, dict[str, Any]]:
    """Lê uma tabela bruta, aplica tratamentos aprovados e retorna metadados."""
    caminho_bruto = PASTA_DADOS_BRUTOS / nome_arquivo
    tabela_bruta = pd.read_csv(caminho_bruto, low_memory=False)
    tabela = tabela_bruta.copy()

    colunas_originais = list(tabela.columns)
    novos_nomes = {coluna: padronizar_nome_coluna(coluna) for coluna in tabela.columns}
    tabela = tabela.rename(columns=novos_nomes)
    colunas_padronizadas = [
        f"{original} -> {novo}"
        for original, novo in novos_nomes.items()
        if original != novo
    ]

    linhas_antes = len(tabela_bruta)
    colunas_antes = len(tabela_bruta.columns)
    duplicadas_antes = int(tabela_bruta.duplicated().sum())

    nulos_relevantes_antes = contar_nulos(tabela, NULOS_RELEVANTES.get(nome_arquivo, []))

    ids_convertidos = []
    for coluna in IDS.intersection(tabela.columns):
        tabela[coluna] = tabela[coluna].astype("string")
        ids_convertidos.append(coluna)

    conversoes_data = []
    for coluna in DATAS_POR_TABELA.get(nome_arquivo, []):
        if coluna not in tabela.columns:
            continue
        convertida, validos_antes, convertidos, nao_convertidos = converter_data_segura(tabela[coluna])
        tabela[coluna] = convertida
        conversoes_data.append(
            {
                "tabela": nome_arquivo,
                "coluna": coluna,
                "valores válidos antes": validos_antes,
                "valores convertidos": convertidos,
                "valores não convertidos": nao_convertidos,
                "observação": "Conversão segura com errors='coerce'; fuso horário não foi alterado.",
            }
        )

    categoricos_tratados = []
    for coluna in CATEGORICOS.intersection(tabela.columns):
        tabela[coluna] = tabela[coluna].astype("string").str.strip()
        categoricos_tratados.append(coluna)

    booleanos_preservados = []
    for coluna in BOOLEANOS.intersection(tabela.columns):
        if pd.api.types.is_bool_dtype(tabela[coluna]):
            booleanos_preservados.append(coluna)
        else:
            tabela[coluna] = tabela[coluna].map(
                {"True": True, "False": False, "true": True, "false": False, True: True, False: False}
            )
            booleanos_preservados.append(coluna)

    mascaramentos = []
    for coluna, prefixo in MASCARAMENTOS.get(nome_arquivo, {}).items():
        if coluna not in tabela.columns:
            continue
        tabela[coluna], quantidade = mascarar_serie(tabela[coluna], prefixo)
        mascaramentos.append(
            {
                "tabela": nome_arquivo,
                "coluna": coluna,
                "tipo de risco": "dado sensível/confidencial",
                "ação aplicada": f"mascaramento consistente de {quantidade} valores distintos",
                "justificativa": "preservar estrutura analítica sem expor valor original.",
            }
        )

    nulos_relevantes_depois = contar_nulos(tabela, NULOS_RELEVANTES.get(nome_arquivo, []))
    duplicadas_depois = int(tabela.duplicated().sum())

    destino = PASTA_DADOS_TRATADOS / ARQUIVOS_ESCOPO[nome_arquivo]
    tabela.to_csv(destino, index=False, encoding="utf-8")

    metadata = {
        "arquivo_bruto": nome_arquivo,
        "arquivo_tratado": destino.name,
        "linhas_antes": linhas_antes,
        "linhas_depois": len(tabela),
        "colunas_antes": colunas_antes,
        "colunas_depois": len(tabela.columns),
        "colunas_padronizadas": colunas_padronizadas,
        "ids_convertidos": ids_convertidos,
        "conversoes_data": conversoes_data,
        "categoricos_tratados": categoricos_tratados,
        "booleanos_preservados": booleanos_preservados,
        "mascaramentos": mascaramentos,
        "colunas_removidas": [],
        "financeiros_preservados": sorted(CAMPOS_FINANCEIROS.intersection(tabela.columns)),
        "taxas_preservadas": sorted(CAMPOS_TAXAS_PREC_UNITARIOS.intersection(tabela.columns)),
        "metricas_preservadas": sorted(METRICAS_OPERACIONAIS.intersection(tabela.columns)),
        "nulos_antes": nulos_relevantes_antes,
        "nulos_depois": nulos_relevantes_depois,
        "duplicadas_antes": duplicadas_antes,
        "duplicadas_depois": duplicadas_depois,
        "colunas_originais": colunas_originais,
    }
    return tabela, metadata


def gerar_relatorio(metadados: list[dict[str, Any]], arquivos_gerados: list[str]) -> None:
    """Gera relatório técnico da Etapa 03."""
    tratamentos_linhas = []
    conversoes_data = []
    mascaramentos = []
    nulos_linhas = []
    metricas_linhas = []
    qc_linhas = []

    for item in metadados:
        tratamentos_linhas.append(
            {
                "arquivo bruto": item["arquivo_bruto"],
                "arquivo tratado": item["arquivo_tratado"],
                "linhas antes/depois": f"{item['linhas_antes']} / {item['linhas_depois']}",
                "colunas antes/depois": f"{item['colunas_antes']} / {item['colunas_depois']}",
                "colunas convertidas": ", ".join(conv["coluna"] for conv in item["conversoes_data"]) or "nenhuma",
                "colunas mascaradas": ", ".join(mask["coluna"] for mask in item["mascaramentos"]) or "nenhuma",
                "colunas removidas": ", ".join(item["colunas_removidas"]) or "nenhuma",
                "observações": "Linhas preservadas; granularidade não alterada; sem joins.",
            }
        )
        conversoes_data.extend(item["conversoes_data"])
        mascaramentos.extend(item["mascaramentos"])

        for coluna, nulos_antes in item["nulos_antes"].items():
            nulos_depois = item["nulos_depois"].get(coluna, 0)
            nulos_linhas.append(
                {
                    "tabela": item["arquivo_bruto"],
                    "coluna": coluna,
                    "nulos antes": nulos_antes,
                    "nulos depois": nulos_depois,
                    "tratamento aplicado": "nulos preservados",
                    "justificativa": "não preencher, remover ou criar categoria sem validação humana.",
                }
            )

        for grupo, campos in [
            ("financeiro preservado", item["financeiros_preservados"]),
            ("taxa/preço unitário preservado", item["taxas_preservadas"]),
            ("métrica operacional preservada", item["metricas_preservadas"]),
        ]:
            for campo in campos:
                metricas_linhas.append(
                    {
                        "tabela": item["arquivo_bruto"],
                        "campo": campo,
                        "tipo": grupo,
                        "ação": "valor preservado, sem agregação, arredondamento ou alteração de escala",
                    }
                )

        qc_linhas.append(
            {
                "tabela": item["arquivo_bruto"],
                "linhas bruto": item["linhas_antes"],
                "linhas tratado": item["linhas_depois"],
                "diferença de linhas": item["linhas_depois"] - item["linhas_antes"],
                "colunas bruto": item["colunas_antes"],
                "colunas tratado": item["colunas_depois"],
                "diferença de colunas": item["colunas_depois"] - item["colunas_antes"],
                "status": "OK - linhas preservadas" if item["linhas_depois"] == item["linhas_antes"] else "Atenção",
            }
        )

    fora_escopo_linhas = [
        {"tabela fora do escopo": tabela, "motivo": motivo}
        for tabela, motivo in ARQUIVOS_FORA_ESCOPO.items()
    ]

    referencias = [
        str(caminho)
        for caminho in RELATORIOS_REFERENCIA
        if caminho.exists()
    ]

    partes = [
        "# Relatório da Etapa 03 — Tratamento e Padronização dos Dados",
        "",
        f"Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## 1. Objetivo da etapa",
        "",
        "Esta etapa aplica os tratamentos aprovados na Etapa 02 para gerar dados tratados, preservando integralmente os dados brutos.",
        "",
        "Python gera evidências. IA interpreta hipóteses. Humano valida decisões.",
        "",
        "## 2. Confirmação de segurança",
        "",
        "- Dados brutos não foram alterados.\n- Dados tratados foram criados em `dados/tratados/`.\n- Nenhum dado final foi criado.\n- Nenhum KPI final foi criado.\n- Nenhum dashboard foi gerado.\n- Nenhuma linha foi removida.\n- Nenhuma imputação automática foi feita.",
        "",
        "## 3. Fontes utilizadas",
        "",
        f"- Arquivos brutos lidos: {', '.join(f'`{arquivo}`' for arquivo in ARQUIVOS_ESCOPO)}.\n- Relatórios de referência: {', '.join(f'`{ref}`' for ref in referencias)}.\n- Arquivos tratados gerados: {', '.join(f'`dados/tratados/{arquivo}`' for arquivo in arquivos_gerados)}.",
        "",
        "## 4. Escopo aplicado na Etapa 03",
        "",
        f"Tabelas tratadas no núcleo V1: {', '.join(f'`{arquivo}`' for arquivo in ARQUIVOS_ESCOPO)}.",
        "",
        "Tabelas fora do escopo desta etapa:",
        "",
        formatar_tabela(fora_escopo_linhas, ["tabela fora do escopo", "motivo"]),
        "",
        "## 5. Tratamentos aplicados por tabela",
        "",
        formatar_tabela(
            tratamentos_linhas,
            [
                "arquivo bruto",
                "arquivo tratado",
                "linhas antes/depois",
                "colunas antes/depois",
                "colunas convertidas",
                "colunas mascaradas",
                "colunas removidas",
                "observações",
            ],
        ),
        "",
        "## 6. Conversão de datas",
        "",
        formatar_tabela(
            conversoes_data,
            [
                "tabela",
                "coluna",
                "valores válidos antes",
                "valores convertidos",
                "valores não convertidos",
                "observação",
            ],
        ),
        "",
        "## 7. Campos sensíveis e mascaramento",
        "",
        formatar_tabela(
            mascaramentos,
            ["tabela", "coluna", "tipo de risco", "ação aplicada", "justificativa"],
        ),
        "",
        "## 8. Valores ausentes preservados",
        "",
        formatar_tabela(
            nulos_linhas,
            ["tabela", "coluna", "nulos antes", "nulos depois", "tratamento aplicado", "justificativa"],
        ),
        "",
        "## 9. Métricas e campos preservados",
        "",
        formatar_tabela(metricas_linhas, ["tabela", "campo", "tipo", "ação"]),
        "",
        "## 10. Controle de qualidade pós-tratamento",
        "",
        formatar_tabela(
            qc_linhas,
            [
                "tabela",
                "linhas bruto",
                "linhas tratado",
                "diferença de linhas",
                "colunas bruto",
                "colunas tratado",
                "diferença de colunas",
                "status",
            ],
        ),
        "",
        "## 11. Pendências para a Etapa 04",
        "",
        "- Validar se datas foram convertidas corretamente.\n- Validar mascaramento.\n- Validar nulos preservados.\n- Validar escalas de taxas/percentuais.\n- Validar relacionamentos.\n- Validar se arquivos tratados estão prontos para geração de dados finais.",
        "",
        "## 12. Decisão da Etapa 03",
        "",
        "Status da Etapa 03:\n\n- [ ] Aprovada\n- [ ] Aprovada com ressalvas\n- [ ] Reprovada para avanço\n\nObservações da validação humana:\n\n- A preencher.",
        "",
        "## 13. Confirmações finais",
        "",
        "- Dados brutos preservados.\n- Arquivos tratados criados.\n- Dados finais não criados.\n- KPIs finais não criados.\n- Dashboard não criado.",
        "",
    ]

    RELATORIO_ETAPA_03.write_text("\n".join(partes), encoding="utf-8")


def main() -> None:
    """Executa a Etapa 03."""
    print("Etapa 03 - Tratamento e Padronização dos Dados")
    print("Dados brutos serão apenas lidos e preservados.")

    PASTA_DADOS_TRATADOS.mkdir(parents=True, exist_ok=True)
    PASTA_RELATORIOS.mkdir(parents=True, exist_ok=True)

    metadados = []
    arquivos_gerados = []

    for nome_arquivo in ARQUIVOS_ESCOPO:
        _, metadata = tratar_tabela(nome_arquivo)
        metadados.append(metadata)
        arquivos_gerados.append(metadata["arquivo_tratado"])

    gerar_relatorio(metadados, arquivos_gerados)

    print("\nArquivos tratados criados:")
    for arquivo in arquivos_gerados:
        print(f"- dados/tratados/{arquivo}")

    print("\nRelatório criado:")
    print(f"- {RELATORIO_ETAPA_03}")

    print("\nResumo da execução:")
    print(f"- Quantidade de arquivos tratados: {len(arquivos_gerados)}")
    print("- Confirmação: dados brutos não foram alterados.")
    print("- Nenhum arquivo foi criado em dados/finais/.")
    print("- Nenhum KPI final ou dashboard foi criado.")


if __name__ == "__main__":
    main()
