# AUTO-RECOVERY - Recupera estado ao iniciar sessão Claude Code
# Executado automaticamente via hook PreSessionStart

$ErrorActionPreference = "Stop"
$VaultRoot = "C:\Users\Gassen\OneDrive\Meu_Segundo_Cerebro"

# Data/hora atual
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

Write-Host ""
Write-Host "🔄 Auto-recovery iniciado..." -ForegroundColor Cyan
Write-Host ""

# 1. Verificar e exibir SESSION_LOG.md
$sessionLog = Join-Path $VaultRoot "SESSION_LOG.md"

if (Test-Path $sessionLog) {
    Write-Host "📖 Lendo SESSION_LOG.md..." -ForegroundColor Yellow

    # Ler primeiras 50 linhas (resumo)
    $logContent = Get-Content $sessionLog -Head 50

    # Extrair seção "ÚLTIMA SESSÃO ENCERRADA"
    $lastSession = $logContent | Select-String -Pattern "ÚLTIMA SESSÃO ENCERRADA" -Context 0,5

    if ($lastSession) {
        Write-Host ""
        Write-Host "📍 ÚLTIMA SESSÃO:" -ForegroundColor Cyan
        Write-Host $lastSession -ForegroundColor Gray
        Write-Host ""
    }

    # Extrair "MENSAGEM PARA CLAUDE" se existir
    $messageForClaude = $logContent | Select-String -Pattern "MENSAGEM PARA CLAUDE" -Context 0,10

    if ($messageForClaude) {
        Write-Host "💬 MENSAGEM PENDENTE:" -ForegroundColor Yellow
        Write-Host $messageForClaude -ForegroundColor White
        Write-Host ""
    }
} else {
    Write-Host "⚠️  SESSION_LOG.md não encontrado" -ForegroundColor Yellow
}

# 2. Verificar git status
Set-Location $VaultRoot

Write-Host "📊 Git Status:" -ForegroundColor Cyan
$gitStatus = git status --short
if ($gitStatus) {
    Write-Host $gitStatus -ForegroundColor Yellow
} else {
    Write-Host "✅ Nenhuma modificação pendente" -ForegroundColor Green
}
Write-Host ""

# 3. Verificar último checkpoint automático
$checkpointDir = Join-Path $VaultRoot "00_SISTEMA\CHECKPOINTS"
$latestCheckpoint = Get-ChildItem $checkpointDir -Filter "AUTO_CHECKPOINT_*.md" |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1

if ($latestCheckpoint) {
    Write-Host "📌 Último checkpoint:" -ForegroundColor Cyan
    Write-Host "   $($latestCheckpoint.Name)" -ForegroundColor Gray
    Write-Host "   $(Get-Date $latestCheckpoint.LastWriteTime -Format 'dd/MM/yyyy HH:mm')" -ForegroundColor Gray
    Write-Host ""
}

# 4. Lembrete de comandos úteis
Write-Host "🎯 COMANDOS DISPONÍVEIS:" -ForegroundColor Green
Write-Host "   /mapa          - Carrega índice completo do vault" -ForegroundColor White
Write-Host "   /coach         - Ativa assistente pessoal TDAH" -ForegroundColor White
Write-Host "   /lucas         - Contexto DeFi (PRIORIDADE)" -ForegroundColor White
Write-Host "   /pedro         - Contexto Tráfego Pago" -ForegroundColor White
Write-Host "   /alan          - Contexto IA & Automação" -ForegroundColor White
Write-Host "   /elena         - Contexto Produtividade TDAH" -ForegroundColor White
Write-Host "   /dr-green      - Contexto Cultivo Medicinal" -ForegroundColor White
Write-Host ""

# 5. Atualizar SESSION_LOG.md com início de sessão
if (Test-Path $sessionLog) {
    $content = Get-Content $sessionLog -Raw

    $recoveryBlock = @"

## 🔄 SESSÃO INICIADA

**Data/Hora:** $timestamp
**Recovery:** Automático (auto-recovery.ps1)
**Status:** ✅ Contexto recuperado

*Pronto para continuar de onde parou!*

---

"@

    # Adiciona no topo (após frontmatter se existir)
    if ($content -match "(?s)^---.*?---") {
        $content = $content -replace "((?s)^---.*?---)", "`$1$recoveryBlock"
    } else {
        $content = $recoveryBlock + $content
    }

    Set-Content -Path $sessionLog -Value $content -Encoding UTF8
}

Write-Host "✅ Auto-recovery completo!" -ForegroundColor Green
Write-Host "Bem-vindo de volta! Continuidade preservada. 🎯" -ForegroundColor Cyan
Write-Host ""
