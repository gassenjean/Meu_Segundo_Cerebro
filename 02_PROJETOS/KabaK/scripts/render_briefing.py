import markdown
import os

# Paths
md_file_path = r"C:\Users\gasse\OneDrive\Meu_Segundo_Cerebro\02_PROJETOS\KabaK\docs\projetos\BRIEFING_OUTLET_SANSOM.md"
html_file_path = r"C:\Users\gasse\OneDrive\Meu_Segundo_Cerebro\02_PROJETOS\KabaK\docs\projetos\BRIEFING_OUTLET_SANSOM.html"

# CSS for a professional look (Business Plan style)
css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    body {
        font-family: 'Inter', sans-serif;
        line-height: 1.6;
        color: #1a1a1a;
        max-width: 900px;
        margin: 0 auto;
        padding: 40px;
        background-color: #f9f9f9;
        -webkit-font-smoothing: antialiased;
    }
    
    .container {
        background-color: white;
        padding: 60px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        border-radius: 12px;
        border: 1px solid #eaeaea;
    }

    h1 {
        font-size: 28px;
        color: #2D3748;
        border-bottom: 2px solid #E2E8F0;
        padding-bottom: 10px;
        margin-top: 0;
    }
    
    h2 {
        font-size: 22px;
        color: #2C5282; /* Professional Blue */
        margin-top: 30px;
        border-left: 4px solid #4299E1;
        padding-left: 12px;
    }
    
    h3 {
        font-size: 18px;
        color: #4A5568;
        font-weight: 700;
        margin-top: 25px;
    }
    
    p, li {
        color: #4A5568;
        font-size: 15px;
    }
    
    strong {
        color: #2D3748;
        font-weight: 700;
    }
    
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 20px 0;
        font-size: 14px;
    }
    
    th, td {
        border: 1px solid #E2E8F0;
        padding: 12px;
        text-align: left;
    }
    
    th {
        background-color: #F7FAFC;
        font-weight: 600;
        color: #4A5568;
    }
    
    blockquote {
        background-color: #EBF8FF;
        border-left: 4px solid #4299E1;
        margin: 20px 0;
        padding: 15px 20px;
        color: #2C5282;
    }
    
    code {
        background-color: #EDF2F7;
        padding: 2px 5px;
        border-radius: 4px;
        font-family: monospace;
        color: #C05621;
    }
    
    .admonition {
        border-radius: 4px;
        padding: 15px;
        margin-bottom: 20px;
        border: 1px solid transparent;
    }
    
    .admonition.important {
        background-color: #fff5f5;
        border-color: #feb2b2;
        color: #c53030;
    }
    
    .admonition.note {
        background-color: #ebf8ff;
        border-color: #90cdf4;
        color: #2b6cb0;
    }
    
    ul {
        padding-left: 20px;
    }
    
    li {
        margin-bottom: 8px;
    }
    
    /* Frontmatter styling if printed */
    .frontmatter {
        background-color: #EDF2F7;
        padding: 15px;
        margin-bottom: 30px;
        border-radius: 6px;
        font-size: 13px;
        color: #718096;
    }

</style>
"""

# Read Markdown
with open(md_file_path, "r", encoding="utf-8") as f:
    text = f.read()

# Handle frontmatter manually (simple extraction)
content_start = 0
frontmatter = ""
if text.startswith("---"):
    end_idx = text.find("---", 3)
    if end_idx != -1:
        frontmatter = text[3:end_idx].strip()
        content_start = end_idx + 3
        text = text[content_start:].strip()

# Format frontmatter for display
formatted_frontmatter = ""
if frontmatter:
    formatted_frontmatter = '<div class="frontmatter">' + "<br>".join(frontmatter.split("\n")) + "</div>"

# Convert MD to HTML (using extensions for better rendering)
# Assuming 'markdown' lib supports these
html_body = markdown.markdown(text, extensions=['tables', 'fenced_code', 'nl2br'])

# Final HTML Structure
final_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>KabaK Briefing</title>
    {css}
</head>
<body>
    <div class="container">
        {formatted_frontmatter}
        {html_body}
    </div>
</body>
</html>
"""

# Write HTML
with open(html_file_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Briefing HTML generated at: {html_file_path}")
