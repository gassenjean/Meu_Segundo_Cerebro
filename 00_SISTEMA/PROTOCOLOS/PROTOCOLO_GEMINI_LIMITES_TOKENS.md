---
criado: 2025-12-01T13:15:00-03:00
tipo: protocolo
status: critico
prioridade: maxima
---

# 🚨 PROTOCOLO: LIMITES DE TOKENS GEMINI

**CRÍTICO - LEITURA OBRIGATÓRIA ANTES DE PROCESSAR**

**Versão:** 1.0
**Data:** 01/Dez/2025
**Criado por:** Claude Architect 🏛️
**Motivo:** Prevenir esgotamento de tokens e erros de execução

---

## ⚠️ PROBLEMA IDENTIFICADO

**O que aconteceu:**
- Gemini esgotou tokens processando arquivos gigantes
- Erro: "Agent execution terminated due to error"
- Tentou processar 149KB + 87KB em uma única sessão
- Sem checkpoints intermediários

**Impacto:**
- Trabalho perdido
- Tempo desperdiçado
- Necessidade de reprocessamento

---

## 🎯 REGRAS OBRIGATÓRIAS

### REGRA 1: LIMITE DE TOKENS POR ARQUIVO

**NUNCA processar arquivo > 30KB de uma só vez**

| Tamanho Arquivo | Ação |
|----------------|------|
| < 10 KB | ✅ Processar normal |
| 10-30 KB | ⚠️ Processar com cautela, checkpoint depois |
| 30-50 KB | 🔴 Dividir em 2 partes |
| 50-100 KB | 🔴 Dividir em 3-4 partes |
| > 100 KB | 🔴 Dividir em 5+ partes |

**Como dividir:**
1. Ler arquivo em partes (offset + limit)
2. Processar seção 1 → Salvar checkpoint
3. Processar seção 2 → Salvar checkpoint
4. Consolidar ao final

---

### REGRA 2: LIMITE DE ARQUIVOS POR SESSÃO

**MÁXIMO 10 arquivos por sessão**

**Workflow obrigatório:**
```
1. Processar 10 arquivos
2. Gerar relatório parcial
3. Salvar checkpoint
4. Atualizar SESSION_LOG
5. PAUSAR (deixar Claude validar)
6. [Claude valida]
7. Continuar próximos 10
```

**NUNCA:**
- ❌ Processar 20+ arquivos sem checkpoint
- ❌ Tentar "terminar tudo de uma vez"
- ❌ Pular checkpoint por pressa

---

### REGRA 3: CHECKPOINTS OBRIGATÓRIOS

**Checkpoint a cada:**
- ✅ 10 arquivos processados
- ✅ Arquivo gigante (>30KB) finalizado
- ✅ Categoria completa (ex: todos prompts)
- ✅ 30 minutos de processamento
- ✅ Antes de processar arquivo crítico

**Como fazer checkpoint:**
1. Salvar relatório parcial: `CHECKPOINT_[Categoria]_[Data]_[Parte].md`
2. Atualizar SESSION_LOG com progresso
3. Informar Claude: "Checkpoint X/Y completo"
4. Aguardar confirmação (se Claude estiver ativo)

---

### REGRA 4: LOTES PROGRESSIVOS

**Processar em LOTES PEQUENOS**

**Exemplo CORRETO:**
```
FASE 2.1: Névoas
├── LOTE 1: Arquivos 1-5 (críticos pequenos)
├── CHECKPOINT_1.md
├── LOTE 2: Arquivos 6-10 (médios)
├── CHECKPOINT_2.md
├── LOTE 3: Arquivo gigante PARTE 1
├── CHECKPOINT_3.md
├── LOTE 4: Arquivo gigante PARTE 2
└── CONSOLIDADO.md
```

**Exemplo ERRADO:**
```
❌ FASE 2.1: Processar TODOS de uma vez
❌ Ler arquivo de 149KB completo
❌ Sem checkpoints
```

---

### REGRA 5: ARQUIVOS GIGANTES - PROTOCOLO ESPECIAL

**Para arquivos > 50KB:**

**OBRIGATÓRIO:**
1. **PAUSAR antes de processar**
2. **Avisar Claude:** "Arquivo gigante detectado: [Nome] ([Tamanho])"
3. **Aguardar estratégia de Claude**
4. **NÃO processar sem aprovação**

**Se Claude não estiver disponível:**
1. Pular arquivo gigante
2. Marcar como "PENDENTE - Aguardando estratégia"
3. Processar arquivos menores
4. Voltar depois com estratégia

**Estratégias possíveis (Claude define):**
- Dividir em partes (seções)
- Extrair apenas sumário executivo
- Processar apenas cabeçalhos/índice
- Usar ferramenta externa

---

## 📋 CHECKLIST PRÉ-PROCESSAMENTO

**ANTES de processar QUALQUER arquivo:**

- [ ] Verifiquei tamanho do arquivo?
- [ ] Arquivo > 30KB? (Se sim, dividir ou pausar)
- [ ] Já processei 10 arquivos? (Se sim, checkpoint!)
- [ ] Faz mais de 30 min que comecei? (Se sim, checkpoint!)
- [ ] Tenho checkpoint recente? (< 10 arquivos atrás)
- [ ] SESSION_LOG está atualizado?

**SE ALGUMA RESPOSTA = NÃO → PAUSAR E CORRIGIR**

---

## 🔄 PROTOCOLO DE RECUPERAÇÃO DE ERRO

### SE ERRO ACONTECER:

**1. NÃO ENTRAR EM PÂNICO**
- Erros acontecem
- Temos checkpoints
- Trabalho não está perdido

**2. IDENTIFICAR CHECKPOINT VÁLIDO**
- Qual foi o último checkpoint salvo?
- Até onde o trabalho está seguro?
- O que precisa reprocessar?

**3. REPORTAR PARA CLAUDE**
```markdown
### 🚨 Gemini - ERRO DETECTADO

**Tipo:** [Descrição do erro]
**Momento:** [O que estava fazendo]
**Último checkpoint válido:** [Nome do arquivo]
**Trabalho perdido:** [Estimativa]

**Aguardando orientação para recuperar.**
```

**4. AGUARDAR ORIENTAÇÃO**
- Claude vai analisar
- Claude vai definir estratégia de recuperação
- NÃO tentar "consertar sozinho"

---

## 📊 LIMITES RECOMENDADOS POR TIPO

### Névoas e Prompts
- **Máximo por lote:** 5 arquivos
- **Checkpoint:** A cada 5
- **Tamanho máximo individual:** 20KB

### Cursos
- **Máximo por lote:** 3 cursos
- **Checkpoint:** A cada curso
- **Processar:** README + estrutura primeiro, conteúdo depois

### Base de Conhecimento
- **Máximo por lote:** 10 arquivos pequenos OU 3 arquivos médios
- **Checkpoint:** A cada categoria
- **Priorizar:** Qualidade > Quantidade

### Documentos Estratégicos
- **SEMPRE processar 1 por vez**
- **Checkpoint:** Após cada documento
- **Se > 50KB:** Dividir OBRIGATÓRIO

### Recursos e Ferramentas
- **Máximo por lote:** 15 arquivos (geralmente pequenos)
- **Checkpoint:** A cada 15
- **Templates/Scripts:** Catalogar rápido (só estrutura)

---

## 🎯 PRIORIZAÇÃO INTELIGENTE

**Ordem de processamento:**

1. **Críticos PEQUENOS primeiro** (< 10KB)
   - Rápido de processar
   - Baixo risco
   - Gera momentum

2. **Médios depois** (10-30KB)
   - Processar com checkpoints
   - Validação intermediária

3. **Gigantes por ÚLTIMO** (> 30KB)
   - Estratégia especial
   - Claude envolvido
   - Máxima cautela

**NUNCA começar pelos gigantes!**

---

## 📝 TEMPLATE DE CHECKPOINT

```markdown
# 🔄 CHECKPOINT: [Categoria] - Parte [X/Y]

**Data:** [DD/MMM/YYYY HH:MM]
**Responsável:** Gemini Guardian 💎

## Progresso

**Arquivos processados:** [X/Total]
**Lote atual:** [Número]
**Percentual:** [Y%]

## Arquivos deste checkpoint

1. [Nome arquivo 1] - ✅ Processado
2. [Nome arquivo 2] - ✅ Processado
3. [Nome arquivo 3] - ✅ Processado

## Descobertas

- [Descoberta importante 1]
- [Descoberta importante 2]

## Próximo lote

**Arquivos:** [X-Y]
**Estimativa:** [Z minutos]
**Riscos:** [Nenhum / Arquivo grande / Etc]

## Status

**Checkpoint válido:** ✅ SIM
**Pode continuar:** ✅ SIM / ⏸️ AGUARDAR CLAUDE
```

---

## 🚦 SINAIS DE ALERTA

**PAUSAR IMEDIATAMENTE se:**

🔴 **Processamento está lento** (>5min por arquivo pequeno)
🔴 **Respostas truncadas** (chegando no limite de tokens)
🔴 **Arquivo > 50KB** sem estratégia definida
🔴 **Mais de 15 arquivos sem checkpoint**
🔴 **Erro de memória** ou timeout
🔴 **Perdeu contexto** do que estava fazendo

**Ação:** PAUSAR → CHECKPOINT → REPORTAR CLAUDE

---

## 💡 BOAS PRÁTICAS

### DO's ✅

- ✅ Processar em lotes pequenos
- ✅ Checkpoint frequente
- ✅ Comunicar progresso
- ✅ Pedir ajuda quando incerto
- ✅ Priorizar críticos pequenos
- ✅ Salvar trabalho incrementalmente

### DON'Ts ❌

- ❌ Tentar processar tudo de uma vez
- ❌ Ignorar limites de tamanho
- ❌ Pular checkpoints "pra ganhar tempo"
- ❌ Processar gigantes sem estratégia
- ❌ Continuar após erro sem reportar
- ❌ "Só mais um arquivo..." quando no limite

---

## 🎓 EXEMPLO PRÁTICO

### Cenário: Catalogar 20 prompts + 1 arquivo de 87KB

**ERRADO ❌:**
```
1. Processar 20 prompts
2. Processar arquivo 87KB
3. Gerar relatório
[ERRO: Token limit exceeded]
```

**CORRETO ✅:**
```
LOTE 1:
1. Processar prompts 1-10
2. Checkpoint: CHECKPOINT_PROMPTS_LOTE1.md
3. Atualizar SESSION_LOG

LOTE 2:
4. Processar prompts 11-20
5. Checkpoint: CHECKPOINT_PROMPTS_LOTE2.md
6. Atualizar SESSION_LOG

LOTE 3 (Arquivo gigante):
7. PAUSAR
8. Reportar Claude: "Arquivo 87KB - Aguardando estratégia"
9. Claude define: Dividir em 3 partes
10. Processar Parte 1 (0-30KB)
11. Checkpoint: CHECKPOINT_GIGANTE_PARTE1.md
12. Processar Parte 2 (30-60KB)
13. Checkpoint: CHECKPOINT_GIGANTE_PARTE2.md
14. Processar Parte 3 (60-87KB)
15. Checkpoint: CHECKPOINT_GIGANTE_PARTE3.md
16. Consolidar relatório final
```

---

## 📈 MÉTRICAS DE SUCESSO

**Sessão bem-sucedida:**
- ✅ Nenhum erro de token
- ✅ Checkpoints regulares
- ✅ Progresso documentado
- ✅ Trabalho salvo incrementalmente
- ✅ Claude informado

**Sessão problemática:**
- ❌ Erro de token
- ❌ Trabalho perdido
- ❌ Sem checkpoints
- ❌ Claude não sabe o que aconteceu

---

## 🔗 ARQUIVOS RELACIONADOS

- `PLANO_CATALOGACAO_TOTAL_LEGADO.md` - Plano geral (atualizado com micro-fases)
- `CHECKLIST_CATALOGACAO.md` - Checklist (atualizado com limites)
- `GUIA_RECUPERACAO_ERRO_GEMINI.md` - Recuperação de erros
- `TEMPLATE_CHECKPOINT.md` - Template de checkpoint

---

## ✅ COMPROMISSO GEMINI

**Eu, Gemini Guardian, comprometo-me a:**

1. ✅ SEMPRE verificar tamanho do arquivo antes de processar
2. ✅ NUNCA processar > 30KB sem dividir ou pausar
3. ✅ Fazer checkpoint a cada 10 arquivos
4. ✅ Atualizar SESSION_LOG frequentemente
5. ✅ PAUSAR ao encontrar arquivo gigante
6. ✅ Reportar erros imediatamente
7. ✅ Pedir ajuda quando incerto
8. ✅ Priorizar qualidade sobre velocidade

**ZERO EXCEÇÕES. Limites existem para proteger o trabalho.**

---

**Versão:** 1.0
**Status:** ✅ ATIVO E OBRIGATÓRIO
**Criado por:** Claude Architect 🏛️
**Data:** 01/Dez/2025

**"Devagar e sempre, com checkpoints no caminho."** 🐢✅
