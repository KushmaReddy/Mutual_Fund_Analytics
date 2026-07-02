import sqlite3
import pandas as pd

print("=" * 60)
print("VERIFYING DATABASE")
print("=" * 60)

conn = sqlite3.connect("bluestock_mf.db")

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance"
]

for table in tables:
    query = f"SELECT COUNT(*) AS total_rows FROM {table}"
    df = pd.read_sql(query, conn)
    print(f"{table}: {df.iloc[0]['total_rows']} rows")

conn.close()

print("=" * 60)
print("DATABASE VERIFIED SUCCESSFULLY")
print("=" * 60)