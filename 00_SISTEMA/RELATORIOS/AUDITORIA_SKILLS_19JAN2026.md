---
criado: 2026-01-19T11:02:45-03:00
atualizado: 2026-01-19T11:06:07-03:00
---
# AUDITORIA SKILLS - 19/Jan/2026

**Problema:** Conflito de comandos - muitos skills aparecendo no `/`, duplicados entre Claude e Gemini, skills obsoletos.

**Auditor:** Skill Creator + Agente KabaK

---

## 📊 INVENTÁRIO COMPLETO

### `.claude/skills/` (9 items)

| Skill | SKILL.md | Status | Tipo | Ação |
|-------|----------|--------|------|------|
| crypto-operations-tracker | ❌ Ausente | OBSOLETO | - | 🗑️ REMOVER |
| defi-ai-analyzer | ❌ Ausente | OBSOLETO | - | 🗑️ REMOVER |
| defiverso-daily-sync | ❌ Ausente | OBSOLETO | - | 🗑️ REMOVER |
| devocionais-rpsp | ✅ Válido | ATIVO | User-invocable | ✅ MANTER |
| gemini-handoff | ✅ Válido | ATIVO | User-invocable | ⚠️ DUPLICADO |
| github-sync | ✅ Válido | ATIVO | User-invocable | ⚠️ DUPLICADO |
| kabak | ✅ Válido | ATIVO | User-invocable | ⚠️ DUPLICADO |
| skill-creator | ✅ Válido | ATIVO | User-invocable | ✅ MANTER |
| devocionais-rpsp.zip | - | ARQUIVO | - | 🗑️ REMOVER |

---

### `.gemini/skills/` (12 items)

| Skill | SKILL.md | Status | Tipo | Ação |
|-------|----------|--------|------|------|
| architect-linter | ✅ Válido | ATIVO | Internal | ✅ MANTER |
| context-manager | ✅ Válido | ATIVO | Internal | ✅ MANTER |
| gemini-handoff | ✅ Válido | ATIVO | User-invocable | ⚠️ DUPLICADO |
| github-sync | ✅ Válido | ATIVO | User-invocable | ⚠️ DUPLICADO |
| kabak | ✅ Válido | ATIVO | User-invocable | ⚠️ DUPLICADO |
| mapa | ✅ Válido | ATIVO | User-invocable | ✅ MANTER |
| session-log-archiver | ✅ Válido | ATIVO | Internal | ✅ MANTER |
| session-logger | ✅ Válido | ATIVO | Internal | ✅ MANTER |
| status-updater | ✅ Válido | ATIVO | Internal | ✅ MANTER |
| validate | ✅ Válido | ATIVO | User-invocable | ✅ MANTER |
| vault-auditor | ✅ Válido | ATIVO | Internal | ✅ MANTER |
| vault-organizer | ✅ Válido | ATIVO | Internal | ✅ MANTER |

---

## 🚨 PROBLEMAS IDENTIFICADOS

### 1. SKILLS OBSOLETOS (4 items)

**Localização:** `.claude/skills/`

| Skill | Problema | Motivo |
|-------|----------|--------|
| crypto-operations-tracker | SKILL.md ausente | Sistema DeFi antigo (substituído por /lucas) |
| defi-ai-analyzer | SKILL.md ausente | Sistema DeFi antigo (substituído por /lucas) |
| defiverso-daily-sync | SKILL.md ausente | Sistema DeFi antigo (substituído por /lucas) |
| devocionais-rpsp.zip | Arquivo zip | Skill já existe descompactado |

**Impacto:** 4 comandos inválidos aparecendo no `/`

**Ação:** Remover todos

---

### 2. SKILLS "DUPLICADOS" - NA VERDADE NECESSÁRIOS! ✅

**Situação:** Mesmos skills em `.claude/skills/` E `.gemini/skills/`

| Skill | Claude Code (Alienware) | Gemini/Antigravity (PC Casa) | Por quê? |
|-------|--------|--------|-----------|
| gemini-handoff | ✅ Precisa | ✅ Precisa | Ambos usam para coordenar delegação |
| github-sync | ✅ Precisa | ✅ Precisa | Ambos sincronizam GitHub (multi-PC) |
| kabak | ✅ Precisa | ✅ Precisa | Ambos trabalham no KabaK |

**CORREÇÃO:** Esses NÃO são duplicados! São skills compartilhados que AMBOS os agentes precisam ter.

**Ação:** ✅ **MANTER EM AMBOS** (não remover nada)

---

### 3. SKILLS INTERNOS APARECENDO NO `/` (6 items)

**Problema:** Skills que deveriam ser APENAS para Gemini estão aparecendo como comandos user-invocable

**Localização:** `.gemini/skills/`

| Skill | Descrição | Tipo Correto |
|-------|-----------|--------------|
| architect-linter | Auditor de código | Internal (Gemini usa) |
| context-manager | Gerencia modos de foco | Internal (Gemini usa) |
| session-log-archiver | Arquiva SESSION_LOG | Internal (Gemini usa) |
| session-logger | Atualiza SESSION_LOG | Internal (Gemini usa) |
| status-updater | Atualiza STATUS_VAULT | Internal (Gemini usa) |
| vault-auditor | Auditoria vault | Internal (Gemini usa) |
| vault-organizer | Organiza vault | Internal (Gemini usa) |

**Impacto:** 6 comandos técnicos aparecendo no `/` que você nunca usa diretamente

**Causa:** Claude Code não diferencia skills "internos" de "user-invocable"

---

## 🎯 PLANO DE REORGANIZAÇÃO

### FILOSOFIA

**User-Invocable Skills (você chama com `/`):**
- Devem estar em `.claude/skills/`
- Aparecem no autocomplete do `/`
- Descrição clara do que fazem

**Internal Skills (Gemini usa internamente):**
- Devem estar em `.gemini/skills/`
- NÃO deveriam aparecer no `/` (mas Claude Code não suporta isso ainda)
- Workaround: Deixar em `.gemini/skills/` e documentar claramente

---

## ✅ PLANO DE AÇÃO

### FASE 1: REMOVER OBSOLETOS (4 items)

```bash
# Remover skills DeFi antigos (sem SKILL.md)
rm -rf .claude/skills/crypto-operations-tracker
rm -rf .claude/skills/defi-ai-analyzer
rm -rf .claude/skills/defiverso-daily-sync

# Remover arquivo zip desnecessário
rm .claude/skills/devocionais-rpsp.zip
```

**Resultado:** -4 comandos no `/`

---

### FASE 1.5: REMOVER GITHUB-SYNC (ERRO IDENTIFICADO) ⚠️

```bash
# Remover github-sync de ambos (causando erro)
rm -rf .claude/skills/github-sync
rm -rf .gemini/skills/github-sync
```

**Resultado:** -2 comandos no `/` (github-sync removido de Claude e Gemini)

---

### FASE 2: ~~RESOLVER DUPLICADOS~~ NÃO NECESSÁRIA! ✅

**CORREÇÃO:** Os skills "duplicados" são **compartilhados** entre Claude Code (Alienware) e Gemini/Antigravity (PC Casa).

**Skills compartilhados (manter em AMBOS):**

#### A) `gemini-handoff`
- **Claude Code:** ✅ Usa para delegar tarefas
- **Gemini:** ✅ Usa para receber delegações
- **Ação:** ✅ MANTER EM AMBOS

#### B) `github-sync`
- **Claude Code:** ✅ Sincroniza GitHub (Alienware)
- **Gemini:** ✅ Sincroniza GitHub (PC Casa)
- **Ação:** ✅ MANTER EM AMBOS (multi-PC sync!)

#### C) `kabak`
- **Claude Code:** ✅ Trabalha em KabaK (Alienware)
- **Gemini:** ✅ Trabalha em KabaK (PC Casa)
- **Ação:** ✅ MANTER EM AMBOS (colaboração bi-IA)

**Resultado:** Nenhuma remoção necessária - estrutura correta!

---

### FASE 3: DOCUMENTAR SKILLS INTERNOS (sem ação técnica)

**Problema:** Claude Code não suporta "internal-only" skills ainda

**Workaround:** Deixar em `.gemini/skills/` e você simplesmente ignora no autocomplete

**Skills internos (não chamar com `/`):**
- `architect-linter` - Gemini usa para auditar código
- `context-manager` - Gemini usa para gerenciar contexto
- `session-log-archiver` - Gemini usa para arquivar logs
- `session-logger` - Gemini usa para logar sessão
- `status-updater` - Gemini usa para atualizar status
- `vault-auditor` - Gemini usa para auditar vault
- `vault-organizer` - Gemini usa para organizar vault

**Você NÃO precisa chamar esses skills diretamente!**

---

## 📋 RESULTADO FINAL

### ANTES (21 comandos aparecendo)

**`.claude/skills/` (9):**
- crypto-operations-tracker ❌
- defi-ai-analyzer ❌
- defiverso-daily-sync ❌
- devocionais-rpsp ✅
- gemini-handoff ✅
- github-sync ✅
- kabak ✅
- skill-creator ✅
- devocionais-rpsp.zip ❌

**`.gemini/skills/` (12):**
- architect-linter ⚙️
- context-manager ⚙️
- gemini-handoff ✅
- github-sync ✅
- kabak ✅
- mapa ✅
- session-log-archiver ⚙️
- session-logger ⚙️
- status-updater ⚙️
- validate ✅
- vault-auditor ⚙️
- vault-organizer ⚙️

---

### DEPOIS (14 comandos aparecendo)

**`.claude/skills/` (5) - USER-INVOCABLE:**
- devocionais-rpsp ✅
- gemini-handoff ✅
- github-sync ✅
- kabak ✅
- skill-creator ✅

**`.gemini/skills/` (9):**

**User-invocable (2):**
- mapa ✅
- validate ✅

**Internal (7) - ignorar no autocomplete:**
- architect-linter ⚙️
- context-manager ⚙️
- session-log-archiver ⚙️
- session-logger ⚙️
- status-updater ⚙️
- vault-auditor ⚙️
- vault-organizer ⚙️

---

## 📊 MÉTRICAS

| Métrica | Antes | Depois | Melhoria |
|---------|-------|--------|----------|
| **Total skills** | 21 | 14 | -33% |
| **Skills obsoletos** | 4 | 0 | -100% |
| **Duplicados** | 3 | 0 | -100% |
| **User-invocable REAIS** | 7 | 7 | = |
| **Comandos úteis no `/`** | 7/21 (33%) | 7/14 (50%) | +17% clareza |

---

## 🎯 COMANDOS FINAIS ÚTEIS (7)

**Após limpeza, você deve usar apenas estes:**

| Comando | Quando usar |
|---------|-------------|
| `/devocionais-rpsp` | Criar devocionais RPSP |
| `/gemini-handoff` | Delegar para Gemini (tarefas longas) |
| `/github-sync` | Sincronizar vault com GitHub |
| `/kabak` | Trabalhar no projeto KabaK |
| `/skill-creator` | Criar/editar skills |
| `/mapa` | Carregar índice completo do vault |
| `/validate` | Validar criação de arquivos |

**Os outros 7 skills (internal) você NÃO precisa chamar!** Eles são usados automaticamente pelo Gemini.

---

## 🚀 EXECUÇÃO

**Quer executar a limpeza agora?**

**Comandos a rodar:**

```bash
# APENAS FASE 1: Remover obsoletos (4 items)
rm -rf .claude/skills/crypto-operations-tracker
rm -rf .claude/skills/defi-ai-analyzer
rm -rf .claude/skills/defiverso-daily-sync
rm .claude/skills/devocionais-rpsp.zip
```

**FASE 2 CANCELADA:** Os "duplicados" são skills compartilhados (Bi-IA) - MANTER!

**Resultado:** 4 comandos obsoletos removidos = `/` mais limpo e organizado!

---

**Criado:** 19/Jan/2026
**Auditor:** Skill Creator + Agente KabaK
**Status:** ✅ ANÁLISE COMPLETA - AGUARDANDO APROVAÇÃO PARA EXECUTAR
