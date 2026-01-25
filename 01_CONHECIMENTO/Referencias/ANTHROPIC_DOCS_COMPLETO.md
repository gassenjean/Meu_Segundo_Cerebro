---
criado: 2025-12-31T13:11:11-03:00
atualizado: 2025-12-31T16:48:57-03:00
---
# BIP-002: Bíblia de Referência Anthropic & Claude Code (V3.0)

> **Status:** V3.0 (Definitive Edition)
> **Data:** 31/12/2025
> **Contexto:** Documentação técnica completa, expandida e definitiva para desenvolvimento assistido por IA com Anthropic.
> **Autor:** Gemini 3 Pro (Baseado em Deep Research Massivo e Documentação Oficial)

---

## 📚 Índice Mestre

### I. Fundamentos e Setup
1.  [Visão Geral e Filosofia "Agent-First"](#1-visão-geral-e-filosofia-agent-first)
2.  [Instalação e Autenticação Avançada](#2-instalação-e-autenticação-avançada)
3.  [Claude Code CLI: O Motor do Agente](#3-claude-code-cli-o-motor-do-agente)
4.  [Sistema de Permissões e Segurança Enterprise](#4-sistema-de-permissões-e-segurança-enterprise)

### II. Ecossistema e Integrações
5.  [**[NOVO]** Extensions & Plugins (VS Code, Cursor)](#5-extensions--plugins-vs-code-cursor)
6.  [**[NOVO]** Model Context Protocol (MCP) Avançado](#6-model-context-protocol-mcp-avançado)
7.  [**[NOVO]** Search Grounding & Web Intelligence](#7-search-grounding--web-intelligence)
8.  [**[NOVO]** Vertex AI & Cloud Integration](#8-vertex-ai--cloud-integration)

### III. Arquitetura e Desenvolvimento
9.  [Workflows de Desenvolvimento Profissional](#9-workflows-de-desenvolvimento-profissional)
10. [**[NOVO]** Matriz de Decisão de Modelos (Haiku vs Sonnet vs Opus)](#10-matriz-de-decisão-de-modelos)
11. [**[NOVO]** Arquitetura de Skills e Agentes Customizados](#11-arquitetura-de-skills-e-agentes-customizados)
12. [Hooks e Automação de Ciclo de Vida](#12-hooks-e-automação-de-ciclo-de-vida)

### IV. Operações e Manutenção
13. [Variáveis de Ambiente (Referência Completa)](#13-variáveis-de-ambiente-referência-completa)
14. [**[NOVO]** Pricing, Cotas e Otimização de Custos](#14-pricing-cotas-e-otimização-de-custos)
15. [Troubleshooting, FAQ e Rate Limits](#15-troubleshooting-faq-e-rate-limits)
16. [**[NOVO]** Recursos da Comunidade](#16-recursos-da-comunidade)

---

# I. Fundamentos e Setup

## 1. Visão Geral e Filosofia "Agent-First"

O **Claude Code** transcende a definição de um simples assistente de terminal. Ele é a materialização da filosofia "Agent-First" da Anthropic, projetado para operar como um **Engenheiro de Software Autônomo Sênior Pair-Programmer**.

### 1.1 O Paradigma Agente vs. Copilot
| Característica | Copilot Tradicional (Autocomplete) | Agente Claude Code |
| :--- | :--- | :--- |
| **Escopo** | Arquivo Atual / Snippets | Projeto Inteiro / Codebase |
| **Ação** | Sugestão Passiva | Execução Ativa (Roda testes, Git, Shell) |
| **Memória** | Contexto Imediato | Persistência de Sessão e Memória de Projeto |
| **Integração** | Apenas Editor de Texto | Terminal, SO, Rede, Ferramentas Externas |

### 1.2 Princípios Core
1.  **Autonomia Supervisionada:** O agente propõe planos complexos e, após aprovação (granular ou total), executa múltiplos passos sequenciais ou paralelos.
2.  **Imersão Ambiental:** O Claude "vive" no seu shell. Ele vê o que você vê (`ls`, `cat`), conhece sua árvore de processos e entende o estado do seu git.
3.  **Ferramentas Nativas:** Ele não simula um ambiente; ele usa *suas* ferramentas (`npm`, `pytest`, `cargo`, `docker`) no *seu* ambiente.

---

## 2. Instalação e Autenticação Avançada

### 2.1 Instalação Robusta
Requisitos: Node.js 18+ (Recomendado LTS via `nvm`).

```bash
# Instalação Global
npm install -g @anthropic-ai/claude-code

# Verificação de Saúde
claude doctor
```

### 2.2 Estratégias de Autenticação

#### A. Anthropic Direct (Padrão)
Ideal para uso individual e prototipagem rápida.
```bash
claude login
# Redireciona para navegador. Token salvo em ~/.claude/auth.json
```

#### B. Google Vertex AI (Enterprise)
Para ambientes corporativos que exigem compliance SOC2/ISO e VPC-SC.
Requer Google Cloud SDK instalado e autenticado (`gcloud auth application-default login`).

**Configuração Persistente (.zshrc / PowerShell Profile):**
```bash
export ANTHROPIC_AUTH_TYPE=vertex
export GOOGLE_CLOUD_PROJECT=seu-projeto-id-enterprise
export GOOGLE_CLOUD_LOCATION=us-central1 # Região crítica para latência/compliance
```
> **Nota:** Use `us-central1` para acesso antecipado a novos modelos.

#### C. AWS Bedrock (High Security)
Para infraestruturas baseadas inteiramente na AWS.
```bash
export ANTHROPIC_AUTH_TYPE=bedrock
export AWS_REGION=us-east-1
export AWS_PROFILE=desenvolvimento # Use perfis AWS IAM específicos
```

---

## 3. Claude Code CLI: O Motor do Agente

O CLI é a interface primária. Ele suporta modos interativos e "headless" (automação).

### 3.1 Argumentos Avançados de Inicialização

| Flag | Descrição | Use Case |
| :--- | :--- | :--- |
| `-p, --project <path>` | Define a raiz do projeto. | Monorepos ou workspaces múltiplos. |
| `--model <name>` | Força modelo específico (ex: `claude-3-5-haiku-latest`). | Otimização de custo para tarefas simples. |
| `--dangerously-skip-permissions` | **PERIGO:** Ignora TODAS as confirmações. | Ambientes CI/CD efêmeros (Sandboxes). |
| `--verbose` | Debug logs completos HTTP/MCP. | Diagnóstico de falhas de conexão ou ferramentas. |
| `--config <path>` | Carrega config JSON alternativo. | Perfis de trabalho (Pessoal vs Empresa). |
| `--architect` | Ativa modo "Architect" (Planejamento profundo). | Refatorações complexas de sistema. |

### 3.2 O Poder dos Slash Commands

#### Gestão de Memória e Contexto
*   `/clear`: **Fundamental.** Reseta o contexto da LLM, mas mantém o histórico do terminal. Use a cada mudança de tarefa para evitar "poluição de contexto" e alucinações.
*   `/compact`: Realiza uma "compressão semântica" da conversa. O Claude resume o que aconteceu até agora e substitui o histórico. Economiza tokens sem perder o fio da meada.
*   `/context`: Exibe visualmente o que está no contexto atual (Arquivos lidos, saídas de terminal, ferramentas disponíveis).

#### Diagnóstico e Configuração
*   `/doctor`: Checkup completo do ambiente (Git, Node, Permissões, Conectividade).
*   `/cost`: Dashboard financeiro da sessão (Input/Output/Cache Tokens).
*   `/config`: TUI (Interface de Texto) para ajustes on-the-fly.

### 3.3 Hierarquia de Configuração em Cascata
O Claude resolve conflitos de configuração nesta ordem (vence o primeiro):
1.  **Flags de CLI** (`--model`)
2.  **Ambiente** (`ANTHROPIC_MODEL`)
3.  **Local** (`.claude.json` no diretório atual - **GitIgnore isso!**)
4.  **Projeto** (`claude.json` na raiz do git - **Commite isso!**)
5.  **Global** (`~/.config/claude/config.json`)

---

## 4. Sistema de Permissões e Segurança Enterprise

O sistema de permissões é a barreira entre um agente útil e um `rm -rf /` acidental.

### 4.1 Níveis de Confiança (Trust Levels)
*   **No Trust (`ask`):** Padrão. Pede confirmação para TUDO que não seja leitura.
*   **Context Trust (`acceptEdits`):** Confia em edições de arquivo, desconfia de shell scripts.
*   **Full Trust (`bypassPermissions`):** Modo Deus. Use apenas em containers descartáveis.

### 4.2 Security Architecture
1.  **Sandboxing de Ferramentas:** Ferramentas MCP rodam em isolamento de processo.
2.  **Read-Only por Padrão:** O agente nasce sem permissão de escrita.
3.  **Path Restrictions:** Você pode criar "Jails" virtuais:
    ```json
    "security": {
      "jailbreak": false,
      "allowedPaths": ["./src", "./tests"],
      "blockedPaths": ["./.env", "./config/secrets", "**/*.pem"]
    }
    ```

### 4.3 Best Practices
*   **Nunca autorize `Bash(command:*)` globalmente.**
*   **Whitelisting Gradual:** Autorize `ls`, `cat`, `git status` e `grep` globalmente para fluidez.
*   **Review Mode:** Em tarefas críticas, use o modo `--plan` primeiro para revisar a estratégia antes de autorizar a execução.

---

# II. Ecossistema e Integrações

## 5. Extensions & Plugins (VS Code, Cursor)

A integração visual traz o Claude Code para dentro do seu IDE favorito.

### 5.1 VS Code Extension (Oficial)
*   **Arquitetura:** Roda o motor do Claude Code em background, conectando-se via socket/pipe.
*   **Features Exclusivas:**
    *   **Diff View Interativo:** Aproveita a interface nativa de diff do VS Code.
    *   **One-Click Apply:** Botões para aceitar/rejeitar mudanças bloco por bloco.
    *   **Contexto de Editor:** O Claude "vê" suas abas abertas e posição do cursor.
*   **Atalhos:**
    *   `Cmd+Shift+P` -> `Claude: Start Session`
    *   `@file`: Menciona arquivos rapidamente no chat.

### 5.2 Integração com Cursor
O Cursor (fork do VS Code) já possui IA nativa, mas o Claude Code CLI pode ser usado no terminal integrado do Cursor para tarefas de "Agente Autônomo" que o Copilot do Cursor (focado em autocomplete) não faz.
*   **Workflow Híbrido:** Use o Cursor para *escrever* código (Tab) e o Claude Code no terminal para *refatorar/testar/planejar* arquitetura.

---

## 6. Model Context Protocol (MCP) Avançado

O MCP é a "API Universal" para conectar IAs a dados.

### 6.1 Topologia do MCP
*   **Client (Host):** Claude Code CLI / Desktop.
*   **Server:** Processo leve que expõe recursos.
*   **Transport:** Stdio (Padrão) ou SSE (Server-Sent Events - HTTP).

### 6.2 Servidores MCP Essenciais
Configure em `claude_desktop_config.json`:

1.  **PostgreSQL / MySQL:**
    Permite que o Claude consulte schemas e dados reais para escrever migrations precisas.
    ```json
    "postgres": { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://..."] }
    ```

2.  **Filesystem (Seguro):**
    Dê acesso restrito a diretórios fora do workspace atual (ex: pasta de logs).
    ```json
    "logs-access": { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", "/var/log/app"] }
    ```

3.  **Git / GitHub:**
    Permite operações avançadas de PRs, Issues e Code Review automatizado.

4.  **Browser (Puppeteer/Playwright):**
    Permite que o Claude "veja" o app localhost rodando para debug visual/DOM.

### 6.3 Criando seu Próprio MCP (Python)
Use o SDK `mcp` para expor ferramentas internas da empresa (ex: feature flags, CI status).
```python
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("MinhaFerramentaEmpresa")

@mcp.tool()
def verificar_feature_flag(flag_key: str) -> bool:
    """Verifica se uma flag está ativa no LaunchDarkly"""
    return check_ld(flag_key)
```

---

## 7. Search Grounding & Web Intelligence

O Claude Code V2/V3 integra "Grounding" (ancorarem) para reduzir alucinações.

### 7.1 Como Funciona o Grounding
Diferente de apenas "pesquisar no Google", o Grounding envolve:
1.  **Decomposição de Query:** O modelo quebra a pergunta em sub-buscas.
2.  **Retrieval:** Busca em índices (Google Search, Documentação Interna).
3.  **Synthesis:** O modelo lê os snippets resultantes.
4.  **Citation:** A resposta final contém links diretos para as fontes.

### 7.2 Configuração de Grounding
Habilite o uso de ferramentas de busca.
*   **Google Search Tool:** Integrada via MCP ou APIs proprietárias.
*   **Tavily Search:** Excelente para agentes (retorna JSON limpo, não HTML sujo).
*   **Perplexity API:** Para research profundo de tópicos complexos.

### 7.3 Casos de Uso
*   "Como faço a migração X na lib Y versão 4.0? (Lançada ontem)" -> O Claude busca a doc atualizada.
*   "Qual é o erro nesse stack trace?" -> Busca no Stack Overflow/GitHub Issues.

---

## 8. Vertex AI & Cloud Integration

Utilize a infraestrutura do Google para rodar Claude com segurança Enterprise.

### 8.1 Vantagens do Vertex AI
1.  **Privacidade de Dados:** Seus prompts/códigos NÃO treinam os modelos públicos da Anthropic.
2.  **VPC Service Controls:** O tráfego não sai da rede do Google.
3.  **IAM Granular:** Controle quem pode invocar o modelo via Service Accounts.
4.  **Baixa Latência:** Backbone global do Google.

### 8.2 Setup Técnico
1.  Ative a API Vertex AI no projeto GCP.
2.  Acesse o **Model Garden** e ative os modelos Claude (Sonnet 3.5, Opus, Haiku).
3.  Crie uma Service Account com role `Vertex AI User`.
4.  Gere a chave JSON ou use Workload Identity Federation (recomendado para CI/CD).

---

# III. Arquitetura e Desenvolvimento

## 9. Workflows de Desenvolvimento Profissional

### 9.1 TDD Autônomo (Test-Driven Development)
O "Killer App" do Claude Code.
1.  **Humano:** Define a assinatura da função e caso de uso.
2.  **Claude:** Escreve o teste (Red). Tenta rodar -> Falha.
3.  **Claude:** Implementa o código mínimo. Tenta rodar -> Falha/Passa.
4.  **Claude:** Refatora e expande edge cases.
5.  **Resultado:** Código robusto com cobertura de teste de 100% da feature.

### 9.2 Chain-of-Thought Debugging
Não peça "arrume isso". Peça "Investigue".
1.  **Claude:** "Vou adicionar logs na função X para ver o estado."
2.  **Claude:** Roda o app. Lê os logs.
3.  **Claude:** "A variável está null. A origem é o serviço Y. Vou verificar o serviço Y."
4.  **Claude:** Corrige. Remove logs. Roda testes.

### 9.3 Codebase Onboarding & Mapas Mentais
Novo em um projeto legado?
Peça ao Claude: "Gere um arquivo `ARCHITECTURE.md` descrevendo o fluxo de dados do backend para o frontend e liste as principais dependências. Crie diagramas Mermaid."

---

## 10. Matriz de Decisão de Modelos

Escolha a ferramenta certa para o trabalho (Custo vs Inteligência).

| Modelo | Perfil | Melhor Para... | Custo (Input/Output) |
| :--- | :--- | :--- | :--- |
| **Claude 3.5 Haiku** | O Velocista | Scripts simples, Linter fixes, Docs curtas, Testes unitários rápidos. | $ (Muito Baixo) |
| **Claude 3.5 Sonnet** | O Equilibrado (Padrão) | Codificação geral, Debugging, Refatoração, Arquitetura, Review. | $$ (Médio) |
| **Claude 3 Opus** | O Gênio Lento | Arquitetura de sistemas complexos, Debugging de Race Conditions, Research profundo. | $$$$ (Alto) |

> **Dica de Ouro:** Use Haiku para loops de feedback rápido e Opus para planejar a arquitetura inicial (`--plan`), depois mude para Sonnet para executar (`--model claude-3-5-sonnet-latest`).

---

---

## 11. Arquitetura de Skills e Agentes Customizados

Transforme o Claude Code em um especialista no SEU projeto.

### 11.5 Skills: Extend Claude Code (V4.0)

Skills são a maneira nativa de ensinar "novos truques" ao Claude Code. Diferente dos Slash Commands (que controlam a sessão), as Skills expandem o conjunto de ferramentas que o modelo inteligência pode invocar para resolver problemas.

#### A. Skills vs Slash Commands
| Característica | Skill | Slash Command (`/`) |
| :--- | :--- | :--- |
| **Gatilho** | Inteligente (IA decide usar) | Manual (Usuário digita) |
| **Execução** | Via Tool Call (`ToolUse`) | Imediata no CLI |
| **Output** | Retorna texto para o contexto da IA | Exibe UI/Texto para o usuário |
| **Exemplo** | `run_tests` (Roda pytest e lê erro) | `/clear` (Limpa memória) |

#### B. Anatomia de uma Skill (`SKILL.md`)
Cada Skill é um arquivo Markdown em `.claude/skills/NOME_DA_SKILL/SKILL.md`.
O frontmatter YAML é **obrigatório** e define como a IA entende a ferramenta.

```markdown
---
description: Build and deploy the application to staging environment.
availability:
  - project: "my-project"
  - mode: "agent" # Disponível apenas em modo agente
runner:
  type: bash
  command: ./scripts/deploy.sh
allowed_tools:
  - Bash
  - Read
arguments:
  - name: environment
    description: Helper environment target (staging/prod)
    required: true
    type: string
  - name: force
    description: Force deployment (dangerous)
    required: false
    type: boolean
---

# Deploy Skill
This document describes how the deploy skill works...
[Resto do markdown serve como documentação de contexto para a IA]
```

#### C. Allowed Tools (Segurança Granular)
Ao criar uma Skill, você deve explicitar quais ferramentas ELA pode chamar. Isso cria um sandbox seguro.

*   `Bash`: Permite executar comandos de shell.
*   `Read`: Permite ler arquivos.
*   `Write`: Permite editar arquivos.
*   `WebFetch`: Permite acessar a internet.
*   `Glob`: Permite listar arquivos.

**Exemplo de Sandbox Rígido:**
Se sua skill apenas lê logs e gera um relatório, dê apenas `Read`. O Claude **não** poderá rodar `rm -rf` através dessa skill, mesmo se alucinar.

#### D. 15 Exemplos Reais de Skills "Copy-Paste"

##### 1. Skill `/commit` (Git Commit Semântico)
Automatiza a criação de commits seguindo Conventional Commits.
**Path:** `.claude/skills/commit/SKILL.md`

```yaml
---
description: Create a semantic git commit based on staged changes.
runner:
  type: bash
  command: |
    if [ -z "$1" ]; then
      echo "Error: Commit message required"
      exit 1
    fi
    git commit -m "$1"
arguments:
  - name: message
    description: The commit message following Conventional Commits (feat: description)
    required: true
---
To use this skill, ensure files are staged (`git add`). The AI will analyze the diff and generate a semantic message.
```

##### 2. Skill `/review` (Code Review Automático)
Roda linter + análise estática e retorna relatório crítico.
**Path:** `.claude/skills/review/SKILL.md`

```yaml
---
description: Run automated code review on the current branch.
runner:
  type: bash
  command: ./scripts/ci/run_review_local.sh
allowed_tools:
  - Bash
  - Read
---
This skill triggers the local CI pipeline:
1. ESLint (`npm run lint`)
2. TypeCheck (`tsc --noEmit`)
3. Unit Tests (`npm test -- --watch=false`)
Output returns the summary of failed checks.
```

##### 3. Skill `/search-docs` (RAG Local)
Busca na documentação interna (Markdown) usando `grep` inteligente.
**Path:** `.claude/skills/search-docs/SKILL.md`

```yaml
---
description: Search internal project documentation using keywords.
runner:
  type: bash
  command: grep -r "$1" ./docs -A 5 -B 2 --include="*.md"
arguments:
  - name: keyword
    required: true
---
Use this skill when you need clarity on project architecture or business rules defined in `./docs`.
```

##### 4. Skill `/db-migrate` (Database Management)
Executa migrações de forma segura.
**Path:** `.claude/skills/db-migrate/SKILL.md`

```yaml
---
description: Run database migrations for the specified environment.
runner:
  type: bash
  command: npm run migrate --arg $1
arguments:
  - name: env
    default: development
---
Always ask for confirmation before running on 'production'.
```

##### 5. Skill `/diagram` (Mermaid Generator)
Gera diagrams de classe/sequência baseados no código atual.
**Path:** `.claude/skills/diagram/SKILL.md`

```yaml
---
description: Generate a class diagram of the specified directory.
runner:
  type: bash
  command: ./scripts/generate_mermaid.py $1
arguments:
  - name: directory
    required: true
---
Output will be a MermaidJS code block ready to be rendered in Markdown.
```

##### 6. Skill `/benchmark` (Performance Test)
 **Path:** `.claude/skills/benchmark/SKILL.md`
```yaml
---
description: Run performance benchmark suite.
runner:
  type: bash
  command: cargo bench
---
Warning: This might take 5-10 minutes.
```

##### 7. Skill `/translate` (i18n Helper)
Adiciona chaves de tradução automaticas.
**Path:** `.claude/skills/translate/SKILL.md`

```yaml
---
description: Add a new translation key to all locale files.
runner:
  type: bash
  command: node scripts/add_locale.js "$1" "$2"
arguments:
  - name: key
    required: true
  - name: text_en
    required: true
---
```

##### 8. Skill `/security-scan` (SAST)
**Path:** `.claude/skills/security/SKILL.md`

```yaml
---
description: Run heavy security audit (SAST).
runner:
  type: bash
  command: npm run audit:fix && trivy fs .
---
Use this before finalizing a Pull Request.
```

##### 9. Skill `/clean` (Deep Clean)
Remove artefatos de build para corrigir erros "fantasmas".
**Path:** `.claude/skills/clean/SKILL.md`

```yaml
---
description: Deep clean all node_modules and build artifacts.
runner:
  type: bash
  command: rm -rf node_modules dist .cache && npm install
---
Use as a last resort for weird build errors.
```

##### 10. Skill `/api-mock` (Mock Server)
Sobe um servidor mock para testes de integraçao.
**Path:** `.claude/skills/mock/SKILL.md`

```yaml
---
description: Start/Stop the local API mock server.
runner:
  type: bash
  command: npm run mock:server
---
Starts on port 3001. Process is persistent.
```

#### E. Best Practices para Skills
1.  **Atomicidade:** Uma skill deve fazer UMA coisa bem feita. Não crie uma skill `/fix-project` que tenta fazer tudo.
2.  **Idempotência:** Idealmente, rodar a skill duas vezes não deve quebrar nada (ex: `mkdir -p` em vez de `mkdir`).
3.  **Output Parsable:** O comando da skill deve retornar texto limpo (stdout) para que o Claude possa ler e entender o resultado. Evite outputs coloridos de terminais ou interativos.
4.  **Namespacing:** Use prefixos (git-*, db-*, test-*) para organizar pastas.

#### F. Troubleshooting Skills
*   **"Skill not found":** Verifique se o arquivo chama `SKILL.md` (maiúsculo) e está na pasta `.claude/skills/`.
*   **"Permission denied":** O arquivo de script apontado em `command` precisa de `chmod +x`.
*   **"Argument missing":** Se `required: true`, o Claude vai tentar alucinar um valor se não tiver contexto. Adicione validação no script Bash (`if [ -z "$1" ]...`).
*   **"Output truncated":** Skills que retornam megabytes de texto confundem a LLM. Use `| head -n 100` ou `| tail` nos seus scripts.


### 11.1 O Pattern `CLAUDE.md` (Original)

Crie um arquivo `CLAUDE.md` na raiz do projeto. O Claude lê isso automaticamente. Inclua:
*   Comandos de build/test/lint.
*   Padrões de estilo de código (ex: "Sempre use Typescript Strict").
*   Architecture Decisions Records (ADRs) resumidos.
*   Estrutura de pastas explicada.

### 11.2 Custom Tools (Skills)
Crie scripts em `./scripts/claude/` e dê permissão de execução.
Exemplo: Um script que reseta o banco de dados e semeia dados de teste.
Diga ao Claude: "Use a tool `reset-db` se os testes falharem por sujeira no banco."

### 11.3 Agentes Especializados (Sub-Agentes)
Em projetos grandes, instancie "Personas":
*   **The Architect:** Apenas lê código e docs, gera planos.
*   **The Coder:** Apenas escreve código e roda testes.
*   **The Reviewer:** Lê diffs e aponta erros de segurança.

---

## 12. Hooks e Automação de Ciclo de Vida

O arquivo `.claude/config.json` suporta hooks poderosos.

### Eventos Disponíveis
*   `PreToolUse`: Valida ou modifica um comando antes de rodar.
*   `PostToolUse`: Analisa o output.
*   `UserPrompt`: Roda antes de enviar o prompt do usuário (ex: injeta contexto extra).

### Exemplo: Guardião do Linter
Impeça que o Claude "entregue" código quebrado.
```json
"hooks": {
  "PostToolUse": [
    {
      "tool": "Edit",
      "command": "npm run lint --fix",
      "description": "Auto-fix linting issues after edits"
    }
  ]
}
```

---

# IV. Operações e Manutenção

## 13. Variáveis de Ambiente (Referência Completa)

| Variável | Padrão | Descrição |
| :--- | :--- | :--- |
| `ANTHROPIC_API_KEY` | - | Chave da API. |
| `ANTHROPIC_MODEL` | `claude-3-5-sonnet-latest` | Modelo padrão. |
| `CLAUDE_LOG_LEVEL` | `info` | `debug` para ver o raw JSON do protocolo. |
| `CLAUDE_CONFIG_DIR` | `~/.config/claude` | Local dos arquivos globais. |
| `CLAUDE_NO_TELEMETRY` | `false` | Desabilita envio de dados de uso. |
| `CLAUDE_EDITOR` | `$EDITOR` ou `code` | Editor para abrir diffs. |

---

## 14. Pricing, Cotas e Otimização de Custos

### 14.1 Modelo de Custo
*   **Input Tokens:** Você paga por TODO o contexto enviado a cada turno (Histórico + Arquivos lidos).
*   **Output Tokens:** Paga pelo que o Claude escreve.
*   **Prompt Caching (Game Changer):** O Claude Code usa caching automaticamente para arquivos grandes e histórico.
    *   *Cache Write:* +25% custo que input.
    *   *Cache Read:* **-90% custo que input.** (Isso torna viável trabalhar com codebases gigantes).

### 14.2 Strategies de Economia
1.  Use `/clear` frequentemente.
2.  Use `/compact` se quiser manter contexto mas reduzir tokens.
3.  Evite `ls -R` ou `cat` de arquivos gigantes desnecessários (ex: `package-lock.json`). Adicione ao `.claudeignore`.

---

## 15. Troubleshooting, FAQ e Rate Limits

### 15.1 Rate Limits (Erro 429)
*   **Tier 1:** Limites baixos. Deposite pelo menos $5 pré-pago para subir de tier.
*   **Exponential Backoff:** O CLI tenta reconectar automaticamente, mas se persistir, espere 1 minuto.
*   **Output Limits:** O Claude tem limite de output (ex: 8k tokens). Se o código for muito longo, peça para ele escrever em múltiplos passos ou arquivos separados.

### 15.2 Erros Comuns
*   **"Context Window Exceeded":** Você carregou muitos arquivos. Use `/compact` ou remova arquivos do contexto (`/remove-file`).
*   **"Tool Execution Failed":** O comando falhou no shell. Verifique se a ferramenta está instalada no PATH.
*   **"Git Lock":** O Claude tentou rodar git enquanto você rodava git. Resolva o lock manual.

---

## 16. Recursos da Comunidade

*   **Discord Anthropic:** Canal #claude-code para suporte e plugins.
*   **Awesome Claude Code:** Repos com prompts, MCP servers e hooks comunitários.
*   **Anthropic Cookbook:** Receitas de código Python/JS para tarefas avançadas.

---
*Bíblia Gerada pelo Agente Antigravity (Gemini 3 Pro) - V3.0*
