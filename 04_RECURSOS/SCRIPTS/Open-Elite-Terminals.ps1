# Open-Elite-Terminals.ps1
# Opens 4 Windows Terminal tabs with specific titles for the System Gassen V2

Write-Host "Iniciando Protocolo Elite..." -ForegroundColor Cyan

# Check if wt.exe (Windows Terminal) is available
if (Get-Command wt -ErrorAction SilentlyContinue) {
    # Open 4 tabs with titles and specific starting directories (Root)
    # Tab 1: LUCAS (DeFi)
    # Tab 2: PEDRO (Traffic)
    # Tab 3: ARCHITECT (System)
    # Tab 4: ELENA (TDAH/Personal)
    
    wt -w 0 nt -t "🪙 LUCAS (DeFi)" -d . ; `
    nt -t "📈 PEDRO (Traffic)" -d . ; `
    nt -t "🏛️ ARCHITECT (System)" -d . ; `
    nt -t "🧠 ELENA (Personal)" -d .

    Write-Host "Terminais Elite abertos com sucesso." -ForegroundColor Green
} else {
    Write-Warning "Windows Terminal (wt.exe) não encontrado. Por favor, instale-o via Microsoft Store."
}
