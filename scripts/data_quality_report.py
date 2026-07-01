import pandas as pd
import os

DATA_PATH = "data/raw"

csv_files = [file for file in os.listdir(DATA_PATH) if file.endswith(".csv")]

print("=" * 80)
print("DATA QUALITY REPORT")
print("=" * 80)

for file in csv_files:

    file_path = os.path.join(DATA_PATH, file)

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
print("Data Quality Assessment Completed")
print("=" * 80)