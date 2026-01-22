---
criado: 2026-01-22T15:00:00-03:00
atualizado: 2026-01-22T15:00:00-03:00
tipo: arquitetura
status: em_revisao
versao: 2.0-draft
---

# ARQUITETURA: Skill KabaK v2.0

**Objetivo:** Definir nova arquitetura robusta baseada em boas práticas (Skill Creator + Alan Nicolas)
**Status:** Em revisao (aguardando aprovacao)
**Criado:** 22/Jan/2026

---

## 1. PROBLEMAS DA SKILL ATUAL (v1.1)

| # | Problema | Impacto | Solucao v2.0 |
|---|----------|---------|--------------|
| 1 | SKILL.md muito longo (309 linhas) | Consome tokens desnecessarios | Progressive disclosure |
| 2 | Nomenclatura inconsistente templates | `TEMPLATE_Reuniao.md` vs `TEMPLATE_BRIEFING.md` | Padronizar UPPERCASE |
| 3 | Nao valida antes de criar arquivos | Arquivos criados fora do padrao | Script validacao |
| 4 | Nao atualiza MOCs automaticamente | MOC desatualizado | Script update_moc |
| 5 | Scripts sao placeholders | Nao funcionam | Implementar funcionais |
| 6 | Investimento desatualizado | R$ 2.6M (errado) vs R$ 2.096.300 (oficial) | Corrigir todas referencias |
| 7 | Workflows duplicados | Info em SKILL.md E references | Mover para references/workflows/ |

---

## 2. PRINCIPIOS DA NOVA ARQUITETURA

### 2.1 Progressive Disclosure (Skill Creator)

```
NIVEL 1: Metadata (name + description)     ~100 palavras  [SEMPRE CARREGADO]
NIVEL 2: SKILL.md body                     ~150 linhas    [QUANDO SKILL ATIVA]
NIVEL 3: references/, assets/, scripts/   Ilimitado      [SOB DEMANDA]
```

**Regra:** SKILL.md deve ter <200 linhas. Detalhes vao para references/.

### 2.2 Metodologia 5C (Alan Nicolas)

```
CONSUMIR → CAPTURAR → CONECTAR → CRIAR → COMPARTILHAR
    ↓          ↓           ↓         ↓           ↓
 Reuniao    _inbox/      Links    Briefing    Enviar
 Pesquisa   Notas       MOC      Planilha    Sansom
```

**Aplicacao:**
- Reunioes chegam brutas → capturar em docs/reunioes/
- Conectar com VALORES_OFICIAIS.md (fonte unica)
- Criar documentos finais usando templates
- Compartilhar via checklist de envio

### 2.3 Integracao Bi-IA

| IA | Funcao | Quando Usar |
|----|--------|-------------|
| **Gemini** | Bulk, leitura massiva (1M tokens) | Consolidar docs, processar transcricoes longas |
| **Claude** | Arquitetura, logica, validacao | Estruturar, calcular, validar padroes |

### 2.4 Validacao Automatica

**ANTES de criar qualquer arquivo:**
1. Verificar NOMENCLATURA.md
2. Verificar localizacao correta
3. Verificar se ja existe
4. Validar frontmatter

**Script:** `scripts/validate_before_create.py`

---

## 3. NOVA ESTRUTURA DE PASTAS

```
.claude/skills/kabak/
├── SKILL.md                          # Enxuto (~150 linhas)
├── ARQUITETURA_V2.md                 # Este documento
│
├── references/                       # Dados estaticos (carregar sob demanda)
│   ├── estrutura_societaria.md       # [EXISTENTE] Participacoes, lucros
│   ├── produto_tecnico.md            # [EXISTENTE] Custos, margem, producao
│   ├── stakeholders.md               # [EXISTENTE] Perfis detalhados
│   ├── metricas_kpis.md              # [EXISTENTE] Projecoes financeiras
│   │
│   ├── workflows/                    # [NOVO] Workflows detalhados
│   │   ├── WORKFLOW_REUNIAO.md       # Passo-a-passo processar reuniao
│   │   ├── WORKFLOW_BRIEFING.md      # Passo-a-passo criar briefing
│   │   ├── WORKFLOW_STATUS.md        # Passo-a-passo atualizar status
│   │   └── WORKFLOW_FINANCEIRO.md    # Passo-a-passo analise financeira
│   │
│   └── nomenclatura_kabak.md         # [NOVO] Regras naming especificas KabaK
│
├── assets/
│   └── templates/                    # Templates padronizados (UPPERCASE)
│       ├── TEMPLATE_RESUMO_REUNIAO.md
│       ├── TEMPLATE_BRIEFING.md
│       ├── TEMPLATE_STATUS.md
│       ├── TEMPLATE_PLANO.md
│       ├── TEMPLATE_DASHBOARD.md
│       └── TEMPLATE_TODO_SPRINT.md
│
├── scripts/                          # Automacoes funcionais
│   ├── validate_before_create.py     # [NOVO] Valida antes de criar
│   ├── update_moc.py                 # [NOVO] Atualiza _MOC_KabaK.md
│   ├── excel_calculator.py           # [EXISTENTE] Calculos financeiros
│   └── meeting_extractor.py          # [EXISTENTE] Extrair action items
│
└── prompts/                          # [NOVO] Personas
    └── system_prompt.md              # Persona KabaK Agent
```

---

## 4. SKILL.MD v2.0 (ESTRUTURA)

### 4.1 Frontmatter
```yaml
---
name: kabak
description: KabaK e-commerce project management. Use for meetings, briefings, status, financials. Validates naming before creating files.
version: 2.0
---
```

### 4.2 Secoes (max 150 linhas)

```markdown
# KabaK Project Skill v2.0

## Quando Usar
- Processar reunioes KabaK/Sansom
- Criar briefings para stakeholders
- Atualizar status e metricas
- Gerar projecoes financeiras

## Contexto Rapido
- Parceria: Sansom (51%) + Jean/Gassen/Kris (49%)
- Lucro: 50/50
- Investimento: R$ 2.096.300 (FONTE UNICA: VALORES_OFICIAIS.md)
- Lancamento: Mai/2026

## Workflows Disponiveis
1. **Reuniao** → `references/workflows/WORKFLOW_REUNIAO.md`
2. **Briefing** → `references/workflows/WORKFLOW_BRIEFING.md`
3. **Status** → `references/workflows/WORKFLOW_STATUS.md`
4. **Financeiro** → `references/workflows/WORKFLOW_FINANCEIRO.md`

## Validacao Obrigatoria
**ANTES de criar arquivo:**
1. Executar `scripts/validate_before_create.py`
2. Seguir `references/nomenclatura_kabak.md`
3. Atualizar MOC via `scripts/update_moc.py`

## Templates
Todos em `assets/templates/`. Usar sem modificar estrutura.

## Referencias (Carregar Sob Demanda)
- estrutura_societaria.md → Participacoes, governanca
- produto_tecnico.md → Custos, producao
- stakeholders.md → Perfis envolvidos
- metricas_kpis.md → Numeros e projecoes

## Principios
1. VALORES_OFICIAIS.md e fonte unica de numeros
2. Validar ANTES de criar
3. Atualizar MOC DEPOIS de criar
4. Templates sao lei (nao modificar estrutura)
```

---

## 5. SCRIPTS FUNCIONAIS

### 5.1 validate_before_create.py

**Funcao:** Validar arquivo antes de criar

**Input:** nome proposto, tipo, localizacao
**Output:** OK ou lista de erros

**Validacoes:**
- [ ] Nome segue NOMENCLATURA.md
- [ ] Prefixo correto para o tipo
- [ ] Localizacao correta (docs/, planejamento/, etc)
- [ ] Frontmatter padrao PT-BR
- [ ] Arquivo nao existe (evitar duplicata)

### 5.2 update_moc.py

**Funcao:** Atualizar _MOC_KabaK.md apos criar arquivo

**Input:** caminho do arquivo criado
**Output:** MOC atualizado

**Acoes:**
- [ ] Identificar secao correta no MOC
- [ ] Adicionar link wiki [[arquivo.md]]
- [ ] Atualizar timestamp do MOC

### 5.3 excel_calculator.py (existente - manter)

**Funcao:** Calculos financeiros complexos

### 5.4 meeting_extractor.py (existente - manter)

**Funcao:** Extrair action items de transcricoes

---

## 6. REFERENCIAS DETALHADAS

### 6.1 references/workflows/WORKFLOW_REUNIAO.md

```markdown
# Workflow: Processar Reuniao

## Trigger
Usuario menciona: reuniao, transcricao, meeting, call, ligacao

## Passos
1. CAPTURAR: Pedir transcricao ou narrar pontos
2. IDENTIFICAR: Quem participou? (consultar stakeholders.md)
3. EXTRAIR: Decisoes, action items, prazos
4. VALIDAR: Verificar nome arquivo (validate_before_create.py)
5. CRIAR: Usar TEMPLATE_RESUMO_REUNIAO.md
6. SALVAR: Em docs/reunioes/RESUMO_REUNIAO_[TEMA]_[DATA].md
7. ATUALIZAR: MOC (update_moc.py)
8. CASCATA: TODO_Sprint_Atual.md, DASHBOARD.md se relevante

## Nomenclatura
- RESUMO_REUNIAO_[STAKEHOLDER]_[DDMMMYYYY].md
- Exemplo: RESUMO_REUNIAO_DR_ALEXANDRE_21JAN2026.md

## Frontmatter Obrigatorio
criado, atualizado, tipo: resumo_reuniao, participantes, status
```

### 6.2 references/nomenclatura_kabak.md

```markdown
# Nomenclatura KabaK

## Prefixos Validos
| Prefixo | Uso | Local |
|---------|-----|-------|
| RESUMO_REUNIAO_ | Resumos de reuniao | docs/reunioes/ |
| RESUMO_FINANCEIRO_ | Analises financeiras | docs/financeiro/ |
| BRIEFING_ | Briefings stakeholders | docs/ |
| PLANO_ | Planos de acao | planejamento/ |
| CHECKLIST_ | Checklists | docs/ |
| STATUS_ | Status reports | raiz projeto |
| TRANSCRICAO_ | Transcricoes brutas | docs/ |
| ANALISE_ | Analises | docs/ |

## Regras
1. UPPERCASE para prefixos
2. CamelCase para nomes proprios (Dr_Alexandre, nao dr_alexandre)
3. Data: DDMMMYYYY (21JAN2026, nao 21-01-2026)
4. Underscores (nao espacos, nao hifens)
5. Max 60 caracteres

## Frontmatter Padrao (PT-BR)
criado: YYYY-MM-DDTHH:MM:SS-03:00
atualizado: YYYY-MM-DDTHH:MM:SS-03:00
tipo: [resumo_reuniao|briefing|plano|status|analise]
status: [ativo|concluido|arquivado]
```

---

## 7. MIGRACAO v1.1 → v2.0

### 7.1 Tarefas de Migracao

| # | Tarefa | Prioridade |
|---|--------|------------|
| 1 | Criar pasta references/workflows/ | Alta |
| 2 | Mover workflows de SKILL.md para references/workflows/ | Alta |
| 3 | Criar references/nomenclatura_kabak.md | Alta |
| 4 | Renomear templates (padronizar UPPERCASE) | Media |
| 5 | Implementar validate_before_create.py | Alta |
| 6 | Implementar update_moc.py | Media |
| 7 | Reescrever SKILL.md (versao enxuta) | Alta |
| 8 | Corrigir investimento R$ 2.096.300 em todas referencias | Alta |
| 9 | Criar prompts/system_prompt.md | Baixa |
| 10 | Sincronizar com .gemini/skills/kabak/ | Media |

### 7.2 Arquivos a Renomear

| De | Para |
|----|------|
| TEMPLATE_Reuniao.md | TEMPLATE_RESUMO_REUNIAO.md |
| TEMPLATE_Plano_Acao.md | TEMPLATE_PLANO.md |
| TEMPLATE_STATUS_PROJETO.md | TEMPLATE_STATUS.md |

### 7.3 Valores a Corrigir

| Arquivo | Valor Atual | Valor Correto |
|---------|-------------|---------------|
| SKILL.md | R$ 2.6M | R$ 2.096.300 |
| metricas_kpis.md | Verificar | R$ 2.096.300 |
| produto_tecnico.md | Verificar | Alinhar com VALORES_OFICIAIS.md |

---

## 8. CRITERIOS DE SUCESSO

1. **SKILL.md < 200 linhas** - Progressive disclosure
2. **Validacao obrigatoria** - Nenhum arquivo criado sem validar
3. **MOC atualizado** - Automaticamente apos criar arquivo
4. **Nomenclatura 100% consistente** - Todos prefixos UPPERCASE
5. **Fonte unica valores** - VALORES_OFICIAIS.md referenciado
6. **Scripts funcionais** - Executaveis, nao placeholders
7. **Skills sincronizadas** - Claude e Gemini com mesma versao

---

## 9. PROXIMOS PASSOS

Apos aprovacao desta arquitetura:

1. **3.2** Criar sistema de validacao automatica (scripts/validate_before_create.py)
2. **3.3** Criar templates padronizados com frontmatter obrigatorio
3. **3.4** Implementar nomenclatura automatica
4. **3.5** Criar workflow de atualizacao de MOCs automatico
5. **3.6** Sincronizar skills Claude e Gemini

---

**Criado por:** Claude Code (Opus 4.5)
**Baseado em:** Skill Creator + Pesquisa Alan Nicolas + Analise skill atual
**Versao:** 2.0-draft
**Status:** Aguardando aprovacao usuario
