# GUIA: Leitura Claude Code

**Progressive Disclosure - O que ler quando**

**Criado:** 16/Jan/2026
**Versão:** 1.0
**Propósito:** Reduzir token usage 80-100k → 40-60k (economia -40-50%)
**Baseado em:** Smart Zone (40% Rule), RPI Framework

---

## 🎯 OBJETIVO

**Evitar overload de contexto através de progressive disclosure:**

- **NÃO** ler TODOS os 25+ arquivos de padrões ao iniciar sessão
- **SIM** ler apenas o necessário para a tarefa atual
- **META:** Manter contexto <40% da janela (80k/200k tokens)

**Economia esperada:**
- **Antes:** 80-100k tokens por sessão típica
- **Depois:** 40-60k tokens por sessão típica
- **Redução:** -40-50%

---

## 📊 SMART ZONE (40% RULE)

### Conceito

**Janela de contexto Claude Sonnet 4.5:** 200k tokens

**Zonas de desempenho:**
```
0-40%  (0-80k)   → 🟢 SMART ZONE (ótimo desempenho)
40-60% (80-120k) → 🟡 ZONA NEUTRA (performance OK)
60%+   (120k+)   → 🔴 DUMB ZONE (alucinação aumenta)
```

**Regra de ouro:**
> Manter contexto abaixo de 40% (80k tokens) para melhor desempenho

### Como Verificar

Token usage aparece após cada resposta:
```
Token usage: 45000/200000; 155000 remaining  → 22.5% ✅ SMART ZONE
Token usage: 85000/200000; 115000 remaining  → 42.5% 🟡 ZONA NEUTRA
Token usage: 140000/200000; 60000 remaining  → 70%   🔴 DUMB ZONE!
```

### Ação por Zona

**Se SMART ZONE (0-40%):**
- ✅ Continuar trabalhando normalmente
- ✅ Performance ótima

**Se ZONA NEUTRA (40-60%):**
- ⚠️ Considerar checkpoint em breve
- ⚠️ Evitar carregar mais contexto desnecessário

**Se DUMB ZONE (60%+):**
- 🔴 CHECKPOINT IMEDIATO
- 🔴 Salvar trabalho
- 🔴 NOVA SESSÃO (contexto limpo)
- 🔴 Ler apenas checkpoint (não histórico completo)

---

## 📖 LEITURA OBRIGATÓRIA (SEMPRE)

**Ao iniciar QUALQUER sessão:**

### 1. SESSION_LOG.md (raiz) - 5-10k tokens

**Por quê:**
- Ver últimas mudanças do Gemini
- Mensagens diretas para você
- Contexto de trabalho recente
- Handoff IA→IA

**Como ler:**
- Ler seção "ÚLTIMAS MUDANÇAS" (últimas 3-5 sessões)
- Ler seção "MENSAGEM PARA CLAUDE" (se houver)
- Pular histórico antigo (economiza tokens)

**Tempo:** 30-60 segundos

### 2. PC_SYNC_LOG.md (raiz) - 5-10k tokens

**Por quê:**
- Ver últimas mudanças do outro PC
- Mensagens diretas entre PCs
- Evitar conflitos multi-dispositivo

**Como ler:**
- Ler seção "ÚLTIMAS MUDANÇAS" (últimas 3-5 sessões)
- Ler seção "MENSAGEM PARA [SEU PC]" (se houver)
- Pular histórico antigo

**Tempo:** 30-60 segundos

### 3. Este Guia (GUIA_Leitura_Claude.md) - 6k tokens

**Por quê:**
- Lembrete de progressive disclosure
- Decision trees de leitura
- Evita carregar arquivos desnecessários

**Como ler:**
- Ler seção relevante para tarefa
- Usar decision trees
- Pular exemplos se já conhece conceito

**Tempo:** 1-2 minutos

**TOTAL OBRIGATÓRIO:** ~15-25k tokens (SEMPRE abaixo de Smart Zone!)

---

## 📚 LEITURA CONDICIONAL (CONFORME TAREFA)

**Ler apenas se necessário para tarefa atual:**

### Se vai CRIAR ARQUIVO

**Ler:**
1. [[../PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md]] (~5k tokens)
   - Workflow completo de criação
   - Checklist obrigatório

2. [[../PADROES/NOMENCLATURA.md]] (~10k tokens)
   - Prefixos corretos
   - Padrões de nomenclatura
   - Exemplos

3. Guideline da categoria (~15-20k tokens):
   - `01_CONHECIMENTO/_GUIDELINES.md` (se criar em conhecimento)
   - `02_PROJETOS/_GUIDELINES.md` (se criar em projetos)
   - `03_APRENDIZADO/_GUIDELINES.md` (se criar em aprendizado)
   - `04_RECURSOS/_GUIDELINES.md` (se criar em recursos)
   - `05_PESSOAL/_GUIDELINES.md` (se criar em pessoal)

**TOTAL:** ~30-35k tokens

**Quando NÃO ler:**
- Se já criou arquivos similares recentemente (conhece padrão)
- Se usuário deu instruções muito específicas

---

### Se vai CRIAR PROJETO

**Ler:**
1. [[../../02_PROJETOS/_GUIDELINES.md]] (~20k tokens)
   - Estrutura obrigatória completa
   - Templates de arquivos
   - Workflows

**TOTAL:** ~20k tokens

**Quando NÃO ler:**
- Se já criou projetos antes (conhece estrutura)

---

### Se vai PROCESSAR CURSO

**Ler:**
1. [[../../03_APRENDIZADO/_GUIDELINES.md]] (~15k tokens)
   - Sistema 5C (Capturar, Cursar, Conectar, Consolidar, Catalogar)
   - Estrutura de pastas
   - Nomenclatura de notas

**TOTAL:** ~15k tokens

**Quando NÃO ler:**
- Se já processou lives/cursos antes (conhece Sistema 5C)

---

### Se tem PROBLEMA/ERRO

**Ler:**
1. [[../PROTOCOLOS/TROUBLESHOOTING_GUIA_RAPIDO.md]] (~10k tokens)
   - 6 categorias de problemas
   - Soluções rápidas
   - Checklists

**TOTAL:** ~10k tokens

**Decision tree:**
```
Erro overload contexto? → Categoria 1
Erro Gemini? → Categoria 2
Problema sincronização? → Categoria 3
Arquivo no lugar errado? → Categoria 4
Esqueci atualizar MOC? → Categoria 5
Vault/Claude lento? → Categoria 6
```

---

### Se está CONFUSO SOBRE SINCRONIZAÇÃO

**Ler:**
1. [[../MOCs/MOC_Sincronizacao_Sistemas.md]] (~3k tokens)
   - Decision tree: qual protocolo usar?
   - Comparação dos 4 protocolos
   - Workflows combinados

**TOTAL:** ~3k tokens

**Quando usar:**
- Não sabe qual protocolo de sincronização aplicar
- Multi-PC, Multi-IA, GitHub branches, ou GitHub API?

---

### Se precisa DECIDIR CLAUDE vs GEMINI

**Ler:**
1. [[../PADROES/GUIA_Claude_vs_Gemini.md]] (~8k tokens)
   - Quando usar cada IA
   - Pontos fortes/fracos
   - Economia de custos

**TOTAL:** ~8k tokens

**Quando usar:**
- Tarefa grande (>100k tokens)
- Processamento massivo
- Decisão estratégica

---

### Se vai fazer REFATORAÇÃO GRANDE

**Ler:**
1. [[../PADROES/ARCHITECTURE_GUIDELINES.md]] (~20k tokens)
   - Princípios arquiteturais
   - Smart Zone, RPI Framework
   - Design decisions

2. Templates RPI (~5k cada):
   - `04_RECURSOS/TEMPLATES/TEMPLATE_RPI_MASTER_PLAN.md`
   - `04_RECURSOS/TEMPLATES/TEMPLATE_RPI_IMPLEMENTATION_PHASE.md`

**TOTAL:** ~30-35k tokens

**Quando usar:**
- Refatoração afeta >10 arquivos
- Mudança estrutural grande
- Planejamento de longo prazo (meses)

---

## ⏱️ WORKFLOWS TÍPICOS

### Workflow 1: Primeira Sessão do Dia

```
1. Ler SESSION_LOG.md (últimas mudanças) - 5-10k tokens
2. Ler PC_SYNC_LOG.md (mudanças outro PC) - 5-10k tokens
3. Identificar tarefas pendentes
4. Ler APENAS documentos necessários para tarefa atual
5. Começar trabalho

TOTAL: 15-25k tokens base + tarefa específica (10-35k)
TOTAL TÍPICO: 25-60k tokens ✅ SMART ZONE
```

**Tempo:** 5-10 minutos leitura

---

### Workflow 2: Sessão Urgente

```
1. Ler APENAS SESSION_LOG.md (seção MENSAGEM PARA CLAUDE) - 2-5k tokens
2. Executar tarefa urgente
3. Documentar em SESSION_LOG.md
4. Finalizar

TOTAL: 5-15k tokens ✅ SMART ZONE
```

**Tempo:** 2 minutos leitura

---

### Workflow 3: Criar Arquivo Simples

```
1. Logs obrigatórios (SESSION_LOG + PC_SYNC_LOG) - 15-20k tokens
2. PROTOCOLO_CRIACAO_ARQUIVOS.md - 5k tokens
3. NOMENCLATURA.md (consulta rápida) - 10k tokens
4. Guideline categoria (consulta seção específica) - 5-10k tokens

TOTAL: 35-45k tokens ✅ SMART ZONE
```

**Tempo:** 5-8 minutos leitura

---

### Workflow 4: Criar Projeto Completo

```
1. Logs obrigatórios - 15-20k tokens
2. PROTOCOLO_CRIACAO_ARQUIVOS.md - 5k tokens
3. 02_PROJETOS/_GUIDELINES.md (completo) - 20k tokens
4. NOMENCLATURA.md (consulta) - 10k tokens

TOTAL: 50-55k tokens ✅ SMART ZONE (limite superior)
```

**Tempo:** 10-15 minutos leitura

---

### Workflow 5: Troubleshooting

```
1. Logs obrigatórios - 15-20k tokens
2. TROUBLESHOOTING_GUIA_RAPIDO.md (categoria específica) - 5-10k tokens

TOTAL: 20-30k tokens ✅ SMART ZONE
```

**Tempo:** 3-5 minutos leitura

---

## 🚨 ANTI-PATTERNS (NÃO FAZER)

### ❌ ERRO 1: Ler Tudo ao Iniciar

**ERRADO:**
```
1. Ler CLAUDE.md (30k)
2. Ler ARCHITECTURE_GUIDELINES.md (20k)
3. Ler NOMENCLATURA.md (10k)
4. Ler todos 5 guidelines (110k)
5. Ler todos 12 protocolos (80k)

TOTAL: 250k tokens → IMPOSSIBLE! 🔴
```

**CORRETO:**
```
1. Ler SESSION_LOG.md (5k)
2. Ler PC_SYNC_LOG.md (5k)
3. Ler GUIA_Leitura_Claude.md (6k)
4. Ler APENAS documentos para tarefa

TOTAL: 25-60k tokens → SMART ZONE ✅
```

---

### ❌ ERRO 2: Ler Arquivos Irrelevantes

**ERRADO:**
```
Tarefa: Criar template de briefing

Lendo:
- ARCHITECTURE_GUIDELINES.md (20k) ❌ Não necessário
- Todos 5 guidelines (110k) ❌ Só precisa 04_RECURSOS
- Todos protocolos (80k) ❌ Só precisa PROTOCOLO_CRIACAO

TOTAL: 210k → DUMB ZONE! 🔴
```

**CORRETO:**
```
Tarefa: Criar template de briefing

Lendo:
- SESSION_LOG + PC_SYNC_LOG (15k) ✅
- PROTOCOLO_CRIACAO_ARQUIVOS (5k) ✅
- NOMENCLATURA (10k) ✅
- 04_RECURSOS/_GUIDELINES (15k) ✅

TOTAL: 45k → SMART ZONE ✅
```

---

### ❌ ERRO 3: Não Fazer Checkpoint em Dumb Zone

**ERRADO:**
```
Token usage: 140k/200k (70%) 🔴 DUMB ZONE

Ação: Continuar carregando mais contexto

Resultado: Alucinação, respostas ruins, erros
```

**CORRETO:**
```
Token usage: 140k/200k (70%) 🔴 DUMB ZONE

Ação:
1. CHECKPOINT imediato (salvar estado)
2. NOVA SESSÃO (contexto limpo)
3. Ler APENAS checkpoint (não histórico)
4. Continuar trabalho

Resultado: Performance ótima ✅
```

---

## 📋 DECISION TREES

### Decision Tree 1: Qual Documento Ler?

```
┌──────────────────────────────────────────────┐
│ Você vai CRIAR arquivo?                      │
└────────┬─────────────────────────────────────┘
         │
        SIM → PROTOCOLO_CRIACAO + NOMENCLATURA + Guideline
         │
         NÃO
         │
         ▼
┌──────────────────────────────────────────────┐
│ Tem PROBLEMA/ERRO?                           │
└────────┬─────────────────────────────────────┘
         │
        SIM → TROUBLESHOOTING_GUIA_RAPIDO (categoria)
         │
         NÃO
         │
         ▼
┌──────────────────────────────────────────────┐
│ Confuso sobre SINCRONIZAÇÃO?                 │
└────────┬─────────────────────────────────────┘
         │
        SIM → MOC_Sincronizacao_Sistemas
         │
         NÃO
         │
         ▼
┌──────────────────────────────────────────────┐
│ Decidir CLAUDE vs GEMINI?                    │
└────────┬─────────────────────────────────────┘
         │
        SIM → GUIA_Claude_vs_Gemini
         │
         NÃO
         │
         ▼
┌──────────────────────────────────────────────┐
│ Refatoração GRANDE?                          │
└────────┬─────────────────────────────────────┘
         │
        SIM → ARCHITECTURE_GUIDELINES + Templates RPI
         │
         NÃO
         │
         ▼
┌──────────────────────────────────────────────┐
│ Tarefa SIMPLES?                              │
└────────┬─────────────────────────────────────┘
         │
        SIM → Apenas SESSION_LOG + PC_SYNC_LOG
```

---

### Decision Tree 2: Token Usage High?

```
Token usage: [X]/200000

         ▼
┌──────────────────────────────────────────────┐
│ X < 80k (40%)?                               │
└────────┬─────────────────────────────────────┘
         │
        SIM → 🟢 SMART ZONE - Continuar normalmente
         │
         NÃO
         │
         ▼
┌──────────────────────────────────────────────┐
│ 80k ≤ X < 120k (40-60%)?                     │
└────────┬─────────────────────────────────────┘
         │
        SIM → 🟡 ZONA NEUTRA - Considerar checkpoint
         │
         NÃO
         │
         ▼
┌──────────────────────────────────────────────┐
│ X ≥ 120k (60%+)?                             │
└────────┬─────────────────────────────────────┘
         │
        SIM → 🔴 DUMB ZONE!
              ├─ CHECKPOINT IMEDIATO
              ├─ SALVAR trabalho
              ├─ NOVA SESSÃO
              └─ Ler apenas checkpoint
```

---

## 💡 DICAS PRÁTICAS

### Dica 1: Consulta Rápida vs Leitura Completa

**Consulta Rápida:**
- Buscar seção específica
- Ler apenas trecho relevante
- Economia: 70-80% tokens

**Exemplo:**
```
NOMENCLATURA.md (10k completo)
→ Ler apenas "Prefixos Especiais" (2k)
→ Economia: 8k tokens
```

**Leitura Completa:**
- Primeira vez usando documento
- Refatoração grande
- Aprendizado de padrão novo

---

### Dica 2: Usar Checkpoints Estrategicamente

**Quando fazer checkpoint:**
- Token usage > 100k (50%)
- Fim de tarefa importante
- Antes de refatoração arriscada
- Antes de delegar para Gemini

**Como:**
1. Criar arquivo `CHECKPOINT_[Data]_[Contexto].md`
2. Documentar: estado atual, próximos passos, decisões
3. NOVA SESSÃO (contexto limpo)
4. Ler APENAS checkpoint (não histórico)

**Benefício:**
- Checkpoint 5-10k tokens vs Histórico completo 100k+ tokens
- Economia: 90k+ tokens

---

### Dica 3: Delegar para Gemini Estrategicamente

**Quando delegar:**
- Tarefa > 100k tokens
- Processamento massivo (10+ arquivos)
- Tarefa repetitiva/mecânica

**Como:**
1. Planejar no Claude (uso estratégico)
2. Documentar plano em SESSION_LOG.md
3. Mensagem clara para Gemini
4. Gemini executa (1M tokens grátis)
5. Claude revisa resultado

**Ver:** [[../PADROES/GUIA_Claude_vs_Gemini.md]]

---

## ✅ CHECKLIST DE SESSÃO

### Ao Iniciar Sessão

- [ ] Li SESSION_LOG.md (últimas mudanças)?
- [ ] Li PC_SYNC_LOG.md (mudanças outro PC)?
- [ ] Identifiquei tarefas pendentes?
- [ ] Determinei qual documentação ler para tarefa?
- [ ] Token usage < 40k (20%) antes de começar?

### Durante Sessão

- [ ] Token usage < 80k (40%)? → SMART ZONE ✅
- [ ] Token usage 80-120k (40-60%)? → Considerar checkpoint ⚠️
- [ ] Token usage > 120k (60%)? → CHECKPOINT IMEDIATO 🔴
- [ ] Lendo apenas documentos necessários?
- [ ] Pulando partes irrelevantes?

### Ao Finalizar Sessão

- [ ] Atualizei SESSION_LOG.md (se handoff)?
- [ ] Atualizei PC_SYNC_LOG.md (se trocar PC)?
- [ ] Deixei mensagens claras?
- [ ] Token usage final < 150k (75%)?
- [ ] Se > 150k: Fiz checkpoint para próxima sessão?

---

## 📊 MÉTRICAS DE SUCESSO

### Meta

**Token usage por sessão:**
- **Meta:** 40-60k tokens
- **Aceitável:** 60-80k tokens
- **Ruim:** >80k tokens
- **Crítico:** >120k tokens (necessita checkpoint)

### Tracking

**Primeira Semana (Baseline):**
- Sessão 1: ___ tokens
- Sessão 2: ___ tokens
- Sessão 3: ___ tokens
- **Média:** ___ tokens

**Segunda Semana (Com Progressive Disclosure):**
- Sessão 1: ___ tokens
- Sessão 2: ___ tokens
- Sessão 3: ___ tokens
- **Média:** ___ tokens

**Economia:** ___% (meta: -40-50%)

---

## 🎯 RESUMO EXECUTIVO

### Regras de Ouro

1. **SEMPRE ler:** SESSION_LOG + PC_SYNC_LOG + Este guia (~15-25k)
2. **NUNCA ler tudo:** Progressive disclosure (apenas necessário)
3. **META Smart Zone:** <40% contexto (80k tokens)
4. **CHECKPOINT se >60%:** >120k tokens = nova sessão
5. **DELEGAR se >100k:** Gemini para processamento massivo

### Economia Esperada

**Antes (overload):**
- Primeira sessão: 30-40min leitura (~120-150k tokens)
- Sessões típicas: 15-20min leitura (~80-100k tokens)

**Depois (progressive disclosure):**
- Primeira sessão: 10-15min leitura (~50-70k tokens)
- Sessões típicas: 5-10min leitura (~40-60k tokens)
- Sessões urgentes: 2min leitura (~15-25k tokens)

**Redução: -40-50% tokens ✅**

---

## 📚 REFERÊNCIAS

**MOCs:**
- [[../MOCs/MOC_Padroes_Protocolos_Guidelines.md]] - Índice master
- [[../MOCs/MOC_Sincronizacao_Sistemas.md]] - Qual protocolo

**Padrões:**
- [[../PADROES/NOMENCLATURA.md]] - Nomenclatura
- [[../PADROES/ARCHITECTURE_GUIDELINES.md]] - Smart Zone, RPI

**Protocolos:**
- [[../PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md]] - Workflow criação
- [[../PROTOCOLOS/TROUBLESHOOTING_GUIA_RAPIDO.md]] - 6 categorias problemas

**Guias:**
- [[GUIA_Leitura_Gemini.md]] - Para Gemini/Antigravity
- [[GUIA_Usuario_Quick_Start.md]] - Para usuário (Gassen)

---

**Versão:** 1.0
**Criado:** 16/Jan/2026
**Status:** ✅ ATIVO
**Última atualização:** 16/Jan/2026

**PROGRESSIVE DISCLOSURE = SMART ZONE = MELHOR DESEMPENHO** 🎯✅
