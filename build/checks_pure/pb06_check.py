"""SymPy/SciPy checks for Unit B6 (pure/pb06.py): partial fractions, antiderivatives (by differentiation) and definite integrals."""
import importlib
import sys
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from sympy import (Rational as R, acosh, apart, asin, asinh, atan, cos, cosh, diff, integrate, lambdify, log, pi, simplify,
                   sin, sinh, sqrt, symbols, tan, sec, nsimplify, expand)

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
UNIT = importlib.import_module("pure.pb06").UNIT
x = symbols("x", positive=True)  # every integral here is checked where x > 0 or on a stated interval
xr = symbols("xr", real=True)
th, u = symbols("theta u", real=True)
a = symbols("a", positive=True)
N = 0


def eq(p, q, msg):
    global N
    assert simplify(p - q) == 0, f"{msg}: {simplify(p - q)}"
    N += 1


def anti(F, f, msg, var=x, pts=(0.3, 0.7, 1.3, 2.1)):
    """F is an antiderivative of f: check dF/dx = f symbolically, or numerically at sample points."""
    global N
    d = simplify(diff(F, var) - f)
    if d != 0:
        g = lambdify(var, diff(F, var) - f, "mpmath")
        for p in pts:
            assert abs(complex(g(p))) < 1e-10, f"{msg}: derivative mismatch at {p}"
    N += 1


def defint(f, lo, hi, exact, msg, var=x):
    """Definite integral: SciPy quad agrees with the stated exact value."""
    global N
    g = lambdify(var, f, "numpy")
    v, _ = quad(g, float(lo), float(hi))
    assert abs(v - float(exact)) < 1e-9, f"{msg}: quad {v} vs {float(exact)}"
    N += 1


# Notes B6.1 boxes
c = symbols("c", positive=True)
anti(log(a * x**2 + c) / (2 * a), x / (a * x**2 + c), "x/(ax^2+c)")
anti(atan(x * sqrt(a / c)) / sqrt(a * c), 1 / (a * x**2 + c), "1/(ax^2+c)")
anti(atan(2 * x / 3) / 6, 1 / (4 * x**2 + 9), "1/(4x^2+9)")
# B6.2 standard integrals and log forms
anti(asin(x / 3), 1 / sqrt(9 - x**2), "arcsin", pts=(0.3, 1.0, 2.5))
anti(atan(x / a) / a, 1 / (a**2 + x**2), "arctan")
anti(asinh(x / a), 1 / sqrt(x**2 + a**2), "arsinh")
anti(log(x + sqrt(x**2 + a**2)), 1 / sqrt(x**2 + a**2), "arsinh log form")
anti(acosh(x / 2), 1 / sqrt(x**2 - 4), "arcosh", pts=(2.5, 3.0, 5.0))
anti(log(x + sqrt(x**2 - 4)), 1 / sqrt(x**2 - 4), "arcosh log form", pts=(2.5, 3.0, 5.0))
eq((asinh(x / a) - (log(x + sqrt(x**2 + a**2)) - log(a))).rewrite(log), 0, "arsinh = ln(...) - ln a")
# substitution derivations (integrand after substitution)
assert abs(float((1 / sqrt(a**2 - (a * sin(th)) ** 2) * a * cos(th)).subs({th: R(1, 3), a: 2})) - 1) < 1e-12; N += 1  # x = a sin
eq(simplify(1 / (a**2 + (a * tan(th)) ** 2) * a * sec(th) ** 2), 1 / a, "x=a tan")
eq(simplify(1 / sqrt((a * sinh(u)) ** 2 + a**2) * a * cosh(u)), 1, "x=a sinh")
assert abs(float((1 / sqrt((a * cosh(u)) ** 2 - a**2) * a * sinh(u)).subs({u: R(1, 2), a: 3})) - 1) < 1e-12; N += 1  # x = a cosh u
anti(asin(2 * x / 3) / 2, 1 / sqrt(9 - 4 * x**2), "coef arcsin", pts=(0.2, 0.9, 1.4))
anti(asinh(2 * x / 3) / 2, 1 / sqrt(4 * x**2 + 9), "coef arsinh")
# B6.3 box results
anti(a**2 / 2 * asin(x / a) + x / 2 * sqrt(a**2 - x**2), sqrt(a**2 - x**2), "sqrt(a^2-x^2)")
anti(a**2 / 2 * asinh(x / a) + x / 2 * sqrt(x**2 + a**2), sqrt(x**2 + a**2), "sqrt(x^2+a^2)")
# B6.4 bullets
anti(atan((x + 2) / 3) / 3, 1 / (x**2 + 4 * x + 13), "complete square 1")
anti(asin((x - 1) / 2), 1 / sqrt(3 + 2 * x - x**2), "complete square 2", pts=(0.2, 1.0, 2.5))
anti(acosh(2 * x + 1), 1 / sqrt(x**2 + x), "CAIE x^2+x")
anti(log(2 * x + 1 + 2 * sqrt(x**2 + x)), 1 / sqrt(x**2 + x), "CAIE log form")
eq(expand(4 * (x + 1) ** 2 + 9), 4 * x**2 + 8 * x + 13, "4x^2+8x+13")
eq(expand(-(xr - 1) ** 2 + 4), -xr**2 + 2 * xr + 3, "3+2x-x^2")
# B6.5 example
anti(sqrt(x**2 + 2 * x + 5) + 2 * asinh((x + 1) / 2), (x + 3) / sqrt(x**2 + 2 * x + 5), "linear over surd")

# Worked example 1
f1 = (5 * xr**2 - 2 * xr + 7) / ((xr - 1) * (xr**2 + 4))
eq(apart(f1, xr), 2 / (xr - 1) + (3 * xr + 1) / (xr**2 + 4), "WE1a")
F1 = 2 * log(x - 1) + R(3, 2) * log(x**2 + 4) + atan(x / 2) / 2
anti(F1, f1.subs(xr, x), "WE1 antiderivative", pts=(1.5, 2.5, 3.5))
v1 = F1.subs(x, 4) - F1.subs(x, 2)
eq(v1, 2 * log(3) + R(3, 2) * log(R(5, 2)) + atan(2) / 2 - pi / 8, "WE1b exact")
defint(f1.subs(xr, x), 2, 4, v1, "WE1b quad"); assert abs(float(v1) - 3.73) < 0.005; N += 1
# Worked example 2
f2 = (x**3 + 2 * x**2 + 3 * x + 4) / (x**2 + 1)
eq(expand((x + 2) * (x**2 + 1) + 2 * x + 2), x**3 + 2 * x**2 + 3 * x + 4, "WE2 division")
eq(integrate(f2, (x, 0, 1)), R(5, 2) + log(2) + pi / 2, "WE2"); defint(f2, 0, 1, R(5, 2) + log(2) + pi / 2, "WE2 quad")
# Worked example 3
defint(1 / sqrt(9 - 4 * x**2), 0, R(3, 4), pi / 12, "WE3a")
defint(1 / (3 + 4 * x**2), 0, R(3, 2), pi * sqrt(3) / 18, "WE3b"); eq(pi / (6 * sqrt(3)), pi * sqrt(3) / 18, "WE3b form")
defint(1 / sqrt(4 * x**2 + 9), 0, 2, log(3) / 2, "WE3c"); eq(asinh(R(4, 3)).rewrite(log), log(3), "arsinh(4/3)=ln3")
defint(1 / sqrt(x**2 - 9), 3, 5, log(3), "WE3d"); eq(acosh(R(5, 3)).rewrite(log), log(3), "arcosh(5/3)=ln3")
# Worked example 4
eq(integrate(4 * cos(th) ** 2, (th, 0, pi / 6)), pi / 3 + sqrt(3) / 2, "WE4 theta")
defint(sqrt(4 - x**2), 0, 1, pi / 3 + sqrt(3) / 2, "WE4 quad")
eq(R(1, 2) * 4 * pi / 6, pi / 3, "sector"); eq(R(1, 2) * 1 * sqrt(3), sqrt(3) / 2, "triangle")
# Worked example 5
defint(1 / (x**2 - 6 * x + 13), 3, 5, pi / 8, "WE5a")
defint(1 / sqrt(xr**2 + 4 * xr + 8), -2, 0, log(1 + sqrt(2)), "WE5b", var=xr); eq(asinh(1).rewrite(log), log(1 + sqrt(2)), "arsinh1")
defint(1 / sqrt(5 + 4 * x - x**2), 2, R(7, 2), pi / 6, "WE5c")
# Worked example 6
F6 = 2 * sqrt(xr**2 + 4 * xr + 13) + 3 * asinh((xr + 2) / 3)
anti(F6, (2 * xr + 7) / sqrt(xr**2 + 4 * xr + 13), "WE6 antiderivative", var=xr, pts=(-1.5, 0.0, 1.7))
eq((F6.subs(xr, 2) - F6.subs(xr, -2)).rewrite(log), 4 + 3 * log(3), "WE6 value")
defint((2 * xr + 7) / sqrt(xr**2 + 4 * xr + 13), -2, 2, 4 + 3 * log(3), "WE6 quad", var=xr)

# Section A
fA1 = (xr + 5) / ((xr + 1) * (xr**2 + 1)); eq(apart(fA1, xr), 2 / (xr + 1) + (3 - 2 * xr) / (xr**2 + 1), "A1 pf")
defint(fA1.subs(xr, x), 0, 1, log(2) + 3 * pi / 4, "A1")
eq(apart(1 / (xr * (xr**2 + 4)), xr), (1 / xr - xr / (xr**2 + 4)) / 4, "A2 pf")
anti(log(x) / 4 - log(x**2 + 4) / 8, 1 / (x * (x**2 + 4)), "A2")
anti(x + 2 * atan(x), (x**2 + 3) / (x**2 + 1), "A3")
defint(1 / (4 + x**2), 0, 2, pi / 8, "A4")
defint(1 / sqrt(1 - x**2), 0, R(1, 2), pi / 6, "A5a"); defint(1 / sqrt(4 - 9 * x**2), 0, R(1, 3), pi / 18, "A5b")
anti(atan(3 * x / 5) / 15, 1 / (25 + 9 * x**2), "A6")
defint(1 / sqrt(x**2 + 9), 0, 4, log(3), "A7")
defint(1 / sqrt(x**2 - 4), 2, 4, log(2 + sqrt(3)), "A8"); eq(acosh(2).rewrite(log), log(2 + sqrt(3)), "arcosh2")
anti(atan((x + 1) / 2) / 2, 1 / (x**2 + 2 * x + 5), "A9")
defint(1 / sqrt(3 + 2 * x - x**2), 1, 3, pi / 2, "A10")
eq(integrate(cos(th) ** 2, (th, 0, pi / 4)), pi / 8 + R(1, 4), "A11 theta"); defint(1 / (1 + x**2) ** 2, 0, 1, pi / 8 + R(1, 4), "A11")
eq(simplify((1 / (1 + tan(th) ** 2) ** 2 * sec(th) ** 2) - cos(th) ** 2), 0, "A11 integrand")
anti(sqrt(x**2 + 1) + 2 * asinh(x), (x + 2) / sqrt(x**2 + 1), "A12")

# Section B1
fB1 = (3 * xr**2 + 4 * xr + 9) / ((xr + 1) * (xr**2 + 3))
eq(apart(fB1, xr), 2 / (xr + 1) + (xr + 3) / (xr**2 + 3), "B1a")
FB1 = 2 * log(x + 1) + log(x**2 + 3) / 2 + (3 / sqrt(3)) * atan(x / sqrt(3))
anti(FB1, fB1.subs(xr, x), "B1 antiderivative")
eq(FB1.subs(x, 3) - FB1.subs(x, 0), 5 * log(2) + pi * sqrt(3) / 3, "B1b"); defint(fB1.subs(xr, x), 0, 3, 5 * log(2) + pi * sqrt(3) / 3, "B1b quad")
# B2
eq(simplify(sqrt((3 * sinh(u)) ** 2 + 9) * 3 * cosh(u) - 9 * cosh(u) ** 2), 0, "B2 integrand")
anti(R(9, 2) * asinh(x / 3) + x / 2 * sqrt(x**2 + 9), sqrt(x**2 + 9), "B2a")
defint(sqrt(x**2 + 9), 0, 4, 10 + R(9, 2) * log(3), "B2b")
# B3
eq(expand(4 * (x + 1) ** 2 + 9), 4 * x**2 + 8 * x + 13, "B3a")
defint(1 / (4 * xr**2 + 8 * xr + 13), -1, R(1, 2), pi / 24, "B3b", var=xr)
anti(atan(2 * (xr + 1) / 3) / 6, 1 / (4 * xr**2 + 8 * xr + 13), "B3b anti", var=xr, pts=(-0.5, 0.2, 1.0))
FB3 = 2 * sqrt(4 * xr**2 + 8 * xr + 13) + R(3, 2) * asinh(2 * (xr + 1) / 3)
anti(FB3, (8 * xr + 11) / sqrt(4 * xr**2 + 8 * xr + 13), "B3c anti", var=xr, pts=(-0.5, 0.2, 1.0))
defint((8 * xr + 11) / sqrt(4 * xr**2 + 8 * xr + 13), -1, 1, 4 + R(3, 2) * log(3), "B3c", var=xr)
# B4
eq(simplify((2 * sec(th) ** 2 / (8 * sec(th) ** 3)) - cos(th) / 4), 0, "B4a integrand")
defint(1 / (4 + x**2) ** R(3, 2), 0, 2, sqrt(2) / 8, "B4a")
eq(integrate(cos(th) ** 2 / 8, (th, 0, pi / 4)), (pi + 2) / 64, "B4b theta")
defint(pi / (4 + x**2) ** 2, 0, 2, pi * (pi + 2) / 64, "B4b volume")

print(f"pb06 checks passed: {N}")
