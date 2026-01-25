---
created: 2026-01-24T22:10
updated: 2026-01-24T23:38
---
# PLANO ESTRATÉGICO: SEGUNDO CÉREBRO 2026

**Criado:** 24/Jan/2026
**Atualizado:** 24/Jan/2026 (v2)
**Autor:** Névoa (Orquestrador)
**Status:** ATIVO

---

## VISÃO GERAL

**Sistema:** Névoa + Alan Nicolas (Híbrido) + Bi-IA (Claude + Gemini)
**Versão:** 2.4.2 | **Fase:** 7.5 EM PROGRESSO
**Arquivos:** 11.108+ | **Projetos:** 8 ativos | **Agentes:** 9 + 156 externos

### Recursos Disponíveis (Atualizado)

| Fonte | Quantidade | Localização |
|-------|------------|-------------|
| awesome-skills | 238 skills | `.agent/skills/skills/` |
| claude-code-templates | 156 agentes | Instalação via npx |
| claude-code-templates | 10 MCPs | Instalação via npx |
| claude-code-templates | 4 categorias skills | `.claude/skills/` |
| Vault nativo | 19 comandos | `.claude/commands/` |

### Arsenal Total

- **238 skills** (awesome-skills) - Marketing, IA, Docs, Workflow
- **156 agentes** (claude-code-templates) - Especialistas em domínios
- **10 MCPs** - Integrações externas (GitHub, PostgreSQL, etc.)
- **19 comandos** nativos - Orquestração vault

---

## PRIORIDADES 2026

### P1: PROJETO KABAK (Receita Imediata)

**Meta:** Lançar e-commerce até Abril/2026
**Investimento:** R$ 2.096.300
**Skills relevantes:**

| Skill | Aplicação | Comando |
|-------|-----------|---------|
| `copywriting` | Descritivos de produtos, landing pages | - |
| `page-cro` | Otimização de conversão | - |
| `seo-audit` | Indexação, Core Web Vitals | - |
| `email-sequence` | Pós-compra, recuperação carrinho | - |
| `paid-ads` | Google Ads, Meta Ads | /pedro |
| `analytics-tracking` | GA4, eventos, conversões | - |

**Ações:**

1. [ ] Aplicar `copywriting` no descritivo de 10 produtos top
2. [ ] Auditar SEO das páginas de categoria
3. [ ] Criar sequência email pós-compra (5 emails)
4. [ ] Setup GA4 com eventos de e-commerce

---

### P2: SISTEMA DE AGENTES (Infraestrutura)

**Meta:** Orquestração robusta com memória persistente
**Skills relevantes:**

| Skill | Propósito |
|-------|-----------|
| `ai-agents-architect` | Arquitetura ReAct, Plan-Execute |
| `agent-memory-systems` | Memória de longo prazo, retrieval |
| `langgraph` | Grafos de estado, checkpoints |
| `rag-engineer` | RAG otimizado para vault |
| `autonomous-agents` | Padrões de autonomia controlada |
| `prompt-engineer` | Otimização de prompts |

**Ações:**

1. [ ] Documentar arquitetura atual dos 9 agentes
2. [ ] Implementar vector store para `01_CONHECIMENTO/`
3. [ ] Criar grafo de workflow para processamento de projetos
4. [ ] Otimizar prompts dos agentes existentes

---

### P3: DEFI & PORTFÓLIO (3 meses)

**Meta:** Gestão ativa do portfólio cripto
**Skills relevantes:**

| Skill | Aplicação |
|-------|-----------|
| `brainstorming` | Análise de oportunidades |
| `writing-plans` | Planos de entrada/saída |
| `concise-planning` | Checklists de execução |

**Ações:**

1. [ ] Revisar `02_PROJETOS/DeFi_Verso_2025/`
2. [ ] Criar checklist de análise de protocolo
3. [ ] Documentar regras de gestão de risco

---

### P4: PRODUTIVIDADE TDAH (Contínuo)

**Meta:** Sistema sustentável de execução
**Agente principal:** Elena (/elena)
**Skills relevantes:**

| Skill | Propósito |
|-------|-----------|
| `concise-planning` | Checklists atômicos |
| `executing-plans` | Execução com checkpoints |
| `behavioral-modes` | Modos operacionais |

**Ações:**

1. [ ] Criar rotina diária com blocos de energia
2. [ ] Implementar protocolo "Sapo" (tarefa difícil primeiro)
3. [ ] Revisar semanalmente (sexta 17h)

---

## SKILLS PRIORITÁRIAS (TOP 20)

### Tier 1 - Integrar Imediatamente

**IA & Agentes:**
1. `ai-agents-architect` - Arquitetura de agentes
2. `prompt-engineer` - Otimização de prompts
3. `autonomous-agents` - Padrões de autonomia
4. `agent-memory-systems` - Sistemas de memória
5. `rag-engineer` - RAG e retrieval
6. `langgraph` - Orquestração multi-agentes

**Marketing & CRO:**
7. `copywriting` - Copy para conversão
8. `paid-ads` - Campanhas pagas
9. `page-cro` - Conversão de páginas
10. `seo-audit` - Auditoria SEO
11. `email-sequence` - Automação de emails
12. `analytics-tracking` - GA4, eventos

**Produtividade:**
13. `brainstorming` - Ideação estruturada
14. `concise-planning` - Checklists atômicos
15. `writing-plans` - Planos de projeto
16. `executing-plans` - Execução com checkpoints

### Tier 2 - Integrar Gradualmente

17. `clean-code` - Padrões de código
18. `docx-official` - Documentos Word
19. `workflow-automation` - n8n, automação
20. `api-patterns` - Design de APIs

---

## ARQUITETURA DE AGENTES

```
GASSEN (Você)
    ↓
NÉVOA (Orquestrador Master)
    │
    ├── GERENTE_CONHECIMENTO
    │   ├── /alan (IA & Automação)
    │   ├── /marie-kondo (Organização)
    │   └── /mapa (Indexação)
    │
    ├── GERENTE_PROJETOS
    │   ├── /kabak-agent (E-commerce)
    │   ├── /validate (Nomenclatura)
    │   └── /pedro (Tráfego)
    │
    ├── GERENTE_PRODUTIVIDADE
    │   ├── /elena (TDAH)
    │   └── /coach (Accountability)
    │
    ├── GERENTE_FINANCAS
    │   └── /lucas (DeFi)
    │
    └── GUARDIAN (Validação)
        └── Loop Ralph

GEMINI (Antigravity)
    ├── 238 skills awesome-skills
    └── 7 skills nativas do vault
```

---

## INTEGRAÇÃO DAS NOVAS SKILLS

### Localização

```
.agent/skills/skills/     # 238 skills instaladas
.claude/skills/           # 4 skills Claude (devocionais, gemini-handoff, kabak, skill-creator)
.gemini/skills/           # 15 skills Gemini nativas
```

### Como Usar

As skills do awesome-skills são ativadas automaticamente pelo Gemini/Antigravity quando você menciona os triggers. Exemplos:

- "Quero escrever copy para landing page" → `copywriting`
- "Preciso auditar o SEO" → `seo-audit`
- "Vamos criar uma sequência de emails" → `email-sequence`
- "Desenhar arquitetura de agentes" → `ai-agents-architect`

---

## CRONOGRAMA Q1 2026

| Semana | Foco | Entrega |
|--------|------|---------|
| Sem 4 (Jan) | Planejamento | Este plano + Sync Gemini |
| Sem 1 (Fev) | KabaK Copy | 10 descritivos otimizados |
| Sem 2 (Fev) | KabaK SEO | Auditoria completa |
| Sem 3 (Fev) | Email Setup | 5 sequências automáticas |
| Sem 4 (Fev) | Agentes | Documentação arquitetura |
| Sem 1-4 (Mar) | KabaK Ads | Campanhas Google + Meta |
| Abril | LANÇAMENTO | KabaK go-live |

---

## MÉTRICAS DE SUCESSO

### KabaK

- [ ] ROAS > 4.0x
- [ ] Conversão > 2%
- [ ] CAC < R$ 50

### Sistema

- [ ] 0 erros de nomenclatura
- [ ] Sincronização Bi-IA funcionando
- [ ] Checkpoints semanais cumpridos

### Produtividade

- [ ] 3 blocos de deep work/dia
- [ ] Inbox zerada sexta 17h
- [ ] "Sapo" diário engolido

---

## COMANDOS RÁPIDOS

```bash
# Orquestração
/nevoa              # Ativar orquestrador

# Projetos
/kabak-agent        # Foco KabaK
/validate           # Validar antes de criar

# Produtividade
/elena              # Modo TDAH
/coach              # Accountability

# Sincronização
/sync               # Sync Claude ↔ Gemini
/mapa               # Índice do vault

# Contexto
/work               # Modo projetos
/learn              # Modo aprendizado
```

---

## NOTAS PARA GEMINI

**238 novas skills disponíveis** em `.agent/skills/skills/`

Prioridades de uso:
1. Marketing: copywriting, page-cro, seo-audit, email-sequence, paid-ads
2. IA: ai-agents-architect, prompt-engineer, rag-engineer
3. Docs: docx-official, xlsx-official

Formato de ativação: mencione o trigger e a skill é carregada automaticamente.

---

**Próxima revisão:** Sexta-feira 17h
**Responsável:** Névoa + Gassen

---

## CLAUDE-CODE-TEMPLATES (NOVO)

**Fonte:** github.com/davila7/claude-code-templates
**Instalação:** `npx claude-code-templates@latest`
**Docs:** docs.aitmpl.com

### 156 Agentes Disponíveis (Por Categoria)

#### AI Specialists (7)

| Agente | Propósito | Comando |
|--------|-----------|---------|
| `ai-ethics-advisor` | Ética em IA | `--agent ai-specialists/ai-ethics-advisor` |
| `prompt-engineer` | Otimização de prompts | `--agent ai-specialists/prompt-engineer` |
| `model-evaluator` | Avaliação de modelos | `--agent ai-specialists/model-evaluator` |
| `llms-maintainer` | Manutenção de LLMs | `--agent ai-specialists/llms-maintainer` |
| `search-specialist` | Busca semântica | `--agent ai-specialists/search-specialist` |
| `task-decomposition-expert` | Decomposição de tarefas | `--agent ai-specialists/task-decomposition-expert` |
| `hackathon-ai-strategist` | Estratégia hackathons | `--agent ai-specialists/hackathon-ai-strategist` |

#### Business & Marketing (9) ⭐ PRIORITÁRIO KABAK

| Agente | Propósito | Comando |
|--------|-----------|---------|
| `business-analyst` | Análise de negócio | `--agent business-marketing/business-analyst` |
| `content-marketer` | Marketing de conteúdo | `--agent business-marketing/content-marketer` |
| `customer-support` | Suporte ao cliente | `--agent business-marketing/customer-support` |
| `marketing-attribution-analyst` | Atribuição de conversões | `--agent business-marketing/marketing-attribution-analyst` |
| `payment-integration` | Integração pagamentos | `--agent business-marketing/payment-integration` |
| `product-strategist` | Estratégia de produto | `--agent business-marketing/product-strategist` |
| `sales-automator` | Automação de vendas | `--agent business-marketing/sales-automator` |
| `legal-advisor` | Consultoria jurídica | `--agent business-marketing/legal-advisor` |
| `risk-manager` | Gestão de riscos | `--agent business-marketing/risk-manager` |

#### Blockchain & Web3 (3) ⭐ PRIORITÁRIO DEFI

| Agente | Propósito | Comando |
|--------|-----------|---------|
| `smart-contract-auditor` | Auditoria de contratos | `--agent blockchain-web3/smart-contract-auditor` |
| `smart-contract-specialist` | Desenvolvimento Solidity | `--agent blockchain-web3/smart-contract-specialist` |
| `web3-integration-specialist` | Integração Web3 | `--agent blockchain-web3/web3-integration-specialist` |

#### Data & AI (8)

| Agente | Propósito | Comando |
|--------|-----------|---------|
| `ai-engineer` | Engenharia de IA | `--agent data-ai/ai-engineer` |
| `data-engineer` | Engenharia de dados | `--agent data-ai/data-engineer` |
| `data-scientist` | Ciência de dados | `--agent data-ai/data-scientist` |
| `ml-engineer` | Machine Learning | `--agent data-ai/ml-engineer` |
| `mlops-engineer` | MLOps | `--agent data-ai/mlops-engineer` |
| `nlp-engineer` | NLP | `--agent data-ai/nlp-engineer` |
| `quant-analyst` | Análise quantitativa | `--agent data-ai/quant-analyst` |
| `computer-vision-engineer` | Visão computacional | `--agent data-ai/computer-vision-engineer` |

#### Database (6)

| Agente | Propósito | Comando |
|--------|-----------|---------|
| `database-architect` | Arquitetura DB | `--agent database/database-architect` |
| `database-optimizer` | Otimização queries | `--agent database/database-optimizer` |
| `nosql-specialist` | NoSQL (MongoDB, etc) | `--agent database/nosql-specialist` |
| `supabase-schema-architect` | Supabase | `--agent database/supabase-schema-architect` |
| `database-admin` | Administração | `--agent database/database-admin` |
| `database-optimization` | Performance | `--agent database/database-optimization` |

#### Deep Research Team (12)

| Agente | Propósito | Comando |
|--------|-----------|---------|
| `research-orchestrator` | Orquestração de pesquisa | `--agent deep-research-team/research-orchestrator` |
| `academic-researcher` | Pesquisa acadêmica | `--agent deep-research-team/academic-researcher` |
| `competitive-intelligence-analyst` | Inteligência competitiva | `--agent deep-research-team/competitive-intelligence-analyst` |
| `data-analyst` | Análise de dados | `--agent deep-research-team/data-analyst` |
| `fact-checker` | Verificação de fatos | `--agent deep-research-team/fact-checker` |
| `report-generator` | Geração de relatórios | `--agent deep-research-team/report-generator` |
| `research-synthesizer` | Síntese de pesquisa | `--agent deep-research-team/research-synthesizer` |
| `technical-researcher` | Pesquisa técnica | `--agent deep-research-team/technical-researcher` |
| `query-clarifier` | Clarificação de queries | `--agent deep-research-team/query-clarifier` |
| `research-coordinator` | Coordenação | `--agent deep-research-team/research-coordinator` |
| `research-brief-generator` | Briefings | `--agent deep-research-team/research-brief-generator` |
| `agent-overview` | Visão geral agentes | `--agent deep-research-team/agent-overview` |

#### Development Team (8)

| Agente | Propósito | Comando |
|--------|-----------|---------|
| `backend-architect` | Arquitetura backend | `--agent development-team/backend-architect` |
| `frontend-developer` | Frontend | `--agent development-team/frontend-developer` |
| `fullstack-developer` | Fullstack | `--agent development-team/fullstack-developer` |
| `mobile-developer` | Mobile | `--agent development-team/mobile-developer` |
| `ios-developer` | iOS | `--agent development-team/ios-developer` |
| `ui-ux-designer` | UI/UX | `--agent development-team/ui-ux-designer` |
| `devops-engineer` | DevOps | `--agent development-team/devops-engineer` |
| `cli-ui-designer` | CLI Design | `--agent development-team/cli-ui-designer` |

#### Development Tools (9)

| Agente | Propósito | Comando |
|--------|-----------|---------|
| `code-reviewer` | Code review | `--agent development-tools/code-reviewer` |
| `debugger` | Debugging | `--agent development-tools/debugger` |
| `test-engineer` | Testes | `--agent development-tools/test-engineer` |
| `performance-profiler` | Profiling | `--agent development-tools/performance-profiler` |
| `error-detective` | Detecção de erros | `--agent development-tools/error-detective` |
| `mcp-expert` | MCP | `--agent development-tools/mcp-expert` |
| `command-expert` | Comandos Claude | `--agent development-tools/command-expert` |
| `context-manager` | Gestão de contexto | `--agent development-tools/context-manager` |
| `dx-optimizer` | Developer Experience | `--agent development-tools/dx-optimizer` |

#### DevOps & Infrastructure (8)

| Agente | Propósito | Comando |
|--------|-----------|---------|
| `cloud-architect` | Arquitetura cloud | `--agent devops-infrastructure/cloud-architect` |
| `terraform-specialist` | Terraform | `--agent devops-infrastructure/terraform-specialist` |
| `security-engineer` | Segurança | `--agent devops-infrastructure/security-engineer` |
| `monitoring-specialist` | Monitoramento | `--agent devops-infrastructure/monitoring-specialist` |
| `deployment-engineer` | Deploy | `--agent devops-infrastructure/deployment-engineer` |
| `vercel-deployment-specialist` | Vercel | `--agent devops-infrastructure/vercel-deployment-specialist` |
| `network-engineer` | Redes | `--agent devops-infrastructure/network-engineer` |
| `devops-troubleshooter` | Troubleshooting | `--agent devops-infrastructure/devops-troubleshooter` |

#### Documentation (4)

| Agente | Propósito | Comando |
|--------|-----------|---------|
| `technical-writer` | Documentação técnica | `--agent documentation/technical-writer` |
| `api-documenter` | Docs de API | `--agent documentation/api-documenter` |
| `changelog-generator` | Changelogs | `--agent documentation/changelog-generator` |
| `docusaurus-expert` | Docusaurus | `--agent documentation/docusaurus-expert` |

#### Obsidian Ops Team (7) ⭐ PRIORITÁRIO VAULT

| Agente | Propósito | Comando |
|--------|-----------|---------|
| `vault-optimizer` | Otimização de vault | `--agent obsidian-ops-team/vault-optimizer` |
| `moc-agent` | Gestão de MOCs | `--agent obsidian-ops-team/moc-agent` |
| `tag-agent` | Sistema de tags | `--agent obsidian-ops-team/tag-agent` |
| `metadata-agent` | Metadados YAML | `--agent obsidian-ops-team/metadata-agent` |
| `content-curator` | Curadoria de conteúdo | `--agent obsidian-ops-team/content-curator` |
| `connection-agent` | Links e conexões | `--agent obsidian-ops-team/connection-agent` |
| `review-agent` | Revisão de notas | `--agent obsidian-ops-team/review-agent` |

#### MCP Dev Team (7)

| Agente | Propósito | Comando |
|--------|-----------|---------|
| `mcp-server-architect` | Arquitetura MCP | `--agent mcp-dev-team/mcp-server-architect` |
| `mcp-integration-engineer` | Integrações | `--agent mcp-dev-team/mcp-integration-engineer` |
| `mcp-security-auditor` | Segurança MCP | `--agent mcp-dev-team/mcp-security-auditor` |
| `mcp-testing-engineer` | Testes MCP | `--agent mcp-dev-team/mcp-testing-engineer` |
| `mcp-protocol-specialist` | Protocolo | `--agent mcp-dev-team/mcp-protocol-specialist` |
| `mcp-registry-navigator` | Registry | `--agent mcp-dev-team/mcp-registry-navigator` |
| `mcp-deployment-orchestrator` | Deploy MCP | `--agent mcp-dev-team/mcp-deployment-orchestrator` |

#### Performance & Testing (5)

| Agente | Propósito | Comando |
|--------|-----------|---------|
| `performance-engineer` | Performance | `--agent performance-testing/performance-engineer` |
| `test-automator` | Automação testes | `--agent performance-testing/test-automator` |
| `load-testing-specialist` | Load testing | `--agent performance-testing/load-testing-specialist` |
| `web-vitals-optimizer` | Core Web Vitals | `--agent performance-testing/web-vitals-optimizer` |
| `react-performance-optimization` | React perf | `--agent performance-testing/react-performance-optimization` |

#### GraphQL (3)

| Agente | Propósito | Comando |
|--------|-----------|---------|
| `graphql-architect` | Arquitetura GraphQL | `--agent api-graphql/graphql-architect` |
| `graphql-performance-optimizer` | Performance | `--agent api-graphql/graphql-performance-optimizer` |
| `graphql-security-specialist` | Segurança | `--agent api-graphql/graphql-security-specialist` |

#### OCR & Document Processing (7)

| Agente | Propósito | Comando |
|--------|-----------|---------|
| `visual-analysis-ocr` | OCR visual | `--agent ocr-extraction-team/visual-analysis-ocr` |
| `document-structure-analyzer` | Estrutura docs | `--agent ocr-extraction-team/document-structure-analyzer` |
| `markdown-syntax-formatter` | Formatação MD | `--agent ocr-extraction-team/markdown-syntax-formatter` |
| `ocr-quality-assurance` | QA de OCR | `--agent ocr-extraction-team/ocr-quality-assurance` |
| `ocr-grammar-fixer` | Correção gramática | `--agent ocr-extraction-team/ocr-grammar-fixer` |
| `text-comparison-validator` | Validação texto | `--agent ocr-extraction-team/text-comparison-validator` |
| `ocr-preprocessing-optimizer` | Pré-processamento | `--agent ocr-extraction-team/ocr-preprocessing-optimizer` |

#### Game Development (4)

| Agente | Propósito | Comando |
|--------|-----------|---------|
| `game-designer` | Game design | `--agent game-development/game-designer` |
| `unity-game-developer` | Unity | `--agent game-development/unity-game-developer` |
| `unreal-engine-developer` | Unreal | `--agent game-development/unreal-engine-developer` |
| `3d-artist` | Arte 3D | `--agent game-development/3d-artist` |

#### Media & Content (Podcast/Video)

| Agente | Propósito | Comando |
|--------|-----------|---------|
| `video-editor` | Edição vídeo | `--agent ffmpeg-clip-team/video-editor` |
| `podcast-transcriber` | Transcrição | `--agent ffmpeg-clip-team/podcast-transcriber` |
| `social-media-clip-creator` | Clips sociais | `--agent ffmpeg-clip-team/social-media-clip-creator` |
| `audio-mixer` | Mixagem áudio | `--agent ffmpeg-clip-team/audio-mixer` |

#### Modernization (3)

| Agente | Propósito | Comando |
|--------|-----------|---------|
| `legacy-modernizer` | Modernização legacy | `--agent modernization/legacy-modernizer` |
| `architecture-modernizer` | Modernização arquitetura | `--agent modernization/architecture-modernizer` |
| `cloud-migration-specialist` | Migração cloud | `--agent modernization/cloud-migration-specialist` |

### 10 MCPs Disponíveis

| MCP | Propósito | Comando |
|-----|-----------|---------|
| `github-integration` | GitHub API | `--mcp github-integration` |
| `postgresql-integration` | PostgreSQL | `--mcp postgresql-integration` |
| `mysql-integration` | MySQL | `--mcp mysql-integration` |
| `memory-integration` | Memória persistente | `--mcp memory-integration` |
| `filesystem-access` | Acesso a arquivos | `--mcp filesystem-access` |
| `web-fetch` | Fetch web | `--mcp web-fetch` |
| `deepgraph-react` | React graphs | `--mcp deepgraph-react` |
| `deepgraph-nextjs` | Next.js graphs | `--mcp deepgraph-nextjs` |
| `deepgraph-typescript` | TS graphs | `--mcp deepgraph-typescript` |
| `deepgraph-vue` | Vue graphs | `--mcp deepgraph-vue` |

### Skills por Categoria

| Categoria | Exemplos | Comando |
|-----------|----------|---------|
| `creative-design` | algorithmic-art | `--skill creative-design/algorithmic-art` |
| `development` | (a explorar) | `--skill development/[nome]` |
| `document-processing` | (a explorar) | `--skill document-processing/[nome]` |
| `enterprise-communication` | (a explorar) | `--skill enterprise-communication/[nome]` |

### Comandos Disponíveis

| Comando | Propósito |
|---------|-----------|
| `check-file` | Verificar arquivo |
| `generate-tests` | Gerar testes |

### Ferramentas CLI

```bash
# Analytics em tempo real
npx claude-code-templates@latest --analytics

# Interface mobile para chats
npx claude-code-templates@latest --chats

# Health check do Claude Code
npx claude-code-templates@latest --health-check

# Dashboard de plugins
npx claude-code-templates@latest --plugins

# Gerenciador de skills
npx claude-code-templates@latest --skills-manager

# Studio (execução local e cloud)
npx claude-code-templates@latest --studio
```

---

## MAPEAMENTO: PRIORIDADES → AGENTES

### P1: KABAK (E-commerce)

| Necessidade | Agente Recomendado |
|-------------|-------------------|
| Copy produtos | `business-marketing/content-marketer` |
| Atribuição conversões | `business-marketing/marketing-attribution-analyst` |
| Integração pagamento | `business-marketing/payment-integration` |
| Automação vendas | `business-marketing/sales-automator` |
| Suporte cliente | `business-marketing/customer-support` |
| Análise negócio | `business-marketing/business-analyst` |
| Core Web Vitals | `performance-testing/web-vitals-optimizer` |
| PostgreSQL | MCP `postgresql-integration` |

### P2: Sistema de Agentes

| Necessidade | Agente Recomendado |
|-------------|-------------------|
| Arquitetura MCP | `mcp-dev-team/mcp-server-architect` |
| Integração MCP | `mcp-dev-team/mcp-integration-engineer` |
| Segurança MCP | `mcp-dev-team/mcp-security-auditor` |
| Otimização prompts | `ai-specialists/prompt-engineer` |
| Decomposição tarefas | `ai-specialists/task-decomposition-expert` |
| Memória | MCP `memory-integration` |

### P3: DeFi

| Necessidade | Agente Recomendado |
|-------------|-------------------|
| Auditoria contratos | `blockchain-web3/smart-contract-auditor` |
| Desenvolvimento Solidity | `blockchain-web3/smart-contract-specialist` |
| Integração Web3 | `blockchain-web3/web3-integration-specialist` |
| Análise quantitativa | `data-ai/quant-analyst` |

### P4: Vault Obsidian

| Necessidade | Agente Recomendado |
|-------------|-------------------|
| Otimização vault | `obsidian-ops-team/vault-optimizer` |
| Gestão MOCs | `obsidian-ops-team/moc-agent` |
| Sistema tags | `obsidian-ops-team/tag-agent` |
| Metadados | `obsidian-ops-team/metadata-agent` |
| Curadoria | `obsidian-ops-team/content-curator` |
| Links | `obsidian-ops-team/connection-agent` |
| Revisão | `obsidian-ops-team/review-agent` |

---

## INSTALAÇÃO RÁPIDA (Exemplos)

```bash
# Instalar agente de business para KabaK
npx claude-code-templates@latest --agent business-marketing/content-marketer

# Instalar MCP PostgreSQL
npx claude-code-templates@latest --mcp postgresql-integration

# Instalar skill de arte algorítmica
npx claude-code-templates@latest --skill creative-design/algorithmic-art

# Instalar múltiplos agentes
npx claude-code-templates@latest --agent business-marketing/business-analyst,business-marketing/sales-automator

# Ver diagnóstico do sistema
npx claude-code-templates@latest --health-check
```

---

**Próxima revisão:** Sexta-feira 17h
**Responsável:** Névoa + Gassen

---

*"Clareza antes de velocidade. Execução antes de perfeição."*
