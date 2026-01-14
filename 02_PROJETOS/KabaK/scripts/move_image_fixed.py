
import shutil
import os

source = r"C:\Users\gasse\.gemini\antigravity\brain\7139e83f-7767-4d2e-98ab-ccaa4224a7fa\tabela_kabak_v5_1768425471586.png"
dest_dir = r"C:\Users\gasse\OneDrive\Meu_Segundo_Cerebro\02_PROJETOS\KabaK\planejamento\recursos"
dest_file = os.path.join(dest_dir, "tabela_kabak_v5.png")

try:
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Diretório criado: {dest_dir}")
        
    shutil.copy2(source, dest_file)
    print(f"Sucesso: Imagem copiada para {dest_file}")
except Exception as e:
    print(f"Erro ao copiar: {e}")
