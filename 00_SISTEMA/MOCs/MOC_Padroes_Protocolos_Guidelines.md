---
created: 2026-01-22T21:58
updated: 2026-01-22T21:56
---
# MOC: Padrões, Protocolos e Guidelines

**Índice Master de Documentação do Sistema**

**Criado:** 16/Jan/2026
**Versão:** 1.0
**Propósito:** Navegação hierárquica de TODA documentação (25+ arquivos)
**Economia estimada:** -40-50% tokens (progressive disclosure)

---

## 🎯 NAVEGAÇÃO RÁPIDA

**Para Claude Code ao iniciar sessão:**
→ [[00_SISTEMA/GUIAS/GUIA_Leitura_Claude.md]] (Progressive disclosure)

**Para Gemini/Antigravity ao iniciar sessão:**
→ [[00_SISTEMA/GUIAS/GUIA_Leitura_Gemini.md]] (Foco execução)

**Para Usuário (Gassen):**
→ [[00_SISTEMA/GUIAS/GUIA_Usuario_Quick_Start.md]] (Decision trees)

**Problemas/Troubleshooting:**
→ [[00_SISTEMA/PROTOCOLOS/TROUBLESHOOTING_GUIA_RAPIDO.md]] (6 categorias)

**Qual protocolo de sincronização usar?**
→ [[00_SISTEMA/MOCs/MOC_Sincronizacao_Sistemas.md]] (Decision tree)

---

## 📚 HIERARQUIA DE DOCUMENTAÇÃO (5 NÍVEIS)

### 🏛️ NÍVEL 1: FUNDAÇÃO (3 arquivos)

**Leitura obrigatória ao iniciar no vault**

| Arquivo | Propósito | Quando Ler |
|---------|-----------|------------|
| [[CLAUDE.md]] | Instruções master para Claude Code | SEMPRE (primeira vez) |
| [[README.md]] | Visão geral do vault | Primeira vez |
| [[00_SISTEMA/PADROES/ARCHITECTURE_GUIDELINES.md]] | Arquitetura completa, Smart Zone (40%), RPI Framework | Criar estrutura grande |

**Total:** ~60KB (CLAUDE.md 30KB + README 10KB + Architecture 20KB)

---

### 📐 NÍVEL 2: PADRÕES (4 arquivos)

**Como o vault está organizado**

| Arquivo | Propósito | Quando Ler |
|---------|-----------|------------|
| [[00_SISTEMA/PADROES/NOMENCLATURA.md]] | **CRÍTICO** - Padrões de nomenclatura | Antes de criar QUALQUER arquivo |
| [[00_SISTEMA/PADROES/GUIA_Claude_vs_Gemini.md]] | Qual IA usar para cada tarefa | Decisão Claude vs Gemini |
| [[00_SISTEMA/PADROES/PADRAO_LOOP_RALPH.md]] | **NOVO** - Verificação automática de tarefas (Alan Nicolas) | Implementar gerentes/skills |
| [[00_SISTEMA/PADROES/ESTRUTURA_PROJETOS.md]] | ⚠️ **DEPRECADO** → Ver [[02_PROJETOS/_GUIDELINES.md]] | Não usar |

**Total:** ~30KB

**Nota:** ESTRUTURA_PROJETOS.md está deprecado (60% duplicação eliminada). Usar [[02_PROJETOS/_GUIDELINES.md]] diretamente.

---

### 📂 NÍVEL 3: GUIDELINES (5 arquivos)

**Padrões por categoria (01-05)**

| Arquivo | Categoria | Conteúdo |
|---------|-----------|----------|
| [[01_CONHECIMENTO/_GUIDELINES.md]] | Conhecimento permanente | O que pertence, nomenclatura, MOC integration |
| [[02_PROJETOS/_GUIDELINES.md]] | Projetos ativos | Estrutura obrigatória, workflows, templates |
| [[03_APRENDIZADO/_GUIDELINES.md]] | Cursos e estudos | Sistema 5C, organização lives, módulos |
| [[04_RECURSOS/_GUIDELINES.md]] | Templates, prompts, ferramentas | Organização recursos reutilizáveis |
| [[05_PESSOAL/_GUIDELINES.md]] | Journal, ideias, autoconhecimento | Estrutura pessoal, privacidade |

**Total:** ~110KB (consolidados, otimizados)

**Quando ler:**

- Criar arquivo na categoria X → Ler X/_GUIDELINES.md
- Mover arquivo → Ler guideline de origem + destino
- Dúvida sobre organização → Guideline relevante

---

### 🔧 NÍVEL 4: PROTOCOLOS (12 arquivos)

**Workflows operacionais**

#### 4.1. Sincronização (4 protocolos)

⚠️ **CONFUSO?** Ver [[00_SISTEMA/MOCs/MOC_Sincronizacao_Sistemas.md]] (Decision tree)

| Arquivo | Uso | Quando Aplicar |
|---------|-----|----------------|
| [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_MULTI_PC.md]] | Sincronizar Alienware ↔ Desktop Casa | Trocar de PC |
| [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_SINCRONIZACAO_AGENTES.md]] | Sincronizar Claude ↔ Gemini | Handoff entre IAs |
| [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_GITHUB_MULTI_DISPOSITIVO.md]] | Sincronizar iPhone ↔ Desktop ↔ Alienware (git) | Resolver branches Claude /* |
| [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_ANTIGRAVITY_GITHUB.md]] | GitHub API via Antigravity/Gemini | Criar issues, PRs via Gemini |

#### 4.2. Criação e Organização (5 protocolos)

| Arquivo | Uso | Quando Aplicar |
|---------|-----|----------------|
| [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md]] | **OBRIGATÓRIO** - Workflow de criação | Antes de criar QUALQUER arquivo |
| [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_INICIALIZACAO_NEVOA.md]] | **NOVO** - Boot proativo, Framework AOC | Ao chamar /nevoa |
| [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_AGENTES_iOS.md]] | Blueprint iOS (Alan Nicolas) | Criar agentes, Quality Gates, loops Ralph |
| [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_DIVISAO_SKILLS_Claude_Antigravity.md]] | **CRÍTICO** - Quem cria qual skill (Claude vs Gemini) | Criar skills, decisão de plataforma |
| [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_REVISAO_SEMANAL.md]] | Checklist semanal (Sexta 17h) | Fim de semana |

#### 4.3. Orquestração Bi-IA (3 protocolos)

| Arquivo | Uso | Quando Aplicar |
|---------|-----|----------------|
| [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_CLAUDE_GEMINI_ORQUESTRACAO.md]] | Divisão de responsabilidades, handoff, economia 90% tokens | Tarefa grande (>100k tokens) |
| [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_GUARDIAN.md]] | **NOVO** - Agente de manutenção automática, orquestrador de skills | Manutenção vault, auditoria, correção nomenclatura |
| [[00_SISTEMA/PROTOCOLOS/SOP_INTEGRACAO_ANTIGRAVITY.md]] | Setup Antigravity, workflows IDE | Configurar ambiente |

#### 4.4. Limites e Ética (2 protocolos)

| Arquivo | Uso | Quando Aplicar |
|---------|-----|----------------|
| [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_GEMINI_LIMITES_TOKENS.md]] | Gerenciar quota free tier Gemini (1M tokens) | Planejar uso Gemini |
| [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_EXTRACAO_ETICA.md]] | Processar conteúdo de terceiros (lives, PDFs) | Processar material externo |

#### 4.5. Troubleshooting (2 guias → 1 consolidado)

| Arquivo | Status | Uso |
|---------|--------|-----|
| [[00_SISTEMA/PROTOCOLOS/TROUBLESHOOTING_GUIA_RAPIDO.md]] | ✅ Ativo | **6 categorias de problemas** (overload, Gemini, sync, padrões, MOCs, performance) |
| [[00_SISTEMA/PROTOCOLOS/GUIA_RAPIDO_ERRO_OVERLOAD.md]] | ⚠️ **DEPRECADO** | Redireciona → TROUBLESHOOTING Seção 1 |
| [[00_SISTEMA/PROTOCOLOS/GUIA_RECUPERACAO_ERRO_GEMINI.md]] | ⚠️ **DEPRECADO** | Redireciona → TROUBLESHOOTING Seção 2 |

#### 4.6. Antigravity Skills (7 documentos - Fase 7.3) ✅

**Adicionado:** 18/JAN/2026

| Arquivo | Tipo | Uso |
|---------|------|-----|
| [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_Uso_Skills_Antigravity.md]] | Protocolo | Triggers, workflows, exemplos de uso das 3 skills |
| [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_Troubleshooting_Skills.md]] | Protocolo | Diagnóstico, erros comuns, fallback manual |
| [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_Manutencao_Skills.md]] | Protocolo | Versionamento, atualização, padrões Python |
| [[00_SISTEMA/GUIAS/GUIA_Edge_Cases_Skills.md]] | Guia | Limitações, cenários especiais, workarounds |
| [[04_RECURSOS/TEMPLATES/TEMPLATE_Criar_Skill_Antigravity.md]] | Template | Estrutura base para criar novas skills |
| [[04_RECURSOS/TEMPLATES/TEMPLATE_Prompt_Gemini_Nova_Skill.md]] | Template | Prompt padrão para pedir skills ao Gemini |
| [[04_RECURSOS/CHECKLISTS/CHECKLIST_Uso_Skills_Antigravity.md]] | Checklist | Pre/Post flight checks |

**Total:** ~80KB + ~40KB (Antigravity Skills) = ~120KB

---

### 📖 NÍVEL 5: GUIAS DE LEITURA (6 guias)

**Progressive disclosure - o que ler quando**

| Arquivo | Persona | Conteúdo |
|---------|---------|----------|
| [[00_SISTEMA/GUIAS/GUIA_Leitura_Claude.md]] | Claude Code | Leitura obrigatória/condicional, workflows, economia 40-50% tokens |
| [[00_SISTEMA/GUIAS/GUIA_Leitura_Gemini.md]] | Gemini/Antigravity | Papel no sistema bi-IA, o que ler/não ler, templates |
| [[00_SISTEMA/GUIAS/GUIA_Usuario_Quick_Start.md]] | Usuário (Gassen) | Decision trees, mapa de pastas, qual IA usar, rotinas |
| [[00_SISTEMA/GUIAS/GUIA_COMANDOS_CLAUDE.md]] | Técnico | Referência completa de comandos Claude |
| [[00_SISTEMA/GUIAS/QUICK_START_ANTIGRAVITY_GITHUB.md]] | Técnico | Quick Start para GitHub via Antigravity |
| [[00_SISTEMA/GUIAS/MANUAL_SYSTEM_GASSEN_V3.md]] | Histórico | Manual V3 do sistema (Referência) |

**Total:** ~40KB

---

### 🔬 NÍVEL 6: ANÁLISES E PESQUISAS (1 arquivo)

**Investigações técnicas e oportunidades de integração**

| Arquivo | Tópico | Status | Quando Consultar |
|---------|--------|--------|------------------|
| [[00_SISTEMA/ANALISES/ANALISE_Antigravity_Skills_Integracao_Sistema_BiIA.md]] | Antigravity Skills vs Claude Code Skills, arquitetura de integração bi-IA | 🔍 EM ANÁLISE | Planejar skills, integração Antigravity, monitoramento updates |

**Total:** ~30KB

**Conteúdo:**

- Comparação arquitetural Claude Skills vs Antigravity Skills
- Oportunidades de integração bi-IA
- Plano de ação em 5 fases
- Pesquisas necessárias (documentação oficial, limitações técnicas)
- Sistema de monitoramento de updates (Anthropic + Google)

---

## 🔀 MAPA DE INTERDEPENDÊNCIAS

**Ver análise completa:** [[00_SISTEMA/MOCs/MAPA_INTERDEPENDENCIAS.md]]

### Circularidades

**Nenhuma circularidade detectada!** ✅

Grafo é acíclico, ordenação topológica possível.

### Dependências Principais

**Fundação (Nível 1):**

- CLAUDE.md → Referencia TODOS os outros
- ARCHITECTURE_GUIDELINES → Define princípios (Smart Zone 40%, RPI)

**Padrões (Nível 2):**

- NOMENCLATURA.md ← Usado por PROTOCOLO_CRIACAO_ARQUIVOS
- GUIA_Claude_vs_Gemini ← Usado por PROTOCOLO_CLAUDE_GEMINI_ORQUESTRACAO

**Guidelines (Nível 3):**

- Cada _GUIDELINES.md ← Depende de NOMENCLATURA.md
- 02_PROJETOS/_GUIDELINES.md ← Substitui ESTRUTURA_PROJETOS.md

**Protocolos (Nível 4):**

- PROTOCOLO_CRIACAO_ARQUIVOS → Depende de NOMENCLATURA + Guidelines
- TROUBLESHOOTING_GUIA_RAPIDO → Consolida 2 guias antigos

**Guias (Nível 5):**

- GUIA_Leitura_Claude → Referencia MOC_Padroes_Protocolos_Guidelines (este arquivo)
- GUIA_Usuario_Quick_Start → Decision trees apontam para docs específicos

---

## 📊 ESTATÍSTICAS

### Arquivos por Nível

| Nível | Arquivos Ativos | Arquivos Deprecados | Total |
|-------|-----------------|---------------------|-------|
| 1. Fundação | 3 | 0 | 3 |
| 2. Padrões | 3 | 1 (ESTRUTURA_PROJETOS) | 4 |
| 3. Guidelines | 6 (1 arch + 5 categorias) | 0 | 6 |
| 4. Protocolos | 13 + 7 (Skills) = 20 | 2 (ERRO_OVERLOAD, ERRO_GEMINI) | 22 |
| 5. Guias | 3 + 1 (Edge Cases) = 4 | 0 | 4 |
| 6. Análises | 1 | 0 | 1 |
| **TOTAL** | **36** | **3** | **39** |

### Tamanho Estimado

- **Antes consolidação:** ~319KB (25 arquivos + redundância 60%)
- **Depois consolidação:** ~300KB ativos + 48KB novos = ~348KB total
- **Fase 7.3 (Skills):** +40KB (7 documentos Antigravity Skills)
- **Total atual:** ~388KB (38 arquivos)
- **Duplicação:** 60% → 0% ✅
- **Economia progressive disclosure:** 80-100k tokens → 40-60k tokens ✅

### Complexidade

- **Profundidade máxima:** 5 níveis
- **Circularidades:** 0
- **Referências cruzadas:** ~50
- **Deprecated mas preservados:** 3 (com avisos claros)

---

## 🎓 WORKFLOWS TÍPICOS

### Workflow 1: Iniciar Sessão (Claude Code)

```
1. Ler SESSION_LOG.md (obrigatório)
2. Ler PC_SYNC_LOG.md (obrigatório)
3. Ler GUIA_Leitura_Claude.md → Progressive disclosure
4. Se criar arquivo → NOMENCLATURA + PROTOCOLO_CRIACAO + guideline relevante
5. Se problema → TROUBLESHOOTING_GUIA_RAPIDO
```

**Tokens:**

- Primeira sessão: 30-40min leitura (~80k tokens)
- Sessões típicas: 5-10min leitura (~20k tokens)
- Sessões urgentes: 2min (logs apenas, ~5k tokens)

### Workflow 2: Criar Arquivo

```
1. PROTOCOLO_CRIACAO_ARQUIVOS (checklist)
   ├─ Ler NOMENCLATURA.md (prefixo, nome)
   ├─ Identificar categoria (01-05)
   ├─ Ler X/_GUIDELINES.md (estrutura, localização)
   └─ Criar arquivo + Atualizar MOC
```

**Tokens:** ~15-20k (3 arquivos relevantes)

### Workflow 3: Troubleshooting

```
1. Ler TROUBLESHOOTING_GUIA_RAPIDO.md
2. Identificar categoria (1-6)
3. Aplicar solução
4. Se não resolver → MOC relevante ou guideline específico
```

**Tokens:** ~5-10k

### Workflow 4: Decisão Claude vs Gemini

```
1. Ler GUIA_Claude_vs_Gemini.md (decisão estratégica)
2. Se Gemini → PROTOCOLO_CLAUDE_GEMINI_ORQUESTRACAO (handoff)
3. Se necessário GitHub → PROTOCOLO_ANTIGRAVITY_GITHUB
```

**Tokens:** ~10-15k

### Workflow 5: Sincronização

```
1. Trocar PC? → PROTOCOLO_MULTI_PC + PC_SYNC_LOG.md
2. Handoff IA? → PROTOCOLO_SINCRONIZACAO_AGENTES + SESSION_LOG.md
3. GitHub branches? → PROTOCOLO_GITHUB_MULTI_DISPOSITIVO
4. Dúvida qual? → MOC_Sincronizacao_Sistemas.md (decision tree)
```

**Tokens:** ~5-15k

---

## 🚨 ANTI-PATTERNS

### ❌ NÃO FAZER

1. **Ler TUDO ao iniciar sessão**
   - Causa: Overload contexto (>60% = Dumb Zone)
   - Solução: Progressive disclosure (GUIA_Leitura_Claude)

2. **Ignorar NOMENCLATURA ao criar arquivo**
   - Causa: Inconsistência, bagunça
   - Solução: PROTOCOLO_CRIACAO_ARQUIVOS (obrigatório)

3. **Duplicar informação em múltiplos docs**
   - Causa: Divergência, manutenção impossível
   - Solução: Single source of truth (VALORES_OFICIAIS em projetos, NOMENCLATURA em sistema)

4. **Criar nova documentação sem consultar MOC**
   - Causa: Estrutura paralela, fragmentação
   - Solução: Sempre atualizar MOC relevante

5. **Usar guias deprecados**
   - Causa: Informação desatualizada
   - Solução: Avisos claros de deprecação + redirecionamento

---

## ✅ BEST PRACTICES

### Smart Zone (40% Rule)

**Princípio:** Manter contexto abaixo de 40% da janela (80k/200k tokens)

**Aplicação:**

- Progressive disclosure (guias de leitura)
- On-demand loading (só ler arquivos necessários)
- Sub-agents (Task tool para tarefas específicas)
- Checkpoints (salvar estado, nova janela limpa)

### Single Source of Truth

**Princípio:** Uma fonte de verdade por tipo de informação

**Aplicação:**

- Nomenclatura → NOMENCLATURA.md (único)
- Estrutura projetos → 02_PROJETOS/_GUIDELINES.md (deprecou ESTRUTURA_PROJETOS)
- Valores KabaK → VALORES_OFICIAIS.md (único)
- Troubleshooting → TROUBLESHOOTING_GUIA_RAPIDO.md (consolidou 2 fragmentados)

### Deprecação sem Destruição

**Princípio:** Nunca deletar, sempre deprecar com aviso claro

**Template:**

```markdown
# [DEPRECADO] Título Original

⚠️ **DEPRECADO** - Ver [[Arquivo_Novo.md]] (Seção X)

Razão: [Por que foi deprecado]
Data deprecação: DD/MMM/YYYY
Substituído por: [[Link]]

---

[Preservar conteúdo original abaixo para referência histórica]
```

---

## 🔄 HISTÓRICO DE CONSOLIDAÇÕES

### 16/Jan/2026 - Consolidação Opção B (Moderada)

**Problema:**

- 25+ arquivos (~319KB)
- Duplicação 60% (ESTRUTURA_PROJETOS vs 02_PROJETOS/_GUIDELINES)
- Troubleshooting fragmentado (2 guias)
- Confusão sincronização (4 protocolos sem decisão tree)
- Token usage 80-100k por sessão típica

**Solução:**

- ✅ Criados 7 novos arquivos estruturais (48KB)
- ✅ Deprecados 3 arquivos (preservados com avisos)
- ✅ Eliminada duplicação 60% → 0%
- ✅ Troubleshooting consolidado (2 → 1)
- ✅ MOC Sincronização criado (decision tree)
- ✅ Guias de leitura por persona (Claude, Gemini, User)
- ✅ Economia estimada: -40-50% tokens (80k → 40-60k)

**Arquivos criados:**

1. MOC_Padroes_Protocolos_Guidelines.md (este arquivo)
2. MOC_Sincronizacao_Sistemas.md
3. TROUBLESHOOTING_GUIA_RAPIDO.md
4. GUIA_Leitura_Claude.md
5. GUIA_Leitura_Gemini.md
6. GUIA_Usuario_Quick_Start.md
7. MAPA_INTERDEPENDENCIAS.md

**Arquivos deprecados:**

1. ESTRUTURA_PROJETOS.md → [[02_PROJETOS/_GUIDELINES.md]]
2. GUIA_RAPIDO_ERRO_OVERLOAD.md → [[TROUBLESHOOTING_GUIA_RAPIDO.md]] Seção 1
3. GUIA_RECUPERACAO_ERRO_GEMINI.md → [[TROUBLESHOOTING_GUIA_RAPIDO.md]] Seção 2

---

## 📖 GLOSSÁRIO

- **MOC (Map of Content):** Arquivo índice que organiza outros arquivos
- **Progressive Disclosure:** Carregar contexto em estágios, não tudo de uma vez
- **Smart Zone:** <40% da janela de contexto (ótimo desempenho LLM)
- **Dumb Zone:** >60% da janela (alucinação aumenta)
- **RPI Framework:** Research → Plan → Implementation (carregamento progressivo)
- **Single Source of Truth:** Uma fonte de verdade por tipo de informação
- **Handoff:** Transferir tarefa de Claude para Gemini (ou vice-versa)
- **Deprecado:** Arquivo obsoleto, preservado com aviso de redirecionamento
- **Guideline:** Padrão de organização por categoria (01-05)
- **Protocolo:** Workflow operacional (como fazer X)

---

## 🆘 AJUDA

### Se está perdido

1. **"Não sei o que ler ao iniciar sessão"**
   → [[00_SISTEMA/GUIAS/GUIA_Leitura_Claude.md]] (se Claude)
   → [[00_SISTEMA/GUIAS/GUIA_Leitura_Gemini.md]] (se Gemini)
   → [[00_SISTEMA/GUIAS/GUIA_Usuario_Quick_Start.md]] (se usuário)

2. **"Não sei onde criar arquivo"**
   → [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md]]
   → [[00_SISTEMA/PADROES/NOMENCLATURA.md]]

3. **"Algo deu errado"**
   → [[00_SISTEMA/PROTOCOLOS/TROUBLESHOOTING_GUIA_RAPIDO.md]]

4. **"Qual protocolo de sincronização usar?"**
   → [[00_SISTEMA/MOCs/MOC_Sincronizacao_Sistemas.md]]

5. **"Claude ou Gemini?"**
   → [[00_SISTEMA/PADROES/GUIA_Claude_vs_Gemini.md]]

6. **"Como está estruturada a arquitetura?"**
   → [[00_SISTEMA/PADROES/ARCHITECTURE_GUIDELINES.md]]

### Se quer entender interdependências

→ [[00_SISTEMA/MOCs/MAPA_INTERDEPENDENCIAS.md]]

---

**Versão:** 1.3
**Criado:** 16/Jan/2026
**Status:** ✅ ATIVO
**Última atualização:** 25/Jan/2026 (PROTOCOLO_CRIACAO_AGENTES_iOS - Blueprint Alan Nicolas)

**NAVEGAÇÃO CLARA = ECONOMIA DE TOKENS = MELHOR DESEMPENHO** 🗺️✅
