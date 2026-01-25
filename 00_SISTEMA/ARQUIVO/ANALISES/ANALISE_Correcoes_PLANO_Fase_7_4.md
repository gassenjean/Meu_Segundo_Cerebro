# ANÁLISE: Correções PLANO_Fase_7_4 (Claude Code)

**Data:** 18/JAN/2026
**Revisor:** Claude Code
**Documento Original:** `00_SISTEMA/planejamento/PLANO_Fase_7_4_Conversao_Top_7_Skills.md`
**Status:** REVISÃO CRÍTICA NECESSÁRIA

---

## 🎯 RESUMO EXECUTIVO

O PLANO_Fase_7_4 criado pelo Gemini tem **boa metodologia** (matriz de decisão, critérios claros), mas contém **erros críticos de inventário** e **seleções questionáveis** que precisam ser corrigidas antes da execução.

---

## ❌ ERRO CRÍTICO #1: Inventário Incorreto

### Problema

O Gemini listou **6 skills como "Já Convertidas/Nativas Antigravity"**, mas apenas **3 existem**:

**Gemini listou:**
1. vault-organizer ✅ CORRETO (existe em `.gemini/skills/`)
2. status-updater ✅ CORRETO (existe em `.gemini/skills/`)
3. session-logger ✅ CORRETO (existe em `.gemini/skills/`)
4. github-sync ❌ **ERRO** (é skill Claude em `.claude/commands/`, NÃO Antigravity)
5. gemini-handoff ❌ **ERRO** (é skill Claude `/gemini`, NÃO Antigravity)
6. kabak-agent ❌ **ERRO** (é skill Claude, NÃO Antigravity)

### Causa

Confusão entre:
- **Antigravity Skills** (`.gemini/skills/` - scripts Python executáveis)
- **Claude Skills** (`.claude/commands/` - prompts/contexto)

### Correção Necessária

**Inventário correto:**
- **Antigravity Skills existentes:** 3 (vault-organizer, status-updater, session-logger)
- **Claude Skills existentes:** 17+ (incluindo github-sync, gemini, kabak-agent, etc.)
- **Total skills no sistema bi-IA:** 20+ (3 Antigravity + 17 Claude)

---

## ⚠️ PROBLEMA #2: Seleções Questionáveis (Top 7)

### Skills Selecionadas - Análise Individual

#### ✅ APROVADAS SEM RESSALVAS (3)

**1. validate (30 pts) - PERFEITA**
- Automatizabilidade: 10/10 ✅
- Impacto: 10/10 ✅ (usado sempre ao criar arquivo)
- Independência: 10/10 ✅
- **Decisão:** APROVAR como Skill #1 (prioridade máxima)

**2. mapa (29 pts) - PERFEITA**
- Automatizabilidade: 10/10 ✅
- Impacto: 9/10 ✅ (economia massiva de tokens)
- Independência: 10/10 ✅
- **Decisão:** APROVAR como Skill #2 (prioridade máxima)

**3. context-manager (27 pts) - MUITO BOA**
- Automatizabilidade: 10/10 ✅
- Impacto: 7/10 ✅
- Independência: 10/10 ✅
- **Decisão:** APROVAR como Skill #3 (prioridade alta)

#### ⚠️ APROVADA COM RESSALVAS (1)

**4. architect-linter (26 pts) - BOA MAS RESTRITA**
- Automatizabilidade: 9/10 ✅
- Impacto: 9/10 ✅
- Independência: 8/10 ⚠️
- **Problema:** Escopo muito amplo. Claude Architect é guardião estratégico, não apenas linter mecânico.
- **Solução:** Limitar escopo a checks **puramente mecânicos**:
  - ✅ H1 duplicados (regex)
  - ✅ Links quebrados (file exists)
  - ✅ Arquivos na raiz (listdir)
  - ✅ Frontmatter ausente (regex)
  - ❌ Análise semântica (manter em Claude)
  - ❌ Decisões arquiteturais (manter em Claude)
- **Decisão:** APROVAR como Skill #4 com **escopo limitado documentado**

#### ❌ NÃO APROVADAS (3)

**5. coach-tools (24 pts) - PROBLEMÁTICA**
- Automatizabilidade: 7/10 ⚠️
- Impacto: 10/10 ✅
- Independência: 7/10 ⚠️
- **Problema:** Coach (`/coach`) é **orquestrador estratégico TDAH**, não conjunto de ferramentas mecânicas. A skill proposta (timers, check-ins) captura <30% do valor do Coach.
- **Alternativa sugerida:**
  - Criar `pomodoro-timer` separado (simples, focado)
  - Manter `/coach` como prompt estratégico Claude
- **Decisão:** **NÃO APROVAR** coach-tools na forma proposta. Considerar `pomodoro-timer` em fase futura.

**6. deep-research (23 pts) - MUITO COMPLEXA**
- Automatizabilidade: 6/10 ❌
- Impacto: 9/10 ✅
- Independência: 8/10 ⚠️
- **Problemas técnicos:**
  - Requer Google Search API (pago ou com limites rígidos)
  - Web scraping (frágil, anti-bot, quebra facilmente)
  - Summarization via LLM (consome tokens free tier Gemini)
  - Complexidade arquitetural muito alta para Antigravity Skill
  - Viabilidade técnica: BAIXA
- **Decisão:** **NÃO APROVAR** para Fase 7.4. Manter como workflow Claude ou adiar para fase futura (7.6+) quando infraestrutura estiver pronta.

**7. idea-processor (19 pts) - NÃO AUTOMATIZÁVEL**
- Automatizabilidade: 5/10 ❌
- Impacto: 8/10 ✅
- Independência: 6/10 ❌
- **Problema fundamental:** Ultra-think (`/ultra-think`) é **framework de raciocínio multi-dimensional**, não processo mecânico. Depende de:
  - Input criativo humano
  - Contexto situacional
  - Julgamento estratégico
  - Iteração interativa
- **Decisão:** **NÃO APROVAR** para Fase 7.4. Manter `/ultra-think` como prompt Claude (seu valor está na orquestração de pensamento, não automação).

---

## 🎯 PLANO REVISADO (Top 4 em vez de Top 7)

### Justificativa

**Qualidade > Quantidade**

Melhor ter **4 skills sólidas, viáveis e de alto impacto** do que 7 skills com 3 problemáticas que:
- Consomem tempo de desenvolvimento
- Podem falhar tecnicamente
- Entregam <50% do valor esperado

### Skills Aprovadas (Top 4)

| # | Skill | Pontuação | Prioridade | Viabilidade | Impacto Real |
|---|-------|-----------|------------|-------------|--------------|
| 1 | validate | 30 | MÁXIMA | ALTA | 10/10 |
| 2 | mapa | 29 | MÁXIMA | ALTA | 9/10 |
| 3 | context-manager | 27 | ALTA | ALTA | 7/10 |
| 4 | architect-linter* | 26 | MÉDIA | MÉDIA-ALTA | 8/10 |

**\*architect-linter:** Escopo limitado a checks mecânicos (documentado em especificações)

### Roadmap Revisado

**Fase 7.4 (Conversão Top 4) - 2 semanas:**
- **Semana 1:** validate + mapa (Quick Wins)
- **Semana 2:** context-manager + architect-linter (escopo limitado)

**Fase 7.5 (Expansão) - Futuro:**
- pomodoro-timer (extraído do conceito coach-tools)
- Outras skills conforme surgirem necessidades validadas

**Fase 7.6+ (Avançado) - Futuro distante:**
- deep-research (quando resolver APIs, custos, infraestrutura)
- Outras skills complexas que requerem pesquisa prévia

---

## 📋 CORREÇÕES ESPECÍFICAS A FAZER

### Correção 1: Atualizar Inventário

**Arquivo:** `PLANO_Fase_7_4_Conversao_Top_7_Skills.md`

**Seção 1 (Inventário & Status Atual):**

```markdown
### ✅ Já Convertidas / Nativas (3) ← CORRIGIR: era 6

| Skill Antigravity | Origem Claude | Status | Obs |
|:---|:---|:---|:---|
| **vault-organizer** | `limpeza-raiz`, `marie-kondo` | ✅ Aprovada | Organização automática |
| **status-updater** | `atualizar-status` | ✅ Aprovada | Dashboard metrics |
| **session-logger** | `sync` | ✅ Aprovada | Comunicação Bi-IA |

**Nota:** Skills Claude (`github-sync`, `gemini`, `kabak-agent`) permanecem como comandos Claude (`.claude/commands/`). Não são Antigravity Skills.
```

### Correção 2: Atualizar Seleção Top 7 → Top 4

**Seção 3 (Seleção Top 7):**

Renomear para: **"Seleção Top 4 (Roadmap de Conversão)"**

Remover skills:
- ~~coach-tools~~ (justificativa: escopo inadequado, manter Coach como prompt)
- ~~deep-research~~ (justificativa: complexidade alta, adiar para fase futura)
- ~~idea-processor~~ (justificativa: não automatizável, manter ultra-think como prompt)

Adicionar nota sobre architect-linter:
```markdown
### 4. `architect-linter` (Codebase Auditor) - ESCOPO LIMITADO

* **Origem:** `.claude/commands/claude-architect.md`
* **Função:** Scan proativo de violações de padrões (APENAS checks mecânicos).
* **Lógica:**
  - ✅ Verificar H1 duplicados (regex)
  - ✅ Verificar links quebrados (file exists)
  - ✅ Verificar arquivos na raiz (listdir)
  - ✅ Verificar frontmatter ausente (regex)
  - ❌ NÃO fazer análise semântica (manter em Claude)
  - ❌ NÃO fazer decisões arquiteturais (manter em Claude)
* **Impacto:** Mantém higiene do vault automaticamente (checks básicos).
* **Nota:** Claude Architect continua como guardião estratégico. Esta skill é apenas o "linter" mecânico.
```

### Correção 3: Atualizar Roadmap

**Seção 4 (Roadmap de Implementação):**

```markdown
**Ordem Revisada (Top 4):**

1. **Semana 1:** `validate` + `mapa` (Quick Wins - Alta viabilidade, alto impacto)
2. **Semana 2:** `context-manager` + `architect-linter` (Estruturais - Escopo bem definido)

**Removidas da Fase 7.4:**
- `coach-tools` → Reconsiderar como `pomodoro-timer` (simples) em fase futura
- `deep-research` → Adiar para Fase 7.6+ (resolver APIs, custos, infraestrutura)
- `idea-processor` → Manter `/ultra-think` como prompt Claude (não automatizável)
```

---

## 🎓 APRENDIZADOS

### O Que Funcionou Bem

1. **Metodologia de seleção:** Matriz A+I+D é sólida
2. **Documentação clara:** Cada skill bem descrita
3. **Quick wins identificados:** validate + mapa são escolhas perfeitas

### O Que Precisa Melhorar

1. **Verificação de inventário:** Sempre validar arquivos físicos (`.gemini/skills/` vs `.claude/commands/`)
2. **Escopo realista:** Nem tudo que é valioso é automatizável
3. **Viabilidade técnica:** Avaliar dependências externas (APIs, custos) antes de aprovar
4. **Valor core vs periférico:** Coach é estratégico (core), timer é mecânico (periférico). Não confundir.

---

## ✅ PRÓXIMOS PASSOS

### Para Gemini (Imediato)

1. **LER** esta análise completa
2. **CORRIGIR** PLANO_Fase_7_4 conforme seções "Correções Específicas"
3. **CRIAR** versão revisada: `PLANO_Fase_7_4_Conversao_Top_4_REVISADO.md`
4. **APROVAR** apenas após Claude validar versão revisada

### Para Claude (Validação)

1. Revisar PLANO_Fase_7_4_REVISADO quando Gemini criar
2. Se aprovado: Autorizar início da implementação (Skill #1: validate)
3. Atualizar MOC_Skills_BiIA.md com roadmap revisado

---

## 📊 MÉTRICAS DE IMPACTO (Projetadas)

### Top 4 Aprovadas

**validate:**
- Economia de erros: ~95% (quase zero arquivos com nomenclatura errada)
- Uso estimado: 5-10x por dia

**mapa:**
- Economia de tokens: ~50-80k tokens por sessão (Claude lê 1 índice vs 1000 arquivos)
- Uso estimado: 1x por sessão (início)

**context-manager:**
- Economia de tempo: ~2-3 min por troca de contexto
- Uso estimado: 3-5x por dia

**architect-linter:**
- Economia de tempo: ~10-15 min de auditoria manual por semana
- Uso estimado: 1x por semana (automatizado)

**Total estimado:**
- Economia de tokens: 100-200k tokens/dia
- Economia de tempo: 30-45 min/dia
- Redução de erros: 80-90%

---

**Versão:** 1.0
**Status:** ANÁLISE COMPLETA
**Próxima ação:** Gemini corrigir PLANO_Fase_7_4 → Claude validar → Iniciar implementação
