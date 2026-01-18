---
name: validate
description: Valida arquivos individuais contra regras de Nomenclatura e Localização, e atualiza MOCs automaticamente.
triggers:
  - validar arquivo
  - validate file
  - check file
  - verificar regras
  - validar
version: 1.0.0
author: Antigravity (Gemini 3 Pro)
parameters:
  file_path:
    type: string
    description: Caminho ou nome do arquivo a validar. Se vazio, valida o último arquivo modificado.
    required: false
steps:
  - name: validate_file
    command: python scripts/validate.py "{file_path}"
    description: Valida o arquivo e atualiza MOC relevante
---
# Skill: Validate

Esta skill serve como o **Guardião do Sistema de Arquivos**.
Ela verifica se um arquivo específico obedece às regras estritas do Vault (`NOMENCLATURA.md`) e garante que ele esteja devidamente conectado à rede de conhecimento (MOCs).

## Funcionalidades

1. **Validação de Nome:** Verifica espaços, caracteres proibidos e prefixos obrigatórios.
2. **Validação de Local:** Verifica se está na pasta correta (não na raiz).
3. **Auto-Link (Smart MOC):** Procura o MOC mais próximo (mesma pasta) e adiciona o link `[[Arquivo]]` se estiver faltando.

## Uso

**Simples:**
> Validar arquivo `01_CONHECIMENTO/IA/Novo_Conceito.md`

**Automático (último arquivo):**
> Validar regras

## Output

Gera um relatório conciso no terminal indicando:

- ✅ Status (Válido/Inválido)
- ❌ Erros (se houver) e sugestões de correção
- 🔗 MOC Atualizado (se aplicável)
