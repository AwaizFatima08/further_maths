"""Figures for Unit B3 (higher derivatives and Maclaurin series). Writes pb03_*.png into this folder."""
from math import factorial
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

HERE = Path(__file__).resolve().parent
NAVY = "#1F3A5F"
RED = "#8A2C1E"
GREY = "#777777"
SHADES = ["#8A2C1E", "#C47A2C", "#4F8A3C", "#6A5ACD"]
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})


def save(fig, name):
    fig.savefig(HERE / f"pb03_{name}.png", dpi=200, facecolor="white", bbox_inches="tight")
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


def ln_partial():
    fig, ax = plt.subplots(figsize=(6, 4))
    xs = np.linspace(-0.95, 2.0, 400)
    ax.plot(xs, np.log(1 + xs), color=NAVY, lw=2.4, label="ln(1 + x)")
    for c, n in zip(SHADES, [2, 5, 10, 20]):
        s = sum((-1) ** (r + 1) * xs**r / r for r in range(1, n + 1))
        ax.plot(xs, s, color=c, lw=1.2, label=f"{n} terms")
    ax.axvline(1, color=GREY, ls=":", lw=1)
    ax.text(1.02, -2.3, "x = 1", color=GREY)
    axes(ax, (-1.1, 2.05), (-2.6, 2.0))
    ax.set_xticks([-1, -0.5, 0.5, 1, 1.5, 2]), ax.set_yticks([-2, -1, 1, 2])
    ax.legend(loc="upper left", fontsize=9, frameon=False)
    save(fig, "ln")


def sin_poly():
    fig, ax = plt.subplots(figsize=(6, 4))
    xs = np.linspace(-2 * np.pi, 2 * np.pi, 500)
    ax.plot(xs, np.sin(xs), color=NAVY, lw=2.4, label="sin x")
    for c, deg in zip(SHADES, [1, 3, 5, 7]):
        p = sum((-1) ** r * xs ** (2 * r + 1) / factorial(2 * r + 1) for r in range((deg + 1) // 2))
        ax.plot(xs, p, color=c, lw=1.2, label=f"degree {deg}")
    axes(ax, (-2 * np.pi, 2 * np.pi), (-2.2, 2.2))
    ax.set_xticks([-2 * np.pi, -np.pi, np.pi, 2 * np.pi], ["−2π", "−π", "π", "2π"])
    ax.set_yticks([-1, 1])
    ax.legend(loc="upper left", fontsize=9, frameon=False)
    save(fig, "sin")


def param():
    fig, ax = plt.subplots(figsize=(6, 4))
    ts = np.linspace(-2.1, 2.1, 400)
    ax.plot(ts**2, ts**3 - 3 * ts, color=NAVY, lw=2)
    for (px, py, lab, dy) in [(1, 2, "max (1, 2)", 0.25), (1, -2, "min (1, −2)", -0.55)]:
        ax.plot(px, py, "o", color=RED, ms=4)
        ax.text(px + 0.1, py + dy, lab, color=RED)
    ax.text(3.6, 2.6, "x = t², y = t³ − 3t", color=NAVY)
    axes(ax, (-0.3, 4.6), (-3.3, 3.3))
    ax.set_xticks([1, 2, 3, 4]), ax.set_yticks([-2, 2])
    save(fig, "param")


if __name__ == "__main__":
    ln_partial(), sin_poly(), param()
    print("pb03 figures written")
