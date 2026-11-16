"""Figures for Unit B6 (further integration techniques). Writes pb06_*.png into this folder."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Arc, Polygon, Wedge  # noqa: E402

HERE = Path(__file__).resolve().parent
NAVY = "#1F3A5F"
RED = "#8A2C1E"
GREY = "#777777"
FILL = "#C9DCEB"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})


def save(fig, name):
    fig.savefig(HERE / f"pb06_{name}.png", dpi=200, facecolor="white", bbox_inches="tight")
    plt.close(fig)


def triangle(ax, A, B, C, labels, angle_label):
    """Right angle at B; angle theta at A. labels = (AB, BC, AC)."""
    ax.add_patch(Polygon([A, B, C], closed=True, fill=False, ec=NAVY, lw=2))
    s = 0.25
    ax.plot([B[0] - s, B[0] - s, B[0]], [B[1], B[1] + s, B[1] + s], color=NAVY, lw=1)
    ax.add_patch(Arc(A, 1.0, 1.0, theta1=0, theta2=np.degrees(np.arctan2(C[1] - A[1], C[0] - A[0])), color=RED, lw=1.2))
    ax.text(A[0] + 0.62, A[1] + 0.12, angle_label, color=RED)
    ab, bc, ac = labels
    ax.text((A[0] + B[0]) / 2, A[1] - 0.3, ab, ha="center", va="top")
    ax.text(B[0] + 0.15, (B[1] + C[1]) / 2, bc, ha="left", va="center")
    ax.text((A[0] + C[0]) / 2 - 0.25, (A[1] + C[1]) / 2 + 0.2, ac, ha="right", va="bottom")


def triangles():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.5, 3.2))
    triangle(ax1, (0, 0), (3, 0), (3, 2), ("√(a² − x²)", "x", "a"), "θ")
    ax1.set_title("x = a sin θ", fontsize=11, color=NAVY)
    triangle(ax2, (0, 0), (3, 0), (3, 2), ("a", "x", "√(a² + x²)"), "θ")
    ax2.set_title("x = a tan θ", fontsize=11, color=NAVY)
    for ax in (ax1, ax2):
        ax.set_xlim(-1.6, 4.3), ax.set_ylim(-0.8, 2.6)
        ax.set_aspect("equal"), ax.axis("off")
    save(fig, "triangles")


def circle():
    fig, ax = plt.subplots(figsize=(5, 4))
    xs = np.linspace(-2, 2, 400)
    ax.plot(xs, np.sqrt(4 - xs**2), color=NAVY, lw=2)
    xr = np.linspace(0, 1, 100)
    ax.fill_between(xr, 0, np.sqrt(4 - xr**2), color=FILL)
    ax.add_patch(Wedge((0, 0), 2, 60, 90, fc="#9DBBD6", ec=NAVY, lw=0.8))
    ax.add_patch(Polygon([(0, 0), (1, 0), (1, np.sqrt(3))], closed=True, fc="#E3D2B5", ec=NAVY, lw=0.8))
    ax.plot([1, 1], [0, np.sqrt(3)], color=NAVY, lw=1)
    ax.text(0.25, 1.35, "sector\nπ/3", fontsize=9, ha="center")
    ax.text(0.68, 0.45, "triangle\n√3/2", fontsize=9, ha="center")
    ax.text(1.05, np.sqrt(3) + 0.05, "(1, √3)", fontsize=9)
    ax.text(-1.9, 1.3, "y = √(4 − x²)", color=NAVY)
    ax.spines["left"].set_position("zero"), ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_visible(False), ax.spines["top"].set_visible(False)
    ax.set_xlim(-2.3, 2.4), ax.set_ylim(-0.3, 2.4), ax.set_aspect("equal")
    ax.set_xticks([-2, -1, 1, 2]), ax.set_yticks([1, 2])
    ax.text(2.4, 0.05, "x", ha="right", va="bottom"), ax.text(0.05, 2.4, "y", va="top")
    save(fig, "circle")


if __name__ == "__main__":
    triangles(), circle()
    print("pb06 figures written")
