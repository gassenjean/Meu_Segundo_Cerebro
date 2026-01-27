---
created: 2026-01-26T11:40
updated: 2026-01-26T14:11
---
# Projeto: Névoa Impecável

**Data:** 26/Jan/2026
**Objetivo:** Estruturar Névoa para cuidar da vida completa de Gassen com excelência
**Prioridade:** MÁXIMA - Nenhum outro projeto até isto estar aprovado

---

## 1. Inventário Atual

### 1.1 Claude Code (.claude/)

**Comandos (18 ativos):**

| Comando | Domínio | Status |
| ------- | ------- | ------ |
| `/nevoa` | iOS Master | Ativo |
| `/coach` | TDAH/Produtividade | Ativo |
| `/pedro` | Tráfego/Marketing | Ativo |
| `/alan` | IA/Automação | Ativo |
| `/lucas` | DeFi/Finanças | Ativo |
| `/marie-kondo` | QA/Organização | Ativo |
| `/kabak-agent` | Projeto KabaK | Ativo |
| `/google` | Ecossistema Google | Ativo |
| `/fe` | Fé/Propósito | Ativo |
| `/familia` | Família | Ativo |
| `/tdah` | TDAH específico | Ativo |
| `/assistente` | Pessoal 80/20 | Ativo |
| `/dev` | Desenvolvimento | Ativo |
| `/mode` | Contexto | Ativo |
| `/validate` | Validação | Ativo |
| `/mapa` | Indexação | Ativo |
| `/sync` | Bi-IA | Ativo |
| `/ultra-think` | Análise profunda | Ativo |
| `/claude-architect` | Qualidade | Ativo |
| `/gemini` | Delegação | Ativo |

**Skills Claude (6):**
- skill-creator
- kabak
- gemini-handoff
- alan-vault-researcher
- coach
- google-workspace

**Agents Claude (29):**
- business-analyst, content-marketer, marketing-attribution-analyst
- moc-agent, vault-optimizer, connection-agent, content-curator
- metadata-agent, review-agent, tag-agent
- mcp-* (4 agentes MCP)
- prompt-engineer, search-specialist, task-decomposition-expert
- competitive-intelligence-analyst, fact-checker
- research-orchestrator, research-synthesizer
- code-reviewer, mcp-expert, technical-writer
- ui-ux-designer, markdown-syntax-formatter, visual-analysis-ocr
- agent-expert, architect-review

### 1.2 Antigravity (.agent/)

**Workflows Ativos (9):**
- sync
- start
- deep-research-alan
- guardian
- gemini-guardian
- gerente-conhecimento
- gerente-financas
- nevoa
- gerente-produtividade

**Skills Awesome (238+):**
- ai-agents-architect, autonomous-agents, agent-memory-systems
- copywriting, paid-ads, page-cro, seo-audit
- E 230+ outras...

### 1.3 Gemini (.gemini/)

**Skills (12):**
- vault-organizer, vault-auditor
- session-logger, session-log-archiver
- status-updater, validate, mapa
- context-manager, architect-linter
- kabak, gemini-handoff, alan-researcher

**Configuração:**
- GEMINI.md
- gemini-guardian.md

### 1.4 Bi-IA (.bi-ia/)

**Arquivos de Estado:**
- state.json (tarefas pendentes/completas)
- COMPROMISSOS_NEVOA.md
- PEDIDOS_GASSEN_PENDENTES.md
- GEMINI_AUTONOMY_LOG.md
- handoffs/ (30+ arquivos)

---

## 2. O que falta pesquisar

### 2.1 Sobre Névoa/Orquestração

| Pergunta | Por que importa |
| -------- | --------------- |
| Como Alan Nicolas estrutura o iOS Master? | Replicar modelo comprovado |
| Qual a diferença entre command, skill, agent, workflow? | Usar cada um corretamente |
| Como fazer Névoa delegar automaticamente? | Autonomia real |
| Como implementar "reuniões entre gerentes"? | Consolidação de outputs |
| Qual o limite de comandos eficiente? | Não sobrecarregar |

### 2.2 Sobre Automação

| Pergunta | Por que importa |
| -------- | --------------- |
| n8n vs GitHub Actions para nosso caso? | Escolher ferramenta certa |
| O que já temos de n8n configurado? | Não duplicar trabalho |
| Como integrar n8n com Claude/Gemini? | Automação real |
| Hooks do Claude Code - como funcionam? | Triggers automáticos |

### 2.3 Sobre Antigravity/Gemini

| Pergunta | Por que importa |
| -------- | --------------- |
| Como Gemini delega internamente entre seus agentes? | Orquestração paralela |
| Quais skills do awesome-skills usamos? | Não reinventar roda |
| Como fazer Gemini pesquisar 24/7 de verdade? | Pesquisa contínua |

---

## 3. Plano de Pesquisa

### Fase 1: Pesquisa Profunda (Delegar para Gemini)

**T035: Pesquisar modelo Alan Nicolas - iOS Master**
```yaml
Objetivo: Entender EXATAMENTE como Alan estrutura o orquestrador
Fontes:
  - 02_PROJETOS/Estudo_Alan_Nicolas/conceitos/
  - 01_CONHECIMENTO/IA_Tecnologia/Alan_Nicolas/
  - Transcrições de lives
Output: PESQUISA_iOS_MASTER_ALAN.md
Prazo: 48h
```

**T036: Pesquisar hooks Claude Code**
```yaml
Objetivo: Como usar hooks para automação
Fontes:
  - Documentação oficial Claude Code
  - Exemplos de uso
Output: PESQUISA_HOOKS_CLAUDE.md
Prazo: 24h
```

**T037: Pesquisar n8n vs GitHub Actions**
```yaml
Objetivo: Qual melhor para nosso caso de uso
Critérios:
  - Facilidade de setup
  - Integração com IA
  - Custo
  - Manutenção
Output: COMPARATIVO_N8N_GITHUB_ACTIONS.md
Prazo: 24h
```

**T038: Mapear skills úteis do awesome-skills**
```yaml
Objetivo: Quais das 238 skills são relevantes para nós
Categorias prioritárias:
  - ai-agents-*
  - copywriting, marketing
  - automation
  - productivity
Output: MAPA_SKILLS_PRIORITARIAS.md
Prazo: 48h
```

### Fase 2: Consolidação (Névoa)

Após pesquisas, criar:

1. **PROTOCOLO_NEVOA_DEFINITIVO.md** - Como eu opero
2. **MAPA_AGENTES_ESSENCIAIS.md** - Quem faz o quê
3. **ARQUITETURA_AUTOMACAO.md** - n8n/hooks/triggers
4. **CHECKLIST_APROVACAO.md** - Validação final

### Fase 3: Implementação

1. Reduzir comandos para essenciais
2. Configurar automação escolhida
3. Testar fluxos completos
4. Documentar e aprovar

---

## 4. Decisões Pendentes de Gassen

### Prioridade de Domínios

Ordenar de 1 a 7 (1 = mais importante):

- [ ] Fé (/fe)
- [ ] Família (/familia)
- [ ] Saúde Mental (/tdah, /coach)
- [ ] Projetos (/kabak-agent)
- [ ] Finanças (/lucas)
- [ ] Conhecimento (/alan, /marie-kondo)
- [ ] Desenvolvimento (/dev)

### Comandos Essenciais

Dos 20 comandos atuais, quais manter?

**Proposta de redução para 10 essenciais:**

| # | Comando | Motivo |
| - | ------- | ------ |
| 1 | `/nevoa` | iOS Master (obrigatório) |
| 2 | `/coach` | TDAH + produtividade (absorve /tdah) |
| 3 | `/fe` | Fé + propósito |
| 4 | `/familia` | Família |
| 5 | `/kabak-agent` | Projeto prioritário |
| 6 | `/alan` | IA + automação |
| 7 | `/lucas` | Finanças + DeFi |
| 8 | `/marie-kondo` | QA + organização (absorve /validate) |
| 9 | `/sync` | Bi-IA |
| 10 | `/mapa` | Navegação |

**Candidatos a remover/absorver:**
- `/pedro` → absorvido por `/kabak-agent`
- `/assistente` → absorvido por `/coach`
- `/dev` → usar só quando precisar
- `/google` → absorvido por `/sync`
- `/mode` → flags em outros comandos
- `/ultra-think` → modo dentro de `/nevoa`
- `/claude-architect` → absorvido por `/marie-kondo`
- `/gemini` → absorvido por `/sync`

### Automação

- [ ] n8n (mais poderoso, curva maior)
- [ ] GitHub Actions (mais simples, integrado)
- [ ] Ambos (n8n para complexo, Actions para simples)

---

## 5. Próximos Passos

### AGORA

1. [ ] Aprovar este documento como plano oficial
2. [ ] Gassen: responder decisões pendentes
3. [ ] Criar handoffs T035-T038 para Gemini

### ESTA SEMANA

1. [ ] Gemini executa T035-T038
2. [ ] Névoa consolida pesquisas
3. [ ] Criar PROTOCOLO_NEVOA_DEFINITIVO.md

### PRÓXIMA SEMANA

1. [ ] Implementar comandos essenciais
2. [ ] Configurar automação
3. [ ] Testar e aprovar

---

## 6. Critérios de "Impecável"

### Névoa está impecável quando:

- [ ] Delega 100% (nunca executa o que gerente pode fazer)
- [ ] Não perde contexto entre sessões
- [ ] Gemini pesquisa continuamente
- [ ] Automação dispara sem intervenção
- [ ] Cobre vida completa (fé, família, TDAH, projetos, finanças)
- [ ] Gassen só decide, não opera
- [ ] Métricas são medidas, não sentidas

---

**Criado:** 26/Jan/2026
**Status:** AGUARDANDO APROVAÇÃO
**Responsável:** Névoa 6.0
