import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("=" * 70)
print("SCHEME PERFORMANCE CLEANING")
print("=" * 70)

print("\nOriginal Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())
import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("=" * 70)
print("SCHEME PERFORMANCE CLEANING")
print("=" * 70)

print("\nOriginal Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 Rows:")
print(df.head())
# --------------------------------------------------------
# Convert return columns to numeric
# --------------------------------------------------------

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("\nReturn columns converted successfully.")

# --------------------------------------------------------
# Convert Expense Ratio to numeric
# --------------------------------------------------------

df["expense_ratio_pct"] = pd.to_numeric(
    df["expense_ratio_pct"],
    errors="coerce"
)

print("Expense Ratio converted successfully.")

# --------------------------------------------------------
# Check Negative Sharpe Ratio
# --------------------------------------------------------

negative_sharpe = (df["sharpe_ratio"] < 0).sum()

print("\nNegative Sharpe Ratios:", negative_sharpe)

# --------------------------------------------------------
# Validate Expense Ratio
# --------------------------------------------------------

invalid_expense = (
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
).sum()

print("Invalid Expense Ratios:", invalid_expense)

# --------------------------------------------------------
# Remove Duplicate Rows
# --------------------------------------------------------

duplicates = df.duplicated().sum()

df = df.drop_duplicates()

print("Duplicate Rows Removed:", duplicates)

# --------------------------------------------------------
# Save Clean Dataset
# --------------------------------------------------------

output_file = "data/processed/clean_scheme_performance.csv"

df.to_csv(output_file, index=False)

print("\nDataset cleaned successfully.")
print("Saved at:", output_file)

print("\n" + "=" * 70)
print("SCHEME PERFORMANCE CLEANING COMPLETED")
print("=" * 70)