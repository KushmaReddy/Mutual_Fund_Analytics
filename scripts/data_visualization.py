import pandas as pd
import matplotlib.pyplot as plt
import os

# ==========================================================
# DATA VISUALIZATION
# ==========================================================

# Load cleaned dataset
df = pd.read_csv("data/processed/02_nav_history.csv")

# Convert date column safely (handles mixed formats)
df["date"] = pd.to_datetime(
    df["date"],
    format="mixed",
    dayfirst=True,
    errors="coerce"
)

# Remove rows with invalid dates
df = df.dropna(subset=["date"])

# Create outputs folder if it doesn't exist
OUTPUT_PATH = "outputs"

if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)

print("=" * 70)
print("DATA VISUALIZATION")
print("=" * 70)

# ==========================================================
# 1. NAV Trend Line Chart
# ==========================================================

plt.figure(figsize=(12,6))

plt.plot(df["date"], df["nav"], color="blue")

plt.title("Mutual Fund NAV Trend")
plt.xlabel("Date")
plt.ylabel("NAV")
plt.grid(True)

plt.tight_layout()

plt.savefig("outputs/nav_trend.png")

plt.close()

print("✓ NAV Trend Chart Saved")

# ==========================================================
# 2. NAV Distribution Histogram
# ==========================================================

plt.figure(figsize=(8,5))

plt.hist(df["nav"], bins=30, edgecolor="black")

plt.title("NAV Distribution")
plt.xlabel("NAV")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("outputs/nav_distribution.png")

plt.close()

print("✓ NAV Distribution Chart Saved")

# ==========================================================
# 3. NAV Box Plot
# ==========================================================

plt.figure(figsize=(6,5))

plt.boxplot(df["nav"])

plt.title("NAV Box Plot")

plt.tight_layout()

plt.savefig("outputs/nav_boxplot.png")

plt.close()

print("✓ NAV Box Plot Saved")

# ==========================================================

print("\n" + "=" * 70)
print("VISUALIZATION COMPLETED SUCCESSFULLY")
print("=" * 70)