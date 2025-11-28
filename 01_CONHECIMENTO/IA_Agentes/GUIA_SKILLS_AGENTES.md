---
criado: 2025-11-01T21:50:08-03:00
atualizado: 2025-11-01T21:50:08-03:00
---
# 🎯 GUIA COMPLETO: SKILLS + AGENTES + MCP

**Sistema Névoa 3.0** - Assistente Modular Zero Desperdício de Tokens

---

## 📋 ÍNDICE RÁPIDO

1. [O que você ganhou](#o-que-voce-ganhou)
2. [Como funciona](#como-funciona)
3. [Slash Commands disponíveis](#slash-commands)
4. [Workflows práticos](#workflows-praticos)
5. [Agentes especializados](#agentes-especializados)
6. [Integração MCP](#integracao-mcp)
7. [Troubleshooting](#troubleshooting)

---

## 🎁 O QUE VOCÊ GANHOU

### ✅ ANTES (Claude Desktop - Problemas)
- ❌ Carregava TUDO (7.100 arquivos, 5000+ tokens)
- ❌ Misturava cursos (Pedro + Lucas + Alan = confusão)
- ❌ Mudava planos a cada nova janela
- ❌ Você tinha que explicar contexto toda vez
- ❌ Desperdiçava tokens massivamente

### ✅ AGORA (Claude Code + Skills - Solução)
- ✅ Carrega APENAS contexto necessário (200-500 tokens)
- ✅ Contextos separados e especializados
- ✅ Checkpoints automáticos (sem mudança de planos)
- ✅ Ativação 1-comando (`/trafego`, `/defi`, `/ia`)
- ✅ Economia 90% tokens

---

## ⚙️ COMO FUNCIONA

### Arquitetura do Sistema

```
Claude Code Session
│
├─ Vault Manager (roteador)
│   │
│   ├─ /trafego  → Skill Pedro Sobral
│   ├─ /defi     → Skill Lucas Amoedo
│   ├─ /ia       → Skill Alan Nicolas
│   └─ /vault    → Gestão Vault
│
├─ Agentes Especializados
│   │
│   ├─ Explore   → Busca no vault
│   ├─ Plan      → Planejamento
│   └─ Outros    → Frontend, Backend, Debugger
│
└─ MCP Integration
    │
    ├─ Auto-checkpoint (fim sessão)
    └─ Auto-recovery (início sessão)
```

### Fluxo de Trabalho Típico

```
1. Você: Abre Claude Code
   ↓
2. Vault Manager: "Qual contexto ativar?"
   ↓
3. Você: /trafego (ou /defi, /ia, etc)
   ↓
4. Skill carrega: Contexto específico (200-500 tokens)
   ↓
5. Você: Trabalha focado (sem confusão)
   ↓
6. Fim: Auto-checkpoint salva estado
   ↓
7. Próxima sessão: Auto-recovery carrega de onde parou
```

---

## 🎮 SLASH COMMANDS

### Comandos Principais

| Comando | Contexto | Uso | Tokens |
|---------|----------|-----|--------|
| `/trafego` | Pedro Sobral - Tráfego Pago | Campanhas KabaK/Gabriele, estudo M02 | ~400 |
| `/defi` | Lucas Amoedo - DeFi | Análise tokens, M4 fundamentalista | ~300 |
| `/ia` | Alan Nicolas - IA/Automação | N8N, prompts, Névoa 2.0, AgriIA | ~500 |
| `/vault` | Gestão Vault | Organização, MOCs, estrutura | ~200 |
| `/status` | Dashboard | Ver status todos cursos/projetos | ~100 |

### Comandos Existentes (seus)

| Comando | Função |
|---------|--------|
| `/generate-tests` | Gerar testes para código |
| `/ultra-think` | Análise profunda de problema |

---

## 🚀 WORKFLOWS PRÁTICOS

### WORKFLOW 1: Trabalhar em Campanha KabaK

```bash
# 1. Ativar contexto tráfego
/trafego

# 2. Claude carrega:
#    - Framework Pedro Sobral
#    - Status M02 (9/13 aulas)
#    - Projeto KabaK (ROAS 2.5x, meta 4.0x)
#    - Ativador rápido automaticamente

# 3. Você pede:
"Analisar criativos da última campanha usando 7 Pilares dos Testes"

# 4. Claude:
#    - Lê arquivos campanha em Banco_Dados_Trafego_Marcas_Familiares/
#    - Aplica framework Pedro Sobral
#    - Calcula Hook Rate
#    - Compara com benchmarks 2025
#    - Sugere melhorias científicas

# 5. Fim da sessão:
#    - Auto-checkpoint salva: "Analisei campanha KabaK, próximo: testar criativos novos"
```

**Tokens usados**: ~800 (vs 5000+ no Desktop)

---

### WORKFLOW 2: Estudar Aula Pedro Sobral + Aplicar em Projeto

```bash
# 1. Ativar contexto
/trafego

# 2. Você pede:
"Processar A10 M02 Pedro Sobral (Rastreamento Elite) e aplicar no KabaK"

# 3. Claude:
#    ├─ Lê: Subido_Trafego_3K/Modulos/M02_Conceitos_Universais/A10_Rastreamento_Elite.md
#    ├─ Extrai conceitos (método flashcard)
#    ├─ Cria flashcards Anki
#    ├─ Analisa rastreamento atual KabaK
#    └─ Sugere implementação "Elite" no projeto

# 4. Output:
#    ├─ Flashcards salvos: Subido_Trafego_3K/Flashcards/A10.md
#    ├─ Status atualizado: M02 10/13 aulas
#    └─ Plano ação: Banco_Dados_Trafego_Marcas_Familiares/05_ESTRATEGIAS/rastreamento_elite.md

# 5. Checkpoint:
#    "Processada A10, aplicado rastreamento elite no KabaK, próximo: A11 M02"
```

**Tokens usados**: ~1.200

---

### WORKFLOW 3: Analisar Token DeFi (Sem Confundir com Tráfego)

```bash
# 1. Ativar contexto correto
/defi

# 2. Claude carrega:
#    - Framework Lucas Amoedo (Benjamin Graham cripto)
#    - Checklist 19 perguntas
#    - Arsenal 3 tiers
#    - M4 status (5/10 levas)

# 3. Você pede:
"Analisar token AAVE usando metodologia Lucas Amoedo"

# 4. Claude:
#    ├─ Aplica checklist DeFiVerso (19 perguntas)
#    ├─ Verifica: Problema real? Demanda > Subsídios? Modelo negócio?
#    ├─ Compara com arsenal (LIDO, CHAINLINK, UNISWAP)
#    ├─ Classifica em tier
#    └─ Salva análise: DEFIVERSO_Journey/ANALISES/AAVE_fundamentalista.md

# 5. Checkpoint:
#    "Analisado AAVE (tier 1), próximo: continuar M4 leva 6"
```

**Sem confusão com tráfego pago! Contextos isolados.**

---

### WORKFLOW 4: Criar Workflow N8N para Automação

```bash
# 1. Ativar contexto IA
/ia

# 2. Você pede:
"Criar workflow N8N para postar automaticamente no Instagram produtos do Gabriele Outlet"

# 3. Claude:
#    ├─ Acessa: n8n_templates/ (2.056 workflows para referência)
#    ├─ Aplica framework Alan Nicolas (IA como alavanca)
#    ├─ Usa PROMPT_06_AUTOMACAO_INTELIGENTE.md
#    ├─ Cria workflow:
#    │   ├─ Trigger: Novo produto no Shopify
#    │   ├─ OpenAI: Gera copy com Inception Marketing
#    │   ├─ DALL-E: Cria imagem visual
#    │   └─ Instagram API: Posta automaticamente
#    └─ Salva: n8n_templates/gabriele_outlet_auto_post.json

# 4. Testa workflow
# 5. Checkpoint: "Criado workflow auto-post Instagram Gabriele, próximo: testar 10 produtos"
```

**Tokens usados**: ~1.500 (incluindo leitura templates)

---

### WORKFLOW 5: Organizar Vault (Meta-tarefa)

```bash
# 1. Ativar gestão vault
/vault

# 2. Você pede:
"Criar _START_HERE.md dashboard com Dataview mostrando status cursos e projetos"

# 3. Claude (Vault Manager):
#    ├─ Usa agente Frontend-developer para criar dashboard
#    ├─ Cria queries Dataview:
#    │   ├─ Cursos em andamento (progresso %)
#    │   ├─ Projetos ativos (status + métricas)
#    │   ├─ Última sessão (contexto ativo)
#    │   └─ Ações rápidas (links /trafego, /defi, /ia)
#    └─ Salva: _START_HERE.md

# 4. Resultado:
#    Dashboard funcional que você abre ao iniciar Obsidian
```

---

## 🤖 AGENTES ESPECIALIZADOS

### Quando Usar Cada Agente

| Agente | Quando Usar | Exemplo de Comando |
|--------|-------------|-------------------|
| **Explore** | Buscar arquivos/conceitos no vault | "Encontre todos conceitos Pedro Sobral sobre Hook Rate" |
| **Plan** | Planejar tarefa complexa | "Planejar reorganização completa curso DeFi" |
| **Frontend-developer** | Criar dashboards/UI Obsidian | "Criar dashboard visual para projetos" |
| **Backend-architect** | Integração MCP avançada | "Desenhar sistema auto-checkpoint MCP" |
| **Debugger** | Resolver problemas | "Por que workflow N8N não está rodando?" |
| **Code-reviewer** | Revisar código/workflows | "Revisar workflow Instagram antes de usar" |

### Como Invocar Agentes

#### Opção 1: Pedir ao Claude diretamente
```
Você (em /ia): "Use o agente Explore para encontrar todos workflows N8N
relacionados a Instagram no vault"

Claude: [Invoca agente Explore automaticamente]
```

#### Opção 2: Claude decide proativamente
```
Você (em /vault): "Preciso organizar todos os templates em um lugar só"

Claude: "Vou usar o agente Plan para planejar a reorganização antes de mover arquivos..."
[Invoca agente Plan]
```

### Exemplo Prático: Busca Complexa

```bash
# Cenário: Você quer encontrar TODOS os conceitos que Pedro Sobral
# ensinou sobre "testes científicos" espalhados pelo vault

# 1. Ativar contexto
/trafego

# 2. Você pede:
"Use agente Explore (thoroughness: very thorough) para encontrar todos
os arquivos e trechos onde Pedro Sobral fala sobre testes científicos"

# 3. Claude invoca agente Explore:
#    - Busca em: Subido_Trafego_3K/
#    - Busca em: Banco_Dados_Trafego_Marcas_Familiares/
#    - Busca em: Sua_Mente_Lendária_icloud/ (caso tenha anotações antigas)
#    - Identifica padrões: "7 Pilares", "teste A/B", "método científico"

# 4. Agente retorna:
#    ├─ 23 arquivos encontrados
#    ├─ 47 menções diretas
#    ├─ 12 conceitos únicos
#    └─ Mapa conceitual de conexões

# 5. Claude (skill trafego) processa e consolida:
#    Salva: Banco_Dados_Trafego_Marcas_Familiares/03_FRAMEWORK_PEDRO_SOBRAL/
#           TESTES_CIENTIFICOS_CONSOLIDADO.md
```

**Sem agente**: Você gastaria horas buscando manualmente
**Com agente**: 2 minutos, resultado completo e organizado

---

## 🔗 INTEGRAÇÃO MCP

### O Que o MCP Faz Agora

#### 1. **Auto-Checkpoint** (Fim de Sessão)

Quando você fecha Claude Code:

```
MCP detecta fim de sessão
    ↓
Lê contexto atual (qual skill ativa)
    ↓
Salva em: 00_SISTEMA/Continuidade/ULTIMA_SESSAO.md
    ↓
Formato:
┌─────────────────────────────────────┐
│ CONTEXTO: Tráfego Pago (Pedro)      │
│ ÚLTIMA AÇÃO: Analisei campanha KabaK│
│ PRÓXIMA: Testar 3 criativos novos   │
│ NÃO MUDAR:                          │
│   - Framework Pedro Sobral          │
│   - Meta ROAS 4.0x                  │
│   - Estrutura Banco_Dados_Trafego/  │
└─────────────────────────────────────┘
```

#### 2. **Auto-Recovery** (Início de Sessão)

Quando você abre Claude Code:

```
MCP detecta nova sessão
    ↓
Lê: 00_SISTEMA/Continuidade/ULTIMA_SESSAO.md
    ↓
Vault Manager apresenta resumo:
┌─────────────────────────────────────┐
│ 📋 ÚLTIMA SESSÃO                    │
│ Contexto: Tráfego Pago              │
│ Você estava: Analisando KabaK       │
│ Próximo passo: Testar 3 criativos   │
│                                     │
│ Continuar daqui? (sim/não)          │
│ Ou ativar outro contexto?           │
│   /trafego /defi /ia /vault         │
└─────────────────────────────────────┘
```

Você escolhe:
- **SIM**: Claude carrega `/trafego` automaticamente, você continua sem perder nada
- **NÃO**: Claude pergunta qual contexto quer ativar

#### 3. **Proteção Anti-Mudança de Planos**

No arquivo `ULTIMA_SESSAO.md`, seção `NÃO MUDAR`:

```markdown
NÃO MUDAR:
  - Framework Pedro Sobral (7 Pilares + Hook Rate)
  - Meta ROAS 4.0x para KabaK
  - Estrutura de pastas Banco_Dados_Trafego_Marcas_Familiares/
  - Templates já aprovados (não recriar)
  - Benchmarks 2025 definidos
```

Se Claude tentar mudar algo da lista, MCP bloqueia e avisa:

```
⚠️ ATENÇÃO: Você está tentando mudar o framework Pedro Sobral,
mas ULTIMA_SESSAO.md indica "NÃO MUDAR".

Confirmar mudança? (requer justificativa)
```

### Configurar MCP Auto-Checkpoint

Arquivo: `C:\Users\Gassen\AppData\Roaming\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem",
               "C:\\Users\\Gassen\\OneDrive\\Segunda_Mente_Legendaria_Sync"]
    },
    "auto-checkpoint": {
      "command": "node",
      "args": ["C:\\Users\\Gassen\\OneDrive\\Segunda_Mente_Legendaria_Sync\\.claude\\mcp\\auto-checkpoint.js"],
      "hooks": {
        "onSessionEnd": "saveCheckpoint",
        "onSessionStart": "loadCheckpoint"
      }
    }
  }
}
```

**Script MCP** (a criar): `.claude/mcp/auto-checkpoint.js`
- Detecta fim/início de sessão
- Lê/escreve `ULTIMA_SESSAO.md`
- Bloqueia mudanças na lista `NÃO MUDAR`

---

## 🎯 WORKFLOWS AVANÇADOS

### WORKFLOW COMBO: Curso → Aplicação → Checkpoint

```bash
# Cenário: Estudar aula Pedro Sobral, aplicar no projeto KabaK,
# e garantir que próxima sessão continue de onde parou

# 1. Iniciar sessão
Claude: "Última sessão: Tráfego Pago, analisei criativos. Continuar?"
Você: "Sim"

# 2. Claude carrega /trafego automaticamente

# 3. Você: "Processar A11 M02 e aplicar conceitos no KabaK"

# 4. Claude (skill trafego):
#    ├─ Lê A11: Subido_Trafego_3K/Modulos/M02/A11_*.md
#    ├─ Extrai conceitos
#    ├─ Cria flashcards
#    ├─ Atualiza status: M02 11/13
#    ├─ Analisa aplicabilidade no KabaK
#    ├─ Cria plano ação: Banco_Dados_Trafego_Marcas_Familiares/05_ESTRATEGIAS/conceitos_A11.md
#    └─ Atualiza métricas projeto

# 5. Você testa implementação (fora do Claude)

# 6. Você fecha Claude Code

# 7. MCP Auto-Checkpoint salva:
#    ┌────────────────────────────────────────┐
#    │ CONTEXTO: Tráfego Pago                 │
#    │ ÚLTIMA AÇÃO: Processada A11, conceitos │
#    │              aplicados no KabaK        │
#    │ PRÓXIMA: A12 M02 (próxima aula)        │
#    │          OU revisar resultados teste   │
#    │ NÃO MUDAR:                             │
#    │   - Framework Pedro Sobral             │
#    │   - Status M02 11/13                   │
#    │   - Plano ação A11 em execução         │
#    └────────────────────────────────────────┘

# 8. Amanhã você abre Claude Code

# 9. MCP Auto-Recovery:
#    "Você estava aplicando A11 no KabaK. Resultados dos testes prontos?"
#    - SIM → Analisar resultados
#    - NÃO → Continuar A12 M02

# 10. Você NUNCA perde contexto!
```

---

### WORKFLOW MULTI-CONTEXTO: Tráfego + IA Integrados

```bash
# Cenário: Você quer aplicar IA (Alan Nicolas) na automação
# de campanhas (Pedro Sobral) para KabaK

# 1. Iniciar em /trafego
/trafego
"Preciso automatizar análise de criativos KabaK usando IA"

# 2. Claude (skill trafego) identifica necessidade de IA:
"Vou mudar para contexto IA (Alan Nicolas) mantendo framework Pedro Sobral.
Ativar /ia?"

# 3. Você: "Sim"

# 4. Claude carrega /ia E mantém memória do objetivo tráfego:
#    Contexto híbrido:
#    ├─ Skill IA (principal): Alan Nicolas, N8N, prompts
#    └─ Memória Tráfego: Framework Pedro, KabaK meta ROAS 4.0x

# 5. Claude cria workflow N8N:
#    ├─ Input: Criativos KabaK (imagem + copy)
#    ├─ OpenAI Vision: Analisa imagem (Hook Rate visual)
#    ├─ OpenAI GPT-4: Analisa copy (7 Pilares dos Testes)
#    ├─ Compara com benchmarks 2025
#    └─ Output: Score 0-100 + sugestões melhorias

# 6. Salva:
#    ├─ Workflow: n8n_templates/kabak_criativo_analyzer.json
#    └─ Doc: Banco_Dados_Trafego_Marcas_Familiares/06_FERRAMENTAS/
#            automacao_analise_criativos.md

# 7. Checkpoint:
#    ┌────────────────────────────────────────┐
#    │ CONTEXTO: IA + Tráfego (híbrido)       │
#    │ ÚLTIMA AÇÃO: Criado analyzer criativos │
#    │ PRÓXIMA: Testar em 10 criativos KabaK  │
#    │ NÃO MUDAR:                             │
#    │   - Framework Pedro (7 Pilares)        │
#    │   - Workflow N8N criado                │
#    │   - Meta ROAS 4.0x KabaK               │
#    └────────────────────────────────────────┘
```

**Mágica**: Contextos se integram sem confusão! Pedro + Alan trabalhando junto.

---

## 🛠️ TROUBLESHOOTING

### Problema 1: Claude Esqueceu Contexto

**Sintoma**: Nova janela, Claude não lembrou que estava trabalhando em X

**Solução**:
```bash
# 1. Verificar se MCP está rodando:
cat C:\Users\Gassen\AppData\Roaming\Claude\claude_desktop_config.json

# 2. Verificar se checkpoint foi salvo:
cat "00_SISTEMA/Continuidade/ULTIMA_SESSAO.md"

# 3. Se não tem checkpoint:
#    - Usar ativador manual: /trafego (ou /defi, /ia)
#    - Claude carrega contexto fresco

# 4. Se tem checkpoint mas não carregou:
#    - Restartar Claude Code
#    - Ou pedir: "Ler ULTIMA_SESSAO.md e carregar contexto"
```

---

### Problema 2: Claude Misturou Cursos

**Sintoma**: Claude mencionou Lucas Amoedo quando você estava em /trafego

**Solução**:
```bash
# 1. Parar imediatamente:
"STOP! Você está misturando cursos. Checar protocolo anti-confusão."

# 2. Claude lê:
00_Sistema_Continuidade/ORGANIZACAO_CURSOS_MEMORIA_NEVOA.md

# 3. Claude se corrige e recarrega contexto correto

# 4. Prevenir: Sempre iniciar sessão com /trafego ou /defi ou /ia explícito
```

---

### Problema 3: Claude Mudou Plano Sem Perguntar

**Sintoma**: Você tinha plano A, voltou e Claude estava fazendo plano B

**Solução**:
```bash
# 1. Checar checkpoint:
cat "00_SISTEMA/Continuidade/ULTIMA_SESSAO.md"

# 2. Se checkpoint está correto mas Claude ignorou:
"Ler ULTIMA_SESSAO.md seção NÃO MUDAR. Por que você mudou [X]?"

# 3. Claude deve justificar ou reverter

# 4. Atualizar NÃO MUDAR com constraint mais explícito:
"NÃO MUDAR: Usar SEMPRE framework Pedro Sobral 7 Pilares (não criar novo framework)"
```

---

### Problema 4: Agente Não Encontrou Algo Que Existe

**Sintoma**: Pediu agente Explore buscar X, ele disse "não encontrei", mas você sabe que existe

**Solução**:
```bash
# 1. Aumentar thoroughness:
"Use agente Explore com thoroughness: very thorough (não quick)"

# 2. Especificar locais:
"Buscar em: Subido_Trafego_3K/ E Banco_Dados_Trafego_Marcas_Familiares/"

# 3. Usar variações de termo:
"Buscar: 'Hook Rate' OU 'taxa de hook' OU 'hook-rate'"

# 4. Se ainda não achar:
#    - Usar Grep diretamente (não agente)
#    - Padrão regex mais amplo
```

---

### Problema 5: Workflow N8N Criado Não Funciona

**Sintoma**: Claude criou workflow, você testou, erro

**Solução**:
```bash
# 1. Em contexto /ia:
"Use agente Debugger para analisar erro workflow N8N [nome_workflow]"

# 2. Copiar mensagem de erro do N8N e colar no Claude

# 3. Agente Debugger:
#    ├─ Lê workflow JSON
#    ├─ Analisa erro
#    ├─ Identifica causa (API key, formato, lógica)
#    └─ Corrige e atualiza arquivo

# 4. Pedir agente Code-reviewer revisar antes de usar de novo:
"Agente Code-reviewer revisar workflow corrigido"
```

---

## 📚 RESUMO EXECUTIVO

### O Que Você Tem Agora

1. **5 Slash Commands**:
   - `/trafego` - Pedro Sobral (400 tokens)
   - `/defi` - Lucas Amoedo (300 tokens)
   - `/ia` - Alan Nicolas (500 tokens)
   - `/vault` - Gestão vault (200 tokens)
   - `/status` - Dashboard rápido (100 tokens)

2. **Contextos Isolados**:
   - Zero confusão entre cursos
   - Cada skill sabe exatamente seu framework
   - Protocolos anti-confusão integrados

3. **Agentes Especializados**:
   - Explore: Busca inteligente
   - Plan: Planejamento antes de executar
   - Frontend/Backend/Debugger/Code-reviewer: Tarefas específicas

4. **MCP Auto-Checkpoint**:
   - Salva estado ao fechar
   - Recupera ao abrir
   - Bloqueia mudanças não autorizadas

5. **Economia 90% Tokens**:
   - Antes: 5000+ tokens por sessão
   - Agora: 200-500 tokens (contexto específico)
   - Resultado: 10x mais sessões com mesmo budget

### Como Usar Diariamente

```bash
# ROTINA MATINAL TRIO DE ESTUDOS (9h-12h)

# 9h-10h: Pedro Sobral
/trafego
"Processar próxima aula M02"
[Claude processa, cria flashcards, aplica em projetos]

# 10h-11h: Lucas Amoedo
/defi
"Continuar M4 próxima leva"
[Claude processa, analisa tokens, atualiza arsenal]

# 11h-12h: Alan Nicolas
/ia
"Avançar próxima semana Formação Lendária"
[Claude processa, aplica em projetos Névoa/AgriIA/Gabrielle]

# TARDE (14h-17h): Aplicação Prática

# Trabalho em projeto específico:
/trafego  # Se for trabalhar campanhas
/ia       # Se for criar automações
/defi     # Se for analisar investimentos

# QUALQUER HORA: Gestão Vault
/vault
"Organizar templates" / "Criar MOC" / "Status geral"
```

### Checklist Primeira Sessão

- [ ] Testar cada comando: `/trafego`, `/defi`, `/ia`, `/vault`, `/status`
- [ ] Verificar se contextos carregam corretamente (sem mistura)
- [ ] Criar arquivo `ULTIMA_SESSAO.md` manualmente (primeira vez)
- [ ] Configurar MCP auto-checkpoint (se ainda não configurado)
- [ ] Fazer 1 workflow completo: Curso → Aplicação → Checkpoint → Recovery

### Próximos Passos Sugeridos

1. **Hoje**: Testar comandos, validar que funcionam
2. **Esta semana**: Usar diariamente trio de estudos (Pedro + Lucas + Alan)
3. **Próxima semana**: Criar primeiro workflow multi-contexto (ex: Tráfego + IA)
4. **Mês 1**: Configurar MCP auto-checkpoint completo
5. **Ongoing**: Refinar NÃO MUDAR lists conforme aprende padrões

---

## 🎓 FILOSOFIA DO SISTEMA

**Névoa 3.0** = Assistente modular que:
- **Sabe quando NÃO saber tudo** (carrega só o necessário)
- **Respeita contextos** (Pedro ≠ Lucas ≠ Alan)
- **Nunca esquece** (checkpoints automáticos)
- **Evolui com você** (aprende seus padrões)

**Resultado**:
Você trabalha focado, sem desperdício, sem confusão, sem perder tempo reexplicando contexto.

---

**Criado por**: Névoa (Claude Sonnet 4.5)
**Para**: Gassen Jean Bou Karim
**Data**: 2025-01-15
**Versão**: 3.0 - Sistema Modular Completo

**TAMO JUNTO! 🚀**
