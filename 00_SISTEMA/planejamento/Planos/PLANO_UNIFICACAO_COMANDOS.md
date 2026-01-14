---
criado: 2025-11-28T14:17:41-03:00
atualizado: 2025-11-28T14:17:41-03:00
---

# Plano de Unificação de Comandos (Claude ↔ Antigravity)

## Objetivo

Garantir que os comandos slash essenciais (ex: `/nevoa`, `/claude-architect`) funcionem identicamente tanto no Claude Code quanto no Antigravity (Gemini), criando uma experiência unificada para o usuário.

## Análise Atual

| Comando             | Claude (.claude) | Antigravity (.agent) | Ação Necessária     |
| ------------------- | ---------------- | -------------------- | ------------------- |
| `/nevoa`            | ✅ Presente      | ❌ Ausente           | Copiar para .agent  |
| `/claude-architect` | ✅ Presente      | ❌ Ausente           | Copiar para .agent  |
| `/marie-kondo`      | ✅ Presente      | ❌ Ausente           | Copiar para .agent  |
| `/sync`             | ✅ Presente      | ❌ Ausente           | Copiar para .agent  |
| `/gemini`           | ✅ Presente      | ❌ Ausente           | Adaptar para .agent |
| `/limpeza-raiz`     | ❌ Ausente       | ✅ Presente          | Copiar para .claude |
| `/atualizar-status` | ❌ Ausente       | ✅ Presente          | Copiar para .claude |

## Mudanças Propostas

### 1. Unificar Comandos Essenciais

Copiar os seguintes workflows de `.claude/commands/` para `.agent/workflows/`:

- `nevoa.md`
- `claude-architect.md`
- `marie-kondo.md`
- `sync.md`

### 2. Unificar Ferramentas Úteis

Copiar de `.agent/workflows/` para `.claude/commands/`:

- `limpeza-raiz-vault.md`
- `atualizar-status.md`

### 3. Atualizar Documentação

- Atualizar `00_SISTEMA/GUIA_RAPIDO_COMANDOS.md` para refletir a unificação.
- Criar `README.md` em `.agent/workflows/` explicando a paridade.

## Verificação

1. Listar diretórios finais para confirmar presença dos arquivos.
2. Verificar conteúdo de `GUIA_RAPIDO_COMANDOS.md`.
