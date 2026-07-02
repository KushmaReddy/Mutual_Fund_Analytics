-- ==========================================================
-- Query 1
-- Top 5 Funds by AUM
-- ==========================================================

SELECT
    scheme_name,
    aum_crore
FROM fact_performance
JOIN dim_fund
ON fact_performance.amfi_code = dim_fund.amfi_code
ORDER BY aum_crore DESC
LIMIT 5;
-- ==========================================================
-- Query 2
-- Average NAV Per Month
-- ==========================================================

SELECT
    strftime('%Y-%m', nav_date) AS month,
    ROUND(AVG(nav), 2) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;
-- ==========================================================
-- Query 3
-- SIP Transactions by Year
-- ==========================================================

SELECT
    strftime('%Y', transaction_date) AS year,
    COUNT(*) AS sip_transactions
FROM fact_transactions
WHERE transaction_type = 'Sip'
GROUP BY year
ORDER BY year;
-- ==========================================================
-- Query 4
-- Transactions by State
-- ==========================================================

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;
-- ==========================================================
-- Query 5
-- Funds with Expense Ratio Less Than 1%
-- ==========================================================

SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
JOIN dim_fund
ON fact_performance.amfi_code = dim_fund.amfi_code
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;
-- ==========================================================
-- Query 6
-- Top 5 Funds by 5-Year Return
-- ==========================================================

SELECT
    scheme_name,
    return_5yr_pct
FROM fact_performance
JOIN dim_fund
ON fact_performance.amfi_code = dim_fund.amfi_code
ORDER BY return_5yr_pct DESC
LIMIT 5;
-- ==========================================================
-- Query 6
-- Top 5 Funds by 5-Year Return
-- ==========================================================

SELECT
    scheme_name,
    return_5yr_pct
FROM fact_performance
JOIN dim_fund
ON fact_performance.amfi_code = dim_fund.amfi_code
ORDER BY return_5yr_pct DESC
LIMIT 5;
-- ==========================================================
-- Query 8
-- Total Investment Amount by Payment Mode
-- ==========================================================

SELECT
    payment_mode,
    ROUND(SUM(amount_inr), 2) AS total_investment
FROM fact_transactions
GROUP BY payment_mode
ORDER BY total_investment DESC;
-- ==========================================================
-- Query 9
-- Number of Investors by City Tier
-- ==========================================================

SELECT
    city_tier,
    COUNT(investor_id) AS total_investors
FROM fact_transactions
GROUP BY city_tier
ORDER BY total_investors DESC;