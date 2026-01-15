#!/usr/bin/env python3
"""
KabaK Dashboard Updater

Atualiza métricas no DASHBOARD.md de forma programática.
Usado pelo workflow Project Manager da skill /kabak.
"""

import re
from datetime import datetime
from typing import Dict, Optional

def update_metric_value(dashboard_content: str, metric_name: str, new_value: str) -> str:
    """
    Atualiza valor de uma métrica específica no dashboard.

    Args:
        dashboard_content: Conteúdo completo do DASHBOARD.md
        metric_name: Nome da métrica (ex: "Progresso", "Faturamento")
        new_value: Novo valor (ex: "50%", "R$ 1.5M")

    Returns:
        Conteúdo atualizado
    """
    # Padrão: | Métrica | Valor_Antigo | Meta | Status |
    pattern = rf'(\|\s*{re.escape(metric_name)}\s*\|)(.*?)(\|.*?\|.*?\|)'

    def replace_value(match):
        return f"{match.group(1)} {new_value} {match.group(3)}"

    updated = re.sub(pattern, replace_value, dashboard_content)

    return updated

def update_status_indicator(dashboard_content: str, metric_name: str, status: str) -> str:
    """
    Atualiza indicador de status (🔴🟡🟢) de uma métrica.

    Args:
        status: '🔴', '🟡', ou '🟢'
    """
    # Mapa de status
    status_map = {
        'critico': '🔴',
        'atencao': '🟡',
        'ok': '🟢',
        'red': '🔴',
        'yellow': '🟡',
        'green': '🟢'
    }

    status_emoji = status_map.get(status.lower(), status)

    # Padrão: | Métrica | Valor | Meta | Status_Antigo |
    pattern = rf'(\|\s*{re.escape(metric_name)}\s*\|.*?\|.*?\|)\s*[🔴🟡🟢]?\s*(\|)'

    def replace_status(match):
        return f"{match.group(1)} {status_emoji} {match.group(2)}"

    updated = re.sub(pattern, replace_status, dashboard_content)

    return updated

def update_progress_bar(dashboard_content: str, section: str, percentage: int) -> str:
    """
    Atualiza barra de progresso visual (████░░░░░░).

    Args:
        section: Nome da seção/fase
        percentage: 0-100
    """
    # Criar barra de progresso
    filled = int(percentage / 10)  # 10 blocos no total
    empty = 10 - filled
    progress_bar = '█' * filled + '░' * empty

    # Padrão: Progresso: ████████░░ 80%
    pattern = rf'(Progresso:\s*)[█░]{{10}}\s*\d+%'

    def replace_progress(match):
        return f"{match.group(1)}{progress_bar} {percentage}%"

    updated = re.sub(pattern, replace_progress, dashboard_content)

    return updated

def update_alert_table(dashboard_content: str, alerts: list[Dict[str, str]]) -> str:
    """
    Atualiza tabela de alertas completamente.

    Args:
        alerts: Lista de dicts com 'alerta', 'severidade', 'acao'
    """
    # Encontrar tabela de alertas
    alert_section_start = dashboard_content.find('## 🚨 Alertas')

    if alert_section_start == -1:
        return dashboard_content

    # Encontrar próxima seção (próximo ##)
    next_section = dashboard_content.find('\n## ', alert_section_start + 1)
    if next_section == -1:
        next_section = len(dashboard_content)

    # Construir nova tabela
    new_table = []
    new_table.append('\n| Alerta | Severidade | Ação |')
    new_table.append('|--------|------------|------|')

    for alert in alerts:
        severity_emoji = {
            'critico': '🔴 CRÍTICO',
            'medio': '🟡 MÉDIO',
            'baixo': '🟢 BAIXO'
        }.get(alert['severidade'].lower(), alert['severidade'])

        new_table.append(f"| {alert['alerta']} | {severity_emoji} | {alert['acao']} |")

    new_table.append('\n')

    # Substituir seção
    before = dashboard_content[:alert_section_start]
    header = '## 🚨 Alertas\n'
    after = dashboard_content[next_section:]

    return before + header + '\n'.join(new_table) + after

def update_timestamp(dashboard_content: str) -> str:
    """
    Atualiza timestamp de última atualização.
    """
    now = datetime.now().strftime('%d/%m/%Y')

    # Padrão: **Última atualização:** DD/MM/YYYY
    pattern = r'(\*\*Última atualização:\*\*\s*)\d{1,2}/\d{1,2}/\d{2,4}'

    updated = re.sub(pattern, rf'\1{now}', dashboard_content)

    return updated

def calculate_status(current: float, target: float) -> str:
    """
    Calcula status baseado em atual vs meta.

    Returns: '🟢', '🟡', ou '🔴'
    """
    percentage = (current / target) * 100 if target > 0 else 0

    if percentage >= 90:
        return '🟢'
    elif percentage >= 70:
        return '🟡'
    else:
        return '🔴'

# Exemplo de uso
if __name__ == '__main__':
    sample_dashboard = """
# DASHBOARD - KabaK

**Última atualização:** 14/01/2026

## 📊 KPIs Principais

| Métrica | Atual | Meta | Status |
|---------|-------|------|--------|
| Progresso | 45% | 100% | 🟡 |
| Contratos Assinados | 0/3 | 3 | 🔴 |

Progresso: ████░░░░░░ 40%

## 🚨 Alertas

| Alerta | Severidade | Ação |
|--------|------------|------|
| Tecido não pedido | 🔴 CRÍTICO | Sansom pedir URGENTE |
"""

    # Atualizar progresso
    updated = update_metric_value(sample_dashboard, 'Progresso', '50%')
    updated = update_progress_bar(updated, 'Fase 1', 50)
    updated = update_timestamp(updated)

    print(updated)
