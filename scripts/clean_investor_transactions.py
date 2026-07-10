"""
============================================================
Mutual Fund Analytics Capstone
File Name : clean_investor_transactions.py
Author    : Kushma Reddy H

Description:
This script cleans the investor transactions dataset by:
1. Loading the raw transaction data
2. Converting transaction dates
3. Removing duplicate records
4. Validating transaction amounts
5. Standardizing transaction types
6. Checking KYC status
7. Saving the cleaned dataset
============================================================
"""

import pandas as pd


def clean_investor_transactions():

    print("=" * 70)
    print("INVESTOR TRANSACTIONS CLEANING")
    print("=" * 70)

    # Load raw dataset
    df = pd.read_csv("data/raw/08_investor_transactions.csv")

    print("\nOriginal Shape:", df.shape)

    # Convert transaction date to datetime format
    df["transaction_date"] = pd.to_datetime(df["transaction_date"])

    # Remove duplicate rows
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()

    print("Duplicate rows removed:", duplicates)

    # Check invalid transaction amounts
    invalid_amount = (df["amount_inr"] <= 0).sum()
    print("Invalid Amount Records:", invalid_amount)

    # Standardize transaction type values
    df["transaction_type"] = (
        df["transaction_type"]
        .str.strip()
        .str.title()
    )

    # Display KYC status summary
    print("\nKYC Status Summary:")
    print(df["kyc_status"].value_counts())

    # Save cleaned dataset
    output_file = "data/processed/clean_transactions.csv"
    df.to_csv(output_file, index=False)

    print("\nCleaned transactions saved successfully.")
    print("Location:", output_file)

    print("=" * 70)
    print("INVESTOR TRANSACTION CLEANING COMPLETED")
    print("=" * 70)


if __name__ == "__main__":
    clean_investor_transactions()
