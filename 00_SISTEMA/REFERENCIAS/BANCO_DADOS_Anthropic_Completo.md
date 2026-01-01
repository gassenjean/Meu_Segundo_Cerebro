# BANCO DE DADOS - Documentação Anthropic/Claude Completa

**Criado:** 30/12/2025
**Fonte:** Deep Research Gemini (docs.anthropic.com, code.claude.com, modelcontextprotocol.io)
**Contexto:** Referência Técnica Definitiva para Agentes e Desenvolvimento.

---

## 1. CLAUDE CODE CLI

A interface de linha de comando (CLI) é o principal ponto de entrada para o desenvolvimento assistido.

### 1.1 Configuração (`Settings.local.json`)
O arquivo `.claude/settings.local.json` (não commitado) é a autoridade máxima para configurações locais.

#### Chaves de Configuração Disponíveis
| Chave | Tipo | Default | Descrição |
| :--- | :--- | :--- | :--- |
| `co-authored-by` | boolean | `true` | Adiciona "Co-authored-by: Claude" nos commits git. |
| `permissions` | object | `{}` | Define regras de permissão granulares por ferramenta. |
| `hooks` | object | `{}` | Define comandos ou prompts disparados por eventos. |
| `disableAllHooks` | boolean | `false` | Desabilita execução de todos os hooks. |
| `allowManagedHooksOnly` | boolean | `false` | (Enterprise) Apenas hooks de marketplace centralizado. |
| `model` | string | `claude-3-7-sonnet-latest` | Sobrescreve o modelo padrão usado. |
| `otelHeadersHelper` | string | `null` | Script para headers OTEL dinâmicos. |
| `statusLine` | object | `{}` | Configuração da linha de status do terminal. |
| `fileSuggestion` | string | `null` | Script para customizar autocomplete de arquivos (`@`). |
| `outputStyle` | string | `null` | Ajusta system prompt para estilos de output específicos. |
| `forceLoginMethod` | string | `null` | Força login via `claudeai` ou `console`. |
| `forceLoginOrgUUID` | string | `null` | Especifica UUID da organização para login. |

### 1.2 Sistema de Permissões
Controla a autonomia do agente. Gerenciado na chave `permissions`.

#### Modos (`defaultMode`)
- `default`: Pergunta na primeira execução de cada ferramenta/comando.
- `acceptEdits`: Aceita edições de arquivo automaticamente (menos fricção).
- `plan`: Modo somente leitura (Plan Mode).
- `bypassPermissions`: Pula TODOS os prompts (Cuidado: permite execução de bash sem confirmação).

#### Exemplo de Schema de Permissões
```json
{
  "permissions": {
    "defaultMode": "default",
    "allow": ["Bash(command:ls)", "Read"],
    "ask": ["Bash", "Write"],
    "deny": ["WebFetch(domain:internal.com)"],
    "additionalDirectories": ["/path/to/other/dir"],
    "disableBypassPermissionsMode": false
  }
}
```

### 1.3 Environment Variables (Variáveis de Ambiente)
Essenciais para configuração em CI/CD ou overrides globais.

| Variável | Descrição |
| :--- | :--- |
| `ANTHROPIC_API_KEY` | **Obrigatória** para uso via API. |
| `CLAUDE_CODE_MODEL` | Sobrescreve o modelo padrão (ex: `claude-3-5-sonnet-latest`). |
| `CLAUDE_CODE_DISABLE_UPDATE_CHECK` | Defina `1` para desabilitar verificação de updates. |
| `CLAUDE_CODE_USE_BUILTIN_RIPGREP` | Defina `0` para usar o binário `rg` do sistema. |
| `CLAUDE_CODE_BASE_URL` | Sobrescreve a URL base da API. |
| `CLAUDE_CODE_REPL_COMMAND` | Comando customizado para iniciar o REPL. |
| `VERTEX_REGION_CLAUDE_3_5_SONNET` | Sobrescreve a região do Vertex AI para Sonnet. |
| `AWS_REGION` | Região para autenticação AWS Bedrock. |

### 1.4 Sistema de Hooks
Permite injeção de lógica customizada no ciclo de vida do agente.

#### Eventos Suportados
- `PreToolUse`: Antes de uma ferramenta ser usada.
- `PostToolUse`: Depois que uma ferramenta retorna.
- `Notification`: Quando o sistema emite notificação.
- `UserPromptSubmit`: Quando o usuário envia um input.
- `Stop`: Quando o Claude termina uma tarefa (útil para "Intelligent Stop").
- `PermissionRequest`: Quando uma aprovação é solicitada.

#### Exemplo Schema (Hooks)
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "type": "exec",
        "command": "npm test"
      }
    ],
    "UserPromptSubmit": [
      {
        "type": "prompt",
        "prompt": "Lembre-se de seguir o style guide do projeto.",
        "timeout": 30
      }
    ]
  }
}
```

#### Resposta de Hooks (Prompt)
Hooks do tipo `prompt` podem influenciar a decisão retornando JSON:
```json
{
  "result": "allow" | "deny" | "modify",
  "reason": "Explicação da decisão",
  "modifiedArguments": { ... }
}
```

### 1.5 Slash Commands (Comandos de Barra)
Disponíveis durente a sessão interativa (REPL).

| Comando | Descrição |
| :--- | :--- |
| `/add-dir <path>` | Adiciona diretório ao contexto. |
| `/bug` | Reporta bug. |
| `/clear` | Limpa histórico da conversa. |
| `/compact` | Compacta o contexto (economia de tokens). |
| `/config` | Menu interativo de configuração. |
| `/cost` | Mostra uso de tokens e custo. |
| `/doctor` | Roda diagnósticos. |
| `/init` | Inicializa configuração do projeto. |
| `/login` / `/logout` | Gestão de autenticação. |
| `/permissions` | Visualiza/Edita permissões atuais. |
| `/plugin` | Gerencia plugins. |
| `/resume [id]` | Retoma uma sessão anterior. |
| `/review` | Solicita code review. |
| `/sandbox` | Ativa ambiente bash isolado (sandbox). |
| `/stats` | Estatísticas da sessão. |
| `/status` | Status do sistema/modelo. |
| `/todos` | Lista TODOs locais. |

### 1.6 Flags de Linha de Comando
Argumentos passados ao iniciar o binário `claude`.

- `-p, --project <path>`: Inicia em diretório específico.
- `--model <name>`: Força modelo específico.
- `--plan`: Inicia em Plan Mode (somente leitura).
- `--yes` / `--bypass-permissions`: Auto-aprova tudo.
- `--print`: Modo não-interativo (single prompt).
- `--system-prompt-file <path>`: Carrega system prompt de arquivo.
- `--add-dir <path>`: Adiciona diretórios extras na inicialização.

---

## 2. MODEL CONTEXT PROTOCOL (MCP)

Protocolo padrão para conectar modelos de IA a fontes de dados e ferramentas.

### 2.1 Schemas JSON

#### Definição de Ferramenta (Tool)
```json
{
  "name": "calculate_sum",
  "description": "Add two numbers together",
  "inputSchema": {
    "type": "object",
    "properties": {
      "a": { "type": "number", "description": "First number" },
      "b": { "type": "number", "description": "Second number" }
    },
    "required": ["a", "b"]
  }
}
```

#### Definição de Recurso (Resource)
```json
{
  "uri": "file:///project/src/main.rs",
  "name": "Main Source File",
  "mimeType": "text/x-rust",
  "description": "The main entry point of the project"
}
```

### 2.2 Configuração (`claude_desktop_config.json`)
Arquivo de configuração para conectar servidores MCP (válido para Claude Desktop e adaptável).

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/Users/username/Desktop",
        "/active/workspace"
      ]
    }
  }
}
```

### 2.3 Servidores Principais (Core/Popular)
- **Filesystem**: Leitura/Escrita de arquivos segura.
- **Git**: Interação com repositórios.
- **Postgres**: Query e gestão de DB.
- **Slack**: Leitura de canais e mensagens.
- **Memory**: Estado persistente (Grafo de conhecimento).
- **Fetch**: Recuperação segura de conteúdo Web.

---

## 3. CLAUDE API & SDK

### 3.1 Definição de Tools (API Request)
Estrutura enviada no corpo da requisição para o Claude.

```json
{
  "name": "get_weather",
  "description": "Get the current weather in a given location",
  "input_schema": {
    "type": "object",
    "properties": {
      "location": {
        "type": "string",
        "description": "The city and state, e.g. San Francisco, CA"
      },
      "unit": {
        "type": "string",
        "enum": ["celsius", "fahrenheit"],
        "description": "The unit of temperature"
      }
    },
    "required": ["location"]
  }
}
```

### 3.2 System Prompt para Agentes
Exemplo de como instruir um agente a usar ferramentas.

**User-Defined System Prompt:**
```text
You are a helpful assistant with access to weather and filesystem tools. 
When asked about the weather, use the 'get_weather' tool. 
Always provide the response in a professional tone and ensure all file paths are absolute.
```

**Internal System Prompt (Gerado pela Anthropic):**
Inclui instruções de formatação de XML/JSON e definições de ferramentas injetadas automaticamente.
