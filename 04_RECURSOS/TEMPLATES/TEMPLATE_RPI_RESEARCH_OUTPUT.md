---
criado: {{date}}
tipo: template
categoria: RPI Workflow
fase: Research Phase
uso: Document research findings before planning implementation
---

# 🔍 RPI RESEARCH OUTPUT: [PROJETO/REFATORAÇÃO]

**Data da pesquisa:** [DD/MMM/YYYY]
**Pesquisador:** [Nome/Agente]
**Duração:** [X horas/dias]
**Status:** [EM ANDAMENTO / COMPLETO]

---

## 📋 RESEARCH OBJECTIVE

### What We're Investigating

[Descreva em 1-2 frases o objetivo da pesquisa]

**Exemplo:**
> Investigar a viabilidade de migrar o sistema de autenticação de JWT para OAuth2, identificando todos os pontos de dependência, riscos, e esforço estimado.

### Key Questions to Answer

1. **[Pergunta 1]:** [Pergunta específica que precisa ser respondida]
2. **[Pergunta 2]:** [Pergunta específica que precisa ser respondida]
3. **[Pergunta 3]:** [Pergunta específica que precisa ser respondida]
4. **[Pergunta 4]:** [Pergunta específica que precisa ser respondida]

### Scope of Research

**In Scope:**
- ✅ [Área de investigação 1]
- ✅ [Área de investigação 2]
- ✅ [Área de investigação 3]

**Out of Scope:**
- ❌ [Área não investigada 1]
- ❌ [Área não investigada 2]

---

## 🗺️ CODEBASE CONTEXT

### Current Architecture Overview

**High-level description:**
[Descreva a arquitetura atual relevante para esta pesquisa]

**Exemplo:**
> Sistema atual usa JWT com refresh tokens. Auth server centralizado (auth-service), 12 microserviços consumidores. User data em PostgreSQL (3 schemas separados: users, admins, external_users).

### Key Components

#### Component 1: [Nome]

**Location:** `[caminho/para/component]`
**Purpose:** [O que faz]
**Technology:** [Linguagem/Framework]
**Size:** [LOC/Complexidade]
**Dependencies:** [Lista de dependências]

**Relevância para projeto:**
[Por que este componente é importante para o que vamos fazer]

---

#### Component 2: [Nome]

[Mesmo formato acima]

---

#### Component 3: [Nome]

[Continue para todos componentes relevantes]

---

### File Inventory

**Critical files identified:**

| File Path | Purpose | LOC | Complexity | Impact |
|-----------|---------|-----|------------|--------|
| `[caminho/arquivo1.ts]` | [Propósito] | [XXX] | [Alta/Média/Baixa] | [Crítico/Alto/Médio/Baixo] |
| `[caminho/arquivo2.ts]` | [Propósito] | [XXX] | [Alta/Média/Baixa] | [Crítico/Alto/Médio/Baixo] |
| `[caminho/arquivo3.ts]` | [Propósito] | [XXX] | [Alta/Média/Baixa] | [Crítico/Alto/Médio/Baixo] |

**Total files to modify:** [X]
**Total LOC impacted:** [Y]

### Dependencies Map

**Internal dependencies:**

```
[Service A] → [Service B] → [Service C]
     ↓            ↓            ↓
[Database]   [Cache]      [Queue]
```

**External dependencies:**

- **[Dependency 1]:** [Nome] v[Versão] - [Como é usado]
- **[Dependency 2]:** [Nome] v[Versão] - [Como é usado]
- **[Dependency 3]:** [Nome] v[Versão] - [Como é usado]

### Data Flow Analysis

**Current flow:**

```
[User] → [Frontend] → [API Gateway] → [Auth Service]
                           ↓
                      [Database]
                           ↓
                    [Other Services]
```

**Details:**
1. [Passo 1 do fluxo] - [Descrição]
2. [Passo 2 do fluxo] - [Descrição]
3. [Passo 3 do fluxo] - [Descrição]

---

## 🔎 DETAILED FINDINGS

### Finding 1: [Título]

**Category:** [Architecture / Security / Performance / Technical Debt]
**Severity:** [Crítico / Alto / Médio / Baixo]
**Discovered:** [DD/MMM/YYYY]

**Description:**
[Descrição detalhada do que foi encontrado]

**Evidence:**
- **File:** `[caminho/arquivo.ts:linhas XX-YY]`
- **Code snippet:**
  ```typescript
  // Código relevante
  ```
- **Metrics:** [Se aplicável - ex: "47 endpoints afetados"]

**Impact:**
- [Impacto 1]
- [Impacto 2]
- [Impacto 3]

**Implications for project:**
[Como isso afeta o que queremos fazer]

---

### Finding 2: [Título]

[Mesmo formato acima]

---

### Finding 3: [Título]

[Continue para todos os findings relevantes]

---

## ⚠️ ISSUES & PROBLEMS IDENTIFIED

### Critical Issues

#### Issue 1: [Título]

**Severity:** 🚨 Crítico
**Area:** [Área afetada]
**Discovered in:** `[caminho/arquivo.ts]`

**Problem:**
[Descrição clara do problema]

**Why it's critical:**
[Por que isso é crítico para o projeto]

**Must be addressed:** [Before/During/After] implementation

**Estimated effort:** [X horas/dias]

---

#### Issue 2: [Título]

[Mesmo formato]

---

### High Priority Issues

#### Issue 3: [Título]

**Severity:** ⚠️ Alto
[Mesmo formato que Critical]

---

### Medium/Low Priority Issues

[Lista mais concisa para issues menos críticas]

- ℹ️ **[Issue]:** [Descrição curta] - **Area:** [Área] - **Effort:** [X]
- ℹ️ **[Issue]:** [Descrição curta] - **Area:** [Área] - **Effort:** [X]

---

## 🎯 OPPORTUNITIES & IMPROVEMENTS

### Quick Wins

**Melhorias fáceis identificadas:**

1. **[Oportunidade 1]:** [Descrição]
   - **Benefit:** [Benefício]
   - **Effort:** [Baixo/Médio]
   - **Can be done:** [Antes/Durante/Depois]

2. **[Oportunidade 2]:** [Descrição]

### Long-term Improvements

**Melhorias que requerem mais esforço:**

1. **[Melhoria 1]:** [Descrição]
   - **Benefit:** [Benefício]
   - **Effort:** [Alto]
   - **Dependencies:** [O que precisa antes]

2. **[Melhoria 2]:** [Descrição]

---

## 🚨 RISK ASSESSMENT

### Risk Matrix

| Risk | Probability | Impact | Severity | Mitigation |
|------|-------------|--------|----------|------------|
| [Risco 1] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | 🚨 Crítico | [Como mitigar] |
| [Risco 2] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | ⚠️ Alto | [Como mitigar] |
| [Risco 3] | [Alta/Média/Baixa] | [Alto/Médio/Baixo] | ℹ️ Médio | [Como mitigar] |

### Detailed Risk Analysis

#### Risk 1: [Título]

**Probability:** [Alta/Média/Baixa]
**Impact:** [Alto/Médio/Baixo]
**Overall Severity:** 🚨 Crítico

**Description:**
[O que pode dar errado]

**Indicators:**
- [Como identificaremos se está acontecendo]
- [Sinais de alerta]

**Mitigation Strategy:**
1. [Ação preventiva 1]
2. [Ação preventiva 2]
3. [Plano B se ocorrer]

**Owner:** [Quem é responsável por monitorar]

---

#### Risk 2: [Título]

[Mesmo formato]

---

### Risk Acceptance

**Risks we're accepting:**
- [Risco aceito 1] - **Reason:** [Por que estamos aceitando]
- [Risco aceito 2] - **Reason:** [Por que estamos aceitando]

---

## 📊 COMPLEXITY ANALYSIS

### Complexity Metrics

**Overall Project Complexity:** [Alta/Média/Baixa]

**Breakdown:**

| Area | Complexity | Reason |
|------|------------|--------|
| [Área 1] | 🔴 Alta | [Por que] |
| [Área 2] | 🟡 Média | [Por que] |
| [Área 3] | 🟢 Baixa | [Por que] |

### Effort Estimation

**Rough estimates (planning phase will refine):**

- **Development:** [X dias/semanas]
- **Testing:** [Y dias/semanas]
- **Documentation:** [Z dias]
- **Total:** [W dias/semanas]

**Confidence Level:** [Alta/Média/Baixa]
**Basis:** [Em que baseamos esta estimativa]

### Team Requirements

**Skills needed:**
- [Skill 1] - [Nível requerido]
- [Skill 2] - [Nível requerido]
- [Skill 3] - [Nível requerido]

**Team size:** [X pessoas]
**Duration:** [Y semanas]

---

## 🔗 DEPENDENCIES & INTEGRATIONS

### External Systems

**Systems that will be affected:**

#### System 1: [Nome]

**Type:** [Database/API/Service/etc]
**Owner:** [Time/Pessoa]
**Impact:** [Crítico/Alto/Médio/Baixo]

**Integration points:**
- [Ponto de integração 1]
- [Ponto de integração 2]

**Changes required:**
- [Mudança necessária 1]
- [Mudança necessária 2]

**Coordination needed:** [Sim/Não]
**Contact:** [Nome/Email]

---

#### System 2: [Nome]

[Mesmo formato]

---

### Third-Party Dependencies

**External services/libraries:**

| Dependency | Current Version | Needs Update? | Breaking Changes? | Effort |
|------------|----------------|---------------|-------------------|--------|
| [Nome] | v[X.Y.Z] | [Sim/Não] | [Sim/Não] | [Baixo/Médio/Alto] |
| [Nome] | v[X.Y.Z] | [Sim/Não] | [Sim/Não] | [Baixo/Médio/Alto] |

---

## 📈 TESTING CONSIDERATIONS

### Current Test Coverage

**Existing coverage:**
- **Unit tests:** [X%] ([Y/Z] files covered)
- **Integration tests:** [X%] ([Y/Z] flows covered)
- **E2E tests:** [X%] ([Y/Z] scenarios covered)

**Gaps identified:**
- ❌ [Área sem cobertura 1]
- ❌ [Área sem cobertura 2]
- ❌ [Área sem cobertura 3]

### Testing Strategy Recommendations

**For this project, we should:**

- [ ] **Unit tests:** [Target coverage %] - [Áreas críticas]
- [ ] **Integration tests:** [Quantos novos testes] - [Fluxos críticos]
- [ ] **E2E tests:** [Quantos novos testes] - [Cenários críticos]
- [ ] **Manual QA:** [Checklist de cenários]
- [ ] **Performance tests:** [Benchmarks a estabelecer]

### Test Data Requirements

**Data needed for testing:**
- [Dataset 1] - [Propósito]
- [Dataset 2] - [Propósito]
- [Dataset 3] - [Propósito]

---

## 💡 RECOMMENDATIONS

### Primary Recommendation

**We recommend:** [Prosseguir / Prosseguir com ajustes / Não prosseguir / Alternativa]

**Reasoning:**
[Justificativa clara da recomendação]

### Recommended Approach

**High-level strategy:**

1. **Phase 1:** [O que fazer primeiro]
2. **Phase 2:** [O que fazer depois]
3. **Phase 3:** [O que fazer por último]

**Why this order:**
[Justificativa da sequência]

### Alternatives Considered

#### Alternative 1: [Nome]

**Pros:**
- [Pro 1]
- [Pro 2]

**Cons:**
- [Con 1]
- [Con 2]

**Why not chosen:**
[Razão da rejeição]

---

#### Alternative 2: [Nome]

[Mesmo formato]

---

### Things to Avoid

**Don't do this:**

- ❌ **[Antipattern 1]:** [Por que evitar]
- ❌ **[Antipattern 2]:** [Por que evitar]
- ❌ **[Antipattern 3]:** [Por que evitar]

---

## 📝 OPEN QUESTIONS

### Critical Questions (Blockers)

- [ ] **Q1:** [Pergunta crítica que precisa resposta antes de planejar]
  - **Why critical:** [Impacto se não responder]
  - **Who can answer:** [Nome/Time]
  - **By when:** [Data limite]

- [ ] **Q2:** [Pergunta crítica]

### Important Questions (Non-blockers)

- [ ] **Q3:** [Pergunta importante mas não bloqueadora]
  - **Impact:** [O que mudaria com a resposta]
  - **Can proceed without:** [Sim/Não]

- [ ] **Q4:** [Pergunta importante]

### Nice to Know

- [ ] **Q5:** [Pergunta opcional]
- [ ] **Q6:** [Pergunta opcional]

---

## 📚 RESEARCH METHODOLOGY

### How Research Was Conducted

**Tools used:**
- [Tool 1] - [Para que foi usado]
- [Tool 2] - [Para que foi usado]

**Methods:**
- [Método 1] - [Descrição]
- [Método 2] - [Descrição]

**Code analysis:**
- **Files examined:** [X]
- **Lines of code reviewed:** [Y]
- **Time spent:** [Z horas]

### Search Patterns Used

```bash
# Grep patterns
grep -r "[pattern1]" src/
grep -r "[pattern2]" src/

# Glob patterns
**/*.ts
**/auth/**/*.ts
```

### Limitations

**Research limitations:**
- [Limitação 1] - [Como isso afeta os findings]
- [Limitação 2] - [Como isso afeta os findings]

---

## 🎯 NEXT STEPS

### Immediate Actions

**Before moving to planning phase:**

1. [ ] **[Ação 1]:** [Descrição] - **Owner:** [Nome] - **By:** [Data]
2. [ ] **[Ação 2]:** [Descrição] - **Owner:** [Nome] - **By:** [Data]
3. [ ] **[Ação 3]:** [Descrição] - **Owner:** [Nome] - **By:** [Data]

### Pre-Planning Requirements

**Must have before planning:**

- [ ] [Requirement 1]
- [ ] [Requirement 2]
- [ ] [Requirement 3]

### Ready for Planning?

**Checklist:**

- [ ] All critical questions answered
- [ ] Key risks identified and understood
- [ ] Architecture context documented
- [ ] Dependencies mapped
- [ ] Effort estimated (rough)
- [ ] Stakeholders identified
- [ ] No critical blockers

**Status:** [✅ Ready / ⚠️ Ready with caveats / ❌ Not ready]

**If not ready, blocking issues:**
- [Blocker 1]
- [Blocker 2]

---

## 📊 RESEARCH SUMMARY (Executive Summary)

### TL;DR

**In 3 sentences:**
[Resumo executivo de 3 frases dos principais findings]

### Key Metrics

- **Files to modify:** [X]
- **LOC impacted:** [Y]
- **Critical issues:** [Z]
- **High risks:** [W]
- **Estimated effort:** [A-B semanas]

### Go/No-Go Recommendation

**Recommendation:** [GO / GO WITH CAUTION / NO-GO / NEEDS MORE RESEARCH]

**Confidence:** [Alta/Média/Baixa]

**Rationale:**
[1-2 frases explicando a recomendação]

---

## 🎯 EXEMPLO PREENCHIDO

```markdown
# 🔍 RPI RESEARCH OUTPUT: Auth System OAuth2 Migration

**Data:** 10/JAN/2026
**Pesquisador:** Claude Architect + DevOps Team
**Duração:** 3 dias (24h total effort)
**Status:** COMPLETO

## 📋 RESEARCH OBJECTIVE

### What We're Investigating

Investigar viabilidade técnica de migrar sistema de autenticação de JWT para OAuth2, mapear todos os 47 endpoints afetados, identificar riscos de downtime, e estimar esforço total.

### Key Questions

1. **Quantos endpoints usam JWT?** → 47 endpoints identificados
2. **Podemos manter backward compatibility?** → Sim, por 90 dias
3. **Qual o risco de downtime?** → Baixo se faseado corretamente
4. **Esforço total?** → 6-8 semanas com 2 devs

## 🗺️ CODEBASE CONTEXT

### Current Architecture

Sistema atual: Auth centralizado (auth-service), JWT com refresh tokens, 12 microserviços consumidores, user data fragmentado em 3 schemas PostgreSQL (users, admins, external_users).

### Key Components

#### Component 1: Auth Service

**Location:** `services/auth-service/`
**Technology:** Node.js (Express) + TypeScript
**Size:** 8,500 LOC
**Dependencies:** jsonwebtoken, bcrypt, pg

**Relevância:** Core do sistema. Todos os 47 endpoints passam por aqui.

#### Component 2: API Gateway

**Location:** `services/api-gateway/`
**Technology:** Node.js (NestJS)
**Size:** 12,000 LOC

**Relevância:** Valida JWT em todo request. Precisa suportar OAuth2 também.

### File Inventory

| File | Purpose | LOC | Complexity | Impact |
|------|---------|-----|------------|--------|
| `auth-service/src/auth/jwt.service.ts` | JWT generation/validation | 450 | Alta | Crítico |
| `auth-service/src/auth/auth.controller.ts` | Login endpoints | 680 | Média | Crítico |
| `api-gateway/src/auth/jwt.middleware.ts` | Token validation | 320 | Alta | Crítico |

**Total:** 47 files, ~15,000 LOC impacted

## 🔎 DETAILED FINDINGS

### Finding 1: Token Expiry Inconsistency

**Category:** Security
**Severity:** 🚨 Crítico

**Description:**
8 endpoints (legacy v1 API) não validam token expiry. Tokens expirados há meses ainda funcionam.

**Evidence:**
- File: `auth-service/src/v1/legacy-auth.ts:lines 45-78`
- Code:
  ```typescript
  // TODO: Add expiry validation
  jwt.verify(token, SECRET); // Missing exp check!
  ```

**Impact:**
- Security vulnerability crítica
- Precisa ser corrigido ANTES da migração OAuth2
- Afeta ~15% dos usuários (legacy clients)

**Implications:**
Devemos criar Sub-Plan 1.1 "Fix Legacy Token Expiry" como pré-requisito.

### Finding 2: Database Fragmentation

**Category:** Architecture
**Severity:** ⚠️ Alto

**Description:**
User data em 3 schemas diferentes (users, admins, external_users) com estruturas inconsistentes. OAuth2 precisa de user store unificado.

**Impact:**
- Adiciona complexidade significativa
- Estimativa aumenta de 6 para 8 semanas
- Requer DB migration como Fase 1

## ⚠️ ISSUES IDENTIFIED

### Critical Issues

#### Issue 1: No Integration Tests

**Severity:** 🚨 Crítico
**Area:** Testing

**Problem:**
Zero integration tests para fluxo de auth. Apenas 12 unit tests (coverage: 30%).

**Must be addressed:** BEFORE implementation
**Estimated effort:** 2 semanas (criar test infrastructure)

## 🚨 RISK ASSESSMENT

| Risk | Probability | Impact | Severity | Mitigation |
|------|-------------|--------|----------|------------|
| Downtime during migration | Média | Alto | 🚨 Crítico | Phased rollout com feature flags |
| Breaking mobile apps | Alta | Alto | 🚨 Crítico | 90-day backward compat period |
| DB migration fails | Baixa | Crítico | ⚠️ Alto | Dry-run + rollback plan |

## 📊 COMPLEXITY ANALYSIS

**Overall:** 🟡 Média-Alta

| Area | Complexity | Reason |
|------|------------|--------|
| Auth Service | 🔴 Alta | Core critical, muitos edge cases |
| API Gateway | 🟡 Média | Middleware complexo mas bem testado |
| Microservices | 🟢 Baixa | Apenas consumer, fácil atualizar |

**Effort:** 6-8 semanas (2 devs senior)
**Confidence:** Alta (já fizemos OAuth2 em outro projeto)

## 💡 RECOMMENDATIONS

**We recommend:** ✅ Prosseguir com ajustes

**Approach:**
1. **Phase 1 (2 sem):** Fix legacy issues + DB unification
2. **Phase 2 (2 sem):** Implement OAuth2 core
3. **Phase 3 (2 sem):** Migrate endpoints (batch 15-16 each)
4. **Phase 4 (1 sem):** Testing + rollout
5. **Phase 5 (1 sem):** Monitor + deprecate JWT

**Total:** 8 semanas

## 📝 OPEN QUESTIONS

- [X] **Q1:** Podemos ter downtime de 5min para DB migration? → SIM (approved by CTO)
- [ ] **Q2:** Mobile apps podem atualizar em 90 dias? → Waiting PM confirmation
- [X] **Q3:** Redis disponível em staging? → SIM

## 🎯 NEXT STEPS

### Immediate Actions

1. [X] Get CTO approval for 8-week timeline → APPROVED
2. [ ] Confirm mobile app update timeline → Waiting
3. [ ] Schedule kickoff meeting → 15/JAN 10am

### Ready for Planning?

- [X] All critical questions answered
- [X] Key risks identified
- [X] Architecture mapped
- [X] No critical blockers

**Status:** ✅ READY FOR PLANNING PHASE

## 📊 EXECUTIVE SUMMARY

**TL;DR:**
OAuth2 migration é viável mas complexa. Requer 8 semanas (2 devs), DB unification primeiro, phased rollout essencial. Principais riscos: breaking mobile apps (mitigado com 90-day compat) e downtime (mitigado com feature flags).

**Recommendation:** GO WITH CAUTION
**Confidence:** Alta
```

---

## 📎 ATTACHMENTS

### Code Samples

[Anexar snippets relevantes que não cabem nas seções acima]

### Diagrams

[Links para diagramas criados: arquitetura, fluxos, etc]

### Spreadsheets

[Links para análises quantitativas: metrics, estimativas, etc]

---

## 📌 METADATA

**Research Tags:** [Tag1] [Tag2] [Tag3]
**Related Projects:** [Link para projetos relacionados]
**Reviewed by:** [Nome] - [Data]

**Approved to proceed to planning:** [ ] Yes / [ ] No / [ ] Conditional

---

**Template Version:** 1.0
**Criado por:** Claude Architect 🏛️
**Última atualização:** {{date}}
