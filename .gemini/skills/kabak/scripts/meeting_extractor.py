#!/usr/bin/env python3
"""
KabaK Meeting Extractor

Extrai action items, decisões e próximos passos de transcrições de reuniões.
Usado pelo workflow Meeting Processor da skill /kabak.
"""

import re
from datetime import datetime
from typing import List, Dict, Tuple

def extract_action_items(text: str) -> List[Dict[str, str]]:
    """
    Extrai action items do texto da reunião.

    Procura por padrões como:
    - "X vai fazer Y"
    - "responsável: X"
    - "prazo: data"
    - verbos de ação (fazer, criar, agendar, etc)
    """
    action_items = []

    # Padrões comuns de action items
    action_verbs = [
        'fazer', 'criar', 'agendar', 'enviar', 'preparar', 'revisar',
        'validar', 'confirmar', 'definir', 'estruturar', 'elaborar',
        'solicitar', 'providenciar', 'organizar', 'fechar', 'contratar'
    ]

    # Buscar responsáveis e ações
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line_lower = line.lower()

        # Padrão: "Responsável: Nome - Ação"
        if 'responsável:' in line_lower or 'responsavel:' in line_lower:
            parts = line.split(':', 1)
            if len(parts) > 1:
                responsible = parts[1].split('-')[0].strip()
                action = parts[1].split('-')[1].strip() if '-' in parts[1] else ''
                action_items.append({
                    'responsible': responsible,
                    'action': action,
                    'line_number': i + 1
                })

        # Padrão: "Nome vai/precisa [verbo]"
        for verb in action_verbs:
            pattern = rf'(\w+)\s+(vai|precisa)\s+{verb}'
            matches = re.finditer(pattern, line_lower)
            for match in matches:
                action_items.append({
                    'responsible': match.group(1).capitalize(),
                    'action': line.strip(),
                    'line_number': i + 1
                })

    return action_items

def extract_decisions(text: str) -> List[Dict[str, str]]:
    """
    Extrai decisões tomadas na reunião.

    Procura por palavras-chave:
    - "decisão", "acordado", "definido", "aprovado"
    """
    decisions = []

    decision_keywords = ['decisão', 'decisao', 'acordado', 'definido', 'aprovado', 'firmado']

    lines = text.split('\n')
    for i, line in enumerate(lines):
        line_lower = line.lower()

        if any(keyword in line_lower for keyword in decision_keywords):
            # Pegar contexto (linha atual + próximas 2 linhas)
            context = '\n'.join(lines[i:min(i+3, len(lines))])
            decisions.append({
                'decision': line.strip(),
                'context': context,
                'line_number': i + 1
            })

    return decisions

def extract_deadlines(text: str) -> List[Dict[str, str]]:
    """
    Extrai prazos mencionados na reunião.

    Procura por padrões de data:
    - DD/MM/YYYY
    - até DD/MM
    - prazo: data
    """
    deadlines = []

    # Padrões de data
    date_patterns = [
        r'\d{1,2}/\d{1,2}/\d{2,4}',  # DD/MM/YY ou DD/MM/YYYY
        r'até\s+\d{1,2}/\d{1,2}',     # até DD/MM
        r'prazo:?\s*\d{1,2}/\d{1,2}',  # prazo: DD/MM
    ]

    lines = text.split('\n')
    for i, line in enumerate(lines):
        for pattern in date_patterns:
            matches = re.finditer(pattern, line, re.IGNORECASE)
            for match in matches:
                deadlines.append({
                    'deadline': match.group(0),
                    'context': line.strip(),
                    'line_number': i + 1
                })

    return deadlines

def extract_participants(text: str) -> List[str]:
    """
    Extrai participantes da reunião.

    Procura por:
    - "Participantes:"
    - Nomes conhecidos do projeto KabaK
    """
    participants = []

    # Nomes conhecidos do projeto
    known_names = ['Sansom', 'Jean', 'Gassen', 'Kris', 'Carol', 'Dr. Alexandre']

    # Procurar seção de participantes
    if 'participantes:' in text.lower():
        # Extrair linha com participantes
        for line in text.split('\n'):
            if 'participantes:' in line.lower():
                parts = line.split(':', 1)
                if len(parts) > 1:
                    names = [n.strip() for n in parts[1].split(',')]
                    participants.extend(names)

    # Procurar nomes conhecidos no texto
    for name in known_names:
        if name in text and name not in participants:
            participants.append(name)

    return list(set(participants))  # Remove duplicatas

def generate_summary(action_items: List[Dict], decisions: List[Dict],
                    deadlines: List[Dict], participants: List[str]) -> str:
    """
    Gera resumo formatado dos itens extraídos.
    """
    summary = []

    summary.append("# EXTRAÇÃO AUTOMÁTICA - Resumo Reunião\n")
    summary.append(f"**Data Extração:** {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")

    if participants:
        summary.append("\n## 👥 Participantes Identificados\n")
        for p in participants:
            summary.append(f"- {p}")

    if decisions:
        summary.append(f"\n## 🎯 Decisões Identificadas ({len(decisions)})\n")
        for i, d in enumerate(decisions, 1):
            summary.append(f"\n{i}. {d['decision']}")
            summary.append(f"   *(Linha {d['line_number']})*")

    if action_items:
        summary.append(f"\n## ✅ Action Items Identificados ({len(action_items)})\n")
        for i, item in enumerate(action_items, 1):
            summary.append(f"\n{i}. **{item['responsible']}:** {item['action']}")
            summary.append(f"   *(Linha {item['line_number']})*")

    if deadlines:
        summary.append(f"\n## ⏱️ Prazos Identificados ({len(deadlines)})\n")
        for i, d in enumerate(deadlines, 1):
            summary.append(f"\n{i}. {d['deadline']}: {d['context']}")
            summary.append(f"   *(Linha {d['line_number']})*")

    summary.append("\n\n---")
    summary.append("\n*Extração automática via /kabak skill - Revisar e validar manualmente*")

    return '\n'.join(summary)

def process_meeting_text(text: str) -> Dict:
    """
    Processa texto completo da reunião e retorna dados estruturados.
    """
    return {
        'action_items': extract_action_items(text),
        'decisions': extract_decisions(text),
        'deadlines': extract_deadlines(text),
        'participants': extract_participants(text),
        'summary': generate_summary(
            extract_action_items(text),
            extract_decisions(text),
            extract_deadlines(text),
            extract_participants(text)
        )
    }

if __name__ == '__main__':
    # Exemplo de uso
    sample_text = """
    Participantes: Sansom, Gassen, Kris, Jean

    Decisão: Sociedade 51% Sansom / 49% Jean
    Sansom vai pedir tecido China até 21/Jan
    Gassen precisa agendar Dr. Alexandre
    Prazo: 28/Jan para contratos
    """

    result = process_meeting_text(sample_text)
    print(result['summary'])
