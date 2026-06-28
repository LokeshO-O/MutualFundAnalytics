# Day 4 - Fund Performance Analytics Summary

## Objective

The objective of Day 4 was to evaluate the performance of mutual fund schemes using historical NAV data and benchmark indices. Various return and risk metrics were computed to compare fund performance and generate an overall ranking.

## Tasks Completed

* Computed daily returns for all mutual fund schemes from historical NAV data.
* Calculated CAGR for 1-year, 3-year, and the available historical period (~4.4 years).
* Computed Sharpe Ratio using a 6.5% risk-free rate.
* Calculated Sortino Ratio using downside volatility.
* Estimated Alpha and Beta for each fund using NIFTY100 benchmark returns through linear regression.
* Calculated Maximum Drawdown and identified the worst drawdown period for each fund.
* Generated a composite Fund Scorecard (0–100) using weighted rankings based on 3-year return, Sharpe Ratio, Alpha, expense ratio, and Maximum Drawdown.
* Compared the top five funds against NIFTY50 and NIFTY100 using a normalized benchmark comparison chart.
* Computed Tracking Error for the top-performing funds.
* Exported analysis outputs as CSV files and saved the benchmark comparison chart.

## Deliverables

* `notebooks/Performance_Analytics.ipynb`
* `outputs/fund_scorecard.csv`
* `outputs/alpha_beta.csv`
* `charts/performance/benchmark_comparison.png`

## Outcome

The performance analytics workflow provides a comprehensive evaluation of mutual fund performance by combining return, risk, benchmark comparison, and composite scoring. The generated outputs can be used for further visualization, reporting, and investment performance analysis.
