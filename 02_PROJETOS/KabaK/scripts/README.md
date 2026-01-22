---
criado: 2026-01-22T12:30:00-03:00
atualizado: 2026-01-22T12:30:00-03:00
tipo: documentacao
---

# Scripts Python - KabaK

Documentação dos scripts de automação do projeto KabaK.

---

## Scripts Atuais (Usar Estes)

| Script | Função | Uso |
|--------|--------|-----|
| `generate_kabak_excel_v5.py` | Gerar planilha Excel com dados financeiros | `python generate_kabak_excel_v5.py` |
| `render_briefing.py` | Renderizar briefing em HTML/PDF | `python render_briefing.py` |
| `excel_to_md.py` | Converter Excel para Markdown | `python excel_to_md.py input.xlsx` |
| `generate_html_print.py` | Gerar HTML para impressão | `python generate_html_print.py` |
| `convert_heic_local.py` | Converter imagens HEIC para JPG | `python convert_heic_local.py` |
| `move_image_fixed.py` | Mover e organizar imagens | `python move_image_fixed.py` |

---

## Versões Antigas (Não Usar)

Estes scripts são versões anteriores mantidas para histórico:

| Script | Substituído Por |
|--------|-----------------|
| `generate_kabak_excel.py` | `generate_kabak_excel_v5.py` |
| `generate_kabak_excel_v2.py` | `generate_kabak_excel_v5.py` |
| `generate_kabak_excel_v3.py` | `generate_kabak_excel_v5.py` |
| `generate_kabak_excel_v4.py` | `generate_kabak_excel_v5.py` |
| `move_image.py` | `move_image_fixed.py` |

---

## Descrição Detalhada

### generate_kabak_excel_v5.py

Gera planilha Excel com projeções financeiras do projeto KabaK.

**Funcionalidades:**
- Calcula investimento por sócio
- Projeção de receitas 12 meses
- Cálculo de margem e lucro
- Formatação profissional

**Dependências:** `openpyxl`

---

### render_briefing.py

Renderiza briefing jurídico em formato HTML para impressão.

**Funcionalidades:**
- Converte Markdown para HTML
- Formatação profissional
- Pronto para impressão

**Dependências:** `markdown`

---

### excel_to_md.py

Converte planilhas Excel para formato Markdown.

**Funcionalidades:**
- Lê arquivos .xlsx
- Gera tabelas Markdown
- Preserva formatação

**Dependências:** `openpyxl`

---

### generate_html_print.py

Gera versão HTML otimizada para impressão de documentos.

**Dependências:** Nenhuma externa

---

### convert_heic_local.py

Converte imagens HEIC (iPhone) para JPG.

**Dependências:** `pillow-heif`, `PIL`

---

### move_image_fixed.py

Move e organiza imagens em pastas apropriadas.

**Dependências:** Nenhuma externa

---

## Instalação de Dependências

```bash
pip install openpyxl markdown pillow pillow-heif
```

---

## Convenções

1. **Versões:** Scripts com versões (v1, v2...) - usar sempre a mais recente
2. **_fixed suffix:** Versão corrigida do script original
3. **Manter histórico:** Não deletar versões antigas (referência)

---

**Última atualização:** 22/Jan/2026
**Mantido por:** Gassen
