"""Figures for Unit C4 (parabola and rectangular hyperbola). Writes pc04_*.png into this folder."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

HERE = Path(__file__).resolve().parent
NAVY = "#1F3A5F"
RED = "#8A2C1E"
GREY = "#777777"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})


def axes_through_origin(ax, xlim, ylim, xlabel="x", ylabel="y"):
    ax.set_xlim(*xlim), ax.set_ylim(*ylim)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False, ms=4)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False, ms=4)
    ax.text(1.0, 0.02, xlabel, transform=ax.get_yaxis_transform(), ha="right", va="bottom")
    ax.text(0.02, 1.0, ylabel, transform=ax.get_xaxis_transform(), ha="left", va="top")
    ax.set_xticks([]), ax.set_yticks([])


def save(fig, name):
    fig.savefig(HERE / f"pc04_{name}.png", dpi=200, facecolor="white", bbox_inches="tight")
    plt.close(fig)


def four_conics():
    fig, axs = plt.subplots(2, 2, figsize=(7.5, 6))
    t = np.linspace(-2.2, 2.2, 400)
    # parabola y^2 = 4ax, a = 1
    ax = axs[0, 0]
    axes_through_origin(ax, (-1.5, 5), (-4.5, 4.5))
    ax.plot(t ** 2, 2 * t, color=NAVY, lw=2)
    ax.set_title("parabola  y² = 4ax", fontsize=10)
    ax.text(-0.15, -0.5, "O", ha="right")
    # ellipse
    ax = axs[0, 1]
    axes_through_origin(ax, (-4.2, 4.2), (-3, 3.3))
    th = np.linspace(0, 2 * np.pi, 400)
    ax.plot(3 * np.cos(th), 2 * np.sin(th), color=NAVY, lw=2)
    for x, y, s, ha, va in [(3, 0, "(a, 0)", "left", "bottom"), (-3, 0, "(−a, 0)", "right", "bottom"),
                            (0, 2, "(0, b)", "left", "bottom"), (0, -2, "(0, −b)", "left", "top")]:
        ax.plot(x, y, "ko", ms=3)
        ax.text(x + (0.1 if ha == "left" else -0.1), y + (0.08 if va == "bottom" else -0.08), s, ha=ha, va=va, fontsize=9)
    ax.set_title("ellipse  x²/a² + y²/b² = 1", fontsize=10)
    # hyperbola
    ax = axs[1, 0]
    axes_through_origin(ax, (-6, 6), (-4.5, 4.5))
    u = np.linspace(-2.1, 2.1, 300)
    for sgn in (1, -1):
        ax.plot(sgn * 2 * np.cosh(u), 1.5 * np.sinh(u), color=NAVY, lw=2)
    xs = np.array([-6, 6])
    ax.plot(xs, 0.75 * xs, color=GREY, ls="--", lw=1)
    ax.plot(xs, -0.75 * xs, color=GREY, ls="--", lw=1)
    ax.text(3.2, 4.1, "y = (b/a)x", ha="right", fontsize=9, color=GREY)
    ax.text(3.0, -4.4, "y = −(b/a)x", ha="right", fontsize=9, color=GREY)
    for x, s, ha in [(2, "(a, 0)", "left"), (-2, "(−a, 0)", "right")]:
        ax.plot(x, 0, "ko", ms=3)
        ax.text(x + (0.15 if ha == "left" else -0.15), 0.15, s, ha=ha, fontsize=9)
    ax.set_title("hyperbola  x²/a² − y²/b² = 1", fontsize=10)
    # rectangular hyperbola
    ax = axs[1, 1]
    axes_through_origin(ax, (-5, 5), (-5, 5))
    x = np.linspace(0.2, 5, 300)
    ax.plot(x, 1 / x * 2, color=NAVY, lw=2)
    ax.plot(-x, -2 / x, color=NAVY, lw=2)
    ax.plot(np.sqrt(2), np.sqrt(2), "ko", ms=3)
    ax.text(1.6, 1.6, "(c, c)", fontsize=9)
    ax.plot(-np.sqrt(2), -np.sqrt(2), "ko", ms=3)
    ax.text(-1.3, -2.1, "(−c, −c)", fontsize=9, ha="right")
    ax.set_title("rectangular hyperbola  xy = c²", fontsize=10)
    fig.tight_layout()
    save(fig, "four_conics")


def parabola_focus():
    fig, ax = plt.subplots(figsize=(6, 4))
    axes_through_origin(ax, (-2.5, 6.5), (-5.5, 5.5))
    t = np.linspace(-2.4, 2.4, 300)
    ax.plot(t ** 2, 2 * t, color=NAVY, lw=2)
    ax.axvline(-1, color=RED, lw=1.4, ls="--")
    ax.text(-1.1, 5.0, "directrix\nx = −a", color=RED, ha="right", fontsize=9)
    tp = 1.5
    P = np.array([tp ** 2, 2 * tp])
    S = np.array([1.0, 0])
    M = np.array([-1, P[1]])
    ax.plot(*S, "o", color=RED, ms=5)
    ax.text(1.1, -0.5, "S(a, 0)", color=RED)
    ax.plot(*P, "ko", ms=4)
    ax.text(P[0] + 0.15, P[1] + 0.15, "P(at², 2at)")
    ax.plot(*M, "ko", ms=4)
    ax.text(M[0] - 0.15, M[1] + 0.2, "M", ha="right")
    ax.plot(*np.array([S, P]).T, color=GREY, lw=1.3)
    ax.plot(*np.array([M, P]).T, color=GREY, lw=1.3)
    ax.text(1.0, 1.9, "SP", color=GREY)
    ax.text(0.5, 3.25, "PM", color=GREY)
    ax.text(-0.15, -0.5, "O", ha="right")
    save(fig, "parabola_focus")


def parabola_tangent():
    fig, ax = plt.subplots(figsize=(6, 4.2))
    axes_through_origin(ax, (-4, 22), (-15, 10))
    t = np.linspace(-3.4, 2.2, 300)
    ax.plot(2 * t ** 2, 4 * t, color=NAVY, lw=2)
    xs = np.linspace(-4, 8, 2)
    ax.plot(xs, xs + 2, color=RED, lw=1.4)
    xs2 = np.linspace(-3, 21, 2)
    ax.plot(xs2, 6 - xs2, color=GREY, lw=1.4, ls="--")
    for X, s, off in [((18, -12), "Q(18, −12)", (0.4, 0.4)), ((2, 0), "S(2, 0)", (0.3, -1.2))]:
        ax.plot(*X, "ko", ms=4)
        ax.text(X[0] + off[0], X[1] + off[1], s)
    ax.plot(2, 4, "ko", ms=4)
    ax.annotate("P(2, 4)", xy=(2, 4), xytext=(6, 1.5), arrowprops=dict(arrowstyle="-", color="black", lw=0.7))
    ax.text(-3.8, -4.0, "tangent\ny = x + 2", color=RED)
    ax.text(10.5, -2.0, "normal x + y = 6", color=GREY)
    ax.text(19, 8.5, "y² = 8x", color=NAVY)
    save(fig, "parabola_tangent")


def rect_hyperbola_tangent():
    fig, ax = plt.subplots(figsize=(6, 4.2))
    axes_through_origin(ax, (-12, 20), (-36, 14))
    x = np.linspace(0.5, 20, 300)
    ax.plot(x, 16 / x, color=NAVY, lw=2)
    x2 = np.linspace(-12, -0.45, 300)
    ax.plot(x2, 16 / x2, color=NAVY, lw=2)
    xs = np.linspace(-4, 20, 2)
    ax.plot(xs, (16 - xs) / 4, color=RED, lw=1.4)
    xs2 = np.linspace(-1.5, 11.5, 2)
    ax.plot(xs2, 4 * xs2 - 30, color=GREY, lw=1.4, ls="--")
    for X, s, off in [((8, 2), "P(8, 2)", (0.4, 1.0)), ((-0.5, -32), "Q(−½, −32)", (-0.6, 0.0))]:
        ax.plot(*X, "ko", ms=4)
        ax.text(X[0] + off[0], X[1] + off[1], s, ha="left" if off[0] > 0 else "right")
    ax.text(12, 2.0, "tangent x + 4y = 16", color=RED, fontsize=9)
    ax.text(5.3, -13, "normal 4x − y = 30", color=GREY, fontsize=9)
    ax.text(14, 9, "xy = 16", color=NAVY)
    save(fig, "rect_hyperbola_tangent")


def focal_chord():
    fig, ax = plt.subplots(figsize=(6, 4.2))
    axes_through_origin(ax, (-2.5, 6.5), (-5, 5.5))
    t = np.linspace(-2.3, 2.4, 300)
    ax.plot(t ** 2, 2 * t, color=NAVY, lw=2)
    ax.axvline(-1, color=RED, lw=1.2, ls="--")
    ax.text(-1.1, 4.6, "x = −a", color=RED, ha="right", fontsize=9)
    p, q = 2.0, -0.5
    P, Q = np.array([p ** 2, 2 * p]), np.array([q ** 2, 2 * q])
    Rr = np.array([p * q, p + q])
    ax.plot(*np.array([P, Q]).T, color=GREY, lw=1.3)
    for X, s, off in [(P, "P(ap², 2ap)", (0.1, -0.75)), ((1, 0), "S", (0.1, 0.25))]:
        ax.plot(*X, "ko", ms=4)
        ax.text(X[0] + off[0], X[1] + off[1], s, fontsize=9)
    for X, s, txt in [(Q, "Q(aq², 2aq)", (2.6, -2.6)), (Rr, "R(apq, a(p + q))", (-0.8, 2.8))]:
        ax.plot(*X, "ko", ms=4)
        ax.annotate(s, xy=X, xytext=txt, fontsize=9, arrowprops=dict(arrowstyle="-", color="black", lw=0.7))
    for X, m in [(P, 1 / p), (Q, 1 / q)]:
        xs = np.array([-2.4, 6.2])
        ax.plot(xs, X[1] + m * (xs - X[0]), color=RED, lw=1.1)
    ax.set_ylim(-5, 5.5)
    save(fig, "focal_chord")


if __name__ == "__main__":
    four_conics()
    parabola_focus()
    parabola_tangent()
    rect_hyperbola_tangent()
    focal_chord()
    print("pc04 figures written")
