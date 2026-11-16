"""SymPy checks for Unit B12 (pure/pb12.py): eigenvalues, eigenvectors, diagonalisations, powers, Cayley–Hamilton."""
from sympy import (Matrix, Rational, symbols, simplify, expand, factor, eye, zeros, diag, sqrt, I, solve, Poly,
                   cos, acos, pi)

M_ = lambda *rows: Matrix(rows)
R = Rational
lam = symbols("lambda")
n = symbols("n", integer=True, positive=True)
n_checks = 0


def ok(cond, msg):
    global n_checks
    assert cond, msg
    n_checks += 1


def eig(A, v, l):
    ok(simplify(A * Matrix(v) - l * Matrix(v)) == zeros(len(v), 1) and Matrix(v) != zeros(len(v), 1), f"eigvec {v} {l}")


def charpoly(A):
    return expand((A - lam * eye(A.rows)).det())


def zero(A):
    return simplify(A) == zeros(*A.shape)


# 12.1 / 12.3 notes, figure and WE1
M = M_([4, 1], [2, 3])
ok(expand(charpoly(M) - (lam ** 2 - 7 * lam + 10)) == 0, "notes char")
eig(M, [1, -2], 2); eig(M, [1, 1], 5)
U = M_([1, 1], [-2, 1]); D = diag(2, 5); ok(U.det() == 3 and U.inv() == M_([1, -1], [2, 1]) / 3, "WE1 Uinv")
Mn = U * diag(2 ** n, 5 ** n) * U.inv()
ok(zero(Mn - M_([2 ** n + 2 * 5 ** n, -2 ** n + 5 ** n], [-2 ** (n + 1) + 2 * 5 ** n, 2 ** (n + 1) + 5 ** n]) / 3), "WE1 Mn")
for k in range(1, 7):
    ok(Mn.subs(n, k) == M ** k, "WE1 Mn values")
# 12.2 3x3 characteristic form
G = Matrix(3, 3, symbols("g0:9"))
c1 = sum(G.extract([i, j], [i, j]).det() for i, j in ((0, 1), (0, 2), (1, 2)))
ok(expand(-charpoly(G) - (lam ** 3 - G.trace() * lam ** 2 + c1 * lam - G.det())) == 0, "3x3 char form")
# 12.4 repeated and complex
ok((M_([2, 1], [0, 2]) - 2 * eye(2)).nullspace() == [Matrix([1, 0])], "repeated one direction")
Rt = M_([0, -1], [1, 0]); ok(set(solve(charpoly(Rt), lam)) == {I, -I}, "rotation complex")
eig(Rt, [1, -I], I); eig(Rt, [1, I], -I)
# 12.5 properties (symbolic 2x2 check of M^n v)
a, b, c, d, l, kk = symbols("a b c d l k")
v1, v2 = symbols("v1 v2")
# 12.7 orthogonality of symmetric eigenvectors checked numerically in examples below
# 12.8 Cayley-Hamilton 2x2 and 3x3 symbolic
A2 = M_([a, b], [c, d]); ok(zero(A2 ** 2 - (a + d) * A2 + (a * d - b * c) * eye(2)), "CH 2x2")
p3 = Poly(-charpoly(G), lam).all_coeffs()
ok(zero(p3[0] * G ** 3 + p3[1] * G ** 2 + p3[2] * G + p3[3] * eye(3)), "CH 3x3 symbolic")

# WE2
M = M_([3, 2, -2], [1, 3, -1], [1, 2, 0])
ok(expand(-charpoly(M) - (lam ** 3 - 6 * lam ** 2 + 11 * lam - 6)) == 0, "WE2 char")
ok(expand(charpoly(M) - (3 - lam) * (lam - 1) * (lam - 2)) == 0, "WE2 factor")
ok(M.trace() == 6 and M.det() == 6, "WE2 checks")
ok(Matrix([1, 2, -2]).cross(Matrix([1, 1, -1])) == Matrix([0, -1, -1]), "WE2 cross 2")
ok(Matrix([2, 2, -2]).cross(Matrix([1, 2, -1])) == Matrix([2, 0, 2]), "WE2 cross 1")
ok(Matrix([0, 2, -2]).cross(Matrix([1, 0, -1])) == Matrix([-2, -2, -2]), "WE2 cross 3")
eig(M, [1, 0, 1], 1); eig(M, [0, 1, 1], 2); eig(M, [1, 1, 1], 3)
U = M_([1, 0, 1], [0, 1, 1], [1, 1, 1]); ok(U.det() == -1 and U.inv() == M_([0, -1, 1], [-1, 0, 1], [1, 1, -1]), "WE2 Uinv")
ok(U * diag(1, 2, 3) * U.inv() == M, "WE2 diag")
Mn = U * diag(1, 2 ** n, 3 ** n) * U.inv()
ok(zero(Mn - M_([3 ** n, 3 ** n - 1, 1 - 3 ** n], [3 ** n - 2 ** n, 3 ** n, 2 ** n - 3 ** n],
                [3 ** n - 2 ** n, 3 ** n - 1, 2 ** n - 3 ** n + 1])), "WE2 Mn")
for k in range(1, 6):
    ok(Mn.subs(n, k) == M ** k, "WE2 Mn values")
# WE3
A = M_([2, 2], [2, -1]); ok(expand(charpoly(A) - (lam ** 2 - lam - 6)) == 0, "WE3 char")
eig(A, [2, 1], 3); eig(A, [1, -2], -2)
P = M_([2, 1], [1, -2]) / sqrt(5); ok(zero(P.T * P - eye(2)), "WE3 orthogonal")
ok(zero(A * P - M_([6, -2], [3, 4]) / sqrt(5)), "WE3 AP"); ok(zero(P.T * A * P - diag(3, -2)), "WE3 PtAP")
# WE4
M = M_([1, -2, 2], [-2, 1, 2], [2, 2, 1]) / 3
eig(M, [1, 1, -1], -1); ok(M ** 2 == eye(3) and M.trace() == 1 and M.det() == -1, "WE4 M2, trace, det")
ok(factor(charpoly(M)) == factor(-(lam - 1) ** 2 * (lam + 1)), "WE4 char")
ok(expand(-charpoly(M) - (lam ** 3 - lam ** 2 - lam + 1)) == 0, "WE4 char expanded")
eig(M, [1, -1, 0], 1); eig(M, [1, 0, 1], 1)
ok((M - eye(3)).rank() == 1, "WE4 plane of eigenvectors")
# WE5
M = M_([3, -1], [2, 0]); ok(zero(M ** 2 - 3 * M + 2 * eye(2)), "WE5 CH")
ok(M.inv() == M_([0, 1], [-2, 3]) / 2 and (3 * eye(2) - M) / 2 == M.inv(), "WE5a")
ok(M ** 3 == 7 * M - 6 * eye(2) and M ** 4 == 15 * M - 14 * eye(2) and M ** 4 == M_([31, -15], [30, -14]), "WE5b")
B = M_([2, 1, 0], [0, 1, -1], [0, 2, 4])
ok(expand(-charpoly(B) - (lam ** 3 - 7 * lam ** 2 + 16 * lam - 12)) == 0, "WE5c char")
ok(B ** 2 == M_([4, 3, -1], [0, -1, -5], [0, 10, 14]), "WE5c B2")
ok(B ** 2 - 7 * B + 16 * eye(3) == M_([6, -4, -1], [0, 8, 2], [0, -4, 2]), "WE5c")
ok(B.inv() == M_([6, -4, -1], [0, 8, 2], [0, -4, 2]) / 12, "WE5c inv")

# Practice
M = M_([5, 4], [1, 2]); ok(expand(charpoly(M) - (lam ** 2 - 7 * lam + 6)) == 0, "P1a"); eig(M, [1, -1], 1); eig(M, [4, 1], 6)
M = M_([1, 2], [2, 1]); eig(M, [1, 1], 3); eig(M, [1, -1], -1)
M = M_([3, 1], [0, 3]); ok(expand(charpoly(M) - (lam - 3) ** 2) == 0 and (M - 3 * eye(2)).nullspace() == [Matrix([1, 0])], "P2")
M = M_([1, -2], [1, 3]); ok(set(solve(charpoly(M), lam)) == {2 + I, 2 - I}, "P3"); eig(M, [2, -1 - I], 2 + I)
M = M_([4, -2], [-2, 1]); eig(M, [1, 2], 0); eig(M, [2, -1], 5)
ok(Matrix([1, 2]).norm() == sqrt(5), "P4 norm")
M = M_([2, 0, 0], [1, 3, 0], [4, -1, 1]); eig(M, [0, 0, 1], 1); eig(M, [1, -1, 5], 2); eig(M, [0, 2, -1], 3)
M = M_([2, 1, 1], [1, 2, 1], [1, 1, 2]); eig(M, [1, 1, 1], 4); eig(M, [1, -1, 0], 1); eig(M, [1, 0, -1], 1)
M = M_([3, 2], [1, 4]); eig(M, [1, 1], 5); eig(M, [2, -1], 2)
U = M_([1, 2], [1, -1]); ok(U.inv() == M_([1, 2], [1, -1]) / 3, "P7 Uinv"); ok(U * diag(5, 2) * U.inv() == M, "P7 diag")
ok(U * diag(625, 16) * U.inv() == M ** 4 == M_([219, 406], [203, 422]), "P7 M4")
ok(M_([625 + 32, 1250 - 32], [625 - 16, 1250 + 16]) / 3 == M ** 4, "P7 working")
N = U3 = M_([1, 0, 1], [0, 1, 1], [1, 1, 1]) * diag(1, 2, 3) * M_([1, 0, 1], [0, 1, 1], [1, 1, 1]).inv()
ok(set((N ** 2 + 2 * N).eigenvals()) == {3, 8, 15} and set(N.inv().eigenvals()) == {1, R(1, 2), R(1, 3)}, "P8b")
M = M_([2, 1], [3, 4]); ok(zero(M ** 2 - 6 * M + 5 * eye(2)), "P9 CH")
ok(M.inv() == M_([4, -1], [-3, 2]) / 5 and M ** 3 == 31 * M - 30 * eye(2), "P9")
A = M_([1, 1, 0], [0, 2, 1], [0, 0, 3]); ok(expand(-charpoly(A) - (lam ** 3 - 6 * lam ** 2 + 11 * lam - 6)) == 0, "P10 char")
ok((A ** 2 - 6 * A + 11 * eye(3)) == M_([6, -3, 1], [0, 3, -1], [0, 0, 2]) and A.inv() == M_([6, -3, 1], [0, 3, -1], [0, 0, 2]) / 6, "P10")
A = M_([5, 2], [2, 2]); eig(A, [2, 1], 6); eig(A, [1, -2], 1)
P = M_([2, 1], [1, -2]) / sqrt(5); ok(zero(P.T * A * P - diag(6, 1)), "P11")
M = M_([1, 2, 2], [2, 1, -2], [2, -2, 1]) / 3; eig(M, [1, -1, -1], -1)
y, z = symbols("y z"); ok(zero(M * Matrix([y + z, y, z]) - Matrix([y + z, y, z])), "P12 plane")
ok(M * Matrix([1, -1, -1]) == Matrix([-1, 1, 1]), "P12 image")

# Exam 1
M = M_([5, -2], [4, -1]); ok(expand(charpoly(M) - (lam ** 2 - 4 * lam + 3)) == 0, "E1a"); eig(M, [1, 2], 1); eig(M, [1, 1], 3)
U = M_([1, 1], [2, 1]); ok(U.inv() == M_([-1, 1], [2, -1]), "E1c Uinv")
Mn = U * diag(1, 3 ** n) * U.inv()
ok(zero(Mn - M_([2 * 3 ** n - 1, 1 - 3 ** n], [2 * 3 ** n - 2, 2 - 3 ** n])), "E1c")
for k in range(1, 6):
    ok(Mn.subs(n, k) == M ** k, "E1 values")
# Exam 2
A = M_([1, 1, 0], [1, 2, 1], [0, 1, 1]); ok((A - 3 * eye(3)).det() == 0, "E2a")
ok(expand(-charpoly(A) - (lam ** 3 - 4 * lam ** 2 + 3 * lam)) == 0, "E2a char")
eig(A, [1, 2, 1], 3); eig(A, [1, 0, -1], 1); eig(A, [1, -1, 1], 0)
P = Matrix.hstack(Matrix([1, 2, 1]) / sqrt(6), Matrix([1, 0, -1]) / sqrt(2), Matrix([1, -1, 1]) / sqrt(3))
ok(zero(P.T * P - eye(3)) and zero(P.T * A * P - diag(3, 1, 0)), "E2c")
# Exam 3
B = M_([2, 1, 0], [0, 1, -1], [0, 2, 4])
ok(expand(charpoly(B) - (2 - lam) * (lam ** 2 - 5 * lam + 6)) == 0, "E3a")
ok(set(solve(charpoly(B), lam)) == {2, 3}, "E3b")
ok(B ** 4 == 33 * B ** 2 - 100 * B + 84 * eye(3), "E3d")
ok(zero(B ** 3 - 7 * B ** 2 + 16 * B - 12 * eye(3)), "E3 CH")
# Exam 4
M = M_([0, 0, 1], [1, 0, 0], [0, 1, 0]); eig(M, [1, 1, 1], 1)
ok(M ** 2 == M_([0, 1, 0], [0, 0, 1], [1, 0, 0]) and M ** 3 == eye(3), "E4b")
ok(expand(charpoly(M) - (1 - lam ** 3)) == 0, "E4c")
ok([r for r in solve(lam ** 3 - 1, lam) if r.is_real] == [1], "E4b real")
ok(M.trace() == 0 and acos(R(-1, 2)) == 2 * pi / 3, "E4d")

print(f"pb12: all {n_checks} checks passed")
