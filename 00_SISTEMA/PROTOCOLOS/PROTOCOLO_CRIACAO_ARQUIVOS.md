---
criado: 2025-11-24T00:00:00-03:00
atualizado: 2025-11-24T21:43:47-03:00
---
# 🛡️ PROTOCOLO: CRIAÇÃO DE ARQUIVOS

**Protocolo Obrigatório para Claude Code**

**Status:** ✅ ATIVO E OBRIGATÓRIO
**Versão:** 1.0
**Criado:** 24/Nov/2025

---

## ⚠️ AVISO CRÍTICO

**ESTE PROTOCOLO É OBRIGATÓRIO.**

Claude Code **DEVE** seguir este checklist **ANTES** de criar qualquer arquivo no vault.

**ZERO EXCEÇÕES.**

---

## ✅ CHECKLIST OBRIGATÓRIO

### PASSO 1: Consultar Padrões (OBRIGATÓRIO)

Antes de criar QUALQUER arquivo, **SEMPRE** ler:

```markdown
1. [ ] Ler: 00_SISTEMA/PADROES/NOMENCLATURA.md
2. [ ] Identificar: Qual prefixo usar? (MOC_, TEMPLATE_, PLANO_, etc)
3. [ ] Verificar: Nome < 60 caracteres
4. [ ] Confirmar: Usa underscores, NÃO espaços
5. [ ] Validar: Segue padrão CamelCase se hierárquico
```

**Se não ler NOMENCLATURA.md primeiro = ERRO**

---

### PASSO 2: Identificar Localização (OBRIGATÓRIO)

Consultar MOC da categoria relevante:

```markdown
TIPO DE ARQUIVO → LOCALIZAÇÃO

Templates       → 04_RECURSOS/TEMPLATES/
Prompts         → 04_RECURSOS/PROMPTS/
Checklists      → 04_RECURSOS/CHECKLISTS/
MOCs categoria  → [Pasta categoria]/_MOC_Nome.md
MOCs sistema    → 00_SISTEMA/MOCs/
Padrões         → 00_SISTEMA/PADROES/
Protocolos      → 00_SISTEMA/
Notas de curso  → 03_APRENDIZADO/Nome_Curso/notas/
Recursos curso  → 03_APRENDIZADO/Nome_Curso/recursos/
```

**Consultar MOC relevante:**
- Criando em 01_CONHECIMENTO → Ler `_MOC_Conhecimento.md`
- Criando em 02_PROJETOS → Ler `00_SISTEMA/MOCs/_MOC_Projetos.md`
- Criando em 03_APRENDIZADO → Ler `_MOC_Aprendizado.md`
- Criando em 04_RECURSOS → Ler `_MOC_Recursos.md`
- Criando em 05_PESSOAL → Ler `_MOC_Pessoal.md`

---

### PASSO 3: Validar Estrutura (OBRIGATÓRIO)

Para cursos/projetos, verificar estrutura padrão:

**Curso (03_APRENDIZADO/):**
```
Nome_Curso/
├── README.md
├── notas/
└── recursos/
```

**Projeto (02_PROJETOS/):**
```
Nome_Projeto/
├── README.md
├── STATUS_ATUAL.md
├── planejamento/
├── checkpoints/
├── docs/
├── recursos/
├── tarefas/
└── metricas/
```

**Se estrutura não existe = Criar TODA a estrutura**

---

### PASSO 4: Confirmar com Usuário (SE NECESSÁRIO)

**Perguntar ao usuário SE:**
- Criando nova categoria/área
- Criando nova estrutura de curso/projeto
- Mudando localização de arquivos existentes
- Criando mais de 5 arquivos de uma vez

**Não precisa perguntar SE:**
- Arquivo único bem definido
- Localização óbvia pelos padrões
- Template simples

---

### PASSO 5: Executar e Documentar (OBRIGATÓRIO)

```markdown
1. [ ] Criar arquivo(s) na localização correta
2. [ ] Atualizar MOC relevante
3. [ ] Atualizar STATUS_VAULT.md se estrutural
4. [ ] Informar usuário sobre localização final
```

---

## 🚨 ERROS COMUNS A EVITAR

### ❌ NUNCA FAÇA ISSO

**Erro 1: Criar sem consultar padrões**
```
❌ Criar INDEX_Algo.md
✅ Ler NOMENCLATURA.md → Usar MOC_Algo.md
```

**Erro 2: Templates em lugar errado**
```
❌ criar template em notas/TEMPLATE_X.md
✅ Criar em 04_RECURSOS/TEMPLATES/TEMPLATE_X.md
```

**Erro 3: Múltiplos arquivos sem estrutura**
```
❌ Criar 5 arquivos soltos em notas/
✅ Criar subpasta organizada: notas/categoria/
```

**Erro 4: Espaços em nomes**
```
❌ Meu Arquivo.md
✅ Meu_Arquivo.md
```

**Erro 5: Prefixo errado**
```
❌ Index_Metodologia.md
✅ MOC_Metodologia.md
```

**Erro 6: Não atualizar MOC**
```
❌ Criar arquivo e esquecer de linkar no MOC
✅ Criar arquivo E atualizar MOC relevante
```

---

## 📋 WORKFLOW VISUAL

```
┌─────────────────────────────────────────┐
│ Usuário pede para criar arquivo(s)     │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ PAUSE - Ler NOMENCLATURA.md             │
│ Identificar: Prefixo, nome, padrão      │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ Identificar categoria (01-05)           │
│ Ler MOC relevante                       │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ Determinar localização exata            │
│ Verificar se estrutura existe           │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ SE nova estrutura → Confirmar com user  │
│ SE óbvio → Prosseguir                   │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ Criar arquivo(s)                        │
│ Atualizar MOC                           │
│ Atualizar STATUS_VAULT (se necessário)  │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│ Informar usuário: "Criado em [path]"   │
└─────────────────────────────────────────┘
```

---

## 🎯 EXEMPLOS PRÁTICOS

### Exemplo 1: Criar Template

**Request:** "Cria um template de briefing"

**Protocolo:**
1. ✅ Ler NOMENCLATURA.md → Prefixo: `TEMPLATE_`
2. ✅ Tipo: Template → Vai em `04_RECURSOS/TEMPLATES/`
3. ✅ Nome: `TEMPLATE_Briefing_Projeto.md`
4. ✅ Criar arquivo
5. ✅ Atualizar `_MOC_Recursos.md`
6. ✅ Informar: "Template criado em 04_RECURSOS/TEMPLATES/"

---

### Exemplo 2: Criar Notas de Live

**Request:** "Processar live do Gemini 3"

**Protocolo:**
1. ✅ Ler NOMENCLATURA.md → Padrão: `Categoria_Sub.md`
2. ✅ Categoria: Aprendizado → Ler `_MOC_Aprendizado.md`
3. ✅ Curso existe? → `Alan_Nicolas_Academia_Lendaria/`
4. ✅ Localização: `03_APRENDIZADO/Alan_Nicolas_Academia_Lendaria/notas/`
5. ✅ Nome: `Live_Gemini3_Antigravity_BananaPro_Warren_Buffett.md`
6. ✅ Criar arquivo em notas/
7. ✅ Atualizar README.md do curso
8. ✅ Atualizar `_MOC_Aprendizado.md`
9. ✅ Informar localização

---

### Exemplo 3: Criar Metodologia Completa

**Request:** "Criar sistema de metodologia profissional com IA"

**Protocolo:**
1. ✅ Ler NOMENCLATURA.md
2. ✅ Múltiplos arquivos → **CONFIRMAR COM USUÁRIO PRIMEIRO**
3. ✅ Usuário aprova
4. ✅ Identificar tipos:
   - MOC → `04_RECURSOS/` ou nova pasta
   - Templates → `04_RECURSOS/TEMPLATES/`
   - Checklists → `04_RECURSOS/CHECKLISTS/`
   - Guias → `04_RECURSOS/GUIAS/`
5. ✅ Criar estrutura completa
6. ✅ Atualizar `_MOC_Recursos.md`
7. ✅ Atualizar STATUS_VAULT.md
8. ✅ Informar estrutura criada

---

## 📊 MATRIZ DE DECISÃO

| Tipo de Arquivo | Prefixo | Localização | Atualizar MOC |
|-----------------|---------|-------------|---------------|
| Map of Content (categoria) | `_MOC_` | Na pasta da categoria | MOC Master |
| Map of Content (sistema) | `MOC_` | 00_SISTEMA/MOCs/ | MOC Master |
| Template | `TEMPLATE_` | 04_RECURSOS/TEMPLATES/ | _MOC_Recursos |
| Checklist | `CHECKLIST_` | 04_RECURSOS/CHECKLISTS/ | _MOC_Recursos |
| Protocolo | `PROTOCOLO_` | 00_SISTEMA/ | MOC Master |
| Plano | `PLANO_` | 00_SISTEMA/planejamento/ | MOC relevante |
| Status | `STATUS_` | Na raiz da pasta relevante | - |
| Checkpoint | `CHECKPOINT_` | checkpoints/ do projeto | MOC Projeto |
| Nota curso | `Categoria_Sub` | curso/notas/ | README curso |
| Recurso curso | Sem prefixo | curso/recursos/ | README curso |

---

## 🔍 COMANDO /validate

Para usar antes de criar:

```bash
# No Claude Code:
/validate "quero criar [descrição]"

# Exemplo:
/validate "quero criar templates de metodologia IA"

# Retorna:
# ✅ Tipo: Templates
# ✅ Localização: 04_RECURSOS/TEMPLATES/
# ✅ Prefixo: TEMPLATE_
# ✅ Atualizar: _MOC_Recursos.md
# ✅ Pode prosseguir
```

---

## ⚠️ EXCEÇÕES (RARAS)

**Única exceção permitida:**
- Arquivos temporários de teste (devem ser deletados após)
- Usar prefixo `TEMP_` e deletar em < 24h

**Qualquer outra exceção = ERRO**

---

## 🎯 RESPONSABILIDADES

### Claude Code DEVE:
- ✅ Seguir este protocolo SEMPRE
- ✅ Ler padrões antes de criar
- ✅ Validar localização
- ✅ Atualizar MOCs
- ✅ Informar usuário claramente

### Claude Code NÃO DEVE:
- ❌ Criar arquivos sem consultar padrões
- ❌ Inventar novos prefixos
- ❌ Colocar arquivos em lugares errados
- ❌ Esquecer de atualizar MOCs
- ❌ Usar espaços em nomes

---

## 📋 VALIDAÇÃO PÓS-CRIAÇÃO

Após criar arquivo(s), verificar:

```markdown
✅ CHECKLIST PÓS-CRIAÇÃO

1. [ ] Arquivo está na localização correta?
2. [ ] Nome segue padrão de NOMENCLATURA.md?
3. [ ] MOC relevante foi atualizado?
4. [ ] STATUS_VAULT.md atualizado (se estrutural)?
5. [ ] Usuário foi informado da localização?
6. [ ] Links/referências funcionam?
```

---

## 🚨 SE ALGO DEU ERRADO

**Se você (Claude) criou arquivo errado:**

1. **PAUSE** imediatamente
2. **ADMITA** o erro ao usuário
3. **EXPLIQUE** o que aconteceu
4. **CORRIJA** movendo/renomeando
5. **DOCUMENTE** no STATUS_VAULT.md (seção Correções)

**Exemplo:**
```
❌ "Criei INDEX_Metodologia.md em notas/ (ERRO)"
✅ "Deveria ser MOC_Metodologia_IA.md em 04_RECURSOS/"
🔧 "Corrigindo agora..."
✅ "Corrigido e documentado"
```

---

## 📚 REFERÊNCIAS OBRIGATÓRIAS

Documentos que Claude DEVE ter lido:

1. [[00_SISTEMA/PADROES/NOMENCLATURA.md]] - CRÍTICO
2. [[00_SISTEMA/PADROES/ESTRUTURA_PROJETOS.md]] - CRÍTICO
3. [[STATUS_VAULT.md]] - Estado atual do vault
4. MOC relevante da categoria - Conforme necessário

---

## ✅ CONFIRMAÇÃO

**Claude Code confirma:**

> "Eu, Claude Code, comprometo-me a seguir este protocolo em TODAS as criações de arquivos no vault Meu_Segundo_Cerebro. Consultarei NOMENCLATURA.md e MOCs relevantes ANTES de criar qualquer arquivo. ZERO exceções."

**Data:** 24/Nov/2025
**Versão:** 1.0
**Status:** ✅ ATIVO E OBRIGATÓRIO

---

## 📊 MÉTRICAS

**Meta de conformidade:** 100%

**Tracking:**
- Total de arquivos criados desde protocolo: 0
- Criados seguindo protocolo: 0
- Criados sem seguir (ERRO): 0
- Taxa de conformidade: N/A (protocolo novo)

**Atualizar mensalmente.**

---

**ESTE PROTOCOLO É LEI NO VAULT.**

**Criado:** 24/Nov/2025
**Versão:** 1.0
**Status:** 🟢 ATIVO
