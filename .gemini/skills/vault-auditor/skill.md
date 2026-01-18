---
name: vault-auditor
description: Varredura completa no vault para identificar erros de padrão, nomenclatura e estrutura.
version: 1.0
triggers:
  - "auditar vault"
  - "varredura completa"
  - "verificar erros no vault"
  - "health check"
author: Gemini 3 Pro
created: 18/JAN/2026
---

# Vault Auditor

Skill de auditoria profunda que verifica a conformidade do vault com os padrões do sistema (Nomenclatura, Localização, Markdown, Links, Projetos).

## Funcionalidades

- ✅ **Varredura Completa:** Analisa todos os arquivos do vault.
- ✅ **Nomenclatura:** Verifica espaços, prefixos, CamelCase, datas e caracteres proibidos.
- ✅ **Localização:** Garante que arquivos estejam nas pastas corretas (00-05).
- ✅ **Estrutura:** Valida presença de H1 e Frontmatter em arquivos MD.
- ✅ **Links:** Detecta links quebrados ou absolutos.
- ✅ **Projetos:** Verifica integridade da estrutura de projetos (README, STATUS).
- ✅ **Relatório:** Gera relatório detalhado em `00_SISTEMA/RELATORIOS/`.
- ✅ **Read-Only:** Não altera arquivos, apenas reporta e sugere correções.

## Como Usar

**Linguagem Natural:**

- "Auditar vault"
- "Executar varredura de erros"
- "Faça um health check no sistema"

## Workflow

1. **Scan:** Indexa todos os arquivos do vault.
2. **Check:** Executa validadores (Nomenclatura, Localização, Markdown, Links, Projetos, Duplicação, Obsoletos).
3. **Report:** Compila os resultados e gera `AUDITORIA_VAULT_[DATA].md`.

## Script

Executa `scripts/auditor.py`.
