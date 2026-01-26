# HANDOFF: Processar Portal 3 DeFi - Análise de Projetos

**ID:** T029
**De:** Claude (Névoa)
**Para:** Gemini (Guardian/IO)
**Data:** 26/Jan/2026
**Prioridade:** CRÍTICA

---

## 1. Contexto

O curso Mente de Tubarão tem 5 portais (módulos). Os portais 1-5 foram parcialmente processados, mas o **Portal 3 (Análise de Projetos)** é crítico para o agente `/lucas` funcionar plenamente.

**Impacto:** Sem Portal 3, /lucas não consegue analisar tokens novos com metodologia completa.

---

## 2. Tarefa

**Ação:** Processar aulas e criar manuais de análise

**Objeto:** Conteúdo do Portal 3 em `03_APRENDIZADO/Investimentos_Crypto/Mente_De_Tubarao/`

**Condição:** Entregar:
1. Framework de análise de projetos (checklist estruturado)
2. Manuais práticos por categoria (tokenomics, team, produto, etc.)
3. Red flags compilados
4. Template de análise para /lucas usar

---

## 3. Ferramenta Google Necessária

| Ferramenta | Squad | Motivo |
| ---------- | ----- | ------ |
| Antigravity (IO) | Research | Processamento de curso |
| NotebookLM | - | Opção para áudio se disponível |

---

## 4. Inputs (O que Gemini precisa)

**Arquivos:**
- [ ] `03_APRENDIZADO/Investimentos_Crypto/Mente_De_Tubarao/` (estrutura completa)
- [ ] Especificamente Portal_3 ou módulo de análise de projetos
- [ ] Transcrições de aulas se disponíveis

**Contexto adicional:**
- Curso criado por Lucas Amoedo (referência real para o agente /lucas)
- Metodologia: Benjamin Graham adaptada para crypto
- Foco: análise fundamentalista, não técnica

---

## 5. Output Esperado

**Formato:** Markdown

**Local de entrega:** `01_CONHECIMENTO/Financas/DeFi/Analise_Projetos/`

**Arquivos a criar:**

```text
01_CONHECIMENTO/Financas/DeFi/Analise_Projetos/
├── FRAMEWORK_ANALISE_PROJETOS.md
├── MANUAL_TOKENOMICS.md
├── MANUAL_ANALISE_TEAM.md
├── MANUAL_ANALISE_PRODUTO.md
├── MANUAL_RED_FLAGS.md
└── TEMPLATE_ANALISE_TOKEN.md
```

**Estrutura do Framework:**

```markdown
# FRAMEWORK: Análise de Projetos DeFi

## Metodologia
[Baseada em Benjamin Graham + Lucas Amoedo]

## Checklist de Análise

### 1. Team (Peso: 25%)
- [ ] Doxxed?
- [ ] Track record?
- [ ] LinkedIn verificável?
...

### 2. Tokenomics (Peso: 30%)
- [ ] Supply total?
- [ ] Distribuição?
- [ ] Vesting?
...

### 3. Produto (Peso: 25%)
- [ ] MVP existe?
- [ ] Usuários ativos?
- [ ] Revenue?
...

### 4. Mercado (Peso: 20%)
- [ ] TAM/SAM/SOM?
- [ ] Concorrentes?
- [ ] Diferencial?
...

## Scoring
| Score | Classificação | Ação |
| ----- | ------------- | ---- |
| 80-100 | A+ | Entrada agressiva |
| 60-79 | B | Entrada conservadora |
| 40-59 | C | Watchlist |
| <40 | F | Evitar |
```

---

## 6. Quality Gate

Antes de marcar como completo, verificar:

- [ ] Completo? (Framework + 4 manuais + template)
- [ ] Correto? (Metodologia fiel ao curso)
- [ ] Útil? (/lucas pode usar imediatamente)
- [ ] Limpo? (Nomenclatura segue padrão vault)

---

## 7. Comunicação

**Ao concluir:**
1. Atualizar `state.json` (status: completed)
2. Atualizar `_MOC_DeFi.md` com links para novos arquivos
3. Notificar Claude para atualizar /lucas

---

**Status:** Pendente
**Criado por:** Névoa 6.0
**Dependentes:** /lucas, researcher-defi
