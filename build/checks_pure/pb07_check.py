"""SymPy/SciPy checks for Unit B7 (pure/pb07.py): improper integrals (limits), standard limits, bounds and limits of sums."""
import importlib
import sys
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from sympy import (E, Rational as R, atan, cbrt, diff, exp, integrate, lambdify, limit, log, oo, pi, simplify, sqrt, symbols,
                   asin, Sum, harmonic, apart, Integral)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
UNIT = importlib.import_module("pure.pb07").UNIT


def _flat(o):
    if isinstance(o, str):
        return [o]
    if isinstance(o, dict):
        return [s for v in o.values() for s in _flat(v)]
    if isinstance(o, (list, tuple)):
        return [s for v in o for s in _flat(v)]
    return [str(o)]


TEXT = "\n".join(_flat(UNIT))
x = symbols("x", positive=True)
t, s, k = symbols("t s k", positive=True)
n = symbols("n", positive=True, integer=True)
N = 0


def eq(a, b, msg):
    global N
    assert simplify(a - b) == 0, f"{msg}: {simplify(a - b)}"
    N += 1


def conv(f, lo, hi, exact, msg, points=None):
    """Improper integral: SymPy value and SciPy quad (handles infinite ranges and endpoint singularities)."""
    global N
    v = integrate(f, (x, lo, hi))
    if not v.has(Integral):  # SymPy sometimes cannot do these; the antiderivative + limit is then checked separately
        assert simplify(v - exact) == 0, f"{msg}: sympy {v} vs {exact}"
    g = lambdify(x, f, "numpy")
    q, _ = quad(g, float(lo), float(hi) if hi != oo else np.inf, points=points, limit=200)
    assert abs(q - float(exact)) < 1e-6, f"{msg}: quad {q} vs {float(exact)}"
    N += 1


def div(f, lo, hi, msg):
    global N
    v = integrate(f, (x, lo, hi))
    assert v in (oo, -oo) or v.has(oo), f"{msg}: expected divergence, got {v}"
    N += 1


def dec(value, stated, msg):
    global N
    d = len(stated.split(".")[1]) if "." in stated else 0
    assert abs(float(value) - float(stated)) <= 0.5 * 10 ** (-d) + 1e-12, f"{msg}: {float(value)} vs {stated}"
    assert stated in TEXT, f"{stated} not in text ({msg})"
    N += 1


# B7.2 / B7.3 notes
conv(1 / x**2, 1, oo, 1, "1/x^2"); div(1 / x, 1, oo, "1/x diverges")
for p in [R(3, 2), 2, 3]:
    conv(x**-p, 1, oo, 1 / (p - 1), f"x^-{p} on [1,oo)")
for p in [R(1, 3), R(1, 2), R(2, 3)]:
    conv(x**-p, 0, 1, 1 / (1 - p), f"x^-{p} on (0,1]")
div(x ** -R(1, 2), 1, oo, "p=1/2 infinite"); div(1 / x**2, 0, 1, "p=2 at 0")
conv(exp(-x), 0, oo, 1, "e^-x"); conv(1 / (1 + x**2), 0, oo, pi / 2, "arctan")
conv(1 / sqrt(x), 0, 2, 2 * sqrt(2), "1/sqrt x"); div(1 / x, 0, 1, "1/x at 0")
xr = symbols("xr", real=True)
eq((-1 / xr).subs(xr, 1) - (-1 / xr).subs(xr, -1), -2, "naive -2")
assert integrate(1 / xr**2, (xr, 0, 1)) == oo; N += 1
# B7.4 standard limits
for kk in [R(1, 2), 1, 2, 5]:
    assert limit(x**kk * exp(-x), x, oo) == 0 and limit(x**kk * log(x), x, 0, "+") == 0; N += 1
    assert limit(log(x) / x**kk, x, oo) == 0; N += 1
eq(integrate(x * exp(-x), (x, 0, t)), 1 - t * exp(-t) - exp(-t), "xe^-x partial"); conv(x * exp(-x), 0, oo, 1, "xe^-x")
eq(integrate(log(x), (x, t, 1)), -1 - t * log(t) + t, "ln partial"); conv(log(x), 0, 1, -1, "ln x")
# u-substitution for second limit
u = symbols("u", positive=True)
eq((x**k * log(x)).subs(x, exp(-u)), -u * exp(-k * u), "x = e^-u")
# B7.5 rectangle inequality example and million
for nn in [2, 10, 1000]:
    H = float(harmonic(nn)); assert np.log(nn + 1) < H < 1 + np.log(nn); N += 1
assert float(np.sum(1.0 / np.arange(1, 10**6 + 1))) < 1 + np.log(10**6) < 15; N += 1
# B7.6 limit of sum example
eq(integrate(1 / (1 + x), (x, 0, 1)), log(2), "ln 2 limit")
assert abs(sum(1 / (2000 + r) for r in range(1, 2001)) - np.log(2)) < 2e-4; N += 1
# B7.7 sqrt bounds
lo7 = float(integrate(sqrt(x), (x, 0, 100))); hi7 = float(integrate(sqrt(x), (x, 1, 101)))
true7 = sum(np.sqrt(r) for r in range(1, 101))
dec(lo7, "666.7", "B7.7 lower"); dec(hi7, "676.0", "B7.7 upper"); dec(true7, "671.5", "B7.7 true"); assert lo7 < true7 < hi7

# Worked example 1
eq(apart(1 / (xr**2 - 1), xr), (1 / (xr - 1) - 1 / (xr + 1)) / 2, "WE1 pf")
F = log((x - 1) / (x + 1)) / 2
eq(diff(F, x), 1 / (x**2 - 1), "WE1 antiderivative")
eq(limit(F.subs(x, t), t, oo) - F.subs(x, 2), log(3) / 2, "WE1a")
q, _ = quad(lambda v: 1 / (v * v - 1), 2, np.inf); assert abs(q - np.log(3) / 2) < 1e-9; N += 1
div(x ** -R(1, 2), 1, oo, "WE1b")
# Worked example 2
conv(x / sqrt(4 - x**2), 0, 2, 2, "WE2a")
g2 = lambda v: 1 / np.cbrt((v - 1) ** 2)
q1, _ = quad(g2, 0, 1); q2, _ = quad(g2, 1, 3)
exact2 = 3 + 3 * 2 ** (1 / 3)
assert abs(q1 - 3) < 1e-6 and abs(q2 - 3 * 2 ** (1 / 3)) < 1e-6; N += 1
dec(exact2, "6.78", "WE2b")
eq(diff(3 * (x - 1) ** R(1, 3), x), (x - 1) ** R(-2, 3), "WE2b antiderivative")
# Worked example 3
G = -x * exp(-2 * x) / 2 - exp(-2 * x) / 4
eq(diff(G, x), x * exp(-2 * x), "WE3 antiderivative")
eq(G.subs(x, t) - G.subs(x, 0), -t * exp(-2 * t) / 2 - exp(-2 * t) / 4 + R(1, 4), "WE3 partial")
conv(x * exp(-2 * x), 0, oo, R(1, 4), "WE3")
# Worked example 4
H4 = x**2 * log(x) / 2 - x**2 / 4
eq(diff(H4, x), x * log(x), "WE4 antiderivative"); conv(x * log(x), 0, 1, -R(1, 4), "WE4")
assert limit(t**2 * log(t), t, 0, "+") == 0; N += 1
# Worked example 5
dec(np.log(1001), "6.909", "WE5 lower"); dec(1 + np.log(1000), "7.908", "WE5 upper"); dec(float(harmonic(1000)), "7.485", "WE5 true")
# Worked example 6
r = symbols("r", positive=True, integer=True)
eq(n / (n**2 + r**2) - (1 / n) / (1 + (r / n) ** 2), 0, "WE6 rewrite")
eq(integrate(1 / (1 + x**2), (x, 0, 1)), pi / 4, "WE6")
s100 = sum(100 / (100**2 + rr**2) for rr in range(1, 101))
dec(s100, "0.78289", "WE6 n=100"); dec(np.pi / 4, "0.78540", "WE6 pi/4")

# Section A
conv(x**-3, 1, oo, R(1, 2), "A1"); conv(exp(-3 * x), 0, oo, R(1, 3), "A2")
div(x ** -R(1, 2), 1, oo, "A3a"); conv(x ** -R(3, 2), 1, oo, 2, "A3b")
conv(x ** -R(1, 2), 0, 9, 6, "A4"); conv(x ** -R(1, 3), 0, 1, R(3, 2), "A5")
conv(1 / (4 + x**2), 0, oo, pi / 4, "A6"); conv(1 / sqrt(1 - x**2), 0, 1, pi / 2, "A7")
assert integrate(xr**-3, (xr, 0, 1)) == oo; eq(integrate(x**-3, (x, t, 1)), (1 / t**2 - 1) / 2, "A8 partial")
conv(x * exp(-x), 0, oo, 1, "A9"); conv(log(x), 0, 1, -1, "A10")
eq(diff(-log(x) / x - 1 / x, x), log(x) / x**2, "A11 antiderivative"); conv(log(x) / x**2, 1, oo, 1, "A11")
assert limit(log(t) / t, t, oo) == 0; N += 1
eq(integrate(x**2, (x, 0, 1)), R(1, 3), "A12a"); eq(integrate(1 / (1 + x), (x, 0, 1)), log(2), "A12b")
eq(limit(Sum(r**2, (r, 1, n)).doit() / n**3, n, oo), R(1, 3), "A12a limit")

# Section B1
eq(apart(1 / (xr * (xr + 2)), xr), (1 / xr - 1 / (xr + 2)) / 2, "B1a")
F1 = log(x / (x + 2)) / 2
eq(diff(F1, x), 1 / (x * (x + 2)), "B1 anti"); eq(limit(F1.subs(x, t), t, oo) - F1.subs(x, 1), log(3) / 2, "B1b")
conv(1 / (x * (x + 2)), 1, oo, log(3) / 2, "B1b quad"); div(1 / (x + 2), 1, oo, "B1c")
# B2
eq(integrate(x**2 * exp(-x), (x, 0, t)), 2 - (t**2 + 2 * t + 2) * exp(-t), "B2a")
conv(x**2 * exp(-x), 0, oo, 2, "B2b")
# B3
F3 = R(2, 3) * x ** R(3, 2) * log(x) - R(4, 9) * x ** R(3, 2)
eq(diff(F3, x), sqrt(x) * log(x), "B3b anti"); eq(F3.subs(x, 1) - limit(F3.subs(x, t), t, 0, "+"), -R(4, 9), "B3b limit"); conv(sqrt(x) * log(x), 0, 1, -R(4, 9), "B3b")
F3c = 2 * sqrt(x) * log(x) - 4 * sqrt(x)
eq(diff(F3c, x), log(x) / sqrt(x), "B3c anti"); eq(F3c.subs(x, 1) - limit(F3c.subs(x, t), t, 0, "+"), -4, "B3c limit"); conv(log(x) / sqrt(x), 0, 1, -4, "B3c")
assert limit(t ** R(3, 2) * log(t), t, 0, "+") == 0 and limit(sqrt(t) * log(t), t, 0, "+") == 0; N += 1
# B4
for nn in [2, 5, 50, 10000]:
    S = sum(1 / np.sqrt(rr) for rr in range(1, nn + 1))
    assert 2 * np.sqrt(nn + 1) - 2 < S < 2 * np.sqrt(nn) - 1; N += 1
dec(2 * np.sqrt(10001) - 2, "198.01", "B4b lower"); dec(2 * np.sqrt(10000) - 1, "199.00", "B4b upper")
dec(sum(1 / np.sqrt(rr) for rr in range(1, 10001)), "198.54", "B4b true")
conv(x ** -R(1, 2), 0, 1, 2, "B4c")
assert abs(sum(1 / np.sqrt(rr) for rr in range(1, 10**6 + 1)) / 1000 - 2) < 2e-3; N += 1

print(f"pb07 checks passed: {N}")
