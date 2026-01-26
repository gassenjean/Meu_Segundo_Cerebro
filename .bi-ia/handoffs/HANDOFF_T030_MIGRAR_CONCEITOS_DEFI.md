# HANDOFF: Migrar Conceitos DeFi M1-M5

**ID:** T030
**De:** Claude (Névoa)
**Para:** Gemini (Guardian/IO)
**Data:** 26/Jan/2026
**Prioridade:** Média

---

## 1. Contexto

O conhecimento DeFi está todo em `03_APRENDIZADO/` mas `01_CONHECIMENTO/Financas/DeFi/` está vazio. Precisamos copiar os conceitos consolidados (M1-M5) para a base de conhecimento permanente.

**Regra:** 03_APRENDIZADO = material de estudo, 01_CONHECIMENTO = conhecimento consolidado.

---

## 2. Tarefa

**Ação:** Migrar e consolidar conceitos atômicos

**Objeto:** Notas dos módulos M1-M5 de `03_APRENDIZADO/Investimentos_Crypto/Mente_De_Tubarao/notas/`

**Condição:**
- Copiar (não mover) conceitos para 01_CONHECIMENTO
- Renomear seguindo NOMENCLATURA.md
- Consolidar notas relacionadas em conceitos atômicos

---

## 3. Ferramenta Google Necessária

| Ferramenta | Squad | Motivo |
| ---------- | ----- | ------ |
| Antigravity (IO) | Research | Leitura e processamento |

---

## 4. Inputs (O que Gemini precisa)

**Arquivos:**
- [ ] `03_APRENDIZADO/Investimentos_Crypto/Mente_De_Tubarao/notas/` (M1-M5)
- [ ] `00_SISTEMA/PADROES/NOMENCLATURA.md` (para naming correto)

**Contexto adicional:**
- M1 = Fundamentos DeFi
- M2 = Análise On-Chain
- M3 = Gestão de Risco
- M4 = Estratégias de Entrada
- M5 = Operação Prática

---

## 5. Output Esperado

**Formato:** Markdown (conceitos atômicos)

**Local de entrega:** `01_CONHECIMENTO/Financas/DeFi/Conceitos_Atomicos/`

**Estrutura esperada:**

```text
01_CONHECIMENTO/Financas/DeFi/Conceitos_Atomicos/
├── DeFi_Fundamentos_Liquidez.md
├── DeFi_Fundamentos_AMM.md
├── DeFi_Fundamentos_Yield_Farming.md
├── DeFi_OnChain_Whale_Watching.md
├── DeFi_OnChain_TVL_Analysis.md
├── DeFi_Risco_Position_Sizing.md
├── DeFi_Risco_Stop_Loss.md
├── DeFi_Entrada_DCA.md
├── DeFi_Entrada_Pyramiding.md
├── DeFi_Operacao_Setup_Alerts.md
└── ... (estimativa: 30 conceitos)
```

**Template por conceito:**

```markdown
# DeFi: [Conceito]

**Fonte:** Mente de Tubarão - M[X]
**Categoria:** [Fundamentos/OnChain/Risco/Entrada/Operação]
**Status:** Consolidado

---

## Conceito

[Definição clara e concisa]

---

## Aplicação Prática

[Como usar na operação]

---

## Conexões

- [[DeFi_Conceito_Relacionado]]
- [[_MOC_DeFi]]
```

---

## 6. Quality Gate

Antes de marcar como completo, verificar:

- [ ] Completo? (Todos conceitos de M1-M5 migrados)
- [ ] Correto? (Nomenclatura segue padrão)
- [ ] Útil? (Conceitos são atômicos e acionáveis)
- [ ] Limpo? (Sem duplicação com 03_APRENDIZADO)

---

## 7. Comunicação

**Ao concluir:**
1. Atualizar `state.json` (status: completed)
2. Atualizar `_MOC_DeFi.md` com lista de conceitos
3. Informar quantidade de conceitos migrados

---

**Status:** Pendente
**Criado por:** Névoa 6.0
**Dependentes:** /lucas (carrega conceitos)
