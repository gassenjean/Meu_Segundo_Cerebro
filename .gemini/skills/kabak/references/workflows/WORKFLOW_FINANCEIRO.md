# Workflow: Analise Financeira

**Versao:** 2.0
**Trigger:** Projecoes, ROI, custos, planilhas, numeros financeiros

---

## 1. FONTE UNICA DE VERDADE

**SEMPRE consultar primeiro:** `VALORES_OFICIAIS.md`

**Valores oficiais (Jan/2026):**
| Metrica | Valor | Nota |
|---------|-------|------|
| Investimento Total | R$ 2.096.300 | Fonte unica |
| Sansom (50% lucro) | R$ 1.053.150 | Aporte |
| Jean+Gassen+Kris (50%) | R$ 1.053.150 | Aporte |
| Custo Kit | ~R$ 48 | Tecido + producao + embalagem |
| Preco Venda Kit | R$ 129 | D2C |
| Margem Bruta | ~45% | Apos custos variaveis |
| Break-even | Mes 4 (Ago/2026) | Lancamento Mai/2026 |
| ROI Ano 1 | 155% | Projecao |

**Se usuario mencionar valor diferente:** Perguntar qual e o correto e atualizar VALORES_OFICIAIS.md

---

## 2. TIPOS DE ANALISE

### 2.1 Projecao Nova
**Quando:** Usuario quer criar cenario financeiro

**Carregar:**
- `references/produto_tecnico.md` - Custos
- `references/metricas_kpis.md` - Benchmarks
- `VALORES_OFICIAIS.md` - Base

**Template:** `assets/templates/TEMPLATE_RESUMO_FINANCEIRO.md`

### 2.2 Atualizacao de Projecao
**Quando:** Ajustar numeros existentes

**Passos:**
1. Identificar qual planilha atualizar
2. Carregar versao atual
3. Identificar mudancas
4. Aplicar e validar

### 2.3 Analise Comparativa
**Quando:** Comparar cenarios

**Cenarios padrao:**
- Conservador: 70% das metas
- Realista: 100% das metas
- Otimista: 130% das metas

---

## 3. ESTRUTURA DE CUSTOS

### Custos Variaveis (por kit)
```
Tecido (China):           R$ 15
Producao (Fabrica Jean):  R$ 30
Embalagem:                R$ 3
-------------------------------
TOTAL POR KIT:            R$ 48
```

### Custos Fixos (mensais)
```
Marketing (Titanium):     R$ 45-60k (escalando)
Trafego:                  R$ 40-100k (escalando)
Operacional:              R$ 20k
-------------------------------
TOTAL FIXO/MES:           R$ 105-180k
```

### Margem
```
Preco venda:              R$ 129
Custo variavel:           R$ 48
-------------------------------
Margem contribuicao:      R$ 81 (63%)

Apos custos fixos:        ~45% margem bruta
```

---

## 4. CALCULOS COMUNS

### Break-even
```python
# Ponto de equilibrio mensal
custos_fixos = 150000  # R$ 150k medio
margem_contribuicao = 81  # R$ por kit
break_even_unidades = custos_fixos / margem_contribuicao
# = 1.852 kits/mes
```

### ROI
```python
# ROI anual
investimento = 2096300
lucro_ano1 = investimento * 1.55  # 155%
roi = (lucro_ano1 - investimento) / investimento * 100
# = 55% (apos retorno do investimento)
```

### Payback
```
Investimento: R$ 2.096.300
Lucro medio mensal (apos break-even): ~R$ 500k
Payback: ~4-5 meses apos break-even
```

---

## 5. VALIDAR ARQUIVO

**Antes de criar, executar:**
```bash
python scripts/validate_before_create.py "PLANILHA_[DESCRICAO].md" "planejamento"
```

**Ou para resumos:**
```bash
python scripts/validate_before_create.py "RESUMO_FINANCEIRO_[STAKEHOLDER].md" "docs/financeiro"
```

**Regras de nome:**
- Planilhas: `PLANILHA_` em `planejamento/`
- Resumos: `RESUMO_FINANCEIRO_` em `docs/financeiro/`
- Analises: `ANALISE_` ou `DOSSIE_` em `docs/`

---

## 6. CRIAR DOCUMENTO

**Para projecoes completas:**
Usar `assets/templates/TEMPLATE_RESUMO_FINANCEIRO.md`

**Frontmatter:**
```yaml
---
criado: YYYY-MM-DDTHH:MM:SS-03:00
atualizado: YYYY-MM-DDTHH:MM:SS-03:00
tipo: projecao_financeira
cenario: [conservador|realista|otimista]
periodo: [6_meses|12_meses|24_meses]
status: ativo
---
```

**Secoes obrigatorias:**
1. Premissas (fonte dos numeros)
2. Investimento (origem e destino)
3. Custos (fixos e variaveis)
4. Receitas (por mes)
5. Fluxo de caixa
6. KPIs (break-even, ROI, payback)
7. Cenarios (se aplicavel)

---

## 7. USAR SCRIPT (SE COMPLEXO)

**Para calculos automatizados:**
```bash
python scripts/excel_calculator.py --scenario realista --months 12
```

**Funcoes disponiveis:**
- Projecao mensal
- Break-even analysis
- ROI calculation
- Scenario comparison

---

## 8. ATUALIZAR RELACIONADOS

**Apos criar/atualizar financeiro:**

1. **VALORES_OFICIAIS.md** - Se numeros base mudaram
2. **DASHBOARD.md** - Se KPIs mudaram
3. **_MOC_KabaK.md** - Se novo arquivo criado

**Cascata:**
```
Projecao nova → VALORES_OFICIAIS (se base) → DASHBOARD (KPIs) → MOC (link)
```

---

## ALERTAS

### Divergencia de Valores
**Se encontrar valor diferente de VALORES_OFICIAIS.md:**
1. Pausar analise
2. Perguntar ao usuario qual e correto
3. Atualizar VALORES_OFICIAIS.md se necessario
4. Corrigir documentos afetados

### Premissas Desatualizadas
**Verificar periodicamente:**
- Custo tecido (varia com cambio)
- Custo marketing (escala)
- Preco venda (estrategia)

---

## CHECKLIST FINAL

- [ ] VALORES_OFICIAIS.md consultado
- [ ] Referencias carregadas
- [ ] Calculos validados
- [ ] Nome arquivo correto
- [ ] Template utilizado
- [ ] Frontmatter PT-BR
- [ ] Salvo em local correto
- [ ] MOC atualizado
- [ ] DASHBOARD atualizado (se KPIs)

---

**Versao:** 2.0
**Criado:** 22/Jan/2026
