
import csv

# Parameters
TAX_RATE = 0.025  # 2.5% (Weighted Avg: 80% Interstate @ 1.3% + 20% Internal @ 6%)
FIXED_COST_FACTORY = 500000
PRICE_KIT = 129
LOGISTICS_RATE = 0.10  # 10%

# ... (Sales Forecast) ...
forecast = [
    {"month": "JAN", "kits": 1000, "ads": 40000},
    {"month": "FEV", "kits": 3300, "ads": 40000},
    {"month": "MAR", "kits": 8300, "ads": 40000},
    {"month": "ABR", "kits": 13300, "ads": 60000},
    {"month": "MAI", "kits": 18300, "ads": 80000},
    {"month": "JUN", "kits": 23300, "ads": 100000},
    {"month": "JUL", "kits": 25000, "ads": 120000},
    {"month": "AGO", "kits": 26600, "ads": 150000},
    {"month": "SET", "kits": 28300, "ads": 150000},
    {"month": "OUT", "kits": 30000, "ads": 150000},
    {"month": "NOV", "kits": 33300, "ads": 200000},
    {"month": "DEZ", "kits": 40000, "ads": 250000},
]

# Variable Cost per Kit (Derived from Junho: 1048500 / 23300 = 45)
COST_PER_KIT_CMV = 45

# Prepare CSV output
output_file = 'calculated_values.csv'

with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["MÊS", "KITS VENDIDOS", "PREÇO MÉDIO (KIT)", "RECEITA BRUTA", "CUSTO PRODUTO (CMV KIT)", "CUSTEIO FABRICAÇÃO", "MKT TITANIUM", "TRÁFEGO PAGO", "IMPOSTOS (2.5%)", "LOGÍSTICA + GATEWAY (10%)", "TOTAL DESPESAS", "LUCRO LÍQUIDO", "MARGEM %", "CAIXA ACUMULADO"])

    cumulative_cash = 0
    total_kits = 0
    total_revenue = 0
    total_cmv = 0
    total_fixed = 0
    total_agency = 0
    total_ads = 0
    total_tax = 0
    total_logistics = 0
    total_expenses = 0
    total_profit = 0

    for row in forecast:
        month = row["month"]
        kits = row["kits"]
        ads = row["ads"]
        
        revenue = kits * PRICE_KIT
        cmv = kits * COST_PER_KIT_CMV
        factory = FIXED_COST_FACTORY
        
        # Titanium Agency Fee (Step-up)
        if month in ["JAN", "FEV", "MAR"]:
            agency = 45000
        elif month in ["ABR", "MAI", "JUN"]:
            agency = 50000
        elif month in ["JUL", "AGO", "SET"]:
            agency = 55000
        else:
            agency = 60000

        tax = revenue * TAX_RATE
        logistics = revenue * LOGISTICS_RATE
        
        expenses = cmv + factory + agency + ads + tax + logistics
        profit = revenue - expenses
        
        cumulative_cash += profit
        margin = (profit / revenue) * 100 if revenue > 0 else 0
        
        # Totals
        total_kits += kits
        total_revenue += revenue
        total_cmv += cmv
        total_fixed += factory
        total_agency += agency
        total_ads += ads
        total_tax += tax
        total_logistics += logistics
        total_expenses += expenses
        total_profit += profit

        writer.writerow([month, kits, PRICE_KIT, f"{revenue:.0f}", f"{cmv:.0f}", f"{factory:.0f}", f"{agency:.0f}", f"{ads:.0f}", f"{tax:.0f}", f"{logistics:.0f}", f"{expenses:.0f}", f"{profit:.0f}", f"{margin:.0f}%", f"{cumulative_cash:.0f}"])

    # Total Line
    total_margin = (total_profit / total_revenue) * 100 if total_revenue > 0 else 0
    writer.writerow(["TOTAL", total_kits, PRICE_KIT, f"{total_revenue:.0f}", f"{total_cmv:.0f}", f"{total_fixed:.0f}", f"{total_agency:.0f}", f"{total_ads:.0f}", f"{total_tax:.0f}", f"{total_logistics:.0f}", f"{total_expenses:.0f}", f"{total_profit:.0f}", f"{total_margin:.0f}%", ""])

print(f"Calculations saved to {output_file}")
print(f"Total Profit: {total_profit}")
print(f"Total Revenue: {total_revenue}")
print(f"ROI Margin: {total_margin}%")

# Calculate Investment Needed (First 6 Months: Jan-Jun)
inv_factory = 500000 * 6
inv_agency = (45000 * 3) + (50000 * 3) # Jan-Mar (45k) + Apr-Jun (50k)
inv_ads = sum([row["ads"] for row in forecast[:6]]) # Sum ads for first 6 months

total_investment_6m = inv_factory + inv_agency + inv_ads
print(f"\n--- SANSOM INVESTMENT (6 MONTHS) ---")
print(f"Factory: {inv_factory}")
print(f"Agency: {inv_agency}")
print(f"Ads: {inv_ads}")
print(f"TOTAL INVESTMENT: {total_investment_6m}")
