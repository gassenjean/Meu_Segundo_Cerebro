---
name: architect-linter
description: Codebase Auditor (Codebase Auditor - Mechanical Checks).
---

# Architect Linter (Codebase Auditor)

Esta skill realiza verificações mecânicas e estruturais no vault para garantir a integridade do sistema. Diferente do `vault-auditor`, o foco aqui é prevenção rápida e validação de padrões arquiteturais básicos.

## Comandos

### `architect-linter run`

Executa a auditoria completa e gera um relatório.

## Verificações Realizadas

1. **Root Hygiene:** Verifica se apenas arquivos permitidos estão na raiz.
2. **H1 Duplicates:** Detecta arquivos com títulos H1 duplicados (conflito de conceito).
3. **Broken Links:** Verifica se links internos `[[link]]` apontam para arquivos existentes.
4. **Frontmatter Check:** Verifica se arquivos Markdown possuem frontmatter YAML válido no início.

## Relatório

O relatório é gerado em: `00_SISTEMA/RELATORIOS/ARCHITECT_LINTER_[DATA].md`
