# Project 1 – River Discharge Data Analysis (Python)

## Overview
This project demonstrates a reproducible Python data analysis workflow:
raw data → cleaning → exploratory analysis → saved figures.

## Dataset
- Raw file: `data/raw/river_discharge_raw.csv`
- Cleaned file: `data/processed/river_discharge_clean.csv`
- Known issues in raw data: missing values, non-numeric entries in discharge column

## Project Structure
- `data/raw/` raw dataset (never edited)
- `data/processed/` cleaned outputs
- `src/` scripts (cleaning + EDA)
- `reports/figures/` saved charts

## How to run
### 1) Set up environment
```bash
conda create -n portfolio-week1 python=3.11 -y
conda activate portfolio-week1
pip install -r requirements.txt