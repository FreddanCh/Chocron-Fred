# Laboration 3 – Linjär klassificering
# Steg:
# 1) Läs in unlabelled_data.csv (kolumner: x,y – med eller utan rubriker)
# 2) Välj en linje y = kx + m
# 3) Klassificera: 0 = under/vänster om linjen, 1 = över/höger om linjen
# 4) Spara labelled_data.csv
# 5) Rita figur med punkter och linjen

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1) Läs data (tålig mot om rubriker saknas)
try:
    tmp = pd.read_csv("unlabelled_data.csv")
    if {"x","y"}.issubset(tmp.columns):
        df = tmp[["x","y"]].copy()
    else:
        # saknar x,y-rubriker -> läs två första kolumnerna utan rubrik
        df = pd.read_csv("unlabelled_data.csv", header=None, usecols=[0,1])
        df.columns = ["x","y"]
except Exception:
    # sista utväg: läs rått utan rubrik
    df = pd.read_csv("unlabelled_data.csv", header=None, usecols=[0,1])
    df.columns = ["x","y"]

# 2) Linje
k = -1.0
m = 0.47

def classify_point(x, y):
    return int(y >= k * x + m)

# 3) Klassificera
df["label"] = [classify_point(x, y) for x, y in zip(df["x"], df["y"])]

# 4) Spara resultat
df.to_csv("labelled_data.csv", index=False)

# 5) Plot
plt.figure(figsize=(8,5))
df0 = df[df["label"] == 0]
df1 = df[df["label"] == 1]
plt.scatter(df0["x"], df0["y"], marker="x", label="0")
plt.scatter(df1["x"], df1["y"], marker="x", label="1")

xs = np.linspace(df["x"].min(), df["x"].max(), 200)
ys = k*xs + m
plt.plot(xs, ys, "r--", label=f"y = {k:.0f}x + {m:.2f}")

plt.title("Lab 3 klassificering")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True, linestyle=":", linewidth=0.5)
plt.tight_layout()
plt.savefig("plot.png")
