# ==========================================================
# Mutual Fund Analytics Project
# Day 1 - Data Ingestion
# ==========================================================

import os
import pandas as pd

# Path to the raw data folder
DATA_PATH = "data/raw"

# Check if the folder exists
if not os.path.exists(DATA_PATH):
    print(f"Error: Folder '{DATA_PATH}' not found!")
    exit()

# Get all CSV files
files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

print("=" * 60)
print("Available Datasets")
print("=" * 60)

# Print all dataset names
for file in files:
    print(file)

print("=" * 60)
print(f"Total Datasets Found: {len(files)}")
print("=" * 60)
