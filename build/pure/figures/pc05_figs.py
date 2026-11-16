"""Figures for Unit C5 (ellipse and hyperbola). Writes pc05_*.png into this folder."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

HERE = Path(__file__).resolve().parent
NAVY = "#1F3A5F"
RED = "#8A2C1E"
GREY = "#777777"
GREEN = "#3B7A57"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})


def axes_through_origin(ax, xlim, ylim):
    ax.set_xlim(*xlim), ax.set_ylim(*ylim)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, ms=4)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, ms=4)
    ax.text(1.0, 0.02, "x", transform=ax.get_yaxis_transform(), ha="right", va="bottom")
    ax.text(0.02, 1.0, "y", transform=ax.get_xaxis_transform(), ha="left", va="top")
    ax.set_xticks([]), ax.set_yticks([])


def save(fig, name):
    fig.savefig(HERE / f"pc05_{name}.png", dpi=200, facecolor="white", bbox_inches="tight")
    plt.close(fig)


def ellipse_fig():
    a, b = 5, 3
    e = 0.8
    fig, ax = plt.subplots(figsize=(6.5, 3.8))
    axes_through_origin(ax, (-7.5, 7.5), (-3.8, 4.2))
    th = np.linspace(0, 2 * np.pi, 400)
    ax.plot(a * np.cos(th), b * np.sin(th), color=NAVY, lw=2)
    for sgn in (1, -1):
        ax.axvline(sgn * a / e, color=RED, ls="--", lw=1.2)
        ax.plot(sgn * a * e, 0, "o", color=RED, ms=5)
    ax.text(6.35, -3.6, "x = a/e", color=RED, fontsize=9)
    ax.text(-6.35, -3.6, "x = −a/e", color=RED, fontsize=9, ha="right")
    ax.text(4.0, -0.55, "S(ae, 0)", color=RED, ha="center", fontsize=9)
    ax.text(-4.0, -0.55, "S′(−ae, 0)", color=RED, ha="center", fontsize=9)
    P = np.array([3, 12 / 5])
    M = np.array([a / e, P[1]])
    ax.plot(*P, "ko", ms=4)
    ax.text(P[0] - 0.2, P[1] + 0.3, "P", ha="right")
    ax.plot(*np.array([P, [4, 0]]).T, color=GREY, lw=1.2)
    ax.plot(*np.array([P, [-4, 0]]).T, color=GREY, lw=1.2)
    ax.plot(*np.array([P, M]).T, color=GREEN, lw=1.2)
    ax.plot(*M, "ko", ms=3)
    ax.text(M[0] + 0.15, M[1], "M", va="center")
    ax.text(4.6, 2.65, "PM", color=GREEN, fontsize=9)
    ax.text(3.7, 1.0, "PS", color=GREY, fontsize=9)
    ax.text(-0.8, 1.45, "PS′", color=GREY, fontsize=9)
    ax.text(5.1, 0.15, "a", fontsize=9)
    ax.text(0.15, 3.1, "b", fontsize=9)
    save(fig, "ellipse")


def hyperbola_fig():
    a, b = 4, 3
    e = 1.25
    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    axes_through_origin(ax, (-9, 9), (-6, 6))
    u = np.linspace(-1.75, 1.75, 300)
    for sgn in (1, -1):
        ax.plot(sgn * a * np.cosh(u), b * np.sinh(u), color=NAVY, lw=2)
        ax.axvline(sgn * a / e, color=RED, ls="--", lw=1.2)
        ax.plot(sgn * a * e, 0, "o", color=RED, ms=5)
    xs = np.array([-9, 9])
    ax.plot(xs, b / a * xs, color=GREY, ls=":", lw=1.2)
    ax.plot(xs, -b / a * xs, color=GREY, ls=":", lw=1.2)
    ax.text(6.0, 4.5, "y = (b/a)x", color=GREY, ha="center", va="center", fontsize=9, bbox=dict(facecolor="white", edgecolor="none", pad=1))
    ax.text(6.0, -4.5, "y = −(b/a)x", color=GREY, ha="center", va="center", fontsize=9, bbox=dict(facecolor="white", edgecolor="none", pad=1))
    ax.text(3.3, 5.3, "x = a/e", color=RED, fontsize=9)
    ax.text(-3.3, 5.3, "x = −a/e", color=RED, fontsize=9, ha="right")
    ax.text(5.1, -0.7, "S(ae, 0)", color=RED, ha="left", fontsize=9)
    ax.text(-5.1, -0.7, "S′(−ae, 0)", color=RED, ha="right", fontsize=9)
    for sgn in (1, -1):
        ax.plot(sgn * a, 0, "ko", ms=3)
    ax.text(3.9, 0.3, "(a, 0)", fontsize=9, ha="right")
    ax.text(-3.9, 0.3, "(−a, 0)", fontsize=9, ha="left")
    save(fig, "hyperbola")


def eccentricity_fig():
    fig, ax = plt.subplots(figsize=(6, 4))
    axes_through_origin(ax, (-1.6, 4.2), (-3.2, 3.2))
    ax.axvline(-1, color=RED, ls="--", lw=1.2)
    ax.text(-1.05, 2.9, "directrix", color=RED, ha="right", fontsize=9)
    ax.plot(0, 0, "o", color=RED, ms=5)
    ax.text(0.08, -0.3, "S", color=RED)
    th = np.linspace(0, 2 * np.pi, 2000)
    for e, col, lab in [(0.5, NAVY, "e = ½ (ellipse)"), (1.0, GREEN, "e = 1 (parabola)"), (2.0, GREY, "e = 2 (hyperbola)")]:
        den = 1 - e * np.cos(th)
        r = np.where(den > 0.02, e / np.where(den > 0.02, den, 1), np.nan)
        x, y = r * np.cos(th), r * np.sin(th)
        x[np.abs(x) > 6] = np.nan
        ax.plot(x, y, color=col, lw=2, label=lab)
    ax.legend(loc="center right", framealpha=1, fontsize=9)
    save(fig, "eccentricity")


def ellipse_tangent_fig():
    fig, ax = plt.subplots(figsize=(6, 4))
    axes_through_origin(ax, (-6.5, 8), (-4.2, 6.2))
    th = np.linspace(0, 2 * np.pi, 400)
    ax.plot(5 * np.cos(th), 3 * np.sin(th), color=NAVY, lw=2)
    xs = np.array([-1, 7.5])
    ax.plot(xs, (25 - 4 * xs) / 5, color=RED, lw=1.4)
    xs2 = np.array([1.5, 6.5])
    ax.plot(xs2, (25 * xs2 - 64) / 20, color=GREY, lw=1.4, ls="--")
    ax.plot(4, 1.8, "ko", ms=4)
    ax.text(4.2, 2.1, "P(4, 9/5)")
    ax.text(0.6, 5.5, "tangent 4x + 5y = 25", color=RED, fontsize=9)
    ax.text(6.0, 3.0, "normal\n25x − 20y = 64", color=GREY, fontsize=9)
    ax.text(-5.8, 3.2, "x²/25 + y²/9 = 1", color=NAVY, fontsize=9)
    save(fig, "ellipse_tangent")


def asymptote_triangle_fig():
    fig, ax = plt.subplots(figsize=(6, 4.2))
    axes_through_origin(ax, (-1, 11), (-3, 6.5))
    u = np.linspace(-1.6, 1.6, 300)
    ax.plot(3 * np.cosh(u), 2 * np.sinh(u), color=NAVY, lw=2)
    xs = np.array([0, 11])
    ax.plot(xs, 2 / 3 * xs, color=GREY, ls=":", lw=1.2)
    ax.plot(xs, -2 / 3 * xs, color=GREY, ls=":", lw=1.2)
    t = 0.9
    A = np.array([3 * np.exp(t), 2 * np.exp(t)])
    B = np.array([3 * np.exp(-t), -2 * np.exp(-t)])
    P = np.array([3 * np.cosh(t), 2 * np.sinh(t)])
    ax.fill([0, A[0], B[0]], [0, A[1], B[1]], color="#cfdde8", alpha=0.7)
    d = A - B
    ax.plot(*np.array([B - 0.15 * d, A + 0.15 * d]).T, color=RED, lw=1.4)
    for X, s, off in [(A, "A(3eᵗ, 2eᵗ)", (-0.3, 0.3)), (B, "B(3e⁻ᵗ, −2e⁻ᵗ)", (0.3, -0.5)),
                      (P, "P(3 cosh t, 2 sinh t)", (0.3, -0.3))]:
        ax.plot(*X, "ko", ms=4)
        ax.text(X[0] + off[0], X[1] + off[1], s, fontsize=9, ha="right" if off[0] < 0 else "left")
    ax.text(-0.3, -0.5, "O")
    ax.text(9.5, 5.2, "y = 2x/3", color=GREY, fontsize=9)
    save(fig, "asymptote_triangle")


if __name__ == "__main__":
    ellipse_fig()
    hyperbola_fig()
    eccentricity_fig()
    ellipse_tangent_fig()
    asymptote_triangle_fig()
    print("pc05 figures written")
