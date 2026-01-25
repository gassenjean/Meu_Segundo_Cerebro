# CHECKPOINT: Comunicação Entre Agentes

**Data:** 23/Jan/2026 00:45
**Sessão:** Hierarquia Completa + Melhorias Comunicação
**Status:** PRONTO PARA IMPLEMENTAR

---

## CONTEXTO

### Hierarquia Implementada
```
VOCÊ
  ↓
NÉVOA ✅
  ├── GERENTE_CONHECIMENTO ✅
  ├── GERENTE_PROJETOS ✅
  ├── GERENTE_PRODUTIVIDADE ✅
  ├── GERENTE_FINANCAS ✅
  └── GUARDIAN ✅
```

### Problemas Identificados

1. **SESSION_LOG instável** - Conflitos OneDrive, arquivo sumindo
2. **Comunicação manual** - Claude escreve, Gemini lê, muito texto
3. **Sem protocolo de handoff** - Quem faz o quê não é claro
4. **Logs dispersos** - SESSION_LOG + PC_SYNC_LOG + checkpoints

---

## SUGESTÕES DE MELHORIA

### 1. SESSION_LOG Simplificado

**Problema:** Arquivo muito grande (74KB), conflitos OneDrive, formatação quebra.

**Solução:** Criar estrutura fixa com seções curtas.

```markdown
# SESSION_LOG

## ÚLTIMA ATUALIZAÇÃO
- **Quem:** Claude/Gemini
- **Quando:** 23/Jan/2026 00:45
- **O quê:** [1 linha]

## PENDÊNCIAS CLAUDE → GEMINI
- [ ] Tarefa 1
- [ ] Tarefa 2

## PENDÊNCIAS GEMINI → CLAUDE
- [ ] Tarefa 1
- [ ] Tarefa 2

## HISTÓRICO (últimas 10 entradas)
[entradas antigas vão para ARQUIVO]
```

**Ação:** Criar `PROTOCOLO_SESSION_LOG_V2.md` com regras:
- Máximo 30 entradas no LOG principal
- Arquivar antigas automaticamente (skill session-log-archiver)
- Formato padronizado (sem tabelas complexas que quebram)

---

### 2. Protocolo de Handoff Estruturado

**Problema:** Mensagens longas "Claude para Gemini!" são difíceis de parsear.

**Solução:** Formato JSON-like padronizado.

```markdown
## HANDOFF: Claude → Gemini

**ID:** H-20260123-001
**Tipo:** DELEGAÇÃO | INFORMAÇÃO | PERGUNTA
**Prioridade:** ALTA | MÉDIA | BAIXA
**Prazo:** Imediato | Hoje | Semana

### Tarefa
[1 parágrafo máximo]

### Contexto
- Arquivo 1: `caminho/arquivo.md`
- Arquivo 2: `caminho/outro.md`

### Critério de Sucesso
- [ ] Critério 1
- [ ] Critério 2

### Resposta Esperada
- Output em: `caminho/output.md`
- Atualizar: SESSION_LOG
```

**Ação:** Criar `TEMPLATE_HANDOFF.md` em `04_RECURSOS/TEMPLATES/`

---

### 3. Canal Único de Comunicação

**Problema:** Informação espalhada (SESSION_LOG, PC_SYNC_LOG, checkpoints, temp/).

**Solução:** Hierarquia clara.

```
SESSION_LOG.md (raiz)
├── Comunicação rápida Claude ↔ Gemini
├── Máximo 30 entradas
└── Formato padronizado

00_SISTEMA/LOGS/
├── SESSION_LOG_ARQUIVO_[MES]_[ANO].md  ← Histórico
└── HANDOFFS/                            ← Handoffs detalhados
    ├── H-20260123-001.md
    └── H-20260123-002.md

00_SISTEMA/CHECKPOINTS/
└── CHECKPOINT_[DATA]_[TEMA].md          ← Snapshots de sessão
```

**Ação:**
1. Criar pasta `00_SISTEMA/LOGS/HANDOFFS/`
2. Atualizar `PROTOCOLO_SINCRONIZACAO_AGENTES.md`

---

### 4. Gerentes com Comunicação Interna

**Problema:** Gerentes não se comunicam entre si.

**Solução:** Adicionar seção de dependências em cada gerente.

```markdown
## Comunicação com Outros Gerentes

### Eu Preciso De
| Gerente | Quando | O Quê |
|---------|--------|-------|
| GUARDIAN | Após organizar | Validar nomenclatura |
| CONHECIMENTO | Antes de criar | Verificar se já existe |

### Eu Forneço Para
| Gerente | Quando | O Quê |
|---------|--------|-------|
| PRODUTIVIDADE | Após criar tarefa | Notificar nova tarefa |
```

**Ação:** Adicionar seção em cada `gerente-*.md`

---

### 5. Loop Ralph como Verificador Central

**Problema:** Loop Ralph implementado mas não centralizado.

**Solução:** Guardian executa Loop Ralph para TODOS os gerentes.

```
Gerente executa ação
    ↓
Guardian verifica (Loop Ralph)
    ↓
Se OK → Registra em SESSION_LOG
Se FALHOU → Alerta + Reverte
```

**Ação:** Atualizar `guardian.md` com:
```markdown
## Integração com Gerentes

Guardian é o verificador central. Após qualquer ação de gerente:
1. Gerente notifica Guardian
2. Guardian executa Loop Ralph
3. Guardian atualiza SESSION_LOG
```

---

### 6. OneDrive-Proof SESSION_LOG

**Problema:** OneDrive cria conflitos (`SESSION_LOG-DESKTOP-5IOF0UE.md`).

**Solução:**
1. Manter SESSION_LOG pequeno (<50KB)
2. Usar formato que não quebra (sem tabelas complexas)
3. Script de limpeza de conflitos

**Ação:** Criar skill `clean-onedrive-conflicts` no Guardian:
```bash
# Detectar e resolver conflitos OneDrive
# Manter apenas a versão mais recente
```

---

## ARQUIVOS A CRIAR

| Arquivo | Localização | Prioridade |
|---------|-------------|------------|
| `PROTOCOLO_SESSION_LOG_V2.md` | `00_SISTEMA/PROTOCOLOS/` | ALTA |
| `TEMPLATE_HANDOFF.md` | `04_RECURSOS/TEMPLATES/` | ALTA |
| Pasta `HANDOFFS/` | `00_SISTEMA/LOGS/` | MÉDIA |
| Atualizar gerentes | `.agent/workflows/` | MÉDIA |
| Clean OneDrive script | Guardian | BAIXA |

---

## COMANDO PARA NOVA JANELA

```
Continuar melhorias comunicação agentes.

Ler:
1. 00_SISTEMA/CHECKPOINTS/CHECKPOINT_23JAN2026_Comunicacao_Agentes.md
2. SESSION_LOG.md (últimas 5 entradas)

Implementar:
1. PROTOCOLO_SESSION_LOG_V2.md (formato simplificado)
2. TEMPLATE_HANDOFF.md (comunicação estruturada)
3. Atualizar SESSION_LOG para novo formato
4. Limpar conflitos OneDrive

Foco: Zero erros no SESSION_LOG.
```

---

## RESUMO SESSÃO ATUAL

### Criados (6 arquivos)
- `.agent/workflows/nevoa.md` (expandido)
- `.agent/workflows/gerente-conhecimento.md`
- `.agent/workflows/gerente-projetos.md`
- `.agent/workflows/gerente-produtividade.md`
- `.agent/workflows/gerente-financas.md`
- `00_SISTEMA/PADROES/PADRAO_LOOP_RALPH.md`

### Corrigidos
- SESSION_LOG conflito OneDrive resolvido
- Plano hierarquia atualizado (Fases 1-3 completas)
- MOC_Padroes atualizado

### Gemini Entregou (4 análises)
- ANALISE_PROMPTS_UTEIS.md (Top 10 prompts)
- METODO_5C_APLICADO.md (5C no Bi-IA)
- COMPARACAO_iOS.md (Gap analysis)
- WORKFLOWS_ADAPTADOS.md (3 workflows MAPA)

---

---

## TAREFAS PARA GEMINI (Paralelo)

### Tarefa 1: Criar TEMPLATE_HANDOFF.md
```
DELEGAÇÃO: Claude → Gemini
ID: H-20260123-001
Tipo: CRIAÇÃO
Prioridade: ALTA

Criar template de handoff estruturado.

Requisitos:
- Formato markdown simples (sem tabelas complexas)
- Campos: ID, Tipo, Prioridade, Tarefa, Contexto, Critério de Sucesso
- Exemplos de uso (Claude→Gemini e Gemini→Claude)
- Máximo 50 linhas

Output: 04_RECURSOS/TEMPLATES/TEMPLATE_HANDOFF.md
```

### Tarefa 2: Limpar SESSION_LOG
```
DELEGAÇÃO: Claude → Gemini
ID: H-20260123-002
Tipo: MANUTENÇÃO
Prioridade: ALTA

Arquivar entradas antigas do SESSION_LOG.

Ações:
1. Ler SESSION_LOG.md atual
2. Manter apenas últimas 15 entradas
3. Mover antigas para 00_SISTEMA/LOGS/SESSION_LOG_ARQUIVO_JAN_2026.md
4. Limpar formatação quebrada
5. Remover tabelas complexas (usar listas)

Output: SESSION_LOG.md limpo (<30KB)
```

### Tarefa 3: Criar PROTOCOLO_SESSION_LOG_V2.md
```
DELEGAÇÃO: Claude → Gemini
ID: H-20260123-003
Tipo: DOCUMENTAÇÃO
Prioridade: MÉDIA

Documentar novo formato do SESSION_LOG.

Conteúdo:
- Formato padrão de entrada (sem tabelas)
- Limite de 30 entradas
- Regra de arquivamento
- Formato de handoff inline
- Anti-patterns (o que NÃO fazer)

Output: 00_SISTEMA/PROTOCOLOS/PROTOCOLO_SESSION_LOG_V2.md
```

### Tarefa 4: Detectar e Limpar Conflitos OneDrive
```
DELEGAÇÃO: Claude → Gemini
ID: H-20260123-004
Tipo: LIMPEZA
Prioridade: MÉDIA

Identificar e resolver arquivos de conflito.

Padrão: *-DESKTOP-*.md, *-aliengass*.md

Ações:
1. Listar todos os conflitos na raiz
2. Para cada conflito:
   - Comparar com versão principal
   - Manter versão mais completa
   - Deletar duplicata
3. Reportar ações em SESSION_LOG

Arquivos conhecidos:
- SESSION_LOG-DESKTOP-5IOF0UE.md
- PC_SYNC_LOG-aliengass.md
- PC_SYNC_LOG-aliengass-2.md
```

### Tarefa 5: Melhorar Descrições dos Workflows
```
DELEGAÇÃO: Claude → Gemini
ID: H-20260123-005
Tipo: DOCUMENTAÇÃO
Prioridade: BAIXA

Adicionar seção "Comunicação com Outros Gerentes" em cada workflow.

Arquivos:
- .agent/workflows/gerente-conhecimento.md
- .agent/workflows/gerente-projetos.md
- .agent/workflows/gerente-produtividade.md
- .agent/workflows/gerente-financas.md

Formato:
## Comunicação com Outros Gerentes
### Eu Preciso De
- [Gerente]: [Quando] → [O quê]
### Eu Forneço Para
- [Gerente]: [Quando] → [O quê]
```

---

## DIVISÃO DE TRABALHO

| Tarefa | Responsável | Prioridade |
|--------|-------------|------------|
| TEMPLATE_HANDOFF.md | Gemini | ALTA |
| Limpar SESSION_LOG | Gemini | ALTA |
| PROTOCOLO_SESSION_LOG_V2.md | Gemini | MÉDIA |
| Limpar conflitos OneDrive | Gemini | MÉDIA |
| Comunicação entre gerentes | Gemini | BAIXA |
| Validar entregas | Claude | - |
| Testar fluxo | Claude | - |

---

**Criado:** 23/Jan/2026 00:45
**Para:** Próxima sessão Claude + Gemini paralelo
**Tokens usados:** ~104k/200k (52%)

**"Comunicação clara = menos erros = mais produtividade."**
