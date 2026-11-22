import argparse
import csv
from pathlib import Path

parser = argparse.ArgumentParser(description="Model a share of US-bound Korean cosmetics exports.")
parser.add_argument("--share", type=float, required=True, help="Percentage of export value attributed to sheet masks")
share = parser.parse_args().share
if not 0 <= share <= 100:
    parser.error("--share must be between 0 and 100")

with Path(__file__).with_name("exports.csv").open(newline="", encoding="utf-8") as source:
    exports = sorted((int(row["year"]), int(row["us_cosmetics_exports_usd_thousands"]) * 1000)
                     for row in csv.DictReader(source))

for year, value in exports:
    print(f"{year} cosmetics exports: USD {value:,}")
previous_year, previous_value = exports[-2]
year, value = exports[-1]
growth = value / previous_value - 1
print(f"Growth from {previous_year} to {year}: {growth:.1%}")
print(f"Illustrative scenario ({share:g}% share in {year}): USD {value * share / 100:,.0f}")
