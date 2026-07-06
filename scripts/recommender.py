import pandas as pd

scheme = pd.read_csv("data/processed/clean_scheme_performance.csv")

def recommend_funds(risk_level):
    filtered = scheme[scheme["risk_grade"].str.lower() == risk_level.lower()]

    recommendations = filtered.sort_values(
        by="sharpe_ratio",
        ascending=False
    )

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
    print(recommend_funds("Low"))