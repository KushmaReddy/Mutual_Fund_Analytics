"""
============================================================
Mutual Fund Analytics Capstone
File Name : clean_scheme_performance.py
Author    : Kushma Reddy H

Description:
This script cleans the Scheme Performance dataset by:
1. Loading the raw scheme performance data
2. Converting return columns to numeric
3. Converting expense ratio to numeric
4. Validating Sharpe Ratio
5. Validating Expense Ratio
6. Removing duplicate records
7. Saving the cleaned dataset
============================================================
"""

import pandas as pd


def clean_scheme_performance():

    print("=" * 70)
    print("SCHEME PERFORMANCE CLEANING")
    print("=" * 70)

    # Load raw dataset
    df = pd.read_csv("data/raw/07_scheme_performance.csv")

    print("\nOriginal Shape:", df.shape)

    # Return columns
    return_columns = [
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct"
    ]

    # Convert return columns to numeric
    for col in return_columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    print("Return columns converted successfully.")

    # Convert expense ratio to numeric
    df["expense_ratio_pct"] = pd.to_numeric(
        df["expense_ratio_pct"],
        errors="coerce"
    )

    print("Expense Ratio converted successfully.")

    # Check negative Sharpe Ratio
    negative_sharpe = (df["sharpe_ratio"] < 0).sum()
    print("Negative Sharpe Ratios:", negative_sharpe)

    # Validate Expense Ratio
    invalid_expense = (
        (df["expense_ratio_pct"] < 0.1) |
        (df["expense_ratio_pct"] > 2.5)
    ).sum()

    print("Invalid Expense Ratios:", invalid_expense)

    # Remove duplicate rows
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()

    print("Duplicate Rows Removed:", duplicates)

    # Save cleaned dataset
    output_file = "data/processed/clean_scheme_performance.csv"
    df.to_csv(output_file, index=False)

    print("\nDataset cleaned successfully.")
    print("Saved at:", output_file)

    print("=" * 70)
    print("SCHEME PERFORMANCE CLEANING COMPLETED")
    print("=" * 70)


if __name__ == "__main__":
    clean_scheme_performance()