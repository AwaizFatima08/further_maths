"""Figures for unit B4 (pb04): graphs of the hyperbolic functions, their reciprocals and inverses.

Run: python pure/figures/pb04_figs.py  (writes pb04_*.png next to this file)
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
    """Axes through the origin with arrow heads and labels at the ends."""
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
    fig.savefig(OUT / f"pb04_{name}.png", dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def basic():
    """sinh, cosh and tanh, with the exponential guide curves."""
    x = np.linspace(-3, 3, 400)
    fig, ax = plt.subplots(figsize=(6, 4))
    axes(ax, (-3.2, 3.2), (-4.2, 4.6))
    ax.plot(x, 0.5 * np.exp(x), ":", color=GREY, lw=1)
    ax.plot(x, 0.5 * np.exp(-x), ":", color=GREY, lw=1)
    ax.plot(x, -0.5 * np.exp(-x), ":", color=GREY, lw=1)
    ax.plot(x, np.cosh(x), color=NAVY, lw=2, label="y = cosh x")
    ax.plot(x, np.sinh(x), color=RED, lw=2, label="y = sinh x")
    ax.plot(x, np.tanh(x), color=GREEN, lw=2, label="y = tanh x")
    for c in (1, -1):
        ax.axhline(c, color=GREEN, ls="--", lw=0.8)
    ax.text(2.2, 1.12, "y = 1", color=GREEN, fontsize=8)
    ax.text(-3.0, -0.88, "y = −1", color=GREEN, fontsize=8)
    ax.text(1.75, 3.9, "½eˣ", color=GREY, fontsize=8)
    ax.text(-2.6, 4.1, "½e⁻ˣ", color=GREY, fontsize=8)
    ax.text(-2.7, -3.9, "−½e⁻ˣ", color=GREY, fontsize=8)
    ax.plot(0, 1, "o", color=NAVY, ms=4)
    ax.annotate("(0, 1)", (0, 1), xytext=(6, 4), textcoords="offset points", fontsize=8)
    ax.legend(loc="lower right", frameon=False, fontsize=9)
    save(fig, "basic")


def reciprocal():
    """sech, cosech and coth."""
    fig, ax = plt.subplots(figsize=(6, 4))
    axes(ax, (-3.2, 3.2), (-4, 4))
    x = np.linspace(-3, 3, 400)
    ax.plot(x, 1 / np.cosh(x), color=NAVY, lw=2, label="y = sech x")
    for xs in (np.linspace(0.05, 3, 300), np.linspace(-3, -0.05, 300)):
        ax.plot(xs, 1 / np.sinh(xs), color=RED, lw=2, label="y = cosech x" if xs[0] > 0 else None)
        ax.plot(xs, 1 / np.tanh(xs), color=GREEN, lw=2, ls="-.", label="y = coth x" if xs[0] > 0 else None)
    for c in (1, -1):
        ax.axhline(c, color=GREEN, ls="--", lw=0.8)
    ax.text(2.3, 1.15, "y = 1", color=GREEN, fontsize=8)
    ax.text(-3.0, -0.8, "y = −1", color=GREEN, fontsize=8)
    ax.legend(loc="lower right", frameon=False, fontsize=9)
    save(fig, "reciprocal")


def inverse():
    """arsinh, arcosh and artanh, each the reflection of its function in y = x."""
    fig, ax = plt.subplots(figsize=(6, 4))
    axes(ax, (-4, 4.2), (-3, 3))
    x = np.linspace(-4, 4, 400)
    ax.plot(x, x, ":", color=GREY, lw=1)
    ax.text(2.4, 2.65, "y = x", color=GREY, fontsize=8)
    ax.plot(x, np.arcsinh(x), color=RED, lw=2, label="y = arsinh x")
    xc = np.linspace(1, 4, 300)
    ax.plot(xc, np.arccosh(xc), color=NAVY, lw=2, label="y = arcosh x")
    ax.plot(1, 0, "o", color=NAVY, ms=4)
    ax.annotate("(1, 0)", (1, 0), xytext=(4, -12), textcoords="offset points", fontsize=8)
    xt = np.linspace(-0.995, 0.995, 400)
    ax.plot(xt, np.arctanh(xt), color=GREEN, lw=2, label="y = artanh x")
    for c in (1, -1):
        ax.axvline(c, color=GREEN, ls="--", lw=0.8)
    ax.text(-1.0, 2.7, "x = −1", color=GREEN, fontsize=8, ha="right")
    ax.text(1.05, 2.7, "x = 1", color=GREEN, fontsize=8)
    ax.legend(loc="lower right", frameon=False, fontsize=9)
    save(fig, "inverse")


def hyperbola():
    """The point (cosh t, sinh t) on the hyperbola x² − y² = 1."""
    fig, ax = plt.subplots(figsize=(6, 4))
    axes(ax, (-3.2, 3.4), (-2.6, 2.6))
    t = np.linspace(-1.7, 1.7, 300)
    ax.plot(np.cosh(t), np.sinh(t), color=NAVY, lw=2)
    ax.plot(-np.cosh(t), np.sinh(t), color=NAVY, lw=2, ls="--")
    xs = np.linspace(-3.2, 3.2, 10)
    ax.plot(xs, xs, ":", color=GREY, lw=1)
    ax.plot(xs, -xs, ":", color=GREY, lw=1)
    t0 = 1.0
    px, py = np.cosh(t0), np.sinh(t0)
    ax.plot(px, py, "o", color=RED, ms=5)
    ax.plot([px, px], [0, py], color=RED, lw=1)
    ax.annotate("P(cosh t, sinh t)", (px, py), xytext=(8, 0), textcoords="offset points", fontsize=9, color=RED)
    ax.text(2.0, -1.2, "x² − y² = 1", color=NAVY, fontsize=9)
    ax.text(2.55, 2.2, "y = x", color=GREY, fontsize=8)
    ax.plot(1, 0, "o", color=NAVY, ms=4)
    ax.annotate("(1, 0)", (1, 0), xytext=(4, -12), textcoords="offset points", fontsize=8)
    ax.set_aspect("equal")
    save(fig, "hyperbola")


def rform():
    """y = 5 cosh x + 4 sinh x = 3 cosh(x + ln 3) and the line y = 5 (worked example 6)."""
    fig, ax = plt.subplots(figsize=(6, 4))
    axes(ax, (-4, 1.6), (-0.6, 11))
    x = np.linspace(-4, 1.3, 400)
    ax.plot(x, 5 * np.cosh(x) + 4 * np.sinh(x), color=NAVY, lw=2, label="y = 5 cosh x + 4 sinh x")
    ax.axhline(5, color=RED, lw=1.2, ls="--")
    ax.text(0.9, 5.3, "y = 5", color=RED, fontsize=9)
    xm = -np.log(3)
    ax.plot(xm, 3, "o", color=NAVY, ms=4)
    ax.annotate("(−ln 3, 3)", (xm, 3), xytext=(-22, -16), textcoords="offset points", fontsize=8)
    for xr in (0, -2 * np.log(3)):
        ax.plot(xr, 5, "o", color=RED, ms=4)
    ax.annotate("(−2 ln 3, 5)", (-2 * np.log(3), 5), xytext=(-62, -14), textcoords="offset points", fontsize=8)
    ax.annotate("(0, 5)", (0, 5), xytext=(6, -14), textcoords="offset points", fontsize=8)
    ax.text(-2.45, 9.6, "y = 5 cosh x + 4 sinh x", color=NAVY, fontsize=9)
    save(fig, "rform")


if __name__ == "__main__":
    basic()
    reciprocal()
    inverse()
    hyperbola()
    rform()
    print("pb04 figures written to", OUT)
