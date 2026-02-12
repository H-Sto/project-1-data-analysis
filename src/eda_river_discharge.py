"""
Day 4 – Exploratory Data Analysis (EDA)

This script loads the cleaned river discharge dataset,
performs simple exploratory analysis,
and saves clean visualisations.
"""

import __main__
import pandas as pd
import matplotlib.pyplot as plt

CLEAN_PATH = "data/processed/river_discharge_cleaned.csv"

if __name__ == "__main__":
   df = pd.read_csv(CLEAN_PATH)

   print("Cleaned data set preview:")
   print(df)

   avg_by_country = df.groupby("Country")["Mean_Discharge_m3s"].mean()
   print("\nAverage discharge by country:")
   print(avg_by_country)

plt.figure()
avg_by_country.plot(kind="bar")
plt.title("Average River Discharge by Country")
plt.ylabel("Mean Discharge (m³/s)")
plt.tight_layout()
plt.savefig("reports/figures/avg_discharge_by_country.png", dpi=200)
plt.close()

plt.figure()
for country in df["Country"].unique():
   subset = df[df["Country"] == country]
   plt.plot(
    subset["Year"],
    subset["Mean_Discharge_m3s"],
    marker="o",
    label=country,
   )

plt.title("River Discharge Over Time by Country")
plt.xlabel("Year")
plt.ylabel("Mean Discharge (m³/s)")
plt.legend()
plt.tight_layout()
plt.savefig("reports/figures/discharge_over_time.png", dpi=200)
plt.close()


