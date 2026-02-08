"""
Day 2 – Python fundamentals with intent

This script demonstrates core Python concepts
through small, realistic data tasks.
"""

import pandas as pd


def validate_numbers(numbers):
    """
    Ensure input is a non-empty list of numeric values.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")

    if len(numbers) == 0:
        raise ValueError("Input list must not be empty")

    for value in numbers:
        if not isinstance(value, (int, float)):
            raise TypeError("All elements must be numeric")


def summarise_numbers(numbers):
    """
    Given a list of numbers, return summary statistics.
    """
    validate_numbers(numbers)

    count = len(numbers)
    mean = sum(numbers) / count
    minimum = min(numbers)
    maximum = max(numbers)

    return {
        "count": count,
        "mean": mean,
        "min": minimum,
        "max": maximum,
    }


if __name__ == "__main__":
    values = [3, 7, 2, 9, 4]
    summary = summarise_numbers(values)
    print(summary)

    data = {
        "site": ["A", "B", "C", "D"],
        "rainfall_mm": [12.4, 8.1, 15.6, 9.3],
        "runoff_mm": [3.2, 1.8, 4.5, 2.1],
    }

    df = pd.DataFrame(data)

    print("\nDataFrame:")
    print(df)

    print("\nDataFrame info:")
    df.info()

    print("\nSummary statistics:")
    print(df.describe())
