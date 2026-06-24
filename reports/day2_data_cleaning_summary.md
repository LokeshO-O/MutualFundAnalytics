# Day 2 - Data Cleaning & Database Design Summary

## Objective

Clean mutual fund datasets, design a SQLite database schema, load processed data, and create analytical SQL queries.

---

## Datasets Cleaned

1. Fund Master
2. NAV (Net Asset Value) History
3. AUM (Assets Under Management) by Fund House
4. Monthly SIP (Systematic Investment Plan) Inflows
5. Category Inflows
6. Industry Folio Count
7. Scheme Performance
8. Investor Transactions
9. Portfolio Holdings
10. Benchmark Indices

---

## Data Cleaning Activities

### NAV History
- Parsed dates to datetime format
- Sorted by AMFI code and date
- Removed duplicate records
- Validated NAV > 0
- Applied forward-fill logic for missing values

### Investor Transactions
- Standardized transaction types
- Validated transaction amounts
- Converted transaction dates
- Verified KYC status values

### Scheme Performance
- Validated return columns
- Checked expense ratio range
- Flagged anomalies
- Removed duplicates

---

## Database Design

Created SQLite database:

bluestock_mf.db

Main Tables:
- dim_fund
- fact_nav
- fact_transactions
- fact_performance
- fact_aum

Schema stored in:
sql/schema.sql

---

## Data Loading

Loaded cleaned datasets into SQLite using:
- SQLAlchemy
- Pandas df.to_sql()

Verified row counts after loading.

---

## SQL Analytics

Created 10 analytical SQL queries including:

- Top 5 funds by AUM
- Average monthly NAV
- SIP YoY growth
- Transactions by state
- Funds with expense ratio below 1%
- Additional fund performance and investor analysis queries

Stored in:
sql/queries.sql

---

