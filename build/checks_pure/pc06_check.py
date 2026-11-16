"""Verifies every result stated in pure/pc06.py (Unit C6: further loci and transformations)."""
import os
import sys

import numpy as np
import sympy as sp
from sympy import I, pi, sqrt, sin, Abs, arg, expand, simplify, Rational as R

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pure.pc06 import UNIT  # noqa: E402

N = 0
x, y, u, v = sp.symbols("x y u v", real=True)
Z, W = x + I * y, u + I * v


def ok(cond, msg=""):
    global N
    assert cond, msg
    N += 1


def eq(a, b, msg=""):
    global N
    d = sp.nsimplify(a) - sp.nsimplify(b)
    assert simplify(expand(d)) == 0 or abs(complex(sp.N(d, 40))) < 1e-30, f"{msg}: {a} != {b}"
    N += 1


def sq(e):
    return expand(e * sp.conjugate(e))


def prop(e1, e2, msg=""):
    """e1 and e2 (polynomials in x,y or u,v) define the same curve: e1 = k e2, k constant != 0."""
    global N
    r = simplify(e1 / e2)
    assert r.free_symbols == set() and r != 0, f"{msg}: {expand(e1)} vs {expand(e2)}"
    N += 1


def on_curve(expr, pts, var=(x, y)):
    global N
    for p in pts:
        assert abs(complex(sp.N(expr.subs({var[0]: p[0], var[1]: p[1]})))) < 1e-12, f"{expr} at {p}"
    N += 1


def arg_locus_check(a, b, beta, centre, radius, side_sign):
    """Sample points on the circle; those on the stated side have arg((z-a)/(z-b)) = beta."""
    global N
    a, b, centre = complex(a), complex(b), complex(centre)
    d = a - b
    for t in np.linspace(0, 2 * np.pi, 73)[:-1]:
        zz = centre + radius * np.exp(1j * t)
        if min(abs(zz - a), abs(zz - b)) < 1e-6:
            continue
        cross = (d.conjugate() * (zz - b)).imag  # >0: left of direction b->a
        val = np.angle((zz - a) / (zz - b))
        if cross * side_sign > 1e-9:
            assert abs(val - beta) < 1e-9, (t, val)
        elif cross * side_sign < -1e-9:
            assert abs(val - beta) > 1e-3
    N += 1


# Notes 6.2
prop(sq(Z + 3) - 4 * sq(Z), (x - 1) ** 2 + y ** 2 - 4)
on_curve((x - 1) ** 2 + y ** 2 - 4, [(1, 2), (3, 0), (-1, 0)])
eq(Abs(1 + 2 * I + 3), sqrt(20)); eq(Abs(1 + 2 * I), sqrt(5))
# check formula: centre (a - k^2 b)/(1 - k^2), radius k|a-b|/|1-k^2|
for a, b, k in [(-3, 0, 2), (2, -2, 3), (I, 4 * I, 2), (6, 3 * I, 2), (1 + 2 * I, -3 + I, R(1, 3))]:
    cen = (a - k ** 2 * b) / (1 - k ** 2); rad = k * Abs(a - b) / Abs(1 - k ** 2)
    e = sq(Z - a) - k ** 2 * sq(Z - b)
    prop(e, sq(Z - cen) - rad ** 2)
# a lies in region |z-a| < k|z-b| trivially; arc rule (left of b->a for beta>0) numerically
arg_locus_check(1, -1, np.pi / 4, 1j, np.sqrt(2), 1)
arg_locus_check(1, -1, np.pi / 2, 0, 1, 1)
arg_locus_check(1, -1, 3 * np.pi / 4, -1j, np.sqrt(2), 1)
arg_locus_check(1, -1, -np.pi / 4, -1j, np.sqrt(2), -1)
# inside circle on arc side -> bigger angle
ok(np.angle((0.5j - 1) / (0.5j + 1)) > np.pi / 4 and np.angle((3j - 1) / (3j + 1)) < np.pi / 4)
# beta = pi/2 -> X = 0
# 6.5 shortcut |z-1|=1 under w = 1/z -> Re w = 1/2
prop(sq(1 - W) - sq(W), u - R(1, 2))
# 6.6 z^2
ok(expand((1 + I * y) ** 2) == 1 - y ** 2 + 2 * I * y)

# Worked example 1
prop(expand((x + 3) ** 2 + y ** 2 - 4 * (x ** 2 + y ** 2)), 3 * x ** 2 + 3 * y ** 2 - 6 * x - 9)
eq(Abs(3 + 3), 2 * 3); eq(Abs(-1 + 3), 2 * 1); ok(Abs(4) >= 2 * Abs(1))
# Worked example 2
eq(2 / (2 * sin(pi / 4)), sqrt(2))
ratio = expand((Z - 1) * sp.conjugate(Z + 1))
eq(sp.re(ratio) - (x ** 2 + y ** 2 - 1), 0); eq(sp.im(ratio) - 2 * y, 0)
arg_locus_check(1, -1, np.pi / 4, 1j, np.sqrt(2), 1)
# Worked example 3
for zz in (2, 1 + I, 1 - I, 1 + sp.exp(I * R(7, 10))):
    eq(sp.re(1 / zz), R(1, 2))
eq(1 / (1 + I), (1 - I) / 2)
# Worked example 4
w_of_z = lambda zz: (2 * zz + 1) / (zz - 1)
ws = sp.symbols("w"); zs = sp.symbols("z")
ok(sp.solve(sp.Eq(ws, (2 * zs + 1) / (zs - 1)), zs) == [(ws + 1) / (ws - 2)])
prop(sq(W + 1) - 4 * sq(W - 2), (u - 3) ** 2 + v ** 2 - 4)
for t in np.linspace(0.1, 6, 7):
    ww = complex(w_of_z(2 * sp.exp(I * t)).evalf())
    ok(abs(abs(ww - 3) - 2) < 1e-12)
eq(w_of_z(2), 5); eq(w_of_z(-2), 1)
# Worked example 5
r = sp.symbols("r", positive=True)
eq(arg((r * sp.exp(I * pi / 3)) ** 2), 2 * pi / 3); eq(Abs((3 * sp.exp(I * R(1, 3))) ** 2), 9)
wz = expand((1 + I * y) ** 2); on_curve(sp.re(wz) - (1 - sp.im(wz) ** 2 / 4), [(0, 0.3), (0, -2.0), (0, 1.7)])
# Worked example 6
ok(sp.solve(sp.Eq(ws, zs / (zs + I)), zs) == [I * ws / (1 - ws)] or
   simplify(sp.solve(sp.Eq(ws, zs / (zs + I)), zs)[0] - I * ws / (1 - ws)) == 0)
for xr in np.linspace(-5, 5, 11):
    ww = xr / (xr + 1j); ok(abs(abs(ww - 0.5) - 0.5) < 1e-12)
eq(I / (2 * I), R(1, 2))
for zz in (0.3 + 0.2j, -2 + 5j, 4 + 0.01j):
    ok(abs(zz / (zz + 1j) - 0.5) < 0.5)

# Practice
prop(sq(Z - 2) - 9 * sq(Z + 2), (x + R(5, 2)) ** 2 + y ** 2 - R(9, 4))
prop(expand((x - 2) ** 2 + y ** 2 - 9 * ((x + 2) ** 2 + y ** 2)), 8 * x ** 2 + 8 * y ** 2 + 40 * x + 32)
prop(sq(Z - I) - 4 * sq(Z - 4 * I), x ** 2 + (y - 5) ** 2 - 4); ok(Abs(-I + I) < 2 * Abs(-3 * I))
on_curve(x ** 2 + y ** 2 - 4, [(-2, 0)]); eq(arg((-2 - 2 * I) / (-2 + 2 * I)), pi / 2)
arg_locus_check(2j, -2j, np.pi / 2, 0, 2, 1)
cen4 = 1 + 2 / sqrt(3) * I; R4 = 4 / sqrt(3); eq(4 / (2 * sin(pi / 3)), R4)
eq(Abs(3 - cen4), R4); eq(Abs(-1 - cen4), R4)
arg_locus_check(3, -1, np.pi / 3, complex(cen4), float(R4), 1)
eq(R4 ** 2, R(16, 3))
eq(R(1, 2) * 2 * 2, 2)
prop(sq((W - I) / 2 - 1) - 4, sq(W - 2 - I) - 16)
eq(expand(I * (2 + I * y) + 1), (1 - y) + 2 * I)
eq(sp.re(1 / W) * (u ** 2 + v ** 2) - u, 0)
prop(u - 2 * (u ** 2 + v ** 2), (u - R(1, 4)) ** 2 + v ** 2 - R(1, 16))
eq(expand(-2 * I * (W + I / 2)), expand(1 - 2 * I * W))
prop(sq(W + I / 2) - sq(W), v + R(1, 4))
for zz in (4 * I, 2 + 2 * I, -2 + 2 * I):
    eq(sp.im(1 / zz), -R(1, 4))
wz = expand((x + I) ** 2); eq(sp.re(wz) - (sp.im(wz) ** 2 / 4 - 1), 0)
for zz in (1 + 0j, 3j, -3j, -0.5j):  # imaginary axis -> |w| = 1 for (z-1)/(z+1)
    if zz.real == 0:
        ok(abs(abs((zz - 1) / (zz + 1)) - 1) < 1e-12)
ok(abs((2 + 1j - 1) / (2 + 1j + 1)) < 1)

# Exam 1
prop(sq(Z - 6) - 4 * sq(Z - 3 * I), (x + 2) ** 2 + (y - 4) ** 2 - 20)
prop(expand((x - 6) ** 2 + y ** 2 - 4 * (x ** 2 + (y - 3) ** 2)), 3 * x ** 2 + 3 * y ** 2 + 12 * x - 24 * y)
eq(Abs(-2 + 4 * I), 2 * sqrt(5)); eq(2 * Abs(-2 + 4 * I), 4 * sqrt(5))
ok(Abs(-2 + 4 * I - 6) >= 2 * Abs(-2 + 4 * I - 3 * I))
area = 20 * np.arccos(1 / np.sqrt(5)) - 8
ok(f"{area:.3g}" == "14.1" and "14.1" in str(UNIT["exam_answers"][0]))
g = np.linspace(0, 8, 2001); X, Y = np.meshgrid(np.linspace(0, 3, 801), g)
mask = (X + 2) ** 2 + (Y - 4) ** 2 <= 20
ok(abs(mask.sum() * (3 / 800) * (8 / 2000) - area) < 0.05)
on_curve((x + 2) ** 2 + (y - 4) ** 2 - 20, [(0, 0), (0, 8)])
# Exam 2
eq(Abs(3 * I + 3) / (2 * sin(pi / 4)), 3); eq(sqrt(9 - R(9, 2)), 3 / sqrt(2))
eq(Abs(-3 + 3 * I + 3), 3); eq(Abs(-3 + 3 * I - 3 * I), 3)
arg_locus_check(3j, -3, np.pi / 4, -3 + 3j, 3, 1)
far = (-3 + 3j) * (1 + 3 / abs(-3 + 3j))
ok(abs(np.angle((far - 3j) / (far + 3)) - np.pi / 4) < 1e-12)
eq(Abs(-3 + 3 * I) + 3, 3 * sqrt(2) + 3)
# Exam 3
ok(simplify(sp.solve(sp.Eq(ws, (zs + 1) / (zs - 2)), zs)[0] - (2 * ws + 1) / (ws - 1)) == 0)
prop(sq(2 * W + 1) - sq(W - 1), (u + 1) ** 2 + v ** 2 - 1)
for t in np.linspace(0.2, 6, 8):
    zz = np.exp(1j * t); ww = (zz + 1) / (zz - 2); ok(abs(abs(ww + 1) - 1) < 1e-12)
    zl = 0.5 + 1j * np.tan(t / 2 - 0.1); wl = (zl + 1) / (zl - 2); ok(abs(abs(wl) - 1) < 1e-12)
eq((0 + 1) / (0 - 2), -R(1, 2)); eq((1 + 1) / (1 - 2), -2)
# Exam 4
xx = sp.symbols("xx", real=True)
wz = expand((xx + I * (1 - xx)) ** 2)
eq(sp.re(wz) - (2 * xx - 1), 0); eq(sp.im(wz) - (2 * xx - 2 * xx ** 2), 0)
eq(simplify(sp.im(wz) - (1 - sp.re(wz) ** 2) / 2), 0)
eq(expand((R(1, 2) + I / 2) ** 2), I / 2)
eq(pi * 1 ** 2 / 4, pi / 4)

assert len(UNIT["practice"]) == len(UNIT["answers"]) == 11 and len(UNIT["exam"]) == len(UNIT["exam_answers"]) == 4
print(f"pc06: all {N} checks passed")
