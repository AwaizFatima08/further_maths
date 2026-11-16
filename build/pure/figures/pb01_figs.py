"""Figures for Unit B1 (pb01). Run: python pb01_figs.py  -> writes pb01_*.png next to this file."""
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Arc, Polygon  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
NAVY = "#1F3A5F"
RED = "#B5462E"
SHADE = "#9FC3D9"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})


def argand(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    for side in ("left", "bottom"):
        ax.spines[side].set_position("zero")
    for side in ("right", "top"):
        ax.spines[side].set_visible(False)
    ax.text(xlim[1], 0.02 * (ylim[1] - ylim[0]), "Re", ha="right", va="bottom")
    ax.text(0.02 * (xlim[1] - xlim[0]), ylim[1], "Im", ha="left", va="top")


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, f"pb01_{name}.png"), dpi=200, facecolor="white", bbox_inches="tight", pad_inches=0.1)
    plt.close(fig)


def spiral():
    fig, ax = plt.subplots(figsize=(6, 4.6))
    argand(ax, (-4.0, 2.2), (-4.2, 2.4))
    t = np.linspace(0, 8 * np.pi / 6, 300)
    ax.plot(1.2 ** (t / (np.pi / 6)) * np.cos(t), 1.2 ** (t / (np.pi / 6)) * np.sin(t), color="grey", lw=1, ls="--")
    for k in range(9):
        r, th = 1.2 ** k, k * np.pi / 6
        p = (r * np.cos(th), r * np.sin(th))
        ax.plot([0, p[0]], [0, p[1]], color=NAVY, lw=1.1)
        ax.plot(*p, "o", color="black", ms=4)
        lab = "1" if k == 0 else ("z" if k == 1 else f"z{'⁰¹²³⁴⁵⁶⁷⁸'[k]}")
        ax.annotate(lab, p, xytext=(5, 3), textcoords="offset points")
    ax.add_patch(Arc((0, 0), 0.9, 0.9, theta1=0, theta2=30, color=RED))
    ax.text(0.5, 0.08, "π/6", color=RED, fontsize=10)
    save(fig, "spiral")


def rotate():
    fig, ax = plt.subplots(figsize=(5.2, 4.6))
    argand(ax, (-2.2, 1.8), (-0.6, 3.0))
    sq = np.array([[0, 0], [1, 0], [1, 1], [0, 1]])
    w = 1 + np.sqrt(3) * 1j
    img = np.array([[(w * complex(*p)).real, (w * complex(*p)).imag] for p in sq])
    ax.add_patch(Polygon(sq, closed=True, fc="#DDDDDD", ec="grey"))
    ax.add_patch(Polygon(img, closed=True, fc=SHADE, ec=NAVY, alpha=0.7, lw=1.5))
    labels = ["", "1 + √3 i", "(1 − √3) + (1 + √3)i", "−√3 + i"]
    offs = [(0, 0), (6, -4), (-60, 8), (-20, 6)]
    for p, lab, off in zip(img[1:], labels[1:], offs[1:]):
        ax.plot(*p, "o", color="black", ms=4)
        ax.annotate(lab, p, xytext=off, textcoords="offset points", fontsize=10)
    ax.text(0.35, 0.4, "S", fontsize=12)
    ax.text(-1.15, 1.75, "image", color=NAVY, fontsize=11)
    save(fig, "rotate")


if __name__ == "__main__":
    spiral(); rotate()
    print("pb01 figures written")
