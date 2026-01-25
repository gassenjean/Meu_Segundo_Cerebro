---
created: 2026-01-24T21:13
updated: 2026-01-22T22:29
---
# BOAS PRÁTICAS CLAUDE CODE - 13 DICAS DO CRIADOR (BORIS)

**Autor:** Boris (Criador do Claude Code)
**Fonte:** Vídeo transcrição - "Como o criador do Claude Code usa a própria ferramenta"
**Extraído em:** 06/01/2026
**Status:** ✅ Técnicas validadas pelo criador

---

## 🎯 OVERVIEW

Boris, criador do Claude Code, compartilhou **13 técnicas profissionais** de como ele mesmo usa a ferramenta. Este documento captura essas práticas comprovadas para maximizar produtividade.

**Nível:** Intermediário a Avançado
**Aplicação:** Imediata
**Impacto:** Alto (técnicas do próprio criador)

---

## 📋 AS 13 DICAS ESSENCIAIS

### 🔥 DICA 1: PARALELIZAÇÃO EXTREMA

**O que Boris faz:**

- Roda **5 instâncias locais** do Claude Code simultaneamente
- Numera cada terminal: 1, 2, 3, 4, 5
- Ativa notificações do sistema quando tarefas terminam

**Como aplicar:**

```bash
# Terminal 1: Frontend development
# Terminal 2: Backend API
# Terminal 3: Testing agent
# Terminal 4: Documentation
# Terminal 5: Code review / cleanup
```

**Casos de uso:**

- Trabalhar em áreas diferentes da mesma codebase sem conflito
- Dedicar um agente específico para testes
- Ter um agente focado em backend e outro em frontend

**Benefício:** Produtividade multiplicada por 5x

---

### 🌐 DICA 2: ECOSSISTEMA COMPLETO (LOCAL + NUVEM + MOBILE)

**O que Boris faz:**

- **5 instâncias locais** (terminal)
- **5-10 instâncias na nuvem** (cloud.ai)
- **App iOS** para iniciar tarefas do celular
- **Total:** Até 15 Claude Code trabalhando simultaneamente

**Estratégia de uso:**

- Usa "teleporte" entre local e nuvem (back and forth)
- Inicia tarefas do celular quando não está no computador
- Aproveita TODO o ecossistema independente da localização

**Benefício:** Trabalho contínuo 24/7, qualquer dispositivo

---

### 💎 DICA 3: OPUS 4.5 COM THINKING MODE - SEMPRE

**O que Boris usa:**

```text
Modelo: Opus 4.5
Modo: Thinking (Raciocínio) - SEMPRE ATIVO
```

**Por quê?**

- ✅ Melhor modelo de código que ele já usou
- ✅ Mais lento que Sonnet, MAS mais rápido no resultado final
- ✅ Resultados mais objetivos (menos refactoring)
- ✅ Melhor uso de ferramentas

**Filosofia:** "Preferir qualidade a velocidade inicial"

**Quando NÃO usar:** Tarefas triviais que não exigem raciocínio profundo

---

### 🤝 DICA 4: CLAUDE.MD COMPARTILHADO NO GIT

**Setup do time de Boris:**

```text
repositório/
├── .git/
├── CLAUDE.md  ← ÚNICO arquivo, compartilhado por TODO o time
└── ...
```

**Como funciona:**

1. **Um único CLAUDE.md** para o repositório inteiro
2. **Commitado no Git** junto com o código
3. **Time contribui múltiplas vezes por semana**
4. Quando alguém vê Claude agindo incorretamente → adiciona regra no CLAUDE.md
5. Claude aprende: não só para essa vez, mas para NUNCA repetir

**Benefício:**

- ✅ Conhecimento coletivo do time
- ✅ Claude melhora continuamente
- ✅ Onboarding automático de novos membros
- ✅ Padrões do time sempre respeitados

**Observação de Boris:**

- Alguns times mantêm múltiplos CLAUDE.md (por módulo)
- Responsabilidade de cada time manter atualizado
- ⚠️ Atenção: Isso trava na ferramenta Claude Code (não é vendor-neutral)

**Alternativa do vault:** `00_SISTEMA/CLAUDE.md` (já implementado!)

---

### 🤖 DICA 5: @CLAUDE EM CODE REVIEWS

**Workflow durante Pull Request:**

```markdown
# No comentário do PR do colega:

@Claude adicione isso ao CLAUDE.md como parte desta PR:

"Sempre validar input de usuário antes de salvar no banco.
Usar biblioteca Zod para validação de schemas."
```

**O que acontece:**

1. Claude Code é marcado no comentário do PR
2. Claude **automaticamente** adiciona alteração ao CLAUDE.md
3. Claude faz commit com a mudança
4. PR já inclui atualização da documentação

**Tool necessário:**

- Cloud Code GitHub Action (instalar com `/install github-action`)

**Benefício:** "Denshipper Compounding Engineering"

- Não precisa pedir ao dono da PR para atualizar docs
- Claude faz o trabalho automaticamente
- Conhecimento capturado instantaneamente

---

### 📐 DICA 6: PLAN MODE WORKFLOW (PREVIZ - PLANEJAMENTO + REVISÃO)

**Workflow de Boris:**

```text
1. Shift + Tab (2x) → Entra em Plan Mode
2. Revisa plano, vai e volta até ficar PERFEITO
3. Quando plano está redondo → Auto Accept Edits
4. Claude executa em ONE SHOT (uma vez só)
```

**Filosofia:**

> "Um bom plano é realmente importante. Com Spec Driven Development
> e um bom plano, você consegue one shot."

**Passos detalhados:**

### FASE 1: Planejamento (Plan Mode)

```text
- Shift Tab 2x → Ativa Plan Mode
- Claude cria plano detalhado
- Você revisa e pede alterações
- Repete até o plano ficar redondinho
```

### FASE 2: Execução (Auto Accept)

```text
- Ativa Auto Accept Edits
- Claude implementa tudo de uma vez
- Código sai pronto (ou próximo disso)
```

**Benefício:**

- ✅ Menos ciclos de refactoring
- ✅ Código mais pensado
- ✅ Menos bugs
- ✅ One-shot execution

**Atalho:** `Shift + Tab (2x)` para Plan Mode

---

### ⚡ DICA 7: SLASH COMMANDS PARA TAREFAS REPETITIVAS

**Princípio:**

> "Toda tarefa que faço várias vezes no dia → crio um slash command"

**Exemplo do Boris:**

```bash
/commit-push-pr
```

**O que esse comando faz:**

1. Pre-computa `git status`
2. Coleta outras informações (usando inline-bash)
3. Cria commit
4. Faz push
5. Abre Pull Request
6. Tudo em um comando!

**Benefícios:**

- ✅ Economiza tempo (não precisa repetir prompts)
- ✅ Executa rápido (pre-computa info com inline-bash)
- ✅ Evita back-and-forth com o modelo
- ✅ Claude também pode usar esses workflows

**Onde criar:**

```text
.claude/commands/nome-do-comando.md
```

**Time do Boris usa dezenas de vezes por dia!**

---

### 🔧 DICA 8: SUB-AGENTES PARA AUTOMATIZAÇÃO

**Sub-agentes de Boris:**

#### 1. Code Simplifier

- Roda DEPOIS que Claude termina
- Simplifica código gerado
- Remove redundâncias

#### 2. Verify App

- Detalha instruções para Claude testar end-to-end
- Valida aplicação completa
- Testa no browser

**3. E outros...**

**Filosofia:**

> "Pense em sub-agentes como maneira de automatizar tarefas comuns
> do dia-a-dia, similar aos slash commands."

**Benefício:** Automatizar pull requests e tarefas repetitivas

---

### 🎨 DICA 9: POST-USE HOOK PARA FORMATAÇÃO

**Setup do time:**

```json
// Hook que roda APÓS cada tarefa
{
  "post-use-hook": "npm run format"
}
```

**Por quê?**

- Claude formata bem o código 90% das vezes
- Hook resolve os **10% restantes**
- Evita erros de formatação na CI/CD

**Benefício:**

- ✅ Zero erros de formatação em CI
- ✅ Código sempre consistente
- ✅ Time não precisa pensar nisso

**Onde configurar:** Hooks do Claude Code

---

### 🔒 DICA 10: NÃO USE YOLO MODE (DANGEROUSLY SKIP PERMISSIONS)

**O que Boris NÃO faz:**
❌ `dangerously_skip_permissions: true` (modo YOLO)

**O que Boris FAZ:**
✅ Usa `/permissions` para pré-permitir comandos comuns
✅ Configura no `cloud-settings.json`
✅ Compartilha configurações com o time (via Git)

**Exemplo:**

```json
{
  "pre_allowed_commands": [
    "npm install",
    "npm run build",
    "git status",
    "git diff"
  ]
}
```

**Benefícios:**

- ✅ Mais seguro (menos alucinações executadas)
- ✅ Permissões persistidas no repo
- ✅ Não precisa aprovar repetidamente
- ✅ Time inteiro usa as mesmas permissões

**Filosofia:**

> "É melhor configurar corretamente uma vez do que liberar tudo."

---

### 🔗 DICA 11: INTEGRAÇÃO COMPLETA COM MCP SERVERS

**Ferramentas que Claude Code de Boris usa:**

- **Slack:** Busca, comenta, posta
- **BigQuery CLI:** Queries analíticas
- **Sentry:** Busca error logs
- E mais...

**Exemplo de uso:**

```text
"Claude, vá no Sentry e busque os últimos erros de produção
relacionados ao módulo de checkout. Depois, analise o código
e proponha fix."
```

**Benefícios:**

- ✅ Debugar bugs com dados de produção diretamente
- ✅ Trazer contexto do Slack para codebase
- ✅ Queries analíticas sem sair do Claude
- ✅ Workflow unificado

**Quando vale a pena:**

- Times maiores
- Gestão complexa de projetos
- Múltiplas ferramentas integradas

**Para times pequenos:** Talvez não compense o setup inicial

---

### ⏳ DICA 12: LONG-RUNNING TASKS COM BACKGROUND AGENTS

**Estratégias para tarefas longas (1-2 dias):**

#### OPÇÃO 1: Background Agent com verificação

```text
"Claude, quando terminar essa tarefa longa, use um background
agent para verificar se está tudo funcionando."
```

#### OPÇÃO 2: Agent Stop Hook (mais determinístico)

```json
{
  "agent_stop_hook": "npm run verify && npm run test"
}
```

#### OPÇÃO 3: Halfwigan Plugin

- Plugin criado por Geoffrey Huntley
- Usa `PermissionMode.ask` OU `DangerouslySkipPermissions` em sandbox
- Evita prompts de permissão durante execução longa
- Claude "cozinha" sem ser bloqueado

**Benefício:** Tarefas longas rodam sem supervisão

**Observação de Boris:**

> "Eu não costumo usar Claude Code para long-running tasks assim,
> mas se você usa, essa é a estratégia."

---

### 🔁 DICA 13: FEEDBACK LOOPS (A MAIS IMPORTANTE!)

**A dica que Boris mais enfatiza:**

> "Dê ao Claude Code uma maneira de verificar o próprio trabalho dele."

**Como funciona:**

1. Claude desenvolve código
2. Claude VERIFICA o código que fez
3. Claude testa no browser (ou via tests)
4. Claude corrige se necessário
5. Repete até funcionar

**Resultado:**

- ✅ Qualidade **2-3x melhor** apenas por adicionar verificação
- ✅ Menos bugs em produção
- ✅ Código auto-testado

**Tipos de verificação:**

#### 1. Simples - Comando Bash

```bash
npm run test
```

#### 2. Médio - Test Suite

```bash
npm run test:integration
```

#### 3. Avançado - Browser Testing

- Abre browser
- Testa UI interativamente
- Valida experiência de usuário
- Garante que "feels good"

**Filosofia:**

> "Invista tempo em fazer as instruções de feedback loops serem
> ROCK SOLID (sólidas como rocha). Isso melhora tudo."

**Aplicação no vault:**

- Use Cloud Coach extension para testar no browser
- Configure test suites automáticos
- Crie verificação em múltiplos domínios

---

## 🎯 TÉCNICAS AVANÇADAS (BÔNUS)

### Combinação de Técnicas

**Workflow Elite (Boris):**

```text
1. Plan Mode (Shift Tab 2x) → Planejar
2. Revisar até perfeito
3. Auto Accept → Executar
4. Sub-agente: Code Simplifier → Limpar
5. Sub-agente: Verify App → Testar
6. Post-use hook → Formatar
7. /commit-push-pr → Publicar
```

**Resultado:** Código production-ready em minutos

---

## 📊 MÉTRICAS DE SUCESSO

**Se você está usando bem as 13 dicas:**

- ✅ Trabalha com 3-5+ instâncias simultaneamente
- ✅ Opus 4.5 Thinking é seu modelo padrão
- ✅ Tem CLAUDE.md compartilhado no Git
- ✅ Usa slash commands para tarefas comuns
- ✅ Sub-agentes automatizam workflows
- ✅ Hooks formatam código automaticamente
- ✅ Permissões configuradas (não usa YOLO)
- ✅ Feedback loops verificam qualidade
- ✅ Qualidade do código aumentou 2-3x

---

## ⚠️ ARMADILHAS COMUNS

### ❌ O que NÃO fazer

1. **Usar apenas 1 instância** → Perde produtividade
2. **Sempre usar Sonnet** → Opus 4.5 é melhor para código complexo
3. **CLAUDE.md individual** → Conhecimento não compartilhado
4. **Modo YOLO sempre ativo** → Menos seguro
5. **Sem feedback loops** → Código 2-3x pior
6. **Não usar slash commands** → Repetir prompts constantemente
7. **Não usar Plan Mode** → Código menos pensado
8. **Ignorar hooks** → Erros de formatação em CI

---

## 🔗 INTEGRAÇÃO COM ESTE VAULT

**Aplicação imediata:**

1. ✅ **CLAUDE.md já existe:** `00_SISTEMA/CLAUDE.md`
2. ✅ **Slash commands já criados:** `.claude/commands/`
3. ✅ **Múltiplos agentes:** Sistema Bi-IA (Claude + Gemini)
4. 🔧 **TODO:** Configurar hooks (post-use formatting)
5. 🔧 **TODO:** Criar sub-agentes (Code Simplifier, Verify)
6. 🔧 **TODO:** Setup MCP Servers relevantes

**Próximos passos:** Ver `CHECKLIST_Setup_Claude_Code_Pro.md`

---

## 📚 REFERÊNCIAS

- **Fonte:** Transcrição de vídeo do criador (Boris)
- **Data:** 2025 (estimado)
- **Contexto:** Uso profissional interno do time Claude Code
- **Relacionados:**
  - [[CHECKLIST_Setup_Claude_Code_Pro]]
  - [[Workflows_Avancados_Claude_Code]]
  - [[Guia_Sistema_Bi_IA_Completo]]

---

**Criado:** 06/01/2026
**Última atualização:** 06/01/2026
**Status:** ✅ Completo e acionável
**Nível de confiança:** Alto (fonte: criador da ferramenta)

---

Boris demonstra que a chave não é apenas USAR Claude Code, mas **orquestrar múltiplas instâncias, automatizar workflows e criar feedback loops**. A diferença entre uso básico e profissional está na **sistemização e automação**.

---

## 🛡️ REGRAS DE OURO DA BI-IA (NOVIDADE)

**Acordo entre Agentes (Claude + Gemini):**

1. **MD040:** Nunca use ` ``` ` sem linguagem. Use ` ```text ` ou ` ```bash `.
2. **MD036:** Nunca use `**Negrito**` como título em linha isolada. Use `### Título`.
3. **MD060:** Tabelas devem ter espaços: `| Texto |` e não `|Texto|`.
4. **MD026:** Títulos nunca terminam com dois pontos `:`.

*Regras aplicadas e monitoradas pelo agente `lint-guardian`.*
