import requests
import pandas as pd
import os

# API URL
url = "https://api.mfapi.in/mf/125497"

print("=" * 60)
print("Fetching Live NAV Data")
print("=" * 60)

# Send GET request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:

    print("API Connected Successfully!\n")

    data = response.json()

    # Fund Information
    meta = data["meta"]

    print("Fund Name :", meta["scheme_name"])
    print("Fund House :", meta["fund_house"])
    print("Scheme Type :", meta["scheme_type"])

    # NAV History
    nav_df = pd.DataFrame(data["data"])

    print("\nFirst 5 Records")
    print(nav_df.head())

    # Save CSV
    output_path = "data/raw/live_nav.csv"

    nav_df.to_csv(output_path, index=False)

    print("\nCSV Saved Successfully!")
    print(output_path)

else:

    print("Failed to Fetch Data")
    print("Status Code :", response.status_code)