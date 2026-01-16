---
criado: 2026-01-16T13:22:30-03:00
atualizado: 2026-01-16T13:22:30-03:00
---
# [DEPRECADO] 📁 ESTRUTURA PADRÃO DE PROJETOS

⚠️ **DEPRECADO** - Ver [[../../02_PROJETOS/_GUIDELINES.md]] (Seção "Estrutura Obrigatória")

**Razão:** Conteúdo consolidado no guideline de projetos (duplicação 60% eliminada)
**Data deprecação:** 16/Jan/2026
**Substituído por:** [[../../02_PROJETOS/_GUIDELINES.md]]

**Por que deprecado:**
- ESTRUTURA_PROJETOS.md e 02_PROJETOS/_GUIDELINES.md tinham 60% de conteúdo duplicado
- Manutenção de 2 arquivos causava divergências
- Single source of truth: _GUIDELINES.md é mais completo e específico da categoria

**Use o novo arquivo:**
→ [[../../02_PROJETOS/_GUIDELINES.md]]

---

**[CONTEÚDO ORIGINAL PRESERVADO ABAIXO PARA REFERÊNCIA HISTÓRICA]**

---

# 📁 ESTRUTURA PADRÃO DE PROJETOS

**Sistema de Organização de Projetos - Segundo Cérebro**

**Criado:** 17/Jan/2025
**Versão:** 1.0
**Propósito:** Garantir que TODOS os projetos sigam a mesma estrutura

---

## 🎯 PRINCÍPIO FUNDAMENTAL

> **"TODO projeto tem a MESMA estrutura.**
> **Quando você abre qualquer projeto, sabe exatamente onde encontrar o quê.**
> **ZERO exceções."**

---

## 📂 ESTRUTURA OBRIGATÓRIA

### Template Base

```
Nome_Projeto/
├── README.md                    # ✅ Visão geral obrigatória
├── STATUS_ATUAL.md             # ✅ Status sempre atualizado
│
├── planejamento/               # 📋 Planos, estratégias, roadmaps
│   ├── PLANO_Principal.md
│   ├── ROADMAP_2025.md
│   ├── PROXIMOS_PASSOS.md
│   └── ACAO_IMEDIATA.md
│
├── checkpoints/                # 💾 Snapshots de progresso
│   ├── CHECKPOINT_17JAN2025.md
│   ├── CHECKPOINT_Milestone.md
│   └── HISTORICO.md
│
├── docs/                       # 📚 Documentação técnica
│   ├── GUIA_Setup.md
│   ├── Arquitetura.md
│   ├── API_Reference.md
│   └── FAQ.md
│
├── recursos/                   # 🛠️ Templates, assets, materiais
│   ├── TEMPLATES/
│   ├── assets/
│   │   ├── images/
│   │   └── files/
│   └── REFERENCIAS.md
│
├── tarefas/                    # ✅ Task management
│   ├── BACKLOG.md
│   ├── TODO_Sprint_Atual.md
│   └── CONCLUIDAS.md
│
└── metricas/                   # 📊 KPIs, analytics
    ├── DASHBOARD.md
    └── RELATORIOS/
```

---

## 📄 ARQUIVOS OBRIGATÓRIOS

### 1. README.md

**Propósito:** Primeira coisa que alguém lê ao abrir o projeto

**Template:**

```markdown
# [Nome do Projeto]

**Status:** [Ativo/Planejamento/Concluído/Pausado]
**Início:** [Data]
**Prazo:** [Data ou "Ongoing"]
**Prioridade:** [Alta/Média/Baixa]

---

## 🎯 Objetivo

[Descrição concisa: o que é e por que existe]

## 📊 Progresso Atual

**Fase:** [Nome da fase atual]
**Progresso:** ███████░░░ 70%

## 🔗 Links Importantes

- [[STATUS_ATUAL.md]] - Status detalhado sempre atualizado
- [[planejamento/PLANO_Principal.md]] - Plano principal
- [[checkpoints/]] - Histórico de progresso

## 🛠️ Tecnologias/Ferramentas

- [Lista de tech stack se aplicável]

## 📁 Estrutura

- `planejamento/` - Planos e estratégias
- `checkpoints/` - Snapshots de progresso
- `docs/` - Documentação técnica
- `recursos/` - Assets e materiais
- `tarefas/` - Task management
- `metricas/` - KPIs e analytics

---

**Última atualização:** [Data]
```

### 2. STATUS_ATUAL.md

**Propósito:** Fonte única de verdade sobre estado do projeto

**Template:**

```markdown
# STATUS ATUAL - [Nome Projeto]

**Última atualização:** [Data e hora]
**Atualizado por:** [Seu nome ou "Auto"]

---

## ✅ ONDE ESTAMOS

**Fase Atual:** [Nome da fase]
**Iniciado em:** [Data]
**Progresso:** [Percentual ou descrição]

### Última Ação Realizada
[O que foi feito na última sessão]

### Estado Atual
[Descrição detalhada do estado atual]

---

## 🎯 PRÓXIMAS AÇÕES

### Imediato (Hoje/Esta Semana)
1. [ ] Ação 1 [Responsável]
2. [ ] Ação 2 [Responsável]
3. [ ] Ação 3 [Responsável]

### Curto Prazo (Este Mês)
- [ ] Meta 1
- [ ] Meta 2

### Pendências/Blockers
- [ ] Blocker 1 [Descrição]
- [ ] Pendência 1 [O que falta]

---

## 📋 DECISÕES RECENTES

### [Data] - Decisão X
**Contexto:** [Por que precisava decidir]
**Decisão:** [O que foi decidido]
**Motivo:** [Justificativa]

---

## 📊 MÉTRICAS CHAVE

**[Métrica 1]:** [Valor atual] (meta: [Valor alvo])
**[Métrica 2]:** [Valor atual] (meta: [Valor alvo])

---

## 🔗 ARQUIVOS RELACIONADOS

### Documentos Principais
- [[README.md]] - Visão geral
- [[planejamento/PLANO_Principal.md]] - Plano completo
- [[checkpoints/CHECKPOINT_Ultimo.md]] - Último checkpoint

### Recursos
- [[recursos/REFERENCIAS.md]] - Referências externas
- [[docs/GUIA_Setup.md]] - Como configurar

---

## 🚨 NÃO MUDAR (Protegido)

[Lista de decisões/estruturas que NÃO devem mudar sem discussão explícita]

- Estrutura de pastas definida
- [Outro item protegido]

---

**Próxima revisão:** [Data planejada]
```

**Regra de ouro:** Atualizar STATUS_ATUAL.md SEMPRE após mudança significativa

---

## 📋 PASTAS OBRIGATÓRIAS

### planejamento/

**Propósito:** Onde vivem todos os documentos de planejamento

**Arquivos comuns:**
- `PLANO_Principal.md` - Plano mestre do projeto
- `ROADMAP_[Período].md` - Roadmap temporal
- `PROXIMOS_PASSOS.md` - Lista de next steps
- `ACAO_IMEDIATA.md` - O que fazer AGORA
- `PAUTA_[Reuniao].md` - Pautas de reuniões

**Regra:** Nenhum plano na raiz. Tudo em `planejamento/`

### checkpoints/

**Propósito:** Snapshots de progresso em momentos chave

**Arquivos comuns:**
- `CHECKPOINT_[Data].md` - Checkpoint por data
- `CHECKPOINT_[Milestone].md` - Checkpoint por marco
- `HISTORICO.md` - Linha do tempo de todos checkpoints

**Quando criar checkpoint:**
- Fim de sprint/fase
- Marco importante atingido
- Antes de mudança grande
- Periodicamente (semanal/mensal)

**Template checkpoint:**
```markdown
# CHECKPOINT - [Nome/Data]

**Data:** [Data]
**Fase:** [Nome da fase]
**Progresso:** [Percentual]

## O QUE FOI FEITO

### Realizações
- [x] Item 1
- [x] Item 2

### Aprendizados
- [Aprendizado 1]
- [Aprendizado 2]

## ESTADO ATUAL

### O que está funcionando
- [Item 1]

### O que precisa melhorar
- [Item 1]

## PRÓXIMOS PASSOS

1. [ ] Próxima ação 1
2. [ ] Próxima ação 2

## LINKS
- [[STATUS_ATUAL.md]]
- [[checkpoints/CHECKPOINT_Anterior.md]]
```

### docs/

**Propósito:** Documentação técnica e guias

**Arquivos comuns:**
- `GUIA_Setup.md` - Como configurar/instalar
- `GUIA_Uso.md` - Como usar
- `Arquitetura.md` - Arquitetura técnica
- `API_Reference.md` - Referência de API
- `FAQ.md` - Perguntas frequentes
- `Troubleshooting.md` - Solução de problemas

**Diferença docs/ vs recursos/:**
- `docs/` = Documentação do PROJETO
- `recursos/` = Materiais PARA o projeto (templates, assets)

### recursos/

**Propósito:** Assets, templates, materiais de apoio

**Estrutura interna:**
```
recursos/
├── TEMPLATES/           # Templates reutilizáveis
│   ├── template_email.md
│   └── template_post.md
├── assets/              # Assets do projeto
│   ├── images/
│   │   ├── logo.png
│   │   └── screenshots/
│   └── files/
│       ├── docs.pdf
│       └── planilhas/
└── REFERENCIAS.md       # Links externos, fontes
```

### tarefas/

**Propósito:** Gestão de tarefas estilo kanban/GTD

**Arquivos:**
- `BACKLOG.md` - Todas as tarefas futuras
- `TODO_Sprint_Atual.md` - Tarefas do sprint/semana atual
- `EM_ANDAMENTO.md` - O que está sendo feito agora
- `CONCLUIDAS.md` - Histórico de tarefas concluídas

**Template TODO:**
```markdown
# TODO - Sprint [Nome/Data]

## 🔴 Alta Prioridade
- [ ] Tarefa urgente 1 [Est: 2h] [Prazo: 18JAN]
- [ ] Tarefa urgente 2

## 🟡 Média Prioridade
- [ ] Tarefa importante 1
- [ ] Tarefa importante 2

## 🟢 Baixa Prioridade
- [ ] Tarefa nice-to-have 1

## 🎯 Concluídas Esta Sprint
- [x] Tarefa concluída 1
- [x] Tarefa concluída 2
```

### metricas/

**Propósito:** Acompanhamento de KPIs e resultados

**Arquivos:**
- `DASHBOARD.md` - Dashboard visual de métricas
- `RELATORIOS/` - Relatórios periódicos
  - `RELATORIO_Semanal_[Data].md`
  - `RELATORIO_Mensal_[Mes].md`

**Template dashboard:**
```markdown
# DASHBOARD - [Projeto]

**Última atualização:** [Data e hora]

## 📊 KPIs Principais

| Métrica | Atual | Meta | Status |
|---------|-------|------|--------|
| [Métrica 1] | [Valor] | [Meta] | 🟢/🟡/🔴 |
| [Métrica 2] | [Valor] | [Meta] | 🟢/🟡/🔴 |

## 📈 Tendências

**[Métrica 1]:**
- Semana passada: [Valor]
- Esta semana: [Valor]
- Mudança: ↑ +10%

## 🎯 Metas e Progresso

### Meta 1: [Nome]
Progresso: ████░░░░░░ 40%
Prazo: [Data]
Status: 🟢 No prazo

---

**Próxima atualização:** [Data]
```

---

## 🎨 VARIAÇÕES POR TIPO DE PROJETO

### Projeto de Software

**Adicionar:**
```
├── src/              # Código fonte
├── tests/            # Testes
├── docs/
│   ├── API_Reference.md
│   ├── Arquitetura.md
│   └── GUIA_Contribuicao.md
└── .github/          # GitHub Actions (se aplicável)
```

### Projeto de Conteúdo

**Adicionar:**
```
├── conteudo/
│   ├── drafts/       # Rascunhos
│   ├── published/    # Publicados
│   └── CALENDARIO_Editorial.md
└── recursos/
    └── GUIAS_Estilo.md
```

### Projeto de Negócio

**Adicionar:**
```
├── financeiro/
│   ├── ORCAMENTO.md
│   └── PROJECOES.md
├── equipe/
│   ├── FUNCOES.md
│   └── CONTATOS.md
└── marketing/
    ├── ESTRATEGIA.md
    └── CAMPANHAS/
```

---

## ✅ REGRAS DE ORGANIZAÇÃO

### 1. Raiz do Projeto

**✅ PERMITIDO na raiz:**
- `README.md`
- `STATUS_ATUAL.md`
- Arquivos de configuração (`.gitignore`, `package.json`, etc)
- `MOC_[Projeto].md` (se projeto grande)

**❌ PROIBIDO na raiz:**
- Checkpoints → vão em `checkpoints/`
- Planos → vão em `planejamento/`
- Tarefas → vão em `tarefas/`
- Docs → vão em `docs/`
- Arquivos temporários
- Qualquer `.md` além dos 3-4 permitidos

### 2. Atualização de STATUS_ATUAL.md

**SEMPRE atualizar após:**
- Criar checkpoint
- Completar tarefa importante
- Mudança de fase
- Decisão importante
- Blocker identificado
- Meta atingida

**Como atualizar:**
1. Abrir `STATUS_ATUAL.md`
2. Atualizar data no topo
3. Revisar "Onde Estamos"
4. Atualizar "Próximas Ações"
5. Adicionar decisões se houver
6. Salvar

### 3. Criação de Checkpoints

**Frequência mínima:**
- Projetos ativos: semanal
- Projetos médios: quinzenal
- Projetos lentos: mensal

**Antes de criar checkpoint:**
- [ ] Atualizar STATUS_ATUAL.md
- [ ] Revisar tarefas concluídas
- [ ] Documentar aprendizados
- [ ] Definir próximos passos

### 4. Limpeza Periódica

**Mensal:**
- [ ] Arquivar checkpoints antigos (>3 meses)
- [ ] Limpar tarefas concluídas (mover para HISTORICO)
- [ ] Revisar e limpar recursos não usados
- [ ] Atualizar README se estrutura mudou

**Trimestral:**
- [ ] Revisar estrutura completa
- [ ] Consolidar docs fragmentados
- [ ] Criar relatório de período
- [ ] Avaliar se projeto continua ativo

---

## 🚨 ANTI-PADRÕES (EVITAR)

### ❌ Erro 1: Checkpoints na Raiz

```
❌ Errado:
Projeto/
├── README.md
├── CHECKPOINT_17JAN2025.md     ← NA RAIZ!
└── checkpoints/

✅ Correto:
Projeto/
├── README.md
└── checkpoints/
    └── CHECKPOINT_17JAN2025.md
```

### ❌ Erro 2: STATUS_ATUAL.md Desatualizado

**Problema:** STATUS diz uma coisa, realidade é outra

**Solução:** Atualizar IMEDIATAMENTE após mudança

### ❌ Erro 3: Múltiplos READMEs

```
❌ Errado:
├── README.md
├── LEIAME.md
└── INFO.md

✅ Correto:
├── README.md              ← Um só
└── docs/
    ├── GUIA_Setup.md
    └── Mais_Informacoes.md
```

### ❌ Erro 4: Pastas Extras Desnecessárias

**Problema:** Criar pasta para 1-2 arquivos

**Evitar:**
```
❌ Errado:
├── analises/
│   └── analise_unica.md    ← Só 1 arquivo
├── ideias/
│   └── ideia_unica.md      ← Só 1 arquivo
```

**Melhor:** Se <3 arquivos, colocar em pasta existente (docs/ ou recursos/)

### ❌ Erro 5: Nomes Inconsistentes

```
❌ Errado:
├── planos/                 ← Minúsculo
├── Checkpoints/            ← Capital
└── DOCS/                   ← Maiúsculo

✅ Correto:
├── planejamento/           ← Consistente
├── checkpoints/            ← Consistente
└── docs/                   ← Consistente
```

---

## 📖 EXEMPLOS COMPLETOS

### Projeto Pequeno (Blog Post)

```
02_PROJETOS/Artigo_IA_Prompts/
├── README.md
├── STATUS_ATUAL.md
├── planejamento/
│   └── PLANO_Artigo.md
├── checkpoints/
│   ├── CHECKPOINT_17JAN2025_Outline.md
│   └── CHECKPOINT_20JAN2025_Draft.md
├── recursos/
│   ├── referencias.md
│   └── assets/
│       └── imagens/
└── drafts/
    ├── draft_v1.md
    └── draft_final.md
```

### Projeto Médio (Website)

```
02_PROJETOS/Website_Portfolio/
├── README.md
├── STATUS_ATUAL.md
├── planejamento/
│   ├── PLANO_Principal.md
│   ├── ROADMAP_2025_Q1.md
│   └── PROXIMOS_PASSOS.md
├── checkpoints/
│   ├── CHECKPOINT_17JAN2025_Inicio.md
│   ├── CHECKPOINT_01FEV2025_Design.md
│   └── CHECKPOINT_15FEV2025_Lancamento.md
├── docs/
│   ├── GUIA_Setup.md
│   ├── Arquitetura.md
│   └── Deploy.md
├── recursos/
│   ├── TEMPLATES/
│   │   └── page_template.md
│   ├── assets/
│   │   ├── design/
│   │   └── content/
│   └── REFERENCIAS.md
├── tarefas/
│   ├── BACKLOG.md
│   ├── TODO_Sprint_01.md
│   └── CONCLUIDAS.md
└── metricas/
    └── DASHBOARD.md
```

### Projeto Grande (Sistema Complexo)

```
02_PROJETOS/Sistema_IA_Completo/
├── README.md
├── STATUS_ATUAL.md
├── MOC_Sistema_IA.md              ← MOC do projeto
├── planejamento/
│   ├── PLANO_Master_v2.0.md
│   ├── ROADMAP_2025.md
│   ├── ARQUITETURA_Decisoes.md
│   └── sprints/
│       ├── Sprint_01_Plan.md
│       └── Sprint_02_Plan.md
├── checkpoints/
│   ├── CHECKPOINT_17JAN2025_Kick-off.md
│   ├── CHECKPOINT_Fase1_Complete.md
│   └── HISTORICO.md
├── docs/
│   ├── GUIA_Setup_Completo.md
│   ├── Arquitetura_Sistema.md
│   ├── API_Reference.md
│   ├── Database_Schema.md
│   └── Troubleshooting.md
├── recursos/
│   ├── TEMPLATES/
│   ├── REFERENCIAS.md
│   ├── assets/
│   └── specs/
│       ├── Feature_Specs/
│       └── Tech_Specs/
├── tarefas/
│   ├── BACKLOG_Master.md
│   ├── TODO_Sprint_Atual.md
│   ├── EM_ANDAMENTO.md
│   └── CONCLUIDAS_Por_Fase.md
├── metricas/
│   ├── DASHBOARD.md
│   ├── KPIs_Por_Fase.md
│   └── RELATORIOS/
│       ├── RELATORIO_Semanal_17JAN2025.md
│       └── RELATORIO_Mensal_JAN2025.md
└── equipe/                        ← Se houver equipe
    ├── FUNCOES.md
    └── CONTATOS.md
```

---

## 🎯 CHECKLIST DE VALIDAÇÃO

### Ao Criar Novo Projeto

- [ ] Estrutura base criada (6 pastas obrigatórias)
- [ ] README.md criado com template completo
- [ ] STATUS_ATUAL.md criado e atualizado
- [ ] PLANO_Principal.md existe em planejamento/
- [ ] Primeiro checkpoint criado
- [ ] Projeto adicionado a [[_MOC_Projetos.md]]

### Manutenção Semanal

- [ ] STATUS_ATUAL.md atualizado
- [ ] Checkpoint semanal criado
- [ ] Tarefas concluídas movidas para CONCLUIDAS.md
- [ ] Métricas atualizadas (se aplicável)

### Manutenção Mensal

- [ ] Checkpoints antigos arquivados
- [ ] README atualizado se necessário
- [ ] Limpeza de arquivos temporários
- [ ] Relatório mensal criado (se aplicável)

### Antes de Fechar Projeto

- [ ] Checkpoint final completo
- [ ] STATUS_ATUAL.md marcado como "Concluído"
- [ ] README com resultados finais
- [ ] Aprendizados documentados
- [ ] Recursos importantes arquivados
- [ ] MOC de projetos atualizado

---

## 📚 TEMPLATES DISPONÍVEIS

**Localização:** `04_RECURSOS/TEMPLATES/`

- `TEMPLATE_Projeto_Padrao.md` - Estrutura completa
- `TEMPLATE_README_Projeto.md` - README padrão
- `TEMPLATE_STATUS_ATUAL.md` - STATUS padrão
- `TEMPLATE_Checkpoint.md` - Checkpoint padrão
- `TEMPLATE_Plano.md` - Plano padrão
- `TEMPLATE_Dashboard_Metricas.md` - Dashboard padrão

**Uso:**
```bash
# Via Claude Code
/work "Create new project [Nome] using TEMPLATE_Projeto_Padrao"
```

---

## 🔗 LINKS RELACIONADOS

- [[NOMENCLATURA.md]] - Padrões de nomenclatura
- [[00_SISTEMA/MOCs/_MOC_Projetos.md]] - Índice de todos projetos
- [[04_RECURSOS/TEMPLATES/]] - Templates disponíveis
- [[CLAUDE.md]] - Guidance geral para Claude

---

**Criado:** 17/Jan/2025
**Versão:** 1.0
**Autor:** Claude Sonnet 4.5
**Status:** ✅ Ativo e obrigatório

**ESTRUTURA É TUDO! 📁✅**
