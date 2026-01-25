---
description: Pesquisar e extrair conteúdo do vault Mente Lendária (Alan Nicolas)
argument-hint: "inventario | extrair [tema] | sync | status"
---

# Alan Vault Researcher

Acessa o vault do Alan Nicolas (mentelendaria.com) para pesquisa e extração ética.

---

## Comandos Disponíveis

```bash
/alan-vault inventario     # Ver mapa completo
/alan-vault extrair [tema] # Extrair tema específico
/alan-vault sync           # Verificar novidades
/alan-vault status         # Progresso da extração
```

---

## Contexto Carregado

- `.claude/skills/alan-vault-researcher/SKILL.md`
- `.claude/skills/alan-vault-researcher/INVENTARIO_MENTE_LENDARIA.md`

---

## Uso Rápido

### Ver o que existe

```bash
/alan-vault inventario
```

### Extrair tema específico

```bash
/alan-vault extrair "Sistema 5C"
/alan-vault extrair "Método MAPA"
/alan-vault extrair "Prompts de Clone"
```

### Verificar novidades

```bash
/alan-vault sync
```

---

## Protocolo Ético

Toda extração segue:
1. Síntese em palavras próprias
2. Citação da fonte original
3. Aplicação ao seu contexto
4. Validação anti-plágio

---

## Integração

- `/gemini` - Para extrações em massa
- `/alan` - Contexto IA & Automação
- `/mapa` - Índice do vault local
