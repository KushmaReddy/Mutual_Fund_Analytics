"""
============================================================
Mutual Fund Analytics Capstone
File Name : live_nav_fetch.py
Author    : Kushma Reddy H

Description:
This script fetches live NAV data from the MFAPI,
displays fund information, and saves the NAV history
to a CSV file.
============================================================
"""

import requests
import pandas as pd


def fetch_live_nav():
    """
    Fetch live NAV data from MFAPI and save it as a CSV file.

    Returns:
        None
    """

    # API URL
    url = "https://api.mfapi.in/mf/125497"

    print("=" * 60)
    print("FETCHING LIVE NAV DATA")
    print("=" * 60)

    # Send GET request
    response = requests.get(url)

    # Check API response
    if response.status_code == 200:

        print("API Connected Successfully!\n")

        data = response.json()

        # Display fund information
        meta = data["meta"]

        print("Fund Name   :", meta["scheme_name"])
        print("Fund House  :", meta["fund_house"])
        print("Scheme Type :", meta["scheme_type"])

        # Convert NAV history to DataFrame
        nav_df = pd.DataFrame(data["data"])

        print("\nFirst 5 Records")
        print(nav_df.head())

        # Save CSV
        output_path = "data/raw/live_nav.csv"
        nav_df.to_csv(output_path, index=False)

        print("\nCSV Saved Successfully!")
        print("Location :", output_path)

    else:
        print("Failed to Fetch Data")
        print("Status Code :", response.status_code)


if __name__ == "__main__":
    fetch_live_nav()