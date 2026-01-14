# Portal 1 - Aula 02: Criptografia

**Versão:** 1.0
**Data Extração:** 04/12/2025
**Status:** ✅ Validado

---

## 🎯 OBJETIVO DA AULA

Dominar a diferença entre Criptografia Simétrica e Assimétrica para garantir a segurança absoluta dos fundos, entendendo o papel da Chave Pública (Endereço) e Chave Privada (Senha Mestra).

---

## 🔢 PARÂMETROS CRÍTICOS

| Parâmetro                | Valor Exato          | Contexto                                              |
| ------------------------ | -------------------- | ----------------------------------------------------- |
| **Tipo de Criptografia** | **Assimétrica**      | Padrão do Bitcoin/DeFi (2 chaves).                    |
| **Chave Pública**        | **Endereço (0x...)** | Pode ser compartilhada livremente (Caixa de Correio). |
| **Chave Privada**        | **Senha Mestra**     | NUNCA compartilhar (Chave que abre a caixa).          |
| **Nível de Segurança**   | **Máximo**           | Se a chave privada for mantida offline/segura.        |

**Mínimo:** 3 parâmetros numéricos/técnicos por estratégia.

---

## 📋 ALGORITMO DE EXECUÇÃO (Segurança)

### Input (Pré-requisitos)

- [ ] Entender que você é o seu próprio banco.
- [ ] Ter uma carteira (Wallet) gerada.

### Processo (Passo a Passo)

1. **Identificação de Chaves**
   - Ação exata: Identificar qual é seu Endereço Público (para receber).
   - Ação exata: Identificar/Guardar sua Chave Privada (Seed Phrase) em local offline.

2. **Operação de Recebimento**
   - Ação exata: Compartilhar APENAS a Chave Pública (Endereço).
   - Validação: Analogia da Caixa de Correio (qualquer um deposita, só você saca).

3. **Operação de Envio**
   - Ação exata: Usar a Chave Privada para assinar a transação (autorizar saída).
   - Validação: A rede confirma que você é o dono sem você revelar a senha.

### Output (Resultado Esperado)

- ✅ Transações seguras sem intermediários.
- ✅ Impossibilidade de confisco (se a chave privada estiver segura).

---

## 🤖 GATILHOS DE AUTOMAÇÃO (Segurança)

| Se (Condição)                           | Então (Ação)                               | Prioridade |
| --------------------------------------- | ------------------------------------------ | ---------- |
| **Se site/suporte pedir Chave Privada** | **BLOQUEAR E DENUNCIAR (É Golpe)**         | 🔴 Crítica |
| **Se for receber pagamentos**           | **Enviar Endereço Público (QR Code/Hash)** | 🟢 Normal  |
| **Se perder a Chave Privada**           | **Considerar fundos perdidos para sempre** | 🔴 Crítica |

**Mínimo:** 2 gatilhos por estratégia.

---

## 🚫 LISTA NEGRA (O que NÃO fazer)

❌ **Proibido:**

- **Confundir as chaves:** Enviar chave privada em vez da pública é erro fatal.
- **Salvar Chave Privada online:** Google Drive, Email, Foto no celular (Risco de hack).
- **Acreditar em "Suporte da Wallet":** Ninguém legítimo pede sua chave privada.

⚠️ **Red Flags:**

- **Sites pedindo "Sincronizar Carteira":** Geralmente pedem a seed phrase -> SCAM.

---

## 💎 INSIGHT DE OURO

"A Criptografia Assimétrica (Caixa de Correio) permite que você tenha um endereço público exposto para o mundo inteiro receber dinheiro, sem NENHUM risco de alguém roubar o que está lá dentro. A segurança está na separação matemática das chaves."

---

## 🔗 RECURSOS TÉCNICOS

- **Conceito:** [Public-key cryptography (Wikipedia)](https://en.wikipedia.org/wiki/Public-key_cryptography)
- **Ferramenta:** Sua Wallet (Metamask/Ledger) gerencia isso automaticamente, mas você deve entender o conceito.

---

## ✅ CHECKLIST DE IMPLEMENTAÇÃO IMEDIATA

- [ ] Verificar se você sabe onde está sua Chave Privada (Seed Phrase).
- [ ] Garantir que ela NÃO está em meio digital (apenas papel/metal).
- [ ] Testar receber uma transação pequena usando apenas o Endereço Público.

---

## 📊 INTEGRAÇÃO COM PROJETO

**Pasta Destino:** `02_PROJETOS/DeFi_Verso_2025/03_Renda_Passiva/Fundamentos/`
**Atualizar:**

- [ ] Agente Lucas (Regra: "Jamais pedir ou compartilhar Chave Privada").
- [ ] Agente Lucas (Regra: "Validar endereço público antes de enviar").
