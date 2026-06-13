"""
Protocolo ADA - Etapa 02: Plano de Tratamento e Padronização dos Dados

Finalidade:
- Ler os arquivos brutos apenas para coletar evidências de apoio.
- Ler o relatório da Etapa 01 como referência documental.
- Gerar um plano de tratamento em relatorios/02_plano_tratamento_dados.md.

Regras principais:
- Este script não altera dados brutos.
- Este script não cria arquivos em dados/tratados/ nem em dados/finais/.
- Este script não aplica limpeza, conversão, remoção, preenchimento, KPI ou dashboard.
- Todas as propostas são hipóteses e exigem validação humana.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd

from ada_relatorios import (
    escrever_relatorio_preservando_validacao,
    montar_secao_validacao_humana,
)


PASTA_DADOS_BRUTOS = Path("dados/brutos")
PASTA_RELATORIOS = Path("relatorios")
RELATORIO_ETAPA_01 = PASTA_RELATORIOS / "01_relatorio_inspecao_dados.md"
RELATORIO_ETAPA_02 = PASTA_RELATORIOS / "02_plano_tratamento_dados.md"

ESCOPO_PRINCIPAL_V1 = [
    "loads.csv",
    "trips.csv",
    "delivery_events.csv",
    "routes.csv",
    "customers.csv",
    "fuel_purchases.csv",
    "trucks.csv",
]

ESCOPO_COMPLEMENTAR_FUTURO = [
    "drivers.csv",
    "driver_monthly_metrics.csv",
    "truck_utilization_metrics.csv",
    "maintenance_records.csv",
    "safety_incidents.csv",
    "trailers.csv",
    "facilities.csv",
]

RELACIONAMENTOS_CANDIDATOS = [
    ("loads.load_id", "trips.load_id", "1:1 observado/provável, com validação conceitual pendente", "validar se toda carga deve ter exatamente uma viagem antes da modelagem"),
    ("trips.trip_id", "delivery_events.trip_id", "1:N potencial", "duplicação de viagens ao juntar eventos"),
    ("loads.customer_id", "customers.customer_id", "N:1 potencial", "cliente ausente ou duplicado afeta segmentação"),
    ("loads.route_id", "routes.route_id", "N:1 potencial", "rota ausente afeta análises por origem/destino"),
    ("trips.driver_id", "drivers.driver_id", "N:1 potencial", "envolve dados pessoais de motorista"),
    ("trips.truck_id", "trucks.truck_id", "N:1 potencial", "vínculo com frota precisa ser validado"),
    ("trips.trailer_id", "trailers.trailer_id", "N:1 potencial", "vínculo com carreta/equipamento precisa ser validado"),
    ("delivery_events.facility_id", "facilities.facility_id", "N:1 potencial", "eventos podem duplicar instalações"),
    ("fuel_purchases.trip_id", "trips.trip_id", "N:1 potencial", "abastecimentos podem ocorrer múltiplas vezes por viagem"),
    ("fuel_purchases.truck_id", "trucks.truck_id", "N:1 potencial", "custo de combustível exige granularidade correta"),
    ("maintenance_records.truck_id", "trucks.truck_id", "N:1 potencial", "manutenções podem ocorrer várias vezes por caminhão"),
    ("safety_incidents.trip_id", "trips.trip_id", "N:1 potencial", "incidentes podem ser zero, um ou vários por viagem"),
]

METRICAS_OPERACIONAIS_CLARAS = {
    "weight_lbs": ("peso", "manter numérico; documentar unidade em libras"),
    "pieces": ("quantidade/contagem", "manter numérico; validar se representa peças transportadas"),
    "actual_distance_miles": ("distância", "manter numérico; documentar unidade em milhas"),
    "fuel_gallons_used": ("volume de combustível", "manter numérico; documentar unidade em galões"),
    "total_fuel_gallons": ("volume total de combustível", "manter numérico; documentar unidade em galões"),
    "gallons": ("volume de combustível", "manter numérico; documentar unidade em galões"),
    "typical_distance_miles": ("distância padrão", "manter numérico; documentar unidade em milhas"),
    "dock_doors": ("quantidade/capacidade operacional", "manter numérico; validar se representa capacidade"),
    "tank_capacity_gallons": ("capacidade de tanque", "manter numérico; documentar unidade em galões"),
    "acquisition_mileage": ("quilometragem de aquisição", "manter numérico; documentar unidade"),
    "odometer_reading": ("leitura de odômetro", "manter numérico; documentar unidade"),
    "length_feet": ("comprimento", "manter numérico; documentar unidade em pés"),
}

CODIGOS_OPERACIONAIS = {
    "unit_number": "código/número operacional",
    "trailer_number": "código/número operacional",
}

NULOS_RELEVANTES = [
    ("drivers.csv", "termination_date", "provavelmente indica motorista ativo, não erro"),
    ("trips.csv", "driver_id", "pode indicar viagem sem motorista associado ou falha de registro"),
    ("trips.csv", "truck_id", "pode indicar viagem sem caminhão associado ou falha de registro"),
    ("trips.csv", "trailer_id", "pode indicar viagem sem carreta associada ou falha de registro"),
    ("fuel_purchases.csv", "driver_id", "pode indicar compra sem motorista associado"),
    ("fuel_purchases.csv", "truck_id", "pode indicar compra sem caminhão associado"),
    ("safety_incidents.csv", "driver_id", "pode indicar incidente sem motorista associado"),
    ("safety_incidents.csv", "truck_id", "pode indicar incidente sem caminhão associado"),
]


def normalizar(nome: str) -> str:
    """Padroniza nomes para comparações simples."""
    return nome.strip().lower()


def partes(nome: str) -> list[str]:
    """Divide nomes de colunas em partes."""
    return [parte for parte in normalizar(nome).split("_") if parte]


def ler_csvs_brutos() -> tuple[dict[str, pd.DataFrame], list[str]]:
    """Lê CSVs brutos apenas para planejar; não altera nenhum arquivo."""
    tabelas: dict[str, pd.DataFrame] = {}
    erros: list[str] = []

    for caminho in sorted(PASTA_DADOS_BRUTOS.glob("*.csv")):
        try:
            tabelas[caminho.name] = pd.read_csv(caminho, low_memory=False)
        except Exception as erro:  # noqa: BLE001 - o erro deve ir ao relatório
            erros.append(f"- `{caminho.name}`: `{type(erro).__name__}: {erro}`")

    return tabelas, erros


def ler_referencia_etapa_01() -> str:
    """Lê o relatório da Etapa 01 como apoio documental."""
    if not RELATORIO_ETAPA_01.exists():
        return "Relatório da Etapa 01 não encontrado."

    conteudo = RELATORIO_ETAPA_01.read_text(encoding="utf-8")
    return f"Relatório encontrado com {len(conteudo.splitlines())} linhas e {len(conteudo)} caracteres."


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


def exemplo_valor(tabela: pd.DataFrame, coluna: str) -> str:
    """Coleta um exemplo pequeno de valor real para orientar o plano."""
    if coluna not in tabela.columns:
        return ""
    valores = tabela[coluna].dropna()
    if valores.empty:
        return "nulo"
    return str(valores.iloc[0])


def eh_id(coluna: str) -> bool:
    """Identifica IDs e chaves por nome."""
    nome = normalizar(coluna)
    return nome == "id" or nome.endswith("_id")


def eh_data(coluna: str) -> bool:
    """Identifica campos de data ou período por nome."""
    nome = normalizar(coluna)
    return (
        "date" in partes(coluna)
        or "datetime" in nome
        or "timestamp" in nome
        or nome == "month"
    )


def eh_financeiro(coluna: str) -> bool:
    """Identifica campos financeiros por nome."""
    termos = {"revenue", "cost", "price", "charge", "charges", "amount", "valor", "custo", "receita", "surcharge"}
    return any(parte in termos for parte in partes(coluna)) or "rate_per" in normalizar(coluna)


def eh_percentual_taxa(coluna: str) -> bool:
    """Identifica percentuais, taxas e índices."""
    nome = normalizar(coluna)
    return any(parte in {"rate", "ratio", "percent", "percentage", "score"} for parte in partes(coluna)) or nome.endswith("_rate")


def eh_preco_unitario(coluna: str) -> bool:
    """Identifica preço ou taxa monetária por unidade."""
    nome = normalizar(coluna)
    return "price_per" in nome or "rate_per" in nome or "_per_" in nome


def eh_duracao(coluna: str) -> bool:
    """Identifica campos de tempo, duração ou quantidade de dias/horas/minutos."""
    return any(parte in {"minutes", "hours", "days", "duration", "years", "experience"} for parte in partes(coluna))


def eh_booleano(coluna: str, serie: pd.Series) -> bool:
    """Identifica booleanos por tipo, nome ou valores."""
    nome = normalizar(coluna)
    if pd.api.types.is_bool_dtype(serie) or nome.endswith("_flag"):
        return True
    valores = {str(valor).strip().lower() for valor in serie.dropna().unique()[:20]}
    return bool(valores) and valores.issubset({"true", "false", "sim", "não", "nao", "yes", "no", "0", "1"})


def eh_confidencial(coluna: str) -> bool:
    """Identifica campos pessoais, identificáveis ou confidenciais."""
    return normalizar(coluna) in {
        "first_name",
        "last_name",
        "date_of_birth",
        "license_number",
        "vin",
        "fuel_card_number",
        "customer_name",
        "description",
        "service_description",
    }


def tipo_risco_confidencial(coluna: str) -> str:
    """Descreve o tipo de risco para campos sensíveis."""
    nome = normalizar(coluna)
    if nome in {"first_name", "last_name", "date_of_birth"}:
        return "dado pessoal"
    if nome == "license_number":
        return "dado pessoal/identificável"
    if nome in {"vin", "fuel_card_number"}:
        return "identificador operacional confidencial"
    if nome == "customer_name":
        return "dado comercial confidencial"
    if nome in {"description", "service_description"}:
        return "texto livre com possível risco"
    return "risco a validar"


def eh_categoria(coluna: str, serie: pd.Series) -> bool:
    """Identifica possíveis categorias, status e códigos."""
    termos = {"type", "status", "state", "city", "class", "location", "terminal", "make", "booking"}
    if any(parte in termos for parte in partes(coluna)):
        return True
    if pd.api.types.is_string_dtype(serie):
        return serie.nunique(dropna=True) <= max(20, int(len(serie) * 0.05))
    return False


def classificar_coluna(tabela: pd.DataFrame, coluna: str) -> dict[str, str]:
    """Classifica a coluna para montar proposta de tratamento."""
    serie = tabela[coluna]
    antes = exemplo_valor(tabela, coluna)
    nome = normalizar(coluna)

    if eh_confidencial(coluna):
        return {
            "papel": tipo_risco_confidencial(coluna),
            "problema": "pode expor informação pessoal, identificável, comercial ou operacional sensível",
            "tratamento": "remover, mascarar ou manter apenas em ambiente privado, conforme aprovação",
            "depois": "[removido/mascarado/controlado]",
            "risco": "alto",
            "impacto": "reduz risco de exposição em relatórios e arquivos finais",
            "validacao": "Sim",
            "antes": antes,
        }

    if nome in CODIGOS_OPERACIONAIS:
        return {
            "papel": CODIGOS_OPERACIONAIS[nome],
            "problema": "não deve ser tratado como métrica, mesmo quando armazenado como número",
            "tratamento": "manter como texto/código operacional; validar uso em filtros ou identificação",
            "depois": antes,
            "risco": "médio",
            "impacto": "evita soma, média ou ordenação numérica indevida no Power BI",
            "validacao": "Sim",
            "antes": antes,
        }

    if eh_id(coluna):
        return {
            "papel": "ID/chave",
            "problema": "risco de conversão indevida para número ou perda de zeros à esquerda",
            "tratamento": "manter como texto e validar chave primária/estrangeira",
            "depois": antes,
            "risco": "médio",
            "impacto": "melhora relacionamentos no modelo",
            "validacao": "Sim",
            "antes": antes,
        }

    if nome == "operating_hours":
        return {
            "papel": "texto/categoria/faixa operacional de horário",
            "problema": "representa faixa de funcionamento, não métrica numérica de duração",
            "tratamento": "manter como texto; padronizar valores apenas se houver inconsistência comprovada",
            "depois": antes,
            "risco": "baixo",
            "impacto": "melhora filtros e descrições operacionais no Power BI",
            "validacao": "Sim",
            "antes": antes,
        }

    if nome == "model_year":
        return {
            "papel": "ano/modelo, atributo temporal",
            "problema": "não deve ser tratado como quantidade operacional",
            "tratamento": "manter como ano/atributo; validar formato e uso como segmentação",
            "depois": antes,
            "risco": "baixo",
            "impacto": "permite análise por ano de modelo sem somas indevidas",
            "validacao": "Sim",
            "antes": antes,
        }

    if eh_data(coluna):
        return {
            "papel": "data, data/hora ou período",
            "problema": "precisa de formato validado antes da conversão",
            "tratamento": "converter em etapa futura para data/data-hora ou período mensal",
            "depois": "data/período padronizado",
            "risco": "médio",
            "impacto": "permite ordenação temporal e filtros corretos no Power BI",
            "validacao": "Sim",
            "antes": antes,
        }

    if nome in METRICAS_OPERACIONAIS_CLARAS:
        papel, tratamento = METRICAS_OPERACIONAIS_CLARAS[nome]
        return {
            "papel": f"métrica numérica operacional: {papel}",
            "problema": "unidade e regra de agregação precisam ser documentadas",
            "tratamento": tratamento,
            "depois": antes,
            "risco": "médio",
            "impacto": "permite medidas operacionais mais claras no Power BI",
            "validacao": "Sim",
            "antes": antes,
        }

    if eh_booleano(coluna, serie):
        return {
            "papel": "booleano/flag operacional",
            "problema": "não deve ser tratado como métrica numérica principal",
            "tratamento": "manter como booleano; criar descrição amigável apenas se aprovado",
            "depois": antes,
            "risco": "baixo",
            "impacto": "permite filtros e cálculo de taxas com regra documentada",
            "validacao": "Sim",
            "antes": antes,
        }

    if eh_preco_unitario(coluna):
        return {
            "papel": "taxa monetária por unidade/preço unitário",
            "problema": "não deve ser somado diretamente",
            "tratamento": "manter numérico e definir agregação futura, preferencialmente média ponderada",
            "depois": antes,
            "risco": "alto",
            "impacto": "evita distorção de valores unitários no Power BI",
            "validacao": "Sim",
            "antes": antes,
        }

    if eh_percentual_taxa(coluna):
        return {
            "papel": "percentual/taxa/índice",
            "problema": "escala precisa ser validada antes de formatar como percentual",
            "tratamento": "validar escala; não multiplicar por 100 sem aprovação",
            "depois": antes,
            "risco": "alto",
            "impacto": "evita percentuais incorretos no Power BI",
            "validacao": "Sim",
            "antes": antes,
        }

    if eh_financeiro(coluna):
        return {
            "papel": "campo financeiro",
            "problema": "moeda, arredondamento e agregação precisam ser validados",
            "tratamento": "manter numérico; formatar como moeda apenas no Power BI",
            "depois": antes,
            "risco": "médio",
            "impacto": "permite análises financeiras sem arredondamento prematuro",
            "validacao": "Sim",
            "antes": antes,
        }

    if eh_duracao(coluna):
        return {
            "papel": "tempo/duração/quantidade temporal",
            "problema": "unidade precisa estar documentada",
            "tratamento": "manter numérico; documentar unidade e não converter para data",
            "depois": antes,
            "risco": "médio",
            "impacto": "permite medidas de tempo coerentes no Power BI",
            "validacao": "Sim",
            "antes": antes,
        }

    if eh_categoria(coluna, serie):
        return {
            "papel": "categoria/status/código",
            "problema": "domínio de valores pode precisar de documentação ou padronização futura",
            "tratamento": "manter como texto; padronizar apenas se inconsistência for comprovada",
            "depois": antes,
            "risco": "baixo",
            "impacto": "melhora filtros, segmentações e rótulos no Power BI",
            "validacao": "Sim",
            "antes": antes,
        }

    return {
        "papel": "ambíguo / exige validação humana",
        "problema": "evidência insuficiente para definir tratamento automático",
        "tratamento": "não aplicar tratamento antes de validação humana",
        "depois": antes,
        "risco": "médio",
        "impacto": "evita tratamento indevido por inferência fraca",
        "validacao": "Sim",
        "antes": antes,
    }


def gerar_plano_por_coluna(tabelas: dict[str, pd.DataFrame]) -> str:
    """Gera tabela detalhada de tratamento proposto por tabela e coluna."""
    linhas = []

    for nome_tabela, tabela in sorted(tabelas.items()):
        for coluna in tabela.columns:
            classificacao = classificar_coluna(tabela, coluna)
            linhas.append(
                {
                    "tabela": nome_tabela,
                    "coluna": coluna,
                    "tipo atual identificado": str(tabela[coluna].dtype),
                    "papel técnico provável": classificacao["papel"],
                    "problema ou oportunidade": classificacao["problema"],
                    "tratamento proposto": classificacao["tratamento"],
                    "exemplo de antes": classificacao["antes"],
                    "exemplo de depois": classificacao["depois"],
                    "nível de risco": classificacao["risco"],
                    "impacto esperado no Power BI": classificacao["impacto"],
                    "validação humana necessária": classificacao["validacao"],
                }
            )

    return formatar_tabela(
        linhas,
        [
            "tabela",
            "coluna",
            "tipo atual identificado",
            "papel técnico provável",
            "problema ou oportunidade",
            "tratamento proposto",
            "exemplo de antes",
            "exemplo de depois",
            "nível de risco",
            "impacto esperado no Power BI",
            "validação humana necessária",
        ],
    )


def papel_tabela(nome_tabela: str) -> str:
    """Retorna papel provável resumido da tabela."""
    papeis = {
        "loads.csv": "possível fato operacional de cargas",
        "trips.csv": "possível fato operacional de viagens",
        "delivery_events.csv": "possível fato de eventos de coleta/entrega",
        "routes.csv": "possível dimensão de rotas",
        "customers.csv": "possível dimensão de clientes",
        "fuel_purchases.csv": "possível fato/transação de abastecimentos",
        "trucks.csv": "possível dimensão de caminhões/frota",
        "drivers.csv": "possível dimensão de motoristas, com dados pessoais",
        "driver_monthly_metrics.csv": "possível tabela agregada mensal por motorista",
        "truck_utilization_metrics.csv": "possível tabela agregada mensal por caminhão",
        "maintenance_records.csv": "possível fato/evento de manutenção",
        "safety_incidents.csv": "possível fato/evento de incidentes",
        "trailers.csv": "possível dimensão de carretas/equipamentos",
        "facilities.csv": "possível dimensão de instalações",
    }
    return papeis.get(nome_tabela, "papel a validar")


def gerar_escopo_principal() -> str:
    """Gera tabela de escopo principal da V1."""
    linhas = []
    for tabela in ESCOPO_PRINCIPAL_V1:
        linhas.append(
            {
                "tabela": tabela,
                "papel provável": papel_tabela(tabela),
                "motivo de entrada na V1": "base provável para fluxo operacional, relacionamentos e visualizações iniciais",
                "riscos ou cuidados": "validar granularidade, chaves, nulos e campos sensíveis antes de tratar",
                "validação humana necessária": "Sim",
            }
        )
    return formatar_tabela(linhas, ["tabela", "papel provável", "motivo de entrada na V1", "riscos ou cuidados", "validação humana necessária"])


def gerar_escopo_complementar() -> str:
    """Gera tabela de escopo complementar/futuro."""
    motivos = {
        "drivers.csv": (
            "contém dados pessoais/identificáveis de motoristas",
            "exposição de dados pessoais e necessidade de regra LGPD",
            "dimensão de motoristas para análises privadas ou controladas",
        ),
        "driver_monthly_metrics.csv": (
            "tabela agregada mensal por motorista, fora do núcleo transacional inicial",
            "risco de duplicar ou misturar métricas agregadas com fatos operacionais",
            "análises mensais de desempenho de motoristas, se aprovado",
        ),
        "truck_utilization_metrics.csv": (
            "tabela agregada mensal por caminhão, fora do núcleo transacional inicial",
            "risco de granularidade entidade + período e agregação incorreta",
            "análises mensais de utilização da frota, se aprovado",
        ),
        "maintenance_records.csv": (
            "manutenção pode entrar como escopo complementar após estabilizar cargas, viagens e frota",
            "risco de custo/manutenção ser interpretado fora da granularidade correta",
            "análise de manutenção, disponibilidade e custos operacionais",
        ),
        "safety_incidents.csv": (
            "dados sensíveis de risco operacional e baixa ocorrência",
            "risco de exposição e interpretação estatística frágil por baixa frequência",
            "análise de segurança operacional em fase futura ou restrita",
        ),
        "trailers.csv": (
            "dimensão complementar de equipamento",
            "risco baixo, mas depende de validação da necessidade no modelo V1",
            "segmentação por tipo/status de carreta",
        ),
        "facilities.csv": (
            "dimensão complementar de instalações",
            "risco baixo, mas depende de validação da necessidade geográfica/operacional",
            "análises por instalação, cidade, estado ou tipo de local",
        ),
    }
    linhas = []
    for tabela in ESCOPO_COMPLEMENTAR_FUTURO:
        motivo, risco, uso = motivos[tabela]
        linhas.append(
            {
                "tabela": tabela,
                "motivo para ficar fora do núcleo inicial ou entrar como complementar": motivo,
                "riscos": risco,
                "possível uso futuro": uso,
                "validação humana necessária": "Sim",
            }
        )
    return formatar_tabela(linhas, ["tabela", "motivo para ficar fora do núcleo inicial ou entrar como complementar", "riscos", "possível uso futuro", "validação humana necessária"])


def gerar_regras_gerais() -> str:
    """Gera regras gerais propostas para tratamento futuro."""
    return """
### 6.1 IDs e chaves

- Manter IDs como texto.
- Não converter IDs para número.
- Preservar zeros à esquerda.
- Não preencher IDs ausentes automaticamente.
- Validar chaves primárias e estrangeiras antes da modelagem.
- Campos aplicáveis: `load_id`, `trip_id`, `customer_id`, `route_id`, `driver_id`, `truck_id`, `trailer_id`, `event_id`, `facility_id`, `maintenance_id`, `incident_id`, `fuel_purchase_id`.

### 6.2 Datas e períodos

- Converter campos de data para tipo data ou data/hora em etapa futura.
- Tratar `month` como período de referência mensal, não como simples categoria.
- Validar formato antes da conversão.
- Não alterar fuso horário sem regra aprovada.
- Campos aplicáveis: `load_date`, `dispatch_date`, `scheduled_datetime`, `actual_datetime`, `purchase_date`, `maintenance_date`, `incident_date`, `contract_start_date`, `hire_date`, `termination_date`, `date_of_birth`, `acquisition_date`, `month`.

### 6.3 Campos financeiros

- Manter como numéricos.
- Formatar como moeda apenas no Power BI.
- Validar moeda.
- Evitar arredondamento prematuro.
- Campos aplicáveis: `revenue`, `fuel_surcharge`, `accessorial_charges`, `annual_revenue_potential`, `total_revenue`, `total_cost`, `maintenance_cost`, `labor_cost`, `parts_cost`, `vehicle_damage_cost`, `cargo_damage_cost`, `claim_amount`.

### 6.4 Percentuais, taxas, índices e escalas

- Validar escala antes de formatar como percentual.
- Diferenciar percentual/taxa operacional de taxa monetária por unidade.
- Não multiplicar por 100 sem aprovação.
- Registrar campos com valores acima de 1 para investigação quando aplicável.
- Campos aplicáveis: `on_time_delivery_rate`, `utilization_rate`, `fuel_surcharge_rate`.
- `base_rate_per_mile` deve ser tratado como taxa monetária por milha, não percentual.
- `price_per_gallon` deve ser tratado como preço unitário, não percentual.

### 6.5 Campos que não devem ser somados diretamente

| campo | agregação preliminar proposta | validação necessária |
| --- | --- | --- |
| `average_mpg` | média ponderada ou validação futura | Sim |
| `average_idle_hours` | média ponderada ou validação futura | Sim |
| `on_time_delivery_rate` | média ponderada ou validação futura | Sim |
| `utilization_rate` | média ponderada ou validação futura | Sim |
| `fuel_surcharge_rate` | média ponderada ou validação futura | Sim |
| `base_rate_per_mile` | média ponderada ou validação futura | Sim |
| `price_per_gallon` | média ponderada ou validação futura | Sim |

### 6.6 Métricas de duração, tempo e quantidade

- Manter como numéricas.
- Documentar unidade.
- Não converter duração em data.
- Validar unidade antes do Power BI.
- Campos aplicáveis: `detention_minutes`, `actual_duration_hours`, `idle_time_hours`, `average_idle_hours`, `downtime_hours`, `labor_hours`, `typical_transit_days`, `credit_terms_days`, `years_experience`.

### 6.7 Campos categóricos, status e códigos

- Manter como texto.
- Padronizar valores apenas se houver inconsistência comprovada.
- Documentar domínio de valores.
- Avaliar criação futura de descrições amigáveis para Power BI.
- Campos aplicáveis: `customer_type`, `primary_freight_type`, `account_status`, `event_type`, `load_type`, `load_status`, `booking_type`, `trip_status`, `employment_status`, `facility_type`, `maintenance_type`, `incident_type`, `status`, `make`, `fuel_type`, `home_terminal`, `location_city`, `location_state`, `origin_city`, `origin_state`, `destination_city`, `destination_state`.

### 6.8 Booleanos e flags

- Manter como booleano.
- Criar descrição amigável apenas em camada final, se aprovado.
- Não tratar como métrica numérica principal.
- Usar para taxas somente com regra documentada.
- Campos aplicáveis: `on_time_flag`, `at_fault_flag`, `injury_flag`, `preventable_flag`.

### 6.9 Dados pessoais, identificáveis e confidenciais

| campo | tipo de risco | recomendação preliminar | impacto no Power BI | validação humana |
| --- | --- | --- | --- | --- |
| `first_name` | dado pessoal | remover, mascarar ou manter em ambiente privado | reduz exposição de pessoas | Sim |
| `last_name` | dado pessoal | remover, mascarar ou manter em ambiente privado | reduz exposição de pessoas | Sim |
| `date_of_birth` | dado pessoal | remover, mascarar ou controlar acesso | reduz risco LGPD | Sim |
| `license_number` | dado pessoal/identificável | remover, mascarar ou controlar acesso | reduz exposição de documento | Sim |
| `vin` | identificador operacional confidencial | remover, mascarar ou restringir | protege ativos/frota | Sim |
| `fuel_card_number` | identificador operacional confidencial | remover, mascarar ou restringir | protege operação financeira | Sim |
| `customer_name` | dado comercial confidencial | anonimizar ou controlar acesso | evita exposição comercial | Sim |
| `description` | texto livre com possível risco | revisar antes de publicar | evita exposição não estruturada | Sim |
| `service_description` | texto livre com possível risco | revisar antes de publicar | evita exposição não estruturada | Sim |
""".strip()


def gerar_nulos_relevantes(tabelas: dict[str, pd.DataFrame]) -> str:
    """Gera tabela de nulos relevantes para validação."""
    linhas = []
    for tabela_nome, coluna, interpretacao in NULOS_RELEVANTES:
        tabela = tabelas.get(tabela_nome)
        if tabela is None or coluna not in tabela.columns:
            continue
        nulos = int(tabela[coluna].isna().sum())
        percentual = (nulos / len(tabela)) * 100 if len(tabela) else 0
        linhas.append(
            {
                "tabela": tabela_nome,
                "coluna": coluna,
                "quantidade de nulos": nulos,
                "percentual de nulos": f"{percentual:.2f}%",
                "interpretação provável": interpretacao,
                "risco de tratamento incorreto": "preencher ou remover automaticamente pode distorcer a leitura operacional",
                "tratamento proposto": "não tratar automaticamente; documentar e validar regra de negócio",
                "validação humana necessária": "Sim",
            }
        )
    return formatar_tabela(linhas, ["tabela", "coluna", "quantidade de nulos", "percentual de nulos", "interpretação provável", "risco de tratamento incorreto", "tratamento proposto", "validação humana necessária"])


def gerar_relacionamentos() -> str:
    """Gera seção de relacionamentos e modelagem preliminar."""
    linhas = []
    for relacao_a, relacao_b, tipo, risco in RELACIONAMENTOS_CANDIDATOS:
        linhas.append(
            {
                "relacionamento candidato": f"`{relacao_a}` ↔ `{relacao_b}`",
                "tipo provável": tipo,
                "risco": risco,
                "impacto no Power BI": "afeta cardinalidade, filtros, duplicação de linhas e agregações",
                "validação necessária": "Sim",
            }
        )
    texto = formatar_tabela(linhas, ["relacionamento candidato", "tipo provável", "risco", "impacto no Power BI", "validação necessária"])
    return (
        f"{texto}\n\n"
        "A cardinalidade observada não deve ser confundida com cardinalidade conceitual. "
        "Tabelas agregadas mensais exigem cuidado com granularidade entidade + período. "
        "Também é necessário evitar duplicar medidas ao juntar tabelas fato com tabelas de eventos."
    )


def gerar_relatorio() -> tuple[int, int]:
    """Gera o relatório da Etapa 02."""
    PASTA_RELATORIOS.mkdir(parents=True, exist_ok=True)
    tabelas, erros = ler_csvs_brutos()
    arquivos_lidos = sorted(tabelas)
    referencia = ler_referencia_etapa_01()

    partes = [
        "# Relatório da Etapa 02 — Plano de Tratamento e Padronização dos Dados",
        "",
        f"Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## 1. Objetivo da etapa",
        "",
        "Esta etapa tem como objetivo transformar as evidências da Etapa 01 em um plano de tratamento, sem alterar os dados. O plano organiza propostas, riscos, exemplos e validações necessárias antes de qualquer transformação futura.",
        "",
        "Python gera evidências. IA interpreta hipóteses. Humano valida decisões.",
        "",
        "## 2. Confirmação de segurança",
        "",
        "- Dados brutos não foram alterados.\n- Nenhuma transformação foi aplicada.\n- Nenhum dado tratado foi criado.\n- Nenhum dado final foi criado.\n- Nenhum KPI final foi criado.\n- Nenhum dashboard foi gerado.\n- Este relatório é apenas um plano para validação humana.",
        "",
        "## 3. Fontes utilizadas",
        "",
        f"- Arquivos CSV lidos em `dados/brutos/`: {', '.join(f'`{arquivo}`' for arquivo in arquivos_lidos) or 'nenhum'}.\n- Relatório de referência: `relatorios/01_relatorio_inspecao_dados.md`.\n- Status da referência: {referencia}\n- Observação: o plano foi criado com base em evidências técnicas, hipóteses interpretativas e validação pendente.",
        "",
        "## 4. Escopo preliminar da V1",
        "",
        "### 4.1 Tabelas candidatas ao escopo principal da V1",
        "",
        gerar_escopo_principal(),
        "",
        "### 4.2 Tabelas candidatas ao escopo complementar ou futuro",
        "",
        gerar_escopo_complementar(),
        "",
        "Nenhuma tabela está sendo excluída nesta etapa. O escopo é apenas uma hipótese para validação humana.",
        "",
        "## 5. Plano de tratamento por tabela e coluna",
        "",
        gerar_plano_por_coluna(tabelas),
        "",
        "## 6. Regras gerais de tratamento propostas",
        "",
        gerar_regras_gerais(),
        "",
        "## 7. Valores ausentes e interpretação de nulos",
        "",
        gerar_nulos_relevantes(tabelas),
        "",
        "## 8. Relacionamentos e modelagem preliminar",
        "",
        gerar_relacionamentos(),
        "",
        "## 9. Entrega prevista para dados tratados",
        "",
        "Arquivos que poderão ser criados futuramente em `dados/tratados/`, sem criação nesta etapa:\n\n- `customers_tratado.csv`;\n- `loads_tratado.csv`;\n- `trips_tratado.csv`;\n- `delivery_events_tratado.csv`;\n- `routes_tratado.csv`;\n- `fuel_purchases_tratado.csv`;\n- `trucks_tratado.csv`.\n\nEsses arquivos representam um núcleo inicial hipotético para V1. As tabelas complementares não estão descartadas; elas podem entrar em fases futuras ou em tratamentos adicionais após validação humana. Os nomes ainda são hipóteses e dependem de aprovação.",
        "",
        "## 10. Entrega prevista para dados finais",
        "",
        "Possíveis arquivos futuros para `dados/finais/`, prontos para Power BI:\n\n- `fato_cargas.csv`;\n- `fato_viagens.csv`;\n- `fato_eventos_entrega.csv`;\n- `fato_abastecimentos.csv`;\n- `dim_clientes.csv`;\n- `dim_rotas.csv`;\n- `dim_caminhoes.csv`;\n- `dim_calendario.csv`.\n\nA camada final da V1 usa um núcleo inicial para reduzir risco e complexidade, mas tabelas complementares podem entrar em fases futuras. A camada final deve remover ou mascarar campos sensíveis e evitar granularidade incorreta.",
        "",
        "## 11. Decisões pendentes antes da Etapa 03",
        "",
        "- Escopo final da V1.\n- Tabelas que entram em `dados/tratados/`.\n- Tabelas que entram em `dados/finais/`.\n- Tratamento de campos pessoais e confidenciais.\n- Tratamento de nulos.\n- Escala de percentuais.\n- Regra de agregação para médias, taxas e preços unitários.\n- Relacionamento e granularidade no modelo.\n- Campos que serão removidos, mascarados ou mantidos.\n- Nomes finais das tabelas para Power BI.",
        "",
        montar_secao_validacao_humana(
            "## 12. Decisão da Etapa 02",
            "Status da Etapa 02:\n\n- [ ] Aprovada\n- [ ] Aprovada com ressalvas\n- [ ] Reprovada para avanço\n\nObservações da validação humana:\n\n- A preencher.",
        ),
        "",
        "## 13. Confirmações finais de segurança",
        "",
        "- Dados brutos não foram alterados.\n- Nenhuma transformação foi aplicada.\n- Nenhum arquivo tratado foi criado.\n- Nenhum arquivo final foi criado.\n- Nenhum KPI final foi criado.\n- Nenhum dashboard foi gerado.\n- Relatório criado apenas como plano de tratamento para validação humana.",
        "",
    ]

    if erros:
        partes.extend(["## Erros de leitura", "", "\n".join(erros), ""])

    escrever_relatorio_preservando_validacao(
        RELATORIO_ETAPA_02,
        "\n".join(partes),
        "## 12. Decisão da Etapa 02",
    )
    return len(tabelas), len(erros)


def main() -> None:
    """Ponto de entrada da Etapa 02."""
    print("Etapa 02 - Plano de Tratamento e Padronização dos Dados")
    print("Nenhuma alteração será feita em dados/brutos/.")
    print("Nenhum arquivo será criado em dados/tratados/ ou dados/finais/.")

    total_lidos, total_erros = gerar_relatorio()

    print("\nArquivos criados ou alterados:")
    print(f"- {RELATORIO_ETAPA_02}")
    print("- scripts/02_plano_tratamento.py")

    print("\nComando para executar o script:")
    print("python scripts/02_plano_tratamento.py")

    print("\nCaminho do relatório gerado:")
    print(RELATORIO_ETAPA_02)

    print("\nResumo da execução:")
    print(f"- Arquivos CSV lidos com sucesso: {total_lidos}")
    print(f"- Arquivos CSV com erro de leitura: {total_erros}")
    print("- Confirmação: nenhum dado bruto foi alterado.")


if __name__ == "__main__":
    main()
