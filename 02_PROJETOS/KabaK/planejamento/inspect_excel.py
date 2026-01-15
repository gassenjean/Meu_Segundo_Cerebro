
import pandas as pd

file_path = r'C:\Users\Gassen\OneDrive\Meu_Segundo_Cerebro\02_PROJETOS\KabaK\planejamento\PLANILHA_KABAK_SANSOM.xlsx'

try:
    df = pd.read_excel(file_path, sheet_name='Sheet1', header=None)
    # Save to CSV for easy reading
    df.to_csv('sheet_dump.csv', index=True, header=True)
    print("Dumped to sheet_dump.csv")
except Exception as e:
    print(f"Error: {e}")
