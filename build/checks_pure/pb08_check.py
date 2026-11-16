"""Verifies every conversion, polar area, intersection and tangent stated in pure/pb08.py (B8 Polar coordinates)."""
import importlib
import math
import sys
from pathlib import Path

import numpy as np
import sympy as sp
from scipy import integrate

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
MODULE = "pb08"
UNIT = importlib.import_module(f"pure.{MODULE}").UNIT


def _flat(o):
    if isinstance(o, str):
        return [o]
    if isinstance(o, dict):
        return [s for v in o.values() for s in _flat(v)]
    if isinstance(o, (list, tuple)):
        return [s for v in o for s in _flat(v)]
    return [str(o)]


TEXT = "\n".join(_flat(UNIT))
COUNT = 0
t = sp.symbols("theta", real=True)
a = sp.symbols("a", positive=True)
X, Y, r = sp.symbols("x y r", real=True)


def same(u, v, tol=1e-12):
    global COUNT
    assert abs(sp.N(sp.sympify(u) - sp.sympify(v), 30)) < tol, f"{u} != {v}"
    COUNT += 1


def has(*snips):
    global COUNT
    for s in snips:
        assert s in TEXT, f"{s!r} not found in {MODULE}"
        COUNT += 1


def area(rr, lo, hi):
    """½∫ r² dθ exactly (sympy)."""
    return sp.simplify(sp.integrate(rr ** 2, (t, lo, hi)) / 2)


def num_area_region(inside, n=1500, R=6.0):
    """Monte-Carlo-free grid estimate of a region's area given an inside(x, y) predicate (vectorised)."""
    g = np.linspace(-R, R, n)
    xx, yy = np.meshgrid(g, g)
    return inside(xx, yy).sum() * (g[1] - g[0]) ** 2


def polar_to_xy(rv, tv):
    return (rv * sp.cos(tv), rv * sp.sin(tv))


def to_polar(xv, yv):
    return (sp.sqrt(xv ** 2 + yv ** 2), sp.atan2(yv, xv))


# 8.1 / 8.2 identities used for conversions
for e1, e2 in ((X * Y, r ** 2 * sp.sin(2 * t) / 2), (X ** 2 - Y ** 2, r ** 2 * sp.cos(2 * t))):
    same(sp.simplify(e1.subs({X: r * sp.cos(t), Y: r * sp.sin(t)}) - e2).subs({r: 1.7, t: 0.9}), 0)
# r = p sec(θ − α) line: x cos α + y sin α = p, check r = 3 sec(θ − π/3) points lie on x + √3 y = 6
for tv in (0.1, 0.7, 1.4, 2.0):
    rv = 3 / sp.cos(tv - sp.pi / 3)
    xv, yv = polar_to_xy(rv, tv)
    same(xv + sp.sqrt(3) * yv, 6)
# spiral crossings of the initial line for r = kθ at 2πk, 4πk (trivial) and r = 2a cos θ is a circle (x − a)² + y² = a²
for tv in (-1.2, 0.3, 1.0):
    xv, yv = polar_to_xy(2 * a * sp.cos(tv), tv)
    same(((xv - a) ** 2 + yv ** 2 - a ** 2).subs(a, 2.5), 0)

# Limaçon convexity rule: r² + 2r'² − r r'' = p² + 3pq cos θ + 2q² ≥ 0 for all θ  <=>  p ≥ 2q (p > q > 0)
p_, q_ = sp.symbols("p q", positive=True)
rr = p_ + q_ * sp.cos(t)
curv = sp.simplify(rr ** 2 + 2 * sp.diff(rr, t) ** 2 - rr * sp.diff(rr, t, 2))
assert sp.simplify(curv - (p_ ** 2 + 3 * p_ * q_ * sp.cos(t) + 2 * q_ ** 2)) == 0
assert sp.factor(curv.subs(t, sp.pi)) in ((p_ - q_) * (p_ - 2 * q_), (p_ - 2 * q_) * (p_ - q_))
for pv, qv, convex in ((3, 2, False), (5, 2, True), (2, 1, True), (1.5, 1, False)):
    mn = min(float(curv.subs({p_: pv, q_: qv, t: tv})) for tv in np.linspace(0, 2 * np.pi, 721))
    assert (mn >= -1e-12) == convex, (pv, qv)
COUNT += 2
has("If q < p < 2q the curve has a <b>dimple</b>", "If p ≥ 2q it is <b>convex</b>")

# Worked example 1
rv, tv = to_polar(-sp.sqrt(3), 1)
same(rv, 2)
same(tv, 5 * sp.pi / 6)
for tv in (-1.2, 0.4, 1.1):
    xv, yv = polar_to_xy(4 * sp.cos(tv), tv)
    same((xv - 2) ** 2 + yv ** 2, 4)
for tv in (0.1, -0.5, 3.3):
    rv = sp.sqrt(4 / sp.cos(2 * tv))
    xv, yv = polar_to_xy(rv, tv)
    same(xv ** 2 - yv ** 2, 4)
# Worked example 2: limaçon values
f2 = a * (3 + 2 * sp.cos(t))
assert [sp.simplify(f2.subs(t, v)) for v in (0, sp.pi / 2, sp.pi, 3 * sp.pi / 2)] == [5 * a, 3 * a, a, 3 * a]
COUNT += 1
# Worked example 3
same(area(a * (1 + sp.cos(t)), 0, 2 * sp.pi).subs(a, 1), sp.Rational(3, 2) * sp.pi)
same(sp.integrate(sp.Rational(3, 2) + 2 * sp.cos(t) + sp.cos(2 * t) / 2 - (1 + sp.cos(t)) ** 2, (t, 0, 1)), 0)
has("3πa²/2")
# Worked example 4
same(area(2 * sp.sin(3 * t), 0, sp.pi / 3), sp.pi / 3)
for k in range(3):
    same(area(2 * sp.sin(3 * t), 2 * k * sp.pi / 3, 2 * k * sp.pi / 3 + sp.pi / 3), sp.pi / 3)
# Worked example 5
same(sp.acos(sp.Rational(1, 2)), sp.pi / 3)
A5 = 2 * sp.integrate((9 * sp.cos(t) ** 2 - (1 + sp.cos(t)) ** 2) / 2, (t, 0, sp.pi / 3))
same(A5, sp.pi)
assert sp.simplify(8 * sp.cos(t) ** 2 - 2 * sp.cos(t) - 1 - (3 + 4 * sp.cos(2 * t) - 2 * sp.cos(t))) == 0
COUNT += 1
inside_c1 = lambda x, y: (x ** 2 + y ** 2) <= 3 * x  # noqa: E731  r <= 3cosθ  <=>  r² <= 3x
inside_c2 = lambda x, y: np.sqrt(x ** 2 + y ** 2) <= 1 + x / np.maximum(np.sqrt(x ** 2 + y ** 2), 1e-12)  # noqa: E731
est = num_area_region(lambda x, y: inside_c1(x, y) & ~inside_c2(x, y), n=2400, R=3.5)
assert abs(est - math.pi) < 0.02, est
COUNT += 1
# Worked example 6: cardioid tangents
ya = (1 + sp.cos(t)) * sp.sin(t)
xa = (1 + sp.cos(t)) * sp.cos(t)
dy, dx = sp.diff(ya, t), sp.diff(xa, t)
assert sp.simplify(dy - (sp.cos(t) + sp.cos(2 * t))) == 0
assert sp.simplify(dx + sp.sin(t) * (1 + 2 * sp.cos(t))) == 0
for tv in (sp.pi / 3, -sp.pi / 3):
    same(dy.subs(t, tv), 0)
    same((1 + sp.cos(tv)), sp.Rational(3, 2))
for tv in (0, 2 * sp.pi / 3, -2 * sp.pi / 3):
    same(dx.subs(t, tv), 0)
same(dy.subs(t, sp.pi), 0)
same(dx.subs(t, sp.pi), 0)
sols_dy = sp.solveset(dy, t, sp.Interval.Lopen(-sp.pi, sp.pi))
assert set(sols_dy) == {-sp.pi / 3, sp.pi / 3, sp.pi}, sols_dy
sols_dx = sp.solveset(dx, t, sp.Interval.Lopen(-sp.pi, sp.pi))
assert set(sols_dx) == {0, sp.pi, 2 * sp.pi / 3, -2 * sp.pi / 3}, sols_dx
COUNT += 2
has("(3a/2, π/3) and (3a/2, −π/3)", "(2a, 0), (a/2, 2π/3) and (a/2, −2π/3)")

# Practice
same(4 * sp.cos(sp.pi / 6), 2 * sp.sqrt(3)); same(4 * sp.sin(sp.pi / 6), 2)
same(2 * sp.cos(3 * sp.pi / 4), -sp.sqrt(2)); same(2 * sp.sin(3 * sp.pi / 4), sp.sqrt(2))
rv, tv = to_polar(3, -3); same(rv, 3 * sp.sqrt(2)); same(tv, -sp.pi / 4)
rv, tv = to_polar(-1, -sp.sqrt(3)); same(rv, 2); same(tv, -2 * sp.pi / 3)
for tv in (0.3, 1.2, 2.5):
    xv, yv = polar_to_xy(6 * sp.sin(tv), tv)
    same(xv ** 2 + (yv - 3) ** 2, 9)
    xv, yv = polar_to_xy(3 / sp.sin(tv), tv)
    same(yv, 3)
for tv in (0.2, 0.7, 3.5):
    xv, yv = polar_to_xy(sp.sqrt(8 / sp.sin(2 * tv)), tv)
    same(xv * yv, 4)
for tv in (-0.4, 0.5, 1.5):
    xv, yv = polar_to_xy(2 / sp.cos(tv - sp.pi / 6), tv)
    same(sp.sqrt(3) * xv + yv, 4)
same(area(3 * sp.cos(2 * t), -sp.pi / 4, sp.pi / 4), 9 * sp.pi / 8)
same(2 * area(2 * sp.sqrt(sp.cos(2 * t)), -sp.pi / 4, sp.pi / 4), 4)
same(area(2 * a * sp.cos(t), -sp.pi / 2, sp.pi / 2).subs(a, 1), sp.pi)
same(area(t, 0, sp.pi), sp.pi ** 3 / 6)
assert round(float(sp.pi ** 3 / 6), 2) == 5.17
COUNT += 1
same(area(2 + sp.cos(t), 0, 2 * sp.pi), 9 * sp.pi / 2)
# Q12: r = a sin 2θ, horizontal tangent
y12 = sp.sin(2 * t) * sp.sin(t)
d12 = sp.diff(y12, t)
assert sp.simplify(d12 - 2 * sp.sin(t) * (2 * sp.cos(t) ** 2 - sp.sin(t) ** 2)) == 0
th12 = sp.atan(sp.sqrt(2))
same(d12.subs(t, th12), 0)
same(sp.sin(2 * th12), 2 * sp.sqrt(2) / 3)
assert round(float(th12), 3) == 0.955
COUNT += 1
has("9π/8", "π³/6", "9π/2", "(2√2a/3, arctan √2)")

# Section B Q1
same(area(a * (3 + 2 * sp.cos(t)), 0, 2 * sp.pi).subs(a, 1), 11 * sp.pi)
x1 = (3 + 2 * sp.cos(t)) * sp.cos(t)
assert sp.simplify(sp.diff(x1, t) + sp.sin(t) * (3 + 4 * sp.cos(t))) == 0
th1 = sp.acos(-sp.Rational(3, 4))
same(sp.diff(x1, t).subs(t, th1), 0)
same(3 + 2 * sp.cos(th1), sp.Rational(3, 2))
assert round(float(th1), 2) == 2.42 and round(float(2 * sp.pi - th1), 2) == 3.86
same(sp.diff((3 + 2 * sp.cos(t)) * sp.sin(t), t).subs(t, sp.pi), -1)  # dy/dθ ≠ 0 at θ = π, so (a, π) is a genuine vertical tangent
COUNT += 1
has("11πa²", "(3a/2, 2.42) and (3a/2, 3.86)")
# Section B Q2
same(sp.acos(sp.Rational(1, 2)), sp.pi / 3)
part1 = 2 * area(4 * (1 - sp.cos(t)), 0, sp.pi / 3)
part2 = 2 * area(4 * sp.cos(t), sp.pi / 3, sp.pi / 2)
same(part1, 8 * sp.pi - 14 * sp.sqrt(3))
same(part2, 4 * sp.pi / 3 - 2 * sp.sqrt(3))
same(part1 + part2, 28 * sp.pi / 3 - 16 * sp.sqrt(3))
assert round(float(28 * sp.pi / 3 - 16 * sp.sqrt(3)), 2) == 1.61
in1 = lambda x, y: (x ** 2 + y ** 2) <= 4 * x  # noqa: E731
in2 = lambda x, y: np.sqrt(x ** 2 + y ** 2) <= 4 * (1 - x / np.maximum(np.sqrt(x ** 2 + y ** 2), 1e-12))  # noqa: E731
est = num_area_region(lambda x, y: in1(x, y) & in2(x, y), n=2400, R=4.5)
assert abs(est - float(28 * sp.pi / 3 - 16 * sp.sqrt(3))) < 0.02, est
COUNT += 2
# Section B Q3
same(area(4 * sp.cos(2 * t), -sp.pi / 4, sp.pi / 4), 2 * sp.pi)
y3 = 4 * sp.cos(2 * t) * sp.sin(t)
assert sp.simplify(sp.diff(y3, t) - 4 * sp.cos(t) * (1 - 6 * sp.sin(t) ** 2)) == 0
th3 = sp.asin(1 / sp.sqrt(6))
same(4 * sp.cos(2 * th3), sp.Rational(8, 3))
assert round(float(th3), 3) == 0.421
same(4 * sp.cos(2 * th3) * sp.sin(th3), 4 * sp.sqrt(6) / 9)
same(2 * 4 * sp.sqrt(6) / 9, 8 * sp.sqrt(6) / 9)
assert round(float(8 * sp.sqrt(6) / 9), 2) == 2.18
COUNT += 2
has("8√6/9", "(8/3, 0.421) and (8/3, −0.421)")
# Section B Q4
same(sp.simplify(((X ** 2 + Y ** 2) ** 2 - 4 * X * Y).subs({X: r * sp.cos(t), Y: r * sp.sin(t)}) - (r ** 4 - 2 * r ** 2 * sp.sin(2 * t))).subs({r: 1.3, t: 0.4}), 0)
same(area(sp.sqrt(2 * sp.sin(2 * t)), 0, sp.pi / 2), 1)
same(sp.sqrt(2 * sp.sin(2 * sp.pi / 4)), sp.sqrt(2))
val = integrate.quad(lambda th: max(2 * math.sin(2 * th), 0) / 2, 0, 2 * math.pi)[0]
assert abs(val - 2) < 1e-9
COUNT += 1

print(f"pb08 checks passed: {COUNT} assertions")
