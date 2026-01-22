# Nomenclatura KabaK - Regras de Naming

**Versao:** 2.0
**Baseado em:** 00_SISTEMA/PADROES/NOMENCLATURA.md

---

## 1. PREFIXOS VALIDOS

| Prefixo | Uso | Localizacao | Exemplo |
|---------|-----|-------------|---------|
| `RESUMO_REUNIAO_` | Resumos de reuniao | `docs/reunioes/` | `RESUMO_REUNIAO_DR_ALEXANDRE_21JAN2026.md` |
| `RESUMO_EXECUTIVO_` | Resumos executivos | `docs/reunioes/` | `RESUMO_EXECUTIVO_REUNIAO_TITANIUM_16JAN2026.md` |
| `RESUMO_FINANCEIRO_` | Analises financeiras | `docs/financeiro/` | `RESUMO_FINANCEIRO_SANSOM.md` |
| `BRIEFING_` | Briefings stakeholders | `docs/` | `BRIEFING_DR_ALEXANDRE_19JAN2026.md` |
| `PLANO_` | Planos de acao | `planejamento/` | `PLANO_Estruturacao_Legal_KabaK.md` |
| `PLANILHA_` | Planilhas/projecoes | `planejamento/` | `PLANILHA_FINANCEIRA_12_MESES.md` |
| `CHECKLIST_` | Checklists | `docs/` | `CHECKLIST_ENVIO_SANSOM.md` |
| `STATUS_` | Status reports | raiz projeto | `STATUS_ATUAL.md` |
| `TRANSCRICAO_` | Transcricoes brutas | `docs/` | `TRANSCRICAO_REUNIAO_SANSOM.md` |
| `ANALISE_` | Analises | `docs/` | `ANALISE_REUNIAO_TITANIUM.md` |
| `DOSSIE_` | Dossies completos | `docs/` | `DOSSIE_FINANCEIRO_ANALISE_TRIBUTARIA.md` |
| `PROPOSTA_` | Propostas | `planejamento/` | `PROPOSTA_FINAL_KABAK_SANSOM.md` |
| `COMUNICADO_` | Comunicados | `docs/reunioes/` | `COMUNICADO_SANSOM_NEGOCIACAO.md` |
| `MENSAGEM_` | Mensagens enviadas | `docs/reunioes/` | `MENSAGEM_ENVIO_DR_ALEXANDRE_19JAN2026.md` |
| `PESQUISA_` | Pesquisas e estudos | `docs/` ou `docs/pesquisas/` | `PESQUISA_ALAN_NICOLAS_22JAN2026.md` |
| `AUDITORIA_` | Auditorias | `docs/` | `AUDITORIA_ALAN_KABAK.md` |
| `TODO_` | Listas de tarefas | `tarefas/` | `TODO_Sprint_Atual.md` |
| `DASHBOARD` | Dashboard metricas | `metricas/` | `DASHBOARD.md` |
| `README` | Visao geral | qualquer pasta | `README.md` |
| `VALORES_OFICIAIS` | Fonte unica numeros | raiz projeto | `VALORES_OFICIAIS.md` |
| `_MOC_` | Indice master | raiz projeto | `_MOC_KabaK.md` |
| `CHECKPOINT_` | Snapshots | `checkpoints/` | `CHECKPOINT_19DEZ2025_Proposta_Titanium.md` |

---

## 2. REGRAS DE FORMATACAO

### 2.1 Prefixos
- **SEMPRE UPPERCASE** (RESUMO_, nao Resumo_)
- **Underscore apos prefixo** (BRIEFING_, nao BRIEFING-)

### 2.2 Nomes Proprios
- **CamelCase para pessoas:** `Dr_Alexandre`, `Sansom`, `Titanium`
- **UPPERCASE para siglas:** `KabaK`, `ROI`, `KPI`

### 2.3 Datas
- **Formato:** DDMMMYYYY (21JAN2026)
- **NAO usar:** 21-01-2026, 2026-01-21, 21/01/2026
- **Posicao:** SEMPRE no final do nome

### 2.4 Separadores
- **Usar:** Underscores `_`
- **NAO usar:** Espacos, hifens `-`, pontos `.`

### 2.5 Tamanho
- **Maximo:** 60 caracteres (sem extensao .md)
- **Minimo:** Prefixo + 1 palavra descritiva

---

## 3. FRONTMATTER PADRAO (PT-BR)

```yaml
---
criado: YYYY-MM-DDTHH:MM:SS-03:00
atualizado: YYYY-MM-DDTHH:MM:SS-03:00
tipo: [resumo_reuniao|briefing|plano|status|analise|dashboard|checklist]
status: [ativo|concluido|arquivado|em_revisao]
prioridade: [critica|alta|media|baixa]  # opcional
---
```

**IMPORTANTE:**
- Usar `criado` e `atualizado` (PT-BR)
- NAO usar `created` e `updated` (EN)
- Timezone: -03:00 (Brasilia)

---

## 4. MAPEAMENTO TIPO → LOCALIZACAO

| Tipo de Arquivo | Pasta Correta |
|-----------------|---------------|
| Reunioes, resumos reuniao | `docs/reunioes/` |
| Briefings, checklists | `docs/` |
| Transcricoes, analises | `docs/` |
| Planos, planilhas, propostas | `planejamento/` |
| Tarefas, TODOs | `tarefas/` |
| Metricas, dashboards | `metricas/` |
| Checkpoints | `checkpoints/` |
| Status projeto | raiz (`02_PROJETOS/KabaK/`) |
| MOC projeto | raiz (`02_PROJETOS/KabaK/`) |
| Valores oficiais | raiz (`02_PROJETOS/KabaK/`) |

---

## 5. VALIDACAO AUTOMATICA

Antes de criar qualquer arquivo, o sistema deve validar:

1. **Prefixo valido?** → Consultar tabela secao 1
2. **Localizacao correta?** → Consultar tabela secao 4
3. **Nome < 60 chars?** → Contar caracteres
4. **Data no formato correto?** → DDMMMYYYY
5. **Frontmatter PT-BR?** → criado/atualizado (nao created/updated)
6. **Arquivo ja existe?** → Evitar duplicatas

**Script:** `scripts/validate_before_create.py`

---

## 6. EXEMPLOS CORRETOS vs INCORRETOS

### Corretos
```
RESUMO_REUNIAO_DR_ALEXANDRE_21JAN2026.md
BRIEFING_SANSOM_PROPOSTA_PARCERIA.md
PLANO_Estruturacao_Legal_KabaK.md
CHECKLIST_ENVIO_SANSOM.md
STATUS_ATUAL.md
```

### Incorretos
```
Reuniao_Dr_Alexandre.md          # Prefixo minusculo
resumo-reuniao-sansom.md         # Hifens, tudo minusculo
BRIEFING DR ALEXANDRE.md         # Espacos
RESUMO_REUNIAO_21-01-2026.md     # Data formato errado
Meeting_Notes_Titanium.md        # Prefixo ingles
```

---

## 7. ARQUIVOS ESPECIAIS (FONTE UNICA)

Estes arquivos sao UNICOS e nao devem ser duplicados:

| Arquivo | Funcao | Localizacao |
|---------|--------|-------------|
| `STATUS_ATUAL.md` | Estado atual projeto | raiz |
| `VALORES_OFICIAIS.md` | Numeros oficiais | raiz |
| `_MOC_KabaK.md` | Indice master | raiz |
| `DASHBOARD.md` | Metricas | metricas/ |
| `TODO_Sprint_Atual.md` | Sprint atual | tarefas/ |
| `BACKLOG.md` | Backlog | tarefas/ |
| `CONCLUIDAS.md` | Tarefas feitas | tarefas/ |

**Regra:** Se ja existe, ATUALIZAR. Nunca criar versao 2, v2, _novo, etc.

---

**Versao:** 2.0
**Criado:** 22/Jan/2026
**Mantido por:** Skill KabaK
