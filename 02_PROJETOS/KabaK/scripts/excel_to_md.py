
import pandas as pd
import shutil
import os

source_excel = r"C:\Users\gasse\OneDrive\Meu_Segundo_Cerebro\02_PROJETOS\KabaK\planejamento\PLANILHA_KABAK_SANSOM.xlsx"
temp_excel = r"C:\Users\gasse\OneDrive\Meu_Segundo_Cerebro\temp_read_kabak.xlsx"
output_md = r"C:\Users\gasse\OneDrive\Meu_Segundo_Cerebro\tabela_final.md"

try:
    shutil.copy2(source_excel, temp_excel)
    
    # Ler layout original (Meses nas Colunas) - É isso que o usuário quer ver, mas sem quebrar
    df = pd.read_excel(temp_excel, index_col=0)
    
    def format_brl(val):
        if isinstance(val, (int, float)):
            return f"R$ {val:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        return val

    df_formatted = df.applymap(format_brl)
    
    # Gerar HTML com classes para estilo
    html_table = df_formatted.to_html(classes="finance-table", border=0)
    
    # CSS para Scroll Horizontal e Estilo Clean
    html_block = f"""
<div style="width: 100%; overflow-x: auto; background-color: #1e1e1e; padding: 10px; border-radius: 5px;">
    <style>
        .finance-table {{
            border-collapse: collapse;
            width: 100%;
            color: #d1d1d1;
            font-family: sans-serif;
            font-size: 13px;
        }}
        .finance-table th, .finance-table td {{
            border: 1px solid #444;
            padding: 8px;
            text-align: right;
            white-space: nowrap;
        }}
        .finance-table th {{
            background-color: #2d2d2d;
            font-weight: bold;
            text-align: center;
            color: #ffffff;
            position: sticky;
            left: 0;
        }}
        /* Primeira coluna sticky para cabecalho das linhas */
        .finance-table tbody th {{
            background-color: #252526;
            position: sticky;
            left: 0;
            z-index: 1;
            text-align: left;
        }}
        .finance-table tr:nth-child(even) {{
            background-color: #252526;
        }}
        .finance-table tr:hover {{
            background-color: #333;
        }}
    </style>
    {html_table}
</div>
<p><em>* Arraste lateralmente para visualizar todos os meses</em></p>
"""

    with open(output_md, "w", encoding="utf-8") as f:
        f.write(html_block)
        
    print("Sucesso: Tabela HTML Scrollable gerada.")

except Exception as e:
    print(f"Erro: {e}")

finally:
    if os.path.exists(temp_excel):
        try:
            os.remove(temp_excel)
        except:
            pass
