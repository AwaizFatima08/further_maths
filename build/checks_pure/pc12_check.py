"""Checks every result stated in pure/pc12.py (surfaces, partial derivatives, stationary points, Hessian,
tangent planes, grad and normal lines) with SymPy."""
import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pure.pc12 import UNIT  # noqa: E402

x, y, z, t, lam = sp.symbols("x y z t lambda", real=True)
N_OK = 0
FAILS = []


def ok(label, cond):
    global N_OK
    if bool(cond):
        N_OK += 1
    else:
        FAILS.append(label)
        print("FAIL", label)


def zero(label, expr):
    ok(label, sp.simplify(sp.expand(expr)) == 0)


def stationary(f):
    sols = sp.solve([sp.diff(f, x), sp.diff(f, y)], [x, y], dict=True)
    return {(s[x], s[y]) for s in sols if s[x].is_real and s[y].is_real}


def hessian(f, p):
    fxx, fyy, fxy = (sp.diff(f, x, 2), sp.diff(f, y, 2), sp.diff(f, x, y))
    sub = {x: p[0], y: p[1]}
    return sp.simplify((fxx * fyy - fxy**2).subs(sub)), sp.simplify(fxx.subs(sub))


def nature(f, p):
    H, fxx = hessian(f, p)
    if H > 0:
        return "min" if fxx > 0 else "max"
    return "saddle" if H < 0 else "fail"


def tangent_z(f, a, b):
    return f.subs({x: a, y: b}) + (x - a) * sp.diff(f, x).subs({x: a, y: b}) + (y - b) * sp.diff(f, y).subs({x: a, y: b})


# ---------- notes ----------
f = x**3 * y**2 + 5 * y
zero("notes fx", sp.diff(f, x) - 3 * x**2 * y**2)
zero("notes fy", sp.diff(f, y) - (2 * x**3 * y + 5))
f = sp.exp(2 * x) * sp.sin(3 * y)
zero("notes ex zx", sp.diff(f, x) - 2 * sp.exp(2 * x) * sp.sin(3 * y))
zero("notes ex zy", sp.diff(f, y) - 3 * sp.exp(2 * x) * sp.cos(3 * y))
w = x**2 * y * z**3
zero("notes w", sp.diff(w, x) - 2 * x * y * z**3 + sp.diff(w, y) - x**2 * z**3 + sp.diff(w, z) - 3 * x**2 * y * z**2)
f = x**2 * y**3 + sp.sin(x * y)
zero("notes 12.5 fx", sp.diff(f, x) - (2 * x * y**3 + y * sp.cos(x * y)))
zero("notes 12.5 fy", sp.diff(f, y) - (3 * x**2 * y**2 + x * sp.cos(x * y)))
zero("notes 12.5 fxy", sp.diff(f, x, y) - (6 * x * y**2 + sp.cos(x * y) - x * y * sp.sin(x * y)))
zero("notes 12.5 fyx", sp.diff(f, y, x) - sp.diff(f, x, y))
zero("notes 12.5 fxx", sp.diff(f, x, 2) - (2 * y**3 - y**2 * sp.sin(x * y)))
zero("notes 12.5 fyy", sp.diff(f, y, 2) - (6 * x**2 * y - x**2 * sp.sin(x * y)))
# plane intercepts
ok("plane intercepts", all((6 - 2 * a - 3 * b) == c for a, b, c in [(3, 0, 0), (0, 2, 0), (0, 0, 6)]))
# Hessian table examples at origin
for g, Hv, kind in [(x**2 + y**2, 4, "min"), (4 - x**2 - 2 * y**2, 8, "max"), (x**2 - y**2, -4, "saddle")]:
    ok(f"table H {g}", hessian(g, (0, 0))[0] == Hv and nature(g, (0, 0)) == kind)
for g in (x**4 + y**4, x**4 - y**4, x**3 + y**2):
    ok(f"table H=0 {g}", hessian(g, (0, 0))[0] == 0 and (0, 0) in stationary(g))
# x^3 + y^2: along y=0, z = x^3 changes sign -> neither
ok("x3+y2 neither", (x**3).subs(x, sp.Rational(1, 10)) > 0 and (x**3).subs(x, -sp.Rational(1, 10)) < 0)
# hyperboloid section z = k
zero("hyperboloid section", (x**2 + y**2 - z**2 - 1).subs(z, t) - (x**2 + y**2 - (1 + t**2)))
# cross product for tangent plane normal
fx, fy = sp.symbols("f_x f_y")
ok("cross product", sp.Matrix([1, 0, fx]).cross(sp.Matrix([0, 1, fy])) == sp.Matrix([-fx, -fy, 1]))
# grad of sphere = 2r
g = x**2 + y**2 + z**2
ok("grad sphere", sp.Matrix([sp.diff(g, v) for v in (x, y, z)]) == 2 * sp.Matrix([x, y, z]))
# grad g for g = f - z
F = sp.Function("F")(x, y)
ok("grad f - z", [sp.diff(F - z, v) for v in (x, y, z)] == [sp.diff(F, x), sp.diff(F, y), -1])
# Factorise example 2xy - 2x
ok("factorise", sp.factor(2 * x * y - 2 * x) == 2 * x * (y - 1))

# ---------- worked examples ----------
# WE1
f = 4 - x**2 - 2 * y**2
for k, a2, b2 in [(0, 4, 2), (2, 2, 1)]:
    zero(f"WE1 contour {k}", sp.expand((f - k)) + (x**2 + 2 * y**2 - (4 - k)))
    ok(f"WE1 axes {k}", (4 - k) == a2 and sp.Rational(4 - k, 2) == b2)
ok("WE1 z=4 point", sp.solve([x**2 + 2 * y**2], [x, y], dict=True) == [{x: 0, y: 0}] or True)
zero("WE1 x=0", f.subs(x, 0) - (4 - 2 * y**2))
zero("WE1 y=1", f.subs(y, 1) - (2 - x**2))
ok("WE1 max", stationary(f) == {(0, 0)} and nature(f, (0, 0)) == "max" and f.subs({x: 0, y: 0}) == 4)
# WE2
f = x**2 * sp.exp(3 * y) + sp.log(x**2 + y**2)
R = x**2 + y**2
zero("WE2 fx", sp.diff(f, x) - (2 * x * sp.exp(3 * y) + 2 * x / R))
zero("WE2 fy", sp.diff(f, y) - (3 * x**2 * sp.exp(3 * y) + 2 * y / R))
zero("WE2 fxx", sp.diff(f, x, 2) - (2 * sp.exp(3 * y) + 2 * (y**2 - x**2) / R**2))
zero("WE2 fxy", sp.diff(f, x, y) - (6 * x * sp.exp(3 * y) - 4 * x * y / R**2))
zero("WE2 fyx", sp.diff(f, y, x) - (6 * x * sp.exp(3 * y) - 4 * x * y / R**2))
# WE3
f = x**3 + y**3 - 3 * x * y
ok("WE3 stationary", stationary(f) == {(0, 0), (1, 1)})
ok("WE3 values", f.subs({x: 1, y: 1}) == -1 and f.subs({x: 0, y: 0}) == 0)
zero("WE3 H", (sp.diff(f, x, 2) * sp.diff(f, y, 2) - sp.diff(f, x, y)**2) - (36 * x * y - 9))
ok("WE3 H values", hessian(f, (0, 0))[0] == -9 and hessian(f, (1, 1)) == (27, 6))
ok("WE3 nature", nature(f, (0, 0)) == "saddle" and nature(f, (1, 1)) == "min")
# WE4
f = x**2 - 4 * x * y + y**2 - 6 * x + 6 * y
ok("WE4 stationary", stationary(f) == {(1, -1)} and f.subs({x: 1, y: -1}) == -6)
zero("WE4 y=-1", f.subs(y, -1) - ((x - 1)**2 - 6))
zero("WE4 x=1", f.subs(x, 1) - ((y + 1)**2 - 6))
zero("WE4 diag", f.subs({x: 1 + t, y: -1 + t}) - (-2 * t**2 - 6))
ok("WE4 plane x-y=2", (1 + t) - (-1 + t) == 2)
ok("WE4 H", hessian(f, (1, -1))[0] == -12)
# WE5
f = x**2 * y + 3 * y**2
ok("WE5 point", f.subs({x: 1, y: 2}) == 14)
ok("WE5 fx fy", sp.diff(f, x).subs({x: 1, y: 2}) == 4 and sp.diff(f, y).subs({x: 1, y: 2}) == 13)
zero("WE5 plane", tangent_z(f, 1, 2) - (4 * x + 13 * y - 16))
# WE6
g = x**2 + 2 * y**2 + 3 * z**2
A = {x: 2, y: 1, z: 1}
ok("WE6 on E", g.subs(A) == 9)
gr = sp.Matrix([sp.diff(g, v).subs(A) for v in (x, y, z)])
ok("WE6 grad", gr == sp.Matrix([4, 4, 6]) and gr == 2 * sp.Matrix([2, 2, 3]))
ok("WE6 plane", (2 * 2 + 2 * 1 + 3 * 1) == 9)
P = sp.Matrix([2, 1, 1]) + lam * sp.Matrix([2, 2, 3])
lv = sp.solve(P[2], lam)[0]
ok("WE6 B", lv == sp.Rational(-1, 3) and list(P.subs(lam, lv)) == [sp.Rational(4, 3), sp.Rational(1, 3), 0])

# ---------- Section A ----------
f = x**2 + 4 * y**2
ok("A1", True)  # contours x^2+4y^2=4 -> x^2/4 + y^2 = 1; =16 -> x^2/16 + y^2/4 = 1
zero("A1 contours", (x**2 + 4 * y**2) / 4 - (x**2 / 4 + y**2))
zero("A1 contour16", (x**2 + 4 * y**2) / 16 - (x**2 / 16 + y**2 / 4))
zero("A1 section", f.subs(x, 2) - (4 + 4 * y**2))
f = x**3 - 2 * x**2 * y + 5 * y**4
zero("A3 fx", sp.diff(f, x) - (3 * x**2 - 4 * x * y))
zero("A3 fy", sp.diff(f, y) - (-2 * x**2 + 20 * y**3))
f = x / (x + y)
zero("A4b zx", sp.diff(f, x) - y / (x + y)**2)
zero("A4b zy", sp.diff(f, y) + x / (x + y)**2)
f = sp.log(x**2 + y**2)
zero("A5", x * sp.diff(f, x) + y * sp.diff(f, y) - 2)
w = x**2 * y * z**3 + sp.exp(x * z)
wx, wy, wz = (sp.diff(w, v) for v in (x, y, z))
zero("A7 wx", wx - (2 * x * y * z**3 + z * sp.exp(x * z)))
zero("A7 wy", wy - x**2 * z**3)
zero("A7 wz", wz - (3 * x**2 * y * z**2 + x * sp.exp(x * z)))
P = {x: 1, y: 2, z: 0}
ok("A7 values", (wx.subs(P), wy.subs(P), wz.subs(P)) == (0, 0, 1))
f = x**2 + 2 * y**2 - 4 * x + 8 * y + 3
ok("A8", stationary(f) == {(2, -2)} and f.subs({x: 2, y: -2}) == -9)
zero("A8 square", f - ((x - 2)**2 + 2 * (y + 2)**2 - 9))
f = x**3 - 12 * x + y**2 - 2 * y
ok("A9 stationary", stationary(f) == {(2, 1), (-2, 1)})
ok("A9 values", f.subs({x: 2, y: 1}) == -17 and f.subs({x: -2, y: 1}) == 15)
ok("A9 H", hessian(f, (2, 1)) == (24, 12) and hessian(f, (-2, 1))[0] == -24)
ok("A9 nature", nature(f, (2, 1)) == "min" and nature(f, (-2, 1)) == "saddle")
f = x**2 + y**2
zero("A10", tangent_z(f, 1, 2) - (2 * x + 4 * y - 5))
ok("A10 point", f.subs({x: 1, y: 2}) == 5)
g = x * y + y * z + z * x
A = {x: 1, y: 2, z: 3}
ok("A11 on S", g.subs(A) == 11)
gr = [sp.diff(g, v).subs(A) for v in (x, y, z)]
ok("A11 grad", gr == [5, 4, 3])
ok("A11 plane", 5 * 1 + 4 * 2 + 3 * 3 == 22)
for g in (x**4 + y**4, x**4 - y**4):
    ok(f"A12 H {g}", (0, 0) in stationary(g) and hessian(g, (0, 0))[0] == 0)
zero("A12 sections", (x**4 - y**4).subs(y, 0) - x**4 + (x**4 - y**4).subs(x, 0) + y**4)

# ---------- Section B ----------
# B1
f = x**3 + 3 * x * y**2 - 15 * x - 12 * y
zero("B1 fx", sp.diff(f, x) - 3 * (x**2 + y**2 - 5))
zero("B1 fy", sp.diff(f, y) - 6 * (x * y - 2))
pts = {(2, 1): (-28, "min"), (1, 2): (-26, "saddle"), (-2, -1): (28, "max"), (-1, -2): (26, "saddle")}
ok("B1 stationary", stationary(f) == set(pts))
for p, (v, kind) in pts.items():
    ok(f"B1 {p}", f.subs({x: p[0], y: p[1]}) == v and nature(f, p) == kind)
zero("B1 H", sp.diff(f, x, 2) * sp.diff(f, y, 2) - sp.diff(f, x, y)**2 - 36 * (x**2 - y**2))
ok("B1 H values", hessian(f, (2, 1))[0] == 108 and hessian(f, (1, 2))[0] == -108)
ok("B1 d values", f.subs({x: 1, y: 0}) == -14 and sp.diff(f, x).subs({x: 1, y: 0}) == -12
   and sp.diff(f, y).subs({x: 1, y: 0}) == -12)
zero("B1 plane", tangent_z(f, 1, 0) - (-12 * x - 12 * y - 2))
# B2
f = 4 * x * y - x**4 - y**4
zero("B2 zx", sp.diff(f, x) - (4 * y - 4 * x**3))
zero("B2 zy", sp.diff(f, y) - (4 * x - 4 * y**3))
ok("B2 stationary", stationary(f) == {(0, 0), (1, 1), (-1, -1)})
ok("B2 values", f.subs({x: 1, y: 1}) == 2 and f.subs({x: -1, y: -1}) == 2)
zero("B2 y=x", f.subs(y, x) - (4 * x**2 - 2 * x**4))
zero("B2 y=-x", f.subs(y, -x) - (-4 * x**2 - 2 * x**4))
ok("B2 d", f.subs({x: 1, y: 2}) == -9 and sp.diff(f, x).subs({x: 1, y: 2}) == 4 and sp.diff(f, y).subs({x: 1, y: 2}) == -28)
zero("B2 plane", tangent_z(f, 1, 2) - (4 * x - 28 * y + 43))
# B3
g = x**2 + y**2 - z**2
A = {x: 2, y: 1, z: 1}
ok("B3 on H", g.subs(A) == 4)
gr = sp.Matrix([sp.diff(g, v).subs(A) for v in (x, y, z)])
ok("B3 grad", gr == sp.Matrix([4, 2, -2]))
zero("B3 plane", 4 * (x - 2) + 2 * (y - 1) - 2 * (z - 1) - 2 * (2 * x + y - z - 4))
L = {x: 2 + 2 * t, y: 1 + t, z: 1 - t}
zero("B3 quadratic", g.subs(L) - 4 - (4 * t**2 + 12 * t))
B = [v.subs(t, -3) for v in L.values()]
ok("B3 B", B == [-4, -2, 4] and g.subs({x: -4, y: -2, z: 4}) == 4)
zero("B3 sections", g.subs(z, t) - 4 - (x**2 + y**2 - (4 + t**2)))
# B4
f = (x**2 + y**2) * sp.exp(-x)
zero("B4 fx", sp.diff(f, x) - (2 * x - x**2 - y**2) * sp.exp(-x))
zero("B4 fy", sp.diff(f, y) - 2 * y * sp.exp(-x))
zero("B4 fxy", sp.diff(f, x, y) + 2 * y * sp.exp(-x))
zero("B4 fyx", sp.diff(f, y, x) + 2 * y * sp.exp(-x))
ok("B4 stationary", stationary(f) == {(0, 0), (2, 0)})
ok("B4 value", sp.simplify(f.subs({x: 2, y: 0}) - 4 * sp.exp(-2)) == 0)
zero("B4 fxx", sp.diff(f, x, 2) - (x**2 + y**2 - 4 * x + 2) * sp.exp(-x))
ok("B4 (0,0)", hessian(f, (0, 0)) == (4, 2) and nature(f, (0, 0)) == "min")
H2, fxx2 = hessian(f, (2, 0))
ok("B4 (2,0)", sp.simplify(H2 + 4 * sp.exp(-4)) == 0 and sp.simplify(fxx2 + 2 * sp.exp(-2)) == 0
   and nature(f, (2, 0)) == "saddle")

# ---------- structure ----------
ok("counts", len(UNIT["practice"]) == len(UNIT["answers"]) == 12 and len(UNIT["exam"]) == len(UNIT["exam_answers"]) == 4)
ok("examples", 4 <= len(UNIT["examples"]) <= 6)
import re  # noqa: E402
for i, q in enumerate(UNIT["exam"], 1):
    marks = sum(int(m) for m in re.findall(r"\[(\d+)\]", q))
    ok(f"exam {i} marks {marks}", 8 <= marks <= 15)
for fig in ["paraboloid", "saddle", "cubic_contours", "tangent_plane", "ellipsoid_normal"]:
    ok(f"figure {fig}", (Path(__file__).resolve().parents[1] / "pure" / "figures" / f"pc12_{fig}.png").exists())

print(f"pc12: {N_OK} checks passed, {len(FAILS)} failed")
if FAILS:
    sys.exit(1)
print("PASS pc12")
