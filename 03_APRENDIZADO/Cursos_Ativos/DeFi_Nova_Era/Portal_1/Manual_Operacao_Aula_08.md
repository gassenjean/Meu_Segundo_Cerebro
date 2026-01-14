# Portal 1 - Aula 08: Cripto vs Token

**Versão:** 1.0
**Data Extração:** 04/12/2025
**Status:** ✅ Validado

---

## 🎯 OBJETIVO DA AULA

Distinguir Criptomoedas (Donas da Rede) de Tokens (Inquilinos) para avaliar a robustez do projeto e blindar-se contra os golpes mais comuns do mercado (Engenharia Social).

---

## 🔢 PARÂMETROS CRÍTICOS

| Parâmetro            | Criptomoeda (Coin)          | Token                        |
| -------------------- | --------------------------- | ---------------------------- |
| **Infraestrutura**   | **Tem Blockchain Própria**  | **Usa Blockchain de Outros** |
| **Função**           | **Pagar Taxa de Gás (Gas)** | **Utilidade/Governança**     |
| **Exemplos**         | **BTC, ETH, SOL, AVAX**     | **UNI, LINK, USDT, AAVE**    |
| **Custo de Criação** | **Alto (Milhões)**          | **Baixo (Centavos)**         |

**Mínimo:** 3 parâmetros comparativos por estratégia.

---

## 📋 ALGORITMO DE EXECUÇÃO (Segurança Anti-Golpe)

### Input (Pré-requisitos)

- [ ] Saber que NINGUÉM dá dinheiro de graça.
- [ ] Entender que "Suporte" nunca chama primeiro.

### Processo (Passo a Passo)

1. **Identificação de Ativo**
   - Ação: Verificar no CoinGecko/CoinMarketCap.
   - Pergunta: "Coin" ou "Token"? Se é Token, em qual rede ele vive?

2. **Protocolo de Segurança (Dust Attack)**
   - Cenário: Apareceu um token desconhecido na sua carteira valendo milhares de dólares.
   - Ação: **NÃO TOCAR.** Não tentar vender, não tentar transferir. Apenas oculte.
   - Risco: Ao interagir, você assina um contrato malicioso que drena sua carteira.

3. **Protocolo Anti-Engenharia Social**
   - Cenário: "Elon Musk vai dobrar seus BTC".
   - Ação: Ignorar. É golpe.

### Output (Resultado Esperado)

- ✅ Carteira limpa de interações maliciosas.
- ✅ Zero perda de fundos por ganância/ingenuidade.

---

## 🤖 GATILHOS DE AUTOMAÇÃO (Mental)

| Se (Condição)                         | Então (Ação)                                | Prioridade |
| ------------------------------------- | ------------------------------------------- | ---------- |
| **Se pedirem 12/24 palavras**         | **BLOQUEAR IMEDIATAMENTE**                  | 🔴 Crítica |
| **Se prometerem "Retorno Garantido"** | **Fugir (Renda Variável não tem garantia)** | 🔴 Alta    |
| **Se token desconhecido aparecer**    | **Ignorar (Dust Attack)**                   | 🟡 Média   |

**Mínimo:** 2 gatilhos por estratégia.

---

## 🚫 LISTA NEGRA (O que NÃO fazer)

❌ **Proibido:**

- **Interagir com Tokens "Mágicos":** Se você não comprou, não é seu. É isca.
- **Achar que Token é pior que Coin:** Não é pior, é diferente. Mas Coin tem infraestrutura (Landlord), Token tem utilidade (Tenant).

⚠️ **Red Flags:**

- **Influencer pedindo dinheiro:** Perfis falsos são comuns. Verifique sempre.

---

## 💎 INSIGHT DE OURO

"Criptomoeda é o Senhorio (Dono do Prédio/Blockchain). Token é o Inquilino (Aluga o apartamento). O Senhorio cobra aluguel (Gas) do Inquilino. Para ser sócio da infraestrutura, compre Coins. Para apostar em negócios específicos, compre Tokens."

---

## 🔗 RECURSOS TÉCNICOS

- **Ferramenta:** [CoinGecko](https://www.coingecko.com/) (Para verificar se é Coin ou Token).
- **Glossário:** [DeFi Verso Glossário](https://defiverso.notion.site/) (Baixar e duplicar).

---

## ✅ CHECKLIST DE IMPLEMENTAÇÃO IMEDIATA

- [ ] Ler o Whitepaper do Bitcoin (em Português).
- [ ] Ensinar o conceito de Bitcoin para 2 pessoas (Técnica Feynman de aprendizado).
- [ ] Baixar o Glossário do DeFi Verso no Notion.

---

## 📊 INTEGRAÇÃO COM PROJETO

**Pasta Destino:** `02_PROJETOS/DeFi_Verso_2025/03_Renda_Passiva/Fundamentos/`
**Atualizar:**

- [ ] Agente Lucas (Regra: "Ignorar tokens não solicitados na wallet").
- [ ] Agente Lucas (Regra: "Diferenciar Coin de Token para análise fundamentalista").
