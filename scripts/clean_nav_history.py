"""
============================================================
Mutual Fund Analytics Capstone
File Name : clean_nav_history.py
Author    : Kushma Reddy H

Description:
This script cleans the NAV History dataset by:
1. Loading the raw NAV history data
2. Converting date column to datetime
3. Sorting records by AMFI Code and Date
4. Filling missing NAV values
5. Removing duplicate records
6. Checking for invalid NAV values
7. Saving the cleaned dataset
============================================================
"""

import pandas as pd


def clean_nav_history():

    print("=" * 70)
    print("NAV HISTORY CLEANING")
    print("=" * 70)

    # Load raw dataset
    df = pd.read_csv("data/raw/02_nav_history.csv")

    print("\nOriginal Shape:", df.shape)

    # Convert date column to datetime
    df["date"] = pd.to_datetime(df["date"])

    print("Date column converted successfully.")

    # Sort data by AMFI Code and Date
    df = df.sort_values(by=["amfi_code", "date"])

    print("Data sorted successfully.")

    # Forward fill missing NAV values
    df["nav"] = df.groupby("amfi_code")["nav"].ffill()

    print("Missing NAV values filled.")

    # Remove duplicate rows
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()

    print("Duplicate rows removed:", duplicates)

    # Check invalid NAV values
    invalid_nav = (df["nav"] <= 0).sum()

    print("Invalid NAV values:", invalid_nav)

    # Save cleaned dataset
    output_file = "data/processed/clean_nav.csv"
    df.to_csv(output_file, index=False)

    print("\nClean dataset saved successfully.")
    print("Location:", output_file)

    print("=" * 70)
    print("NAV HISTORY CLEANING COMPLETED")
    print("=" * 70)


if __name__ == "__main__":
    clean_nav_history()