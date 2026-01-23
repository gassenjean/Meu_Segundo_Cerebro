# PROTOCOLO: Sincronização Bi-IA (Claude ↔ Gemini)

**Versão:** 1.0
**Criado:** 23/Jan/2026
**Status:** ✅ OBRIGATÓRIO PARA AMBOS AGENTES

---

## Propósito

Garantir comunicação consistente e automática entre Claude Code e Gemini/Antigravity através de um estado compartilhado.

---

## Arquitetura

```
┌─────────────┐     ┌─────────────────┐     ┌─────────────┐
│   Claude    │────▶│   state.json    │◀────│   Gemini    │
│   Code      │     │   (Bridge)      │     │ Antigravity │
└─────────────┘     └─────────────────┘     └─────────────┘
```

**Arquivo central:** `.bi-ia/state.json`

---

## Protocolo Obrigatório

### AO INICIAR SESSÃO

Todo agente DEVE executar estes passos:

```
1. LER .bi-ia/state.json
2. VERIFICAR pendingTasks onde "to" = meu nome
3. EXECUTAR tarefas pendentes ANTES de qualquer nova tarefa
4. ATUALIZAR activeSession com meus dados
5. REGISTRAR lastSync com meu timestamp
```

**Código de verificação (pseudocódigo):**

```javascript
// Ao iniciar
const state = readJSON('.bi-ia/state.json');
const myTasks = state.pendingTasks.filter(t => t.to === 'claude' || t.to === 'gemini');

if (myTasks.length > 0) {
  console.log('TAREFAS PENDENTES PARA MIM:', myTasks);
  // Executar cada tarefa ANTES de começar nova sessão
}

// Atualizar sessão ativa
state.activeSession = {
  agent: 'claude', // ou 'gemini'
  startedAt: new Date().toISOString(),
  device: 'Alienware' // ou 'Desktop Casa'
};

writeJSON('.bi-ia/state.json', state);
```

### AO FINALIZAR SESSÃO

Todo agente DEVE executar estes passos:

```
1. MOVER tarefas completadas de pendingTasks para completedTasks
2. ADICIONAR novas tarefas em pendingTasks (se houver)
3. REGISTRAR erros em errors (se ocorreram)
4. LIMPAR activeSession
5. ATUALIZAR lastSync e lastUpdate
6. SALVAR state.json
```

### AO DELEGAR TAREFA

Formato obrigatório para nova tarefa:

```json
{
  "id": "T001",
  "from": "claude",
  "to": "gemini",
  "task": "Descrição clara da tarefa",
  "priority": "alta",
  "context": ["arquivo1.md", "arquivo2.md"],
  "criteria": ["Critério de sucesso 1", "Critério de sucesso 2"],
  "status": "pending",
  "created": "2026-01-23T02:00:00-03:00",
  "completed": null
}
```

---

## Estrutura do state.json

```json
{
  "meta": {
    "version": "1.0",
    "created": "ISO timestamp",
    "lastUpdate": "ISO timestamp",
    "lastAgent": "claude | gemini"
  },
  "activeSession": {
    "agent": "claude | gemini | null",
    "startedAt": "ISO timestamp | null",
    "device": "Alienware | Desktop Casa | null"
  },
  "pendingTasks": [
    {
      "id": "T001",
      "from": "agente origem",
      "to": "agente destino",
      "task": "descrição",
      "priority": "alta | media | baixa",
      "context": ["arquivos relevantes"],
      "criteria": ["critérios de sucesso"],
      "status": "pending",
      "created": "ISO timestamp",
      "completed": null
    }
  ],
  "completedTasks": [],
  "errors": [
    {
      "id": "E001",
      "agent": "quem errou",
      "error": "descrição do erro",
      "timestamp": "ISO timestamp",
      "resolved": false
    }
  ],
  "rules": {
    "RULE_ID": "descrição da regra"
  },
  "lastSync": {
    "claude": "ISO timestamp | null",
    "gemini": "ISO timestamp | null"
  }
}
```

---

## Regras de Formatação (Acordo Bi-IA)

Ambos agentes DEVEM seguir:

| Regra | Descrição | Exemplo Correto |
|-------|-----------|-----------------|
| MD040 | Code blocks com linguagem | ` ```bash ` não ` ``` ` |
| MD036 | Títulos com ### | `### Título` não `**Título**` |
| MD026 | Títulos sem : no final | `### Título` não `### Título:` |
| MD060 | Tabelas com espaços | `\| Texto \|` não `\|Texto\|` |

---

## Regras de Sincronização

| Regra | Descrição |
|-------|-----------|
| SYNC001 | SEMPRE ler state.json ao iniciar |
| SYNC002 | SEMPRE atualizar state.json ao finalizar |
| SYNC003 | Executar tarefas pendentes ANTES de novas |
| SYNC004 | Não sobrescrever tarefas do outro agente |
| SYNC005 | Manter histórico em completedTasks (últimas 20) |

---

## Fluxo de Exemplo

### Claude delegando para Gemini

```
1. Claude adiciona tarefa em pendingTasks:
   {
     "id": "T002",
     "from": "claude",
     "to": "gemini",
     "task": "Reorganizar pasta _inbox",
     "priority": "media",
     "status": "pending"
   }

2. Claude atualiza lastSync.claude

3. Claude finaliza sessão

4. Gemini inicia sessão

5. Gemini lê state.json

6. Gemini encontra T002 em pendingTasks

7. Gemini executa tarefa

8. Gemini move T002 para completedTasks com status "completed"

9. Gemini atualiza lastSync.gemini
```

---

## Checklist de Sessão

### Início

- [ ] Li `.bi-ia/state.json`?
- [ ] Verifiquei `pendingTasks` para mim?
- [ ] Executei tarefas pendentes?
- [ ] Atualizei `activeSession`?

### Fim

- [ ] Movi tarefas completas para `completedTasks`?
- [ ] Adicionei novas tarefas em `pendingTasks`?
- [ ] Registrei erros em `errors`?
- [ ] Limpei `activeSession`?
- [ ] Atualizei `lastSync` e `lastUpdate`?

---

## Integração com SESSION_LOG

O `state.json` NÃO substitui o SESSION_LOG. Ele complementa:

| Arquivo | Propósito |
|---------|-----------|
| `state.json` | Estado técnico, tarefas, sincronização |
| `SESSION_LOG.md` | Histórico humano, contexto, narrativa |

**Regra:** Sempre atualizar AMBOS.

---

## Localização

```
.bi-ia/
├── state.json           ← Estado compartilhado (CRÍTICO)
├── PROTOCOLO_BI_IA_SYNC.md  ← Este documento
└── archive/             ← Histórico de states antigos (opcional)
```

---

## Troubleshooting

### Conflito de estado

Se dois agentes editaram simultaneamente:
1. Verificar `lastUpdate` - quem editou por último?
2. Mesclar `pendingTasks` manualmente
3. Não perder tarefas de nenhum lado

### Tarefa não executada

Se Gemini/Claude não executou tarefa pendente:
1. Verificar se leu `state.json` no início
2. Adicionar em `errors` com descrição
3. Re-adicionar tarefa em `pendingTasks`

### State.json corrompido

1. Verificar backup em `archive/`
2. Se não houver, recriar com estrutura vazia
3. Registrar incidente

---

**Este protocolo é LEI para ambos agentes.**

**Criado:** 23/Jan/2026
**Autor:** Claude Code
**Para:** Claude Code + Gemini/Antigravity

**"Comunicação estruturada = zero erros de sincronização."**
