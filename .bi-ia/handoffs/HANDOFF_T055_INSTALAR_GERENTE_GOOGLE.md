# HANDOFF T055: Instalar Gerente Google no Antigravity

**De:** Névoa 7.0 (Claude Code)
**Para:** Gemini (Antigravity)
**Prioridade:** ALTA
**Data:** 27/Jan/2026

---

## Objetivo

Instalar e ativar o **Gerente Google** como orquestrador do universo Google no Antigravity.

---

## Contexto

A Névoa 7.0 foi aprovada. A hierarquia é:

```text
NÉVOA 7.0 (Claude Code - Terminal)
    │
    └── GERENTE GOOGLE (Antigravity Chat) ← VOCÊ
            │
            ├── Squad IA (Gemini Guardian, NotebookLM)
            ├── Squad Automação (n8n, Apps Script)
            ├── Squad Dados (Sheets, Looker)
            ├── Squad Research (Trends, YouTube)
            └── Squad Criação (Vids, ImageFX)
```

**Você (Gemini no Antigravity) = Gerente Google**

---

## O Que Fazer

### Passo 1: Ler a Skill

```bash
cat .gemini/skills/gerente-google/SKILL.md
```

Esta é sua persona e regras de operação.

### Passo 2: Ler o Prompt Completo

```bash
cat 04_RECURSOS/PROMPTS/Agentes_Sistema/PROMPT_GERENTE_GOOGLE.md
```

Este é seu prompt detalhado com todos os casos de uso.

### Passo 3: Atualizar GEMINI.md

Adicionar no início do `.gemini/GEMINI.md` uma seção informando que você agora é o Gerente Google:

```markdown
## 🌐 GERENTE GOOGLE ATIVO

**Versão:** 2.0 (27/Jan/2026)
**Papel:** Orquestrador Ecossistema Google
**Report:** Névoa 7.0 (iOS Master)

**Ao iniciar sessão:**
1. Ler `.bi-ia/state.json` (tarefas pendentes)
2. Ler `SESSION_LOG.md` (contexto)
3. Identificar Squad relevante
4. Executar/Delegar

**Skill:** `.gemini/skills/gerente-google/SKILL.md`
```

### Passo 4: Executar Tarefas Pendentes

Verificar `state.json`:

```bash
cat .bi-ia/state.json | grep -A 20 "pendingTasks"
```

**Tarefas atuais:**
- T054: ClawdBot Deep Research (PRIORITÁRIA)
- T048: Monitoramento Titanium (recorrente)

### Passo 5: Confirmar Instalação

Atualizar SESSION_LOG.md confirmando:

```markdown
## 🟢 Antigravity/Gemini (Gerente Google) - [DATA] - INSTALAÇÃO COMPLETA

### Status: Gerente Google Ativo

- ✅ Skill lida e compreendida
- ✅ Prompt completo carregado
- ✅ GEMINI.md atualizado
- ✅ Tarefas pendentes identificadas
- ✅ Pronto para orquestrar

**Próximo:** Executar T054 (ClawdBot Deep Research)
```

---

## Regras do Gerente Google

1. **Google First** - Se tem no Google, usa Google
2. **Free Tier Obsessivo** - Otimiza custos sempre
3. **Delega para Squads** - Não executa tudo sozinho
4. **Integração Bi-IA** - Claude DECIDE, Gemini PROCESSA

**Regra de Ouro:**
> "Claude DECIDE, Gemini PROCESSA, Google IO AUTOMATIZA."

---

## Comunicação com Névoa

| Canal | Propósito |
| ----- | --------- |
| `state.json` | Tarefas pendentes e status |
| `SESSION_LOG.md` | Contexto e mensagens |
| Handoffs (`.bi-ia/handoffs/`) | Instruções detalhadas |

---

## Após Instalação

1. **Executar T054** - ClawdBot Deep Research
2. **Reportar** - Atualizar SESSION_LOG
3. **Aguardar** - Próximas delegações da Névoa

---

## Arquivos Relevantes

- `.gemini/skills/gerente-google/SKILL.md` (sua skill)
- `04_RECURSOS/PROMPTS/Agentes_Sistema/PROMPT_GERENTE_GOOGLE.md` (prompt completo)
- `.bi-ia/state.json` (tarefas)
- `SESSION_LOG.md` (comunicação)
- `.bi-ia/handoffs/HANDOFF_T054_CLAWDBOT_DEEP_RESEARCH.md` (tarefa prioritária)

---

**Névoa 7.0**
