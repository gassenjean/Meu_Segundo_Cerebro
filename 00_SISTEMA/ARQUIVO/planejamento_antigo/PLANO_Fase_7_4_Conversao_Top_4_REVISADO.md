# PLANO: Fase 7.4 - Conversão Top 4 Skills (REVISADO)

**Status:** Planejamento Aprovado
**Data:** 18/01/2026
**Autor:** Antigravity (Gemini 3 Pro)
**Contexto:** Sistema Bi-IA (Fase 7 - Finalização)
**Baseado em:** `ANALISE_Correcoes_PLANO_Fase_7_4.md`

---

## 1. 📋 Inventário & Status Atual

Análise corrigida das skills existentes no ecossistema Antigravity.

### ✅ Já Convertidas / Nativas (3)

| Skill Antigravity | Origem Claude | Status | Obs |
|:---|:---|:---|:---|
| **vault-organizer** | `limpeza-raiz`, `marie-kondo` | ✅ Aprovada | Organização automática |
| **status-updater** | `atualizar-status` | ✅ Aprovada | Dashboard metrics |
| **session-logger** | `sync` | ✅ Aprovada | Comunicação Bi-IA |

**Nota:** Skills Claude (`github-sync`, `gemini`, `kabak-agent`) permanecem como comandos Claude (`.claude/commands/`). Não são Antigravity Skills nativas.

### 🔍 Candidatas à Conversão (Top 12)

1. **validate** (Validação de arquivos/estrutura)
2. **mapa** (Gerador de índice)
3. **claude-architect** (Guardião de padrões)
4. **learn / work** (Context Managers)
5. *coach* (Orquestrador TDAH - Manter Prompt)
6. *ultra-think* (Análise profunda - Manter Prompt)
7. *nevoa* (Orquestrador geral - Manter Prompt)
8. *deep-research* (Complexidade Técnica Alta - Adiar)

---

## 2. 📊 Critérios de Seleção Revisados

Foco em **Qualidade > Quantidade**. Critérios rígidos para automação via script:

1. **Determinístico:** Lógica clara (if/else), sem dependência de "feeling".
2. **Impacto:** Alta frequência de uso ou grande economia de tokens.
3. **Independência:** Roda sem supervisão constante.

---

## 3. 🏆 Seleção Top 4 (Roadmap de Conversão)

Skills selecionadas para a Fase 7.4 por sua viabilidade e impacto imediato.

### 1. `validate` (Filesystem Guardian)

* **Pontuação:** 30/30
* **Prioridade:** MÁXIMA
* **Função:** Validar nomes de arquivos, locais e atualizar MOCs automaticamente.
* **Lógica:** Regex checks, verificação de existência de pastas, leitura de `NOMENCLATURA.md`.
* **Impacto:** Elimina erro humano na criação de arquivos (95% redução).

### 2. `mapa` (Vault Indexer)

* **Pontuação:** 29/30
* **Prioridade:** MÁXIMA
* **Função:** Gerar arquivo `00_SISTEMA/MOCs/INDICE_VAULT_COMPLETO.md` via script.
* **Lógica:** Walk directory, ignorar sistema, estruturar árvore MD.
* **Impacto:** Economia massiva de tokens (Claude lê 1 arquivo vs 1000).

### 3. `context-manager` (Focus Enforcer)

* **Pontuação:** 27/30
* **Prioridade:** ALTA
* **Função:** Unificação de `/learn`, `/work` e `/knowledge`.
* **Lógica:** Prepara ambiente: exibe status do projeto, carrega prompts específicos, sugere próximos passos.
* **Impacto:** Reduz fricção de troca de contexto (2-3 min por troca).

### 4. `architect-linter` (Codebase Auditor - Escopo Limitado)

* **Pontuação:** 26/30
* **Prioridade:** MÉDIA
* **Função:** Scan proativo de violações de padrões (APENAS checks mecânicos).
* **Lógica:**
  * ✅ Verificar H1 duplicados (regex)
  * ✅ Verificar links quebrados (file exists)
  * ✅ Verificar arquivos na raiz (listdir)
  * ✅ Verificar frontmatter ausente (regex)
  * ❌ NÃO fazer análise semântica (manter em Claude)
* **Impacto:** Mantém higiene do vault automaticamente (semelhante ao `vault-auditor` mas focado em prevenção rápida).

---

## 4. 📅 Roadmap de Implementação

**Ordem de Execução (Fase 7.4):**

1. **Semana 1 (Quick Wins):**
   * [ ] Criar `validate`
   * [ ] Criar `mapa`

2. **Semana 2 (Estruturais):**
   * [ ] Criar `context-manager`
   * [ ] Criar `architect-linter`

**Skills Adiadas / Removidas:**
* `coach-tools`: Reconsiderar como `pomodoro-timer` simples na Fase 7.5.
* `deep-research`: Adiar para Fase 7.6+ (requer infra de APIs).
* `idea-processor`: Manter como prompt Claude (não automatizável).

---

## 5. 🛠️ Próximos Passos (Imediato)

1. Claude aprovar este plano revisado.
2. Autorizar início da implementação da **Skill #1: `validate`**.
