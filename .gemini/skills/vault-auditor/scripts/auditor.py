
import os
import sys
import re
import datetime
import hashlib
from collections import defaultdict

# Configuração
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
REPORTS_DIR = os.path.join(ROOT_DIR, "00_SISTEMA", "RELATORIOS")

def log(message: str, level: str = "INFO"):
    emojis = {"INFO": "ℹ️", "SUCCESS": "✅", "WARN": "⚠️", "ERROR": "❌", "CRITICAL": "🔴"}
    print(f"{emojis.get(level, '')} [{level}] {message}")

class VaultAuditor:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.files = []
        self.errors = defaultdict(list)
        self.stats = defaultdict(int)
        self.valid_prefixes = ['MOC_', '_MOC_', 'TEMPLATE_', 'PROTOCOLO_', 'PLANO_', 'STATUS_', 'CHECKPOINT_', 'ROADMAP_', 'GUIA_', 'README', '_temp_', '_draft_', 'REF_']
        self.ignored_dirs = ['.git', '.claude', '.gemini', '.obsidian', 'node_modules', '.trash', '.venv']
        self.link_cache = set()

    def scan_files(self):
        log("Indexando arquivos...", "INFO")
        for root, dirs, files in os.walk(self.root_dir):
            # Ignore hidden/system dirs
            dirs[:] = [d for d in dirs if d not in self.ignored_dirs]
            
            for file in files:
                filepath = os.path.join(root, file)
                relpath = os.path.relpath(filepath, self.root_dir)
                self.files.append({'path': filepath, 'relpath': relpath, 'name': file})
                self.link_cache.add(file) # Cache filenames for link checking
                
        self.stats['total_files'] = len(self.files)
        log(f"Total arquivos: {self.stats['total_files']}", "INFO")

    def check_nomenclature(self):
        log("Verificando Nomenclatura...", "INFO")
        for f in self.files:
            name = f['name']
            if not name.endswith('.md'): continue
            
            issues = []
            
            # 1. Espaços
            if ' ' in name:
                issues.append("Espaços no nome")
                
            # 2. Caracteres proibidos
            if any(char in name for char in [':', '?', '*', '<', '>', '|']):
                issues.append("Caractere proibido")
                
            # 3. Tamanho
            if len(name) > 60:
                issues.append("Nome > 60 chars")
                
            # 4. Prefixos
            # Se for MOC, Template, etc
            upper_name = name.upper()
            # Fix: Use regex word boundary to avoid substrings like eMOCional
            if re.search(r'\bMOC\b', upper_name) and not (name.startswith("MOC_") or name.startswith("_MOC_")):
                issues.append("Prefixo MOC ausente/incorreto")
            if "TEMPLATE" in upper_name and not name.startswith("TEMPLATE_"):
                issues.append("Prefixo TEMPLATE ausente")
                
            # 5. Datas (DDMMMYYYY)
            # Regex simples para datas
            # Se tiver data no nome, verificar formato
            # match 2026-01-18 (errado)
            if re.search(r'\d{4}-\d{2}-\d{2}', name) or re.search(r'\d{2}-\d{2}-\d{4}', name):
                issues.append("Formato data incorreto (Use DDMMMYYYY)")
                
            if issues:
                self.errors['Nomenclatura'].append({'file': f['relpath'], 'issues': issues, 'severity': 'CRITICAL'})
                self.stats['nomenclatura'] += 1

    def check_localization(self):
        log("Verificando Localização...", "INFO")
        allowed_root = ['README.md', 'CLAUDE.md', 'SESSION_LOG.md', 'PC_SYNC_LOG.md', 'STATUS_VAULT.md', 'CHANGELOG.md']
        
        for f in self.files:
            path = f['relpath']
            name = f['name']
            folder = os.path.dirname(path)
            
            issues = []
            
            # 1. Arquivos na raiz
            if not folder and name not in allowed_root and not name.startswith('.'):
                 issues.append("Arquivo na raiz do vault")
                 
            # 2. Pastas específicas
            if name.startswith("TEMPLATE_") and "04_RECURSOS\\TEMPLATES" not in path.replace('/', '\\'):
                 issues.append("Template fora de 04_RECURSOS/TEMPLATES")
                 
            if issues:
                self.errors['Localização'].append({'file': path, 'issues': issues, 'severity': 'CRITICAL'})
                self.stats['localizacao'] += 1

    def check_markdown(self):
        log("Verificando Markdown...", "INFO")
        for f in self.files:
            if not f['name'].endswith('.md'): continue
            
            try:
                with open(f['path'], 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                    
                issues = []
                # 1. Empty
                if not content.strip():
                    issues.append("Arquivo vazio")
                else:
                    # 2. H1
                    h1_count = len(re.findall(r'^# ', content, re.MULTILINE))
                    if h1_count == 0:
                        issues.append("Sem título H1 (# Título)")
                    elif h1_count > 1:
                        issues.append(f"Múltiplos H1 ({h1_count})")
                        
                if issues:
                     self.errors['Estrutura Markdown'].append({'file': f['relpath'], 'issues': issues, 'severity': 'IMPORTANTE'})
                     self.stats['markdown'] += 1
            except Exception:
                pass

    def check_links(self):
        log("Verificando Links...", "INFO")
        for f in self.files:
            if not f['name'].endswith('.md'): continue
            
            try:
                with open(f['path'], 'r', encoding='utf-8', errors='ignore') as file:
                    content = file.read()
                    
                links = re.findall(r'\[\[(.+?)\]\]', content)
                for link in links:
                    # Remove alias [[link|alias]]
                    target = link.split('|')[0]
                    # Remove anchor [[link#anchor]]
                    target = target.split('#')[0]
                    
                    if not target: continue
                    
                    found = False
                    # Check exact match
                    if target in self.link_cache:
                        found = True
                    else:
                        # Check with .md
                        if target + ".md" in self.link_cache:
                            found = True
                            
                    if not found:
                        self.errors['Links'].append({'file': f['relpath'], 'issues': [f"Link quebrado: [[{target}]]"], 'severity': 'IMPORTANTE'})
                        self.stats['links'] += 1
                        
            except Exception:
                pass

    def check_projects(self):
        log("Verificando Projetos...", "INFO")
        projects_dir = os.path.join(self.root_dir, "02_PROJETOS")
        if not os.path.exists(projects_dir): return
        
        # List direct subfolders
        projects = [d for d in os.listdir(projects_dir) if os.path.isdir(os.path.join(projects_dir, d)) and not d.startswith('_')]
        
        for proj in projects:
            p_path = os.path.join(projects_dir, proj)
            files = os.listdir(p_path)
            
            issues = []
            if "README.md" not in files:
                issues.append("Sem README.md")
            if "STATUS_ATUAL.md" not in files:
                issues.append("Sem STATUS_ATUAL.md")
                
            # Check folders
            subdirs = [d for d in files if os.path.isdir(os.path.join(p_path, d))]
            required = ['planejamento', 'docs'] # Checkpoints e recursos opcional
            missing = [r for r in required if r not in subdirs]
            if missing:
                issues.append(f"Faltando pastas: {', '.join(missing)}")
                
            if issues:
                self.errors['Projetos'].append({'file': f"02_PROJETOS/{proj}", 'issues': issues, 'severity': 'IMPORTANTE'})
                self.stats['projetos'] += 1

    def check_conflicts_and_obsolete(self):
        log("Verificando Obsoletos...", "INFO")
        # Duplicates by name
        name_map = defaultdict(list)
        for f in self.files:
            name_map[f['name']].append(f['relpath'])
            
        for name, paths in name_map.items():
            if len(paths) > 1 and name != 'README.md': # READMEs are allowed
                 self.errors['Duplicação'].append({'file': name, 'issues': [f"Duplicado em: {', '.join(paths)}"], 'severity': 'ATENÇÃO'})
                 self.stats['duplicacao'] += 1
                 
        # Obsolete .bak
        for f in self.files:
            if '.bak' in f['name']:
                 self.errors['Arquivos Obsoletos'].append({'file': f['relpath'], 'issues': ["Arquivo de backup"], 'severity': 'LIMPEZA'})
                 self.stats['obsoletos'] += 1

    def generate_report(self):
        log("Gerando Relatório...", "INFO")
        timestamp = datetime.datetime.now().strftime("%d/%b/%Y %H:%M").upper()
        filename = f"AUDITORIA_VAULT_{datetime.datetime.now().strftime('%d%b%Y').upper()}.md"
        filepath = os.path.join(REPORTS_DIR, filename)
        
        os.makedirs(REPORTS_DIR, exist_ok=True)
        
        lines = []
        lines.append("---")
        lines.append(f"data: {timestamp}")
        lines.append("tipo: auditoria-vault")
        lines.append("versao-auditor: 1.0")
        lines.append("---\n")
        lines.append("# RELATÓRIO: Auditoria Completa do Vault\n")
        lines.append(f"**Data:** {timestamp}")
        lines.append(f"**Ferramenta:** vault-auditor v1.0")
        lines.append(f"**Total de arquivos analisados:** {self.stats['total_files']}\n")
        lines.append("---\n")
        
        # Summary
        lines.append("## 📊 RESUMO EXECUTIVO\n")
        lines.append("| Categoria | Total Erros | Severidade |")
        lines.append("|-----------|-------------|------------|")
        
        cats = [
            ('Nomenclatura', 'CRÍTICO'), 
            ('Localização', 'CRÍTICO'), 
            ('Estrutura Markdown', 'IMPORTANTE'),
            ('Links', 'IMPORTANTE'),
            ('Projetos', 'IMPORTANTE'),
            ('Duplicação', 'ATENÇÃO'),
            ('Arquivos Obsoletos', 'LIMPEZA')
        ]
        
        total_errors = sum(self.stats[k.lower().replace(' ', '_')] for k, _ in cats) # Adjust keys later
        # Simplified mapping
        key_map = {
            'Nomenclatura': 'nomenclatura',
            'Localização': 'localizacao',
            'Estrutura Markdown': 'markdown',
            'Links': 'links',
            'Projetos': 'projetos',
            'Duplicação': 'duplicacao',
            'Arquivos Obsoletos': 'obsoletos'
        }
        
        total_sev = 0
        for cat, sev_label in cats:
            count = len(self.errors[cat])
            icon = "🔴" if "CRÍTICO" in sev_label else "🟡" if "IMPORTANTE" in sev_label else "🟢"
            lines.append(f"| {cat} | {count} | {icon} {sev_label} |")
            if "CRÍTICO" in sev_label: total_sev += count * 2
            else: total_sev += count
            
        status = "✅ Saudável"
        if total_sev > 0: status = "⚠️ Atenção Necessária"
        if total_sev > 10: status = "🔴 Ação Urgente"
        
        lines.append(f"\n**Status Geral:** {status}\n")
        lines.append("---\n")
        
        # Details
        for cat, sev_label in cats:
            items = self.errors[cat]
            if not items: continue
            
            icon = "🔴" if "CRÍTICO" in sev_label else "🟡" if "IMPORTANTE" in sev_label else "🟢"
            lines.append(f"## {icon} {cat} ({len(items)} found)\n")
            
            for item in items[:50]: # Limit to avoid huge report
                lines.append(f"### `{item['file']}`")
                for issue in item['issues']:
                    lines.append(f"- **Erro:** {issue}")
                    # Suggestion logic could go here
                lines.append("")
                
            if len(items) > 50:
                lines.append(f"*... e mais {len(items)-50} arquivos.*")
            lines.append("---\n")
            
        # Checklist
        lines.append("## ✅ CHECKLIST DE CORREÇÃO\n")
        if self.errors['Nomenclatura']:
            lines.append(f"- [ ] Corrigir {len(self.errors['Nomenclatura'])} erros de Nomenclatura")
        if self.errors['Localização']:
            lines.append(f"- [ ] Mover {len(self.errors['Localização'])} arquivos para local correto")
            
        lines.append("\n**FIM DO RELATÓRIO**")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("\n".join(lines))
            
        log(f"Relatório gerado: {filepath}", "SUCCESS")
        return filename

    def run(self):
        self.scan_files()
        self.check_nomenclature()
        self.check_localization()
        self.check_markdown()
        self.check_links()
        self.check_projects()
        self.check_conflicts_and_obsolete()
        report = self.generate_report()
        print(f"Relatório criado em: 00_SISTEMA/RELATORIOS/{report}")

if __name__ == "__main__":
    auditor = VaultAuditor(ROOT_DIR)
    auditor.run()
