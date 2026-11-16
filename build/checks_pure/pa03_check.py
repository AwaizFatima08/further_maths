"""Checks every result stated in pure/pa03.py (Roots of polynomial equations)."""
import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pure.pa03 import UNIT  # noqa: E402,F401  (import checks the module loads)

x, w, y = sp.symbols("x w y")
FAILS = []


def eq(label, value, expected):
    if isinstance(value, (list, tuple)):
        ok = len(value) == len(expected) and all(sp.simplify(u - v) == 0 for u, v in zip(value, expected))
    else:
        ok = sp.simplify(sp.nsimplify(value) - sp.nsimplify(expected)) == 0
    print(("ok  " if ok else "FAIL"), label, value, expected)
    if not ok:
        FAILS.append(label)


def roots(poly):
    """All roots (with multiplicity) of a polynomial in x, as sympy numbers (exact where possible)."""
    p = sp.Poly(poly, x)
    linear = all(f.degree() == 1 for f, _ in sp.factor_list(p)[1])
    if p.degree() <= 2 or linear:
        return sp.roots(p, multiple=True)
    return p.nroots(n=45, maxsteps=500)  # 45-digit numerical roots


def num(expr):
    return sp.N(expr, 30)


def close(label, value, expected):
    ok = abs(complex(num(value)) - complex(num(expected))) < 1e-20
    print(("ok  " if ok else "FAIL"), label, sp.N(value, 12), expected)
    if not ok:
        FAILS.append(label)


def same_poly(label, poly, expected, var=w):
    ok = sp.expand(poly - expected) == 0
    print(("ok  " if ok else "FAIL"), label, sp.expand(poly))
    if not ok:
        FAILS.append(label)


def transformed(poly, g, var=w):
    """Monic polynomial whose roots are g(root) for every root of poly, built numerically and compared later."""
    rs = roots(poly)
    return sp.expand(sp.prod([var - g(r) for r in rs]))


def check_roots_of(label, newpoly, poly, g, var=w):
    """newpoly (in var) must have roots g(r) for each root r of poly: compare monic forms numerically."""
    lead = sp.Poly(newpoly, var).LC()
    target = transformed(poly, g, var)
    diff = sp.Poly(sp.expand(newpoly / lead - target), var)
    ok = all(abs(complex(sp.N(c, 30))) < 1e-15 for c in diff.all_coeffs())
    print(("ok  " if ok else "FAIL"), label)
    if not ok:
        FAILS.append(label)


# Identities in the table (quadratic)
a, b = sp.symbols("alpha beta")
s, p = a + b, a * b
for lhs, rhs in [(a**2 + b**2, s**2 - 2 * p), (a**3 + b**3, s**3 - 3 * p * s), ((a - b)**2, s**2 - 4 * p),
                 (1 / a + 1 / b, s / p), (1 / a**2 + 1 / b**2, (s**2 - 2 * p) / p**2), (a / b + b / a, (s**2 - 2 * p) / p),
                 (a**4 + b**4, (s**2 - 2 * p)**2 - 2 * p**2)]:
    eq(f"identity {lhs}", sp.simplify(lhs - rhs), 0)
# Cubic sum of cubes identity, reciprocal squares, product of shifted roots
c1, c2, c3, k = sp.symbols("c1 c2 c3 k")
e1, e2, e3 = c1 + c2 + c3, c1 * c2 + c2 * c3 + c3 * c1, c1 * c2 * c3
eq("sum cubes identity", sp.expand(c1**3 + c2**3 + c3**3 - (e1**3 - 3 * e1 * e2 + 3 * e3)), 0)
d4 = sp.symbols("d4")
q = [c1, c2, c3, d4]
E1 = sum(q)
E2 = sum(q[i] * q[j] for i in range(4) for j in range(i + 1, 4))
E3 = sum(q[i] * q[j] * q[l] for i in range(4) for j in range(i + 1, 4) for l in range(j + 1, 4))
eq("sum cubes identity (4 roots)", sp.expand(sum(t**3 for t in q) - (E1**3 - 3 * E1 * E2 + 3 * E3)), 0)

# Example 1
r = roots(2 * x**2 - 3 * x + 4)
eq("Ex1 a", sp.simplify(r[0]**2 + r[1]**2), sp.Rational(-7, 4))
eq("Ex1 b", sp.simplify(r[0]**3 + r[1]**3), sp.Rational(-45, 8))
r0, r1 = r
eq("Ex1 c sum", sp.simplify(r0 / r1 + r1 / r0), sp.Rational(-7, 8))
eq("Ex1 c prod", sp.simplify((r0 / r1) * (r1 / r0)), 1)

# Example 2
f2 = 2 * x**3 + 5 * x**2 - 3 * x + 7
r = roots(f2)
close("Ex2 a", sum(t**2 for t in r), sp.Rational(37, 4))
close("Ex2 b", sum(1 / t for t in r), sp.Rational(3, 7))
close("Ex2 c", sum(t**3 for t in r), sp.Rational(-299, 8))
close("Ex2 d", sp.prod([1 + t for t in r]), sp.Rational(-13, 2))
eq("Ex2 f(-1)", f2.subs(x, -1), 13)

# Example 3
k3 = 39
r = roots(x**3 - 12 * x**2 + k3 * x - 28)
eq("Ex3 roots", sorted(r), [1, 4, 7])

# Example 4
f4 = x**4 - 2 * x**3 + 3 * x**2 - x + 5
r = roots(f4)
close("Ex4 a", sum(t**2 for t in r), -2)
close("Ex4 b1", sum(1 / t for t in r), sp.Rational(1, 5))
close("Ex4 b2", sum(1 / t**2 for t in r), sp.Rational(-29, 25))

# Example 5
f5 = x**3 - 3 * x**2 + 5 * x - 2
check_roots_of("Ex5 a", w**3 - 3 * w**2 + 11 * w - 1, f5, lambda t: 2 * t - 1)
same_poly("Ex5 a expansion", sp.expand(8 * f5.subs(x, (w + 1) / 2)), w**3 - 3 * w**2 + 11 * w - 1)
check_roots_of("Ex5 b", w**3 + w**2 + 13 * w - 4, f5, lambda t: t**2)
same_poly("Ex5 b expansion", sp.expand(w * (w + 5)**2 - (3 * w + 2)**2), w**3 + w**2 + 13 * w - 4)

# Example 6
f6 = x**4 + 2 * x**2 - x + 3
r = roots(f6)
for n, val in [(1, 0), (2, -4), (3, 3), (4, -4), (5, -10)]:
    close(f"Ex6 S{n}", sum(t**n for t in r), val)

# Practice
r = roots(3 * x**2 - 5 * x + 1)
eq("P1 a", sp.simplify(r[0]**2 + r[1]**2), sp.Rational(19, 9))
eq("P1 b", sp.simplify(1 / r[0] + 1 / r[1]), 5)
eq("P1 c", sp.simplify((r[0] - r[1])**2), sp.Rational(13, 9))
check_roots_of("P2", w**2 - 20 * w + 4, x**2 + 4 * x - 2, lambda t: t**2)
r = roots(2 * x**2 - x + 3)
newr = [r[0] + 1 / r[1], r[1] + 1 / r[0]]
close("P3 sum", sum(newr), sp.Rational(5, 6))
close("P3 prod", newr[0] * newr[1], sp.Rational(25, 6))
r = roots(x**3 - 4 * x**2 + 2 * x + 5)
close("P4 sumsq", sum(t**2 for t in r), 12)
close("P4 recip", sum(1 / t for t in r), sp.Rational(-2, 5))
f = 2 * x**3 + 3 * x**2 - x + 4
r = roots(f)
close("P5 a", sp.prod([2 - t for t in r]), 15)
close("P5 b", sum(t**3 for t in r), sp.Rational(-93, 8))
r = roots(2 * x**4 - 3 * x**3 + x - 6)
close("P6 sumsq", sum(t**2 for t in r), sp.Rational(9, 4))
close("P6 recip", sum(1 / t for t in r), sp.Rational(1, 6))
eq("P7 roots", sorted(roots(x**3 - 14 * x**2 + 56 * x - 64)), [2, 4, 8])
eq("P8 roots", sorted(roots(x**3 - 6 * x**2 + 11 * x - 6)), [1, 2, 3])
f = x**3 + 2 * x**2 - 5 * x + 1
check_roots_of("P9", w**3 - 4 * w**2 - w + 11, f, lambda t: t + 2)
check_roots_of("P10", 2 * w**3 - 3 * w**2 + 36 * w - 189, 2 * x**3 - x**2 + 4 * x - 7, lambda t: 3 * t)
f = x**4 + 3 * x**3 - 2 * x + 5
check_roots_of("P11", 5 * w**4 - 2 * w**3 + 3 * w + 1, f, lambda t: 1 / t)
close("P11 sum", sum(1 / t for t in roots(f)), sp.Rational(2, 5))
r = roots(x**3 - 2 * x + 3)
for n, val in [(2, 4), (3, -9), (4, 8)]:
    close(f"P12 S{n}", sum(t**n for t in r), val)

# Exam
f = x**3 + 3 * x**2 - 2 * x + 6
r = roots(f)
close("B1 a", sum(t**2 for t in r), 13)
close("B1 b", sum(t**3 for t in r), -63)
check_roots_of("B1 c", w**3 + 9 * w**2 + 7 * w + 47, f, lambda t: 2 * t - 1)
close("B1 d", sum((2 * t - 1)**2 for t in r), 67)
f = 2 * x**4 - 4 * x**3 + 5 * x**2 + 6 * x - 3
r = roots(f)
close("B2 sum", sum(r), 2)
close("B2 sumsq", sum(t**2 for t in r), -1)
close("B2 recip", sum(1 / t for t in r), 2)
check_roots_of("B2 d", 3 * y**4 - 6 * y**3 - 5 * y**2 + 4 * y - 2, f, lambda t: 1 / t, var=y)
f = 4 * x**3 - 12 * x**2 - 4 * x + 12
eq("B3 roots", sorted(roots(f)), [-1, 1, 3])
check_roots_of("B3 c", y**3 - 11 * y**2 + 19 * y - 9, f, lambda t: t**2, var=y)
r = roots(x**2 - 3 * x + 5)
eq("B4 a", sp.simplify(r[0]**3 + r[1]**3), -18)
eq("B4 b sum", sp.simplify(r[0]**2 / r[1] + r[1]**2 / r[0]), sp.Rational(-18, 5))
eq("B4 b prod", sp.simplify(r[0] * r[1]), 5)
eq("B4 c", sp.simplify(sp.Abs(r[0])), sp.sqrt(5))

print("\nFAILED:" if FAILS else "\nALL CHECKS PASSED (pa03)", FAILS if FAILS else "")
sys.exit(1 if FAILS else 0)
