---
criado: {{date}}
tipo: template
categoria: RPI Workflow
fase: Implementation Phase
uso: Individual implementation sub-plans within RPI workflow
---

# 🛠️ RPI IMPLEMENTATION PHASE: [NOME DO SUB-PLAN]

**Master Plan:** `[caminho/para/TEMPLATE_RPI_MASTER_PLAN.md]`
**Fase:** [Número da Fase] - [Nome da Fase]
**Sub-Plan:** [Número] (ex: 2.1, 3.4)
**Criado em:** [DD/MMM/YYYY]
**Status:** [NÃO INICIADO / EM PROGRESSO / COMPLETO / BLOQUEADO]

---

## 📋 OVERVIEW

### Objetivo

[Descreva em 1-2 frases o que este sub-plan específico alcança]

**Exemplo:**
> Implementar o Authorization Code Flow do OAuth2, incluindo endpoints de autorização, callback, e token exchange, com validação completa de PKCE.

### Contexto

**Por que estamos fazendo isso agora?**
[Explique como este sub-plan se encaixa no master plan]

**O que aconteceu antes?**
- [Sub-plan anterior 1] - [O que ele entregou]
- [Sub-plan anterior 2] - [O que ele entregou]

**O que vem depois?**
- [Sub-plan seguinte 1] - [O que ele vai fazer]
- [Sub-plan seguinte 2] - [O que ele vai fazer]

---

## ✅ PRE-REQUISITES

### Must Have (Bloqueadores)

- [ ] **[Pré-requisito 1]:** [Descrição] - **Status:** [Completo/Pendente]
- [ ] **[Pré-requisito 2]:** [Descrição] - **Status:** [Completo/Pendente]
- [ ] **[Pré-requisito 3]:** [Descrição] - **Status:** [Completo/Pendente]

### Nice to Have (Não-bloqueadores)

- [ ] [Item opcional 1]
- [ ] [Item opcional 2]

### Environment Setup

**Antes de começar, você precisa:**

```bash
# Commands to run
[comando 1]
[comando 2]
[comando 3]
```

**Environment Variables:**
```bash
[VAR_1]=[valor]
[VAR_2]=[valor]
```

**Dependencies to install:**
```bash
npm install [package1] [package2]
# ou
pip install [package1] [package2]
```

---

## 📁 FILES & COMPONENTS

### Files to Create

**Novos arquivos que serão criados:**

- [ ] `[caminho/arquivo1.ts]` - [Propósito]
- [ ] `[caminho/arquivo2.ts]` - [Propósito]
- [ ] `[caminho/arquivo3.test.ts]` - [Propósito]
- [ ] `[caminho/arquivo4.md]` - [Propósito]

### Files to Modify

**Arquivos existentes que serão modificados:**

- [ ] `[caminho/arquivo1.ts]` - [O que vai mudar]
- [ ] `[caminho/arquivo2.ts]` - [O que vai mudar]
- [ ] `[caminho/config.json]` - [O que vai mudar]

### Files to Delete

**Arquivos que serão removidos (se aplicável):**

- [ ] `[caminho/arquivo-obsoleto.ts]` - [Por que está sendo deletado]

---

## 🎯 IMPLEMENTATION STEPS

### Step 1: [Nome do Passo]

**Objetivo:** [O que este passo alcança]
**Duração estimada:** [X minutos/horas]

**Ações:**

1. [ ] [Ação específica 1]
   ```typescript
   // Code snippet se relevante
   ```

2. [ ] [Ação específica 2]
   ```typescript
   // Code snippet se relevante
   ```

3. [ ] [Ação específica 3]

**Validação imediata:**
- [ ] [Como verificar que este passo funcionou]
- [ ] [Comando para testar]

**Se algo der errado:**
- [Troubleshooting comum 1]
- [Troubleshooting comum 2]

---

### Step 2: [Nome do Passo]

**Objetivo:** [O que este passo alcança]
**Duração estimada:** [X minutos/horas]

**Ações:**

1. [ ] [Ação específica 1]
2. [ ] [Ação específica 2]
3. [ ] [Ação específica 3]

**Validação imediata:**
- [ ] [Como verificar]

**Se algo der errado:**
- [Troubleshooting]

---

### Step 3: [Nome do Passo]

[Repita o padrão acima para cada passo]

---

### Step 4: [Nome do Passo]

[Continue quantos steps forem necessários]

---

## 🧪 VALIDATION & TESTING

### Unit Tests

**Casos de teste a implementar:**

- [ ] **Test 1:** [Descrição do caso]
   ```typescript
   describe('[Nome do teste]', () => {
     it('should [comportamento esperado]', () => {
       // Test implementation
     });
   });
   ```

- [ ] **Test 2:** [Descrição do caso]
- [ ] **Test 3:** [Descrição do caso]

**Coverage Target:** [X%] (mínimo aceitável)
**Current Coverage:** [Y%]

### Integration Tests

**Fluxos a testar:**

- [ ] **Flow 1:** [Descrição]
   - **Setup:** [Como preparar]
   - **Action:** [O que fazer]
   - **Expected:** [Resultado esperado]

- [ ] **Flow 2:** [Descrição]
- [ ] **Flow 3:** [Descrição]

### Manual Testing Checklist

**Testes manuais necessários:**

- [ ] [Cenário 1] - **Expected:** [Resultado]
- [ ] [Cenário 2] - **Expected:** [Resultado]
- [ ] [Cenário 3] - **Expected:** [Resultado]
- [ ] [Cenário 4 - Edge case] - **Expected:** [Resultado]
- [ ] [Cenário 5 - Error case] - **Expected:** [Resultado]

### Commands to Run

**Para validar completude:**

```bash
# Run tests
npm test [caminho/tests]

# Run linter
npm run lint

# Build
npm run build

# Type check
npm run typecheck

# E2E (se aplicável)
npm run test:e2e
```

**Expected Output:**
```
✅ All tests passing (X/X)
✅ No lint errors
✅ Build successful
✅ No type errors
```

---

## 🎯 SUCCESS CRITERIA

### Definition of Done

**Este sub-plan só está completo quando:**

- [ ] **Funcionalidade:** Todos os steps implementados e funcionando
- [ ] **Testes:** 100% dos casos de teste passando (unit + integration)
- [ ] **Coverage:** Mínimo [X%] de cobertura nas áreas críticas
- [ ] **Build:** `npm run build` bem-sucedido sem warnings
- [ ] **Linter:** Zero erros de lint
- [ ] **Type Safety:** Zero erros de tipo (TypeScript/etc)
- [ ] **Manual QA:** Todos os cenários da checklist validados
- [ ] **Documentation:** README/docs atualizados se necessário
- [ ] **Code Review:** PR aprovado (se aplicável)
- [ ] **Backward Compat:** Nenhuma quebra de compatibilidade (se aplicável)

### Acceptance Criteria

**Critérios específicos para este sub-plan:**

- [ ] [Critério específico 1]
- [ ] [Critério específico 2]
- [ ] [Critério específico 3]

---

## ⚠️ EDGE CASES & ERROR HANDLING

### Known Edge Cases

**Casos especiais a considerar:**

1. **[Edge Case 1]:**
   - **Situação:** [Quando ocorre]
   - **Comportamento esperado:** [Como deve ser tratado]
   - **Implementado?** [ ] Sim / [ ] Não

2. **[Edge Case 2]:**
   - **Situação:** [Quando ocorre]
   - **Comportamento esperado:** [Como deve ser tratado]
   - **Implementado?** [ ] Sim / [ ] Não

### Error Scenarios

**Erros possíveis e como lidar:**

1. **[Error Scenario 1]:**
   - **Quando:** [Condição]
   - **Mensagem de erro:** `[Mensagem]`
   - **Recovery:** [Como recuperar]
   - **Implementado?** [ ] Sim / [ ] Não

2. **[Error Scenario 2]:**
   [Mesmo formato acima]

### Logging & Monitoring

**O que deve ser logado:**

- [ ] [Evento 1] - **Level:** [Info/Warn/Error]
- [ ] [Evento 2] - **Level:** [Info/Warn/Error]
- [ ] [Evento 3] - **Level:** [Info/Warn/Error]

**Alertas a configurar:**
- [ ] [Alerta 1] - **Threshold:** [Valor]
- [ ] [Alerta 2] - **Threshold:** [Valor]

---

## 🔄 ROLLBACK PLAN

### How to Rollback

**Se este sub-plan falhar, como reverter:**

```bash
# Commands to rollback
git revert [commit-hash]
# ou
git checkout [branch-anterior]
# ou
[comandos específicos]
```

### Rollback Checklist

- [ ] Reverter código
- [ ] Reverter migrations (se aplicável)
- [ ] Reverter configurações
- [ ] Notificar time
- [ ] Documentar causa da falha

### Safe Rollback Window

**Até quando é seguro fazer rollback?**
- [Timeframe] após deploy (ex: 24 horas)
- [Condições que invalidam rollback]

---

## 📊 PROGRESS TRACKING

### Implementation Progress

```
Overall: [████████░░] 80%

Step 1: [██████████] 100% ✅
Step 2: [██████████] 100% ✅
Step 3: [████████░░]  80% 🔄
Step 4: [░░░░░░░░░░]   0% ⏸️
Step 5: [░░░░░░░░░░]   0% ⏸️
```

### Test Progress

```
Unit Tests:        [██████████] 10/10 ✅
Integration Tests: [████░░░░░░]  2/5  🔄
Manual Tests:      [░░░░░░░░░░]  0/8  ⏸️
```

### Time Tracking

**Estimativa:** [X horas]
**Tempo real:** [Y horas]
**Variance:** [+/- Z%]

**Breakdown:**
- Step 1: [X min] (estimado: [Y min])
- Step 2: [X min] (estimado: [Y min])
- Step 3: [X min] (estimado: [Y min])

---

## 🚨 BLOCKERS & ISSUES

### Active Blockers

- 🚨 **[Blocker 1]:** [Descrição]
  - **Impact:** [Alto/Médio/Baixo]
  - **Owner:** [Nome]
  - **ETA:** [Data estimada resolução]
  - **Workaround:** [Se existe]

### Resolved Issues

- ✅ **[Issue 1]:** [Descrição] - **Resolved:** [DD/MMM] - [Como foi resolvido]
- ✅ **[Issue 2]:** [Descrição] - **Resolved:** [DD/MMM] - [Como foi resolvido]

### Questions & Decisions

- [ ] **Q1:** [Pergunta] - **Decision:** [Pendente/Decidido]
- [ ] **Q2:** [Pergunta] - **Decision:** [Pendente/Decidido]

---

## 📚 REFERENCES & DOCUMENTATION

### Code References

**Arquivos/funções relevantes:**
- `[caminho/arquivo.ts]` - [Descrição]
- `[caminho/arquivo.ts:Linha XX-YY]` - [Função específica]

### External Documentation

- [Nome do doc](URL) - [Por que é relevante]
- [Nome do doc](URL) - [Por que é relevante]

### Related PRs/Issues

- [PR #123](URL) - [Descrição]
- [Issue #456](URL) - [Descrição]

### Design Decisions

**Decisões importantes tomadas:**

1. **[Decisão 1]:** [Por que foi escolhida]
   - **Alternativas consideradas:** [Opções rejeitadas]
   - **Trade-offs:** [Prós e contras]

2. **[Decisão 2]:** [Por que foi escolhida]

---

## 💬 COMMUNICATION

### Team Updates

**Última atualização:** [DD/MMM/YYYY HH:MM]

**Status summary:**
[1-2 frases sobre o estado atual]

### Next Steps

**Próximas ações:**
1. [Ação 1]
2. [Ação 2]
3. [Ação 3]

### Help Needed

- [ ] **Help 1:** [Do que precisa] - **From:** [Quem pode ajudar]
- [ ] **Help 2:** [Do que precisa] - **From:** [Quem pode ajudar]

---

## 🎯 EXEMPLO PREENCHIDO

```markdown
# 🛠️ RPI IMPLEMENTATION PHASE: OAuth2 Authorization Code Flow

**Master Plan:** `docs/RPI_MASTER_AUTH_MIGRATION.md`
**Fase:** 2 - OAuth2 Core Implementation
**Sub-Plan:** 2.1
**Status:** EM PROGRESSO (80%)

## 📋 OVERVIEW

### Objetivo

Implementar o Authorization Code Flow do OAuth2 com suporte completo a PKCE, incluindo endpoints de autorização (/authorize), callback, e token exchange (/token).

### Contexto

**Por que agora?**
Este é o primeiro fluxo OAuth2 a ser implementado e é a base para os demais. Sem ele, não podemos migrar nenhum endpoint existente.

**O que aconteceu antes?**
- Sub-plan 1.3: Backward compatibility layer - permite JWT e OAuth2 coexistirem

**O que vem depois?**
- Sub-plan 2.2: Refresh Token Flow
- Sub-plan 2.3: Client Credentials Flow

## ✅ PRE-REQUISITES

### Must Have

- [X] **Database migrations:** Tables oauth_clients, oauth_codes, oauth_tokens - **Status:** Completo
- [X] **OAuth2 server package:** @node-oauth/oauth2-server installed - **Status:** Completo
- [ ] **Redis setup:** For code/token storage - **Status:** Pendente (blocker!)

## 📁 FILES & COMPONENTS

### Files to Create

- [X] `src/auth/oauth2/authorize.controller.ts` - Handle /authorize endpoint
- [X] `src/auth/oauth2/token.controller.ts` - Handle /token endpoint
- [ ] `src/auth/oauth2/pkce.service.ts` - PKCE validation logic
- [ ] `src/auth/oauth2/oauth2.service.test.ts` - Unit tests

### Files to Modify

- [X] `src/auth/auth.module.ts` - Register OAuth2 controllers
- [ ] `src/config/oauth2.config.ts` - Add PKCE settings

## 🎯 IMPLEMENTATION STEPS

### Step 1: Authorization Endpoint ✅

**Objetivo:** Implementar GET /oauth2/authorize
**Duração real:** 2 horas (estimado: 1.5h)

**Ações:**

1. [X] Create AuthorizeController
   ```typescript
   @Controller('oauth2')
   export class AuthorizeController {
     @Get('authorize')
     async authorize(@Query() query: AuthorizeDto) {
       // Generate authorization code
       // Store with PKCE challenge
       // Redirect to callback
     }
   }
   ```

2. [X] Validate client_id, redirect_uri, scope
3. [X] Generate authorization code (6-digit, 5min expiry)

**Validação:**
- [X] Endpoint responde 200 com valid params
- [X] Retorna 400 com invalid client_id

### Step 2: Token Exchange Endpoint ✅

**Objetivo:** Implementar POST /oauth2/token
**Duração real:** 3 horas (estimado: 2h)

**Ações:**

1. [X] Create TokenController
2. [X] Validate authorization code
3. [X] Verify PKCE code_verifier
4. [X] Issue access_token + refresh_token

**Validação:**
- [X] Can exchange valid code for tokens
- [X] PKCE validation rejects wrong verifier

### Step 3: PKCE Service 🔄 (CURRENT)

**Objetivo:** Extrair lógica PKCE em service reutilizável
**Duração estimada:** 1 hora

**Ações:**

1. [X] Create PKCEService
2. [ ] Extract challenge validation logic
3. [ ] Add unit tests

## 🧪 VALIDATION & TESTING

### Unit Tests

- [X] **AuthorizeController:** Should generate valid auth code - PASSING
- [X] **TokenController:** Should exchange code for tokens - PASSING
- [ ] **PKCEService:** Should validate code_verifier correctly - IN PROGRESS
- [ ] **PKCEService:** Should reject invalid verifier - PENDING

**Coverage:** 75% (target: 90%)

### Integration Tests

- [X] **Full flow:** authorize → callback → token exchange - PASSING
- [ ] **PKCE flow:** With code_challenge + code_verifier - IN PROGRESS
- [ ] **Error cases:** Invalid client, expired code, wrong verifier - PENDING

### Manual Testing

- [X] Valid authorization request redirects correctly
- [X] Token endpoint returns valid JWT
- [ ] PKCE validation blocks replay attacks
- [ ] Error messages are clear and secure (no leaks)

## 🎯 SUCCESS CRITERIA

- [X] Funcionalidade: Steps 1-2 completos, Step 3 em 80%
- [X] Testes: Unit tests principais passando
- [ ] Coverage: 90% (atual: 75%)
- [X] Build: Sucesso sem warnings
- [ ] Manual QA: 2/4 cenários validados
- [ ] Code Review: PR #234 aberto, aguardando review

## 🚨 BLOCKERS

- 🚨 **Redis não configurado em staging:** Preciso para testar token storage
  - **Impact:** Médio (posso usar in-memory temporariamente)
  - **Owner:** DevOps team
  - **ETA:** Amanhã
  - **Workaround:** Usando Map() in-memory

## 📊 PROGRESS

```
Overall: [████████░░] 80%

Step 1: [██████████] 100% ✅
Step 2: [██████████] 100% ✅
Step 3: [████████░░]  80% 🔄
```

**Estimativa:** 6 horas
**Tempo real:** 5 horas (até agora)
**Próximo:** Finalizar Step 3 (1h), depois integration tests (2h)
```

---

## 📌 NOTAS & LEARNINGS

### Lessons Learned

- [Lição aprendida durante implementação]
- [Algo que funcionou bem]
- [Algo que faria diferente]

### Future Improvements

- [ ] [Melhoria futura 1]
- [ ] [Melhoria futura 2]

---

**Template Version:** 1.0
**Criado por:** Claude Architect 🏛️
**Última atualização:** {{date}}
