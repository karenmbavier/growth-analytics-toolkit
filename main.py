from pathlib import Path

import pandas as pd

from metrics import calculate_channel_metrics
from recommendations import recommend_action


def main() -> None:
    data_path = Path("sample_channel_data.csv")
    df = pd.read_csv(data_path)

    results = calculate_channel_metrics(df)
    results["recommendation"] = results.apply(recommend_action, axis=1)

    display_columns = [
        "channel",
        "spend",
        "new_customers",
        "cac",
        "estimated_ltv",
        "ltv_to_cac",
        "payback_months",
        "recommendation",
    ]

    print("\nGrowth Analytics Channel Summary\n")
    print(results[display_columns].to_string(index=False))


if __name__ == "__main__":
    main()
