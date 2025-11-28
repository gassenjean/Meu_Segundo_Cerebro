---
criado: 2025-11-18T10:03:29-03:00
atualizado: 2025-11-18T10:03:29-03:00
---
# 🤖 GUIA: Integração Gemini CLI

**Sistema Bi-IA - Claude Code + Gemini CLI**

**Criado:** 17/Jan/2025
**Versão:** 1.0
**Objetivo:** Economizar tokens usando Gemini para tarefas simples

---

## 🎯 POR QUE USAR GEMINI CLI

### Economia de Custos

| IA | Custo Relativo | Quando Usar |
|----|----------------|-------------|
| Claude | $$$ | Tarefas complexas, estratégicas |
| Gemini | $ | Tarefas simples, repetitivas |

**Meta:** 70% tarefas → Gemini | 30% tarefas → Claude

### Resultado Esperado

- **Economia:** >50% nos custos de IA
- **Velocidade:** Gemini responde mais rápido
- **Qualidade:** Claude para o que importa

---

## 📦 INSTALAÇÃO

### Pré-requisitos

- **Node.js v20+** (obrigatório)
- Conta Google (para autenticação gratuita) OU API Key

### Passo 1: Instalar Gemini CLI

```bash
# Instalar globalmente
npm install -g @google/gemini-cli

# OU executar sem instalar
npx @google/gemini-cli
```

### Passo 2: Primeira Execução (Autenticação)

```bash
# Executar pela primeira vez
gemini
```

Isso vai:
1. Abrir navegador para login com Google
2. Autorizar acesso
3. Pronto para usar!

### Passo 3: (Opcional) Usar API Key

Se preferir API Key em vez de login Google:

```bash
# Obter key em: https://aistudio.google.com/app/apikey

# Configurar como variável de ambiente
# Windows PowerShell:
$env:GEMINI_API_KEY="SUA_API_KEY_AQUI"

# Ou permanente no sistema
[System.Environment]::SetEnvironmentVariable('GEMINI_API_KEY','SUA_KEY','User')
```

### Passo 4: Testar

```bash
# Teste básico
gemini "Olá, responda em português: qual é 2+2?"
```

Se retornar resposta, está funcionando!

### Limites da Versão Gratuita

- **60 requests/minuto**
- **1.000 requests/dia**
- Modelo: Gemini 2.5 Pro (1M tokens de contexto)

---

## 🎮 COMANDOS BÁSICOS

### Prompt Simples

```bash
gemini "seu prompt aqui"
```

### Com Arquivo de Entrada

```bash
# Processar arquivo
gemini "summarize this text" < arquivo.txt

# Ou com cat
cat arquivo.md | gemini "extract key points"
```

### Salvando Output

```bash
# Salvar em arquivo
gemini "translate to english" < input.md > output.md
```

### Modelo Específico

```bash
# Usar modelo específico (flash é mais rápido/barato)
gemini --model gemini-1.5-flash "prompt"

# Pro é mais capaz
gemini --model gemini-1.5-pro "prompt"
```

---

## 📋 QUANDO USAR CADA IA

### Gemini CLI (Tarefas Simples)

✅ **USE para:**

| Tarefa | Exemplo |
|--------|---------|
| **Summarização** | Resumir artigo longo em bullet points |
| **Tradução** | Traduzir documento PT↔EN |
| **Extração** | Extrair datas, nomes, números de texto |
| **Formatação** | Converter texto em markdown estruturado |
| **Listas** | Gerar lista de ideias, tópicos |
| **Perguntas factuais** | "Qual a capital da França?" |
| **Reformulação** | Reescrever texto de forma diferente |
| **Correção** | Corrigir gramática/ortografia |

### Claude Code (Tarefas Complexas)

✅ **USE para:**

| Tarefa | Por quê |
|--------|---------|
| **Planejamento** | Precisa entender contexto do vault |
| **Código complexo** | Melhor raciocínio lógico |
| **Análise profunda** | Conexões não óbvias |
| **Decisões** | Precisa seu histórico/preferências |
| **Organização vault** | Conhece a estrutura |
| **Criação de conteúdo** | Qualidade superior |
| **Debug** | Melhor em encontrar problemas |

### Regra Prática

> **Se a tarefa pode ser feita sem conhecer seu vault/contexto → Gemini**
> **Se precisa conhecer seu sistema/preferências → Claude**

---

## 🔧 PROMPTS PRONTOS PARA GEMINI

### 1. Summarização

```bash
# Resumo em bullets
gemini "Summarize this text in 5 bullet points in Portuguese. Be concise." < texto.md

# Resumo executivo
gemini "Create an executive summary (max 100 words) in Portuguese" < documento.md
```

### 2. Tradução

```bash
# PT → EN
gemini "Translate to English. Maintain formatting and tone." < texto_pt.md > texto_en.md

# EN → PT
gemini "Translate to Brazilian Portuguese. Maintain technical terms." < texto_en.md > texto_pt.md
```

### 3. Extração de Dados

```bash
# Extrair entidades
gemini "Extract all names, dates, and numbers. Format as markdown table." < texto.md

# Extrair ações
gemini "Extract all action items and tasks. Format as checkbox list." < meeting_notes.md
```

### 4. Formatação

```bash
# Texto → Markdown
gemini "Convert to well-formatted markdown with headers, bullets, and emphasis." < rascunho.txt

# Estruturar conteúdo
gemini "Organize this content with clear sections and hierarchy." < notas.txt
```

### 5. Geração de Listas

```bash
# Brainstorm
gemini "Generate 10 ideas for [tema]. Be creative and specific."

# Tópicos
gemini "List 5 main topics covered in this text" < artigo.md
```

### 6. Correção

```bash
# Gramática
gemini "Fix grammar and spelling errors. Keep the original meaning." < texto.md

# Clareza
gemini "Rewrite for clarity and conciseness. Remove redundancy." < texto.md
```

### 7. Conversão

```bash
# JSON → Markdown
gemini "Convert this JSON to a readable markdown table" < data.json

# Markdown → Plain text
gemini "Convert to plain text, removing all markdown formatting" < doc.md
```

---

## 🔄 WORKFLOWS HÍBRIDOS

### Workflow 1: Processar Artigo Longo

```bash
# 1. Gemini: Resumir (barato)
gemini "Summarize in 10 bullet points" < artigo_longo.md > resumo.md

# 2. Claude: Analisar e conectar (contexto)
# No Claude Code:
/knowledge
"Analyze resumo.md and connect with existing knowledge in my vault"
```

**Economia:** Gemini processa 5000 palavras por centavos

### Workflow 2: Traduzir e Adaptar

```bash
# 1. Gemini: Traduzir (rápido)
gemini "Translate to Portuguese" < doc_en.md > doc_pt_raw.md

# 2. Claude: Adaptar ao contexto
# No Claude Code:
"Adapt doc_pt_raw.md to match my writing style and vault terminology"
```

### Workflow 3: Pesquisa → Conhecimento

```bash
# 1. Gemini: Extrair fatos
gemini "Extract all facts and data points as bullet list" < research.md > facts.md

# 2. Claude: Criar nota estruturada
# No Claude Code:
/knowledge
"Create knowledge note from facts.md following my templates"
```

### Workflow 4: Notas de Reunião

```bash
# 1. Gemini: Estruturar
gemini "Format as meeting notes with: attendees, topics, decisions, actions" < raw_notes.txt > structured.md

# 2. Claude: Criar tasks
# No Claude Code:
/work
"Extract action items from structured.md and add to project [X]"
```

---

## 📁 BIBLIOTECA DE PROMPTS

### Localização

Prompts prontos estão em:
```
04_RECURSOS/PROMPTS/Gemini/
```

### Estrutura de Prompt

```markdown
# Prompt: [Nome]

**Função:** [O que faz]
**Quando usar:** [Situações]

## Comando

```bash
gemini "[prompt]" < input.md
```

## Variáveis

- `[VAR]`: [O que colocar]

## Exemplo

[Exemplo prático]
```

---

## ⚙️ CONFIGURAÇÕES AVANÇADAS

### Modelos Disponíveis

| Modelo | Características | Uso |
|--------|-----------------|-----|
| `gemini-2.5-pro` | Padrão, 1M contexto | Maioria das tarefas |
| `gemini-2.5-flash` | Mais rápido | Tarefas simples |
| `gemini-1.5-pro` | Versão anterior | Backup |

### Selecionar Modelo

```bash
# Usar modelo específico
gemini --model gemini-2.5-flash "prompt"
```

### Temperatura

```bash
# Mais criativo
gemini --temperature 0.9 "generate creative ideas"

# Mais preciso
gemini --temperature 0.1 "extract exact data"
```

---

## 🚨 LIMITAÇÕES E CUIDADOS

### Gemini NÃO deve ser usado para:

❌ Tarefas que precisam conhecer seu vault
❌ Código complexo ou debugging
❌ Decisões que afetam sua organização
❌ Conteúdo que precisa do seu estilo pessoal
❌ Análises que precisam de contexto histórico

### Sempre validar output:

```bash
# Gemini faz
gemini "process this" < input.md > output.md

# Você/Claude valida
cat output.md
# ou
# No Claude Code: "Review output.md for accuracy"
```

### Rate Limits

- API gratuita tem limites
- Se receber erro 429, aguarde alguns minutos
- Para uso intenso, considere plano pago

---

## 📊 MÉTRICAS DE ECONOMIA

### Tracking Sugerido

Mantenha um log simples:

```markdown
# Log de Uso IA - [Mês]

## Tarefas Gemini
- [x] Summarização artigo X (economia: ~1000 tokens)
- [x] Tradução documento Y (economia: ~2000 tokens)

## Tarefas Claude
- [x] Planejamento projeto Z
- [x] Organização vault

## Totais
- Gemini: X tarefas
- Claude: Y tarefas
- Ratio: X:Y
- Economia estimada: $Z
```

### Meta

```
Mês 1: 50% Gemini / 50% Claude
Mês 2: 60% Gemini / 40% Claude
Mês 3+: 70% Gemini / 30% Claude
```

---

## 🎯 CHECKLIST DE SETUP

### Instalação
- [ ] Node.js instalado (v20+)
- [ ] Gemini CLI instalado (`npm install -g @google/gemini-cli`)
- [ ] Autenticação feita (login Google ou API Key)
- [ ] Teste básico funcionando (`gemini "teste"`)

### Configuração
- [ ] Modelo padrão definido (flash recomendado)
- [ ] Prompts básicos testados
- [ ] Workflow híbrido testado

### Integração
- [ ] Comando `/gemini` no Claude funcionando
- [ ] Biblioteca de prompts criada
- [ ] GEMINI.md configurado

---

## 🔗 LINKS

### Recursos
- [Google AI Studio](https://aistudio.google.com/)
- [Documentação Gemini API](https://ai.google.dev/docs)

### No Vault
- [[.gemini/GEMINI.md]] - Custom instructions
- [[04_RECURSOS/PROMPTS/Gemini/]] - Biblioteca de prompts
- [[.claude/commands/gemini.md]] - Comando de delegação

---

## 📝 EXEMPLOS PRÁTICOS

### Exemplo 1: Processar Aula de Curso

```bash
# Você tem transcrição de aula (5000 palavras)

# 1. Gemini resume
gemini "Summarize this lecture in 10 key points. Include any formulas or frameworks mentioned." < aula_raw.txt > aula_resumo.md

# 2. Claude estrutura como nota
# No Claude Code:
/learn
"Create course note from aula_resumo.md for [Curso] module [X]"
```

### Exemplo 2: Preparar Conteúdo para Projeto

```bash
# Você tem pesquisa em inglês

# 1. Gemini traduz e extrai
gemini "Translate to Portuguese and extract: main argument, supporting evidence, conclusions" < research_en.md > research_pt.md

# 2. Claude integra ao projeto
# No Claude Code:
/work
"Add research_pt.md insights to project [X] documentation"
```

### Exemplo 3: Organizar Ideias

```bash
# Você tem braindump bagunçado

# 1. Gemini estrutura
gemini "Organize these ideas into categories. Create clear hierarchy with headers." < braindump.txt > organized.md

# 2. Claude distribui
# No Claude Code:
/system
"Distribute content from organized.md to appropriate areas in vault"
```

---

**Criado:** 17/Jan/2025
**Versão:** 1.0

**ECONOMIZE TOKENS COM INTELIGÊNCIA! 🤖💰**
