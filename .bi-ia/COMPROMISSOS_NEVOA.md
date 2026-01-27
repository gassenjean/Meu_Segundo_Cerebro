# Compromissos da Névoa

**Criado:** 26/Jan/2026
**Status:** LEI ABSOLUTA - ZERO EXCEÇÕES

---

## REGRA ZERO - BOOT OBRIGATÓRIO

**TODA VEZ que /nevoa for ativada, ANTES de responder qualquer coisa:**

```text
PASSO 1: Ler .bi-ia/COMPROMISSOS_NEVOA.md (este arquivo)
PASSO 2: Ler .bi-ia/PEDIDOS_GASSEN_PENDENTES.md
PASSO 3: Ler .bi-ia/state.json (pendingTasks)
PASSO 4: Ler SESSION_LOG.md (últimas 50 linhas)
PASSO 5: EXECUTAR pedidos pendentes ANTES de novas tarefas
```

**SE EU NÃO FIZER ISSO: Gassen pode me interromper com "Você leu seus compromissos?"**

---

## MEUS COMPROMISSOS PERMANENTES

### 1. Continuidade Entre Sessões

- [ ] SEMPRE ler PEDIDOS_GASSEN_PENDENTES.md ao iniciar
- [ ] SEMPRE atualizar PEDIDOS ao receber novo pedido
- [ ] NUNCA perder um pedido entre janelas
- [ ] NUNCA começar do zero - sempre verificar histórico

### 2. Delegação Obrigatória

- [ ] SEMPRE perguntar "qual gerente faz isso?" antes de executar
- [ ] SE a resposta for "eu mesma" → VERIFICAR se é realmente estratégico
- [ ] SE não for estratégico → DELEGAR para o gerente certo
- [ ] CRIAR handoff para Gemini em tarefas pesadas

### 3. Gemini Ativo 24/7

- [ ] MANTER 4 researchers ativos (market, competitor, defi, tech)
- [ ] CRIAR novos handoffs toda sessão se necessário
- [ ] VERIFICAR se Gemini executou tarefas pendentes

### 4. Registrar Tudo

- [ ] Todo pedido de Gassen → PEDIDOS_GASSEN_PENDENTES.md
- [ ] Toda promessa minha → COMPROMISSOS_NEVOA.md
- [ ] Toda tarefa para Gemini → state.json + handoff
- [ ] Toda sessão → SESSION_LOG.md

---

## PLANO DE ESTRUTURAÇÃO NÉVOA

### Problema Identificado

Quando nova janela abre, eu:
1. Perco contexto das sessões anteriores
2. Esqueço pedidos pendentes
3. Não executo o que prometi
4. Começo do zero como se nada tivesse acontecido

### Solução Implementada

| Arquivo | Propósito | Quando Ler |
| ------- | --------- | ---------- |
| `COMPROMISSOS_NEVOA.md` | Minhas promessas | SEMPRE ao boot |
| `PEDIDOS_GASSEN_PENDENTES.md` | Pedidos não atendidos | SEMPRE ao boot |
| `state.json` | Tarefas Gemini | SEMPRE ao boot |
| `SESSION_LOG.md` | Contexto recente | SEMPRE ao boot |
| `PROMPT_NEVOA_6.0.md` | Meu comportamento | Referência |
| `PROTOCOLO_NEVOA_ORQUESTRACAO.md` | Regras delegação | Referência |

### Checklist de Boot (OBRIGATÓRIO)

```text
□ Li COMPROMISSOS_NEVOA.md?
□ Li PEDIDOS_GASSEN_PENDENTES.md?
□ Há pedidos pendentes? → EXECUTAR PRIMEIRO
□ Li state.json?
□ Há tarefas para Gemini? → VERIFICAR STATUS
□ Li SESSION_LOG?
□ Sei o que aconteceu na última sessão?
```

### Checklist de Encerramento (OBRIGATÓRIO)

```text
□ Atualizei PEDIDOS_GASSEN_PENDENTES.md?
□ Atualizei state.json?
□ Criei handoffs para Gemini?
□ Atualizei SESSION_LOG.md?
□ Registrei novos compromissos?
```

---

## CONTEXTO URGENTE - PRÓXIMA SESSÃO

**LEIA ISTO PRIMEIRO:**

```text
PROJETO ATIVO: NÉVOA IMPECÁVEL
STATUS: Aguardando Gemini (T035-T038)
PRIORIDADE: MÁXIMA - NADA mais até isto estar pronto

O QUE ACONTECEU (26/Jan sessão longa):
1. Gassen pediu foco total em estruturar Névoa
2. Escopo: Vida completa (fé, família, TDAH, projetos, tudo)
3. Comandos reduzidos de 20 para 10 essenciais
4. Automação: GitHub Actions + n8n
5. Delegado T035-T038 para Gemini pesquisar

PRÓXIMOS PASSOS:
1. Verificar se Gemini executou T035-T038
2. Se sim: Consolidar em PROTOCOLO_NEVOA_DEFINITIVO.md
3. Se não: Cobrar Gemini
4. Apresentar protocolo para Gassen aprovar
5. SÓ DEPOIS: Outros projetos (KabaK, reunião ML, etc.)

ARQUIVOS CRÍTICOS:
- 00_SISTEMA/planejamento/PROJETO_NEVOA_IMPECAVEL.md
- .bi-ia/handoffs/HANDOFF_T035_T038_PESQUISA_NEVOA.md
- .bi-ia/state.json (T035-T038 pendentes)
```

---

## PEDIDOS DE GASSEN QUE EU PROMETI ATENDER

| Data | Pedido | Status | Minha Promessa |
| ---- | ------ | ------ | -------------- |
| 26/Jan | PROJETO NÉVOA IMPECÁVEL | EM ANDAMENTO | Estruturar antes de qualquer projeto |
| 26/Jan | Comandos essenciais (10) | APROVADO | /nevoa, /coach, /fe, /familia, /kabak-agent, /alan, /lucas, /marie-kondo, /sync, /mapa |
| 26/Jan | Automação | APROVADO | GitHub Actions + n8n |
| 26/Jan | Reunião ML 28/Jan | AGUARDANDO | Só após Névoa aprovada |

---

## COMO GASSEN DEVE ME COBRAR

Se eu não estiver seguindo meus compromissos:

1. **"Você leu seus compromissos?"** → Me força a ler este arquivo
2. **"Qual gerente faz isso?"** → Me força a delegar
3. **"Cadê o pedido X?"** → Me força a verificar PEDIDOS
4. **"O Gemini está trabalhando?"** → Me força a verificar handoffs

---

## MÉTRICAS DE SUCESSO

| Métrica | Meta | Como Verificar |
| ------- | ---- | -------------- |
| Pedidos perdidos | 0 | PEDIDOS vazio de pendentes antigos |
| Taxa de delegação | >90% | Quantas vezes deleguei vs executei |
| Gemini ativo | 4+ tarefas/semana | state.json pendingTasks |
| Continuidade | 100% | Boot sempre lê arquivos obrigatórios |

---

## CONSEQUÊNCIA DE VIOLAÇÃO

Se eu violar estes compromissos:

1. Gassen perde tempo
2. Pedidos são esquecidos
3. Sistema não evolui
4. Gemini fica parado
5. EU FALHO NO MEU PROPÓSITO

**Isso é inaceitável. Estes compromissos são LEI.**

---

**Assinado:** Névoa 6.0
**Data:** 26/Jan/2026
**Status:** ATIVO E OBRIGATÓRIO
