-- 1. Top 5 Funds by AUM (Assets Under Management)

SELECT
    scheme_name,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average NAV (Net Asset Value) per Month

SELECT
    SUBSTR(date, 1, 7) AS month,
    AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY SUBSTR(date, 1, 7)
ORDER BY month;


-- 3. SIP (Systematic Investment Plan) YoY Growth

SELECT
    month,
    yoy_growth_pct
FROM sip_inflows
ORDER BY month;


-- 4. Transactions by State

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 5. Funds with Expense Ratio below 1%

SELECT
    amfi_code,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;


-- 6. Total Investment Amount by Transaction Type

SELECT
    transaction_type,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;


-- 7. Average 3-Year Return by Fund House

SELECT
    fund_house,
    AVG(return_3yr_pct) AS avg_return_3yr
FROM fact_performance
GROUP BY fund_house
ORDER BY avg_return_3yr DESC;


-- 8. Top 10 Stocks by Portfolio Weight

SELECT
    stock_name,
    weight_pct
FROM portfolio_holdings
ORDER BY weight_pct DESC
LIMIT 10;


-- 9. Average Benchmark Index Value

SELECT
    index_name,
    AVG(close_value) AS avg_close
FROM benchmark_indices
GROUP BY index_name;


-- 10. Highest Sharpe Ratio Funds

SELECT
    scheme_name,
    sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;