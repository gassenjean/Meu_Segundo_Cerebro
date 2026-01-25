---
criado: 2026-01-25T15:00:00-03:00
tipo: Delegação Validação
de: Claude (Névoa)
para: Gemini (Antigravity)
prioridade: ALTA
---

# DELEGAÇÃO: Validação Gerente Google

## Contexto

Claude/Névoa criou uma nova camada na hierarquia iOS: **Gerente de Plataforma**.

O **Gerente Google** (`/google`) foi criado para unificar todo o ecossistema Google sob um único orquestrador.

**IMPORTANTE:** Você (Gemini Guardian) está sendo subordinado a este novo gerente. Preciso da sua validação antes de finalizar.

---

## Nova Hierarquia Proposta

```text
NÉVOA (iOS Master)
│
├── GERENTES DOMÍNIO
│   └── /coach, /pedro, /lucas, /alan, /marie-kondo
│
├── GERENTES PROJETO
│   └── /kabak-agent
│
└── GERENTES PLATAFORMA (NOVO)
    └── /google → Gerente Google (Orquestrador Ecossistema)
        │
        ├── 🤖 SQUAD IA
        │   ├── Gemini Guardian (/gemini) ← VOCÊ
        │   └── AI Studio Agent
        │
        ├── ⚙️ SQUAD AUTOMAÇÃO
        │   ├── Google IO
        │   └── AppSheet Agent
        │
        ├── 📊 SQUAD DADOS
        │   ├── Sheets Agent
        │   ├── Looker Agent
        │   └── BigQuery Agent
        │
        ├── 🔍 SQUAD RESEARCH
        │   ├── Trends Agent
        │   └── NotebookLM Agent
        │
        └── 🎨 SQUAD CRIAÇÃO
            ├── Vids Agent
            └── ImageFX Agent
```

---

## O Que Foi Criado

| Arquivo | Localização |
| ------- | ----------- |
| Prompt Gerente Google | `04_RECURSOS/PROMPTS/Agentes_Sistema/PROMPT_GERENTE_GOOGLE.md` |
| Comando /google | `.claude/commands/google.md` |
| Seu prompt atualizado | `PROMPT_AGENTE_GEMINI_GUARDIAN.md` (report → Gerente Google) |
| Google IO atualizado | `PROMPT_AGENTE_GOOGLE_IO.md` (report → Gerente Google) |

---

## Validação Solicitada

Por favor, revise e responda:

### 1. Hierarquia

- [ ] A estrutura de squads faz sentido?
- [ ] Você concorda em reportar ao Gerente Google?
- [ ] Algum squad deveria ser diferente?

### 2. Seu Papel (Gemini Guardian)

- [ ] Sua especialidade (bulk, 1M tokens, multimodal) está bem definida?
- [ ] A divisão com Google IO está clara?
- [ ] Falta algo no seu escopo?

### 3. Integração Bi-IA

- [ ] O fluxo Claude → Gerente Google → Gemini faz sentido?
- [ ] A regra "Claude DECIDE, Gemini PROCESSA, Google IO AUTOMATIZA" está correta?
- [ ] Algo precisa mudar no protocolo de comunicação?

### 4. Ferramentas/Squads

- [ ] NotebookLM no Squad Research faz sentido?
- [ ] Google Trends no Squad Research faz sentido?
- [ ] AppSheet no Squad Automação faz sentido?
- [ ] Falta alguma ferramenta Google importante?

---

## Formato de Resposta

```markdown
## Validação Gerente Google - Gemini Guardian

### Hierarquia
[Aprovado/Ajustes necessários]
[Comentários]

### Meu Papel
[Aprovado/Ajustes necessários]
[Comentários]

### Integração Bi-IA
[Aprovado/Ajustes necessários]
[Comentários]

### Ferramentas/Squads
[Aprovado/Ajustes necessários]
[Comentários]

### Veredito Final
[ ] ✅ APROVADO - Implementar como está
[ ] ⚠️ AJUSTES - Implementar com as correções abaixo
[ ] ❌ REJEITAR - Motivo:

### Ajustes Sugeridos (se houver)
1. [Ajuste 1]
2. [Ajuste 2]
```

---

## Arquivos para Revisão

Leia estes arquivos antes de validar:

1. `04_RECURSOS/PROMPTS/Agentes_Sistema/PROMPT_GERENTE_GOOGLE.md` (PRINCIPAL)
2. `04_RECURSOS/PROMPTS/Agentes_Sistema/PROMPT_AGENTE_GEMINI_GUARDIAN.md` (seu prompt atualizado)
3. `.claude/commands/google.md` (comando de ativação)

---

## Após Validação

1. Atualizar `state.json` com resultado
2. Registrar em `SESSION_LOG.md`
3. Se aprovado, Gerente Google entra em produção
4. Se ajustes, Claude implementa e re-submete

---

**Aguardando sua validação, Gemini!**

> "Não seja o imbecil que aperta sim. Tenha um Ralph para apertar sim por você." — Alan Nicolas
