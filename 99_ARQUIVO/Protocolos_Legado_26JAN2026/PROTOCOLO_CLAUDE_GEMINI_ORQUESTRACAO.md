# PROTOCOLO: Orquestração Claude + Gemini

**Status**: ✅ Active
**Criado**: 14/Jan/2026
**Versão**: 2.0 (Arquitetura Real)

---

## 🏗️ Arquitetura do Sistema

### Setup Real

```
🌌 ANTIGRAVITY (IDE/Terminal Principal)
│
├─── 🧠 CLAUDE SONNET 4.5 (Terminal)
│    │
│    ├── Capacidade: 200k tokens
│    ├── Custo: Pago (Pro/Teams)
│    ├── Acesso: Via terminal no Antigravity
│    │
│    └── ESPECIALIDADE: Cérebro do Sistema
│         ├── 🎯 Decisões estratégicas
│         ├── 🏗️ Arquitetura de código
│         ├── ✏️ Edições precisas de arquivos
│         ├── 🎨 Design de soluções
│         ├── 🔍 Code review crítico
│         └── 🎭 Orquestração geral
│
└─── 🤖 GEMINI 3 PRO (Agente Integrado)
     │
     ├── Capacidade: 1M tokens (5x mais!)
     ├── Custo: GRATUITO
     ├── Acesso: Nativo no Antigravity
     │
     └── ESPECIALIDADE: Assistente de Processamento
          ├── 📚 Ler múltiplos arquivos (volume)
          ├── 🔬 Análises extensas
          ├── 📊 Gerar relatórios longos
          ├── 🔄 Processar dados massivos
          ├── 🌐 GitHub API (Issues, PRs, etc)
          ├── 📖 Documentação volumosa
          ├── 🗂️ Catalogação de arquivos
          └── 💾 Backup e sincronização
```

---

## 🎯 Divisão de Responsabilidades

### 🧠 CLAUDE (Você é o CÉREBRO)

**Use Claude para:**

✅ **Decisões Estratégicas**
```bash
# Exemplo:
"Qual a melhor estrutura para organizar este projeto?"
"Como devo arquitetar esta feature?"
"Este código está seguindo as melhores práticas?"
```

✅ **Código Preciso**
```bash
# Exemplo:
"Edite o arquivo X para adicionar feature Y"
"Refatore esta função seguindo padrão Z"
"Corrija o bug no arquivo W linha 42"
```

✅ **Arquitetura**
```bash
# Exemplo:
"Crie estrutura de pastas para novo projeto"
"Design a integração entre X e Y"
"Planeje implementação de feature Z"
```

✅ **Code Review Crítico**
```bash
# Exemplo:
"Revise se este PR segue os padrões do vault"
"Analise se há problemas de segurança neste código"
"Verifique se a nomenclatura está correta"
```

✅ **Orquestração**
```bash
# Exemplo:
"Delegue para Gemini analisar todos os arquivos de cultivo"
"Coordene backup semanal com Gemini"
"Passe contexto X para Gemini processar"
```

---

### 🤖 GEMINI (ASSISTENTE de Alto Volume)

**Use Gemini para:**

✅ **Leitura Massiva**
```bash
# Exemplo:
"Leia todos os 50 arquivos da pasta X e me dê resumo"
"Analise todo o histórico do repositório (1000 commits)"
"Processe todos os checkpoints e extraia padrões"
```

✅ **Análises Extensas**
```bash
# Exemplo:
"Analise 6 meses de commits e gere relatório de produtividade"
"Compare todos os MOCs e identifique inconsistências"
"Audite todo o vault buscando arquivos duplicados"
```

✅ **Geração de Conteúdo Volumoso**
```bash
# Exemplo:
"Gere documentação completa de 100 páginas do projeto"
"Crie índice detalhado de todo o vault (2000 arquivos)"
"Transcreva e organize 10 horas de áudio/vídeo"
```

✅ **GitHub API Operations**
```bash
# Exemplo:
"Crie 20 Issues baseadas no backlog"
"Analise todos os PRs dos últimos 6 meses"
"Gere relatório de todas as releases"
```

✅ **Catalogação e Organização**
```bash
# Exemplo:
"Cataloge todos os 2000 arquivos do vault"
"Reorganize estrutura baseado em padrões"
"Crie mapa completo de relações entre arquivos"
```

---

## 🔄 Sistema de Handoff (Passagem de Bastão)

### Cenário 1: Claude → Gemini (Delegar Processamento)

**Quando:** Você precisa processar volume alto que gastaria muitos tokens Claude

**Como fazer:**

**1. No Claude (você):**
```
Vou precisar que o Gemini processe isso. Prepare contexto.
```

**2. Claude prepara contexto:**
```markdown
# CONTEXTO PARA GEMINI

## Tarefa
[Descrição clara da tarefa]

## Arquivos Relevantes
- arquivo1.md (path completo)
- arquivo2.md (path completo)

## Padrões a Seguir
- NOMENCLATURA.md
- ESTRUTURA_PROJETOS.md

## Output Esperado
[Formato específico]

## Entrega
Salvar em: [path específico]
```

**3. Você copia e cola no Gemini:**
```
[Cole o contexto preparado pelo Claude]

Processe conforme instruído e me avise quando terminar.
```

**4. Gemini processa e entrega**

**5. De volta ao Claude para validar:**
```
Gemini completou. Revise o output em [path] e valide.
```

---

### Cenário 2: Gemini → Claude (Decisão Estratégica)

**Quando:** Gemini encontrou algo que precisa decisão humana + expertise do Claude

**Como fazer:**

**1. No Gemini (detectou problema):**
```
Encontrei inconsistência em 15 arquivos.
Preciso de decisão estratégica do Claude.

Prepare resumo executivo:
- O que encontrou
- Opções possíveis
- Recomendação
```

**2. Gemini gera resumo:**
```markdown
# RESUMO PARA CLAUDE

## Problema Identificado
[Descrição concisa]

## Arquivos Afetados
[Lista dos 15 arquivos]

## Opções
1. Opção A - [prós e contras]
2. Opção B - [prós e contras]
3. Opção C - [prós e contras]

## Recomendação Gemini
[Sugestão com justificativa]

## Ação Requerida
Decisão sobre qual caminho seguir
```

**3. Você copia para Claude:**
```
[Cole o resumo do Gemini]

Analise e decida qual caminho seguir.
```

**4. Claude decide:**
```
Decisão: Seguir Opção B

Instruções para Gemini:
[Passos específicos para executar]
```

**5. Você passa instruções de volta ao Gemini**

---

## 📋 Workflows Otimizados

### Workflow 1: Análise Completa do Vault

**Tarefa:** Analisar todos os 2000+ arquivos do vault

**❌ ERRADO (Gastar tokens Claude):**
```bash
# No Claude:
"Leia todos os arquivos do vault e analise"
# ⚠️ Vai gastar 150k+ tokens!
```

**✅ CERTO (Usar Gemini):**

**1. No Claude:**
```
Vou delegar análise massiva para Gemini.

Contexto a passar:
- Analisar todos os arquivos do vault
- Identificar: duplicados, órfãos, mal nomeados
- Gerar relatório seguindo NOMENCLATURA.md
- Salvar em 00_SISTEMA/RELATORIOS/AUDITORIA_VAULT_[DATA].md
```

**2. No Gemini:**
```
Analise TODOS os arquivos do vault em:
C:\Users\gasse\OneDrive\Meu_Segundo_Cerebro

Para cada arquivo:
1. Verificar nomenclatura (NOMENCLATURA.md)
2. Verificar localização (ESTRUTURA_PROJETOS.md)
3. Detectar duplicados
4. Identificar órfãos (sem links)

Gere relatório completo em:
00_SISTEMA/RELATORIOS/AUDITORIA_VAULT_14JAN2026.md

Formato:
## 📊 Auditoria Completa do Vault

### Estatísticas Gerais
- Total arquivos: X
- Arquivos OK: Y
- Problemas encontrados: Z

### 🐛 Problemas por Categoria
[Detalhes]

### ✅ Recomendações
[Lista priorizada]
```

**3. Gemini processa (usando 1M tokens se necessário)**

**4. De volta ao Claude:**
```
Gemini completou auditoria.
Revise relatório e priorize ações corretivas.
```

---

### Workflow 2: Criar Feature Complexa

**Tarefa:** Implementar nova feature que toca vários arquivos

**✅ Divisão Inteligente:**

**1. PLANEJAMENTO (Claude - 10k tokens)**
```bash
# No Claude:
"Preciso implementar feature X.

Analise:
- Arquivos que precisam ser modificados
- Nova estrutura necessária
- Padrões a seguir
- Plano de implementação

Gere plano detalhado."
```

**2. PESQUISA DE CONTEXTO (Gemini - 100k tokens)**
```bash
# No Gemini:
"Leia os seguintes 20 arquivos relacionados:
[lista de arquivos]

Extraia:
- Padrões de código usados
- Nomenclatura seguida
- Estruturas similares
- Referências cruzadas

Gere documento de contexto para Claude implementar."
```

**3. IMPLEMENTAÇÃO (Claude - 30k tokens)**
```bash
# No Claude (com contexto do Gemini):
"Com base no contexto fornecido, implemente feature X:

[Código preciso, edições específicas]
```

**4. VALIDAÇÃO (Gemini - 50k tokens)**
```bash
# No Gemini:
"Valide implementação:
- Todos os arquivos seguem padrões?
- Links entre arquivos funcionam?
- MOCs foram atualizados?
- Nomenclatura OK?

Gere relatório de validação."
```

**5. REFINAMENTO (Claude - 10k tokens)**
```bash
# No Claude:
"Baseado na validação do Gemini, corrija:
[Ajustes finos]
```

**Total:** 50k Claude + 150k Gemini = ✅ Otimizado!

---

### Workflow 3: Documentação Massiva

**Tarefa:** Documentar todo um projeto grande

**✅ Divisão:**

**1. ESTRUTURA (Claude - 5k tokens)**
```
Defina estrutura da documentação do projeto X:
- Seções principais
- Ordem lógica
- Templates a usar
```

**2. CONTEÚDO (Gemini - 200k tokens)**
```
Gere documentação completa seguindo estrutura:
- Leia todos os arquivos do projeto
- Extraia informações relevantes
- Escreva seções completas
- Adicione exemplos
- Cross-references

Gere documento de 50+ páginas.
```

**3. REVIEW (Claude - 15k tokens)**
```
Revise documentação gerada por Gemini:
- Qualidade técnica
- Precisão
- Completude
- Aderência aos padrões

Corrija problemas críticos.
```

**4. POLISH (Gemini - 50k tokens)**
```
Aplique correções do Claude:
[Lista de correções]

Gere versão final.
```

---

### Workflow 4: Sincronização Multi-Dispositivo

**Cenário:** Você trabalhou no iPhone, agora está no Desktop

**✅ Divisão:**

**1. DETECÇÃO (Gemini - 10k tokens)**
```bash
# No Gemini (automatizado):
"Verifique repositório GitHub:
- Branches do iPhone (claude/*)
- Commits novos no master
- Conflitos potenciais

Gere relatório de sincronização."
```

**2. ESTRATÉGIA (Claude - 5k tokens)**
```bash
# No Claude:
"Baseado no relatório do Gemini, qual estratégia:
- Merge direto
- Rebase
- Cherry-pick
- Resolver conflitos

Decida e instrua."
```

**3. EXECUÇÃO (Claude - 10k tokens)**
```bash
# No Claude:
git pull origin master
git merge origin/claude/BRANCH
# Resolver conflitos se necessário
git push origin master
```

**4. VALIDAÇÃO (Gemini - 20k tokens)**
```bash
# No Gemini:
"Valide sincronização:
- Todos os commits mesclados?
- Sem perda de dados?
- Histórico limpo?
- Branches antigas limpas?

Gere checklist de pós-sync."
```

---

## 🎭 Casos de Uso Práticos

### Caso 1: "Preciso Organizar 500 Notas Antigas"

**❌ Tentação:** Pedir pro Claude ler tudo (gastaria 80k tokens)

**✅ Estratégia Otimizada:**

1. **Gemini lê as 500 notas** (100k tokens dele, grátis)
2. **Gemini categoriza e sugere estrutura**
3. **Claude revisa estrutura** (5k tokens) e decide
4. **Gemini executa reorganização** (50k tokens dele)
5. **Claude valida sample** (10k tokens)

**Você:** 15k tokens gastos ✅
**Resultado:** 500 notas organizadas!

---

### Caso 2: "Implementar Sistema de Tags"

**✅ Estratégia:**

1. **Claude:** Design do sistema (5k)
2. **Gemini:** Analisa todos os arquivos e sugere tags (150k dele)
3. **Claude:** Aprova/ajusta taxonomia (5k)
4. **Gemini:** Aplica tags em 2000 arquivos (200k dele)
5. **Claude:** Valida amostra aleatória (10k)

**Você:** 20k tokens ✅
**Gemini:** 350k tokens (grátis!) ✅

---

### Caso 3: "Revisar Semana de Trabalho"

**✅ Estratégia:**

1. **Gemini:** Lê todos os commits da semana + GitHub (50k dele)
2. **Gemini:** Gera relatório detalhado (30k dele)
3. **Claude:** Analisa relatório e dá insights estratégicos (10k)
4. **Claude:** Define prioridades para próxima semana (5k)

**Você:** 15k tokens ✅

---

## 🔧 Comandos e Patterns

### Pattern: "Prepare Contexto"

**No Claude:**
```
Prepare contexto para Gemini processar:

Tarefa: [X]
Arquivos: [Y]
Padrões: [Z]
Output: [W]
```

Claude gera markdown estruturado que você copia para Gemini.

---

### Pattern: "Resumo Executivo"

**No Gemini:**
```
Após processar, gere resumo executivo para Claude:

Máximo 500 palavras com:
- Principais descobertas
- Decisões necessárias
- Recomendações

Formato otimizado para tokens do Claude.
```

---

### Pattern: "Validação por Amostragem"

**No Claude (após Gemini processar 1000 arquivos):**
```
Gemini processou 1000 arquivos.

Selecione amostra aleatória de 10 arquivos.
Valide qualidade do processamento.
Se OK, aprove todo o lote.
```

Economiza tokens validando amostra em vez de tudo.

---

## 📊 Economia de Tokens

### Exemplo Real: Auditoria Completa do Vault

**❌ Só Claude:**
- Ler 2000 arquivos: ~150k tokens
- Analisar: ~30k tokens
- Gerar relatório: ~20k tokens
- **Total: 200k tokens (LIMITE!)**

**✅ Claude + Gemini:**
- Claude planeja (5k tokens)
- Gemini lê e analisa 2000 arquivos (300k tokens dele, grátis)
- Claude revisa resumo (10k tokens)
- Claude decide ações (5k tokens)
- **Total Claude: 20k tokens ✅**
- **Gemini: 300k tokens (grátis) ✅**

**Economia:** 90% dos tokens Claude!

---

## 🎯 Matriz de Decisão

| Tarefa | Tokens | Complexidade | Decisão | Usa Quem |
|--------|--------|--------------|---------|----------|
| Ler 1 arquivo | <1k | Baixa | Rápida | Claude |
| Ler 100 arquivos | ~50k | Média | - | Gemini |
| Editar código | <5k | Alta | Crítica | Claude |
| Catalogar vault | ~200k | Baixa | - | Gemini |
| Arquitetar feature | ~10k | Alta | Crítica | Claude |
| Gerar relatório 50pg | ~100k | Baixa | - | Gemini |
| Code review | ~5k | Alta | Crítica | Claude |
| GitHub API ops | ~10k | Média | - | Gemini |
| Decisão estratégica | ~5k | Alta | Crítica | Claude |
| Processar dados | ~100k | Baixa | - | Gemini |

**Regra de Ouro:**
- **Alto volume + Baixa complexidade** = Gemini
- **Baixo volume + Alta complexidade** = Claude
- **Decisões críticas** = SEMPRE Claude

---

## 🚀 Workflow Diário Otimizado

### Manhã (Desktop)

**1. Gemini Check (5 min - grátis)**
```bash
# No Gemini:
"Verifique sincronização:
- GitHub branches do iPhone
- Commits novos
- Issues/PRs pendentes
Gere relatório matinal."
```

**2. Claude Strategy (2 min - 5k tokens)**
```bash
# No Claude:
"Baseado no relatório Gemini:
- Prioridades do dia
- Estratégia de sync
- Ordem de tarefas"
```

**3. Execute (Gemini + Claude alternando)**

---

### Noite (Desktop)

**1. Gemini Review (10 min - grátis)**
```bash
# No Gemini:
"Analise trabalho do dia:
- O que foi feito
- Commits realizados
- Arquivos modificados
Gere relatório diário."
```

**2. Claude Reflect (5 min - 5k tokens)**
```bash
# No Claude:
"Baseado no relatório:
- Qualidade do código
- Padrões seguidos
- Melhorias para amanhã
- Ações pendentes"
```

**3. Commit & Push (Claude)**

---

## 📚 Scripts Úteis

### Script: Handoff Context

**Salve em: `00_SISTEMA/SCRIPTS/handoff_context.md`**

```markdown
# HANDOFF: Claude → Gemini

## Tarefa
[Descrição em 1 frase]

## Contexto
[Background necessário]

## Arquivos
[Lista com paths completos]

## Padrões
- NOMENCLATURA.md: [pontos relevantes]
- ESTRUTURA_PROJETOS.md: [pontos relevantes]

## Output Esperado
- Formato: [markdown/json/csv]
- Localização: [path completo]
- Estrutura: [template se necessário]

## Validação
- [ ] [Critério 1]
- [ ] [Critério 2]

## Entrega
Notificar quando completo com resumo de:
- O que foi processado
- Problemas encontrados
- Decisões que precisam de Claude
```

---

### Script: Executive Summary

**Salve em: `00_SISTEMA/SCRIPTS/executive_summary.md`**

```markdown
# SUMMARY: Gemini → Claude

## Tarefa Completada
[Nome da tarefa]

## Processamento
- Arquivos lidos: X
- Tempo: Y minutos
- Tokens usados: Z

## Principais Descobertas
1. [Descoberta 1]
2. [Descoberta 2]
3. [Descoberta 3]

## Decisões Necessárias
1. [Decisão 1] - Opções: A, B, C
2. [Decisão 2] - Opções: X, Y, Z

## Recomendações Gemini
[Top 3 recomendações priorizadas]

## Output
- Arquivo: [path]
- Tamanho: [linhas/páginas]
- Status: ✅ Completo / ⚠️ Parcial / ❌ Bloqueado

## Próximos Passos Sugeridos
1. [Passo 1]
2. [Passo 2]
```

---

## 🎓 Lições Aprendidas

### 1. **Claude é Caro, Gemini é Grátis**
- Use Gemini para volume
- Reserve Claude para expertise

### 2. **Contexto É Rei**
- Sempre prepare contexto estruturado
- Summaries executivos economizam tokens

### 3. **Validação por Amostragem**
- Não valide tudo item por item
- Amostra aleatória é suficiente

### 4. **Handoff Estruturado**
- Templates reduzem tokens
- Formato consistente acelera

### 5. **Gemini Pode Errar Mais**
- 1M tokens grátis = menos precisão
- Claude valida decisões críticas

---

## 🔗 Referências

- `PROTOCOLO_GITHUB_MULTI_DISPOSITIVO.md`
- `PROTOCOLO_ANTIGRAVITY_GITHUB.md`
- `PROTOCOLO_SINCRONIZACAO_AGENTES.md`
- `SESSION_LOG.md`
- `.gemini/GEMINI.md`

---

## 🎯 Resumo Executivo

```
🧠 CLAUDE = CÉREBRO
   - Decisões estratégicas
   - Código preciso
   - Arquitetura
   - 200k tokens (economize!)

🤖 GEMINI = ASSISTENTE
   - Processamento massivo
   - Análises volumosas
   - GitHub API
   - 1M tokens (use à vontade!)

🌌 ANTIGRAVITY = ORQUESTRADOR
   - Hospeda ambos
   - Facilita handoff
   - Integra ferramentas
```

**Regra de Ouro:**
> **Gemini processa, Claude decide.**

---

**🤖 Generated with Claude Code**
**Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>**
