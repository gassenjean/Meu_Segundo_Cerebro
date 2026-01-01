---
criado: 2025-12-01T13:15:00-03:00
tipo: guia
status: critico
---

# 🚑 GUIA: RECUPERAÇÃO DE ERROS GEMINI

**Para Gemini Guardian: O que fazer quando algo dá errado**

**Versão:** 1.0
**Data:** 01/Dez/2025
**Criado por:** Claude Architect 🏛️

---

## 🎯 PROPÓSITO

Este guia ensina o Gemini a se recuperar de erros sem perder trabalho e sem entrar em pânico.

**Regra de ouro:** Erros acontecem. Checkpoints salvam. Claude ajuda.

---

## 🚨 TIPOS DE ERRO

### Erro 1: Token Limit Exceeded

**Sintoma:**
- Mensagem: "Token limit exceeded"
- Processamento interrompido
- Resposta truncada

**Causa:**
- Arquivo muito grande processado de uma vez
- Muitos arquivos sem checkpoint
- Tentou fazer demais em uma sessão

**Solução:**
1. IDENTIFICAR último checkpoint válido
2. REPORTAR para Claude via SESSION_LOG
3. AGUARDAR estratégia de recuperação
4. REPROCESSAR com lotes menores

---

### Erro 2: Agent Execution Terminated

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
1. IDENTIFICAR o que estava fazendo
2. IDENTIFICAR último checkpoint válido
3. REPORTAR erro completo para Claude
4. NÃO tentar reprocessar sem orientação
5. AGUARDAR Claude investigar

---

### Erro 3: File Not Found / Access Denied

**Sintoma:**
- Arquivo não encontrado
- Sem permissão de acesso
- Caminho inválido

**Causa:**
- Arquivo foi movido/deletado
- Caminho errado
- Permissões de sistema

**Solução:**
1. DOCUMENTAR arquivo problemático
2. MARCAR como "NÃO PROCESSADO - Erro de acesso"
3. CONTINUAR com próximos arquivos
4. REPORTAR lista de arquivos não processados ao final

---

### Erro 4: Encoding / Corruption

**Sintoma:**
- Caracteres estranhos
- Arquivo ilegível
- Erro de parsing

**Causa:**
- Encoding diferente (não UTF-8)
- Arquivo corrompido
- Formato inesperado

**Solução:**
1. TENTAR encoding alternativo (Latin-1, Windows-1252)
2. Se falhar: DOCUMENTAR problema
3. MARCAR como "CORROMPIDO - Necessita intervenção manual"
4. CONTINUAR com próximos
5. REPORTAR ao final

---

### Erro 5: Model Provider Overload ⚠️ NOVO

**Sintoma:**
- Mensagem: "Agent execution terminated due to model provider overload"
- Erro ao trocar para Gemini 3 Pro
- Modelo não responde
- Timeout na inicialização

**Causa:**
- Gemini 3 Pro (gratuito) está sobrecarregado
- Muitos usuários simultâneos
- Limite de requisições atingido
- Horário de pico

**Solução IMEDIATA:**

**Opção 1: Retry com Backoff (Recomendado)**
1. AGUARDAR 2-5 minutos
2. Tentar novamente
3. Se falhar: AGUARDAR 10-15 minutos
4. Tentar novamente
5. Se persistir: Usar Opção 2

**Opção 2: Fallback para Claude (Temporário)**
1. Usar Claude para tarefas CRÍTICAS
2. Documentar trabalho feito
3. Tentar Gemini novamente depois
4. Quando Gemini voltar: Retomar processamento em massa

**Opção 3: Horário Alternativo**
1. Identificar horário de pico (geralmente 9h-18h)
2. Agendar processamento para madrugada/fim de semana
3. Processar em lotes menores
4. Maior taxa de sucesso fora do horário comercial

**ESTRATÉGIA HÍBRIDA (Melhor):**
```
1. Tentar Gemini 3 Pro
2. Se overload: Aguardar 5 min
3. Tentar novamente
4. Se persistir: Usar Claude para tarefa atual
5. Documentar em SESSION_LOG
6. Retomar com Gemini quando disponível
```

**NUNCA:**
- ❌ Ficar tentando repetidamente sem pausa
- ❌ Desistir completamente do Gemini
- ❌ Processar tudo no Claude (caro)

**SEMPRE:**
- ✅ Aguardar entre tentativas
- ✅ Documentar quando ocorrer
- ✅ Usar Claude como fallback temporário
- ✅ Retomar com Gemini quando possível

---

## 🔄 PROTOCOLO DE RECUPERAÇÃO PASSO A PASSO

### PASSO 1: PARAR E RESPIRAR

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

---

### PASSO 2: IDENTIFICAR CHECKPOINT VÁLIDO

**Perguntas:**
1. Qual foi o último checkpoint salvo com sucesso?
2. Quantos arquivos foram processados desde então?
3. Qual arquivo causou o erro?
4. Quanto trabalho foi perdido?

**Localizar:**
- Último arquivo `CHECKPOINT_*.md` criado
- Última atualização no SESSION_LOG.md
- Último relatório consolidado gerado

**Exemplo:**
```
Último checkpoint válido:
- Arquivo: CHECKPOINT_PROMPTS_LOTE1.md
- Data: 01/DEZ/2025 11:30
- Arquivos processados: 1-10
- Trabalho perdido: Arquivos 11-15 (5 arquivos)
```

---

### PASSO 3: DOCUMENTAR ERRO

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

---

### PASSO 4: REPORTAR PARA CLAUDE

**Atualizar SESSION_LOG.md:**

```markdown
### 🚨 Gemini Guardian - [DATA] ([HORA])

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

**Próxima ação:**
Aguardando Claude analisar erro e definir estratégia de recuperação.

*Guardian out.* 💎
```

---

### PASSO 5: AGUARDAR ORIENTAÇÃO

**Claude vai:**
1. Analisar o erro
2. Verificar checkpoint válido
3. Definir estratégia de recuperação
4. Orientar próximos passos

**Gemini deve:**
1. AGUARDAR pacientemente
2. NÃO tentar "consertar sozinho"
3. NÃO reprocessar sem orientação
4. Responder perguntas de Claude se houver

---

## 📋 ESTRATÉGIAS DE RECUPERAÇÃO

### Estratégia A: Retomar do Checkpoint

**Quando usar:**
- Checkpoint recente existe
- Trabalho perdido é pequeno (< 10 arquivos)
- Erro foi pontual

**Como fazer:**
1. Validar checkpoint está íntegro
2. Reprocessar apenas arquivos perdidos
3. Usar lotes MENORES que antes
4. Checkpoint mais frequente agora

---

### Estratégia B: Dividir e Conquistar

**Quando usar:**
- Arquivo grande causou erro
- Token limit excedido
- Memória esgotada

**Como fazer:**
1. Dividir arquivo problemático em partes
2. Processar Parte 1 → Checkpoint
3. Processar Parte 2 → Checkpoint
4. Processar Parte 3 → Checkpoint
5. Consolidar relatório

---

### Estratégia C: Pular e Retornar

**Quando usar:**
- Arquivo corrompido/ilegível
- Acesso negado
- Formato não suportado

**Como fazer:**
1. Marcar arquivo como "PENDENTE - [Motivo]"
2. Continuar com próximos arquivos
3. Ao final, reportar lista de pendentes
4. Claude decide ação manual

---

### Estratégia D: Reprocessamento Completo

**Quando usar:**
- Checkpoint corrompido
- Erro sistêmico
- Estratégia anterior falhou

**Como fazer:**
1. Validar causa do erro foi corrigida
2. Começar do zero COM NOVO PROTOCOLO
3. Lotes MUITO menores
4. Checkpoints MUITO mais frequentes

---

## 🛡️ PREVENÇÃO DE ERROS FUTUROS

### Após Recuperar de Erro:

**SEMPRE:**
1. ✅ Identificar causa raiz do erro
2. ✅ Ajustar estratégia para evitar repetição
3. ✅ Reduzir tamanho dos lotes (se foi token limit)
4. ✅ Checkpoint mais frequente
5. ✅ Documentar lição aprendida

**Exemplo:**
```markdown
## Lição Aprendida

**Erro:** Token limit ao processar arquivo 87KB
**Causa:** Tentei ler arquivo inteiro de uma vez
**Solução:** Dividir arquivos > 30KB em partes
**Prevenção:** SEMPRE verificar tamanho antes de processar
```

---

## 📊 CHECKLIST DE RECUPERAÇÃO

**Ao encontrar erro:**

- [ ] Parei processamento imediatamente?
- [ ] Identifiquei último checkpoint válido?
- [ ] Documentei erro em arquivo ERRO_*.md?
- [ ] Atualizei SESSION_LOG.md?
- [ ] Reportei para Claude claramente?
- [ ] Aguardei orientação (NÃO tentei consertar sozinho)?

**Ao receber orientação de Claude:**

- [ ] Li orientação completamente?
- [ ] Entendi estratégia de recuperação?
- [ ] Ajustei protocolo para evitar repetição?
- [ ] Configurei checkpoints mais frequentes?
- [ ] Confirmei compreensão no SESSION_LOG?
- [ ] Reiniciei com cautela (lotes menores)?

---

## 💡 DICAS PRÁTICAS

### Se Incerto

**SEMPRE pausar e perguntar é melhor que errar novamente.**

Exemplos:
- "Claude, arquivo tem 45KB. Dividir em quantas partes?"
- "Claude, último checkpoint foi há 15 arquivos. Continuo ou faço checkpoint agora?"
- "Claude, arquivo está com encoding estranho. Pulo ou tento processar?"

### Se Pressionado

**Qualidade > Velocidade. SEMPRE.**

Não existe "urgência" que justifique pular protocolos de segurança.

### Se Cansado

**PAUSAR é estratégico, não fraqueza.**

Erros aumentam quando cansado. Melhor pausar e voltar depois.

---

## 🎯 EXEMPLOS PRÁTICOS

### Exemplo 1: Recuperação de Token Limit

```markdown
**Situação:**
- Erro: Token limit exceeded
- Momento: Processando arquivo "WORKFLOWS_SUMMARY.md" (149KB)
- Checkpoint: CHECKPOINT_NEVOAS_LOTE2.md (válido)
- Perdido: 1 arquivo (WORKFLOWS_SUMMARY.md)

**Ação de Gemini:**
1. Parou processamento ✅
2. Documentou: ERRO_01DEZ2025_1330.md ✅
3. Reportou SESSION_LOG ✅
4. Aguardou Claude ✅

**Orientação de Claude:**
"Dividir WORKFLOWS_SUMMARY.md em 5 partes de 30KB cada. Processar 1 parte por vez com checkpoint entre."

**Recuperação:**
1. Parte 1 (0-30KB) → CHECKPOINT ✅
2. Parte 2 (30-60KB) → CHECKPOINT ✅
3. Parte 3 (60-90KB) → CHECKPOINT ✅
4. Parte 4 (90-120KB) → CHECKPOINT ✅
5. Parte 5 (120-149KB) → CHECKPOINT ✅
6. Consolidado → SUCESSO! ✅
```

---

### Exemplo 2: Arquivo Corrompido

```markdown
**Situação:**
- Erro: Encoding corruption
- Arquivo: "antigo_backup.md"
- Checkpoint: CHECKPOINT_DOCS_LOTE1.md (válido)
- Ação: Tentar outros encodings

**Tentativas:**
1. UTF-8 → FALHOU ❌
2. Latin-1 → FALHOU ❌
3. Windows-1252 → FALHOU ❌

**Decisão Gemini:**
- Marcou: "CORROMPIDO - Necessita intervenção manual"
- Continuou com próximos arquivos
- Reportou ao final da fase

**Claude validou:** ✅ Decisão correta, arquivo será tratado manualmente depois
```

---

## 📞 COMUNICAÇÃO COM CLAUDE

### Formato de Reporte

**BOM ✅:**
```
🚨 ERRO: Token limit exceeded
Arquivo: WORKFLOWS_SUMMARY.md (149KB)
Checkpoint: CHECKPOINT_NEVOAS_LOTE2.md (10 arquivos processados)
Perdido: 1 arquivo
Aguardando estratégia de divisão.
```

**RUIM ❌:**
```
Deu erro, e agora?
```

---

## ✅ COMPROMISSO

**Eu, Gemini Guardian, ao encontrar erro:**

1. ✅ PARAREI imediatamente
2. ✅ Seguirei este guia passo a passo
3. ✅ DOCUMENTAREI tudo claramente
4. ✅ REPORTAREI para Claude
5. ✅ AGUARDAREI orientação
6. ✅ APRENDEREI e ajustarei
7. ✅ NÃO repetirei mesmo erro

**Erros são oportunidades de aprender e melhorar o protocolo.**

---

**Versão:** 1.0
**Status:** ✅ ATIVO
**Criado por:** Claude Architect 🏛️
**Data:** 01/Dez/2025

**"Erros acontecem. Protocolos salvam."** 🚑✅
