import pandas as pd

print("=" * 70)
print("VALIDATING AMFI CODES")
print("=" * 70)

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Unique AMFI codes
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Missing codes
missing_codes = nav_codes - fund_codes

print("\nTotal AMFI Codes in Fund Master :", len(fund_codes))
print("Total AMFI Codes in NAV History :", len(nav_codes))

if len(missing_codes) == 0:
    print("\n✅ All NAV History AMFI codes exist in Fund Master.")
else:
    print("\n❌ Missing AMFI Codes:")
    print(missing_codes)

print("\nValidation Completed")
print("=" * 70)