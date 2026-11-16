"""SymPy/SciPy checks for Unit A14 (pure/pa14.py): every volume, mean value and numerical answer stated."""
import importlib
import sys
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from sympy import E, Rational as R, cos, exp, integrate, lambdify, log, nsimplify, pi, simplify, sin, sqrt, symbols, solve

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
UNIT = importlib.import_module("pure.pa14").UNIT


def _flat(o):
    if isinstance(o, str):
        return [o]
    if isinstance(o, dict):
        return [s for v in o.values() for s in _flat(v)]
    if isinstance(o, (list, tuple)):
        return [s for v in o for s in _flat(v)]
    return [str(o)]


TEXT = "\n".join(_flat(UNIT))
x, y, t, r, h = symbols("x y t r h", positive=True)
N = 0


def eq(a, b, msg):
    global N
    assert simplify(a - b) == 0, f"{msg}: {a} != {b}"
    N += 1


def num(f, a, b, exact, msg, var=x):
    """Check a definite integral numerically with scipy quad against the exact value."""
    global N
    g = lambdify(var, f, "numpy")
    v, _ = quad(g, float(a), float(b))
    assert abs(v - float(exact)) < 1e-8, f"{msg}: quad {v} vs {float(exact)}"
    N += 1


def dec(value, stated, msg):
    global N
    d = len(stated.split(".")[1]) if "." in stated else 0
    assert abs(float(value) - float(stated)) <= 0.5 * 10 ** (-d) + 1e-12, f"{msg}: {float(value)} vs {stated}"
    assert stated in TEXT, f"{stated} not in text ({msg})"
    N += 1


def has(s):
    global N
    assert s in TEXT, f"missing text: {s}"
    N += 1


# Worked example 1
V = pi * integrate((x**2 + 1) ** 2, (x, 0, 2)); eq(V, 206 * pi / 15, "WE1"); num(pi * (x**2 + 1) ** 2, 0, 2, V, "WE1 quad")
eq(R(32, 5) + R(16, 3) + 2, R(206, 15), "WE1 arithmetic"); dec(V.evalf(), "43.1", "WE1 dec"); has("206π/15")
# Worked example 2
Va = pi * integrate(exp(2 * y), (y, 0, 2)); eq(Va, pi * (E**4 - 1) / 2, "WE2a"); dec(Va.evalf(), "84.2", "WE2a dec")
num(pi * exp(2 * y), 0, 2, Va, "WE2a quad", y)
Vb = pi * E**2 - pi * integrate(exp(2 * y), (y, 0, 1)); eq(Vb, pi * (E**2 + 1) / 2, "WE2b"); dec(Vb.evalf(), "13.2", "WE2b dec")
eq(2 * pi * integrate(x * log(x), (x, 1, E)), Vb, "WE2b by shells")
# Worked example 3
xr = symbols("xr", real=True); assert set(solve(3 * xr - xr**2 - xr, xr)) == {0, 2}
V3 = pi * integrate((3 * x - x**2) ** 2 - x**2, (x, 0, 2)); eq(V3, 56 * pi / 15, "WE3"); dec(V3.evalf(), "11.7", "WE3 dec")
eq((3 * x - x**2) ** 2 - x**2, 8 * x**2 - 6 * x**3 + x**4, "WE3 expand")
num(pi * ((3 * x - x**2) ** 2 - x**2), 0, 2, V3, "WE3 quad")
# Worked example 4 (parametric ellipse)
V4 = pi * integrate((3 * sin(t)) ** 2 * (-4 * sin(t)), (t, pi / 2, 0)); eq(V4, 24 * pi, "WE4")
eq(integrate(sin(t) ** 3, (t, 0, pi / 2)), R(2, 3), "sin^3")
eq(pi * integrate(9 * (1 - x**2 / 16), (x, -4, 4)), 48 * pi, "ellipsoid Cartesian")
num(36 * pi * sin(t) ** 3, 0, np.pi / 2, V4, "WE4 quad", t)
# Worked example 5 (bowl)
V5 = pi * integrate(8 * y, (y, 0, 8)); eq(V5, 256 * pi, "WE5a"); dec(V5.evalf(), "804", "WE5a dec")
hh = solve(4 * pi * h**2 - 128 * pi, h); assert hh == [4 * sqrt(2)]; dec((4 * sqrt(2)).evalf(), "5.66", "WE5b")
# Worked example 6 (mean values)
m6 = integrate(x * (4 - x), (x, 0, 4)) / 4; eq(m6, R(8, 3), "WE6a"); eq(3 + 2 * m6, R(25, 3), "WE6b")
Tm = integrate(15 + 5 * sin(pi * t / 12), (t, 0, 12)) / 12; eq(Tm, 15 + 10 / pi, "WE6c"); dec(Tm.evalf(), "18.2", "WE6c dec")
num(15 + 5 * sin(pi * t / 12), 0, 12, Tm * 12, "WE6c quad", t)

# Section A
ans = [
    (pi * integrate((2 * x + 1) ** 2, (x, 0, 3)), 57 * pi),
    (pi * integrate(x**-2, (x, 1, 4)), 3 * pi / 4),
    (pi * integrate(y, (y, 0, 9)), 81 * pi / 2),
    (pi * integrate(exp(2 * x), (x, 0, 1)), pi * (E**2 - 1) / 2),
    (pi * integrate((r * x / h) ** 2, (x, 0, h)), pi * r**2 * h / 3),
    (pi * integrate(r**2 - x**2, (x, -r, r)), 4 * pi * r**3 / 3),
    (pi * integrate(4 * x**2 - x**4, (x, 0, 2)), 64 * pi / 15),
    (pi * integrate(y - y**2 / 4, (y, 0, 4)), 8 * pi / 3),
    (pi * integrate((t**2) ** 2 * 3 * t**2, (t, 0, 1)), 3 * pi / 7),
    (integrate(3 * x**2 - 2 * x, (x, 1, 3)) / 2, 9),
    (integrate(cos(x), (x, 0, pi / 2)) / (pi / 2), 2 / pi),
    (integrate(1 / x, (x, 1, E)) / (E - 1), 1 / (E - 1)),
]
for k, (a, b) in enumerate(ans, 1):
    eq(a, b, f"A{k}")
eq(5 - 2 * (2 / pi), 5 - 4 / pi, "A11b"); dec((1 / (E - 1)).evalf(), "0.582", "A12"); dec(exp(-1).evalf(), "0.368", "A12 1/e")
# Q8 by Cartesian: about y-axis, region between y = x^2 and y = 2x: outer x = sqrt(y), inner x = y/2
num(np.pi * (x - x**2 / 4), 0, 4, 8 * np.pi / 3, "A8 quad")
# Q9 Cartesian check: y = x^(2/3)
eq(pi * integrate(x ** R(4, 3), (x, 0, 1)), 3 * pi / 7, "A9 Cartesian")

# Section B1
assert set(solve(4 - xr**2 - (xr + 2), xr)) == {-2, 1}
f1 = (4 - x**2) ** 2 - (x + 2) ** 2
eq(f1, x**4 - 9 * x**2 - 4 * x + 12, "B1 integrand")
xs = symbols("xs", real=True)
F1 = xs**5 / 5 - 3 * xs**3 - 2 * xs**2 + 12 * xs
eq(F1.subs(xs, 1), R(36, 5), "B1 F(1)"); eq(F1.subs(xs, -2), -R(72, 5), "B1 F(-2)")
V1 = pi * integrate(f1.subs(x, xs), (xs, -2, 1)); eq(V1, 108 * pi / 5, "B1b"); num(np.pi * f1.subs(x, xs), -2, 1, V1, "B1b quad", xs)
m1 = integrate(4 - xs**2, (xs, -2, 1)) / 3; eq(m1, 3, "B1c")
# B2 vase
V2 = pi * integrate((2 + sin(y / 2)) ** 2, (y, 0, 2 * pi)); eq(V2, pi * (9 * pi + 16), "B2a")
dec(V2.evalf(), "139", "B2a dec"); num(np.pi * (2 + sin(y / 2)) ** 2, 0, 2 * np.pi, V2, "B2 quad", y)
m2 = integrate(2 + sin(y / 2), (y, 0, 2 * pi)) / (2 * pi); eq(m2, 2 + 2 / pi, "B2b"); dec(m2.evalf(), "2.64", "B2b dec")
# B3 parametric
xt, yt = t**2, t - t**3
eq(yt**2 - xt * (1 - xt) ** 2, 0, "B3a")
V3b = pi * integrate(yt**2 * 2 * t, (t, 0, 1)); eq(V3b, pi / 12, "B3b")
eq(pi * integrate(x * (1 - x) ** 2, (x, 0, 1)), pi / 12, "B3b Cartesian")
eq(integrate(sqrt(x) * (1 - x), (x, 0, 1)), R(4, 15), "B3c")
# B4 spherical cap
Vc = pi * integrate(r**2 - y**2, (y, r - h, r)); eq(Vc, pi * h**2 * (3 * r - h) / 3, "B4a")
Vw = (pi * h**2 * (30 - h) / 3).subs(h, 4); eq(Vw, 416 * pi / 3, "B4b"); dec(Vw.evalf(), "436", "B4b dec")
g = lambda hv: np.pi * hv**2 * (30 - hv) / 3 - 1000
hroot = brentq(g, 0.1, 10); dec(hroot, "6.36", "B4c")

print(f"pa14 checks passed: {N}")
