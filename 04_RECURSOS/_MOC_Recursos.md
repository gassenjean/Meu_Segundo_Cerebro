---
criado: 2025-11-18T10:43:54-03:00
atualizado: 2025-11-25T00:02:22-03:00
---
# 🛠️ MOC: RECURSOS

**Map of Content - Templates, Prompts e Ferramentas**

**Criado:** 17/Jan/2025
**Última atualização:** 24/Nov/2025
**Total de recursos:** 15

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

### PROMPTS/Claude/
Prompts especializados para Claude

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
📁 Total de recursos: 15
📄 Templates: 6 (4 base + 2 Metodologia IA)
✅ Checklists: 1 (200+ verificações)
📖 Guias: 3 (Metodologia Profissional IA completa)
🤖 Prompts Claude: 2
🤖 Prompts Gemini: 4
⚙️ Workflows: 0
📅 Último recurso criado: 24/Nov/2025
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
