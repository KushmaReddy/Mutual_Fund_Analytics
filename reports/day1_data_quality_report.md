# Day 1 Data Quality Report

## Project
Mutual Fund Analytics

## Date
01-07-2026

---

## Dataset Inspection

All 10 datasets were successfully loaded using Pandas.

The following checks were performed:

- Dataset Shape
- Column Names
- Data Types
- First 5 Rows
- Missing Values

---

## Fund Master Exploration

The following information was explored:

- Unique Fund Houses
- Unique Categories
- Unique Sub Categories
- Risk Category information

---

## Live NAV

- Successfully fetched live NAV data from MFAPI.
- Saved data as raw CSV.

---

## AMFI Code Validation

Validation completed successfully.

Result:

- Total AMFI Codes in Fund Master: 40
- Total AMFI Codes in NAV History: 40
- Missing Codes: 0

All NAV History AMFI codes exist in Fund Master.

---

## Conclusion

The project environment has been successfully set up.

All datasets were loaded successfully.

Data inspection and AMFI validation completed successfully.

The project is ready for Day 2.