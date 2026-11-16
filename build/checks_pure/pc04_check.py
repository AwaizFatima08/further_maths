"""SymPy checks for Unit C4 (parabola and rectangular hyperbola)."""
from sympy import (symbols, Rational as R, sqrt, simplify, factor, expand, solve, diff, Eq, atan, deg, discriminant, Poly,
                   sec, cos, sin)

a, c, t, s, x, y, m, k, p, q = symbols("a c t s x y m k p q", nonzero=True)
n = 0


def close(v, target, tol=0.05):
    assert abs(float(v) - target) < tol, (float(v), target)


# Focus-directrix derivation
assert expand((x - a) ** 2 + y ** 2 - (x + a) ** 2) == y ** 2 - 4 * a * x
# parametric forms
assert expand((2 * a * t) ** 2 - 4 * a * (a * t ** 2)) == 0
assert simplify(c * t * (c / t) - c ** 2) == 0
# rectangular hyperbola is x^2 - y^2 = 2c^2 rotated by 45 degrees; e = sqrt2, foci (+-c sqrt2, +-c sqrt2)
u, v = symbols("u v")
X, Y = (u - v) / sqrt(2), (u + v) / sqrt(2)  # rotate
assert simplify(X * Y - (u ** 2 - v ** 2) / 2) == 0  # xy = c^2  <=>  u^2 - v^2 = 2c^2
cpos = symbols("cpos", positive=True)
A2 = 2 * cpos ** 2  # u^2/A2 - v^2/A2 = 1, so a^2 = b^2 = 2c^2
e2 = (A2 + A2) / A2
assert e2 == 2
fu = sqrt(A2) * sqrt(2)  # focus at (ae, 0) in (u, v) coordinates
assert simplify(fu - 2 * cpos) == 0
assert simplify(X.subs({u: 2 * cpos, v: 0}) - cpos * sqrt(2)) == 0 and simplify(Y.subs({u: 2 * cpos, v: 0}) - cpos * sqrt(2)) == 0
n += 1

# gradients
assert simplify(diff(2 * a * t, t) / diff(a * t ** 2, t) - 1 / t) == 0
assert simplify(diff(c / t, t) / diff(c * t, t) + 1 / t ** 2) == 0
# tangent & normal lines pass through the point with the right gradient
tan_par = t * y - x - a * t ** 2
nor_par = y + t * x - 2 * a * t - a * t ** 3
assert simplify(tan_par.subs({x: a * t ** 2, y: 2 * a * t})) == 0 and simplify(nor_par.subs({x: a * t ** 2, y: 2 * a * t})) == 0
assert simplify(-diff(tan_par, x) / diff(tan_par, y) - 1 / t) == 0 and simplify(-diff(nor_par, x) / diff(nor_par, y) + t) == 0
tan_h = x + t ** 2 * y - 2 * c * t
nor_h = t ** 3 * x - t * y - c * (t ** 4 - 1)
assert simplify(tan_h.subs({x: c * t, y: c / t})) == 0 and simplify(nor_h.subs({x: c * t, y: c / t})) == 0
assert simplify(-diff(tan_h, x) / diff(tan_h, y) + 1 / t ** 2) == 0 and simplify(-diff(nor_h, x) / diff(nor_h, y) - t ** 2) == 0
# second intersections of normals
expr = expand(nor_par.subs({x: a * s ** 2, y: 2 * a * s}))
assert simplify(expr - a * (s - t) * (t * s + t ** 2 + 2)) == 0
assert simplify(expand(nor_h.subs({x: c * s, y: c / s}) * s) - c * (s - t) * (t ** 3 * s + 1)) == 0
n += 1

# tangency conditions
d1 = discriminant(Poly(m * y ** 2 - 4 * a * y + 4 * a * k, y))
assert expand(d1 - (16 * a ** 2 - 16 * a * m * k)) == 0
assert solve(Eq(d1, 0), k) == [a / m]
ycont = solve(Eq(m * y ** 2 - 4 * a * y + 4 * a * (a / m), 0), y)
assert ycont == [2 * a / m]
assert simplify(((2 * a / m - a / m) / m) - a / m ** 2) == 0
d2 = discriminant(Poly(m * x ** 2 + k * x - c ** 2, x))
assert expand(d2 - (k ** 2 + 4 * m * c ** 2)) == 0
n += 1

# Loci results for P(ap^2, 2ap), Q(aq^2, 2aq)
chord = (p + q) * y - 2 * x - 2 * a * p * q
for tt in (p, q):
    assert simplify(chord.subs({x: a * tt ** 2, y: 2 * a * tt})) == 0
assert solve(Eq(chord.subs({x: a, y: 0}), 0), q) == [-1 / p]
sol = solve([p * y - x - a * p ** 2, q * y - x - a * q ** 2], [x, y], dict=True)[0]
assert simplify(sol[x] - a * p * q) == 0 and simplify(sol[y] - a * (p + q)) == 0
n += 1

# WE1
assert R(12, 4) == 3 and sqrt(36) == 6
# WE2: y^2 = 8x at (2,4)
assert solve(Eq(y ** 2 / 8 + y, 6), y) == [-12, 4]
assert R(144, 8) == 18
assert (2 * (-3) ** 2, 4 * (-3)) == (18, -12) and -1 - 2 / 1 == -3
# WE4 xy = 16
assert solve(Eq(4 * x - 16 / x, 30), x) == [R(-1, 2), 8]
assert R(16) / R(-1, 2) == -32
assert (4 * R(-1, 8), 4 / R(-1, 8)) == (R(-1, 2), -32)
assert (8 * 8 - 2 * 2 - 4 * (2 ** 4 - 1)) == 0
# WE5
assert solve(Eq(16 - 16 * k, 0), k) == [1]
assert solve(Eq(y ** 2 - 4 * y + 4, 0), y) == [2]
assert solve(Eq(3, R(3) / m), m) == [1]
assert factor(x ** 2 - 6 * x + 9) == (x - 3) ** 2
assert expand((x + 3) ** 2 - 12 * x) == x ** 2 - 6 * x + 9
# WE6
sol = solve([x + p ** 2 * y - 2 * c * p, x + q ** 2 * y - 2 * c * q], [x, y], dict=True)[0]
assert simplify(sol[x] - 2 * c * p * q / (p + q)) == 0 and simplify(sol[y] - 2 * c / (p + q)) == 0
assert simplify((c / q - c / p) / (c * q - c * p) + 1 / (p * q)) == 0
n += 6

# Practice
assert R(20, 4) == 5
assert expand((x - 2) ** 2 + y ** 2 - (x + 2) ** 2) == y ** 2 - 8 * x
assert simplify((6 * t) ** 2 - 12 * 3 * t ** 2) == 0 and simplify(5 * t * 5 / t) == 25
assert 9 + 4 == 13
# 6: y^2=4x at (4,4): a=1, t=2
assert (2 * 4 - 4 - 4) == 0 and (4 + 2 * 4 - 12) == 0
# 7: xy = 9 at (9,1): c=3, t=3
assert (9 + 9 * 1 - 18) == 0 and (9 * 9 - 1 - 80) == 0
assert simplify(tan_h.subs({c: 3, t: 3}) - (x + 9 * y - 18)) == 0
assert simplify(nor_h.subs({c: 3, t: 3}) / 3 - (9 * x - y - 80)) == 0
# 9
assert R(6, 3) == 2 and (R(6, 9), R(12, 3)) == (R(2, 3), 4)
assert 4 ** 2 == 24 * R(2, 3) and 3 * R(2, 3) + 2 == 4
# 10
assert sorted(solve(k ** 2 - 16, k)) == [-4, 4]
assert expand(x * (-x + k) - 4 + (x ** 2 - k * x + 4)) == 0
# 11 locus of midpoint of SP
X1, Y1 = (a + a * t ** 2) / 2, a * t
assert simplify(Y1 ** 2 - (2 * a * X1 - a ** 2)) == 0
# 12 midpoint of PG
G = solve(nor_par.subs(y, 0), x)[0]
assert simplify(G - (2 * a + a * t ** 2)) == 0
X2, Y2 = (a * t ** 2 + G) / 2, a * t
assert simplify(Y2 ** 2 - a * (X2 - a)) == 0
n += 12

# Section B
# B2
tt = R(1, 2)
assert (5 * tt, 5 / tt) == (R(5, 2), 10)
nor = nor_h.subs({c: 5, t: tt})
assert simplify(nor * 16 - (2 * x - 8 * y + 75)) == 0
xs = solve(Eq(2 * x - 8 * 25 / x + 75, 0), x)
assert sorted(xs) == [-40, R(5, 2)]
assert R(25) / -40 == R(-5, 8)
assert expand((2 * x - 5) * (x + 40)) == 2 * x ** 2 + 75 * x - 200
Ax = solve(tan_h.subs({c: 5, y: 0}), x)[0]
By = solve(tan_h.subs({c: 5, x: 0}), y)[0]
assert simplify(Ax * By / 2) == 50
# B3
ms = solve(Eq(1 + m, 2 / m), m)
assert sorted(ms) == [-2, 1]
assert [(R(2) / mm ** 2, R(4) / mm) for mm in (1, -2)] == [(2, 4), (R(1, 2), -2)]
close(deg(atan(3)), 71.6)
n += 3
print(f"pc04 checks passed ({n} groups)")
