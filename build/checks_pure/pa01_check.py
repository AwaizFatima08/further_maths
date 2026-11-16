"""Verifies every result stated in pure/pa01.py (Unit A1: complex arithmetic and complex roots)."""
import os
import sys

import sympy as sp
from sympy import I, expand, simplify, sqrt

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pure.pa01 import UNIT  # noqa: E402


def _text(o):
    if isinstance(o, str):
        return o
    if isinstance(o, dict):
        return " ".join(_text(v) for v in o.values())
    if isinstance(o, (list, tuple)):
        return " ".join(_text(v) for v in o)
    return str(o)


TEXT = _text(UNIT)
z = sp.symbols("z")
N = 0


def eq(a, b, msg=""):
    global N
    assert simplify(sp.nsimplify(a) - sp.nsimplify(b)) == 0, f"{msg}: {a} != {b}"
    N += 1


def has(*strings):
    global N
    for s in strings:
        assert s in TEXT, f"not in unit text: {s!r}"
        N += 1


def roots_are(poly, expected, msg=""):
    """poly (in z) has exactly the expected roots (with multiplicity)."""
    global N
    sols = sp.roots(sp.Poly(poly, z))
    flat = []
    for r, m in sols.items():
        flat += [sp.simplify(r)] * m
    assert len(flat) == sp.degree(poly, z), f"{msg}: not all roots found"
    rem = list(expected)
    for r in flat:
        for e in rem:
            if simplify(r - e) == 0:
                rem.remove(e)
                break
        else:
            raise AssertionError(f"{msg}: unexpected root {r}")
    assert not rem, f"{msg}: missing {rem}"
    N += 1


def same_poly(a, b, msg=""):
    global N
    assert expand(a - b) == 0, f"{msg}: {expand(a)} != {expand(b)}"
    N += 1


# Notes
eq(I ** 10, -1); eq(I ** 23, -I); eq(1 / I, -I); eq(sqrt(-12), 2 * sqrt(3) * I)
eq((3 + 2 * I) + (1 - 5 * I), 4 - 3 * I); eq(expand((3 + 2 * I) * (1 - 5 * I)), 13 - 13 * I)
a, b, c, d, x, y, u, v = sp.symbols("a b c d x y u v", real=True)
eq(expand((a + I * b) * (c - I * d)), (a * c + b * d) + I * (b * c - a * d))
eq(expand((x + I * y) * (x - I * y)), x ** 2 + y ** 2)
zz, ww = x + I * y, u + I * v
eq(sp.conjugate(expand(zz * ww)), expand(sp.conjugate(zz) * sp.conjugate(ww)))
eq(sp.conjugate(zz / ww), sp.conjugate(zz) / sp.conjugate(ww))
roots_are(z ** 2 - 4 * z + 13, [2 + 3 * I, 2 - 3 * I])
roots_are(z ** 2 - I * z, [0, I])
same_poly((z ** 2 - 2 * z + 5) * (z + 3), z ** 3 + z ** 2 - z + 15)

# Worked example 1
Z, W = 3 - 2 * I, 1 + 4 * I
eq(expand(Z * W), 11 + 10 * I); eq(Z / W, sp.Rational(-5, 17) - sp.Rational(14, 17) * I)
eq(expand(Z ** 2), 5 - 12 * I); eq(expand(Z ** 2) - sp.conjugate(W), 4 - 8 * I)
has("11 + 10i", "−5/17 − (14/17)i", "4 − 8i")
# Worked example 2
zc = 2 + I
eq(2 * zc + I * sp.conjugate(zc), 5 + 4 * I)
sol = sp.solve([2 * x + y - 5, x + 2 * y - 4], [x, y]); assert sol == {x: 2, y: 1}
# Worked example 3
eq(expand((3 - 2 * I) ** 2), 5 - 12 * I); assert abs(sqrt(5 ** 2 + 12 ** 2) - 13) == 0
disc = expand((1 + 2 * I) ** 2 - 4 * (-2 + 4 * I)); eq(disc, 5 - 12 * I)
roots_are(z ** 2 - (1 + 2 * I) * z - 2 + 4 * I, [2, -1 + 2 * I])
# Worked example 4
f4 = z ** 3 - 6 * z ** 2 + 21 * z - 26
eq(f4.subs(z, 2), 0); same_poly((z - 2) * (z ** 2 - 4 * z + 13), f4); roots_are(f4, [2, 2 + 3 * I, 2 - 3 * I])
# Worked example 5
eq(expand((1 + 2 * I) ** 2), -3 + 4 * I); eq(expand((1 + 2 * I) ** 3), -11 - 2 * I)
same_poly((z - 1 - 2 * I) * (z - 1 + 2 * I), z ** 2 - 2 * z + 5)
A, B = sp.symbols("A B")
expr = expand((1 + 2 * I) ** 3 + A * (1 + 2 * I) ** 2 + B * (1 + 2 * I) + 15)
re_part, im_part = expr.coeff(I, 0), expr.coeff(I, 1)
same_poly(re_part, 4 - 3 * A + B); same_poly(im_part, -2 + 4 * A + 2 * B)
assert sp.solve([re_part, im_part], [A, B]) == {A: 1, B: -1}; N += 1
roots_are(z ** 3 + z ** 2 - z + 15, [1 + 2 * I, 1 - 2 * I, -3])
# Worked example 6
f6 = z ** 4 - 6 * z ** 3 + 18 * z ** 2 - 30 * z + 25
same_poly((z ** 2 - 4 * z + 5) * (z ** 2 - 2 * z + 5), f6); roots_are(f6, [2 + I, 2 - I, 1 + 2 * I, 1 - 2 * I])

# Practice
eq(I ** 3, -I); eq(I ** 4, 1); eq(I ** 10, -1); eq(1 / I, -I); eq(I ** 23, -I)
Z, W = 4 + 3 * I, 2 - I
eq(Z + W, 6 + 2 * I); eq(Z - 2 * W, 5 * I); eq(expand(Z * W), 11 + 2 * I); eq(expand(sp.conjugate(Z) * W), 5 - 10 * I)
eq((5 + I) / (2 - 3 * I), sp.Rational(7, 13) + sp.Rational(17, 13) * I); eq(1 / (1 + I) ** 2, -I / 2)
eq((3 + 4 * I) / I, 4 - 3 * I)
eq((7 + 9 * I) / (3 + I), 3 + 2 * I)
zc = 2 + 3 * I; eq(zc + 3 * sp.conjugate(zc), 8 - 6 * I)
eq(expand((1 + 4 * I) ** 2), -15 + 8 * I); eq(expand((2 * sqrt(3) * (1 + I)) ** 2), 24 * I)
roots_are(z ** 2 + 6 * z + 13, [-3 + 2 * I, -3 - 2 * I])
roots_are(2 * z ** 2 - 2 * z + 5, [sp.Rational(1, 2) + sp.Rational(3, 2) * I, sp.Rational(1, 2) - sp.Rational(3, 2) * I])
roots_are(z ** 2 - 6 * z + 34, [3 + 5 * I, 3 - 5 * I])
f9 = z ** 3 - z ** 2 + 2; eq(f9.subs(z, -1), 0); same_poly((z + 1) * (z ** 2 - 2 * z + 2), f9)
roots_are(f9, [-1, 1 + I, 1 - I])
same_poly((z ** 2 + 2 * z + 2) * (z - 2), z ** 3 - 2 * z - 4); roots_are(z ** 3 - 2 * z - 4, [2, -1 + I, -1 - I])
f11 = z ** 4 + 4 * z ** 3 + 9 * z ** 2 + 4 * z + 8
same_poly((z ** 2 + 1) * (z ** 2 + 4 * z + 8), f11); roots_are(f11, [I, -I, -2 + 2 * I, -2 - 2 * I])
for zc in (3 + 4 * I, 3 - 4 * I):
    eq(zc + sp.conjugate(zc), 6); eq(expand(zc * sp.conjugate(zc)), 25)

# Exam 1
fE = z ** 4 - 2 * z ** 3 + 6 * z ** 2 - 2 * z + 5
eq(fE.subs(z, I), 0); same_poly((z ** 2 + 1) * (z ** 2 - 2 * z + 5), fE)
rts = [I, -I, 1 + 2 * I, 1 - 2 * I]; roots_are(fE, rts); eq(sum(expand(r ** 2) for r in rts), -8)
# Exam 2
z1, z2 = 3 + 4 * I, 1 - 2 * I
eq(expand(z1 * z2), 11 - 2 * I); eq(z1 / z2, -1 + 2 * I); eq(expand((2 + I) ** 2), z1)
eq(expand(4 + 8 + 16 * I - 4 * (3 + 4 * I)), 0)
w = sp.symbols("w"); roots_are((w ** 2 - 2 * w - 2 - 4 * I).subs(w, z), [3 + I, -1 - I])
# Exam 3
same_poly((z - 2 + 3 * I) * (z - 2 - 3 * I), z ** 2 - 4 * z + 13)
same_poly((z ** 2 - 4 * z + 13) * (2 * z + 3), 2 * z ** 3 - 5 * z ** 2 + 14 * z + 39)
roots_are(2 * z ** 3 - 5 * z ** 2 + 14 * z + 39, [2 + 3 * I, 2 - 3 * I, sp.Rational(-3, 2)])
# Exam 4
eq(expand((1 + I) ** 2), 2 * I); eq(expand((1 + I) ** 4), -4)
same_poly((z ** 2 - 2 * z + 2) * (z ** 2 + 2 * z + 2), z ** 4 + 4)
roots_are(z ** 4 + 4, [1 + I, 1 - I, -1 + I, -1 - I])

assert len(UNIT["practice"]) == len(UNIT["answers"]) == 12 and len(UNIT["exam"]) == len(UNIT["exam_answers"]) == 4
print(f"pa01: all {N} checks passed")
