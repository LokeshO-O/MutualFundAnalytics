# Day 1 - Data Quality Summary

## Dataset Overview

- Successfully loaded 10 CSV datasets.
- Dataset structures reviewed using shape, dtypes and head().
- No file loading issues encountered.

## Anomalies

1. Multiple datasets contain date columns stored as object datatype instead of datetime.
2. monthly_sip_inflows contains missing values in yoy_growth_pct.
3. AUM dataset contains similar metrics in two units (aum_lakh_crore and aum_crore).
4. No obvious schema inconsistencies found.
5. AMFI codes appear consistently formatted as integers across datasets.

## Observations

1. Several datasets contain date columns stored as object datatype rather than datetime.
2. monthly_sip_inflows dataset contains missing values in yoy_growth_pct.
3. AUM dataset contains two related metrics:
   - aum_lakh_crore
   - aum_crore
4. AMFI codes are consistently stored as integers.
5. Fund master contains:
   - 10 fund houses
   - 2 categories
   - 12 sub-categories
   - 5 risk categories

## AMFI Code Validation

- Fund Master Codes: 40
- NAV History Codes: 40

Result:
All AMFI codes from fund_master are present in nav_history.

## Conclusion

Initial data ingestion completed successfully.
Datasets are ready for further cleaning, transformation and analysis.