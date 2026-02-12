"""
Day 4/5 – Exploratory Data Analysis (EDA)

Loads the cleaned river discharge dataset, prints basic summaries,
and saves visualisations to reports/figures/.
"""

from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

CLEAN_PATH = Path("data/processed/river_discharge_cleaned.csv")
FIG_DIR = Path("reports/figures")


def load_clean_data(path: Path) -> pd.DataFrame:
    """Load cleaned dataset from disk."""

    return pd.read_csv(path)


def validate_expected_columns(df: pd.DataFrame) -> None:
    """Fail fast if required columns are missing."""
    required = {"Country", "Year", "Mean_Discharge_m3s"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")


def avg_discharge_by_country(df: pd.DataFrame) -> pd.Series:
    """Return average discharge (m³/s) grouped by country."""
    return (
        df.groupby("Country")["Mean_Discharge_m3s"]
        .mean()
        .sort_values(ascending=False)
    )


def plot_avg_by_country(avg_series: pd.Series, out_path: Path) -> None:
    """Save bar chart of average discharge by country."""
    plt.figure()
    avg_series.plot(kind="bar")
    plt.title("Average River Discharge by Country")
    plt.ylabel("Mean Discharge (m³/s)")
    plt.tight_layout()
    plt.savefig(out_path, dpi=200)
    plt.close()


def plot_discharge_over_time(df: pd.DataFrame, out_path: Path) -> None:
    """Save line chart of discharge over time by country."""
    plt.figure()

    for country in sorted(df["Country"].unique()):
        subset = df[df["Country"] == country].sort_values("Year")
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
    plt.savefig(out_path, dpi=200)
    plt.close()


def main() -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)

    df = load_clean_data(CLEAN_PATH)
    validate_expected_columns(df)

    print("Cleaned dataset preview:")
    print(df)

    print("\nDataset info:")
    df.info()

    avg = avg_discharge_by_country(df)
    print("\nAverage discharge by country (m³/s):")
    print(avg)

    plot_avg_by_country(avg, FIG_DIR / "avg_discharge_by_country.png")
    plot_discharge_over_time(df, FIG_DIR / "discharge_over_time.png")

    print(f"\nSaved figures to: {FIG_DIR}")


if __name__ == "__main__":
    main()
