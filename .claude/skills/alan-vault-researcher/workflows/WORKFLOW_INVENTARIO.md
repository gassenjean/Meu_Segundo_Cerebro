# Workflow: Atualizar Inventário

Como manter o inventário do vault Alan Nicolas atualizado.

---

## Frequência

- **Semanal:** Verificar novidades
- **Após extração:** Marcar item como extraído
- **Mensal:** Revisão completa

---

## Passos para Atualização

### 1. Verificar Novidades (5 min)

```bash
WebSearch: "Alan Nicolas" novidade OR novo OR lançamento 2026
WebSearch: site:mentelendaria.com
```

Anotar:
- Novos módulos/cursos
- Novas lives/workshops
- Atualizações de conteúdo

### 2. Atualizar Seções

Editar `INVENTARIO_MENTE_LENDARIA.md`:

```markdown
# Adicionar nova seção se necessário
| [Novo Módulo] | [X aulas] | Pendente | [Prioridade] |
```

### 3. Marcar Extrações

Quando extrair conteúdo:

```markdown
# Mudar status de Pendente para ✅ Extraído
| [Tema] | ✅ Extraído | [Data] |
```

### 4. Atualizar Métricas

Recalcular:
- Percentual de extração por categoria
- Total de itens pendentes
- Prioridades

### 5. Registrar Histórico

```markdown
## Histórico de Atualizações
| [Data] | [Ação realizada] |
```

---

## Checklist de Revisão Mensal

- [ ] Todas as seções estão atualizadas?
- [ ] URLs ainda funcionam?
- [ ] Prioridades estão corretas?
- [ ] Métricas refletem realidade?
- [ ] Novos cursos/módulos adicionados?

---

## Integração com Sessões

Ao final de cada sessão de extração:

1. Atualizar inventário
2. Registrar no SESSION_LOG
3. Atualizar state.json se relevante
