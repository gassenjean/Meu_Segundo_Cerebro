
import shutil
import os

source = r"C:\Users\gasse\.gemini\antigravity\brain\7139e83f-7767-4d2e-98ab-ccaa4224a7fa\tabela_kabak_v5_1768425471586.png"
dest = r"C:\Users\gasse\OneDrive\Meu_Segundo_Cerebro\02_PROJETOS\KabaK\planejamento\recursos\tabela_kabak_v5.png"

try:
    shutil.copy2(source, dest)
    print(f"Sucesso: Imagem copiada para {dest}")
except Exception as e:
    print(f"Erro ao copiar: {e}")
