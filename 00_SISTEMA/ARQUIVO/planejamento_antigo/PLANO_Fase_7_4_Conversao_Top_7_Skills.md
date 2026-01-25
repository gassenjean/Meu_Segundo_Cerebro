# PLANO: Fase 7.4 - Conversão Top 7 Skills (Claude → Antigravity)

**Status:** Planejamento
**Data:** 18/01/2026
**Autor:** Antigravity (Gemini 3 Pro)
**Contexto:** Sistema Bi-IA (Fase 7 - Finalização)

---

## 1. 📋 Inventário & Status Atual

Análise das 21 skills/comandos identificados no ecossistema atual.

### ✅ Já Convertidas / Nativas (6)

| Skill Antigravity | Origem Claude | Status | Obs |
|:---|:---|:---|:---|
| **vault-organizer** | `limpeza-raiz`, `marie-kondo` | ✅ Aprovada | Organização automática |
| **status-updater** | `atualizar-status` | ✅ Aprovada | Dashboard metrics |
| **session-logger** | `sync` | ✅ Aprovada | Comunicação Bi-IA |
| **github-sync** | `github-sync` | ✅ Ativa | Gestão de git (Já existe!) |
| **gemini-handoff** | `gemini` | ✅ Ativa | Delegação de tarefas |
| **kabak-agent** | `kabak-agent` | ✅ Ativa | Gestão específica KabaK |

### 🔍 Candidatas à Conversão (15)

*Filtradas de `.claude/commands/` e Workflows*

1. **validate** (Validação de arquivos/estrutura)
2. **mapa** (Gerador de índice)
3. **coach** (Orquestrador TDAH)
4. **claude-architect** (Guardião de padrões)
5. **ultra-think** (Análise profunda)
6. **learn** (Contexto aprendizado)
7. **work** (Contexto projetos)
8. **nevoa** (Orquestrador geral)
9. **elena** (Agente Produtividade)
10. **pedro** (Agente Tráfego)
11. **lucas** (Agente DeFi)
12. **alan** (Agente IA)
13. **dr-green** (Agente Cultivo)
14. **deep-research** (Workflow existente)
15. **obsidian-bridge** (Conceito novo)

---

## 2. 📊 Critérios de Seleção

Para entrar no Top 7, a skill deve pontuar alto em:

1. **Automatizabilidade (A):** Capacidade de ser transformada em script Python determinístico.
2. **Impacto (I):** Frequência de uso e valor agregado (economia de tempo/tokens).
3. **Independência (D):** Capacidade de rodar sem supervisão humana constante.

**Matriz de Decisão:**

| Candidata | A (1-10) | I (1-10) | D (1-10) | Pontuação | Decisão |
|:---|:---:|:---:|:---:|:---:|:---|
| **validate** | 10 | 10 | 10 | **30** | 🚀 **Top 1** |
| **mapa** | 10 | 9 | 10 | **29** | 🚀 **Top 2** |
| **architect** | 9 | 9 | 8 | **26** | 🚀 **Top 3** (Linter) |
| **coach** | 7 | 10 | 7 | **24** | 🚀 **Top 4** (Tools) |
| **deep-research**| 6 | 9 | 8 | **23** | 🚀 **Top 5** |
| **context** | 10 | 7 | 10 | **27** | 🚀 **Top 6** (Merge learn/work) |
| **idea-proc** | 5 | 8 | 6 | **19** | 🚀 **Top 7** (Ultra-Think) |
| *nevoa* | 3 | 8 | 4 | 15 | ❌ Manter Prompt |
| *personas* | 4 | 7 | 5 | 16 | ❌ Manter Prompt |

---

## 3. 🏆 Seleção Top 7 (Roadmap de Conversão)

### 1. `validate` (Filesystem Guardian)

* **Origem:** `.claude/commands/validate.md`
* **Função:** Validar nomes de arquivos, locais e atualizar MOCs automaticamente.
* **Lógica:** Regex checks, verificação de existência de pastas, leitura de `NOMENCLATURA.md`.
* **Impacto:** Elimina erro humano na criação de arquivos.

### 2. `mapa` (Vault Indexer)

* **Origem:** `.claude/commands/mapa.md`
* **Função:** Gerar arquivo `00_SISTEMA/INDICE_VAULT_COMPLETO.md` via script.
* **Lógica:** Walk directory, ignorar `.git`/`.obsidian`, formatar árvore Markdown, extrair H1s.
* **Impacto:** Economia massiva de tokens (Claude lê 1 arquivo vs 1000).

### 3. `architect-linter` (Codebase Auditor)

* **Origem:** `.claude/commands/claude-architect.md`
* **Função:** Scan proativo de violações de padrões (além de nomes).
* **Lógica:** Verificar H1 duplicados, links quebrados, arquivos na raiz, frontmatter ausente.
* **Impacto:** Mantém higiene do vault automaticamente.

### 4. `coach-tools` (TDAH Toolkit)

* **Origem:** `.claude/commands/coach.md`
* **Função:** Ferramentas mecânicas do Coach.
* **Lógica:** Timers (Pomodoro/Timebox), Log de check-in diário, Calculadora de Deep Work.
* **Impacto:** Transforma o Coach de "conselheiro" em "ferramenta ativa".

### 5. `deep-research` (Web & Vault Miner)

* **Origem:** Workflows `/deep-research-alan` e `alan.md`
* **Função:** Pesquisa profunda em múltiplas fontes.
* **Lógica:** Google Search API + Scraping + Summarization (uso pesado de LLM via script).
* **Impacto:** Automação de pesquisa que leva horas.

### 6. `context-manager` (Environment Switcher)

* **Origem:** `learn.md`, `work.md`
* **Função:** Prepara o ambiente para modos específicos.
* **Lógica:** Fecha abas irrelevantes (simulado), abre MOCs da área, exibe status do projeto, carrega prompts específicos.
* **Impacto:** Reduz fricção de troca de contexto.

### 7. `idea-processor` (Ultra-Think Engine)

* **Origem:** `ultra-think.md`
* **Função:** Framework de estruturação de pensamento.
* **Lógica:** Script que pega um "input vago" e força passar por 6 chapéus/etapas, gerando markdown estruturado.
* **Impacto:** Melhora qualidade de planejamento sem esforço cognitivo inicial.

---

## 4. 📅 Roadmap de Implementação (Fase 7.5+)

A execução será feita uma a uma, seguindo o padrão estabelecido:

1. Criar Prompt de Especificação (`PROMPT_Gemini_Criar_Skill_X.md`)
2. Gerar Estrutura (`.gemini/skills/X/`)
3. Implementar Scripts Python
4. Validar e Registrar

**Ordem Sugerida:**

1. **Semana 1:** `validate` + `mapa` (Quick Wins)
2. **Semana 2:** `context-manager` + `architect-linter` (Estruturais)
3. **Semana 3:** `coach-tools` (Complexidade Média)
4. **Semana 4:** `deep-research` + `idea-processor` (Alta Complexidade/IA)

---

## 5. 🛠️ Próximos Passos (Imediato)

1. Aprovar este plano.
2. Criar prompt para a Skill #1 (`validate`).
3. Iniciar implementação.
