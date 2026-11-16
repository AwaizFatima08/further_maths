"""SymPy/SciPy checks for Unit B13 (pure/pb13.py): reduction formulae (several n), arc lengths and surface areas."""
import importlib
import sys
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from sympy import (E, Rational as R, cos, cosh, diff, exp, expand, integrate, lambdify, log, pi, sec, simplify, sin, sinh,
                   sqrt, symbols, tan, trigsimp)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
UNIT = importlib.import_module("pure.pb13").UNIT


def _flat(o):
    if isinstance(o, str):
        return [o]
    if isinstance(o, dict):
        return [s for v in o.values() for s in _flat(v)]
    if isinstance(o, (list, tuple)):
        return [s for v in o for s in _flat(v)]
    return [str(o)]


TEXT = "\n".join(_flat(UNIT))
x, t, th, w = symbols("x t theta w", real=True)
a = symbols("a", positive=True)
N = 0


def eq(p, q, msg):
    global N
    assert simplify(p - q) == 0, f"{msg}: {simplify(p - q)}"
    N += 1


def num(f, lo, hi, exact, msg, var=x):
    global N
    v, _ = quad(lambdify(var, f, "numpy"), float(lo), float(hi), limit=200)
    assert abs(v - float(exact)) < 1e-8, f"{msg}: quad {v} vs {float(exact)}"
    N += 1


def dec(value, stated, msg):
    global N
    d = len(stated.split(".")[1]) if "." in stated else 0
    assert abs(float(value) - float(stated)) <= 0.5 * 10 ** (-d) + 1e-12, f"{msg}: {float(value)} vs {stated}"
    assert stated in TEXT, f"{stated} not in text ({msg})"
    N += 1


def Iq(f, lo, hi):
    return quad(lambdify(x, f, "numpy"), float(lo), float(hi), limit=200)[0]


# ---- Reduction formulae: check the formula numerically for several n, and the stated values ----
# x^n e^x on [0,1]: I_n = e - n I_{n-1}
I = lambda m: Iq(x**m * exp(x), 0, 1)
for m in range(1, 8):
    assert abs(I(m) - (np.e - m * I(m - 1))) < 1e-10; N += 1
vals = [E - 1]
for m in range(1, 4):
    vals.append(E - m * vals[-1])
eq(vals[1], 1, "I1"); eq(vals[2], E - 2, "I2"); eq(vals[3], 6 - 2 * E, "I3"); dec(float(6 - 2 * E), "0.563", "I3 dec")
eq(integrate(x**3 * exp(x), (x, 0, 1)), 6 - 2 * E, "I3 direct")
# Wallis sin^n and cos^n
for f in (sin, cos):
    for m in range(2, 10):
        assert abs(m * Iq(f(x) ** m, 0, np.pi / 2) - (m - 1) * Iq(f(x) ** (m - 2), 0, np.pi / 2)) < 1e-10; N += 1
eq(integrate(sin(x) ** 6, (x, 0, pi / 2)), 5 * pi / 32, "sin^6"); eq(integrate(sin(x) ** 5, (x, 0, pi / 2)), R(8, 15), "sin^5")
eq(integrate(cos(x) ** 4, (x, 0, pi / 2)), 3 * pi / 16, "A2 cos^4"); eq(integrate(cos(x) ** 3, (x, 0, pi / 2)), R(2, 3), "A2 cos^3")
eq(diff(-cos(x) * sin(x) ** 4, x) - (sin(x) ** 5 - 4 * sin(x) ** 3 * cos(x) ** 2), 0, "Wallis by parts (n=5)")
# tan^n on [0, pi/4]
for m in range(2, 9):
    assert abs(Iq(tan(x) ** m, 0, np.pi / 4) + Iq(tan(x) ** (m - 2), 0, np.pi / 4) - 1 / (m - 1)) < 1e-10; N += 1
eq(integrate(tan(x), (x, 0, pi / 4)), log(2) / 2, "tan I1")
I5 = log(2) / 2 - R(1, 4); num(tan(x) ** 5, 0, pi / 4, I5, "tan^5"); dec(float(I5), "0.0966", "tan^5 dec")
# CAIE e^-x (1-x)^n
J = lambda m: Iq(exp(-x) * (1 - x) ** m, 0, 1)
for m in range(1, 8):
    assert abs(J(m) - (1 - m * J(m - 1))) < 1e-10; N += 1
eq(integrate(exp(-x) * (1 - x) ** 3, (x, 0, 1)), 6 / E - 2, "A4 I3")
eq(integrate(exp(-x), (x, 0, 1)), 1 - 1 / E, "A4 I0"); eq(integrate(exp(-x) * (1 - x), (x, 0, 1)), 1 / E, "A4 I1")
eq(integrate(exp(-x) * (1 - x) ** 2, (x, 0, 1)), 1 - 2 / E, "A4 I2")
# A1: x^n e^{2x}
for m in range(1, 5):
    lhs = integrate(x**m * exp(2 * x), x); rhs = x**m * exp(2 * x) / 2 - R(m, 2) * integrate(x ** (m - 1) * exp(2 * x), x)
    eq(diff(lhs - rhs, x), 0, f"A1 n={m}")
eq(diff(exp(2 * x) * (x**2 / 2 - x / 2 + R(1, 4)), x), x**2 * exp(2 * x), "A1 I2")
# A3: (ln x)^n on [1, e]
L = lambda m: Iq(log(x) ** m, 1, np.e)
for m in range(1, 7):
    assert abs(L(m) - (np.e - m * L(m - 1))) < 1e-10; N += 1
eq(integrate(log(x) ** 3, (x, 1, E)), 6 - 2 * E, "A3 I3")
# A5: x^n cos x on [0, pi/2]
K = lambda m: Iq(x**m * cos(x), 0, np.pi / 2)
for m in range(2, 8):
    assert abs(K(m) - ((np.pi / 2) ** m - m * (m - 1) * K(m - 2))) < 1e-9; N += 1
eq(integrate(x**2 * cos(x), (x, 0, pi / 2)), pi**2 / 4 - 2, "A5 I2")
eq(integrate(x**4 * cos(x), (x, 0, pi / 2)), pi**4 / 16 - 3 * pi**2 + 24, "A5 I4")
# B1: sec^n
n = symbols("n", positive=True)
eq(trigsimp(diff(tan(x) * sec(x) ** (n - 2), x) - ((n - 1) * sec(x) ** n - (n - 2) * sec(x) ** (n - 2))), 0, "B1a")
S_ = lambda m: Iq(sec(x) ** m, 0, np.pi / 4)
for m in range(2, 9):
    assert abs((m - 1) * S_(m) - (np.sqrt(2) ** (m - 2) + (m - 2) * S_(m - 2))) < 1e-10; N += 1
eq(integrate(sec(x) ** 2, (x, 0, pi / 4)), 1, "B1 I2"); num(sec(x) ** 4, 0, pi / 4, R(4, 3), "B1 I4")
num(sec(x), 0, pi / 4, log(1 + sqrt(2)), "B1 I1"); num(sec(x) ** 3, 0, pi / 4, sqrt(2) / 2 + log(1 + sqrt(2)) / 2, "B1 I3")
# B2: sin(nx)/sin x
m_ = symbols("m", integer=True)
eq(expand((sin((m_ + 2) * x) - sin(m_ * x) - 2 * cos((m_ + 1) * x) * sin(x)).rewrite(exp)), 0, "B2a")
Jn = lambda m, up: Iq(sin(m * x) / sin(x), 1e-12, up)
for m in [1, 2, 3, 4, 5, 6]:
    assert abs(Jn(m + 2, np.pi / 4) - Jn(m, np.pi / 4) - 2 / (m + 1) * np.sin((m + 1) * np.pi / 4)) < 1e-8; N += 1
assert abs(Jn(7, np.pi / 4) - (np.pi / 4 + 2 / 3)) < 1e-8; N += 1
assert abs(Jn(3, np.pi / 4) - (np.pi / 4 + 1)) < 1e-8 and abs(Jn(5, np.pi / 4) - (np.pi / 4 + 1)) < 1e-8; N += 1
for m in [1, 3, 5, 7, 9, 11]:
    assert abs(Jn(m, np.pi / 2) - np.pi / 2) < 1e-8; N += 1


# ---- Arc length and surface area ----
def arc(y, lo, hi):
    return sqrt(1 + diff(y, x) ** 2)


# Worked example 4
y4 = x**2 / 4 - log(x) / 2
eq(1 + diff(y4, x) ** 2 - (x / 2 + 1 / (2 * x)) ** 2, 0, "WE4 square")
eq(integrate(x / 2 + 1 / (2 * x), (x, 1, E)), (E**2 + 1) / 4, "WE4"); num(arc(y4, 1, np.e), 1, np.e, (E**2 + 1) / 4, "WE4 quad")
dec(float((E**2 + 1) / 4), "2.10", "WE4 dec")
# Worked example 5 cycloid
X, Y = t - sin(t), 1 - cos(t)
eq(diff(X, t) ** 2 + diff(Y, t) ** 2 - 4 * sin(t / 2) ** 2, 0, "WE5 ds")
eq(integrate(2 * sin(t / 2), (t, 0, 2 * pi)), 8, "WE5a")
num(sqrt(diff(X, t) ** 2 + diff(Y, t) ** 2), 0, 2 * pi, 8, "WE5a quad", t)
eq(2 * integrate(sin(w) ** 3, (w, 0, pi)), R(8, 3), "WE5 sin^3")
Scyc = 2 * pi * integrate(Y * 2 * sin(t / 2), (t, 0, 2 * pi)); eq(Scyc, 64 * pi / 3, "WE5b")
num(2 * pi * Y * sqrt(diff(X, t) ** 2 + diff(Y, t) ** 2), 0, 2 * pi, 64 * pi / 3, "WE5b quad", t)
dec(float(64 * pi / 3), "67.0", "WE5b dec")
# Worked example 6 cardioid (a = 1 numerically, symbolic a in identities)
r = a * (1 + cos(th))
eq(r**2 + diff(r, th) ** 2 - 4 * a**2 * cos(th / 2) ** 2, 0, "WE6 ds")
eq(2 * integrate(2 * a * cos(th / 2), (th, 0, pi)), 8 * a, "WE6a")
r1 = 1 + cos(th)
num(sqrt(r1**2 + diff(r1, th) ** 2), 0, 2 * pi, 8, "WE6a quad", th)
eq(r * sin(th) * 2 * a * cos(th / 2) - 8 * a**2 * cos(th / 2) ** 4 * sin(th / 2), 0, "WE6 integrand")
eq(integrate(8 * a**2 * cos(th / 2) ** 4 * sin(th / 2), (th, 0, pi)), 16 * a**2 / 5, "WE6 integral")
num(2 * pi * r1 * sin(th) * sqrt(r1**2 + diff(r1, th) ** 2), 0, pi, 32 * pi / 5, "WE6b quad", th)

# Section A arcs and surfaces
num(arc(R(2, 3) * x ** R(3, 2), 0, 3), 0, 3, R(14, 3), "A6")
num(arc(log(cos(x)), 0, pi / 4), 0, pi / 4, log(sqrt(2) + 1), "A7")
num(arc(cosh(x), 0, log(2)), 0, log(2), R(3, 4), "A8"); eq(sinh(log(2)).rewrite(exp), R(3, 4), "A8 exact")
Xa, Ya = t**2, R(2, 3) * t**3
num(sqrt(diff(Xa, t) ** 2 + diff(Ya, t) ** 2), 0, 2 * sqrt(2), R(52, 3), "A9", t)
Xs, Ys = cos(t) ** 3, sin(t) ** 3
eq(diff(Xs, t) ** 2 + diff(Ys, t) ** 2 - 9 * sin(t) ** 2 * cos(t) ** 2, 0, "A10 ds")
num(sqrt(diff(Xs, t) ** 2 + diff(Ys, t) ** 2), 0, 2 * pi, 6, "A10a", t)
num(2 * pi * Ys * sqrt(diff(Xs, t) ** 2 + diff(Ys, t) ** 2), 0, pi / 2, 6 * pi / 5, "A10b", t)
num(2 * pi * sqrt(x) * arc(sqrt(x), 0, 2), 0, 2, 13 * pi / 3, "A11")
re = exp(th)
num(sqrt(re**2 + diff(re, th) ** 2), 0, pi, sqrt(2) * (exp(pi) - 1), "A12", th); dec(float(sqrt(2) * (exp(pi) - 1)), "31.3", "A12 dec")

# Section B3
y3 = x**2 / 8 - log(x)
eq(1 + diff(y3, x) ** 2 - (x / 4 + 1 / x) ** 2, 0, "B3a square")
num(arc(y3, 1, 4), 1, 4, R(15, 8) + 2 * log(2), "B3a")
num(2 * pi * 2 * sqrt(x) * arc(2 * sqrt(x), 0, 3), 1e-12, 3, 56 * pi / 3, "B3b")
# B4 loop
X4, Y4 = 3 * t**2, 3 * t - t**3
eq(diff(X4, t) ** 2 + diff(Y4, t) ** 2 - 9 * (1 + t**2) ** 2, 0, "B4a")
eq(integrate(3 * (1 + t**2), (t, -sqrt(3), sqrt(3))), 12 * sqrt(3), "B4b")
eq(2 * pi * integrate(Y4 * 3 * (1 + t**2), (t, 0, sqrt(3))), 27 * pi, "B4c")
assert Y4.subs(t, sqrt(3)) == 0 and X4.subs(t, sqrt(3)) == 9; N += 1

print(f"pb13 checks passed: {N}")
