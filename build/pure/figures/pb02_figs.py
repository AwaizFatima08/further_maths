"""Figures for Unit B2 (pb02). Run: python pb02_figs.py  -> writes pb02_*.png next to this file."""
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Circle, Polygon  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
NAVY = "#1F3A5F"
SHADE = "#9FC3D9"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})


def argand(ax, lim):
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect("equal")
    for side in ("left", "bottom"):
        ax.spines[side].set_position("zero")
    for side in ("right", "top"):
        ax.spines[side].set_visible(False)
    ax.text(lim, 0.04 * lim, "Re", ha="right", va="bottom")
    ax.text(0.04 * lim, lim, "Im", ha="left", va="top")


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, f"pb02_{name}.png"), dpi=200, facecolor="white", bbox_inches="tight", pad_inches=0.1)
    plt.close(fig)


def polygon(ax, pts, labels, offs):
    ax.add_patch(Polygon([(p.real, p.imag) for p in pts], closed=True, fc=SHADE, ec=NAVY, alpha=0.5, lw=1.5))
    for p, lab, off in zip(pts, labels, offs):
        ax.plot([p.real], [p.imag], "o", color="black", ms=4)
        ax.annotate(lab, (p.real, p.imag), xytext=off, textcoords="offset points")


def cube8i():
    fig, ax = plt.subplots(figsize=(4.8, 4.8))
    argand(ax, 2.8)
    ax.add_patch(Circle((0, 0), 2, fill=False, ec="grey", ls="--"))
    pts = [2 * np.exp(1j * (np.pi / 6 + 2 * k * np.pi / 3)) for k in range(3)]
    polygon(ax, pts, ["√3 + i", "−√3 + i", "−2i"], [(6, 4), (-50, 4), (6, -12)])
    ax.text(1.45, -1.6, "|z| = 2", color="grey")
    save(fig, "cube8i")


def unity5():
    fig, ax = plt.subplots(figsize=(4.8, 4.8))
    argand(ax, 1.5)
    ax.add_patch(Circle((0, 0), 1, fill=False, ec="grey", ls="--"))
    pts = [np.exp(2j * np.pi * k / 5) for k in range(5)]
    polygon(ax, pts, ["1", "ω", "ω²", "ω³", "ω⁴"], [(6, 4), (6, 4), (-18, 4), (-18, -12), (6, -12)])
    for p in pts:
        ax.plot([0, p.real], [0, p.imag], color="grey", lw=0.8)
    ax.text(0.22, 0.07, "2π/5", fontsize=9)
    save(fig, "unity5")


def triangle():
    fig, ax = plt.subplots(figsize=(4.8, 4.8))
    ax.set_xlim(-1.8, 3.8); ax.set_ylim(-1.8, 3.8); ax.set_aspect("equal")
    for side in ("left", "bottom"):
        ax.spines[side].set_position("zero")
    for side in ("right", "top"):
        ax.spines[side].set_visible(False)
    ax.text(3.8, 0.1, "Re", ha="right"); ax.text(0.1, 3.8, "Im", va="top")
    c = 1 + 1j
    pts = [c + 2 * np.exp(2j * np.pi * k / 3) for k in range(3)]
    polygon(ax, pts, ["3 + i", "(1 + √3)i", "(1 − √3)i"], [(6, 2), (6, 4), (6, -12)])
    ax.plot([c.real], [c.imag], "+", color=NAVY, ms=10, mew=2)
    ax.annotate("1 + i", (1, 1), xytext=(-12, 8), textcoords="offset points", color=NAVY)
    save(fig, "triangle")


if __name__ == "__main__":
    cube8i(); unity5(); triangle()
    print("pb02 figures written")
