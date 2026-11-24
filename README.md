# Sales Data – Exploratory Data Analysis

Get a first look at a sales dataset: its structure, summary statistics, data quality, and how sales records are spread across cities.

## Dataset

**File:** `data/sales.csv`

Key columns used:

- City – city where the sale took place
- Other sales fields in the file (summarised with `info()` and `describe()`)

## What the analysis does

1. Load the dataset and inspect its structure with `info()`, `describe()` and `head()`
2. Check for missing values and duplicate rows
3. Count records per city

## Visualisations

| Chart | Type |
|-------|------|
| City Distribution | Bar chart of the number of records per city |

## Questions explored

- Which cities contribute the most sales records?
- Is the data clean (no missing values or duplicates)?

## Key insights

<!-- Run the script and write 3–5 findings here, e.g. "Customers in X had the highest ..." -->

- _Add your findings here_

## How to run

From the root of the repository:

```bash
pip install -r requirements.txt
python 01_sales_eda/sales_eda.py
```

Make sure `sales.csv` is in the `data/` folder. Each chart opens in a window; close it to see the next one.

## Tools

Python · pandas · matplotlib · seaborn

---
[← Back to all projects](../README.md)
