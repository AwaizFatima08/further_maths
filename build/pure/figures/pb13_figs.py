"""Figures for Unit B13 (reduction formulae, arc length, surface area). Writes pb13_*.png into this folder."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Ellipse  # noqa: E402

HERE = Path(__file__).resolve().parent
NAVY = "#1F3A5F"
RED = "#8A2C1E"
GREY = "#777777"
FILL = "#C9DCEB"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})


def save(fig, name):
    fig.savefig(HERE / f"pb13_{name}.png", dpi=200, facecolor="white", bbox_inches="tight")
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


def ds():
    f = lambda x: 0.15 * x**2 + 0.5
    fig, ax = plt.subplots(figsize=(5.5, 3.8))
    xs = np.linspace(0, 4, 200)
    ax.plot(xs, f(xs), color=NAVY, lw=2)
    x0, x1 = 2.0, 3.2
    ax.plot([x0, x1], [f(x0), f(x0)], color=RED, lw=1.3)
    ax.plot([x1, x1], [f(x0), f(x1)], color=RED, lw=1.3)
    xm = np.linspace(x0, x1, 50)
    ax.plot(xm, f(xm), color=RED, lw=3)
    ax.text((x0 + x1) / 2, f(x0) - 0.18, "δx", color=RED, ha="center")
    ax.text(x1 + 0.08, (f(x0) + f(x1)) / 2, "δy", color=RED, va="center")
    ax.text((x0 + x1) / 2 - 0.25, (f(x0) + f(x1)) / 2 + 0.2, "δs", color=RED, ha="right")
    axes(ax, (-0.2, 4.3), (-0.2, 3.2))
    ax.set_xticks([]), ax.set_yticks([])
    save(fig, "ds")


def band():
    f = lambda x: 0.12 * x**2 + 0.6
    fig, ax = plt.subplots(figsize=(6, 4))
    xs = np.linspace(0, 4, 200)
    ax.plot(xs, f(xs), color=NAVY, lw=2)
    ax.plot(xs, -f(xs), color=NAVY, lw=1, ls="--")
    x0, x1 = 2.2, 2.6
    for xe, st in [(x0, "-"), (x1, "-")]:
        ax.add_patch(Ellipse((xe, 0), 0.35, 2 * f(xe), fill=False, ec=RED, lw=1.2, ls=st))
    xm = np.linspace(x0, x1, 30)
    ax.fill_between(xm, -f(xm), f(xm), color=RED, alpha=0.15)
    ax.plot([x0, x0], [0, f(x0)], color=GREY, lw=1, ls=":")
    ax.text(x0 - 0.1, f(x0) / 2, "y", ha="right", color=GREY)
    ax.text((x0 + x1) / 2, f(x1) + 0.18, "δs", color=RED, ha="center")
    axes(ax, (-0.2, 4.4), (-2.8, 2.8))
    ax.set_xticks([]), ax.set_yticks([])
    save(fig, "band")


def cycloid():
    fig, ax = plt.subplots(figsize=(6, 2.8))
    ts = np.linspace(0, 2 * np.pi, 300)
    ax.plot(ts - np.sin(ts), 1 - np.cos(ts), color=NAVY, lw=2)
    axes(ax, (-0.3, 7), (-0.2, 2.6))
    ax.set_xticks([np.pi, 2 * np.pi], ["π", "2π"]), ax.set_yticks([1, 2])
    ax.set_aspect("equal")
    save(fig, "cycloid")


def cardioid():
    fig, ax = plt.subplots(figsize=(5, 4))
    th = np.linspace(0, 2 * np.pi, 400)
    r = 1 + np.cos(th)
    ax.plot(r * np.cos(th), r * np.sin(th), color=NAVY, lw=2)
    ax.plot([0, 2.3], [0, 0], color="k", lw=1)
    ax.plot(0, 0, "ko", ms=3)
    ax.text(0.02, -0.2, "O", fontsize=10)
    ax.text(2.0, 0.08, "2a", fontsize=10)
    ax.text(2.3, -0.2, "initial line", fontsize=9, ha="right", va="top", color=GREY)
    ax.set_xlim(-0.6, 2.4), ax.set_ylim(-1.5, 1.5), ax.set_aspect("equal"), ax.axis("off")
    save(fig, "cardioid")


def loop():
    fig, ax = plt.subplots(figsize=(6, 3.6))
    ts = np.linspace(-np.sqrt(3), np.sqrt(3), 400)
    ax.plot(3 * ts**2, 3 * ts - ts**3, color=NAVY, lw=2)
    ax.plot(9, 0, "ko", ms=3)
    ax.text(9.2, 0.15, "(9, 0)")
    ax.text(4.6, 2.3, "t > 0", color=GREY), ax.text(4.6, -2.6, "t < 0", color=GREY)
    axes(ax, (-0.5, 11), (-3.2, 3.2))
    ax.set_xticks([3, 6, 9]), ax.set_yticks([-2, 2])
    save(fig, "loop")


if __name__ == "__main__":
    ds(), band(), cycloid(), cardioid(), loop()
    print("pb13 figures written")
