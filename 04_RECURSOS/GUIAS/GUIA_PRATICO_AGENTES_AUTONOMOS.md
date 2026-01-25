---
created: 2026-01-25
updated: 2026-01-25
tags:
  - guia
  - agentes
  - metodologia
  - pratico
---

# Guia Prático: Agentes Autônomos

Zero teoria. Só receita.

---

## Antes de Qualquer Coisa

```text
[ ] Eu sei fazer essa tarefa manualmente?
[ ] Já fiz pelo menos 3x e odiei?
[ ] Consigo explicar em 3 frases o que quero?

Se NÃO para qualquer uma → NÃO delegue ainda.
```

---

## Método MAPA (4 Passos)

### M - Mapear (5 min, papel/obsidian)

```text
TAREFA: _______________________
OUTPUT ESPERADO: _______________
QUEM FAZ: [ ] Claude [ ] Gemini [ ] Outro
DEPENDE DE: ____________________
```

### A - Atomizar (quebrar em pedaços)

```text
Tarefa Grande → Micro-tarefas

Exemplo:
"Criar landing page" →
  1. Definir estrutura (Header, Hero, CTA)
  2. Escrever copy do Hero
  3. Escrever copy do CTA
  4. Montar HTML
  5. Revisar
```

### P - Programar (escrever instruções)

Use este template:

```markdown
## TAREFA
[O que fazer em 1 frase]

## CONTEXTO
[Arquivos para ler, informações necessárias]

## OUTPUT
- Formato: [MD/JSON/Código]
- Onde salvar: [caminho]
- Tamanho: [estimativa]

## REGRAS
- NÃO faça: [lista do que evitar]
- SEMPRE faça: [lista obrigatória]

## VALIDAÇÃO
- [ ] Critério 1
- [ ] Critério 2
```

### A - Ativar (executar e SOLTAR)

```text
1. Cole o prompt
2. Deixe rodar
3. NÃO interrompa (a menos que alucine)
4. Valide no final
```

---

## Hierarquia de Agentes (Quem Chamar)

### Nível 1: Orquestração

| Comando | Quando Usar |
| ------- | ----------- |
| `/nevoa` | Não sabe qual agente chamar |
| `/coach` | Precisa de foco e direção |

### Nível 2: Domínio Específico

| Comando | Domínio | Exemplo |
| ------- | ------- | ------- |
| `/alan` | IA & Automação | Criar workflow n8n |
| `/pedro` | Tráfego & Marketing | Analisar campanha |
| `/lucas` | DeFi & Investimentos | Avaliar protocolo |
| `/elena` | TDAH & Produtividade | Organizar dia |
| `/dr-green` | Cultivo | Pesquisa especializada |

### Nível 3: Operacional

| Comando | Função |
| ------- | ------ |
| `/validate` | Antes de criar arquivo |
| `/mapa` | Ver índice do vault |
| `/marie-kondo` | Organizar/limpar |

### Nível 4: Projetos

| Comando | Projeto |
| ------- | ------- |
| `/kabak` | E-commerce KabaK |
| `/kabak-agent` | Gerente do projeto |

### Nível 5: Delegação em Massa

| Comando | Quando |
| ------- | ------ |
| `/gemini` | Tarefas >50k tokens |
| `/gemini-handoff` | Preparar delegação estruturada |

---

## Template de Handoff (Copiar e Colar)

```markdown
## HANDOFF PARA GEMINI

### Objetivo
[1 frase clara]

### Output Esperado
- Arquivo: [caminho completo]
- Formato: [MD/JSON/etc]
- Tamanho: [~X palavras]

### Fontes (Ler Antes)
1. [arquivo 1]
2. [arquivo 2]

### Estrutura Obrigatória
1. [seção 1]
2. [seção 2]
3. [seção 3]

### NÃO Fazer
- [restrição 1]
- [restrição 2]

### Validação
- [ ] [critério 1]
- [ ] [critério 2]
```

---

## 3 Cenários Práticos

### Cenário 1: Processar Curso (Bulk)

```text
1. /gemini-handoff
2. Objetivo: "Extrair insights do módulo X"
3. Fontes: pasta do curso
4. Output: RESUMO_MODULO_X.md em 03_APRENDIZADO/
5. Validação: tem os 5 pontos principais?
```

### Cenário 2: Criar Conteúdo (Copy)

```text
1. /pedro (contexto de marketing)
2. Tarefa: "Headlines para campanha Y"
3. Dar: público, produto, tom
4. Output: 10 headlines
5. Validação: fala com a dor do cliente?
```

### Cenário 3: Organizar Vault

```text
1. /marie-kondo
2. Tarefa: "Limpar pasta X"
3. Regras: seguir NOMENCLATURA.md
4. Output: arquivos reorganizados
5. Validação: /validate confirmou?
```

---

## Quando Dá Errado (Troubleshooting)

| Problema | Causa Provável | Solução |
| -------- | -------------- | ------- |
| Agente alucina | Contexto insuficiente | Dar mais arquivos de referência |
| Output errado | Instrução ambígua | Reescrever com exemplo |
| Demora muito | Tarefa grande demais | Atomizar mais |
| Ignora regras | Regras no fim do prompt | Mover regras para o INÍCIO |
| Formato errado | Não especificou | Adicionar "Formato: [X]" |

---

## Checklist Diário (Agent-First)

```text
MANHÃ (5 min)
[ ] O que vou delegar hoje?
[ ] Tenho os inputs prontos?
[ ] Qual agente usar?

EXECUÇÃO
[ ] Handoff preparado?
[ ] Critérios de validação definidos?
[ ] Ativei e SOLTEI?

FIM DO DIA
[ ] Validei outputs?
[ ] Loguei no SESSION_LOG?
[ ] Próximas delegações identificadas?
```

---

## Regra de Ouro

> "Só automatize o que você já fez manualmente 3x e odiou."
> — Alan Nicolas

---

## Links Rápidos

- Método MAPA completo: `02_PROJETOS/Estudo_Alan_Nicolas/WIKI/MANUAL_ENGENHARIA_DE_AGENTES.md`
- Sistema 5C: `02_PROJETOS/Estudo_Alan_Nicolas/Alan_Nicolas_Metodo_5C.md`
- Névoa 3.0: `04_RECURSOS/PROMPTS/Agentes_Sistema/PROMPT_NEVOA_3.0.md`
- Gemini Handoff: `.claude/skills/gemini-handoff/SKILL.md`
- Plano Master: `00_SISTEMA/planejamento/PLANO_MASTER_2026.md`
