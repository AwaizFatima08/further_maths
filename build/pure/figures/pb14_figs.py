"""Figures for unit B14 (numerical methods). Writes pb14_*.png into this folder."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

HERE = Path(__file__).resolve().parent
NAVY = "#1F3A5F"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})


def tidy(ax):
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)


def save(fig, name):
    fig.savefig(HERE / f"pb14_{name}.png", dpi=200, facecolor="white", bbox_inches="tight")
    plt.close(fig)


# Newton-Raphson tangents for f(x) = x^3 - 2x - 5 from x0 = 2.5
f = lambda x: x ** 3 - 2 * x - 5
df = lambda x: 3 * x ** 2 - 2
fig, ax = plt.subplots(figsize=(6, 4))
xs = np.linspace(1.9, 2.7, 300)
ax.plot(xs, f(xs), color=NAVY, lw=1.8)
ax.axhline(0, color="black", lw=0.8)
x = 2.5
for n in range(3):
    x_next = x - f(x) / df(x)
    ax.plot([x, x], [0, f(x)], color="0.5", ls=":", lw=1)
    ax.plot([x, x_next], [f(x), 0], color="black", lw=1)
    ax.plot([x], [f(x)], "o", color=NAVY, ms=3.5)
    ax.annotate(f"x{'₀₁₂'[n]}", (x, 0), xytext=(x + 0.005, -1.4), fontsize=9)
    x = x_next
ax.annotate("α ≈ 2.0946", (2.0946, 0), xytext=(1.93, 1.4), fontsize=9,
            arrowprops=dict(arrowstyle="-", color="0.4", lw=0.8))
ax.set_xlim(1.9, 2.7)
ax.set_ylim(-3, 10)
tidy(ax)
ax.set_xlabel("x")
ax.set_ylabel("y = f(x)")
save(fig, "newton")

# Mid-ordinate and Simpson strips for sqrt(1 + x^3) on [0, 1], four strips
g = lambda x: np.sqrt(1 + x ** 3)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4))
xs = np.linspace(0, 1, 300)
h = 0.25
for ax in (a1, a2):
    ax.plot(xs, g(xs), color=NAVY, lw=1.8)
    ax.set_xlim(-0.02, 1.05)
    ax.set_ylim(0, 1.55)
    tidy(ax)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
for i in range(4):
    m = (i + 0.5) * h
    a1.add_patch(plt.Rectangle((i * h, 0), h, g(m), facecolor="#E8F1F5", edgecolor="black", lw=0.8))
    a1.plot([m], [g(m)], "o", color="black", ms=3)
a1.plot(xs, g(xs), color=NAVY, lw=1.8)
for i in range(5):
    a2.plot([i * h, i * h], [0, g(i * h)], color="black", lw=0.8)
for j in range(2):
    x0, x1, x2 = 2 * j * h, (2 * j + 1) * h, (2 * j + 2) * h
    p = np.polyfit([x0, x1, x2], [g(x0), g(x1), g(x2)], 2)
    xx = np.linspace(x0, x2, 100)
    a2.fill_between(xx, np.polyval(p, xx), color="#E8F1F5")
    a2.plot(xx, np.polyval(p, xx), color="black", ls="--", lw=1.1)
a2.plot(xs, g(xs), color=NAVY, lw=1.8, alpha=0.8)
for i in range(5):
    a2.annotate(f"y{'₀₁₂₃₄'[i]}", (i * h, g(i * h)), xytext=(max(i * h - 0.03, 0.005), g(i * h) + 0.06), fontsize=9)
fig.tight_layout()
save(fig, "strips")

# Euler steps for y' = x + y, y(0) = 1, h = 0.1, compared with exact 2e^x - x - 1
fig, ax = plt.subplots(figsize=(6, 4))
xs = np.linspace(0, 0.32, 200)
ax.plot(xs, 2 * np.exp(xs) - xs - 1, color=NAVY, lw=1.8, label="exact y = 2eˣ − x − 1")
px, py = [0.0], [1.0]
for r in range(3):
    py.append(py[-1] + 0.1 * (px[-1] + py[-1]))
    px.append(px[-1] + 0.1)
ax.plot(px, py, "o-", color="black", lw=1.2, ms=4, label="Euler, h = 0.1")
for xv, yv in zip(px, py):
    ax.annotate(f"{yv:.4g}", (xv, yv), xytext=(xv + 0.005, yv - 0.035), fontsize=8)
ax.annotate("1.3997", (0.3, 2 * np.exp(0.3) - 1.3), xytext=(0.262, 1.395), fontsize=8, color=NAVY)
ax.set_xlim(0, 0.33)
ax.set_ylim(0.95, 1.45)
tidy(ax)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend(frameon=False, loc="upper left")
save(fig, "euler")
print("pb14 figures written")
