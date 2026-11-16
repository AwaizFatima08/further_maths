"""Figures for unit B8 (pb08): polar coordinates, standard polar curves, areas and tangents.

Curves are drawn with the convention r >= 0: where f(θ) < 0 nothing is plotted.
Run: python pure/figures/pb08_figs.py  (writes pb08_*.png next to this file)
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
SHADE2 = "#F2D7D3"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
TH = np.linspace(0, 2 * np.pi, 2000)


def xy(r, th):
    r = np.where(r >= -1e-12, r, np.nan)
    return r * np.cos(th), r * np.sin(th)


def polar_axes(ax, lim, label_line=True, line_len=None):
    """Blank frame with the pole O, the initial line and a faint θ = π/2 line."""
    (x0, x1), (y0, y1) = lim
    ax.set_xlim(x0, x1)
    ax.set_ylim(y0, y1)
    ax.set_aspect("equal")
    ax.axis("off")
    L = line_len if line_len is not None else x1
    ax.annotate("", xy=(L, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color="black", lw=0.9))
    ax.plot([x0, 0], [0, 0], ":", color=GREY, lw=0.7)
    ax.plot([0, 0], [y0, y1], ":", color=GREY, lw=0.7)
    ax.plot(0, 0, "ko", ms=3)
    ax.annotate("O", (0, 0), xytext=(-10, -11), textcoords="offset points", fontsize=9)
    if label_line:
        ax.annotate("initial line", (L, 0), xytext=(-48, 4), textcoords="offset points", fontsize=8)


def save(fig, name):
    fig.savefig(OUT / f"pb08_{name}.png", dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def point():
    fig, ax = plt.subplots(figsize=(6, 4))
    polar_axes(ax, ((-0.6, 4.2), (-0.5, 3.0)))
    r, th = 3.2, np.radians(40)
    px, py = r * np.cos(th), r * np.sin(th)
    ax.plot([0, px], [0, py], color=NAVY, lw=1.6)
    ax.plot(px, py, "o", color=RED, ms=5)
    ax.annotate("P(r, θ)", (px, py), xytext=(6, 4), textcoords="offset points", color=RED)
    ax.plot([px, px], [0, py], "--", color=GREY, lw=0.8)
    a = np.linspace(0, th, 50)
    ax.plot(0.8 * np.cos(a), 0.8 * np.sin(a), color=NAVY, lw=1)
    ax.text(0.9, 0.25, "θ", fontsize=11)
    ax.text(1.05, 1.25, "r", fontsize=11, color=NAVY)
    ax.text(px + 0.08, py / 2, "y = r sin θ", fontsize=9)
    ax.text(px / 2 - 0.5, -0.3, "x = r cos θ", fontsize=9)
    save(fig, "point")


def standard():
    curves = [
        ("r = a", lambda t: np.ones_like(t), 1.3),
        ("r = 2a cos θ", lambda t: 2 * np.cos(t), 2.3),
        ("r = p sec(α − θ)", None, 2.3),
        ("r = kθ, 0 ≤ θ ≤ 2π", lambda t: t / (2 * np.pi), 1.2),
        ("r = a(1 + cos θ)", lambda t: 1 + np.cos(t), 2.2),
        ("r = a(3 + 2 cos θ)", lambda t: (3 + 2 * np.cos(t)) / 2.5, 2.2),
        ("r = a cos 2θ", lambda t: np.cos(2 * t), 1.2),
        ("r² = a² cos 2θ", lambda t: np.sqrt(np.clip(np.cos(2 * t), 0, None)) * np.where(np.cos(2 * t) >= 0, 1, np.nan), 1.2),
        ("r = a sin 3θ", lambda t: np.sin(3 * t), 1.2),
    ]
    fig, axs = plt.subplots(3, 3, figsize=(7.5, 7.2))
    for ax, (label, f, lim) in zip(axs.flat, curves):
        x0 = -lim if label not in ("r = 2a cos θ",) else -0.4
        polar_axes(ax, ((x0, lim), (-lim, lim)), label_line=False)
        if f is None:  # straight line at distance p = 1.2 from O, foot of perpendicular at angle α = π/3
            p, al = 1.2, np.pi / 3
            t = np.linspace(al - 1.25, al + 1.25, 200)
            ax.plot(p / np.cos(t - al) * np.cos(t), p / np.cos(t - al) * np.sin(t), color=NAVY, lw=1.8)
            ax.plot([0, p * np.cos(al)], [0, p * np.sin(al)], "--", color=RED, lw=1)
            ax.text(0.15, 0.6, "p", color=RED, fontsize=9)
            ax.text(0.35, 0.12, "α", color=RED, fontsize=9)
        else:
            X, Y = xy(f(TH), TH)
            ax.plot(X, Y, color=NAVY, lw=1.8)
        ax.set_title(label, fontsize=9.5, pad=2)
    fig.tight_layout()
    save(fig, "standard")


def limacons():
    fig, ax = plt.subplots(figsize=(6, 4))
    polar_axes(ax, ((-2.2, 5.0), (-3.2, 3.2)), line_len=4.9)
    for p, col, lab, pos in ((1, RED, "p = q: cardioid", (0.3, 1.35)), (1.5, GREEN, "q < p < 2q: dimple", (1.7, 2.1)),
                             (3, NAVY, "p ≥ 2q: convex", (2.6, 2.95))):
        X, Y = xy(p + np.cos(TH), TH)
        s = 4 / (p + 1)
        ax.plot(s * X, s * Y, color=col, lw=1.8, label=lab)
    ax.legend(loc="center left", bbox_to_anchor=(0.98, 0.5), frameon=False, fontsize=9)
    save(fig, "limacons")


def cardioid_area():
    fig, ax = plt.subplots(figsize=(6, 4))
    polar_axes(ax, ((-0.6, 2.6), (-1.5, 1.5)))
    X, Y = xy(1 + np.cos(TH), TH)
    ax.fill(X, Y, color=SHADE)
    ax.plot(X, Y, color=NAVY, lw=2)
    ax.plot(2, 0, "o", color=RED, ms=4)
    ax.annotate("(2a, 0)", (2, 0), xytext=(4, -14), textcoords="offset points", fontsize=8)
    ax.plot(0, 1, "o", color=RED, ms=4)
    ax.annotate("(a, π/2)", (0, 1), xytext=(4, 4), textcoords="offset points", fontsize=8)
    t = 1.0
    r = 1 + np.cos(t)
    a = np.linspace(t, t + 0.12, 20)
    ax.fill(np.r_[0, (1 + np.cos(a)) * np.cos(a), 0], np.r_[0, (1 + np.cos(a)) * np.sin(a), 0], color=RED, alpha=0.6)
    ax.annotate("sector ≈ ½r²δθ", (r * np.cos(t + 0.06) * 0.7, r * np.sin(t + 0.06) * 0.7), xytext=(40, 2),
                textcoords="offset points", fontsize=8, color=RED, arrowprops=dict(arrowstyle="-", color=RED, lw=0.7))
    save(fig, "cardioid_area")


def rose():
    fig, ax = plt.subplots(figsize=(6, 4))
    polar_axes(ax, ((-2.3, 2.3), (-2.3, 2.3)), line_len=2.3)
    X, Y = xy(2 * np.sin(3 * TH), TH)
    ax.plot(X, Y, color=NAVY, lw=2)
    t = np.linspace(0, np.pi / 3, 300)
    Xl, Yl = xy(2 * np.sin(3 * t), t)
    ax.fill(Xl, Yl, color=SHADE)
    ax.plot(Xl, Yl, color=NAVY, lw=2)
    for a in (0, np.pi / 3):
        ax.plot([0, 2.2 * np.cos(a)], [0, 2.2 * np.sin(a)], "--", color=RED, lw=0.9)
    ax.text(2.2 * np.cos(np.pi / 3) + 0.05, 2.2 * np.sin(np.pi / 3) - 0.1, "θ = π/3", color=RED, fontsize=8)
    ax.plot(2 * np.cos(np.pi / 6), 2 * np.sin(np.pi / 6), "o", color=RED, ms=4)
    ax.annotate("(2, π/6)", (2 * np.cos(np.pi / 6), 2 * np.sin(np.pi / 6)), xytext=(5, 2), textcoords="offset points", fontsize=8)
    save(fig, "rose")


def two_curves():
    fig, ax = plt.subplots(figsize=(6, 4))
    polar_axes(ax, ((-0.4, 3.4), (-1.7, 1.7)), line_len=3.4)
    t = np.linspace(-np.pi / 3, np.pi / 3, 400)
    xo, yo = 3 * np.cos(t) * np.cos(t), 3 * np.cos(t) * np.sin(t)
    xi, yi = (1 + np.cos(t)) * np.cos(t), (1 + np.cos(t)) * np.sin(t)
    ax.fill(np.r_[xo, xi[::-1]], np.r_[yo, yi[::-1]], color=SHADE)
    X, Y = xy(3 * np.cos(TH), TH)
    ax.plot(X, Y, color=RED, lw=1.8, label="r = 3 cos θ")
    X, Y = xy(1 + np.cos(TH), TH)
    ax.plot(X, Y, color=NAVY, lw=1.8, label="r = 1 + cos θ")
    for s in (1, -1):
        px, py = 1.5 * np.cos(s * np.pi / 3), 1.5 * np.sin(s * np.pi / 3)
        ax.plot(px, py, "o", color="black", ms=4)
        ax.annotate(f"(3/2, {'' if s > 0 else '−'}π/3)", (px, py), xytext=(6, 2 if s > 0 else -10), textcoords="offset points", fontsize=8)
    ax.text(2.3, 0.15, "R", fontsize=11)
    ax.legend(loc="upper right", frameon=False, fontsize=8)
    save(fig, "two_curves")


def tangents():
    fig, ax = plt.subplots(figsize=(6, 4))
    polar_axes(ax, ((-0.9, 2.6), (-1.6, 1.6)), label_line=False, line_len=2.6)
    X, Y = xy(1 + np.cos(TH), TH)
    ax.plot(X, Y, color=NAVY, lw=2)
    yh = 1.5 * np.sin(np.pi / 3)
    for s in (1, -1):
        ax.plot([-0.9, 2.5], [s * yh, s * yh], "--", color=RED, lw=1)
        ax.plot(0.75, s * yh, "o", color=RED, ms=4)
    ax.annotate("(3a/2, π/3)", (0.75, yh), xytext=(4, 5), textcoords="offset points", fontsize=8, color=RED)
    ax.annotate("(3a/2, −π/3)", (0.75, -yh), xytext=(4, -13), textcoords="offset points", fontsize=8, color=RED)
    xv = 0.5 * np.cos(2 * np.pi / 3)
    for xx in (2.0, xv):
        ax.plot([xx, xx], [-1.55, 1.55], "--", color=GREEN, lw=1)
    for s in (1, -1):
        ax.plot(xv, s * 0.5 * np.sin(2 * np.pi / 3), "o", color=GREEN, ms=4)
    ax.annotate("(a/2, 2π/3)", (xv, 0.5 * np.sin(2 * np.pi / 3)), xytext=(-62, 4), textcoords="offset points", fontsize=8, color=GREEN)
    ax.annotate("(a/2, −2π/3)", (xv, -0.5 * np.sin(2 * np.pi / 3)), xytext=(-66, -10), textcoords="offset points", fontsize=8, color=GREEN)
    ax.plot(2, 0, "o", color=GREEN, ms=4)
    ax.annotate("(2a, 0)", (2, 0), xytext=(4, 4), textcoords="offset points", fontsize=8, color=GREEN)
    save(fig, "tangents")


def exam_region():
    """Section B: r = 4 cos θ and r = 4(1 − cos θ); region inside both shaded."""
    fig, ax = plt.subplots(figsize=(6, 4))
    polar_axes(ax, ((-8.6, 4.6), (-5.4, 5.4)), line_len=4.6)
    t1 = np.linspace(-np.pi / 3, np.pi / 3, 300)
    t2a = np.linspace(np.pi / 3, np.pi / 2, 200)
    t2b = np.linspace(-np.pi / 2, -np.pi / 3, 200)
    # boundary of region: cardioid for |θ| <= π/3, circle for π/3 <= |θ| <= π/2
    xs = np.r_[4 * np.cos(t2b) * np.cos(t2b), 4 * (1 - np.cos(t1)) * np.cos(t1), 4 * np.cos(t2a) * np.cos(t2a)]
    ys = np.r_[4 * np.cos(t2b) * np.sin(t2b), 4 * (1 - np.cos(t1)) * np.sin(t1), 4 * np.cos(t2a) * np.sin(t2a)]
    ax.fill(xs, ys, color=SHADE)
    X, Y = xy(4 * np.cos(TH), TH)
    ax.plot(X, Y, color=RED, lw=1.8)
    X, Y = xy(4 * (1 - np.cos(TH)), TH)
    ax.plot(X, Y, color=NAVY, lw=1.8)
    ax.text(3.0, 2.5, "C₁", color=RED, fontsize=10)
    ax.text(-6.5, 3.7, "C₂", color=NAVY, fontsize=10)
    ax.text(0.55, 1.15, "R", fontsize=10)
    ax.text(0.55, -1.75, "R", fontsize=10)
    save(fig, "exam_region")


if __name__ == "__main__":
    point()
    standard()
    limacons()
    cardioid_area()
    rose()
    two_curves()
    tangents()
    exam_region()
    print("pb08 figures written to", OUT)
