"""Figures for Unit A5: the unit square under standard transformations."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).parent
NAVY = "#1F3A5F"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
SQ = np.array([[0, 1, 1, 0, 0], [0, 0, 1, 1, 0]], dtype=float)


def axes(ax, lim):
    ax.set_xlim(*lim[0]); ax.set_ylim(*lim[1]); ax.set_aspect("equal")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_position("zero"); ax.spines["bottom"].set_position("zero")
    ax.set_xlabel("x", loc="right"); ax.set_ylabel("y", loc="top", rotation=0)


def panel(ax, Mx, title, lim):
    axes(ax, lim)
    ax.plot(SQ[0], SQ[1], "--", color="grey", lw=1)
    img = Mx @ SQ
    ax.fill(img[0], img[1], color="#C9D7E8", alpha=0.8)
    ax.plot(img[0], img[1], color=NAVY, lw=1.6)
    for col, name in ((0, "Mi"), (1, "Mj")):
        v = Mx[:, col]
        ax.annotate("", xy=v, xytext=(0, 0), arrowprops=dict(arrowstyle="->", color="#8A2C1E", lw=1.4))
        ax.text(v[0] + 0.05, v[1] + 0.05, name, fontsize=9, color="#8A2C1E")
    ax.text(0.98, 0.98, title, transform=ax.transAxes, fontsize=10, fontweight="bold", va="top", ha="right")


def main():
    fig, axs = plt.subplots(2, 2, figsize=(7, 6.2))
    r = np.radians(60)
    panel(axs[0, 0], np.array([[0, 1], [1, 0]]), "(a)", ((-0.6, 1.8), (-0.6, 1.8)))
    panel(axs[0, 1], np.array([[np.cos(r), -np.sin(r)], [np.sin(r), np.cos(r)]]), "(b)",
          ((-1.6, 1.6), (-0.4, 1.8)))
    panel(axs[1, 0], np.array([[3, 0], [0, 1]]), "(c)", ((-0.4, 3.6), (-0.4, 1.6)))
    panel(axs[1, 1], np.array([[1, 2], [0, 1]]), "(d)", ((-0.4, 3.6), (-0.4, 1.6)))
    fig.tight_layout()
    fig.savefig(HERE / "pa05_square.png", dpi=200, facecolor="white")

    fig, ax = plt.subplots(figsize=(5, 2.6))
    axes(ax, ((-0.3, 3.4), (-0.3, 1.5)))
    ax.plot(SQ[0], SQ[1], "--", color="grey", lw=1)
    img = np.array([[1, 2], [0, 1]]) @ SQ
    ax.fill(img[0], img[1], color="#C9D7E8", alpha=0.8); ax.plot(img[0], img[1], color=NAVY, lw=1.6)
    for (px, py), lab in (((0, 1), "(0, 1)"), ((1, 1), "(1, 1)"), ((2, 1), "(2, 1)"), ((3, 1), "(3, 1)"), ((1, 0), "(1, 0)")):
        ax.plot(px, py, "o", color=NAVY, ms=3); ax.text(px + 0.03, py + (0.07 if py else -0.2), lab, fontsize=8)
    ax.annotate("", xy=(2, 1), xytext=(0, 1), arrowprops=dict(arrowstyle="->", color="#8A2C1E"))
    ax.annotate("", xy=(3, 1), xytext=(1, 1), arrowprops=dict(arrowstyle="->", color="#8A2C1E"))
    fig.tight_layout()
    fig.savefig(HERE / "pa05_shear.png", dpi=200, facecolor="white")


if __name__ == "__main__":
    main()
