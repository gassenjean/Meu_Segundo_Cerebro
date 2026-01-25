---
created: 2026-01-25T12:27
updated: 2026-01-25T12:28
---
# CONCEITOS: Context Engineering & RPI (Valdemar Neto)

**Fonte:** Valdemar Neto - Por_que_IA_falha_em_codebases_grandes__e_como_eu_resolvi_iss.pdf
**Categoria:** Metodologia / Arquitetura de Contexto
**Tags:** #context-engineering #RPI #grandes-codebases #produtividade

---

## 1. Smart Zone vs Dumb Zone (Regra dos 40%)

### O Que É

A gestão da janela de contexto da LLM para evitar alucinações.

- **Smart Zone (< 40-60% da janela):** Onde a IA é efetiva, acurada e inteligente.
- **Dumb Zone (> 60% da janela):** Onde a "máquina de probabilidade" começa a falhar, perder o início do contexto e alucinar.

### Por Que Importa

"Um milhão de tokens ter mais... não quer dizer que é melhor". Encher a janela dilui a atenção da IA. Codebases grandes (300k+ linhas) invariavelmente estouram isso se não gerenciados.

### Como Aplicar

Mantenha o contexto sempre leve (idealmente ~200k tokens ou 30-40% da capacidade). Se passar disso, é hora de limpar ou segmentar.

---

## 2. Framework RPI (Research, Plan, Implement)

### O Que É

A metodologia core para lidar com tarefas complexas em grandes codebases sem estourar o contexto.

#### Fase 1: Research (Pesquisa)

- **Objetivo:** Descobrir onde estão as coisas, entender o problema.
- **Contexto:** Alto (carrega muitos arquivos para leitura).
- **Ação:** "Fazer um prompt primeiro para descobrir".
- **Saída:** Um **Plano** ou Documento de Memória de Longo Prazo. Não gera código final aqui.

#### Fase 2: Plan (Planejamento)

- **Objetivo:** Detalhar a execução.
- **Contexto:** Médio (focado no plano).
- **A importância:** "Por que o plano é tão importante? Porque ele detalha exatamente o que ele precisa fazer." Um bom plano permite execução "one shot".
- **Saída:** Um plano de implementação detalhado, dividido em fases se necessário.

#### Fase 3: Implement (Implementação)

- **Objetivo:** Escrever o código.
- **Contexto:** **MÍNIMO (~30%)**.
- **Segredo:** Você **não** carrega toda a pesquisa. Você carrega **apenas o plano** e os arquivos estritamente necessários para aquela fase específica.
- **Ação:** Executar sub-planos (Fase 1, Fase 2...).

### Aplicação no Bi-IA

Isso valida nosso fluxo atual:

1. `Research` -> (Notebook LM / Deep Research)
2. `Plan` -> `implementation_plan.md` (Task Planning)
3. `Implement` -> Execução focada com `task.md` e checklist.

---

## 3. Progressive Disclosure (Contexto Gradual)

### O Que É

Ir entregando para a LLM as informações de forma gradual, apenas o que ela precisa para o momento.

### Como Aplicar

Estruturar documentos de contexto (markdowns) em diretórios específicos ou por responsabilidade. Não ter um único "README gigante", mas sim `Architecture Guidelines`, `Domain Guidelines`, etc., que são carregados apenas quando o assunto é pertinente.

---

## 4. On-Demand Loading (Carregamento Sob Demanda)

### O Que É

Configurar o ambiente (via `.cursorrules`, `.cloud-settings` ou Skills) para carregar contextos específicos baseados em gatilhos (triggers).

### Exemplo Concreto

- O usuário pede "Analise a complexidade".
- O sistema carrega **apenas** o arquivo `ComplexityAnalysisRules.md`.
- Ele **não** carrega o `DatabaseSchema.md` pois é irrelevante.

### Como Aplicar

Criar Skills no Gemini ou regras no Claude que ativem contextos específicos baseados em palavras-chave do prompt.

---

## 5. Memória de Longo Prazo (Arquivos de Saída)

### O Que É

Salvar o resultado da fase de Research em um arquivo Markdown estático.

### Por Que Importa

LLMs são *stateless* (sem estado). Se você faz uma pesquisa longa e não salva, perdeu aqueles tokens e o raciocínio. Ao salvar em um arquivo, você "congela" a inteligência da IA num formato barato de carregar depois.

### Como Aplicar

Sempre terminar uma sessão de pesquisa complexa com a criação de um artefato (ex: `contexto_do_problema_X.md`). Na próxima sessão, carregue esse arquivo em vez de rodar a pesquisa de novo.

---

## 6. Quebrando Planos em Sub-Planos

### O Que É

Para refatorações grandes ou features complexas, um único plano também pode ficar grande demais para a janela de contexto da implementação.

### Técnica

1. Gere o "Plano Mestre" (visão geral).
2. Quebre em "Sub-Planos de Implementação" (Fase 1, Fase 2, Fase 3...).
3. Execute cada fase em uma sessão (ou janela) limpa, carregando apenas o sub-plano daquela fase.

> "A janela de contexto vai se manter pequena, porque ele é pequeno... e dá um contexto para IA do que carregar."

---

## 7. Spec Driven vs RPI

### O Que É

O esclarecimento de que RPI não substitui Spec Driven Development (SDD), mas o contém.

- **SDD:** Usar uma especificação (PRD, API Spec) como base.
- **RPI:** O processo lógico de usar essa spec.
  - Research: Entender a spec.
  - Plan: Planejar como implementar a spec.
  - Implement: Codar a spec.

### Veredito

RPI é o "como fazemos", Spec Driven é "o que usamos".
