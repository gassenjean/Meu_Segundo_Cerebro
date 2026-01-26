# Plano de Evolução Névoa 5.0 → 6.0

**Data:** 26/Jan/2026
**Autor:** Névoa 5.0 + Gassen
**Objetivo:** Repertório fenomenal de gerentes e skills
**Status:** Em planejamento

---

## 1. Inventário Atual

### 1.1 Comandos Claude (16 total)

| Comando | Tipo | Função | Status |
| ------- | ---- | ------ | ------ |
| `/nevoa` | iOS Master | Orquestrador supremo | ✅ Ativo |
| `/claude-architect` | Plataforma | Qualidade e padrões | ✅ Ativo |
| `/coach` | Domínio | Produtividade TDAH | ✅ Ativo |
| `/pedro` | Domínio | Tráfego pago | ✅ Ativo |
| `/lucas` | Domínio | DeFi/Portfolio | ✅ Ativo |
| `/alan` | Domínio | IA/Automação | ✅ Ativo |
| `/marie-kondo` | Domínio | QA/Vault | ✅ Ativo |
| `/kabak-agent` | Projeto | KabaK E-commerce | ✅ Ativo |
| `/google` | Plataforma | Ecossistema Google | ✅ Ativo |
| `/gemini` | Delegação | Handoff para Gemini | ✅ Ativo |
| `/validate` | Ferramenta | Validação arquivos | ✅ Ativo |
| `/mapa` | Ferramenta | Índice inteligente | ✅ Ativo |
| `/ultra-think` | Ferramenta | Análise profunda | ✅ Ativo |
| `/sync` | Ferramenta | Sincronização Bi-IA | ✅ Ativo |
| `/learn` | Contexto | Modo aprendizado | ✅ Ativo |
| `/work` | Contexto | Modo projetos | ✅ Ativo |

**Limite:** 15 comandos (atualmente 16 - precisa consolidar)

### 1.2 Skills Claude (4 total)

| Skill | Função | Maturidade |
| ----- | ------ | ---------- |
| `skill-creator/` | Criação de novas skills | ✅ Produção |
| `kabak/` | Templates e workflows KabaK | ✅ Produção |
| `gemini-handoff/` | Delegação para Gemini | ✅ Produção |
| `alan-vault-researcher/` | Pesquisa vault Alan Nicolas | 🔄 Beta |

### 1.3 Workflows Gemini (14 total)

| Workflow | Função | Sincronizado |
| -------- | ------ | ------------ |
| `/nevoa` | Orquestrador | ✅ |
| `/sync` | Sincronização | ✅ |
| `/start` | Boot sessão | ✅ |
| `/guardian` | Guardian principal | ✅ |
| `/gemini-guardian` | Alias Guardian | ✅ |
| `/gerente-conhecimento` | Gestão conhecimento | ⚠️ Sem equivalente Claude |
| `/gerente-financas` | Gestão financeira | ⚠️ Sem equivalente Claude |
| `/gerente-produtividade` | Produtividade | ✅ = /coach |
| `/gerente-projetos` | Gestão projetos | ⚠️ Sem equivalente Claude |
| `/deep-research-alan` | Pesquisa profunda | ✅ |
| `/google` | Gerente Google | ✅ |
| `/alan` | Agente Alan | ✅ |
| `/kabak-agent` | Agente KabaK | ✅ |
| `/gemini` | Auto-referência | ✅ |

### 1.4 Skills Gemini (13 total)

| Skill | Função | Exclusiva |
| ----- | ------ | --------- |
| `kabak/` | KabaK templates | Espelhada |
| `gemini-handoff/` | Handoff | Espelhada |
| `vault-organizer/` | Organização bulk | ✅ Gemini |
| `status-updater/` | Atualização status | ✅ Gemini |
| `session-logger/` | Log de sessões | ✅ Gemini |
| `session-log-archiver/` | Arquivamento logs | ✅ Gemini |
| `vault-auditor/` | Auditoria vault | ✅ Gemini |
| `validate/` | Validação | Espelhada |
| `mapa/` | Índice | Espelhada |
| `context-manager/` | Gestão contexto | ✅ Gemini |
| `architect-linter/` | Linting MD | ✅ Gemini |
| `alan-researcher/` | Pesquisa Alan | ✅ Gemini |
| `guardian/` | Scripts Guardian | ✅ Gemini |

### 1.5 Prompts Agentes (16 total)

| Prompt | Status | Observação |
| ------ | ------ | ---------- |
| `PROMPT_NEVOA_5.0.md` | ✅ Ativo | Versão atual |
| `PROMPT_NEVOA_4.2.md` | 📦 Legacy | Manter backup |
| `PROMPT_AGENTE_CLAUDE_ARCHITECT.md` | ✅ Ativo | |
| `PROMPT_AGENTE_PEDRO_SOBRAL.md` | ✅ Ativo | |
| `PROMPT_AGENTE_LUCAS_AMOEDO.md` | ✅ Ativo | |
| `PROMPT_AGENTE_ALAN_NICOLAS.md` | ✅ Ativo | |
| `PROMPT_AGENTE_MARIE_KONDO.md` | ✅ Ativo | |
| `PROMPT_AGENTE_ELENA_VASQUEZ.md` | 📦 Absorvido | → /coach |
| `PROMPT_AGENTE_DR_GREEN.md` | ⚠️ Inativo | Potencial /saude |
| `PROMPT_AGENTE_KABAK.md` | ✅ Ativo | |
| `PROMPT_AGENTE_SUPORTE_KABAK.md` | ⚠️ Específico | Sub-agente |
| `PROMPT_AGENTE_PESQUISA_MERCADO_KABAK.md` | ⚠️ Específico | Sub-agente |
| `PROMPT_AGENTE_BENCHMARK_KABAK.md` | ⚠️ Específico | Sub-agente |
| `PROMPT_GERENTE_GOOGLE.md` | ✅ Ativo | |
| `PROMPT_AGENTE_GEMINI_GUARDIAN.md` | ✅ Ativo | |
| `PROMPT_AGENTE_GOOGLE_IO.md` | ⚠️ Redundante | → /google |

---

## 2. Análise de Gaps

### 2.1 Gerentes que Faltam

| Gap | Necessidade | Prioridade | Justificativa |
| --- | ----------- | ---------- | ------------- |
| **Gerente Finanças** | Alta | 🔴 P1 | Workflow Gemini existe, Claude não tem |
| **Gerente Jurídico** | Alta | 🔴 P1 | KabaK precisa, Dr. Alexandre ativo |
| **Gerente Conteúdo** | Média | 🟡 P2 | Blog, social media, copywriting |
| **Gerente Conhecimento** | Média | 🟡 P2 | Workflow Gemini existe |
| **Gerente Saúde** | Baixa | 🟢 P3 | Dr. Green existe, reativar |
| **Gerente Relacionamentos** | Baixa | 🟢 P3 | CRM, networking |

### 2.2 Skills que Faltam

| Gap | Função | Prioridade | Onde |
| --- | ------ | ---------- | ---- |
| `research-rpi/` | Framework RPI automatizado | 🔴 P1 | Claude + Gemini |
| `ralph-qa/` | Quality gate automático | 🔴 P1 | Claude + Gemini |
| `daily-brief/` | Resumo diário proativo | 🟡 P2 | Claude |
| `meeting-prep/` | Preparação reuniões | 🟡 P2 | Claude + Gemini |
| `competitor-intel/` | Inteligência competitiva | 🟡 P2 | Gemini |
| `content-creator/` | Criação de conteúdo | 🟢 P3 | Claude + Gemini |

### 2.3 Problemas de Sincronização

| Problema | Impacto | Solução |
| -------- | ------- | ------- |
| Comandos Claude > Limite 15 | Confusão | Consolidar /learn + /work |
| Workflows Gemini sem equivalente Claude | Assimetria | Criar comandos faltantes |
| Skills não espelhadas | Funcionalidade limitada | Espelhar prioritárias |
| Prompts redundantes | Manutenção | Arquivar obsoletos |

---

## 3. Hierarquia Proposta (Névoa 6.0)

```text
NÉVOA 6.0 (iOS Master)
│
├── GERENTES DE PLATAFORMA
│   ├── /claude-architect → Qualidade Claude
│   └── /google → Ecossistema Google (Gemini, Sheets, Looker, AppSheet...)
│
├── GERENTES DE DOMÍNIO (Expertise Pessoal)
│   ├── /coach → Produtividade (TDAH) [Tom: Névoa direto]
│   ├── /pedro → Marketing (Tráfego Pago) [Tom: Pedro Sobral]
│   ├── /lucas → DeFi (Portfolio) [Tom: Lucas Amoedo]
│   ├── /alan → IA (Automação, Agentes, N8N) [Tom: Alan Nicolas]
│   ├── /marie-kondo → QA (Vault, Organização) [Tom: Marie Kondo]
│   ├── /financas → Finanças (Pessoal + Projetos) [NOVO]
│   ├── /juridico → Jurídico (Contratos, Societário) [NOVO]
│   └── /conteudo → Conteúdo (Blog, Social, Copy) [NOVO]
│
├── GERENTES DE PROJETO
│   └── /kabak-agent → KabaK (E-commerce Fitness)
│   └── [Futuros projetos aqui]
│
└── FERRAMENTAS (Não são gerentes, são utilities)
    ├── /validate → Validação de arquivos
    ├── /mapa → Índice inteligente do vault
    ├── /ultra-think → Análise profunda
    ├── /sync → Sincronização Bi-IA
    └── /context → Contexto (fusão learn+work) [CONSOLIDADO]
```

### 3.1 Novos Gerentes Propostos

#### /financas - Gerente Finanças

```yaml
Nome: Gerente Finanças
Domínio: Finanças pessoais e de projetos
Expertise:
  - Orçamentos e projeções
  - Fluxo de caixa
  - Investimentos
  - Tributação básica
Tom: Profissional, números precisos
Delegação:
  - Planilhas complexas → /google (Sheets)
  - Dashboards → /google (Looker)
Exemplos de uso:
  - "Qual meu fluxo de caixa este mês?"
  - "Projeção de receita KabaK 6 meses"
  - "Onde estou gastando demais?"
```

#### /juridico - Gerente Jurídico

```yaml
Nome: Gerente Jurídico
Domínio: Assuntos legais e societários
Expertise:
  - Contratos (revisão, minutas)
  - Estrutura societária
  - Compliance
  - Marcas e patentes
Tom: Cauteloso, detalhista
Delegação:
  - Pesquisa jurisprudência → /google (Search)
  - Documentos longos → Gemini
Exemplos de uso:
  - "Revisar cláusula X do contrato"
  - "Checklist para abertura de empresa"
  - "Implicações de acordo de sócios"
Integração:
  - Conectar com docs Dr. Alexandre
  - Usar CHECKLIST_DOCS_DR_ALEXANDRE como referência
```

#### /conteudo - Gerente Conteúdo

```yaml
Nome: Gerente Conteúdo
Domínio: Criação e estratégia de conteúdo
Expertise:
  - Blog posts e artigos
  - Social media (captions, threads)
  - Copywriting (vendas, email)
  - SEO básico
Tom: Criativo, persuasivo
Delegação:
  - Imagens → /google (ImageFX)
  - Pesquisa tendências → /google (Trends)
  - Textos longos → Gemini
Exemplos de uso:
  - "Criar post sobre [tema] para Instagram"
  - "Thread Twitter sobre [assunto]"
  - "Copy para landing page KabaK"
```

---

## 4. Skills Prioritárias

### 4.1 Skill: research-rpi (P1)

```yaml
Nome: research-rpi
Função: Automatizar framework RPI em pesquisas
Estrutura:
  - SKILL.md (instruções)
  - templates/TEMPLATE_RESEARCH.md
  - templates/TEMPLATE_PLAN.md
  - scripts/save_research.py (salvar em arquivo)
Workflow:
  1. Research: Coletar informações, salvar em RESEARCH_*.md
  2. Plan: Criar plano de implementação
  3. Implement: Executar em sessão limpa
Gatilho: "pesquisa [tema]" ou "/research [tema]"
```

### 4.2 Skill: ralph-qa (P1)

```yaml
Nome: ralph-qa
Função: Quality Gate automático antes de entregas
Estrutura:
  - SKILL.md (checklist Ralph)
  - scripts/validate_output.py
Checklist:
  - [ ] Completo? (Todos itens)
  - [ ] Correto? (Padrões vault)
  - [ ] Útil? (Resolve problema)
  - [ ] Limpo? (Sem TODOs/erros)
Gatilho: Automático antes de qualquer entrega significativa
```

### 4.3 Skill: daily-brief (P2)

```yaml
Nome: daily-brief
Função: Resumo diário proativo ao iniciar sessão
Estrutura:
  - SKILL.md
  - templates/TEMPLATE_DAILY.md
Conteúdo:
  - Tarefas pendentes (state.json)
  - Eventos do dia (calendário)
  - Progresso projetos
  - Lembretes importantes
Gatilho: "/daily" ou automático no boot
```

### 4.4 Skill: meeting-prep (P2)

```yaml
Nome: meeting-prep
Função: Preparar reuniões automaticamente
Estrutura:
  - SKILL.md
  - templates/TEMPLATE_TALKING_POINTS.md
  - templates/TEMPLATE_AGENDA.md
Workflow:
  1. Identificar reunião (data, participantes)
  2. Buscar contexto no vault
  3. Gerar talking points
  4. Criar agenda sugerida
Gatilho: "/prep [reunião]"
```

---

## 5. Roadmap de Implementação

### Fase 1: Consolidação (Semana 27-31/Jan)

| Tarefa | Responsável | Prioridade |
| ------ | ----------- | ---------- |
| Consolidar /learn + /work → /context | Claude | 🔴 |
| Arquivar prompts obsoletos (Elena, Google_IO) | Claude | 🔴 |
| Criar /financas (comando + prompt) | Claude | 🔴 |
| Criar /juridico (comando + prompt) | Claude | 🔴 |
| Sincronizar comandos Claude → Gemini | Gemini | 🟡 |

### Fase 2: Skills Core (Semana 03-07/Fev)

| Tarefa | Responsável | Prioridade |
| ------ | ----------- | ---------- |
| Criar skill research-rpi/ | Claude | 🔴 |
| Criar skill ralph-qa/ | Claude | 🔴 |
| Espelhar skills para Gemini | Gemini | 🟡 |
| Testar workflow completo RPI | Claude + Gemini | 🟡 |

### Fase 3: Expansão (Semana 10-14/Fev)

| Tarefa | Responsável | Prioridade |
| ------ | ----------- | ---------- |
| Criar /conteudo (comando + prompt) | Claude | 🟡 |
| Criar skill daily-brief/ | Claude | 🟡 |
| Criar skill meeting-prep/ | Claude | 🟡 |
| Documentar hierarquia completa | Claude | 🟡 |

### Fase 4: Otimização (Semana 17-21/Fev)

| Tarefa | Responsável | Prioridade |
| ------ | ----------- | ---------- |
| Reativar /saude (Dr. Green) | Claude | 🟢 |
| Criar skill competitor-intel/ | Gemini | 🟢 |
| Auditoria completa do sistema | Marie Kondo | 🟢 |
| Publicar Névoa 6.0 | Claude | 🟢 |

---

## 6. Métricas de Sucesso

| Métrica | Atual | Meta Névoa 6.0 |
| ------- | ----- | -------------- |
| Comandos Claude | 16 | 15 (limite) |
| Skills Claude | 4 | 8 |
| Gerentes Domínio | 5 | 8 |
| Skills Gemini | 13 | 15 |
| Sincronização Claude↔Gemini | 70% | 95% |
| Uso de RPI em tarefas | 30% | 100% |
| Ralph Loop em entregas | 50% | 100% |

---

## 7. Decisões Necessárias (Gassen)

### 7.1 Prioridade dos Novos Gerentes

| Opção | Descrição |
| ----- | --------- |
| A | /financas primeiro (fluxo de caixa KabaK) |
| B | /juridico primeiro (Dr. Alexandre ativo) |
| C | Ambos em paralelo |

### 7.2 Consolidação de Comandos

| Opção | Descrição |
| ----- | --------- |
| A | Manter /learn e /work separados |
| B | Consolidar em /context (economia 1 slot) |

### 7.3 Investimento em Skills

| Opção | Descrição |
| ----- | --------- |
| A | Foco em skills de produtividade (RPI, Ralph, Daily) |
| B | Foco em skills de projeto (meeting-prep, competitor-intel) |
| C | Balanceado (2 de cada) |

---

## 8. Anexos

### A. Estrutura de Diretórios Proposta

```text
.claude/
├── commands/
│   ├── nevoa.md
│   ├── claude-architect.md
│   ├── google.md
│   ├── coach.md
│   ├── pedro.md
│   ├── lucas.md
│   ├── alan.md
│   ├── marie-kondo.md
│   ├── financas.md      [NOVO]
│   ├── juridico.md      [NOVO]
│   ├── conteudo.md      [NOVO]
│   ├── kabak-agent.md
│   ├── validate.md
│   ├── mapa.md
│   ├── ultra-think.md
│   ├── sync.md
│   └── context.md       [CONSOLIDADO]
│
└── skills/
    ├── skill-creator/
    ├── kabak/
    ├── gemini-handoff/
    ├── alan-vault-researcher/
    ├── research-rpi/    [NOVO]
    ├── ralph-qa/        [NOVO]
    ├── daily-brief/     [NOVO]
    └── meeting-prep/    [NOVO]
```

### B. Template de Novo Gerente

```markdown
# Gerente [Nome]

**Domínio:** [Área de atuação]
**Tom:** [Personalidade]
**Ativo desde:** [Data]

## Expertise

- [Área 1]
- [Área 2]
- [Área 3]

## Delegação

| Tarefa | Delegar Para |
| ------ | ------------ |
| [Tipo 1] | [Agente] |
| [Tipo 2] | [Agente] |

## Exemplos de Uso

- "[Pergunta típica 1]"
- "[Pergunta típica 2]"

## Conexões

- [[Gerente Relacionado 1]]
- [[Skill Relacionada]]
```

---

**Próximo passo:** Aprovar prioridades e iniciar Fase 1.

**Criado por:** Névoa 5.0
**Revisão:** Gassen
