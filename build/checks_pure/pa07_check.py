"""SymPy checks for Unit A7 (pure/pa07.py): invariant points, invariant lines through O and not through O."""
from sympy import Matrix, Rational, symbols, simplify, expand, eye, zeros, solve, Poly, atan, cos, sin, sqrt, linsolve

M = lambda *rows: Matrix(rows)
R = Rational
x, y, m, k, h, t, a, p, c = symbols("x y m k h t a p c")
n_checks = 0


def ok(cond, msg):
    global n_checks
    assert cond, msg
    n_checks += 1


def inv_points(A):
    """Solution set of (A - I)v = 0, as a list of basis vectors."""
    return (A - eye(2)).nullspace()


def gradients(A):
    """Real gradients m of invariant lines y = mx through O, plus whether x = 0 is invariant."""
    a_, b_, c_, d_ = A
    ms = sorted(set(r for r in solve(b_ * m ** 2 + (a_ - d_) * m - c_, m) if r.is_real))
    return ms, b_ == 0


def line_invariant(A, mm, kk):
    """Is y = mm*x + kk invariant under A (for all x)?"""
    X, Y = A * Matrix([x, mm * x + kk])
    return expand(Y - (mm * X + kk)) == 0


def all_invariant_lines(A):
    """Solve for (m, k) with y = mx + k invariant: coefficients of x and constant must vanish."""
    X, Y = A * Matrix([x, m * x + k])
    expr = expand(Y - (m * X + k))
    return solve([expr.coeff(x, 1), expr.coeff(x, 0)], [m, k], dict=True)


# 7.1 example
A = M([3, -2], [1, 0]); ns = inv_points(A); ok(len(ns) == 1 and ns[0][0] == ns[0][1], "7.1 y=x")
ok(M([2, 1], [1, 3]).__sub__(eye(2)).det() == 1, "7.1 det")
# 7.2 enlargement
ok(M([2, 0], [0, 2]) * Matrix([1, 1]) == Matrix([2, 2]), "7.2")
# 7.3 general condition
a_, b_, c_, d_ = symbols("a b c d")
X, Y = M([a_, b_], [c_, d_]) * Matrix([x, m * x])
ok(expand((Y - m * X) / x + (b_ * m ** 2 + (a_ - d_) * m - c_)) == 0, "7.3 condition")
# 7.4 shear example
ok(all(line_invariant(M([1, 3], [0, 1]), 0, kk) for kk in (-2, 0, 5)), "7.4 shear")
# 7.5 table
th = symbols("theta", real=True)
Ref = lambda tt: M([cos(2 * tt), sin(2 * tt)], [sin(2 * tt), -cos(2 * tt)])
Rf = Ref(th)
X, Y = Rf * Matrix([cos(th), sin(th)]); ok(simplify(X - cos(th)) == 0 and simplify(Y - sin(th)) == 0, "refl fixes L")
P0 = Matrix([cos(th), sin(th)]) * h + Matrix([-sin(th), cos(th)]) * t  # point on line perpendicular to L through h*u
img = Rf * P0
ok(simplify(img - (Matrix([cos(th), sin(th)]) * h - Matrix([-sin(th), cos(th)]) * t)) == zeros(2, 1), "refl perp lines")
Rot = lambda tt: M([cos(tt), -sin(tt)], [sin(tt), cos(tt)])
ok(gradients(Rot(R(1, 3)))[0] == [] , "rotation no lines (theta=1/3 rad)")
ok(gradients(M([3, 0], [0, 1])) == ([0], True), "stretch lines through O")
ok(all_invariant_lines(M([3, 0], [0, 1])) == [{m: 0}], "stretch: all y = k")
ok(all_invariant_lines(M([1, 3], [0, 1])) == [{m: 0}], "shear: all y = k")
# figure: reflection in y=2x
Mr = M([R(-3, 5), R(4, 5)], [R(4, 5), R(3, 5)])
ok(simplify(Mr - Ref(atan(2))) == zeros(2, 2), "WE4 matrix")
ok(Mr * Matrix([1, 2]) == Matrix([1, 2]), "WE4 fixed")
X, Y = Mr * Matrix([x, -x / 2 + k])
ok(expand(X - (-x + R(4, 5) * k)) == 0 and expand(Y - (x / 2 + R(3, 5) * k)) == 0, "WE4 image")
ok(line_invariant(Mr, R(-1, 2), k), "WE4 perpendicular invariant")

# WE1
ok(M([3, -2], [1, 0]) * Matrix([2, 2]) == Matrix([2, 2]), "WE1a")
N = M([1, 2], [3, 1]); ok((N - eye(2)).det() == -6 and inv_points(N) == [], "WE1b")
# WE2
A = M([3, 2], [1, 4]); ok(gradients(A) == ([R(-1, 2), 1], False), "WE2")
ok(A * Matrix([0, 1]) == Matrix([2, 4]), "WE2 x=0")
ok(A * Matrix([1, 1]) == Matrix([5, 5]) and A * Matrix([2, -1]) == Matrix([4, -2]), "WE2 images")
ok((A - eye(2)).det() == 4, "WE2 det")
# WE3
A = M([2, 1], [0, 1]); ns = inv_points(A); ok(len(ns) == 1 and ns[0][0] == -ns[0][1], "WE3a")
sols = all_invariant_lines(A)
ok({m: 0} in sols and {m: -1, k: 0} in sols and len(sols) == 2, f"WE3b {sols}")
X, Y = A * Matrix([h, y]); ok(expand(X - h) != 0, "WE3 vertical not invariant")
ok(A * Matrix([x, k]) == Matrix([2 * x + k, k]), "WE3 slide")
# WE5
A = M([1, a], [3, 2]); sol = solve((A * Matrix([1, 2]))[1] - 2 * (A * Matrix([1, 2]))[0], a); ok(sol == [R(5, 4)], "WE5a")
A = A.subs(a, R(5, 4)); ok(gradients(A) == ([R(-6, 5), 2], False), "WE5b")
ok(expand(4 * (R(5, 4) * m ** 2 - m - 3) - (5 * m ** 2 - 4 * m - 12)) == 0, "WE5b eq")
ok((A - eye(2)).det() == R(-15, 4), "WE5c")

# Practice
ns = inv_points(M([4, -3], [1, 0])); ok(len(ns) == 1 and ns[0][0] == ns[0][1], "P1a")
ns = inv_points(M([2, 1], [3, 4])); ok(len(ns) == 1 and ns[0][0] == -ns[0][1], "P1b")
ok((M([1, 2], [3, 1]) - eye(2)).det() == -6, "P1c")
kk = symbols("kk"); A = M([kk, 2], [3, 4]); ok(solve((A - eye(2)).det(), kk) == [3], "P2")
ns = inv_points(A.subs(kk, 3)); ok(ns[0][0] == -ns[0][1], "P2 line")
ok(gradients(M([4, 1], [2, 3])) == ([-2, 1], False), "P3a"); ok(gradients(M([5, -2], [3, 0])) == ([1, R(3, 2)], False), "P3b")
ok(gradients(M([0, -1], [1, 0])) == ([], False), "P4")
ok((M([3, 0], [0, 3]) - eye(2)).det() == 4, "P5")
A = M([1, 0], [3, 1]); ok(A * Matrix([0, y]) == Matrix([0, y]) and (A * Matrix([c, y]))[0] == c, "P6")
A = M([3, 0], [0, 1]); ok(all_invariant_lines(A) == [{m: 0}] and A * Matrix([0, y]) == Matrix([0, y]), "P7")
ok(solve((A * Matrix([h, y]))[0] - h, h) == [0], "P7 vertical")
A = M([0, 1], [1, 0]); ok(gradients(A) == ([-1, 1], False) and line_invariant(A, -1, k), "P8")
ns = inv_points(A); ok(ns[0][0] == ns[0][1], "P8 points")
A = M([3, 4], [4, -3]); ok(gradients(A) == ([-2, R(1, 2)], False), "P9a")
ok(A * Matrix([2, 1]) == 5 * Matrix([2, 1]) and A * Matrix([1, -2]) == -5 * Matrix([1, -2]), "P9a factors")
X, Y = A * Matrix([x, x / 2 + k]); ok(expand(X - (5 * x + 4 * k)) == 0 and expand(Y - (R(5, 2) * x - 3 * k)) == 0, "P9b image")
ok(solve(expand(Y - (X / 2 + k)), k) == [0], "P9b")
ok(simplify(A / 5 - Ref(atan(R(1, 2)))) == zeros(2, 2), "P9c")
ok((A - eye(2)).det() == -24, "P9 points")
A = M([1, 1], [0, 2]); ok(line_invariant(A, 1, k), "P10")
ns = inv_points(A); ok(len(ns) == 1 and ns[0][1] == 0, "P10 points")
A = M([1, 4], [1, 1]); ok(gradients(A) == ([R(-1, 2), R(1, 2)], False), "P11")
ok(A * Matrix([t, t / 2]) == 3 * Matrix([t, t / 2]) and A * Matrix([t, -t / 2]) == -Matrix([t, -t / 2]), "P11 images")

# Exam 1
A = M([5, -2], [1, 2]); ok((A - eye(2)).det() == 6, "E1a"); ok(gradients(A) == ([R(1, 2), 1], False), "E1b")
X, Y = A * Matrix([x, x + 1]); ok(expand(X - (3 * x - 2)) == 0 and expand(Y - (3 * x + 2)) == 0 and expand(Y - X) == 4, "E1c")
# Exam 2
A = M([R(3, 5), R(4, 5)], [R(4, 5), R(-3, 5)]); ok(A ** 2 == eye(2), "E2a")
ns = inv_points(A); ok(ns[0][1] / ns[0][0] == R(1, 2), "E2b"); ok(simplify(A - Ref(atan(R(1, 2)))) == zeros(2, 2), "E2b refl")
X, Y = A * Matrix([x, -2 * x + c]); ok(expand(X - (-x + R(4, 5) * c)) == 0 and expand(Y - (2 * x - R(3, 5) * c)) == 0, "E2c")
ok(line_invariant(A, -2, c), "E2c invariant"); ok(A * Matrix([0, c]) == Matrix([R(4, 5) * c, R(-3, 5) * c]), "E2d")
# Exam 3
A = M([1, 2], [p, 3]); ok(solve((A * Matrix([1, 2]))[1] - 2 * (A * Matrix([1, 2]))[0], p) == [4], "E3a")
A = A.subs(p, 4); ok(gradients(A) == ([-1, 2], False), "E3b")
ok(A * Matrix([1, 2]) == Matrix([5, 10]) and A * Matrix([1, -1]) == Matrix([-1, 1]), "E3c")
sols = all_invariant_lines(A); ok(sorted(sols, key=str) == sorted([{m: -1, k: 0}, {m: 2, k: 0}], key=str), f"E3d {sols}")
X, Y = A * Matrix([x, 2 * x + k]); ok(expand(X - (5 * x + 2 * k)) == 0 and expand(Y - (10 * x + 3 * k)) == 0, "E3d img1")
X, Y = A * Matrix([x, -x + k]); ok(expand(X - (-x + 2 * k)) == 0 and expand(Y - (x + 3 * k)) == 0, "E3d img2")
ok(A * Matrix([h, y]) == Matrix([h + 2 * y, 4 * h + 3 * y]), "E3d vertical")

print(f"pa07: all {n_checks} checks passed")
