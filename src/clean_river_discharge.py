"""
Day 3 – Data loading and cleaning

This script loads raw river discharge data,
performs basic cleaning, and writes a cleaned dataset.
"""

import pandas as pd

RAW_PATH = "data/raw/river_discharge_raw.csv"
PROCESSED_PATH = "data/processed/river_discharge_cleaned.csv"

if __name__ == "__main__":
   df = pd.read_csv(RAW_PATH)

   print("Raw data preview:")
   print(df)

   print("\nRaw data info") 
   print(df.info())

   df["Mean_Discharge_m3s"] = pd.to_numeric(
      df["Mean_Discharge_m3s"], errors="coerce"
   )

print("\nAfter converting discharge to numeric:")
print(df)

df_clean = df.dropna(subset=["Mean_Discharge_m3s"])

print("\nAfter dropping rows with missing discharge values:")
print(df_clean)

df_clean.to_csv(PROCESSED_PATH, index=False)
print(f"\nCleaned data saved to {PROCESSED_PATH}")
