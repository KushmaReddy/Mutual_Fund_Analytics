-- ==========================================================
-- Mutual Fund Analytics Database Schema
-- ==========================================================

DROP TABLE IF EXISTS dim_fund;

CREATE TABLE dim_fund (

    amfi_code INTEGER PRIMARY KEY,

    fund_house TEXT,

    scheme_name TEXT,

    category TEXT,

    sub_category TEXT,

    plan TEXT,

    launch_date TEXT,

    benchmark TEXT,

    expense_ratio_pct REAL,

    exit_load_pct REAL,

    min_sip_amount REAL,

    min_lumpsum_amount REAL,

    fund_manager TEXT,

    risk_category TEXT,

    sebi_category_code TEXT

);
-- ==========================================================
-- NAV Fact Table
-- ==========================================================

DROP TABLE IF EXISTS fact_nav;

CREATE TABLE fact_nav (

    amfi_code INTEGER,

    nav_date DATE,

    nav REAL,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)

);
-- ==========================================================
-- Transactions Fact Table
-- ==========================================================

DROP TABLE IF EXISTS fact_transactions;

CREATE TABLE fact_transactions (

    investor_id TEXT,

    transaction_date DATE,

    amfi_code INTEGER,

    transaction_type TEXT,

    amount_inr REAL,

    state TEXT,

    city TEXT,

    city_tier TEXT,

    age_group TEXT,

    gender TEXT,

    annual_income_lakh REAL,

    payment_mode TEXT,

    kyc_status TEXT,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)

);
-- ==========================================================
-- Performance Fact Table
-- ==========================================================

DROP TABLE IF EXISTS fact_performance;

CREATE TABLE fact_performance (

    amfi_code INTEGER,

    return_1yr_pct REAL,

    return_3yr_pct REAL,

    return_5yr_pct REAL,

    alpha REAL,

    beta REAL,

    sharpe_ratio REAL,

    sortino_ratio REAL,

    std_dev_ann_pct REAL,

    max_drawdown_pct REAL,

    expense_ratio_pct REAL,

    aum_crore REAL,

    morningstar_rating INTEGER,

    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)

);