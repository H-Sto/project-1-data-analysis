

from clean_river_discharge import main as clean_river_discharge
from eda_river_discharge import main as eda_river_discharge

def run_pipeline():
    print("Starting pipeline")
    clean_river_discharge()
    print("Completed data cleaning")

    eda_river_discharge()
    print("Completed exploratory data analysis")

    print("Pipeline finished successfully")

if __name__== "__main__":
    run_pipeline()

