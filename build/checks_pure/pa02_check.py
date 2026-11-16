"""Verifies every result stated in pure/pa02.py (Unit A2: Argand diagrams, modulus-argument form, loci)."""
import os
import sys
from math import isclose

import numpy as np
import sympy as sp
from sympy import I, pi, sqrt, cos, sin, atan, asin, Abs, arg, expand, simplify

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pure.pa02 import UNIT  # noqa: E402


def _text(o):
    if isinstance(o, str):
        return o
    if isinstance(o, dict):
        return " ".join(_text(v) for v in o.values())
    if isinstance(o, (list, tuple)):
        return " ".join(_text(v) for v in o)
    return str(o)


TEXT = _text(UNIT)
N = 0
x, y = sp.symbols("x y", real=True)


def eq(a, b, msg=""):
    global N
    d = simplify(expand(sp.nsimplify(a) - sp.nsimplify(b)))
    assert d == 0 or abs(complex(sp.N(d, 30))) < 1e-25, f"{msg}: {a} != {b}"
    N += 1


def num(s, v, dp=None, sf=None):
    """String s (as printed) agrees with value v."""
    global N
    v = float(v)
    if sf:
        assert float(f"{v:.{sf}g}") == float(s), f"{s} vs {v}"
    else:
        d = dp if dp is not None else (len(s.split(".")[1]) if "." in s else 0)
        assert abs(round(v, d) - float(s)) < 1e-9, f"{s} vs {v}"
    assert s in TEXT, f"{s} not in text"
    N += 1


def modarg(zv, r, th):
    eq(Abs(zv), r, f"|{zv}|"); eq(arg(zv), th, f"arg {zv}")


def cart(expr, zz=x + I * y):
    """|..|² etc: return expression in x, y."""
    return sp.expand(expr.subs(sp.Symbol("Z"), zz))


def same_line(e1, e2):
    """Two linear/quadratic expressions in x, y are proportional (same curve)."""
    global N
    r = sp.simplify(e1 / e2)
    assert r.free_symbols == set(), f"{e1} not prop. to {e2}"
    N += 1


def sq(w):
    return sp.expand(w * sp.conjugate(w))


Z = x + I * y

# Notes: table examples
modarg(1 + sqrt(3) * I, 2, pi / 3); modarg(-sqrt(3) + I, 2, 5 * pi / 6); modarg(-2 - 2 * I, 2 * sqrt(2), -3 * pi / 4)
num("0.927", -float(arg(3 - 4 * I)), 3); eq(arg(-5), pi); eq(arg(-2 * I), -pi / 2)
eq(I * Z, -y + I * x)
# |2z - 4| = 6 -> |z - 2| = 3
same_line(sq(2 * Z - 4) - 36, (x - 2) ** 2 + y ** 2 - 9)
# figure values z = 4 + i, w = 1 + 3i
eq((4 + I) + (1 + 3 * I), 5 + 4 * I); eq((4 + I) - (1 + 3 * I), 3 - 2 * I)
# product proof
r1, r2, t1, t2 = sp.symbols("r1 r2 t1 t2", positive=True)
prod = expand(r1 * (cos(t1) + I * sin(t1)) * r2 * (cos(t2) + I * sin(t2)))
eq(sp.simplify(sp.expand_trig(r1 * r2 * (cos(t1 + t2) + I * sin(t1 + t2))) - prod), 0)
quot = r1 * (cos(t1) + I * sin(t1)) / (r2 * (cos(t2) + I * sin(t2)))
eq(sp.simplify(quot - r1 / r2 * (cos(t1 - t2) + I * sin(t1 - t2))), 0)
# set-notation example
for p in [(1, 1, True), (-1, 0, False), (1.9, 0.5, True), (1, 1.9, False)]:
    assert (abs(complex(p[0], p[1])) < 2 and p[0] > 0) == p[2]

# Worked example 1
num("0.9273", np.arctan(4 / 3), 4)
# Worked example 2
zz = 4 * (cos(pi / 3) + I * sin(pi / 3)); ww = 2 * (cos(3 * pi / 4) + I * sin(3 * pi / 4))
modarg(zz * ww, 8, -11 * pi / 12); modarg(zz / ww, 2, -5 * pi / 12)
eq(zz, 2 + 2 * sqrt(3) * I); eq(ww, -sqrt(2) + sqrt(2) * I)
eq(zz / ww, ((sqrt(3) - 1) - (sqrt(3) + 1) * I) / sqrt(2))
eq(cos(5 * pi / 12), (sqrt(6) - sqrt(2)) / 4)
# Worked example 3
z3 = 3 + I
eq(I * z3, -1 + 3 * I); eq(z3 + I * z3, 2 + 4 * I); eq(Abs(z3), sqrt(10))
eq(sp.re(z3 * sp.conjugate(I * z3)), 0)  # perpendicular
# Worked example 4
same_line(sq(Z - 3 + 2 * I) - 16, (x - 3) ** 2 + (y + 2) ** 2 - 16)
same_line(sq(Z + 1) - sq(Z - 3 * I), x + 3 * y - 4)
eq(sp.Rational(-1, 2) + 3 * sp.Rational(3, 2), 4)
# arg(z-2)=pi/4: points 2 + t(1+i), t>0
for t in (0.5, 3):
    assert isclose(float(arg(t * (1 + I))), np.pi / 4); N += 1
# Worked example 5: half disc area, extreme moduli
num("4.83", 2 + 2 * np.sqrt(2), 2); num("0.828", 2 * np.sqrt(2) - 2, 3)
eq(Abs((2 + sqrt(2)) * (1 + I)), 2 + 2 * sqrt(2)); eq(Abs((2 - sqrt(2)) * (1 + I) - 2 - 2 * I), 2)
eq(Abs((2 + sqrt(2)) * (1 + I) - 2 - 2 * I), 2)
# numerical check of half-disc area by Monte Carlo grid
g = np.linspace(0, 4, 1601); X, Y = np.meshgrid(g, g)
inR = ((X - 2) ** 2 + (Y - 2) ** 2 <= 4) & (Y <= X)
assert abs(inR.sum() * (4 / 1600) ** 2 - 2 * np.pi) < 0.02; N += 1
# Worked example 6
num("0.6435", np.arcsin(0.6), 4); num("0.927", np.pi / 2 - np.arcsin(0.6), 3); num("2.21", np.pi / 2 + np.arcsin(0.6), 2)
eq(Abs(sp.Rational(12, 5) + sp.Rational(16, 5) * I - 5 * I), 3)
eq(arg(sp.Rational(12, 5) + sp.Rational(16, 5) * I), pi / 2 - asin(sp.Rational(3, 5)))

# Practice
zp, wp = 2 - 5 * I, -3 + I
eq(zp + wp, -1 - 4 * I); eq(zp - wp, 5 - 6 * I)
modarg(1 + I, sqrt(2), pi / 4); modarg(-5, 5, pi); modarg(-2 * I, 2, -pi / 2); modarg(-1 - sqrt(3) * I, 2, -2 * pi / 3)
num("2.21", float(arg(-3 + 4 * I)), 2); eq(Abs(-3 + 4 * I), 5)
eq(6 * (cos(pi / 6) + I * sin(pi / 6)), 3 * sqrt(3) + 3 * I)
eq(sqrt(2) * (cos(-3 * pi / 4) + I * sin(-3 * pi / 4)), -1 - I)
eq(4 * (cos(2 * pi / 3) + I * sin(2 * pi / 3)), -2 + 2 * sqrt(3) * I)
modarg(sqrt(3) - I, 2, -pi / 6)
zz = 6 * (cos(5 * pi / 6) + I * sin(5 * pi / 6)); ww = 2 * (cos(pi / 3) + I * sin(pi / 3))
modarg(zz * ww, 12, -5 * pi / 6); eq(zz / ww, 3 * I); modarg(zz ** 2, 36, -pi / 3)
eq(Abs((3 + 4 * I) * (1 - I)), 5 * sqrt(2)); eq((1 + I) / (1 - I), I)
same_line(sq(Z - 1) - sq(Z + I), x + y)
for t in (0.5, 2):  # arg(z+1-i) = -pi/4 : z = -1 + i + t(1 - i), lies on y = -x
    pt = -1 + I + t * (1 - I); eq(arg(pt + 1 - I), -pi / 4); eq(sp.re(pt) + sp.im(pt), 0)
same_line(sq(Z + 2 - I) - sq(Z - 4 + 3 * I), 3 * x - 2 * y - 5)
eq(sp.Rational(1, 2) * 9 * pi / 3, 3 * pi / 2)
same_line(sq(Z) - sq(Z - 4), x - 2)
eq(Abs(3 + 4 * I) + 2, 7); eq(Abs(3 + 4 * I) - 2, 3)
zt = 3 * sqrt(3) * (cos(pi / 3) + I * sin(pi / 3)); eq(zt, 3 * sqrt(3) / 2 + sp.Rational(9, 2) * I); eq(Abs(zt - 6 * I), 3)
eq(asin(sp.Rational(1, 2)), pi / 6)

# Exam 1
zz, ww = 1 + sqrt(3) * I, 1 - I
modarg(zz, 2, pi / 3); modarg(ww, sqrt(2), -pi / 4); modarg(zz * ww, 2 * sqrt(2), pi / 12); modarg(zz / ww, sqrt(2), 7 * pi / 12)
eq(zz / ww, ((1 - sqrt(3)) + (1 + sqrt(3)) * I) / 2); eq(cos(7 * pi / 12), (sqrt(2) - sqrt(6)) / 4)
# Exam 2
for s in (1, -1):
    pt = (4 + s * sqrt(2)) + (2 + s * sqrt(2)) * I
    eq(Abs(pt - 4 - 2 * I), 2); eq(arg(pt - 2), pi / 4)
# Exam 3
num("0.9273", np.arctan(4 / 3), 4); num("0.4115", np.arcsin(0.4), 4); num("1.34", np.arctan(4 / 3) + np.arcsin(0.4), 2)
eq(sp.Rational(6, 10) * (6 + 8 * I), sp.Rational(18, 5) + sp.Rational(24, 5) * I); eq(Abs(6 + 8 * I), 10)
# Exam 4
q = expand((1 + I) * (4 + 2 * I)); eq(q, 2 + 6 * I)
eq(Abs(4 + 2 * I) ** 2, 20); eq(Abs(q - 4 - 2 * I) ** 2, 20); eq(Abs(q) ** 2, 40)

assert len(UNIT["practice"]) == len(UNIT["answers"]) == 12 and len(UNIT["exam"]) == len(UNIT["exam_answers"]) == 4
print(f"pa02: all {N} checks passed")
