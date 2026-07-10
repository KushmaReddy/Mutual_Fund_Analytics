"""
============================================================
Mutual Fund Analytics Capstone
File Name : validate_amfi_codes.py
Author    : Kushma Reddy H

Description:
This script validates whether all AMFI codes present in the
NAV History dataset also exist in the Fund Master dataset.
============================================================
"""

import pandas as pd


def validate_amfi_codes():
    """
    Validate AMFI codes between the Fund Master and
    NAV History datasets.

    Returns:
        None
    """

    print("=" * 70)
    print("VALIDATING AMFI CODES")
    print("=" * 70)

    # Load datasets
    fund_master = pd.read_csv("data/raw/01_fund_master.csv")
    nav_history = pd.read_csv("data/raw/02_nav_history.csv")

    # Extract unique AMFI codes
    fund_codes = set(fund_master["amfi_code"])
    nav_codes = set(nav_history["amfi_code"])

    # Find missing AMFI codes
    missing_codes = nav_codes - fund_codes

    print("\nTotal AMFI Codes in Fund Master :", len(fund_codes))
    print("Total AMFI Codes in NAV History :", len(nav_codes))

    if len(missing_codes) == 0:
        print("\nAll NAV History AMFI codes exist in Fund Master.")
    else:
        print("\nMissing AMFI Codes:")
        print(missing_codes)

    print("\nValidation Completed")
    print("=" * 70)


if __name__ == "__main__":
    validate_amfi_codes()