# Design de Extração de Conhecimento: DeFi Portal 1

**Arquiteto:** Claude Architect
**Executor:** Gemini Guardian
**Objetivo:** Extração Cirúrgica para Resultados Financeiros (Zero Genérico)

---

## 🎯 A Filosofia "Zero Genérico"

Para garantir que o conhecimento se traduza em dinheiro, não podemos extrair "o que é". Precisamos extrair "como fazer", "quando fazer" e "exatamente quanto".

**❌ Genérico (Ruim):**
"Fazer staking é bom para renda passiva. Procure pools seguras."

**✅ Cirúrgico (Meta):**
"Fazer staking de ETH na Lido se o APY > 3.5%. Se o Gas estiver < 20 gwei, fazer o claim semanalmente. Se > 20 gwei, acumular mensalmente. Risco aceitável: Despeg do stETH até 2%."

---

## 🛠️ O Prompt de Extração (Blueprint)

Quando tivermos as transcrições, o Gemini usará este framework para cada aula:

### 1. O "Algoritmo" da Aula

Extrair o processo decisório do Lucas Amoedo em formato de pseudocódigo ou fluxograma lógico.

- **Input:** O que preciso ter/saber antes de começar?
- **Processo:** Passo a passo exato (clique a clique, se necessário).
- **Output:** Qual o resultado esperado tangível?

### 2. Parâmetros Críticos (Hard Numbers)

Buscar números específicos que definem a estratégia:

- % de alocação recomendada.
- Níveis de preço para entrada/saída.
- Indicadores on-chain específicos (ex: MVRV Z-Score < 0).
- Taxas aceitáveis.

### 3. Gatilhos de Automação (If This Then That)

Identificar regras claras para automação (mental ou técnica via n8n):

- "Se o Bitcoin cair 20%, comprar X."
- "Se a taxa de funding ficar negativa, fazer Y."

### 4. A Lista Negra (O que NÃO fazer)

Tão importante quanto o que fazer.

- Protocolos proibidos.
- Erros comuns que custam dinheiro.
- Sinais de perigo (Red Flags).

---

## 📋 Estrutura de Saída (O Artefato Final)

Para cada aula, geraremos um **Manual de Operação** (não um resumo), contendo:

1.  **Checklist de Execução:** Lista de tarefas para implementar IMEDIATAMENTE.
2.  **Matriz de Decisão:** Tabela "Se Acontecer X -> Faça Y".
3.  **Configuração Técnica:** Parâmetros exatos para colocar na ferramenta (ex: alertas de preço).
4.  **Insight de Ouro:** Aquele detalhe que diferencia o amador do pro.

---

## 🤖 Integração com Agente Lucas

Após a extração, o Agente Lucas será atualizado não com "texto", mas com **regras**.

- Ele não vai "saber sobre" staking.
- Ele vai "ter a regra" de staking.

---

---

## 📝 TEMPLATE DE EXTRAÇÃO (Usar para cada aula)

```markdown
# Portal 1 - Aula [XX]: [Título]

**Versão:** 1.0
**Data Extração:** [DATA]
**Status:** ✅ Validado | ⏳ Em Revisão

---

## 🎯 OBJETIVO DA AULA

[O que Lucas quer que você consiga fazer após esta aula - 1 frase]

---

## 🔢 PARÂMETROS CRÍTICOS

| Parâmetro        | Valor Exato         | Contexto               |
| ---------------- | ------------------- | ---------------------- |
| [Ex: APY Mínimo] | [Ex: 3.5%]          | [Ex: Para staking ETH] |
| [Ex: Gas Limite] | [Ex: 20 gwei]       | [Ex: Para claims]      |
| [Ex: % Alocação] | [Ex: 10% portfólio] | [Ex: Em stablecoins]   |

**Mínimo:** 3 parâmetros numéricos por estratégia

---

## 📋 ALGORITMO DE EXECUÇÃO

### Input (Pré-requisitos)

- [ ] [Ex: Ter wallet com Ledger configurado]
- [ ] [Ex: Ter mínimo 0.1 ETH para fees]
- [ ] [Ex: Entender impermanent loss]

### Processo (Passo a Passo)

1. **[Nome Etapa 1]**
   - Ação exata: [Ex: "Conectar wallet em app.lido.fi"]
   - Screenshot/Link: [Se aplicável]
   - Tempo estimado: [Ex: 2 min]

2. **[Nome Etapa 2]**
   - Ação exata: [...]
   - Validação: [Como saber que deu certo]

### Output (Resultado Esperado)

- ✅ [Ex: "stETH aparecendo na wallet"]
- ✅ [Ex: "Yield começando a acumular em ~24h"]

---

## 🤖 GATILHOS DE AUTOMAÇÃO

| Se (Condição)       | Então (Ação)                  | Prioridade |
| ------------------- | ----------------------------- | ---------- |
| [Ex: BTC cair 20%]  | [Comprar 5% portfólio]        | 🔴 Alta    |
| [Ex: Gas < 15 gwei] | [Fazer compound]              | 🟡 Média   |
| [Ex: APY < 2%]      | [Migrar para outro protocolo] | 🟢 Baixa   |

**Mínimo:** 2 gatilhos por estratégia

---

## 🚫 LISTA NEGRA (O que NÃO fazer)

❌ **Proibido:**

- [Ex: Nunca fazer LP com tokens não correlacionados]
- [Ex: Não usar protocolos sem audit]

⚠️ **Red Flags:**

- [Ex: APY > 50% em protocolo novo = suspeito]
- [Ex: TVL < $1M = risco alto]

---

## 💎 INSIGHT DE OURO

[Aquele detalhe que Lucas menciona casualmente mas vale milhões]

Exemplo: "A galera não sabe, mas você pode usar o Revoke.cash para limpar aprovações antigas e economizar gas nas próximas transações."

---

## 🔗 RECURSOS TÉCNICOS

- **Links Oficiais:** [URL protocolo, dashboard, documentação]
- **Ferramentas Necessárias:** [Ex: Ledger, Metamask, DeBank]
- **Alertas Recomendados:** [Ex: Alert de preço em X]

---

## ✅ CHECKLIST DE IMPLEMENTAÇÃO IMEDIATA

- [ ] [Tarefa concreta 1]
- [ ] [Tarefa concreta 2]
- [ ] [Tarefa concreta 3]

---

## 📊 INTEGRAÇÃO COM PROJETO

**Pasta Destino:** `02_PROJETOS/DeFi_Verso_2025/03_Renda_Passiva/[Estrategia]/`
**Atualizar:**

- [ ] Agente Lucas (adicionar regras)
- [ ] Dashboard de métricas
- [ ] Ritual Semanal (se aplicável)
```

---

## ✅ CRITÉRIOS DE QUALIDADE (Checklist de Validação)

Antes de considerar a extração completa, verificar:

### Nível 1: Básico (Mínimo Aceitável)

- [ ] Pelo menos **3 números específicos** (%, valores, limites)
- [ ] Processo tem **mínimo 3 passos** detalhados
- [ ] Identificados **2+ gatilhos** de automação
- [ ] Lista negra tem **3+ itens**

### Nível 2: Profissional (Meta)

- [ ] **5+ parâmetros** críticos documentados
- [ ] Processo é **clonável** (outra pessoa consegue executar sozinha)
- [ ] Gatilhos têm **priorização** (alta/média/baixa)
- [ ] Red flags têm **exemplos concretos**
- [ ] Tem **insight de ouro** identificável

### Nível 3: Cirúrgico (Ideal)

- [ ] **Automação n8n viável** (pode ser programada)
- [ ] **Métricas de sucesso** definidas (como medir ROI)
- [ ] **Plano B** documentado (se der errado, fazer X)
- [ ] **Timeline** realista (quanto tempo até ver resultados)

**Regra:** Mínimo Nível 2 para aprovar extração.

---

## 🔄 PROTOCOLO DE VERSIONAMENTO

### Quando uma aula contradiz outra:

1. **Identificar conflito**
   - Documentar: "Portal X Aula Y diz A, mas Portal Z Aula W diz B"

2. **Priorização por recência**
   - Portal mais recente prevalece (Lucas evoluiu estratégia)
   - Marcar versão antiga como `[DEPRECATED]`

3. **Atualizar Agente Lucas**
   - Remover regra antiga
   - Adicionar nova com nota: "Atualizado em [DATA] - Portal [X]"

4. **Manter histórico**
   - Pasta: `02_PROJETOS/DeFi_Verso_2025/historico/`
   - Arquivo: `Changelog_Estrategias.md`

---

## 📂 DESTINO DAS REGRAS (Output Final)

### Para cada aula processada, criar:

1. **Manual de Operação**
   - `02_PROJETOS/DeFi_Verso_2025/docs/Portal_1_Aula_[XX]_Manual.md`
   - Usar template acima preenchido

2. **Regras do Agente Lucas**
   - `04_RECURSOS/PROMPTS/AGENTES_SISTEMA/PROMPT_AGENTE_LUCAS_AMOEDO.md`
   - Seção: `## Regras de Execução DeFi`
   - Formato: Pseudocódigo IF-THEN

3. **Dashboard de Progresso**
   - `02_PROJETOS/DeFi_Verso_2025/STATUS_ATUAL.md`
   - Atualizar checklist de aulas processadas

4. **Relatório de Extração**
   - `00_SISTEMA/planejamento/Relatorios/Portal_1_Extracao_Completo.md`
   - Consolidado final quando todas 8 aulas forem processadas

---

## 🚀 PRÓXIMOS PASSOS

1.  **Receber Arquivos:** Aguardando usuário indicar local das 8 aulas.
2.  **Executar Extração:** Gemini processa aula por aula usando TEMPLATE acima.
3.  **Validar:** Claude revisa checklist de qualidade (Nível 2 mínimo).
4.  **Implementar:** Salvar nos 4 destinos definidos.
5.  **Ativar:** Atualizar Agente Lucas com novas regras.

**Status:** ✅ Design refinado - Pronto para execução
