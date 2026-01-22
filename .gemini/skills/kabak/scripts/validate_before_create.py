#!/usr/bin/env python3
"""
validate_before_create.py - Validador de arquivos KabaK v2.0

Valida nome, localizacao e frontmatter ANTES de criar arquivos.
Baseado em: references/nomenclatura_kabak.md

Uso:
    python validate_before_create.py "RESUMO_REUNIAO_EXEMPLO_22JAN2026.md" "docs/reunioes"
    python validate_before_create.py --check-existing "02_PROJETOS/KabaK/docs/arquivo.md"
"""

import sys
import re
import os
from pathlib import Path
from datetime import datetime

# Configuracao
KABAK_ROOT = "02_PROJETOS/KabaK"
MAX_FILENAME_LENGTH = 60

# Prefixos validos e suas localizacoes esperadas
PREFIXES = {
    "RESUMO_REUNIAO_": ["docs/reunioes"],
    "RESUMO_EXECUTIVO_": ["docs/reunioes"],
    "RESUMO_FINANCEIRO_": ["docs/financeiro"],
    "RESUMO_LIGACAO_": ["docs/reunioes"],
    "RESUMO_RETORNO_": ["docs/reunioes"],
    "RESUMO_PARCERIA_": ["docs/reunioes"],
    "BRIEFING_": ["docs"],
    "PLANO_": ["planejamento"],
    "PLANILHA_": ["planejamento"],
    "CHECKLIST_": ["docs"],
    "STATUS_": [""],  # raiz
    "TRANSCRICAO_": ["docs"],
    "ANALISE_": ["docs"],
    "DOSSIE_": ["docs"],
    "PROPOSTA_": ["planejamento"],
    "COMUNICADO_": ["docs/reunioes"],
    "MENSAGEM_": ["docs/reunioes"],
    "PAUTA_": ["docs/reunioes"],
    "PESQUISA_": ["docs", "docs/pesquisas"],
    "AUDITORIA_": ["docs"],
    "TODO_": ["tarefas"],
    "DASHBOARD": ["metricas"],
    "README": [""],  # qualquer pasta
    "VALORES_OFICIAIS": [""],  # raiz
    "_MOC_": [""],  # raiz
    "CHECKPOINT_": ["checkpoints"],
    "RELATORIO_": ["metricas/RELATORIOS"],
    "SUMARIO_": ["metricas/RELATORIOS"],
    "PO_": ["docs/contratos"],
    "PROJETO_": ["docs/projetos"],
}

# Arquivos unicos (nao duplicar)
UNIQUE_FILES = [
    "STATUS_ATUAL.md",
    "VALORES_OFICIAIS.md",
    "_MOC_KabaK.md",
    "DASHBOARD.md",
    "TODO_Sprint_Atual.md",
    "BACKLOG.md",
    "CONCLUIDAS.md",
    "README.md",
]

# Regex para data DDMMMYYYY
DATE_PATTERN = r'\d{2}[A-Z]{3}\d{4}'


class ValidationResult:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.suggestions = []

    def add_error(self, msg):
        self.errors.append(f"ERRO: {msg}")

    def add_warning(self, msg):
        self.warnings.append(f"AVISO: {msg}")

    def add_suggestion(self, msg):
        self.suggestions.append(f"SUGESTAO: {msg}")

    def is_valid(self):
        return len(self.errors) == 0

    def __str__(self):
        lines = []
        if self.errors:
            lines.extend(self.errors)
        if self.warnings:
            lines.extend(self.warnings)
        if self.suggestions:
            lines.extend(self.suggestions)
        if self.is_valid():
            lines.insert(0, "OK: Validacao passou!")
        return "\n".join(lines) if lines else "OK: Validacao passou!"


def validate_prefix(filename: str, result: ValidationResult) -> str | None:
    """Valida se o prefixo e valido e retorna o prefixo encontrado."""
    for prefix in sorted(PREFIXES.keys(), key=len, reverse=True):
        if filename.startswith(prefix):
            return prefix

    # Verificar prefixo minusculo (erro comum)
    lower_filename = filename.lower()
    for prefix in PREFIXES.keys():
        if lower_filename.startswith(prefix.lower()):
            result.add_error(f"Prefixo deve ser UPPERCASE: '{prefix}' (encontrado minusculo)")
            return None

    result.add_error(f"Prefixo invalido. Prefixos validos: {', '.join(sorted(PREFIXES.keys()))}")
    return None


def validate_location(prefix: str, location: str, result: ValidationResult):
    """Valida se a localizacao e correta para o prefixo."""
    expected_locations = PREFIXES.get(prefix, [])

    # Normalizar location (remover KABAK_ROOT se presente)
    normalized_loc = location.replace("\\", "/")
    if KABAK_ROOT in normalized_loc:
        normalized_loc = normalized_loc.split(KABAK_ROOT)[-1].lstrip("/")

    # README pode estar em qualquer lugar
    if prefix == "README":
        return

    if expected_locations == [""]:
        # Deve estar na raiz
        if normalized_loc and normalized_loc not in ["", "."]:
            result.add_warning(f"'{prefix}' geralmente fica na raiz do projeto, nao em '{normalized_loc}'")
    elif normalized_loc not in expected_locations:
        result.add_error(f"Localizacao incorreta. '{prefix}' deve estar em: {expected_locations}")
        result.add_suggestion(f"Mova para: {KABAK_ROOT}/{expected_locations[0]}/")


def validate_filename_format(filename: str, result: ValidationResult):
    """Valida formato do nome do arquivo."""
    name_without_ext = filename.replace(".md", "")

    # Verificar tamanho
    if len(name_without_ext) > MAX_FILENAME_LENGTH:
        result.add_error(f"Nome muito longo: {len(name_without_ext)} chars (max {MAX_FILENAME_LENGTH})")

    # Verificar espacos
    if " " in filename:
        result.add_error("Nome contem espacos. Use underscores (_)")
        result.add_suggestion(f"Renomear para: {filename.replace(' ', '_')}")

    # Verificar hifens
    if "-" in name_without_ext and not re.search(r'\d{2}-\d{2}', name_without_ext):
        result.add_warning("Hifens encontrados. Prefira underscores (_)")

    # Verificar data no formato errado
    wrong_date_patterns = [
        (r'\d{2}-\d{2}-\d{4}', "DD-MM-YYYY"),
        (r'\d{4}-\d{2}-\d{2}', "YYYY-MM-DD"),
        (r'\d{2}/\d{2}/\d{4}', "DD/MM/YYYY"),
    ]
    for pattern, format_name in wrong_date_patterns:
        if re.search(pattern, name_without_ext):
            result.add_error(f"Data em formato errado ({format_name}). Use DDMMMYYYY (ex: 21JAN2026)")


def validate_date_format(filename: str, result: ValidationResult):
    """Valida se a data esta no formato DDMMMYYYY."""
    match = re.search(DATE_PATTERN, filename)
    if match:
        date_str = match.group()
        try:
            # Validar se a data e real
            datetime.strptime(date_str, "%d%b%Y")
        except ValueError:
            result.add_error(f"Data invalida: {date_str}. Verificar mes (JAN, FEV, MAR...)")


def validate_unique_file(filename: str, location: str, result: ValidationResult):
    """Verifica se e um arquivo unico que ja existe."""
    if filename in UNIQUE_FILES:
        result.add_warning(f"'{filename}' e arquivo UNICO. Se ja existe, ATUALIZE em vez de criar novo.")


def check_file_exists(filepath: str, result: ValidationResult):
    """Verifica se o arquivo ja existe."""
    if os.path.exists(filepath):
        result.add_warning(f"Arquivo ja existe: {filepath}")
        result.add_suggestion("Se for o mesmo conteudo, ATUALIZE o existente em vez de criar duplicata.")


def validate_frontmatter(content: str, result: ValidationResult):
    """Valida frontmatter de um arquivo existente."""
    if not content.startswith("---"):
        result.add_warning("Arquivo nao tem frontmatter YAML")
        return

    # Extrair frontmatter
    parts = content.split("---", 2)
    if len(parts) < 3:
        result.add_error("Frontmatter mal formatado")
        return

    frontmatter = parts[1]

    # Verificar campos EN vs PT
    if "created:" in frontmatter and "criado:" not in frontmatter:
        result.add_error("Usar 'criado:' em vez de 'created:' (padrao PT-BR)")

    if "updated:" in frontmatter and "atualizado:" not in frontmatter:
        result.add_error("Usar 'atualizado:' em vez de 'updated:' (padrao PT-BR)")

    # Verificar campos obrigatorios
    required_fields = ["criado", "atualizado", "tipo", "status"]
    for field in required_fields:
        if f"{field}:" not in frontmatter:
            result.add_warning(f"Campo '{field}' ausente no frontmatter")


def validate_new_file(filename: str, location: str) -> ValidationResult:
    """Valida um novo arquivo antes de criar."""
    result = ValidationResult()

    # 1. Validar prefixo
    prefix = validate_prefix(filename, result)

    # 2. Validar localizacao (se prefixo valido)
    if prefix:
        validate_location(prefix, location, result)

    # 3. Validar formato do nome
    validate_filename_format(filename, result)

    # 4. Validar formato da data
    validate_date_format(filename, result)

    # 5. Verificar se e arquivo unico
    validate_unique_file(filename, location, result)

    # 6. Verificar se ja existe
    full_path = os.path.join(location, filename)
    check_file_exists(full_path, result)

    return result


def validate_existing_file(filepath: str) -> ValidationResult:
    """Valida um arquivo existente."""
    result = ValidationResult()

    path = Path(filepath)
    filename = path.name
    location = str(path.parent)

    # Validacoes de nome
    prefix = validate_prefix(filename, result)
    if prefix:
        validate_location(prefix, location, result)
    validate_filename_format(filename, result)
    validate_date_format(filename, result)

    # Validar frontmatter se arquivo existe
    if path.exists():
        try:
            content = path.read_text(encoding="utf-8")
            validate_frontmatter(content, result)
        except Exception as e:
            result.add_error(f"Erro ao ler arquivo: {e}")
    else:
        result.add_error(f"Arquivo nao encontrado: {filepath}")

    return result


def suggest_correct_name(filename: str) -> str:
    """Sugere nome corrigido."""
    # Corrigir espacos
    corrected = filename.replace(" ", "_")

    # Corrigir hifens em datas
    corrected = re.sub(r'(\d{2})-(\d{2})-(\d{4})', r'\1\2\3', corrected)

    return corrected


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    if sys.argv[1] == "--check-existing" and len(sys.argv) >= 3:
        # Validar arquivo existente
        filepath = sys.argv[2]
        result = validate_existing_file(filepath)
    elif len(sys.argv) >= 3:
        # Validar novo arquivo
        filename = sys.argv[1]
        location = sys.argv[2]
        result = validate_new_file(filename, location)
    else:
        # Validar apenas nome
        filename = sys.argv[1]
        result = validate_new_file(filename, "")

    print(result)
    sys.exit(0 if result.is_valid() else 1)


if __name__ == "__main__":
    main()
