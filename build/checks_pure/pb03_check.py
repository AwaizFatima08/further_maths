"""SymPy/SciPy checks for Unit B3 (pure/pb03.py): derivatives, series coefficients, general terms, validity and numbers."""
import importlib
import sys
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from sympy import (E, Rational as R, atan, binomial, cos, diff, exp, factorial, ff, idiff, integrate, lambdify, log, pi,
                   series, simplify, sin, sqrt, symbols, tan, sec, solve, sinh, cosh, atanh, Function, Eq)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
UNIT = importlib.import_module("pure.pb03").UNIT


def _flat(o):
    if isinstance(o, str):
        return [o]
    if isinstance(o, dict):
        return [s for v in o.values() for s in _flat(v)]
    if isinstance(o, (list, tuple)):
        return [s for v in o for s in _flat(v)]
    return [str(o)]


TEXT = "\n".join(_flat(UNIT))
x, t = symbols("x t", real=True)
r, n, k = symbols("r n k", integer=True, nonnegative=True)
N = 0


def eq(a, b, msg):
    global N
    assert simplify(a - b) == 0, f"{msg}: {simplify(a)} != {b}"
    N += 1


def ser(f, order, expected, msg):
    """Maclaurin series of f up to x^order equals the polynomial expected."""
    global N
    s = series(f, x, 0, order + 1).removeO()
    assert simplify(s - expected) == 0, f"{msg}: {s} vs {expected}"
    N += 1


def dec(value, stated, msg, tol=None):
    global N
    d = len(stated.split(".")[1]) if "." in stated else 0
    tol = 0.5 * 10 ** (-d) + 1e-12 if tol is None else tol
    assert abs(float(value) - float(stated)) <= tol, f"{msg}: {float(value)} vs {stated}"
    assert stated.replace("-", "−") in TEXT or stated in TEXT, f"{stated} not in text ({msg})"
    N += 1


def gen(term, f, msg, upto=8):
    """General term (expression in r and x) reproduces the Maclaurin coefficients of f."""
    global N
    s = series(f, x, 0, upto + 1).removeO()
    total = sum(term.subs(r, j) for j in range(0, upto + 1))
    total = series(total, x, 0, upto + 1).removeO()
    assert simplify(total - s) == 0, f"{msg}: general term mismatch"
    N += 1


# Box: nth derivatives
a = symbols("a", real=True)
for m in range(1, 7):
    eq(diff(exp(a * x), x, m), a**m * exp(a * x), "e^ax")
    eq(diff(sin(x), x, m), sin(x + m * pi / 2), "sin")
    eq(diff(cos(x), x, m), cos(x + m * pi / 2), "cos")
    eq(diff(log(1 + x), x, m), (-1) ** (m - 1) * factorial(m - 1) / (1 + x) ** m, "ln")
    kk = R(5, 3)
    eq(diff((1 + x) ** kk, x, m), ff(kk, m) * (1 + x) ** (kk - m), "power")
# B3.2 implicit circle
y = symbols("y", real=True)
yp = idiff(x**2 + y**2 - 25, y, x, 1); ypp = idiff(x**2 + y**2 - 25, y, x, 2)
eq(ypp.subs(x**2, 25 - y**2), -25 / y**3, "circle y''")
eq(ypp + (x**2 + y**2) / y**3, 0, "circle y'' form")
# Maclaurin e^x general term
gen(x**r / factorial(r), exp(x), "e^x")
# Table of standard series (general terms)
s_ln = sum((-1) ** (j + 1) * x**j / j for j in range(1, 9)); ser(log(1 + x), 8, s_ln, "ln(1+x) table")
gen((-1) ** r * x ** (2 * r + 1) / factorial(2 * r + 1), sin(x), "sin", 9)
gen((-1) ** r * x ** (2 * r) / factorial(2 * r), cos(x), "cos", 9)
nn = R(-1, 2)
ser((1 + x) ** nn, 6, sum(ff(nn, j) * x**j / factorial(j) for j in range(7)), "binomial general term")
gen((-1) ** r * x ** (2 * r + 1) / (2 * r + 1), atan(x), "atan", 9)
gen(x ** (2 * r + 1) / factorial(2 * r + 1), sinh(x), "sinh", 9)
gen(x ** (2 * r) / factorial(2 * r), cosh(x), "cosh", 9)
gen(x ** (2 * r + 1) / (2 * r + 1), atanh(x), "artanh", 9)
# B3.5 ln 2 partial sums converge, at x=2 the terms grow
assert abs(sum((-1) ** (j + 1) / j for j in range(1, 20001)) - np.log(2)) < 1e-4
eq(sum((-1) ** (j + 1) * R(2) ** j / j for j in range(1, 5)), 2 - 2 + R(8, 3) - 4, "x=2 terms")
# B3.6 bullets
ser(exp(-x**2), 4, 1 - x**2 + x**4 / 2, "e^-x^2")
ser(log(2 + x), 3, log(2) + x / 2 - x**2 / 8 + x**3 / 24, "ln(2+x)")
ser(1 / (3 + x), 3, R(1, 3) * (1 - x / 3 + x**2 / 9 - x**3 / 27), "1/(3+x)")
ser(log((1 + x) / (1 - x)), 7, 2 * (x + x**3 / 3 + x**5 / 5 + x**7 / 7), "ln((1+x)/(1-x))")
ser(exp(x) * sin(x), 4, x + x**2 + x**3 / 3, "e^x sin x")
ser(exp(x) * sin(x), 5, x + x**2 + x**3 / 3 - x**5 / 30, "e^x sin x x^5")
ser(cos(x) ** 2, 4, 1 - x**2 + x**4 / 3, "cos^2")
ser(diff(log(1 + x), x), 3, 1 - x + x**2 - x**3, "derivative of ln series")
# B3.7 ln 1.2
approx = 0.2 - 0.2**2 / 2 + 0.2**3 / 3
dec(approx, "0.182667", "ln1.2 approx"); dec(np.log(1.2), "0.182322", "ln1.2 exact")
assert abs((np.log(1.2) - approx) + 3.4e-4) < 0.06e-4; N += 1
eq(R(2, 10) ** 4 / 4, R(4, 10000), "next term 0.0004")
# B3.8 tan
eq(diff(tan(x), x) - (1 + tan(x) ** 2), 0, "tan' = 1 + tan^2")
yy = exp(x) * cos(x)
eq(diff(yy, x, 2) - 2 * diff(yy, x) + 2 * yy, 0, "e^x cos x DE")

# Worked example 1
f = cos(2 * x)
d = [diff(f, x, j).subs(x, 0) for j in range(7)]
assert d == [1, 0, -4, 0, 16, 0, -64]; N += 1
ser(f, 6, 1 - 2 * x**2 + R(2, 3) * x**4 - R(4, 45) * x**6, "WE1")
gen((-1) ** r * 2 ** (2 * r) * x ** (2 * r) / factorial(2 * r), f, "WE1 general", 10)
# Worked example 2
F = x**2 + x * y + y**2 - 7
y1 = idiff(F, y, x, 1).subs({x: 1, y: 2}); y2 = idiff(F, y, x, 2).subs({x: 1, y: 2})
eq(y1, -R(4, 5), "WE2a y'"); eq(y2, -R(42, 125), "WE2a y''"); eq(2 - R(8, 5) + R(32, 25), R(42, 25), "WE2a arithmetic")
X, Y = t**2, t**3 - 3 * t
dydx = diff(Y, t) / diff(X, t); d2 = diff(dydx, t) / diff(X, t)
eq(d2, 3 * (t**2 + 1) / (4 * t**3), "WE2b"); eq(diff(dydx, t), 3 * (t**2 + 1) / (2 * t**2), "WE2b step")
assert set(solve(diff(Y, t), t)) == {-1, 1}
eq(d2.subs(t, 1), R(3, 2), "t=1"); eq(d2.subs(t, -1), -R(3, 2), "t=-1")
assert (X.subs(t, 1), Y.subs(t, 1)) == (1, -2) and (X.subs(t, -1), Y.subs(t, -1)) == (1, 2); N += 1
# Worked example 3
f3 = log((1 + x) / (1 - 2 * x))
ser(f3, 3, 3 * x + R(3, 2) * x**2 + 3 * x**3, "WE3")
ser(log(1 - 2 * x), 3, -2 * x - 2 * x**2 - R(8, 3) * x**3, "WE3 ln(1-2x)")
s3 = series(f3, x, 0, 9).removeO()
for j in range(1, 9):
    eq(s3.coeff(x, j), ((-1) ** (j + 1) + 2**j) / R(j), f"WE3 general r={j}")
# Worked example 4
f4 = exp(sin(x))
d4 = [diff(f4, x, j).subs(x, 0) for j in range(5)]
assert d4 == [1, 1, 1, 0, -3]; N += 1
ser(f4, 4, 1 + x + x**2 / 2 - x**4 / 8, "WE4")
yv = f4
eq(diff(yv, x, 3) - (diff(yv, x, 2) * cos(x) - 2 * diff(yv, x) * sin(x) - yv * cos(x)), 0, "WE4 y'''")
eq(diff(yv, x, 4) - (diff(yv, x, 3) * cos(x) - 3 * diff(yv, x, 2) * sin(x) - 3 * diff(yv, x) * cos(x) + yv * sin(x)), 0, "WE4 y4")
# Worked example 5
ys = tan(x)
d5 = [diff(ys, x, j).subs(x, 0) for j in range(6)]
assert d5 == [0, 1, 0, 2, 0, 16]; N += 1
ser(tan(x), 5, x + x**3 / 3 + R(2, 15) * x**5, "WE5")
yp1 = 1 + ys**2; ypp = 2 * ys * yp1
eq(diff(ys, x, 2) - ypp, 0, "y''=2yy'")
eq(diff(ys, x, 3) - (2 * yp1**2 + 2 * ys * ypp), 0, "y'''")
eq(diff(ys, x, 4) - (6 * yp1 * ypp + 2 * ys * diff(ys, x, 3)), 0, "y4")
eq(diff(ys, x, 5) - (6 * ypp**2 + 8 * yp1 * diff(ys, x, 3) + 2 * ys * diff(ys, x, 4)), 0, "y5")
# Worked example 6
ser(exp(-x**2), 6, 1 - x**2 + x**4 / 2 - x**6 / 6, "WE6a")
est = 0.5 - 0.5**3 / 3 + 0.5**5 / 10 - 0.5**7 / 42
dec(est, "0.461272", "WE6b"); exact, _ = quad(lambda u: np.exp(-u * u), 0, 0.5); dec(exact, "0.461281", "WE6c exact")
assert abs((exact - est) - 9e-6) < 0.5e-6; N += 1
assert abs(0.5**9 / 216 - 9.0e-6) < 0.05e-6; N += 1

# Section A
eq(diff(x**3 * log(x), x, 3), 6 * log(x) + 11, "A1")
for m in range(1, 6):
    eq(diff(x * exp(x), x, m), (x + m) * exp(x), f"A2 n={m}")
yp = idiff(y**2 - 4 * x, y, x, 2); eq(yp, -4 / y**3, "A3")
X4, Y4 = 3 * cos(t), 3 * sin(t)
dydx4 = diff(Y4, t) / diff(X4, t); eq(dydx4, -cos(t) / sin(t), "A4 dydx")
eq(diff(dydx4, t) / diff(X4, t), -1 / (3 * sin(t) ** 3), "A4")
eq(diff(sec(x), x, 2), 2 * sec(x) ** 3 - sec(x), "A5 f''")
assert diff(sec(x), x, 4).subs(x, 0) == 5; N += 1
ser(sec(x), 4, 1 + x**2 / 2 + R(5, 24) * x**4, "A5")
ser(exp(-2 * x), 3, 1 - 2 * x + 2 * x**2 - R(4, 3) * x**3, "A6"); gen((-2) ** r * x**r / factorial(r), exp(-2 * x), "A6 general")
ser(sin(3 * x), 5, 3 * x - R(9, 2) * x**3 + R(81, 40) * x**5, "A7")
gen((-1) ** r * 3 ** (2 * r + 1) * x ** (2 * r + 1) / factorial(2 * r + 1), sin(3 * x), "A7 general", 9)
ser((1 - 3 * x) ** R(-1, 3), 3, 1 + x + 2 * x**2 + R(14, 3) * x**3, "A8")
ser(log(2 + x), 3, log(2) + x / 2 - x**2 / 8 + x**3 / 24, "A9")
ser(exp(x) * sin(x), 4, x + x**2 + x**3 / 3, "A10")
ser(cos(x) ** 2, 4, 1 - x**2 + x**4 / 3, "A11")
s12 = 0.2 - 0.2**3 / 6
dec(s12, "0.198667", "A12 approx"); dec(np.sin(0.2), "0.198669", "A12 exact")
err = np.sin(0.2) - s12; assert abs(err - 2.66e-6) < 0.005e-6; N += 1
assert abs(0.2**5 / 120 - 2.67e-6) < 0.005e-6; N += 1

# Section B1
f1 = log(cos(x))
eq(diff(f1, x), -tan(x), "B1 f'"); eq(diff(f1, x, 2), -sec(x) ** 2, "B1 f''")
eq(diff(f1, x, 3), -2 * sec(x) ** 2 * tan(x), "B1 f'''"); eq(diff(f1, x, 4), -4 * sec(x) ** 2 * tan(x) ** 2 - 2 * sec(x) ** 4, "B1 f4")
assert [diff(f1, x, j).subs(x, 0) for j in range(5)] == [0, 0, -1, 0, -2]; N += 1
ser(f1, 4, -x**2 / 2 - x**4 / 12, "B1b")
est1 = -(0.3**3) / 6 - 0.3**5 / 60
assert abs(est1 + 0.0045405) < 1e-12; assert "−0.0045405" in TEXT; N += 1
ex1, _ = quad(lambda u: np.log(np.cos(u)), 0, 0.3); assert abs(ex1 - est1) < 2e-6; N += 1  # series is a good approximation
# B2
F2 = x**2 + 2 * x * y + 3 * y**2 - 6
eq(idiff(F2, y, x, 1), -(x + y) / (x + 3 * y), "B2a")
pts = [(sqrt(3), -sqrt(3)), (-sqrt(3), sqrt(3))]
for (px, py) in pts:
    eq(F2.subs({x: px, y: py}), 0, "B2b on curve"); eq((x + y).subs({x: px, y: py}), 0, "B2b stationary")
eq(idiff(F2, y, x, 2).subs({x: sqrt(3), y: -sqrt(3)}), sqrt(3) / 6, "B2c min")
eq(idiff(F2, y, x, 2).subs({x: -sqrt(3), y: sqrt(3)}), -sqrt(3) / 6, "B2c max")
eq(1 / (2 * sqrt(3)), sqrt(3) / 6, "B2c form")
# B3
gen(2 * x ** (2 * r + 1) / (2 * r + 1), log((1 + x) / (1 - x)), "B3a general", 11)
eq((1 + R(1, 3)) / (1 - R(1, 3)), 2, "B3b x=1/3")
v = 2 * (R(1, 3) + R(1, 81) + R(1, 1215) + R(1, 15309))
eq(R(1, 3) ** 3 / 3, R(1, 81), "t2"); eq(R(1, 3) ** 5 / 5, R(1, 1215), "t3"); eq(R(1, 3) ** 7 / 7, R(1, 15309), "t4")
dec(float(v), "0.693135", "B3b approx"); dec(np.log(2), "0.693147", "B3b ln2")
assert abs((np.log(2) - float(v)) - 1.2e-5) < 0.05e-5; N += 1
dec(1 - 0.5 + 1 / 3 - 0.25, "0.583", "B3c")
# B4
eq(diff(yy, x), exp(x) * (cos(x) - sin(x)), "B4 y'"); eq(diff(yy, x, 2), -2 * exp(x) * sin(x), "B4 y''")
assert [diff(yy, x, j).subs(x, 0) for j in range(5)] == [1, 1, 0, -2, -4]; N += 1
ser(yy, 4, 1 + x - x**3 / 3 - x**4 / 6, "B4b")
est4 = 0.2 + 0.2**2 / 2 - 0.2**4 / 12 - 0.2**5 / 30
dec(est4, "0.21986", "B4c")
ex4, _ = quad(lambda u: np.exp(u) * np.cos(u), 0, 0.2); assert abs(ex4 - est4) < 5e-6; N += 1
exact4 = (np.exp(0.2) * (np.sin(0.2) + np.cos(0.2)) - 1) / 2; assert abs(exact4 - ex4) < 1e-12; N += 1

print(f"pb03 checks passed: {N}")
