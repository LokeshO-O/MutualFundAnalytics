import pandas as pd


# Load fund performance dataset
performance = pd.read_csv("data/processed/07_scheme_performance_cleaned.csv")


def recommend_funds(risk_level):
    """
    Recommend top 3 mutual funds based on risk appetite.
    """

    risk_level = risk_level.strip().title()

    funds = performance[
        performance["risk_grade"] == risk_level
    ].copy()

    if funds.empty:
        print("\nNo funds found for the selected risk level.")
        return

    recommendations = (
        funds.sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(3)
    )

    print("\nRecommended Funds\n")
    print(
        recommendations[
            [
                "scheme_name",
                "category",
                "risk_grade",
                "sharpe_ratio",
                "return_3yr_pct",
                "expense_ratio_pct",
            ]
        ].to_string(index=False)
    )


if __name__ == "__main__":

    print("=" * 55)
    print("Bluestock Mutual Fund Recommender")
    print("=" * 55)

    print("\nAvailable Risk Levels:")
    print("- Low")
    print("- Moderate")
    print("- High")

    risk = input("\nEnter your risk appetite: ")

    recommend_funds(risk)