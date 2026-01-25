# PLANO ESTRATÉGICO: SEGUNDO CÉREBRO 2026

**Criado:** 24/Jan/2026
**Autor:** Névoa (Orquestrador)
**Status:** ATIVO

---

## VISÃO GERAL

**Sistema:** Névoa + Alan Nicolas (Híbrido) + Bi-IA (Claude + Gemini)
**Versão:** 2.4.1 | **Fase:** 7.4 COMPLETA
**Arquivos:** 11.108+ | **Projetos:** 8 ativos | **Agentes:** 9

### Recursos Novos Disponíveis

- **238 skills** do repositório `antigravity-awesome-skills` instaladas
- Localização: `.agent/skills/skills/`
- Categorias: IA & Agentes, Marketing/CRO, Desenvolvimento, Documentos, Workflow

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

*"Clareza antes de velocidade. Execução antes de perfeição."*
