"""
============================================================
Mutual Fund Analytics Capstone
File Name : data_ingestion.py
Author    : Kushma Reddy H

Description:
This script loads the cleaned mutual fund datasets into the
SQLite database. It creates and populates the dimension and
fact tables required for analysis.
============================================================
"""

import sqlite3
import pandas as pd


def load_data_to_database():
    """
    Load cleaned datasets into the SQLite database.

    This function connects to the SQLite database,
    loads the processed CSV files, inserts them into
    the corresponding tables, and closes the connection.

    Returns:
        None
    """

    print("=" * 70)
    print("LOADING CLEANED DATA INTO SQLITE")
    print("=" * 70)

    # Connect to SQLite database
    conn = sqlite3.connect("bluestock_mf.db")

    print("\nDatabase Connected Successfully.")

    # Load cleaned datasets
    fund = pd.read_csv("data/processed/01_fund_master.csv")
    nav = pd.read_csv("data/processed/clean_nav.csv")
    transactions = pd.read_csv("data/processed/clean_transactions.csv")
    performance = pd.read_csv("data/processed/clean_scheme_performance.csv")

    print("\nDatasets Loaded Successfully.")

    # Load datasets into SQLite tables
    fund.to_sql("dim_fund", conn, if_exists="append", index=False)
    nav.to_sql("fact_nav", conn, if_exists="append", index=False)
    transactions.to_sql("fact_transactions", conn, if_exists="append", index=False)
    performance.to_sql("fact_performance", conn, if_exists="append", index=False)

    print("\nAll Data Loaded Successfully.")

    # Save changes and close connection
    conn.commit()
    conn.close()

    print("\nDatabase Connection Closed.")
    print("=" * 70)
    print("DATABASE LOADING COMPLETED")
    print("=" * 70)


if __name__ == "__main__":
    load_data_to_database()