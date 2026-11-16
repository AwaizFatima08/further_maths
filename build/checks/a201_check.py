"""Recomputes every number stated in content/a201.py and checks it appears in the unit text."""
import importlib
import math
import sys
from fractions import Fraction
from pathlib import Path

from scipy import integrate, optimize

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
MODULE = "a201"
UNIT = importlib.import_module(f"content.{MODULE}").UNIT


def _flat(o):
    if isinstance(o, str):
        return [o]
    if isinstance(o, dict):
        return [s for v in o.values() for s in _flat(v)]
    if isinstance(o, (list, tuple)):
        return [s for v in o for s in _flat(v)]
    return [str(o)]


TEXT = "\n".join(_flat(UNIT)).replace("−", "-")
COUNT = 0


def ok(value, stated, tol=None):
    """value rounds to the decimal string `stated`, and `stated` appears in the unit."""
    global COUNT
    s = stated.replace("−", "-")
    dec = len(s.split(".")[1]) if "." in s else 0
    tol = 0.5 * 10 ** (-dec) + 1e-9 if tol is None else tol
    assert abs(value - float(s)) <= tol, f"{stated}: computed {value}"
    assert s in TEXT, f"{stated!r} not found in {MODULE} text"
    COUNT += 1


def okf(value, stated):
    """value equals the fraction `stated` (e.g. '3/8') to 1e-9, and it appears in the unit."""
    global COUNT
    assert abs(value - float(Fraction(stated))) < 1e-9, f"{stated}: computed {value}"
    assert stated in TEXT, f"{stated!r} not found in {MODULE} text"
    COUNT += 1


def I(f, a, b):
    return integrate.quad(f, a, b, epsabs=1e-13, epsrel=1e-13)[0]


def root(f, a, b):
    return optimize.brentq(f, a, b, xtol=1e-14)


from scipy import stats

# Notes: skewness illustration, f = x/4 on [1, 3]
f = lambda x: x / 4
E = I(lambda x: x * f(x), 1, 3); E2 = I(lambda x: x * x * f(x), 1, 3); sd = math.sqrt(E2 - E * E)
okf(E, "13/6"); ok(E, "2.167"); ok(math.sqrt(5), "2.236"); okf(E2 - E * E, "11/36"); ok(sd, "0.553")
ok(3 * (E - math.sqrt(5)) / sd, "-0.377")

# WE1
F = lambda x: x ** 3 / 8
ok(F(1.5) - F(0.5), "0.40625"); ok(root(lambda x: F(x) - 0.75, 0, 2), "1.82")
# WE2
f = lambda x: x / 3 if x <= 2 else 2 / 3 * (3 - x)
assert abs(I(f, 0, 2) + I(f, 2, 3) - 1) < 1e-12
okf(I(f, 0, 2), "2/3")
for x in (2.2, 2.5, 2.9):
    assert abs(2 / 3 + I(f, 2, x) - (2 * x - x * x / 3 - 2)) < 1e-12
ok(math.sqrt(3), "1.73"); q3 = root(lambda x: 2 / 3 + I(f, 2, x) - 0.75, 2, 3); ok(q3, "2.13")
assert abs(q3 - (3 - math.sqrt(0.75))) < 1e-9
# WE3
F = lambda x: (x * x - 1) / 8
okf(1 - F(2), "5/8"); ok(math.sqrt(5), "2.24"); okf(I(lambda x: x * x / 4, 1, 3), "13/6"); ok(13 / 6, "2.17")
# WE4
W = stats.uniform(0, 12)
ok(W.mean(), "6"); ok(W.var(), "12"); ok(W.std(), "3.46"); ok(W.sf(9), "0.25")
B = stats.binom(5, 0.25)
ok(B.pmf(0), "0.2373", tol=5e-5); ok(B.pmf(1), "0.3955", tol=5e-5); ok(B.sf(1), "0.367")
# WE5: f = 2x, Y = X^3
h = lambda y: 2 / 3 * y ** (-1 / 3)
assert abs(I(h, 0, 1) - 1) < 1e-8
ok(0.5 ** 1.5, "0.354"); assert abs(0.5 ** 1.5 - (1 / math.sqrt(2)) ** 3) < 1e-12
okf(I(lambda x: x ** 3 * 2 * x, 0, 1), "2/5"); assert abs(I(lambda y: y * h(y), 0, 1) - 0.4) < 1e-8
# WE6: Y = 6/X
G = lambda y: 9 / 8 - 9 / (2 * y * y)
assert abs(G(2)) < 1e-12 and abs(G(6) - 1) < 1e-12
Fx = lambda x: (x * x - 1) / 8
for y in (2.5, 3.7, 5.5):
    assert abs(G(y) - (1 - Fx(6 / y))) < 1e-12
ok(I(lambda y: y * 9 / y ** 3, 2, 6), "3"); assert abs(I(lambda x: 6 / x * x / 4, 1, 3) - 3) < 1e-12

# Practice
ok(2.25 / 4 - 0.25 / 4, "0.5")
ok(0.5 ** (1 / 3), "0.794"); ok(0.9 ** (1 / 3), "0.965")
F = lambda x: x * x * (3 - x) / 4
ok(F(0.5), "0.15625"); ok(F(1), "0.5")
a, b = -0.25, 1.0
assert abs(4 * a + 2 * b - 1) < 1e-12 and abs(4 * a + b) < 1e-12
ok(root(lambda x: x - x * x / 4 - 0.5, 0, 2), "0.586")
f = lambda x: x / 8 if x <= 2 else 0.25
assert abs(I(f, 0, 2) + I(f, 2, 5) - 1) < 1e-12
F = lambda x: x * x / 16 if x <= 2 else (x - 1) / 4
for x in (2.5, 4.0):
    assert abs(F(x) - (I(f, 0, 2) + I(f, 2, x))) < 1e-12
okf(F(2), "1/4"); ok(root(lambda x: F(x) - 0.5, 2, 5), "3"); ok(F(3) - F(1), "0.4375")
U = stats.uniform(-2, 6); ok(U.mean(), "1"); ok(U.var(), "3"); okf(U.cdf(0), "1/3")
U = stats.uniform(2, 6); ok(U.mean(), "5"); ok(U.var(), "3"); ok(U.sf(6.5), "0.25")
U = stats.uniform(-0.5, 1); ok(U.std(), "0.289"); ok(U.cdf(-0.3) + U.sf(0.3), "0.4")
f = lambda x: 2 * (1 - x)
ok(I(lambda x: x * f(x), 0, 1), "0.333"); ok(1 - math.sqrt(0.5), "0.293")
h = lambda y: 1 / (4 * math.sqrt(y))
assert abs(I(h, 0, 4) - 1) < 1e-8
ok(1 - math.sqrt(1) / 2, "0.5"); okf(I(lambda y: y * h(y), 0, 4), "4/3")
ok(stats.uniform(0, 8).mean(), "4"); okf(stats.uniform(0, 8).var(), "16/3")
Fx = lambda x: x * x
for y in (0.1, 0.5, 0.9):
    assert abs(1 - Fx(math.sqrt(1 - y)) - y) < 1e-12

# Section B Q1
f = lambda x: 2 * x / 15 if x <= 3 else (5 - x) / 5
assert abs(I(f, 0, 3) + I(f, 3, 5) - 1) < 1e-12
ok(f(3), "0.4"); ok(I(f, 0, 3), "0.6")
F = lambda x: x * x / 15 if x <= 3 else x - x * x / 10 - 1.5
for x in (3.5, 4.5):
    assert abs(F(x) - (0.6 + I(f, 3, x))) < 1e-12
ok(root(lambda x: F(x) - 0.5, 0, 3), "2.74"); assert abs(root(lambda x: F(x) - 0.5, 0, 3) - math.sqrt(7.5)) < 1e-9
ok(root(lambda x: F(x) - 0.9, 3, 5), "4"); okf(F(2), "4/15"); ok(F(4), "0.9"); ok(F(4) - F(2), "0.633")
# Section B Q2
ok(stats.uniform(0, 10).sf(7.5), "0.25"); ok(stats.uniform(0, 10).cdf(7) - stats.uniform(0, 10).cdf(3), "0.4")
# Section B Q3
k = 1 / 26; okf(k, "1/26"); F = lambda x: (x ** 3 - 1) / 26
okf(1 - F(2), "19/26"); ok(1 - F(2), "0.731")
ok(root(lambda x: F(x) - 0.5, 1, 3), "2.41"); ok(root(lambda x: F(x) - 0.25, 1, 3), "1.96")
E = I(lambda x: x * 3 * x * x / 26, 1, 3); okf(E, "30/13"); ok(E, "2.31")
# Section B Q4
G = lambda a: (math.sqrt(a / math.pi) - 1) / 2
assert abs(G(math.pi)) < 1e-12 and abs(G(9 * math.pi) - 1) < 1e-12
g = lambda a: 1 / (4 * math.sqrt(math.pi * a))
assert abs(I(g, math.pi, 9 * math.pi) - 1) < 1e-9
ok(root(lambda a: G(a) - 0.5, math.pi, 9 * math.pi), "12.6"); ok(1 - G(20), "0.238")
EA = I(lambda a: a * g(a), math.pi, 9 * math.pi); ok(EA, "13.6"); assert abs(EA - 13 * math.pi / 3) < 1e-8

print(f"{MODULE}: all {COUNT} checks passed")
