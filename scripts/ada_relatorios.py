"""
Funções auxiliares para relatórios do Protocolo ADA.

Estas funções preservam a seção de validação humana quando um relatório
é gerado novamente. Isso evita que observações e decisões manuais sejam
apagadas por uma nova execução do Python.
"""

from pathlib import Path


MARCADOR_INICIO = "<!-- INICIO_VALIDACAO_HUMANA -->"
MARCADOR_FIM = "<!-- FIM_VALIDACAO_HUMANA -->"


def montar_secao_validacao_humana(titulo: str, conteudo_padrao: str) -> str:
    """Monta a seção de decisão com marcadores de preservação."""
    return "\n".join(
        [
            titulo,
            "",
            MARCADOR_INICIO,
            conteudo_padrao.strip(),
            MARCADOR_FIM,
        ]
    )


def preservar_validacao_humana(caminho_relatorio: Path, novo_conteudo: str, titulo_secao: str) -> str:
    """
    Preserva a validação humana já existente antes de reescrever o relatório.

    Regras:
    - Se o relatório anterior tiver marcadores, preserva exatamente o conteúdo
      entre eles.
    - Se o relatório anterior ainda não tiver marcadores, tenta preservar o
      texto da seção pelo título informado.
    - Se não houver relatório anterior, mantém o bloco padrão do novo relatório.
    """
    if not caminho_relatorio.exists():
        return novo_conteudo

    conteudo_antigo = caminho_relatorio.read_text(encoding="utf-8")
    bloco_antigo = extrair_bloco_validacao(conteudo_antigo, titulo_secao)
    if not bloco_antigo:
        return novo_conteudo

    bloco_novo = extrair_bloco_validacao(novo_conteudo, titulo_secao)
    if not bloco_novo:
        return novo_conteudo

    return novo_conteudo.replace(bloco_novo, bloco_antigo)


def extrair_bloco_validacao(conteudo: str, titulo_secao: str) -> str:
    """Extrai a seção de decisão humana completa, incluindo o título."""
    inicio_titulo = conteudo.find(titulo_secao)
    if inicio_titulo == -1:
        return ""

    proxima_secao = conteudo.find("\n## ", inicio_titulo + len(titulo_secao))
    if proxima_secao == -1:
        bloco = conteudo[inicio_titulo:].rstrip()
    else:
        bloco = conteudo[inicio_titulo:proxima_secao].rstrip()

    if MARCADOR_INICIO in bloco and MARCADOR_FIM in bloco:
        return bloco

    linhas = bloco.splitlines()
    if not linhas:
        return ""

    titulo = linhas[0].strip()
    corpo = "\n".join(linhas[1:]).strip()
    return montar_secao_validacao_humana(titulo, corpo)


def escrever_relatorio_preservando_validacao(
    caminho_relatorio: Path,
    novo_conteudo: str,
    titulo_secao: str,
) -> None:
    """Escreve o relatório sem apagar a decisão ou validação humana anterior."""
    conteudo_final = preservar_validacao_humana(caminho_relatorio, novo_conteudo, titulo_secao)
    caminho_relatorio.write_text(conteudo_final, encoding="utf-8")
