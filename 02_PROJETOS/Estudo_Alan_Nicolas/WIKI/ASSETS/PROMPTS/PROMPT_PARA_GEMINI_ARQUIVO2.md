# PROMPT PARA GEMINI - PROCESSAR ARQUIVO 2 (ANTIGRAVITY)

**Use este prompt no Antigravity com Gemini 3 Pro**

---

## 📋 INSTRUÇÕES PARA VOCÊ (USUÁRIO)

1. Abra o Antigravity
2. Crie novo agent ou use o deep-research-alan
3. Cole o PDF "How_to_Use_AntiGravity_Better_than_99\_\_of_People.pdf"
4. Cole o prompt abaixo
5. Aguarde processamento (~10 minutos)
6. Copie o output completo
7. Cole na próxima mensagem aqui no Claude Code

---

## 🤖 PROMPT PARA COLAR NO GEMINI:

````markdown
# MISSÃO: EXTRAIR E ESTRUTURAR CONHECIMENTO SOBRE ANTIGRAVITY

Você acabou de receber um tutorial completo de 9 páginas sobre como usar Antigravity (Google's AI Code Editor) no nível profissional.

## SEU OBJETIVO:

Processar TODO o conteúdo e criar um **RASCUNHO ESTRUTURADO** que será refinado pelo Claude Code depois.

## INSTRUÇÕES DETALHADAS:

### FASE 1: LEITURA COMPLETA (5 minutos)

1. Leia TODAS as 9 páginas com atenção
2. Identifique a estrutura principal do tutorial
3. Localize o Framework FLOW (4 passos)
4. Identifique conceitos-chave que se repetem

### FASE 2: EXTRAÇÃO ESTRUTURADA (10 minutos)

Extraia e organize o conteúdo nas seguintes seções:

---

## SEÇÃO 1: FRAMEWORK FLOW (PRINCIPAL)

**Identifique os 4 passos do Framework:**

### F - FRAME (Definir Problema)

- O que é?
- Como fazer?
- Ferramentas usadas
- Exemplos

### L - LAYOUT (Design e Branding)

- O que é?
- Como fazer?
- Ferramentas usadas
- Exemplos

### O - ORCHESTRATION (Construção)

- O que é?
- Como fazer?
- Ferramentas usadas
- Sub-conceitos importantes

### W - WORLD (Deploy)

- O que é?
- Como fazer?
- Ferramentas usadas
- Integrações

---

## SEÇÃO 2: AGENT MANAGER

**Extraia TUDO sobre Agent Manager:**

- O que é?
- Como funciona?
- Múltiplos agentes em paralelo
- Inbox de gerenciamento
- Playground
- Casos de uso

---

## SEÇÃO 3: MCP SERVERS

**Extraia TUDO sobre MCP Servers:**

- O que é MCP?
- Como instalar MCP Servers?
- Lista de MCP Servers mencionados (Context 7, GitHub, N8N, Supabase, etc)
- Setup de tokens e credenciais
- Como adicionar MCP customizado (raw config)
- Integrações mencionadas

---

## SEÇÃO 4: PROJECT NOTES & CUSTOMIZATIONS

**Extraia:**

- O que são Project Notes?
- Rules vs Workflows
- Global vs Workspace
- Exemplos de uso

---

## SEÇÃO 5: ARTEFATOS & COMENTÁRIOS

**Extraia:**

- O que são Artefatos?
- Como adicionar comentários no código
- Back and forth iterativo
- Exemplos

---

## SEÇÃO 6: ESCOLHA DE MODELOS

**Extraia recomendações:**

- Quando usar Gemini 3 Pro
- Quando usar Claude Sonnet 4.5
- Quando usar Claude Opus 4.5
- Quando usar GPT
- Filosofia de uso

---

## SEÇÃO 7: DEPLOY WORKFLOW (GitHub + Vercel)

**Extraia workflow completo:**

- Integração GitHub
- Setup de tokens
- Deploy no Vercel
- Triangulação (Antigravity → GitHub → Vercel)

---

## SEÇÃO 8: BROWSER TESTING & AUTO-TESTING

**Extraia:**

- Como funciona browser automation
- Chrome integration
- Auto-correção
- Self-healing workflows

---

## SEÇÃO 9: EXTENSÕES & MARKETPLACE

**Extraia:**

- O que são extensões?
- Como instalar?
- Exemplos mencionados

---

## SEÇÃO 10: TÉCNICAS AVANÇADAS (MISC)

**Extraia qualquer outra técnica importante não coberta acima:**

- Dicas de produtividade
- Atalhos
- Boas práticas
- Anti-patterns

---

## FORMATO DO OUTPUT:

Para CADA seção acima, forneça:

```markdown
# SEÇÃO X: [NOME]

## Conceito Principal

[Explicação em 2-3 parágrafos]

## Como Usar (Passo a Passo)

1. Passo 1
2. Passo 2
3. ...

## Ferramentas/Comandos Mencionados

- Ferramenta 1: [descrição]
- Comando X: [descrição]

## Exemplos do Tutorial

[Copie exemplos relevantes do texto]

## Benefícios

- Benefício 1
- Benefício 2

## Quando Usar

[Contexto de aplicação]

---
```
````

## REQUISITOS CRÍTICOS:

1. ✅ **NÃO INVENTE NADA** - apenas extraia o que está no documento
2. ✅ **MANTENHA COMANDOS EXATOS** - copie sintaxe literal de comandos/código
3. ✅ **PRESERVE EXEMPLOS** - copie exemplos do tutorial sem modificar
4. ✅ **SEJA COMPLETO** - não pule seções
5. ✅ **ORGANIZE HIERARQUICAMENTE** - use headers (##, ###)
6. ✅ **IDENTIFIQUE PÁGINAS** - quando mencionar conceito, indique "Página X"

---

## OUTPUT ESPERADO:

Um documento estruturado de ~2000-3000 linhas contendo:

- Framework FLOW completo
- Agent Manager detalhado
- MCP Servers setup
- Todos os conceitos-chave organizados
- Exemplos preservados
- Comandos exatos
- Workflows documentados

---

## IMPORTANTE:

Este é um RASCUNHO que será refinado pelo Claude Code depois.
Foque em EXTRAIR e ESTRUTURAR - não precisa refinar a escrita.

**PRIORIDADE MÁXIMA:**

1. Completude (pegar TUDO)
2. Estrutura hierárquica clara
3. Preservar comandos/exemplos exatos
4. Indicar páginas de origem

Comece agora a extração!

```

---

## 📤 DEPOIS QUE O GEMINI TERMINAR:

1. ✅ Copie TODO o output do Gemini
2. ✅ Cole aqui no Claude Code
3. ✅ Eu vou refinar e criar os documentos finais
4. ✅ Total: ~15 minutos de trabalho do Gemini + 15 minutos de refinamento meu

---

**Pronto para usar!** 🚀

Cole este prompt no Antigravity e me avise quando o Gemini terminar.
```