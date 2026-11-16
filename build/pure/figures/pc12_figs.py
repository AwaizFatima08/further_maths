"""Figures for Unit C12 (surfaces and partial differentiation). Writes pc12_*.png into this folder."""
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


def save(fig, name):
    fig.savefig(HERE / f"pc12_{name}.png", dpi=200, facecolor="white", bbox_inches="tight")
    plt.close(fig)


def clean3d(ax, xl="x", yl="y", zl="z"):
    ax.set_xlabel(xl, labelpad=-6)
    ax.set_ylabel(yl, labelpad=-6)
    ax.set_zlabel(zl, labelpad=-6)
    ax.tick_params(labelsize=7, pad=-2)
    ax.xaxis.set_major_locator(plt.MaxNLocator(4))
    ax.yaxis.set_major_locator(plt.MaxNLocator(4))
    ax.zaxis.set_major_locator(plt.MaxNLocator(4))
    for a in (ax.xaxis, ax.yaxis, ax.zaxis):
        a.pane.set_facecolor("white")
        a.pane.set_edgecolor("#BBBBBB")
    ax.grid(False)


def contour_axes(ax, lim):
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y", rotation=0)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


def paraboloid():
    fig = plt.figure(figsize=(8, 3.6))
    ax = fig.add_subplot(1, 2, 1, projection="3d", computed_zorder=False)
    r, t = np.meshgrid(np.linspace(0, 2, 30), np.linspace(0, 2 * np.pi, 60))
    x, y = r * np.cos(t), r * np.sin(t)
    ax.plot_surface(x, y, x**2 + y**2, color="#C9DCEB", edgecolor="#8FAAC4", lw=0.2, alpha=0.85)
    for k in (1, 2, 3):
        tt = np.linspace(0, 2 * np.pi, 100)
        ax.plot(np.sqrt(k) * np.cos(tt), np.sqrt(k) * np.sin(tt), k, color=RED, lw=1.4, zorder=5)
    xs = np.linspace(-2, 2, 50)
    ax.plot(xs, 0 * xs, xs**2, color=NAVY, lw=1.8, zorder=5)
    ax.view_init(22, -55)
    clean3d(ax)
    ax2 = fig.add_subplot(1, 2, 2)
    contour_axes(ax2, 2.2)
    for k in (1, 2, 3, 4):
        tt = np.linspace(0, 2 * np.pi, 200)
        ax2.plot(np.sqrt(k) * np.cos(tt), np.sqrt(k) * np.sin(tt), color=RED, lw=1.2)
        ax2.text(np.sqrt(k) * 0.72, np.sqrt(k) * 0.72, f"z = {k}", fontsize=8, color=RED)
    fig.tight_layout()
    save(fig, "paraboloid")


def saddle():
    fig = plt.figure(figsize=(8, 3.6))
    ax = fig.add_subplot(1, 2, 1, projection="3d", computed_zorder=False)
    x, y = np.meshgrid(np.linspace(-2, 2, 40), np.linspace(-2, 2, 40))
    ax.plot_surface(x, y, x**2 - y**2, color="#C9DCEB", edgecolor="#8FAAC4", lw=0.2, alpha=0.85)
    s = np.linspace(-2, 2, 60)
    ax.plot(s, 0 * s, s**2, color=NAVY, lw=2, label="section y = 0: z = x²", zorder=5)
    ax.plot(0 * s, s, -s**2, color=RED, lw=2, label="section x = 0: z = −y²", zorder=5)
    ax.scatter([0], [0], [0], color="black", s=18, zorder=6)
    ax.view_init(25, -60)
    clean3d(ax)
    ax.legend(loc="upper left", fontsize=7, frameon=False)
    ax2 = fig.add_subplot(1, 2, 2)
    contour_axes(ax2, 2.2)
    X, Y = np.meshgrid(np.linspace(-2.2, 2.2, 300), np.linspace(-2.2, 2.2, 300))
    cs = ax2.contour(X, Y, X**2 - Y**2, levels=[-3, -2, -1, 0, 1, 2, 3], colors=NAVY, linewidths=1, linestyles="solid")
    ax2.clabel(cs, fontsize=7, fmt="%d")
    ax2.plot(0, 0, "ko", ms=4)
    ax2.text(0.1, -0.35, "saddle", fontsize=8)
    fig.tight_layout()
    save(fig, "saddle")


def cubic_contours():
    fig, ax = plt.subplots(figsize=(6, 4.4))
    X, Y = np.meshgrid(np.linspace(-1.5, 2, 400), np.linspace(-1.5, 2, 400))
    Z = X**3 + Y**3 - 3 * X * Y
    cs = ax.contour(X, Y, Z, levels=[-0.9, -0.6, -0.3, 0, 0.5, 1, 2, 4], colors=NAVY, linewidths=0.9, linestyles="solid")
    ax.clabel(cs, fontsize=7, fmt="%g")
    ax.axhline(0, color="black", lw=0.6)
    ax.axvline(0, color="black", lw=0.6)
    ax.plot(0, 0, "o", color=RED, ms=5)
    ax.plot(1, 1, "o", color=RED, ms=5)
    ax.annotate("saddle (0, 0, 0)", (0, 0), (0.25, -0.75), color=RED, fontsize=9,
                arrowprops=dict(arrowstyle="->", color=RED, lw=0.8))
    ax.annotate("minimum (1, 1, −1)", (1, 1), (1.15, 1.6), color=RED, fontsize=9,
                arrowprops=dict(arrowstyle="->", color=RED, lw=0.8))
    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y", rotation=0)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    save(fig, "cubic_contours")


def tangent_plane():
    fig = plt.figure(figsize=(6, 4.4))
    ax = fig.add_subplot(projection="3d", computed_zorder=False)
    x, y = np.meshgrid(np.linspace(0, 2, 30), np.linspace(1, 3, 30))
    ax.plot_surface(x, y, x**2 * y + 3 * y**2, color="#C9DCEB", edgecolor="#8FAAC4", lw=0.2, alpha=0.5, zorder=1)
    xp, yp = np.meshgrid(np.linspace(0.4, 1.6, 6), np.linspace(1.4, 2.6, 6))
    ax.plot_surface(xp, yp, 4 * xp + 13 * yp - 16, color="#E9B8AE", alpha=0.85, edgecolor=RED, lw=0.3, zorder=3)
    ax.scatter([1], [2], [14], color="black", s=20, zorder=6)
    ax.text(1, 2, 18, "(1, 2, 14)", fontsize=9, zorder=7)
    ax.view_init(20, -125)
    clean3d(ax)
    save(fig, "tangent_plane")


def ellipsoid_normal():
    fig = plt.figure(figsize=(6, 4.6))
    ax = fig.add_subplot(projection="3d", computed_zorder=False)
    u, v = np.meshgrid(np.linspace(0, 2 * np.pi, 60), np.linspace(0, np.pi, 30))
    a, b, c = 3, np.sqrt(4.5), np.sqrt(3)
    ax.plot_surface(a * np.cos(u) * np.sin(v), b * np.sin(u) * np.sin(v), c * np.cos(v),
                    color="#C9DCEB", edgecolor="#8FAAC4", lw=0.15, alpha=0.55, zorder=1)
    t = np.linspace(0, 0.9, 20)
    ax.plot(2 + 2 * t, 1 + 2 * t, 1 + 3 * t, color=RED, lw=2.2, zorder=5)
    ax.scatter([2], [1], [1], color="black", s=20, zorder=6)
    ax.text(2.2, 0.6, 0.2, "(2, 1, 1)", fontsize=9, zorder=7)
    ax.text(2.6, 2.6, 4.2, "normal line", color=RED, fontsize=9, zorder=7)
    ax.set_box_aspect((a, b, c))
    ax.view_init(18, -40)
    clean3d(ax)
    save(fig, "ellipsoid_normal")


if __name__ == "__main__":
    paraboloid()
    saddle()
    cubic_contours()
    tangent_plane()
    ellipsoid_normal()
    print("pc12 figures written")
