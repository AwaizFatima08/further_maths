"""SymPy checks for Unit A6 (pure/pa06.py): determinants, inverses, factorisations, areas and volumes."""
from sympy import Matrix, Rational, symbols, simplify, expand, factor, eye, zeros, solve, sqrt, MatrixSymbol

M = lambda *rows: Matrix(rows)
R = Rational
n_checks = 0


def ok(cond, msg):
    global n_checks
    assert cond, msg
    n_checks += 1


def eq(a, b, msg):
    ok(simplify(Matrix(a) - Matrix(b)) == zeros(*Matrix(a).shape), msg)


def shoelace(pts):
    s = 0
    for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]):
        s += x1 * y2 - x2 * y1
    return abs(R(s, 2))


a, b, c, d, p, q, r, s_, k, x, t = symbols("a b c d p q r s k x t")
# 6.1 area derivation and figure
ok(expand((a + b) * (c + d) - a * c - b * d - 2 * b * c - (a * d - b * c)) == 0, "area derivation")
F = M([3, 1], [1, 2]); ok(F.det() == 5, "fig det")
ok(shoelace([(0, 0), (3, 1), (4, 3), (1, 2)]) == 5, "fig area")
# 6.2 example det
A = M([2, 0, 1], [1, 3, -1], [0, 1, 1]); ok(A.det() == 9, "6.2 det")
ok(2 * (3 + 1) - 1 * (0 - 1) == 9, "6.2 column expansion")
# 6.3 properties (2x2 symbolic det(AB))
A2 = M([a, b], [c, d]); B2 = M([p, q], [r, s_])
ok(expand((A2 * B2).det() - A2.det() * B2.det()) == 0, "det AB")
ok(expand((k * A2).det() - k ** 2 * A2.det()) == 0, "det kA 2x2")
G = Matrix(3, 3, symbols("g0:9")); ok(expand((k * G).det() - k ** 3 * G.det()) == 0, "det kA 3x3")
ok(expand(G.T.det() - G.det()) == 0, "det transpose")
ok(expand(A2 * M([d, -b], [-c, a]) - (a * d - b * c) * eye(2)) == zeros(2, 2), "2x2 inverse check")
# 6.10 Vandermonde
V = M([1, 1, 1], [a, b, c], [a ** 2, b ** 2, c ** 2])
ok(expand(V.det() - (a - b) * (b - c) * (c - a)) == 0, "vandermonde")
ok(expand((b - a) * (c - a) * (c - b) - (a - b) * (b - c) * (c - a)) == 0, "vandermonde sign")
ok(M([1, 0, 0], [a, 1, 1], [a ** 2, b + a, c + a]).det().expand() == (c - b).expand(), "vandermonde step")

# WE1
Mm = M([4, 1], [2, -1]); ok(Mm.det() == -6, "WE1 det")
eq(Mm * Matrix([2, 0]), Matrix([8, 4]), "WE1 A'"); eq(Mm * Matrix([1, 3]), Matrix([7, -1]), "WE1 B'")
ok(shoelace([(0, 0), (2, 0), (1, 3)]) == 3 and shoelace([(0, 0), (8, 4), (7, -1)]) == 18, "WE1 areas")
ok(2 * 3 - 0 * 1 > 0 and 8 * (-1) - 4 * 7 < 0, "WE1 orientation")
# WE2
A = M([1, k, 2], [0, 3, k], [2, 1, 4]); ok(expand(A.det() - k * (2 * k - 1)) == 0, "WE2 det")
ok(set(solve(A.det(), k)) == {0, R(1, 2)}, "WE2 roots")
# WE3
A = M([2, 0, 1], [1, 3, -1], [0, 1, 1])
minors = Matrix(3, 3, lambda i, j: A.minor(i, j)); eq(minors, M([4, 1, 1], [-1, 2, 2], [-3, -3, 6]), "WE3 minors")
eq(A.cofactor_matrix(), M([4, -1, 1], [1, 2, -2], [-3, 3, 6]), "WE3 cofactors")
eq(A.adjugate(), M([4, 1, -3], [-1, 2, 3], [1, -2, 6]), "WE3 adj"); eq(A.inv(), M([4, 1, -3], [-1, 2, 3], [1, -2, 6]) / 9, "WE3 inv")
# WE4
A = M([2, 1], [5, 3]); B = M([1, -2], [3, -4])
eq(A.inv(), M([3, -1], [-5, 2]), "WE4 Ainv"); eq(B.inv(), M([-4, 2], [-3, 1]) / 2, "WE4 Binv")
eq(A * B, M([5, -8], [14, -22]), "WE4 AB"); ok((A * B).det() == 2 == A.det() * B.det(), "WE4 det")
eq((A * B).inv(), M([-22, 8], [-14, 5]) / 2, "WE4 ABinv"); eq(B.inv() * A.inv(), (A * B).inv(), "WE4 rule")
X = M([1, 0], [2, 1]) * A.inv(); eq(X, M([3, -1], [1, 0]), "WE4 X"); eq(X * A, M([1, 0], [2, 1]), "WE4 XA")
# WE5
Mm = M([3, 1], [1, 1]); eq(Mm.inv(), M([1, -1], [-1, 3]) / 2, "WE5 inv")
for img, obj in [((4, 2), (1, 1)), ((5, 3), (1, 2)), ((2, 2), (0, 2))]:
    eq(Mm.inv() * Matrix(img), Matrix(obj), "WE5 vertex")
ok(shoelace([(1, 1), (1, 2), (0, 2)]) == R(1, 2) and shoelace([(4, 2), (5, 3), (2, 2)]) == 1, "WE5 areas")
# WE6
D6 = M([1, 1, 1], [a, b, c], [b * c, c * a, a * b])
ok(expand(D6.det() - (a - b) * (b - c) * (c - a)) == 0, "WE6")
ok(expand(M([0, 0, 1], [1, 1, c], [-c, -a, a * b]).det() - (c - a)) == 0, "WE6 step")
ok(expand(b * c - c * a + c * (a - b)) == 0 and expand(c * a - a * b + a * (b - c)) == 0, "WE6 column factor")

# Practice
ok(M([5, 3], [2, 4]).det() == 14 and M([-2, 7], [1, -3]).det() == -1, "P1ab")
ok(expand(M([a, 2 * a], [3, b]).det() - (a * b - 6 * a)) == 0, "P1c")
ok(set(solve(M([k, 3], [4, k + 1]).det(), k)) == {-4, 3}, "P1d")
eq(M([5, 3], [2, 4]).inv(), M([4, -3], [-2, 5]) / 14, "P2a"); eq(M([-2, 7], [1, -3]).inv(), M([3, 7], [1, 2]), "P2b")
ok(M([1, 2, 3], [0, 4, 5], [1, 0, 6]).det() == 22 and M([2, -1, 0], [3, 1, 4], [-1, 2, 1]).det() == -7, "P3")
ok(set(solve(M([x, 1, 0], [1, x, 1], [0, 1, x]).det(), x)) == {0, sqrt(2), -sqrt(2)}, "P4")
Mm = M([2, -3], [1, 4]); ok(Mm.det() * 5 == 55 and (Mm ** 2).det() * 5 == 605, "P5")
N = M([1, 2, 0], [0, 1, 3], [2, 0, 1]); ok(N.det() == 13 and 24 * N.det() == 312, "P6")
P7 = M([1, 2, 3], [0, 1, 4], [5, 6, 0]); ok(P7.det() == 1, "P7 det")
eq(P7.cofactor_matrix(), M([-24, 20, -5], [18, -15, 4], [5, -4, 1]), "P7 cof"); eq(P7.inv(), M([-24, 18, 5], [20, -15, -4], [-5, 4, 1]), "P7 inv")
# P8 with concrete matrices having those determinants
Aq = M([3, 0, 0], [0, 1, 0], [1, 2, 1]); Bq = M([-2, 1, 0], [0, 1, 0], [0, 4, 1])
ok(Aq.det() == 3 and Bq.det() == -2, "P8 setup")
ok((Aq * Bq).det() == -6 and Aq.inv().det() == R(1, 3) and (2 * Aq).det() == 24 and (Aq.T * Bq ** 2).det() == 12, "P8")
Ai = M([2, 1], [1, 1]); Bi = M([1, -1], [0, 2])
eq(Bi * Ai, M([1, 0], [2, 2]), "P9 (AB)^-1"); eq((Bi * Ai).inv(), M([1, 0], [-1, R(1, 2)]), "P9 AB")
eq(Ai.inv() * Bi.inv(), M([1, 0], [-1, R(1, 2)]), "P9 AB direct")
A = M([1, 2], [0, -1], [3, 1]); B = M([2, 0], [1, 4])
eq(A * B, M([4, 8], [-1, -4], [7, 4]), "P10 AB"); eq((A * B).T, M([4, -1, 7], [8, -4, 4]), "P10 T"); eq(B.T * A.T, (A * B).T, "P10 rule")
T = M([1, 2], [3, 5]); ok(T.det() == -1, "P11 det"); eq(T.inv(), M([-5, 2], [3, -1]), "P11 inv"); eq(T.inv() * Matrix([4, 11]), Matrix([2, 1]), "P11 pt")
ok(factor(M([x, 1, 1], [1, x, 1], [1, 1, x]).det()) == (x - 1) ** 2 * (x + 2), "P12")
ok(expand(M([1, 0, 0], [1, x - 1, 0], [1, 0, x - 1]).det() - (x - 1) ** 2) == 0, "P12 step")

# Exam 1
A = M([2, 1, -1], [0, k, 3], [1, 2, 1]); ok(expand(A.det() - 3 * (k - 3)) == 0, "E1a")
A2 = A.subs(k, 2); ok(A2.det() == -3, "E1c det")
eq(A2.cofactor_matrix(), M([-4, 3, -2], [-3, 3, -3], [5, -6, 4]), "E1c cof")
eq(A2.inv(), M([R(4, 3), 1, R(-5, 3)], [-1, -1, 2], [R(2, 3), 1, R(-4, 3)]), "E1c inv")
eq(A2.inv(), -R(1, 3) * M([-4, -3, 5], [3, 3, -6], [-2, -3, 4]), "E1c inv form")
ok(abs(A2.det()) * 7 == 21, "E1d")
# Exam 2
Mm = M([3, -1], [2, 1]); ok(Mm.det() == 5, "E2a"); eq(Mm.inv(), M([1, 1], [-2, 3]) / 5, "E2a inv")
for img, obj in [((2, 3), (1, 1)), ((6, 4), (2, 0)), ((-1, 1), (0, 1))]:
    eq(Mm.inv() * Matrix(img), Matrix(obj), "E2b")
ok(shoelace([(1, 1), (2, 0), (0, 1)]) == R(1, 2) and shoelace([(2, 3), (6, 4), (-1, 1)]) == R(5, 2), "E2c")
Nn = M([-1, 0], [0, 1]); eq(Nn * Mm, M([-3, 1], [2, 1]), "E2d"); ok((Nn * Mm).det() == -5, "E2d det")
# Exam 3
A = M([1, 2], [1, 3]); C = M([3, 1], [5, 2])
eq(C * A, M([4, 9], [7, 16]), "E3 B^-1"); B = (C * A).inv(); eq(B, M([16, -9], [-7, 4]), "E3 B")
eq((A * B).inv(), C, "E3 check"); eq(A * B, M([2, -1], [-5, 3]), "E3c AB")
ok((A * B).det() == 1 == A.det() * B.det(), "E3c")
# Exam 4
D4 = M([1, 1, 1], [a, b, c], [a ** 3, b ** 3, c ** 3])
ok(expand(D4.det() - (a - b) * (b - c) * (c - a) * (a + b + c)) == 0, "E4b")
ok(D4.det().subs(b, a) == 0, "E4a")
ok(expand(M([0, 0, 1], [1, 1, c], [a ** 2 + a * b + b ** 2, b ** 2 + b * c + c ** 2, c ** 3]).det()
          - (c - a) * (a + b + c)) == 0, "E4b step")
Mt = M([1, 1, 1], [1, 2, t], [1, 8, t ** 3]); ok(set(solve(Mt.det(), t)) == {1, 2, -3}, "E4c")
ok(expand(Mt.det() - (-1) * (2 - t) * (t - 1) * (3 + t)) == 0, "E4c form")

print(f"pa06: all {n_checks} checks passed")
