import os
from pathlib import Path

def count_files_recursive(directory):
    """Counts all files in a directory recursively."""
    path = Path(directory)
    if not path.exists():
        return 0
    return sum(1 for _ in path.rglob('*') if _.is_file())

def count_folders_recursive(directory):
    """Counts all folders in a directory recursively."""
    path = Path(directory)
    if not path.exists():
        return 0
    return sum(1 for _ in path.rglob('*') if _.is_dir())

def count_immediate_subfolders(directory):
    """Counts immediate subfolders (for projects/courses)."""
    path = Path(directory)
    if not path.exists():
        return 0
    return sum(1 for _ in path.iterdir() if _.is_dir())

def count_files_in_dir(directory):
    """Counts files in a specific directory (non-recursive)."""
    path = Path(directory)
    if not path.exists():
        return 0
    return sum(1 for _ in path.iterdir() if _.is_file())

def count_mocs(directory):
    """Counts MOC files (starting with _MOC or MOC_)."""
    path = Path(directory)
    if not path.exists():
        return 0
    return sum(1 for _ in path.rglob('*.md') if _.name.startswith('MOC_') or _.name.startswith('_MOC'))

def count_skills(directory):
    """Counts skill folders (files named skill.md or config.json)."""
    path = Path(directory)
    if not path.exists():
        return 0
    # Assuming each folder in skills dir is a skill
    return count_immediate_subfolders(directory)

def collect_metrics(vault_root):
    """Collects all metrics from the vault."""
    vault_path = Path(vault_root)
    
    metrics = {
        # Arquivos e Pastas
        "total_files": count_files_recursive(vault_path),
        "total_folders": count_folders_recursive(vault_path),

        # Projetos
        "projetos_ativos": count_immediate_subfolders(vault_path / "02_PROJETOS"),

        # Aprendizado
        "cursos_ativos": count_immediate_subfolders(vault_path / "03_APRENDIZADO"),

        # Conhecimento (Categorias principais em 01)
        "areas_conhecimento": count_immediate_subfolders(vault_path / "01_CONHECIMENTO"),

        # Sistema
        "mocs_total": count_mocs(vault_path / "00_SISTEMA/MOCs") + count_mocs(vault_path / "01_CONHECIMENTO") + count_mocs(vault_path / "02_PROJETOS") + count_mocs(vault_path / "03_APRENDIZADO") + count_mocs(vault_path / "04_RECURSOS") + count_mocs(vault_path / "05_PESSOAL"), # Approximate
        
        # Recursos
        "templates": count_files_in_dir(vault_path / "04_RECURSOS/TEMPLATES"),
        "prompts": count_files_in_dir(vault_path / "04_RECURSOS/PROMPTS"),
        "checklists": count_files_in_dir(vault_path / "04_RECURSOS/CHECKLISTS"),
        "guias": count_files_in_dir(vault_path / "04_RECURSOS/GUIAS"),

        # Comandos e Skills
        "skills_claude": count_skills(vault_path / ".claude/skills"), # Assuming structure
        "skills_gemini": count_skills(vault_path / ".gemini/skills"),
        
        # Phase Progress (Calculated)
        "fases": {}
    }
    
    # Total commands estimate (skills + core commands)
    # Core agents (9) + Tools (8) + Contexts (2) -> approx from STATUS_VAULT
    metrics["comandos_total"] = metrics["skills_claude"] + metrics["skills_gemini"] + 11 # Baseline
    
    # Calculate Phase Progress
    metrics["fases"] = {
        1: 100 if metrics["cursos_ativos"] > 0 else 0, # Fase 1: Aprendizado
        2: 100 if (vault_path / "00_SISTEMA").exists() else 0, # Fase 2: Estrutura Base
        3: 100 if (vault_path / ".gemini").exists() else 0, # Fase 3: Gemini CLI
        4: 100 if metrics["total_files"] > 1000 else int(metrics["total_files"] / 10), # Fase 4: Migração (heuristic)
        5: int((metrics["skills_gemini"] / 7) * 100) if metrics["skills_gemini"] < 7 else 100, # Fase 5: Automação (Target 7 skills)
        6: 100 if (vault_path / "00_SISTEMA/PADROES").exists() else 0, # Fase 6: Arquitetura
        7: 100 if (vault_path / "00_SISTEMA/PROTOCOLOS/PROTOCOLO_REVISAO_SEMANAL.md").exists() else 0 # Fase 7: Manutenção
    }
    
    # Correction for known completed phases based on STATUS_VAULT history
    # We want to enable automation but respect current state which says Fases 1-6 are 100%
    # We will trust the heuristic but clamp to 100 if it looks like it's done or use logic
    # Actually, let's keep the logic simple and relevant.
    
    return metrics
