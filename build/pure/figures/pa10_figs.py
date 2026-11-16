"""Figures for Unit A10 (vector product and scalar triple product). Writes pa10_*.png into this folder."""
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
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})


def blank3d(fig, pos=111, lim=(-0.5, 3), elev=20, azim=-60, zoom=1.2):
    ax = fig.add_subplot(pos, projection="3d")
    ax.set_axis_off()
    ax.computed_zorder = False
    ax.view_init(elev=elev, azim=azim)
    ax.set_xlim(*lim), ax.set_ylim(*lim), ax.set_zlim(*lim)
    ax.set_box_aspect((1, 1, 1), zoom=zoom)
    return ax


def arrow(ax, p, q, color=NAVY, lw=2, head=0.1):
    p, q = np.array(p, float), np.array(q, float)
    ax.quiver(*p, *(q - p), color=color, lw=lw, arrow_length_ratio=head)


def save(fig, name):
    fig.savefig(HERE / f"pa10_{name}.png", dpi=200, facecolor="white", bbox_inches="tight")
    plt.close(fig)


def cross_fig():
    fig = plt.figure(figsize=(6, 4.2))
    ax = blank3d(fig, lim=(-0.3, 3), elev=18, azim=-58)
    a = np.array([2.4, 0.3, 0.0])
    b = np.array([0.8, 2.2, 0.0])
    o = np.zeros(3)
    ax.add_collection3d(Poly3DCollection([[o, a, a + b, b]], facecolor=FILL, edgecolor=NAVY, alpha=0.7, zorder=1))
    arrow(ax, o, a)
    arrow(ax, o, b)
    ax.text(*(a + np.array([0.1, -0.1, -0.2])), "a", color=NAVY, weight="bold")
    ax.text(*(b + np.array([-0.2, 0.1, 0.1])), "b", color=NAVY, weight="bold")
    c = np.cross(a, b)
    c = c / np.linalg.norm(c) * 2.4
    arrow(ax, o, c, color=RED, head=0.08)
    ax.text(*(c + np.array([0.1, 0, 0.1])), "a × b", color=RED, weight="bold")
    ax.text(*(-c * 0.0 + np.array([-0.1, 0.0, -0.35])), "O")
    t = np.linspace(0, 1, 30)
    ang = np.arccos(np.dot(a, b) / np.linalg.norm(a) / np.linalg.norm(b))
    ua = a / np.linalg.norm(a)
    w = b - np.dot(b, ua) * ua
    w = w / np.linalg.norm(w)
    arc = np.array([0.55 * (np.cos(s * ang) * ua + np.sin(s * ang) * w) for s in t])
    ax.plot(*arc.T, color="black", lw=1)
    ax.text(*(arc[15] * 1.5), "θ", fontsize=12)
    mid = (a + b) / 2
    ax.text(*(mid + np.array([0.2, 0.2, 0])), "area |a × b|", color=NAVY, fontsize=10)
    save(fig, "cross")


def volumes_fig():
    fig = plt.figure(figsize=(9, 4))
    a = np.array([2.2, 0.2, 0.0])
    b = np.array([0.6, 2.0, 0.0])
    c = np.array([0.7, 0.6, 1.8])
    o = np.zeros(3)
    ax = blank3d(fig, 121, lim=(0, 3.6), elev=18, azim=-62, zoom=1.0)
    faces = [[o, a, a + b, b], [c, a + c, a + b + c, b + c], [o, a, a + c, c], [b, a + b, a + b + c, b + c],
             [o, b, b + c, c], [a, a + b, a + b + c, a + c]]
    ax.add_collection3d(Poly3DCollection(faces, facecolor=FILL, edgecolor=NAVY, alpha=0.35, lw=1))
    for v, name in [(a, "a"), (b, "b"), (c, "c")]:
        arrow(ax, o, v, color=RED, lw=2.2, head=0.12)
        ax.text(*(v * 1.12), name, color=RED, weight="bold")
    ax.text2D(0.5, -0.06, "parallelepiped: V = |a·(b × c)|", transform=ax.transAxes, ha="center", fontsize=11)
    ax2 = blank3d(fig, 122, lim=(0, 3.6), elev=18, azim=-62, zoom=1.0)
    A, B, C, D = np.array([0.2, 0.2, 0]), np.array([2.6, 0.5, 0]), np.array([1.0, 2.5, 0]), np.array([1.3, 1.0, 2.2])
    ax2.add_collection3d(Poly3DCollection([[A, B, C], [A, B, D], [B, C, D], [A, C, D]], facecolor=FILL,
                                          edgecolor=NAVY, alpha=0.35, lw=1))
    for P, nm, off in [(A, "A", (-0.25, -0.1, -0.15)), (B, "B", (0.15, 0, 0.1)), (C, "C", (0.1, 0.1, 0)),
                       (D, "D", (0, 0, 0.15))]:
        ax2.scatter(*P, color="black", s=12)
        ax2.text(*(P + np.array(off)), nm)
    for P in (B, C, D):
        arrow(ax2, A, P, color=RED, lw=1.8, head=0.1)
    ax2.text2D(0.5, -0.06, "tetrahedron: V = ⅙|AB·(AC × AD)|", transform=ax2.transAxes, ha="center", fontsize=11)
    save(fig, "volumes")


if __name__ == "__main__":
    cross_fig()
    volumes_fig()
    print("pa10 figures written")
