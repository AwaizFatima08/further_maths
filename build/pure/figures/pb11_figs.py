"""Figures for unit B11 (SHM, damping, coupled systems). Writes pb11_*.png into this folder."""
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
    fig.savefig(HERE / f"pb11_{name}.png", dpi=200, facecolor="white", bbox_inches="tight")
    plt.close(fig)


# Damping cases, x(0) = 1, x'(0) = 0
t = np.linspace(0, 4, 600)
light = np.exp(-t) * (np.cos(4 * t) + 0.25 * np.sin(4 * t))           # x'' + 2x' + 17x = 0
critical = (1 + 4 * t) * np.exp(-4 * t)                                # x'' + 8x' + 16x = 0
heavy = (4 * np.exp(-2 * t) - np.exp(-8 * t)) / 3                      # x'' + 10x' + 16x = 0
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(t, light, color=NAVY, lw=1.3, label="light damping")
ax.plot(t, critical, color="black", lw=1.6, label="critical damping")
ax.plot(t, heavy, color=NAVY, ls="--", lw=1.5, label="heavy damping")
axes_origin(ax)
ax.set_xlim(0, 4)
ax.set_ylim(-0.8, 1.1)
ax.set_xlabel("t", loc="right")
ax.set_ylabel("x", loc="top", rotation=0)
ax.legend(frameon=False, loc="upper right")
save(fig, "damping")

# Forced: x = sin 2t - 2t e^{-2t}
t = np.linspace(0, 10, 800)
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(t, np.sin(2 * t) - 2 * t * np.exp(-2 * t), color=NAVY, lw=1.5, label="x = sin 2t − 2te⁻²ᵗ")
ax.plot(t, np.sin(2 * t), color="0.45", ls="--", lw=1.1, label="steady state sin 2t")
axes_origin(ax)
ax.set_xlim(0, 10)
ax.set_ylim(-1.6, 1.4)
ax.set_xlabel("t", loc="right")
ax.set_ylabel("x", loc="top", rotation=0)
ax.legend(frameon=False, loc="lower right", fontsize=9)
save(fig, "forced")

# Predator-prey: x = 200 + 100 cos t + 100 sin t, y = 150 + 100 sin t
t = np.linspace(0, 4 * np.pi, 800)
x = 200 + 100 * np.cos(t) + 100 * np.sin(t)
y = 150 + 100 * np.sin(t)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4))
a1.plot(t, x, color=NAVY, lw=1.5, label="prey x")
a1.plot(t, y, color="black", ls="--", lw=1.3, label="predators y")
a1.set_xlim(0, 4 * np.pi)
a1.set_ylim(0, 380)
a1.set_xlabel("t (years)")
a1.set_ylabel("number")
a1.spines["right"].set_visible(False)
a1.spines["top"].set_visible(False)
a1.legend(frameon=False, loc="upper right", fontsize=9, ncol=2)
a2.plot(x, y, color=NAVY, lw=1.5)
a2.plot([200], [150], "o", color="black", ms=4)
a2.annotate("(200, 150)", (200, 150), xytext=(206, 140), fontsize=9)
a2.plot([300], [150], "o", color=NAVY, ms=4)
a2.annotate("start (300, 150)", (300, 150), xytext=(250, 120), fontsize=9)
i = 60
a2.annotate("", xy=(x[i + 5], y[i + 5]), xytext=(x[i], y[i]), arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.5))
a2.set_xlim(0, 380)
a2.set_ylim(0, 280)
a2.set_xlabel("prey x")
a2.set_ylabel("predators y")
a2.spines["right"].set_visible(False)
a2.spines["top"].set_visible(False)
fig.tight_layout()
save(fig, "predator_prey")
print("pb11 figures written")
