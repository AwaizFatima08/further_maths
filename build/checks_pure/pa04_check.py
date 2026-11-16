"""Checks every result stated in pure/pa04.py (Summation of series and the method of differences)."""
import math
import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pure.pa04 import UNIT  # noqa: E402,F401

n, r = sp.symbols("n r", positive=True, integer=True)
FAILS = []


def zero(label, expr):
    ok = sp.simplify(expr) == 0
    print(("ok  " if ok else "FAIL"), label)
    if not ok:
        FAILS.append(label)


def eq(label, value, expected):
    ok = sp.simplify(value - expected) == 0
    print(("ok  " if ok else "FAIL"), label, value, expected)
    if not ok:
        FAILS.append(label)


def S(term, lo, hi):
    return sp.simplify(sp.summation(term, (r, lo, hi)))


def numeric_sum(f, lo, hi):
    return sum(sp.Rational(f(k)) if not isinstance(f(k), sp.Basic) else f(k) for k in range(lo, hi + 1))


def check_formula(label, term, lo, formula, ns=range(1, 13)):
    """Symbolic check plus a direct numerical check for several n."""
    zero(label + " (symbolic)", S(term, lo, n) - formula)
    for m in ns:
        direct = sum(term.subs(r, k) for k in range(lo, m + 1))
        if sp.simplify(direct - formula.subs(n, m)) != 0:
            print("FAIL", label, "n =", m)
            FAILS.append(f"{label} n={m}")
            return
    print("ok  ", label, "(numeric n = 1..12)")


# Standard results and table
check_formula("Sum r", r, 1, n * (n + 1) / 2)
check_formula("Sum r^2", r**2, 1, n * (n + 1) * (2 * n + 1) / 6)
check_formula("Sum r^3", r**3, 1, n**2 * (n + 1)**2 / 4)
check_formula("r(r+1)", r * (r + 1), 1, n * (n + 1) * (n + 2) / 3)
check_formula("r(r+1)(r+2)", r * (r + 1) * (r + 2), 1, n * (n + 1) * (n + 2) * (n + 3) / 4)
check_formula("2r-1", 2 * r - 1, 1, n**2)
check_formula("(2r-1)^2", (2 * r - 1)**2, 1, n * (2 * n - 1) * (2 * n + 1) / 3)
check_formula("r^2(r+2)", r**2 * (r + 2), 1, n * (n + 1) * (3 * n**2 + 11 * n + 4) / 12)
# Partial-fraction table
check_formula("1/(r(r+1))", 1 / (r * (r + 1)), 1, n / (n + 1))
check_formula("1/((2r-1)(2r+1))", 1 / ((2 * r - 1) * (2 * r + 1)), 1, n / (2 * n + 1))
check_formula("1/(r(r+2))", 1 / (r * (r + 2)), 1, sp.Rational(3, 4) - (2 * n + 3) / (2 * (n + 1) * (n + 2)))
check_formula("1/(r(r+1)(r+2))", 1 / (r * (r + 1) * (r + 2)), 1, sp.Rational(1, 4) - 1 / (2 * (n + 1) * (n + 2)))
zero("pf 1/(r(r+1)(r+2))", 1 / (r * (r + 1) * (r + 2)) - (1 / (r * (r + 1)) - 1 / ((r + 1) * (r + 2))) / 2)
zero("pf 1/((2r-1)(2r+1))", 1 / ((2 * r - 1) * (2 * r + 1)) - (1 / (2 * r - 1) - 1 / (2 * r + 1)) / 2)
for m in range(1, 10):
    assert sum(k * math.factorial(k) for k in range(1, m + 1)) == math.factorial(m + 1) - 1
print("ok   r*r! = (n+1)! - 1 (n = 1..9)")
zero("ln telescoping", sp.expand_log(sum(sp.log(sp.Rational(k + 1, k)) for k in range(1, 9)) - sp.log(9), force=True))
# Differences box: f(r) - f(r+2) and f(r+1) - f(r-1)
f = sp.Function("f")
m = 7
lhs = sum(f(k) - f(k + 2) for k in range(1, m + 1))
eq("two-term box", sp.expand(lhs), f(1) + f(2) - f(m + 1) - f(m + 2))
lhs = sum(f(k + 1) - f(k - 1) for k in range(1, m + 1))
eq("f(r+1)-f(r-1) box", sp.expand(lhs), f(m + 1) + f(m) - f(1) - f(0))

# Examples
zero("Ex1", sp.Rational(1, 4) * n**2 * (n + 1)**2 + sp.Rational(1, 3) * n * (n + 1) * (2 * n + 1)
     - n * (n + 1) * (3 * n**2 + 11 * n + 4) / 12)
zero("Ex2 a", S(r**2, n + 1, 2 * n) - n * (2 * n + 1) * (7 * n + 1) / 6)
eq("Ex2 b", sum(k * k for k in range(11, 21)), 2485)
eq("Ex2 b formula", sp.Rational(10 * 21 * 71, 6), 2485)
assert sum(k * k for k in range(1, 21)) == 2870 and sum(k * k for k in range(1, 11)) == 385
zero("Ex3 identity", (r + 1)**3 - r**3 - (3 * r**2 + 3 * r + 1))
zero("Ex3 algebra", ((n + 1)**3 - 1 - sp.Rational(3, 2) * n * (n + 1) - n) - (n**3 + sp.Rational(3, 2) * n**2 + n / 2))
zero("Ex4 limit", sp.limit(n / (2 * n + 1), n, sp.oo) - sp.Rational(1, 2))
zero("Ex5 limit", sp.limit(sp.Rational(3, 4) - (2 * n + 3) / (2 * (n + 1) * (n + 2)), n, sp.oo) - sp.Rational(3, 4))
zero("Ex6 a", 1 / (r * (r + 1)) - 1 / ((r + 1) * (r + 2)) - 2 / (r * (r + 1) * (r + 2)))
check_formula("Ex6 b", 1 / (r * (r + 1) * (r + 2)), 1, n * (n + 3) / (4 * (n + 1) * (n + 2)))
least = next(k for k in range(1, 1000) if sp.Rational(1, 2 * (k + 1) * (k + 2)) < sp.Rational(1, 1000))
eq("Ex6 c least n", least, 21)
assert 21 * 22 == 462 and 22 * 23 == 506

# Practice
eq("P1", sum(3 * k - 1 for k in range(1, 21)), 610)
check_formula("P2", 6 * r**2 + 2 * r, 1, 2 * n * (n + 1)**2)
check_formula("P3", r * (r + 1) * (r + 2), 1, n * (n + 1) * (n + 2) * (n + 3) / 4)
check_formula("P4", (2 * r - 1)**2, 1, n * (2 * n - 1) * (2 * n + 1) / 3)
check_formula("P5", r**2 * (r - 1), 1, (n - 1) * n * (n + 1) * (3 * n + 2) / 12)
zero("P6", S(r**3, n + 1, 2 * n) - n**2 * (3 * n + 1) * (5 * n + 3) / 4)
eq("P7", sum(k * k for k in range(10, 31)), 9170)
assert sum(k * k for k in range(1, 31)) == 9455 and sum(k * k for k in range(1, 10)) == 285
check_formula("P8", 1 / ((3 * r - 1) * (3 * r + 2)), 1, n / (2 * (3 * n + 2)))
zero("P9", sp.expand_log(sum(sp.log(1 + sp.Rational(1, k)) for k in range(1, 12)) - sp.log(12), force=True))
check_formula("P10", 1 / (r**2 - 1), 2, sp.Rational(3, 4) - (2 * n + 1) / (2 * n * (n + 1)), ns=range(2, 13))
zero("P10 pf", 1 / (r**2 - 1) - (1 / (r - 1) - 1 / (r + 1)) / 2)
zero("P12 u_n", n / (2 * n + 1) - (n - 1) / (2 * n - 1) - 1 / ((2 * n - 1) * (2 * n + 1)))

# Exam
check_formula("B1 a", r * (r + 3), 1, n * (n + 1) * (n + 5) / 3)
eq("B1 b", sum(k * (k + 3) for k in range(11, 21)), 2950)
assert 20 * 21 * 25 // 3 == 3500 and 10 * 11 * 15 // 3 == 550
eq("B1 c", sum(k * (k + 3) for k in range(1, 13)), 884)
assert 12 * 13 * 17 == 2652
zero("B2 a", (2 * r + 1) / (r**2 * (r + 1)**2) - (1 / r**2 - 1 / (r + 1)**2))
check_formula("B2 b", (2 * r + 1) / (r**2 * (r + 1)**2), 1, 1 - 1 / (n + 1)**2)
zero("B2 d", S((2 * r + 1) / (r**2 * (r + 1)**2), n + 1, 2 * n) - n * (3 * n + 2) / ((n + 1)**2 * (2 * n + 1)**2))
zero("B3 a", (r + 1)**4 - r**4 - (4 * r**3 + 6 * r**2 + 4 * r + 1))
zero("B3 b step", (n + 1)**4 - (n + 1) - n * (n + 1) * (n**2 + 3 * n + 3))
zero("B3 b final", (n + 1)**4 - 1 - n * (n + 1) * (2 * n + 1) - 2 * n * (n + 1) - n - n**2 * (n + 1)**2)
check_formula("B3 c", (2 * r - 1)**3, 1, n**2 * (2 * n**2 - 1))
u = sp.log(r * (r + 2) / (r + 1)**2)
fr = lambda t: sp.log(t / (t + 1))  # noqa: E731
zero("B4 a", sp.expand_log(u - (fr(r) - fr(r + 1)), force=True))
for m in range(1, 8):
    s_m = sum(sp.log(sp.Rational(k * (k + 2), (k + 1)**2)) for k in range(1, m + 1))
    assert abs(sp.N(s_m - sp.log(sp.Rational(m + 2, 2 * (m + 1))), 30)) < 1e-25
print("ok   B4 b (n = 1..7)")
zero("B4 c", sp.limit(sp.log((n + 2) / (2 * (n + 1))), n, sp.oo) + sp.log(2))
least = next(k for k in range(1, 10000) if math.log((k + 2) / (k + 1)) < 0.01)
eq("B4 d", least, 99)
print("   B4 d values", math.log(100 / 99), math.log(101 / 100), math.exp(0.01) - 1)

print("\nFAILED:" if FAILS else "\nALL CHECKS PASSED (pa04)", FAILS if FAILS else "")
sys.exit(1 if FAILS else 0)
