# Data Cleaning Pipeline

A simple Python project using `pandas` to automate loading, cleaning, and exporting tabular datasets.

## Features
* Loads raw CSV data with missing values.
* Imputes missing numeric values (e.g., median salary) and handles missing categorical data.
* Standardizes and renames column headers for better clarity.
* Exports a clean, analysis-ready dataset (`cleaned_dataset.csv`).

## Project Structure
```text
data_cleaning_project/
│
├── dataset.csv            # Raw input dataset
├── cleaned_dataset.csv    # Output cleaned dataset
├── clean_data.py          # Main Python script for data processing
└── README.md              # Project documentation