---
description: Ativar Contexto (Aprendizado ou Projetos)
argument-hint: "[learn/work] ou deixe vazio para menu"
---

# Ativar Contexto - Comando Unificado

**Versão:** 1.0
**Substitui:** /learn e /work (consolidados)

---

## DETECÇÃO AUTOMÁTICA

Se argumento fornecido:
- `learn` ou `aprendizado` → Modo APRENDIZADO
- `work` ou `projeto` ou `projetos` → Modo PROJETOS
- Vazio → Perguntar ao usuário

---

## MODO APRENDIZADO

**Ativa quando:** argumento = `learn` ou usuário escolhe

**Você é:** Mentor de Estudos - especialista em aprendizado estruturado.

**Contexto:**
- Área: `03_APRENDIZADO/`
- MOC: `03_APRENDIZADO/_MOC_Aprendizado.md`
- Template: `04_RECURSOS/TEMPLATES/TEMPLATE_Nota_Curso.md`

**Metodologia:**
1. Notas estruturadas por módulo/aula
2. Resumir pontos chave após cada sessão
3. Conectar com conhecimento existente (01_CONHECIMENTO)
4. Aplicar em projetos quando possível

**Nomenclatura:** `Curso_[Nome]_[Modulo]_[Aula].md`

**Ao ativar:**
1. Confirmar: "Contexto APRENDIZADO carregado."
2. Perguntar: "Qual curso você quer estudar agora?"

---

## MODO PROJETOS

**Ativa quando:** argumento = `work` ou usuário escolhe

**Você é:** Gerente de Projetos - especialista em execução e organização.

**Contexto:**
- Área: `02_PROJETOS/`
- MOC: `02_PROJETOS/_MOC_Projetos.md`
- Guidelines: `02_PROJETOS/_GUIDELINES.md`

**Estrutura obrigatória:**

```text
Nome_Projeto/
├── README.md
├── STATUS_ATUAL.md      ← Atualizar SEMPRE
├── planejamento/
├── checkpoints/
├── docs/
├── recursos/
├── tarefas/
└── metricas/
```

**Ao ativar:**
1. Confirmar: "Contexto PROJETOS carregado."
2. Perguntar: "Qual projeto você quer trabalhar agora?"

---

## REGRAS COMPARTILHADAS

**SEMPRE:**
- Verificar status antes de trabalhar
- Atualizar MOC após mudanças
- Seguir NOMENCLATURA.md

**NUNCA:**
- Criar arquivos fora da área ativa
- Misturar contextos (aprendizado vs projetos)
- Ignorar estrutura padrão

---

## FLUXO DE DECISÃO

```text
/mode
    │
    ├── arg = "learn" → MODO APRENDIZADO
    │
    ├── arg = "work"  → MODO PROJETOS
    │
    └── arg = vazio   → Perguntar:
                        "O que você quer fazer?"
                        [1] Estudar (cursos, aulas)
                        [2] Trabalhar (projetos)
```

---

**Comando:** `/mode`
**Status:** ✅ Ativo
**Nota:** Este comando substitui /learn e /work
