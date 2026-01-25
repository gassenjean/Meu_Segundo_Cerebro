---
criado: 2026-01-16T12:42:09-03:00
atualizado: 2026-01-16T12:42:09-03:00
---
# 🚀 GUIDELINES: PROJETOS

**Diretrizes Específicas - Gestão de Projetos Ativos**

**Categoria:** 02_PROJETOS
**Versão:** 2.0 (Expandida)
**Criado:** 16/Jan/2026
**Atualizado:** 16/Jan/2026

---

## 🎯 O QUE PERTENCE AQUI

### Sim, Vai em PROJETOS

- ✅ Projetos ativos com múltiplas ações/entregas
- ✅ Iniciativas com começo, meio e fim definidos
- ✅ Empreendimentos com planejamento estruturado
- ✅ Projetos pessoais de longo prazo
- ✅ Trabalhos freelance/consultoria
- ✅ Projetos de software/apps
- ✅ Projetos de conteúdo (blog, YouTube, curso próprio)
- ✅ Projetos de negócio (MVP, lançamento, expansão)
- ✅ Projetos de pesquisa/experimentação com deliverables

### Não, Vai em Outro Lugar

- ❌ Cursos/aprendizado → `03_APRENDIZADO/`
- ❌ Áreas de responsabilidade contínua (sem fim claro) → Considere se é projeto ou área
- ❌ Tarefas únicas/simples → Lista de tarefas pessoal ou `05_PESSOAL/Tasks/`
- ❌ Ideias não iniciadas → `05_PESSOAL/Ideas/`
- ❌ Conhecimento consolidado de projetos passados → `01_CONHECIMENTO/`
- ❌ Projetos arquivados (>6 meses inativos) → `00_SISTEMA/ARQUIVO/`

**Princípio:** Projeto = Tem **objetivo claro**, **prazo** (mesmo que flexível), **múltiplas etapas** e **critério de conclusão**.

---

## 📛 NOMENCLATURA ESPECÍFICA

### Padrão de Nome de Projeto

```
[Nome_Projeto]

Regras:
- CamelCase obrigatório
- Sem prefixos especiais
- Descritivo e único
- Máximo 30 caracteres

Exemplos corretos:
✅ KabaK
✅ Blog_Pessoal_2026
✅ App_Gestao_TDAH
✅ Consultoria_Cliente_X
✅ MVP_Plataforma_Cursos
```

### Nomenclatura de Arquivos Internos

#### README.md e STATUS_ATUAL.md
```
✅ README.md (sempre na raiz do projeto)
✅ STATUS_ATUAL.md (sempre na raiz do projeto)
```

#### Planejamento
```
planejamento/
├── PLANO_ESTRATEGICO.md          # Visão geral e estratégia
├── PLANO_[Fase].md                # Ex: PLANO_MVP.md, PLANO_Lancamento.md
├── ROADMAP.md                     # Timeline visual
└── DECISOES.md                    # Log de decisões importantes

Padrão: PLANO_ ou ROADMAP_ ou DECISOES_
```

#### Checkpoints
```
checkpoints/
├── CHECKPOINT_16JAN2026_[Descricao].md
├── CHECKPOINT_23JAN2026_[Descricao].md

Padrão: CHECKPOINT_DDMMMYYYY_Descricao.md
Data: SEMPRE formato DDMMMYYYY (17JAN2026)
```

#### Documentação
```
docs/
├── briefing/
│   └── BRIEFING_[Nome].md
├── especificacoes/
│   └── SPEC_[Funcionalidade].md
├── arquitetura/
│   └── ARCH_[Sistema].md
└── processos/
    └── PROCESSO_[Nome].md

Padrões: BRIEFING_, SPEC_, ARCH_, PROCESSO_
```

#### Tarefas
```
tarefas/
├── BACKLOG.md                     # Tarefas futuras
├── SPRINT_ATUAL.md                # Sprint/semana ativa
├── SPRINT_[Data].md               # Sprints passados
└── TAREFAS_CONCLUIDAS.md          # Histórico

Padrão: BACKLOG, SPRINT_, TAREFAS_
```

#### Métricas
```
metricas/
├── METRICAS_[Periodo].md          # Ex: METRICAS_JAN2026.md
├── RELATORIO_[Tipo].md            # Ex: RELATORIO_Financeiro.md
└── DASHBOARD.md                   # Visão consolidada

Padrão: METRICAS_, RELATORIO_, DASHBOARD
```

---

## 🏗️ ESTRUTURA OBRIGATÓRIA

### Template Base (NUNCA DESVIAR)

```
Nome_Projeto/
├── README.md                    # ✅ OBRIGATÓRIO - Visão geral do projeto
├── STATUS_ATUAL.md             # ✅ OBRIGATÓRIO - Status vivo (atualizar sempre)
│
├── planejamento/               # ✅ OBRIGATÓRIO - Planos e estratégias
│   ├── PLANO_ESTRATEGICO.md
│   ├── ROADMAP.md
│   └── DECISOES.md
│
├── checkpoints/                # ✅ OBRIGATÓRIO - Histórico de progresso
│   ├── CHECKPOINT_[Data]_Inicio.md
│   └── CHECKPOINT_[Data]_[Fase].md
│
├── docs/                       # ✅ OBRIGATÓRIO - Documentação técnica
│   ├── briefing/
│   ├── especificacoes/
│   └── processos/
│
├── recursos/                   # ✅ OBRIGATÓRIO - Assets e materiais
│   ├── imagens/
│   ├── videos/
│   └── templates/
│
├── tarefas/                    # ✅ OBRIGATÓRIO - Gestão de tarefas
│   ├── BACKLOG.md
│   └── SPRINT_ATUAL.md
│
└── metricas/                   # ✅ OBRIGATÓRIO - KPIs e resultados
    └── DASHBOARD.md
```

**Regra de Ouro:** Se criou o projeto, TODAS as 7 pastas obrigatórias devem existir. Mesmo que vazias inicialmente.

---

## 📝 TEMPLATES COMPLETOS

### Template: README.md

```markdown
# [Nome do Projeto]

**Status:** [🔵 Planejamento | 🟢 Ativo | 🟡 Pausado | ✅ Concluído | 📦 Arquivado]
**Início:** [DD/MMM/YYYY]
**Prazo:** [DD/MMM/YYYY ou "Contínuo"]
**Proprietário:** Gassen Jean Bou Karim

---

## 🎯 Objetivo

[Descrição clara do que este projeto pretende alcançar em 2-4 parágrafos]

### Problema que Resolve

[Qual problema/necessidade este projeto atende?]

### Resultado Esperado

[O que será considerado sucesso? Como saber que terminou?]

---

## 📊 Visão Geral

### Escopo

**Incluído:**
- Item 1
- Item 2
- Item 3

**Excluído (Fora do Escopo):**
- Item 1
- Item 2

### Stakeholders

- **Responsável:** [Nome]
- **Cliente:** [Nome/Empresa se aplicável]
- **Equipe:** [Colaboradores se houver]

---

## 🗓️ Timeline

### Fases Principais

```
Fase 1: [Nome] (DD/MMM - DD/MMM/YYYY)
├── Entregas: [O que será entregue]
└── Status: [Não iniciado/Em andamento/Concluído]

Fase 2: [Nome] (DD/MMM - DD/MMM/YYYY)
├── Entregas: [O que será entregue]
└── Status: [Não iniciado/Em andamento/Concluído]
```

---

## 📁 Estrutura de Pastas

```
[mostrar estrutura do projeto]
```

---

## 🔗 Links Importantes

- [[STATUS_ATUAL.md]] - Status do projeto em tempo real
- [[planejamento/PLANO_ESTRATEGICO.md]] - Plano estratégico completo
- [[tarefas/BACKLOG.md]] - Backlog de tarefas
- [[metricas/DASHBOARD.md]] - Métricas e KPIs

**Última atualização:** [DD/MMM/YYYY]
```

### Template: STATUS_ATUAL.md

```markdown
# STATUS ATUAL - [Nome do Projeto]

**Última atualização:** [DD/MMM/YYYY HH:MM]
**Status:** [🔵 Planejamento | 🟢 Ativo | 🟡 Pausado | ✅ Concluído]

---

## 📍 ONDE ESTAMOS

### Fase Atual

**[Nome da Fase]** (DD/MMM - DD/MMM/YYYY)

**Progresso:** [XX%] ████████░░

**Tempo decorrido:** [X semanas de Y]
**Tempo restante estimado:** [X semanas]

---

## ✅ ÚLTIMAS CONQUISTAS (Última Semana)

- [DD/MMM] - Conquista 1
- [DD/MMM] - Conquista 2
- [DD/MMM] - Conquista 3

---

## 🎯 PRÓXIMOS PASSOS (Próxima Semana)

- [ ] Ação 1 (prioridade: alta)
- [ ] Ação 2 (prioridade: média)
- [ ] Ação 3 (prioridade: baixa)

---

## 🚧 BLOQUEIOS ATIVOS

**Bloqueio 1:**
- Descrição: [O que está bloqueando]
- Impacto: [Alto/Médio/Baixo]
- Ação necessária: [O que fazer para desbloquear]
- Responsável: [Quem vai resolver]

---

## 📊 MÉTRICAS RÁPIDAS

| Métrica | Atual | Meta | Status |
|---------|-------|------|--------|
| [KPI 1] | X     | Y    | 🟢/🟡/🔴 |
| [KPI 2] | X     | Y    | 🟢/🟡/🔴 |
| [KPI 3] | X     | Y    | 🟢/🟡/🔴 |

---

## 💡 INSIGHTS DA SEMANA

[Aprendizados, descobertas, mudanças de direção importantes]

---

## 🔗 Referências Rápidas

- [[planejamento/PLANO_ESTRATEGICO.md]]
- [[tarefas/SPRINT_ATUAL.md]]
- [[checkpoints/CHECKPOINT_[Data].md]] (último checkpoint)

---

**Próxima atualização prevista:** [DD/MMM/YYYY]
```

### Template: CHECKPOINT

```markdown
# CHECKPOINT - [DD/MMM/YYYY] - [Descrição Curta]

**Data:** [DD/MMM/YYYY] ([HH:MM-HH:MM])
**Fase:** [Nome da Fase]
**Status:** [Emoji + Texto]

---

## 📊 ONDE ESTAMOS

### Progresso Geral

```
Progresso: XX%
Tempo decorrido: X semanas de Y
Fase atual: [Nome]
```

---

## ✅ O QUE FOI FEITO (COMPLETO)

### [Categoria 1]

**Descrição do trabalho:**
- Item específico 1
- Item específico 2

**Entregas:**
- Arquivo/Feature X criado
- Processo Y implementado

### [Categoria 2]

[mesmo padrão]

---

## 📝 ARQUIVOS CRIADOS/MODIFICADOS

### NOVOS

```
pasta/arquivo1.md         XXkb - Descrição
pasta/arquivo2.md         XXkb - Descrição
```

### MODIFICADOS

```
arquivo.md                Mudança: [descrição]
```

---

## 🎯 DECISÕES IMPORTANTES

**Decisão 1: [Título]**
- Contexto: [Por que a decisão foi necessária]
- Opções consideradas: A, B, C
- Decisão: Escolhemos A
- Razão: [Por que A é melhor que B e C]

---

## 🚨 PROBLEMAS ENCONTRADOS

**Problema 1:**
- Descrição: [O que aconteceu]
- Impacto: [Alto/Médio/Baixo]
- Solução aplicada: [Como resolvemos]
- Lição aprendida: [O que aprendemos]

---

## 🎓 APRENDIZADOS

### Lição 1: [Título]

```
❌ FIZEMOS: [O que fizemos de errado]
✅ DEVERÍAMOS: [O que deveríamos ter feito]

RAZÃO: [Por que isso importa]
```

---

## 📋 PARA PRÓXIMA SESSÃO/FASE

### ✅ O QUE JÁ ESTÁ PRONTO (NÃO REFAZER)

```
✅ Item 1 - COMPLETO
✅ Item 2 - COMPLETO
```

### 🔍 O QUE AVALIAR

**Opções em aberto:**

**Opção A:** [Descrição]
- Pros: [Vantagens]
- Cons: [Desvantagens]

**RECOMENDAÇÃO:** [Qual opção e por quê]

### 🎯 PRÓXIMOS PASSOS (SUGERIDOS)

1. Passo 1
2. Passo 2
3. Passo 3

---

## 📊 ESTATÍSTICAS

```
Duração: Xh
Tarefas completadas: X
Arquivos criados: X
Decisões importantes: X
Bloqueios resolvidos: X
```

---

**Checkpoint criado:** [DD/MMM/YYYY HH:MM]
**Status:** ✅ Documentado completamente
**Próxima ação:** [Resumo em 1 linha]
```

---

## 🔄 WORKFLOW DE CRIAÇÃO DE PROJETO

### Do Conceito à Execução

```
1. CONCEPÇÃO
   ↓
   Ideia surge em 05_PESSOAL/Ideas/ ou _inbox/

2. VALIDAÇÃO
   ↓
   Responder:
   - Tem objetivo claro? (Sim/Não)
   - Tem prazo ou critério de conclusão? (Sim/Não)
   - Requer múltiplas ações/etapas? (Sim/Não)
   - Vale a pena estruturar? (Sim/Não)

   Se 4x Sim → É PROJETO
   Se não → Pode ser tarefa simples ou área de responsabilidade

3. NOMEAÇÃO
   ↓
   Escolher nome CamelCase único
   Exemplo: KabaK, App_TDAH_Manager

4. ESTRUTURAÇÃO
   ↓
   Criar estrutura base obrigatória:
   - 7 pastas obrigatórias
   - README.md (template completo)
   - STATUS_ATUAL.md (template completo)

5. PLANEJAMENTO INICIAL
   ↓
   Criar em planejamento/:
   - PLANO_ESTRATEGICO.md
   - ROADMAP.md (opcional inicial)

6. CHECKPOINT INICIAL
   ↓
   Criar: checkpoints/CHECKPOINT_DDMMMYYYY_Inicio.md

7. INDEXAÇÃO
   ↓
   Atualizar _MOC_Projetos.md com novo projeto

8. ATIVAÇÃO
   ↓
   Marcar STATUS_ATUAL.md como 🟢 Ativo
   Iniciar trabalho
```

### Checklist de Validação Inicial

Antes de marcar projeto como "Ativo":

- [ ] Nome segue padrão CamelCase
- [ ] Estrutura de 7 pastas criada
- [ ] README.md completo (template preenchido)
- [ ] STATUS_ATUAL.md criado
- [ ] PLANO_ESTRATEGICO.md existe
- [ ] CHECKPOINT inicial criado
- [ ] Adicionado ao _MOC_Projetos.md
- [ ] Objetivo claro definido
- [ ] Critério de conclusão estabelecido

---

## 📋 CICLO DE VIDA DO PROJETO

### Estágios e Transições

```
1. 🔵 PLANEJAMENTO
   ├── Foco: Definir escopo, plano, recursos
   ├── Duração: 1-2 semanas típico
   └── Próximo: 🟢 Ativo (quando plano aprovado)

2. 🟢 ATIVO
   ├── Foco: Execução, entregas, iteração
   ├── Duração: Variável (semanas a meses)
   ├── Checkpoints: Frequentes (semanal/quinzenal)
   └── Próximo: ✅ Concluído OU 🟡 Pausado

3. 🟡 PAUSADO
   ├── Foco: Preservar contexto para retomada
   ├── Antes de pausar: CHECKPOINT obrigatório
   ├── Atualizar: STATUS_ATUAL.md com razão da pausa
   └── Próximo: 🟢 Ativo (retomada) OU 📦 Arquivado

4. ✅ CONCLUÍDO
   ├── Foco: Documentar resultados, aprendizados
   ├── Criar: CHECKPOINT final obrigatório
   ├── Extrair: Conhecimento para 01_CONHECIMENTO/
   └── Próximo: 📦 Arquivado (após 3-6 meses)

5. 📦 ARQUIVADO
   ├── Quando: Projeto concluído há >6 meses E não consultado
   ├── Ação: Mover para 00_SISTEMA/ARQUIVO/
   └── Manter: Link no _MOC_Projetos.md (seção Arquivados)
```

### Transições Críticas

**Ativo → Pausado:**
1. Criar CHECKPOINT descrevendo onde parou
2. Atualizar STATUS_ATUAL.md (razão, previsão retomada)
3. Documentar bloqueios/dependências
4. Atualizar _MOC_Projetos.md (emoji 🟡)

**Pausado → Ativo:**
1. Ler último CHECKPOINT
2. Ler STATUS_ATUAL.md
3. Atualizar STATUS_ATUAL.md (novo foco)
4. Criar checkpoint de retomada (opcional)
5. Atualizar _MOC_Projetos.md (emoji 🟢)

**Ativo → Concluído:**
1. Verificar critério de conclusão atingido
2. Criar CHECKPOINT final (completo)
3. Atualizar README.md (adicionar resultados finais)
4. Extrair conhecimento → 01_CONHECIMENTO/
5. Celebrar! 🎉
6. Atualizar _MOC_Projetos.md (emoji ✅)

---

## 📊 CHECKPOINTS: ESTRATÉGIA

### Quando Criar Checkpoint

**Obrigatório:**
- ✅ Início do projeto (CHECKPOINT_[Data]_Inicio.md)
- ✅ Fim de cada fase/sprint importante
- ✅ Antes de pausa longa (>1 semana)
- ✅ Após decisão importante/mudança de direção
- ✅ Fim do projeto (CHECKPOINT_[Data]_Final.md)

**Recomendado:**
- Após sessão de trabalho produtiva (>2h)
- Quando atingir milestone importante
- Ao final de semana/sprint
- Quando contexto está muito alto (>40% tokens) e precisa parar

**Não criar quando:**
- Mudanças triviais (typo, pequeno ajuste)
- Trabalho incremental sem decisões
- <30min de trabalho

### Estrutura de Checkpoint

**Use template fornecido acima.**

**Seções obrigatórias:**
- Onde estamos (progresso, fase)
- O que foi feito (completo)
- Arquivos criados/modificados
- Para próxima sessão (o que está pronto, próximos passos)

**Seções opcionais (conforme necessário):**
- Decisões importantes
- Problemas encontrados
- Aprendizados
- Estatísticas

---

## ⚠️ ANTI-PADRÕES (EVITAR)

### ❌ Erro 1: Arquivo Solto na Raiz

```
❌ Errado:
Nome_Projeto/
├── README.md
├── STATUS_ATUAL.md
├── checkpoint_inicial.md        ← ERRADO (na raiz)
├── plano.md                     ← ERRADO (na raiz)
└── tarefa1.md                   ← ERRADO (na raiz)

✅ Correto:
Nome_Projeto/
├── README.md
├── STATUS_ATUAL.md
├── checkpoints/
│   └── CHECKPOINT_16JAN2026_Inicio.md
├── planejamento/
│   └── PLANO_ESTRATEGICO.md
└── tarefas/
    └── BACKLOG.md
```

**Regra:** Raiz = APENAS README.md + STATUS_ATUAL.md + pastas obrigatórias.

### ❌ Erro 2: Projeto Sem Estrutura

```
❌ Errado:
Nome_Projeto/
└── README.md                    ← Só isso?

✅ Correto:
Nome_Projeto/
├── README.md
├── STATUS_ATUAL.md
├── planejamento/
├── checkpoints/
├── docs/
├── recursos/
├── tarefas/
└── metricas/
```

**Regra:** Criar projeto = criar TODA estrutura obrigatória (mesmo que pastas vazias).

### ❌ Erro 3: STATUS_ATUAL.md Desatualizado

```
❌ Errado:
STATUS_ATUAL.md mostra: "Última atualização: 01/Jan/2026"
Hoje: 16/Jan/2026
Projeto mudou muito, mas STATUS não foi atualizado

✅ Correto:
Atualizar STATUS_ATUAL.md:
- Após cada checkpoint
- Após completar tarefa importante
- Ao final de cada dia de trabalho
- Antes de pausar projeto
```

**Regra:** STATUS_ATUAL.md deve ser... ATUAL! Máximo 1 semana desatualizado.

### ❌ Erro 4: Checkpoint Genérico

```
❌ Errado:
# CHECKPOINT - 16/Jan/2026

Trabalhei no projeto hoje. Fiz algumas coisas.

✅ Correto:
# CHECKPOINT - 16/JAN/2026 - Implementação MVP Core

[Usar template completo com todas as seções]
- Onde estamos (específico)
- O que foi feito (lista detalhada)
- Arquivos criados (lista completa)
- Decisões (se houver)
- Próximos passos (claros)
```

**Regra:** Checkpoint = snapshot completo. Outra pessoa deve conseguir retomar projeto só lendo checkpoint.

### ❌ Erro 5: Projeto Fantasma

```
❌ Errado:
Projeto criado, estrutura completa, mas:
- README.md = template vazio
- STATUS_ATUAL.md = nunca atualizado
- Checkpoints = nenhum
- Tarefas = nenhuma
- Resultado: Projeto morto que polui _MOC_Projetos.md

✅ Correto:
Se projeto não decolou:
1. Criar CHECKPOINT explicando por quê
2. Marcar como 🟡 Pausado OU 📦 Arquivado
3. Atualizar _MOC_Projetos.md
4. Extrair aprendizados para 01_CONHECIMENTO/ se houver
5. Mover para arquivo se necessário
```

**Regra:** Projeto ativo = trabalho ativo. Sem trabalho = pausar/arquivar.

### ❌ Erro 6: Nomenclatura Inconsistente

```
❌ Errado:
checkpoints/
├── checkpoint 16 jan.md         ← espaços, sem UPPERCASE
├── CHECKPOINT-17-jan-2026.md    ← hífens em vez de underscores
├── check_18jan.md               ← prefixo errado

✅ Correto:
checkpoints/
├── CHECKPOINT_16JAN2026_Inicio.md
├── CHECKPOINT_17JAN2026_MVP_Completo.md
├── CHECKPOINT_18JAN2026_Sprint_1.md
```

**Regra:** Seguir padrões de nomenclatura à risca (ver seção Nomenclatura).

---

## 🔗 ESTRATÉGIAS DE ORGANIZAÇÃO

### 1. Sistema de Fases

**Para projetos grandes (>3 meses):**

```
planejamento/
├── PLANO_ESTRATEGICO.md         ← Visão geral
├── PLANO_Fase1_Fundacao.md      ← Fase 1
├── PLANO_Fase2_MVP.md           ← Fase 2
├── PLANO_Fase3_Lancamento.md    ← Fase 3
└── ROADMAP.md                   ← Timeline visual
```

**Cada fase:**
- Objetivo claro
- Entregas definidas
- Critério de conclusão
- Checkpoint ao final

### 2. Sistema de Sprints

**Para projetos ágeis (iterações curtas):**

```
tarefas/
├── BACKLOG.md                   ← Todas as tarefas futuras
├── SPRINT_ATUAL.md              ← Sprint ativo (ex: 16-22 Jan)
├── SPRINT_09JAN2026.md          ← Sprint passado
├── SPRINT_16JAN2026.md          ← Sprint passado
└── TAREFAS_CONCLUIDAS.md        ← Histórico

checkpoints/
├── CHECKPOINT_09JAN2026_Sprint_1.md
├── CHECKPOINT_16JAN2026_Sprint_2.md
```

**Cada sprint:**
- Duração fixa (1-2 semanas)
- Objetivo específico
- Checkpoint ao final
- Retrospectiva

### 3. Sistema de Métricas

**Para projetos orientados a resultados:**

```
metricas/
├── DASHBOARD.md                 ← Visão consolidada (sempre atual)
├── METRICAS_JAN2026.md          ← Mensal
├── METRICAS_FEV2026.md
├── RELATORIO_Financeiro.md      ← Por tipo
├── RELATORIO_Alcance.md
└── RELATORIO_Qualidade.md
```

**DASHBOARD.md atualizar:**
- Semanal mínimo
- Após cada milestone
- Antes de checkpoint

### 4. Documentação Progressiva

**Não criar tudo de uma vez:**

```
INÍCIO DO PROJETO:
docs/
└── briefing/
    └── BRIEFING_Inicial.md       ← Só o essencial

CONFORME NECESSÁRIO:
docs/
├── briefing/
│   ├── BRIEFING_Inicial.md
│   └── BRIEFING_Cliente.md       ← Adicionado quando houver cliente
├── especificacoes/
│   └── SPEC_Feature_X.md         ← Adicionado quando feature surgir
└── processos/
    └── PROCESSO_Deploy.md        ← Adicionado quando processo definir
```

**Regra:** Documentar quando necessário, não antecipadamente.

---

## ✅ CHECKLIST DE MANUTENÇÃO

### Diário (5 min)

- [ ] Atualizar STATUS_ATUAL.md (progresso do dia)
- [ ] Atualizar tarefas/SPRINT_ATUAL.md (marcar concluídas)
- [ ] Registrar bloqueios novos em STATUS_ATUAL.md

### Semanal (30 min)

- [ ] Criar CHECKPOINT (se projeto ativo)
- [ ] Revisar e atualizar DASHBOARD.md (métricas)
- [ ] Processar tarefas concluídas → TAREFAS_CONCLUIDAS.md
- [ ] Planejar próxima semana/sprint
- [ ] Atualizar _MOC_Projetos.md (se status mudou)

### Mensal (1h)

- [ ] Revisar PLANO_ESTRATEGICO.md (ainda alinhado?)
- [ ] Consolidar métricas mensais → METRICAS_[MES]YYYY.md
- [ ] Revisar roadmap (ajustar prazos se necessário)
- [ ] Avaliar se projeto deve continuar/pausar/arquivar
- [ ] Extrair conhecimento para 01_CONHECIMENTO/ (se houver)

### Ao Concluir Projeto (2h)

- [ ] Criar CHECKPOINT final completo
- [ ] Atualizar README.md (adicionar resultados)
- [ ] Documentar aprendizados principais
- [ ] Extrair conhecimento permanente → 01_CONHECIMENTO/
- [ ] Atualizar _MOC_Projetos.md (marcar ✅ Concluído)
- [ ] Celebrar! 🎉
- [ ] Agendar arquivamento (3-6 meses)

---

## 🔗 LINKS RELACIONADOS

- [[00_SISTEMA/PADROES/NOMENCLATURA.md]] - Padrões gerais de nomenclatura
- [[00_SISTEMA/PADROES/ESTRUTURA_PROJETOS.md]] - Estrutura detalhada de projetos
- [[_MOC_Projetos.md]] - MOC master desta categoria
- [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md]] - Protocolo geral
- [[04_RECURSOS/TEMPLATES/]] - Templates disponíveis (RPI, etc)
- [[01_CONHECIMENTO/]] - Para extrair conhecimento de projetos concluídos

---

**Versão:** 2.0 (Expandida)
**Criado:** 16/Jan/2026
**Atualizado:** 16/Jan/2026

**PROJETOS BEM ESTRUTURADOS = EXECUÇÃO IMPECÁVEL! 🚀**
