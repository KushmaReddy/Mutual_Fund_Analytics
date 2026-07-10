"""
============================================================
Mutual Fund Analytics Capstone
File Name : explore_fund_master.py
Author    : Kushma Reddy H

Description:
This script explores the Fund Master dataset by displaying
the total number of schemes, column names, sample records,
fund houses, categories, sub-categories, and risk grades.
============================================================
"""

import pandas as pd


def explore_fund_master():
    """
    Explore the Fund Master dataset and display
    important information.

    Returns:
        None
    """

    print("=" * 70)
    print("FUND MASTER EXPLORATION")
    print("=" * 70)

    # Load Fund Master Dataset
    df = pd.read_csv("data/raw/01_fund_master.csv")

    # Total Schemes
    print("\nTotal Schemes:")
    print(len(df))

    # Column Names
    print("\nColumn Names:")
    print(df.columns.tolist())

    # First Five Records
    print("\nFirst 5 Rows:")
    print(df.head())

    # Fund Houses
    if "fund_house" in df.columns:
        print("\nUnique Fund Houses:")
        print(df["fund_house"].unique())

    # Categories
    if "category" in df.columns:
        print("\nUnique Categories:")
        print(df["category"].unique())

    # Sub Categories
    if "sub_category" in df.columns:
        print("\nUnique Sub Categories:")
        print(df["sub_category"].unique())

    # Risk Information
    if "risk_grade" in df.columns:
        print("\nUnique Risk Grades:")
        print(df["risk_grade"].unique())

    elif "risk" in df.columns:
        print("\nUnique Risk:")
        print(df["risk"].unique())

    elif "riskometer" in df.columns:
        print("\nUnique Riskometer:")
        print(df["riskometer"].unique())

    elif "risk_level" in df.columns:
        print("\nUnique Risk Level:")
        print(df["risk_level"].unique())

    else:
        print("\nRisk column not found.")

    print("\n" + "=" * 70)
    print("FUND MASTER EXPLORATION COMPLETED")
    print("=" * 70)


if __name__ == "__main__":
    explore_fund_master()