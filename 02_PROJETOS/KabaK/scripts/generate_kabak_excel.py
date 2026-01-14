
import pandas as pd
import os

# Dados baseados em PLANILHA_FINANCEIRA_12_MESES.md
months = ['Jan/26', 'Fev/26', 'Mar/26', 'Abr/26', 'Mai/26', 'Jun/26', 'Jul/26', 'Ago/26', 'Set/26', 'Out/26', 'Nov/26', 'Dez/26']

# Inicializando estrutura de dados (valores em R$)
data = {
    'Mês': months,
    '1) Investimento': [0] * 12,
    '2) Receita': [0] * 12,
    'Custos Variáveis (Fabricação/China)': [0] * 12,
    'Despesas Marketing (Tráfego)': [0] * 12,
    'Despesas Marketing (Titanium)': [0] * 12,
    'Despesas Logística': [0] * 12,
    'Despesas Operação (Fixo)': [0] * 12,
    'Impostos': [0] * 12,
    '3) Lucro': [0] * 12,
    '4) Caixa Acumulado': [0] * 12
}

# --- PREENCHENDO DADOS ---

# 1. Investimento (Jan-Abr: Pré-operacional / Mai-Jun: Operacional)
# Jan-Abr: Preparação estoque e estrutura (Total ~1.98M)
# Mai-Jun: Cobertura de prejuízo inicial (Total ~126k)
data['1) Investimento'][0] = 500000  # Jan
data['1) Investimento'][1] = 500000  # Fev
data['1) Investimento'][2] = 500000  # Mar
data['1) Investimento'][3] = 480000  # Abr
data['1) Investimento'][4] = 116575  # Mai (cobrir prejuízo)
data['1) Investimento'][5] = 9725    # Jun (cobrir prejuízo)
# Total Investido: ~2.1M

# 2. Receita (Vendas começam em Mai)
# Mai: 1k kits | Jun: 3k | Jul: 8k | Ago: 12k | Set: 15k | Out: 18k | Nov: 20k | Dez: 20k
price = 129
sales_vol = [0, 0, 0, 0, 1000, 3000, 8000, 12000, 15000, 18000, 20000, 20000]

for i, vol in enumerate(sales_vol):
    data['2) Receita'][i] = vol * price

# 3. Despesas Detalhadas

# Fabricação/Produto (China + Jean) = R$ 48/kit + Embalagem/Tags = R$ 48 (conforme md)
cost_per_kit = 48
for i, vol in enumerate(sales_vol):
    data['Custos Variáveis (Fabricação/China)'][i] = vol * cost_per_kit

# Marketing (Titanium fixo 60k + Tráfego variável)
# Titanium começa Fev (onboarding)
titanium_fee = 60000
for i in range(1, 12): # Fev em diante
    data['Despesas Marketing (Titanium)'][i] = titanium_fee

# Tráfego Pago (Jan: 0, Fev-Abr: 0, Mai: 40k, Jun: 50k, Jul: 70k, Ago: 90k, Set-Dez: 100k)
traffic = [0, 0, 0, 0, 40000, 50000, 70000, 90000, 100000, 100000, 100000, 100000]
data['Despesas Marketing (Tráfego)'] = traffic

# Logística (12% da receita) + Fixo (10k)
log_fixed = 10000
log_var_pct = 0.12
for i, rev in enumerate(data['2) Receita']):
    variable = rev * log_var_pct
    fixed = log_fixed if i >= 4 else 0 # Fixo começa em Mai
    data['Despesas Logística'][i] = variable + fixed

# Operação (Fixo 40k-60k) + Gateway (3%)
# Op Fixo: Mai: 40k, Jun: 40k, Jul: 45k, Ago: 50k, Set: 55k, Out+: 60k
# Gateway: 3% Receita
op_fixed = [0, 0, 0, 0, 40000, 40000, 45000, 50000, 55000, 60000, 60000, 60000]
gateway_pct = 0.03
for i, rev in enumerate(data['2) Receita']):
    data['Despesas Operação (Fixo)'][i] = op_fixed[i] + (rev * gateway_pct)

# Impostos (2.5% Receita - MG Simples/Incentivo)
tax_pct = 0.025
for i, rev in enumerate(data['2) Receita']):
    data['Impostos'][i] = rev * tax_pct

# 4. Lucro (Receita - Todas Despesas)
for i in range(12):
    total_expenses = (
        data['Custos Variáveis (Fabricação/China)'][i] +
        data['Despesas Marketing (Tráfego)'][i] +
        data['Despesas Marketing (Titanium)'][i] +
        data['Despesas Logística'][i] +
        data['Despesas Operação (Fixo)'][i] +
        data['Impostos'][i]
    )
    # Lucro operacional (sem contar investimento como receita)
    data['3) Lucro'][i] = data['2) Receita'][i] - total_expenses

# 5. Caixa (Acumulado)
# Caixa inicial = 0. Entradas = Investimento + Receita. Saídas = Despesas.
balance = 0
for i in range(12):
    inflow = data['1) Investimento'][i] + data['2) Receita'][i]
    
    total_outflow = (
        data['Custos Variáveis (Fabricação/China)'][i] +
        data['Despesas Marketing (Tráfego)'][i] +
        data['Despesas Marketing (Titanium)'][i] +
        data['Despesas Logística'][i] +
        data['Despesas Operação (Fixo)'][i] +
        data['Impostos'][i]
    )
    
    net_flow = inflow - total_outflow
    balance += net_flow
    data['4) Caixa Acumulado'][i] = balance

# --- GERANDO DATAFRAME E EXCEL ---
df = pd.DataFrame(data)

# Transpondo para ficar igual ao desenho (Meses nas colunas, Itens nas linhas)
df_t = df.set_index('Mês').T

output_path = r"C:\Users\gasse\OneDrive\Meu_Segundo_Cerebro\02_PROJETOS\KabaK\planejamento\PLANILHA_KABAK_SANSOM.xlsx"

# Requires openpyxl
try:
    df_t.to_excel(output_path)
    print(f"Success: Created {output_path}")
except Exception as e:
    print(f"Error: {e}")
