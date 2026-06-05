import pandas as pd


def calculate_channel_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate core acquisition efficiency metrics by channel.

    Expected columns:
    - channel
    - spend
    - new_customers
    - avg_monthly_revenue_per_customer
    - gross_margin
    - monthly_churn_rate
    """
    required_columns = {
        "channel",
        "spend",
        "new_customers",
        "avg_monthly_revenue_per_customer",
        "gross_margin",
        "monthly_churn_rate",
    }

    missing_columns = required_columns - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

    results = df.copy()

    results["cac"] = results["spend"] / results["new_customers"]

    # Simple steady-state LTV estimate:
    # monthly revenue * gross margin / churn rate
    results["estimated_ltv"] = (
        results["avg_monthly_revenue_per_customer"]
        * results["gross_margin"]
        / results["monthly_churn_rate"]
    )

    results["ltv_to_cac"] = results["estimated_ltv"] / results["cac"]

    # Payback months:
    # CAC / monthly gross profit per customer
    monthly_gross_profit = (
        results["avg_monthly_revenue_per_customer"] * results["gross_margin"]
    )
    results["payback_months"] = results["cac"] / monthly_gross_profit

    numeric_columns = ["cac", "estimated_ltv", "ltv_to_cac", "payback_months"]
    results[numeric_columns] = results[numeric_columns].round(2)

    return results
