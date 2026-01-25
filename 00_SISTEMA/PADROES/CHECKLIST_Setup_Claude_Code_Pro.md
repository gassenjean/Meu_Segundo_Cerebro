# CHECKLIST - SETUP CLAUDE CODE PROFISSIONAL (NÍVEL BORIS)

**Objetivo:** Transformar seu uso de Claude Code de básico para profissional
**Baseado em:** 13 Dicas do criador (Boris)
**Tempo estimado:** 2-3 horas de setup inicial
**ROI:** 2-3x mais produtividade + qualidade de código

---

## 🎯 NÍVEL 1: FUNDAMENTOS (30 minutos)

### Setup Básico

- [ ] **Claude Code instalado e funcionando**
  - Version mais recente
  - Extensão VSCode OU CLI configurado

- [ ] **Modelo correto configurado**
  - [ ] Opus 4.5 como modelo padrão
  - [ ] Thinking Mode SEMPRE ativo
  - [ ] Sonnet 4.5 disponível para tarefas rápidas

- [ ] **Workspace organizado**
  - [ ] Pasta de projeto com estrutura clara
  - [ ] `.gitignore` configurado
  - [ ] README.md básico

---

## 🚀 NÍVEL 2: PRODUTIVIDADE (1 hora)

### Paralelização

- [ ] **Setup de múltiplas instâncias**
  - [ ] Abrir 3-5 terminais numerados
  - [ ] Configurar notificações do sistema
  - [ ] Testar execução paralela

  ```bash
  # Terminal 1: Frontend
  # Terminal 2: Backend
  # Terminal 3: Testing
  # Terminal 4: Docs
  # Terminal 5: Review
  ```

### Ecossistema Completo

- [ ] **Claude Code local** (terminal) - OK
- [ ] **Claude Code na nuvem** (cloud.ai)
  - [ ] Criar conta em cloud.ai
  - [ ] Testar teleporte local ↔ nuvem
- [ ] **App Mobile** (se aplicável)
  - [ ] Instalar app iOS/Android
  - [ ] Configurar sincronização

### CLAUDE.md Compartilhado

- [ ] **Criar/Atualizar CLAUDE.md no repositório**

  ```bash
  # No root do projeto:
  touch CLAUDE.md
  git add CLAUDE.md
  git commit -m "Add shared CLAUDE.md for team"
  ```

- [ ] **Adicionar regras iniciais**
  - [ ] Padrões de código do time
  - [ ] Convenções de nomenclatura
  - [ ] Arquitetura do projeto
  - [ ] Anti-patterns a evitar

- [ ] **Educar o time**
  - [ ] Documentar como contribuir
  - [ ] Estabelecer rotina de atualização
  - [ ] Fazer onboarding com CLAUDE.md

---

## ⚡ NÍVEL 3: AUTOMAÇÃO (1 hora)

### Slash Commands

- [ ] **Criar pasta de comandos**

  ```bash
  mkdir -p .claude/commands
  ```

- [ ] **Comandos essenciais criados:**
  - [ ] `/commit-push-pr` - Commit + Push + Create PR
  - [ ] `/test-all` - Rodar todos os testes
  - [ ] `/build-check` - Build + validações
  - [ ] `/format-code` - Formatar código
  - [ ] `/review-changes` - Review de mudanças

- [ ] **Comandos específicos do projeto:**
  - [ ] ***
  - [ ] ***
  - [ ] ***

**Template de comando:**

````markdown
# Nome do Comando

## Prompt

[Instruções para o Claude]

## Inline Bash (opcional)

```bash
git status --short
git diff --stat
```
````

## Output esperado

[O que o comando deve produzir]

````

### Sub-Agentes

- [ ] **Code Simplifier**
  - [ ] Criar agente que simplifica código
  - [ ] Configurar para rodar após desenvolvimento
  - [ ] Testar em código de exemplo

- [ ] **Verify App**
  - [ ] Criar agente de teste end-to-end
  - [ ] Configurar checklist de verificação
  - [ ] Integrar com test suite

- [ ] **Outros sub-agentes (opcional):**
  - [ ] Documentation Generator
  - [ ] Security Scanner
  - [ ] Performance Analyzer

### Hooks

- [ ] **Post-use Hook (formatação)**
  ```json
  {
    "hooks": {
      "post-use": "npm run format"
    }
  }
````

- [ ] **Agent Stop Hook (long-running tasks)**

  ```json
  {
    "hooks": {
      "agent-stop": "npm run verify && npm test"
    }
  }
  ```

- [ ] **Testar hooks**
  - [ ] Rodar tarefa e verificar hook executado
  - [ ] Validar que formatação acontece automaticamente

---

## 🔒 NÍVEL 4: SEGURANÇA E PERMISSÕES (30 minutos)

### Configuração de Permissões

- [ ] **Desativar modo YOLO**

  ```json
  {
    "dangerously_skip_permissions": false
  }
  ```

- [ ] **Configurar permissões pré-aprovadas**

  Editar `cloud-settings.json`:

  ```json
  {
    "pre_allowed_commands": [
      "npm install",
      "npm run build",
      "npm run test",
      "git status",
      "git diff",
      "git add",
      "git commit"
    ]
  }
  ```

- [ ] **Adicionar ao Git (compartilhar com time)**

  ```bash
  git add .claude/settings.json cloud-settings.json
  git commit -m "Add shared Claude Code permissions"
  ```

- [ ] **Revisar permissões regularmente**
  - [ ] Adicionar novas conforme necessário
  - [ ] Remover as não utilizadas

---

## 🔗 NÍVEL 5: INTEGRAÇÕES (1 hora+)

### GitHub Action

- [ ] **Instalar GitHub Action**

  ```bash
  /install github-action
  ```

- [ ] **Configurar @Claude em PRs**
  - [ ] Testar em PR de exemplo
  - [ ] Validar que Claude atualiza CLAUDE.md
  - [ ] Documentar workflow para o time

### MCP Servers (Se aplicável ao projeto)

- [ ] **Identificar ferramentas necessárias:**
  - [ ] Slack (comunicação)
  - [ ] Sentry (error tracking)
  - [ ] BigQuery (analytics)
  - [ ] Outros: **\*\***\_\_\_**\*\***

- [ ] **Instalar MCP Servers relevantes**

  ```bash
  # Exemplo: Slack
  npm install @claude/mcp-slack
  ```

- [ ] **Configurar credenciais**
  - [ ] Criar tokens de API
  - [ ] Adicionar ao `.env` (não commitar!)
  - [ ] Documentar setup para o time

- [ ] **Testar integrações**
  - [ ] Claude consegue acessar Slack
  - [ ] Claude consegue buscar logs no Sentry
  - [ ] Validar queries no BigQuery

---

## 🔁 NÍVEL 6: FEEDBACK LOOPS (CRÍTICO!)

### Setup de Verificação Automática

- [ ] **Nível 1: Testes unitários**

  ```bash
  npm run test
  ```

- [ ] **Nível 2: Testes de integração**

  ```bash
  npm run test:integration
  ```

- [ ] **Nível 3: Browser testing**
  - [ ] Instalar Claude Coach extension
  - [ ] Configurar browser padrão (Chrome)
  - [ ] Criar workflow de teste UI

### Configurar Feedback Loops

- [ ] **Prompt padrão de verificação:**

  ```markdown
  "Após desenvolver, verifique seu trabalho:

  1. Rode os testes
  2. Teste no browser (se aplicável)
  3. Valide a experiência do usuário
  4. Corrija qualquer problema encontrado
  5. Repita até tudo funcionar perfeitamente"
  ```

- [ ] **Adicionar ao CLAUDE.md:**

  ```markdown
  ## Verificação Obrigatória

  Sempre que terminar uma tarefa:

  1. Rode `npm test`
  2. Teste no localhost
  3. Valide edge cases
  4. Confirme que código está limpo
  ```

- [ ] **Testar feedback loop:**
  - [ ] Claude desenvolve feature
  - [ ] Claude verifica automaticamente
  - [ ] Claude corrige se necessário
  - [ ] Qualidade 2-3x melhor confirmada

---

## 🎓 NÍVEL 7: WORKFLOWS AVANÇADOS (Opcional)

### Plan Mode Workflow

- [ ] **Memorizar atalho:** `Shift + Tab (2x)`

- [ ] **Praticar workflow PREVIZ:**
  1. [ ] Entrar em Plan Mode
  2. [ ] Revisar plano
  3. [ ] Iterar até perfeito
  4. [ ] Auto Accept → Executar

- [ ] **Criar template de planejamento:**

  ```markdown
  # Template de Plano

  ## Objetivo

  [O que queremos alcançar]

  ## Arquivos Afetados

  - file1.js
  - file2.js

  ## Passos

  1. ...
  2. ...

  ## Testes

  - [ ] Test 1
  - [ ] Test 2

  ## Verificação

  Como validar que funcionou?
  ```

### Workflow Completo (Boris Style)

- [ ] **Documentar workflow elite:**

  ```
  1. Plan Mode (Shift Tab 2x)
  2. Revisar plano
  3. Auto Accept
  4. Sub-agente: Code Simplifier
  5. Sub-agente: Verify App
  6. Post-use hook: Format
  7. /commit-push-pr
  ```

- [ ] **Testar workflow end-to-end**
- [ ] **Medir tempo economizado**
- [ ] **Iterar e melhorar**

---

## 📊 VALIDAÇÃO FINAL

### Checklist de Sucesso

Você está no nível profissional se:

- ✅ Trabalha com 3-5 instâncias simultaneamente
- ✅ Opus 4.5 Thinking é modelo padrão
- ✅ CLAUDE.md compartilhado e atualizado regularmente
- ✅ Pelo menos 3 slash commands criados e usados diariamente
- ✅ Hooks configurados e funcionando
- ✅ Permissões configuradas (não usa YOLO)
- ✅ Feedback loops implementados
- ✅ Qualidade de código aumentou visivelmente

### Métricas para Acompanhar

- [ ] **Tempo por feature:** Antes **_ vs Depois _**
- [ ] **Bugs em produção:** Antes **_ vs Depois _**
- [ ] **PRs por dia:** Antes **_ vs Depois _**
- [ ] **Tempo em code review:** Antes **_ vs Depois _**
- [ ] **Satisfação do time:** Antes **_ vs Depois _**

---

## 🔄 MANUTENÇÃO CONTÍNUA

### Semanal

- [ ] Revisar CLAUDE.md (adicionar novos aprendizados)
- [ ] Verificar se hooks estão funcionando
- [ ] Atualizar slash commands conforme necessário

### Mensal

- [ ] Revisar permissões (adicionar/remover)
- [ ] Avaliar necessidade de novos MCP Servers
- [ ] Medir impacto (métricas)
- [ ] Compartilhar aprendizados com o time

### Trimestral

- [ ] Fazer retrospectiva de uso
- [ ] Identificar gargalos
- [ ] Criar novos sub-agentes se necessário
- [ ] Atualizar workflows baseado em uso real

---

## 🎯 PRÓXIMOS PASSOS

1. **Hoje:** Completar Nível 1 e 2
2. **Esta semana:** Completar Nível 3 e 4
3. **Próximas 2 semanas:** Completar Nível 5 e 6
4. **Mês 1:** Masterizar Nível 7

---

## 📚 RECURSOS

- [[Boas_Praticas_Claude_Code_Boris]] - Documento completo das 13 dicas
- [[Workflows_Avancados_Claude_Code]] - Workflows específicos
- [[Guia_Sistema_Bi_IA_Completo]] - Integração Claude + Gemini

---

**Criado:** 06/01/2026
**Baseado em:** 13 Dicas do Boris (criador do Claude Code)
**Status:** ✅ Pronto para execução
**Tempo total estimado:** 4-6 horas de setup inicial

**ROI Esperado:**

- 2-3x qualidade de código
- 3-5x produtividade em tarefas repetitivas
- 50%+ redução de bugs
- Setup pago em < 1 semana de uso
