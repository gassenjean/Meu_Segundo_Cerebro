---
name: mapa
description: Gera um mapa completo do vault (Índice) para economizar tokens e facilitar navegação.
triggers:
  - mapa
  - índice
  - index
  - gerar indice
  - update index
version: 1.0.0
author: Antigravity (Gemini 3 Pro)
steps:
  - name: generate_map
    command: python scripts/mapa.py
    description: Gera o arquivo INDICE_VAULT_COMPLETO.md
---
# Skill: Mapa (Vault Indexer)

Esta skill gera uma **visualização completa da estrutura do seu Segundo Cérebro**.
Ela cria um arquivo Markdown contendo uma árvore de arquivos e seus títulos, permitindo que a IA (e você) encontre rapidamente qualquer conteúdo sem precisar navegar pasta por pasta.

## Output

O arquivo gerado é salvo em: `00_SISTEMA/INDICE_VAULT_COMPLETO.md`

## Uso
>
> mapa
> gerar indice

## Detalhes

- Ignora pastas de sistema (`.git`, `.obsidian`, etc).
- Lê o título H1 de cada nota para dar contexto.
- Usa WikiLinks para navegação rápida.
