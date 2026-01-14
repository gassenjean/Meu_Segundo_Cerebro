"""
AUDITORIA KABAK - RECÁLCULO COM IMPOSTOS CORRETOS
Data: 23/Dez/2025
Autor: Claude Architect

PROBLEMA IDENTIFICADO:
- Planilha antiga usava 6% imposto fixo (ERRADO)
- Benefício fiscal MG: 1,3% fora do estado | 6% dentro

PREMISSAS AUDITADAS:
- 85% vendas FORA de MG (1,3% ICMS)
- 15% vendas DENTRO de MG (6% ICMS)
- Alíquota efetiva = (0.85 × 1.3%) + (0.15 × 6%) = 2.005%
"""

import csv
from datetime import datetime

# ========== PREMISSAS AUDITADAS ==========
PRECO_KIT = 129.00
CMV_KIT = 45.00  # Custo Mercadoria Vendida por kit
CUSTEIO_FABRICA = 500_000.00  # Fixo mensal
MKT_TITANIUM_BASE = 60_000.00
TRAFEGO_PAGO_BASE = 40_000.00

# IMPOSTOS CORRETOS (AUDITADO)
VENDAS_FORA_MG = 0.85  # 85% fora do estado
VENDAS_DENTRO_MG = 0.15  # 15% dentro do estado
ICMS_FORA_MG = 0.013  # 1,3%
ICMS_DENTRO_MG = 0.06  # 6%
ALIQUOTA_EFETIVA = (VENDAS_FORA_MG * ICMS_FORA_MG) + (VENDAS_DENTRO_MG * ICMS_DENTRO_MG)

LOGISTICA_GATEWAY = 0.10  # 10% da receita

# Quantidades por mês (mantidas conforme planilha original)
KITS_POR_MES = {
    'JAN': 1_000,
    'FEV': 3_300,
    'MAR': 8_300,
    'ABR': 13_300,
    'MAI': 18_300,
    'JUN': 23_300,
    'JUL': 25_000,
    'AGO': 26_600,
    'SET': 28_300,
    'OUT': 30_000,
    'NOV': 33_300,
    'DEZ': 40_000
}

# Tráfego pago progressivo
TRAFEGO_POR_MES = {
    'JAN': 40_000,
    'FEV': 40_000,
    'MAR': 40_000,
    'ABR': 60_000,
    'MAI': 80_000,
    'JUN': 100_000,
    'JUL': 120_000,
    'AGO': 150_000,
    'SET': 150_000,
    'OUT': 150_000,
    'NOV': 200_000,
    'DEZ': 250_000
}

def calcular_mes(mes, kits):
    """Calcula resultado mensal com impostos CORRETOS"""

    receita_bruta = kits * PRECO_KIT
    cmv = kits * CMV_KIT
    custeio_fabrica = CUSTEIO_FABRICA
    mkt = MKT_TITANIUM_BASE
    trafego = TRAFEGO_POR_MES[mes]

    # IMPOSTO CORRETO (AUDITADO)
    impostos = receita_bruta * ALIQUOTA_EFETIVA

    logistica = receita_bruta * LOGISTICA_GATEWAY

    total_despesas = cmv + custeio_fabrica + mkt + trafego + impostos + logistica
    lucro_liquido = receita_bruta - total_despesas
    margem = (lucro_liquido / receita_bruta * 100) if receita_bruta > 0 else 0

    return {
        'mes': mes,
        'kits': kits,
        'receita_bruta': receita_bruta,
        'cmv': cmv,
        'custeio_fabrica': custeio_fabrica,
        'mkt': mkt,
        'trafego': trafego,
        'impostos': impostos,
        'logistica': logistica,
        'total_despesas': total_despesas,
        'lucro_liquido': lucro_liquido,
        'margem': margem
    }

def main():
    """Gera planilha AUDITADA com impostos corretos"""

    print("=" * 80)
    print("AUDITORIA KABAK - RECALCULO FINANCEIRO")
    print("=" * 80)
    print(f"\nData: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
    print(f"\n[PREMISSAS AUDITADAS]")
    print(f"   - Preco Kit: R$ {PRECO_KIT:,.2f}")
    print(f"   - CMV Kit: R$ {CMV_KIT:,.2f}")
    print(f"   - Custeio Fabrica: R$ {CUSTEIO_FABRICA:,.2f}/mes")
    print(f"\n[IMPOSTOS CORRETOS - BENEFICIO FISCAL MG]")
    print(f"   - {VENDAS_FORA_MG*100:.0f}% vendas FORA de MG -> {ICMS_FORA_MG*100:.1f}% ICMS")
    print(f"   - {VENDAS_DENTRO_MG*100:.0f}% vendas DENTRO de MG -> {ICMS_DENTRO_MG*100:.1f}% ICMS")
    print(f"   - ALIQUOTA EFETIVA: {ALIQUOTA_EFETIVA*100:.2f}%")
    print(f"\n[COMPARACAO]")
    print(f"   - Imposto ANTIGO (errado): 6.00%")
    print(f"   - Imposto NOVO (correto): {ALIQUOTA_EFETIVA*100:.2f}%")
    print(f"   - ECONOMIA: {(0.06 - ALIQUOTA_EFETIVA)*100:.2f} pontos percentuais!")
    print("\n" + "=" * 80)

    resultados = []
    caixa_acumulado = 0

    print("\n[RESULTADOS MENSAIS AUDITADOS]\n")
    print(f"{'MÊS':<6} {'KITS':>8} {'RECEITA':>14} {'IMPOSTOS':>12} {'LUCRO LÍQ':>14} {'MARGEM':>8} {'CAIXA ACUM':>14}")
    print("-" * 80)

    for mes, kits in KITS_POR_MES.items():
        resultado = calcular_mes(mes, kits)
        caixa_acumulado += resultado['lucro_liquido']
        resultado['caixa_acumulado'] = caixa_acumulado
        resultados.append(resultado)

        print(f"{mes:<6} {kits:>8,} R$ {resultado['receita_bruta']:>10,.0f} "
              f"R$ {resultado['impostos']:>9,.0f} R$ {resultado['lucro_liquido']:>11,.0f} "
              f"{resultado['margem']:>7.1f}% R$ {caixa_acumulado:>11,.0f}")

    # Totais
    total_kits = sum(r['kits'] for r in resultados)
    total_receita = sum(r['receita_bruta'] for r in resultados)
    total_impostos = sum(r['impostos'] for r in resultados)
    total_despesas = sum(r['total_despesas'] for r in resultados)
    total_lucro = sum(r['lucro_liquido'] for r in resultados)
    margem_media = (total_lucro / total_receita * 100) if total_receita > 0 else 0

    print("-" * 80)
    print(f"{'TOTAL':<6} {total_kits:>8,} R$ {total_receita:>10,.0f} "
          f"R$ {total_impostos:>9,.0f} R$ {total_lucro:>11,.0f} "
          f"{margem_media:>7.1f}%")

    # Salvar CSV
    csv_file = 'PLANILHA_FINANCEIRA_KABAK_AUDITADA.csv'
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, delimiter=';')

        # Cabeçalho
        writer.writerow([
            'MÊS', 'KITS VENDIDOS', 'PREÇO MÉDIO (KIT)', 'RECEITA BRUTA',
            'CUSTO PRODUTO (CMV KIT)', 'CUSTEIO FABRICAÇÃO', 'MKT TITANIUM',
            'TRÁFEGO PAGO', f'IMPOSTOS ({ALIQUOTA_EFETIVA*100:.2f}%)',
            'LOGÍSTICA + GATEWAY (10%)', 'TOTAL DESPESAS', 'LUCRO LÍQUIDO',
            'MARGEM %', 'CAIXA ACUMULADO'
        ])

        # Dados
        for r in resultados:
            writer.writerow([
                r['mes'],
                int(r['kits']),
                int(PRECO_KIT),
                int(r['receita_bruta']),
                int(r['cmv']),
                int(r['custeio_fabrica']),
                int(r['mkt']),
                int(r['trafego']),
                int(r['impostos']),
                int(r['logistica']),
                int(r['total_despesas']),
                int(r['lucro_liquido']),
                f"{r['margem']:.0f}%",
                int(r['caixa_acumulado'])
            ])

        # Total
        writer.writerow([
            'TOTAL',
            int(total_kits),
            int(PRECO_KIT),
            int(total_receita),
            int(sum(r['cmv'] for r in resultados)),
            int(CUSTEIO_FABRICA * 12),
            int(MKT_TITANIUM_BASE * 12),
            int(sum(r['trafego'] for r in resultados)),
            int(total_impostos),
            int(sum(r['logistica'] for r in resultados)),
            int(total_despesas),
            int(total_lucro),
            f"{margem_media:.0f}%",
            ''
        ])

    print(f"\n[OK] Arquivo CSV gerado: {csv_file}")

    # Comparação com planilha antiga
    impostos_antigos = total_receita * 0.06
    economia_impostos = impostos_antigos - total_impostos
    lucro_antigo = total_receita - (total_despesas - total_impostos + impostos_antigos)
    ganho_lucro = total_lucro - lucro_antigo

    print("\n" + "=" * 80)
    print("COMPARACAO: ANTES vs DEPOIS DA AUDITORIA")
    print("=" * 80)
    print(f"\n{'Métrica':<30} {'ANTES (6%)':<20} {'DEPOIS ({:.2f}%)'.format(ALIQUOTA_EFETIVA*100):<20} {'DIFERENÇA':<15}")
    print("-" * 80)
    print(f"{'Impostos Anuais':<30} R$ {impostos_antigos:>15,.0f} R$ {total_impostos:>15,.0f} R$ {economia_impostos:>12,.0f}")
    print(f"{'Lucro Líquido Anual':<30} R$ {lucro_antigo:>15,.0f} R$ {total_lucro:>15,.0f} R$ {ganho_lucro:>12,.0f}")
    print(f"{'Margem Líquida':<30} {(lucro_antigo/total_receita*100):>16.1f}% {margem_media:>16.1f}% {(margem_media - lucro_antigo/total_receita*100):>12.1f}pp")

    print("\n" + "=" * 80)
    print("DISTRIBUICAO DE LUCROS (WATERFALL) - AUDITADO")
    print("=" * 80)

    prolabore_kabak = 100_000 * 12  # R$ 100k/mês
    reembolso_sansom = 3_000_000 + 360_000 + sum(TRAFEGO_POR_MES.values())  # Fabricação + Mkt + Tráfego
    saldo_divisao = total_lucro - prolabore_kabak - reembolso_sansom
    kabak_50 = saldo_divisao * 0.5
    sansom_50 = saldo_divisao * 0.5

    print(f"\n1. PRIORIDADE: Pro-labore KABAK")
    print(f"    R$ 100.000/mes x 12 meses = R$ {prolabore_kabak:,.0f}")

    print(f"\n2. PRIORIDADE: Reembolso SANSOM")
    print(f"    Fabricacao: R$ 3.000.000")
    print(f"    Marketing: R$ 360.000")
    print(f"    Trafego: R$ {sum(TRAFEGO_POR_MES.values()):,.0f}")
    print(f"    ------------------------------")
    print(f"    TOTAL: R$ {reembolso_sansom:,.0f}")

    print(f"\n3. DIVISAO 50/50:")
    print(f"    Saldo Restante: R$ {saldo_divisao:,.0f}")
    print(f"    - KABAK (50%):  R$ {kabak_50:,.0f}")
    print(f"    - SANSOM (50%): R$ {sansom_50:,.0f}")

    print("\n" + "=" * 80)
    print("TOTAL RECEBIDO (ANO 1) - AUDITADO")
    print("=" * 80)

    total_kabak = prolabore_kabak + kabak_50
    total_sansom = reembolso_sansom + sansom_50
    roi_sansom = (total_sansom / reembolso_sansom - 1) * 100

    print(f"\n==========================================")
    print(f"             KABAK RECEBE                ")
    print(f"==========================================")
    print(f"Pro-labore (12 meses):    R$ {prolabore_kabak:>12,}")
    print(f"Lucro 50%:                R$ {kabak_50:>12,}")
    print(f"------------------------------------------")
    print(f"TOTAL ANO 1:              R$ {total_kabak:>12,}")

    print(f"\n==========================================")
    print(f"             SANSOM RECEBE               ")
    print(f"==========================================")
    print(f"Reembolso investimento:   R$ {reembolso_sansom:>12,}")
    print(f"Lucro 50%:                R$ {sansom_50:>12,}")
    print(f"------------------------------------------")
    print(f"TOTAL ANO 1:              R$ {total_sansom:>12,}")
    print(f"\nROI: {roi_sansom:.0f}% EM 12 MESES!")
    print(f"(Investiu R$ {reembolso_sansom/1_000_000:.1f}M -> Recebeu R$ {total_sansom/1_000_000:.1f}M)")

    print("\n" + "=" * 80)
    print("AUDITORIA CONCLUIDA!")
    print("=" * 80)
    print(f"\n[+] ECONOMIA DE IMPOSTOS: R$ {economia_impostos:,.0f}")
    print(f"[+] AUMENTO NO LUCRO: R$ {ganho_lucro:,.0f} (+{(ganho_lucro/lucro_antigo*100):.1f}%)")
    print(f"\n[OK] Arquivo gerado: {csv_file}")
    print(f"[OK] Data: {datetime.now().strftime('%d/%m/%Y as %H:%M')}")

if __name__ == '__main__':
    main()
