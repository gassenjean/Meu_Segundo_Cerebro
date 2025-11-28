# Prompt: Summarizer

**IA:** Gemini CLI
**Função:** Resumir textos longos em bullet points
**Quando usar:** Artigos, transcrições, documentos extensos

---

## Comando

```bash
gemini "Summarize this text in [N] bullet points in Portuguese. Be concise and capture the main ideas. Format: - Point" < input.md
```

## Variações

### Resumo curto (5 pontos)
```bash
gemini "Summarize in 5 bullet points in Portuguese. Focus on key takeaways." < input.md
```

### Resumo médio (10 pontos)
```bash
gemini "Summarize in 10 bullet points in Portuguese. Include main arguments and evidence." < input.md
```

### Resumo executivo
```bash
gemini "Create executive summary (max 100 words) in Portuguese. Start with the main conclusion." < input.md
```

### Com categorias
```bash
gemini "Summarize in Portuguese with these categories: Main Idea, Key Points, Action Items, Questions" < input.md
```

---

## Exemplo

**Input:** Artigo de 3000 palavras sobre produtividade

**Comando:**
```bash
gemini "Summarize in 7 bullet points in Portuguese. Focus on actionable advice." < artigo_produtividade.md
```

**Output esperado:**
```markdown
- Técnica Pomodoro aumenta foco em 40% segundo estudos
- Bloquear distrações digitais é mais efetivo que força de vontade
- Tarefas difíceis devem ser feitas nas primeiras 2h do dia
- Listas de 3 itens são mais efetivas que listas longas
- Pausas de 5-10 min a cada hora previnem fadiga mental
- Ambiente físico organizado reduz carga cognitiva
- Revisão semanal de metas mantém direção clara
```

---

**Criado:** 17/Jan/2025
**Testado:** Sim
