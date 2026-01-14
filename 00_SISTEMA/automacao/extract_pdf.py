import os
import pypdf
from pathlib import Path

def extract_text_from_pdf(pdf_path):
    """Extracts text from a PDF file."""
    try:
        reader = pypdf.PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return None

def main():
    base_dir = Path(r"c:\Users\gasse\OneDrive\Meu_Segundo_Cerebro\03_APRENDIZADO\Cursos_Ativos\DeFi_Nova_Era\Portal_2\Transcricoes")
    output_dir = base_dir / "Processed"
    print(f"Attempting to create: {output_dir}")
    output_dir.mkdir(exist_ok=True)

    print(f"Scanning directory: {base_dir}")

    pdf_files = list(base_dir.glob("*.pdf"))
    
    if not pdf_files:
        print("No PDF files found.")
        return

    print(f"Found {len(pdf_files)} PDF files.")

    for pdf_file in pdf_files:
        print(f"Processing: {pdf_file.name}")
        text = extract_text_from_pdf(pdf_file)
        
        if text:
            output_filename = pdf_file.stem + ".md"
            output_path = output_dir / output_filename
            
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(f"# {pdf_file.stem}\n\n")
                f.write(text)
            
            print(f"Saved to: {output_path}")
        else:
            print(f"Failed to extract text from {pdf_file.name}")

if __name__ == "__main__":
    main()
