"""Verifies every result stated in pure/pb01.py (Unit B1: Euler's form and de Moivre's theorem)."""
import os
import sys

import numpy as np
import sympy as sp
from sympy import I, pi, sqrt, cos, sin, tan, exp, Abs, arg, expand, simplify, binomial, Rational as R

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pure.pb01 import UNIT  # noqa: E402

N = 0
th = sp.symbols("theta", real=True)
c, s, t = sp.symbols("c s t")


def eq(a, b, msg=""):
    global N
    d = sp.nsimplify(a) - sp.nsimplify(b)
    ok = simplify(expand(d)) == 0
    if not ok:  # numerical fallback
        ok = abs(complex(sp.N(d, 40))) < 1e-30
    assert ok, f"{msg}: {a} != {b}"
    N += 1


def ident(lhs, rhs, var=th, msg=""):
    """Identity in var: check symbolically and at random points."""
    global N
    f = sp.lambdify(var, lhs - rhs, "numpy")
    for v in np.linspace(0.13, 2.9, 11):
        assert abs(complex(f(v))) < 1e-10, f"{msg} fails at {v}"
    N += 1


def modarg(zv, r, a):
    eq(Abs(zv), r); eq(arg(zv), a)


# Notes
eq(exp(I * pi), -1); eq(exp(I * pi / 2), I); eq(exp(2 * pi * I), 1); eq(exp(13 * pi * I / 6), exp(pi * I / 6))
ident(cos(th), (exp(I * th) + exp(-I * th)) / 2); ident(sin(th), (exp(I * th) - exp(-I * th)) / (2 * I))
# Maclaurin real/imag parts agree to order 9
ser = sp.series(exp(I * th), th, 0, 10).removeO()
eq(sp.re(ser.subs(th, sp.Symbol('u', real=True))) - sp.series(cos(sp.Symbol('u', real=True)), sp.Symbol('u', real=True), 0, 10).removeO(), 0)
# de Moivre for integer n incl. negative
for n in range(-6, 8):
    ident((cos(th) + I * sin(th)) ** n, cos(n * th) + I * sin(n * th), msg=f"dM n={n}")
# triple angles
ident(cos(3 * th), 4 * cos(th) ** 3 - 3 * cos(th)); ident(sin(3 * th), 3 * sin(th) - 4 * sin(th) ** 3)
ident(tan(3 * th), (3 * tan(th) - tan(th) ** 3) / (1 - 3 * tan(th) ** 2))
C, S = sp.symbols('C S', real=True)
e3 = expand((C + I * S) ** 3); eq(sp.re(e3) - (C ** 3 - 3 * C * S ** 2), 0); eq(sp.im(e3) - (3 * C ** 2 * S - S ** 3), 0)
ident(cos(th) ** 4, (cos(4 * th) + 4 * cos(2 * th) + 3) / 8)
z = sp.symbols("z")
eq(expand((z + 1 / z) ** 4), z ** 4 + 4 * z ** 2 + 6 + 4 * z ** -2 + z ** -4)
ident(1 + exp(I * th), 2 * cos(th / 2) * exp(I * th / 2)); ident(exp(I * th) - 1, 2 * I * sin(th / 2) * exp(I * th / 2))
n_ = 5
ident(sum(binomial(n_, r) * exp(I * r * th) for r in range(n_ + 1)), (1 + exp(I * th)) ** n_)

# Worked example 1
modarg(sqrt(3) + I, 2, pi / 6); eq(expand((sqrt(3) + I) ** 9), -512 * I)
eq((1 - I) ** -6, -I / 8); eq(expand((1 - I) ** 2), -2 * I); eq(expand((1 - I) ** 6), 8 * I)
# Worked example 2
w = 1 + sqrt(3) * I; modarg(w, 2, pi / 3)
eq(w * I, -sqrt(3) + I); eq(expand(w * (1 + I)), (1 - sqrt(3)) + (1 + sqrt(3)) * I)
# area of image = |w|^2 * 1 = 4 (shoelace)
pts = [complex(sp.N(w * p)) for p in (0, 1, 1 + I, I)]
area = 0.5 * abs(sum(pts[k].real * pts[(k + 1) % 4].imag - pts[(k + 1) % 4].real * pts[k].imag for k in range(4)))
assert abs(area - 4) < 1e-12; N += 1
# Worked example 3
ident(cos(5 * th), 16 * cos(th) ** 5 - 20 * cos(th) ** 3 + 5 * cos(th))
C, S = sp.symbols("C S", real=True)
re5 = sp.re(expand((C + I * S) ** 5)); eq(re5 - (C ** 5 - 10 * C ** 3 * S ** 2 + 5 * C * S ** 4), 0)
eq(expand(re5.subs(S ** 2, 1 - C ** 2).subs(S ** 4, (1 - C ** 2) ** 2)), 16 * C ** 5 - 20 * C ** 3 + 5 * C)
eq(cos(pi / 10) ** 2, (5 + sqrt(5)) / 8); eq(cos(3 * pi / 10) ** 2, (5 - sqrt(5)) / 8)
assert f"{float((5 + sqrt(5)) / 8):.3f}" == "0.905" and f"{float((5 - sqrt(5)) / 8):.3f}" == "0.345"; N += 1
# Worked example 4
ident(tan(4 * th), (4 * tan(th) - 4 * tan(th) ** 3) / (1 - 6 * tan(th) ** 2 + tan(th) ** 4))
e4 = expand((C + I * S) ** 4)
eq(sp.re(e4) - (C ** 4 - 6 * C ** 2 * S ** 2 + S ** 4), 0); eq(sp.im(e4) - (4 * C ** 3 * S - 4 * C * S ** 3), 0)
q = t ** 4 + 4 * t ** 3 - 6 * t ** 2 - 4 * t + 1
eq(expand((4 * t - 4 * t ** 3) - (1 - 6 * t ** 2 + t ** 4) + q), 0)
rts = sorted(float(tan(k * pi / 16)) for k in (1, 5, 9, 13))
num = sorted(np.roots([1, 4, -6, -4, 1]).real)
assert np.allclose(rts, num); N += 1
# Worked example 5
eq(expand((z - 1 / z) ** 6), z ** 6 - 6 * z ** 4 + 15 * z ** 2 - 20 + 15 * z ** -2 - 6 * z ** -4 + z ** -6)
eq((2 * I) ** 6, -64)
ident(sin(th) ** 6, (10 - 15 * cos(2 * th) + 6 * cos(4 * th) - cos(6 * th)) / 32)
eq(sp.integrate(sin(th) ** 6, (th, 0, pi / 2)), 5 * pi / 32)
# Worked example 6
nn = sp.symbols("n", integer=True, positive=True)
for n_ in range(1, 7):
    ident(sum(binomial(n_, r) * cos(r * th) for r in range(n_ + 1)), 2 ** n_ * cos(th / 2) ** n_ * cos(n_ * th / 2))
    ident(sum(binomial(n_, r) * sin(r * th) for r in range(n_ + 1)), 2 ** n_ * cos(th / 2) ** n_ * sin(n_ * th / 2))
eq(1 + 2 * cos(pi / 2) + cos(pi), 0)

# Practice
modarg(-4, 4, pi); modarg(1 - sqrt(3) * I, 2, -pi / 3); modarg(3 * I, 3, pi / 2)
eq(4 * exp(5 * I * pi / 6), -2 * sqrt(3) + 2 * I); eq(sqrt(2) * exp(-I * pi / 4), 1 - I); eq(exp(I * pi) + exp(-I * pi / 2), -1 - I)
zz, ww = 3 * exp(I * pi / 4), 2 * exp(I * pi / 3)
modarg(zz * ww, 6, 7 * pi / 12); modarg(zz / ww, R(3, 2), -pi / 12); eq(zz ** 4, -81); modarg(sp.conjugate(ww), 2, -pi / 3)
eq((cos(pi / 9) + I * sin(pi / 9)) ** 6, -R(1, 2) + sqrt(3) / 2 * I)
ident((cos(th) + I * sin(th)) ** 5 / (cos(2 * th) - I * sin(2 * th)) ** 3, cos(11 * th) + I * sin(11 * th))
eq(expand((1 + I) ** 10), 32 * I); eq((1 - sqrt(3) * I) ** -4, -R(1, 32) - sqrt(3) / 32 * I)
modarg(3 * I, 3, pi / 2); modarg(1 - I, sqrt(2), -pi / 4)
ident(cos(th) ** 3, (cos(3 * th) + 3 * cos(th)) / 4)
eq(expand((z + 1 / z) ** 3), z ** 3 + 3 * z + 3 / z + z ** -3)
eq(sp.integrate(cos(th) ** 3, (th, 0, pi / 3)), 3 * sqrt(3) / 8)
ident(sin(th) ** 4, (cos(4 * th) - 4 * cos(2 * th) + 3) / 8)
eq(expand((z - 1 / z) ** 4), z ** 4 - 4 * z ** 2 + 6 - 4 * z ** -2 + z ** -4)
ident(Abs(1 + exp(I * th)), 2 * cos(th / 2))  # 0 < th < pi in sample range up to 2.9
ident(1 / (1 - exp(I * th) / 2), 2 * (2 - cos(th) + I * sin(th)) / (5 - 4 * cos(th)))
f = sp.lambdify(th, sum((0.5) ** r * cos(r * th) for r in range(80)) - (4 - 2 * cos(th)) / (5 - 4 * cos(th)))
assert abs(f(1.1)) < 1e-12; N += 1
f = sp.lambdify(th, sum((0.5) ** r * sin(r * th) for r in range(80)) - 2 * sin(th) / (5 - 4 * cos(th)))
assert abs(f(2.3)) < 1e-12; N += 1

# Exam 1
eq((1 + I) ** -8, R(1, 16))
# Exam 2
ident(sin(5 * th), 16 * sin(th) ** 5 - 20 * sin(th) ** 3 + 5 * sin(th))
eq(sp.im(expand((C + I * S) ** 5)) - (5 * C ** 4 * S - 10 * C ** 2 * S ** 3 + S ** 5), 0)
xs = sp.symbols("x")
for k in (1, 2):
    for sg in (1, -1):
        eq((16 * xs ** 4 - 20 * xs ** 2 + 5).subs(xs, sg * sin(k * pi / 5)), 0)
eq(sin(pi / 5) ** 2 * sin(2 * pi / 5) ** 2, R(5, 16))
# Exam 3
ident(cos(th) ** 5, (cos(5 * th) + 5 * cos(3 * th) + 10 * cos(th)) / 16)
eq(sp.integrate(cos(th) ** 5, (th, 0, pi / 2)), R(8, 15)); eq(R(1, 16) * (R(1, 5) - R(5, 3) + 10), R(8, 15))
# Exam 4
for n_ in range(2, 9):
    zq = exp(I * pi / n_)
    eq(sum(zq ** r for r in range(n_)), 2 / (1 - zq)); eq(2 / (1 - zq), 1 + I * sp.cot(pi / (2 * n_)))
    eq(sum(sin(r * pi / n_) for r in range(n_)), sp.cot(pi / (2 * n_))); eq(sum(cos(r * pi / n_) for r in range(n_)), 1)
ident(1 - exp(I * th), -2 * I * sin(th / 2) * exp(I * th / 2))

assert len(UNIT["practice"]) == len(UNIT["answers"]) == 12 and len(UNIT["exam"]) == len(UNIT["exam_answers"]) == 4
print(f"pb01: all {N} checks passed")
