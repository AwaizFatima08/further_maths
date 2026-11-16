"""Checks every result stated in pure/pb09.py (first-order differential equations)."""
import math
import sys
from pathlib import Path

import sympy as sp
from scipy.integrate import solve_ivp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pure.pb09 import UNIT  # noqa: E402,F401  (import checks the module loads)

FAILS = []
x, t, c, A = sp.symbols("x t c A", real=True)
y = sp.Function("y")


def ok(label, cond):
    print(("ok  " if cond else "FAIL"), label)
    if not cond:
        FAILS.append(label)


def near(label, value, stated):
    """value rounds to the stated decimal string."""
    dp = len(stated.split(".")[1]) if "." in stated else 0
    ok(f"{label}: {float(value):.6g} vs {stated}", abs(float(value) - float(stated)) <= 0.5 * 10 ** (-dp) + 1e-12)


def sf3(label, value, stated):
    ok(f"{label}: {float(value):.6g} vs {stated}", float(f"{float(value):.3g}") == float(stated))


def solves(label, ode_lhs_minus_rhs, sol, var=x):
    """sol is an expression for y; ode is an expression in y(var) equal to zero."""
    expr = ode_lhs_minus_rhs.subs(y(var), sol).doit()
    ok(label, sp.simplify(expr) == 0)


D = lambda f: sp.diff(f, x)
Y = y(x)

# 9.1 verification
solves("9.1 y=Ae^2x-x-1/2", D(Y) - 2 * Y - 2 * x, A * sp.exp(2 * x) - x - sp.Rational(1, 2))

# Table of integrating factors
for P, I in [(-2, sp.exp(-2 * x)), (-1 / x, 1 / x), (2 / x, x ** 2), (sp.tan(x), sp.sec(x)), (sp.coth(x), sp.sinh(x))]:
    ok(f"IF for P={P}", sp.simplify(sp.diff(I, x) - P * I) == 0)

# Family figure: y = x - 1 + c e^-x solves y' + y = x
solves("9.4 field family", D(Y) + Y - x, x - 1 + c * sp.exp(-x))

# E1
sol = (sp.exp(2 * x) + 4 * sp.exp(-3 * x)) / 5
solves("E1", D(Y) + 3 * Y - sp.exp(2 * x), sol)
ok("E1 ic", sol.subs(x, 0) == 1)
# E2
sol = x ** 2 * (2 - sp.cos(x))
solves("E2", x * D(Y) - 2 * Y - x ** 3 * sp.sin(x), sol)
ok("E2 ic", sp.simplify(sol.subs(x, sp.pi) - 3 * sp.pi ** 2) == 0)
# E3
solves("E3 family", x * D(Y) + Y - 3 * x ** 2, x ** 2 + c / x)
ok("E3 min c=2 at (1,3)", sp.diff(x ** 2 + 2 / x, x).subs(x, 1) == 0 and (x ** 2 + 2 / x).subs(x, 1) == 3)
near("E3 crossing 2^(1/3)", 2 ** (1 / 3), "1.26")
ok("E3 through (1,4)", (x ** 2 + 3 / x).subs(x, 1) == 4)
# E4
v = sp.Function("v")
vs = sp.Rational(3, 2) * t - sp.Rational(3, 4) + sp.Rational(3, 4) * sp.exp(-2 * t)
ok("E4 ode", sp.simplify(sp.diff(vs, t) + 2 * vs - 3 * t) == 0 and vs.subs(t, 0) == 0)
ok("E4 integral by parts", sp.simplify(sp.diff((3 * t / 2 - sp.Rational(3, 4)) * sp.exp(2 * t), t) - 3 * t * sp.exp(2 * t)) == 0)
dist = sp.integrate(vs, (t, 0, 2))
ok("E4 distance exact", sp.simplify(dist - (sp.Rational(15, 8) - sp.Rational(3, 8) * sp.exp(-4))) == 0)
sf3("E4 distance", dist, "1.87")
ok("E4 v' >0", sp.simplify(sp.diff(vs, t) - sp.Rational(3, 2) * (1 - sp.exp(-2 * t))) == 0)
# E5
S = sp.Rational(1, 5) * (100 + t) - 150000 / (100 + t) ** 2
ok("E5 ode", sp.simplify(sp.diff(S, t) - (sp.Rational(3, 5) - 2 * S / (100 + t))) == 0 and S.subs(t, 0) == 5)
ok("E5 full", S.subs(t, 100) == sp.Rational(145, 4))
near("E5 conc", S.subs(t, 100) / 200, "0.181")
# E6
vx = 10 * sp.exp(-sp.Rational(1, 25) * x)
ok("E6 v dv/dx", sp.simplify(500 * vx * sp.diff(vx, x) + 20 * vx ** 2) == 0)
sf3("E6 distance", 25 * math.log(2), "17.3")
vt = 1 / (sp.Rational(1, 10) + sp.Rational(1, 25) * t)
ok("E6 dv/dt", sp.simplify(500 * sp.diff(vt, t) + 20 * vt ** 2) == 0 and vt.subs(t, sp.Rational(5, 2)) == 5)

# Practice
ok("P1", True)  # same as 9.1 check
sol = 2 / (2 - x ** 2)
solves("P2", D(Y) - x * Y ** 2, sol); ok("P2 ic", sol.subs(x, 0) == 1)
sol = sp.tan(sp.sin(x) + sp.pi / 4)
solves("P3", D(Y) - (1 + Y ** 2) * sp.cos(x), sol); ok("P3 ic", sp.simplify(sol.subs(x, 0) - 1) == 0)
ok("P4 integral", sp.simplify(sp.diff(-sp.exp(-2 * x) * (x ** 2 / 2 + x / 2 + sp.Rational(1, 4)), x) - x ** 2 * sp.exp(-2 * x)) == 0)
solves("P4", D(Y) - 2 * Y - x ** 2, c * sp.exp(2 * x) - x ** 2 / 2 - x / 2 - sp.Rational(1, 4))
solves("P5", x * D(Y) - Y - x ** 4, x ** 4 / 3 + c * x)
solves("P6", D(Y) + Y * sp.coth(x) - sp.cosh(x), sp.sinh(x) / 2 + c / sp.sinh(x))
sol = sp.sin(x) + 2 * sp.cos(x)
solves("P7", D(Y) + Y * sp.tan(x) - sp.sec(x), sol); ok("P7 ic", sol.subs(x, 0) == 2)
sol = (2 * x ** 3 + 1) / (1 + x ** 2)
solves("P8", (1 + x ** 2) * D(Y) + 2 * x * Y - 6 * x ** 2, sol); ok("P8 ic", sol.subs(x, 0) == 1)
solves("P9", D(Y) + Y / x - 2, x + c / x)
ok("P9 min c=1", sp.diff(x + 1 / x, x).subs(x, 1) == 0 and (x + 1 / x).subs(x, 1) == 2)
ok("P9 (2,3)", (x + 2 / x).subs(x, 2) == 3)
k = math.log(7 / 4) / 10
sf3("P10 k", k, "0.0560")
sf3("P10 t", math.log(7) / k, "34.8")
h = (10 - sp.Rational(1, 5) * t) ** 2
ok("P11", sp.simplify(sp.diff(h, t) + sp.Rational(2, 5) * sp.sqrt(h)).subs(t, 3) == 0 and h.subs(t, 10) == 64 and h.subs(t, 50) == 0)
vs = 4 * (1 - sp.exp(-t / 2))
ok("P12 ode", sp.simplify(4 * sp.diff(vs, t) - (8 - 2 * vs)) == 0 and vs.subs(t, 0) == 0)
T = 2 * sp.log(4)
ok("P12 v=3", sp.simplify(vs.subs(t, T) - 3) == 0)
sf3("P12 t", T, "2.77")
X = sp.integrate(vs, (t, 0, T))
ok("P12 x exact", sp.simplify(X - (8 * sp.log(4) - 6)) == 0)
sf3("P12 x", X, "5.09")

# Section B
# Q13
sol = sp.sin(x) * sp.cos(x) + c * sp.cos(x)
solves("Q13a", sp.cos(x) * D(Y) + Y * sp.sin(x) - sp.cos(x) ** 3, sol)
p = sp.cos(x) * (1 + sp.sin(x))
ok("Q13b", p.subs(x, 0) == 1)
ok("Q13c factor", sp.simplify(sp.diff(p, x) - (1 - 2 * sp.sin(x)) * (1 + sp.sin(x))) == 0)
ok("Q13c value", sp.simplify(p.subs(x, sp.pi / 6) - 3 * sp.sqrt(3) / 4) == 0)
# Q14
X = 40 * (sp.exp(-t / 10) - sp.exp(-t / 4))
ok("Q14 ode", sp.simplify(sp.diff(X, t) + X / 4 - 6 * sp.exp(-t / 10)) == 0 and X.subs(t, 0) == 0)
tm = math.log(2.5) / 0.15
ok("Q14 stationary", abs(float(sp.diff(X, t).subs(t, tm))) < 1e-12)
sf3("Q14 t", tm, "6.11")
sf3("Q14 x", X.subs(t, tm), "13.0")
# Q15
vs = 49 * (1 - sp.exp(-t / 5))
ok("Q15 ode", sp.simplify(sp.diff(vs, t) - (sp.Rational(49, 5) - vs / 5)) == 0 and vs.subs(t, 0) == 0)
d = sp.integrate(vs, (t, 0, 10))
ok("Q15 exact", sp.simplify(d - (245 + 245 * sp.exp(-2))) == 0)
sf3("Q15 distance", d, "278")
# Q16
solves("Q16a", x * D(Y) + 2 * Y - 4 * x ** 2, x ** 2 + c / x ** 2)
cp = sp.symbols("cp", positive=True)
f = x ** 2 + cp / x ** 2
xs = cp ** sp.Rational(1, 4)
ok("Q16b", sp.simplify(sp.diff(f, x).subs(x, xs)) == 0 and sp.simplify(f.subs(x, xs) - 2 * sp.sqrt(cp)) == 0)

# Numerical cross-check of the drug model with an ODE solver
s = solve_ivp(lambda tt, z: [6 * math.exp(-0.1 * tt) - 0.25 * z[0]], [0, tm], [0], rtol=1e-11, atol=1e-11)
ok("Q14 numeric", abs(s.y[0][-1] - float(X.subs(t, tm))) < 1e-7)

print()
print("PASS pb09" if not FAILS else f"FAILED pb09: {FAILS}")
sys.exit(1 if FAILS else 0)
