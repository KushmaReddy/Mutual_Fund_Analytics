import pandas as pd

# ======================================================
# Exploratory Data Analysis (EDA)
# ======================================================

# Load cleaned dataset
df = pd.read_csv("data/processed/02_nav_history.csv")

print("=" * 70)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 70)

# Dataset Shape
print("\nDataset Shape")
print(df.shape)

# Column Names
print("\nColumn Names")
print(df.columns.tolist())

# First 5 Rows
print("\nFirst 5 Rows")
print(df.head())

# Last 5 Rows
print("\nLast 5 Rows")
print(df.tail())

# Summary Statistics
print("\nSummary Statistics")
print(df.describe())

# Total Records
print("\nTotal Records")
print(len(df))

# Date Range
print("\nDate Range")
print("From :", df["date"].min())
print("To   :", df["date"].max())

# Average NAV
print("\nAverage NAV")
print(df["nav"].mean())

# Highest NAV
print("\nHighest NAV")
print(df["nav"].max())

# Lowest NAV
print("\nLowest NAV")
print(df["nav"].min())

# Median NAV
print("\nMedian NAV")
print(df["nav"].median())

# Standard Deviation
print("\nStandard Deviation")
print(df["nav"].std())

print("\n" + "=" * 70)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 70)