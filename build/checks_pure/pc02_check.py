"""Verifies every Taylor coefficient, limit, approximation and Leibnitz expansion stated in pure/pc02.py (C2)."""
import importlib
import math
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
MODULE = "pc02"
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
x, h, u = sp.symbols("x h u", real=True)
n = sp.symbols("n", integer=True, positive=True)
A = sp.symbols("a", real=True)


def taylor(f, a, order):
    """Taylor polynomial of f about a, up to (x − a)^order, as an expression in x."""
    return sp.series(f.subs(x, a + h), h, 0, order + 1).removeO().subs(h, x - a)


def same_poly(p, q):
    global COUNT
    assert sp.simplify(sp.expand(p - q)) == 0, (p, q)
    COUNT += 1


def lim(f, point, val, direction="+-"):
    global COUNT
    if point in (sp.oo, -sp.oo) or direction != "+-":
        L = sp.limit(f, x, point, dir=direction if direction != "+-" else "+")
    else:
        L = sp.limit(f, x, point)
    assert sp.simplify(L - val) == 0, (f, L, val)
    COUNT += 1


def has(*snips):
    global COUNT
    for s in snips:
        assert s in TEXT, f"{s!r} not found in {MODULE}"
        COUNT += 1


# 2.1 Taylor coefficients f^(r)(a)/r! (general check on a polynomial-like function)
g = sp.exp(2 * x) * sp.cos(x)
same_poly(taylor(g, 1, 4), sum(sp.diff(g, x, r).subs(x, 1) / sp.factorial(r) * (x - 1) ** r for r in range(5)))

# Worked example 1
same_poly(taylor(sp.sin(x), sp.pi, 3), -(x - sp.pi) + (x - sp.pi) ** 3 / 6)
# Worked example 2
T2 = sp.log(2) + (x - 2) / 2 - (x - 2) ** 2 / 8 + (x - 2) ** 3 / 24
same_poly(taylor(sp.log(x), 2, 3), T2)
est = float(T2.subs(x, sp.Rational(21, 10)))
assert f"{est:.6f}" == "0.741939" and f"{math.log(2.1):.6f}" == "0.741937"
assert abs(est - math.log(2.1) - 2e-6) < 5e-7
COUNT += 1
has("0.741939", "0.741937")

# 2.2 table and text limits
lim((sp.sin(x) - x) / x ** 3, 0, -sp.Rational(1, 6))
for f, v in ((sp.sin(x) / x, 1), ((1 - sp.cos(x)) / x ** 2, sp.Rational(1, 2)), ((sp.exp(x) - 1) / x, 1),
             ((sp.exp(x) - 1 - x) / x ** 2, sp.Rational(1, 2)), ((sp.log(1 + x) - x) / x ** 2, -sp.Rational(1, 2)),
             ((sp.tan(x) - x) / x ** 3, sp.Rational(1, 3))):
    lim(f, 0, v)
same_poly(sp.series(sp.tan(x), x, 0, 6).removeO(), x + x ** 3 / 3 + 2 * x ** 5 / 15)
# 2.3 other forms
lim(x * sp.log(x), 0, 0, "+")
lim((1 + A / x) ** x, sp.oo, sp.exp(A))
for k in (sp.Rational(1, 2), 3):
    lim(x ** k * sp.exp(-x), sp.oo, 0)
    lim(x ** k * sp.log(x), 0, 0, "+")
# 2.4 Leibnitz example x² eˣ
same_poly(sp.diff(x ** 2 * sp.exp(x), x, 7), sp.exp(x) * (x ** 2 + 14 * x + 42))
for nv in (3, 5, 8):
    same_poly(sp.diff(x ** 2 * sp.exp(x), x, nv), sp.exp(x) * (x ** 2 + 2 * nv * x + nv * (nv - 1)))

# Worked example 3
lim((x * sp.cos(x) - sp.sin(x)) / x ** 3, 0, -sp.Rational(1, 3))
lim((sp.exp(2 * x) - 1 - 2 * x) / (x * sp.sin(x)), 0, 2)
same_poly(sp.series(sp.exp(2 * x), x, 0, 4).removeO(), 1 + 2 * x + 2 * x ** 2 + sp.Rational(4, 3) * x ** 3)
# Worked example 4
lim((1 - sp.cos(2 * x)) / x ** 2, 0, 2)
lim(x ** 2 / sp.exp(x), sp.oo, 0)
# Worked example 5
lim(sp.log(1 + A * x) / x, 0, A)
lim((1 + 3 * x) ** (1 / x), 0, sp.exp(3), "+")
lim((1 + 3 * x) ** (1 / x), 0, sp.exp(3), "-")
# Worked example 6
y = sp.exp(sp.asin(x))
assert sp.simplify((1 - x ** 2) * sp.diff(y, x, 2) - x * sp.diff(y, x) - y) == 0
COUNT += 1
for nv in range(0, 5):
    e = (1 - x ** 2) * sp.diff(y, x, nv + 2) - (2 * nv + 1) * x * sp.diff(y, x, nv + 1) - (nv ** 2 + 1) * sp.diff(y, x, nv)
    assert abs(sp.N(e.subs(x, sp.Rational(3, 10)))) < 1e-20
COUNT += 1
same_poly(sp.series(y, x, 0, 6).removeO(),
          1 + x + x ** 2 / 2 + x ** 3 / 3 + sp.Rational(5, 24) * x ** 4 + x ** 5 / 6)
assert [sp.diff(y, x, k).subs(x, 0) for k in range(6)] == [1, 1, 1, 2, 5, 20]
COUNT += 1

# Practice
same_poly(taylor(sp.exp(x), 1, 3), sp.E * (1 + (x - 1) + (x - 1) ** 2 / 2 + (x - 1) ** 3 / 6))
same_poly(taylor(sp.cos(x), sp.pi / 3, 2), sp.Rational(1, 2) - sp.sqrt(3) / 2 * (x - sp.pi / 3) - (x - sp.pi / 3) ** 2 / 4)
T3 = 2 + (x - 4) / 4 - (x - 4) ** 2 / 64
same_poly(taylor(sp.sqrt(x), 4, 2), T3)
assert T3.subs(x, sp.Rational(42, 10)) == sp.Rational(2049375, 1000000)
assert f"{math.sqrt(4.2):.7f}" == "2.0493902" and abs(math.sqrt(4.2) - 2.049375 - 1.5e-5) < 1e-6
COUNT += 1
same_poly(taylor(sp.tan(x), sp.pi / 4, 2), 1 + 2 * (x - sp.pi / 4) + 2 * (x - sp.pi / 4) ** 2)
same_poly(sp.series(sp.log(3 + x), x, 0, 4).removeO(), sp.log(3) + x / 3 - x ** 2 / 18 + x ** 3 / 81)
lim((1 - sp.cos(x)) / x ** 2, 0, sp.Rational(1, 2))
lim((sp.exp(x) - 1 - x) / x ** 2, 0, sp.Rational(1, 2))
lim((sp.log(1 + x) - x) / x ** 2, 0, -sp.Rational(1, 2))
lim((sp.tan(x) - x) / x ** 3, 0, sp.Rational(1, 3))
lim(sp.log(x) / (x - 1), 1, 1)
lim((sp.exp(x) - sp.exp(-x)) / sp.sin(x), 0, 2)
lim(sp.log(x) / sp.sqrt(x), sp.oo, 0)
lim(x ** 2 * sp.log(x), 0, 0, "+")
lim(x ** x, 0, 1, "+")
lim((1 + 2 / x) ** (3 * x), sp.oo, sp.exp(6))
same_poly(sp.diff(x ** 3 * sp.exp(2 * x), x, 4), sp.exp(2 * x) * (16 * x ** 3 + 96 * x ** 2 + 144 * x + 48))
for nv in (1, 4, 9):
    same_poly(sp.diff(x * sp.exp(x), x, nv), (x + nv) * sp.exp(x))
has("2.049375", "e²ˣ(16x³ + 96x² + 144x + 48)", "e⁶")

# Section B Q1
f = sp.tan(x)
assert sp.simplify(sp.diff(f, x, 2) - 2 / sp.cos(x) ** 2 * sp.tan(x)) == 0
assert sp.simplify(sp.diff(f, x, 3) - (2 / sp.cos(x) ** 4 + 4 / sp.cos(x) ** 2 * sp.tan(x) ** 2)) == 0
COUNT += 2
TB1 = 1 + 2 * (x - sp.pi / 4) + 2 * (x - sp.pi / 4) ** 2 + sp.Rational(8, 3) * (x - sp.pi / 4) ** 3
same_poly(taylor(f, sp.pi / 4, 3), TB1)
estB = float(TB1.subs(x, sp.Rational(4, 5)))
assert f"{estB:.4f}" == "1.0296" and f"{math.tan(0.8):.7f}" == "1.0296386" and f"{0.8 - math.pi / 4:.7f}" == "0.0146018"
COUNT += 1
# Section B Q2
lim((sp.exp(x) - 1 - sp.sin(x)) / x ** 2, 0, sp.Rational(1, 2))
lim((sp.cosh(x) - sp.cos(x)) / x ** 2, 0, 1)
lim((1 - 3 / x) ** (2 * x), sp.oo, sp.exp(-6))
# Section B Q3
for nv in range(2, 11):
    same_poly(sp.diff(x ** 2 * sp.exp(2 * x), x, nv),
              2 ** (nv - 2) * sp.exp(2 * x) * (4 * x ** 2 + 4 * nv * x + nv * (nv - 1)))
assert sp.diff(x ** 2 * sp.exp(2 * x), x, 10).subs(x, 0) == 23040 == 2 ** 8 * 90
COUNT += 1
same_poly(sp.diff(x ** 2 * sp.exp(2 * x), x, 2), sp.exp(2 * x) * (4 * x ** 2 + 8 * x + 2))
# Section B Q4
y = sp.asin(x) ** 2
assert sp.simplify((1 - x ** 2) * sp.diff(y, x, 2) - x * sp.diff(y, x) - 2) == 0
COUNT += 1
for nv in range(1, 6):
    e = (1 - x ** 2) * sp.diff(y, x, nv + 2) - (2 * nv + 1) * x * sp.diff(y, x, nv + 1) - nv ** 2 * sp.diff(y, x, nv)
    assert abs(sp.N(e.subs(x, sp.Rational(2, 5)))) < 1e-20
COUNT += 1
same_poly(sp.series(y, x, 0, 7).removeO(), x ** 2 + x ** 4 / 3 + sp.Rational(8, 45) * x ** 6)
assert [sp.limit(sp.diff(y, x, k), x, 0) for k in (2, 4, 6)] == [2, 8, 128]
COUNT += 1
has("x² + x⁴/3 + 8x⁶/45", "23040", "e⁻⁶", "1.0296")

print(f"pc02 checks passed: {COUNT} assertions")
