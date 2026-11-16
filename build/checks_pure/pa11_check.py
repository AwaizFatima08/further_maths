"""SymPy checks for Unit A11 (pure/pa11.py): every system's solution, inconsistency, and plane arrangement."""
from sympy import Matrix, Rational, symbols, simplify, expand, factor, eye, zeros, solve, linsolve, S, nsimplify

M = lambda *rows: Matrix(rows)
R = Rational
x, y, z, t, k, a, b, c = symbols("x y z t k a b c")
X = Matrix([x, y, z])
n_checks = 0


def ok(cond, msg):
    global n_checks
    assert cond, msg
    n_checks += 1


def parallel(u, v):
    return Matrix(u).cross(Matrix(v)) == zeros(3, 1)


def classify(A, bvec):
    """Classify three planes A x = b: 'point', 'sheaf', 'prism', 'two parallel + cut', 'three parallel',
    'two coincident + cut', 'coincident'."""
    A, bvec = Matrix(A), Matrix(bvec)
    if A.det() != 0:
        return "point"
    aug = A.row_join(bvec)
    rA, rAug = A.rank(), aug.rank()
    rows = [A.row(i) for i in range(3)]
    par = [(i, j) for i in range(3) for j in range(i + 1, 3) if parallel(rows[i].T, rows[j].T)]
    coinc = [(i, j) for (i, j) in par if Matrix.vstack(aug.row(i), aug.row(j)).rank() == 1]
    if rAug == rA:  # consistent
        if rA == 1:
            return "coincident"
        return "two coincident + cut" if coinc else "sheaf"
    if not par:
        return "prism"
    if len(par) == 3:
        return "three parallel"
    return "two parallel + cut"


# 11.1
A = M([2, -1, 3], [1, 0, 4], [0, 3, -1]); ok(list(A * X - Matrix([7, 1, 0])) == [2 * x - y + 3 * z - 7, x + 4 * z - 1, 3 * y - z], "11.1")
# figure configurations (pa11_figs uses these systems)
ok(classify(M([1, 0, 0], [0, 1, 0], [0, 0, 1]), [1, 1, 1]) == "point", "fig a")
# WE1
A = M([1, 2, -1], [2, -1, 1], [3, 1, 2]); bb = Matrix([3, 4, 9])
ok(A.det() == -10, "WE1 det"); ok(A.inv() == M([3, 5, -1], [1, -5, 3], [-5, -5, 5]) / 10, "WE1 inv")
ok(A.inv() * bb == Matrix([2, 1, 1]), "WE1 sol"); ok(A * Matrix([2, 1, 1]) == bb, "WE1 check")
# WE2
A = M([1, 1, 1], [1, -1, 2], [3, 1, 4]); ok(A.det() == 0, "WE2a")
ok(2 * A.row(0) + A.row(1) == A.row(2) and 2 * 6 + 5 == 17, "WE2b combination")
ok(classify(A, [6, 5, 17]) == "sheaf" and classify(A, [6, 5, 20]) == "prism", "WE2 classify")
sol = linsolve((A, Matrix([6, 5, 17])), [x, y, z]); (sx, sy, sz), = sol
zz = sz
ok(simplify(sx.subs(zz, t) - (11 - 3 * t) / 2) == 0 and simplify(sy.subs(zz, t) - (1 + t) / 2) == 0, "WE2 param")
line = Matrix([4, 1, 1]) + t * Matrix([3, -1, -2]); ok(expand(A * line - Matrix([6, 5, 17])) == zeros(3, 1), "WE2 line")
ok(Matrix([1, 1, 1]).cross(Matrix([1, -1, 2])) == Matrix([3, -1, -2]), "WE2 cross")
ok(linsolve((A, Matrix([6, 5, 20])), [x, y, z]) == S.EmptySet, "WE2c")
# WE3
A = M([1, 2, -1], [2, 4, -2], [1, -1, 1]); ok(classify(A, [4, 3, 2]) == "two parallel + cut", "WE3")
ok(linsolve((A, Matrix([4, 3, 2])), [x, y, z]) == S.EmptySet and A.det() == 0, "WE3 none")
# WE4
A = M([k, 1, 1], [1, k, 1], [1, 1, k]); bb = Matrix([1, 1, -2])
ok(factor(A.det()) == (k - 1) ** 2 * (k + 2) and expand(A.det() - (k ** 3 - 3 * k + 2)) == 0, "WE4a")
solk = simplify(A.inv() * bb); ok(simplify(solk - Matrix([1, 1, -2]) / (k - 1)) == zeros(3, 1), "WE4b")
ok(classify(A.subs(k, 1), bb) == "three parallel", "WE4c k=1 (two coincident, third parallel)")
ok(A.subs(k, 1).row(0) == A.subs(k, 1).row(1), "WE4c coincident pair")
ok(classify(A.subs(k, -2), bb) == "sheaf", "WE4c k=-2")
line = Matrix([0, 0, 1]) + t * Matrix([1, 1, 1]); ok(expand(A.subs(k, -2) * line - bb) == zeros(3, 1), "WE4 line")
# WE5
A = M([2, 1, 3], [1, 2, 1], [3, 1, 2]); bb = Matrix([R(1410, 100), R(1120, 100), R(1310, 100)])
ok(A.det() == -8 and A.inv() * bb == Matrix([R(3, 2), R(18, 5), R(5, 2)]), "WE5")

# Practice
A = M([1, 2, 0], [0, 1, -1], [3, 0, 1]); ok(list(A * X) == [x + 2 * y, y - z, 3 * x + z], "P1b")
A = M([1, 1, 1], [2, -1, 3], [1, 2, -1]); ok(A.det() == 5 and A.inv() * Matrix([6, 9, 2]) == Matrix([1, 2, 3]), "P2")
A = M([1, 2, 3], [0, 1, 4], [5, 6, 0]); ok(A.inv() == M([-24, 18, 5], [20, -15, -4], [-5, 4, 1]), "P3 inv")
ok(A.inv() * Matrix([1, 2, 3]) == Matrix([27, -22, 6]), "P3")
A = M([2, 1, -1], [1, -1, 2], [3, 2, 1]); ok(A.det() == -10 and A.inv() * Matrix([3, 5, 10]) == Matrix([2, 1, 2]), "P4")
ok(classify(M([1, 2, -1], [2, 4, -2], [1, -1, 1]), [1, 5, 0]) == "two parallel + cut", "P5a")
ok(classify(M([1, 1, 1], [2, 2, 2], [3, 3, 3]), [1, 3, 5]) == "three parallel", "P5b")
A = M([1, 2, -1], [2, -1, 1], [4, 3, -1]); ok(2 * A.row(0) + A.row(1) == A.row(2), "P6 rows")
ok(classify(A, [1, 3, 5]) == "sheaf", "P6")
line = Matrix([0, 4, 7]) + t * Matrix([1, -3, -5]); ok(expand(A * line - Matrix([1, 3, 5])) == zeros(3, 1), "P6 line")
ok(Matrix([1, 2, -1]).cross(Matrix([2, -1, 1])) == Matrix([1, -3, -5]), "P6 cross")
ok(classify(A, [1, 3, 6]) == "prism", "P7")
A = M([1, 1, 1], [1, 2, 3], [2, 3, k]); ok(expand(A.det() - (k - 4)) == 0, "P8a")
ok(classify(A.subs(k, 4), [2, 5, 7]) == "sheaf", "P8b")
A = M([1, -1, 2], [3, 1, -1], [5, -1, 3]); ok(2 * A.row(0) + A.row(1) == A.row(2) and A.det() == 0, "P9")
ok(classify(A, [1, 4, 6]) == "sheaf" and classify(A, [1, 4, 5]) == "prism", "P9 c=6")
A = M([1, 1, 0], [0, 1, 1], [1, 0, 1]); ok(A.det() == 2, "P10 det")
ok(simplify(A.inv() * Matrix([a, 1, 2]) - Matrix([(a + 1) / 2, (a - 1) / 2, (3 - a) / 2])) == zeros(3, 1), "P10")
A = M([1, 1, -1], [2, -1, 1], [1, -2, 2]); ok(A.det() == 0 and A.row(1) - A.row(0) == A.row(2), "P11")
ok(classify(A, [2, 1, -1]) == "sheaf" and classify(A, [2, 1, 3]) == "prism", "P11 classify")
A = M([1, 1, 1], [1, 2, 0], [0, 1, 3]); ok(A.det() == 4 and A.inv() * Matrix([20, 19, 31]) == Matrix([5, 7, 8]), "P12")

# Exam 1
A = M([1, 2, -1], [2, -1, 3], [3, 1, k]); ok(expand(A.det() - (10 - 5 * k)) == 0, "E1a")
A3 = A.subs(k, 3); ok(A3.det() == -5 and A3.inv() * Matrix([1, 7, 10]) == Matrix([1, 1, 2]), "E1b")
A2 = A.subs(k, 2); ok(A2.row(0) + A2.row(1) == A2.row(2), "E1c rows")
ok(classify(A2, [1, 7, 8]) == "sheaf" and classify(A2, [1, 7, 9]) == "prism", "E1c")
line = Matrix([3, -1, 0]) + t * Matrix([-1, 1, 1]); ok(expand(A2 * line - Matrix([1, 7, 8])) == zeros(3, 1), "E1d")
ok(Matrix([1, 2, -1]).cross(Matrix([2, -1, 3])) == Matrix([5, -5, -5]), "E1d cross")
# Exam 2
A = M([3, -1, 2], [1, 1, -1], [5, 1, a]); ok(expand(A.det() - 4 * a) == 0, "E2a")
A0 = A.subs(a, 0); ok(A0.row(0) + 2 * A0.row(1) == A0.row(2), "E2b rows")
ok(classify(A0, [4, 2, 8]) == "sheaf" and classify(A0, [4, 2, 9]) == "prism", "E2bc")
ok(A.subs(a, 2).inv() * Matrix([4, 2, 12]) == Matrix([1, 3, 2]), "E2d")
# Exam 3
ok(classify(M([1, 1, 1], [2, 2, 2], [1, -1, 0]), [3, 5, 0]) == "two parallel + cut", "E3a")
A = M([1, -1, 1], [2, 1, -1], [1, 2, -2]); ok(A.row(1) - A.row(0) == A.row(2) and classify(A, [1, 2, 3]) == "prism", "E3b")
A = M([1, 1, 1], [1, -1, 1], [3, 1, 3]); ok(2 * A.row(0) + A.row(1) == A.row(2) and classify(A, [1, 1, 3]) == "sheaf", "E3c")
# Exam 4
A = M([1, 1, 1], [1, -1, 2], [2, 1, -1]); ok(A.det() == 7, "E4 det")
ok(A.cofactor_matrix() == M([-1, 5, 3], [2, -3, 1], [3, -1, -2]), "E4 cof")
ok(A.inv() == M([-1, 2, 3], [5, -3, -1], [3, 1, -2]) / 7, "E4 inv"); ok(A.inv() * Matrix([6, 5, 1]) == Matrix([1, 2, 3]), "E4b")

print(f"pa11: all {n_checks} checks passed")
