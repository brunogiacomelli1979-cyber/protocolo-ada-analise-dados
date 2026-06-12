"""
Protocolo ADA - Etapa 01: Inspecao dos dados

Finalidade:
- Registrar uma inspecao inicial dos arquivos recebidos.
- Avaliar estrutura, formatos, colunas, volumes e possiveis problemas de qualidade.
- Preservar integralmente os dados brutos.

Regra principal:
- Este script nao deve alterar arquivos na pasta dados/brutos/.
"""

from pathlib import Path


PASTA_DADOS_BRUTOS = Path("dados/brutos")


def listar_arquivos_brutos() -> None:
    """Lista arquivos disponiveis para inspecao, sem abrir ou modificar dados."""
    print("Arquivos brutos encontrados:")
    for caminho in sorted(PASTA_DADOS_BRUTOS.glob("*")):
        if caminho.is_file() and caminho.name != ".gitkeep":
            print(f"- {caminho.name}")


def main() -> None:
    """Ponto de entrada da etapa de inspecao."""
    print("Etapa 01 - Inspecao dos dados")
    print("Nenhuma alteracao sera feita nos dados brutos.")
    listar_arquivos_brutos()


if __name__ == "__main__":
    main()

