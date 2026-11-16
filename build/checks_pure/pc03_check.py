"""Checks every result stated in pure/pc03.py (DEs by substitution and Taylor-series solutions)."""
import math
import sys
from pathlib import Path

import sympy as sp
from scipy.integrate import solve_ivp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pure.pc03 import UNIT  # noqa: E402,F401

FAILS = []
x = sp.symbols("x", positive=True)
t = sp.symbols("t", real=True)
A, B, c, d = sp.symbols("A B c d", real=True)
E = sp.exp
y = sp.Function("y")
z = sp.Function("z")


def ok(label, cond):
    print(("ok  " if cond else "FAIL"), label)
    if not cond:
        FAILS.append(label)


def zero(e):
    return sp.simplify(e) == 0


def dp(label, value, stated):
    places = len(stated.split(".")[1])
    ok(f"{label}: {float(value):.7f} vs {stated}", abs(float(value) - float(stated)) <= 0.5 * 10 ** (-places) + 1e-12)


def sf3(label, value, stated):
    ok(f"{label}: {float(value):.6g} vs {stated}", float(f"{float(value):.3g}") == float(stated))


def implicit_check(label, F, rhs):
    """F(x, Y) = 0 defines y implicitly; check dy/dx = -F_x/F_y equals rhs(x, Y)."""
    Y = sp.symbols("Y")
    Fx, Fy = sp.diff(F(x, Y), x), sp.diff(F(x, Y), Y)
    ok(label, zero(-Fx / Fy - rhs(x, Y)))


def taylor_coeffs(ode_rhs, order, a, init, n_terms):
    """Successive derivatives of a DE y^(order) = ode_rhs(x, [y, y', ...]) at x = a; returns list of y^(k)(a)."""
    X = sp.symbols("X")
    Y = sp.Function("Y")(X)
    derivs = [Y] + [sp.diff(Y, X, k) for k in range(1, order)]
    expr = ode_rhs(X, derivs)
    vals = list(init)
    exprs = [expr]
    for _ in range(n_terms - order - 1):
        exprs.append(sp.diff(exprs[-1], X))
    for e in exprs:
        rep = {sp.diff(Y, X, k): vals[k] for k in range(len(vals) - 1, 0, -1)}
        sub = e.subs(rep).subs(Y, vals[0]).subs(X, a)
        vals.append(sp.nsimplify(sp.simplify(sub)))
    return vals


# 3.3 Euler substitution identities (with y as a generic function of x, x = e^t)
# dy/dt = x dy/dx and d2y/dt2 = x dy/dx + x^2 y''
g = sp.Function("g")
Yx = g(x)
dy_dt = x * sp.diff(Yx, x)               # chain rule with dx/dt = x
d2y_dt2 = x * sp.diff(dy_dt, x)          # d/dt = x d/dx
ok("x=e^t: d2y/dt2 = x y' + x^2 y''", zero(d2y_dt2 - (x * sp.diff(Yx, x) + x ** 2 * sp.diff(Yx, x, 2))))
# 3.4 y = z/x identity
Z = z(x)
Yv = Z / x
ok("y=z/x: x y'' + 2y' = z''", zero(x * sp.diff(Yv, x, 2) + 2 * sp.diff(Yv, x) - sp.diff(Z, x, 2)))
# Bernoulli general (n symbolic)
n = sp.symbols("n")
P, Q = sp.Function("P")(x), sp.Function("Q")(x)
Yb = y(x)
zz = Yb ** (1 - n)
expr = sp.diff(zz, x).subs(sp.Derivative(Yb, x), Q * Yb ** n - P * Yb) + (1 - n) * P * zz - (1 - n) * Q
ok("Bernoulli table", zero(sp.powsimp(sp.expand(expr), force=True)))

# E1: arctan(y/x) = 1/2 ln(x^2+y^2) solves dy/dx = (x+y)/(x-y), passes (1,0)
implicit_check("E1", lambda X, Y: sp.atan(Y / X) - sp.log(X ** 2 + Y ** 2) / 2, lambda X, Y: (X + Y) / (X - Y))
u = sp.symbols("u")
ok("E1 integral", zero(sp.diff(sp.atan(u) - sp.log(1 + u ** 2) / 2, u) - (1 - u) / (1 + u ** 2)))
# E2
sol = 1 / (c * x - x ** 2)
ok("E2", zero(sp.diff(sol, x) + sol / x - x * sol ** 2))
# E3
sol = A * x + B * x ** 2 + x ** 3 / 2
ok("E3", zero(x ** 2 * sp.diff(sol, x, 2) - 2 * x * sp.diff(sol, x) + 2 * sol - x ** 3))
st = A * E(t) + B * E(2 * t) + E(3 * t) / 2
ok("E3 t-eq", zero(sp.diff(st, t, 2) - 3 * sp.diff(st, t) + 2 * st - E(3 * t)))
# E4
sol = (A * sp.cos(2 * x) + B * sp.sin(2 * x)) / x
ok("E4", zero(x * sp.diff(sol, x, 2) + 2 * sp.diff(sol, x) + 4 * x * sol))
# E5 series 1 + 2x - x^2/2 - 2x^3/3 + x^4/8 : compare with exact solution y' + x y = 2 -> series
X = sp.symbols("X", real=True)
ser = 1 + 2 * X - X ** 2 / 2 - sp.Rational(2, 3) * X ** 3 + X ** 4 / 8
v = taylor_coeffs(lambda XX, D: -XX * D[1] - D[0], 2, 0, [1, 2], 5)
ok("E5 derivs", v == [1, 2, -1, -4, 3])
ok("E5 series", zero(sum(v[k] * X ** k / sp.factorial(k) for k in range(5)) - ser))
# independent check: power series of the ODE by undetermined coefficients
a = sp.symbols("a0:9")
S = sum(a[k] * X ** k for k in range(9))
eqs = sp.Poly(sp.expand(sp.diff(S, X, 2) + X * sp.diff(S, X) + S), X).all_coeffs()[::-1][:5]
solc = sp.solve(eqs + [a[0] - 1, a[1] - 2], a[:7], dict=True)[0]
ok("E5 undetermined coefficients", [solc[a[k]] for k in range(5)] == [1, 2, sp.Rational(-1, 2), sp.Rational(-2, 3), sp.Rational(1, 8)])
# E6
v = taylor_coeffs(lambda XX, D: XX ** 2 + D[0] ** 2, 1, 1, [1], 4)
ok("E6 derivs", v == [1, 2, 6, 22])
est = 1 + 2 * 0.1 + 3 * 0.01 + 11 / 3 * 0.001
dp("E6 estimate", est, "1.2337")
s = solve_ivp(lambda xx, yy: [xx ** 2 + yy[0] ** 2], [1, 1.1], [1], rtol=1e-12, atol=1e-12)
dp("E6 accurate", s.y[0][-1], "1.2342")

# Practice
sol = x * sp.sqrt(2 * sp.log(x) + c)  # y^2 = 2x^2 ln x + c x^2 (positive branch)
ok("P1", zero(sp.diff(sol, x) - (x ** 2 + sol ** 2) / (x * sol)))
sol = x / (1 - sp.log(x))
ok("P2", zero(x ** 2 * sp.diff(sol, x) - x * sol - sol ** 2) and sol.subs(x, 1) == 1)
sol = E(-x) / (c - x)
ok("P3", zero(sp.diff(sol, x) + sol - sol ** 2 * E(x)))
sol = sp.tan(x + c) - x
ok("P4", zero(sp.diff(sol, x) - (x + sol) ** 2))
for lab, sol, p, q, rhs in [("P6", A * x ** 2 + B * x ** 3, -4, 6, 0),
                            ("P7", A * sp.cos(3 * sp.log(x)) + B * sp.sin(3 * sp.log(x)), 1, 9, 0),
                            ("P8", (A + B * sp.log(x)) * x + sp.log(x) + 2, -1, 1, sp.log(x))]:
    ok(lab, zero(x ** 2 * sp.diff(sol, x, 2) + p * x * sp.diff(sol, x) + q * sol - rhs))
v = taylor_coeffs(lambda XX, D: XX + D[0] ** 2, 1, 0, [1], 4)
ok("P9", v == [1, 1, 3, 8])
v = taylor_coeffs(lambda XX, D: XX * D[0], 2, 0, [1, 0], 7)
ok("P10", v == [1, 0, 0, 1, 0, 0, 4])
ok("P10 coefficient", sp.Rational(4, 720) == sp.Rational(1, 180))
v = taylor_coeffs(lambda XX, D: D[0] / XX + XX, 1, 1, [2], 4)
ok("P11", v == [2, 3, 2, 0])
ok("P11 exact", zero(sp.expand(2 + 3 * (x - 1) + (x - 1) ** 2) - (x ** 2 + x)))
sol = x ** 2 + c * sp.log(x) + d
ok("P12", zero(x * sp.diff(sol, x, 2) + sp.diff(sol, x) - 4 * x))

# Section B
sol = x * sp.log(1 + sp.log(x))
ok("Q13", zero(x * sp.diff(sol, x) - sol - x * E(-sol / x)) and sol.subs(x, 1) == 0)
sf3("Q13c", float(sol.subs(x, sp.E)), "1.88")
sol = (A + B * sp.log(x)) / x + x / 4
ok("Q14b", zero(x ** 2 * sp.diff(sol, x, 2) + 3 * x * sp.diff(sol, x) + sol - x))
st = (A + B * t) * E(-t) + E(t) / 4
ok("Q14 t-eq", zero(sp.diff(st, t, 2) + 2 * sp.diff(st, t) + st - E(t)))
sol = (3 + 2 * sp.log(x)) / (4 * x) + x / 4
ok("Q14c", zero(x ** 2 * sp.diff(sol, x, 2) + 3 * x * sp.diff(sol, x) + sol - x) and sol.subs(x, 1) == 1
   and zero(sp.diff(sol, x).subs(x, 1)))
v = taylor_coeffs(lambda XX, D: 2 * XX * D[1] + 2 * D[0], 2, 0, [1, 1], 5)
ok("Q15 derivs", v == [1, 1, 2, 4, 12])
est = 1 + 0.2 + 0.04 + 2 / 3 * 0.008 + 0.5 * 0.0016
dp("Q15 estimate", est, "1.2461")
Yq = y(x)
ok("Q15a", zero(sp.diff(2 * x * sp.diff(Yq, x) + 2 * Yq, x) - (2 * x * sp.diff(Yq, x, 2) + 4 * sp.diff(Yq, x))))
sol = ((A + B * x) * E(-x) + E(x)) / x
ok("Q16", zero(x * sp.diff(sol, x, 2) + 2 * (x + 1) * sp.diff(sol, x) + (x + 2) * sol - 4 * E(x)))

print()
print("PASS pc03" if not FAILS else f"FAILED pc03: {FAILS}")
sys.exit(1 if FAILS else 0)
