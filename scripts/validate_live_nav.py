"""
============================================================
Mutual Fund Analytics Capstone
File Name : validate_live_nav.py
Author    : Kushma Reddy H

Description:
This script validates the live NAV dataset by comparing it
with the historical NAV dataset. It displays sample records,
column names, data types, and the latest available records
to verify data consistency.
============================================================
"""

import pandas as pd


def validate_live_nav():
    """
    Validate the live NAV dataset against the historical NAV dataset.

    Returns:
        None
    """

    # Load datasets
    historical = pd.read_csv("data/raw/02_nav_history.csv")
    live = pd.read_csv("data/raw/live_nav.csv")

    print("=" * 60)
    print("LIVE NAV VALIDATION")
    print("=" * 60)

    # Historical dataset preview
    print("\nHistorical Dataset (First 5 Records)")
    print(historical.head())

    # Live dataset preview
    print("\nLive Dataset (First 5 Records)")
    print(live.head())

    # Column comparison
    print("\nHistorical Columns")
    print(historical.columns.tolist())

    print("\nLive Columns")
    print(live.columns.tolist())

    # Data types
    print("\nHistorical Data Types")
    print(historical.dtypes)

    print("\nLive Data Types")
    print(live.dtypes)

    # Latest records
    print("\nLatest Historical Records")
    print(historical.tail())

    print("\nLatest Live Records")
    print(live.head())

    print("\n" + "=" * 60)
    print("LIVE NAV VALIDATION COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    validate_live_nav()