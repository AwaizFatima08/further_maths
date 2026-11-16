"""Verifies every derivative, integral and exact value stated in pure/pb05.py (B5 Calculus of hyperbolic and inverse functions)."""
import importlib
import random
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
MODULE = "pb05"
UNIT = importlib.import_module(f"pure.{MODULE}").UNIT


def _flat(o):
    if isinstance(o, str):
        return [o]
    if isinstance(o, dict):
        return [s for v in o.values() for s in _flat(v)]
    if isinstance(o, (list, tuple)):
        return [s for v in o for s in _flat(v)]
    return [str(o)]


TEXT = "\n".join(_flat(UNIT))
COUNT = 0
x = sp.symbols("x", real=True)
k = sp.symbols("k", positive=True)


def zero(expr, lo=-0.9, hi=0.9, sym=x):
    """expr == 0 identically on (lo, hi): symbolic attempt plus numeric spot checks."""
    global COUNT
    e = sp.simplify(expr)
    if e != 0:
        for _ in range(15):
            v = random.uniform(lo, hi)
            val = complex(sp.N(expr.subs(sym, v), 30))
            assert abs(val) < 1e-10, f"not zero at {v}: {expr} -> {val}"
    COUNT += 1


def deriv(f, stated, lo=-0.9, hi=0.9):
    zero(sp.diff(f, x) - stated, lo, hi)


def antideriv(F, integrand, lo=-0.9, hi=0.9):
    zero(sp.diff(F, x) - integrand, lo, hi)


def same(a, b, tol=1e-15):
    global COUNT
    assert abs(sp.N(sp.sympify(a) - sp.sympify(b), 40)) < tol, f"{a} != {b}"
    COUNT += 1


def has(*snips):
    global COUNT
    for s in snips:
        assert s in TEXT, f"{s!r} not found in {MODULE}"
        COUNT += 1


sh, ch, th = sp.sinh, sp.cosh, sp.tanh
sech = lambda t: 1 / ch(t)  # noqa: E731
cosech = lambda t: 1 / sh(t)  # noqa: E731
coth = lambda t: 1 / th(t)  # noqa: E731

# 5.1 facts
for v in (-1, -0.3, 0.2, 0.8, 1):
    same(sp.asin(v) + sp.acos(v), sp.pi / 2)
    same(sp.acos(-sp.Float(v)), sp.pi - sp.acos(v))

# 5.2 inverse trig derivatives (+ chain-rule forms)
deriv(sp.asin(x), 1 / sp.sqrt(1 - x ** 2))
deriv(sp.acos(x), -1 / sp.sqrt(1 - x ** 2))
deriv(sp.atan(x), 1 / (1 + x ** 2), -5, 5)
a = sp.Integer(3)
deriv(sp.asin(x / a), 1 / sp.sqrt(a ** 2 - x ** 2), -2.9, 2.9)
deriv(sp.atan(x / a), a / (a ** 2 + x ** 2), -5, 5)

# 5.3 hyperbolic derivatives
deriv(sh(x), ch(x), -3, 3)
deriv(ch(x), sh(x), -3, 3)
deriv(th(x), sech(x) ** 2, -3, 3)
deriv(sech(x), -sech(x) * th(x), -3, 3)
deriv(cosech(x), -cosech(x) * coth(x), 0.1, 3)
deriv(coth(x), -cosech(x) ** 2, 0.1, 3)
deriv(sh(k * x).subs(k, 5), 5 * ch(5 * x), -1, 1)
deriv(ch(k * x).subs(k, 5), 5 * sh(5 * x), -1, 1)

# 5.4 inverse hyperbolic derivatives, including via log form
deriv(sp.asinh(x), 1 / sp.sqrt(x ** 2 + 1), -5, 5)
deriv(sp.acosh(x), 1 / sp.sqrt(x ** 2 - 1), 1.01, 6)
deriv(sp.atanh(x), 1 / (1 - x ** 2))
deriv(sp.log(x + sp.sqrt(x ** 2 + 1)), 1 / sp.sqrt(x ** 2 + 1), -5, 5)
zero((1 + x / sp.sqrt(x ** 2 + 1)) / (x + sp.sqrt(x ** 2 + 1)) - 1 / sp.sqrt(x ** 2 + 1), -5, 5)

# 5.5 standard integrals and techniques
antideriv(ch(5 * x) / 5, sh(5 * x), -1, 1)
antideriv(sh(5 * x) / 5, ch(5 * x), -1, 1)
antideriv(th(5 * x) / 5, sech(5 * x) ** 2, -1, 1)
antideriv(sp.log(ch(x)), th(x), -3, 3)
antideriv(sp.log(sh(x)), coth(x), 0.1, 3)
antideriv(-coth(x), cosech(x) ** 2, 0.1, 3)
antideriv(-sech(x), sech(x) * th(x), -3, 3)
antideriv(-cosech(x), cosech(x) * coth(x), 0.1, 3)
antideriv(2 * sp.atan(sp.exp(x)), sech(x), -3, 3)
zero(sh(x) ** 2 - (ch(2 * x) - 1) / 2, -3, 3)
zero(ch(x) ** 2 - (ch(2 * x) + 1) / 2, -3, 3)
antideriv(sh(2 * x) / 4 - x / 2, sh(x) ** 2, -3, 3)
antideriv(sh(x) + sh(x) ** 3 / 3, ch(x) ** 3, -3, 3)
antideriv(sp.exp(2 * x) / 4 - x / 2, sp.exp(x) * sh(x), -3, 3)
antideriv(x * sh(x) - ch(x), x * ch(x), -3, 3)
has("¼ sinh 2x − ½x + C", "sinh x + ⅓ sinh³x + C", "¼e²ˣ − ½x + C", "x sinh x − cosh x + C", "2 arctan(eˣ) + C")

# 5.6 integrals of inverse functions (table)
antideriv(x * sp.asin(x) + sp.sqrt(1 - x ** 2), sp.asin(x))
antideriv(x * sp.atan(x) - sp.log(1 + x ** 2) / 2, sp.atan(x), -5, 5)
antideriv(x * sp.asinh(x) - sp.sqrt(1 + x ** 2), sp.asinh(x), -5, 5)
antideriv(x * sp.acosh(x) - sp.sqrt(x ** 2 - 1), sp.acosh(x), 1.01, 6)
antideriv(x * sp.atanh(x) + sp.log(1 - x ** 2) / 2, sp.atanh(x))
has("x arcsin x + √(1 − x²)", "x arctan x − ½ ln(1 + x²)", "x arsinh x − √(1 + x²)", "x arcosh x − √(x² − 1)",
    "x artanh x + ½ ln(1 − x²)")

# Worked example 1
deriv(sp.asin(x) + x * sp.sqrt(1 - x ** 2), 2 * sp.sqrt(1 - x ** 2))
# Worked example 2
deriv(sp.atanh(x ** 2), 2 * x / (1 - x ** 4))
deriv(sp.atan(3 * x), 3 / (1 + 9 * x ** 2), -3, 3)
deriv(sp.acosh(2 * x), 2 / sp.sqrt(4 * x ** 2 - 1), 0.51, 4)
deriv(sp.log(th(x)), 2 / sh(2 * x), 0.1, 3)
zero(sech(x) ** 2 / th(x) - 1 / (sh(x) * ch(x)), 0.1, 3)
# Worked example 3
deriv(sp.log(x + sp.sqrt(x ** 2 - 1)), 1 / sp.sqrt(x ** 2 - 1), 1.01, 6)
# Worked example 4
I4a = sp.integrate(ch(x) ** 2, (x, 0, sp.log(2)))
same(I4a, sp.log(2) / 2 + sp.Rational(15, 32))
same(sh(2 * sp.log(2)), sp.Rational(15, 8))
I4b = sp.integrate(sp.exp(x) * sh(x), (x, 0, sp.log(3)))
same(I4b, 2 - sp.log(3) / 2)
has("½ ln 2 + 15/32", "2 − ½ ln 3")
# Worked example 5
I5 = sp.Integral(sp.asinh(x), (x, 0, sp.Rational(3, 4))).evalf(30)
same(I5, sp.Rational(3, 4) * sp.log(2) - sp.Rational(1, 4), 1e-25)
assert round(float(I5), 3) == 0.270
COUNT += 1
has("(3/4) ln 2 − ¼ ≈ 0.270")
# Worked example 6
f6 = 5 * ch(x) - 3 * sh(x)
same(sp.atanh(sp.Rational(3, 5)), sp.log(2))
assert abs(sp.N(sp.diff(f6, x).subs(x, sp.log(2)))) < 1e-30
same(f6.subs(x, sp.log(2)), 4)
same(sp.diff(f6, x, 2).subs(x, sp.log(2)), 4)
same(sp.integrate(f6, (x, 0, sp.log(2))), 3)

# Practice answers
deriv(sh(4 * x), 4 * ch(4 * x), -2, 2)
deriv(ch(x ** 2), 2 * x * sh(x ** 2), -2, 2)
deriv(th(3 * x), 3 * sech(3 * x) ** 2, -2, 2)
deriv(x ** 2 * sh(x), 2 * x * sh(x) + x ** 2 * ch(x), -2, 2)
deriv(sp.exp(2 * x) * ch(x), sp.exp(2 * x) * (2 * ch(x) + sh(x)), -2, 2)
deriv(sp.asin(2 * x), 2 / sp.sqrt(1 - 4 * x ** 2), -0.49, 0.49)
deriv(sp.atan(x / 3), 3 / (9 + x ** 2), -5, 5)
deriv(sp.acos(x ** 2), -2 * x / sp.sqrt(1 - x ** 4))
deriv(sp.asinh(3 * x), 3 / sp.sqrt(1 + 9 * x ** 2), -3, 3)
deriv(sp.acosh(x ** 2), 2 * x / sp.sqrt(x ** 4 - 1), 1.01, 4)
deriv(sp.atanh(2 * x), 2 / (1 - 4 * x ** 2), -0.49, 0.49)
antideriv(sh(3 * x) / 3, ch(3 * x), -2, 2)
antideriv(2 * ch(x / 2), sh(x / 2), -2, 2)
antideriv(th(2 * x) / 2, sech(2 * x) ** 2, -2, 2)
same(sp.integrate(sh(x), (x, 0, sp.log(3))), sp.Rational(2, 3))
antideriv(ch(x) ** 3 / 3 - ch(x), sh(x) ** 3, -2, 2)
P12 = sp.integrate(sp.asin(x), (x, 0, sp.Rational(1, 2)))
same(P12, sp.pi / 12 + sp.sqrt(3) / 2 - 1)
assert round(float(P12), 3) == 0.128
COUNT += 1

# Section B Q1
f1 = x * sp.atan(x) - sp.log(1 + x ** 2) / 2
deriv(f1, sp.atan(x), -5, 5)
B1 = sp.integrate(sp.atan(x), (x, 0, sp.sqrt(3)))
same(B1, sp.pi * sp.sqrt(3) / 3 - sp.log(2))
assert round(float(B1), 2) == 1.12
COUNT += 1
# Section B Q2
y = sp.asinh(x) ** 2
zero((1 + x ** 2) * sp.diff(y, x) ** 2 - 4 * y, -3, 3)
zero((1 + x ** 2) * sp.diff(y, x, 2) + x * sp.diff(y, x) - 2, -3, 3)
zero((1 + x ** 2) * sp.diff(y, x, 3) + 3 * x * sp.diff(y, x, 2) + sp.diff(y, x), -3, 3)
zero((1 + x ** 2) * sp.diff(y, x, 4) + 5 * x * sp.diff(y, x, 3) + 4 * sp.diff(y, x, 2), -3, 3)
ser = sp.series(y, x, 0, 5).removeO()
assert sp.expand(ser - (x ** 2 - x ** 4 / 3)) == 0
COUNT += 1
assert [sp.limit(sp.diff(y, x, n), x, 0) for n in range(5)] == [0, 0, 2, 0, -8]
COUNT += 1
# Section B Q3
deriv(sp.atanh(sp.sin(x)), 1 / sp.cos(x), -1.5, 1.5)
same(sp.Integral(1 / sp.cos(x), (x, 0, sp.pi / 6)).evalf(30), sp.log(3) / 2, 1e-25)
deriv(x * sp.sqrt(x ** 2 + 1) + sp.asinh(x), 2 * sp.sqrt(x ** 2 + 1), -3, 3)
B3 = sp.Integral(sp.sqrt(x ** 2 + 1), (x, 0, 1)).evalf(30)
same(B3, (sp.sqrt(2) + sp.log(1 + sp.sqrt(2))) / 2, 1e-25)
assert round(float(B3), 2) == 1.15
COUNT += 1
# Section B Q4
same(sp.integrate(th(x), (x, 0, sp.log(3))), sp.log(sp.Rational(5, 3)))
same(sh(2 * sp.log(3)), sp.Rational(40, 9))
V = sp.pi * sp.integrate(sh(x) ** 2, (x, 0, sp.log(3)))
same(V, sp.pi * (sp.Rational(10, 9) - sp.log(3) / 2))
assert round(float(V), 3) == 1.765
COUNT += 1
has("π√3/3 − ln 2", "x² − x⁴/3", "½(√2 + ln(1 + √2))", "π(10/9 − ½ ln 3)", "π/12 + √3/2 − 1")

print(f"pb05 checks passed: {COUNT} assertions")
