"""Figures for unit C1 (pc01): reciprocal trigonometric graphs, the t-formula triangle and a lost root.

Run: python pure/figures/pc01_figs.py  (writes pc01_*.png next to this file)
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
PI_TICKS = ([-2 * np.pi, -3 * np.pi / 2, -np.pi, -np.pi / 2, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
            ["−2π", "−3π/2", "−π", "−π/2", "π/2", "π", "3π/2", "2π"])


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
    fig.savefig(OUT / f"pc01_{name}.png", dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def pieces(f, x, lim=6):
    y = f(x)
    y[np.abs(y) > lim] = np.nan
    return y


def reciprocal():
    fig, axs = plt.subplots(3, 1, figsize=(6, 7.2))
    x = np.linspace(-2 * np.pi, 2 * np.pi, 4000)
    specs = [("y = sec x", lambda t: 1 / np.cos(t), np.cos, "y = cos x", [-3 * np.pi / 2, -np.pi / 2, np.pi / 2, 3 * np.pi / 2]),
             ("y = cosec x", lambda t: 1 / np.sin(t), np.sin, "y = sin x", [-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi]),
             ("y = cot x", lambda t: 1 / np.tan(t), None, None, [-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi])]
    for ax, (lab, f, g, glab, asym) in zip(axs, specs):
        axes(ax, (-2 * np.pi - 0.3, 2 * np.pi + 0.3), (-4.5, 4.5))
        for a in asym:
            ax.axvline(a, color=GREEN, ls="--", lw=0.7)
        if g is not None:
            ax.plot(x, g(x), ":", color=GREY, lw=1)
            ax.text(2 * np.pi - 1.2, -1.6 if lab == "y = sec x" else 1.2, glab, color=GREY, fontsize=8)
        ax.plot(x, pieces(f, x), color=NAVY, lw=1.8)
        ax.text(-2 * np.pi, 3.6, lab, color=NAVY, fontsize=10, bbox=dict(fc="white", ec="none", pad=1))
        ax.set_xticks(*PI_TICKS)
        ax.tick_params(labelsize=8)
    fig.tight_layout()
    save(fig, "reciprocal")


def triangle():
    fig, ax = plt.subplots(figsize=(5, 3.2))
    ax.axis("off")
    ax.set_aspect("equal")
    t = 0.6
    A, B, C = (0, 0), (1 - t ** 2, 0), (1 - t ** 2, 2 * t)
    ax.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], color=NAVY, lw=2)
    ax.plot([B[0] - 0.05, B[0] - 0.05, B[0]], [0, 0.05, 0.05], color=NAVY, lw=1)
    a = np.linspace(0, np.arctan2(2 * t, 1 - t ** 2), 30)
    ax.plot(0.15 * np.cos(a), 0.15 * np.sin(a), color=RED)
    ax.text(0.19, 0.08, "θ", color=RED, fontsize=12)
    ax.text(B[0] / 2 - 0.08, -0.12, "1 − t²", fontsize=11)
    ax.text(B[0] + 0.04, t - 0.03, "2t", fontsize=11)
    ax.text(0.12, t + 0.12, "1 + t²", fontsize=11)
    ax.set_xlim(-0.1, 1.0)
    ax.set_ylim(-0.2, 1.35)
    save(fig, "triangle")


def lost_root():
    fig, ax = plt.subplots(figsize=(6, 3.6))
    axes(ax, (-0.2, 2 * np.pi + 0.3), (-2.6, 2.6))
    x = np.linspace(0, 2 * np.pi, 600)
    ax.plot(x, 2 * np.sin(x) - np.cos(x), color=NAVY, lw=2, label="y = 2 sin x − cos x")
    ax.axhline(1, color=RED, ls="--", lw=1.2)
    ax.text(5.6, 1.12, "y = 1", color=RED, fontsize=9)
    x1 = 2 * np.arctan(0.5)
    for xr, lab, off in ((x1, "x = 2 arctan ½ ≈ 0.927", (-60, 10)), (np.pi, "x = π (t undefined)", (8, 6))):
        ax.plot(xr, 1, "o", color=RED, ms=5)
        ax.annotate(lab, (xr, 1), xytext=off, textcoords="offset points", fontsize=8)
    ax.set_xticks([np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi], ["π/2", "π", "3π/2", "2π"])
    ax.legend(loc="lower left", frameon=False, fontsize=9)
    save(fig, "lost_root")


if __name__ == "__main__":
    reciprocal()
    triangle()
    lost_root()
    print("pc01 figures written to", OUT)
