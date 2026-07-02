import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("=" * 70)
print("INVESTOR TRANSACTIONS CLEANING")
print("=" * 70)

print("\nOriginal Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())
# Convert transaction date to datetime
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

print("\nTransaction date converted successfully.")
print(df.dtypes)
# Remove duplicate rows
duplicates = df.duplicated().sum()
df = df.drop_duplicates()

print("\nDuplicate rows removed:", duplicates)
# Validate transaction amount
invalid_amount = (df["amount_inr"] <= 0).sum()

print("\nInvalid Amount Records:", invalid_amount)
# Standardize transaction type
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

print("\nTransaction Types:")
print(df["transaction_type"].unique())
# Check KYC Status
print("\nKYC Status Values:")
print(df["kyc_status"].value_counts())
# Save cleaned file
output_file = "data/processed/clean_transactions.csv"

df.to_csv(output_file, index=False)

print("\nCleaned transactions saved successfully.")
print("Location:", output_file)

print("\n" + "=" * 70)
print("INVESTOR TRANSACTION CLEANING COMPLETED")
print("=" * 70)