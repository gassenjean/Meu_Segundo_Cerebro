---
name: session-logger
description: Atualiza SESSION_LOG.md automaticamente com ações da sessão (comunicação bi-IA)
version: 1.0
triggers:
  - "sync"
  - "atualizar session log"
  - "registrar sessão"
  - "session log"
  - "salvar estado"
author: Gemini 3 Pro
created: 18/JAN/2026
---

# Session Logger

Automação inteligente que atualiza `SESSION_LOG.md` com ações da sessão atual, facilitando a comunicação entre Claude Code e Antigravity/Gemini.

## Funcionalidades

- ✅ Detecta mudanças na sessão (arquivos criados/modificados via git)
- ✅ Identifica agente ativo (Claude ou Gemini)
- ✅ Gera entrada com timestamp formatado
- ✅ Lista ações e arquivos modificados
- ✅ Mantém formatação original do SESSION_LOG.md
- ✅ Cria backup automático antes de escrever
- ✅ Preserva histórico completo

## Como Usar

**Linguagem Natural:**

- "Sync"
- "Atualizar session log"
- "Registrar sessão"
- "Salvar estado para o outro agente"

**Comando Explícito:**

- `/session-logger` (executa registro da sessão)

## Workflow

1. **Scan:** Detecta mudanças via `git status`
2. **Análise:** Identifica ações significativas e categoriza
3. **Template:** Gera entrada seguindo formato padrão do `SESSION_LOG.md`
4. **Update:** Insere no topo de `SESSION_LOG.md`
5. **Backup:** Cria cópia de segurança (`.bak`)
6. **Relatório:** Confirma ações registradas

## Script

Executa `scripts/logger.py` que implementa toda lógica automaticamente.
