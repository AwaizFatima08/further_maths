"""Checks every result stated in pure/pc11.py (Recurrence relations). Each closed form is compared with the
recurrence for many n, and each inductive step is verified symbolically."""
import math
import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pure.pc11 import UNIT  # noqa: E402,F401

k, n = sp.symbols("k n", integer=True, nonnegative=True)
FAILS = []
R = sp.Rational


def ok_(label, cond):
    print(("ok  " if cond else "FAIL"), label)
    if not cond:
        FAILS.append(label)


def zero(label, expr):
    ok_(label, sp.simplify(expr) == 0)


def run(start, rule, count=40):
    """start: list of initial terms (index from first index); rule(i, terms) gives next term where i is the index of
    the new term relative to the first index."""
    u = list(start)
    while len(u) < count:
        u.append(rule(len(u), u))
    return u


def matches(label, terms, first_index, closed, tol=None):
    bad = []
    for j, t in enumerate(terms):
        m = first_index + j
        c = closed(m)
        if tol is None:
            if sp.simplify(sp.sympify(t) - c) != 0:
                bad.append(m)
        elif abs(float(t) - float(c)) > tol * max(1, abs(float(c))):
            bad.append(m)
    ok_(f"{label} (n = {first_index}..{first_index + len(terms) - 1})" + (f" bad {bad[:4]}" if bad else ""), not bad)


# Example 1
u = run([sp.Integer(2)], lambda i, u: 1 / (1 - u[-1]), 12)
ok_("Ex1 a periodic", u[:4] == [2, -1, R(1, 2), 2] and all(u[j] == u[j + 3] for j in range(9)))
u = run([sp.Integer(0)], lambda i, u: -u[-1] / 2 + 3, 30)
matches("Ex1 b", u, 1, lambda m: 2 + 4 * R(-1, 2)**m)
ok_("Ex1 b terms", u[:6] == [0, 3, R(3, 2), R(9, 4), R(15, 8), R(33, 16)])
u = run([0.0], lambda i, u: math.sqrt(u[-1] + 6), 60)
ok_("Ex1 c", abs(u[-1] - 3) < 1e-12 and abs(u[1] - 2.449) < 1e-3 and abs(u[2] - 2.907) < 1e-3 and abs(u[3] - 2.985) < 1e-3)
# Example 2
u = run([sp.Integer(5)], lambda i, u: 3 * u[-1] - 4 * i + 2, 30)  # i = index of previous term (u_1 at i=1)
matches("Ex2", u, 1, lambda m: 3**m + 2 * m)
zero("Ex2 step", 3 * (3**k + 2 * k) - 4 * k + 2 - (3**(k + 1) + 2 * (k + 1)))
# Example 3
u = run([sp.Integer(3)], lambda i, u: 2 * u[-1] + 3**(i - 1), 30)
matches("Ex3 a", u, 0, lambda m: 2**(m + 1) + 3**m)
u = run([sp.Integer(1)], lambda i, u: 2 * u[-1] + 2**(i - 1), 30)
matches("Ex3 b", u, 0, lambda m: (m + 2) * R(2)**(m - 1))
# Example 4 / Fibonacci
phi, psi = (1 + sp.sqrt(5)) / 2, (1 - sp.sqrt(5)) / 2
F = run([0, 1], lambda i, u: u[-1] + u[-2], 40)
matches("Binet", F, 0, lambda m: (phi**m - psi**m) / sp.sqrt(5), tol=1e-12)
ok_("nearest integer", all(F[m] == round(float(phi**m / sp.sqrt(5))) for m in range(40)))
zero("phi^2 = phi + 1", phi**2 - phi - 1)
zero("1/phi = phi - 1", 1 / phi - (phi - 1))
zero("psi = -1/phi", psi + 1 / phi)
ok_("phi^n = F_n phi + F_{n-1}", all(sp.simplify(sp.expand(phi**m - F[m] * phi - F[m - 1])) == 0 for m in range(1, 25)))
ok_("psi^n = F_n psi + F_{n-1}", all(sp.simplify(sp.expand(psi**m - F[m] * psi - F[m - 1])) == 0 for m in range(1, 25)))
ok_("ratio -> phi", abs(F[39] / F[38] - float(phi)) < 1e-12)
L = run([2, 1], lambda i, u: u[-1] + u[-2], 30)
matches("Lucas", L, 0, lambda m: phi**m + psi**m, tol=1e-12)
ok_("Lucas L10 = 123, L1=1, L2=3", L[10] == 123 and L[1] == 1 and L[2] == 3)
# Example 5
u = run([sp.Integer(2), sp.Integer(-3)], lambda i, u: (6 - 7 * u[-1] + 15 * u[-2]) / 2, 30)
matches("Ex5", u, 0, lambda m: 2 * R(3, 2)**m + (-5)**m - 1)
ok_("Ex5 u2", u[2] == R(57, 2))
# Notes 11.5 examples
u = run([1, 4], lambda i, u: 4 * u[-1] - 4 * u[-2], 30)
matches("repeated root", u, 0, lambda m: (m + 1) * 2**m)
u = run([0, 1], lambda i, u: 2 * u[-1] - 2 * u[-2], 30)
matches("complex root", u, 0, lambda m: sp.sqrt(2)**m * sp.sin(m * sp.pi / 4))
# Notes: n! example
u = run([1], lambda i, u: (i + 1) * u[-1], 15)  # u_{n+1} = (n+1) u_n, u_1 = 1 -> index i is n+1
matches("n! example", u, 1, lambda m: sp.factorial(m))
# Example 6
g = 1.01**24
Rr = 50 * g / (g - 1)
ok_("Ex6 1.01^24", f"{g:.6f}" == "1.269735")
ok_("Ex6 R", f"{Rr:.2f}" == "235.37")
ok_("Ex6 interest", f"{24 * 235.37:.2f}" == "5648.88")
u = run([5000.0], lambda i, u: 1.01 * u[-1] - Rr, 25)
ok_("Ex6 u24 = 0", abs(u[24]) < 1e-8)
matches("Ex6 closed", u, 0, lambda m: 100 * Rr + (5000 - 100 * Rr) * 1.01**m, tol=1e-9)

# Practice
u = run([1], lambda i, u: 3 - u[-1], 5)
ok_("P1 a", u == [1, 2, 1, 2, 1])
u = run([R(0)], lambda i, u: u[-1] / 2 + 1, 5)
ok_("P1 b", u == [0, 1, R(3, 2), R(7, 4), R(15, 8)])
ok_("P1 c", [(-1)**m * m for m in range(1, 6)] == [-1, 2, -3, 4, -5])
u = run([1.0], lambda i, u: math.sqrt(2 * u[-1] + 3), 80)
ok_("P2", abs(u[-1] - 3) < 1e-12)
u = run([3], lambda i, u: 4 * u[-1], 20)
matches("P3 a", u, 0, lambda m: 3 * 4**m)
u = run([5], lambda i, u: 4 * u[-1] - 6, 20)
matches("P3 b", u, 0, lambda m: 2 + 3 * 4**m)
u = run([0], lambda i, u: 2 * u[-1] + (i - 1), 30)
matches("P4", u, 0, lambda m: 2**m - m - 1)
u = run([1], lambda i, u: u[-1] + 2 * i + 1, 30)  # previous index is i
matches("P5", u, 1, lambda m: m**2)
u = run([2], lambda i, u: 3 * u[-1] + 2**(i - 1), 30)
matches("P6", u, 0, lambda m: 3**(m + 1) - 2**m)
u = run([1], lambda i, u: 5 * u[-1] + 5**(i - 1), 30)
matches("P7", u, 0, lambda m: (m + 5) * R(5)**(m - 1))
u = run([0, 5], lambda i, u: u[-1] + 6 * u[-2], 30)
matches("P8", u, 0, lambda m: 3**m - (-2)**m)
u = run([1, 6], lambda i, u: 6 * u[-1] - 9 * u[-2], 30)
matches("P9", u, 0, lambda m: (m + 1) * 3**m)
u = run([1, 1], lambda i, u: u[-1] - u[-2], 30)
matches("P10", u, 0, lambda m: sp.cos(m * sp.pi / 3) + sp.sin(m * sp.pi / 3) / sp.sqrt(3))
ok_("P10 period 6", u[:8] == [1, 1, 0, -1, -1, 0, 1, 1] and all(u[j] == u[j + 6] for j in range(20)))
u = run([0, 1], lambda i, u: 5 * u[-1] - 6 * u[-2] + 4, 30)
matches("P11", u, 0, lambda m: 3**(m + 1) - 5 * 2**m + 2)

# Exam
u = run([0, 0], lambda i, u: -u[-1] + 6 * u[-2] + 4 * (i - 2) + 1, 40)
matches("B1", u, 0, lambda m: 2**m - m - 1)
zero("B1 PS", (-(n + 2) - 1) + (-(n + 1) - 1) - 6 * (-n - 1) - (4 * n + 1))
zero("B1 step", -(2**(k + 1) - k - 2) + 6 * (2**k - k - 1) + 4 * k + 1 - (2**(k + 2) - (k + 2) - 1))
P = run([1000.0], lambda i, u: 1.1 * u[-1] - 120, 25)
matches("B2 b", P, 0, lambda m: 1200 - 200 * 1.1**m, tol=1e-9)
ok_("B2 c", P[18] > 0 > P[19] and f"{math.log(6) / math.log(1.1):.1f}" == "18.8"
    and round(P[18]) == 88 and round(P[19]) == -23)
Q = run([1000], lambda i, u: math.floor(1.1 * u[-1] + 1e-9) - 120, 4)
ok_("B2 d", Q == [1000, 980, 958, 933] and abs(P[3] - 933.8) < 1e-9)
zero("B3 a", phi**2 - (phi + 1))
zero("B3 b step", sp.expand(F[5] * phi**2 + F[4] * phi - (F[6] * phi + F[5])))
kk = sp.symbols("F_k F_km1")
zero("B3 b step symbolic", sp.expand(kk[0] * (phi + 1) + kk[1] * phi - ((kk[0] + kk[1]) * phi + kk[0])))
zero("B3 c", phi - psi - sp.sqrt(5))
u = run([1, 1], lambda i, u: 2 * u[-1] - 4 * u[-2], 40)
matches("B4 a", u, 0, lambda m: 2**m * sp.cos(m * sp.pi / 3))
ok_("B4 roots", set(sp.solve(sp.Symbol("m")**2 - 2 * sp.Symbol("m") + 4)) == {1 + sp.sqrt(3) * sp.I, 1 - sp.sqrt(3) * sp.I}
    and sp.Abs(1 + sp.sqrt(3) * sp.I) == 2)
ok_("B4 b", all(u[j + 6] == 64 * u[j] for j in range(30)))
ok_("B4 c", u[30] == 2**30 == 1073741824)
ok_("B4 d never zero", all(u[j] != 0 for j in range(40)))

print("\nFAILED:" if FAILS else "\nALL CHECKS PASSED (pc11)", FAILS if FAILS else "")
sys.exit(1 if FAILS else 0)
