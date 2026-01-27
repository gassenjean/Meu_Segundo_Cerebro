---
created: 2026-01-26T11:56
updated: 2026-01-26T11:56
---
# PESQUISA: Claude Code Hooks

**Contexto:** Automação e Governança da Névoa (T036)
**Researcher:** Gemini Guardian
**Fonte:** Documentação Oficial Anthropic + Comunidade
**Data:** 26/Jan/2026

## 1. O que são Hooks no Claude Code?

Hooks são "gatilhos" automatizados que permitem interceptar o fluxo de trabalho do Claude Code para executar ações determinísticas ou avaliações de IA. Eles funcionam como o `.git/hooks`, mas para o agente.

Eles permitem **forçar comportamentos** sem depender apenas da "vontade" do modelo.

## 2. Tipos e Eventos Disponíveis

Os hooks são configurados no arquivo `config.json` (ou `.claude/config.json` no projeto).

### Principais Gatilhos (Events)

1. `PreToolUse`: Antes de usar uma ferramenta (ex: antes de editar um arquivo).
    * *Uso:* Bloquear edição em arquivos protegidos (`.env`, `MASTER_PLAN.md`).
2. `PostToolUse`: Depois que uma ferramenta rodou.
    * *Uso:* Rodar linter/formatador automaticamente após edição.
3. `UserPromptSubmit`: Assim que o usuário manda mensagem.
    * *Uso:* Injetar contexto obrigatório (ex: "Lembre-se das regras de TDAH").
4. `SessionStart`: Ao abrir o Claude.
    * *Uso:* Ler o `PEDIDOS_GASSEN_PENDENTES.md` (Isso resolveria nosso problema de esquecimento!).
5. `PermissionRequest`: Quando o Claude pede para rodar comando.
    * *Uso:* Auto-aprovar comandos seguros (ex: `ls`, `cat`) para agilizar.

### Tipos de Ação

* **Command:** Roda um script shell (Bash/Powershell).
* **Prompt:** Roda uma avaliação de IA (ex: "O usuário está irritado? Se sim, mude o tom").

## 3. Como Configurar

Estrutura básica no JSON de configuração:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "NoteEditor_WriteFile",
        "command": "python scripts/security_check.py"
      }
    ],
    "SessionStart": [
      {
        "type": "prompt",
        "prompt": "Leia o arquivo .bi-ia/PEDIDOS_GASSEN_PENDENTES.md e liste o que está pendente."
      }
    ]
  }
}
```

## 4. Exemplos Práticos para Névoa

### Caso A: O "Ralph" de Conformidade (Linting)

Sempre que o Claude editar um arquivo `.md`, rodar um script que verifica se o cabeçalho (frontmatter) está correto.

* **Event:** `PostToolUse` (EditFile)
* **Action:** `node scripts/verify_frontmatter.js`

### Caso B: Proteção contra Destruição

Impedir que o Claude delete arquivos críticos sem confirmação dupla.

* **Event:** `PreToolUse` (DeleteFile)
* **Action:** (Prompt) "Você tem CERTEZA que quer deletar isso? Verifique se tem backup."

### Caso C: Injeção de Contexto TDAH

* **Event:** `UserPromptSubmit`
* **Action:** (Prompt oculto) "Responda de forma concisa e direta. O usuário tem TDAH. Não faça preâmbulos."

## 5. Aplicação Imediata (Recomendação)

1. **Criar Hook de Inicialização:** Implementar um hook `SessionStart` que força a leitura do `PEDIDOS_GASSEN_PENDENTES.md`. Isso automatiza a regra "Névoa deve ler este arquivo".
2. **Criar Hook de Segurança:** Bloquear edições diretas no `NOMENCLATURA.md` ou `VAULT_CONSTITUTION.md` sem um passo extra de verificação.
