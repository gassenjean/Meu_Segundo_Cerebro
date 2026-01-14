# AUTO-CHECKPOINT - Salva estado ao encerrar sessão Claude Code
# Executado automaticamente via hook PostSessionEnd

$ErrorActionPreference = "Stop"
$VaultRoot = "C:\Users\Gassen\OneDrive\Meu_Segundo_Cerebro"

# Data/hora atual
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$date = Get-Date -Format "ddMMMyyyy"

Write-Host "🔄 Auto-checkpoint iniciado..." -ForegroundColor Cyan

# 1. Atualizar SESSION_LOG.md
$sessionLog = Join-Path $VaultRoot "SESSION_LOG.md"

if (Test-Path $sessionLog) {
    $content = Get-Content $sessionLog -Raw

    # Atualizar seção "ÚLTIMA SESSÃO ENCERRADA"
    $updateBlock = @"

## 📍 ÚLTIMA SESSÃO ENCERRADA

**Data/Hora:** $timestamp
**Encerramento:** Automático (auto-checkpoint.ps1)
**Status:** ✅ Checkpoint salvo

*Sessão encerrada com sucesso. Contexto preservado para próxima sessão.*

"@

    # Se já existe seção, substitui. Se não, adiciona no topo
    if ($content -match "## 📍 ÚLTIMA SESSÃO ENCERRADA") {
        $content = $content -replace "(?s)## 📍 ÚLTIMA SESSÃO ENCERRADA.*?(?=##|\z)", $updateBlock
    } else {
        $content = $updateBlock + "`n`n" + $content
    }

    Set-Content -Path $sessionLog -Value $content -Encoding UTF8
    Write-Host "✅ SESSION_LOG.md atualizado" -ForegroundColor Green
}

# 2. Verificar git status e salvar snapshot
Set-Location $VaultRoot

$gitStatus = git status --porcelain
if ($gitStatus) {
    Write-Host "⚠️  Arquivos modificados detectados:" -ForegroundColor Yellow
    Write-Host $gitStatus

    # Opcional: Criar checkpoint git automático
    # Descomente se quiser commits automáticos:
    # git add .
    # git commit -m "Auto-checkpoint: $timestamp"
    # Write-Host "✅ Checkpoint git criado" -ForegroundColor Green
} else {
    Write-Host "✅ Nenhuma modificação detectada" -ForegroundColor Green
}

# 3. Salvar estado das tasks (se existir .claude/tasks.json ou similar)
# Placeholder para futuro

# 4. Criar checkpoint arquivo (backup leve)
$checkpointDir = Join-Path $VaultRoot "00_SISTEMA\CHECKPOINTS"
$checkpointFile = Join-Path $checkpointDir "AUTO_CHECKPOINT_$date.md"

$checkpointContent = @"
---
criado: $(Get-Date -Format "yyyy-MM-dd")
tipo: Auto-Checkpoint
sessao: Encerramento automático
---

# AUTO-CHECKPOINT - $timestamp

**Tipo:** Encerramento automático
**Script:** auto-checkpoint.ps1
**Status:** ✅ Salvo

## 📊 Estado do Vault

**Git status:**
``````
$gitStatus
``````

**Última modificação:** $timestamp

## 🔄 Próxima Sessão

Ao abrir próxima sessão:
- `auto-recovery.ps1` será executado
- SESSION_LOG.md será lido
- Contexto será recuperado

---

**Checkpoint salvo automaticamente. Continuidade garantida! 🎯**
"@

Set-Content -Path $checkpointFile -Value $checkpointContent -Encoding UTF8
Write-Host "✅ Checkpoint arquivo criado: $checkpointFile" -ForegroundColor Green

Write-Host ""
Write-Host "🎯 Auto-checkpoint completo!" -ForegroundColor Green
Write-Host "Sessão encerrada com segurança. Até a próxima! 👋" -ForegroundColor Cyan
