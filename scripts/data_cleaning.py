import os
import pandas as pd

RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"

# Create processed folder if it doesn't exist
os.makedirs(PROCESSED_PATH, exist_ok=True)

print("=" * 70)
print("DATA CLEANING PROCESS STARTED")
print("=" * 70)

# Get all CSV files
csv_files = [file for file in os.listdir(RAW_PATH) if file.endswith(".csv")]

for file in csv_files:

    print("\n" + "=" * 70)
    print(f"Cleaning: {file}")
    print("=" * 70)

    file_path = os.path.join(RAW_PATH, file)

    df = pd.read_csv(file_path)

    print(f"Original Shape : {df.shape}")

    # Remove duplicate rows
    duplicates = df.duplicated().sum()
    df = df.drop_duplicates()

    print(f"Duplicates Removed : {duplicates}")

    # Missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    print("\nUpdated Column Names:")
    print(df.columns.tolist())

    # Save cleaned dataset
    output_file = os.path.join(PROCESSED_PATH, file)

    df.to_csv(output_file, index=False)

    print(f"\nSaved Clean Dataset -> {output_file}")

print("\n" + "=" * 70)
print("ALL DATASETS CLEANED SUCCESSFULLY")
print("=" * 70)