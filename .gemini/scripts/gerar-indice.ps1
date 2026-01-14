# gerar-indice.ps1
# Gera INDICE_VAULT_COMPLETO.md automaticamente
# Versão: 1.0
# Criado: 30/12/2025

$ErrorActionPreference = "Continue"
$outputPath = "C:\Users\Gassen\OneDrive\Meu_Segundo_Cerebro\00_SISTEMA\INDICE_VAULT_COMPLETO.md"
$vaultRoot = "C:\Users\Gassen\OneDrive\Meu_Segundo_Cerebro"

Write-Host "🔍 Gerando índice do vault..." -ForegroundColor Cyan

# Contar arquivos
$totalFiles = (Get-ChildItem -Path $vaultRoot -Recurse -File -ErrorAction SilentlyContinue | Measure-Object).Count

# Header
$content = @"
# ÍNDICE COMPLETO - MEU SEGUNDO CÉREBRO

**Última atualização:** $(Get-Date -Format "dd/MM/yyyy HH:mm")
**Total de arquivos:** $totalFiles
**Gerado automaticamente por:** scripts/gerar-indice.ps1

---

## 🗂️ ESTRUTURA DE CATEGORIAS

"@

# Função para listar arquivos principais
function Get-MainFiles {
    param($path, $category)

    $files = Get-ChildItem -Path $path -File -Filter "*.md" -ErrorAction SilentlyContinue |
             Where-Object { $_.Name -notlike ".*" } |
             Select-Object -First 10 |
             Sort-Object Name

    $result = ""
    foreach ($file in $files) {
        $result += "- $($file.Name)`n"
    }
    return $result
}

# Processar cada categoria
$categories = @(
    @{Name="00_SISTEMA"; Title="Meta-organização"},
    @{Name="01_CONHECIMENTO"; Title="Base de conhecimento"},
    @{Name="02_PROJETOS"; Title="Projetos ativos"},
    @{Name="03_APRENDIZADO"; Title="Cursos e estudos"},
    @{Name="04_RECURSOS"; Title="Templates, prompts, tools"},
    @{Name="05_PESSOAL"; Title="Notas pessoais"}
)

foreach ($cat in $categories) {
    $catPath = Join-Path $vaultRoot $cat.Name

    if (Test-Path $catPath) {
        $fileCount = (Get-ChildItem -Path $catPath -Recurse -File -ErrorAction SilentlyContinue | Measure-Object).Count
        $folderCount = (Get-ChildItem -Path $catPath -Directory -ErrorAction SilentlyContinue | Measure-Object).Count

        $content += @"

### $($cat.Name) ($($cat.Title))
**Arquivos:** $fileCount | **Pastas:** $folderCount

**Principais arquivos:**
$(Get-MainFiles -path $catPath -category $cat.Name)

"@
    }
}

# Seção de conceitos-chave
$content += @"

---

## 🔍 ÍNDICE DE CONCEITOS-CHAVE

### TDAH & Produtividade
- **Mentes Inquietas (15 capítulos)** → ``04_RECURSOS/Mentes_Inquietas/``
  - Cap 1: O que é TDAH (checklist 50 perguntas)
  - Cap 5: Criatividade (superpoder TDAH)
  - Caps 2-15: Mulheres, Infância, Vida Afetiva, Tratamento, etc
- **Procrastinação (Episódio 017)** → ``01_CONHECIMENTO/Desenvolvimento_Pessoal/017_-_Por_Que_Procrastinamos__E_Como_Parar!.md``
- **Elena Vasquez (agente TDAH)** → ``04_RECURSOS/PROMPTS/Agentes_Sistema/PROMPT_AGENTE_ELENA_VASQUEZ.md``
- **Foco (3 tipos)** → ``01_CONHECIMENTO/Desenvolvimento_Pessoal/Foco.md``
- **Obsessão Focada** → ``01_CONHECIMENTO/Desenvolvimento_Pessoal/Obsessão_Focada.md``
- **Hiperconsciência** → ``01_CONHECIMENTO/Desenvolvimento_Pessoal/Hiperconsciencia.md``

### Tráfego Pago (Pedro Sobral)
- **Curso Subido Tráfego** → ``03_APRENDIZADO/Cursos_Ativos/Subido_Trafego/``
- **Framework 7 Pilares** → ``03_APRENDIZADO/Cursos_Ativos/Subido_Trafego/Conceitos/``
- **Status:** M02 (9/13 aulas - 69%)
- **Projeto:** KabaK (referências no curso)

### DeFi & Cripto (Lucas Amoedo)
- **Curso DeFi Journey** → ``03_APRENDIZADO/Cursos_Ativos/DeFi_Journey/``
- **Status:** M4 Leva 5/10 (50%)
- **Projeto:** DeFi_Verso_2025 → ``02_PROJETOS/DeFi_Verso_2025/``
- **Metodologia:** Benjamin Graham DeFi

### IA & Automação (Alan Nicolas)
- **Curso Formação Lendária** → ``03_APRENDIZADO/Cursos_Ativos/Formacao_Lendaria_2025/``
- **N8N workflows** → ``03_APRENDIZADO/Cursos_Ativos/Formacao_Lendaria_2025/N8N/``
- **Status:** Semana 7/10 (70%)
- **Sistema 5C** → ``04_RECURSOS/WORKFLOWS/Workflow_Sistema_5C_Automatizado.md``

### Agentes do Sistema
- **Névoa** (Orquestração) → ``04_RECURSOS/PROMPTS/Agentes_Sistema/PROMPT_AGENTE_NEVOA.md``
- **Elena Vasquez** (TDAH/Produtividade) → ``04_RECURSOS/PROMPTS/Agentes_Sistema/PROMPT_AGENTE_ELENA_VASQUEZ.md``
- **Pedro Sobral** (Tráfego) → ``04_RECURSOS/PROMPTS/Agentes_Sistema/PROMPT_AGENTE_PEDRO_SOBRAL.md``
- **Lucas Amoedo** (DeFi) → ``04_RECURSOS/PROMPTS/Agentes_Sistema/PROMPT_AGENTE_LUCAS_AMOEDO.md``
- **Alan Nicolas** (IA) → ``04_RECURSOS/PROMPTS/Agentes_Sistema/PROMPT_AGENTE_ALAN_NICOLAS.md``
- **Marie Kondo** (Organização) → ``04_RECURSOS/PROMPTS/Agentes_Sistema/PROMPT_AGENTE_MARIE_KONDO.md``

---

## 🎯 ATALHOS RÁPIDOS (Skills)

**Trabalhar com TDAH/Produtividade:**
``````bash
/coach        # Assistente pessoal TDAH
/mapa         # Este índice (sempre atualizado)
``````

**Trabalhar em Tráfego:**
``````bash
/pedro        # Contexto Pedro Sobral
``````

**Trabalhar em DeFi:**
``````bash
/lucas        # Contexto Lucas Amoedo
``````

**Trabalhar em IA:**
``````bash
/alan         # Contexto Alan Nicolas
``````

**Orquestração:**
``````bash
/nevoa        # Névoa (decisões complexas)
/dashboard    # Visão 360° do vault
``````

---

## 📊 ESTATÍSTICAS DO VAULT

**Total:** $totalFiles arquivos

**Por categoria:**
- 00_SISTEMA: $(if (Test-Path "$vaultRoot\00_SISTEMA") { (Get-ChildItem -Path "$vaultRoot\00_SISTEMA" -Recurse -File -ErrorAction SilentlyContinue | Measure-Object).Count } else { 0 }) arquivos
- 01_CONHECIMENTO: $(if (Test-Path "$vaultRoot\01_CONHECIMENTO") { (Get-ChildItem -Path "$vaultRoot\01_CONHECIMENTO" -Recurse -File -ErrorAction SilentlyContinue | Measure-Object).Count } else { 0 }) arquivos
- 02_PROJETOS: $(if (Test-Path "$vaultRoot\02_PROJETOS") { (Get-ChildItem -Path "$vaultRoot\02_PROJETOS" -Recurse -File -ErrorAction SilentlyContinue | Measure-Object).Count } else { 0 }) arquivos
- 03_APRENDIZADO: $(if (Test-Path "$vaultRoot\03_APRENDIZADO") { (Get-ChildItem -Path "$vaultRoot\03_APRENDIZADO" -Recurse -File -ErrorAction SilentlyContinue | Measure-Object).Count } else { 0 }) arquivos
- 04_RECURSOS: $(if (Test-Path "$vaultRoot\04_RECURSOS") { (Get-ChildItem -Path "$vaultRoot\04_RECURSOS" -Recurse -File -ErrorAction SilentlyContinue | Measure-Object).Count } else { 0 }) arquivos
- 05_PESSOAL: $(if (Test-Path "$vaultRoot\05_PESSOAL") { (Get-ChildItem -Path "$vaultRoot\05_PESSOAL" -Recurse -File -ErrorAction SilentlyContinue | Measure-Object).Count } else { 0 }) arquivos

---

**Gerado em:** $(Get-Date -Format "dd/MM/yyyy HH:mm:ss")
**Próxima atualização:** Manual via ``/mapa atualizar`` ou rodando script
**Script:** ``scripts/gerar-indice.ps1``

"@

# Salvar
Set-Content -Path $outputPath -Value $content -Encoding UTF8

Write-Host "✅ Índice gerado com sucesso!" -ForegroundColor Green
Write-Host "📍 Localização: $outputPath" -ForegroundColor Yellow
Write-Host "📊 Total de arquivos indexados: $totalFiles" -ForegroundColor Cyan
