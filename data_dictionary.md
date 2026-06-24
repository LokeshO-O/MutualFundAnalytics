# Mutual Fund Analytics Data Dictionary

## Dataset: 01_fund_master_cleaned.csv

Source: 01_fund_master.csv

| Column            | Data Type | Description                                  |
| ----------------- | --------- | -------------------------------------------- |
| amfi_code         | Integer   | Unique mutual fund identifier issued by AMFI |
| fund_house        | Text      | Mutual fund company name                     |
| scheme_name       | Text      | Mutual fund scheme name                      |
| category          | Text      | Fund category                                |
| sub_category      | Text      | Fund sub-category                            |
| plan              | Text      | Direct or Regular plan                       |
| launch_date       | Date      | Fund launch date                             |
| benchmark         | Text      | Benchmark index                              |
| expense_ratio_pct | Float     | Expense ratio percentage                     |
| fund_manager      | Text      | Fund manager name                            |

---

## Dataset: 02_nav_history_cleaned.csv

Source: 02_nav_history.csv

| Column    | Data Type | Description                       |
| --------- | --------- | --------------------------------- |
| amfi_code | Integer   | Mutual fund identifier            |
| date      | Date      | NAV date                          |
| nav       | Float     | NAV (Net Asset Value) of the fund |

---

## Dataset: 03_aum_by_fund_house_cleaned.csv

Source: 03_aum_by_fund_house.csv

| Column         | Data Type | Description                                 |
| -------------- | --------- | ------------------------------------------- |
| date           | Date      | Reporting date                              |
| fund_house     | Text      | Fund house name                             |
| aum_lakh_crore | Float     | AUM (Assets Under Management) in lakh crore |
| aum_crore      | Float     | AUM in crore                                |
| num_schemes    | Integer   | Number of schemes managed                   |

---

## Dataset: 04_monthly_sip_inflows_cleaned.csv

Source: 04_monthly_sip_inflows.csv

| Column                    | Data Type | Description                                      |
| ------------------------- | --------- | ------------------------------------------------ |
| month                     | Text      | Reporting month                                  |
| sip_inflow_crore          | Float     | SIP (Systematic Investment Plan) inflow in crore |
| active_sip_accounts_crore | Float     | Active SIP accounts                              |
| new_sip_accounts_lakh     | Float     | New SIP accounts opened                          |
| sip_aum_lakh_crore        | Float     | SIP AUM                                          |
| yoy_growth_pct            | Float     | Year-over-Year growth percentage                 |

---

## Dataset: 05_category_inflows_cleaned.csv

Source: 05_category_inflows.csv

| Column           | Data Type | Description         |
| ---------------- | --------- | ------------------- |
| month            | Text      | Reporting month     |
| category         | Text      | Fund category       |
| net_inflow_crore | Float     | Net inflow in crore |

---

## Dataset: 06_industry_folio_count_cleaned.csv

Source: 06_industry_folio_count.csv

| Column              | Data Type | Description           |
| ------------------- | --------- | --------------------- |
| month               | Text      | Reporting month       |
| total_folios_crore  | Float     | Total investor folios |
| equity_folios_crore | Float     | Equity folios         |
| debt_folios_crore   | Float     | Debt folios           |
| hybrid_folios_crore | Float     | Hybrid folios         |
| others_folios_crore | Float     | Other folios          |

---

## Dataset: 07_scheme_performance_cleaned.csv

Source: 07_scheme_performance.csv

| Column            | Data Type | Description                  |
| ----------------- | --------- | ---------------------------- |
| amfi_code         | Integer   | Fund identifier              |
| return_1yr_pct    | Float     | One-year return percentage   |
| return_3yr_pct    | Float     | Three-year return percentage |
| return_5yr_pct    | Float     | Five-year return percentage  |
| alpha             | Float     | Alpha performance metric     |
| beta              | Float     | Beta risk metric             |
| sharpe_ratio      | Float     | Risk-adjusted return measure |
| expense_ratio_pct | Float     | Expense ratio percentage     |
| aum_crore         | Float     | Assets Under Management      |

---

## Dataset: 08_investor_transactions_cleaned.csv

Source: 08_investor_transactions.csv

| Column           | Data Type | Description                 |
| ---------------- | --------- | --------------------------- |
| investor_id      | Text      | Investor identifier         |
| transaction_date | Date      | Transaction date            |
| transaction_type | Text      | SIP, Lumpsum, or Redemption |
| amount_inr       | Float     | Transaction amount in INR   |
| state            | Text      | Investor state              |
| city             | Text      | Investor city               |
| kyc_status       | Text      | KYC verification status     |

---

## Dataset: 09_portfolio_holdings_cleaned.csv

Source: 09_portfolio_holdings.csv

| Column       | Data Type | Description                     |
| ------------ | --------- | ------------------------------- |
| amfi_code    | Integer   | Fund identifier                 |
| stock_symbol | Text      | Stock ticker symbol             |
| stock_name   | Text      | Company name                    |
| sector       | Text      | Industry sector                 |
| weight_pct   | Float     | Portfolio allocation percentage |

---

## Dataset: 10_benchmark_indices_cleaned.csv

Source: 10_benchmark_indices.csv

| Column      | Data Type | Description          |
| ----------- | --------- | -------------------- |
| date        | Date      | Trading date         |
| index_name  | Text      | Benchmark index name |
| close_value | Float     | Closing index value  |
