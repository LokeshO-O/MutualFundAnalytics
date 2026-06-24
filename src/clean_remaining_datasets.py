import pandas as pd

files = {
    "01_fund_master.csv":
        "01_fund_master_cleaned.csv",

    "03_aum_by_fund_house.csv":
        "03_aum_by_fund_house_cleaned.csv",

    "04_monthly_sip_inflows.csv":
        "04_monthly_sip_inflows_cleaned.csv",

    "05_category_inflows.csv":
        "05_category_inflows_cleaned.csv",

    "06_industry_folio_count.csv":
        "06_industry_folio_count_cleaned.csv",

    "09_portfolio_holdings.csv":
        "09_portfolio_holdings_cleaned.csv",

    "10_benchmark_indices.csv":
        "10_benchmark_indices_cleaned.csv"
}

for input_file, output_file in files.items():

    print(f"\nProcessing {input_file}")

    df = pd.read_csv(
        f"data/raw/{input_file}"
    )

    original_rows = len(df)

    # Remove duplicates
    df = df.drop_duplicates()

    # Save cleaned dataset
    df.to_csv(
        f"data/processed/{output_file}",
        index=False
    )

    print(
        f"Rows: {len(df)} "
        f"(removed {original_rows - len(df)} duplicates)"
    )

print("\nAll remaining datasets cleaned successfully.")