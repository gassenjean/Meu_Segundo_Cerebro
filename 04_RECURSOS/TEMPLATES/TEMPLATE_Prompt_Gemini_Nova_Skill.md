# 🤖 TEMPLATE: Prompt para Criar Nova Skill (Gemini)

Use este prompt ao solicitar que o Gemini (Antigravity) crie uma nova automação.

---

## Estrutura do Prompt

Copie e preencha as seções entre colchetes `[...]`.

```markdown
# PEDIDO: Criar Nova Antigravity Skill - [NOME DA SKILL]

**Para:** Gemini 3 Pro (Antigravity)
**Contexto:** Sistema Bi-IA (Claude + Gemini)
**Objetivo:** Automatizar [DESCRIÇÃO CURTA DO OBJETIVO]

---

## 📋 Especificações da Skill

**Nome Técnico:** `[nome-kebab-case]` (ex: vault-organizer)
**Trigger Words:**
- "[frase gatilho 1]"
- "[frase gatilho 2]"

**Funcionalidades Obrigatórias:**
1. [Funcionalidade A]
2. [Funcionalidade B]
3. [Safety Feature - ex: Backup]

**Entrada (Input):**
- [O que a skill lê? Ex: Arquivos na raiz, lista de check]

**Saída (Output):**
- [O que a skill produz? Ex: Arquivos movidos, Relatório MD]

---

## 🛠️ Requisitos Técnicos

1. **Linguagem:** Python 3 (executável localmente).
2. **Estrutura:** Seguir `TEMPLATE_Criar_Skill_Antigravity.md`.
3. **Localização:** `.gemini/skills/[nome-da-skill]/`.
4. **Safety:**
   - Criar backup `.bak` ante de sobrescrever.
   - Usar `utf-8`.
   -Logs claros com Emojis.

---

## 🧪 Casos de Teste (Validação)

Ao finalizar, teste os seguintes cenários:
1. [Cenário 1 - Caminho Feliz]
2. [Cenário 2 - Erro/Exceção]

---

**Instruções para o Agente:**
1. Crie a estrutura de pastas.
2. Escreva o `skill.md`.
3. Escreva o script Python.
4. Teste a skill (simulação).
5. Confirme criação para registro no SESSION_LOG.
```

---

## Exemplo Real (Session Logger)

```markdown
# PEDIDO: Criar Nova Antigravity Skill - Session Logger

**Para:** Gemini 3 Pro
**Objetivo:** Automatizar o registro de sessão no SESSION_LOG.md

## Especificações
**Nome:** `session-logger`
**Triggers:** "sync", "registrar sessão"

**Funcionalidades:**
1. Ler status do git (`git status`).
2. Identificar arquivos criados/modificados.
3. Gerar entrada no topo de `SESSION_LOG.md` seguindo padrão.
4. Usar emojis (🟣 para Gemini).

**Safety:**
- Backup de SESSION_LOG.md antes de editar.
- Não quebrar formatação existente.
```

---

**Fim do Template**
