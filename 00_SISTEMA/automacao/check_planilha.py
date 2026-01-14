import pandas as pd
import sys

excel_path = r"C:\Users\gasse\OneDrive\Meu_Segundo_Cerebro\02_PROJETOS\KabaK\Outlet_Expansion\recursos\Analise de negócio Jean x Samson.xlsx"

print("=" * 80)
print("ANÁLISE DA PLANILHA SANSOM - STATUS ATUAL")
print("=" * 80)

try:
    df = pd.read_excel(excel_path, sheet_name=0, header=None)

    print("\n📊 ESTRUTURA DA PLANILHA:")
    print(f"Linhas: {len(df)}")
    print(f"Colunas: {len(df.columns)}")

    print("\n📋 DADOS PRINCIPAIS:")
    print("-" * 80)

    # Linha do produto (geralmente linha 2)
    if len(df) > 2:
        print(f"\nPRODUTO (Linha 2): {df.iloc[2, 1]}")

    # Quantidade
    if len(df) > 2 and len(df.columns) > 2:
        print(f"Quantidade Jan: {df.iloc[2, 2]}")

    # Valor unitário
    if len(df) > 3 and len(df.columns) > 2:
        print(f"Valor Unitário: R$ {df.iloc[3, 2]}")

    # Custos fixos importantes
    print("\n💰 CUSTOS MENSAIS:")
    print("-" * 80)

    for idx, row in df.iterrows():
        if idx < 20:  # Primeiras 20 linhas
            descricao = row.iloc[1]
            valor = row.iloc[2] if len(row) > 2 else None

            if pd.notna(descricao) and pd.notna(valor):
                if isinstance(valor, (int, float)) and valor > 0:
                    print(f"{descricao}: R$ {valor:,.2f}")

    print("\n📈 RESULTADO MENSAL:")
    print("-" * 80)

    # Procurar linha de Lucro
    for idx, row in df.iterrows():
        descricao = str(row.iloc[1]).lower() if pd.notna(row.iloc[1]) else ""
        if "lucro" in descricao:
            valor = row.iloc[2] if len(row) > 2 else None
            if pd.notna(valor):
                print(f"{row.iloc[1]}: R$ {valor:,.2f}")

    # Procurar margem
    for idx, row in df.iterrows():
        descricao = str(row.iloc[1]).lower() if pd.notna(row.iloc[1]) else ""
        if "margem" in descricao:
            valor = row.iloc[2] if len(row) > 2 else None
            if pd.notna(valor):
                print(f"{row.iloc[1]}: {valor:.2%}")

    print("\n👥 DISTRIBUIÇÃO SÓCIOS:")
    print("-" * 80)

    for idx, row in df.iterrows():
        descricao = str(row.iloc[1]).lower() if pd.notna(row.iloc[1]) else ""
        if "sansom" in descricao or "jean" in descricao or "prolabore" in descricao:
            valor = row.iloc[2] if len(row) > 2 else None
            if pd.notna(valor) and isinstance(valor, (int, float)):
                print(f"{row.iloc[1]}: R$ {valor:,.2f}")

    print("\n" + "=" * 80)
    print("✅ Status: Planilha lida com sucesso")

except Exception as e:
    print(f"\n❌ ERRO: {e}")
    import traceback
    traceback.print_exc()
