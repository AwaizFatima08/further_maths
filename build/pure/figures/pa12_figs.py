"""Figures for Unit A12 (distances and intersections in 3-D). Writes pa12_*.png into this folder."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from mpl_toolkits.mplot3d.art3d import Poly3DCollection  # noqa: E402

HERE = Path(__file__).resolve().parent
NAVY = "#1F3A5F"
RED = "#8A2C1E"
GREY = "#777777"
FILL = "#cfdde8"
FILL2 = "#e8d9cf"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})


def blank3d(fig, pos=111, lim=(-3, 3), elev=18, azim=-60, zoom=1.15):
    ax = fig.add_subplot(pos, projection="3d")
    ax.set_axis_off()
    ax.computed_zorder = False
    ax.view_init(elev=elev, azim=azim)
    ax.set_xlim(*lim), ax.set_ylim(*lim), ax.set_zlim(*lim)
    ax.set_box_aspect((1, 1, 1), zoom=zoom)
    return ax


def save(fig, name):
    fig.savefig(HERE / f"pa12_{name}.png", dpi=200, facecolor="white", bbox_inches="tight")
    plt.close(fig)


def right_angle(ax, corner, u, v, size=0.3, color="black"):
    u = np.array(u, float) / np.linalg.norm(u) * size
    v = np.array(v, float) / np.linalg.norm(v) * size
    c = np.array(corner, float)
    ax.plot(*np.array([c + u, c + u + v, c + v]).T, color=color, lw=0.9)


def point_plane_fig():
    fig = plt.figure(figsize=(6, 4.2))
    ax = blank3d(fig, lim=(-3, 3), elev=16, azim=-62)
    corners = [(-3, -3, -1), (3, -3, -1), (3, 3, -1), (-3, 3, -1)]
    ax.add_collection3d(Poly3DCollection([corners], facecolor=FILL, edgecolor=NAVY, alpha=0.6))
    P, N = np.array([0.3, 0.2, 2.2]), np.array([0.3, 0.2, -1])
    ax.plot(*np.array([P, N]).T, color=RED, lw=2)
    ax.plot(*np.array([N, N + (N - P) * 0.999]).T, color=RED, lw=1, ls="--")
    Pr = 2 * N - P
    for X, nm, off in [(P, "P", (0.15, 0, 0.1)), (N, "N", (0.2, 0.1, 0.1)), (Pr, "P′", (0.15, 0, -0.2))]:
        ax.scatter(*X, color="black", s=15)
        ax.text(*(X + np.array(off)), nm)
    A = np.array([-1.8, 1.2, -1])
    ax.scatter(*A, color="black", s=12)
    ax.text(*(A + np.array([-0.3, 0, 0.15])), "A")
    ax.plot(*np.array([A, P]).T, color=GREY, lw=1.2)
    ax.plot(*np.array([A, N]).T, color=GREY, lw=1.0, ls=":")
    right_angle(ax, N, P - N, A - N)
    ax.quiver(*(np.array([2.0, -2.0, -1])), 0, 0, 1.4, color=NAVY, lw=2, arrow_length_ratio=0.15)
    ax.text(2.1, -2.0, 0.5, "n", color=NAVY, weight="bold")
    ax.text(*((P + N) / 2 + np.array([0.2, 0, 0])), "d", color=RED, weight="bold")
    ax.text(2.4, 2.2, -0.95, "Π", color=NAVY, fontsize=14)
    save(fig, "point_plane")


def skew_fig():
    fig = plt.figure(figsize=(6, 4.2))
    ax = blank3d(fig, lim=(-3, 3), elev=20, azim=-55)
    P, Q = np.array([0, 0, -1.2]), np.array([0, 0, 1.4])
    b, d = np.array([1, 0.15, 0]), np.array([0.25, 1, 0])
    ax.plot(*np.array([P - 2.8 * b, P + 2.8 * b]).T, color=NAVY, lw=2.2)
    ax.plot(*np.array([Q - 2.8 * d, Q + 2.8 * d]).T, color=NAVY, lw=2.2)
    ax.plot(*np.array([P, Q]).T, color=RED, lw=2)
    for X, nm, off in [(P, "P", (0.15, -0.3, -0.35)), (Q, "Q", (0.15, 0, 0.2))]:
        ax.scatter(*X, color="black", s=15)
        ax.text(*(X + np.array(off)), nm)
    right_angle(ax, P, b, Q - P)
    right_angle(ax, Q, d, P - Q)
    ax.text(*(P + 1.0 * b + np.array([0, 0, -1.0])), "l₁: r = a + λb", color=NAVY)
    ax.text2D(0.62, 0.78, "l₂: r = c + μd", transform=ax.transAxes, color=NAVY)
    ax.text(0.25, 0.1, 0.0, "  b × d", color=RED)
    save(fig, "skew")


def two_planes_fig():
    fig = plt.figure(figsize=(6, 4.2))
    ax = blank3d(fig, lim=(-2.2, 2.2), elev=18, azim=-50, zoom=1.2)
    # plane 1: z = 0.5 y ; plane 2: z = -0.8 y (meet along the x-axis)
    s = 2.0
    p1 = [(-s, -s, -0.5 * s), (s, -s, -0.5 * s), (s, s, 0.5 * s), (-s, s, 0.5 * s)]
    p2 = [(-s, -s, 0.8 * s), (s, -s, 0.8 * s), (s, s, -0.8 * s), (-s, s, -0.8 * s)]
    ax.add_collection3d(Poly3DCollection([p1], facecolor=FILL, edgecolor=NAVY, alpha=0.55))
    ax.add_collection3d(Poly3DCollection([p2], facecolor=FILL2, edgecolor=RED, alpha=0.55))
    ax.plot([-s, s], [0, 0], [0, 0], color="black", lw=2.4)
    ax.text2D(0.55, 0.12, "line of intersection,\ndirection n₁ × n₂", transform=ax.transAxes, fontsize=10)
    ax.quiver(-1.2, 1.0, 0.5, 0, -0.45, 0.9, color=NAVY, lw=2, arrow_length_ratio=0.15)
    ax.text(-1.2, 0.2, 0.75, "n₁", color=NAVY, weight="bold")
    ax.quiver(-1.2, -1.0, 0.8, 0, 0.6, 0.75, color=RED, lw=2, arrow_length_ratio=0.15)
    ax.text(-1.2, -0.4, 1.65, "n₂", color=RED, weight="bold")
    ax.text(0.6 * s, s, 0.5 * s + 0.1, "Π₁", color=NAVY, fontsize=13)
    ax.text(-s, -s, 0.8 * s + 0.1, "Π₂", color=RED, fontsize=13)
    save(fig, "two_planes")


def point_line_fig():
    fig, ax = plt.subplots(figsize=(6, 3.2))
    ax.set_axis_off()
    ax.set_aspect("equal")
    ax.plot([-0.5, 7], [0, 0], color=NAVY, lw=2)
    A, F, P = np.array([0.5, 0]), np.array([4.0, 0]), np.array([4.0, 2.4])
    ax.annotate("", xy=(2.2, 0), xytext=A, arrowprops=dict(arrowstyle="-|>", color=RED, lw=2))
    ax.text(1.3, -0.4, "b", color=RED, weight="bold")
    ax.plot(*np.array([A, P]).T, color=GREY, lw=1.2)
    ax.plot(*np.array([F, P]).T, color=RED, lw=2)
    ax.plot([F[0] - 0.25, F[0] - 0.25, F[0]], [0, 0.25, 0.25], color="black", lw=0.9)
    for X, nm, off in [(A, "A", (-0.1, -0.45)), (F, "F", (0.05, -0.45)), (P, "P", (0.1, 0.1))]:
        ax.plot(*X, "ko", ms=4)
        ax.text(*(X + np.array(off)), nm)
    ax.text(4.15, 1.1, "d = |PF|", color=RED)
    ax.text(1.6, 1.4, "p − a", color=GREY)
    ax.text(6.3, 0.15, "l", color=NAVY, fontsize=13)
    ax.set_xlim(-0.6, 7.2), ax.set_ylim(-0.7, 2.8)
    save(fig, "point_line")


if __name__ == "__main__":
    point_plane_fig()
    skew_fig()
    two_planes_fig()
    point_line_fig()
    print("pa12 figures written")
