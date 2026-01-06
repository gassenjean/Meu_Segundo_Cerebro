---
description: Limpar pastas duplicadas da raiz do vault
---

# Workflow: Limpeza de Raiz do Vault

Este workflow remove pastas duplicadas da raiz, mantendo apenas as 6 pastas numeradas (00-05) + arquivos essenciais.

## Quando usar

Quando você notar pastas extras na raiz do vault que não deveriam estar lá (ex: `Conhecimento/`, `Projetos/`, etc).

## Passos

### 1. Verificar o que está na raiz

```powershell
Get-ChildItem -Path "c:\Users\Gassen\OneDrive\Meu_Segundo_Cerebro" | Select-Object Name, PSIsContainer
```

### 2. Identificar pastas duplicadas

Apenas estas devem estar na raiz:

- `00_SISTEMA/`
- `01_CONHECIMENTO/`
- `02_PROJETOS/`
- `03_APRENDIZADO/`
- `04_RECURSOS/`
- `05_PESSOAL/`
- `.obsidian/`, `.git/`, `.claude/`, `.gemini/` (config)
- `README.md`, `CLAUDE.md`, `STATUS_VAULT.md`, `task.md`

Tudo mais = duplicado ou fora do lugar.

### 3. Mover conteúdo das duplicadas (se houver)

// turbo

```powershell
# Exemplo: Se houver pasta "Conhecimento/" duplicada
robocopy "c:\Users\Gassen\OneDrive\Meu_Segundo_Cerebro\Conhecimento" "c:\Users\Gassen\OneDrive\Meu_Segundo_Cerebro\01_CONHECIMENTO" /E /MOVE
```

### 4. Remover pastas vazias

// turbo

```powershell
Remove-Item -Path "c:\Users\Gassen\OneDrive\Meu_Segundo_Cerebro\Conhecimento" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "c:\Users\Gassen\OneDrive\Meu_Segundo_Cerebro\Projetos" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "c:\Users\Gassen\OneDrive\Meu_Segundo_Cerebro\Recursos" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path "c:\Users\Gassen\OneDrive\Meu_Segundo_Cerebro\Sistema" -Recurse -Force -ErrorAction SilentlyContinue
```

### 5. Verificar resultado

// turbo

```powershell
Get-ChildItem -Path "c:\Users\Gassen\OneDrive\Meu_Segundo_Cerebro" -Directory | Where-Object { $_.Name -notmatch '^(00|01|02|03|04|05|\.obsidian|\.git|\.claude|\.gemini|\.agent|\.github|\.smart-env|_inbox)' }
```

Se retornar vazio = ✅ Raiz limpa!

## Resultado Esperado

Apenas 6 pastas numeradas + arquivos essenciais + pastas de config.
