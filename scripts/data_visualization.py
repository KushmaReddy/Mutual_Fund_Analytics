"""
============================================================
Mutual Fund Analytics Capstone
File Name : data_visualization.py
Author    : Kushma Reddy H

Description:
This script generates basic visualizations from the cleaned
NAV history dataset and saves them in the outputs folder.
============================================================
"""

import os
import pandas as pd
import matplotlib.pyplot as plt


OUTPUT_PATH = "outputs"


def create_visualizations():
    """
    Generate NAV visualizations and save them as PNG images.

    Returns:
        None
    """

    print("=" * 70)
    print("DATA VISUALIZATION")
    print("=" * 70)

    # Load cleaned dataset
    df = pd.read_csv("data/processed/02_nav_history.csv")

    # Convert date column
    df["date"] = pd.to_datetime(
        df["date"],
        format="mixed",
        dayfirst=True,
        errors="coerce"
    )

    # Remove invalid dates
    df = df.dropna(subset=["date"])

    # Create output folder if needed
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    # --------------------------------------------------------
    # NAV Trend Chart
    # --------------------------------------------------------
    plt.figure(figsize=(12, 6))
    plt.plot(df["date"], df["nav"])
    plt.title("Mutual Fund NAV Trend")
    plt.xlabel("Date")
    plt.ylabel("NAV")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_PATH, "nav_trend.png"))
    plt.close()

    print("✓ NAV Trend Chart Saved")

    # --------------------------------------------------------
    # NAV Distribution
    # --------------------------------------------------------
    plt.figure(figsize=(8, 5))
    plt.hist(df["nav"], bins=30, edgecolor="black")
    plt.title("NAV Distribution")
    plt.xlabel("NAV")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_PATH, "nav_distribution.png"))
    plt.close()

    print("✓ NAV Distribution Chart Saved")

    # --------------------------------------------------------
    # NAV Box Plot
    # --------------------------------------------------------
    plt.figure(figsize=(6, 5))
    plt.boxplot(df["nav"])
    plt.title("NAV Box Plot")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_PATH, "nav_boxplot.png"))
    plt.close()

    print("✓ NAV Box Plot Saved")

    print("\n" + "=" * 70)
    print("VISUALIZATION COMPLETED SUCCESSFULLY")
    print("=" * 70)


if __name__ == "__main__":
    create_visualizations()