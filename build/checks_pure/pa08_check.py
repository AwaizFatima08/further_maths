"""Checks every result stated in pure/pa08.py (Proof by induction and other methods of proof).
Each induction claim is tested directly for many n, and each inductive-step identity is verified symbolically."""
import math
import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pure.pa08 import UNIT  # noqa: E402,F401

k, n, X = sp.symbols("k n x")
FAILS = []
N = range(1, 41)


def ok_(label, cond):
    print(("ok  " if cond else "FAIL"), label)
    if not cond:
        FAILS.append(label)


def zero(label, expr):
    ok_(label, sp.simplify(expr) == 0)


def all_n(label, pred, ns=N):
    bad = [m for m in ns if not pred(m)]
    ok_(f"{label} (n = {ns[0]}..{ns[-1]})" + (f" fails at {bad[:5]}" if bad else ""), not bad)


# 8.2 Σr^3 ; Example 1 ; P1-P3
all_n("sum r^3", lambda m: sum(r**3 for r in range(1, m + 1)) * 4 == m * m * (m + 1)**2)
zero("sum r^3 step", sp.Rational(1, 4) * k**2 * (k + 1)**2 + (k + 1)**3 - sp.Rational(1, 4) * (k + 1)**2 * (k + 2)**2)
all_n("Ex1", lambda m: 3 * sum(r * (r + 1) for r in range(1, m + 1)) == m * (m + 1) * (m + 2))
zero("Ex1 step", k * (k + 1) * (k + 2) / 3 + (k + 1) * (k + 2) - (k + 1) * (k + 2) * (k + 3) / 3)
all_n("P1", lambda m: sum(2 * r - 1 for r in range(1, m + 1)) == m * m)
all_n("P2", lambda m: sum(sp.Rational(1, r * (r + 1)) for r in range(1, m + 1)) == sp.Rational(m, m + 1))
zero("P2 step", k / (k + 1) + 1 / ((k + 1) * (k + 2)) - (k + 1) / (k + 2))
all_n("P3", lambda m: sum(r * 2**r for r in range(1, m + 1)) == (m - 1) * 2**(m + 1) + 2)
zero("P3 step", (k - 1) * 2**(k + 1) + 2 + (k + 1) * 2**(k + 1) - (k * 2**(k + 2) + 2))

# 8.3 divisibility
all_n("3^(2n)+11 div 4", lambda m: (3**(2 * m) + 11) % 4 == 0)
A = sp.symbols("A")
zero("3^(2n)+11 step", 9 * (4 * A - 11) + 11 - 4 * (9 * A - 22))
f = lambda m: 3**(2 * m + 2) + 8 * m - 9  # noqa: E731
all_n("Ex2 div 8", lambda m: f(m) % 8 == 0)
ok_("Ex2 f(1)=80", f(1) == 80)
fk = 3**(2 * k + 2) + 8 * k - 9
zero("Ex2 step", sp.expand(fk.subs(k, k + 1) - 9 * fk - 8 * (10 - 8 * k)))
all_n("P4", lambda m: (7**m - 3**m) % 4 == 0)
zero("P4 step", sp.expand(7**(k + 1) - 3**(k + 1) - (7 * (7**k - 3**k) + 4 * 3**k)))
g = 5**k + 8 * k + 3
all_n("P5", lambda m: (5**m + 8 * m + 3) % 4 == 0)
zero("P5 step", sp.expand(g.subs(k, k + 1) - 5 * g + 4 * (8 * k + 1)))
all_n("P6", lambda m: (3**(2 * m) + 7) % 8 == 0)
zero("P6 step", 9 * (8 * A - 7) + 7 - 8 * (9 * A - 7))
h = 2**(k + 2) + 3**(2 * k + 1)
all_n("B1 b", lambda m: (2**(m + 2) + 3**(2 * m + 1)) % 7 == 0)
zero("B1 b step", sp.expand(h.subs(k, k + 1) - (2 * h + 7 * 3**(2 * k + 1))))

# 8.4 matrices
M = sp.Matrix([[3, -4], [1, -1]])
Fm = lambda m: sp.Matrix([[2 * m + 1, -4 * m], [m, 1 - 2 * m]])  # noqa: E731
all_n("Edexcel M^n", lambda m: M**m == Fm(m))
zero("Edexcel step", (Fm(k) * M - Fm(k + 1)).norm())
ok_("B2 b inverse", M.inv() == sp.Matrix([[-1, 4], [-1, 3]]) and Fm(0) == sp.eye(2) and Fm(-1) == M.inv())
M3 = sp.Matrix([[4, -1], [6, -1]])
F3 = lambda m: sp.Matrix([[3 * 2**m - 2, 1 - 2**m], [6 * 2**m - 6, 3 - 2**(m + 1)]])  # noqa: E731
all_n("Ex3 M^n", lambda m: M3**m == F3(m))
zero("Ex3 step", sp.simplify((F3(k) * M3 - F3(k + 1)).norm()))
M7 = sp.Matrix([[1, 2], [0, 3]])
F7 = lambda m: sp.Matrix([[1, 3**m - 1], [0, 3**m]])  # noqa: E731
all_n("P7", lambda m: M7**m == F7(m))
zero("P7 step", sp.simplify((F7(k) * M7 - F7(k + 1)).norm()))
M8 = sp.Matrix([[2, 1], [-1, 0]])
F8 = lambda m: sp.Matrix([[m + 1, m], [-m, 1 - m]])  # noqa: E731
all_n("P8", lambda m: M8**m == F8(m))
zero("P8 step", (F8(k) * M8 - F8(k + 1)).norm())

# 8.5 sequences
def seq(u1, step, m):
    u = sp.Integer(u1) if not isinstance(u1, sp.Basic) else u1
    out = [u]
    for _ in range(m - 1):
        u = step(u)
        out.append(u)
    return out


s = seq(1, lambda u: 3 * u + 4, 40)
all_n("IAL 3^n - 2", lambda m: s[m - 1] == 3**m - 2)
s = seq(1, lambda u: 3 * u - 1, 40)
all_n("Ex4", lambda m: s[m - 1] == sp.Rational(1 + 3**(m - 1), 2))
zero("Ex4 step", 3 * (1 + 3**(k - 1)) / 2 - 1 - (1 + 3**k) / 2)
s = seq(sp.Integer(1), lambda u: u / (1 + u), 40)
all_n("P9 u_n = 1/n", lambda m: s[m - 1] == sp.Rational(1, m))
u = [None, 1, 5]
for m in range(3, 42):
    u.append(5 * u[m - 1] - 6 * u[m - 2])
all_n("B3 a", lambda m: u[m] == 3**m - 2**m)
zero("B3 step", 5 * (3**(k + 1) - 2**(k + 1)) - 6 * (3**k - 2**k) - (3**(k + 2) - 2**(k + 2)))
all_n("B3 b odd", lambda m: u[m] % 2 == 1)

# 8.6 derivatives
for m in range(1, 13):
    d = sp.diff(X * sp.exp(X), X, m)
    if sp.simplify(d - (X + m) * sp.exp(X)) != 0:
        FAILS.append(f"x e^x deriv {m}")
print("ok   d^n(x e^x) = (x+n)e^x (n = 1..12)")
for m in range(1, 13):
    d = sp.diff(X**2 * sp.exp(X), X, m)
    if sp.simplify(d - (X**2 + 2 * m * X + m * (m - 1)) * sp.exp(X)) != 0:
        FAILS.append(f"Ex5 deriv {m}")
print("ok   Ex5 d^n(x^2 e^x) (n = 1..12)")
zero("Ex5 step", sp.diff((X**2 + 2 * k * X + k * (k - 1)) * sp.exp(X), X)
     - (X**2 + 2 * (k + 1) * X + (k + 1) * k) * sp.exp(X))
zero("Ex5 d1", sp.diff(X**2 * sp.exp(X), X) - (X**2 + 2 * X) * sp.exp(X))
zero("Ex5 d2", sp.diff(X**2 * sp.exp(X), X, 2) - (X**2 + 4 * X + 2) * sp.exp(X))
zero("Ex5 d3", sp.diff(X**2 * sp.exp(X), X, 3) - (X**2 + 6 * X + 6) * sp.exp(X))
for m in range(1, 13):
    d = sp.diff(X * sp.exp(2 * X), X, m)
    if sp.simplify(d - 2**(m - 1) * (2 * X + m) * sp.exp(2 * X)) != 0:
        FAILS.append(f"P10 deriv {m}")
print("ok   P10 (n = 1..12)")
zero("P10 step", sp.diff(2**(k - 1) * (2 * X + k) * sp.exp(2 * X), X) - 2**k * (2 * X + k + 1) * sp.exp(2 * X))
for m in range(1, 13):
    d = sp.diff(sp.exp(X) * sp.sin(X), X, m)
    target = 2**sp.Rational(m, 2) * sp.exp(X) * sp.sin(X + m * sp.pi / 4)
    if sp.simplify(sp.expand_trig(d - target)) != 0:
        FAILS.append(f"B4 a deriv {m}")
print("ok   B4 a d^n(e^x sin x) (n = 1..12)")
zero("B4 a identity", sp.expand_trig(sp.sin(X) + sp.cos(X) - sp.sqrt(2) * sp.sin(X + sp.pi / 4)))

# inequalities
all_n("Ex6 n! > 2^n", lambda m: math.factorial(m) > 2**m, range(4, 61))
ok_("Ex6 fails n=1,2,3", all(math.factorial(m) <= 2**m for m in (1, 2, 3)))
all_n("P11 2^n > n^2", lambda m: 2**m > m * m, range(5, 61))
ok_("P11 k^2-2k-1>0 for k>=3", all(m * m - 2 * m - 1 > 0 for m in range(3, 100)))
all_n("B4 b n! > 3^n", lambda m: math.factorial(m) > 3**m, range(7, 61))
ok_("B4 b n=6 fails", math.factorial(6) == 720 and 3**6 == 729)
ok_("B4 b 7! and 3^7", math.factorial(7) == 5040 and 3**7 == 2187)

# sums with factorials
all_n("B1 a", lambda m: sum(r * math.factorial(r) for r in range(1, m + 1)) == math.factorial(m + 1) - 1)

# 8.7 other methods
ok_("counter-example 41", 40**2 + 40 + 41 == 41**2 and all(sp.isprime(m * m + m + 41) for m in range(0, 40)))
ok_("squares mod 3", all((m * m) % 3 in (0, 1) for m in range(-200, 200)))
mm = sp.symbols("m", integer=True)
zero("exhaustion forms 1", (3 * mm + 1)**2 - (3 * (3 * mm**2 + 2 * mm) + 1))
zero("exhaustion forms 2", (3 * mm + 2)**2 - (3 * (3 * mm**2 + 4 * mm + 1) + 1))
ok_("P12 a", all((m + m + 1 + m + 2) % 3 == 0 for m in range(-100, 100)))
ok_("P12 b", all((m * m - m) % 2 == 0 for m in range(-100, 100)))
ok_("P12 c", 2**11 - 1 == 2047 == 23 * 89 and sp.isprime(11))
ok_("P12 c smaller primes give primes", all(sp.isprime(2**p - 1) for p in (2, 3, 5, 7)))

print("\nFAILED:" if FAILS else "\nALL CHECKS PASSED (pa08)", FAILS if FAILS else "")
sys.exit(1 if FAILS else 0)
