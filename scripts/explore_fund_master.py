import pandas as pd

print("=" * 70)
print("FUND MASTER EXPLORATION")
print("=" * 70)

# Load Fund Master Dataset
df = pd.read_csv("data/raw/01_fund_master.csv")

# Total Schemes
print("\nTotal Schemes:")
print(len(df))

# Column Names
print("\nColumn Names:")
print(df.columns.tolist())

# First 5 Rows
print("\nFirst 5 Rows:")
print(df.head())

# Unique Fund Houses
if "fund_house" in df.columns:
    print("\nUnique Fund Houses:")
    print(df["fund_house"].unique())

# Unique Categories
if "category" in df.columns:
    print("\nUnique Categories:")
    print(df["category"].unique())

# Unique Sub Categories
if "sub_category" in df.columns:
    print("\nUnique Sub Categories:")
    print(df["sub_category"].unique())

# Check for Risk Column (different datasets use different names)
if "risk_grade" in df.columns:
    print("\nUnique Risk Grades:")
    print(df["risk_grade"].unique())
elif "risk" in df.columns:
    print("\nUnique Risk:")
    print(df["risk"].unique())
elif "riskometer" in df.columns:
    print("\nUnique Riskometer:")
    print(df["riskometer"].unique())
elif "risk_level" in df.columns:
    print("\nUnique Risk Level:")
    print(df["risk_level"].unique())
else:
    print("\nRisk Grade column not found in this dataset.")

print("\n" + "=" * 70)
print("FUND MASTER EXPLORATION COMPLETED")
print("=" * 70)