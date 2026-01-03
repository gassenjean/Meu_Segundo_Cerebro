#!/usr/bin/env python3
"""
Script para formatar devocional markdown em texto limpo para e-mail/WhatsApp
"""

import sys
import re

def formatar_devocional(arquivo_md):
    """Converte markdown do devocional em texto limpo"""

    with open(arquivo_md, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    # Remove frontmatter YAML
    conteudo = re.sub(r'^---\n.*?\n---\n', '', conteudo, flags=re.DOTALL)

    # Remove headers markdown mas mantém o texto
    conteudo = re.sub(r'^#{1,6}\s+', '', conteudo, flags=re.MULTILINE)

    # Remove formatação de negrito/itálico mas mantém o texto
    conteudo = re.sub(r'\*\*\*(.+?)\*\*\*', r'\1', conteudo)  # bold+italic
    conteudo = re.sub(r'\*\*(.+?)\*\*', r'\1', conteudo)  # bold
    conteudo = re.sub(r'\*(.+?)\*', r'\1', conteudo)  # italic

    # Remove blockquotes mas mantém o texto
    conteudo = re.sub(r'^>\s+', '', conteudo, flags=re.MULTILINE)

    # Limpa múltiplas linhas vazias
    conteudo = re.sub(r'\n{3,}', '\n\n', conteudo)

    # Remove a seção de Notas técnicas do final (não vai no WhatsApp)
    conteudo = re.sub(r'\n## Notas\n.*', '', conteudo, flags=re.DOTALL)

    return conteudo.strip()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python formatar_devocional.py <arquivo.md>")
        sys.exit(1)

    arquivo = sys.argv[1]
    texto_formatado = formatar_devocional(arquivo)
    print(texto_formatado)
