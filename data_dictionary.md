# Data Dictionary

## Project
Mutual Fund Analytics Capstone Project

## Dataset Information

### 1. fund_master.csv
| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | Integer | Unique AMFI Scheme Code |
| fund_house | Text | Mutual Fund Company |
| scheme_name | Text | Name of Scheme |
| category | Text | Fund Category |
| sub_category | Text | Fund Sub Category |
| risk_grade | Text | Risk Level |

### 2. nav_history.csv
| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | Integer | AMFI Scheme Code |
| nav_date | Date | NAV Date |
| nav | Float | Net Asset Value |
| daily_return | Float | Daily Return |

### 3. investor_transactions.csv
| Column | Data Type | Description |
|--------|-----------|-------------|
| transaction_id | Integer | Unique Transaction ID |
| investor_id | Integer | Investor ID |
| transaction_type | Text | SIP / Lumpsum / Redemption |
| amount | Float | Transaction Amount |
| transaction_date | Date | Transaction Date |
| state | Text | Investor State |
| kyc_status | Text | KYC Verification Status |

### 4. scheme_performance.csv
| Column | Data Type | Description |
|--------|-----------|-------------|
| amfi_code | Integer | AMFI Scheme Code |
| expense_ratio | Float | Expense Ratio (%) |
| sharpe_ratio | Float | Sharpe Ratio |
| returns_1y | Float | One Year Return |
| returns_3y | Float | Three Year Return |
| returns_5y | Float | Five Year Return |

## Database Tables

- dim_fund
- fact_nav
- fact_transactions
- fact_performance

## Data Cleaning Performed

- Removed duplicate records
- Converted date columns to datetime format
- Standardized transaction types
- Validated NAV values (>0)
- Validated transaction amounts (>0)
- Checked KYC status values
- Verified expense ratio range
- Checked missing values
- Forward-filled missing NAV values