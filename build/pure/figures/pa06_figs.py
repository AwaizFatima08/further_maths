"""Figure for Unit A6: area scale factor of M = (3 1; 1 2)."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).parent
NAVY = "#1F3A5F"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})


def main():
    M = np.array([[3, 1], [1, 2]])
    sq = np.array([[0, 1, 1, 0, 0], [0, 0, 1, 1, 0]], dtype=float)
    img = M @ sq
    fig, ax = plt.subplots(figsize=(5.5, 4))
    ax.fill(img[0], img[1], color="#C9D7E8"); ax.plot(img[0], img[1], color=NAVY, lw=1.8)
    ax.fill(sq[0], sq[1], color="#E8E8E8"); ax.plot(sq[0], sq[1], "--", color="grey", lw=1.2)
    for (x, y), lab in zip(img.T[:4], ["O", "A′(3, 1)", "B′(4, 3)", "C′(1, 2)"]):
        ax.plot(x, y, "o", color=NAVY, ms=3)
        ax.text(x + 0.08, y + 0.08 if lab != "O" else y - 0.3, lab, fontsize=9)
    ax.text(0.55, 0.35, "1", fontsize=9, color="grey")
    ax.text(2.0, 1.45, "area = det M = 5", fontsize=10, color=NAVY, ha="center")
    ax.set_xlim(-0.5, 4.8); ax.set_ylim(-0.5, 3.6); ax.set_aspect("equal")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_position("zero"); ax.spines["bottom"].set_position("zero")
    ax.set_xlabel("x", loc="right"); ax.set_ylabel("y", loc="top", rotation=0)
    fig.tight_layout()
    fig.savefig(HERE / "pa06_area.png", dpi=200, facecolor="white")


if __name__ == "__main__":
    main()
