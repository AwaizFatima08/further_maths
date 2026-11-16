"""Figures for Unit A11: arrangements of three planes (3-D sketches) and end-on views of a sheaf and a prism."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).parent
NAVY = "#1F3A5F"
COLS = ["#1F3A5F", "#8A2C1E", "#4F8A5B"]
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})


def patch(ax, n, d, col, half=(1.3, 1.0), centre=None, alpha=0.35):
    """Draw a square patch of the plane n.r = d."""
    n = np.asarray(n, float); n = n / np.linalg.norm(n); d = d / np.linalg.norm(np.asarray(n, float))
    p0 = n * d if centre is None else np.asarray(centre, float)
    helper = np.array([0, 0, 1.0]) if abs(n[2]) < 0.9 else np.array([1.0, 0, 0])
    u = np.cross(n, helper); u /= np.linalg.norm(u)
    v = np.cross(n, u)
    s, t = np.meshgrid(np.linspace(-half[0], half[0], 2), np.linspace(-half[1], half[1], 2))
    P = p0[:, None, None] + u[:, None, None] * s + v[:, None, None] * t
    ax.plot_surface(P[0], P[1], P[2], color=col, alpha=alpha, edgecolor=col, linewidth=0.6, shade=False)


def frame(ax, label):
    ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.3, 1.3); ax.set_zlim(-1.1, 1.1)
    ax.set_box_aspect((1, 1, 0.85))
    ax.set_xticks([]); ax.set_yticks([]); ax.set_zticks([])
    ax.xaxis.pane.fill = ax.yaxis.pane.fill = ax.zaxis.pane.fill = False
    ax.view_init(elev=22, azim=-55)
    ax.text2D(0.02, 0.95, label, transform=ax.transAxes, fontsize=11, fontweight="bold")


def planes():
    fig = plt.figure(figsize=(9, 6))
    # (a) single point
    ax = fig.add_subplot(2, 3, 1, projection="3d"); frame(ax, "(a)")
    patch(ax, (1, 0, 0.25), 0, COLS[0]); patch(ax, (0, 1, 0.2), 0, COLS[1]); patch(ax, (0.15, 0.1, 1), 0, COLS[2])
    ax.scatter([0], [0], [0], color="black", s=18)
    # (b) sheaf: three planes containing the z-axis
    ax = fig.add_subplot(2, 3, 2, projection="3d"); frame(ax, "(b)")
    for i, phi in enumerate(np.radians([0, 60, 120])):
        patch(ax, (np.cos(phi), np.sin(phi), 0), 0, COLS[i], half=(1.2, 1.0))
    ax.plot([0, 0], [0, 0], [-1, 1], color="black", lw=2)
    # (c) prism: three vertical planes forming a triangle
    ax = fig.add_subplot(2, 3, 3, projection="3d"); frame(ax, "(c)")
    ax.view_init(elev=40, azim=-90)
    ns = [np.array([np.cos(p), np.sin(p)]) for p in np.radians([90, 210, 330])]
    for i, n in enumerate(ns):
        patch(ax, (n[0], n[1], 0), 0.5, COLS[i], half=(1.25, 0.9))
    for i in range(3):  # the three parallel lines of intersection
        v = np.linalg.solve(np.array([ns[i], ns[(i + 1) % 3]]), [0.5, 0.5])
        ax.plot([v[0], v[0]], [v[1], v[1]], [-0.9, 0.9], color="black", lw=1.6)
    # (d) two parallel planes cut by a third
    ax = fig.add_subplot(2, 3, 4, projection="3d"); frame(ax, "(d)")
    patch(ax, (0, 0, 1), -0.6, COLS[0]); patch(ax, (0, 0, 1), 0.6, COLS[0]); patch(ax, (1, 0.3, 0), 0, COLS[1], half=(1.2, 1.0))
    # (e) three parallel planes
    ax = fig.add_subplot(2, 3, 5, projection="3d"); frame(ax, "(e)")
    for i, d in enumerate((-0.8, 0, 0.8)):
        patch(ax, (0, 0, 1), d, COLS[i])
    # (f) two coincident planes and a third cutting them
    ax = fig.add_subplot(2, 3, 6, projection="3d"); frame(ax, "(f)")
    patch(ax, (0, 0, 1), 0, COLS[0], alpha=0.6); patch(ax, (1, 0.3, 0), 0, COLS[1], half=(1.2, 1.0))
    ax.plot([0.3 * 1.2 / 1.044, -0.3 * 1.2 / 1.044], [-1.2 / 1.044, 1.2 / 1.044], [0, 0], color="black", lw=2)
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1, wspace=0, hspace=0.02)
    fig.savefig(HERE / "pa11_planes.png", dpi=200, facecolor="white")


def endon():
    fig, axs = plt.subplots(1, 2, figsize=(7, 3.4))
    xs = np.linspace(-2, 2, 50)
    for ax, lab in zip(axs, ("(a)", "(b)")):
        ax.set_xlim(-2, 2); ax.set_ylim(-1.6, 2.0); ax.set_aspect("equal"); ax.axis("off")
        ax.text(-1.95, 1.8, lab, fontsize=11, fontweight="bold")
    for i, phi in enumerate(np.radians([0, 60, 120])):
        axs[0].plot(xs * np.cos(phi), xs * np.sin(phi), color=COLS[i], lw=2)
    axs[0].plot(0, 0, "o", color="black", ms=5); axs[0].text(0.12, -0.3, "common line", fontsize=9)
    for i, phi in enumerate(np.radians([90, 210, 330])):
        n = np.array([np.cos(phi), np.sin(phi)]); u = np.array([-n[1], n[0]])
        pts = 0.6 * n[:, None] + u[:, None] * xs
        axs[1].plot(pts[0], pts[1], color=COLS[i], lw=2)
    axs[1].text(-0.25, -0.05, "no common\n point", fontsize=9)
    fig.tight_layout()
    fig.savefig(HERE / "pa11_endon.png", dpi=200, facecolor="white")


if __name__ == "__main__":
    planes()
    endon()
