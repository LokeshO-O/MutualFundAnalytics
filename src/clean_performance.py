import pandas as pd

print("Loading scheme performance data...")

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

original_rows = len(df)

# Return columns
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

# Ensure returns are numeric
for col in return_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# Remove duplicates
df = df.drop_duplicates()

# Expense ratio validation
expense_anomalies = df[
    (df["expense_ratio_pct"] < 0.1)
    |
    (df["expense_ratio_pct"] > 2.5)
]

# Return anomalies
return_anomalies = df[
    (df["return_1yr_pct"] > 200)
    |
    (df["return_1yr_pct"] < -100)
    |
    (df["return_3yr_pct"] > 200)
    |
    (df["return_3yr_pct"] < -100)
    |
    (df["return_5yr_pct"] > 200)
    |
    (df["return_5yr_pct"] < -100)
]

# Save cleaned file
output_path = (
    "data/processed/"
    "07_scheme_performance_cleaned.csv"
)

df.to_csv(
    output_path,
    index=False
)

# Quality Report
print(f"Rows after cleaning: {len(df)}")
print(
    f"Duplicate rows removed: "
    f"{original_rows - len(df)}"
)
print(
    f"Expense ratio anomalies: "
    f"{len(expense_anomalies)}"
)
print(
    f"Return anomalies: "
    f"{len(return_anomalies)}"
)

print(f"Cleaned file saved to: {output_path}")
print(
    "Scheme performance cleaning completed successfully."
)