"""Figures for Unit C6 (pc06). Run: python pc06_figs.py  -> writes pc06_*.png next to this file."""
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Circle, Wedge  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
NAVY = "#1F3A5F"
RED = "#B5462E"
SHADE = "#9FC3D9"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})


def argand(ax, xlim, ylim, re="Re", im="Im"):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    for side in ("left", "bottom"):
        ax.spines[side].set_position("zero")
    for side in ("right", "top"):
        ax.spines[side].set_visible(False)
    ax.text(xlim[1], 0.02 * (ylim[1] - ylim[0]), re, ha="right", va="bottom")
    ax.text(0.02 * (xlim[1] - xlim[0]), ylim[1], im, ha="left", va="top")


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, f"pc06_{name}.png"), dpi=200, facecolor="white", bbox_inches="tight", pad_inches=0.1)
    plt.close(fig)


def apollonius():
    fig, ax = plt.subplots(figsize=(5.6, 4.2))
    argand(ax, (-3.8, 3.8), (-2.6, 2.8))
    ax.add_patch(Circle((1, 0), 2, fc=SHADE, ec=NAVY, lw=2, alpha=0.6))
    for p, lab, off in [((-3, 0), "−3", (-6, -14)), ((0, 0), "0", (-12, -14)), ((1, 0), "centre 1", (2, 6)),
                        ((3, 0), "3", (4, -14)), ((-1, 0), "−1", (-16, 6)), ((1, 2), "1 + 2i", (6, 2))]:
        ax.plot(*p, "o", color="black", ms=4)
        ax.annotate(lab, p, xytext=off, textcoords="offset points", fontsize=10)
    ax.plot([-3, 1], [0, 2], color=RED, ls="--", lw=1)
    ax.plot([0, 1], [0, 2], color=RED, ls="--", lw=1)
    ax.text(-3.6, 2.2, "|z + 3| = 2|z|", color=NAVY)
    ax.set_xticks([]); ax.set_yticks([])
    save(fig, "apollonius")


def arcs():
    fig, ax = plt.subplots(figsize=(5.6, 4.6))
    argand(ax, (-2.6, 2.6), (-0.8, 3.3))
    for beta, ls in [(np.pi / 4, "-"), (np.pi / 2, "--"), (3 * np.pi / 4, ":")]:
        R = 1 / np.sin(beta)
        h = 1 / np.tan(beta)  # centre (0, h)
        t = np.linspace(0, 2 * np.pi, 2000)
        x, y = R * np.cos(t), h + R * np.sin(t)
        keep = y > 1e-9
        xs, ys = np.where(keep, x, np.nan), np.where(keep, y, np.nan)
        ax.plot(xs, ys, color=NAVY, lw=2, ls=ls)
    ax.plot([-1, 1], [0, 0], "o", mfc="white", mec="black", ms=6, zorder=5)
    ax.text(1.55, 2.2, "β = π/4", color=NAVY)
    ax.text(0.9, 0.72, "β = π/2", color=NAVY)
    ax.text(-0.42, 0.12, "β = 3π/4", color=NAVY, fontsize=9)
    ax.plot([0], [1], "+", color=RED, ms=8)
    ax.annotate("centre i (β = π/4)", (0, 1), xytext=(6, 6), textcoords="offset points", color=RED, fontsize=9)
    save(fig, "arcs")


def zsquared():
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.6))
    ax = axs[0]
    argand(ax, (-1.6, 2.2), (-2.2, 2.2), "x", "y")
    ax.add_patch(Wedge((0, 0), 1, 0, 90, fc=SHADE, ec=NAVY, alpha=0.7))
    ax.axvline(1, color=RED, lw=2)
    ax.text(1.08, 1.7, "Re(z) = 1", color=RED)
    ax.text(0.5, -0.12, "z-plane", transform=ax.transAxes, ha="center", va="top")
    ax = axs[1]
    argand(ax, (-4.2, 2.2), (-3.2, 3.2), "u", "v")
    ax.add_patch(Wedge((0, 0), 1, 0, 180, fc=SHADE, ec=NAVY, alpha=0.7))
    v = np.linspace(-3.2, 3.2, 300)
    ax.plot(1 - v ** 2 / 4, v, color=RED, lw=2)
    ax.text(-3.9, 2.4, "u = 1 − v²/4", color=RED)
    ax.text(0.5, -0.12, "w-plane", transform=ax.transAxes, ha="center", va="top")
    save(fig, "zsquared")


if __name__ == "__main__":
    apollonius(); arcs(); zsquared()
    print("pc06 figures written")
