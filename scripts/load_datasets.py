# ==========================================================
# Mutual Fund Analytics Project
# Day 1 - Load All Datasets
# ==========================================================

import pandas as pd
import os

# Folder containing CSV files
DATA_PATH = "data/raw"

# Dictionary to store DataFrames
datasets = {}

# Get all CSV files
csv_files = [file for file in os.listdir(DATA_PATH) if file.endswith(".csv")]

print("=" * 60)
print("Loading Datasets")
print("=" * 60)

# Read every CSV file
for file in csv_files:

    file_path = os.path.join(DATA_PATH, file)

    df = pd.read_csv(file_path)

    datasets[file] = df

    print(f"Loaded: {file}")
    print(f"Rows : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")
    print("-" * 60)

print("\nAll datasets loaded successfully!")