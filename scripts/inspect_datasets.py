# ==========================================================
# Mutual Fund Analytics Project
# Day 1 - Data Inspection
# ==========================================================

import pandas as pd
import os

DATA_PATH = "data/raw"

csv_files = [file for file in os.listdir(DATA_PATH) if file.endswith(".csv")]

for file in csv_files:

    print("\n" + "=" * 70)
    print(f"Dataset: {file}")
    print("=" * 70)

    file_path = os.path.join(DATA_PATH, file)

    df = pd.read_csv(file_path)

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