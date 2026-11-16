"""Figures for Unit A9 (lines and planes in three dimensions). Writes pa09_*.png into this folder."""
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
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})


def axes3d(fig, pos=111, lim=(-1, 5), elev=20, azim=-60, labels=True):
    ax = fig.add_subplot(pos, projection="3d")
    ax.set_axis_off()
    ax.computed_zorder = False
    ax.view_init(elev=elev, azim=azim)
    lo, hi = lim
    for v, name in [((1, 0, 0), "x"), ((0, 1, 0), "y"), ((0, 0, 1), "z")]:
        v = np.array(v)
        ax.plot(*zip(lo * 0 * v, hi * v), color=GREY, lw=0.9)
        if labels:
            ax.text(*(hi * 1.05 * v), name, color=GREY)
    ax.set_xlim(lo, hi), ax.set_ylim(lo, hi), ax.set_zlim(lo, hi)
    ax.set_box_aspect((1, 1, 1), zoom=1.15)
    return ax


def arrow(ax, p, q, color=NAVY, lw=1.8, head=0.08):
    p, q = np.array(p, float), np.array(q, float)
    ax.quiver(*p, *(q - p), color=color, lw=lw, arrow_length_ratio=head)


def save(fig, name):
    fig.savefig(HERE / f"pa09_{name}.png", dpi=200, facecolor="white", bbox_inches="tight")
    plt.close(fig)


def line_fig():
    fig = plt.figure(figsize=(6, 4.2))
    ax = axes3d(fig, lim=(0, 5), elev=18, azim=-60)
    a = np.array([3.2, 0.6, 0.6])
    b = np.array([-0.6, 1.2, 0.9])
    pts = np.array([a + t * b for t in np.linspace(-0.8, 3.6, 2)])
    ax.plot(*pts.T, color=NAVY, lw=2)
    arrow(ax, (0, 0, 0), a, color=GREY, lw=1.3)
    ax.text(*(a / 2 + np.array([0, -0.3, -0.45])), "a", color=GREY, weight="bold")
    arrow(ax, a, a + b, color=RED, lw=2.2, head=0.2)
    ax.text(*(a + b / 2 + np.array([0.25, 0, -0.1])), "b", color=RED, weight="bold")
    r = a + 3.0 * b
    arrow(ax, (0, 0, 0), r, color=NAVY, lw=1.3)
    ax.text(*(r / 2 + np.array([-0.9, 0, 0.3])), "r = a + λb", color=NAVY, weight="bold")
    ax.scatter(*a, color="black", s=15)
    ax.text(*(a + np.array([0.2, 0, -0.35])), "A", color="black")
    ax.scatter(*r, color="black", s=15)
    ax.text(*(r + np.array([0.15, 0, 0.15])), "R", color="black")
    ax.text(0, 0, -0.45, "O")
    save(fig, "line")


def plane_fig():
    fig = plt.figure(figsize=(6, 4.2))
    ax = axes3d(fig, lim=(0, 5), elev=22, azim=-50, labels=False)
    c = np.array([2.5, 2.5, 1.5])
    u = np.array([1.0, 0.0, -0.25])
    v = np.array([0.0, 1.0, -0.15])
    corners = [c + s * 2.2 * u + t * 2.2 * v for s, t in [(-1, -1), (1, -1), (1, 1), (-1, 1)]]
    ax.add_collection3d(Poly3DCollection([corners], facecolor="#cfdde8", edgecolor=NAVY, alpha=0.6))
    n = np.cross(u, v)
    n = n / np.linalg.norm(n) * 1.8
    a = c + np.array([-1.0, -0.8, 0]) @ np.array([u, v, [0, 0, 0]])
    arrow(ax, a, a + n, color=RED, lw=2.2, head=0.15)
    ax.text(*(a + n + np.array([0, 0, 0.15])), "n", color=RED, weight="bold")
    r = c + 1.3 * u + 1.0 * v
    arrow(ax, a, r, color=NAVY, lw=2, head=0.12)
    ax.text(*((a + r) / 2 + np.array([0.3, -0.6, 0.35])), "r − a", color=NAVY, weight="bold")
    ax.scatter(*a, color="black", s=15)
    ax.text(*(a + np.array([-0.35, -0.2, -0.3])), "A", color="black")
    ax.scatter(*r, color="black", s=15)
    ax.text(*(r + np.array([0.1, 0.1, 0.15])), "R", color="black")
    ax.text(*(c + 1.7 * u - 1.6 * v + np.array([0, 0, 0.1])), "Π", color=NAVY, fontsize=14)
    save(fig, "plane")


def line_plane_angle_fig():
    fig = plt.figure(figsize=(6, 4.2))
    ax = axes3d(fig, lim=(-3, 3), elev=14, azim=-62, labels=False)
    corners = [(-3, -3, 0), (3, -3, 0), (3, 3, 0), (-3, 3, 0)]
    ax.add_collection3d(Poly3DCollection([corners], facecolor="#cfdde8", edgecolor=NAVY, alpha=0.55))
    d = np.array([1.6, 0.9, 1.4])
    ax.plot(*np.array([-1.0 * d, 1.5 * d]).T, color=NAVY, lw=2)
    proj = np.array([d[0], d[1], 0])
    ax.plot(*np.array([(0, 0, 0), 1.5 * proj]).T, color=GREY, lw=1.4, ls="--")
    ax.plot(*np.array([1.5 * d, 1.5 * proj]).T, color=GREY, lw=1, ls=":")
    arrow(ax, (0, 0, 0), (0, 0, 2.6), color=RED, lw=2, head=0.12)
    ax.text(0.1, 0.1, 2.7, "n", color=RED, weight="bold")
    t = np.linspace(0, 1, 30)
    th = np.arctan2(d[2], np.linalg.norm(proj))
    arc = np.array([np.cos(s * th) * proj / np.linalg.norm(proj) * 0.9 + np.array([0, 0, np.sin(s * th) * 0.9]) for s in t])
    ax.plot(*arc.T, color="black", lw=1)
    ax.text(*(arc[15] + np.array([0.35, 0.1, -0.15])), "θ", fontsize=13)
    phi = np.pi / 2 - th
    unit_d = d / np.linalg.norm(d)
    arc2 = np.array([np.cos(s * phi) * np.array([0, 0, 1]) * 0.7 + np.sin(s * phi) *
                     (unit_d - np.dot(unit_d, [0, 0, 1]) * np.array([0, 0, 1])) /
                     np.linalg.norm(unit_d - np.dot(unit_d, [0, 0, 1]) * np.array([0, 0, 1])) * 0.7 for s in t])
    ax.plot(*arc2.T, color=RED, lw=1)
    ax.text(*(arc2[15] + np.array([-0.1, 0.0, 0.25])), "90° − θ", color=RED, fontsize=10)
    ax.text(*(1.5 * d + np.array([-0.4, 0, 0.25])), "b", color=NAVY, weight="bold")
    ax.text(2.2, -2.6, 0.05, "Π", color=NAVY, fontsize=14)
    save(fig, "line_plane_angle")


def three_cases_fig():
    fig = plt.figure(figsize=(9, 3.4))
    titles = ["intersecting", "parallel", "skew"]
    for k, title in enumerate(titles):
        ax = axes3d(fig, pos=131 + k, lim=(0, 4), elev=20, azim=-60, labels=False)
        if k == 0:
            p = np.array([2, 2, 2])
            for d in ([1, -0.4, 0.6], [-0.3, 1, 0.5]):
                d = np.array(d)
                ax.plot(*np.array([p - 1.6 * d, p + 1.6 * d]).T, color=NAVY, lw=2)
            ax.scatter(*p, color=RED, s=20)
        elif k == 1:
            d = np.array([1, 0.6, 0.5])
            for base in ([0.5, 0.5, 1.0], [0.5, 1.8, 2.4]):
                base = np.array(base)
                ax.plot(*np.array([base, base + 2.6 * d]).T, color=NAVY, lw=2)
        else:
            ax.plot([0.3, 3.7], [1, 1], [1, 1], color=NAVY, lw=2)
            ax.plot([2, 2], [0.2, 3.8], [2.6, 2.6], color=NAVY, lw=2)
            ax.plot([2, 2], [1, 1], [1, 2.6], color=RED, lw=1, ls="--")
        ax.text2D(0.5, 0.02, title, transform=ax.transAxes, ha="center", fontsize=12)
    save(fig, "three_cases")


if __name__ == "__main__":
    line_fig()
    plane_fig()
    line_plane_angle_fig()
    three_cases_fig()
    print("pa09 figures written")
