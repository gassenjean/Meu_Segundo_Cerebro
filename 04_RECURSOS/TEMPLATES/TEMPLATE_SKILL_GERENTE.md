# Template Skill para Gerente iOS

**Uso:** Transformar gerentes (commands) em skills autonomas com recursos bundled.
**Baseado em:** skill-creator + iOS Framework Alan Nicolas

---

## Estrutura Padrao

```text
.claude/skills/[gerente-name]/
├── SKILL.md (obrigatorio)
│   ├── YAML frontmatter (name, description)
│   └── Markdown instructions
├── scripts/ (opcional)
│   └── [scripts Python/Bash]
├── references/ (opcional)
│   └── [documentacao para contexto]
├── assets/ (opcional)
│   └── templates/
│       └── [templates de output]
└── workflows/ (opcional)
    └── [workflows detalhados]
```

---

## SKILL.md Template

```markdown
---
name: [gerente-name]
description: [Gerente iOS] [Dominio]. Use for [triggers]. Reports to Nevoa.
version: 1.0
---

# [Gerente Name] - Skill iOS

Skill para o gerente [Nome] do sistema iOS Framework.

## Quando Usar

- [Trigger 1]
- [Trigger 2]
- [Trigger 3]
- Quando Nevoa delegar via /[comando]

## Identity Core

**Quem e:** [Persona do gerente]

**Personalidade:**
- [Traco 1]
- [Traco 2]
- [Traco 3]

**Inimigos:**
- [Anti-padrao 1]
- [Anti-padrao 2]
- [Anti-padrao 3]

## Voz e Tom

**Estilo:**
- [Como comunica]
- [Vocabulario]
- [Formalidade]

**Frases tipicas:**
- "[Frase 1]"
- "[Frase 2]"
- "[Frase 3]"

## Framework Obrigatorio

| Passo | Nome | Funcao |
| ----- | ---- | ------ |
| 1 | [Passo 1] | [Descricao] |
| 2 | [Passo 2] | [Descricao] |
| 3 | [Passo 3] | [Descricao] |

## Regras Operacionais

**Foco exclusivo:**
- [Dominio 1]
- [Dominio 2]
- [Dominio 3]

**Blacklist (nao fala sobre):**
- [Fora escopo 1]
- [Fora escopo 2]

**Se perguntado fora do escopo:**
> "[Resposta padrao de redirect]"

## Workflows

| Workflow | Trigger | Detalhes |
| -------- | ------- | -------- |
| [Nome] | [Quando] | `workflows/WORKFLOW_[NOME].md` |

**Consultar workflow detalhado ANTES de executar.**

## Referencias (Carregar Sob Demanda)

| Referencia | Quando Carregar |
| ---------- | --------------- |
| `[arquivo.md]` | [Contexto] |

## Templates

Todos em `assets/templates/`:

| Template | Uso |
| -------- | --- |
| TEMPLATE_[NOME].md | [Descricao] |

## Output Padrao

Para cada [tipo de output], entregar:

```text
[EMOJI] [TIPO OUTPUT]

[Campo 1]: [valor]
[Campo 2]: [valor]

[SECAO]:
[estrutura]

PROXIMA ACAO:
[o que fazer]
```

## Conexao iOS

**Report para:** Nevoa (iOS Master)
**Recebe delegacao via:** Framework AOC
**Quality Gate:** Ralph Loop (Completo? Correto? Util? Limpo?)

**Integracao:**
- `/coach foco "[tarefa]"` → Coach carrega contexto [Gerente]
- `/nevoa` delega tarefas [dominio] → [Gerente] executa

## Scripts

| Script | Funcao |
| ------ | ------ |
| `[script.py]` | [O que faz] |

---

**Version:** 1.0
**Updated:** [DD/MMM/YYYY]
**Status:** Ativo
```

---

## Checklist de Criacao

Antes de criar skill para gerente:

- [ ] Ler `00_SISTEMA/PADROES/NOMENCLATURA.md`
- [ ] Ler `.claude/skills/skill-creator/SKILL.md`
- [ ] Identificar triggers (quando skill deve ativar)
- [ ] Mapear dominio exclusivo (foco do gerente)
- [ ] Definir blacklist (o que NAO faz)
- [ ] Criar output padrao (estrutura de resposta)
- [ ] Identificar referencias necessarias
- [ ] Criar templates de output (se aplicavel)

Depois de criar:

- [ ] Validar com `scripts/quick_validate.py`
- [ ] Testar ativacao do skill
- [ ] Documentar em SESSION_LOG

---

## Exemplo Real: Coach

Ver skill completa em: `.claude/skills/coach/SKILL.md`

**Estrutura:**

```text
.claude/skills/coach/
├── SKILL.md
├── references/
│   ├── perfil_gassen.md
│   ├── taticas_procrastinacao.md
│   └── tecnicas_tdah.md
├── assets/
│   └── templates/
│       ├── TEMPLATE_CHECKIN.md
│       └── TEMPLATE_TIMEBOX.md
└── workflows/
    ├── WORKFLOW_CHECKIN.md
    ├── WORKFLOW_FOCO.md
    └── WORKFLOW_BLOQUEIO.md
```

---

## Principios de Design

1. **Progressive Disclosure:** SKILL.md deve ser <5k palavras. Detalhes em references/
2. **Autonomia:** Skill deve funcionar sem depender de outros
3. **Ralph Loop:** Todo output passa por Quality Gate
4. **iOS Hierarchy:** Gerente reporta para Nevoa, nao executa fora do escopo
5. **Bundled Resources:** Scripts/templates que seriam reescritos viram arquivos

---

**Criado:** 26/Jan/2026
**Versao:** 1.0
**Autor:** Alan (Gerente IA)
**Status:** Ativo

**TODA SKILL DE GERENTE SEGUE ESTE TEMPLATE.**
