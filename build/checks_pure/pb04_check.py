"""Verifies every identity, equation solution and exact value stated in pure/pb04.py (B4 Hyperbolic functions)."""
import importlib
import random
import sys
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
MODULE = "pb04"
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
x, y, A, B, u = sp.symbols("x y A B u", real=True)


def zero(expr, sym=(x,), lo=-2.0, hi=2.0):
    """expr is identically zero: symbolic simplification, confirmed at random points."""
    global COUNT
    e = sp.simplify(sp.expand(sp.sympify(expr).rewrite(sp.exp)))
    if e != 0:
        for _ in range(12):
            vals = {s: random.uniform(lo, hi) for s in sym}
            assert abs(complex(sp.N(expr.subs(vals)))) < 1e-9, f"not identically zero: {expr}"
    COUNT += 1


def same(a, b, tol=1e-12):
    """Two exact constants are equal (symbolic, with numeric confirmation)."""
    global COUNT
    assert abs(sp.N(sp.sympify(a) - sp.sympify(b), 30)) < tol, f"{a} != {b}"
    COUNT += 1


def has(*snippets):
    global COUNT
    for s in snippets:
        assert s in TEXT, f"{s!r} not found in {MODULE}"
        COUNT += 1


def roots_ok(lhs, rhs, sols, domain_ok=lambda v: True):
    """Each stated solution satisfies lhs = rhs, and there are no other real solutions (checked by nsolve sweep)."""
    global COUNT
    f = sp.lambdify(x, lhs - rhs, "mpmath")
    for s in sols:
        assert abs(sp.N((lhs - rhs).subs(x, s), 30)) < 1e-20, f"{s} does not solve {lhs} = {rhs}"
    found = set()
    for start in [i / 4 for i in range(-40, 41)]:
        try:
            r = sp.nsolve(lhs - rhs, x, start)
            if abs(sp.im(r)) < 1e-12:
                found.add(round(float(sp.re(r)), 8))
        except Exception:
            pass
    stated = {round(float(sp.N(s)), 8) for s in sols}
    assert found <= stated or not found, f"extra roots {found - stated} for {lhs} = {rhs}"
    assert stated <= found | stated
    COUNT += 1


sh, ch, th = sp.sinh, sp.cosh, sp.tanh

# 4.1 definitions and basic facts
zero(sh(x) - (sp.exp(x) - sp.exp(-x)) / 2)
zero(ch(x) - (sp.exp(x) + sp.exp(-x)) / 2)
zero(th(x) - (sp.exp(2 * x) - 1) / (sp.exp(2 * x) + 1))
zero(ch(x) + sh(x) - sp.exp(x))
zero(ch(x) - sh(x) - sp.exp(-x))
zero(ch(-x) - ch(x))
zero(sh(-x) + sh(x))
assert sp.limit(th(x), x, sp.oo) == 1 and sp.limit(th(x), x, -sp.oo) == -1
assert sp.limit(1 / sp.tanh(x), x, sp.oo) == 1
has("(1 − e⁻²ˣ)/(1 + e⁻²ˣ)", "x² − y² = 1")

# 4.4 identities box
zero(ch(x) ** 2 - sh(x) ** 2 - 1)
zero(1 / ch(x) ** 2 - (1 - th(x) ** 2))
zero(1 / sh(x) ** 2 - (1 / th(x) ** 2 - 1), lo=0.2, hi=2)
zero(sh(2 * x) - 2 * sh(x) * ch(x))
for form in (ch(x) ** 2 + sh(x) ** 2, 2 * ch(x) ** 2 - 1, 1 + 2 * sh(x) ** 2):
    zero(ch(2 * x) - form)
for sgn in (1, -1):
    zero(sh(A + sgn * B) - (sh(A) * ch(B) + sgn * ch(A) * sh(B)), sym=(A, B))
    zero(ch(A + sgn * B) - (ch(A) * ch(B) + sgn * sh(A) * sh(B)), sym=(A, B))
zero(th(2 * x) - 2 * th(x) / (1 + th(x) ** 2))
zero(ch(3 * x) - (4 * ch(x) ** 3 - 3 * ch(x)))
zero(sh(3 * x) - (3 * sh(x) + 4 * sh(x) ** 3))
has("cosh²x − sinh²x ≡ 1", "sech²x ≡ 1 − tanh²x", "cosech²x ≡ coth²x − 1", "sinh 3x ≡ 3 sinh x + 4 sinh³x",
    "cosh 3x ≡ 4cosh³x − 3cosh x", "tanh 2x ≡ 2 tanh x/(1 + tanh²x)")

# 4.5 methods: exponential quadratic and harmonic form
a, b, c = sp.symbols("a b c", positive=True)
lhs = (a * ch(x) + b * sh(x) - c).rewrite(sp.exp) * 2 * sp.exp(x)
assert sp.expand(lhs - ((a + b) * u ** 2 - 2 * c * u + (a - b)).subs(u, sp.exp(x))) == 0
COUNT += 1
has("(a + b)u² − 2cu + (a − b) = 0")
R = sp.sqrt(a ** 2 - b ** 2)
alpha = sp.atanh(b / a)
for av, bv in ((5, 4), (13, 5), (7, -3)):
    zero((R * ch(x + alpha)).subs({a: av, b: bv}) - (av * ch(x) + bv * sh(x)))

# 4.6/4.7 logarithmic forms and reciprocal inverses
for v in (-3.5, -0.7, 0, 0.4, 2.2, 10):
    same(sp.asinh(v), sp.log(v + sp.sqrt(v ** 2 + 1)))
for v in (1, 1.3, 2, 7.5):
    same(sp.acosh(v), sp.log(v + sp.sqrt(v ** 2 - 1)))
    same(sp.log(v - sp.sqrt(v ** 2 - 1)), -sp.log(v + sp.sqrt(v ** 2 - 1)))
for v in (-0.9, -0.2, 0.5, 0.95):
    same(sp.atanh(v), sp.log((1 + sp.Rational(1) * v) / (1 - v)) / 2)
for v in (0.2, 0.6, 1):
    same(sp.acosh(1 / sp.Float(v)), sp.asech(v))
for v in (1.5, -3):
    same(sp.atanh(1 / sp.Float(v)), sp.acoth(v))
# quadratic steps in the derivations
zero(((sp.exp(y) - sp.exp(-y)) / 2 - x) * 2 * sp.exp(y) - (sp.exp(2 * y) - 2 * x * sp.exp(y) - 1), sym=(x, y))
zero(((sp.exp(y) + sp.exp(-y)) / 2 - x) * 2 * sp.exp(y) - (sp.exp(2 * y) - 2 * x * sp.exp(y) + 1), sym=(x, y))
zero((x + sp.sqrt(x ** 2 - 1)) * (x - sp.sqrt(x ** 2 - 1)) - 1, lo=1, hi=5)
assert sp.solve(sp.Eq(x * (sp.exp(2 * y) + 1), sp.exp(2 * y) - 1), sp.exp(2 * y)) == [(1 + x) / (1 - x)] or \
    sp.simplify(sp.solve(sp.Eq(x * (u + 1), u - 1), u)[0] - (1 + x) / (1 - x)) == 0
COUNT += 1
has("ln(x + √(x² + 1))", "ln(x + √(x² − 1))", "½ ln((1 + x)/(1 − x))")

# Worked example 2: sinh x = 3/4
X = sp.asinh(sp.Rational(3, 4))
same(X, sp.log(2))
same(ch(X), sp.Rational(5, 4))
same(th(X), sp.Rational(3, 5))
same(1 / ch(X), sp.Rational(4, 5))
same(1 / th(X), sp.Rational(5, 3))
same(ch(2 * X), sp.Rational(17, 8))
has("1 + 2 × 9/16 = 17/8")

# Worked example 3
roots_ok(5 * ch(x) - 3 * sh(x), 5, [0, sp.log(4)])
same(ch(sp.log(4)), sp.Rational(17, 8))
same(sh(sp.log(4)), sp.Rational(15, 8))

# Worked example 4
roots_ok(2 * ch(x) ** 2 - 5 * sh(x), 5, [sp.log(3 + sp.sqrt(10)), sp.log((sp.sqrt(5) - 1) / 2)])
assert round(float(sp.log(3 + sp.sqrt(10))), 3) == 1.818 and round(float(sp.log((sp.sqrt(5) - 1) / 2)), 3) == -0.481
has("x ≈ 1.818", "x ≈ −0.481")

# Worked example 5
same(sp.atanh(sp.Rational(1, 2)), sp.log(3) / 2)
roots_ok(2 * sp.atanh(x), sp.log(3), [sp.Rational(1, 2)])
same(sp.atanh(sp.Rational(1, 3)) + sp.atanh(sp.Rational(1, 5)), sp.atanh(sp.Rational(1, 2)))
same(sp.atanh(sp.Rational(1, 3)), sp.log(2) / 2)
same(sp.atanh(sp.Rational(1, 5)), sp.log(sp.Rational(3, 2)) / 2)

# Worked example 6
same(sp.atanh(sp.Rational(4, 5)), sp.log(3))
zero(3 * ch(x + sp.log(3)) - (5 * ch(x) + 4 * sh(x)))
same(sp.acosh(sp.Rational(5, 3)), sp.log(3))
roots_ok(5 * ch(x) + 4 * sh(x), 5, [0, -2 * sp.log(3)])
fmin = sp.lambdify(x, 5 * ch(x) + 4 * sh(x))
from scipy.optimize import minimize_scalar  # noqa: E402

m = minimize_scalar(fmin)
assert abs(m.x + float(sp.log(3))) < 1e-5 and abs(m.fun - 3) < 1e-9
COUNT += 1

# Practice answers
same(ch(sp.log(3)), sp.Rational(5, 3))
same(sh(sp.log(2)), sp.Rational(3, 4))
same(th(sp.log(4)), sp.Rational(15, 17))
same(sh(-sp.log(5)), -sp.Rational(12, 5))
same(th(-sp.log(5)), -sp.Rational(12, 13))
same(ch(-sp.log(5)), sp.Rational(13, 5))
roots_ok(3 * ch(x) - sh(x), 3, [0, sp.log(2)])
roots_ok(ch(2 * x), 5 * ch(x) - 3, [sp.log(2 + sp.sqrt(3)), -sp.log(2 + sp.sqrt(3))])
same(sp.asinh(2), sp.log(2 + sp.sqrt(5)))
same(sp.acosh(2), sp.log(2 + sp.sqrt(3)))
same(sp.atanh(sp.Rational(1, 3)), sp.log(2) / 2)
same(ch(2 * sp.log(1 + sp.sqrt(2))), 3)
same(sh(sp.log(3)), sp.Rational(4, 3))
has("5/3", "15/17", "−12/13", "x = ±ln(2 + √3)", "ln(2 + √5)", "= 3.", "4/3.")

# Section B Q1
roots_ok(ch(3 * x), 13 * ch(x), [sp.log(2 + sp.sqrt(3)), -sp.log(2 + sp.sqrt(3))])
# Section B Q2
roots_ok(3 * sh(x) ** 2 - 13 * ch(x) + 7, 0, [sp.log(4 + sp.sqrt(15)), -sp.log(4 + sp.sqrt(15))])
assert sp.factor(3 * u ** 2 - 13 * u + 4) == (3 * u - 1) * (u - 4)
COUNT += 1
# Section B Q3
same(sp.atanh(sp.Rational(5, 13)), sp.log(sp.Rational(3, 2)))
zero(12 * ch(x + sp.log(sp.Rational(3, 2))) - (13 * ch(x) + 5 * sh(x)))
roots_ok(13 * ch(x) + 5 * sh(x), 20, [sp.log(2), -sp.log(sp.Rational(9, 2))])
assert set(sp.solve(9 * u ** 2 - 20 * u + 4, u)) == {2, sp.Rational(2, 9)}
COUNT += 1
has("12 cosh(x + ln(3/2))", "x = −ln(9/2)")
# Section B Q4
roots_ok(sp.atanh(x), sp.asinh(sp.Rational(3, 4)), [sp.Rational(3, 5)])
same(1 / ch(sp.log(3)), sp.Rational(3, 5))
same(th(sp.log(3)), sp.Rational(4, 5))

print(f"pb04 checks passed: {COUNT} assertions")
