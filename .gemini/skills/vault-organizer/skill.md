---
name: vault-organizer
description: Organiza arquivos automaticamente seguindo padrões do vault (NOMENCLATURA.md)
version: 1.0
triggers:
  - "organizar vault"
  - "marie kondo"
  - "limpar arquivos"
  - "vault organizer"
author: Gemini 3 Pro
created: 18/JAN/2026
---

# Vault Organizer

Automação inteligente que organiza arquivos do vault seguindo os padrões definidos em `NOMENCLATURA.md` e `PROTOCOLO_CRIACAO_ARQUIVOS.md`.

## Funcionalidades

- ✅ Identifica arquivos fora do lugar
- ✅ Move para localização correta (01-05 categorias)
- ✅ Renomeia seguindo padrões (CamelCase, underscores)
- ✅ Atualiza MOCs automaticamente
- ✅ Gera relatório detalhado

## Como Usar

**Linguagem Natural:**

- "Organize os arquivos da raiz"
- "Marie Kondo no vault"
- "Limpar arquivos soltos"
- "Organizar PDFs que estão fora do lugar"

**Comando Explícito:**

- `/vault-organizer` (executa scan completo)

## Workflow

1. **Scan:** Identifica arquivos fora do lugar
2. **Análise:** Determina tipo e localização correta
3. **Ação:** Move e renomeia (com confirmação se necessário)
4. **Atualização:** Atualiza MOCs relevantes
5. **Relatório:** Gera resumo de ações realizadas

## Padrões Aplicados

**Lê e aplica:**

- `00_SISTEMA/PADROES/NOMENCLATURA.md` - Padrões de nome
- `00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md` - Workflow
- MOCs de cada categoria (estrutura)

**Categorizações:**

- PDFs de pesquisa → `01_CONHECIMENTO/[Area]/`
- Screenshots de projeto → `02_PROJETOS/[Projeto]/docs/`
- Templates → `04_RECURSOS/TEMPLATES/`
- Ideias pessoais → `05_PESSOAL/Ideas/`

## Script

Executa `scripts/organizer.py` que implementa toda lógica automaticamente.
