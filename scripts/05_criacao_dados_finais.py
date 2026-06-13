"""
Protocolo ADA - Etapa 05: Criação dos Dados Finais para Power BI

Finalidade:
- Criar arquivos finais em dados/finais/ a partir dos arquivos tratados.
- Preservar a granularidade definida no checklist de decisão da Etapa 05.
- Remover campos sensíveis que não devem seguir para os dados finais.
- Gerar um relatório documentando arquivos criados, validações e pendências.

Regras de segurança:
- Este script não altera dados brutos.
- Este script não altera dados tratados.
- Este script cria arquivos apenas em dados/finais/.
- Este script não cria dashboard.
- Este script não cria KPIs finais complexos.
- Este script não faz imputação automática.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


PASTA_RAIZ = Path(__file__).resolve().parents[1]
PASTA_TRATADOS = PASTA_RAIZ / "dados" / "tratados"
PASTA_FINAIS = PASTA_RAIZ / "dados" / "finais"
PASTA_RELATORIOS = PASTA_RAIZ / "relatorios"

RELATORIO_SAIDA = PASTA_RELATORIOS / "05_relatorio_criacao_dados_finais.md"

REFERENCIAS = [
    "relatorios/02_plano_tratamento_dados.md",
    "relatorios/03_relatorio_tratamento_padronizacao.md",
    "relatorios/04_relatorio_validacao_dados_tratados.md",
    "relatorios/04_1_checklist_decisao_etapa_05.md",
]


@dataclass
class ArquivoFinal:
    """Guarda as principais informações de cada arquivo final criado."""

    nome: str
    origem: str
    granularidade: str
    chave: str
    dados: pd.DataFrame
    observacoes: str = ""


MESES = {
    1: "janeiro",
    2: "fevereiro",
    3: "março",
    4: "abril",
    5: "maio",
    6: "junho",
    7: "julho",
    8: "agosto",
    9: "setembro",
    10: "outubro",
    11: "novembro",
    12: "dezembro",
}

DIAS_SEMANA = {
    0: "segunda-feira",
    1: "terça-feira",
    2: "quarta-feira",
    3: "quinta-feira",
    4: "sexta-feira",
    5: "sábado",
    6: "domingo",
}


def ler_csv_tratado(nome_arquivo: str) -> pd.DataFrame:
    """Lê um arquivo tratado sem alterar o arquivo original."""
    caminho = PASTA_TRATADOS / nome_arquivo
    return pd.read_csv(caminho)


def selecionar_colunas(df: pd.DataFrame, colunas: list[str], nome_origem: str) -> pd.DataFrame:
    """Seleciona apenas colunas aprovadas para o arquivo final."""
    faltantes = [coluna for coluna in colunas if coluna not in df.columns]
    if faltantes:
        raise ValueError(f"Colunas ausentes em {nome_origem}: {', '.join(faltantes)}")
    return df[colunas].copy()


def criar_arquivos_finais() -> list[ArquivoFinal]:
    """Cria os dataframes finais em memória antes de salvar em dados/finais/."""
    customers = ler_csv_tratado("customers_tratado.csv")
    routes = ler_csv_tratado("routes_tratado.csv")
    trucks = ler_csv_tratado("trucks_tratado.csv")
    loads = ler_csv_tratado("loads_tratado.csv")
    trips = ler_csv_tratado("trips_tratado.csv")
    events = ler_csv_tratado("delivery_events_tratado.csv")
    fuel = ler_csv_tratado("fuel_purchases_tratado.csv")

    arquivos = [
        ArquivoFinal(
            nome="dim_clientes.csv",
            origem="customers_tratado.csv",
            granularidade="uma linha por customer_id",
            chave="customer_id",
            dados=selecionar_colunas(
                customers,
                [
                    "customer_id",
                    "customer_name",
                    "customer_type",
                    "primary_freight_type",
                    "account_status",
                    "contract_start_date",
                    "credit_terms_days",
                    "annual_revenue_potential",
                ],
                "customers_tratado.csv",
            ),
            observacoes="customer_name mantido mascarado.",
        ),
        ArquivoFinal(
            nome="dim_rotas.csv",
            origem="routes_tratado.csv",
            granularidade="uma linha por route_id",
            chave="route_id",
            dados=selecionar_colunas(
                routes,
                [
                    "route_id",
                    "origin_city",
                    "origin_state",
                    "destination_city",
                    "destination_state",
                    "typical_distance_miles",
                    "base_rate_per_mile",
                    "fuel_surcharge_rate",
                    "typical_transit_days",
                ],
                "routes_tratado.csv",
            ),
            observacoes="Taxas preservadas na escala original.",
        ),
        ArquivoFinal(
            nome="dim_caminhoes.csv",
            origem="trucks_tratado.csv",
            granularidade="uma linha por truck_id",
            chave="truck_id",
            dados=selecionar_colunas(
                trucks,
                [
                    "truck_id",
                    "unit_number",
                    "make",
                    "model_year",
                    "acquisition_date",
                    "acquisition_mileage",
                    "fuel_type",
                    "tank_capacity_gallons",
                    "status",
                    "home_terminal",
                ],
                "trucks_tratado.csv",
            ),
            observacoes="vin removido dos dados finais.",
        ),
        ArquivoFinal(
            nome="fato_cargas.csv",
            origem="loads_tratado.csv",
            granularidade="uma linha por load_id",
            chave="load_id",
            dados=selecionar_colunas(
                loads,
                [
                    "load_id",
                    "customer_id",
                    "route_id",
                    "load_date",
                    "load_type",
                    "weight_lbs",
                    "pieces",
                    "revenue",
                    "fuel_surcharge",
                    "accessorial_charges",
                    "load_status",
                    "booking_type",
                ],
                "loads_tratado.csv",
            ),
        ),
        ArquivoFinal(
            nome="fato_viagens.csv",
            origem="trips_tratado.csv",
            granularidade="uma linha por trip_id",
            chave="trip_id",
            dados=selecionar_colunas(
                trips,
                [
                    "trip_id",
                    "load_id",
                    "driver_id",
                    "truck_id",
                    "trailer_id",
                    "dispatch_date",
                    "actual_distance_miles",
                    "actual_duration_hours",
                    "fuel_gallons_used",
                    "average_mpg",
                    "idle_time_hours",
                    "trip_status",
                ],
                "trips_tratado.csv",
            ),
            observacoes="Nulos operacionais preservados; average_mpg não deve ser somado diretamente.",
        ),
        ArquivoFinal(
            nome="fato_eventos_entrega.csv",
            origem="delivery_events_tratado.csv",
            granularidade="uma linha por event_id",
            chave="event_id",
            dados=selecionar_colunas(
                events,
                [
                    "event_id",
                    "load_id",
                    "trip_id",
                    "event_type",
                    "facility_id",
                    "scheduled_datetime",
                    "actual_datetime",
                    "detention_minutes",
                    "on_time_flag",
                    "location_city",
                    "location_state",
                ],
                "delivery_events_tratado.csv",
            ),
            observacoes="on_time_flag preservado; KPI de pontualidade não foi criado.",
        ),
        ArquivoFinal(
            nome="fato_abastecimentos.csv",
            origem="fuel_purchases_tratado.csv",
            granularidade="uma linha por fuel_purchase_id",
            chave="fuel_purchase_id",
            dados=selecionar_colunas(
                fuel,
                [
                    "fuel_purchase_id",
                    "trip_id",
                    "truck_id",
                    "driver_id",
                    "purchase_date",
                    "location_city",
                    "location_state",
                    "gallons",
                    "price_per_gallon",
                    "total_cost",
                ],
                "fuel_purchases_tratado.csv",
            ),
            observacoes="fuel_card_number removido; price_per_gallon não deve ser somado diretamente.",
        ),
    ]

    calendario = criar_dim_calendario(arquivos)
    arquivos.append(
        ArquivoFinal(
            nome="dim_calendario.csv",
            origem="datas do núcleo final V1",
            granularidade="uma linha por data",
            chave="data",
            dados=calendario,
            observacoes="Calendário padrão; sem feriados e sem calendário fiscal.",
        )
    )

    return arquivos


def criar_dim_calendario(arquivos: list[ArquivoFinal]) -> pd.DataFrame:
    """Cria calendário usando a menor e maior data encontradas no núcleo final V1."""
    campos_data = [
        ("dim_clientes.csv", "contract_start_date"),
        ("dim_caminhoes.csv", "acquisition_date"),
        ("fato_cargas.csv", "load_date"),
        ("fato_viagens.csv", "dispatch_date"),
        ("fato_eventos_entrega.csv", "scheduled_datetime"),
        ("fato_eventos_entrega.csv", "actual_datetime"),
        ("fato_abastecimentos.csv", "purchase_date"),
    ]

    datas = []
    por_nome = {arquivo.nome: arquivo.dados for arquivo in arquivos}

    for nome_arquivo, coluna in campos_data:
        serie = pd.to_datetime(por_nome[nome_arquivo][coluna], errors="coerce")
        datas.append(serie.dropna().dt.normalize())

    datas_validas = pd.concat(datas, ignore_index=True).dropna()
    if datas_validas.empty:
        raise ValueError("Não foram encontradas datas válidas para criar dim_calendario.csv.")

    menor_data = datas_validas.min()
    maior_data = datas_validas.max()
    calendario = pd.DataFrame({"data": pd.date_range(menor_data, maior_data, freq="D")})

    calendario["ano"] = calendario["data"].dt.year
    calendario["mes"] = calendario["data"].dt.month
    calendario["nome_mes"] = calendario["mes"].map(MESES)
    calendario["trimestre"] = "T" + calendario["data"].dt.quarter.astype(str)
    calendario["ano_mes"] = calendario["data"].dt.strftime("%Y-%m")
    calendario["dia"] = calendario["data"].dt.day
    calendario["dia_semana"] = calendario["data"].dt.weekday + 1
    calendario["nome_dia_semana"] = calendario["data"].dt.weekday.map(DIAS_SEMANA)
    calendario["data"] = calendario["data"].dt.strftime("%Y-%m-%d")

    return calendario


def salvar_arquivos_finais(arquivos: list[ArquivoFinal]) -> None:
    """Salva os arquivos finais apenas na pasta dados/finais/."""
    PASTA_FINAIS.mkdir(parents=True, exist_ok=True)
    for arquivo in arquivos:
        caminho = PASTA_FINAIS / arquivo.nome
        arquivo.dados.to_csv(caminho, index=False, encoding="utf-8")


def percentual(nulos: int, total: int) -> float:
    """Calcula percentual evitando divisão por zero."""
    if total == 0:
        return 0.0
    return nulos / total * 100


def validar_arquivos(arquivos: list[ArquivoFinal]) -> list[dict[str, object]]:
    """Valida existência, chave principal, duplicidades e nulos críticos."""
    validacoes = []

    for arquivo in arquivos:
        caminho = PASTA_FINAIS / arquivo.nome
        df = arquivo.dados
        chave = arquivo.chave
        duplicidades = int(df.duplicated(subset=[chave]).sum())
        nulos_chave = int(df[chave].isna().sum())
        status = "OK" if caminho.exists() and duplicidades == 0 and nulos_chave == 0 else "Atenção"

        validacoes.append(
            {
                "arquivo": arquivo.nome,
                "chave": chave,
                "existe": "sim" if caminho.exists() else "não",
                "duplicidades": duplicidades,
                "nulos_chave": nulos_chave,
                "linhas": len(df),
                "colunas": len(df.columns),
                "status": status,
            }
        )

    return validacoes


def validar_relacionamentos(arquivos: list[ArquivoFinal]) -> list[dict[str, object]]:
    """Valida correspondência entre chaves, ignorando nulos quando permitido."""
    tabelas = {arquivo.nome: arquivo.dados for arquivo in arquivos}
    relacionamentos = [
        ("fato_cargas.csv", "customer_id", "dim_clientes.csv", "customer_id", "muitos para um"),
        ("fato_cargas.csv", "route_id", "dim_rotas.csv", "route_id", "muitos para um"),
        ("fato_viagens.csv", "load_id", "fato_cargas.csv", "load_id", "1:1 observado; validar no modelo"),
        ("fato_viagens.csv", "truck_id", "dim_caminhoes.csv", "truck_id", "muitos para um"),
        ("fato_eventos_entrega.csv", "trip_id", "fato_viagens.csv", "trip_id", "muitos para um"),
        ("fato_eventos_entrega.csv", "load_id", "fato_cargas.csv", "load_id", "muitos para um"),
        ("fato_abastecimentos.csv", "trip_id", "fato_viagens.csv", "trip_id", "muitos para um"),
        ("fato_abastecimentos.csv", "truck_id", "dim_caminhoes.csv", "truck_id", "muitos para um"),
    ]

    resultados = []
    for origem, coluna_origem, destino, coluna_destino, tipo in relacionamentos:
        serie_origem = tabelas[origem][coluna_origem]
        valores_origem = set(serie_origem.dropna().astype(str))
        valores_destino = set(tabelas[destino][coluna_destino].dropna().astype(str))
        sem_correspondencia = len(valores_origem - valores_destino)
        nulos_preservados = int(serie_origem.isna().sum())
        status = "OK" if sem_correspondencia == 0 else "Atenção"

        resultados.append(
            {
                "origem": origem,
                "coluna_origem": coluna_origem,
                "destino": destino,
                "coluna_destino": coluna_destino,
                "tipo": tipo,
                "sem_correspondencia": sem_correspondencia,
                "nulos_preservados": nulos_preservados,
                "status": status,
                "observacao": "Nulos ignorados na correspondência e preservados no arquivo final."
                if nulos_preservados
                else "Sem nulos na coluna de relacionamento.",
            }
        )

    return resultados


def validar_campos_sensiveis(arquivos: list[ArquivoFinal]) -> list[dict[str, str]]:
    """Registra as decisões aplicadas sobre campos sensíveis."""
    tabelas = {arquivo.nome: arquivo.dados for arquivo in arquivos}
    return [
        {
            "campo": "customer_name",
            "origem": "customers_tratado.csv",
            "decisao": "manter mascarado",
            "acao": "mantido em dim_clientes.csv",
            "justificativa": "Permite segmentação sem expor o nome original do cliente.",
            "status": "OK" if "customer_name" in tabelas["dim_clientes.csv"].columns else "Atenção",
        },
        {
            "campo": "vin",
            "origem": "trucks_tratado.csv",
            "decisao": "remover dos dados finais",
            "acao": "removido de dim_caminhoes.csv",
            "justificativa": "Identificador operacional sem valor analítico público para a V1.",
            "status": "OK" if "vin" not in tabelas["dim_caminhoes.csv"].columns else "Atenção",
        },
        {
            "campo": "fuel_card_number",
            "origem": "fuel_purchases_tratado.csv",
            "decisao": "remover dos dados finais",
            "acao": "removido de fato_abastecimentos.csv",
            "justificativa": "Reduz risco de exposição e não agrega valor analítico público.",
            "status": "OK"
            if "fuel_card_number" not in tabelas["fato_abastecimentos.csv"].columns
            else "Atenção",
        },
    ]


def nulos_preservados(arquivos: list[ArquivoFinal]) -> list[dict[str, object]]:
    """Lista os nulos operacionais que devem ser preservados por decisão humana."""
    tabelas = {arquivo.nome: arquivo.dados for arquivo in arquivos}
    campos = [
        ("fato_viagens.csv", "driver_id"),
        ("fato_viagens.csv", "truck_id"),
        ("fato_viagens.csv", "trailer_id"),
        ("fato_abastecimentos.csv", "driver_id"),
        ("fato_abastecimentos.csv", "truck_id"),
    ]

    registros = []
    for tabela, coluna in campos:
        df = tabelas[tabela]
        nulos = int(df[coluna].isna().sum())
        registros.append(
            {
                "tabela": tabela,
                "coluna": coluna,
                "nulos": nulos,
                "percentual": percentual(nulos, len(df)),
                "justificativa": "Nulo preservado; sem imputação automática e sem remoção de registros.",
            }
        )
    return registros


def linha_tabela(valores: list[object]) -> str:
    """Cria uma linha de tabela Markdown."""
    return "| " + " | ".join(str(valor) for valor in valores) + " |"


def gerar_relatorio(
    arquivos: list[ArquivoFinal],
    validacoes: list[dict[str, object]],
    relacionamentos: list[dict[str, object]],
    sensiveis: list[dict[str, str]],
    nulos: list[dict[str, object]],
) -> None:
    """Gera o relatório Markdown da Etapa 05."""
    por_nome = {arquivo.nome: arquivo for arquivo in arquivos}
    calendario = por_nome["dim_calendario.csv"].dados

    linhas = [
        "# Relatório da Etapa 05 — Criação dos Dados Finais para Power BI",
        "",
        "## 1. Objetivo da etapa",
        "",
        "Esta etapa cria os arquivos finais para Power BI a partir dos dados tratados validados nas etapas anteriores do Protocolo ADA.",
        "",
        "Python gera evidências. IA interpreta hipóteses. Humano valida decisões.",
        "",
        "## 2. Confirmação de segurança",
        "",
        "* dados brutos não foram alterados;",
        "* dados tratados não foram alterados;",
        "* dados finais foram criados em `dados/finais/`;",
        "* nenhum dashboard foi criado;",
        "* nenhum KPI final complexo foi criado;",
        "* nenhuma imputação automática foi feita.",
        "",
        "## 3. Fontes utilizadas",
        "",
        "Arquivos tratados utilizados:",
    ]

    for arquivo in arquivos:
        if arquivo.nome != "dim_calendario.csv":
            linhas.append(f"* `dados/tratados/{arquivo.origem}`")

    linhas.extend(["", "Relatórios de referência:"])
    for referencia in REFERENCIAS:
        linhas.append(f"* `{referencia}`")

    linhas.extend(
        [
            "",
            "Checklist de decisão utilizado:",
            "",
            "* `relatorios/04_1_checklist_decisao_etapa_05.md`",
            "",
            "## 4. Arquivos finais criados",
            "",
            "| arquivo final | origem | granularidade | linhas | colunas | status |",
            "|---|---|---|---:|---:|---|",
        ]
    )

    for arquivo in arquivos:
        linhas.append(
            linha_tabela(
                [
                    f"`{arquivo.nome}`",
                    arquivo.origem,
                    arquivo.granularidade,
                    len(arquivo.dados),
                    len(arquivo.dados.columns),
                    "OK",
                ]
            )
        )

    linhas.extend(["", "## 5. Estrutura das dimensões", ""])
    for nome in ["dim_clientes.csv", "dim_rotas.csv", "dim_caminhoes.csv"]:
        arquivo = por_nome[nome]
        linhas.extend(
            [
                f"### {nome}",
                "",
                f"* origem: `{arquivo.origem}`;",
                f"* chave: `{arquivo.chave}`;",
                f"* granularidade: {arquivo.granularidade};",
                f"* colunas: {', '.join(f'`{coluna}`' for coluna in arquivo.dados.columns)};",
                f"* campos sensíveis removidos ou mantidos mascarados: {descricao_sensivel_dimensao(nome)};",
                f"* observações: {arquivo.observacoes or 'sem observações adicionais.'}",
                "",
            ]
        )

    linhas.extend(["## 6. Estrutura das tabelas fato", ""])
    for nome in ["fato_cargas.csv", "fato_viagens.csv", "fato_eventos_entrega.csv", "fato_abastecimentos.csv"]:
        arquivo = por_nome[nome]
        linhas.extend(
            [
                f"### {nome}",
                "",
                f"* origem: `{arquivo.origem}`;",
                f"* chave: `{arquivo.chave}`;",
                f"* granularidade: {arquivo.granularidade};",
                f"* colunas: {', '.join(f'`{coluna}`' for coluna in arquivo.dados.columns)};",
                f"* nulos preservados: {descricao_nulos_fato(nome, nulos)};",
                f"* campos que não devem ser somados diretamente: {descricao_nao_somar(nome)};",
                f"* observações: {arquivo.observacoes or 'sem observações adicionais.'}",
                "",
            ]
        )

    linhas.extend(
        [
            "## 7. Dimensão calendário",
            "",
            f"* menor data usada: `{calendario['data'].min()}`;",
            f"* maior data usada: `{calendario['data'].max()}`;",
            f"* quantidade de datas criadas: {len(calendario)};",
            f"* campos criados: {', '.join(f'`{coluna}`' for coluna in calendario.columns)};",
            "* observações: calendário criado sem feriados e sem calendário fiscal.",
            "",
            "## 8. Campos sensíveis e decisões aplicadas",
            "",
            "| campo | origem | decisão | ação aplicada | justificativa | status |",
            "|---|---|---|---|---|---|",
        ]
    )

    for item in sensiveis:
        linhas.append(
            linha_tabela(
                [
                    f"`{item['campo']}`",
                    item["origem"],
                    item["decisao"],
                    item["acao"],
                    item["justificativa"],
                    item["status"],
                ]
            )
        )

    linhas.extend(
        [
            "",
            "## 9. Nulos preservados",
            "",
            "| tabela final | coluna | nulos preservados | percentual | justificativa |",
            "|---|---|---:|---:|---|",
        ]
    )

    for item in nulos:
        linhas.append(
            linha_tabela(
                [
                    f"`{item['tabela']}`",
                    f"`{item['coluna']}`",
                    item["nulos"],
                    f"{item['percentual']:.2f}%",
                    item["justificativa"],
                ]
            )
        )

    linhas.extend(
        [
            "",
            "## 10. Relacionamentos esperados para Power BI",
            "",
            "| tabela origem | coluna origem | tabela destino | coluna destino | tipo esperado | valores sem correspondência | status | observação |",
            "|---|---|---|---|---|---:|---|---|",
        ]
    )

    for item in relacionamentos:
        linhas.append(
            linha_tabela(
                [
                    f"`{item['origem']}`",
                    f"`{item['coluna_origem']}`",
                    f"`{item['destino']}`",
                    f"`{item['coluna_destino']}`",
                    item["tipo"],
                    item["sem_correspondencia"],
                    item["status"],
                    item["observacao"],
                ]
            )
        )

    linhas.extend(
        [
            "",
            "## 11. Validações pós-criação",
            "",
            "| arquivo | chave principal | duplicidades | linhas | colunas | status |",
            "|---|---|---:|---:|---:|---|",
        ]
    )

    for item in validacoes:
        linhas.append(
            linha_tabela(
                [
                    f"`{item['arquivo']}`",
                    f"`{item['chave']}`",
                    item["duplicidades"],
                    item["linhas"],
                    item["colunas"],
                    item["status"],
                ]
            )
        )

    linhas.extend(
        [
            "",
            "## 12. Pontos de atenção para Power BI",
            "",
            "* não somar `average_mpg`;",
            "* não somar `price_per_gallon`;",
            "* não somar `base_rate_per_mile`;",
            "* não somar `fuel_surcharge_rate`;",
            "* formatar `fuel_surcharge_rate` como percentual no Power BI, se confirmado;",
            "* formatar campos financeiros como moeda no Power BI;",
            "* usar dimensão calendário para filtros temporais;",
            "* revisar nulos preservados em relacionamentos.",
            "",
            "## 13. Pendências para próxima etapa",
            "",
            "* validação final dos dados finais;",
            "* documentação dos KPIs;",
            "* criação das medidas no Power BI;",
            "* definição dos visuais;",
            "* criação do dashboard.",
            "",
            "## 14. Decisão da Etapa 05",
            "",
            "Status da Etapa 05:",
            "",
            "* [ ] Aprovada",
            "* [ ] Aprovada com ressalvas",
            "* [ ] Reprovada para avanço",
            "",
            "Observações da validação humana:",
            "",
            "* A preencher.",
            "",
            "## 15. Confirmações finais",
            "",
            "* dados brutos preservados;",
            "* dados tratados preservados;",
            "* arquivos finais criados;",
            "* dashboard não criado;",
            "* KPIs finais complexos não criados.",
            "",
        ]
    )

    RELATORIO_SAIDA.write_text("\n".join(linhas), encoding="utf-8")


def descricao_sensivel_dimensao(nome: str) -> str:
    """Descreve campos sensíveis por dimensão."""
    descricoes = {
        "dim_clientes.csv": "`customer_name` mantido mascarado.",
        "dim_rotas.csv": "nenhum campo sensível identificado para remoção na V1.",
        "dim_caminhoes.csv": "`vin` removido.",
    }
    return descricoes.get(nome, "não aplicável.")


def descricao_nulos_fato(nome: str, nulos: list[dict[str, object]]) -> str:
    """Resume nulos preservados por tabela fato."""
    itens = [item for item in nulos if item["tabela"] == nome and item["nulos"] > 0]
    if not itens:
        return "sem nulos operacionais destacados."
    return "; ".join(f"`{item['coluna']}`: {item['nulos']}" for item in itens)


def descricao_nao_somar(nome: str) -> str:
    """Indica campos que exigem cuidado em agregações."""
    campos = {
        "fato_cargas.csv": "sem restrição específica além de validar regras de negócio para valores financeiros.",
        "fato_viagens.csv": "`average_mpg`.",
        "fato_eventos_entrega.csv": "não criar KPI de pontualidade diretamente nesta etapa.",
        "fato_abastecimentos.csv": "`price_per_gallon`.",
    }
    return campos.get(nome, "não aplicável.")


def verificar_referencias() -> None:
    """Confirma que os relatórios usados como referência existem."""
    faltantes = [referencia for referencia in REFERENCIAS if not (PASTA_RAIZ / referencia).exists()]
    if faltantes:
        raise FileNotFoundError("Referências ausentes: " + ", ".join(faltantes))


def main() -> None:
    """Executa a criação dos dados finais e do relatório da Etapa 05."""
    verificar_referencias()

    arquivos = criar_arquivos_finais()
    salvar_arquivos_finais(arquivos)

    validacoes = validar_arquivos(arquivos)
    relacionamentos = validar_relacionamentos(arquivos)
    sensiveis = validar_campos_sensiveis(arquivos)
    nulos = nulos_preservados(arquivos)

    gerar_relatorio(arquivos, validacoes, relacionamentos, sensiveis, nulos)

    print("Etapa 05 concluída: criação dos dados finais para Power BI.")
    print("\nArquivos finais criados:")
    for arquivo in arquivos:
        print(f"- dados/finais/{arquivo.nome}: {len(arquivo.dados)} linhas, {len(arquivo.dados.columns)} colunas")
    print(f"\nRelatório criado: {RELATORIO_SAIDA.relative_to(PASTA_RAIZ)}")
    print(f"Quantidade de arquivos finais: {len(arquivos)}")
    print("Confirmação: dados brutos e dados tratados não foram alterados.")
    print("Confirmação: nenhum dashboard foi criado e nenhum KPI final complexo foi criado.")


if __name__ == "__main__":
    main()
