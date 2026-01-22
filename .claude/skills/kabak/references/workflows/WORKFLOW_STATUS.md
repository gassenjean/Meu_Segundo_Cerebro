# Workflow: Atualizar Status

**Versao:** 2.0
**Trigger:** Atualizacao de progresso, mudanca de status, revisao semanal

---

## 1. IDENTIFICAR TIPO DE ATUALIZACAO

**Perguntar:**
- O que mudou?
- E atualizacao pontual ou revisao completa?
- Alguma tarefa foi concluida?

**Tipos:**
| Tipo | Frequencia | Escopo |
|------|-----------|--------|
| Pontual | Ad-hoc | 1 item especifico |
| Post-reuniao | Apos cada reuniao | Decisoes e action items |
| Revisao semanal | Friday 17h | Todos os 3 arquivos |

---

## 2. ARQUIVOS A ATUALIZAR

**Trio de status (sempre sincronizados):**

| Arquivo | Funcao | Localizacao |
|---------|--------|-------------|
| `STATUS_ATUAL.md` | Estado geral projeto | Raiz projeto |
| `TODO_Sprint_Atual.md` | Tarefas em andamento | tarefas/ |
| `DASHBOARD.md` | Metricas e KPIs | metricas/ |

**Regra:** Mudanca em um deve refletir nos outros.

---

## 3. ATUALIZAR STATUS_ATUAL.md

**Secoes a verificar:**

### Progresso Geral
```markdown
## Status Rapido
| Metrica | Valor |
|---------|-------|
| Progresso | [X]% |
| Fase Atual | [Fase] |
| Proxima Entrega | [Data] |
```

### Frentes Ativas
```markdown
### 1. [Frente]
- **Status:** [emoji] [descricao]
- **Proxima entrega:** [data]
- **Bloqueadores:** [se houver]
```

**Emojis padrao:**
- 🟢 Em andamento/OK
- 🟡 Atencao/Aguardando
- 🔴 Bloqueado/Critico
- ✅ Concluido

### Timeline
- Atualizar se houver mudancas de datas
- Marcar marcos concluidos

---

## 4. ATUALIZAR TODO_Sprint_Atual.md

**Estrutura:**
```markdown
## Sprint Atual (DD/MMM - DD/MMM)

### 🔴 Criticas
- [ ] Tarefa 1 - @responsavel - ate DD/MMM
- [x] Tarefa concluida

### 🟡 Importantes
- [ ] Tarefa 2 - @responsavel - ate DD/MMM

### 🟢 Nice-to-have
- [ ] Tarefa 3
```

**Acoes:**
1. Mover tarefas concluidas para `CONCLUIDAS.md`
2. Adicionar novas tarefas de reunioes
3. Ajustar prioridades se necessario
4. Atualizar responsaveis e prazos

---

## 5. ATUALIZAR DASHBOARD.md

**Metricas a verificar:**

### Financeiras
- Investimento total: R$ 2.096.300 (VALORES_OFICIAIS.md)
- Gastos ate data
- Runway

### Progresso
- % conclusao por frente
- Tarefas concluidas vs pendentes

### Timeline
- Proximos marcos
- Desvios de cronograma

**Formato tabela:**
```markdown
| KPI | Meta | Atual | Status |
|-----|------|-------|--------|
| [KPI] | [valor] | [valor] | [emoji] |
```

---

## 6. MOVER PARA CONCLUIDAS.md

**Quando tarefa concluida:**
1. Remover de TODO_Sprint_Atual.md
2. Adicionar em CONCLUIDAS.md com data

**Formato:**
```markdown
## Jan/2026

### Semana 20-26
- [x] Tarefa concluida - @responsavel - 22/Jan
```

---

## 7. VALIDAR CONSISTENCIA

**Checklist:**
- [ ] Progresso % consistente entre arquivos
- [ ] Datas proximas entregas batem
- [ ] Tarefas nao duplicadas
- [ ] Numeros validados contra VALORES_OFICIAIS.md
- [ ] Emojis de status consistentes

---

## 8. ATUALIZAR MOC (SE NECESSARIO)

**Quando atualizar MOC:**
- Nova frente adicionada
- Estrutura de pastas mudou
- Arquivos criados/removidos

**NAO atualizar MOC para:**
- Mudancas de conteudo apenas
- Atualizacoes de progresso %

---

## REVISAO SEMANAL (Friday 17h)

**Checklist completo:**

### STATUS_ATUAL.md
- [ ] Progresso % atualizado
- [ ] Frentes com status correto
- [ ] Timeline atualizada
- [ ] Bloqueadores documentados

### TODO_Sprint_Atual.md
- [ ] Tarefas concluidas movidas
- [ ] Novas tarefas adicionadas
- [ ] Prioridades revisadas
- [ ] Prazos atualizados

### DASHBOARD.md
- [ ] Metricas atualizadas
- [ ] KPIs verificados
- [ ] Graficos/tabelas atuais

### CONCLUIDAS.md
- [ ] Tarefas da semana registradas
- [ ] Formatacao consistente

### _MOC_KabaK.md
- [ ] Links funcionando
- [ ] Novos arquivos adicionados
- [ ] Arquivos removidos excluidos

---

## CHECKLIST FINAL

- [ ] Tipo atualizacao identificado
- [ ] STATUS_ATUAL.md atualizado
- [ ] TODO_Sprint_Atual.md atualizado
- [ ] DASHBOARD.md atualizado
- [ ] CONCLUIDAS.md atualizado (se tarefas concluidas)
- [ ] Consistencia validada
- [ ] Timestamps atualizados (frontmatter)

---

**Versao:** 2.0
**Criado:** 22/Jan/2026
