
import os
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

# Caminhos dentro do workspace
workspace_root = r"C:\Users\gasse\OneDrive\Meu_Segundo_Cerebro"
source_rel = r"02_PROJETOS\KabaK\recursos\ESBOCO_FINANCEIRO_SANSOM.HEIC"
dest_rel = r"02_PROJETOS\KabaK\recursos\ESBOCO_FINANCEIRO_SANSOM.png"

source = os.path.join(workspace_root, source_rel)
destination = os.path.join(workspace_root, dest_rel)

print(f"Converting: {source} -> {destination}")

try:
    if not os.path.exists(source):
        print(f"Error: Source file not found at {source}")
    else:
        image = Image.open(source)
        image.save(destination, format="png")
        print(f"Success: Converted to {destination}")
except Exception as e:
    print(f"Error: {e}")
