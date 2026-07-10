"""
============================================================
Mutual Fund Analytics Capstone
File Name : data_quality_report.py
Author    : Kushma Reddy H

Description:
This script generates a data quality report for all raw datasets.
It displays the number of rows, columns, duplicate records,
missing values, and data types for each CSV file.
============================================================
"""

import os
import pandas as pd


DATA_PATH = "data/raw"


def generate_data_quality_report():
    """
    Generate a data quality report for all CSV files
    available in the raw data folder.

    Returns:
        None
    """

    # Get all CSV files
    csv_files = [
        file for file in os.listdir(DATA_PATH)
        if file.endswith(".csv")
    ]

    print("=" * 80)
    print("DATA QUALITY REPORT")
    print("=" * 80)

    # Process each dataset
    for file in csv_files:

        file_path = os.path.join(DATA_PATH, file)

        # Load dataset
        df = pd.read_csv(file_path)

        print("\n" + "=" * 80)
        print(f"Dataset : {file}")
        print("=" * 80)

        print(f"Rows             : {df.shape[0]}")
        print(f"Columns          : {df.shape[1]}")
        print(f"Duplicate Rows   : {df.duplicated().sum()}")

        print("\nMissing Values")
        print(df.isnull().sum())

        print("\nData Types")
        print(df.dtypes)

    print("\n" + "=" * 80)
    print("DATA QUALITY ASSESSMENT COMPLETED")
    print("=" * 80)


if __name__ == "__main__":
    generate_data_quality_report()