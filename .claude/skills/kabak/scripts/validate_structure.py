#!/usr/bin/env python3
"""
KabaK Structure Validator

Valida nomenclatura e estrutura de documentos do projeto KabaK.
Garante conformidade com padrões do vault.
"""

import re
from pathlib import Path
from typing import List, Dict, Tuple

# Padrões de nomenclatura válidos
VALID_PATTERNS = {
    'RESUMO_EXECUTIVO': r'^RESUMO_EXECUTIVO_[A-Z_]+_\d{2}[A-Z]{3}\d{4}\.md$',
    'RESUMO_FINANCEIRO': r'^RESUMO_FINANCEIRO_[A-Z_]+\.md$',
    'PROXIMOS_PASSOS': r'^PROXIMOS_PASSOS_[A-Z_]+\.md$',
    'BRIEFING': r'^BRIEFING_[A-Z_]+\.md$',
    'STATUS': r'^STATUS_[A-Z]+\.md$',
    'DASHBOARD': r'^DASHBOARD\.md$',
    'TODO': r'^TODO_[A-Za-z_]+\.md$',
    'CONCLUIDAS': r'^CONCLUIDAS\.md$',
    'BACKLOG': r'^BACKLOG\.md$',
    'README': r'^README\.md$',
}

def validate_filename(filename: str) -> Tuple[bool, str]:
    """
    Valida se nome de arquivo segue padrões KabaK.

    Returns:
        (is_valid, message)
    """
    # Verificar underscores (não espaços)
    if ' ' in filename:
        return False, "Nome contém espaços - usar underscores (_)"

    # Verificar extensão
    if not filename.endswith('.md'):
        return False, "Arquivo deve terminar com .md"

    # Verificar se corresponde a algum padrão válido
    for pattern_name, pattern in VALID_PATTERNS.items():
        if re.match(pattern, filename):
            return True, f"Válido - padrão {pattern_name}"

    # Se não corresponder a nenhum padrão específico, verificar padrões gerais
    # CamelCase para hierarquia
    if re.match(r'^[A-Z][a-z]+(_[A-Z][a-z]+)*\.md$', filename):
        return True, "Válido - padrão CamelCase hierárquico"

    return False, "Nome não segue padrão conhecido do vault"

def validate_frontmatter(content: str) -> Tuple[bool, List[str]]:
    """
    Valida frontmatter YAML do documento.

    Returns:
        (is_valid, list_of_issues)
    """
    issues = []

    # Verificar presença de frontmatter
    if not content.startswith('---'):
        return False, ["Frontmatter YAML ausente (deve começar com ---)"]

    # Extrair frontmatter
    try:
        end = content.find('---', 3)
        if end == -1:
            return False, ["Frontmatter YAML mal-formado (falta --- de fechamento)"]

        frontmatter = content[3:end]
    except:
        return False, ["Erro ao processar frontmatter"]

    # Campos obrigatórios
    required_fields = ['criado', 'atualizado']

    for field in required_fields:
        if f'{field}:' not in frontmatter:
            issues.append(f"Campo obrigatório ausente: {field}")

    # Validar formato de data
    date_pattern = r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}'

    if 'criado:' in frontmatter:
        criado_line = [l for l in frontmatter.split('\n') if 'criado:' in l][0]
        if not re.search(date_pattern, criado_line):
            issues.append("Campo 'criado' com formato incorreto (usar YYYY-MM-DDTHH:MM:SS)")

    if 'atualizado:' in frontmatter:
        atualizado_line = [l for l in frontmatter.split('\n') if 'atualizado:' in l][0]
        if not re.search(date_pattern, atualizado_line):
            issues.append("Campo 'atualizado' com formato incorreto (usar YYYY-MM-DDTHH:MM:SS)")

    return len(issues) == 0, issues

def validate_structure_folders(base_path: Path) -> Dict[str, bool]:
    """
    Valida estrutura de pastas do projeto KabaK.

    Returns:
        Dict com pastas e status de existência
    """
    required_folders = {
        'planejamento': base_path / 'planejamento',
        'checkpoints': base_path / 'checkpoints',
        'docs': base_path / 'docs',
        'recursos': base_path / 'recursos',
        'tarefas': base_path / 'tarefas',
        'metricas': base_path / 'metricas',
    }

    return {
        name: path.exists() and path.is_dir()
        for name, path in required_folders.items()
    }

def validate_required_files(base_path: Path) -> Dict[str, bool]:
    """
    Valida existência de arquivos obrigatórios.

    Returns:
        Dict com arquivos e status de existência
    """
    required_files = {
        'README.md': base_path / 'README.md',
        'STATUS_ATUAL.md': base_path / 'STATUS_ATUAL.md',
        'DASHBOARD.md': base_path / 'metricas' / 'DASHBOARD.md',
        'TODO_Sprint_Atual.md': base_path / 'tarefas' / 'TODO_Sprint_Atual.md',
        'BACKLOG.md': base_path / 'tarefas' / 'BACKLOG.md',
        'CONCLUIDAS.md': base_path / 'tarefas' / 'CONCLUIDAS.md',
    }

    return {
        name: path.exists() and path.is_file()
        for name, path in required_files.items()
    }

def generate_validation_report(base_path: Path) -> str:
    """
    Gera relatório completo de validação do projeto.
    """
    report = []
    report.append("# RELATÓRIO DE VALIDAÇÃO - Projeto KabaK\n")

    # Validar estrutura de pastas
    report.append("## 📁 Estrutura de Pastas\n")
    folders = validate_structure_folders(base_path)
    for name, exists in folders.items():
        status = "✅" if exists else "❌"
        report.append(f"{status} `{name}/`")

    # Validar arquivos obrigatórios
    report.append("\n## 📄 Arquivos Obrigatórios\n")
    files = validate_required_files(base_path)
    for name, exists in files.items():
        status = "✅" if exists else "❌"
        report.append(f"{status} `{name}`")

    # Validar nomenclatura de arquivos existentes
    report.append("\n## 📝 Nomenclatura de Arquivos\n")
    if base_path.exists():
        for folder in base_path.rglob('*.md'):
            if folder.is_file():
                is_valid, message = validate_filename(folder.name)
                status = "✅" if is_valid else "⚠️"
                report.append(f"{status} `{folder.name}`: {message}")

    return '\n'.join(report)

# Exemplo de uso
if __name__ == '__main__':
    # Testes de nomenclatura
    test_files = [
        'RESUMO_EXECUTIVO_REUNIAO_SANSOM_14JAN2026.md',  # Válido
        'resumo executivo.md',  # Inválido (espaços)
        'STATUS_ATUAL.md',  # Válido
        'dashboard.md',  # Inválido (não maiúsculo)
        'TODO_Sprint_Atual.md',  # Válido
    ]

    print("=== Teste de Validação de Nomes ===\n")
    for filename in test_files:
        valid, msg = validate_filename(filename)
        status = "✅" if valid else "❌"
        print(f"{status} {filename}")
        print(f"   {msg}\n")

    # Teste de frontmatter
    sample_content = """---
criado: 2026-01-14T10:00:00-03:00
atualizado: 2026-01-14T15:30:00-03:00
tipo: resumo_executivo
---

# Conteúdo do documento
"""

    print("\n=== Teste de Validação de Frontmatter ===\n")
    valid, issues = validate_frontmatter(sample_content)
    if valid:
        print("✅ Frontmatter válido")
    else:
        print("❌ Frontmatter inválido:")
        for issue in issues:
            print(f"   - {issue}")
