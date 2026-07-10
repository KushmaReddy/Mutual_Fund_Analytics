# Mutual Fund Analytics

Bluestock Fintech Capstone Project

---

# Project Overview

The Mutual Fund Analytics project is an end-to-end data analytics solution developed as part of the Bluestock Fintech Capstone Program.

This project analyzes mutual fund datasets using Python, Pandas, SQLite, SQL, and Power BI.

The project covers:

- Data Ingestion
- Data Cleaning
- Data Validation
- SQLite Database Design
- Exploratory Data Analysis (EDA)
- Data Visualization
- Mutual Fund Recommendation System
- Power BI Dashboard

---

# Objectives

- Analyze mutual fund datasets.
- Clean and validate financial data.
- Store cleaned data in SQLite.
- Perform Exploratory Data Analysis.
- Visualize NAV trends.
- Build a recommendation system.
- Develop an interactive Power BI dashboard.

---

# Day 1 Completed

## Data Ingestion & Validation

### Tasks Completed

- Project setup
- Data ingestion
- Live NAV fetching
- Dataset inspection
- Fund master exploration
- AMFI code validation
- Data quality report
- GitHub integration

### Technologies Used

- Python
- Pandas
- Requests API

---

# Day 2 Completed

## Data Cleaning & SQLite Database Design

Successfully completed the data cleaning and database design phase of the Mutual Fund Analytics project.

### Tasks Completed

- Cleaned investor transaction dataset.
- Cleaned NAV history dataset.
- Cleaned scheme performance dataset.
- Removed duplicate records.
- Handled missing values.
- Standardized column names.
- Standardized data types.
- Created SQLite database (bluestock_mf.db).
- Imported cleaned datasets into SQL tables.
- Verified database tables.

### Technologies Used

- Python
- Pandas
- SQLite
- SQL

---

# Day 3 Completed

## Exploratory Data Analysis (EDA)

Performed exploratory data analysis on cleaned mutual fund datasets.

### Tasks Completed

- Explored dataset structure.
- Generated summary statistics.
- Analyzed NAV distribution.
- Visualized NAV trends over time.
- Created Histogram.
- Created Box Plot.
- Identified average NAV.
- Identified highest NAV.
- Identified lowest NAV.
- Generated EDA summary.

### Technologies Used

- Python
- Pandas
- Matplotlib

---

# Day 4 Completed

## Fund Performance Analytics

Performed performance analysis using the available mutual fund performance dataset.

### Tasks Completed

- Cleaned scheme performance dataset.
- Converted return columns to numeric values.
- Converted expense ratio to numeric values.
- Validated expense ratios.
- Identified negative Sharpe Ratio values.
- Removed duplicate records.
- Generated cleaned performance dataset.
- Prepared performance data for dashboard.

### Technologies Used

- Python
- Pandas
- SQLite

---

# Day 5 Completed

## Dashboard Development

Developed an interactive Power BI dashboard for mutual fund analysis.

### Tasks Completed

- Connected Power BI with SQLite database.
- Imported cleaned datasets.
- Created data model.
- Built KPI Cards.
- Created NAV Trend chart.
- Created Fund House comparison.
- Created Category analysis.
- Added Risk Grade analysis.
- Added interactive slicers.
- Improved dashboard formatting.

### Dashboard Features

- Total Mutual Funds
- Average NAV
- NAV Trend
- Category Analysis
- Fund House Analysis
- Risk Analysis
- Interactive Filters

### Technologies Used

- Power BI
- SQLite
- SQL

---

# Day 6 Completed

## Mutual Fund Recommendation System

Developed a recommendation system based on fund risk level.

### Tasks Completed

- Loaded cleaned scheme performance dataset.
- Filtered funds using Risk Grade.
- Ranked funds using Sharpe Ratio.
- Generated Top 3 fund recommendations.
- Displayed recommendation results.

### Technologies Used

- Python
- Pandas

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Mutual_Fund_Analytics.git
```

Move into the project directory

```bash
cd Mutual_Fund_Analytics
```

Install required libraries

```bash
pip install -r requirements.txt
```

---

# Project Structure

```
Mutual_Fund_Analytics/

│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   ├── data_ingestion.py
│   ├── data_cleaning.py
│   ├── clean_nav_history.py
│   ├── clean_investor_transactions.py
│   ├── clean_scheme_performance.py
│   ├── load_datasets.py
│   ├── check_database.py
│   ├── data_quality_report.py
│   ├── data_visualization.py
│   ├── eda_summary.py
│   ├── recommender.py
│   ├── validate_amfi_codes.py
│   ├── validate_live_nav.py
│   └── explore_fund_master.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── powerbi/
│   └── Mutual_Fund_Dashboard.pbix
│
├── reports/
│   └── day1_data_quality_report.md
│
├── outputs/
│
├── bluestock_mf.db
│
├── requirements.txt
│
└── README.md
```

---

# File Description

| File | Description |
|------|-------------|
| data_ingestion.py | Loads raw datasets |
| data_cleaning.py | Cleans raw datasets |
| clean_nav_history.py | Cleans NAV History |
| clean_investor_transactions.py | Cleans Investor Transactions |
| clean_scheme_performance.py | Cleans Scheme Performance |
| load_datasets.py | Loads cleaned data into SQLite |
| check_database.py | Verifies SQLite database |
| data_quality_report.py | Generates data quality report |
| data_visualization.py | Creates charts |
| eda_summary.py | Performs Exploratory Data Analysis |
| recommender.py | Recommends mutual funds |
| validate_amfi_codes.py | Validates AMFI Codes |
| validate_live_nav.py | Validates Live NAV dataset |
| explore_fund_master.py | Explores Fund Master dataset |

---

# Project Workflow

Raw Data

↓

Data Cleaning

↓

SQLite Database

↓

Exploratory Data Analysis

↓

Data Visualization

↓

Recommendation System

↓

Power BI Dashboard

↓

Final Report

---

# How to Run

Install required packages

```bash
pip install -r requirements.txt
```

Run the scripts in the following order

```bash
python scripts/data_ingestion.py

python scripts/data_cleaning.py

python scripts/load_datasets.py

python scripts/check_database.py

python scripts/data_quality_report.py

python scripts/data_visualization.py

python scripts/recommender.py
```

---

# Power BI Dashboard

Open

```
powerbi/bluestock_mf_dashboard.pbix
```

Refresh the data source.

Dashboard includes

- NAV Trend
- Fund House Analysis
- Category Analysis
- Risk Analysis
- KPI Cards
- Interactive Filters

---

# Project Outputs

- Cleaned CSV Datasets
- SQLite Database
- SQL Queries
- Data Quality Reports
- EDA Reports
- Visualization Charts
- Mutual Fund Recommendation System
- Power BI Dashboard
- Final Project Report
- Presentation

---

# Technologies Used

- Python
- Pandas
- SQLite
- SQL
- Matplotlib
- Requests API
- Power BI
- VS Code
- Git
- GitHub

---

# Future Enhancements

- Machine Learning based Fund Recommendation
- Streamlit Web Application
- Real-Time NAV Dashboard
- Automated ETL Pipeline
- Cloud Deployment

---

# Author

**Kushma Reddy H**

PGDM – Data Science & Business Analytics

ISBR Business School

Bluestock Fintech Capstone Project

---

