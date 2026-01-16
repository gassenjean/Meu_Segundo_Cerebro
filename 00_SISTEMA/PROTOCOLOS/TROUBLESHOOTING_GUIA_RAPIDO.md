# TROUBLESHOOTING: Guia Rápido

**Soluções para Problemas Comuns do Vault**

**Criado:** 16/Jan/2026
**Versão:** 1.0
**Consolidou:** GUIA_RAPIDO_ERRO_OVERLOAD.md + GUIA_RECUPERACAO_ERRO_GEMINI.md
**Propósito:** Resolver 90% dos problemas em <5 minutos

---

## 🎯 NAVEGAÇÃO RÁPIDA (30 SEGUNDOS)

**Qual é o seu problema?**

```
┌─────────────────────────────────────────────────────────┐
│ CLAUDE: Erro "Model Provider Overload"                 │
└─────────────────────┬───────────────────────────────────┘
                      ▼
                  CATEGORIA 1


┌─────────────────────────────────────────────────────────┐
│ GEMINI: Token limit, execution terminated, etc         │
└─────────────────────┬───────────────────────────────────┘
                      ▼
                  CATEGORIA 2


┌─────────────────────────────────────────────────────────┐
│ SINCRONIZAÇÃO: Logs desatualizados, conflitos PC/IA    │
└─────────────────────┬───────────────────────────────────┘
                      ▼
                  CATEGORIA 3


┌─────────────────────────────────────────────────────────┐
│ PADRÕES: Arquivo no lugar errado, nome incorreto       │
└─────────────────────┬───────────────────────────────────┘
                      ▼
                  CATEGORIA 4


┌─────────────────────────────────────────────────────────┐
│ MOCs: Esqueci atualizar, links quebrados               │
└─────────────────────┬───────────────────────────────────┘
                      ▼
                  CATEGORIA 5


┌─────────────────────────────────────────────────────────┐
│ PERFORMANCE: Vault lento, Claude lento, overload       │
└─────────────────────┬───────────────────────────────────┘
                      ▼
                  CATEGORIA 6
```

---

## 📚 ÍNDICE

1. [Overload Contexto (Claude)](#categoria-1-overload-contexto-claude)
2. [Erros Gemini](#categoria-2-erros-gemini)
3. [Sincronização](#categoria-3-sincronizacao)
4. [Padrões/Nomenclatura](#categoria-4-padroes-nomenclatura)
5. [MOCs/Integração](#categoria-5-mocs-integracao)
6. [Performance](#categoria-6-performance)

---

## CATEGORIA 1: Overload Contexto (Claude)

### Problema: "Model Provider Overload"

**Sintoma:**
- Mensagem: "Agent execution terminated due to model provider overload"
- Claude não responde
- Timeout ao iniciar
- Erro ao trocar modelo

**Causa:**
- Claude Sonnet 4.5 (API) está sobrecarregado
- Muitos usuários simultâneos
- Horário de pico

### Solução IMEDIATA

#### Opção 1: Aguardar e Tentar Novamente (Recomendado)

```
1. ⏸️ Aguardar 5 minutos
2. 🔄 Tentar trocar para Sonnet 4.5 novamente
3. ✅ Se funcionar: Continuar trabalho
4. ❌ Se falhar: Ir para Opção 2
```

#### Opção 2: Usar Gemini Temporariamente

```
1. 🟣 Delegar para Gemini (tarefas de processamento)
2. 📝 Fazer a tarefa atual
3. 💾 Documentar no SESSION_LOG
4. ⏰ Tentar Claude novamente em 15-30 min
```

#### Opção 3: Agendar para Depois

```
1. 📅 Anotar tarefa pendente
2. ⏰ Processar em horário alternativo:
   - Madrugada (0h-6h)
   - Fim de semana
   - Horários fora de pico
3. ✅ Maior taxa de sucesso
```

### Horários

**PICO (mais erros):**
- 🔴 Segunda a Sexta: 9h-18h
- 🔴 Início da manhã: 8h-10h
- 🔴 Após almoço: 13h-15h

**MELHORES (menos erros):**
- 🟢 Madrugada: 0h-6h
- 🟢 Fim de semana
- 🟢 Noite: 22h-0h

### Estratégia Híbrida (Recomendada)

```
1. Tentar Claude Sonnet 4.5
   ├─ Funcionou? → Usar Claude
   └─ Falhou?
      ├─ Aguardar 5 min
      ├─ Tentar novamente
      │  ├─ Funcionou? → Usar Claude
      │  └─ Falhou?
      │     ├─ Usar Gemini (fallback)
      │     ├─ Documentar SESSION_LOG
      │     └─ Tentar Claude depois
```

### Template Documentação

**Adicionar ao SESSION_LOG.md:**

```markdown
### 🔵 Claude Code - [DATA] ([HORA])

**FALLBACK: Claude Overload**

**Ações realizadas:**
- ⚠️ Claude Sonnet 4.5 indisponível (model provider overload)
- ✅ Tarefa delegada para Gemini: [Descrição]
- 📝 Arquivos: [Lista]

**Próximos passos:**
- [ ] Tentar Claude novamente em [Horário]
- [ ] Retomar tarefas estratégicas quando disponível

**Mensagem para Gemini:**
> Claude indisponível temporariamente.
> Execute [tarefa] e me reporte quando finalizar.
```

### Checklist Rápido

- [ ] Aguardei 5 minutos?
- [ ] Tentei novamente?
- [ ] Se persistiu: Usei Gemini?
- [ ] Documentei no SESSION_LOG?
- [ ] Agendei retry para depois?

### Regra de Ouro

**NÃO ficar tentando repetidamente!**

```
❌ ERRADO:
Tentar → Erro → Tentar → Erro → Tentar → Erro...

✅ CORRETO:
Tentar → Erro → Aguardar 5min → Tentar → Erro → Usar Gemini → Tentar depois
```

---

## CATEGORIA 2: Erros Gemini

### Erro 2.1: Token Limit Exceeded

**Sintoma:**
- Mensagem: "Token limit exceeded"
- Processamento interrompido
- Resposta truncada

**Causa:**
- Arquivo muito grande processado de uma vez
- Muitos arquivos sem checkpoint
- Tentou fazer demais em uma sessão

**Solução:**

1. **PARAR** processamento imediatamente
2. **IDENTIFICAR** último checkpoint válido
3. **REPORTAR** para Claude via SESSION_LOG
4. **AGUARDAR** estratégia de recuperação
5. **REPROCESSAR** com lotes menores

**Exemplo:**
```markdown
## 🟣 Gemini - 16/01/2026 (14:30)

**ERRO: Token Limit Exceeded**

**Arquivo problemático:** WORKFLOWS_SUMMARY.md (149KB)
**Último checkpoint:** CHECKPOINT_LOTE2.md (10 arquivos OK)
**Trabalho perdido:** 1 arquivo

**Aguardando orientação de Claude para divisão.**
```

### Erro 2.2: Agent Execution Terminated

**Sintoma:**
- Mensagem: "Agent execution terminated due to error"
- Processo completamente parado
- Não consegue continuar

**Causa:**
- Erro crítico no código
- Timeout
- Memória esgotada
- Arquivo corrompido

**Solução:**

1. **IDENTIFICAR** o que estava fazendo
2. **IDENTIFICAR** último checkpoint válido
3. **REPORTAR** erro completo para Claude
4. **NÃO** tentar reprocessar sem orientação
5. **AGUARDAR** Claude investigar

### Erro 2.3: File Not Found / Access Denied

**Sintoma:**
- Arquivo não encontrado
- Sem permissão de acesso
- Caminho inválido

**Causa:**
- Arquivo foi movido/deletado
- Caminho errado
- Permissões de sistema

**Solução:**

1. **DOCUMENTAR** arquivo problemático
2. **MARCAR** como "NÃO PROCESSADO - Erro de acesso"
3. **CONTINUAR** com próximos arquivos
4. **REPORTAR** lista ao final

### Erro 2.4: Encoding / Corruption

**Sintoma:**
- Caracteres estranhos
- Arquivo ilegível
- Erro de parsing

**Causa:**
- Encoding diferente (não UTF-8)
- Arquivo corrompido
- Formato inesperado

**Solução:**

1. **TENTAR** encoding alternativo (Latin-1, Windows-1252)
2. Se falhar: **DOCUMENTAR** problema
3. **MARCAR** como "CORROMPIDO - Intervenção manual"
4. **CONTINUAR** com próximos
5. **REPORTAR** ao final

### Erro 2.5: Model Provider Overload (Gemini)

**Sintoma:**
- Mensagem: "Model provider overload"
- Gemini 3 Pro não responde
- Timeout na inicialização

**Causa:**
- Gemini 3 Pro (gratuito) está sobrecarregado
- Muitos usuários simultâneos
- Limite de requisições atingido
- Horário de pico

**Solução:**

**Opção 1: Retry com Backoff**
```
1. Aguardar 2-5 minutos
2. Tentar novamente
3. Se falhar: Aguardar 10-15 minutos
4. Tentar novamente
5. Se persistir: Opção 2
```

**Opção 2: Fallback Claude**
```
1. Usar Claude para tarefas CRÍTICAS
2. Documentar trabalho feito
3. Tentar Gemini depois
4. Quando Gemini voltar: Retomar processamento
```

**Opção 3: Horário Alternativo**
```
1. Identificar horário de pico (9h-18h)
2. Agendar para madrugada/fim de semana
3. Processar em lotes menores
4. Maior taxa de sucesso
```

### Protocolo Recuperação (Gemini)

#### PASSO 1: Parar e Respirar

**NÃO:**
- ❌ Entrar em pânico
- ❌ Tentar "consertar" rapidamente
- ❌ Recomeçar do zero
- ❌ Ignorar o erro

**SIM:**
- ✅ Pausar processamento
- ✅ Ler este guia
- ✅ Seguir protocolo
- ✅ Comunicar Claude

#### PASSO 2: Identificar Checkpoint

**Perguntas:**
1. Qual foi o último checkpoint salvo com sucesso?
2. Quantos arquivos foram processados desde então?
3. Qual arquivo causou o erro?
4. Quanto trabalho foi perdido?

**Localizar:**
- Último arquivo `CHECKPOINT_*.md` criado
- Última atualização no SESSION_LOG.md
- Último relatório consolidado gerado

#### PASSO 3: Documentar Erro

**Criar arquivo:** `ERRO_[Data]_[Hora].md`

**Template:**
```markdown
# 🚨 RELATÓRIO DE ERRO

**Data/Hora:** [DD/MMM/YYYY HH:MM]
**Tipo de Erro:** [Nome do erro]

## O que estava fazendo

[Descrição clara]

## Mensagem de erro

```
[Copiar mensagem exata do erro]
```

## Último checkpoint válido

- Arquivo: [Nome]
- Data: [Data/Hora]
- Progresso: [X/Y arquivos]

## Trabalho perdido

- Arquivos: [Lista]
- Estimativa: [Número] arquivos

## Arquivo problemático

- Nome: [Nome do arquivo]
- Tamanho: [KB]
- Localização: [Caminho]

## Próximos passos

- [ ] Aguardando orientação de Claude
```

#### PASSO 4: Reportar para Claude

**Atualizar SESSION_LOG.md:**

```markdown
### 🟣 Gemini - [DATA] ([HORA])

**ERRO DETECTADO**

**Tipo:** [Nome do erro]
**Momento:** [O que estava fazendo]
**Último checkpoint válido:** [Nome do arquivo + data]
**Trabalho perdido:** [X arquivos]

**Detalhes:**
- Arquivo problemático: [Nome] ([Tamanho])
- Mensagem: [Erro resumido]
- Relatório completo: `ERRO_[Data]_[Hora].md`

**Status:** ⏸️ PAUSADO - Aguardando orientação de Claude
```

#### PASSO 5: Aguardar Orientação

**Claude vai:**
1. Analisar o erro
2. Verificar checkpoint válido
3. Definir estratégia de recuperação
4. Orientar próximos passos

**Gemini deve:**
1. AGUARDAR pacientemente
2. NÃO tentar "consertar sozinho"
3. NÃO reprocessar sem orientação
4. Responder perguntas de Claude

### Checklist Recuperação (Gemini)

**Ao encontrar erro:**

- [ ] Parei processamento imediatamente?
- [ ] Identifiquei último checkpoint válido?
- [ ] Documentei erro em arquivo ERRO_*.md?
- [ ] Atualizei SESSION_LOG.md?
- [ ] Reportei para Claude claramente?
- [ ] Aguardei orientação (NÃO tentei consertar sozinho)?

---

## CATEGORIA 3: Sincronização

### Problema 3.1: Logs Desatualizados

**Sintoma:**
- SESSION_LOG.md não mostra trabalho recente
- PC_SYNC_LOG.md desatualizado
- Outro agente/PC não vê mudanças

**Causa:**
- Esqueceu de atualizar log ao finalizar sessão
- OneDrive não sincronizou ainda
- Conflito de edição

**Solução:**

#### Para SESSION_LOG (Claude ↔ Gemini)

```
1. Abrir SESSION_LOG.md
2. Adicionar seção no TOPO (mais recente)
3. Usar template:

### [🔵 Claude | 🟣 Gemini] - DD/MMM/YYYY (HH:MM)

**Trabalho Realizado:**
- [Ação 1]
- [Ação 2]

**Arquivos Modificados:**
- [Lista]

**Mensagem para [outro agente]:**
> [Mensagem direta]
```

#### Para PC_SYNC_LOG (Alienware ↔ Desktop)

```
1. Abrir PC_SYNC_LOG.md
2. Adicionar seção no TOPO
3. Usar template:

### [🖥️ Desktop | 💻 Alienware] - DD/MMM/YYYY (HH:MM)

**Ações realizadas:**
- [Ação 1]

**Próximos passos sugeridos:**
- [ ] [Tarefa]

**Mensagem para [outro PC]:**
> [Mensagem direta]
```

### Problema 3.2: Conflito Multi-PC

**Sintoma:**
- OneDrive mostra conflito
- Arquivos duplicados (-aliengass, -DESKTOP, etc)
- Mudanças sobrescritas

**Causa:**
- Editou mesmo arquivo em 2 PCs sem sincronizar
- OneDrive não sincronizou antes de trocar PC
- Edição simultânea

**Solução:**

```
1. IDENTIFICAR versões conflitantes
2. COMPARAR conteúdos (diff)
3. MESCLAR manualmente (pegar melhor de cada)
4. DELETAR versões duplicadas
5. AGUARDAR OneDrive sync completo (2-5 min)
6. ATUALIZAR PC_SYNC_LOG.md
```

**Prevenção:**
- SEMPRE aguardar OneDrive sync antes de fechar vault
- SEMPRE ler PC_SYNC_LOG ao abrir vault
- NUNCA editar em 2 PCs simultaneamente

### Problema 3.3: Handoff IA Incompleto

**Sintoma:**
- Gemini não viu mensagem de Claude (ou vice-versa)
- Contexto perdido entre IAs
- Retrabalho

**Causa:**
- Não atualizou SESSION_LOG.md
- Mensagem não clara
- IA não leu log ao iniciar

**Solução:**

**Claude:**
```markdown
### 🔵 Claude - [DATA]

**Trabalho Realizado:**
[Detalhes]

**Mensagem para Gemini:**
> Gemini: [Instrução clara e específica]
> Quando finalizar: [O que fazer]
```

**Gemini:**
```
1. LER SESSION_LOG.md PRIMEIRO (obrigatório)
2. VERIFICAR seção "Mensagem para Gemini"
3. EXECUTAR conforme orientação
4. REPORTAR conclusão no SESSION_LOG
```

**Ver decision tree completo:**
→ [[00_SISTEMA/MOCs/MOC_Sincronizacao_Sistemas.md]]

---

## CATEGORIA 4: Padrões/Nomenclatura

### Problema 4.1: Arquivo no Lugar Errado

**Sintoma:**
- Template em notas/ (deveria estar em 04_RECURSOS/TEMPLATES/)
- MOC no lugar errado
- Arquivo na raiz do vault

**Causa:**
- Não leu PROTOCOLO_CRIACAO_ARQUIVOS antes de criar
- Não consultou NOMENCLATURA.md
- Criou sem validar localização

**Solução:**

```
1. IDENTIFICAR tipo do arquivo (ver NOMENCLATURA.md)
2. DETERMINAR localização correta (ver guideline da categoria)
3. MOVER arquivo para local correto
4. ATUALIZAR MOC relevante (remover link antigo, adicionar novo)
5. VERIFICAR links quebrados (buscar nome do arquivo)
6. DOCUMENTAR correção no STATUS_VAULT.md
```

**Exemplo:**
```bash
# Arquivo errado: notas/TEMPLATE_Briefing.md
# Correto: 04_RECURSOS/TEMPLATES/TEMPLATE_Briefing.md

# Mover
mv "notas/TEMPLATE_Briefing.md" "04_RECURSOS/TEMPLATES/TEMPLATE_Briefing.md"

# Atualizar _MOC_Recursos.md (adicionar link)
# Verificar links quebrados
```

**Prevenção:**
- SEMPRE ler [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md]]
- SEMPRE consultar [[00_SISTEMA/PADROES/NOMENCLATURA.md]]
- USAR comando `/validate` antes de criar

### Problema 4.2: Nome Incorreto

**Sintoma:**
- Espaços no nome (Meu Arquivo.md)
- Prefixo errado (INDEX_ em vez de MOC_)
- Nome muito longo (>60 caracteres)
- Data errada (17-01-2025 em vez de 17JAN2025)

**Causa:**
- Não seguiu padrão NOMENCLATURA.md
- Criou sem validar
- Esqueceu regras

**Solução:**

```
1. IDENTIFICAR problema no nome
2. APLICAR padrão correto (ver NOMENCLATURA.md)
3. RENOMEAR arquivo (git mv se versionado)
4. ATUALIZAR todos links/referências
5. ATUALIZAR MOC relevante
6. VERIFICAR links quebrados
```

**Exemplos de Correção:**

```bash
# Espaços → Underscores
mv "Plano de Implementacao.md" "PLANO_Implementacao.md"

# Prefixo errado
mv "INDEX_Metodologia.md" "MOC_Metodologia.md"

# Data errada
mv "CHECKPOINT_17-01-2025.md" "CHECKPOINT_17JAN2025.md"

# Nome longo (90 chars) → Dividir em pasta
mv "Conhecimento_Desenvolvimento_Pessoal_Produtividade_TDAH_Estrategias.md" \
   "Conhecimento/DevPessoal/TDAH/Estrategias_Foco.md"
```

**Prevenção:**
- LER [[00_SISTEMA/PADROES/NOMENCLATURA.md]]
- VALIDAR antes de criar
- USAR CamelCase
- USAR underscores (nunca espaços)

### Problema 4.3: Estrutura de Projeto Errada

**Sintoma:**
- Pasta de projeto sem STATUS_ATUAL.md
- Faltando subpastas obrigatórias (planejamento/, docs/, etc)
- Estrutura inconsistente

**Causa:**
- Não seguiu [[02_PROJETOS/_GUIDELINES.md]]
- Criou estrutura incompleta

**Solução:**

```
1. LER 02_PROJETOS/_GUIDELINES.md
2. CRIAR pastas faltantes
3. CRIAR arquivos obrigatórios:
   - README.md
   - STATUS_ATUAL.md
   - planejamento/
   - checkpoints/
   - docs/
   - recursos/
   - tarefas/
   - metricas/
4. ATUALIZAR _MOC_Projetos.md
```

**Template Completo:**
```bash
mkdir -p "02_PROJETOS/Nome_Projeto/"{planejamento,checkpoints,docs,recursos,tarefas,metricas}
touch "02_PROJETOS/Nome_Projeto/README.md"
touch "02_PROJETOS/Nome_Projeto/STATUS_ATUAL.md"
```

---

## CATEGORIA 5: MOCs/Integração

### Problema 5.1: Esqueci de Atualizar MOC

**Sintoma:**
- Arquivo criado mas não aparece no MOC
- MOC desatualizado
- Links faltando

**Causa:**
- Criou arquivo e esqueceu de atualizar MOC
- Não seguiu PROTOCOLO_CRIACAO_ARQUIVOS

**Solução:**

```
1. IDENTIFICAR qual MOC deveria ter link
   - Arquivo em 01_CONHECIMENTO → _MOC_Conhecimento.md
   - Arquivo em 02_PROJETOS → _MOC_Projetos.md
   - Arquivo em 03_APRENDIZADO → _MOC_Aprendizado.md
   - Arquivo em 04_RECURSOS → _MOC_Recursos.md
   - Arquivo em 05_PESSOAL → _MOC_Pessoal.md

2. ABRIR MOC relevante

3. ADICIONAR link na seção correta
   Formato: [[caminho/arquivo.md|Título Descritivo]]

4. ATUALIZAR estatísticas do MOC
   - Total de itens: X → X+1
   - Data última adição

5. SALVAR
```

**Exemplo:**
```markdown
# _MOC_Recursos.md

**Total:** 18 → 19 recursos
**Última adição:** 16/Jan/2026

## Templates

- [[04_RECURSOS/TEMPLATES/TEMPLATE_Briefing.md|Template Briefing Projeto]]
- [[04_RECURSOS/TEMPLATES/TEMPLATE_RPI_MASTER_PLAN.md|RPI Master Plan]]  ← NOVO
- [outros...]
```

### Problema 5.2: Links Quebrados

**Sintoma:**
- Link não funciona (arquivo não encontrado)
- MOC aponta para arquivo movido/renomeado
- Referências quebradas

**Causa:**
- Arquivo movido sem atualizar links
- Arquivo renomeado sem atualizar referências
- Arquivo deletado

**Solução:**

```
1. IDENTIFICAR arquivo antigo (buscar no git log se necessário)

2. ENCONTRAR novo caminho/nome

3. BUSCAR todas referências ao nome antigo
   grep -r "nome_antigo" --include="*.md"

4. ATUALIZAR todos links/referências

5. VERIFICAR funcionamento
```

**Prevenção:**
- Ao MOVER arquivo → Atualizar MOC imediatamente
- Ao RENOMEAR → Buscar referências antes
- USAR links wikilink [[]] (Obsidian atualiza automaticamente)

### Problema 5.3: MOC Muito Grande (>200 links)

**Sintoma:**
- MOC difícil de navegar
- Carregamento lento
- Confusão visual

**Causa:**
- Categoria cresceu muito
- Não dividiu em sub-MOCs

**Solução:**

```
1. ANALISAR estrutura de pastas da categoria

2. IDENTIFICAR subcategorias naturais
   Exemplo: 01_CONHECIMENTO/
   ├── IA_Tecnologia/ (20 arquivos)
   ├── Negocios/ (15 arquivos)
   ├── Desenvolvimento_Pessoal/ (25 arquivos)

3. CRIAR sub-MOCs
   - MOC_IA_Tecnologia.md (20 links)
   - MOC_Negocios.md (15 links)
   - MOC_Desenvolvimento_Pessoal.md (25 links)

4. MOC principal vira índice de sub-MOCs
   _MOC_Conhecimento.md (3 links para sub-MOCs)

5. ATUALIZAR MOC Master
```

---

## CATEGORIA 6: Performance

### Problema 6.1: Vault Lento

**Sintoma:**
- Obsidian demora para abrir
- Busca lenta
- Navegação travando

**Causa:**
- Muitos arquivos (>5000)
- Arquivos muito grandes (>1MB)
- Plugins pesados
- OneDrive sincronizando

**Solução:**

```
1. VERIFICAR tamanho do vault
   - Total arquivos: Ideal <3000
   - Arquivos grandes: Mover PDFs/imagens para pasta externa

2. DESABILITAR plugins não usados
   - Settings → Community Plugins
   - Desabilitar temporariamente

3. AGUARDAR OneDrive sync completo
   - Ícone OneDrive (sincronizando vs sincronizado)

4. DIVIDIR vault se >5000 arquivos
   - Criar vaults separados por projeto grande

5. USAR .gitignore
   - Ignorar .obsidian/workspace
   - Ignorar arquivos temporários
```

### Problema 6.2: Claude Lento (Token Overload)

**Sintoma:**
- Claude demora para responder
- Respostas genéricas/alucinações
- "Thinking..." muito tempo

**Causa:**
- Contexto acima de 60% (Dumb Zone)
- Muitos arquivos carregados
- Sessão muito longa

**Diagnóstico:**

```
Token usage: 140k/200k = 70% → DUMB ZONE! 🔴
Token usage: 80k/200k = 40% → SMART ZONE ✅
```

**Solução:**

#### Imediato

```
1. CRIAR checkpoint
2. SALVAR trabalho atual
3. INICIAR nova sessão (contexto limpo)
4. LER apenas checkpoint (não todo histórico)
```

#### Preventivo

**Progressive Disclosure:**
```
1. NÃO ler TODOS os padrões ao iniciar
2. LER apenas o necessário para tarefa atual
3. USAR guias de leitura:
   [[00_SISTEMA/GUIAS/GUIA_Leitura_Claude.md]]
```

**Smart Zone (40% Rule):**
```
- Meta: Manter contexto < 80k tokens (40% de 200k)
- Ideal: 40-60k tokens
- Evitar: >120k tokens (60% = Dumb Zone)
```

**RPI Framework:**
```
1. Research: Carregar contexto específico
2. Plan: Carregar padrões relevantes
3. Implementation: Carregar arquivos a editar
```

### Problema 6.3: Gemini Quota Excedida

**Sintoma:**
- Mensagem: "Quota exceeded"
- Gemini não processa
- Free tier esgotado

**Causa:**
- Usou >1M tokens em curto período
- Processamento massivo demais
- Horário de pico

**Solução:**

```
1. VERIFICAR quota restante
   (Gemini mostra no erro)

2. AGUARDAR reset (24h)

3. DIVIDIR trabalho:
   - Processar metade hoje
   - Metade amanhã

4. USAR Claude para urgente
   (custo, mas resolve)

5. OTIMIZAR prompts
   (reduzir tokens por tarefa)
```

**Prevenção:**
- PLANEJAR processamento massivo
- DIVIDIR em múltiplos dias
- USAR horários fora de pico
- PROCESSAR lotes menores

---

## ⚡ CHECKLISTS ANTI-ERRO

### Ao Criar Arquivo

- [ ] Li NOMENCLATURA.md?
- [ ] Li PROTOCOLO_CRIACAO_ARQUIVOS.md?
- [ ] Consultei guideline da categoria?
- [ ] Nome <60 caracteres?
- [ ] Sem espaços (usar underscores)?
- [ ] Prefixo correto?
- [ ] Localização correta?
- [ ] Atualizei MOC relevante?

### Ao Finalizar Sessão

- [ ] Atualizei SESSION_LOG.md (se handoff IA)?
- [ ] Atualizei PC_SYNC_LOG.md (se trocar PC)?
- [ ] Deixei mensagens claras?
- [ ] Commitei mudanças importantes?
- [ ] Aguardei OneDrive sync completo?

### Ao Iniciar Sessão

- [ ] Li SESSION_LOG.md (últimas mudanças)?
- [ ] Li PC_SYNC_LOG.md (mudanças outro PC)?
- [ ] Verifiquei mensagens para mim?
- [ ] Token usage < 40% (Smart Zone)?
- [ ] Identifiquei tarefas pendentes?

---

## 🎯 REGRAS DE OURO

### Regra 1: Progressive Disclosure

**NÃO carregar tudo de uma vez.**

```
❌ Ler 25 arquivos de padrões ao iniciar (120k tokens)
✅ Ler guia de leitura (5k) → Ler só o necessário (20k)
```

### Regra 2: Checkpoints Frequentes

**Salvar progresso regularmente.**

```
✅ A cada 10 arquivos processados → Checkpoint
✅ A cada decisão importante → Checkpoint
✅ Antes de tarefa arriscada → Checkpoint
```

### Regra 3: Comunicação Clara

**Logs detalhados salvam tempo.**

```
❌ "Fiz umas mudanças"
✅ "Criados 7 arquivos em 00_SISTEMA/GUIAS/, consolidado troubleshooting"
```

### Regra 4: Padrões São Lei

**SEMPRE consultar antes de criar.**

```
❌ Criar INDEX_Algo.md (inventou prefixo)
✅ Ler NOMENCLATURA → MOC_Algo.md (padrão correto)
```

### Regra 5: Admitir Erros Rapidamente

**Errar é humano. Esconder é problemático.**

```
✅ "Criei arquivo errado em notas/. Movendo para 04_RECURSOS/TEMPLATES/"
✅ "Nome tinha espaços. Renomeando para padrão correto"
```

---

## 📞 QUANDO PEDIR AJUDA

**Se não conseguir resolver em 15 minutos:**

1. **DOCUMENTAR** problema claramente
2. **CRIAR** arquivo ERRO_*.md se apropriado
3. **ATUALIZAR** SESSION_LOG.md
4. **MARCAR** status como ⏸️ PAUSADO
5. **AGUARDAR** orientação

**Formato de pedido de ajuda:**

```markdown
### [IA] - [DATA]

**PROBLEMA: [Título claro]**

**Sintoma:**
[O que está acontecendo]

**Tentativas:**
- [O que já tentei]
- [Resultados]

**Checkpoint válido:**
[Último ponto seguro]

**Aguardando orientação.**
```

---

## 📚 REFERÊNCIAS

**Padrões:**
- [[00_SISTEMA/PADROES/NOMENCLATURA.md]] - Nomes corretos
- [[00_SISTEMA/PADROES/ARCHITECTURE_GUIDELINES.md]] - Smart Zone 40%, RPI

**Protocolos:**
- [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md]] - Workflow criação
- [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_MULTI_PC.md]] - Sincronização PCs
- [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_SINCRONIZACAO_AGENTES.md]] - Handoff IAs

**Guidelines:**
- [[01_CONHECIMENTO/_GUIDELINES.md]]
- [[02_PROJETOS/_GUIDELINES.md]]
- [[03_APRENDIZADO/_GUIDELINES.md]]
- [[04_RECURSOS/_GUIDELINES.md]]
- [[05_PESSOAL/_GUIDELINES.md]]

**MOCs:**
- [[00_SISTEMA/MOCs/MOC_Padroes_Protocolos_Guidelines.md]] - Índice master
- [[00_SISTEMA/MOCs/MOC_Sincronizacao_Sistemas.md]] - Qual protocolo usar

**Guias:**
- [[00_SISTEMA/GUIAS/GUIA_Leitura_Claude.md]] - Progressive disclosure
- [[00_SISTEMA/GUIAS/GUIA_Leitura_Gemini.md]] - Papel Gemini
- [[00_SISTEMA/GUIAS/GUIA_Usuario_Quick_Start.md]] - Quick start usuário

---

**Versão:** 1.0
**Criado:** 16/Jan/2026
**Status:** ✅ ATIVO
**Consolidou:** GUIA_RAPIDO_ERRO_OVERLOAD + GUIA_RECUPERACAO_ERRO_GEMINI
**Última atualização:** 16/Jan/2026

**PREVENÇÃO > CORREÇÃO. COMUNICAÇÃO > SILÊNCIO. PADRÕES > IMPROVISO.** 🚑✅
