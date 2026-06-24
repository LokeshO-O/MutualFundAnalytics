import pandas as pd

print("Loading NAV history data...")

df = pd.read_csv("data/raw/02_nav_history.csv")

# Parse date column
df["date"] = pd.to_datetime(df["date"])

# Sort by AMFI code and date
df = df.sort_values(
    ["amfi_code", "date"]
).reset_index(drop=True)


df = df.drop_duplicates()

# Validate NAV > 0
df = df[df["nav"] > 0]

# Forward-fill missing NAV values within each scheme
df["nav"] = (
    df.groupby("amfi_code")["nav"]
      .ffill()
)

# Save cleaned dataset
output_path = "data/processed/02_nav_history_cleaned.csv"

df.to_csv(
    output_path,
    index=False
)

print(f"Cleaned file saved to: {output_path}")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print("NAV history cleaning completed successfully.")


original_rows = len(df)

# cleaning logic ...

print(f"Rows after cleaning: {len(df)}")
print(f"Duplicate rows removed: {original_rows - len(df)}")
print(f"Missing NAV values: {df['nav'].isnull().sum()}")