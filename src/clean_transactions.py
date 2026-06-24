import pandas as pd

print("Loading investor transactions data...")

# Load dataset
df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

original_rows = len(df)

# Parse date column
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Remove duplicates
df = df.drop_duplicates()

# Validate amount > 0
df = df[df["amount_inr"] > 0]

# Validate KYC status
valid_kyc = ["Verified", "Pending"]

invalid_kyc = df[
    ~df["kyc_status"].isin(valid_kyc)
]

print(
    f"Invalid KYC records: {len(invalid_kyc)}"
)

# Save cleaned file
output_path = (
    "data/processed/"
    "08_investor_transactions_cleaned.csv"
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
    f"Invalid amounts: "
    f"{(df['amount_inr'] <= 0).sum()}"
)

print(f"Cleaned file saved to: {output_path}")
print(
    "Investor transactions cleaning "
    "completed successfully."
)