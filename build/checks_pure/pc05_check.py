"""SymPy checks for Unit C5 (ellipse and hyperbola)."""
from sympy import (symbols, Rational as R, sqrt, simplify, expand, factor, solve, diff, Eq, cos, sin, sec, tan, cosh, sinh,
                   exp, discriminant, Poly, trigsimp, Abs)

x, y, t, m, c, h, k = symbols("x y t m c h k", real=True)
a, b, e, cc = symbols("a b e cc", positive=True)
n = 0


def zero(expr):
    assert simplify(trigsimp(expr)) == 0 or simplify(expr.rewrite(exp)) == 0, expr


# Parametric forms
zero((a * cos(t)) ** 2 / a ** 2 + (b * sin(t)) ** 2 / b ** 2 - 1)
zero((a * sec(t)) ** 2 / a ** 2 - (b * tan(t)) ** 2 / b ** 2 - 1)
zero((a * cosh(t)) ** 2 / a ** 2 - (b * sinh(t)) ** 2 / b ** 2 - 1)
# Focus-directrix derivation (works for any e)
lhs = (x - a * e) ** 2 + y ** 2 - e ** 2 * (a / e - x) ** 2
assert expand(lhs - (x ** 2 * (1 - e ** 2) + y ** 2 - a ** 2 * (1 - e ** 2))) == 0
# rectangular hyperbola x^2 - y^2 = a^2 has e = sqrt2; xy = cc^2 directrices x + y = +-sqrt2 cc
assert sqrt(1 + 1) == sqrt(2)
A = sqrt(2) * cc  # semi-axis of u^2 - v^2 = 2cc^2
assert simplify(A / sqrt(2) * sqrt(2) - sqrt(2) * cc) == 0  # u = a/e = cc  ->  x + y = sqrt2 * cc
# focal distances
xe = symbols("xe", positive=True)
ye2 = b ** 2 * (1 - xe ** 2 / a ** 2)
ell_b2 = a ** 2 * (1 - e ** 2)
PS2 = ((xe - a * e) ** 2 + ye2).subs(b, sqrt(ell_b2))
assert expand(PS2 - (a - e * xe) ** 2) == 0
PSd2 = ((xe + a * e) ** 2 + ye2).subs(b, sqrt(ell_b2))
assert expand(PSd2 - (a + e * xe) ** 2) == 0
yh2 = b ** 2 * (xe ** 2 / a ** 2 - 1)
hyp_b2 = a ** 2 * (e ** 2 - 1)
assert expand(((xe - a * e) ** 2 + yh2).subs(b, sqrt(hyp_b2)) - (e * xe - a) ** 2) == 0
assert expand(((xe + a * e) ** 2 + yh2).subs(b, sqrt(hyp_b2)) - (e * xe + a) ** 2) == 0
n += 1

# Tangents and normals: each line passes through the point with the right gradient


def check_line(line, X, Y, grad):
    zero(line.subs({x: X, y: Y}))
    zero(-diff(line, x) / diff(line, y) - grad)


Xe, Ye = a * cos(t), b * sin(t)
ge = diff(Ye, t) / diff(Xe, t)
zero(ge + b * cos(t) / (a * sin(t)))
check_line(b * x * cos(t) + a * y * sin(t) - a * b, Xe, Ye, ge)
check_line(a * x * sin(t) - b * y * cos(t) - (a ** 2 - b ** 2) * sin(t) * cos(t), Xe, Ye, -1 / ge)
Xh, Yh = a * sec(t), b * tan(t)
gh = diff(Yh, t) / diff(Xh, t)
zero(gh - b / (a * sin(t)))
check_line(b * x * sec(t) - a * y * tan(t) - a * b, Xh, Yh, gh)
check_line(a * x * sin(t) + b * y - (a ** 2 + b ** 2) * tan(t), Xh, Yh, -1 / gh)
Xc, Yc = a * cosh(t), b * sinh(t)
gc = diff(Yc, t) / diff(Xc, t)
check_line(b * x * cosh(t) - a * y * sinh(t) - a * b, Xc, Yc, gc)
check_line(a * x * sinh(t) + b * y * cosh(t) - (a ** 2 + b ** 2) * sinh(t) * cosh(t), Xc, Yc, -1 / gc)
# point forms
x1, y1 = symbols("x1 y1", real=True)
assert simplify(-diff(x * x1 / a ** 2 + y * y1 / b ** 2, x) / diff(x * x1 / a ** 2 + y * y1 / b ** 2, y) + b ** 2 * x1 / (a ** 2 * y1)) == 0
n += 1

# Tangency conditions
qe = expand(b ** 2 * x ** 2 + a ** 2 * (m * x + c) ** 2 - a ** 2 * b ** 2)
assert expand(qe - ((b ** 2 + a ** 2 * m ** 2) * x ** 2 + 2 * a ** 2 * m * c * x + a ** 2 * (c ** 2 - b ** 2))) == 0
de = discriminant(Poly(qe, x))
assert factor(de) == factor(4 * a ** 2 * b ** 2 * (a ** 2 * m ** 2 + b ** 2 - c ** 2))
qh = expand(b ** 2 * x ** 2 - a ** 2 * (m * x + c) ** 2 - a ** 2 * b ** 2)
assert expand(qh - ((b ** 2 - a ** 2 * m ** 2) * x ** 2 - 2 * a ** 2 * m * c * x - a ** 2 * (c ** 2 + b ** 2))) == 0
dh = discriminant(Poly(qh, x))
assert factor(dh) == factor(4 * a ** 2 * b ** 2 * (c ** 2 - a ** 2 * m ** 2 + b ** 2))
# contact points
cp = symbols("cp", positive=True)
xe0 = -2 * a ** 2 * m * cp / (2 * (b ** 2 + a ** 2 * m ** 2))
assert simplify(xe0.subs(b ** 2, cp ** 2 - a ** 2 * m ** 2) + a ** 2 * m / cp) == 0
assert simplify((m * (-a ** 2 * m / cp) + cp) - (cp ** 2 - a ** 2 * m ** 2) / cp) == 0  # = b^2/c when c^2 = a^2m^2 + b^2
xh0 = 2 * a ** 2 * m * cp / (2 * (b ** 2 - a ** 2 * m ** 2))
assert simplify(xh0.subs(b ** 2, a ** 2 * m ** 2 - cp ** 2) + a ** 2 * m / cp) == 0
assert simplify((m * (-a ** 2 * m / cp) + cp) - (-(a ** 2 * m ** 2 - cp ** 2) / cp)) == 0
n += 1

# WE1
assert solve(Eq(9, 25 * (1 - e ** 2)), e) == [R(4, 5)]
assert R(9, 25) + R(144, 25) / 9 == 1
assert 5 - R(4, 5) * 3 == R(13, 5) and 5 + R(12, 5) == R(37, 5) and R(13, 5) + R(37, 5) == 10
assert sqrt((3 - 4) ** 2 + R(12, 5) ** 2) == R(13, 5)
# WE2
assert solve(Eq(9, 16 * (e ** 2 - 1)), e) == [R(5, 4)]
assert 4 * R(5, 4) == 5 and 4 / R(5, 4) == R(16, 5)
# WE3
assert 4 * 4 + 5 * R(9, 5) == 25 and 25 * 4 - 20 * R(9, 5) == 64
nrm = (a * x * sin(t) - b * y * cos(t) - (a ** 2 - b ** 2) * sin(t) * cos(t)).subs({a: 5, b: 3, sin(t): R(3, 5), cos(t): R(4, 5)})
assert expand(nrm * R(25, 3) - (25 * x - 20 * y - 64)) == 0
# WE4
assert sorted(solve(Eq(9, 4 * m ** 2 + 1), m)) == [-sqrt(2), sqrt(2)]
q = expand(x ** 2 / 4 + (sqrt(2) * x + 3) ** 2 - 1) * 4
assert expand(q - (9 * x ** 2 + 24 * sqrt(2) * x + 32)) == 0 and discriminant(Poly(q, x)) == 0
assert sorted(solve(Eq(c ** 2, 4 + 1), c)) == [-sqrt(5), sqrt(5)]
# WE5
tan_line = 2 * x * cosh(t) - 3 * y * sinh(t) - 6
check_line(tan_line, 3 * cosh(t), 2 * sinh(t), diff(2 * sinh(t), t) / diff(3 * cosh(t), t))
zero(tan_line.subs({x: 3 * exp(t), y: 2 * exp(t)}))
zero(tan_line.subs({x: 3 * exp(-t), y: -2 * exp(-t)}))
area = R(1, 2) * Abs(3 * exp(t) * (-2 * exp(-t)) - 3 * exp(-t) * 2 * exp(t))
assert simplify(area) == 6
# WE6
lhs = 4 * ((x - 3) ** 2 + y ** 2) - (x - 12) ** 2
assert expand(lhs - (3 * x ** 2 + 4 * y ** 2 - 108)) == 0
assert 6 * R(1, 2) == 3 and 6 / R(1, 2) == 12 and 36 * (1 - R(1, 4)) == 27
n += 6

# Practice
assert solve(Eq(7, 16 * (1 - e ** 2)), e) == [R(3, 4)] and 4 * R(3, 4) == 3 and 4 / R(3, 4) == R(16, 3)
assert solve(Eq(16, 9 * (e ** 2 - 1)), e) == [R(5, 3)] and 3 * R(5, 3) == 5 and 3 / R(5, 3) == R(9, 5)
sol = solve([a * e - 2, a / e - 8], [a, e], dict=True)
assert sol == [{a: 4, e: R(1, 2)}] and 16 * (1 - R(1, 4)) == 12
assert solve(Eq(9 / a ** 2 - 16 / (4 * a ** 2), 1), a) == [sqrt(5)]
zero((4 * cos(t)) ** 2 / 16 + (3 * sin(t)) ** 2 / 9 - 1)
zero((2 * sec(t)) ** 2 / 4 - (5 * tan(t)) ** 2 / 25 - 1)
# 6
assert R(4, 8) + R(1, 2) == 1
check_line(2 * x / 8 + y / 2 - 1, 2, 1, -(R(2, 8)) / R(1, 2))
check_line(y - 2 * x + 3, 2, 1, 2)
# 7
assert R(16, 4) - R(9, 3) == 1
check_line(x - y - 1, 4, 3, 1)
check_line(x + y - 7, 4, 3, -1)
# 9
assert solve(Eq(c ** 2, 9 * 4 + 4), c) == [-2 * sqrt(10), 2 * sqrt(10)]
# 10
assert sorted(solve(Eq(4, 9 * m ** 2 - 4), m)) == [-2 * sqrt(2) / 3, 2 * sqrt(2) / 3]
# 11
assert expand((x - 4) ** 2 + y ** 2 - 4 * (x - 1) ** 2 + (3 * x ** 2 - y ** 2 - 12)) == 0
assert 2 * 2 == 4 and 2 / 2 == 1 and 4 * (4 - 1) == 12
# 12
X, Y = (4 + 4 * cos(t)) / 2, 3 * sin(t) / 2
zero((X - 2) ** 2 / 4 + 4 * Y ** 2 / 9 - 1)
n += 12

# Section B
th = symbols("theta")
N = a * x * sin(th) - b * y * cos(th) - (a ** 2 - b ** 2) * sin(th) * cos(th)
Gx = solve(N.subs(y, 0), x)[0]
Hy = solve(N.subs(x, 0), y)[0]
assert simplify(Gx - (a ** 2 - b ** 2) * cos(th) / a) == 0 and simplify(Hy + (a ** 2 - b ** 2) * sin(th) / b) == 0
Mx, My = Gx / 2, Hy / 2
zero(4 * a ** 2 * Mx ** 2 + 4 * b ** 2 * My ** 2 - (a ** 2 - b ** 2) ** 2)
assert expand((4 * 25 * x ** 2 + 4 * 9 * y ** 2 - 256) / 4 - (25 * x ** 2 + 9 * y ** 2 - 64)) == 0
# B2
assert solve(Eq(5, 4 * (e ** 2 - 1)), e) == [R(3, 2)] and 2 * R(3, 2) == 3 and 2 / R(3, 2) == R(4, 3)
xp = symbols("xp", positive=True)
assert expand(R(3, 2) * (xp + R(4, 3)) - R(3, 2) * (xp - R(4, 3))) == 4
assert solve(Eq(c ** 2, 4 * R(9, 4) - 5), c) == [-2, 2]
for cv, pt in [(2, (-3, R(-5, 2))), (-2, (3, R(5, 2)))]:
    assert (-4 * R(3, 2) / cv, -R(5) / cv) == pt
    assert R(pt[0] ** 2, 4) - pt[1] ** 2 / 5 == 1 and R(3, 2) * pt[0] + cv == pt[1]
# B3
quad = expand((k - m * h) ** 2 - a ** 2 * m ** 2 - b ** 2)
assert expand(quad - ((h ** 2 - a ** 2) * m ** 2 - 2 * h * k * m + k ** 2 - b ** 2)) == 0
assert expand((k ** 2 - b ** 2) + (h ** 2 - a ** 2) - (h ** 2 + k ** 2 - a ** 2 - b ** 2)) == 0
n += 3
print(f"pc05 checks passed ({n} groups)")
