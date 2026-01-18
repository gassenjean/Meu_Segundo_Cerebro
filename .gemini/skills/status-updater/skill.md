---
name: status-updater
description: Atualiza STATUS_VAULT.md automaticamente com métricas e progresso
version: 1.0
triggers:
  - "atualizar status"
  - "update vault status"
  - "status vault"
  - "atualizar progresso"
author: Gemini 3 Pro
created: 18/JAN/2026
---

# Status Updater

Automação inteligente que atualiza `STATUS_VAULT.md` com métricas coletadas automaticamente do vault.

## Funcionalidades

- ✅ Coleta métricas do vault (arquivos, projetos, MOCs)
- ✅ Calcula progresso por fase (1-7)
- ✅ Atualiza estatísticas automaticamente
- ✅ Adiciona entrada no histórico com timestamp
- ✅ Mantém formatação original
- ✅ Gera relatório de mudanças

## Como Usar

**Linguagem Natural:**

- "Atualize o status do vault"
- "Atualizar progresso"
- "Status vault update"
- "Gerar relatório de progresso"

**Comando Explícito:**

- `/status-updater` (executa update completo)

## Workflow

1. **Scan:** Coleta métricas do vault (arquivos, pastas, MOCs, comandos)
2. **Análise:** Calcula progresso por fase e geral
3. **Update:** Atualiza seções de STATUS_VAULT.md
4. **Histórico:** Adiciona nova entrada com timestamp
5. **Relatório:** Gera resumo de mudanças

## Métricas Coletadas

**Estrutura:**

- Total de arquivos
- Projetos ativos (02_PROJETOS/)
- Cursos ativos (03_APRENDIZADO/)
- MOCs criados (00_SISTEMA/MOCs/)
- Templates (04_RECURSOS/TEMPLATES/)
- Checklists, Prompts, Guias

**Comandos:**

- Skills Claude (.claude/skills/)
- Skills Antigravity (.gemini/skills/)
- Total de comandos disponíveis

**Progresso:**

- Fase 1-7 (% baseado em critérios)
- Progresso geral calculado

## Script

Executa `scripts/updater.py` que implementa toda lógica automaticamente.
