"""
============================================================
Mutual Fund Analytics Capstone
File Name : recommender.py
Author    : Kushma Reddy H

Description:
This script recommends the top three mutual fund schemes
based on the selected risk level. The recommendation is
made by ranking funds according to their Sharpe Ratio.
============================================================
"""

import pandas as pd


# Load cleaned scheme performance dataset
scheme = pd.read_csv("data/processed/clean_scheme_performance.csv")


def recommend_funds(risk_level):
    """
    Recommend the top three mutual funds for a given risk level.

    Parameters:
        risk_level (str): Risk category (e.g., Low, Moderate, High)

    Returns:
        pandas.DataFrame: Top three recommended mutual funds.
    """

    # Filter funds by selected risk level
    filtered = scheme[
        scheme["risk_grade"].str.lower() == risk_level.lower()
    ]

    # Rank funds by Sharpe Ratio
    recommendations = filtered.sort_values(
        by="sharpe_ratio",
        ascending=False
    )

    # Return top three recommendations
    return recommendations[
        [
            "scheme_name",
            "fund_house",
            "category",
            "risk_grade",
            "sharpe_ratio"
        ]
    ].head(3)


if __name__ == "__main__":
    print("=" * 60)
    print("MUTUAL FUND RECOMMENDATION SYSTEM")
    print("=" * 60)

    print(recommend_funds("Low"))