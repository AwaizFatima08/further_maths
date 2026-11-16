"""Figures for unit B9 (first-order differential equations). Writes pb09_*.png into this folder."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

HERE = Path(__file__).resolve().parent
NAVY = "#1F3A5F"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})


def axes_origin(ax):
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)


def save(fig, name):
    fig.savefig(HERE / f"pb09_{name}.png", dpi=200, facecolor="white", bbox_inches="tight")
    plt.close(fig)


# Direction field of y' = x - y with curves y = x - 1 + c e^-x
fig, ax = plt.subplots(figsize=(6, 4))
X, Y = np.meshgrid(np.linspace(-1, 4, 21), np.linspace(-3, 4, 22))
U = np.ones_like(X)
V = X - Y
N = np.hypot(U, V)
ax.quiver(X, Y, U / N, V / N, angles="xy", color="0.6", width=0.0025, headwidth=0, headlength=0, headaxislength=0,
          scale=30, pivot="middle")
xs = np.linspace(-1, 4, 300)
for c in [-2, -1, 0, 1, 2, 3]:
    ys = xs - 1 + c * np.exp(-xs)
    ax.plot(xs, ys, color=NAVY if c != 0 else "black", lw=1.6 if c == 0 else 1.1)
ax.text(-0.9, 3.3, "c > 0", fontsize=9, color=NAVY)
ax.text(1.2, -2.6, "c < 0", fontsize=9, color=NAVY)
ax.set_xlim(-1, 4)
ax.set_ylim(-3, 4)
axes_origin(ax)
ax.set_xlabel("x", loc="right")
ax.set_ylabel("y", loc="top", rotation=0)
ax.text(3.3, 1.75, "y = x − 1", fontsize=9)
save(fig, "family_field")

# Family y = x^2 + c/x for x > 0
fig, ax = plt.subplots(figsize=(6, 4))
xs = np.linspace(0.05, 2.6, 400)
for c, ls in [(-2, "--"), (0, "-"), (2, ":")]:
    ys = xs ** 2 + c / xs
    ax.plot(xs, ys, color=NAVY if c else "black", ls=ls, lw=1.5, label=f"c = {c}")
ax.plot([1], [3], "o", color=NAVY, ms=4)
ax.annotate("(1, 3)", (1, 3), xytext=(0.85, 3.6), fontsize=9)
ax.plot([2 ** (1 / 3)], [0], "o", color=NAVY, ms=4)
ax.annotate("∛2", (2 ** (1 / 3), 0), xytext=(1.3, 0.5), fontsize=9)
ax.set_xlim(0, 2.6)
ax.set_ylim(-6, 8)
axes_origin(ax)
ax.set_xlabel("x", loc="right")
ax.set_ylabel("y", loc="top", rotation=0)
ax.legend(frameon=False, loc="upper left", bbox_to_anchor=(0.05, 1))
save(fig, "family_example")
print("pb09 figures written")
