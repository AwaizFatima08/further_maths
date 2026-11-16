"""Figures for unit C2 (pc02): Taylor polynomials about a point other than 0.

Run: python pure/figures/pc02_figs.py  (writes pc02_*.png next to this file)
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
    fig.savefig(OUT / f"pc02_{name}.png", dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def sin_taylor():
    fig, ax = plt.subplots(figsize=(6, 4))
    axes(ax, (-0.3, 2 * np.pi + 0.3), (-2.2, 2.2))
    x = np.linspace(0, 2 * np.pi, 500)
    h = x - np.pi
    ax.plot(x, np.sin(x), color=NAVY, lw=2.2, label="y = sin x")
    ax.plot(x, -h, color=GREEN, lw=1.4, ls="--", label="y = −(x − π)  (linear)")
    ax.plot(x, -h + h ** 3 / 6, color=RED, lw=1.6, label="y = −(x − π) + (x − π)³/6  (cubic)")
    ax.plot(np.pi, 0, "ko", ms=4)
    ax.set_xticks([np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi], ["π/2", "π", "3π/2", "2π"])
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), frameon=False, fontsize=8.5, ncol=2)
    save(fig, "sin_taylor")


def ln_taylor():
    fig, ax = plt.subplots(figsize=(6, 4))
    axes(ax, (-0.2, 4.6), (-1.6, 1.9))
    x = np.linspace(0.05, 4.5, 500)
    h = x - 2
    ln2 = np.log(2)
    ax.plot(x, np.log(x), color=NAVY, lw=2.2, label="y = ln x")
    ax.plot(x, ln2 + h / 2 - h ** 2 / 8, color=GREEN, lw=1.4, ls="--", label="Taylor polynomial to (x − 2)²")
    ax.plot(x, ln2 + h / 2 - h ** 2 / 8 + h ** 3 / 24, color=RED, lw=1.6, label="Taylor polynomial to (x − 2)³")
    ax.plot(2, ln2, "ko", ms=4)
    ax.annotate("(2, ln 2)", (2, ln2), xytext=(6, -14), textcoords="offset points", fontsize=8)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.1), frameon=False, fontsize=8.5, ncol=2)
    save(fig, "ln_taylor")


if __name__ == "__main__":
    sin_taylor()
    ln_taylor()
    print("pc02 figures written to", OUT)
