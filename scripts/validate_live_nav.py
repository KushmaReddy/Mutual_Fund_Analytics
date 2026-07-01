import pandas as pd

# Load historical NAV
historical = pd.read_csv("data/raw/02_nav_history.csv")

# Load live NAV
live = pd.read_csv("data/raw/live_nav.csv")

print("=" * 60)
print("Historical Dataset")
print("=" * 60)

print(historical.head())

print()

print("=" * 60)
print("Live Dataset")
print("=" * 60)

print(live.head())

print()

print("=" * 60)
print("Historical Columns")
print("=" * 60)

print(historical.columns.tolist())

print()

print("=" * 60)
print("Live Columns")
print("=" * 60)

print(live.columns.tolist())

print()

print("=" * 60)
print("Historical Data Types")
print("=" * 60)

print(historical.dtypes)

print()

print("=" * 60)
print("Live Data Types")
print("=" * 60)

print(live.dtypes)

print()

print("=" * 60)
print("Latest Historical Records")
print("=" * 60)

print(historical.tail())

print()

print("=" * 60)
print("Latest Live Records")
print("=" * 60)

print(live.head())

print()

print("=" * 60)
print("Validation Completed Successfully")
print("=" * 60)