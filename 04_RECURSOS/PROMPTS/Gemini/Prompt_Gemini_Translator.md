# Prompt: Translator

**IA:** Gemini CLI
**Função:** Traduzir documentos entre idiomas
**Quando usar:** Artigos em inglês, documentação técnica, conteúdo para traduzir

---

## Comando

### Inglês → Português

```bash
gemini "Translate to Brazilian Portuguese. Maintain original formatting, tone, and technical terms. Keep code blocks unchanged." < input_en.md > output_pt.md
```

### Português → Inglês

```bash
gemini "Translate to English. Maintain formatting and professional tone. Keep proper nouns unchanged." < input_pt.md > output_en.md
```

---

## Variações

### Tradução técnica
```bash
gemini "Translate to Portuguese. Keep technical terms in English when commonly used (API, framework, etc). Maintain code examples." < doc_en.md
```

### Tradução informal
```bash
gemini "Translate to Brazilian Portuguese with casual, friendly tone. Use 'você' instead of formal forms." < text_en.md
```

### Tradução com glossário
```bash
gemini "Translate to Portuguese. Use these translations: 'workflow'='fluxo de trabalho', 'insight'='insight', 'deadline'='prazo'" < doc_en.md
```

---

## Exemplo

**Input:** README de projeto em inglês

**Comando:**
```bash
gemini "Translate to Brazilian Portuguese. Keep technical terms, code blocks, and URLs unchanged. Maintain markdown formatting." < README_en.md > README_pt.md
```

**Dica:** Sempre revise traduções técnicas para garantir precisão.

---

**Criado:** 17/Jan/2025
**Testado:** Sim
