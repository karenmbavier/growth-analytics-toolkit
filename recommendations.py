import pandas as pd


def recommend_action(row: pd.Series) -> str:
    """Create a simple channel-level recommendation.

    This is intentionally lightweight. In a production setting, this logic would
    include confidence intervals, incrementality, cohort quality, and budget
    constraints.
    """
    if row["ltv_to_cac"] >= 4 and row["payback_months"] <= 4:
        return "Scale carefully"

    if row["ltv_to_cac"] >= 3 and row["payback_months"] <= 6:
        return "Hold and optimize"

    if row["ltv_to_cac"] >= 2:
        return "Review before scaling"

    return "Pause or rebuild"
