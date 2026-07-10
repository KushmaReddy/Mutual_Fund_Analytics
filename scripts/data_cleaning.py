"""
============================================================
Mutual Fund Analytics Capstone
File Name : data_cleaning.py
Author    : Kushma Reddy H

Description:
This script performs generic data cleaning on all raw CSV files by:
1. Reading all CSV files from the raw folder
2. Removing duplicate records
3. Checking missing values
4. Standardizing column names
5. Saving cleaned files into the processed folder
============================================================
"""

import os
import pandas as pd


RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"


def clean_all_datasets():

    # Create processed folder if it does not exist
    os.makedirs(PROCESSED_PATH, exist_ok=True)

    print("=" * 70)
    print("DATA CLEANING PROCESS STARTED")
    print("=" * 70)

    # Get all CSV files
    csv_files = [
        file for file in os.listdir(RAW_PATH)
        if file.endswith(".csv")
    ]

    # Process each CSV file
    for file in csv_files:

        print("\n" + "=" * 70)
        print(f"Cleaning: {file}")
        print("=" * 70)

        file_path = os.path.join(RAW_PATH, file)

        # Load dataset
        df = pd.read_csv(file_path)

        print(f"Original Shape : {df.shape}")

        # Remove duplicate rows
        duplicates = df.duplicated().sum()
        df = df.drop_duplicates()

        print(f"Duplicates Removed : {duplicates}")

        # Check missing values
        print("\nMissing Values:")
        print(df.isnull().sum())

        # Standardize column names
        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        print("\nUpdated Column Names:")
        print(df.columns.tolist())

        # Save cleaned dataset
        output_file = os.path.join(PROCESSED_PATH, file)
        df.to_csv(output_file, index=False)

        print(f"\nSaved Clean Dataset -> {output_file}")

    print("\n" + "=" * 70)
    print("ALL DATASETS CLEANED SUCCESSFULLY")
    print("=" * 70)


if __name__ == "__main__":
    clean_all_datasets()