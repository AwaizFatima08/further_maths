"""Verifies every result stated in pure/pb02.py (Unit B2: nth roots and roots of unity)."""
import os
import sys

import numpy as np
import sympy as sp
from sympy import I, pi, sqrt, cos, sin, cot, exp, Abs, arg, expand, simplify, Rational as R

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pure.pb02 import UNIT  # noqa: E402

N = 0
z = sp.symbols("z")


def eq(a, b, msg=""):
    global N
    d = sp.nsimplify(a) - sp.nsimplify(b)
    ok = simplify(expand(d)) == 0 or abs(complex(sp.N(d, 40))) < 1e-30
    assert ok, f"{msg}: {a} != {b}"
    N += 1


def is_root_set(n, w, roots, msg=""):
    """roots are exactly the n distinct solutions of z^n = w."""
    global N
    assert len(roots) == n
    num = [complex(sp.N(r, 30)) for r in roots]
    for r in roots:
        eq(sp.sympify(r) ** n, w, msg)
    for i in range(n):
        for j in range(i):
            assert abs(num[i] - num[j]) > 1e-9, f"{msg}: repeated root"
    N += 1


def same_poly(a, b):
    global N
    assert expand(a - b) == 0, f"{expand(a)} != {expand(b)}"
    N += 1


# Notes
w5 = exp(2 * pi * I / 5)
eq(sum(w5 ** k for k in range(5)), 0)
for n in range(2, 10):
    om = exp(2 * pi * I / n)
    eq(sum(om ** k for k in range(n)), 0)
    for k in range(1, n):
        eq(expand((z - om ** k) * (z - om ** -k)) - (z ** 2 - 2 * cos(2 * k * pi / n) * z + 1), 0)
om3 = exp(2 * pi * I / 3); eq(om3, -R(1, 2) + sqrt(3) / 2 * I); eq(om3 ** 2, sp.conjugate(om3))
eq(w5 + w5 ** 4, 2 * cos(2 * pi / 5)); eq(w5 ** 2 + w5 ** 3, 2 * cos(4 * pi / 5))
eq((w5 + w5 ** 4) + (w5 ** 2 + w5 ** 3), -1); eq((w5 + w5 ** 4) * (w5 ** 2 + w5 ** 3), -1)
eq((1 + I) ** 4, -4)
# rational exponent: q distinct values
th = 0.7
vals = {np.round(np.exp(1j * 2 * (th + 2 * k * np.pi) / 3), 9) for k in range(6)}
assert len(vals) == 3; N += 1

# Worked example 1
is_root_set(3, 8 * I, [sqrt(3) + I, -sqrt(3) + I, -2 * I])
eq(2 * exp(I * pi / 6), sqrt(3) + I); eq(2 * exp(5 * I * pi / 6), -sqrt(3) + I); eq(2 * exp(-I * pi / 2), -2 * I)
eq(sqrt(3) + I - sqrt(3) + I - 2 * I, 0)
# Worked example 2
w2 = -8 + 8 * sqrt(3) * I; eq(Abs(w2), 16); eq(arg(w2), 2 * pi / 3)
rts = [sqrt(3) + I, -1 + sqrt(3) * I, -sqrt(3) - I, 1 - sqrt(3) * I]
is_root_set(4, w2, rts)
for k in range(3):
    eq(I * rts[k], rts[k + 1])
eq(Abs(rts[0] - rts[1]), 2 * sqrt(2))
# Worked example 3
f = (z - 1) * (z ** 2 - 2 * cos(2 * pi / 5) * z + 1) * (z ** 2 - 2 * cos(4 * pi / 5) * z + 1)
for zv in (0.3, 1.7, -2.1):
    assert abs(complex(f.subs(z, zv)) - (zv ** 5 - 1)) < 1e-12
N += 1
eq(cos(2 * pi / 5) + cos(4 * pi / 5), -R(1, 2)); eq(cos(2 * pi / 5) * cos(4 * pi / 5), -R(1, 4))
eq(cos(2 * pi / 5), (sqrt(5) - 1) / 4); assert f"{float((sqrt(5) - 1) / 4):.3f}" == "0.309"; N += 1
x = sp.symbols("x"); assert set(sp.solve(4 * x ** 2 + 2 * x - 1, x)) == {(-1 + sqrt(5)) / 4, (-1 - sqrt(5)) / 4}; N += 1
# Worked example 4
c = 1 + I
verts = [3 + I, (1 + sqrt(3)) * I, (1 - sqrt(3)) * I]
for k in range(3):
    eq(c + 2 * om3 ** k, verts[k])
eq(sum(verts), 3 * c); eq(Abs(verts[1] - verts[0]), Abs(verts[2] - verts[1])); eq(Abs(verts[0] - verts[2]), Abs(verts[2] - verts[1]))
# Worked example 5
same_poly((1 + z) ** 4 - z ** 4, 4 * z ** 3 + 6 * z ** 2 + 4 * z + 1)
for r in (-R(1, 2), (-1 - I) / 2, (-1 + I) / 2):
    eq(expand((1 + r) ** 4 - r ** 4), 0); eq(sp.re(r), -R(1, 2))
eq(1 / (I - 1), (-1 - I) / 2); eq(1 / (-I - 1), (-1 + I) / 2)
# Worked example 6
cr = [2 * exp(I * pi / 3), -2, 2 * exp(-I * pi / 3)]
is_root_set(3, -8, cr)
sqs = [expand(sp.nsimplify(sp.expand_complex(r ** 2))) for r in cr]
assert {sp.nsimplify(s) for s in sqs} == {4, -2 + 2 * sqrt(3) * I, -2 - 2 * sqrt(3) * I}; N += 1

# Practice
is_root_set(3, 27, [3, -R(3, 2) + 3 * sqrt(3) / 2 * I, -R(3, 2) - 3 * sqrt(3) / 2 * I])
is_root_set(4, 16 * I, [2 * exp(I * a) for a in (pi / 8, 5 * pi / 8, -3 * pi / 8, -7 * pi / 8)])
is_root_set(5, -32, [2 * exp(I * a) for a in (pi / 5, 3 * pi / 5, pi, -pi / 5, -3 * pi / 5)])
w4 = -4 * sqrt(2) + 4 * sqrt(2) * I; eq(Abs(w4), 8); eq(arg(w4), 3 * pi / 4)
is_root_set(3, w4, [sqrt(2) + sqrt(2) * I, 2 * exp(11 * I * pi / 12), 2 * exp(-5 * I * pi / 12)])
six = [1, -1, R(1, 2) + sqrt(3) / 2 * I, R(1, 2) - sqrt(3) / 2 * I, -R(1, 2) + sqrt(3) / 2 * I, -R(1, 2) - sqrt(3) / 2 * I]
is_root_set(6, 1, six); eq(Abs(1 - six[2]), 1)
eq(1 + om3 + om3 ** 2, 0); eq((1 + om3) * (1 + om3 ** 2), 1); eq((1 + om3 ** 2) ** 4, om3)
c = 1 - I; a = 4 + I
eq(c + I * (a - c), -1 + 2 * I); eq(c - (a - c), -2 - 3 * I); eq(c - I * (a - c), 3 - 4 * I)
for sg in (1, -1):
    t3 = 4 * exp(sg * I * pi / 3); eq(t3, 2 + sg * 2 * sqrt(3) * I); eq(Abs(t3 - 4), 4)
same_poly((z ** 2 - 1) * (z ** 2 + z + 1) * (z ** 2 - z + 1), z ** 6 - 1)
for r in (3, 2 + I, 1, 2 - I):
    eq(expand((r - 2) ** 4), 1)
is_root_set(3, -8 * I, [sqrt(3) - I, 2 * I, -sqrt(3) - I])

# Exam 1
w = sp.symbols("w")
same_poly(expand((w ** 3 - 3 * w) + (w ** 2 - 2) + w + 1), w ** 3 + w ** 2 - 2 * w - 1)
zs = sp.symbols("zs")
same_poly(expand((zs + 1 / zs) ** 3 - 3 * (zs + 1 / zs)), zs ** 3 + zs ** -3)
for k in (1, 2, 3):
    wk = 2 * cos(2 * k * pi / 7); assert abs(complex(sp.N(wk ** 3 + wk ** 2 - 2 * wk - 1))) < 1e-25
N += 1
eq(cos(2 * pi / 7) + cos(4 * pi / 7) + cos(6 * pi / 7), -R(1, 2))
assert abs(float(cos(2 * pi / 7) * cos(4 * pi / 7) * cos(6 * pi / 7)) - 1 / 8) < 1e-14; N += 1
# Exam 2
hexr = [sqrt(3) + I, sqrt(3) - I, -sqrt(3) + I, -sqrt(3) - I, 2 * I, -2 * I]
is_root_set(6, -64, hexr)
same_poly((z ** 2 + 4) * (z ** 2 - 2 * sqrt(3) * z + 4) * (z ** 2 + 2 * sqrt(3) * z + 4), z ** 6 + 64)
eq(6 * sqrt(3) / 4 * 2 ** 2, 6 * sqrt(3))
# Exam 3
eq(om3 ** 2, -exp(I * pi / 3))
av, bv = sp.symbols("a b")
cv = av + (bv - av) * exp(I * pi / 3)
eq(sp.expand_complex(av + om3 * bv + om3 ** 2 * cv), 0)
a, b = 1 + I, 5 + I
cc = a + (b - a) * exp(I * pi / 3); eq(cc, 3 + (1 + 2 * sqrt(3)) * I); eq(a + om3 * b + om3 ** 2 * cc, 0)
eq(Abs(cc - a), 4); eq(Abs(cc - b), 4)
# Exam 4
t = sp.symbols("t", real=True)
fexpr = 1 / (exp(I * t) - 1) - (-R(1, 2) - I / 2 * cot(t / 2))
for tv in (0.4, 1.3, 2.7, 4.1):
    assert abs(complex(fexpr.subs(t, tv))) < 1e-12
N += 1
same_poly(expand((z + 1) ** 5 - z ** 5), 5 * z ** 4 + 10 * z ** 3 + 10 * z ** 2 + 5 * z + 1)
for k in (1, 2, 3, 4):
    r = -R(1, 2) - I / 2 * cot(k * pi / 5)
    assert abs(complex(sp.N((r + 1) ** 5 - r ** 5, 30))) < 1e-20
N += 1

assert len(UNIT["practice"]) == len(UNIT["answers"]) == 12 and len(UNIT["exam"]) == len(UNIT["exam_answers"]) == 4
print(f"pb02: all {N} checks passed")
