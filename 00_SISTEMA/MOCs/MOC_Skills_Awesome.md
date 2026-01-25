# MOC: Skills Awesome (238 skills)

**Criado:** 24/Jan/2026
**Fonte:** github.com/sickn33/antigravity-awesome-skills
**Localização:** `.agent/skills/skills/`

---

## VISÃO GERAL

238 skills profissionais instaladas do repositório awesome-skills. Organizadas por categoria com seleção das mais relevantes para o vault.

---

## TIER 1 - PRIORITÁRIAS (16 skills)

### IA & Agentes (6)

| Skill | Descrição | Triggers |
|-------|-----------|----------|
| `ai-agents-architect` | Arquitetura de agentes autônomos | "build agent", "autonomous agent" |
| `prompt-engineer` | Otimização de prompts | "prompt engineering", "system prompt" |
| `autonomous-agents` | Padrões de autonomia controlada | "agent loops", "self-correction" |
| `agent-memory-systems` | Memória de longo prazo | "agent memory", "vector store" |
| `rag-engineer` | RAG e retrieval | "RAG", "retrieval" |
| `langgraph` | Orquestração multi-agentes | "langgraph", "agent graph" |

### Marketing & CRO (6)

| Skill | Descrição | Triggers |
|-------|-----------|----------|
| `copywriting` | Copy para conversão | "write copy", "landing page" |
| `paid-ads` | Campanhas Google/Meta | "PPC", "ROAS", "ad campaign" |
| `page-cro` | Conversão de páginas | "CRO", "conversion rate" |
| `seo-audit` | Auditoria SEO | "SEO audit", "Core Web Vitals" |
| `email-sequence` | Automação de emails | "email sequence", "drip campaign" |
| `analytics-tracking` | GA4, eventos | "GA4", "conversion tracking" |

### Produtividade (4)

| Skill | Descrição | Triggers |
|-------|-----------|----------|
| `brainstorming` | Ideação estruturada | "brainstorm", "ideate" |
| `concise-planning` | Checklists atômicos | "checklist", "task breakdown" |
| `writing-plans` | Planos de projeto | "project plan", "planning" |
| `executing-plans` | Execução com checkpoints | "execute plan", "implementation" |

---

## TIER 2 - ÚTEIS (15 skills)

### Desenvolvimento

| Skill | Descrição |
|-------|-----------|
| `clean-code` | Padrões pragmáticos de código |
| `tdd-workflow` | Test-driven development |
| `backend-dev-guidelines` | Arquitetura backend Node.js |
| `frontend-dev-guidelines` | React/TypeScript patterns |
| `api-patterns` | REST vs GraphQL |
| `docker-expert` | Containers e orquestração |
| `systematic-debugging` | Debug estruturado |

### Documentos

| Skill | Descrição |
|-------|-----------|
| `docx-official` | Criar/editar Word |
| `pdf-official` | Manipular PDF |
| `xlsx-official` | Planilhas Excel |
| `pptx-official` | Apresentações |

### Workflow

| Skill | Descrição |
|-------|-----------|
| `workflow-automation` | n8n, Temporal, Inngest |
| `zapier-make-patterns` | No-code automation |
| `inngest` | Event-driven workflows |
| `bullmq-specialist` | Job queues Redis |

---

## CATEGORIAS COMPLETAS

### Autonomous & Agentic (~8)

- loki-mode
- subagent-driven-dev
- dispatching-parallel-agents
- planning-with-files
- skill-creator
- autonomous-agents
- autonomous-agent-patterns
- ai-agents-architect

### Integrations & APIs (~25)

- stripe, firebase, supabase, vercel
- clerk-auth, twilio, discord-bot-architect
- slack-bot, graphql, aws-serverless
- azure-functions, algolia-search
- file-uploads, email-systems, bullmq-specialist

### Cybersecurity (~51)

- active-directory-attacks
- api-fuzzing-bug-bounty
- aws-penetration-testing
- metasploit-framework
- sqlmap, xss-html-injection
- (geralmente baixa prioridade para vault PKM)

### Creative & Design (~10)

- ui-ux-pro-max, frontend-design
- canvas-design, algorithmic-art
- theme-factory, d3-viz
- web-artifacts, 3d-web-experience

### Marketing & Growth (~23)

- page-cro, copywriting, copy-editing
- seo-audit, paid-ads, email-sequence
- pricing-strategy, referral-program
- launch-strategy, analytics-tracking
- form-cro, signup-flow-cro

### Maker Tools (~11)

- micro-saas-launcher
- browser-extension-builder
- telegram-bot, ai-wrapper-product
- viral-generator

---

## COMO USAR

### No Gemini/Antigravity

As skills são ativadas automaticamente quando você menciona triggers relacionados.

Exemplo:
```
"Preciso escrever copy para a página de produto do KabaK"
→ skill `copywriting` é carregada automaticamente
```

### No Claude Code

As skills estão disponíveis como referência em `.agent/skills/skills/`. Para carregar o conhecimento de uma skill específica:

```
Leia .agent/skills/skills/copywriting/skill.md e aplique os princípios
```

---

## MANUTENÇÃO

- **Atualizar:** `git pull` em `.agent/skills/`
- **Adicionar:** Copiar skill para pasta e documentar aqui
- **Remover:** Deletar pasta (não afeta o índice)

---

## LINKS

- Repositório: https://github.com/sickn33/antigravity-awesome-skills
- Skills index: `.agent/skills/skills_index.json`
- Docs: `.agent/skills/docs/`

---

**Última atualização:** 24/Jan/2026
