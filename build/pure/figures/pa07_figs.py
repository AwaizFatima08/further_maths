"""Figures for Unit A7: invariant lines of a reflection and of M = (2 1; 0 1)."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).parent
NAVY = "#1F3A5F"
RED = "#8A2C1E"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})


def axes(ax, lim):
    ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim); ax.set_aspect("equal")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_position("zero"); ax.spines["bottom"].set_position("zero")
    ax.set_xlabel("x", loc="right"); ax.set_ylabel("y", loc="top", rotation=0)


def reflection():
    fig, ax = plt.subplots(figsize=(5, 5))
    axes(ax, 4)
    xs = np.linspace(-4, 4, 50)
    ax.plot(xs, 2 * xs, color=NAVY, lw=2.2)
    ax.text(1.75, 3.6, "y = 2x", color=NAVY)
    M = np.array([[-3, 4], [4, 3]]) / 5
    for k in (-3, 0, 3):
        ax.plot(xs, -xs / 2 + k, "--", color="grey", lw=1)
    k = 3
    P = np.array([-1.0, 0.5 + k])
    Q = M @ P
    ax.plot(*P, "o", color=RED, ms=4); ax.plot(*Q, "o", color=RED, ms=4)
    ax.annotate("", xy=Q, xytext=P, arrowprops=dict(arrowstyle="->", color=RED, connectionstyle="arc3,rad=-0.3"))
    ax.text(P[0] - 0.5, P[1] + 0.25, "P", color=RED); ax.text(Q[0] + 0.15, Q[1] + 0.2, "P′", color=RED)
    ax.text(2.0, -2.6, "y = −½x + k", color="grey")
    fig.tight_layout()
    fig.savefig(HERE / "pa07_reflection.png", dpi=200, facecolor="white")


def shear_like():
    fig, ax = plt.subplots(figsize=(5, 4.2))
    axes(ax, 3.5)
    ax.set_ylim(-2.5, 2.5)
    xs = np.linspace(-3.5, 3.5, 50)
    ax.plot(xs, -xs, color=NAVY, lw=2.2); ax.text(-3.3, 2.2, "y = −x", color=NAVY)
    M = np.array([[2, 1], [0, 1]])
    for k in (-2, -1, 1, 2):
        ax.plot(xs, 0 * xs + k, "--", color="grey", lw=1)
        for x0 in (-k + 0.6, -k - 0.6):
            P = np.array([x0, k]); Q = M @ P
            if abs(Q[0]) < 3.4:
                ax.annotate("", xy=Q, xytext=P, arrowprops=dict(arrowstyle="->", color=RED, lw=1.1))
        ax.plot(-k, k, "o", color=NAVY, ms=4)
    ax.text(2.3, 1.1, "y = 1", color="grey"); ax.text(2.3, 2.1, "y = 2", color="grey")
    fig.tight_layout()
    fig.savefig(HERE / "pa07_lines.png", dpi=200, facecolor="white")


if __name__ == "__main__":
    reflection()
    shear_like()
