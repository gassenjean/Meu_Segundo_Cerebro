---
criado: 2025-11-18T10:43:54-03:00
atualizado: 2026-01-16T11:16:59-03:00
---
# 🛠️ MOC: RECURSOS

**Map of Content - Templates, Prompts e Ferramentas**

**Criado:** 17/Jan/2025
**Última atualização:** 26/Jan/2026
**Total de recursos:** 23

---

## 🎯 O QUE É ESTA ÁREA

Biblioteca de recursos reutilizáveis:
- Templates de documentos
- Prompts de IA (Claude, Gemini)
- Workflows de automação
- Ferramentas e scripts

**Princípio:** Não reinventar a roda. Criar uma vez, usar sempre.

---

## 📂 ESTRUTURA

### TEMPLATES/
Templates de documentos reutilizáveis

**Disponíveis:**
- [[TEMPLATE_Projeto_Padrao.md]] ← Estrutura de projeto
- [[TEMPLATE_Checkpoint.md]] ← Snapshot de progresso
- [[TEMPLATE_MOC.md]] ← Map of Content
- [[TEMPLATE_Nota_Curso.md]] ← Nota de aula

**Metodologia Profissional IA:**
- [[TEMPLATES/Metodologia_IA/TEMPLATE_Briefing_Projeto.md]] ← Briefing completo de projeto
- [[TEMPLATES/Metodologia_IA/TEMPLATE_PRD_Tecnico.md]] ← Product Requirements Document técnico

**Agentes:**
- [[TEMPLATES/Agentes/Prompt_Clone.md]] ← Framework base para criar clones de IA (SDR, Copywriter, etc)

**RPI Workflow (Research-Plan-Implementation):**
- [[TEMPLATES/TEMPLATE_RPI_MASTER_PLAN.md]] ← Master plan para grandes refatorações
- [[TEMPLATES/TEMPLATE_RPI_IMPLEMENTATION_PHASE.md]] ← Sub-plans de implementação detalhados
- [[TEMPLATES/TEMPLATE_RPI_RESEARCH_OUTPUT.md]] ← Documentação da fase de pesquisa

### PROMPTS/Bibliotecas/
Bibliotecas e colecoes de prompts

**Disponíveis:**
- [[Biblioteca_36_Prompts.md]] - 36 prompts profissionais Alan Nicolas (TOP 10 + 26)

### PROMPTS/Utilidades/
Prompts utilitarios para extracao e processamento

**Disponíveis:**
- [[Prompt_Framework_Extractor.md]] - Ultimate Course Framework Extractor v2.0

### PROMPTS/Funcionais/
Prompts funcionais para Claude

**Disponíveis:**
- [[_MOC_Clones_Alan_Nicolas.md]] - MOC dos clones
- [[Prompt_Claude_Alan_IA_Avaliador.md]] - Avaliador de sistemas

### PROMPTS/Gemini/
Prompts especializados para Gemini CLI

**Disponíveis:**
- [[Prompt_Gemini_Summarizer.md]] - Resumir textos
- [[Prompt_Gemini_Translator.md]] - Traduzir PT↔EN
- [[Prompt_Gemini_Extractor.md]] - Extrair dados
- [[Prompt_Gemini_Formatter.md]] - Formatar texto

### CHECKLISTS/
Checklists de validação e revisão

**Disponíveis:**
- [[CHECKLISTS/CHECKLIST_Revisao_Projeto.md]] ← 200+ verificações de qualidade

### GUIAS/
Guias completos e metodologias

**Disponíveis:**
- [[GUIAS/MOC_Metodologia_Profissional_IA.md]] ← Hub central Metodologia IA
- [[GUIAS/METODOLOGIA_PROFISSIONAL_IA.md]] ← Metodologia completa (5 etapas)
- [[GUIAS/PLANO_ACAO_7_DIAS_Metodologia_IA.md]] ← Plano implementação 7 dias
- [[GUIAS/Guia_para_um_Bom_Prompt.md]] ← 8 tecnicas para prompts eficazes

### WORKFLOWS/
Automações e scripts

**Disponíveis:**
- (adicionar conforme criar)

---

## 📋 COMO USAR

### Usando Templates

1. **Encontre o template certo** (lista acima)
2. **Copie para o destino:**
   ```bash
   # Via Claude Code:
   /work "Create [tipo] using [template] in [local]"
   ```
3. **Preencha os campos**
4. **Remova instruções do template**

### Usando RPI Workflow

**Para grandes refatorações/features (3+ semanas):**

1. **RESEARCH PHASE:**
   - Use `TEMPLATE_RPI_RESEARCH_OUTPUT.md`
   - Investigue codebase, identifique problemas, riscos
   - Output: Documento de pesquisa completo

2. **PLANNING PHASE:**
   - Use `TEMPLATE_RPI_MASTER_PLAN.md`
   - Quebre em fases e sub-plans
   - Defina success criteria, timeline, riscos

3. **IMPLEMENTATION PHASE:**
   - Para cada sub-plan: use `TEMPLATE_RPI_IMPLEMENTATION_PHASE.md`
   - Implemente em chunks pequenos e validáveis
   - Valide: testes passando, build OK, 100% casos cobertos

**Quando usar RPI:**
- Refatorações grandes (meses de trabalho)
- Features complexas com múltiplas dependências
- Quando precisa quebrar em partes reviewáveis
- Migrações de sistemas críticos

### Criando Novo Template

1. **Nomeie corretamente:**
   ```
   TEMPLATE_[Tipo]_[Nome].md
   ```

2. **Estrutura do template:**
   ```markdown
   # [Título]

   > Template para [descrição]
   > Remova este bloco após usar

   ---

   [Conteúdo com placeholders]
   [Campo]: [Descrição do que colocar]

   ---

   **Template criado:** [Data]
   **Versão:** [X.X]
   ```

3. **Adicione a este MOC**

### Usando Prompts

1. **Encontre o prompt certo** (lista acima)
2. **Copie o prompt**
3. **Adapte variáveis se necessário**
4. **Execute na IA correspondente**

### Criando Novo Prompt

1. **Nomeie corretamente:**
   ```
   Prompt_[IA]_[Funcao].md
   ```

2. **Estrutura do prompt:**
   ```markdown
   # Prompt: [Nome]

   **IA:** Claude/Gemini
   **Função:** [O que faz]
   **Quando usar:** [Situações]

   ---

   ## Prompt

   ```
   [Texto do prompt aqui]
   ```

   ## Variáveis

   - `[VAR1]`: [O que colocar]
   - `[VAR2]`: [O que colocar]

   ## Exemplo de Uso

   [Exemplo prático]

   ---

   **Criado:** [Data]
   **Testado:** [Sim/Não]
   ```

3. **Adicione a este MOC**

---

## 📊 ESTATÍSTICAS

```
📁 Total de recursos: 23
📄 Templates: 10 (4 base + 2 Metodologia IA + 3 RPI Workflow + 1 Agentes)
✅ Checklists: 1 (200+ verificações)
📖 Guias: 4 (Metodologia Profissional IA completa + Bom Prompt)
📚 Bibliotecas: 1 (36 prompts profissionais)
🔧 Utilidades: 1 (Framework Extractor)
🤖 Prompts Funcionais: 2
🤖 Prompts Gemini: 4
⚙️ Workflows: 0
📅 Última atualização: 26/Jan/2026
```

---

## 🔗 LINKS

### MOCs Relacionados
- [[00_SISTEMA/MOCs/MOC_SEGUNDO_CEREBRO_MASTER.md]] - MOC principal
- [[_MOC_Projetos.md]] - Onde usar templates
- [[_MOC_Conhecimento.md]] - Onde documentar prompts

### Padrões
- [[00_SISTEMA/PADROES/NOMENCLATURA.md]] - Como nomear
- [[00_SISTEMA/PADROES/ESTRUTURA_PROJETOS.md]] - Estrutura padrão

---

## ✅ MANUTENÇÃO

### Mensal
- [ ] Revisar templates (ainda relevantes?)
- [ ] Atualizar prompts (melhorias?)
- [ ] Testar workflows (ainda funcionam?)
- [ ] Atualizar estatísticas

### Trimestral
- [ ] Consolidar templates similares
- [ ] Arquivar recursos não usados
- [ ] Criar novos baseado em necessidades

---

**Criado:** 17/Jan/2025
**Versão:** 1.0

**RECURSOS PRONTOS = PRODUTIVIDADE! 🛠️**
