print("✅ env_check.py started")

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("Python version:", sys.version)
print("pandas:", pd.__version__)
print("numpy:", np.__version__)

df = pd.DataFrame({"x": np.arange(1, 6), "y": np.array([2, 1, 3, 5, 4])})

plt.figure()
plt.plot(df["x"], df["y"], marker="o")
plt.title("Environment check plot")
plt.xlabel("x")
plt.ylabel("y")
plt.tight_layout()
plt.savefig("reports/figures/env_check.png", dpi=200)
plt.close()

print("✅ Saved reports/figures/env_check.png")
