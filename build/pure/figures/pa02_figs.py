"""Figures for Unit A2 (pa02). Run: python pa02_figs.py  -> writes pa02_*.png next to this file."""
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import Arc, Circle, Polygon, Wedge  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
NAVY = "#1F3A5F"
SHADE = "#9FC3D9"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11})


def argand(ax, xlim, ylim, labels=True):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    for side in ("left", "bottom"):
        ax.spines[side].set_position("zero")
        ax.spines[side].set_color("black")
    for side in ("right", "top"):
        ax.spines[side].set_visible(False)
    if labels:
        ax.text(xlim[1], 0.02 * (ylim[1] - ylim[0]), "Re", ha="right", va="bottom")
        ax.text(0.02 * (xlim[1] - xlim[0]), ylim[1], "Im", ha="left", va="top")


def arrow(ax, p, q, color=NAVY, ls="-"):
    ax.annotate("", xy=q, xytext=p, arrowprops=dict(arrowstyle="-|>", color=color, lw=1.6, ls=ls, shrinkA=0, shrinkB=0))


def dot(ax, p, label, offset=(6, 4), color="black"):
    ax.plot([p[0]], [p[1]], "o", color=color, ms=4)
    ax.annotate(label, p, xytext=offset, textcoords="offset points")


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(HERE, f"pa02_{name}.png"), dpi=200, facecolor="white", bbox_inches="tight", pad_inches=0.1)
    plt.close(fig)


def addsub():
    fig, ax = plt.subplots(figsize=(6, 4.6))
    argand(ax, (-0.8, 6.2), (-2.6, 4.8))
    z, w = (4, 1), (1, 3)
    s, d = (5, 4), (3, -2)
    arrow(ax, (0, 0), z); arrow(ax, (0, 0), w); arrow(ax, (0, 0), s)
    ax.plot([z[0], s[0]], [z[1], s[1]], color="grey", ls="--", lw=1)
    ax.plot([w[0], s[0]], [w[1], s[1]], color="grey", ls="--", lw=1)
    arrow(ax, w, z, color="#B5462E")
    arrow(ax, (0, 0), d, color="#B5462E", ls="--")
    arrow(ax, (0, 0), (4, -1), color="grey")
    dot(ax, z, "z = 4 + i"); dot(ax, w, "w = 1 + 3i", (-20, 8)); dot(ax, s, "z + w", (6, -4))
    dot(ax, d, "z − w = 3 − 2i", (6, -10)); dot(ax, (4, -1), "z* = 4 − i", (8, -2))
    save(fig, "addsub")


def args():
    fig, ax = plt.subplots(figsize=(6, 4.2))
    argand(ax, (-3.2, 2.2), (-2.6, 2.0))
    a, b = (-np.sqrt(3), 1), (-2, -2)
    arrow(ax, (0, 0), a); arrow(ax, (0, 0), b)
    dot(ax, a, "−√3 + i", (-40, 6)); dot(ax, b, "−2 − 2i", (-30, -14))
    ax.add_patch(Arc((0, 0), 1.0, 1.0, theta1=0, theta2=150, color=NAVY, lw=1.3))
    ax.text(0.15, 0.6, "θ = 5π/6", color=NAVY)
    ax.add_patch(Arc((0, 0), 1.6, 1.6, theta1=-135, theta2=0, color="#B5462E", lw=1.3))
    ax.text(0.5, -0.9, "θ = −3π/4", color="#B5462E")
    ax.text(-1.25, 0.75, "r = 2", rotation=-30)
    ax.text(-1.95, -1.2, "r = 2√2", rotation=45)
    save(fig, "args")


def square():
    fig, ax = plt.subplots(figsize=(5, 4.6))
    argand(ax, (-2.6, 4.2), (-1.8, 4.8))
    z, iz, s, zc = (3, 1), (-1, 3), (2, 4), (3, -1)
    ax.add_patch(Polygon([(0, 0), z, s, iz], closed=True, fc=SHADE, ec=NAVY, alpha=0.5))
    for p, lab, off in [(z, "z = 3 + i", (6, -4)), (iz, "iz = −1 + 3i", (-70, 8)), (s, "z + iz = 2 + 4i", (6, 4)),
                        (zc, "z* = 3 − i", (6, -6))]:
        dot(ax, p, lab, off)
    arrow(ax, (0, 0), z); arrow(ax, (0, 0), iz); arrow(ax, (0, 0), zc, color="grey")
    save(fig, "square")


def loci():
    fig, axs = plt.subplots(1, 3, figsize=(12, 4.3))
    ax = axs[0]
    argand(ax, (-2, 8), (-7, 3))
    ax.add_patch(Circle((3, -2), 4, fill=False, ec=NAVY, lw=2))
    dot(ax, (3, -2), "3 − 2i")
    ax.text(0.5, -0.08, "(a) |z − 3 + 2i| = 4", transform=ax.transAxes, ha="center", va="top")
    ax = axs[1]
    argand(ax, (-3, 4), (-1.5, 4))
    x = np.linspace(-3, 4, 10)
    ax.plot(x, (4 - x) / 3, color=NAVY, lw=2)
    ax.plot([-1, 0], [0, 3], color="grey", ls="--", lw=1)
    dot(ax, (-1, 0), "−1", (-12, -14)); dot(ax, (0, 3), "3i")
    ax.text(0.5, -0.08, "(b) |z + 1| = |z − 3i|", transform=ax.transAxes, ha="center", va="top")
    ax.text(1.2, 1.25, "x + 3y = 4", color=NAVY, fontsize=10)
    ax = axs[2]
    argand(ax, (-1, 6), (-1.5, 4.5))
    ax.plot([2, 6], [0, 4], color=NAVY, lw=2)
    ax.plot([2], [0], "o", mfc="white", mec=NAVY, ms=6)
    ax.add_patch(Arc((2, 0), 1.2, 1.2, theta1=0, theta2=45, color="black"))
    ax.text(2.7, 0.15, "π/4")
    ax.text(0.5, -0.08, "(c) arg(z − 2) = π/4", transform=ax.transAxes, ha="center", va="top")
    save(fig, "loci")


def region():
    fig, ax = plt.subplots(figsize=(5, 4.6))
    argand(ax, (-0.7, 5), (-0.7, 4.8))
    ax.add_patch(Wedge((2, 2), 2, -135, 45, fc=SHADE, ec="none", alpha=0.8))
    ax.add_patch(Circle((2, 2), 2, fill=False, ec=NAVY, lw=1.6))
    ax.plot([0, 4.6], [0, 4.6], color=NAVY, lw=1.6)
    dot(ax, (2, 2), "2 + 2i", (-44, 4))
    r = 2 + 2 * np.sqrt(2)
    dot(ax, (r / np.sqrt(2), r / np.sqrt(2)), "greatest |z|", (6, -2))
    q = 2 * np.sqrt(2) - 2
    dot(ax, (q / np.sqrt(2), q / np.sqrt(2)), "least |z|", (6, -10))
    ax.text(2.6, 0.9, "R", fontsize=14, color=NAVY)
    ax.text(3.2, 4.4, "arg z = π/4", fontsize=10)
    save(fig, "region")


def tangent():
    fig, ax = plt.subplots(figsize=(5, 5))
    argand(ax, (-4.5, 4.5), (-0.6, 8.8))
    ax.add_patch(Circle((0, 5), 3, fill=False, ec=NAVY, lw=2))
    dot(ax, (0, 5), "5i")
    a = np.arcsin(0.6)
    for th in (np.pi / 2 - a, np.pi / 2 + a):
        ax.plot([0, 6 * np.cos(th)], [0, 6 * np.sin(th)], color="grey", lw=1.2)
        p = (4 * np.cos(th), 4 * np.sin(th))
        ax.plot([0, p[0]], [5, p[1]], color="grey", ls="--", lw=1)
        ax.plot([p[0]], [p[1]], "o", color="black", ms=4)
    ax.annotate("2.4 + 3.2i", (2.4, 3.2), xytext=(8, -8), textcoords="offset points")
    dot(ax, (0, 8), "8i", (6, 4)); dot(ax, (0, 2), "2i", (6, -12))
    ax.add_patch(Arc((0, 0), 2, 2, theta1=0, theta2=np.degrees(np.pi / 2 - a), color="black"))
    ax.text(0.9, 0.35, "0.927", fontsize=10)
    save(fig, "tangent")


if __name__ == "__main__":
    addsub(); args(); square(); loci(); region(); tangent()
    print("pa02 figures written")
