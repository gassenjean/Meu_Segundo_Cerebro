# Prompt: Formatter

**IA:** Gemini CLI
**Função:** Converter e formatar textos
**Quando usar:** Rascunhos, notas brutas, conversão de formatos

---

## Comando Base

```bash
gemini "Convert/Format this text to [formato]. [Instruções específicas]." < input.txt
```

---

## Variações

### Texto → Markdown estruturado

```bash
gemini "Convert to well-formatted markdown. Add appropriate headers (##), bullet points, bold for emphasis, and code blocks where relevant." < rascunho.txt
```

### Bagunça → Organizado

```bash
gemini "Organize this messy text into clear sections with headers. Group related ideas together. Remove redundancy." < notas_bagunca.txt
```

### Lista → Tabela

```bash
gemini "Convert this list to a markdown table. Infer appropriate column headers from the content." < lista.txt
```

### Texto corrido → Bullets

```bash
gemini "Convert this paragraph into bullet points. One idea per bullet. Keep it concise." < paragrafo.txt
```

### Corrigir formatação

```bash
gemini "Fix formatting issues: consistent headers, proper spacing, correct markdown syntax. Don't change content." < doc_quebrado.md
```

### Simplificar

```bash
gemini "Simplify this text. Use shorter sentences, simpler words, remove jargon. Target: easy to understand." < complexo.md
```

### Expandir

```bash
gemini "Expand these bullet points into full paragraphs. Add context and examples." < bullets.md
```

---

## Exemplo

**Input:** Anotações rápidas de brainstorm

```
app produtividade - foco em tdah
features: pomodoro customizado, bloqueio apps, recompensas
monetização freemium
tech: react native? flutter?
competidores: forest, focus keeper
diferencial: gamificação + comunidade
mvp em 2 meses
```

**Comando:**

```bash
gemini "Convert to structured markdown with sections: Overview, Features, Business Model, Tech Stack, Competition, Differentiators, Timeline" < brainstorm.txt
```

**Output esperado:**

```markdown
## Overview

App de produtividade focado em pessoas com TDAH

## Features

- Pomodoro customizável
- Bloqueio de aplicativos distrativos
- Sistema de recompensas

## Business Model

- Modelo freemium

## Tech Stack

- Opções: React Native ou Flutter

## Competition

- Forest
- Focus Keeper

## Differentiators

- Gamificação avançada
- Comunidade integrada

## Timeline

- MVP: 2 meses
```

---

**Criado:** 17/Jan/2025
**Testado:** Sim
