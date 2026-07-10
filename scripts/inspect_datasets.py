"""
============================================================
Mutual Fund Analytics Capstone
File Name : inspect_datasets.py
Author    : Kushma Reddy H

Description:
This script inspects all raw datasets by displaying their
shape, column names, data types, sample records,
and missing values.
============================================================
"""

import os
import pandas as pd


DATA_PATH = "data/raw"


def inspect_datasets():
    """
    Inspect all CSV datasets available in the raw data folder.

    Returns:
        None
    """

    # Get all CSV files
    csv_files = [
        file for file in os.listdir(DATA_PATH)
        if file.endswith(".csv")
    ]

    print("=" * 70)
    print("DATASET INSPECTION")
    print("=" * 70)

    # Inspect each dataset
    for file in csv_files:

        print("\n" + "=" * 70)
        print(f"Dataset: {file}")
        print("=" * 70)

        file_path = os.path.join(DATA_PATH, file)

        # Load dataset
        df = pd.read_csv(file_path)

        # Display dataset information
        print("\nShape:")
        print(df.shape)

        print("\nColumn Names:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

    print("\n" + "=" * 70)
    print("DATASET INSPECTION COMPLETED")
    print("=" * 70)


if __name__ == "__main__":
    inspect_datasets()