"""
============================================================
Mutual Fund Analytics Capstone
File Name : run_pipeline.py
Author    : Kushma Reddy H

Description:
Master script to execute the Mutual Fund Analytics pipeline.
============================================================
"""

import os

scripts = [
    "scripts/data_ingestion.py",
    "scripts/data_cleaning.py",
    "scripts/check_database.py",
    "scripts/data_quality_report.py",
    "scripts/data_visualization.py",
    "scripts/recommender.py"
]

print("=" * 70)
print("STARTING MUTUAL FUND ANALYTICS PIPELINE")
print("=" * 70)

for script in scripts:
    print(f"\nRunning: {script}")
    os.system(f'python "{script}"')
print("\n" + "=" * 70)
print("PIPELINE COMPLETED SUCCESSFULLY")
print("=" * 70)