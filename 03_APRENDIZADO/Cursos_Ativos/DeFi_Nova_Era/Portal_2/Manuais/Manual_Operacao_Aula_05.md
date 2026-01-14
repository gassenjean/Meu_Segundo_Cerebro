---
criado: 2025-12-08T11:52:32-03:00
atualizado: 2025-12-08T11:52:32-03:00
---

# Portal 2 - Aula 05: Indicadores (Caro ou Barato?)

**Versão:** 1.0
**Data Extração:** 08/Dez/2025
**Status:** ✅ Validado

---

## 🎯 OBJETIVO DA AULA

Saber matematicamente se o Bitcoin está **Caro (Topo)** ou **Barato (Fundo)** usando dados On-Chain e Técnicos, sem "achismo".

---

## 🔢 PARÂMETROS CRÍTICOS (O Semáforo)

| Indicador          | Ferramenta   | Sinal de VENDA (Topo) 🔴              | Sinal de COMPRA (Fundo) 🟢              |
| ------------------ | ------------ | ------------------------------------- | --------------------------------------- |
| **MVRV Z-Score**   | CheckOnChain | Acima de 3.0 (Zona Vermelha)          | Abaixo de 1.0 (Zona Verde)              |
| **Puell Multiple** | CheckOnChain | -                                     | Abaixo de 0.5 (Capitulação Mineradores) |
| **Funding Rates**  | Coinglass    | Acima de 40-50% (Euforia)             | Negativo ou Neutro                      |
| **SMA 50 Semanas** | TradingView  | Preço perde a média (cruzou p/ baixo) | Preço retoma a média (cruzou p/ cima)   |

---

## 📋 ALGORITMO DE VALUATION

### Input (CheckOnChain + TradingView)

- [ ] Onde está o MVRV hoje?
- [ ] O preço está acima da média de 50 semanas?
- [ ] Os "Long Term Holders" (LTH) estão vendendo?

### Processo

1. **Verificar Tendência (SMA 50W):**
   - Acima da linha? Bull Market. (Procurar compra).
   - Abaixo da linha? Bear Market. (Procurar venda ou caixa).

2. **Verificar Valuation (MVRV):**
   - MVRV < 1? É Oportunidade Geracional (Comprar até a mãe).
   - MVRV > 3? É Bolha (Vender tudo para o vizinho eufórico).

3. **Verificar Smart Money (LTH):**
   - Se LTHs estão distribuindo (vendendo) forte e o preço está subindo -> Cuidado, topo próximo.

### Output

- ✅ **Zona de Compra:** MVRV < 1 + Puell < 0.5.
- ✅ **Zona de Venda:** MVRV > 3.0 + Funding > 50% + LTH Vendendo.

---

## 🤖 GATILHOS DE AUTOMAÇÃO

| Se (Condição)                        | Então (Ação)                                         | Prioridade |
| ------------------------------------ | ---------------------------------------------------- | ---------- |
| MVRV cruza 3.0 para cima             | **Venda Escalonada** (Começar a sair)                | 🔴 Alta    |
| Preço fecha semanal abaixo da SMA 50 | **Ativar Modo Defensivo** (Stop loss, assumir caixa) | 🔴 Alta    |
| MVRV toca 0.8 (Fundo histórico)      | **All-In** (Aporte máximo)                           | 🔴 Alta    |

---

## 🚫 LISTA NEGRA (O que NÃO fazer)

❌ **Proibido:**

- Comprar Bitcoin quando o MVRV está acima de 3.0 (Risco de queda de 80%).
- Vender Bitcoin quando o MVRV está abaixo de 1.0 (Você está vendendo o fundo para smart money).
- Ficar comprado (long) quando o preço perde a SMA 50 Semanal.

---

## 💎 INSIGHT DE OURO

"O indicador MVRV é a regressão à média. Ele nos diz a verdade sobre o preço. Historicamente, comprar abaixo de 1 e vender acima de 3 nunca falhou em nenhum ciclo. É a bússola mais confiável que existe."

---

## 🔗 RECURSOS TÉCNICOS

- **On-Chain:** [CheckOnChain](https://checkonchain.com/) (Gratuito e excelente).
- **Alternativa:** [Bitcoin Magazine Pro](https://bitcoinmagazine.com/pro).
- **Funding:** [Coinglass](https://www.coinglass.com/FundingRate).

---

## ✅ CHECKLIST DE IMPLEMENTAÇÃO IMEDIATA

- [ ] Criar conta no CheckOnChain.
- [ ] Adicionar SMA 50 no gráfico semanal do TradingView (Linha grossa para ver bem).
- [ ] Verificar onde estamos no MVRV HOJE.

---

## 📊 INTEGRAÇÃO COM PROJETO

**Pasta Destino:** `03_APRENDIZADO/Cursos_Ativos/DeFi_Nova_Era/Portal_2/Manuais/`
**Atualizar:**

- [ ] Agente Lucas (Regra MVRV < 1 = Compra, MVRV > 3 = Venda)
