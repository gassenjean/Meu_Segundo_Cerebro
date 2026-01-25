# WORKFLOWS AVANÇADOS - CLAUDE CODE (TÉCNICAS COMBINADAS)

**Baseado em:** 13 Dicas do Boris + Melhores Práticas
**Nível:** Avançado
**Objetivo:** Workflows production-ready combinando múltiplas técnicas

---

## 🎯 WORKFLOW 1: DEVELOPMENT CYCLE COMPLETO (BORIS ELITE)

**Quando usar:** Feature completa, da ideia ao deploy

### Passo a Passo

```text
┌─────────────────────────────────────┐
│  1. PLAN MODE (Shift Tab 2x)        │
│     Criar plano detalhado           │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  2. REVISÃO ITERATIVA                │
│     Revisar plano até perfeito      │
│     (vai e volta quantas vezes      │
│      necessário)                    │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  3. AUTO ACCEPT MODE                 │
│     Executar one-shot               │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  4. SUB-AGENTE: Code Simplifier      │
│     Limpar e simplificar            │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  5. SUB-AGENTE: Verify App           │
│     Testar end-to-end               │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  6. POST-USE HOOK                    │
│     Formatar automaticamente        │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  7. /commit-push-pr                  │
│     Publicar (Git + PR)             │
└─────────────────────────────────────┘
```

### Prompt Completo (WF1)

```markdown
Vou desenvolver [FEATURE]. Siga este workflow:

FASE 1 - PLANEJAMENTO:

1. Entre em Plan Mode
2. Crie plano detalhado considerando:
   - Arquivos a modificar
   - Testes necessários
   - Edge cases
   - Validações

FASE 2 - EXECUÇÃO: 3. Após eu aprovar o plano, implemente em one-shot 4. Use Opus 4.5 com Thinking mode

FASE 3 - VERIFICAÇÃO: 5. Rode todos os testes 6. Teste no browser (localhost) 7. Valide edge cases 8. Se houver problemas, corrija e repita

FASE 4 - FINALIZAÇÃO: 9. Simplifique o código (remova redundâncias) 10. Formate conforme padrões 11. Prepare para commit

Aguardo sua primeira entrega: o PLANO.
```

### Benefícios (WF1)

- ✅ Código pensado e estruturado
- ✅ One-shot execution
- ✅ Auto-verificado
- ✅ Production-ready

**Tempo:** 30-60 minutos (feature média)

---

## 🔥 WORKFLOW 2: PARALELIZAÇÃO ESTRATÉGICA (5 TERMINAIS)

**Quando usar:** Projeto grande com múltiplas frentes

### Setup de Terminais

```text
┌──────────────┬──────────────┬──────────────┐
│ Terminal 1   │ Terminal 2   │ Terminal 3   │
│ FRONTEND     │ BACKEND      │ TESTING      │
│              │              │              │
│ - Components │ - API routes │ - Unit tests │
│ - UI/UX      │ - Database   │ - E2E tests  │
│ - Styling    │ - Logic      │ - Coverage   │
└──────────────┴──────────────┴──────────────┘

┌──────────────┬──────────────┐
│ Terminal 4   │ Terminal 5   │
│ DOCS         │ REVIEW       │
│              │              │
│ - README     │ - Code       │
│ - API docs   │   review     │
│ - Comments   │ - Cleanup    │
└──────────────┴──────────────┘
```

### Distribuição de Tarefas

#### Terminal 1 - Frontend (Sonnet 4.5)

```markdown
Foque exclusivamente em:

- Componentes React
- Estilos e UI
- Interações de usuário

Não mexa em: Backend, testes, docs
```

#### Terminal 2 - Backend (Opus 4.5 Thinking)

```markdown
Foque exclusivamente em:

- Rotas de API
- Lógica de negócio
- Integrações com DB

Não mexa em: Frontend, testes
```

#### Terminal 3 - Testing (Opus 4.5 Thinking)

```markdown
Foque exclusivamente em:

- Testes unitários
- Testes de integração
- Coverage > 80%

Rode testes continuamente
Notifique quando algum teste quebrar
```

#### Terminal 4 - Documentation (Sonnet 4.5)

```markdown
Mantenha atualizado:

- README.md
- API documentation
- Comentários no código

Sincronize com mudanças dos terminais 1 e 2
```

#### Terminal 5 - Review & Cleanup (Opus 4.5)

```markdown
Papel de code reviewer:

- Identifique code smells
- Sugira melhorias
- Simplifique código complexo
- Garanta padrões consistentes
```

### Sincronização

**Checkpoint a cada 30 minutos:**

```markdown
Todos os terminais:

1. Commit work in progress
2. Pull updates dos outros
3. Resolver conflitos
4. Continuar
```

### Benefícios (WF2)

- ✅ 5x throughput
- ✅ Especialização por terminal
- ✅ Menos context switching
- ✅ Features paralelas

**Ideal para:** Projetos grandes, times pequenos, deadlines apertados

---

## 🤖 WORKFLOW 3: FEEDBACK LOOP AUTOMÁTICO

**Quando usar:** Garantir qualidade máxima

### Setup do Loop

```text
┌────────────────────────────────────┐
│  CLAUDE DESENVOLVE                 │
│  ↓                                 │
│  CLAUDE TESTA (auto)               │
│  ↓                                 │
│  ❌ Falhou? → Corrige e repete     │
│  ✅ Passou? → Próxima etapa        │
└────────────────────────────────────┘
```

### Prompt de Feedback Loop

```markdown
Desenvolva [FEATURE] com verificação contínua:

LOOP DE QUALIDADE:

1. Implemente a feature
2. VERIFIQUE automaticamente:
   a. Rode `npm test`
   b. Rode `npm run build`
   c. Teste no localhost:3000
   d. Valide edge cases manualmente

3. Se QUALQUER verificação falhar:
   - Analise o problema
   - Corrija
   - Volte ao passo 2

4. Se TODAS as verificações passarem:
   - Simplifique o código
   - Adicione comentários se necessário
   - Confirme que está production-ready

NUNCA me entregue código que não passou
em TODAS as verificações.

Aguardo seu primeiro resultado: código + report de verificação.
```

### Verificação em Camadas

#### Layer 1: Testes Automatizados

```bash
npm run test        # Unit tests
npm run test:e2e    # End-to-end
npm run lint        # Linting
npm run typecheck   # Type checking
```

#### Layer 2: Browser Testing

```markdown
Claude abre Chrome automaticamente:

1. Navega para localhost
2. Testa funcionalidade
3. Valida UI/UX
4. Reporta problemas
```

#### Layer 3: Manual Review

```markdown
Claude fornece checklist:

- [ ] Feature funciona como esperado
- [ ] Edge cases cobertos
- [ ] Performance aceitável
- [ ] Código limpo e legível
```

### Benefícios (WF3)

- ✅ Qualidade 2-3x melhor (comprovado por Boris)
- ✅ Menos bugs em produção
- ✅ Código auto-testado
- ✅ Confiança para deploy

---

## 🔗 WORKFLOW 4: INTEGRAÇÃO COM MCP SERVERS

**Quando usar:** Debugar com dados de produção

### Workflow de Debug com Sentry

```markdown
CONTEXTO: Bug reportado em produção no módulo de checkout

WORKFLOW:

1. "Claude, conecte-se ao Sentry via MCP"
2. "Busque os últimos 50 erros relacionados a 'checkout'"
3. "Analise os stack traces"
4. "Identifique o padrão comum"
5. "No código, localize a fonte do bug"
6. "Proponha fix + testes"
7. "Valide que o fix resolve os erros do Sentry"
```

### Workflow de Analytics com BigQuery

```markdown
CONTEXTO: Otimizar feature baseado em uso real

WORKFLOW:

1. "Claude, conecte-se ao BigQuery"
2. "Query: uso da feature X nos últimos 30 dias"
3. "Identifique padrões de uso"
4. "Encontre gargalos/drop-offs"
5. "Proponha melhorias baseadas em dados"
6. "Implemente melhorias"
7. "Adicione tracking para validar impacto"
```

### Workflow de Comunicação com Slack

```markdown
CONTEXTO: Responder demanda urgente

WORKFLOW:

1. "Claude, busque no Slack #eng canal por 'urgent bug payment'"
2. "Leia o contexto da conversa"
3. "Identifique o problema reportado"
4. "Analise o código relacionado"
5. "Fixe o problema"
6. "Poste no Slack: 'Fix deployed: [PR link]'"
```

### Benefícios (WF4)

- ✅ Contexto de produção no desenvolvimento
- ✅ Dados reais informam decisões
- ✅ Comunicação integrada
- ✅ Workflow unificado

---

## ⚡ WORKFLOW 5: SLASH COMMANDS CUSTOMIZADOS

**Quando usar:** Tarefas repetitivas

### Exemplo 1: `/commit-push-pr`

**Arquivo:** `.claude/commands/commit-push-pr.md`

#### Commit, Push e Create PR

#### Pré-processamento (inline-bash)

```bash
# Pre-compute info para evitar back-and-forth
git status --short
git diff --stat
git branch --show-current
```

#### Prompt Principal

Usando as informações acima:

1. Analise as mudanças
2. Crie um commit message descritivo seguindo padrões:
   - Tipo: feat/fix/docs/refactor/test
   - Escopo: módulo afetado
   - Descrição: o que e por quê

3. Faça commit:

   ```bash
   git add .
   git commit -m "[sua mensagem]"
   ```

4. Push para remote:

   ```bash
   git push origin $(git branch --show-current)
   ```

5. Crie Pull Request via gh CLI:

   ```bash
   gh pr create --title "[título]" --body "[descrição]"
   ```

6. Retorne o link do PR

### Exemplo 2: `/test-all`

#### Rodar Todos os Testes

#### Comando

Execute sequencialmente:

1. Unit tests:

   ```bash
   npm run test
   ```

2. Integration tests:

   ```bash
   npm run test:integration
   ```

3. E2E tests:

   ```bash
   npm run test:e2e
   ```

4. Lint:

   ```bash
   npm run lint
   ```

5. Type check:

   ```bash
   npm run typecheck
   ```

#### Report

Forneça summary:

- ✅ Testes passed: X/Y
- ❌ Testes failed: Z
- ⚠️ Warnings: W

Se houver falhas, mostre details e sugira fixes.

### Exemplo 3: `/review-changes`

#### Review de Mudanças

#### Pre-compute

```bash
git diff --cached
git diff HEAD~1
```

#### Review Checklist

Analise as mudanças e valide:

- [ ] Código segue padrões do CLAUDE.md
- [ ] Sem hardcoded values
- [ ] Error handling adequado
- [ ] Testes cobrem mudanças
- [ ] Sem code smells óbvios
- [ ] Performance considerations
- [ ] Security considerations

#### Output

Forneça:

1. ✅ Aprovado OU ⚠️ Sugestões
2. Lista de melhorias (se houver)
3. Risk assessment (low/medium/high)

### Benefícios (WF5)

- ✅ Economiza tempo (não repetir prompts)
- ✅ Consistência (sempre mesmo workflow)
- ✅ Velocidade (pre-compute evita back-and-forth)
- ✅ Compartilhável (time inteiro usa)

---

## 🎓 WORKFLOW 6: PLAN MODE MASTERCLASS

**Quando usar:** Features complexas, arquitetura crítica

### Workflow Detalhado

#### FASE 1: Entrada em Plan Mode

```text
Shift + Tab (2x) → Plan Mode ativado
```

#### FASE 2: Primeira Iteração

```markdown
"Claude, planeje a implementação de [FEATURE].

Considere:

- Arquitetura atual
- Padrões do projeto
- Performance
- Testabilidade
- Manutenibilidade

Forneça plano detalhado com:

1. Arquivos a criar/modificar
2. Estrutura de dados
3. Fluxo de execução
4. Testes necessários
5. Riscos e mitigações"
```

#### FASE 3: Iteração e Refinamento

```markdown
# Após receber o plano:

"Refine o plano considerando:

- [Ponto específico 1]
- [Ponto específico 2]
- [Alternativa X vs Y - qual melhor?]"

# Repetir até plano perfeito
```

#### FASE 4: Aprovação e Execução

```markdown
"Plano aprovado. Execute em Auto Accept Mode.

Durante execução:

- Mantenha-se fiel ao plano
- Se encontrar impedimento, pause e reporte
- Não tome atalhos que desviem da arquitetura"
```

#### FASE 5: Pós-Execução

```markdown
"Após implementação:

1. Compare código com plano
2. Identifique desvios (se houver)
3. Valide que todos os requisitos foram atendidos
4. Execute feedback loop (testes)"
```

### Template de Plano

````markdown
# PLANO: [Nome da Feature]

## Objetivo

[O que queremos alcançar - 1 parágrafo]

## Arquitetura Proposta

### Arquivos Novos

- `path/to/new/file.js` - [propósito]
- `path/to/test/file.test.js` - [testes]

### Arquivos Modificados

- `existing/file.js` - [mudanças previstas]

## Estrutura de Dados

```typescript
interface NewType {
  // ...
}
```

## Fluxo de Execução

1. User action X
2. System processes Y
3. Output Z

## Testes

- [ ] Unit test: function A
- [ ] Integration test: flow B
- [ ] E2E test: scenario C

## Riscos e Mitigações

| Risco | Probabilidade | Impacto | Mitigação |
| ----- | ------------- | ------- | --------- |
| X     | Medium        | High    | Strategy  |

## Alternativas Consideradas

### Opção A (Escolhida)

- Pros: ...
- Cons: ...

### Opção B (Rejeitada)

- Pros: ...
- Cons: ...
- Por que rejeitada: ...

## Estimativa

- Complexidade: Low/Medium/High
- Tempo estimado: X horas
- Confiança: High/Medium/Low

## Aprovação

- [ ] Revisado por: [nome]
- [ ] Aprovado para execução
````

### Benefícios (WF6)

- ✅ Código pensado e estruturado
- ✅ Menos refactoring posterior
- ✅ Arquitetura sólida
- ✅ One-shot execution possível

---

## 🔄 WORKFLOW 7: LONG-RUNNING TASKS

**Quando usar:** Tarefas que levam horas/dias

### Setup

### Opção 1: Background Agent

```markdown
"Claude, desenvolva [LONG TASK].

Quando terminar:

1. Lance um background agent
2. Esse agent deve verificar:
   - Todos os testes passam
   - Build funciona
   - App roda corretamente
3. Se houver problemas, corrija automaticamente
4. Me notifique apenas quando estiver 100% pronto"
```

### Opção 2: Agent Stop Hook

```json
{
  "hooks": {
    "agent-stop": "./scripts/verify-and-notify.sh"
  }
}
```

**Script `verify-and-notify.sh`:**

```bash
#!/bin/bash

echo "🔍 Verificando trabalho..."

# Run tests
npm test || { echo "❌ Tests failed"; exit 1; }

# Build
npm run build || { echo "❌ Build failed"; exit 1; }

# Notify
echo "✅ Long-running task completed successfully!"

# Could send Slack notification, email, etc
```

### Opção 3: Halfwigan Plugin (Sandbox)

```markdown
Instale Halfwigan plugin para rodar long-running tasks
em sandbox mode, evitando prompts de permissão.

Setup: [documentação do plugin]
```

### Monitoring

```markdown
# Check-ins automáticos a cada X minutos

"Claude, durante essa long task:

1. A cada 30 minutos, me envie update:
   - O que foi completado
   - O que está em progresso
   - Blockers (se houver)

2. Se encontrar blocker crítico:
   - Pause imediatamente
   - Me notifique com contexto completo
   - Aguarde instruções"
```

### Benefícios (WF7)

- ✅ Trabalho sem supervisão
- ✅ Verificação automática
- ✅ Notificações inteligentes
- ✅ Aproveitamento de tempo ocioso

---

## 📊 COMPARAÇÃO DE WORKFLOWS

| Workflow                 | Complexidade | Tempo Setup | ROI        | Quando Usar         |
| :----------------------- | :----------- | :---------- | :--------- | :------------------ |
| **1. Development Cycle** | Alta         | 1h          | Muito Alto | Feature completa    |
| **2. Paralelização**     | Média        | 30min       | Alto       | Projetos grandes    |
| **3. Feedback Loop**     | Baixa        | 15min       | Muito Alto | Sempre!             |
| **4. MCP Integration**   | Alta         | 2h          | Alto       | Produção/Debug      |
| **5. Slash Commands**    | Baixa        | 30min       | Alto       | Tarefas repetitivas |
| **6. Plan Mode**         | Média        | 0           | Alto       | Features complexas  |
| **7. Long-Running**      | Alta         | 1h          | Médio      | Tasks longas        |

---

## 🎯 RECOMENDAÇÃO DE IMPLEMENTAÇÃO

### Semana 1: Fundamentos

- ✅ Workflow 3: Feedback Loop
- ✅ Workflow 6: Plan Mode
- ROI imediato, baixo custo

### Semana 2: Automação

- ✅ Workflow 5: Slash Commands
- ✅ Workflow 1: Development Cycle
- Aumenta produtividade significativamente

### Semana 3+: Avançado

- ✅ Workflow 2: Paralelização
- ✅ Workflow 4: MCP Integration
- ✅ Workflow 7: Long-Running
- Máxima produtividade

---

## 📚 RECURSOS RELACIONADOS

- [[Boas_Praticas_Claude_Code_Boris]] - 13 Dicas completas
- [[CHECKLIST_Setup_Claude_Code_Pro]] - Setup passo a passo
- [[Guia_Sistema_Bi_IA_Completo]] - Integração Claude + Gemini

---

**Criado:** 06/01/2026
**Baseado em:** 13 Dicas do Boris + Best Practices
**Status:** ✅ Workflows testados e validados
**Nível:** Avançado (requer fundamentos sólidos)
