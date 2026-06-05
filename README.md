# Growth Analytics Toolkit

A lightweight Python toolkit for evaluating paid acquisition performance across channels using CAC, LTV, payback period, contribution margin, and scale/efficiency tradeoffs.

This project is designed as a clean, recruiter-safe example of how I think about growth marketing analytics: turning channel inputs into decision-ready metrics.

## What it does

- Calculates CAC by channel
- Estimates gross margin-adjusted LTV
- Calculates LTV:CAC ratio
- Estimates payback period in months
- Compares channels by efficiency and scale
- Flags channels that may be candidates to scale, hold, or review
- Uses sample data only

## Why this matters

In performance marketing, front-end acquisition volume is not enough. Good growth decisions require connecting spend, conversion, revenue quality, margin, and payback. This toolkit reflects the kind of analysis I use to support budget allocation, experimentation, and performance readouts.

## Example output

```text
Channel: Paid Search
CAC: $42.50
Estimated LTV: $185.00
LTV:CAC: 4.35
Payback Period: 3.2 months
Recommendation: Scale carefully
```

## Project structure

```text
growth-analytics-toolkit/
├── main.py
├── metrics.py
├── recommendations.py
├── sample_channel_data.csv
├── requirements.txt
├── LICENSE
└── README.md
```

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python main.py
```

For Mac/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

## Files

- `main.py`: Loads sample channel data and prints a channel performance summary
- `metrics.py`: Calculates CAC, LTV, LTV:CAC, and payback period
- `recommendations.py`: Adds simple scale, hold, review, or pause recommendations
- `sample_channel_data.csv`: Fictional sample data for paid acquisition channels

## Notes

This project uses fictional sample data only and does not include any proprietary company data.
