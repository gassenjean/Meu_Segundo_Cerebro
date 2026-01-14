---
criado: 2025-12-08T11:51:41-03:00
atualizado: 2025-12-08T11:51:41-03:00
---

# Portal 2 - Aula 03: Altcoin Season (Temporada das Altcoins)

**Versão:** 1.0
**Data Extração:** 08/Dez/2025
**Status:** ✅ Validado

---

## 🎯 OBJETIVO DA AULA

Identificar o **momento exato** em que o capital migra do Bitcoin para as Altcoins para capturar valorizações exponenciais (10x, 50x, 100x).

---

## 🔢 PARÂMETROS CRÍTICOS (O Painel da Explosão)

| Indicador                 | Código TradingView | Sinal de ALT SEASON 🟢          | Sinal de BTC SEASON 🟠        |
| ------------------------- | ------------------ | ------------------------------- | ----------------------------- |
| **Dominância do Bitcoin** | `BTC.D`            | Caindo forte (Rompendo suporte) | Subindo ou Lateral            |
| **Par Ethereum/Bitcoin**  | `ETHBTC`           | Subindo (ETH ganhando força)    | Caindo (ETH fraco)            |
| **Total 3 / BTC**         | `TOTAL3/BTC`       | Gráfico em tendência de ALTA    | Gráfico em tendência de BAIXA |
| **Balanço Fed**           | `WALCL`            | Expandindo (Dinheiro novo)      | Contraindo (Seca)             |

---

## 📋 ALGORITMO DE ROTAÇÃO DE CAPITAL

### Input (O Copo Transbordando)

- [ ] O Bitcoin já subiu e estagnou (lateralizou)?
- [ ] O Ethereum começou a acordar?
- [ ] A liquidez global está alta?

### Processo (O Caminho do Dinheiro)

1. **Fase 1: Bitcoin King**
   - Dominância subindo. Altcoins sangrando vs BTC.
   - **Ação:** Ficar 100% em BTC/ETH. Não toque em alts pequenas.

2. **Fase 2: Ethereum Awakening**
   - `ETHBTC` encontra fundo e reverte.
   - **Ação:** Começar a migrar parte do lucro de BTC para ETH e top Alts (Solana, etc).

3. **Fase 3: Altcoin Season (A Festa)**
   - `BTC.D` em queda livre + `TOTAL3/BTC` explodindo.
   - **Ação:** Rotação agressiva para Mid/Low Caps. É aqui que se faz 50x.

4. **Fase 4: A Ressaca**
   - Tudo cai junto (pânico ou realização final).
   - **Ação:** Voltar para BTC ou Dólar.

### Output

- ✅ **Alt Season Confirmada:** Apenas se `TOTAL3/BTC` estiver subindo. Se Alts sobem em Dólar mas caem em BTC, **NÃO É** Alt Season, é ilusão.

---

## 🤖 GATILHOS DE AUTOMAÇÃO

| Se (Condição)                                  | Então (Ação)                                   | Prioridade     |
| ---------------------------------------------- | ---------------------------------------------- | -------------- |
| `ETHBTC` rompe resistência semanal             | **Iniciar migração** para Alts L1 de qualidade | 🟡 Média       |
| `BTC.D` perde suporte crítico (Ex: 50% ou 40%) | **Aportar em Mid/Low Caps**                    | 🔴 Alta        |
| `TOTAL3/BTC` perde fundo                       | **ABORTAR Alt Season** (Voltar para BTC/USDT)  | 🔴 Alta (Stop) |

---

## 🚫 LISTA NEGRA (O que NÃO fazer)

❌ **Proibido:**

- Comprar Altcoins quando a Dominância do BTC está subindo verticalmente.
- Analisar Altcoins apenas em par Dólar (USDT). **Sempre analise o par BTC.**
- Casar com Altcoins (Elas tendem a zero no longo prazo).

---

## 💎 INSIGHT DE OURO

"Pare de olhar o gráfico em Dólar. O objetivo do jogo é acumular BITCOIN. Se sua Altcoin subiu 10% em Dólar mas o Bitcoin subiu 15%, você **perdeu dinheiro**. Use o gráfico `TOTAL3/BTC` (A Fórmula Mágica) para saber a verdade."

---

## ✅ CHECKLIST DE IMPLEMENTAÇÃO IMEDIATA

- [ ] Criar lista de observação no TradingView com: `BTC.D`, `ETHBTC`, `TOTAL3/BTC`.
- [ ] Nunca mais comprar uma Altcoin sem olhar o gráfico dela contra o BTC.

---

## 📊 INTEGRAÇÃO COM PROJETO

**Pasta Destino:** `03_APRENDIZADO/Cursos_Ativos/DeFi_Nova_Era/Portal_2/Manuais/`
**Atualizar:**

- [ ] Agente Lucas (Regra: Só comprar Alt se `TOTAL3/BTC` estiver favorável)
