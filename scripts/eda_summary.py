"""
============================================================
Mutual Fund Analytics Capstone
File Name : eda_summary.py
Author    : Kushma Reddy H

Description:
This script performs Exploratory Data Analysis (EDA) on the
cleaned NAV history dataset. It displays dataset structure,
summary statistics, and key insights.
============================================================
"""

import pandas as pd


def perform_eda():
    """
    Perform Exploratory Data Analysis (EDA)
    on the cleaned NAV history dataset.

    Returns:
        None
    """

    print("=" * 70)
    print("EXPLORATORY DATA ANALYSIS")
    print("=" * 70)

    # Load cleaned dataset
    df = pd.read_csv("data/processed/02_nav_history.csv")

    # Dataset information
    print("\nDataset Shape")
    print(df.shape)

    print("\nColumn Names")
    print(df.columns.tolist())

    print("\nFirst 5 Rows")
    print(df.head())

    print("\nLast 5 Rows")
    print(df.tail())

    # Summary statistics
    print("\nSummary Statistics")
    print(df.describe())

    # Basic metrics
    print("\nTotal Records")
    print(len(df))

    print("\nDate Range")
    print("From :", df["date"].min())
    print("To   :", df["date"].max())

    print("\nAverage NAV")
    print(df["nav"].mean())

    print("\nHighest NAV")
    print(df["nav"].max())

    print("\nLowest NAV")
    print(df["nav"].min())

    print("\nMedian NAV")
    print(df["nav"].median())

    print("\nStandard Deviation")
    print(df["nav"].std())

    print("\n" + "=" * 70)
    print("EDA COMPLETED SUCCESSFULLY")
    print("=" * 70)


if __name__ == "__main__":
    perform_eda()