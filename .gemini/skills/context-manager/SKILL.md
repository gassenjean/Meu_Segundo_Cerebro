---
name: context-manager
description: Gerencia modos de foco e contexto de trabalho (Learn, Work, Knowledge, System).
---

# Context Manager (Focus Enforcer)

Esta skill ajuda a trocar de contexto rapidamente, carregando as informações mais relevantes para o modo de trabalho escolhido.

## Comandos

### `context-manager set <mode>`

Define o contexto atual e exibe informações relevantes.

**Argumentos:**

- `<mode>`: O modo de foco desejado.
  - `work`: Foco em PROJETOS (02_PROJETOS).
  - `learn`: Foco em APRENDIZADO (03_APRENDIZADO).
  - `knowledge`: Foco em CONHECIMENTO/ZETTELKASTEN (01_CONHECIMENTO).
  - `system`: Foco em MANUTENÇÃO DO SISTEMA (00_SISTEMA).

**Exemplo:**

```bash
context-manager set work
```

### `context-manager status`

Exibe o status atual do contexto (re-imprime o dashboard do modo atual).

## Funcionamento

1. Limpa a tela.
2. Exibe um banner ASCII do modo.
3. Lê o `STATUS_VAULT.md` para contexto global.
4. Lê o MOC principal da área selecionada para sugerir próximos passos.
5. Lista ferramentas recomendadas para o contexto.
