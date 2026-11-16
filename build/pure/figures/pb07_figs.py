"""Figures for Unit B7 (improper integrals, rectangles and limits of sums). Writes pb07_*.png into this folder."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

HERE = Path(__file__).resolve().parent
NAVY = "#1F3A5F"
RED = "#8A2C1E"
GREY = "#777777"
FILL = "#C9DCEB"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})


def save(fig, name):
    fig.savefig(HERE / f"pb07_{name}.png", dpi=200, facecolor="white", bbox_inches="tight")
    plt.close(fig)


def axes(ax, xlim, ylim, xlabel="x", ylabel="y"):
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.set_xlim(*xlim), ax.set_ylim(*ylim)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, ms=5)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, ms=5)
    ax.text(xlim[1], 0.03 * (ylim[1] - ylim[0]), xlabel, ha="right", va="bottom")
    ax.text(0.02 * (xlim[1] - xlim[0]), ylim[1], ylabel, ha="left", va="top")


def improper():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(8, 3.4))
    xs = np.linspace(1, 8, 300)
    a1.fill_between(xs, 0, 1 / xs**2, color=FILL)
    xx = np.linspace(0.35, 8, 300)
    a1.plot(xx, 1 / xx**2, color=NAVY, lw=2)
    a1.plot([1, 1], [0, 1], color=NAVY, lw=1)
    a1.text(3.0, 0.5, "y = 1/x²", color=NAVY)
    a1.text(5.0, 0.12, "area 1 →", color=RED)
    axes(a1, (-0.3, 8), (-0.1, 1.6))
    a1.set_xticks([1, 4, 7]), a1.set_yticks([1])
    xs = np.linspace(0.01, 4, 400)
    a2.fill_between(xs, 0, 1 / np.sqrt(xs), color=FILL)
    a2.plot(xs, 1 / np.sqrt(xs), color=NAVY, lw=2)
    a2.plot([4, 4], [0, 0.5], color=NAVY, lw=1)
    a2.text(1.3, 1.6, "y = 1/√x", color=NAVY)
    a2.text(1.2, 0.3, "area 4", color=RED)
    axes(a2, (-0.3, 5), (-0.2, 5))
    a2.set_xticks([1, 2, 3, 4]), a2.set_yticks([1, 2, 3, 4])
    save(fig, "improper")


def rect():
    fig, ax = plt.subplots(figsize=(6, 4))
    for r in range(1, 6):
        ax.add_patch(plt.Rectangle((r, 0), 1, 1 / r, fill=False, ec=RED, lw=1.2))
        ax.add_patch(plt.Rectangle((r, 0), 1, 1 / (r + 1), color=FILL, ec=NAVY, lw=0.6))
    xs = np.linspace(0.6, 6.6, 300)
    ax.plot(xs, 1 / xs, color=NAVY, lw=2)
    ax.text(2.2, 0.75, "y = 1/x", color=NAVY)
    ax.text(1.1, 1.04, "height 1", color=RED, fontsize=9)
    ax.text(2.05, 0.53, "1/2", color=RED, fontsize=9)
    axes(ax, (-0.2, 7), (-0.08, 1.45))
    ax.set_xticks(range(1, 7)), ax.set_yticks([0.5, 1])
    save(fig, "rect")


if __name__ == "__main__":
    improper(), rect()
    print("pb07 figures written")
