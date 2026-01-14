---
criado: 2025-12-23T20:33:32-03:00
atualizado: 2025-12-23T20:40:25-03:00
---

# ⚡ PLANO DE CORREÇÃO URGENTE - KabaK

**Data:** 24/Dez/2025
**Prazo:** 2-4 horas
**Prioridade:** 🔴 CRÍTICA

---

## 🎯 OBJETIVO

Corrigir inconsistência crítica entre alíquota declarada (2,5%) e alíquota calculada (6%) nos documentos do projeto KabaK.

---

## 📋 CHECKLIST EXECUTIVO (Para Gassen)

### ✅ ETAPA 1: DECISÃO (30 min - AGORA!)

- [ ] **Ligar para contador** (Perguntas abaixo)
- [ ] **Decidir cenário** (A, B ou C)
- [ ] **Comunicar decisão** a Claude para execução

#### Perguntas para o Contador:

1. **Regime Tributário:**
   - "Qual o regime tributário atual da KabaK?"
   - "Qual alíquota de ICMS esperada para 2026?"

2. **Benefício Fiscal MG:**
   - "Conseguimos aplicar benefício fiscal MG (1,3% ICMS) para vendas interestaduais?"
   - "Quais documentos/requisitos preciso para isso?"

3. **Estimativa Realista:**
   - "Pensando em e-commerce nacional, que % de vendas você espera que sejam FORA de MG?"
   - "Qual alíquota efetiva você recomenda usar na projeção: 2%, 2,5% ou 6%?"

4. **Recomendação:**
   - "Para ser conservador mas realista, qual número devo prometer ao investidor?"

#### Cenários Possíveis:

**Cenário A - CONSERVADOR (Recomendado):**

- Contador diz: "Use 6% para ser seguro"
- Ação: Corrigir apenas cabeçalho planilha (2,5% → 6%)
- ROI: 140%

**Cenário B - EQUILIBRADO:**

- Contador diz: "2,5% é razoável, 80% vendas fora MG é viável"
- Ação: RECALCULAR toda planilha com 2,5%
- ROI: 157%

**Cenário C - OTIMISTA:**

- Contador diz: "2% está correto, 85% vendas fora MG"
- Ação: Usar auditoria Claude (2%)
- ROI: 33%\*

\*ROI menor porque reembolso maior

---

### ✅ ETAPA 2: EXECUÇÃO (1-2h - Claude faz)

#### Se Cenário A (6% - Conservador):

**Arquivos a editar:**

1. `docs/PLANILHA_KABAK_PREENCHIDA.md`:
   - Linha 8: "Imposto 2,5%" → "Imposto 6,0%"
   - Manter resto (já está calculado em 6%)

2. `planejamento/PROPOSTA_FINAL_KABAK_SANSOM.md`:
   - Linha 483: "2,5%" → "6,0%"
   - Linha 492: Confirmar lucro R$ 9.006.262 está errado
   - Recalcular: Lucro = R$ 7.784.352
   - Linha 546: ROI 157% → ROI 140%

3. `STATUS_ATUAL.md`:
   - Linha 17: "ROI 157%" → "ROI 140%"

**Tempo estimado:** 30 minutos

---

#### Se Cenário B (2,5% - Equilibrado):

**Arquivos a editar:**

1. `docs/PLANILHA_KABAK_PREENCHIDA.md`:
   - Linha 37: Impostos (6%) R$ 180.342 → Impostos (2,5%) R$ 75.142
   - Linhas 12-23: Recalcular TODOS os 12 meses
   - Linha 56: Corrigir nota fiscal
   - Linha 68: Recalcular distribuição lucros
   - Linha 100: Atualizar total KABAK/SANSOM

2. `planejamento/PROPOSTA_FINAL_KABAK_SANSOM.md`:
   - Confirmar linha 492 lucro R$ 9.006.262 (se cálculo bater)
   - Confirmar ROI 157%

3. `STATUS_ATUAL.md`:
   - Confirmar ROI 157%

**Tempo estimado:** 1-2 horas (recálculo completo)

---

#### Se Cenário C (2% - Otimista):

**Arquivos a copiar/editar:**

1. Copiar: `99_ARQUIVO/.../PLANILHA_KABAK_PREENCHIDA_AUDITADA.md`
   - Para: `docs/PLANILHA_KABAK_PREENCHIDA.md`

2. Atualizar `planejamento/PROPOSTA_FINAL_KABAK_SANSOM.md`:
   - Linha 483: "2,5%" → "2,0%"
   - Linha 492: Lucro R$ 9.006.262 → R$ 9.076.347
   - Linha 546: ROI 157% → ROI 33%
   - Linha 542: SANSOM recebe R$ 5.725.631 → R$ 6.308.173

3. Atualizar `STATUS_ATUAL.md`:
   - Linha 17: ROI 157% → ROI 33%
   - Adicionar nota: "ROI conservador devido a reembolso tráfego maior"

**Tempo estimado:** 45 minutos

---

### ✅ ETAPA 3: VALIDAÇÃO (30 min)

**Checklist de Qualidade:**

- [ ] **Teste Matemático:** Recalcular junho manualmente
  - Receita: R$ 3.005.700
  - Imposto escolhido: R$ **\_\_**
  - Conferir se bate com planilha

- [ ] **Consistência Interna:**
  - Cabeçalho = Notas = Cálculos
  - Soma 12 meses = Total anual
  - Distribuição lucros = Lucro total

- [ ] **Consistência Externa:**
  - Planilha = Proposta
  - ROI declarado = ROI calculado
  - Números de junho exemplo = Números gerais

- [ ] **Cruzamento Final:**
  - Ler proposta completa
  - Conferir TODOS os números citados
  - Garantir zero contradições

---

### ✅ ETAPA 4: FINALIZAÇÃO (30 min)

**Documentação:**

1. [ ] Criar checkpoint:
   - Arquivo: `checkpoints/CHECKPOINT_24DEZ2025_Correcao_Impostos.md`
   - Conteúdo: O que foi corrigido, por quê, versão final

2. [ ] Arquivar versões antigas:
   - Mover planilha antiga para `99_ARQUIVO/Versoes_Antigas/`
   - Renomear: `PLANILHA_v2_imposto6_24dez2025.md`

3. [ ] Atualizar SESSION_LOG:
   - Registrar correção realizada
   - Deixar mensagem para Gemini

4. [ ] Atualizar STATUS_ATUAL:
   - Confirmar: "Pacote pronto para envio - Números validados"
   - Data atualização: 24/Dez/2025

---

## 🎯 DECISÃO RÁPIDA (Se Contador Não Atender)

**SEM resposta do contador → Usar Cenário A (Conservador - 6%)**

**Por quê:**

- ✅ Seguro (não promete demais)
- ✅ Rápido de corrigir (só mudar cabeçalho)
- ✅ Se benefício fiscal funcionar = Upside bônus
- ✅ Credibilidade (números conservadores)

**Mensagem ao Sansom:**

> "Usamos projeção conservadora (imposto 6%). Se conseguirmos aplicar benefício fiscal MG nas vendas interestaduais, o lucro pode aumentar R$ 1-2M. Estamos prometendo menos para entregar mais!"

---

## 📊 TABELA COMPARATIVA FINAL

| Métrica           | Cenário A (6%) | Cenário B (2,5%) | Cenário C (2%) |
| ----------------- | -------------- | ---------------- | -------------- |
| **Imposto Anual** | R$ 1.940.418   | R$ 808.508       | R$ 648.423     |
| **Lucro Líquido** | R$ 7.784.352   | R$ 9.006.262     | R$ 9.076.347   |
| **KABAK Recebe**  | R$ 2.692.176   | R$ 3.280.631     | R$ 2.768.173   |
| **SANSOM Recebe** | R$ 5.092.176   | R$ 5.725.631     | R$ 6.308.173   |
| **ROI SANSOM**    | 140%           | 157%             | 33%\*          |
| **Risco**         | BAIXO          | MÉDIO            | MÉDIO          |
| **Recomendação**  | ✅ SIM         | ⚠️ Se validado   | ⚠️ Se validado |

\*ROI menor em C porque reembolso maior (tráfego R$ 1,38M vs R$ 645k)

---

## ⚡ EXECUÇÃO RÁPIDA (Se Escolher A)

### Correção em 15 minutos:

**1. Editar `docs/PLANILHA_KABAK_PREENCHIDA.md`:**

```markdown
ANTES (Linha 8):
**Premissas:** Imposto 2,5% (Mix Interestadual)

DEPOIS:
**Premissas:** Imposto 6,0% (Conservador)
```

**2. Editar `planejamento/PROPOSTA_FINAL_KABAK_SANSOM.md`:**

```markdown
ANTES (Linha 483):
_Premissa Fiscal: 2,5%_

DEPOIS:
_Premissa Fiscal: 6,0% (Conservador - Upside se benefício MG funcionar)_
```

```markdown
ANTES (Linha 492):
| **Lucro Líquido** | **R$ 9.006.262** |

DEPOIS:
| **Lucro Líquido** | **R$ 7.784.352** |
```

```markdown
ANTES (Linha 532-544):
Pró-labore (12 meses): R$ 1.200.000
Lucro 50%: R$ 1.492.176

DEPOIS:
Pró-labore (12 meses): R$ 1.200.000
Lucro 50%: R$ 1.492.176
```

```markdown
ANTES (Linha 546):
ROI: 157% EM 12 MESES!

DEPOIS:
ROI: 140% EM 12 MESES!
```

**3. Editar `STATUS_ATUAL.md`:**

```markdown
ANTES (Linha 17):
Imposto 2.5% (Weighted) -> ROI 157%

DEPOIS:
Imposto 6% (Conservador) -> ROI 140%
```

**PRONTO! ✅**

---

## 📞 COMUNICAÇÃO

### Após Correção, Informar Sansom:

**Opção 1 (Se usou 6% conservador):**

> "Olá Sansom,
>
> Finalizamos a proposta com números **conservadores** (imposto 6%). Isso garante que prometemos menos e entregamos mais.
>
> **Lucro projetado: R$ 7,78M (ROI 140%)**
>
> Upside: Se conseguirmos aplicar benefício fiscal MG (1,3-2,5% ICMS) para vendas interestaduais, o lucro pode aumentar R$ 1-2M. Isso seria um bônus, não uma promessa.
>
> Proposta pronta para envio!
>
> Att, Gassen"

**Opção 2 (Se usou 2,5% validado):**

> "Olá Sansom,
>
> Validamos com contador e confirmamos **benefício fiscal MG** aplicável.
>
> **Lucro projetado: R$ 9,00M (ROI 157%)**
>
> Premissa: 80% vendas interestaduais (e-commerce nacional) com ICMS 1,3%.
>
> Proposta pronta para envio!
>
> Att, Gassen"

---

## 🚨 ALERTA FINAL

**NÃO enviar proposta até:**

- ✅ Decidir cenário (A, B ou C)
- ✅ Executar correções
- ✅ Validar cruzado
- ✅ Confirmar zero inconsistências

**Tempo total:** 2-4 horas bem investidas!

**Resultado:** Proposta profissional, consistente e confiável!

---

**Elaborado por:** Claude Architect
**Data:** 24/Dez/2025
**Status:** Aguardando decisão de Gassen

🔐 **CONFIDENCIAL - KabaK**
