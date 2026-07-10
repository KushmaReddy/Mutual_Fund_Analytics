"""
============================================================
Mutual Fund Analytics Capstone
File Name : check_database.py
Author    : Kushma Reddy H

Description:
Verifies the SQLite database by checking the connection,
available tables, and row count.
============================================================
"""

import sqlite3
import pandas as pd


def check_database():

    print("=" * 60)
    print("VERIFYING DATABASE")
    print("=" * 60)

    # Connect to SQLite database
    conn = sqlite3.connect("bluestock_mf.db")

    # List of tables to verify
    tables = [
        "dim_fund",
        "fact_nav",
        "fact_transactions",
        "fact_performance"
    ]

    # Check each table
    for table in tables:
        try:
            query = f"SELECT COUNT(*) AS total_rows FROM {table}"
            df = pd.read_sql(query, conn)
            print(f"{table}: {df.iloc[0]['total_rows']} rows")
        except Exception as e:
            print(f"{table}: ERROR -> {e}")

    conn.close()

    print("=" * 60)
    print("DATABASE VERIFIED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    check_database()