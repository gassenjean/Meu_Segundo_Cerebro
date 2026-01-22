---
name: kabak
description: KabaK e-commerce project management. Use for meetings, briefings, status updates, financial reports. Validates naming before creating files. Investment R$ 2.096.300.
version: 2.0
---

# KabaK Project Skill v2.0

Skill para gestao do projeto KabaK - e-commerce de moda fitness feminina.

## Quando Usar

- Processar reunioes (KabaK, Sansom, Dr. Alexandre, Titanium)
- Criar briefings para stakeholders
- Atualizar status, tarefas, metricas
- Gerar projecoes financeiras
- Qualquer tarefa mencionando "KabaK", "Sansom", "sociedade"

## Contexto Rapido

| Metrica | Valor |
|---------|-------|
| **Investimento** | R$ 2.096.300 (VALORES_OFICIAIS.md) |
| **Parceria** | Sansom 51% decisao / Jean 49% |
| **Lucro** | 50% Sansom / 50% Jean+Gassen+Kris |
| **Produto** | Kit 3 pecas R$ 129 (custo ~R$ 48) |
| **Lancamento** | Mai/2026 |
| **Break-even** | Mes 4 (Ago/2026) |

**Stakeholders:** Sansom (investidor), Jean (fabrica), Gassen (projeto), Kris (producao), Titanium (marketing), Dr. Alexandre (juridico)

## Workflows

| Workflow | Trigger | Detalhes |
|----------|---------|----------|
| **Reuniao** | Transcricao, meeting, call | `references/workflows/WORKFLOW_REUNIAO.md` |
| **Briefing** | Documento para stakeholder | `references/workflows/WORKFLOW_BRIEFING.md` |
| **Status** | Atualizar progresso | `references/workflows/WORKFLOW_STATUS.md` |
| **Financeiro** | Projecoes, ROI, custos | `references/workflows/WORKFLOW_FINANCEIRO.md` |

**Consultar workflow detalhado ANTES de executar.**

## Validacao Obrigatoria

**ANTES de criar arquivo:**

```bash
python scripts/validate_before_create.py "NOME_ARQUIVO.md" "pasta/destino"
```

**DEPOIS de criar arquivo:**

```bash
python scripts/update_moc.py "caminho/completo/arquivo.md"
```

**Regras:** `references/nomenclatura_kabak.md`

## Templates

Todos em `assets/templates/`:

| Template | Uso |
|----------|-----|
| TEMPLATE_RESUMO_REUNIAO.md | Resumos de reuniao |
| TEMPLATE_BRIEFING.md | Briefings stakeholders |
| TEMPLATE_PLANO.md | Planos de acao |
| TEMPLATE_STATUS.md | Status projeto |
| TEMPLATE_DASHBOARD.md | Dashboard metricas |
| TEMPLATE_RESUMO_FINANCEIRO.md | Analises financeiras |
| TEMPLATE_TODO_SPRINT.md | Sprint tarefas |

**Usar template sem modificar estrutura base.**

## Referencias (Carregar Sob Demanda)

| Referencia | Quando Carregar |
|------------|-----------------|
| `estrutura_societaria.md` | Participacoes, governanca |
| `produto_tecnico.md` | Custos, producao, margem |
| `stakeholders.md` | Perfis envolvidos |
| `metricas_kpis.md` | Numeros, projecoes |
| `nomenclatura_kabak.md` | Regras de naming |

## Scripts

| Script | Funcao |
|--------|--------|
| `validate_before_create.py` | Validar nome/local antes de criar |
| `update_moc.py` | Atualizar MOC apos criar |
| `excel_calculator.py` | Calculos financeiros |
| `meeting_extractor.py` | Extrair action items |

## Arquivos Fonte Unica

**NAO duplicar - apenas atualizar:**

- `STATUS_ATUAL.md` - Estado geral
- `VALORES_OFICIAIS.md` - Numeros oficiais
- `_MOC_KabaK.md` - Indice master
- `DASHBOARD.md` - Metricas
- `TODO_Sprint_Atual.md` - Sprint atual

## Principios

1. **VALORES_OFICIAIS.md** e fonte unica de numeros
2. **Validar ANTES** de criar (script)
3. **Atualizar MOC DEPOIS** de criar (script)
4. **Templates sao lei** - nao modificar estrutura
5. **Frontmatter PT-BR** - criado/atualizado (nao created/updated)
6. **Cascata** - STATUS → DASHBOARD → TODO

## Frontmatter Padrao

```yaml
---
criado: YYYY-MM-DDTHH:MM:SS-03:00
atualizado: YYYY-MM-DDTHH:MM:SS-03:00
tipo: [resumo_reuniao|briefing|plano|status|analise]
status: [ativo|concluido|arquivado]
---
```

## Nomenclatura Rapida

| Prefixo | Local |
|---------|-------|
| RESUMO_REUNIAO_ | docs/reunioes/ |
| BRIEFING_ | docs/ |
| PLANO_ | planejamento/ |
| PLANILHA_ | planejamento/ |
| CHECKLIST_ | docs/ |
| STATUS_ | raiz |

**Data:** DDMMMYYYY (21JAN2026)
**Detalhes:** `references/nomenclatura_kabak.md`

---

**Version:** 2.0
**Updated:** 22/Jan/2026
**Changes:** Progressive disclosure, validacao obrigatoria, workflows em references/
