"""Figures for Unit A14 (volumes of revolution, mean value). Writes pa14_*.png into this folder."""
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
    fig.savefig(HERE / f"pa14_{name}.png", dpi=200, facecolor="white", bbox_inches="tight")
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


def disc():
    f = lambda x: x**2 + 1
    fig, ax = plt.subplots(figsize=(6, 4))
    xs = np.linspace(0, 2, 200)
    ax.fill_between(xs, 0, f(xs), color=FILL)
    ax.plot(xs, f(xs), color=NAVY, lw=2)
    ax.plot(xs, -f(xs), color=NAVY, lw=1.2, ls="--")
    ax.plot([2, 2], [-f(2), f(2)], color=NAVY, lw=1)
    x0, dx = 1.2, 0.12
    ax.add_patch(plt.Rectangle((x0, 0), dx, f(x0 + dx / 2), color=RED, alpha=0.55))
    ax.add_patch(Ellipse((x0 + dx / 2, 0), 0.25, 2 * f(x0 + dx / 2), fill=False, ec=RED, lw=1.2))
    for xe in [0.4, 2.0]:
        ax.add_patch(Ellipse((xe, 0), 0.3, 2 * f(xe), fill=False, ec=GREY, lw=0.8, ls=":"))
    ax.annotate("δx", (x0 + dx / 2, -0.25), ha="center", va="top", color=RED)
    ax.annotate("y", (x0 - 0.05, f(x0) / 2), ha="right", color=RED)
    ax.text(0.75, 3.6, "y = x² + 1", color=NAVY)
    ax.text(2.03, -0.35, "2", ha="left")
    axes(ax, (-0.3, 2.6), (-5.5, 5.8))
    ax.set_xticks([]), ax.set_yticks([])
    save(fig, "disc")


def solid3d():
    fig = plt.figure(figsize=(6, 4.5))
    ax = fig.add_subplot(111, projection="3d")
    xs = np.linspace(0, 2, 60)
    th = np.linspace(0, 2 * np.pi, 60)
    X, T = np.meshgrid(xs, th)
    Rr = X**2 + 1
    ax.plot_surface(X, Rr * np.cos(T), Rr * np.sin(T), color=FILL, edgecolor=NAVY, lw=0.2, alpha=0.9, rstride=4, cstride=4, shade=False)
    ax.plot(xs, np.zeros_like(xs), xs**2 + 1, color=NAVY, lw=2)
    ax.plot([-0.5, 2.8], [0, 0], [0, 0], color="k", lw=1)
    ax.text(2.9, 0, 0, "x")
    ax.set_axis_off()
    ax.view_init(elev=18, azim=-62)
    ax.set_xlim(-0.3, 2.6), ax.set_ylim(-5, 5), ax.set_zlim(-5, 5)
    ax.set_box_aspect((1.4, 2, 2), zoom=1.1)
    save(fig, "solid3d")


def washer():
    fig, ax = plt.subplots(figsize=(6, 4))
    xs = np.linspace(0, 2, 200)
    y1, y2 = 3 * xs - xs**2, xs
    ax.fill_between(xs, y2, y1, color=FILL)
    xx = np.linspace(-0.2, 3.1, 300)
    ax.plot(xx, 3 * xx - xx**2, color=NAVY, lw=2)
    ax.plot(xx, xx, color=NAVY, lw=1.6)
    x0 = 0.9
    ax.plot([x0, x0], [0, 3 * x0 - x0**2], color=RED, lw=1.2, ls="--")
    ax.plot([x0], [x0], "o", color=RED, ms=4)
    ax.plot([x0], [3 * x0 - x0**2], "o", color=RED, ms=4)
    ax.text(x0 + 0.06, x0 - 0.35, "y₂", color=RED)
    ax.text(x0 + 0.06, 3 * x0 - x0**2 + 0.08, "y₁", color=RED)
    ax.text(2.55, 2.9, "y = x", color=NAVY)
    ax.text(2.6, 0.55, "y = 3x − x²", color=NAVY)
    ax.text(1.3, 1.6, "R", fontsize=13, color=NAVY)
    ax.plot([2], [2], "ko", ms=3)
    ax.text(2.12, 1.55, "(2, 2)")
    axes(ax, (-0.3, 3.3), (-0.5, 3.2))
    ax.set_xticks([1, 2, 3]), ax.set_yticks([1, 2, 3])
    save(fig, "washer")


def mean():
    fig, ax = plt.subplots(figsize=(6, 4))
    xs = np.linspace(0, 4, 200)
    ax.fill_between(xs, 0, xs * (4 - xs), color=FILL)
    ax.plot(xs, xs * (4 - xs), color=NAVY, lw=2)
    m = 8 / 3
    ax.plot([0, 4, 4], [m, m, 0], color=RED, lw=1.6, ls="--")
    ax.text(4.05, m, "f̄ = 8/3", color=RED, va="center")
    ax.text(1.4, 4.15, "y = x(4 − x)", color=NAVY)
    axes(ax, (-0.3, 5.0), (-0.4, 4.6))
    ax.set_xticks([1, 2, 3, 4]), ax.set_yticks([1, 2, 3, 4])
    save(fig, "mean")


if __name__ == "__main__":
    disc(), solid3d(), washer(), mean()
    print("pa14 figures written")
