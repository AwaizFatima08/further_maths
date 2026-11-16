"""Checks every result stated in pure/pa13.py (Curve sketching, rational functions and inequalities)."""
import sys
from pathlib import Path

import numpy as np
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pure.pa13 import UNIT  # noqa: E402,F401

x, y = sp.symbols("x y", real=True)
FAILS = []


def ok_(label, cond):
    print(("ok  " if cond else "FAIL"), label)
    if not cond:
        FAILS.append(label)


def zero(label, expr):
    ok_(label, sp.simplify(expr) == 0)


def solset(label, expr_true, expected):
    """Compare sympy's solution set of an inequality with the stated one, plus a dense numeric scan."""
    got = sp.solve_univariate_inequality(expr_true, x, relational=False)
    ok = sp.simplify(got.symmetric_difference(expected)) in (sp.S.EmptySet,) or got == expected
    print(("ok  " if ok else "FAIL"), label, got)
    if not ok:
        FAILS.append(label)
    f = sp.lambdify(x, expr_true, "numpy")
    xs = np.linspace(-20, 20, 40001) + 1e-7
    with np.errstate(all="ignore"):
        truth = np.array(f(xs), dtype=bool)
    member = np.array([bool(expected.contains(sp.Float(v))) for v in xs[::40]])
    if not np.array_equal(truth[::40], member):
        print("FAIL numeric", label)
        FAILS.append(label + " numeric")


def stationary(f):
    return sorted([(sp.nsimplify(s), sp.simplify(f.subs(x, s))) for s in sp.solve(sp.diff(f, x), x) if s.is_real],
                  key=lambda t: float(t[0]))


def rng(f):
    """Range of f via the discriminant method (numerically checked)."""
    xs = np.linspace(-200, 200, 400001)
    vals = sp.lambdify(x, f, "numpy")(xs)
    vals = vals[np.isfinite(vals)]
    return vals.min(), vals.max()


R = sp.Rational
oo = sp.oo
I = sp.Interval
# Ex1
f = (2 * x + 1) / (x - 3)
zero("Ex1 form", f - (2 + 7 / (x - 3)))
ok_("Ex1 limit", sp.limit(f, x, oo) == 2 and f.subs(x, 0) == R(-1, 3))
sols = sp.solve(sp.Eq(f, x + 1), x)
ok_("Ex1 intersections", set(sols) == {2 + 2 * sp.sqrt(2), 2 - 2 * sp.sqrt(2)})
print("   Ex1 approx", [(round(float(s), 3), round(float(s + 1), 3)) for s in sols])
# Ex2
f = (x + 1) / (x**2 + 3)
ok_("Ex2 stationary", stationary(f) == [(-3, R(-1, 6)), (1, R(1, 2))])
lo, hi = rng(f)
ok_("Ex2 range numeric", abs(lo + 1 / 6) < 1e-6 and abs(hi - 0.5) < 1e-6)
zero("Ex2 discriminant", sp.expand(1 - 4 * y * (3 * y - 1) + (6 * y + 1) * (2 * y - 1)))
# Ex3
f = (x**2 + x - 2) / (x - 2)
zero("Ex3 division", f - (x + 3 + 4 / (x - 2)))
zero("Ex3 disc", sp.expand((1 - y)**2 - 4 * (2 * y - 2) - (y - 1) * (y - 9)))
ok_("Ex3 stationary", stationary(f) == [(0, 1), (4, 9)])
# Ex4
f = (x - 1) / (x + 2)
zero("Ex4 form", f - (1 - 3 / (x + 2)))
ok_("Ex4 values", f.subs(x, 0) == R(-1, 2) and (1 / f).subs(x, 0) == -2)
solset("Ex4 f<0 region", f < 0, I.open(-2, 1))
# Ex5
expr = 1 / (x - 1) > x / (x + 2)
solset("Ex5", expr, sp.Union(I.open(-2, 1 - sp.sqrt(3)), I.open(1, 1 + sp.sqrt(3))))
zero("Ex5 combine", 1 / (x - 1) - x / (x + 2) - (-x**2 + 2 * x + 2) / ((x - 1) * (x + 2)))
# Ex6
solset("Ex6", sp.Abs(x**2 - 1) > 2 * (x + 1), sp.Union(I.open(-oo, -1), I.open(3, oo)))
# Notes: y^2 = f example
g = (x + 1) * (x - 1) * (x - 3)
ok_("notes y^2 f(0)=3", g.subs(x, 0) == 3)
solset("notes f>=0 set", g >= 0, sp.Union(I(-1, 1), I(3, oo)))
# Notes inequality method (x + 3)/(x - 1) >= x - 3 ; transformations
zero("notes 2 + 7/(x-3)", (2 * x + 1) / (x - 3) - 2 - 7 / (x - 3))

# Practice
f = (3 * x - 2) / (x + 1)
zero("P1", f - (3 - 5 / (x + 1)))
ok_("P1 intercepts", f.subs(x, 0) == -2 and sp.solve(f, x) == [R(2, 3)])
solset("P2", (x + 3) / (x - 1) >= x - 3, sp.Union(I(-oo, 0), I.Lopen(1, 5)))
solset("P3", x**3 - 2 * x**2 - 5 * x + 6 > 0, sp.Union(I.open(-2, 1), I.open(3, oo)))
zero("P3 factor", x**3 - 2 * x**2 - 5 * x + 6 - (x - 1) * (x + 2) * (x - 3))
solset("P4", x**4 - 13 * x**2 + 36 <= 0, sp.Union(I(-3, -2), I(2, 3)))
f = (2 * x**2 - 3 * x + 1) / (x**2 - 4)
ok_("P5", sp.limit(f, x, oo) == 2 and f.subs(x, 0) == R(-1, 4) and set(sp.solve(f, x)) == {R(1, 2), 1}
    and sp.solve(sp.Eq(f, 2), x) == [3])
f = (2 * x**2 + 3 * x - 1) / (x + 2)
zero("P6", f - (2 * x - 1 + 1 / (x + 2)))
f = (x - 2) / (x**2 + 5)
ok_("P7 stationary", stationary(f) == [(-1, R(-1, 2)), (5, R(1, 10))])
lo, hi = rng(f)
ok_("P7 range", abs(lo + 0.5) < 1e-6 and abs(hi - 0.1) < 1e-6)
f = (x**2 + 3) / (x - 1)
ok_("P8 stationary", stationary(f) == [(-1, -2), (3, 6)])
zero("P8 disc", sp.expand(y**2 - 4 * (y + 3) - (y - 6) * (y + 2)))
solset("P9", sp.Abs(2 * x - 3) > sp.Abs(x + 1), sp.Union(I.open(-oo, R(2, 3)), I.open(4, oo)))
solset("P10", sp.Abs(x**2 - 4) < 3 * x, I.open(1, 4))
f = x**2 - 2 * x - 3
ok_("P11", (1 / f).subs(x, 0) == R(-1, 3) and (1 / f).subs(x, 1) == R(-1, 4) and stationary(f) == [(1, -4)])
solset("P11 f>=0", f >= 0, sp.Union(I(-oo, -1), I(3, oo)))
X, Y = sp.symbols("X Y")
zero("P12 b", (Y / 2 - ((X / 2)**3 - X / 2)) * 2 - (Y - (X**3 / 4 - X)))

# Exam
f = (x**2 - 3) / (x - 2)
zero("B1 a", f - (x + 2 + 1 / (x - 2)))
zero("B1 b disc", sp.expand(y**2 - 4 * (2 * y - 3) - (y - 2) * (y - 6)))
ok_("B1 b stationary", stationary(f) == [(1, 2), (3, 6)])
ok_("B1 c intercepts", f.subs(x, 0) == R(3, 2) and set(sp.solve(f, x)) == {sp.sqrt(3), -sp.sqrt(3)})
zero("B1 d part1", f - 2 - (x - 1)**2 / (x - 2))
zero("B1 d part2", f + 2 - (x**2 + 2 * x - 7) / (x - 2))
solset("B1 d", sp.Abs(f) > 2,
       sp.Union(I.open(-oo, -1 - 2 * sp.sqrt(2)), I.open(-1 + 2 * sp.sqrt(2), 2), I.open(2, oo)))
solset("B2 a", x / (x + 2) <= 2 / (x - 1), sp.Union(I.Lopen(-2, -1), I.Lopen(1, 4)))
solset("B2 b", sp.Abs(x**2 - 2 * x - 3) < x + 1, I.open(2, 4))
f = x**3 + x**2 - 2 * x
zero("B3 a factor", f - x * (x - 1) * (x + 2))
st = stationary(f)
ok_("B3 a x", {s for s, _ in st} == {(-1 + sp.sqrt(7)) / 3, (-1 - sp.sqrt(7)) / 3}
    or {sp.nsimplify(s) for s, _ in st} == {(-1 + sp.sqrt(7)) / 3, (-1 - sp.sqrt(7)) / 3})
xs = sorted(float(s) for s in sp.solve(sp.diff(f, x), x))
vals = [float(f.subs(x, v)) for v in xs]
print("   B3 stationary", xs, vals)
ok_("B3 c", f"{vals[0]:.3g}" == "2.11" and f"{np.sqrt(vals[0]):.3g}" == "1.45")
ok_("B3 d", f"{1 / vals[0]:.3g}" == "0.473" and f"{1 / vals[1]:.3g}" == "-1.58"
    and f"{xs[0]:.3g}" == "-1.22" and f"{xs[1]:.3g}" == "0.549")
solset("B3 f>=0", f >= 0, sp.Union(I(-2, 0), I(1, oo)))
f = (4 * x - 3) / (x - 1)
zero("B4 a", f - (4 + 1 / (x - 1)))
ok_("B4 b", set(sp.solve(sp.Eq(f, x + 2), x)) == {(3 + sp.sqrt(5)) / 2, (3 - sp.sqrt(5)) / 2})
solset("B4 c", f > x + 2, sp.Union(I.open(-oo, (3 - sp.sqrt(5)) / 2), I.open(1, (3 + sp.sqrt(5)) / 2)))

print("\nFAILED:" if FAILS else "\nALL CHECKS PASSED (pa13)", FAILS if FAILS else "")
sys.exit(1 if FAILS else 0)
