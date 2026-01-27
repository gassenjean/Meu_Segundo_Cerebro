---
created: 2026-01-26T08:54
updated: 2026-01-26T12:04
---
# 📛 PADRÃO DE NOMENCLATURA

**Sistema de Nomeação de Arquivos - Segundo Cérebro**

**Criado:** 17/Jan/2025
**Versão:** 1.0
**Propósito:** Manter consistência absoluta na nomenclatura de todos arquivos

---

## 🎯 PRINCÍPIO FUNDAMENTAL

> **"Nome de arquivo deve comunicar:**
> **1. TIPO do conteúdo**
> **2. CONTEXTO/Categoria**
> **3. ASSUNTO específico"**

---

## 📋 SISTEMA DE PREFIXOS

### Arquivos Especiais (MAIÚSCULAS)

| Prefixo | Uso | Exemplo |
|---------|-----|---------|
| `MOC_` | Map of Content (índice) | `MOC_Conhecimento.md` |
| `PLANO_` | Documento de planejamento | `PLANO_Implementacao_Fase1.md` |
| `CHECKPOINT_` | Snapshot de progresso | `CHECKPOINT_17JAN2025.md` |
| `TEMPLATE_` | Template reutilizável | `TEMPLATE_Projeto_Padrao.md` |
| `STATUS_` | Documento de status | `STATUS_Projeto_XYZ.md` |
| `ROADMAP_` | Planejamento de longo prazo | `ROADMAP_2025.md` |
| `GUIA_` | Guia/tutorial | `GUIA_Claude_Commands.md` |
| `README` | Visão geral de pasta/projeto | `README.md` |

**Regra:** Prefixos sempre em MAIÚSCULAS para destaque visual

---

## 🗂️ NOMENCLATURA POR TIPO

### 1. Arquivos de Conhecimento

**Formato:** `Categoria_Subcategoria_Topico.md`

**Exemplos:**

```
Conhecimento_IA_Prompt_Engineering.md
Conhecimento_Negocios_Marketing_Digital.md
Conhecimento_DevPessoal_Produtividade_TDAH.md
```

**Regras:**

- Underscores separam hierarquia
- Máximo 3 níveis (Categoria_Sub_Topico)
- Se nome ficar >60 caracteres, usar pasta em vez de underscore
- CamelCase para clareza: `Marketing_Digital` não `marketing_digital`

### 2. Arquivos de Projetos

**Formato:** `Projeto_Nome_Documento.md`

**Exemplos:**

```
Projeto_SecondBrain_Plano.md
Projeto_Website_Requisitos.md
Projeto_App_Arquitetura.md
```

**Localização:** Sempre dentro de `02_PROJETOS/Nome_Projeto/`

**Estrutura interna projeto:**

```
02_PROJETOS/Meu_Website/
├── README.md                      ← Visão geral
├── STATUS_ATUAL.md               ← Status (SEMPRE atualizado)
├── planejamento/
│   ├── PLANO_Principal.md
│   ├── ROADMAP_2025.md
│   └── PROXIMOS_PASSOS.md
├── checkpoints/
│   ├── CHECKPOINT_17JAN2025.md
│   └── CHECKPOINT_Lancamento.md
└── recursos/
    └── TEMPLATE_Landing_Page.md
```

### 3. Arquivos de Aprendizado

**Formato:** `Curso_Nome_Modulo_Aula.md`

**Exemplos:**

```
Curso_Claude_M01_Introducao.md
Curso_Obsidian_M02_L03_Wikilinks.md
Curso_Python_Basico_Variaveis.md
```

**Para notas de aula:**

```
Curso_[Nome]_Notas_[Data].md
Curso_Claude_Notas_17JAN2025.md
```

### 4. MOCs (Maps of Content)

**Formato:** `MOC_Nome_Area.md` ou `_MOC_Nome.md`

**Exemplos:**

```
MOC_SEGUNDO_CEREBRO_MASTER.md     ← MOC principal
_MOC_Conhecimento.md              ← MOC de categoria
_MOC_Projetos.md
MOC_Projeto_Website.md            ← MOC de projeto específico
```

**Regra underscore inicial:**

- `_MOC_` quando é índice de categoria (aparece primeiro na ordenação)
- `MOC_` quando é MOC específico de projeto/curso

### 5. Templates

**Formato:** `TEMPLATE_Tipo_Nome.md`

**Exemplos:**

```
TEMPLATE_Projeto_Padrao.md
TEMPLATE_Nota_Curso.md
TEMPLATE_Checkpoint.md
TEMPLATE_MOC.md
```

**Localização:** `04_RECURSOS/TEMPLATES/`

### 6. Prompts (IA)

**Formato:** `Prompt_IA_Funcao.md`

**Exemplos:**

```
Prompt_Claude_Revisor_Codigo.md
Prompt_Gemini_Summarizer.md
Prompt_ChatGPT_Tradutor.md
```

**Localização:** `04_RECURSOS/PROMPTS/[Nome_IA]/`

---

## 📅 FORMATO DE DATAS

### Padrão Obrigatório: `DDMMMYYYY`

**Correto:**

```
17JAN2025
05FEV2025
23DEZ2024
```

**Errado:**

```
❌ 17-01-2025
❌ 2025-01-17
❌ 17/01/2025
❌ Jan_17_2025
```

**Motivo:**

- Ordenação alfabética funciona corretamente
- Compacto (9 caracteres)
- Não ambíguo (sem confusão DD/MM vs MM/DD)
- Meses em português (consistência)

**Abreviações de meses:**

```
JAN FEV MAR ABR MAI JUN
JUL AGO SET OUT NOV DEZ
```

---

## 🔤 CONVENÇÕES DE TEXTO

### Capitalização

**MAIÚSCULAS:**

- Prefixos especiais: `MOC_`, `PLANO_`, `TEMPLATE_`
- Siglas: `IA`, `TDAH`, `KPI`, `ROI`
- Primeira letra de cada palavra em hierarquia

**CamelCase:**

```
✅ Marketing_Digital.md
✅ Desenvolvimento_Pessoal.md
✅ Segunda_Mente.md

❌ marketing_digital.md
❌ desenvolvimento pessoal.md
❌ segunda-mente.md
```

### Separadores

**Underscores `_` para:**

- Hierarquia: `Categoria_Subcategoria_Topico`
- Espaços em nomes: `Segundo_Cerebro` não `Segundo Cerebro`
- Separação de partes: `PLANO_Implementacao_Fase1`

**Hífens `-` para:**

- Versões: `v1-2-3`
- Ranges: `M01-M03`
- Sub-partes: `Aula-Parte-1`

**Espaços NUNCA:**

```
❌ Segundo Cerebro.md
❌ Plano de Implementacao.md

✅ Segundo_Cerebro.md
✅ Plano_Implementacao.md
```

### Caracteres Proibidos

**NUNCA usar:**

```text
/ \ : * ? " < > |
```

**Motivo:** Problemas em Windows e outros sistemas operacionais

### Nomes Reservados Windows (CRÍTICO)

**NUNCA usar estes nomes de arquivo:**

```text
nul, con, prn, aux
com1, com2, com3, com4, com5, com6, com7, com8, com9
lpt1, lpt2, lpt3, lpt4, lpt5, lpt6, lpt7, lpt8, lpt9
```

**Motivo:** São nomes de dispositivos do Windows. Causam:

- Conflitos de sincronização no OneDrive
- Erros no Git (impossível clonar/push)
- Arquivos impossíveis de deletar normalmente

**Se criou por engano, deletar via Git Bash:**

```bash
rm -f "caminho/para/nul"
```

---

## 📁 NOMENCLATURA DE PASTAS

### Estrutura Principal (Prefixos Numéricos)

```
00_SISTEMA/          ← Meta sistema (ordem primeiro)
01_CONHECIMENTO/     ← Base conhecimento
02_PROJETOS/         ← Projetos ativos
03_APRENDIZADO/      ← Cursos e estudos
04_RECURSOS/         ← Templates, ferramentas
05_PESSOAL/          ← Notas pessoais
```

**Motivo dos números:**

- Força ordenação específica
- Independente de alfabeto
- Estrutura fixa e previsível

### Subpastas (Sem Prefixo Numérico)

```
01_CONHECIMENTO/
├── Desenvolvimento_Pessoal/
├── Tecnologia/
├── Negocios/
└── Saude/

02_PROJETOS/
├── Segundo_Cerebro/
├── Website_Portfolio/
└── App_Produtividade/
```

**Regra:** Números só no nível superior (01-05)

### Pastas Especiais

| Nome | Uso | Localização |
|------|-----|-------------|
| `.claude/` | Config Claude Code | Raiz |
| `.gemini/` | Config Gemini CLI | Raiz |
| `.obsidian/` | Config Obsidian | Raiz |
| `MOCs/` | Maps of Content | `00_SISTEMA/` |
| `PADROES/` | Documentação padrões | `00_SISTEMA/` |
| `TEMPLATES/` | Templates | `04_RECURSOS/` |
| `PROMPTS/` | Biblioteca prompts | `04_RECURSOS/` |

**Regra:** Pastas de config começam com `.` (hidden)

---

## 🎨 CASOS ESPECIAIS

### 1. Arquivos com Versões

**Formato:** `Nome_vX.Y.md`

**Exemplos:**

```
PLANO_Implementacao_v1.0.md
PLANO_Implementacao_v1.1.md
PLANO_Implementacao_v2.0.md
```

**Regra:** Sempre manter histórico (não sobrescrever)

### 2. Arquivos Temporários/Rascunhos

**Formato:** `_temp_Nome.md` ou `_draft_Nome.md`

**Exemplos:**

```
_temp_Ideias_Projeto.md
_draft_Artigo_IA.md
```

**Localização:** Pasta `_temp/` na raiz (limpar periodicamente)

**Regra:** Underscore inicial = temporário

### 3. Arquivos de Referência

**Formato:** `REF_Fonte_Topico.md`

**Exemplos:**

```
REF_Alan_Nicolas_Sistema_MOC.md
REF_Tiago_Forte_PARA.md
REF_Obsidian_Docs_Wikilinks.md
```

**Localização:** `04_RECURSOS/Referencas/`

### 4. Arquivos Multi-Categoria

**Problema:** Arquivo pertence a 2+ categorias

**Solução 1 - Localização primária + wikilinks:**

```
Arquivo principal: 01_CONHECIMENTO/IA/LLMs.md
Referenciado em: MOC_Projetos.md via [[LLMs]]
```

**Solução 2 - Tags no frontmatter:**

```markdown
---
tags: [IA, Projeto, Tecnologia]
categorias: [Conhecimento, Projetos]
---
```

**Nunca:** Duplicar arquivo em múltiplas pastas

---

## ✅ CHECKLIST DE VALIDAÇÃO

### Antes de Criar Arquivo

- [ ] Nome tem prefixo correto se aplicável?
- [ ] Categoria clara no nome?
- [ ] Sem espaços (usar underscores)?
- [ ] NUNCA usar nomes reservados do Windows (`nul`, `con`, `prn`, `aux`, `com1`-`com9`, `lpt1`-`lpt9`).
- [ ] Sem caracteres proibidos (/ \ : * etc)?
- [ ] Se tem data, está em DDMMMYYYY?
- [ ] Nome <60 caracteres?
- [ ] CamelCase aplicado?
- [ ] Extensão `.md` (não `.md.md`)?

### Depois de Criar Arquivo

- [ ] Arquivo está na pasta correta?
- [ ] Nome segue padrão da categoria?
- [ ] Atualizado MOC relevante?
- [ ] Se template, copiado para TEMPLATES/?
- [ ] Frontmatter completo (se usando)?

---

## 🚨 ERROS COMUNS E CORREÇÕES

### Erro 1: Espaços no Nome

```
❌ Plano de Implementacao.md
✅ PLANO_Implementacao.md
```

**Correção:**

```bash
# Renomear
mv "Plano de Implementacao.md" "PLANO_Implementacao.md"
```

### Erro 2: Data Errada

```
❌ CHECKPOINT_17-01-2025.md
❌ CHECKPOINT_2025-01-17.md
✅ CHECKPOINT_17JAN2025.md
```

### Erro 3: Dupla Extensão

```
❌ Documento.md.md
✅ Documento.md
```

**Causa:** Bug em scraper/automação

### Erro 4: Nome Muito Longo

```
❌ Conhecimento_Desenvolvimento_Pessoal_Produtividade_Pessoas_TDAH_Estrategias_Focalizacao.md (90 chars)

✅ Opção 1 (usar pasta):
   Conhecimento/DevPessoal/TDAH/Estrategias_Focalizacao.md

✅ Opção 2 (simplificar):
   Conhecimento_DevPessoal_TDAH_Foco.md (37 chars)
```

### Erro 5: Inconsistência de Capitalização

```
❌ Conhecimento_ia_prompt_engineering.md
❌ conhecimento_IA_Prompt_Engineering.md
✅ Conhecimento_IA_Prompt_Engineering.md
```

---

## 🔄 MIGRAÇÃO DE ARQUIVOS ANTIGOS

### Script de Renomeação em Massa

**Para executar via Claude Code:**

```bash
/system "Rename all files in [pasta] to follow NOMENCLATURA standards"
```

**Validações automáticas:**

1. Substituir espaços por underscores
2. Aplicar CamelCase
3. Corrigir datas para DDMMMYYYY
4. Remover caracteres inválidos
5. Adicionar prefixos onde faltam
6. Verificar extensão .md única

### Mapa de Conversão

**Padrão antigo → Padrão novo:**

```
plano implementacao.md → PLANO_Implementacao.md
checkpoint 17-01-25.md → CHECKPOINT_17JAN2025.md
template projeto.md → TEMPLATE_Projeto.md
moc conhecimento.md → _MOC_Conhecimento.md
segundo cerebro notas.md → Conhecimento_Sistema_Notas.md
```

---

## 📖 EXEMPLOS COMPLETOS

### Projeto Completo

```
02_PROJETOS/Website_Portfolio/
├── README.md
├── STATUS_ATUAL.md
├── planejamento/
│   ├── PLANO_Principal_v1.0.md
│   ├── ROADMAP_2025_Q1.md
│   └── PROXIMOS_PASSOS.md
├── checkpoints/
│   ├── CHECKPOINT_17JAN2025_Inicio.md
│   ├── CHECKPOINT_01FEV2025_Design.md
│   └── CHECKPOINT_15FEV2025_Lancamento.md
├── docs/
│   ├── GUIA_Setup.md
│   ├── Arquitetura_Sistema.md
│   └── REF_Next.js_Docs.md
└── recursos/
    ├── TEMPLATE_Blog_Post.md
    └── Wireframes/
```

### Base de Conhecimento

```
01_CONHECIMENTO/
├── _MOC_Conhecimento.md
├── Desenvolvimento_Pessoal/
│   ├── _MOC_DevPessoal.md
│   ├── TDAH_Estrategias_Foco.md
│   ├── Produtividade_GTD.md
│   └── Habitos_Atomic_Habits.md
├── Tecnologia/
│   ├── _MOC_Tech.md
│   ├── IA_LLMs_Fundamentals.md
│   ├── IA_Prompt_Engineering.md
│   └── Web_Next.js_Basics.md
└── README.md
```

### Recursos e Templates

```
04_RECURSOS/
├── _MOC_Recursos.md
├── TEMPLATES/
│   ├── TEMPLATE_Projeto_Padrao.md
│   ├── TEMPLATE_Checkpoint.md
│   ├── TEMPLATE_MOC.md
│   └── TEMPLATE_Nota_Curso.md
├── PROMPTS/
│   ├── Claude/
│   │   ├── Prompt_Claude_Code_Reviewer.md
│   │   └── Prompt_Claude_Planner.md
│   └── Gemini/
│       ├── Prompt_Gemini_Summarizer.md
│       └── Prompt_Gemini_Translator.md
└── README.md
```

---

## 🎯 RESUMO EXECUTIVO

### Regras de Ouro

1. **Prefixos MAIÚSCULOS** para arquivos especiais (`MOC_`, `PLANO_`, etc)
2. **CamelCase** para hierarquia (`Categoria_Subcategoria_Topico`)
3. **Underscores** para espaços (NUNCA espaços reais)
4. **Datas DDMMMYYYY** (17JAN2025)
5. **<60 caracteres** por nome
6. **Sem caracteres especiais** (/ \ : * ? " < > |)
7. **Uma extensão** (.md não .md.md)
8. **Localização correta** (pasta apropriada)

### Quick Reference

```
MOC → Map of Content → MOC_Nome.md ou _MOC_Nome.md
Plano → PLANO_Nome.md
Checkpoint → CHECKPOINT_17JAN2025.md
Template → TEMPLATE_Tipo.md
Status → STATUS_Nome.md
Conhecimento → Categoria_Sub_Topico.md
Projeto → Sempre em 02_PROJETOS/Nome/
```

---

**Criado:** 17/Jan/2025
**Versão:** 1.0
**Autor:** Claude Sonnet 4.5
**Status:** ✅ Ativo e obrigatório

**CONSISTÊNCIA É A CHAVE! 📛✅**
