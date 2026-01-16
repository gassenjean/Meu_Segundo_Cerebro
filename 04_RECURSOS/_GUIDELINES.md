---
criado: 2026-01-16T12:47:07-03:00
atualizado: 2026-01-16T12:47:07-03:00
---
# 🛠️ GUIDELINES: RECURSOS

**Diretrizes Específicas - Templates, Prompts e Ferramentas**

**Categoria:** 04_RECURSOS
**Versão:** 2.0 (Expandida)
**Criado:** 16/Jan/2026
**Atualizado:** 16/Jan/2026

---

## 🎯 O QUE PERTENCE AQUI

### Sim, Vai em RECURSOS

- ✅ Templates reutilizáveis (documentos, estruturas, padrões)
- ✅ Prompts de IA (Claude, Gemini, ChatGPT, Perplexity)
- ✅ Agentes de sistema (Névoa, Elena, Pedro, Alan, etc)
- ✅ Checklists de validação/revisão/manutenção
- ✅ Guias e metodologias step-by-step
- ✅ Workflows de automação (N8N, Zapier, etc)
- ✅ Scripts utilitários (Python, Bash, JavaScript)
- ✅ Assets compartilhados (ícones, logos, paletas de cores)
- ✅ Frameworks e sistemas (RPI, Sistema 5C, PARA, etc)
- ✅ Formulários e questionários padrão

### Não, Vai em Outro Lugar

- ❌ Templates específicos de projeto → `02_PROJETOS/[Projeto]/recursos/templates/`
- ❌ Conhecimento conceitual sobre ferramentas → `01_CONHECIMENTO/`
- ❌ Material de curso (slides, exercícios) → `03_APRENDIZADO/[Curso]/recursos/`
- ❌ Arquivos de configuração de projeto → `02_PROJETOS/[Projeto]/`
- ❌ Notas pessoais ou journaling → `05_PESSOAL/`
- ❌ Código fonte de projetos → `02_PROJETOS/[Projeto]/`

**Princípio:** Recursos = Ferramentas **reutilizáveis** em múltiplos contextos. Se usado em apenas 1 lugar → não é recurso, é parte daquele projeto/contexto.

---

## 📛 NOMENCLATURA ESPECÍFICA

### Templates

```
TEMPLATE_[Tipo]_[Nome].md

Regras:
- Prefixo TEMPLATE_ obrigatório (UPPERCASE)
- Tipo: Categoria do template (Projeto, Briefing, Reuniao, etc)
- Nome: Descritivo e específico
- CamelCase para Tipo e Nome

Exemplos corretos:
✅ TEMPLATE_Projeto_Padrao.md
✅ TEMPLATE_Briefing_Cliente.md
✅ TEMPLATE_Checkpoint.md
✅ TEMPLATE_Reuniao_Semanal.md
✅ TEMPLATE_Plano_Estrategico.md
✅ TEMPLATE_Status_Update.md
✅ TEMPLATE_RPI_Master_Plan.md
```

### Prompts

```
Prompt_[IA]_[Funcao].md OU PROMPT_[AGENTE]_[VERSAO].md

Regras:
- Prompt_ (CamelCase) para prompts genéricos de IA
- PROMPT_ (UPPERCASE) para agentes de sistema
- IA: Claude, Gemini, ChatGPT, Perplexity
- Função: O que o prompt faz
- Agente: Nome do agente (NEVOA, ELENA, etc)
- Versão: Número da versão (3.0, 2.5, etc)

Exemplos corretos:
✅ Prompt_Claude_Code_Reviewer.md
✅ Prompt_Gemini_Summarizer.md
✅ Prompt_ChatGPT_Content_Writer.md
✅ PROMPT_AGENTE_NEVOA_3.0.md
✅ PROMPT_AGENTE_ELENA_2.5.md
✅ PROMPT_AGENTE_ALAN_NICOLAS.md
```

### Checklists

```
CHECKLIST_[Funcao].md

Regras:
- Prefixo CHECKLIST_ obrigatório (UPPERCASE)
- Função: Para que serve a checklist
- CamelCase para função

Exemplos corretos:
✅ CHECKLIST_Revisao_Projeto.md
✅ CHECKLIST_Pre_Lancamento.md
✅ CHECKLIST_Criacao_Arquivo.md
✅ CHECKLIST_Publicacao_Conteudo.md
✅ CHECKLIST_Code_Review.md
```

### Guias

```
GUIA_[Topico].md

Exemplos:
✅ GUIA_Nomenclatura_Arquivos.md
✅ GUIA_Git_Workflow.md
✅ GUIA_RPI_Framework.md
```

### Workflows

```
WORKFLOW_[Nome]_[Ferramenta].json OU .md

Exemplos:
✅ WORKFLOW_Captura_Notas_N8N.json
✅ WORKFLOW_Backup_Vault_Zapier.json
✅ WORKFLOW_Deploy_Automatico.md
```

### Scripts

```
script_[funcao].[extensao]

Regras:
- Lowercase + underscores
- Extensão conforme linguagem (.py, .sh, .js)

Exemplos:
✅ backup_vault.sh
✅ organize_files.py
✅ convert_markdown.js
```

---

## 🗂️ ORGANIZAÇÃO POR SUBPASTA

### Estrutura Obrigatória

```
04_RECURSOS/
│
├── _MOC_Recursos.md             # MOC master (índice de todos os recursos)
│
├── TEMPLATES/                   # Templates reutilizáveis
│   ├── Projetos/
│   │   ├── TEMPLATE_Projeto_Padrao.md
│   │   ├── TEMPLATE_README.md
│   │   └── TEMPLATE_Status_Atual.md
│   ├── Documentacao/
│   │   ├── TEMPLATE_Briefing_Cliente.md
│   │   ├── TEMPLATE_Especificacao_Tecnica.md
│   │   └── TEMPLATE_Manual_Usuario.md
│   ├── Planejamento/
│   │   ├── TEMPLATE_Plano_Estrategico.md
│   │   ├── TEMPLATE_Roadmap.md
│   │   └── TEMPLATE_Sprint_Planning.md
│   └── Checkpoints/
│       ├── TEMPLATE_Checkpoint_Projeto.md
│       └── TEMPLATE_Checkpoint_Sessao.md
│
├── PROMPTS/                     # Prompts de IA organizados
│   ├── Claude/
│   │   ├── Prompt_Claude_Code_Reviewer.md
│   │   ├── Prompt_Claude_Refactor_Helper.md
│   │   └── Prompt_Claude_Documentation.md
│   ├── Gemini/
│   │   ├── Prompt_Gemini_Summarizer.md
│   │   ├── Prompt_Gemini_Translator.md
│   │   └── Prompt_Gemini_Research.md
│   ├── ChatGPT/
│   │   └── Prompt_ChatGPT_Content_Writer.md
│   └── Agentes_Sistema/
│       ├── PROMPT_AGENTE_NEVOA_3.0.md
│       ├── PROMPT_AGENTE_ELENA_2.5.md
│       ├── PROMPT_AGENTE_PEDRO_SOBRAL.md
│       ├── PROMPT_AGENTE_ALAN_NICOLAS.md
│       ├── PROMPT_AGENTE_LUCAS_AMOEDO.md
│       └── PROMPT_AGENTE_DR_GREEN.md
│
├── CHECKLISTS/                  # Checklists de validação
│   ├── CHECKLIST_Criacao_Arquivo.md
│   ├── CHECKLIST_Revisao_Projeto.md
│   ├── CHECKLIST_Pre_Lancamento.md
│   ├── CHECKLIST_Code_Review.md
│   └── CHECKLIST_Revisao_Semanal.md
│
├── GUIAS/                       # Guias e metodologias
│   ├── GUIA_RPI_Framework.md
│   ├── GUIA_Sistema_5C.md
│   ├── GUIA_PARA_Method.md
│   └── GUIA_Git_Workflow.md
│
├── WORKFLOWS/                   # Automações e processos
│   ├── N8N/
│   │   ├── WORKFLOW_Captura_Notas.json
│   │   └── WORKFLOW_Backup_Vault.json
│   ├── Zapier/
│   └── Make/
│
├── SCRIPTS/                     # Scripts utilitários
│   ├── Python/
│   │   ├── organize_files.py
│   │   └── backup_vault.py
│   ├── Bash/
│   │   └── sync_vault.sh
│   └── JavaScript/
│       └── convert_markdown.js
│
└── ASSETS/                      # Assets compartilhados
    ├── Logos/
    ├── Icons/
    └── Paletas_Cores/
```

---

## 📝 TEMPLATES COMPLETOS

### Template: TEMPLATE (meta-template)

**Como criar um template reutilizável:**

```markdown
# TEMPLATE - [Nome do Template]

**Tipo:** [Tipo do template: Projeto, Briefing, etc]
**Versão:** [X.X]
**Criado:** [DD/MMM/YYYY]
**Atualizado:** [DD/MMM/YYYY]
**Uso:** [Quando usar este template]

---

## 🎯 Objetivo

[Para que serve este template? Que problema resolve?]

---

## 📋 Como Usar

1. Copiar este arquivo
2. Renomear para [padrão específico]
3. Preencher seções marcadas com [PLACEHOLDER]
4. Remover/adicionar seções conforme necessário

---

## ⚠️ Variáveis para Substituir

Antes de usar, substituir:

- `[NOME_PROJETO]` → Nome real do projeto
- `[DATA]` → Data atual (DD/MMM/YYYY)
- `[AUTOR]` → Seu nome
- [Outras variáveis específicas]

---

## 📄 TEMPLATE COMEÇA AQUI

---

[Conteúdo do template com placeholders]

# [NOME_PROJETO]

**Criado:** [DATA]
**Autor:** [AUTOR]

[Seções do template...]

---

## 📄 TEMPLATE TERMINA AQUI

---

## 📊 Histórico de Versões

**v1.0** (DD/MMM/YYYY) - Versão inicial
**v1.1** (DD/MMM/YYYY) - [O que mudou]

---

## 🔗 Links Relacionados

- [[_MOC_Recursos.md]] - Voltar ao índice
- [Outros templates relacionados]

---

**Última atualização:** [DD/MMM/YYYY]
```

### Template: PROMPT (para documentar prompts)

```markdown
# PROMPT - [Nome do Prompt]

**IA:** [Claude, Gemini, ChatGPT, etc]
**Versão:** [X.X]
**Criado:** [DD/MMM/YYYY]
**Atualizado:** [DD/MMM/YYYY]

---

## 🎯 Função

[O que este prompt faz? Qual o resultado esperado?]

---

## 🔧 Quando Usar

**Use este prompt quando:**
- Situação 1
- Situação 2
- Situação 3

**Não use quando:**
- Situação A
- Situação B

---

## 📋 Variáveis Configuráveis

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `{CONTEXTO}` | Contexto do problema | "Projeto de e-commerce" |
| `{OBJETIVO}` | O que quer alcançar | "Melhorar conversão" |
| `{INPUT}` | Entrada específica | "Código Python" |

---

## 📄 PROMPT

```
[Texto do prompt aqui, com variáveis marcadas como {VARIAVEL}]

Você é um especialista em {CONTEXTO}.

Objetivo: {OBJETIVO}

Input:
{INPUT}

Tarefa:
1. [Passo 1]
2. [Passo 2]
3. [Passo 3]

Output esperado:
- [Formato esperado]
```

---

## 💡 Exemplo de Uso

**Input:**
```
CONTEXTO: Desenvolvimento web
OBJETIVO: Otimizar performance
INPUT: [código React lento]
```

**Output esperado:**
```
[Exemplo do resultado típico]
```

---

## ⚙️ Configurações Recomendadas

**Temperatura:** 0.7
**Max tokens:** 2000
**Top-p:** 0.9
**Outras:** [Configurações específicas]

---

## 📊 Histórico de Versões

**v1.0** (DD/MMM/YYYY) - Versão inicial
**v1.1** (DD/MMM/YYYY) - Melhorias no output

---

## 🔗 Links Relacionados

- [[_MOC_Recursos.md]]
- [[01_CONHECIMENTO/IA/Prompt_Engineering.md]]

---

**Última atualização:** [DD/MMM/YYYY]
```

### Template: CHECKLIST

```markdown
# CHECKLIST - [Nome da Checklist]

**Função:** [Para que serve esta checklist]
**Frequência:** [Diária, Semanal, Por demanda, etc]
**Tempo estimado:** [X minutos]
**Criado:** [DD/MMM/YYYY]
**Atualizado:** [DD/MMM/YYYY]

---

## 🎯 Quando Usar

Use esta checklist:
- [Situação 1]
- [Situação 2]
- [Situação 3]

---

## ✅ CHECKLIST

### Fase 1: [Nome da Fase]

- [ ] Item 1
- [ ] Item 2
- [ ] Item 3

### Fase 2: [Nome da Fase]

- [ ] Item 4
- [ ] Item 5
- [ ] Item 6

### Fase 3: [Nome da Fase]

- [ ] Item 7
- [ ] Item 8
- [ ] Item 9

---

## ⚠️ Itens Críticos (Não Pular)

- [ ] 🔴 Item crítico 1
- [ ] 🔴 Item crítico 2
- [ ] 🔴 Item crítico 3

---

## 📊 Critério de Conclusão

**Considere completo quando:**
- Todos os itens críticos (🔴) estiverem marcados
- Pelo menos 80% dos itens normais estiverem feitos
- [Outros critérios específicos]

---

## 🔗 Links Relacionados

- [[_MOC_Recursos.md]]
- [Documentos relacionados]

---

**Última atualização:** [DD/MMM/YYYY]
```

---

## 🔄 WORKFLOW DE CRIAÇÃO DE RECURSO

### Do Específico ao Reutilizável

```
1. CRIAR EM CONTEXTO ESPECÍFICO
   ↓
   Criar arquivo em projeto/curso específico
   Exemplo: 02_PROJETOS/KabaK/recursos/briefing_outlet.md

2. USAR MÚLTIPLAS VEZES
   ↓
   Usar o mesmo padrão 2-3 vezes em contextos diferentes
   Perceber: "Isso poderia ser um template!"

3. AVALIAR REUTILIZABILIDADE
   ↓
   Perguntar:
   - Este arquivo é útil em outros contextos? (Sim/Não)
   - Posso remover detalhes específicos e tornar genérico? (Sim/Não)
   - Outras pessoas/projetos usariam isso? (Sim/Não)

   Se 3x Sim → TRANSFORMAR EM RECURSO

4. GENERALIZAR
   ↓
   - Remover detalhes específicos do projeto
   - Substituir valores por {VARIAVEIS}
   - Adicionar seções de documentação
   - Criar instruções de uso

5. DOCUMENTAR
   ↓
   - Adicionar cabeçalho (Objetivo, Quando usar, Variáveis)
   - Criar exemplo de uso
   - Documentar versão inicial (v1.0)

6. MOVER PARA 04_RECURSOS/
   ↓
   Determinar subpasta correta:
   - Template? → TEMPLATES/[Categoria]/
   - Prompt? → PROMPTS/[IA]/
   - Checklist? → CHECKLISTS/
   - Guia? → GUIAS/
   - Script? → SCRIPTS/[Linguagem]/

7. INDEXAR
   ↓
   Atualizar _MOC_Recursos.md com novo recurso

8. LINKAR DE VOLTA
   ↓
   No arquivo original em 02_PROJETOS/, adicionar:
   "Baseado em [[04_RECURSOS/TEMPLATES/TEMPLATE_Nome.md]]"
```

### Checklist de Validação de Recurso

Antes de mover arquivo para 04_RECURSOS/:

- [ ] Usado em pelo menos 2 contextos diferentes?
- [ ] Detalhes específicos removidos/substituídos por variáveis?
- [ ] Documentação completa (objetivo, quando usar, como usar)?
- [ ] Exemplo de uso incluído?
- [ ] Nomenclatura segue padrões (TEMPLATE_, Prompt_, CHECKLIST_)?
- [ ] Subpasta correta identificada?
- [ ] _MOC_Recursos.md será atualizado?

---

## ⚠️ ANTI-PADRÕES (EVITAR)

### ❌ Erro 1: Recurso Específico de Projeto

```
❌ Errado:
04_RECURSOS/TEMPLATES/TEMPLATE_Briefing_KabaK_Outlet_Sansom.md

Problemas:
- Nome de projeto no nome do arquivo
- Não reutilizável em outros contextos
- Deveria ficar em 02_PROJETOS/KabaK/

✅ Correto:
04_RECURSOS/TEMPLATES/Documentacao/TEMPLATE_Briefing_Outlet.md

Ou melhor ainda:
04_RECURSOS/TEMPLATES/Documentacao/TEMPLATE_Briefing_Cliente.md
```

**Regra:** Se tem nome de projeto/pessoa específica → NÃO É RECURSO GERAL.

### ❌ Erro 2: Prompt Sem Documentação

```
❌ Errado:
# Prompt Revisor de Código

```
Revise este código e encontre bugs.
```

✅ Correto:
# PROMPT - Code Reviewer

**IA:** Claude
**Versão:** 1.0

## 🎯 Função
Revisar código e identificar bugs, vulnerabilidades e más práticas.

## 🔧 Quando Usar
- Antes de fazer commit
- Ao revisar PR
- Ao refatorar código legado

## 📋 Variáveis
- {LINGUAGEM}: Linguagem do código (Python, JS, etc)
- {CODIGO}: Código a ser revisado
- {FOCO}: Área de foco (performance, segurança, etc)

## 📄 PROMPT
```
Você é um especialista em {LINGUAGEM} com foco em {FOCO}.

Revise o código abaixo e identifique:
1. Bugs potenciais
2. Vulnerabilidades de segurança
3. Problemas de performance
4. Más práticas

Código:
{CODIGO}

[resto do prompt...]
```

## 💡 Exemplo de Uso
[Exemplo completo]
```

**Regra:** Prompt sem documentação = difícil reutilizar. Documentar é obrigatório.

### ❌ Erro 3: Template Sem Placeholders

```
❌ Errado:
# TEMPLATE - Briefing Cliente

Cliente: KabaK
Projeto: Outlet Sansom
Data: 16/Jan/2026

[Conteúdo específico do projeto KabaK]

✅ Correto:
# TEMPLATE - Briefing Cliente

Cliente: [NOME_CLIENTE]
Projeto: [NOME_PROJETO]
Data: [DATA]

[Conteúdo genérico com placeholders]

## Como Usar
1. Substituir [NOME_CLIENTE] pelo nome real
2. Substituir [NOME_PROJETO] pelo projeto
3. [etc]
```

**Regra:** Template com dados específicos = NÃO É TEMPLATE, é documento.

### ❌ Erro 4: Script Sem Comentários

```
❌ Errado:
# backup_vault.py

import os
import shutil
shutil.copytree('/vault', '/backup')

✅ Correto:
# backup_vault.py
"""
Backup automatizado do vault Obsidian.

Uso:
    python backup_vault.py --source /vault --dest /backup

Autor: Gassen
Versão: 1.0
Criado: 16/Jan/2026
"""

import os
import shutil

def backup_vault(source, destination):
    """
    Copia vault para destino de backup.

    Args:
        source (str): Caminho do vault original
        destination (str): Caminho do backup
    """
    shutil.copytree(source, destination)

# [resto do código com comentários]
```

**Regra:** Script sem documentação = ninguém vai reusar (nem você daqui 3 meses).

### ❌ Erro 5: Versão Única de Recurso

```
❌ Errado:
Criar TEMPLATE_Briefing_v1.md, TEMPLATE_Briefing_v2.md, etc
(múltiplos arquivos)

✅ Correto:
TEMPLATE_Briefing_Cliente.md (um arquivo)

Com seção de histórico de versões:
## 📊 Histórico de Versões
**v2.0** (16/Jan/2026) - Adicionado seção de métricas
**v1.1** (10/Jan/2026) - Melhorado layout
**v1.0** (05/Jan/2026) - Versão inicial
```

**Regra:** Versionamento vai DENTRO do arquivo, não no nome do arquivo.

### ❌ Erro 6: Recursos Órfãos (Sem Índice)

```
❌ Errado:
Criar recurso novo, não adicionar ao _MOC_Recursos.md
Resultado: Ninguém descobre que existe

✅ Correto:
1. Criar recurso
2. ATUALIZAR _MOC_Recursos.md imediatamente
3. Adicionar link e descrição curta
```

**Regra:** Recurso não indexado = recurso perdido.

---

## 📊 ESTRATÉGIAS DE ORGANIZAÇÃO

### 1. Organização por Tipo (Atual)

**Estrutura recomendada:**

```
04_RECURSOS/
├── TEMPLATES/
├── PROMPTS/
├── CHECKLISTS/
├── GUIAS/
├── WORKFLOWS/
├── SCRIPTS/
└── ASSETS/
```

**Vantagens:**
- Fácil encontrar todos os templates
- Clara separação de tipos
- Escalável

### 2. Subpastas por Categoria

**Para pastas grandes (ex: TEMPLATES/):**

```
TEMPLATES/
├── Projetos/
├── Documentacao/
├── Planejamento/
├── Checkpoints/
└── Comunicacao/
```

### 3. Organização de Prompts por IA

**Prompts por ferramenta:**

```
PROMPTS/
├── Claude/           ← Prompts específicos para Claude
├── Gemini/           ← Prompts específicos para Gemini
├── ChatGPT/          ← Prompts específicos para ChatGPT
└── Agentes_Sistema/  ← Agentes customizados (Névoa, Elena, etc)
```

**Por quê?**
- Cada IA tem características específicas
- Facilita encontrar prompt para IA que está usando
- Permite otimização específica por modelo

### 4. Versionamento Inline (Não em Nome)

**✅ Certo:**
```
TEMPLATE_Briefing_Cliente.md

Dentro do arquivo:
## 📊 Histórico de Versões
v2.0, v1.1, v1.0
```

**❌ Errado:**
```
TEMPLATE_Briefing_Cliente_v1.md
TEMPLATE_Briefing_Cliente_v2.md
TEMPLATE_Briefing_Cliente_v3.md
```

---

## ✅ CHECKLIST DE MANUTENÇÃO

### Mensal (30 min)

- [ ] Revisar _MOC_Recursos.md (está atualizado?)
- [ ] Verificar recursos duplicados
- [ ] Identificar recursos nunca usados (candidatos a remoção)
- [ ] Atualizar versões de prompts/templates se melhorou

### Trimestral (1-2h)

- [ ] Revisar TODOS os recursos em uso
- [ ] Validar se ainda são relevantes
- [ ] Consolidar templates similares
- [ ] Atualizar documentação desatualizada
- [ ] Testar scripts (ainda funcionam?)
- [ ] Criar recursos novos baseados em padrões repetidos

### Anual (3h)

- [ ] Auditoria completa de recursos
- [ ] Arquivar recursos obsoletos
- [ ] Reorganizar estrutura se necessário
- [ ] Atualizar todos os exemplos de uso
- [ ] Validar compatibilidade de scripts com novas versões

---

## 🔗 LINKS RELACIONADOS

- [[00_SISTEMA/PADROES/NOMENCLATURA.md]] - Padrões gerais de nomenclatura
- [[_MOC_Recursos.md]] - MOC master desta categoria
- [[00_SISTEMA/PROTOCOLOS/PROTOCOLO_CRIACAO_ARQUIVOS.md]] - Protocolo geral
- [[01_CONHECIMENTO/]] - Conhecimento sobre ferramentas e metodologias
- [[02_PROJETOS/]] - Onde recursos são aplicados

---

**Versão:** 2.0 (Expandida)
**Criado:** 16/Jan/2026
**Atualizado:** 16/Jan/2026

**RECURSOS PRONTOS = RETRABALHO ZERO! 🛠️**
