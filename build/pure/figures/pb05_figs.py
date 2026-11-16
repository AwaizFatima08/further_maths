"""Figures for unit B5 (pb05): inverse trigonometric graphs and a hyperbolic curve with a shaded area.

Run: python pure/figures/pb05_figs.py  (writes pb05_*.png next to this file)
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

OUT = Path(__file__).resolve().parent
NAVY = "#1F3A5F"
RED = "#B03A2E"
GREEN = "#2E7D4F"
GREY = "#888888"
SHADE = "#C9D8E8"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})


def axes(ax, xlim, ylim, xlabel="x", ylabel="y"):
    for side in ("right", "top"):
        ax.spines[side].set_visible(False)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, ms=4)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, ms=4)
    ax.annotate(xlabel, xy=(1, 0), xycoords=("axes fraction", "data"), xytext=(4, -12), textcoords="offset points")
    ax.annotate(ylabel, xy=(0, 1), xycoords=("data", "axes fraction"), xytext=(6, -4), textcoords="offset points")
    ax.grid(False)


def save(fig, name):
    fig.savefig(OUT / f"pb05_{name}.png", dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def inverse_trig():
    fig, ax = plt.subplots(figsize=(6, 4))
    axes(ax, (-4.2, 4.2), (-1.9, 3.5))
    x = np.linspace(-1, 1, 300)
    ax.plot(x, np.arcsin(x), color=RED, lw=2, label="y = arcsin x")
    ax.plot(x, np.arccos(x), color=NAVY, lw=2, label="y = arccos x")
    xt = np.linspace(-4.2, 4.2, 400)
    ax.plot(xt, np.arctan(xt), color=GREEN, lw=2, label="y = arctan x")
    for c in (np.pi / 2, -np.pi / 2):
        ax.axhline(c, color=GREEN, ls="--", lw=0.8)
    ax.axhline(np.pi, color=GREY, ls=":", lw=0.8)
    ax.text(-4.1, np.pi / 2 + 0.08, "y = π/2", color=GREEN, fontsize=8)
    ax.text(-4.1, -np.pi / 2 + 0.08, "y = −π/2", color=GREEN, fontsize=8)
    ax.text(-4.1, np.pi + 0.08, "y = π", color=GREY, fontsize=8)
    for px, py, lab, off in ((1, np.pi / 2, "(1, π/2)", (6, -4)), (-1, -np.pi / 2, "(−1, −π/2)", (-58, -4)),
                             (-1, np.pi, "(−1, π)", (-44, -4)), (1, 0, "(1, 0)", (4, 6))):
        ax.plot(px, py, "o", color="black", ms=3.5)
        ax.annotate(lab, (px, py), xytext=off, textcoords="offset points", fontsize=8)
    ax.legend(loc="lower right", frameon=False, fontsize=9)
    save(fig, "inverse_trig")


def area_curve():
    """y = 5 cosh x − 3 sinh x, minimum (ln 2, 4); region under it for 0 ≤ x ≤ ln 2."""
    fig, ax = plt.subplots(figsize=(6, 4))
    axes(ax, (-1.2, 2.3), (-0.4, 8))
    x = np.linspace(-1.1, 2.2, 400)
    f = 5 * np.cosh(x) - 3 * np.sinh(x)
    ax.plot(x, f, color=NAVY, lw=2)
    xs = np.linspace(0, np.log(2), 100)
    ax.fill_between(xs, 0, 5 * np.cosh(xs) - 3 * np.sinh(xs), color=SHADE)
    ax.plot([np.log(2)] * 2, [0, 4], color=NAVY, lw=0.8, ls="--")
    ax.plot(np.log(2), 4, "o", color=RED, ms=4)
    ax.annotate("(ln 2, 4)", (np.log(2), 4), xytext=(4, -16), textcoords="offset points", fontsize=8)
    ax.text(0.15, 1.8, "R", fontsize=11)
    ax.text(1.55, 4.3, "y = 5 cosh x − 3 sinh x", color=NAVY, fontsize=9, ha="left")
    ax.set_xticks([-1, 1, 2])
    ax.text(np.log(2), -0.35, "ln 2", fontsize=9, ha="center", va="top")
    save(fig, "area")


if __name__ == "__main__":
    inverse_trig()
    area_curve()
    print("pb05 figures written to", OUT)
