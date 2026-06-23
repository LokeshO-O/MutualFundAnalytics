import pandas as pd
import os

# Folder in which CSV files 
data_pa = "data/raw"

# Getting CSV files
csv_f = [i for i in os.listdir(data_pa) if i.endswith(".csv")]

print(f"\nFound {len(csv_f)} CSV files\n")

for f in csv_f:

    print("=" * 80)
    print(f"FILE: {f}")
    print("=" * 80)

    file_path = os.path.join(data_pa, f)

    try:
        df = pd.read_csv(file_path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

    except Exception as e:
        print(f"Error reading {f}: {e}")

    print("\n")

    print("\n" + "=" * 80)
print("FUND MASTER EXPLORATION")
print("=" * 80)

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub Categories:")
print(fund_master["sub_category"].unique())

print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())

print("\n" + "=" * 80)
print("AMFI CODE VALIDATION")
print("=" * 80)

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = fund_codes - nav_codes

print(f"\nFund Master Codes: {len(fund_codes)}")
print(f"NAV History Codes: {len(nav_codes)}")

if len(missing_codes) == 0:
    print("\nSUCCESS: All AMFI codes exist in NAV history.")
else:
    print("\nMissing Codes:")
    print(missing_codes)