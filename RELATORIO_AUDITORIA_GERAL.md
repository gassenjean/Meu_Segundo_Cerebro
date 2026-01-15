---
criado: 2026-01-15T15:30:00-03:00
tipo: relatorio_auditoria
status: pendente_correcao
---

# 🕵️ RELATÓRIO DE AUDITORIA GERAL (CLAUDE ↔ GEMINI)

**Objetivo:** Garantir consistência e simetria entre os ambientes `.claude` (Claude Code) e `.gemini` (Antigravity).

---

## 🚨 1. DIVERGÊNCIAS CRÍTICAS (Agentes Desconectados)

Detectamos que o Gemini tem acesso aos PROMPTS dos agentes, mas **não tem os COMANDOS SLASH** criados para ativá-los facilmente, enquanto o Claude tem.

| Agente | Prompt em `04_RECURSOS`? | Cmd `.claude`? | Cmd `.gemini`? | Status Gemini |
| :--- | :---: | :---: | :---: | :--- |
| **Alan Nicolas** | ✅ | ✅ | ❌ | **Inacessível** |
| **Pedro Sobral** | ✅ | ✅ | ❌ | **Inacessível** |
| **Lucas Amoedo** | ✅ | ✅ | ❌ | **Inacessível** |
| **Elena Vasquez** | ✅ | ✅ | ❌ | **Inacessível** |
| **Dr. Green** | ✅ | ✅ | ❌ | **Inacessível** |
| **Névoa** | ✅ (Duplicado) | ✅ | ✅ | OK |
| **KabaK** | ✅ | ✅ | ✅ | OK |

> **Risco:** Você tenta chamar `/alan` no Gemini e não funciona, quebrando o fluxo.

---

## 🛠️ 2. DIVERGÊNCIAS DE SKILLS (Ferramentas Faltando)

O ambiente Claude está "armado até os dentes" com skills que não foram portadas para o Gemini.

| Skill | `.claude/skills` | `.gemini/skills` | Ação Recomendada |
| :--- | :---: | :---: | :--- |
| `kabak` | ✅ | ✅ | OK (Sincronizado) |
| `gemini-handoff` | ✅ | ✅ | OK (Recém-criado) |
| `github-sync` | ✅ | ❌ | **PORTAR URGENTE** |
| `skill-creator` | ✅ | ❌ | Portar (Baixa prio) |
| `crypto-operations` | ✅ | ❌ | Portar se for operar |
| `defi-ai-analyzer` | ✅ | ❌ | Portar se for operar |

> **Risco:** Gemini não consegue fazer sync com GitHub autonomamente (`github-sync`), dependendo de comandos manuais.

---

## 📂 3. ORGANIZAÇÃO DE ARQUIVOS (Protocolos)

*   ✅ `00_SISTEMA/PROTOCOLOS` está bem populado e centralizado.
*   ✅ `PROTOCOLO_CLAUDE_GEMINI_ORQUESTRACAO.md` existe e define as regras.
*   ⚠️ **Alerta:** Encontramos `PROMPT_AGENTE_NEVOA.md` e `PROMPT_NEVOA_3.0.md`. Precisamos definir qual é o oficial e arquivar o outro.

---

## 📝 PLANO DE AÇÃO IMEDIATO (Correção)

1.  **Criar Comandos Slash no Gemini (.agent/workflows):** `alan.md`, `pedro.md`, `lucas.md`, `elena.md`, `dr-green.md`.
2.  **Portar Skill GitHub-Sync:** Para o Gemini poder commitar e manter o log de PC Sync atualizado.
3.  **Unificar Névoa:** Consolidar prompt oficial.

**Posso prosseguir com essas correções?**
