import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/02_nav_history.csv")

print("=" * 70)
print("NAV HISTORY CLEANING")
print("=" * 70)

print("\nOriginal Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())
# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

print("\nDate column converted successfully.")
print(df.dtypes)
# Sort by AMFI Code and Date
df = df.sort_values(by=["amfi_code", "date"])

print("\nData sorted successfully.")
# Forward fill missing NAV values
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

print("\nMissing NAV values filled.")
# Remove duplicate rows
duplicates = df.duplicated().sum()
df = df.drop_duplicates()

print("\nDuplicate rows removed:", duplicates)
# Check invalid NAV values
invalid_nav = (df["nav"] <= 0).sum()

print("\nInvalid NAV values:", invalid_nav)
# Save cleaned dataset
output_file = "data/processed/clean_nav.csv"

df.to_csv(output_file, index=False)

print("\nClean dataset saved successfully.")
print("Location:", output_file)
print("\n" + "=" * 70)
print("NAV HISTORY CLEANING COMPLETED")
print("=" * 70)