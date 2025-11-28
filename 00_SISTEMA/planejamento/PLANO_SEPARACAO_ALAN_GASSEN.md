---
criado: 2025-11-28
tipo: plano_reorganizacao
agente: Marie Kondo + Névoa
status: em_validacao
atualizado: 2025-11-28T11:15:14-03:00
---

# 🎯 PLANO REVISADO: SEPARAÇÃO ALAN vs GASSEN

**Problema Identificado:** O vault está misturando:
*   📚 **Conteúdo do Alan** (referência, metodologia, cursos dele)
*   👤 **Conteúdo do Gassen** (suas notas, seus projetos, seu conhecimento)

**Solução:** Criar separação clara mantendo a metodologia do Alan como guia.

---

## 🏗️ NOVA ESTRUTURA PROPOSTA

### Conceito: "Aprenda com o Alan, Aplique no Seu"

```
Meu_Segundo_Cerebro/
│
├── 01_CONHECIMENTO/              ← SEU conhecimento
│   ├── TDAH/                     ← Suas notas sobre TDAH
│   ├── Cultivo/                  ← Seu conhecimento de cultivo
│   ├── Marketing/                ← Suas notas de marketing
│   └── _Referencia_Alan/         ← 🆕 Material do Alan como referência
│       ├── Metodologia_5C/
│       ├── Sistema_MOCs/
│       └── Filosofia_Segunda_Mente/
│
├── 03_APRENDIZADO/               ← SEUS estudos + Cursos que você fez
│   ├── Formacao_Lendaria_2025/   ← Curso que VOCÊ fez (do Alan)
│   ├── Subido_Trafego/           ← Curso que VOCÊ fez (do Pedro)
│   ├── Mentes_Inquietas/         ← Livro que VOCÊ estudou
│   └── _Referencia_Cursos_Alan/  ← 🆕 Cursos originais do Alan (referência)
│       ├── Zona_Genialidade/
│       ├── Engenharia_Prompts/
│       └── Dominando_Obsidian/
│
├── 04_RECURSOS/                  ← SUAS ferramentas + Templates do Alan
│   ├── TEMPLATES/
│   │   ├── Seus/                 ← Templates que VOCÊ criou
│   │   └── Alan_Nicolas/         ← 🆕 Templates originais do Alan
│   ├── PROMPTS/
│   │   ├── Agentes_Sistema/      ← Seus agentes (Névoa, Elena, etc)
│   │   └── Alan_Biblioteca/      ← 🆕 Biblioteca de prompts do Alan
│   └── GUIAS/
│
└── 05_PESSOAL/                   ← 100% SEU
    ├── Familia/
    ├── Fe/
    └── Reflexoes/
```

---

## 🔄 MAPEAMENTO: O QUE VAI ONDE

### Material do Alan (Referência) → Mover para `_Referencia_*`

| Origem | Novo Destino | Motivo |
|--------|--------------|--------|
| `03_APRENDIZADO/Alan_Vault_Reference/` | `01_CONHECIMENTO/_Referencia_Alan/Vault_Original/` | É o segundo cérebro DELE, não o seu |
| `03_APRENDIZADO/Alan_Nicolas_Academia/` | `03_APRENDIZADO/_Referencia_Cursos_Alan/Academia/` | Curso original dele (referência) |
| `03_APRENDIZADO/Alan_Nicolas_Mentoria/` | `03_APRENDIZADO/_Referencia_Cursos_Alan/Mentoria/` | Curso original dele (referência) |
| `03_APRENDIZADO/Zona_Genialidade/` | `03_APRENDIZADO/_Referencia_Cursos_Alan/Zona_Genialidade/` | Curso original dele |
| `03_APRENDIZADO/Engenharia_Prompts/` | `03_APRENDIZADO/_Referencia_Cursos_Alan/Engenharia_Prompts/` | Curso original dele |
| `03_APRENDIZADO/Dominando_Obsidian/` | `03_APRENDIZADO/_Referencia_Cursos_Alan/Dominando_Obsidian/` | Curso original dele |

### Seus Estudos (Aplicação) → Manter em `03_APRENDIZADO`

| Arquivo | Destino | Motivo |
|---------|---------|--------|
| `03_APRENDIZADO/Formacao_Lendaria_2025/` | **MANTER** | Você FEZ esse curso (suas notas) |
| `03_APRENDIZADO/Subido_Trafego/` | **MANTER** | Você FEZ esse curso |
| `01_CONHECIMENTO/TDAH_Mentes_Inquietas/` | **MANTER** | Você ESTUDOU esse livro |
| `03_APRENDIZADO/DeFi_Journey/` | **MANTER** | Você FEZ esse curso |

---

## 💡 FILOSOFIA DA SEPARAÇÃO

### 📚 `_Referencia_*` = Biblioteca de Consulta
*   Conteúdo original do Alan (ou outros autores)
*   Você NÃO edita, apenas consulta
*   É como ter os livros dele na sua estante

### 👤 Pastas Normais = Seu Conhecimento Ativo
*   Suas notas, suas aplicações, seus insights
*   Você edita, expande, conecta
*   É o seu segundo cérebro de verdade

---

## 🎯 BENEFÍCIOS DESTA ABORDAGEM

1.  ✅ **Clareza:** Você sabe o que é seu e o que é referência
2.  ✅ **Respeito:** O trabalho do Alan fica preservado e citável
3.  ✅ **Aplicação:** Você usa a metodologia dele, mas no SEU contexto
4.  ✅ **Escalabilidade:** Pode adicionar referências de outros autores depois

---

## 📋 NOVO PLANO DE EXECUÇÃO

### Fase 1: Criar Estrutura de Referência (10min)
- [ ] Criar `01_CONHECIMENTO/_Referencia_Alan/`
- [ ] Criar `03_APRENDIZADO/_Referencia_Cursos_Alan/`
- [ ] Criar `04_RECURSOS/TEMPLATES/Alan_Nicolas/`

### Fase 2: Mover Material do Alan (20min)
- [ ] Mover 3 pastas do Alan para `_Referencia_Cursos_Alan/`
- [ ] Mover Alan_Vault_Reference para `_Referencia_Alan/`
- [ ] Mover cursos originais (Zona, Engenharia, Obsidian)

### Fase 3: Organizar SEU Conteúdo (15min)
- [ ] Mover arquivos soltos (do relatório anterior)
- [ ] Criar estrutura interna nos SEUS cursos
- [ ] Atualizar MOCs

### Fase 4: Validação (10min)
- [ ] Verificar links
- [ ] Atualizar `STATUS_VAULT.md`
- [ ] Criar checkpoint

**Tempo Total:** ~55 minutos

---

## 🗣️ NÉVOA COMENTA:

> "Agora sim faz sentido. O Alan é seu mentor, não seu clone. Você aprende com ele, mas constrói o SEU segundo cérebro. A metodologia é dele, mas o conteúdo é seu."

**Aprovação Necessária:** Gassen, você concorda com essa separação?
