import sqlite3
import pandas as pd

print("=" * 70)
print("LOADING CLEANED DATA INTO SQLITE")
print("=" * 70)

# Connect to SQLite
conn = sqlite3.connect("bluestock_mf.db")

print("\nDatabase Connected Successfully.")

# Load cleaned datasets
fund = pd.read_csv("data/processed/01_fund_master.csv")
nav = pd.read_csv("data/processed/clean_nav.csv")
transactions = pd.read_csv("data/processed/clean_transactions.csv")
performance = pd.read_csv("data/processed/clean_scheme_performance.csv")

print("\nDatasets Loaded Successfully.")

# Load into SQLite tables
fund.to_sql("dim_fund", conn, if_exists="append", index=False)
nav.to_sql("fact_nav", conn, if_exists="append", index=False)
transactions.to_sql("fact_transactions", conn, if_exists="append", index=False)
performance.to_sql("fact_performance", conn, if_exists="append", index=False)

print("\nAll Data Loaded Successfully.")

conn.commit()
conn.close()

print("\nDatabase Connection Closed.")
print("=" * 70)
print("DATABASE LOADING COMPLETED")
print("=" * 70)