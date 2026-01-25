---
created: 2026-01-24T23:00
updated: 2026-01-24T23:39
---
# PLANO MASTER 2026: Segundo Cérebro + Hierarquia de Agentes

**Status:** ATIVO
**Versão:** 1.0
**Autor:** Névoa (Orquestrador)
**Consolidado de:** PLANO_SEGUNDO_CEREBRO_2026 + PLANO_Hierarquia_Agentes_Alan + PLANO_ORGANIZACAO_TOTAL_2026

---

## PARTE 1: VISÃO ESTRATÉGICA

### 1.1 Estado Atual

| Métrica | Valor |
| ------- | ----- |
| Arquivos no Vault | 11.108+ |
| Skills (awesome-skills) | 238 |
| Agentes instalados (.claude/agents/) | 53 |
| Agentes disponíveis (templates) | 156 |
| Projetos ativos | 8 |
| Fase atual | 7.5 |

### 1.2 Prioridades 2026

| # | Projeto | Meta | Prazo | Skills Chave |
| - | ------- | ---- | ----- | ------------ |
| P1 | KabaK | Lançar e-commerce | Abril/2026 | copywriting, seo-audit, paid-ads |
| P2 | Sistema Agentes | Orquestração robusta | Contínuo | ai-agents-architect, langgraph |
| P3 | DeFi | Gestão ativa portfólio | 3 meses | quant-analyst, smart-contract-auditor |
| P4 | Produtividade TDAH | Sistema sustentável | Contínuo | concise-planning, executing-plans |

### 1.3 Cronograma Q1 2026

| Semana | Foco | Entrega |
| ------ | ---- | ------- |
| Sem 4 (Jan) | Planejamento + Triagem Inbox | Este plano + Inbox Zero |
| Sem 1 (Fev) | KabaK Copy | 10 descritivos otimizados |
| Sem 2 (Fev) | KabaK SEO | Auditoria completa |
| Sem 3 (Fev) | Email Setup | 5 sequências automáticas |
| Sem 4 (Fev) | Agentes | Documentação arquitetura |
| Março | KabaK Ads | Campanhas Google + Meta |
| Abril | LANÇAMENTO | KabaK go-live |

---

## PARTE 2: ARQUITETURA DE AGENTES (Alan Nicolas)

### 2.1 Hierarquia de Comando

```
GASSEN (Você)
    ↓
NÉVOA (Master Orquestrador)
    │
    ├── GERENTE_CONHECIMENTO
    │   ├── /alan (IA & Automação)
    │   ├── /marie-kondo (Organização)
    │   ├── /mapa (Indexação)
    │   └── /dr-green (Cultivo - Domínio)
    │
    ├── GERENTE_PROJETOS
    │   ├── /kabak-agent (E-commerce KabaK)
    │   ├── /validate (Nomenclatura)
    │   └── /pedro (Tráfego & Ads)
    │
    ├── GERENTE_PRODUTIVIDADE
    │   ├── /elena (TDAH & Energia)
    │   └── /coach (Accountability)
    │
    ├── GERENTE_FINANCAS
    │   └── /lucas (DeFi & Portfólio)
    │
    └── GUARDIAN (Loop Ralph)
        ├── vault-auditor
        ├── vault-organizer
        └── architect-linter
```

### 2.2 Sistema de Permissões (1-2-3)

| Nível | Nome | Ação | Agentes |
| ----- | ---- | ---- | ------- |
| 1 | READ | Só pesquisa/lê | mapa, alan, vault-auditor |
| 2 | PROPOSE | Sugere, você aprova | validate, névoa, gerentes, kabak-agent |
| 3 | EXECUTE | Faz direto (pós-aprovação) | vault-organizer, session-logger |

### 2.3 Loop Ralph (Verificação Automática)

```
1. Tarefa Iniciada
       ↓
2. Execução (Agente/Guardian)
       ↓
3. Verificação Automática
       ├── SUCESSO → Notifica + Próxima Tarefa
       └── FALHA → Diagnóstico + Retry
       ↓
4. Log em SESSION_LOG.md
```

---

## PARTE 3: AUTONOMIA DOS GERENTES

### 3.1 Princípio

Cada Gerente decide **autonomamente** dentro do seu domínio. Só escala para Névoa quando:

- Arquivo cruza domínios (ex: projeto + conhecimento)
- Não existe template adequado
- Conflito de nomenclatura
- Dúvida sobre destino

### 3.2 Templates por Gerente

#### Gerente Conhecimento

| Template | Uso | Localização |
| -------- | --- | ----------- |
| TEMPLATE_NOTA_CONHECIMENTO | Notas de estudo | `04_RECURSOS/TEMPLATES/` |
| TEMPLATE_RESUMO_CURSO | Resumos de aulas | `04_RECURSOS/TEMPLATES/` |
| TEMPLATE_REFERENCIA | Links e fontes | `04_RECURSOS/TEMPLATES/` |

**Destinos:**

- Cursos → `03_APRENDIZADO/Cursos_Ativos/`
- Referências → `01_CONHECIMENTO/[categoria]/`
- Pesquisas → `01_CONHECIMENTO/Pesquisas/`

#### Gerente Projetos

| Template | Uso | Localização |
| -------- | --- | ----------- |
| TEMPLATE_PROJETO | Novo projeto | `04_RECURSOS/TEMPLATES/` |
| TEMPLATE_STATUS | Status semanal | `04_RECURSOS/TEMPLATES/` |
| TEMPLATE_BRIEFING | Briefings | `04_RECURSOS/TEMPLATES/` |

**Destinos:**

- Projetos ativos → `02_PROJETOS/[NomeProjeto]/`
- Projetos concluídos → `99_ARQUIVO/Projetos_Concluidos/`

#### Gerente Produtividade

| Template | Uso | Localização |
| -------- | --- | ----------- |
| TEMPLATE_ROTINA | Rotinas diárias | `04_RECURSOS/TEMPLATES/` |
| TEMPLATE_CHECKLIST | Checklists | `04_RECURSOS/TEMPLATES/` |

**Destinos:**

- Rotinas → `05_PESSOAL/Rotinas/`
- Reflexões → `05_PESSOAL/Reflexoes/`

#### Gerente Finanças

| Template | Uso | Localização |
| -------- | --- | ----------- |
| TEMPLATE_ANALISE_DEFI | Análise protocolo | `04_RECURSOS/TEMPLATES/` |
| TEMPLATE_TRADE_LOG | Log de trades | `04_RECURSOS/TEMPLATES/` |

**Destinos:**

- DeFi → `02_PROJETOS/DeFi_Verso_2025/`
- Relatórios → `02_PROJETOS/DeFi_Verso_2025/relatorios/`

### 3.3 Regras de Classificação Automática

| Se arquivo contém... | Gerente | Destino |
| -------------------- | ------- | ------- |
| "aula", "curso", "módulo" | Conhecimento | `03_APRENDIZADO/` |
| "KabaK", "e-commerce", "produto" | Projetos | `02_PROJETOS/KabaK/` |
| "DeFi", "cripto", "trade" | Finanças | `02_PROJETOS/DeFi_Verso_2025/` |
| "rotina", "energia", "foco" | Produtividade | `05_PESSOAL/` |
| "template", "checklist", "prompt" | Conhecimento | `04_RECURSOS/` |
| "protocolo", "padrão", "guia" | Conhecimento | `00_SISTEMA/` |

### 3.4 Fluxo de Decisão

```
Arquivo Novo
     ↓
1. Identificar palavras-chave
     ↓
2. Determinar Gerente responsável
     ├── Único domínio → Gerente decide sozinho
     └── Múltiplos domínios → Escala para Névoa
     ↓
3. Aplicar template adequado
     ↓
4. Mover para destino correto
     ↓
5. Atualizar MOC relevante
     ↓
6. Guardian valida nomenclatura
```

---

## PARTE 4: A GRANDE TRIAGEM (Execução)

### 4.1 Fases

#### FASE 0: Preparação (AGORA)

- [x] Consolidar planos neste documento
- [ ] Verificar `_inbox/` atual
- [ ] Mapear arquivos na raiz do vault
- [ ] Definir "Zonas Seguras" (não tocar)

#### FASE 1: Inbox Zero (Semana 4 Jan)

**Escopo:** Processar `_inbox/` e arquivos soltos na raiz

**Executor:** Névoa + Guardian

**Ciclo:**

1. Listar arquivos em `_inbox/`
2. Para cada arquivo: classificar por Gerente
3. Gerente decide destino + template
4. Guardian move e renomeia
5. Loop Ralph verifica

#### FASE 2: Migração de Projetos (Fevereiro)

**Escopo:** Organizar `02_PROJETOS/`

**Executor:** Gerente Projetos

**Foco:**

- KabaK (P1)
- DeFi (P3)
- Cursos concluídos → Arquivo

#### FASE 3: Consolidação de Conhecimento (Fevereiro)

**Escopo:** Organizar `01_CONHECIMENTO/` e `03_APRENDIZADO/`

**Executor:** Gerente Conhecimento

**Foco:**

- Cursos ativos com estrutura padrão
- Notas soltas → Vincular a MOCs
- Duplicatas → Mesclar ou arquivar

#### FASE 4: Refinamento (Março)

**Escopo:** Auditoria final

**Executor:** Guardian

**Foco:**

- Nomenclatura 100% compliance
- Links quebrados corrigidos
- MOCs atualizados
- Zero arquivos órfãos

---

## PARTE 5: RECURSOS DISPONÍVEIS

### 5.1 Skills (238 awesome-skills)

**Localização:** `.agent/skills/skills/`

**TOP 16 Prioritárias:**

| Categoria | Skills |
| --------- | ------ |
| IA & Agentes | ai-agents-architect, prompt-engineer, autonomous-agents, agent-memory-systems, rag-engineer, langgraph |
| Marketing & CRO | copywriting, paid-ads, page-cro, seo-audit, email-sequence, analytics-tracking |
| Produtividade | brainstorming, concise-planning, writing-plans, executing-plans |

### 5.2 Agentes Instalados (53 em .claude/agents/)

**Categorias principais:**

| Categoria | Qtd | Para |
| --------- | --- | ---- |
| business-marketing | 7 | KabaK |
| obsidian-ops-team | 7 | Vault |
| blockchain-web3 | 3 | DeFi |
| mcp-dev-team | 4 | Sistema |
| deep-research-team | 4 | Pesquisa |

### 5.3 Comandos Nativos (19)

```bash
# Orquestração
/nevoa              # Master orquestrador

# Projetos
/kabak-agent        # Foco KabaK
/validate           # Validar nomenclatura

# Produtividade
/elena              # Modo TDAH
/coach              # Accountability

# Sincronização
/sync               # Claude ↔ Gemini
/mapa               # Índice do vault
```

---

## PARTE 6: MÉTRICAS DE SUCESSO

### KabaK (P1)

- [ ] ROAS > 4.0x
- [ ] Conversão > 2%
- [ ] CAC < R$ 50
- [ ] Lançamento até Abril/2026

### Sistema (P2)

- [ ] 0 erros de nomenclatura no vault
- [ ] Sincronização Bi-IA funcionando 100%
- [ ] Checkpoints semanais cumpridos
- [ ] Loop Ralph implementado e testado

### Produtividade (P4)

- [ ] 3 blocos deep work/dia
- [ ] Inbox zerada sexta 17h
- [ ] "Sapo" diário engolido

### Grande Triagem

- [ ] FASE 1 completa (Inbox Zero) - Jan
- [ ] FASE 2 completa (Projetos) - Fev
- [ ] FASE 3 completa (Conhecimento) - Fev
- [ ] FASE 4 completa (Refinamento) - Mar

---

## PARTE 7: PRÓXIMOS PASSOS IMEDIATOS

### Hoje (24/Jan)

1. [ ] Aprovar este plano
2. [ ] Listar conteúdo de `_inbox/`
3. [ ] Classificar primeiros 10 arquivos
4. [ ] Testar fluxo de autonomia do Gerente

### Esta Semana (Sem 4 Jan)

1. [ ] Completar FASE 1 (Inbox Zero)
2. [ ] Criar templates faltantes
3. [ ] Documentar regras de cada Gerente

### Próxima Sessão

```bash
/nevoa "Executar FASE 1 - Inbox Zero conforme PLANO_MASTER_2026.md"
```

---

## ARQUIVOS RELACIONADOS

| Arquivo | Propósito | Status |
| ------- | --------- | ------ |
| `PLANO_SEGUNDO_CEREBRO_2026.md` | Estratégico | Incorporado |
| `PLANO_Hierarquia_Agentes_Alan.md` | Arquitetura | Incorporado |
| `PLANO_ORGANIZACAO_TOTAL_2026.md` | Triagem | Incorporado |
| `.bi-ia/state.json` | Sync Bi-IA | Ativo |

---

## PRINCÍPIOS (Alan Nicolas)

1. **"Só automatize o que você fez 3x e odiou"**
2. **"Human-first design - nunca comece no código"**
3. **"Code above LLM - use código para tarefas determinísticas"**
4. **"Permissões 1-2-3 - coleira na IA"**
5. **"Não seja o imbecil que aperta sim"** (Loop Ralph)

---

**Próxima revisão:** Sexta-feira 17h
**Responsável:** Névoa + Gassen

---

*"Clareza antes de velocidade. Execução antes de perfeição."*
