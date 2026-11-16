"""Checks every result stated in pure/pb10.py (second-order linear DEs with constant coefficients)."""
import math
import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pure.pb10 import UNIT  # noqa: E402,F401

FAILS = []
x, A, B, lam, mu, k = sp.symbols("x A B lambda mu k", real=True)
al, a_, b_, c_ = sp.symbols("alpha a b c", real=True)


def ok(label, cond):
    print(("ok  " if cond else "FAIL"), label)
    if not cond:
        FAILS.append(label)


def sf3(label, value, stated):
    ok(f"{label}: {float(value):.6g} vs {stated}", float(f"{float(value):.3g}") == float(stated))


def L(y, p, q):
    """y'' + p y' + q y"""
    return sp.diff(y, x, 2) + p * sp.diff(y, x) + q * y


def solves(label, y, p, q, f, coeff=1):
    ok(label, sp.simplify(coeff * sp.diff(y, x, 2) + p * sp.diff(y, x) + q * y - f) == 0)


def ic(label, y, y0, dy0, at=0):
    ok(label, sp.simplify(y.subs(x, at) - y0) == 0 and sp.simplify(sp.diff(y, x).subs(x, at) - dy0) == 0)


E = sp.exp
# 10.2 repeated root proof: a y'' + b y' + c y for y = x e^{alpha x}
expr = sp.expand((a_ * sp.diff(x * E(al * x), x, 2) + b_ * sp.diff(x * E(al * x), x) + c_ * x * E(al * x)) / E(al * x))
ok("repeated-root identity", sp.simplify(expr - (x * (a_ * al ** 2 + b_ * al + c_) + 2 * a_ * al + b_)) == 0)
# figure cases
for p, q, sol in [(-1, -2, sp.Rational(1, 3) * E(2 * x) + sp.Rational(2, 3) * E(-x)), (2, 1, (1 + x) * E(-x)),
                  (2, 10, E(-x) * (sp.cos(3 * x) + sp.sin(3 * x) / 3))]:
    solves(f"fig case p={p} q={q}", sol, p, q, 0)
    ic(f"fig ic p={p}", sol, 1, 0)
# 10.5 table
solves("table y''-6y'+9y=e^3x trial", sp.Rational(1, 2) * x ** 2 * E(3 * x), -6, 9, E(3 * x))
solves("table y''-3y'=6", -2 * x, -3, 0, 6)
# 10.7
ok("10.7 first order", sp.simplify(sp.diff(A * E(-2 * x) + 2 * x - sp.Rational(1, 2), x) + 2 * (A * E(-2 * x) + 2 * x - sp.Rational(1, 2)) - (4 * x + 1)) == 0)

# Examples
y = E(3 * x) + 2 * E(-2 * x); solves("E1", y, -1, -6, 0); ic("E1 ic", y, 3, -1)
solves("E2a", (A + B * x) * E(-3 * x), 6, 9, 0)
y = E(-2 * x) * (sp.cos(3 * x) + 2 * sp.sin(3 * x)); solves("E2b", y, 4, 13, 0); ic("E2b ic", y, 1, 4)
ok("E2b derivative form", sp.simplify(sp.diff(E(-2 * x) * (A * sp.cos(3 * x) + B * sp.sin(3 * x)), x)
                                       - E(-2 * x) * ((-2 * A + 3 * B) * sp.cos(3 * x) + (-2 * B - 3 * A) * sp.sin(3 * x))) == 0)
solves("E3", A * E(x) + B * E(2 * x) + 2 * x + 3 + E(3 * x) / 2, -3, 2, 4 * x + E(3 * x))
y = (E(-x) - E(2 * x)) / 3 + 2 * x * E(2 * x); solves("E4", y, -1, -2, 6 * E(2 * x)); ic("E4 ic", y, 0, 1)
solves("E5a k=-1/4", -x * sp.cos(2 * x) / 4, 0, 4, sp.sin(2 * x))
y = sp.sin(2 * x) / 8 - x * sp.cos(2 * x) / 4; solves("E5b", y, 0, 4, sp.sin(2 * x)); ic("E5b ic", y, 0, 0)
y = E(-x) * (A * sp.cos(2 * x) + B * sp.sin(2 * x)) + 2 * sp.cos(x) + sp.sin(x); solves("E6", y, 2, 5, 10 * sp.cos(x))
ok("E6 amplitude", sp.simplify(sp.sqrt(2 ** 2 + 1 ** 2) - sp.sqrt(5)) == 0)

# Practice
solves("P1", A * E(2 * x) + B * E(3 * x), -5, 6, 0)
solves("P2", (A + B * x) * E(-x / 2), 4, 1, 0, coeff=4)
solves("P3", A * sp.cos(3 * x) + B * sp.sin(3 * x), 0, 9, 0)
solves("P4", E(x) * (A * sp.cos(2 * x) + B * sp.sin(2 * x)), -2, 5, 0)
y = 2 * sp.cosh(2 * x); solves("P5", y, 0, -4, 0); ic("P5 ic", y, 2, 0)
solves("P6", A * E(x) + B * E(-3 * x) - 3 * x ** 2 - 4 * x - sp.Rational(14, 3), 2, -3, 9 * x ** 2)
solves("P7", A * E(x) + B * E(-2 * x) - sp.Rational(5, 3) * x * E(-2 * x), 1, -2, 5 * E(-2 * x))
solves("P8", (A + B * x) * E(3 * x) + x ** 2 * E(3 * x) / 2, -6, 9, E(3 * x))
solves("P9", A * sp.cos(x) + B * sp.sin(x) - sp.cos(2 * x), 0, 1, 3 * sp.cos(2 * x))
solves("P10", A * sp.cos(x) + B * sp.sin(x) - x * sp.cos(x), 0, 1, 2 * sp.sin(x))
y = 5 * E(-x) - 2 * E(-2 * x) - 3 * sp.cos(x) + sp.sin(x); solves("P11", y, 3, 2, 10 * sp.sin(x)); ic("P11 ic", y, 0, 0)
alpha = sp.atan(3)
ok("P11 R-form", sp.simplify(sp.expand_trig(sp.sqrt(10) * sp.sin(x - alpha)) - (sp.sin(x) - 3 * sp.cos(x))) == 0)
yy = A * E(-2 * x) + 2 * x - sp.Rational(1, 2)
ok("P12", sp.simplify(sp.diff(yy, x) + 2 * yy - 4 * x - 1) == 0)

# Section B
y = E(-2 * x) * (8 * sp.cos(x) + 14 * sp.sin(x)) - 8 * sp.cos(2 * x) + sp.sin(2 * x)
solves("Q13", y, 4, 5, 65 * sp.sin(2 * x)); ic("Q13 ic", y, 0, 0)
ok("Q13 R", sp.sqrt(8 ** 2 + 1) == sp.sqrt(65))
y = E(-x) - E(-9 * x); solves("Q14c", y, 10, 9, 0); ic("Q14c ic", y, 0, 8)
solves("Q14b", (A + B * x) * E(-3 * x), 6, 9, 0)
xm = math.log(9) / 8
ok("Q14d stationary", abs(float(sp.diff(y, x).subs(x, xm))) < 1e-12)
sf3("Q14d x", xm, "0.275")
sf3("Q14d ymax", y.subs(x, xm), "0.675")
y = (4 * x ** 2 - 2 * x + 1) * E(2 * x); solves("Q15", y, -4, 4, 8 * E(2 * x)); ic("Q15 ic", y, 1, 0)
solves("Q15 PI", 4 * x ** 2 * E(2 * x), -4, 4, 8 * E(2 * x))
ok("Q15 trials fail", sp.simplify(L(E(2 * x), -4, 4)) == 0 and sp.simplify(L(x * E(2 * x), -4, 4)) == 0)
ok("Q15 discriminant", (-2) ** 2 - 4 * 4 * 1 < 0)
solves("Q16a", 2 * x * sp.sin(3 * x), 0, 9, 12 * sp.cos(3 * x))
y = sp.cos(3 * x) + 2 * x * sp.sin(3 * x); solves("Q16c", y, 0, 9, 12 * sp.cos(3 * x))
ok("Q16c bc", y.subs(x, 0) == 1 and sp.simplify(y.subs(x, sp.pi / 6) - sp.pi / 3) == 0)

print()
print("PASS pb10" if not FAILS else f"FAILED pb10: {FAILS}")
sys.exit(1 if FAILS else 0)
