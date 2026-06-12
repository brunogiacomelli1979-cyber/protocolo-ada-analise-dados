"""
Protocolo ADA - Etapa 05: Criacao de KPIs

Finalidade:
- Estruturar a etapa futura de definicao de metricas e KPIs.
- Reforcar que KPIs precisam de contexto, regra de calculo e validacao humana.
- Preparar dados finais apenas quando criterios forem aprovados.

Regra principal:
- Nao criar, calcular ou publicar metricas sem aprovacao humana.
"""

from pathlib import Path


PASTA_DADOS_FINAIS = Path("dados/finais")


def orientar_definicao_kpis() -> None:
    """Espaco reservado para definicoes futuras de KPIs aprovados."""
    print("Nenhum KPI foi definido nesta estrutura inicial.")
    print("Cada KPI futuro deve ter nome, objetivo, formula, fonte e aprovacao.")


def main() -> None:
    """Ponto de entrada da etapa de criacao de KPIs."""
    print("Etapa 05 - Criacao de KPIs")
    print(f"Pasta prevista para dados finais: {PASTA_DADOS_FINAIS}")
    orientar_definicao_kpis()


if __name__ == "__main__":
    main()

