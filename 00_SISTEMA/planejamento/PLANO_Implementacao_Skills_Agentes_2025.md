---
criado: 2025-12-30
atualizado: 2025-12-30
versao: 1.0
status: Em Planejamento
tipo: Plano de Implementação Técnica
responsavel: Claude Architect + Gassen
---

# 🚀 PLANO DE IMPLEMENTAÇÃO: SKILLS + AGENTES + CHECKPOINTS 2025

**Sistema Evolutivo de Skills para Claude Code**

---

## 📋 ÍNDICE

1. [Visão Geral](#visão-geral)
2. [Análise da Situação Atual](#análise-da-situação-atual)
3. [Arquitetura Proposta](#arquitetura-proposta)
4. [Especificações Técnicas](#especificações-técnicas)
5. [Roadmap de Implementação](#roadmap-de-implementação)
6. [Análise de ROI](#análise-de-roi)
7. [Riscos e Mitigações](#riscos-e-mitigações)
8. [Métricas de Sucesso](#métricas-de-sucesso)
9. [Próximos Passos](#próximos-passos)

---

## 🎯 VISÃO GERAL

### Objetivo

Implementar sistema avançado de skills para Claude Code aproveitando as **novas funcionalidades 2025**:

- Agentes em background (paralelos)
- Checkpoints autônomos
- Sugestões inteligentes
- Skills com parâmetros dinâmicos

### Problema a Resolver

**Estado atual:**

- 11 skills funcionais mas limitadas
- Agentes executam sequencialmente (lento)
- Sincronização manual (falível)
- 9 agentes de domínio SEM skills dedicadas
- Perda de contexto entre sessões
- ~5000 tokens/sessão (desperdício)

**Estado desejado:**

- 20+ skills especializadas
- Execução paralela (5x mais rápido)
- Sincronização automática (100% confiável)
- Skills para TODOS os agentes
- Zero perda de contexto
- ~500 tokens/sessão (90% economia)

### Impacto Esperado

| Métrica                      | Antes    | Depois | Ganho               |
| ---------------------------- | -------- | ------ | ------------------- |
| Velocidade tarefas complexas | 1x       | 5x     | +400%               |
| Economia de tokens           | Baseline | 90%    | -4500 tokens/sessão |
| Continuidade sessões         | 30%      | 100%   | +233%               |
| Isolamento contextos         | 60%      | 100%   | +67%                |
| Produtividade diária         | 1x       | 10x    | +900%               |

---

## 📊 ANÁLISE DA SITUAÇÃO ATUAL

### Skills Existentes (11)

#### **Agentes Especializados** (3)

1. `/nevoa` - Orquestração
2. `/claude-architect` - Padrões
3. `/marie-kondo` - Organização

**Gap:** Agentes de domínio (Elena, Pedro, Alan, Lucas, Dr. Green) não têm skills!

#### **Ferramentas** (5)

1. `/validate` - Validação
2. `/gemini` - Delegação
3. `/ultra-think` - Análise
4. `/sync` - Sincronização manual
5. `/atualizar-status` - Status

**Gap:** Sincronização é manual, não automática!

#### **Contextos** (2)

1. `/learn` - Aprendizado
2. `/work` - Projetos

**Gap:** Contextos muito genéricos, falta especialização!

#### **Utilitários** (1)

1. `/limpeza-raiz-vault` - Limpeza

**Gap:** Falta dashboard de monitoramento!

### Funcionalidades Claude Code 2025 NÃO Utilizadas

1. **Agentes em Background** ❌
   - Disponível: `run_in_background=true` no Task tool
   - Não utilizado: Todas skills rodam sequencialmente

2. **Checkpoints Automáticos** ❌
   - Disponível: Hooks de sessão
   - Não utilizado: Sincronização manual via `/sync`

3. **Skills com Parâmetros** ❌
   - Disponível: `$ARGUMENTS` em skills
   - Não utilizado: Skills são estáticas

4. **Sugestões Inteligentes** ✅
   - Disponível e ativo (Tab/Enter)

5. **Task Monitoring** ❌
   - Disponível: `TaskOutput` tool
   - Não utilizado: Sem visibilidade de tasks em background

### Análise de Uso de Tokens

**Sessão típica atual:**

```
Início sessão: ~1000 tokens (CLAUDE.md + contexto geral)
Trabalho: ~3000-4000 tokens (mistura de contextos)
Finalização: ~500 tokens (atualizar STATUS)
TOTAL: ~5000 tokens/sessão
```

**Problema identificado:**

- Carrega TUDO mesmo quando só precisa de UMA área
- Exemplo: Trabalhando em tráfego mas carrega contexto DeFi, IA, etc
- Desperdiça ~80% dos tokens

---

## 🏗️ ARQUITETURA PROPOSTA

### Arquitetura Geral

```
┌─────────────────────────────────────────────────────────────┐
│                     CLAUDE CODE SESSION                      │
└───────────────────────┬─────────────────────────────────────┘
                        │
        ┌───────────────┴───────────────┐
        │                               │
        ▼                               ▼
┌──────────────────┐          ┌─────────────────┐
│  AGENTES CORE    │          │ AGENTES DOMÍNIO │
│  (Plataforma)    │          │ (Especializados)│
└────────┬─────────┘          └────────┬────────┘
         │                              │
    ┌────┴────┐                    ┌────┴─────────────────┐
    │         │                    │    │    │    │       │
    ▼         ▼                    ▼    ▼    ▼    ▼       ▼
/nevoa  /claude-architect    /pedro /lucas /alan /elena /dr-green
/marie-kondo                 (Tráfego)(DeFi)(IA)(Prod)(Cultivo)
                                     │
                        ┌────────────┴────────────┐
                        │                         │
                        ▼                         ▼
              ┌──────────────────┐      ┌─────────────────┐
              │ WORKFLOWS        │      │ AUTOMAÇÕES      │
              │ (Orquestrados)   │      │ (Checkpoints)   │
              └──────┬───────────┘      └────────┬────────┘
                     │                            │
        ┌────────────┴──────────┐        ┌────────┴────────┐
        ▼                       ▼        ▼                 ▼
/processar-live          /analise-   auto-      auto-
/criar-conteudo          completa  checkpoint  recovery
/workflow-comercial      -projeto
```

### Camadas do Sistema

#### **Camada 1: Core (Plataforma)**

Skills que gerenciam o sistema:

- `/nevoa` - Orquestrador master
- `/claude-architect` - Guardião de padrões
- `/marie-kondo` - Organização
- `/dashboard` - **NOVO** Monitoramento

#### **Camada 2: Domínio (Especialistas)**

Skills com contexto específico:

- `/pedro` - **NOVO** Pedro Sobral (Tráfego)
- `/lucas` - **NOVO** Lucas Amoedo (DeFi)
- `/alan` - **NOVO** Alan Nicolas (IA)
- `/elena` - **NOVO** Elena Vasquez (Produtividade)
- `/dr-green` - **NOVO** Dr. Green (Cultivo)

#### **Camada 3: Workflows (Orquestrados)**

Skills que combinam múltiplos agentes:

- `/processar-live` - **NOVO** Multi-agente
- `/analise-completa-projeto` - **NOVO** Multi-agente
- `/workflow-comercial` - **NOVO** Multi-agente

#### **Camada 4: Automações (Sistema)**

Hooks e automações invisíveis:

- `auto-checkpoint.sh` - **NOVO** Salva estado ao fechar
- `auto-recovery.sh` - **NOVO** Recupera ao abrir

### Integração com Funcionalidades 2025

```
┌─────────────────────────────────────────────────────────┐
│              SKILLS (Interface Usuário)                  │
└───────────────────────┬─────────────────────────────────┘
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
┌───────────────┐ ┌──────────┐ ┌────────────────┐
│  Background   │ │Parameters│ │  Checkpoints   │
│    Agents     │ │ Dinâmicos│ │   Automáticos  │
└───────┬───────┘ └────┬─────┘ └────────┬───────┘
        │              │                 │
        └──────────────┴─────────────────┘
                       │
                       ▼
        ┌──────────────────────────────┐
        │     TASK TOOL + HOOKS        │
        │  run_in_background=true      │
        │  $ARGUMENTS dinâmicos        │
        │  PostSessionEnd hooks        │
        └──────────────────────────────┘
```

---

## 🔧 ESPECIFICAÇÕES TÉCNICAS

### SPEC 1: Skills de Domínio

#### `/pedro` - Pedro Sobral (Tráfego Pago)

**Arquivo:** `.claude/commands/pedro.md`

**Especificação:**

```yaml
Nome: pedro
Descrição: Ativar contexto Pedro Sobral (Tráfego Pago)
Argumentos: [opcional] "processar M0X A0Y" | "analisar campanha [nome]"
Background: Sim (suporta run_in_background)
Token Limit: ~400 tokens

Contexto Carregado:
  - Framework Pedro Sobral (7 Pilares, Hook Rate)
  - Status curso M02 (progresso atual)
  - Projetos: KabaK, Gabriele
  - Métricas: ROAS, CTR, CPM benchmarks 2025
  - Pasta: Banco_Dados_Trafego_Marcas_Familiares/

Agentes Utilizáveis:
  - Explore (busca conceitos no curso)
  - Plan (planejar campanhas)
  - Code-reviewer (revisar scripts)

Workflows Especiais:
  - Processar aula: extrai conceitos + flashcards + aplicação
  - Analisar campanha: 7 Pilares + métricas + sugestões
  - Testar criativo: Hook Rate + benchmarks

Bloqueios (NÃO MUDAR):
  - Framework Pedro Sobral
  - Metas de ROAS definidas
  - Estrutura de pastas
  - Benchmarks 2025
```

**Template do arquivo:**

````markdown
---
description: Ativar Pedro Sobral (Tráfego Pago)
argument-hint: [opcional] "processar M0X A0Y" | "analisar campanha"
---

# Pedro Sobral - Especialista em Tráfego Pago

Ativa o agente **Pedro Sobral** para trabalhar com tráfego pago e marketing de performance.

## Contexto Carregado

**Framework:**

- 7 Pilares dos Testes Científicos
- Hook Rate (benchmarks 2025)
- Estrutura de campanhas científicas

**Curso:**

- Status: M02 (9/13 aulas completadas)
- Próxima: A10 Rastreamento Elite
- Localização: `Subido_Trafego_3K/`

**Projetos:**

- KabaK (ROAS atual: 2.5x, meta: 4.0x)
- Gabriele Outlet (setup inicial)
- Pasta: `Banco_Dados_Trafego_Marcas_Familiares/`

**Métricas 2025:**

- Hook Rate bom: >3.0s
- CTR bom: >2%
- CPM benchmark: R$15-25

## Comandos Disponíveis

```bash
# Processar aula do curso
/pedro "processar M02 A10"

# Analisar campanha
/pedro "analisar campanha KabaK última"

# Criar teste científico
/pedro "criar teste 7 pilares para produto X"

# Modo background (enquanto trabalha em outra coisa)
/pedro --background "processar M02 A11"
```
````

## Protocolos

**SEMPRE:**

- Aplicar framework Pedro Sobral (7 Pilares)
- Comparar com benchmarks 2025
- Criar flashcards para conceitos novos
- Atualizar progresso do curso
- Salvar análises em Banco_Dados_Trafego_Marcas_Familiares/

**NUNCA:**

- Misturar com outros contextos (DeFi, IA)
- Mudar framework sem justificativa
- Ignorar benchmarks científicos
- Criar estruturas fora do padrão

## NÃO MUDAR

Lista de elementos fixos (bloqueio anti-mudança):

- Framework Pedro Sobral (7 Pilares + Hook Rate)
- Meta ROAS 4.0x para KabaK
- Estrutura Banco_Dados_Trafego_Marcas_Familiares/
- Benchmarks 2025 definidos
- Templates de campanha aprovados

## Workflows Especiais

### Processar Aula

1. Lê aula em `Subido_Trafego_3K/Modulos/M0X/`
2. Extrai conceitos principais
3. Cria flashcards Anki
4. Atualiza status curso
5. Identifica aplicação em projetos
6. Cria plano de ação se aplicável

### Analisar Campanha

1. Lê dados campanha em `Banco_Dados_Trafego_Marcas_Familiares/`
2. Aplica 7 Pilares dos Testes
3. Calcula Hook Rate
4. Compara com benchmarks
5. Sugere melhorias científicas
6. Salva relatório estruturado

## Integração com Outros Agentes

**Pode combinar com:**

- `/alan` - Para criar automações de análise
- `/nevoa` - Para decisões estratégicas
- `/validate` - Para validar estruturas

**NÃO combinar com:**

- `/lucas` (DeFi) - Contextos incompatíveis
- `/dr-green` (Cultivo) - Contextos incompatíveis

````

**Implementação (Fase 1):**
1. Criar arquivo `.claude/commands/pedro.md`
2. Testar carregamento de contexto
3. Validar isolamento (não vaza para outros domínios)
4. Testar modo background
5. Documentar em GUIA_SKILLS_AGENTES.md

#### `/lucas` - Lucas Amoedo (DeFi & Cripto)

**Arquivo:** `.claude/commands/lucas.md`

**Especificação:**
```yaml
Nome: lucas
Descrição: Ativar contexto Lucas Amoedo (DeFi)
Argumentos: [opcional] "analisar token [SYMBOL]" | "processar M04 leva X"
Background: Sim
Token Limit: ~300 tokens

Contexto Carregado:
  - Metodologia Benjamin Graham DeFi
  - Checklist 19 perguntas
  - Arsenal 3 tiers (LIDO, CHAINLINK, UNISWAP, etc)
  - Status M4 (5/10 levas)
  - Pasta: DEFIVERSO_Journey/

Agentes Utilizáveis:
  - Explore (busca tokens/protocolos)
  - Plan (estratégia de investimento)

Workflows Especiais:
  - Análise fundamentalista token
  - Classificação em tier
  - Atualização arsenal
````

**Template:** Similar ao `/pedro`, adaptado para DeFi

#### `/alan` - Alan Nicolas (IA & Automação)

**Arquivo:** `.claude/commands/alan.md`

**Especificação:**

```yaml
Nome: alan
Descrição: Ativar contexto Alan Nicolas (IA)
Argumentos: [opcional] "criar workflow [tipo]" | "processar live [tema]"
Background: Sim
Token Limit: ~500 tokens

Contexto Carregado:
  - Framework 5C (Capturar, Conectar, Criar, Compartilhar)
  - N8N workflows (2056 templates)
  - Prompts biblioteca
  - Status Formação Lendária
  - Projetos: Névoa, AgriIA, Gabriele

Agentes Utilizáveis:
  - Explore (busca workflows/prompts)
  - Plan (arquitetar automações)
  - Code-reviewer (revisar workflows)

Workflows Especiais:
  - Processar live/podcast → nota estruturada
  - Criar workflow N8N
  - Gerar prompts otimizados
```

#### `/elena` - Elena Vasquez (Produtividade & TDAH)

**Arquivo:** `.claude/commands/elena.md`

**Especificação:**

```yaml
Nome: elena
Descrição: Ativar contexto Elena Vasquez (Produtividade)
Argumentos: [opcional] "criar sistema [tipo]" | "otimizar workflow"
Background: Sim
Token Limit: ~350 tokens

Contexto Carregado:
  - Metodologias TDAH-friendly
  - GTD adaptado
  - Timeboxing científico
  - Sistemas de foco

Workflows Especiais:
  - Criar sistema produtividade personalizado
  - Otimizar workflow existente
  - Quebrar projeto em micro-tarefas
```

#### `/dr-green` - Dr. Green (Cultivo Medicinal)

**Arquivo:** `.claude/commands/dr-green.md`

**Especificação:**

```yaml
Nome: dr-green
Descrição: Ativar contexto Dr. Green (Cultivo)
Argumentos: [opcional] "analisar cepa [nome]" | "planejar cultivo"
Background: Sim
Token Limit: ~300 tokens

Contexto Carregado:
  - Técnicas de cultivo
  - Genética e cepas
  - Protocolos de cura
  - Projeto DeFi_Verso_2025 (tangente)

Workflows Especiais:
  - Análise de cepa
  - Planejamento de cultivo
  - Troubleshooting problemas
```

### SPEC 2: Workflows Orquestrados

#### `/processar-live` - Processador Multi-Agente de Lives

**Arquivo:** `.claude/commands/processar-live.md`

**Especificação:**

```yaml
Nome: processar-live
Descrição: Processar live/podcast com múltiplos agentes
Argumentos: OBRIGATÓRIO "fonte [URL/arquivo]" "tema [área]"
Background: Sim (multi-task)
Token Limit: Variável (delega para Gemini)

Workflow:
  1. Gemini 3 Pro: Transcrever + resumir (1M tokens)
  2. Agente domínio (Pedro/Lucas/Alan): Extrair conceitos específicos
  3. Elena: Criar plano implementação TDAH-friendly
  4. Névoa: Consolidar + salvar + checkpoint

Exemplo:
  /processar-live "live_gemini3.mp4" "IA"

  Executa:
  - Gemini: Transcreve vídeo completo
  - Alan: Extrai conceitos IA
  - Elena: Cria plano de 7 dias para aplicar
  - Névoa: Salva tudo estruturado
```

**Template do arquivo:**

```markdown
---
description: Processar live/podcast com multi-agentes
argument-hint: "fonte [URL/arquivo]" "tema [pedro|lucas|alan|elena|dr-green]"
---

# Processar Live - Workflow Multi-Agente

Processa lives, podcasts, vídeos com **múltiplos agentes especializados** trabalhando em paralelo.

## Como Funciona
```

Você: /processar-live "live.mp4" "IA"
↓
[PARALELO - 4 agentes simultâneos]
│
├─> Gemini 3 Pro (background)
│ └─> Transcreve TUDO (1M tokens)
│ Output: transcricao*completa.txt
│
├─> Alan Nicolas (aguarda transcrição)
│ └─> Extrai conceitos IA
│ Output: conceitos_ia.md
│
├─> Elena Vasquez (aguarda conceitos)
│ └─> Cria plano 7 dias TDAH-friendly
│ Output: plano_implementacao.md
│
└─> Névoa (aguarda tudo)
└─> Consolida + salva + checkpoint
Output: Live*[Tema]\_[Data]\_Processada.md

````

## Uso

```bash
# Básico
/processar-live "live.mp4" "IA"
/processar-live "podcast.mp3" "trafego"
/processar-live "https://youtube.com/watch?v=xxx" "defi"

# Com background (não bloqueia)
/processar-live --background "live.mp4" "IA"
````

## Agentes Ativados

Baseado no tema:

| Tema            | Agentes                        | Tempo Estimado |
| --------------- | ------------------------------ | -------------- |
| `ia`            | Gemini + Alan + Elena + Névoa  | ~5 min         |
| `trafego`       | Gemini + Pedro + Elena + Névoa | ~5 min         |
| `defi`          | Gemini + Lucas + Elena + Névoa | ~5 min         |
| `produtividade` | Gemini + Elena + Névoa         | ~3 min         |

## Output Estruturado

```markdown
# Live: [Título] - Processada

## 📊 Resumo Executivo

[Gemini - 3 parágrafos]

## 🎯 Conceitos Principais ([Tema])

[Agente Domínio - Lista estruturada]

## ✅ Plano de Implementação (7 Dias)

[Elena - Plano TDAH-friendly]

## 🔗 Conexões

[Névoa - Links com conhecimento existente]

## 📝 Transcrição Completa

[Gemini - Full text]
```

## Economia

**Sem workflow:**

- Claude lê transcrição: 50k tokens ($2.50)
- Você processa manualmente: 2 horas
- Cria plano: 30 min
- TOTAL: $2.50 + 2.5h

**Com workflow:**

- Gemini transcreve: $0.00
- Agentes processam: automático
- Você recebe pronto: 5 min
- TOTAL: $0.00 + 5 min

**ROI:** 30x mais rápido, 100% mais barato

````

#### `/analise-completa-projeto` - Análise Multi-Dimensional

**Arquivo:** `.claude/commands/analise-completa-projeto.md`

**Especificação:**
```yaml
Nome: analise-completa-projeto
Descrição: Análise 360° de projeto com múltiplos agentes
Argumentos: OBRIGATÓRIO "projeto [nome]"
Background: Sim

Workflow:
  1. Marie Kondo (paralelo): Audita estrutura
  2. Claude Architect (paralelo): Valida padrões
  3. Agente domínio (paralelo): Analisa conteúdo
  4. Névoa (sequencial): Decisões + relatório final

Exemplo:
  /analise-completa-projeto "KabaK"

  Output:
  - Relatório de estrutura (Marie Kondo)
  - Relatório de conformidade (Claude Architect)
  - Análise de performance (Pedro)
  - Decisões e próximos passos (Névoa)
````

#### `/dashboard` - Dashboard de Monitoramento

**Arquivo:** `.claude/commands/dashboard.md`

**Especificação:**

```yaml
Nome: dashboard
Descrição: Dashboard de monitoramento do vault
Argumentos: Nenhum
Background: Não (instantâneo)

Output:
  - Tasks rodando em background (+ progresso)
  - Última sessão (checkpoint)
  - Projetos ativos (status)
  - Cursos em progresso (%)
  - Métricas gerais
  - Sugestões de próximas ações
```

**Template:**

```markdown
---
description: Dashboard de monitoramento do vault
---

# Dashboard - Visão 360°

Mostra status completo do vault em tempo real.

## Output
```

╔════════════════════════════════════════════════════════════╗
║ MEU SEGUNDO CÉREBRO - DASHBOARD ║
╚════════════════════════════════════════════════════════════╝

📊 TASKS EM EXECUÇÃO (Background)
┌────────────────────────────────────────────────────────────┐
│ [1] /pedro --bg "processar M02 A11" [████████░░] 80% │
│ [2] /alan --bg "criar workflow IG" [██████░░░░] 60% │
└────────────────────────────────────────────────────────────┘

🕐 ÚLTIMA SESSÃO
┌────────────────────────────────────────────────────────────┐
│ Contexto: Tráfego Pago (Pedro) │
│ Ação: Analisada campanha KabaK │
│ Próximo: Testar 3 criativos novos │
│ Timestamp: 30/12/2025 14:32 │
└────────────────────────────────────────────────────────────┘

📂 PROJETOS ATIVOS
┌────────────────────────────────────────────────────────────┐
│ [1] KabaK (Tráfego) ⚡ Ativo ROAS: 2.5→4.0x │
│ [2] Gabriele (E-commerce) 🟡 Pausado Setup: 60% │
│ [3] DeFi_Verso_2025 ⚡ Ativo Tokens: 12 │
│ [4] Névoa 3.0 (IA) 🟢 Completo v3.0 │
└────────────────────────────────────────────────────────────┘

📚 CURSOS EM PROGRESSO
┌────────────────────────────────────────────────────────────┐
│ Pedro Sobral M02 [█████████░] 90% (A10/A13) │
│ Lucas Amoedo M04 [█████░░░░░] 50% (Leva 5/10) │
│ Alan Nicolas S03 [███████░░░] 70% (Semana 7/10) │
└────────────────────────────────────────────────────────────┘

📈 MÉTRICAS GERAIS
┌────────────────────────────────────────────────────────────┐
│ Arquivos vault: 1.847 │
│ Tokens sessão média: 512 (↓ 90% vs baseline) │
│ Skills ativas: 18 │
│ Checkpoints: 47 │
│ Última sincronização: 2 horas atrás │
└────────────────────────────────────────────────────────────┘

💡 SUGESTÕES
┌────────────────────────────────────────────────────────────┐
│ [1] Processar A11 M02 Pedro (próxima aula) │
│ [2] Testar criativos KabaK (análise pronta) │
│ [3] Atualizar arsenal DeFi (2 tokens novos detectados) │
└────────────────────────────────────────────────────────────┘

⌨️ AÇÕES RÁPIDAS
/pedro /lucas /alan /elena /processar-live /sync

````

## Uso

```bash
# Mostrar dashboard
/dashboard

# Dashboard + sugestão de próxima ação
/dashboard --next

# Dashboard minimalista (só tasks + última sessão)
/dashboard --minimal
````

````

### SPEC 3: Checkpoints Automáticos

#### Auto-Checkpoint (Ao Fechar Sessão)

**Arquivo:** `scripts/auto-checkpoint.sh`

**Especificação:**
```yaml
Trigger: PostSessionEnd hook
Função: Salvar estado ao fechar Claude Code

Workflow:
  1. Detecta skill ativa (qual contexto estava usando)
  2. Lê arquivos modificados (git status)
  3. Identifica última ação realizada
  4. Determina próximos passos sugeridos
  5. Salva em SESSION_LOG.md
  6. Cria checkpoint em 00_SISTEMA/CHECKPOINTS/AUTO_[DATA].md

Formato SESSION_LOG.md:
  - Data/hora
  - Contexto ativo (skill)
  - Ações realizadas
  - Arquivos modificados
  - Próximos passos
  - Lista NÃO MUDAR
  - Mensagem para próxima sessão
````

**Implementação (PowerShell para Windows):**

```powershell
# auto-checkpoint.ps1

# Detectar skill ativa (via arquivo temporário .claude_active_skill)
$activeSkill = Get-Content ".claude_active_skill" -ErrorAction SilentlyContinue

# Git status (arquivos modificados)
$modifiedFiles = git status --short

# Timestamp
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$dateTag = Get-Date -Format "ddMMMyyyy"

# Construir entrada SESSION_LOG
$logEntry = @"
### 🔵 Claude Code - $timestamp
**Contexto ativo:** $activeSkill
**Ações realizadas:**
- [Extrair de histórico da sessão - TBD]

**Arquivos modificados:**
$modifiedFiles

**Próximos passos sugeridos:**
- [Detectar automaticamente - TBD]

**Estado do vault:**
- Sincronização OK
- Checkpoints atualizados

**Mensagem para próxima sessão:**
> Continuar de onde parou
"@

# Append em SESSION_LOG.md
Add-Content -Path "SESSION_LOG.md" -Value "`n$logEntry"

# Criar checkpoint AUTO
$checkpointPath = "00_SISTEMA/CHECKPOINTS/AUTO_$dateTag.md"
Copy-Item "STATUS_VAULT.md" -Destination $checkpointPath

Write-Host "✅ Checkpoint automático criado: $checkpointPath"
```

**Configuração em `.claude/settings.local.json`:**

```json
{
  "hooks": {
    "PostSessionEnd": [
      {
        "matcher": "*",
        "hooks": [
          {
            "type": "command",
            "command": "powershell -ExecutionPolicy Bypass -File scripts/auto-checkpoint.ps1"
          }
        ]
      }
    ]
  }
}
```

#### Auto-Recovery (Ao Abrir Sessão)

**Arquivo:** `scripts/auto-recovery.sh`

**Especificação:**

```yaml
Trigger: PreSessionStart hook
Função: Recuperar estado ao abrir Claude Code

Workflow: 1. Lê SESSION_LOG.md (última entrada)
  2. Identifica contexto anterior
  3. Verifica lista NÃO MUDAR
  4. Apresenta resumo ao usuário
  5. Pergunta se quer continuar ou mudar contexto
  6. Carrega skill apropriada
```

**Implementação:**

```powershell
# auto-recovery.ps1

# Ler última entrada SESSION_LOG.md
$lastEntry = Get-Content "SESSION_LOG.md" | Select-Object -Last 20

# Extrair contexto ativo
$context = $lastEntry | Select-String "Contexto ativo:" | Select-Object -First 1

# Mostrar resumo
Write-Host @"
╔════════════════════════════════════════════════════════════╗
║                 BEM-VINDO DE VOLTA!                         ║
╚════════════════════════════════════════════════════════════╝

📋 ÚLTIMA SESSÃO
$lastEntry

Deseja continuar de onde parou? (S/N)
"@

# [Interação com usuário - TBD na integração real]
```

### SPEC 4: Parâmetros Dinâmicos

**Todas as skills de domínio aceitam argumentos:**

```bash
# Sem argumentos: carrega contexto genérico
/pedro

# Com argumentos: executa ação específica
/pedro "processar M02 A11"
/pedro "analisar campanha KabaK"
/pedro "criar teste 7 pilares produto X"

# Background
/pedro --background "processar M02 A11"
```

**Implementação no skill:**

```markdown
# pedro.md

## Instructions

1. **Parse arguments**
   - Se `$ARGUMENTS` vazio: carregar contexto genérico
   - Se `$ARGUMENTS` = "processar M0X A0Y": workflow processar aula
   - Se `$ARGUMENTS` = "analisar campanha [nome]": workflow análise

2. **Execute ação apropriada**

3. **Atualizar progresso**
```

---

## 🗓️ ROADMAP DE IMPLEMENTAÇÃO

### FASE 1: Skills de Domínio (Semana 1-2)

**Objetivo:** Criar skills para todos agentes de domínio

**Tasks:**

- [ ] Criar `/pedro` (Tráfego)
  - [ ] Escrever `.claude/commands/pedro.md`
  - [ ] Testar carregamento contexto
  - [ ] Validar isolamento (não vaza)
  - [ ] Testar argumentos dinâmicos
  - [ ] Testar modo background
  - [ ] Documentar em GUIA_SKILLS_AGENTES.md

- [ ] Criar `/lucas` (DeFi)
  - [ ] Similar ao pedro

- [ ] Criar `/alan` (IA)
  - [ ] Similar ao pedro

- [ ] Criar `/elena` (Produtividade)
  - [ ] Similar ao pedro

- [ ] Criar `/dr-green` (Cultivo)
  - [ ] Similar ao pedro

**Critérios de Sucesso:**

- [ ] 5 skills novas funcionando
- [ ] Isolamento 100% (zero confusão entre domínios)
- [ ] Economia de tokens validada (>80%)
- [ ] Modo background testado e funcional

**Tempo estimado:** 7-10 dias
**Risco:** Baixo (incremento simples)

---

### FASE 2: Checkpoints Automáticos (Semana 3)

**Objetivo:** Implementar sincronização automática

**Tasks:**

- [ ] Criar `scripts/auto-checkpoint.ps1`
  - [ ] Detectar skill ativa
  - [ ] Capturar arquivos modificados
  - [ ] Atualizar SESSION_LOG.md
  - [ ] Criar checkpoint AUTO

- [ ] Criar `scripts/auto-recovery.ps1`
  - [ ] Ler SESSION_LOG.md
  - [ ] Mostrar resumo
  - [ ] Carregar contexto anterior

- [ ] Configurar hooks `.claude/settings.local.json`
  - [ ] PostSessionEnd → auto-checkpoint
  - [ ] PreSessionStart → auto-recovery

- [ ] Testar ciclo completo
  - [ ] Trabalhar → Fechar → Abrir → Recuperar

**Critérios de Sucesso:**

- [ ] 100% continuidade entre sessões
- [ ] Zero perda de contexto
- [ ] Auto-checkpoint funciona sem intervenção
- [ ] Lista NÃO MUDAR bloqueia mudanças

**Tempo estimado:** 5-7 dias
**Risco:** Médio (integração sistema)

---

### FASE 3: Workflows Orquestrados (Semana 4-5)

**Objetivo:** Criar workflows multi-agente

**Tasks:**

- [ ] Criar `/processar-live`
  - [ ] Workflow: Gemini + Agente + Elena + Névoa
  - [ ] Testar em paralelo
  - [ ] Validar output estruturado

- [ ] Criar `/analise-completa-projeto`
  - [ ] Workflow: Marie Kondo + Architect + Domínio + Névoa
  - [ ] Testar sequenciamento

- [ ] Criar `/workflow-comercial`
  - [ ] Workflow: Briefing → Gemini → Claude → Output

- [ ] Testar performance paralela
  - [ ] Medir ganho de velocidade
  - [ ] Validar economia de tokens

**Critérios de Sucesso:**

- [ ] 3 workflows funcionando
- [ ] Velocidade 5x em tarefas complexas
- [ ] Output de qualidade consistente

**Tempo estimado:** 10-14 dias
**Risco:** Alto (complexidade orquestração)

---

### FASE 4: Dashboard (Semana 6)

**Objetivo:** Criar visibilidade de tasks e status

**Tasks:**

- [ ] Criar `/dashboard`
  - [ ] Monitorar tasks background
  - [ ] Mostrar última sessão
  - [ ] Listar projetos/cursos
  - [ ] Calcular métricas
  - [ ] Gerar sugestões

- [ ] Integrar com STATUS_VAULT.md
- [ ] Integrar com SESSION_LOG.md
- [ ] Testar atualização em tempo real

**Critérios de Sucesso:**

- [ ] Dashboard mostra status preciso
- [ ] Tasks em background visíveis
- [ ] Sugestões relevantes

**Tempo estimado:** 5-7 dias
**Risco:** Baixo (feature standalone)

---

### FASE 5: Refinamento (Semana 7-8)

**Objetivo:** Otimizar e documentar tudo

**Tasks:**

- [ ] Otimizar economia de tokens
  - [ ] Medir consumo real
  - [ ] Ajustar contextos

- [ ] Criar documentação completa
  - [ ] Guia de uso para cada skill
  - [ ] Troubleshooting
  - [ ] Best practices

- [ ] Treinar usuário
  - [ ] Sessão prática
  - [ ] Testes reais

- [ ] Criar vídeos/tutoriais (opcional)

**Critérios de Sucesso:**

- [ ] Documentação completa
- [ ] Usuário confortável com sistema
- [ ] Economia de tokens atingida (90%)

**Tempo estimado:** 7-10 dias
**Risco:** Baixo (polimento)

---

### TIMELINE GERAL

```
Semana 1-2:  FASE 1 - Skills Domínio        [██████████]
Semana 3:    FASE 2 - Checkpoints Auto      [█████]
Semana 4-5:  FASE 3 - Workflows Orquestrados[██████████]
Semana 6:    FASE 4 - Dashboard             [█████]
Semana 7-8:  FASE 5 - Refinamento           [██████████]

TOTAL: 8 semanas (~2 meses)
```

---

## 💰 ANÁLISE DE ROI

### Investimento

**Tempo de implementação:**

- Desenvolvimento: 40-50 horas (8 semanas × 5-6h/semana)
- Testes: 10-15 horas
- Documentação: 5-10 horas
- **TOTAL:** 55-75 horas

**Custo de oportunidade:**

- Usando Claude Code para implementar: ~$50-100 (tokens)
- Tempo pessoal: 55-75h × valor/hora

### Retorno

**Economia de tokens (mensal):**

```
Antes: ~5000 tokens/sessão × 30 sessões = 150k tokens/mês
Depois: ~500 tokens/sessão × 30 sessões = 15k tokens/mês

Economia: 135k tokens/mês = 90%

Em $: ~$70/mês economizados (assumindo $0.50 per 1k tokens)
```

**Ganho de produtividade:**

```
Tarefas complexas (processamento de lives, análises):
Antes: 2-3 horas por tarefa
Depois: 15-30 minutos por tarefa

Ganho: 5-10x mais rápido

Valor mensal:
- 10 tarefas complexas/mês
- 2.5h economizadas por tarefa
- 25 horas economizadas/mês

Em valor: 25h × $X/hora = $$$
```

**Ganho de continuidade:**

```
Antes: ~30% de contexto perdido entre sessões
  → Tempo gasto re-explicando: ~15 min/sessão
  → 30 sessões × 15 min = 7.5 horas/mês perdidas

Depois: 0% perda de contexto
  → 7.5 horas economizadas/mês
```

### ROI Total (Primeiro Ano)

**Investimento:** 55-75 horas (one-time)

**Retorno mensal:**

- Economia tokens: $70
- Economia tempo (produtividade): 25h
- Economia contexto: 7.5h
- **TOTAL:** $70 + 32.5h/mês

**Retorno anual:**

- $840 (tokens)
- 390 horas (produtividade)

**ROI:**

```
Payback period: ~2 meses
ROI 12 meses: 600-800% (dependendo do valor/hora)
```

---

## ⚠️ RISCOS E MITIGAÇÕES

### RISCO 1: Complexidade de Orquestração

**Descrição:** Workflows multi-agente podem falhar em sequenciamento

**Probabilidade:** Média
**Impacto:** Alto

**Mitigação:**

- Começar com workflows simples (1-2 agentes)
- Testar exaustivamente antes de adicionar mais agentes
- Implementar logs detalhados
- Criar fallback para modo sequencial se paralelo falhar

### RISCO 2: Hooks Não Funcionam no Windows

**Descrição:** PowerShell hooks podem não executar corretamente

**Probabilidade:** Baixa
**Impacto:** Alto

**Mitigação:**

- Testar hooks em ambiente isolado primeiro
- Criar versão fallback manual (`/sync` mantido como backup)
- Documentar troubleshooting
- Considerar versão Node.js se PowerShell falhar

### RISCO 3: Confusão Entre Contextos

**Descrição:** Agentes podem vazar contexto entre domínios

**Probabilidade:** Média
**Impacto:** Médio

**Mitigação:**

- Testes rigorosos de isolamento
- Lista NÃO MUDAR em cada skill
- Validação automática de contexto
- Alertas quando mistura detectada

### RISCO 4: Economia de Tokens Não Atingida

**Descrição:** Skills podem não reduzir tokens como esperado

**Probabilidade:** Baixa
**Impacto:** Baixo

**Mitigação:**

- Medir tokens ANTES de implementar (baseline)
- Medir tokens DEPOIS de cada fase
- Ajustar contextos conforme necessário
- Meta: >80% já seria sucesso

### RISCO 5: Usuário Não Adota Sistema

**Descrição:** Sistema pode ser complexo demais para uso diário

**Probabilidade:** Baixa
**Impacto:** Alto

**Mitigação:**

- Manter skills antigas funcionando (transição gradual)
- Criar guias práticos e exemplos
- Sessão de treinamento hands-on
- Dashboard mostra valor claramente

---

## 📊 MÉTRICAS DE SUCESSO

### Métricas Técnicas

| Métrica                      | Baseline | Meta | Método de Medição            |
| ---------------------------- | -------- | ---- | ---------------------------- |
| Tokens/sessão média          | 5000     | <500 | Tracking manual + logs       |
| Velocidade tarefas complexas | 1x       | 5x   | Cronometrar antes/depois     |
| Continuidade contexto        | 30%      | 100% | % sessões sem re-explicar    |
| Skills disponíveis           | 11       | 20+  | Contagem `.claude/commands/` |
| Isolamento contextos         | 60%      | 100% | Testes de confusão           |

### Métricas de Uso

| Métrica                    | Meta Semana 4 | Meta Semana 8 |
| -------------------------- | ------------- | ------------- |
| Skills usadas/dia          | 3-5           | 5-10          |
| Tasks background/dia       | 1-2           | 3-5           |
| Checkpoints automáticos    | 100%          | 100%          |
| Sessões sem perda contexto | 80%           | 100%          |

### Métricas de Qualidade

| Métrica               | Método              |
| --------------------- | ------------------- |
| Satisfação usuário    | Escala 1-10 semanal |
| Bugs encontrados      | Tracking de issues  |
| Tempo troubleshooting | Horas/semana        |

---

## 🚀 PRÓXIMOS PASSOS

### Imediato (Hoje)

1. **Aprovação do plano**
   - [ ] Revisar este documento
   - [ ] Aprovar roadmap
   - [ ] Aprovar investimento de tempo

2. **Setup inicial**
   - [ ] Criar pasta `scripts/`
   - [ ] Backup completo do vault
   - [ ] Git commit antes de começar

### Semana 1 (Dias 1-7)

1. **Segunda-feira**
   - [ ] Criar `/pedro` skill
   - [ ] Testar contexto tráfego

2. **Terça-feira**
   - [ ] Criar `/lucas` skill
   - [ ] Testar contexto DeFi

3. **Quarta-feira**
   - [ ] Criar `/alan` skill
   - [ ] Testar contexto IA

4. **Quinta-feira**
   - [ ] Criar `/elena` skill
   - [ ] Testar contexto produtividade

5. **Sexta-feira**
   - [ ] Criar `/dr-green` skill
   - [ ] Testar todos skills em paralelo
   - [ ] Validar isolamento

6. **Fim de semana**
   - [ ] Documentar resultados
   - [ ] Preparar FASE 2

### Pergunta para Você

**Você quer:**

A) **Começar implementação agora** (Fase 1 - Skill `/pedro`)
B) **Revisar/ajustar o plano primeiro** (discutir detalhes)
C) **Ver prova de conceito** (implementar 1 skill completa para validar)
D) **Outra abordagem** (especificar)

---

**Criado:** 30/12/2025
**Autor:** Claude Sonnet 4.5 (Claude Architect)
**Status:** ✅ Pronto para Aprovação
**Próximo:** Aguardando decisão do usuário
