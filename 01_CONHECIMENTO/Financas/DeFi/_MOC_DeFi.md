---
criado: 2026-01-26T09:00:00-03:00
atualizado: 2026-01-26T09:00:00-03:00
tags: [DeFi, Cripto, Investimentos, MOC]
---
# MOC: DeFi

**Map of Content - Finanças Descentralizadas**

**Criado:** 26/Jan/2026
**Status:** 🚧 Em construção (aguardando migração)
**Agente:** /lucas

---

## VISÃO GERAL

Este MOC centraliza todo conhecimento de DeFi no vault. Aqui você encontra:

- Conceitos fundamentais (M1-M5)
- Manuais de operação (13 documentos)
- Estratégias e frameworks
- Insights de mercado

---

## ESTRUTURA

### Conceitos Atômicos (A Migrar)

**Fonte:** `03_APRENDIZADO/Investimentos_Crypto/Mente_De_Tubarao/` M1-M5

| Módulo | Tema | Status |
| ------ | ---- | ------ |
| M1 | Fundamentos DeFi | 🟡 Pendente migração |
| M2 | Análise On-Chain | 🟡 Pendente migração |
| M3 | Gestão de Risco | 🟡 Pendente migração |
| M4 | Estratégias de Entrada | 🟡 Pendente migração |
| M5 | Operação Prática | 🟡 Pendente migração |

### Manuais de Operação (A Migrar)

**Fonte:** `03_APRENDIZADO/Investimentos_Crypto/Mente_De_Tubarao/recursos/`

| Manual | Descrição | Status |
| ------ | --------- | ------ |
| manual_stoploss.md | Gestão de stop loss | 🟡 Pendente |
| manual_entrada_posicao.md | Entrada em posições | 🟡 Pendente |
| manual_setup_price_alerts.md | Configurar alertas | 🟡 Pendente |
| ... | (10 outros manuais) | 🟡 Pendente |

### Portal 3: Análise de Projetos (A Processar)

**Fonte:** `03_APRENDIZADO/Investimentos_Crypto/Mente_De_Tubarao/Portal_3/`

| Conteúdo | Descrição | Status |
| -------- | --------- | ------ |
| Aulas de análise | Framework de análise de tokens | 🔴 Não processado |
| Critérios de avaliação | O que olhar em um projeto | 🔴 Não processado |

**Tarefa Gemini T029:** Processar Portal 3 completo

---

## FERRAMENTAS EXTERNAS

| Ferramenta | Uso | Link |
| ---------- | --- | ---- |
| LookIntoBitcoin | Métricas on-chain BTC | lookintoBitcoin.com |
| TradingView | Análise técnica | tradingview.com |
| CheckOnChain | Fluxos de exchange | checkonchain.com |
| DefiLlama | TVL e protocolos | defillama.com |

---

## INSIGHTS DE MERCADO

**Localização:** `01_CONHECIMENTO/Financas/DeFi/INSIGHTS_MERCADO_SEMANAL.md` (a criar)

**Responsável:** researcher-defi (Gemini)
**Frequência:** Semanal (segundas)
**Status:** 🔴 Não implementado

---

## INTEGRAÇÃO COM /lucas

O comando `/lucas` é o agente especializado em DeFi. Ele deve:

1. **Ler este MOC** ao iniciar
2. **Carregar conceitos** de M1-M5
3. **Usar manuais** para operações
4. **Consultar insights** semanais
5. **Aplicar framework Portal 3** para análise de tokens

**Arquivo do comando:** `.claude/commands/lucas.md`

---

## CONEXÕES

### MOCs Relacionados

- [[01_CONHECIMENTO/_MOC_Conhecimento.md|_MOC_Conhecimento]] - MOC pai
- [[03_APRENDIZADO/Investimentos_Crypto/_MOC_Crypto.md|_MOC_Crypto]] - Material de estudo

### Projetos que Usam DeFi

- Operações pessoais de Gassen (R$3k validado)

### Agentes Relacionados

- `/lucas` - Agente especializado DeFi
- `/coach` - Gestão emocional em operações

---

## PLANO DE MIGRAÇÃO

**Tarefa Gemini T030:** Migrar conceitos DeFi M1-M5

### Fase 1: Conceitos Atômicos

```text
03_APRENDIZADO/.../Mente_De_Tubarao/notas/M[1-5]/
    ↓ (copiar e consolidar)
01_CONHECIMENTO/Financas/DeFi/Conceitos_Atomicos/
```

### Fase 2: Manuais

```text
03_APRENDIZADO/.../Mente_De_Tubarao/recursos/*.md
    ↓ (copiar)
01_CONHECIMENTO/Financas/DeFi/Manuais/
```

### Fase 3: Portal 3

```text
03_APRENDIZADO/.../Portal_3/ (aulas brutas)
    ↓ (Gemini processa T029)
01_CONHECIMENTO/Financas/DeFi/Analise_Projetos/
```

---

## CHECKLIST DE IMPLEMENTAÇÃO

### FASE 0 (Esta semana)

- [x] Criar _MOC_DeFi.md (este arquivo)
- [ ] Atualizar /lucas para ler este MOC

### FASE 1-2 (Semana 1-2)

- [ ] T030: Migrar conceitos M1-M5
- [ ] Copiar 13 manuais
- [ ] T029: Processar Portal 3

### FASE 3 (Semana 2+)

- [ ] Criar INSIGHTS_MERCADO_SEMANAL.md
- [ ] Configurar researcher-defi (Gemini)
- [ ] Briefing semanal automático

---

**Versão:** 1.0
**Criado:** 26/Jan/2026
**Próxima revisão:** Após migração completa
