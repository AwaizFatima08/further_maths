"""Figures for unit C8 (groups II): symmetries of a square."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

OUT = Path(__file__).resolve().parent
NAVY = "#1F3A5F"
RED = "#8A2C1E"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})


def square():
    fig, ax = plt.subplots(figsize=(5, 5))
    P = np.array([[1, 1], [-1, 1], [-1, -1], [1, -1]])
    ax.fill(P[:, 0], P[:, 1], color="#E8F1F5", ec=NAVY, lw=2)
    for (x, y), lab in zip(P, "ABCD"):
        ax.plot(x, y, "o", color=NAVY)
        ax.text(1.15 * x, 1.15 * y, lab, ha="center", va="center", fontsize=14, weight="bold", color=NAVY)
    lines = [((-1.6, 0), (1.6, 0), "H", (1.72, 0)), ((0, -1.6), (0, 1.6), "V", (0, 1.72)),
             ((-1.45, -1.45), (1.45, 1.45), "D₁", (1.58, 1.58)), ((1.45, -1.45), (-1.45, 1.45), "D₂", (-1.6, 1.6))]
    for a, b, lab, pos in lines:
        ax.plot([a[0], b[0]], [a[1], b[1]], "--", color=RED, lw=1.2)
        ax.text(*pos, lab, ha="center", va="center", fontsize=13, color=RED)
    ax.plot(0, 0, "o", color="black", ms=4)
    ax.text(0.16, 0.04, "O", fontsize=11)
    arr = FancyArrowPatch((0.55, 0.2), (0.2, 0.55), connectionstyle="arc3,rad=0.45",
                          arrowstyle="-|>", mutation_scale=14, color=NAVY, lw=1.5)
    ax.add_patch(arr)
    ax.text(0.22, 0.62, "r", fontsize=13, style="italic", color=NAVY)
    ax.set_xlim(-1.9, 1.9); ax.set_ylim(-1.9, 1.9); ax.set_aspect("equal"); ax.axis("off")
    fig.savefig(OUT / "pc08_square.png", dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    square()
    print("written", OUT / "pc08_square.png")
