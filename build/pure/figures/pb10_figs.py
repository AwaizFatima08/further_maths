"""Figures for unit B10 (second-order DEs). Writes pb10_*.png into this folder."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

HERE = Path(__file__).resolve().parent
NAVY = "#1F3A5F"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})


def axes_origin(ax):
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)


def save(fig, name):
    fig.savefig(HERE / f"pb10_{name}.png", dpi=200, facecolor="white", bbox_inches="tight")
    plt.close(fig)


x = np.linspace(0, 4, 400)
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, np.exp(2 * x) / 3 + 2 * np.exp(-x) / 3, color=NAVY, ls="--", lw=1.5, label="distinct real roots: ⅓e²ˣ + ⅔e⁻ˣ")
ax.plot(x, (1 + x) * np.exp(-x), color="black", lw=1.5, label="repeated root: (1 + x)e⁻ˣ")
ax.plot(x, np.exp(-x) * (np.cos(3 * x) + np.sin(3 * x) / 3), color=NAVY, lw=1.3,
        label="complex roots: e⁻ˣ(cos 3x + ⅓ sin 3x)")
ax.set_ylim(-0.6, 3)
ax.set_xlim(0, 4)
axes_origin(ax)
ax.set_xlabel("x", loc="right")
ax.set_ylabel("y", loc="top", rotation=0)
ax.legend(frameon=False, loc="upper right", fontsize=9)
save(fig, "three_cases")

x = np.linspace(0, 20, 1000)
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, np.sin(2 * x) / 8 - x * np.cos(2 * x) / 4, color=NAVY, lw=1.2)
ax.plot(x, x / 4, color="0.5", ls="--", lw=1)
ax.plot(x, -x / 4, color="0.5", ls="--", lw=1)
ax.text(17.5, 5.0, "y = x/4", fontsize=9)
ax.text(17.5, -5.3, "y = −x/4", fontsize=9)
axes_origin(ax)
ax.set_xlim(0, 20)
ax.set_xlabel("x", loc="right")
ax.set_ylabel("y", loc="top", rotation=0)
save(fig, "resonance")
print("pb10 figures written")
