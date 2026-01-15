#!/usr/bin/env python3
"""
KabaK Excel Calculator

Cálculos financeiros padronizados para projeções.
Usado pelo workflow Financial Planner da skill /kabak.
"""

from typing import Dict, List

# Constantes do projeto KabaK
PRODUCT_COST = 48.00  # Custo produto (tecido R$30 + produção R$15 + embalagem R$3)
SALE_PRICE = 129.00   # Preço venda
LOGISTICS_PCT = 0.12  # 12% do preço
GATEWAY_PCT = 0.03    # 3% do preço
TAX_PCT = 0.025       # 2,5% MG

def calculate_unit_margin(price: float = SALE_PRICE, cost: float = PRODUCT_COST) -> Dict[str, float]:
    """
    Calcula margem por unidade vendida.

    Returns:
        Dict com: price, cost, logistics, gateway, tax, gross_margin, margin_pct
    """
    logistics = price * LOGISTICS_PCT
    gateway = price * GATEWAY_PCT
    tax = price * TAX_PCT

    total_cost = cost + logistics + gateway + tax
    gross_margin = price - total_cost
    margin_pct = (gross_margin / price) * 100

    return {
        'price': price,
        'cost': cost,
        'logistics': logistics,
        'gateway': gateway,
        'tax': tax,
        'total_cost': total_cost,
        'gross_margin': gross_margin,
        'margin_pct': margin_pct
    }

def calculate_monthly_projection(units: int, fixed_costs: float = 150000) -> Dict[str, float]:
    """
    Calcula projeção financeira mensal.

    Args:
        units: Quantidade de kits vendidos no mês
        fixed_costs: Custos fixos mensais (marketing, operação, etc)

    Returns:
        Dict com métricas financeiras do mês
    """
    unit_margin = calculate_unit_margin()

    revenue = units * SALE_PRICE
    variable_costs = units * unit_margin['total_cost']
    gross_profit = units * unit_margin['gross_margin']
    net_profit = gross_profit - fixed_costs

    return {
        'units': units,
        'revenue': revenue,
        'variable_costs': variable_costs,
        'fixed_costs': fixed_costs,
        'gross_profit': gross_profit,
        'net_profit': net_profit,
        'margin_pct': (net_profit / revenue * 100) if revenue > 0 else 0
    }

def calculate_annual_projection(monthly_units: List[int], monthly_fixed: List[float] = None) -> Dict:
    """
    Calcula projeção anual mês a mês.

    Args:
        monthly_units: Lista com 12 valores (unidades por mês)
        monthly_fixed: Lista com 12 valores (custos fixos por mês), ou None para usar padrão

    Returns:
        Dict com projeções mensais e totais anuais
    """
    if monthly_fixed is None:
        # Crescimento gradual de custos fixos
        monthly_fixed = [150000] * 3 + [220000] * 3 + [265000] * 6

    monthly_results = []
    cumulative_profit = 0

    for month, (units, fixed) in enumerate(zip(monthly_units, monthly_fixed), 1):
        month_data = calculate_monthly_projection(units, fixed)
        cumulative_profit += month_data['net_profit']

        month_data['month'] = month
        month_data['cumulative_profit'] = cumulative_profit

        monthly_results.append(month_data)

    # Totais anuais
    total_revenue = sum(m['revenue'] for m in monthly_results)
    total_profit = sum(m['net_profit'] for m in monthly_results)
    total_units = sum(m['units'] for m in monthly_results)

    return {
        'monthly': monthly_results,
        'annual': {
            'total_revenue': total_revenue,
            'total_profit': total_profit,
            'total_units': total_units,
            'avg_margin_pct': (total_profit / total_revenue * 100) if total_revenue > 0 else 0
        }
    }

def calculate_roi(investment: float, profit: float) -> Dict[str, float]:
    """
    Calcula ROI e payback.

    Args:
        investment: Investimento total
        profit: Lucro total no período

    Returns:
        Dict com ROI %, payback em meses, múltiplo
    """
    roi_pct = ((profit - investment) / investment) * 100 if investment > 0 else 0
    multiple = profit / investment if investment > 0 else 0

    return {
        'investment': investment,
        'profit': profit,
        'roi_pct': roi_pct,
        'multiple': multiple,
        'net_gain': profit - investment
    }

def calculate_break_even(fixed_costs: float) -> Dict[str, float]:
    """
    Calcula ponto de equilíbrio (break-even).

    Args:
        fixed_costs: Custos fixos mensais

    Returns:
        Dict com unidades necessárias e receita break-even
    """
    unit_margin = calculate_unit_margin()
    contribution_margin = unit_margin['gross_margin']

    units_break_even = fixed_costs / contribution_margin if contribution_margin > 0 else 0
    revenue_break_even = units_break_even * SALE_PRICE

    return {
        'fixed_costs': fixed_costs,
        'units_needed': units_break_even,
        'revenue_needed': revenue_break_even,
        'contribution_margin': contribution_margin
    }

# Cenários pré-configurados KabaK
SCENARIO_CONSERVATIVE = [1000, 3000, 8000, 12000, 15000, 18000, 20000, 20000, 20000, 20000, 20000, 20000]
SCENARIO_OPTIMISTIC = [1500, 4500, 10000, 15000, 19000, 23000, 26000, 26000, 26000, 26000, 26000, 26000]
SCENARIO_PESSIMISTIC = [700, 2100, 5600, 8400, 10500, 12600, 14000, 14000, 14000, 14000, 14000, 14000]

# Exemplo de uso
if __name__ == '__main__':
    print("=== Margem por Kit ===")
    margin = calculate_unit_margin()
    print(f"Preço: R$ {margin['price']:.2f}")
    print(f"Custo Total: R$ {margin['total_cost']:.2f}")
    print(f"Margem: R$ {margin['gross_margin']:.2f} ({margin['margin_pct']:.1f}%)\n")

    print("=== Projeção Mês 1 ===")
    month1 = calculate_monthly_projection(1000)
    print(f"Receita: R$ {month1['revenue']:,.2f}")
    print(f"Lucro: R$ {month1['net_profit']:,.2f}\n")

    print("=== Projeção Anual (Conservador) ===")
    annual = calculate_annual_projection(SCENARIO_CONSERVATIVE)
    print(f"Receita Total: R$ {annual['annual']['total_revenue']:,.2f}")
    print(f"Lucro Total: R$ {annual['annual']['total_profit']:,.2f}")
    print(f"Unidades: {annual['annual']['total_units']:,}")

    print("\n=== ROI ===")
    roi = calculate_roi(2600000, annual['annual']['total_profit'])
    print(f"Investimento: R$ {roi['investment']:,.2f}")
    print(f"Lucro: R$ {roi['profit']:,.2f}")
    print(f"ROI: {roi['roi_pct']:.1f}%")
