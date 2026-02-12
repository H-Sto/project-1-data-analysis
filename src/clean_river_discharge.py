"""
Day 3 – Data loading and cleaning

This script loads raw river discharge data,
performs basic cleaning, and writes a cleaned dataset.
"""


import pandas as pd

RAW_PATH = "data/raw/river_discharge_raw.csv"
PROCESSED_PATH = "data/processed/river_discharge_cleaned.csv"

def load_raw_data(path: str) -> pd.DataFrame:
   return pd.read_csv(path)

def clean_discharge(df: pd.DataFrame) -> pd.DataFrame:
   df = df.copy()

   df["Mean_Discharge_m3s"] = pd.to_numeric(df["Mean_Discharge_m3s"], errors="coerce")

   df = df.dropna(subset=["Mean_Discharge_m3s"])

   return df
def save_clean_data(df: pd.DataFrame, path: str) -> None:
   df.to_csv(path, index=False)

def main() -> None:
   df_raw = load_raw_data(RAW_PATH)
   df_clean = clean_discharge(df_raw)
   save_clean_data(df_clean, PROCESSED_PATH)

   print(f"Save cleaned dataset: {PROCESSED_PATH}")
   print(f"Rows: {len(df_clean)}")

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
