"""Figures for unit C3 (substitutions and series solutions). Writes pc03_*.png into this folder."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from scipy.integrate import solve_ivp  # noqa: E402

HERE = Path(__file__).resolve().parent
NAVY = "#1F3A5F"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})

# dy/dx = x^2 + y^2, y(1) = 1: numerical solution both sides of x = 1, and the cubic Taylor polynomial.
f = lambda x, y: [x ** 2 + y[0] ** 2]
right = solve_ivp(f, [1, 1.5], [1], dense_output=True, rtol=1e-10, atol=1e-10)
left = solve_ivp(f, [1, 0.6], [1], dense_output=True, rtol=1e-10, atol=1e-10)
xr = np.linspace(1, 1.5, 200)
xl = np.linspace(0.6, 1, 200)
xs = np.linspace(0.6, 1.5, 300)
taylor = 1 + 2 * (xs - 1) + 3 * (xs - 1) ** 2 + 11 / 3 * (xs - 1) ** 3

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(xl, left.sol(xl)[0], color=NAVY, lw=1.6, label="solution (numerical)")
ax.plot(xr, right.sol(xr)[0], color=NAVY, lw=1.6)
ax.plot(xs, taylor, color="black", ls="--", lw=1.3, label="Taylor polynomial, degree 3")
ax.plot([1], [1], "o", color="black", ms=4)
ax.annotate("(1, 1)", (1, 1), xytext=(1.02, 0.8), fontsize=9)
ax.set_xlim(0.6, 1.5)
ax.set_ylim(0, 4.5)
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.set_xlabel("x", loc="right")
ax.set_ylabel("y", loc="top", rotation=0)
ax.legend(frameon=False, loc="upper left")
fig.savefig(HERE / "pc03_series.png", dpi=200, facecolor="white", bbox_inches="tight")
plt.close(fig)
print("pc03 figures written")
