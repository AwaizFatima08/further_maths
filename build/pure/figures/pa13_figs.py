"""Figures for Unit A13 (curve sketching, rational functions and inequalities). Writes pa13_*.png here."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

HERE = Path(__file__).resolve().parent
NAVY = "#1F3A5F"
RED = "#B03A2E"
GREY = "#777777"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "axes.grid": False})


def axes(ax, xlim, ylim):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["left"].set_color("black")
    ax.spines["bottom"].set_color("black")
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, ms=4)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, ms=4)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.text(xlim[1], 0, "  x", va="center", ha="left")
    ax.text(0, ylim[1], "y", va="bottom", ha="center")


def panel(ax, text):
    ax.text(0.5, -0.06, text, transform=ax.transAxes, ha="center", va="top", fontsize=11)


def branch(ax, f, a, b, color=NAVY, lw=1.8, ylim=None, **kw):
    xs = np.linspace(a, b, 1200)
    ys = f(xs)
    if ylim:
        ys = np.where((ys < ylim[0] - 5) | (ys > ylim[1] + 5), np.nan, ys)
    ax.plot(xs, ys, color=color, lw=lw, **kw)


def vline(ax, x0, ylim, label=None):
    ax.plot([x0, x0], ylim, ls="--", color=GREY, lw=1)
    if label:
        ax.text(x0, ylim[1], label, ha="center", va="bottom", fontsize=9, color=GREY)


def hline(ax, y0, xlim, label=None, side="right"):
    ax.plot(xlim, [y0, y0], ls="--", color=GREY, lw=1)
    if label:
        x = xlim[1] if side == "right" else xlim[0]
        ax.text(x, y0 + 0.15, label, ha="right" if side == "right" else "left", va="bottom", fontsize=9, color=GREY)


def pt(ax, x, y, text, dx=0.15, dy=0.25, ha="left"):
    ax.plot([x], [y], "o", color=NAVY, ms=4)
    ax.text(x + dx, y + dy, text, fontsize=9, ha=ha)


def save(fig, name):
    fig.savefig(HERE / f"pa13_{name}.png", dpi=200, facecolor="white", bbox_inches="tight")
    plt.close(fig)


# 1. y = (2x + 1)/(x - 3)
fig, ax = plt.subplots(figsize=(6, 4))
xl, yl = (-8, 12), (-8, 12)
axes(ax, xl, yl)
f = lambda x: (2 * x + 1) / (x - 3)  # noqa: E731
branch(ax, f, xl[0], 2.999, ylim=yl)
branch(ax, f, 3.001, xl[1], ylim=yl)
vline(ax, 3, yl, "x = 3")
hline(ax, 2, xl, "y = 2")
pt(ax, 0, -1 / 3, "(0, −1/3)", dx=0.3, dy=-0.9)
pt(ax, -0.5, 0, "(−1/2, 0)", dx=-0.3, dy=0.4, ha="right")
save(fig, "linear")

# 2. y = (x + 1)/(x^2 + 3)
fig, ax = plt.subplots(figsize=(6, 3.6))
xl, yl = (-10, 10), (-0.4, 0.75)
axes(ax, xl, yl)
f = lambda x: (x + 1) / (x**2 + 3)  # noqa: E731
branch(ax, f, *xl)
pt(ax, 1, 0.5, "max (1, 1/2)", dx=0.3, dy=0.03)
pt(ax, -3, -1 / 6, "min (−3, −1/6)", dx=0, dy=-0.1, ha="center")
pt(ax, 0, 1 / 3, "(0, 1/3)", dx=-0.3, dy=0.04, ha="right")
pt(ax, -1, 0, "(−1, 0)", dx=-0.2, dy=0.04, ha="right")
ax.text(9.5, 0.04, "y → 0", fontsize=9, color=GREY, ha="right")
save(fig, "range")

# 3. y = (x^2 + x - 2)/(x - 2), oblique asymptote y = x + 3
fig, ax = plt.subplots(figsize=(6, 4.2))
xl, yl = (-8, 12), (-10, 22)
axes(ax, xl, yl)
f = lambda x: (x**2 + x - 2) / (x - 2)  # noqa: E731
branch(ax, f, xl[0], 1.999, ylim=yl)
branch(ax, f, 2.001, xl[1], ylim=yl)
vline(ax, 2, yl, "x = 2")
xs = np.array(xl)
ax.plot(xs, xs + 3, ls="--", color=GREY, lw=1)
ax.text(10.5, 15.2, "y = x + 3", fontsize=9, color=GREY, ha="right")
pt(ax, 0, 1, "max (0, 1)", dx=0.3, dy=0.8)
pt(ax, 4, 9, "min (4, 9)", dx=0.4, dy=-1.6)
pt(ax, -2, 0, "(−2, 0)", dx=-0.3, dy=0.6, ha="right")
pt(ax, 1, 0, "(1, 0)", dx=0.3, dy=-1.6)
save(fig, "oblique")

# 4. f(x) = (x - 1)/(x + 2): |f|, 1/f, y^2 = f
fig, axs = plt.subplots(1, 3, figsize=(11, 3.8))
f = lambda x: (x - 1) / (x + 2)  # noqa: E731
xl, yl = (-8, 6), (-5, 6)
# |f|
ax = axs[0]
axes(ax, xl, yl)
branch(ax, lambda x: f(x), xl[0], -2.001, color="#BBBBBB", lw=1, ylim=yl)
branch(ax, lambda x: f(x), -1.999, xl[1], color="#BBBBBB", lw=1, ylim=yl)
branch(ax, lambda x: np.abs(f(x)), xl[0], -2.001, ylim=yl)
branch(ax, lambda x: np.abs(f(x)), -1.999, xl[1], ylim=yl)
vline(ax, -2, yl, "x = −2")
hline(ax, 1, xl, "y = 1")
pt(ax, 1, 0, "(1, 0)", dx=0.2, dy=-0.7)
pt(ax, 0, 0.5, "(0, 1/2)", dx=0.2, dy=0.2)
panel(ax, "y = |f(x)|")
# 1/f
ax = axs[1]
axes(ax, xl, yl)
g = lambda x: (x + 2) / (x - 1)  # noqa: E731
branch(ax, f, xl[0], -2.001, color="#BBBBBB", lw=1, ylim=yl)
branch(ax, f, -1.999, xl[1], color="#BBBBBB", lw=1, ylim=yl)
branch(ax, g, xl[0], 0.999, ylim=yl)
branch(ax, g, 1.001, xl[1], ylim=yl)
vline(ax, 1, yl, "x = 1")
hline(ax, 1, xl, "y = 1")
pt(ax, -2, 0, "(−2, 0)", dx=-0.2, dy=0.3, ha="right")
pt(ax, 0, -2, "(0, −2)", dx=0.2, dy=-0.6)
panel(ax, "y = 1/f(x)")
# y^2 = f
ax = axs[2]
xl3, yl3 = (-8, 6), (-4, 4)
axes(ax, xl3, yl3)
for sgn in (1, -1):
    branch(ax, lambda x: sgn * np.sqrt(np.clip(f(x), 0, None)), xl3[0], -2.0005, ylim=yl3)
    branch(ax, lambda x: sgn * np.sqrt(np.clip(f(x), 0, None)), 1, xl3[1], ylim=yl3)
vline(ax, -2, yl3, "x = −2")
hline(ax, 1, xl3, "y = 1")
hline(ax, -1, xl3, "y = −1")
pt(ax, 1, 0, "(1, 0)", dx=0.2, dy=0.25)
panel(ax, "y² = f(x)")
fig.tight_layout()
save(fig, "modrecip")

# 5. 1/(x - 1) and x/(x + 2): solution set of 1/(x-1) > x/(x+2)
fig, ax = plt.subplots(figsize=(6, 4.2))
xl, yl = (-7, 7), (-7, 7)
axes(ax, xl, yl)
f1 = lambda x: 1 / (x - 1)  # noqa: E731
f2 = lambda x: x / (x + 2)  # noqa: E731
branch(ax, f1, xl[0], 0.999, ylim=yl, label="y = 1/(x − 1)")
branch(ax, f1, 1.001, xl[1], ylim=yl)
branch(ax, f2, xl[0], -2.001, color=RED, ylim=yl, label="y = x/(x + 2)")
branch(ax, f2, -1.999, xl[1], color=RED, ylim=yl)
vline(ax, 1, yl)
vline(ax, -2, yl)
for a, b in [(-2, 1 - np.sqrt(3)), (1, 1 + np.sqrt(3))]:
    ax.plot([a, b], [0, 0], color="#2E8B57", lw=5, alpha=0.6, solid_capstyle="butt")
for x0 in (1 - np.sqrt(3), 1 + np.sqrt(3)):
    ax.plot([x0], [f1(x0)], "o", color="black", ms=4)
ax.text(1 - np.sqrt(3), -1.2, "1 − √3", ha="center", fontsize=9)
ax.text(1 + np.sqrt(3), -1.2, "1 + √3", ha="center", fontsize=9)
ax.text(-2, -1.2, "−2", ha="center", fontsize=9)
ax.text(1.05, -1.2, "1", ha="left", fontsize=9)
ax.legend(loc="upper left", fontsize=9, frameon=False)
save(fig, "ineq")

# 6. |x^2 - 1| and 2(x + 1)
fig, ax = plt.subplots(figsize=(6, 4))
xl, yl = (-4, 5), (-3, 14)
axes(ax, xl, yl)
branch(ax, lambda x: np.abs(x**2 - 1), *xl, label="y = |x² − 1|")
branch(ax, lambda x: 2 * (x + 1), *xl, color=RED, label="y = 2(x + 1)")
for a, b in [(-4, -1), (3, 5)]:
    ax.plot([a, b], [0, 0], color="#2E8B57", lw=5, alpha=0.6, solid_capstyle="butt")
pt(ax, -1, 0, "(−1, 0)", dx=-0.15, dy=0.5, ha="right")
pt(ax, 3, 8, "(3, 8)", dx=-0.2, dy=0.5, ha="right")
ax.legend(loc="upper left", fontsize=9, frameon=False)
save(fig, "modineq")

# 7. Notes figure: f(x) = (x + 1)(x - 1)(x - 3) with y^2 = f(x)
fig, axs = plt.subplots(1, 2, figsize=(10, 3.8))
f = lambda x: (x + 1) * (x - 1) * (x - 3)  # noqa: E731
xl, yl = (-2.5, 5), (-6, 9)
ax = axs[0]
axes(ax, xl, yl)
branch(ax, f, *xl, ylim=yl)
for x0 in (-1, 1, 3):
    ax.plot([x0], [0], "o", color=NAVY, ms=4)
ax.text(-1, -1.0, "−1", ha="center", fontsize=9)
ax.text(1, 0.5, "1", ha="center", fontsize=9)
ax.text(3, -1.0, "3", ha="center", fontsize=9)
pt(ax, 0, 3, "(0, 3)", dx=0.15, dy=0.3)
panel(ax, "y = f(x)")
ax = axs[1]
xl2, yl2 = (-2.5, 5), (-3.5, 3.5)
axes(ax, xl2, yl2)
xs = np.linspace(-1, 1, 4001)
top = np.sqrt(np.clip(f(xs), 0, None))
ax.plot(np.concatenate([xs, xs[::-1]]), np.concatenate([top, -top[::-1]]), color=NAVY, lw=1.8)
xs = np.linspace(3, xl2[1], 2000)
top = np.sqrt(np.clip(f(xs), 0, None))
ax.plot(xs, top, color=NAVY, lw=1.8)
ax.plot(xs, -top, color=NAVY, lw=1.8)
for x0 in (-1, 1, 3):
    ax.plot([x0], [0], "o", color=NAVY, ms=4)
ax.text(-1.1, 0.25, "−1", ha="right", fontsize=9)
ax.text(1.1, 0.25, "1", ha="left", fontsize=9)
ax.text(3.1, 0.25, "3", ha="left", fontsize=9)
ax.text(0.1, np.sqrt(3) + 0.15, "(0, √3)", fontsize=9)
panel(ax, "y² = f(x)")
fig.tight_layout()
save(fig, "ysq")
print("written pa13 figures")
