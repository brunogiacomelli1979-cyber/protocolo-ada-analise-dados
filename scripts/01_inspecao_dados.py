"""
Protocolo ADA - Etapa 01: Inspeção Segura e Interpretação Inicial dos Dados Brutos

Finalidade:
- Ler arquivos CSV da pasta dados/brutos/.
- Gerar evidências técnicas objetivas com Python.
- Registrar hipóteses iniciais de interpretação para validação humana.
- Gerar um único relatório em relatorios/01_relatorio_inspecao_dados.md.

Regras principais:
- Este script não altera, move, limpa, sobrescreve ou transforma arquivos em dados/brutos/.
- Este script não cria arquivos em dados/tratados/ nem em dados/finais/.
- O relatório contém hipóteses iniciais, nunca decisões finais.
- Amostras de dados são limitadas a no máximo 3 linhas por tabela.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
import warnings

import pandas as pd

from ada_relatorios import (
    escrever_relatorio_preservando_validacao,
    montar_secao_validacao_humana,
)


PASTA_DADOS_BRUTOS = Path("dados/brutos")
PASTA_RELATORIOS = Path("relatorios")
CAMINHO_RELATORIO = PASTA_RELATORIOS / "01_relatorio_inspecao_dados.md"
CAMINHO_SCHEMA = PASTA_DADOS_BRUTOS / "DATABASE_SCHEMA.txt"

RELACIONAMENTOS_ESPERADOS = [
    ("loads.csv", "load_id", "trips.csv", "load_id", "1:N potencial"),
    ("trips.csv", "trip_id", "delivery_events.csv", "trip_id", "1:N potencial"),
    ("customers.csv", "customer_id", "loads.csv", "customer_id", "1:N potencial"),
    ("routes.csv", "route_id", "loads.csv", "route_id", "1:N potencial"),
    ("drivers.csv", "driver_id", "trips.csv", "driver_id", "1:N potencial"),
    ("trucks.csv", "truck_id", "trips.csv", "truck_id", "1:N potencial"),
    ("trailers.csv", "trailer_id", "trips.csv", "trailer_id", "1:N potencial"),
    ("facilities.csv", "facility_id", "delivery_events.csv", "facility_id", "1:N potencial"),
    ("trips.csv", "trip_id", "fuel_purchases.csv", "trip_id", "1:N potencial"),
    ("trucks.csv", "truck_id", "fuel_purchases.csv", "truck_id", "1:N potencial"),
    ("trucks.csv", "truck_id", "maintenance_records.csv", "truck_id", "1:N potencial"),
    ("trips.csv", "trip_id", "safety_incidents.csv", "trip_id", "1:N potencial"),
]


def normalizar_nome(nome: str) -> str:
    """Padroniza nomes para comparação simples."""
    return nome.strip().lower()


def separar_partes(nome: str) -> list[str]:
    """Divide nomes no padrão com sublinhado."""
    return [parte for parte in normalizar_nome(nome).split("_") if parte]


def tentar_ler_csv(caminho_csv: Path) -> tuple[pd.DataFrame | None, str | None]:
    """Tenta ler um CSV sem alterar o arquivo original."""
    codificacoes = ["utf-8", "utf-8-sig", "latin1"]
    ultimo_erro = "Erro não identificado."

    for codificacao in codificacoes:
        try:
            tabela = pd.read_csv(caminho_csv, encoding=codificacao, low_memory=False)
            return tabela, None
        except Exception as erro:  # noqa: BLE001 - erro registrado no relatório
            ultimo_erro = f"{type(erro).__name__}: {erro}"

    return None, ultimo_erro


def formatar_lista(valores: list[str]) -> str:
    """Formata listas para Markdown."""
    if not valores:
        return "Nenhum campo identificado automaticamente."
    return "\n".join(f"- `{valor}`" for valor in valores)


def valor_para_texto(valor: Any) -> str:
    """Converte valores para texto seguro em tabela Markdown."""
    if pd.isna(valor):
        return ""
    return str(valor).replace("\n", " ").replace("|", "\\|")


def formatar_tabela_markdown(linhas: list[dict[str, Any]], colunas: list[str]) -> str:
    """Cria uma tabela Markdown simples."""
    if not linhas:
        return "Sem registros para exibir."

    cabecalho = "| " + " | ".join(colunas) + " |"
    separador = "| " + " | ".join("---" for _ in colunas) + " |"
    corpo = []

    for linha in linhas:
        corpo.append("| " + " | ".join(valor_para_texto(linha.get(coluna, "")) for coluna in colunas) + " |")

    return "\n".join([cabecalho, separador, *corpo])


def amostra_valores(serie: pd.Series, limite: int = 3) -> str:
    """Mostra poucos exemplos distintos para evitar exposição excessiva."""
    valores = [valor_para_texto(valor) for valor in serie.dropna().drop_duplicates().head(limite)]
    return ", ".join(valores) if valores else "Sem exemplos não nulos."


def eh_booleano_por_comportamento(serie: pd.Series) -> bool:
    """Verifica se os valores parecem booleanos."""
    valores = {str(valor).strip().lower() for valor in serie.dropna().unique()[:20]}
    booleanos = {"true", "false", "sim", "não", "nao", "yes", "no", "0", "1"}
    return bool(valores) and valores.issubset(booleanos)


def eh_data_por_comportamento(serie: pd.Series) -> bool:
    """Testa se uma coluna textual parece conter datas."""
    valores = serie.dropna().astype(str).head(200)
    if len(valores) < 3:
        return False

    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            datas = pd.to_datetime(valores, errors="coerce", utc=True, format="mixed")
        return float(datas.notna().mean()) >= 0.8
    except Exception:
        return False


def padrao_texto_observado(serie: pd.Series) -> str:
    """Resume padrões simples de texto."""
    valores = serie.dropna().astype(str).head(200)
    if valores.empty:
        return "Sem valores não nulos."

    tamanho_medio = valores.str.len().mean()
    if eh_data_por_comportamento(serie):
        return "Texto com padrão provável de data."
    if tamanho_medio >= 50:
        return "Texto longo ou campo livre."
    if valores.str.contains("@", regex=False).mean() > 0.5:
        return "Texto com padrão semelhante a e-mail."
    return "Texto curto ou código descritivo."


def eh_id_por_nome(coluna: str) -> bool:
    """Identifica nomes com aparência de identificador."""
    nome = normalizar_nome(coluna)
    return nome == "id" or nome.endswith("_id") or nome in {"codigo", "código", "code"}


def eh_data_por_nome(coluna: str) -> bool:
    """Identifica nomes com aparência de data/hora, sem usar time sozinho."""
    nome = normalizar_nome(coluna)
    partes = separar_partes(coluna)
    return "datetime" in nome or "timestamp" in nome or any(parte in {"date", "data", "hora"} for parte in partes)


def eh_booleano_por_nome(coluna: str) -> bool:
    """Identifica nomes com aparência de flag booleana."""
    nome = normalizar_nome(coluna)
    partes = separar_partes(coluna)
    return nome.endswith("_flag") or nome.startswith("is_") or nome.startswith("has_") or "flag" in partes


def eh_financeiro_por_nome(coluna: str) -> bool:
    """Identifica nomes com aparência financeira."""
    nome = normalizar_nome(coluna)
    partes = separar_partes(coluna)
    termos = {
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
    return "rate_per" in nome or any(parte in termos for parte in partes)


def eh_percentual_ou_taxa_por_nome(coluna: str) -> bool:
    """Identifica nomes com aparência de percentual, taxa ou índice."""
    nome = normalizar_nome(coluna)
    partes = separar_partes(coluna)
    return (
        "rate" in partes
        or "ratio" in partes
        or "percent" in partes
        or "percentage" in partes
        or "score" in partes
        or nome.endswith("_rate")
        or nome.endswith("_ratio")
        or nome.endswith("_percent")
        or nome.endswith("_percentage")
    )


def eh_taxa_monetaria_por_unidade(coluna: str) -> bool:
    """Diferencia taxa monetária por unidade de taxa percentual."""
    nome = normalizar_nome(coluna)
    return "rate_per" in nome or "price_per" in nome or "_per_" in nome


def eh_tempo_por_nome(coluna: str) -> bool:
    """Identifica nomes com aparência de duração ou tempo."""
    nome = normalizar_nome(coluna)
    if nome == "operating_hours":
        return False
    partes = separar_partes(coluna)
    termos = {"duration", "hours", "minutes", "days", "years", "experience"}
    return nome in {"downtime_hours", "idle_time_hours", "average_idle_hours", "detention_minutes"} or any(
        parte in termos for parte in partes
    )


def eh_coluna_categorica_por_nome(coluna: str) -> bool:
    """Identifica nomes que normalmente representam categorias, status ou códigos."""
    nome = normalizar_nome(coluna)
    partes = separar_partes(coluna)
    termos = {
        "type",
        "status",
        "state",
        "city",
        "class",
        "category",
        "location",
        "terminal",
        "hours",
        "make",
        "fuel",
        "event",
        "booking",
    }
    return nome in {"operating_hours", "home_terminal", "current_location"} or any(parte in termos for parte in partes)


def eh_ano_ou_atributo_temporal(coluna: str, serie: pd.Series) -> bool:
    """Identifica anos como atributos temporais, não como métricas."""
    nome = normalizar_nome(coluna)
    if "year" not in separar_partes(coluna):
        return False
    if not pd.api.types.is_numeric_dtype(serie):
        return False
    valores = serie.dropna()
    return not valores.empty and valores.between(1900, 2100).mean() >= 0.8


def eh_coordenada_geografica(coluna: str) -> bool:
    """Identifica latitude e longitude."""
    return normalizar_nome(coluna) in {"latitude", "longitude", "lat", "lon", "lng"}


def eh_codigo_operacional_por_nome(coluna: str) -> bool:
    """Identifica números ou textos que parecem códigos operacionais, não métricas."""
    nome = normalizar_nome(coluna)
    partes = separar_partes(coluna)
    return nome in {"unit_number", "trailer_number"} or "number" in partes


def eh_contagem_por_nome(coluna: str) -> bool:
    """Identifica contagens operacionais."""
    nome = normalizar_nome(coluna)
    partes = separar_partes(coluna)
    return "count" in partes or nome.endswith("_count") or nome.endswith("_events") or nome.endswith("_completed")


def tipo_risco_campo(coluna: str, serie: pd.Series) -> tuple[str, str, str, str]:
    """Classifica risco de privacidade/confidencialidade como hipótese."""
    nome = normalizar_nome(coluna)
    partes = separar_partes(coluna)

    if nome in {"first_name", "last_name", "driver_name", "date_of_birth", "birth"}:
        return ("dado pessoal", "Nome da coluna indica identificação de pessoa.", "Remover, mascarar ou controlar acesso.", "alto")

    if nome == "license_number":
        return ("dado pessoal/identificável", "Nome da coluna indica número de licença individual.", "Remover, mascarar ou controlar acesso.", "alto")

    if nome in {"email", "phone", "cpf", "rg", "address"}:
        return ("dado pessoal", "Nome da coluna indica contato, documento ou endereço.", "Remover de arquivos finais públicos.", "alto")

    if nome in {"customer_name"}:
        return ("dado comercial confidencial", "Nome da coluna indica cliente identificado.", "Avaliar anonimização ou uso controlado.", "médio")

    if nome in {"vin", "fuel_card_number"}:
        return (
            "identificador operacional confidencial",
            "Nome da coluna indica identificador operacional sensível.",
            "Remover, mascarar ou restringir em arquivos finais públicos.",
            "alto",
        )

    if "description" in partes or "notes" in partes or "comment" in partes:
        return (
            "texto livre com possível risco",
            "Campo textual livre pode conter informação sensível não padronizada.",
            "Revisar conteúdo antes de qualquer publicação.",
            "médio",
        )

    if pd.api.types.is_string_dtype(serie) and serie.dropna().astype(str).str.len().mean() > 80:
        return (
            "texto livre com possível risco",
            "Comportamento de texto longo pode carregar informação não estruturada.",
            "Revisar antes de expor em arquivos finais.",
            "baixo",
        )

    return ("sem risco aparente", "Nome e comportamento não sugerem risco direto.", "Sem ação preliminar específica.", "baixo")


def estatisticas_numericas(serie: pd.Series) -> dict[str, Any]:
    """Calcula estatísticas numéricas quando aplicável."""
    if not pd.api.types.is_numeric_dtype(serie):
        return {"min": "", "max": "", "media": "", "mediana": "", "zeros": "", "percentual_zeros": ""}

    serie_sem_nulos = serie.dropna()
    if serie_sem_nulos.empty:
        return {"min": "", "max": "", "media": "", "mediana": "", "zeros": 0, "percentual_zeros": "0.00%"}

    zeros = int((serie_sem_nulos == 0).sum())
    percentual_zeros = (zeros / len(serie)) * 100 if len(serie) else 0

    return {
        "min": round(float(serie_sem_nulos.min()), 4),
        "max": round(float(serie_sem_nulos.max()), 4),
        "media": round(float(serie_sem_nulos.mean()), 4),
        "mediana": round(float(serie_sem_nulos.median()), 4),
        "zeros": zeros,
        "percentual_zeros": f"{percentual_zeros:.2f}%",
    }


def inferir_hipotese_coluna(
    arquivo: str,
    coluna: str,
    serie: pd.Series,
    total_linhas: int,
    colunas_relacionadas: set[str],
) -> tuple[str, str, str, str]:
    """Infere hipótese técnica inicial usando nome, tipo, comportamento e contexto."""
    nome = normalizar_nome(coluna)
    partes = separar_partes(coluna)
    nulos = int(serie.isna().sum())
    unicos = int(serie.nunique(dropna=True))
    percentual_unicos = (unicos / total_linhas) * 100 if total_linhas else 0
    stats = estatisticas_numericas(serie)
    risco, _, _, risco_confianca = tipo_risco_campo(coluna, serie)

    if risco != "sem risco aparente":
        return (f"possível {risco}", "nome/comportamento indica risco de exposição", risco_confianca, "Sim")

    if eh_booleano_por_nome(coluna) or pd.api.types.is_bool_dtype(serie) or eh_booleano_por_comportamento(serie):
        return ("possível booleano", "nome, tipo ou valores sugerem flag/status binário", "alto", "Validar regra de negócio")

    if eh_data_por_nome(coluna) and ("datetime" in nome or "timestamp" in nome):
        return ("possível data/hora", "nome indica data/hora", "alto", "Validar formato e fuso")

    if eh_data_por_nome(coluna) or (pd.api.types.is_string_dtype(serie) and eh_data_por_comportamento(serie)):
        return ("possível data", "nome ou padrão de texto sugere data", "médio", "Validar formato antes de converter")

    if eh_id_por_nome(coluna) and percentual_unicos >= 95:
        return ("possível identificador", "nome e alta cardinalidade sugerem chave", "alto", "Validar se é chave primária")

    if eh_id_por_nome(coluna) or coluna in colunas_relacionadas:
        return ("possível chave estrangeira", "nome ou relação com outras tabelas sugere vínculo", "médio", "Validar relacionamento")

    if eh_codigo_operacional_por_nome(coluna):
        return ("possível código operacional ou número de unidade", "nome sugere número/código de cadastro", "alto", "Não tratar como métrica")

    if eh_ano_ou_atributo_temporal(coluna, serie):
        return ("possível ano/atributo temporal", "nome e valores sugerem ano de cadastro/modelo", "alto", "Validar significado")

    if eh_coordenada_geografica(coluna):
        return ("possível coordenada geográfica", "nome indica latitude/longitude", "alto", "Validar uso geográfico")

    if eh_taxa_monetaria_por_unidade(coluna):
        return ("possível taxa monetária por unidade", "nome indica valor por unidade", "alto", "Não somar diretamente")

    if "average" in partes or "avg" in partes:
        return ("possível média", "nome sugere média operacional ou métrica média", "alto", "Não somar diretamente")

    if eh_percentual_ou_taxa_por_nome(coluna):
        if pd.api.types.is_numeric_dtype(serie) and stats["min"] != "" and 0 <= float(stats["min"]) and float(stats["max"]) <= 1:
            return ("possível percentual em escala decimal", "nome e faixa 0 a 1 sugerem taxa decimal", "médio", "Validar escala")
        if pd.api.types.is_numeric_dtype(serie) and stats["min"] != "" and 0 <= float(stats["min"]) and float(stats["max"]) <= 100:
            return ("possível percentual em escala 0 a 100", "nome e faixa 0 a 100 sugerem percentual", "médio", "Validar escala")
        return ("possível taxa ou índice", "nome sugere taxa, índice ou score", "médio", "Validar significado")

    if eh_financeiro_por_nome(coluna):
        return ("possível valor financeiro", "nome sugere custo, preço, receita, cobrança ou valor", "alto", "Validar moeda e regra")

    if eh_tempo_por_nome(coluna):
        if "average" in partes:
            return ("possível média", "nome sugere média de duração", "alto", "Não somar diretamente")
        if "experience" in partes or "years" in partes:
            return ("possível métrica de duração/experiência em anos", "nome sugere duração ou experiência", "alto", "Validar unidade")
        return ("possível métrica de duração", "nome sugere tempo ou duração", "alto", "Validar unidade")

    if pd.api.types.is_numeric_dtype(serie):
        if eh_contagem_por_nome(coluna):
            return ("possível contagem", "nome sugere quantidade contada", "alto", "Validar unidade")
        if percentual_unicos >= 95 and stats["min"] != "" and float(stats["min"]) >= 0:
            return ("possível identificador operacional confidencial", "número com alta cardinalidade pode ser código operacional", "baixo", "Validar significado")
        if 0 <= float(stats["min"]) and float(stats["max"]) <= 1:
            return ("possível percentual em escala decimal", "faixa numérica entre 0 e 1", "baixo", "Validar escala e significado")
        if 0 <= float(stats["min"]) and float(stats["max"]) <= 100:
            return ("ambíguo / exige validação humana", "faixa numérica entre 0 e 100 pode ter vários significados", "baixo", "Validação humana obrigatória")
        return ("possível quantidade ou métrica contínua", "coluna numérica com variação observada", "médio", "Validar unidade e agregação")

    if pd.api.types.is_string_dtype(serie):
        if eh_coluna_categorica_por_nome(coluna) or unicos <= max(20, int(total_linhas * 0.05)):
            return ("possível categoria/status/código", "nome ou baixa cardinalidade relativa sugere domínio discreto", "médio", "Validar domínio de valores")
        if serie.dropna().astype(str).str.len().mean() >= 50:
            return ("possível texto descritivo", "texto longo ou campo livre", "médio", "Revisar risco de exposição")
        return ("ambíguo / exige validação", "texto com cardinalidade ou padrão insuficiente", "baixo", "Validação humana necessária")

    return ("ambíguo / exige validação", "evidência insuficiente", "baixo", "Validação humana necessária")


def gerar_perfil_colunas(arquivo: str, tabela: pd.DataFrame, colunas_relacionadas: set[str]) -> list[dict[str, Any]]:
    """Gera perfil técnico por coluna."""
    total_linhas = len(tabela)
    perfis = []

    for coluna in tabela.columns:
        serie = tabela[coluna]
        nulos = int(serie.isna().sum())
        percentual_nulos = (nulos / total_linhas) * 100 if total_linhas else 0
        unicos = int(serie.nunique(dropna=True))
        percentual_unicos = (unicos / total_linhas) * 100 if total_linhas else 0
        stats = estatisticas_numericas(serie)

        if pd.api.types.is_numeric_dtype(serie):
            padrao = "Numérico"
        else:
            padrao = padrao_texto_observado(serie)

        hipotese, evidencia, confianca, validacao = inferir_hipotese_coluna(
            arquivo, coluna, serie, total_linhas, colunas_relacionadas
        )

        perfis.append(
            {
                "coluna": coluna,
                "tipo_pandas": str(serie.dtype),
                "nulos": nulos,
                "percentual_nulos": f"{percentual_nulos:.2f}%",
                "unicos": unicos,
                "percentual_unicos": f"{percentual_unicos:.2f}%",
                "exemplos": amostra_valores(serie),
                "minimo": stats["min"],
                "maximo": stats["max"],
                "media": stats["media"],
                "mediana": stats["mediana"],
                "zeros": stats["zeros"],
                "percentual_zeros": stats["percentual_zeros"],
                "padrao": padrao,
                "hipotese": hipotese,
                "evidencia": evidencia,
                "confianca": confianca,
                "validacao": validacao,
            }
        )

    return perfis


def colunas_em_relacionamentos(tabelas: dict[str, pd.DataFrame]) -> set[str]:
    """Identifica colunas que aparecem com o mesmo nome em mais de uma tabela."""
    aparicoes: dict[str, int] = {}
    for tabela in tabelas.values():
        for coluna in tabela.columns:
            if eh_id_por_nome(coluna):
                aparicoes[coluna] = aparicoes.get(coluna, 0) + 1
    return {coluna for coluna, quantidade in aparicoes.items() if quantidade > 1}


def papel_provavel_tabela(arquivo: str, perfil: dict[str, Any]) -> tuple[str, str, str]:
    """Classifica o papel provável da tabela com regras hierárquicas e conservadoras."""
    linhas = perfil["linhas"]
    datas = perfil["datas"]
    ids = perfil["ids"]
    numericos = len(perfil["numericos"])
    categorias = len(perfil["categoricos"])
    colunas = [normalizar_nome(coluna) for coluna in perfil["colunas"]]
    nome = normalizar_nome(arquivo)
    metricas_agregadas = [
        coluna
        for coluna in colunas
        if any(termo in coluna for termo in ["total", "average", "rate", "utilization", "completed"])
    ]

    evidencias = []
    if linhas >= 10000:
        evidencias.append("muitas linhas")
    if datas:
        evidencias.append("presença de data")
    if len(ids) >= 2:
        evidencias.append("presença de IDs externos")
    if ids:
        evidencias.append("chave identificadora provável")
    if numericos:
        evidencias.append("métricas numéricas")
    if metricas_agregadas:
        evidencias.append("métricas consolidadas ou derivadas")
    if categorias:
        evidencias.append("atributos categóricos")

    tem_periodo = any(coluna in {"month", "period", "competencia", "reference_date"} for coluna in colunas)
    tem_chave_propria = bool(perfil["possivel_chave_primaria"])
    tem_data_evento = any(
        coluna
        for coluna in colunas
        if coluna.endswith("_date")
        or coluna.endswith("_datetime")
        or coluna in {"purchase_date", "load_date", "dispatch_date", "incident_datetime", "event_datetime"}
    )

    if tem_periodo and len(metricas_agregadas) >= 2:
        if "driver" in nome:
            return ("possível tabela agregada mensal por motorista", ", ".join(evidencias), "alto")
        if "truck" in nome:
            return ("possível tabela agregada mensal por caminhão", ", ".join(evidencias), "alto")
        return ("possível tabela agregada", ", ".join(evidencias), "alto")

    if ("event" in nome or "incident" in nome or "maintenance" in nome) and tem_data_evento and len(ids) >= 2:
        if "delivery_events" in nome:
            return ("possível tabela de eventos", ", ".join(evidencias), "alto")
        if "maintenance" in nome:
            return ("possível tabela fato/evento de manutenção", ", ".join(evidencias), "alto")
        if "incident" in nome:
            return ("possível tabela fato/evento de incidentes", ", ".join(evidencias), "alto")
        return ("possível tabela de eventos", ", ".join(evidencias), "alto")

    if linhas >= 10000 and tem_chave_propria and len(ids) >= 2 and tem_data_evento and numericos:
        if "fuel" in nome:
            return ("possível tabela fato/transacional de abastecimentos", ", ".join(evidencias), "alto")
        return ("possível tabela fato operacional", ", ".join(evidencias), "alto")

    if tem_chave_propria and categorias and linhas <= 10000:
        if "customer" in nome:
            return ("possível dimensão de clientes", ", ".join(evidencias), "alto")
        if "driver" in nome:
            return ("possível dimensão de motoristas, com dados pessoais", ", ".join(evidencias), "alto")
        if "truck" in nome:
            return ("possível dimensão de caminhões/frota", ", ".join(evidencias), "alto")
        if "trailer" in nome:
            return ("possível dimensão de carretas/equipamentos", ", ".join(evidencias), "alto")
        if "facilities" in nome or "facility" in nome:
            return ("possível dimensão de instalações", ", ".join(evidencias), "alto")
        if "routes" in nome or "route" in nome:
            return ("possível dimensão de rotas", ", ".join(evidencias), "alto")
        return ("possível dimensão", ", ".join(evidencias), "médio")

    if tem_chave_propria and linhas <= 10000:
        return ("possível dimensão", ", ".join(evidencias), "médio")

    if tem_data_evento and len(ids) >= 2 and numericos:
        return ("possível tabela fato operacional", ", ".join(evidencias), "médio")

    return ("apoio ou referência operacional", ", ".join(evidencias) or "evidência limitada", "baixo")


def identificar_colunas_basicas(tabela: pd.DataFrame) -> dict[str, list[str]]:
    """Lista categorias iniciais de colunas para inspeção por arquivo."""
    booleanos = [
        coluna
        for coluna in tabela.columns
        if eh_booleano_por_nome(coluna) or pd.api.types.is_bool_dtype(tabela[coluna]) or eh_booleano_por_comportamento(tabela[coluna])
    ]

    return {
        "ids": [coluna for coluna in tabela.columns if eh_id_por_nome(coluna)],
        "datas": [coluna for coluna in tabela.columns if eh_data_por_nome(coluna)],
        "numericos": [
            coluna
            for coluna in tabela.columns
            if pd.api.types.is_numeric_dtype(tabela[coluna])
            and coluna not in booleanos
            and not eh_codigo_operacional_por_nome(coluna)
            and not eh_ano_ou_atributo_temporal(coluna, tabela[coluna])
            and not eh_coordenada_geografica(coluna)
        ],
        "categoricos": [
            coluna
            for coluna in tabela.columns
            if pd.api.types.is_string_dtype(tabela[coluna])
            and not eh_id_por_nome(coluna)
            and tipo_risco_campo(coluna, tabela[coluna])[0] == "sem risco aparente"
            and (
                eh_coluna_categorica_por_nome(coluna)
                or tabela[coluna].nunique(dropna=True) <= max(20, int(len(tabela) * 0.05))
            )
        ],
        "booleanos": booleanos,
        "financeiros": [coluna for coluna in tabela.columns if eh_financeiro_por_nome(coluna)],
        "percentuais_taxas": [coluna for coluna in tabela.columns if eh_percentual_ou_taxa_por_nome(coluna)],
        "tempo": [coluna for coluna in tabela.columns if eh_tempo_por_nome(coluna)],
    }


def identificar_cuidados_agregacao(arquivo: str, tabela: pd.DataFrame) -> list[dict[str, Any]]:
    """Identifica campos que não devem ser somados automaticamente."""
    cuidados = []

    for coluna in tabela.columns:
        nome = normalizar_nome(coluna)
        partes = separar_partes(coluna)
        motivo = ""
        sugestao = "validação futura"
        confianca = "baixo"

        if "average" in partes or "avg" in partes:
            motivo = "média operacional; soma direta distorce interpretação"
            sugestao = "média ponderada"
            confianca = "alto"
        elif eh_taxa_monetaria_por_unidade(coluna):
            motivo = "taxa monetária por unidade ou preço unitário"
            sugestao = "média ponderada"
            confianca = "alto"
        elif eh_percentual_ou_taxa_por_nome(coluna):
            motivo = "percentual, taxa, índice ou score"
            sugestao = "média ponderada"
            confianca = "alto"
        elif "score" in partes or "index" in partes:
            motivo = "score ou índice"
            sugestao = "não agregar"
            confianca = "médio"
        elif nome.endswith("_status") or "status" in partes:
            motivo = "status codificado ou categoria operacional"
            sugestao = "contagem"
            confianca = "médio"

        if motivo:
            cuidados.append(
                {
                    "Tabela": arquivo,
                    "Coluna": coluna,
                    "Motivo do cuidado": motivo,
                    "Agregação preliminar sugerida": sugestao,
                    "Nível de confiança": confianca,
                    "Validação humana necessária": "Sim",
                }
            )

    return cuidados


def gerar_amostra_controlada(tabela: pd.DataFrame) -> str:
    """Gera amostra limitada a 3 linhas por tabela."""
    linhas = tabela.head(3).fillna("").to_dict(orient="records")
    return formatar_tabela_markdown(linhas, list(tabela.columns))


def obter_info_schema() -> dict[str, Any]:
    """Registra a existência do DATABASE_SCHEMA.txt sem usar como fonte única."""
    if not CAMINHO_SCHEMA.exists():
        return {"existe": False, "nome": "DATABASE_SCHEMA.txt", "linhas": 0, "caracteres": 0, "erro": ""}

    try:
        conteudo = CAMINHO_SCHEMA.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        conteudo = CAMINHO_SCHEMA.read_text(encoding="latin1")
    except Exception as erro:  # noqa: BLE001
        return {"existe": True, "nome": CAMINHO_SCHEMA.name, "linhas": 0, "caracteres": 0, "erro": str(erro)}

    return {
        "existe": True,
        "nome": CAMINHO_SCHEMA.name,
        "linhas": len(conteudo.splitlines()),
        "caracteres": len(conteudo),
        "erro": "",
    }


def gerar_secao_schema(info: dict[str, Any]) -> str:
    """Gera texto da documentação da base."""
    if not info["existe"]:
        return "O arquivo `DATABASE_SCHEMA.txt` não foi encontrado em `dados/brutos/`."
    if info["erro"]:
        return f"- Nome do arquivo: `{info['nome']}`\n- Erro de leitura: `{info['erro']}`"
    return (
        f"- Nome do arquivo: `{info['nome']}`\n"
        f"- Quantidade de linhas: {info['linhas']}\n"
        f"- Quantidade de caracteres: {info['caracteres']}\n"
        "- Observação: este arquivo será usado apenas como apoio, não como fonte única de decisão."
    )


def gerar_inventario(perfis_tabelas: dict[str, dict[str, Any]]) -> str:
    """Gera inventário dos arquivos brutos com evidências."""
    linhas = []

    for arquivo, perfil in sorted(perfis_tabelas.items()):
        papel, evidencias, confianca = papel_provavel_tabela(arquivo, perfil)
        chave = perfil["possivel_chave_primaria"]
        unicos_chave = perfil["unicos_chave"] if chave else "Não identificada"
        linhas.append(
            {
                "Arquivo": arquivo,
                "Linhas": perfil["linhas"],
                "Colunas": perfil["colunas_qtd"],
                "Registros únicos por possível chave": unicos_chave,
                "Papel provável na base": papel,
                "Evidências usadas": evidencias,
                "Nível de confiança": confianca,
                "Observação inicial": "Hipótese inicial; requer validação humana.",
            }
        )

    return formatar_tabela_markdown(
        linhas,
        [
            "Arquivo",
            "Linhas",
            "Colunas",
            "Registros únicos por possível chave",
            "Papel provável na base",
            "Evidências usadas",
            "Nível de confiança",
            "Observação inicial",
        ],
    )


def gerar_secao_inspecao_arquivo(arquivo: str, tabela: pd.DataFrame, categorias: dict[str, list[str]]) -> str:
    """Gera inspeção técnica resumida por arquivo."""
    tipos = [{"Coluna": coluna, "Tipo pandas": str(tipo)} for coluna, tipo in tabela.dtypes.items()]
    nulos = []

    for coluna in tabela.columns:
        qtd_nulos = int(tabela[coluna].isna().sum())
        pct_nulos = (qtd_nulos / len(tabela)) * 100 if len(tabela) else 0
        nulos.append({"Coluna": coluna, "Valores nulos": qtd_nulos, "Percentual de nulos": f"{pct_nulos:.2f}%"})

    return f"""
### Arquivo: `{arquivo}`

**Quantidade de linhas:** {len(tabela)}

**Quantidade de colunas:** {len(tabela.columns)}

**Lista de colunas:**

{formatar_lista(list(tabela.columns))}

**Tipos pandas:**

{formatar_tabela_markdown(tipos, ["Coluna", "Tipo pandas"])}

**Valores nulos por coluna:**

{formatar_tabela_markdown(nulos, ["Coluna", "Valores nulos", "Percentual de nulos"])}

**Quantidade de linhas duplicadas:** {int(tabela.duplicated().sum())}

**Possíveis IDs:** {", ".join(categorias["ids"]) or "nenhum identificado automaticamente"}

**Possíveis datas:** {", ".join(categorias["datas"]) or "nenhuma identificada automaticamente"}

**Possíveis campos numéricos:** {", ".join(categorias["numericos"]) or "nenhum identificado automaticamente"}

**Possíveis campos categóricos:** {", ".join(categorias["categoricos"]) or "nenhum identificado automaticamente"}

**Possíveis booleanos:** {", ".join(categorias["booleanos"]) or "nenhum identificado automaticamente"}

**Possíveis financeiros:** {", ".join(categorias["financeiros"]) or "nenhum identificado automaticamente"}

**Possíveis percentuais ou taxas:** {", ".join(categorias["percentuais_taxas"]) or "nenhum identificado automaticamente"}

**Possíveis métricas de tempo/duração:** {", ".join(categorias["tempo"]) or "nenhuma identificada automaticamente"}

**Amostra controlada de até 3 linhas:**

{gerar_amostra_controlada(tabela)}
""".strip()


def gerar_secao_perfil_colunas(perfis_colunas: dict[str, list[dict[str, Any]]]) -> str:
    """Gera perfil técnico detalhado por coluna."""
    partes = []
    colunas = [
        "coluna",
        "tipo_pandas",
        "nulos",
        "percentual_nulos",
        "unicos",
        "percentual_unicos",
        "exemplos",
        "minimo",
        "maximo",
        "media",
        "mediana",
        "zeros",
        "percentual_zeros",
        "padrao",
        "hipotese",
        "confianca",
        "validacao",
    ]

    for arquivo, perfis in sorted(perfis_colunas.items()):
        partes.append(f"### `{arquivo}`\n\n{formatar_tabela_markdown(perfis, colunas)}")

    return "\n\n".join(partes)


def regras_interpretacao() -> str:
    """Explica regras usadas pelo agente."""
    return """
1. Uma coluna com alta cardinalidade, muitos valores únicos e valores repetidos raramente pode ser possível identificador.
2. Uma coluna com valores somente `True/False`, `0/1`, `sim/não`, `yes/no` ou equivalentes pode ser possível booleano.
3. Uma coluna numérica com valores entre 0 e 1 pode ser percentual, taxa, score ou índice em escala decimal, mas exige validação humana.
4. Uma coluna numérica com valores entre 0 e 100 pode ser percentual em escala 0 a 100, quantidade, nota ou métrica operacional, exigindo validação humana.
5. Uma coluna numérica positiva com casas decimais e grande variação pode ser valor financeiro, métrica contínua, preço, custo, receita ou medida operacional.
6. Uma coluna com poucos valores únicos e muitos registros pode ser categoria, status ou código.
7. Uma coluna textual longa pode ser descrição, observação ou campo livre.
8. Uma coluna com padrões de data em texto deve ser candidata a data, mesmo que o nome da coluna não indique data.
9. Uma coluna com números inteiros sequenciais pode ser identificador, código operacional ou número de unidade, não necessariamente métrica.
10. Campos com comportamento de média, taxa, percentual, preço unitário ou índice não devem ser somados diretamente.
11. Nomes de colunas devem ser tratados apenas como pistas auxiliares.
12. Quando comportamento dos dados e nomenclatura divergirem, o relatório registra conflito e pede validação humana.
""".strip()


def cardinalidade_observada(tabela_a: pd.DataFrame, coluna_a: str, tabela_b: pd.DataFrame, coluna_b: str) -> str:
    """Infere cardinalidade observada, sem concluir cardinalidade conceitual."""
    dup_a = tabela_a[coluna_a].dropna().duplicated().any()
    dup_b = tabela_b[coluna_b].dropna().duplicated().any()
    if not dup_a and not dup_b:
        return "1:1 observado"
    if not dup_a and dup_b:
        return "1:N observado"
    if dup_a and not dup_b:
        return "N:1 observado"
    return "N:N observado"


def eh_tabela_agregada_mensal(arquivo: str, tabela: pd.DataFrame) -> bool:
    """Identifica tabelas agregadas por entidade e período."""
    nome = normalizar_nome(arquivo)
    return ("monthly" in nome or "metrics" in nome or "utilization" in nome) and "month" in tabela.columns


def gerar_relacionamentos(tabelas: dict[str, pd.DataFrame]) -> str:
    """Infere relações potenciais entre tabelas usando nomes e interseção de valores."""
    linhas = []
    pares = list(RELACIONAMENTOS_ESPERADOS)
    vistos = {(a, ca, b, cb) for a, ca, b, cb, _ in pares}

    arquivos = sorted(tabelas)
    for i, arquivo_a in enumerate(arquivos):
        for arquivo_b in arquivos[i + 1 :]:
            colunas_comuns = set(tabelas[arquivo_a].columns).intersection(tabelas[arquivo_b].columns)
            for coluna in sorted(colunas_comuns):
                if not eh_id_por_nome(coluna):
                    continue
                par = (arquivo_a, coluna, arquivo_b, coluna)
                if par not in vistos:
                    if eh_tabela_agregada_mensal(arquivo_a, tabelas[arquivo_a]) or eh_tabela_agregada_mensal(arquivo_b, tabelas[arquivo_b]):
                        cardinalidade = "N:1 potencial com granularidade entidade + período; exige cuidado"
                    else:
                        cardinalidade = "cardinalidade conceitual exige validação"
                    pares.append((arquivo_a, coluna, arquivo_b, coluna, cardinalidade))
                    vistos.add(par)

    for arquivo_a, coluna_a, arquivo_b, coluna_b, cardinalidade_conceitual in pares:
        if arquivo_a not in tabelas or arquivo_b not in tabelas or coluna_a not in tabelas[arquivo_a] or coluna_b not in tabelas[arquivo_b]:
            continue

        tabela_a = tabelas[arquivo_a]
        tabela_b = tabelas[arquivo_b]
        valores_a = set(tabela_a[coluna_a].dropna().unique())
        valores_b = set(tabela_b[coluna_b].dropna().unique())
        intersecao = valores_a.intersection(valores_b)
        cobertura_a = (len(intersecao) / len(valores_a)) * 100 if valores_a else 0
        cobertura_b = (len(intersecao) / len(valores_b)) * 100 if valores_b else 0
        orfaos_a = len(valores_a - valores_b)
        orfaos_b = len(valores_b - valores_a)
        confianca = "alto" if cobertura_a >= 90 or cobertura_b >= 90 else "médio" if cobertura_a >= 50 or cobertura_b >= 50 else "baixo"

        cardinalidade_obs = cardinalidade_observada(tabela_a, coluna_a, tabela_b, coluna_b)
        observacao = "Hipótese de modelagem; cardinalidade observada não é verdade conceitual definitiva."

        if eh_tabela_agregada_mensal(arquivo_a, tabela_a) or eh_tabela_agregada_mensal(arquivo_b, tabela_b):
            if cardinalidade_obs == "N:N observado":
                cardinalidade_obs = "repetição observada por entidade + período"
            observacao = (
                "Tabela agregada mensal detectada; a relação com dimensão tende a ser N:1 por entidade, "
                "mas a granularidade entidade + período exige cuidado."
            )

        linhas.append(
            {
                "Relação hipotética": f"{arquivo_a}.{coluna_a} ↔ {arquivo_b}.{coluna_b}",
                "Chaves distintas A": len(valores_a),
                "Chaves distintas B": len(valores_b),
                "Cobertura percentual": f"A→B {cobertura_a:.2f}% / B→A {cobertura_b:.2f}%",
                "IDs órfãos": f"A sem B: {orfaos_a}; B sem A: {orfaos_b}",
                "Cardinalidade observada": cardinalidade_obs,
                "Cardinalidade conceitual provável": cardinalidade_conceitual,
                "Nível de confiança": confianca,
                "Observação": observacao,
            }
        )

    return formatar_tabela_markdown(
        linhas,
        [
            "Relação hipotética",
            "Chaves distintas A",
            "Chaves distintas B",
            "Cobertura percentual",
            "IDs órfãos",
            "Cardinalidade observada",
            "Cardinalidade conceitual provável",
            "Nível de confiança",
            "Observação",
        ],
    )


def gerar_campos_agregacao(cuidados: list[dict[str, Any]]) -> str:
    """Gera seção de campos que exigem cuidado de agregação."""
    return formatar_tabela_markdown(
        cuidados,
        [
            "Tabela",
            "Coluna",
            "Motivo do cuidado",
            "Agregação preliminar sugerida",
            "Nível de confiança",
            "Validação humana necessária",
        ],
    )


def gerar_campos_risco(tabelas: dict[str, pd.DataFrame]) -> str:
    """Gera seção de campos pessoais, identificáveis ou confidenciais."""
    linhas = []

    for arquivo, tabela in sorted(tabelas.items()):
        for coluna in tabela.columns:
            risco, evidencia, recomendacao, confianca = tipo_risco_campo(coluna, tabela[coluna])
            if risco == "sem risco aparente":
                continue
            linhas.append(
                {
                    "Tabela": arquivo,
                    "Coluna": coluna,
                    "Tipo de risco": risco,
                    "Evidência": evidencia,
                    "Recomendação preliminar para arquivos finais públicos": recomendacao,
                    "Nível de confiança": confianca,
                    "Validação humana necessária": "Sim",
                }
            )

    return formatar_tabela_markdown(
        linhas,
        [
            "Tabela",
            "Coluna",
            "Tipo de risco",
            "Evidência",
            "Recomendação preliminar para arquivos finais públicos",
            "Nível de confiança",
            "Validação humana necessária",
        ],
    )


def gerar_entrega_dados(perfis_tabelas: dict[str, dict[str, Any]]) -> str:
    """Descreve hipóteses de entrega futura, sem criar arquivos."""
    principais = []
    complementares = []
    futuras = []
    cuidado = []

    for arquivo, perfil in sorted(perfis_tabelas.items()):
        papel, _, _ = papel_provavel_tabela(arquivo, perfil)
        if perfil["riscos"] or "agregada" in papel:
            cuidado.append(arquivo)
        elif "fato" in papel or "eventos" in papel:
            principais.append(arquivo)
        elif "dimensão" in papel:
            complementares.append(arquivo)
        else:
            futuras.append(arquivo)

    return f"""
### 11.1 Dados tratados

`dados/tratados/` deverá conter tabelas limpas e documentadas, com:

- tipos padronizados;
- datas convertidas;
- IDs preservados como texto;
- campos pessoais removidos, mascarados ou controlados quando necessário;
- nulos tratados ou documentados;
- sem alteração dos dados brutos.

### 11.2 Dados finais

`dados/finais/` deverá conter bases prontas para Power BI, como:

- tabelas fato e dimensão selecionadas;
- tabelas agregadas de KPIs, quando aprovadas;
- campos de data prontos para ordenação;
- campos percentuais em escala correta;
- campos de status descritivos quando aprovados;
- campos sensíveis removidos ou mascarados para uso público.

### 11.3 Escopo sugerido para V1

Esta sugestão é uma hipótese inicial baseada nas evidências observadas, não apenas nos nomes das tabelas.

**Tabelas candidatas ao escopo principal:**

{formatar_lista(principais)}

**Tabelas candidatas ao escopo complementar:**

{formatar_lista(complementares)}

**Tabelas candidatas a fase futura:**

{formatar_lista(futuras)}

**Tabelas que exigem cuidado por conter dados pessoais, confidenciais ou agregados:**

{formatar_lista(cuidado)}
""".strip()


def pontos_criticos() -> str:
    """Lista pontos críticos antes do plano de tratamento."""
    return """
- confirmação do escopo da V1;
- tratamento de dados pessoais e confidenciais;
- validação de escala de percentuais, taxas, índices e scores;
- separação entre taxa percentual e taxa monetária por unidade;
- campos que não devem ser somados diretamente;
- nulos em IDs operacionais;
- significado de campos nulos relevantes;
- validação de relacionamentos observados;
- diferença entre cardinalidade observada e cardinalidade conceitual;
- definição de quais campos entram nos arquivos finais públicos;
- validação humana das hipóteses com baixa ou média confiança.
""".strip()


def recomendacoes_iniciais() -> str:
    """Gera recomendações como hipóteses iniciais."""
    return """
- IDs devem ser tratados como texto.
- Datas devem ser convertidas em etapa futura.
- Campos financeiros devem permanecer numéricos e ser formatados como moeda no Power BI.
- Percentuais e taxas precisam de validação de escala.
- Taxas monetárias por unidade não devem ser confundidas com percentuais.
- Métricas de tempo devem permanecer numéricas, com unidade documentada.
- Campos pessoais e confidenciais não devem ir para arquivos finais públicos sem aprovação.
- Campos médios, percentuais, índices e preços unitários não devem ser somados diretamente.
- Dados brutos devem permanecer preservados.
- Power BI deve receber dados finais já tratados, documentados e aprovados.
""".strip()


def validacao_humana() -> str:
    """Lista decisões que dependem de aprovação humana."""
    return """
- aprovar ou ajustar o escopo da V1;
- confirmar quais tabelas serão usadas no primeiro ciclo analítico;
- confirmar significado de colunas ambíguas;
- validar colunas cujo comportamento estatístico e nome não sejam suficientes;
- definir regras de tratamento para dados pessoais, identificáveis ou confidenciais;
- confirmar escala correta de percentuais e taxas;
- definir tratamento para valores ausentes;
- validar regras para campos de status e flags operacionais;
- confirmar relacionamentos entre tabelas;
- definir quais campos podem entrar em arquivos finais públicos;
- aprovar qualquer transformação antes de sua execução.
""".strip()


def decisao_etapa() -> str:
    """Cria espaço para decisão manual posterior."""
    return """
Status da Etapa 01:

- [ ] Aprovada
- [ ] Aprovada com ressalvas
- [ ] Reprovada para avanço

Observações da validação humana:

- A preencher.
""".strip()


def confirmacao_seguranca() -> str:
    """Declara confirmações de segurança."""
    return """
- Dados brutos não foram alterados.
- Nenhuma transformação foi aplicada.
- Nenhum dado tratado foi criado.
- Nenhum KPI final foi criado.
- Nenhum dashboard foi gerado.
- As classificações são hipóteses iniciais.
- Nenhuma decisão de tratamento foi tomada.
""".strip()


def preparar_evidencias() -> tuple[dict[str, pd.DataFrame], dict[str, dict[str, Any]], dict[str, list[dict[str, Any]]], list[str]]:
    """Lê os CSVs e prepara evidências para o relatório."""
    tabelas: dict[str, pd.DataFrame] = {}
    erros: list[str] = []

    for caminho_csv in sorted(PASTA_DADOS_BRUTOS.glob("*.csv")):
        tabela, erro = tentar_ler_csv(caminho_csv)
        if erro or tabela is None:
            erros.append(f"- `{caminho_csv.name}`: `{erro}`")
        else:
            tabelas[caminho_csv.name] = tabela

    colunas_relacionadas = colunas_em_relacionamentos(tabelas)
    perfis_colunas: dict[str, list[dict[str, Any]]] = {}
    perfis_tabelas: dict[str, dict[str, Any]] = {}

    for arquivo, tabela in tabelas.items():
        categorias = identificar_colunas_basicas(tabela)
        cuidados = identificar_cuidados_agregacao(arquivo, tabela)
        riscos = [
            coluna
            for coluna in tabela.columns
            if tipo_risco_campo(coluna, tabela[coluna])[0] != "sem risco aparente"
        ]
        chave = next((coluna for coluna in categorias["ids"] if tabela[coluna].nunique(dropna=True) == len(tabela)), "")
        perfis_colunas[arquivo] = gerar_perfil_colunas(arquivo, tabela, colunas_relacionadas)
        perfis_tabelas[arquivo] = {
            "linhas": len(tabela),
            "colunas_qtd": len(tabela.columns),
            "colunas": list(tabela.columns),
            "possivel_chave_primaria": chave,
            "unicos_chave": tabela[chave].nunique(dropna=True) if chave else "",
            "cuidados_agregacao": cuidados,
            "riscos": riscos,
            **categorias,
        }

    return tabelas, perfis_tabelas, perfis_colunas, erros


def gerar_relatorio() -> tuple[int, int]:
    """Gera o relatório único da Etapa 01."""
    PASTA_RELATORIOS.mkdir(parents=True, exist_ok=True)
    tabelas, perfis_tabelas, perfis_colunas, erros = preparar_evidencias()

    secoes_inspecao = []
    cuidados_agregacao = []
    for arquivo, tabela in sorted(tabelas.items()):
        categorias = identificar_colunas_basicas(tabela)
        secoes_inspecao.append(gerar_secao_inspecao_arquivo(arquivo, tabela, categorias))
        cuidados_agregacao.extend(identificar_cuidados_agregacao(arquivo, tabela))

    partes = [
        "# Relatório da Etapa 01 — Inspeção Segura e Interpretação Inicial dos Dados Brutos",
        "",
        f"Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## 1. Objetivo da etapa",
        "",
        (
            "Esta etapa tem como objetivo compreender a estrutura técnica dos dados brutos, gerar evidências objetivas "
            "com Python, apoiar a interpretação com IA e preparar a base para validação humana antes do plano de tratamento."
        ),
        "",
        "Python gera evidências. IA interpreta hipóteses. Humano valida decisões.",
        "",
        "## 2. Confirmação de segurança",
        "",
        confirmacao_seguranca(),
        "",
        "## 3. Documentação da base",
        "",
        gerar_secao_schema(obter_info_schema()),
        "",
        "## 4. Inventário dos arquivos brutos",
        "",
        gerar_inventario(perfis_tabelas),
        "",
        "## 5. Inspeção técnica por arquivo",
        "",
        "\n\n".join(secoes_inspecao) if secoes_inspecao else "Nenhum CSV foi inspecionado com sucesso.",
        "",
        "## Erros de leitura",
        "",
        "\n".join(erros) if erros else "Nenhum erro de leitura foi registrado.",
        "",
        "## 6. Perfil técnico das colunas",
        "",
        gerar_secao_perfil_colunas(perfis_colunas),
        "",
        "## 7. Regras de interpretação por comportamento dos dados",
        "",
        regras_interpretacao(),
        "",
        "## 8. Leitura inicial dos relacionamentos",
        "",
        gerar_relacionamentos(tabelas),
        "",
        "## 9. Campos que exigem cuidado de agregação",
        "",
        gerar_campos_agregacao(cuidados_agregacao),
        "",
        "## 10. Campos pessoais, identificáveis ou confidenciais",
        "",
        gerar_campos_risco(tabelas),
        "",
        "## 11. Leitura de entrega dos dados para próximas etapas",
        "",
        gerar_entrega_dados(perfis_tabelas),
        "",
        "## 12. Pontos críticos antes do plano de tratamento",
        "",
        pontos_criticos(),
        "",
        "## 13. Recomendações iniciais do Agente ADA",
        "",
        "As recomendações abaixo são hipóteses iniciais e dependem de validação humana.",
        "",
        recomendacoes_iniciais(),
        "",
        "## 14. Validação humana necessária",
        "",
        validacao_humana(),
        "",
        montar_secao_validacao_humana("## 15. Decisão da Etapa 01", decisao_etapa()),
        "",
    ]

    escrever_relatorio_preservando_validacao(
        CAMINHO_RELATORIO,
        "\n".join(partes),
        "## 15. Decisão da Etapa 01",
    )
    return len(tabelas), len(erros)


def main() -> None:
    """Ponto de entrada da inspeção segura."""
    print("Etapa 01 - Inspeção Segura e Interpretação Inicial dos Dados Brutos")
    print("Nenhuma alteração será feita em dados/brutos/.")
    print("Nenhum arquivo será criado em dados/tratados/ ou dados/finais/.")

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
