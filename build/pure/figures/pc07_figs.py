"""Figures for unit C7 (groups I): symmetries of an equilateral triangle."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch

OUT = Path(__file__).resolve().parent
NAVY = "#1F3A5F"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})


def triangle():
    fig, ax = plt.subplots(figsize=(5, 4.6))
    ang = np.radians([90, 210, 330])
    P = np.c_[np.cos(ang), np.sin(ang)]
    ax.fill(P[:, 0], P[:, 1], color="#E8F1F5", ec=NAVY, lw=2)
    for (x, y), lab in zip(P, "ABC"):
        ax.plot(x, y, "o", color=NAVY)
        ax.text(1.13 * x, 1.13 * y, lab, ha="center", va="center", fontsize=14, weight="bold", color=NAVY)
    # lines of symmetry, fixed in the plane, through each corner position
    for (x, y), lab in zip(P, "abc"):
        ax.plot([-0.75 * x, 1.0 * x], [-0.75 * y, 1.0 * y], "--", color="#8A2C1E", lw=1.2)
        ax.text(-0.85 * x, -0.85 * y, lab, ha="center", va="center", fontsize=13, style="italic", color="#8A2C1E")
    ax.plot(0, 0, "o", color="black", ms=4)
    ax.text(-0.2, -0.04, "O", fontsize=11)
    arr = FancyArrowPatch((0.3, 0.05), (-0.05, 0.32), connectionstyle="arc3,rad=0.45",
                          arrowstyle="-|>", mutation_scale=14, color=NAVY, lw=1.5)
    ax.add_patch(arr)
    ax.text(0.1, 0.36, "r", fontsize=13, style="italic", color=NAVY)
    ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.0, 1.3); ax.set_aspect("equal"); ax.axis("off")
    fig.savefig(OUT / "pc07_triangle.png", dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    triangle()
    print("written", OUT / "pc07_triangle.png")
