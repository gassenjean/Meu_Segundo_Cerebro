import re
import os

SOURCE_FILE = r"c:/Users/gasse/OneDrive/Meu_Segundo_Cerebro/02_PROJETOS/Estudo_Alan_Nicolas/WIKI/TEMP_AGREGADO_PROMPTS_RAW.md"
OUTPUT_DIR = r"c:/Users/gasse/OneDrive/Meu_Segundo_Cerebro/02_PROJETOS/Estudo_Alan_Nicolas/WIKI/ASSETS/PROMPTS"

def extract_prompts():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    with open(SOURCE_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    # Split by the header pattern
    # Pattern looks like: # 📄 FONTE: filename.md\nCaminho: ...\n---\n
    
    # We regex split but keep the delimiter to know filenames
    # Actually, simpler: define a pattern and finditer
    
    pattern = re.compile(r'# 📄 FONTE: (.+?)\nCaminho: (.+?)\n---\n', re.DOTALL)
    
    # We need to split the content based on this, or iterate.
    # Since the content is between headers, let's use split.
    # format: [header1, content1, header2, content2...]
    
    parts = re.split(r'(# 📄 FONTE: .+?\nCaminho: .+?\n---\n)', content)
    
    # parts[0] is usually preamble before first file
    
    count = 0
    
    # Iterate in pairs (header, content)
    # Since split returns [preamble, sep1, content1, sep2, content2...]
    # We skip preamble (0)
    
    for i in range(1, len(parts), 2):
        header_block = parts[i]
        file_content = parts[i+1] if i+1 < len(parts) else ""
        
        # Extract filename from header
        match = pattern.match(header_block)
        if match:
            filename = match.group(1).strip()
            # Clean filename to be safe
            safe_filename = filename.split('/')[-1].split('\\')[-1]
            
            # If filename has spaces, maybe replace with _ or keep
            # Let's keep original names but ensure they are safe
            safe_filename = re.sub(r'[<>:"/\\|?*]', '_', safe_filename)
            
            output_path = os.path.join(OUTPUT_DIR, safe_filename)
            
            # Write content
            with open(output_path, 'w', encoding='utf-8') as out:
                # Remove extra newlines at start/end
                out.write(file_content.strip())
                
            print(f"✅ Extracted: {safe_filename}")
            count += 1
            
    print(f"\n🎉 Total extracted: {count}")

if __name__ == "__main__":
    extract_prompts()
