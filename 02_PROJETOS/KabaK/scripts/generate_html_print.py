
import pandas as pd
import shutil
import os

source_excel = r"C:\Users\gasse\OneDrive\Meu_Segundo_Cerebro\02_PROJETOS\KabaK\planejamento\PLANILHA_KABAK_SANSOM.xlsx"
temp_excel = r"C:\Users\gasse\OneDrive\Meu_Segundo_Cerebro\temp_read_kabak.xlsx"
output_html = r"C:\Users\gasse\OneDrive\Meu_Segundo_Cerebro\02_PROJETOS\KabaK\planejamento\tabela_para_print.html"

try:
    shutil.copy2(source_excel, temp_excel)
    
    # Ler Excel (Original: Horizontal)
    df = pd.read_excel(temp_excel, index_col=0)
    
    def format_brl(val):
        if isinstance(val, (int, float)):
            return f"{val:,.0f}".replace(",", ".") # Simplificar sem centavos para caber melhor? Nao, manter.
        return val

    # Formatar strings
    # Vamos manter centavos mas formatar bonito
    def fmt(x):
        if isinstance(x, (int, float)):
             return f"R$ {x:,.2f}".replace(",", "_").replace(".", ",").replace("_", ".")
        return x

    df_formatted = df.applymap(fmt)
    
    # Gerar HTML completo com CSS estilo Excel
    html_content = f"""
    <html>
    <head>
        <style>
            body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #ffffff; padding: 20px; }}
            table {{ border-collapse: collapse; width: 100%; box-shadow: 0 0 20px rgba(0,0,0,0.1); }}
            th, td {{ border: 1px solid #d0d7de; padding: 12px 8px; text-align: right; white-space: nowrap; font-size: 14px; color: #333; }}
            th {{ background-color: #f6f8fa; font-weight: 600; text-align: center; color: #24292f; }}
            tr:nth-child(even) {{ background-color: #fcfcfc; }}
            tr:hover {{ background-color: #f0f0f0; }}
            
            /* Destaque para headers de linha */
            tbody th {{ text-align: left; background-color: #fafbfc; min-width: 150px; font-weight: 500; }}
            
            /* Cores especiais para certas linhas se possivel (Lucro/Caixa) */
            tr:last-child td {{ font-weight: bold; background-color: #e6ffec; color: #1a7f37; }} /* Caixa */
            tr:nth-last-child(2) td {{ font-weight: bold; }} /* Lucro */
            
        </style>
    </head>
    <body>
        {df_formatted.to_html(border=0)}
    </body>
    </html>
    """

    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print(f"Sucesso: HTML gerado em {output_html}")

except Exception as e:
    print(f"Erro: {e}")

finally:
    if os.path.exists(temp_excel):
        try:
            os.remove(temp_excel)
        except:
            pass
