#!/usr/bin/env python3
"""
update_moc.py - Atualizador de MOC KabaK v2.0

Atualiza automaticamente o _MOC_KabaK.md apos criar novos arquivos.

Uso:
    python update_moc.py "02_PROJETOS/KabaK/docs/reunioes/RESUMO_REUNIAO_EXEMPLO.md"
    python update_moc.py --scan  # Escaneia todos arquivos e sugere atualizacoes
"""

import sys
import os
import re
from pathlib import Path
from datetime import datetime

# Configuracao
KABAK_ROOT = "02_PROJETOS/KabaK"
MOC_FILE = "_MOC_KabaK.md"

# Mapeamento de pastas para secoes do MOC
FOLDER_TO_SECTION = {
    "docs/reunioes": "/docs/reunioes (Reunioes)",
    "docs/financeiro": "/docs/financeiro (Planilhas e Numeros)",
    "docs/projetos": "/docs/projetos (Projetos Especificos)",
    "docs/pesquisas": "/docs/pesquisas (Pesquisas)",
    "docs/contratos": "/docs/contratos (Contratos)",
    "docs/suprimentos": "/docs/suprimentos (Cadeia de Suprimentos)",
    "docs": "/docs (Documentacao Geral)",
    "planejamento": "/planejamento (Estrategia & Financeiro)",
    "tarefas": "/tarefas (Gestao de Tarefas)",
    "metricas": "/metricas (KPIs e Dashboards)",
    "metricas/RELATORIOS": "/metricas (KPIs e Dashboards)",
    "checkpoints": "/checkpoints (Snapshots)",
    "recursos": "/recursos (Assets e Referencias)",
    "scripts": "/scripts (Automacoes Python)",
}

# Tipos de arquivo e descricoes
FILE_TYPES = {
    "RESUMO_REUNIAO_": "Resumo reuniao",
    "RESUMO_EXECUTIVO_": "Resumo executivo",
    "RESUMO_FINANCEIRO_": "Resumo financeiro",
    "RESUMO_LIGACAO_": "Resumo ligacao",
    "RESUMO_RETORNO_": "Resumo retorno",
    "RESUMO_PARCERIA_": "Resumo parceria",
    "BRIEFING_": "Briefing",
    "PLANO_": "Plano de acao",
    "PLANILHA_": "Planilha",
    "CHECKLIST_": "Checklist",
    "STATUS_": "Status",
    "TRANSCRICAO_": "Transcricao",
    "ANALISE_": "Analise",
    "DOSSIE_": "Dossie",
    "PROPOSTA_": "Proposta",
    "COMUNICADO_": "Comunicado",
    "MENSAGEM_": "Mensagem",
    "PESQUISA_": "Pesquisa",
    "AUDITORIA_": "Auditoria",
    "CHECKPOINT_": "Checkpoint",
    "RELATORIO_": "Relatorio",
}


def get_file_type(filename: str) -> str:
    """Retorna o tipo do arquivo baseado no prefixo."""
    for prefix, file_type in FILE_TYPES.items():
        if filename.startswith(prefix):
            return file_type
    return "Documento"


def get_section_for_path(relative_path: str) -> str:
    """Retorna a secao do MOC para um caminho relativo."""
    path_parts = relative_path.replace("\\", "/")

    # Tentar match mais especifico primeiro
    for folder, section in sorted(FOLDER_TO_SECTION.items(), key=lambda x: -len(x[0])):
        if folder in path_parts:
            return section

    return "/docs (Documentacao Geral)"  # Default


def extract_date_from_filename(filename: str) -> str:
    """Extrai data do nome do arquivo (formato DDMMMYYYY)."""
    match = re.search(r'(\d{2}[A-Z]{3}\d{4})', filename)
    if match:
        return match.group(1)
    return ""


def generate_moc_entry(filepath: str) -> dict:
    """Gera uma entrada para o MOC."""
    path = Path(filepath)
    filename = path.name

    # Caminho relativo ao projeto KabaK
    full_path = str(path).replace("\\", "/")
    if KABAK_ROOT in full_path:
        relative_to_kabak = full_path.split(KABAK_ROOT + "/")[-1]
    else:
        relative_to_kabak = filename

    # Remover extensao para link wiki
    name_without_ext = filename.replace(".md", "")

    # Determinar tipo e secao
    file_type = get_file_type(filename)
    section = get_section_for_path(relative_to_kabak)
    date = extract_date_from_filename(filename)

    # Gerar descricao
    description = file_type
    if date:
        # Converter DDMMMYYYY para DD/MMM
        try:
            dt = datetime.strptime(date, "%d%b%Y")
            description += f" {dt.strftime('%d/%b')}"
        except:
            description += f" {date}"

    return {
        "filename": filename,
        "link": f"[[{relative_to_kabak.replace('.md', '')}]]",
        "description": description,
        "section": section,
        "relative_path": relative_to_kabak,
    }


def read_moc(moc_path: str) -> str:
    """Le o conteudo do MOC."""
    try:
        with open(moc_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def check_if_in_moc(moc_content: str, filename: str) -> bool:
    """Verifica se o arquivo ja esta no MOC."""
    # Verificar por diferentes formatos de link
    patterns = [
        filename,
        filename.replace(".md", ""),
        f"[[{filename}]]",
        f"[[{filename.replace('.md', '')}]]",
    ]

    for pattern in patterns:
        if pattern in moc_content:
            return True
    return False


def suggest_moc_update(entry: dict) -> str:
    """Sugere a linha a ser adicionada ao MOC."""
    return f"| {entry['link']} | {entry['description']} | Novo |"


def find_section_in_moc(moc_content: str, section: str) -> int:
    """Encontra a posicao da secao no MOC."""
    # Procurar por headers que contenham a pasta
    section_patterns = [
        f"### {section}",
        f"### /{section}",
        section.split("(")[0].strip(),
    ]

    lines = moc_content.split("\n")
    for i, line in enumerate(lines):
        for pattern in section_patterns:
            if pattern.lower() in line.lower():
                return i

    return -1


def scan_kabak_folder(kabak_path: str) -> list:
    """Escaneia a pasta KabaK e retorna arquivos nao no MOC."""
    moc_path = os.path.join(kabak_path, MOC_FILE)
    moc_content = read_moc(moc_path)

    missing_files = []

    # Pastas para escanear
    scan_folders = [
        "docs", "docs/reunioes", "docs/financeiro", "docs/projetos",
        "docs/pesquisas", "docs/contratos", "docs/suprimentos",
        "planejamento", "tarefas", "metricas", "checkpoints", "recursos"
    ]

    for folder in scan_folders:
        folder_path = os.path.join(kabak_path, folder)
        if os.path.exists(folder_path):
            for filename in os.listdir(folder_path):
                if filename.endswith(".md") and not filename.startswith("_"):
                    filepath = os.path.join(folder_path, filename)
                    if not check_if_in_moc(moc_content, filename):
                        entry = generate_moc_entry(filepath)
                        missing_files.append(entry)

    return missing_files


def update_single_file(filepath: str, kabak_path: str) -> str:
    """Processa um unico arquivo e retorna a sugestao de atualizacao."""
    moc_path = os.path.join(kabak_path, MOC_FILE)
    moc_content = read_moc(moc_path)

    filename = os.path.basename(filepath)

    if check_if_in_moc(moc_content, filename):
        return f"INFO: {filename} ja esta no MOC"

    entry = generate_moc_entry(filepath)
    suggestion = suggest_moc_update(entry)

    output = []
    output.append(f"NOVO ARQUIVO: {filename}")
    output.append(f"SECAO: {entry['section']}")
    output.append(f"ADICIONAR:")
    output.append(suggestion)
    output.append("")
    output.append("Para adicionar manualmente:")
    output.append(f"1. Abra {MOC_FILE}")
    output.append(f"2. Encontre a secao '{entry['section']}'")
    output.append(f"3. Adicione a linha acima na tabela")

    return "\n".join(output)


def main():
    # Determinar caminho base do KabaK
    cwd = os.getcwd()
    if KABAK_ROOT in cwd:
        kabak_path = cwd.split(KABAK_ROOT)[0] + KABAK_ROOT
    else:
        # Assumir estrutura padrao
        kabak_path = os.path.join(cwd, KABAK_ROOT)
        if not os.path.exists(kabak_path):
            # Tentar caminho absoluto comum
            kabak_path = "C:/Users/gasse/OneDrive/Meu_Segundo_Cerebro/02_PROJETOS/KabaK"

    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    if sys.argv[1] == "--scan":
        # Modo scan: listar todos arquivos faltando no MOC
        print("Escaneando pasta KabaK...")
        print(f"Caminho: {kabak_path}")
        print("-" * 50)

        missing = scan_kabak_folder(kabak_path)

        if not missing:
            print("OK: Todos os arquivos ja estao no MOC!")
        else:
            print(f"ARQUIVOS FALTANDO NO MOC: {len(missing)}")
            print("-" * 50)

            # Agrupar por secao
            by_section = {}
            for entry in missing:
                section = entry["section"]
                if section not in by_section:
                    by_section[section] = []
                by_section[section].append(entry)

            for section, entries in sorted(by_section.items()):
                print(f"\n### {section}")
                for entry in entries:
                    print(suggest_moc_update(entry))
    else:
        # Modo single file
        filepath = sys.argv[1]
        result = update_single_file(filepath, kabak_path)
        print(result)


if __name__ == "__main__":
    main()
