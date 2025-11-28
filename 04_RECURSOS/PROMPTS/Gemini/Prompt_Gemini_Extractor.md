# Prompt: Data Extractor

**IA:** Gemini CLI
**Função:** Extrair informações estruturadas de textos
**Quando usar:** Notas de reunião, artigos, documentos com dados

---

## Comando Base

```bash
gemini "Extract [tipo de dado] from this text. Format as [formato]." < input.md
```

---

## Variações

### Extrair entidades (nomes, datas, números)
```bash
gemini "Extract all names, dates, numbers, and locations. Format as markdown table with columns: Type, Value, Context" < texto.md
```

### Extrair action items
```bash
gemini "Extract all action items, tasks, and to-dos. Format as checkbox list with owner if mentioned: - [ ] Task (@owner)" < meeting_notes.md
```

### Extrair decisões
```bash
gemini "Extract all decisions made. Format as: Decision: [what], Reason: [why], Date: [when]" < documento.md
```

### Extrair perguntas
```bash
gemini "Extract all questions (explicit or implicit). Format as numbered list." < texto.md
```

### Extrair citações
```bash
gemini "Extract notable quotes and key statements. Format: > Quote - Source" < artigo.md
```

### Extrair métricas
```bash
gemini "Extract all numbers, percentages, and metrics. Format as table: Metric, Value, Context" < relatorio.md
```

---

## Exemplo

**Input:** Notas brutas de reunião

**Comando:**
```bash
gemini "Extract: 1) Attendees, 2) Decisions made, 3) Action items with owners, 4) Next steps. Format with clear headers." < meeting_raw.txt
```

**Output esperado:**
```markdown
## Attendees
- João (PM)
- Maria (Dev)
- Carlos (Design)

## Decisions
1. Launch date: March 15th
2. Use React for frontend
3. Weekly syncs on Mondays

## Action Items
- [ ] João: Create project timeline by Friday
- [ ] Maria: Setup development environment
- [ ] Carlos: Deliver wireframes by Wednesday

## Next Steps
- Next meeting: Monday 10am
- Review wireframes before meeting
```

---

**Criado:** 17/Jan/2025
**Testado:** Sim
