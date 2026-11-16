"""Figures for Unit A1 (pa01). Run: python pa01_figs.py  -> writes pa01_*.png next to this file."""
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
NAVY = "#1F3A5F"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})


def axes_through_origin(ax):
    for side in ("left", "bottom"):
        ax.spines[side].set_position("zero")
    for side in ("right", "top"):
        ax.spines[side].set_visible(False)


def cubic():
    fig, ax = plt.subplots(figsize=(6, 4))
    x = np.linspace(-0.5, 4.2, 400)
    ax.plot(x, x ** 3 - 6 * x ** 2 + 21 * x - 26, color=NAVY, lw=2)
    axes_through_origin(ax)
    ax.plot([2], [0], "o", color="black")
    ax.annotate("(2, 0)", (2, 0), xytext=(2.15, -5), fontsize=11)
    ax.set_xlabel("x", loc="right")
    ax.set_ylabel("y", loc="top", rotation=0)
    ax.text(0.15, 16, "y = x³ − 6x² + 21x − 26", color=NAVY)
    ax.set_ylim(-40, 25)
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, "pa01_cubic.png"), dpi=200, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    cubic()
    print("pa01 figures written")
