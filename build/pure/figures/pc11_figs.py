"""Figures for Unit C11 (recurrence relations). Writes pc11_*.png here."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

HERE = Path(__file__).resolve().parent
NAVY = "#1F3A5F"
RED = "#B03A2E"
GREY = "#777777"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "axes.grid": False})


def save(fig, name):
    fig.savefig(HERE / f"pc11_{name}.png", dpi=200, facecolor="white", bbox_inches="tight")
    plt.close(fig)


def iterate(f, u1, n):
    out = [u1]
    for _ in range(n - 1):
        out.append(f(out[-1]))
    return np.array(out, dtype=float)


def style(ax):
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)


# 1. Four kinds of behaviour (terms against n)
fig, axs = plt.subplots(2, 2, figsize=(9, 5.6))
cases = [
    (iterate(lambda u: u / 2 + 1, 0, 12), "Monotonic, convergent: uₙ₊₁ = ½uₙ + 1, u₁ = 0 (limit 2)", 2),
    (iterate(lambda u: -u / 2 + 3, 0, 12), "Oscillating, convergent: uₙ₊₁ = −½uₙ + 3, u₁ = 0 (limit 2)", 2),
    (iterate(lambda u: 1 / (1 - u), 2, 12), "Periodic, period 3: uₙ₊₁ = 1/(1 − uₙ), u₁ = 2", None),
    (np.array([(-1)**m * m for m in range(1, 13)], dtype=float), "Oscillating, divergent: uₙ = (−1)ⁿ n", None),
]
for ax, (u, label, lim) in zip(axs.flat, cases):
    style(ax)
    ns = np.arange(1, len(u) + 1)
    ax.axhline(0, color="black", lw=0.8)
    if lim is not None:
        ax.axhline(lim, color=GREY, ls="--", lw=1)
    ax.plot(ns, u, color=GREY, lw=0.8)
    ax.plot(ns, u, "o", color=NAVY, ms=4)
    ax.set_xlabel("n", fontsize=9)
    ax.set_ylabel("uₙ", fontsize=9)
    ax.set_xticks(range(1, 13))
    ax.text(0.5, -0.32, label, transform=ax.transAxes, ha="center", va="top", fontsize=9)
fig.tight_layout(h_pad=3.2)
save(fig, "behaviour")


# 2. Staircase and cobweb diagrams
def web(ax, f, u1, steps, xlim, ylim, flabel, L):
    style(ax)
    xs = np.linspace(*xlim, 400)
    ax.plot(xs, f(xs), color=NAVY, lw=1.8, label=flabel)
    ax.plot(xs, xs, color=RED, lw=1.2, label="y = x")
    u = u1
    px, py = [u], [0]
    for _ in range(steps):
        v = f(u)
        px += [u, v]
        py += [v, v]
        u = v
    ax.plot(px, py, color="#2E8B57", lw=1)
    ax.plot([u1], [0], "o", color="#2E8B57", ms=4)
    ax.plot([L], [L], "o", color="black", ms=4)
    ax.annotate(f"({L}, {L})", (L, L), xytext=(8, -14), textcoords="offset points", fontsize=9)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xlabel("uₙ")
    ax.set_ylabel("uₙ₊₁")
    ax.legend(loc="upper left", fontsize=9, frameon=False)


fig, axs = plt.subplots(1, 2, figsize=(10, 4.2))
web(axs[0], lambda u: np.sqrt(u + 6), 0, 6, (0, 4.5), (0, 4.5), "y = √(x + 6)", 3)
axs[0].text(0.5, -0.18, "Staircase: u₁ = 0, uₙ₊₁ = √(uₙ + 6) increases to 3", transform=axs[0].transAxes,
            ha="center", va="top", fontsize=9)
web(axs[1], lambda u: -u / 2 + 3, 0, 8, (0, 4), (0, 4), "y = −½x + 3", 2)
axs[1].text(0.5, -0.18, "Cobweb: u₁ = 0, uₙ₊₁ = −½uₙ + 3 oscillates towards 2", transform=axs[1].transAxes,
            ha="center", va="top", fontsize=9)
fig.tight_layout()
save(fig, "cobweb")

# 3. Fibonacci ratios approaching phi
F = [1, 1]
for _ in range(14):
    F.append(F[-1] + F[-2])
ratios = [F[i + 1] / F[i] for i in range(len(F) - 1)]
phi = (1 + 5**0.5) / 2
fig, ax = plt.subplots(figsize=(6, 3.4))
style(ax)
ax.axhline(phi, color=GREY, ls="--", lw=1)
ax.text(len(ratios), phi + 0.03, "φ ≈ 1.618", ha="right", va="bottom", fontsize=9, color=GREY)
ax.plot(range(1, len(ratios) + 1), ratios, color=GREY, lw=0.8)
ax.plot(range(1, len(ratios) + 1), ratios, "o", color=NAVY, ms=4)
ax.set_xlabel("n")
ax.set_ylabel("Fₙ₊₁ / Fₙ")
ax.set_ylim(0.9, 2.1)
save(fig, "fibratio")
print("written pc11 figures")
