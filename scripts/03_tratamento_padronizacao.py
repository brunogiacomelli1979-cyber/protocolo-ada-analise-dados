"""
Protocolo ADA - Etapa 03: Tratamento e padronizacao

Finalidade:
- Executar apenas tratamentos previamente documentados e aprovados.
- Gerar dados tratados em pasta separada.
- Manter rastreabilidade das transformacoes aplicadas.

Regra principal:
- Os dados brutos nunca devem ser alterados.
"""

from pathlib import Path


PASTA_DADOS_BRUTOS = Path("dados/brutos")
PASTA_DADOS_TRATADOS = Path("dados/tratados")


def preparar_saida() -> None:
    """Garante que a pasta de dados tratados exista para etapas futuras."""
    PASTA_DADOS_TRATADOS.mkdir(parents=True, exist_ok=True)
    print(f"Pasta de saida preparada: {PASTA_DADOS_TRATADOS}")


def main() -> None:
    """Ponto de entrada da etapa de tratamento e padronizacao."""
    print("Etapa 03 - Tratamento e padronizacao")
    print("Executar somente tratamentos aprovados e documentados.")
    print(f"Origem preservada: {PASTA_DADOS_BRUTOS}")
    preparar_saida()


if __name__ == "__main__":
    main()

