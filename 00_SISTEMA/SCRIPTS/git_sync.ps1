$ErrorActionPreference = "Stop"

Write-Host "🔄 Iniciando Sincronização Git..." -ForegroundColor Cyan

# 1. Verificar Status
Write-Host "1. Verificando status..." -ForegroundColor Yellow
git status

# 2. Pull (Trazer mudanças remotas)
Write-Host "`n2. Baixando atualizações (Pull)..." -ForegroundColor Yellow
git pull --rebase origin master
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Erro no Pull. Resolva conflitos manualmente." -ForegroundColor Red
    exit
}

# 3. Add (Adicionar mudanças locais)
Write-Host "`n3. Adicionando arquivos..." -ForegroundColor Yellow
git add .

# 4. Commit e Push
$status = git status --porcelain
if ($status) {
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
    $message = "sync: auto-sync $timestamp 🚀"
    
    Write-Host "`n4. Comitando: $message" -ForegroundColor Yellow
    git commit -m "$message"
    
    Write-Host "`n5. Enviando (Push)..." -ForegroundColor Yellow
    git push origin master
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`n✅ Sincronização concluída com sucesso!" -ForegroundColor Green
    } else {
        Write-Host "`n❌ Erro no Push." -ForegroundColor Red
    }
} else {
    Write-Host "`n✅ Nada para comitar. Tudo limpo." -ForegroundColor Green
}
