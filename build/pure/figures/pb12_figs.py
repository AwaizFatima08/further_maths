"""Figures for Unit B12: eigenvector directions of (4 1; 2 3) and the symmetric matrix (2 2; 2 −1)."""
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


def directions():
    M = np.array([[4, 1], [2, 3]])
    fig, ax = plt.subplots(figsize=(5, 5))
    axes(ax, 5.6)
    th = np.linspace(0, 2 * np.pi, 200)
    ax.plot(np.cos(th), np.sin(th), color="grey", lw=1)
    for t in np.radians(np.arange(0, 360, 30)):
        v = np.array([np.cos(t), np.sin(t)]); w = M @ v
        ax.annotate("", xy=w, xytext=v, arrowprops=dict(arrowstyle="->", color="#9AAABB", lw=0.9))
    for v, lam, lab in ((np.array([1, 1]) / np.sqrt(2), 5, "λ = 5"), (np.array([1, -2]) / np.sqrt(5), 2, "λ = 2")):
        for s in (1, -1):
            ax.plot([0, s * lam * v[0]], [0, s * lam * v[1]], color=NAVY, lw=1.2, ls="--")
            ax.annotate("", xy=s * lam * v, xytext=s * v, arrowprops=dict(arrowstyle="->", color=RED, lw=1.8))
        ax.text(lam * v[0] + 0.15, lam * v[1], lab, color=RED)
    fig.tight_layout()
    fig.savefig(HERE / "pb12_directions.png", dpi=200, facecolor="white")


def symmetric():
    A = np.array([[2, 2], [2, -1]])
    fig, ax = plt.subplots(figsize=(4.6, 4.6))
    axes(ax, 3.6)
    th = np.linspace(0, 2 * np.pi, 300)
    circ = np.vstack([np.cos(th), np.sin(th)])
    ell = A @ circ
    ax.plot(circ[0], circ[1], "--", color="grey", lw=1)
    ax.plot(ell[0], ell[1], color=NAVY, lw=1.8)
    for v, lam, lab in ((np.array([2, 1]) / np.sqrt(5), 3, "(2, 1), λ = 3"), (np.array([1, -2]) / np.sqrt(5), -2, "(1, −2), λ = −2")):
        ax.plot([-3.4 * v[0], 3.4 * v[0]], [-3.4 * v[1], 3.4 * v[1]], color=RED, lw=1, ls=":")
        ax.annotate("", xy=lam * v, xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=RED, lw=1.6))
        ax.text(3.0 * v[0] + 0.1, 3.0 * v[1] + (0.25 if lam > 0 else -0.45), lab, color=RED, fontsize=9)
    fig.tight_layout()
    fig.savefig(HERE / "pb12_symmetric.png", dpi=200, facecolor="white")


if __name__ == "__main__":
    directions()
    symmetric()
