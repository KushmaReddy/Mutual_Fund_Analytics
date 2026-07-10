"""
============================================================
Mutual Fund Analytics Capstone
File Name : load_datasets.py
Author    : Kushma Reddy H

Description:
This script loads all CSV datasets from the raw data folder
and stores them in a dictionary for further processing.
============================================================
"""

import os
import pandas as pd


DATA_PATH = "data/raw"


def load_datasets():
    """
    Load all CSV datasets from the raw folder.

    Returns:
        dict: Dictionary containing all loaded DataFrames.
    """

    # Dictionary to store datasets
    datasets = {}

    # Get all CSV files
    csv_files = [
        file for file in os.listdir(DATA_PATH)
        if file.endswith(".csv")
    ]

    print("=" * 60)
    print("LOADING DATASETS")
    print("=" * 60)

    # Read each CSV file
    for file in csv_files:

        file_path = os.path.join(DATA_PATH, file)

        df = pd.read_csv(file_path)

        datasets[file] = df

        print(f"Loaded : {file}")
        print(f"Rows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")
        print("-" * 60)

    print("\nAll datasets loaded successfully!")

    return datasets


if __name__ == "__main__":
    load_datasets()