"""Verifies every t-formula result, identity, equation solution and integral stated in pure/pc01.py (C1)."""
import importlib
import math
import random
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
MODULE = "pc01"
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
x, th = sp.symbols("x theta", real=True)
t = sp.symbols("t", real=True)
S = lambda tt: 2 * tt / (1 + tt ** 2)  # noqa: E731
C = lambda tt: (1 - tt ** 2) / (1 + tt ** 2)  # noqa: E731
T = lambda tt: 2 * tt / (1 - tt ** 2)  # noqa: E731


def same(a, b, tol=1e-12):
    global COUNT
    assert abs(sp.N(sp.sympify(a) - sp.sympify(b), 30)) < tol, f"{a} != {b}"
    COUNT += 1


def zero_t(expr):
    """Rational expression in t simplifies to zero."""
    global COUNT
    assert sp.simplify(sp.together(expr)) == 0, expr
    COUNT += 1


def ident(lhs, rhs, lo=0.1, hi=3.0):
    """Trig identity in θ holds at random points (avoiding singularities)."""
    global COUNT
    f = sp.lambdify(th, lhs - rhs, "mpmath")
    for _ in range(20):
        v = random.uniform(lo, hi)
        assert abs(f(v)) < 1e-10, (lhs, rhs, v)
    COUNT += 1


def has(*snips):
    global COUNT
    for s in snips:
        assert s in TEXT, f"{s!r} not found in {MODULE}"
        COUNT += 1


def all_roots(f, lo, hi, n=4000):
    """All roots of f on [lo, hi) by sign changes and tangency (min |f|) with refinement."""
    import numpy as np
    from scipy.optimize import brentq, minimize_scalar
    xs = np.linspace(lo, hi, n + 1)
    vals = [f(v) for v in xs]
    roots = []
    for i in range(n):
        a, b = xs[i], xs[i + 1]
        if vals[i] == 0:
            roots.append(a)
        elif vals[i] * vals[i + 1] < 0:
            roots.append(brentq(f, a, b))
        elif i > 0 and abs(vals[i]) < abs(vals[i - 1]) and abs(vals[i]) < abs(vals[i + 1]) and abs(vals[i]) < 1e-3:
            m = minimize_scalar(lambda z: abs(f(z)), bounds=(xs[i - 1], xs[i + 1]), method="bounded", options={"xatol": 1e-12})
            if abs(f(m.x)) < 1e-8:
                roots.append(m.x)
    out = []
    for r in sorted(roots):
        if not out or abs(r - out[-1]) > 1e-6:
            out.append(r)
    return out


def solved(f, lo, hi, stated, dp=None, sf=None):
    """The roots of f on [lo, hi) are exactly `stated` (floats), compared after rounding."""
    global COUNT
    rs = all_roots(f, lo, hi)
    assert len(rs) == len(stated), (rs, stated)
    for r, s in zip(rs, sorted(stated)):
        if sf:
            assert float(f"{r:.{sf}g}") == s, (r, s)
        elif dp is not None:
            assert round(r, dp) == s, (r, s)
        else:
            assert abs(r - s) < 1e-9, (r, s)
    COUNT += 1


# 1.1 reciprocal identities
ident(1 + sp.tan(th) ** 2, 1 / sp.cos(th) ** 2, 0.1, 1.4)
ident(1 + 1 / sp.tan(th) ** 2, 1 / sp.sin(th) ** 2, 0.1, 3.0)

# 1.2 t-formulae (θ = 2 arctan t)
for f_, g in ((sp.sin, S), (sp.cos, C), (sp.tan, T)):
    for tv in (-3.1, -0.4, 0.3, 0.7, 2.5):
        same(f_(2 * sp.atan(tv)), g(sp.Float(tv)))
zero_t((1 - t ** 2) ** 2 + (2 * t) ** 2 - (1 + t ** 2) ** 2)
zero_t(1 / S(t) - (1 + t ** 2) / (2 * t))
zero_t(1 / C(t) - (1 + t ** 2) / (1 - t ** 2))
zero_t(C(t) / S(t) - (1 - t ** 2) / (2 * t))
has("sin θ = 2t/(1 + t²)", "cos θ = (1 − t²)/(1 + t²)", "tan θ = 2t/(1 − t²)")

# 1.3 identities quoted in notes
ident((1 - sp.cos(th)) / sp.sin(th), sp.tan(th / 2))
ident(1 / sp.sin(th) + 1 / sp.tan(th), 1 / sp.tan(th / 2))
ident(1 / sp.cos(th) + sp.tan(th), sp.tan(sp.pi / 4 + th / 2), -1.4, 1.4)
zero_t(1 / C(t) + T(t) - (1 + t) / (1 - t))

# 1.4 quadratic for a cos x + b sin x = c
a, b, c = sp.symbols("a b c")
zero_t(sp.expand((a * C(t) + b * S(t) - c) * (1 + t ** 2)) + ((a + c) * t ** 2 - 2 * b * t + (c - a)))
disc = sp.expand((2 * b) ** 2 - 4 * (a + c) * (c - a))
assert sp.expand(disc - 4 * (a ** 2 + b ** 2 - c ** 2)) == 0
COUNT += 1
has("(a + c)t² − 2bt + (c − a) = 0", "a² + b² ≥ c²")

# 1.5 Weierstrass: dx/dt and the sec/cosec antiderivatives
assert sp.simplify(sp.diff(2 * sp.atan(t), t) - 2 / (1 + t ** 2)) == 0
COUNT += 1
zero_t((1 + t ** 2) / (1 - t ** 2) * 2 / (1 + t ** 2) - 2 / (1 - t ** 2))
assert sp.simplify(sp.diff(sp.log((1 + t) / (1 - t)), t) - 2 / (1 - t ** 2)) == 0
COUNT += 1
ident(sp.log(1 / sp.cos(th) + sp.tan(th)), sp.log((1 + sp.tan(th / 2)) / (1 - sp.tan(th / 2))), 0.05, 1.5)
ident(sp.diff(sp.log(sp.tan(th / 2)), th), 1 / sp.sin(th), 0.1, 3.0)
for xv, tv in ((sp.pi / 3, 1 / sp.sqrt(3)), (sp.pi / 2, 1), (2 * sp.pi / 3, sp.sqrt(3))):
    same(sp.tan(xv / 2), tv)

# Worked example 2
zero_t((1 + S(t) - C(t)) / (1 + S(t) + C(t)) - t)
ident((1 + sp.sin(th) - sp.cos(th)) / (1 + sp.sin(th) + sp.cos(th)), sp.tan(th / 2), 0.1, 3.0)
# Worked example 3
assert set(sp.solve(5 * t ** 2 - 8 * t - 1, t)) == {(4 + sp.sqrt(21)) / 5, (4 - sp.sqrt(21)) / 5}
COUNT += 1
zero_t(sp.expand((3 * C(t) + 4 * S(t) - 2) * (1 + t ** 2)) + (5 * t ** 2 - 8 * t - 1))
solved(lambda v: 3 * math.cos(v) + 4 * math.sin(v) - 2, 0, 2 * math.pi, [2.09, 6.05], sf=3)
assert round(math.atan((4 + math.sqrt(21)) / 5), 4) == 1.0433 and round(math.atan((4 - math.sqrt(21)) / 5) + math.pi, 4) == 3.0256
COUNT += 1
has("x = 2.09 or x = 6.05", "(4 ± √21)/5")
# Worked example 4
solved(lambda v: 2 * math.sin(v) - math.cos(v) - 1, 0, 2 * math.pi, [2 * math.atan(0.5), math.pi])
assert round(2 * math.atan(0.5), 3) == 0.927
same(sp.sin(2 * sp.atan(sp.Rational(1, 2))), sp.Rational(4, 5))
same(sp.cos(2 * sp.atan(sp.Rational(1, 2))), sp.Rational(3, 5))
# Worked example 5
zero_t((1 + S(t) + C(t)) - (2 + 2 * t) / (1 + t ** 2))
zero_t(1 / (1 + S(t) + C(t)) * 2 / (1 + t ** 2) - 1 / (1 + t))
same(sp.Integral(1 / (1 + sp.sin(x) + sp.cos(x)), (x, 0, sp.pi / 2)).evalf(30), sp.log(2))
# Worked example 6
zero_t(1 / (2 + C(t)) * 2 / (1 + t ** 2) - 2 / (3 + t ** 2))
I6 = sp.Integral(1 / (2 + sp.cos(x)), (x, 0, sp.pi / 2)).evalf(30)
same(I6, sp.pi * sp.sqrt(3) / 9)
same(sp.integrate(2 / (3 + t ** 2), (t, 0, 1)), sp.pi / (3 * sp.sqrt(3)))
assert round(float(I6), 3) == 0.605
COUNT += 1

# Practice
same(1 / sp.cos(sp.pi / 3), 2); same(1 / sp.sin(5 * sp.pi / 6), 2); same(1 / sp.tan(3 * sp.pi / 4), -1)
tv = sp.Rational(1, 3)
same(S(tv), sp.Rational(3, 5)); same(C(tv), sp.Rational(4, 5)); same(T(tv), sp.Rational(3, 4))
tv = sp.Integer(2)
same(1 / C(tv), -sp.Rational(5, 3)); same(1 / S(tv), sp.Rational(5, 4)); same(C(tv) / S(tv), -sp.Rational(3, 4))
zero_t((1 - C(t)) / S(t) - t)
ident((1 + sp.cos(th)) / (1 - sp.cos(th)), 1 / sp.tan(th / 2) ** 2)
zero_t((1 + C(t)) / (1 - C(t)) - 1 / t ** 2)
zero_t(1 / S(t) + C(t) / S(t) - 1 / t)
solved(lambda v: 1 / math.sin(v) + 1 / math.tan(v) - 3, 0.01, 2 * math.pi - 0.01, [0.644], sf=3)
zero_t(sp.expand((5 * C(t) + 12 * S(t) - 13) * (1 + t ** 2)) + (18 * t ** 2 - 24 * t + 8))
assert sp.factor(9 * t ** 2 - 12 * t + 4) == (3 * t - 2) ** 2
COUNT += 1
solved(lambda v: 5 * math.cos(v) + 12 * math.sin(v) - 13, 0, 2 * math.pi, [1.18], sf=3)
solved(lambda v: 2 * math.cos(v) + math.sin(v) - 1, 0, 2 * math.pi, [math.pi / 2, 2 * math.pi - 2 * math.atan(1 / 3)])
assert round(2 * math.pi - 2 * math.atan(1 / 3), 2) == 5.64
COUNT += 1
solved(lambda v: 3 * math.sin(math.radians(v)) + math.cos(math.radians(v)) + 1, 0, 360, [180.0, 323.1], dp=1)
assert sp.simplify(sp.integrate(1 / (1 + C(t)) * 2 / (1 + t ** 2), t) - t) == 0
COUNT += 1
same(sp.Integral(1 / (1 + sp.sin(x)), (x, 0, sp.pi / 2)).evalf(30), 1)
zero_t(1 + S(t) - (1 + t) ** 2 / (1 + t ** 2))
same(sp.Integral(1 / (5 - 4 * sp.cos(x)), (x, 0, sp.pi / 3)).evalf(30), 2 * sp.pi / 9)
zero_t(5 - 4 * C(t) - (1 + 9 * t ** 2) / (1 + t ** 2))
has("x = 2 arctan(1/3) = 0.644", "x = 2 arctan(2/3) = 1.18", "5.64", "323.1°", "2π/9")

# Section B Q1
zero_t(sp.expand((4 * S(t) - 3 * C(t) - 2) * (1 + t ** 2)) - (t ** 2 + 8 * t - 5))
solved(lambda v: 4 * math.sin(v) - 3 * math.cos(v) - 2, 0, 2 * math.pi, [1.06, 3.37], sf=3)
assert abs(-4 + math.sqrt(21) - 0.5826) < 1e-4 and abs(-4 - math.sqrt(21) + 8.583) < 1e-3
COUNT += 1
# Section B Q2
zero_t(1 / S(t) - C(t) / S(t) - t)
same(sp.tan(sp.pi / 8), sp.sqrt(2) - 1)
same(sp.Integral(1 / sp.sin(x), (x, sp.pi / 3, sp.pi / 2)).evalf(30), sp.log(3) / 2)
# Section B Q3
zero_t(3 + 5 * C(t) - (8 - 2 * t ** 2) / (1 + t ** 2))
zero_t(1 / (3 + 5 * C(t)) * 2 / (1 + t ** 2) - 1 / (4 - t ** 2))
zero_t(1 / (4 - t ** 2) - (1 / (2 - t) + 1 / (2 + t)) / 4)
same(sp.Integral(1 / (3 + 5 * sp.cos(x)), (x, 0, sp.pi / 2)).evalf(30), sp.log(3) / 4)
# Section B Q4
zero_t(1 / (2 - S(t)) * 2 / (1 + t ** 2) - 1 / (t ** 2 - t + 1))
I4 = sp.Integral(1 / (2 - sp.sin(x)), (x, 0, sp.pi / 2)).evalf(30)
same(I4, 2 * sp.pi * sp.sqrt(3) / 9)
assert round(float(I4), 2) == 1.21
COUNT += 1
solved(lambda v: 2 - math.sin(v) - 2 * math.cos(v), 0, 2 * math.pi, [0.0, 2 * math.atan(0.5)])
has("2π√3/9", "¼ ln 3", "½ ln 3", "√2 − 1", "x = 0 or x = 2 arctan ½ = 0.927")

print(f"pc01 checks passed: {COUNT} assertions")
