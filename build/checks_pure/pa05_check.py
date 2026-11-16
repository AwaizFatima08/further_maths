"""SymPy checks for Unit A5 (pure/pa05.py): every product, power and transformation matrix stated."""
from sympy import Matrix, Rational, sqrt, cos, sin, symbols, simplify, eye, zeros, pi, solve, tan, atan

M = lambda *rows: Matrix(rows)
n_checks = 0


def eq(a, b, msg):
    global n_checks
    assert simplify(Matrix(a) - Matrix(b)) == zeros(*Matrix(a).shape), msg
    n_checks += 1


def R2(t):
    return M([cos(t), -sin(t)], [sin(t), cos(t)])


def Ref(t):
    return M([cos(2 * t), sin(2 * t)], [sin(2 * t), -cos(2 * t)])


def Rx(t):
    return M([1, 0, 0], [0, cos(t), -sin(t)], [0, sin(t), cos(t)])


def Ry(t):
    return M([cos(t), 0, sin(t)], [0, 1, 0], [-sin(t), 0, cos(t)])


def Rz(t):
    return M([cos(t), -sin(t), 0], [sin(t), cos(t), 0], [0, 0, 1])


# Notes 5.2 / 5.3
A = M([3, -2], [1, 4]); B = M([0, 5], [-1, 2])
eq(A + B, M([3, 3], [0, 6]), "A+B"); eq(2 * A - B, M([6, -9], [3, 6]), "2A-B")
A1 = M([1, 2], [0, 1]); B1 = M([1, 0], [3, 1])
eq(A1 * B1, M([7, 2], [3, 1]), "AB notes"); eq(B1 * A1, M([1, 2], [3, 7]), "BA notes")
# Table of standard matrices: check against definitions via images of i, j
i, j = Matrix([1, 0]), Matrix([0, 1])
eq(Ref(0), M([1, 0], [0, -1]), "refl x-axis"); eq(Ref(pi / 2), M([-1, 0], [0, 1]), "refl y-axis")
eq(Ref(pi / 4), M([0, 1], [1, 0]), "refl y=x"); eq(Ref(-pi / 4), M([0, -1], [-1, 0]), "refl y=-x")
# reflection formula: fixes direction (cos t, sin t), negates normal
t = symbols("t", real=True)
eq(Ref(t) * Matrix([cos(t), sin(t)]), Matrix([cos(t), sin(t)]), "refl fixes line")
eq(Ref(t) * Matrix([-sin(t), cos(t)]), -Matrix([-sin(t), cos(t)]), "refl negates normal")
eq(M([1, 3], [0, 1]) * j, Matrix([3, 1]), "shear image of j")
# 5.6 composite rules
a, b = symbols("a b", real=True)
eq(R2(a) * R2(b), R2(a + b), "R(a)R(b)")
eq(Ref(a) * Ref(b), R2(2 * (a - b)), "two reflections")
# 5.7 3-D rotation sense: Ry(90) takes k to i
eq(Ry(pi / 2) * Matrix([0, 0, 1]), Matrix([1, 0, 0]), "Ry k->i")
eq(Rx(pi / 2) * Matrix([0, 1, 0]), Matrix([0, 0, 1]), "Rx j->k")
eq(Rz(pi / 2) * Matrix([1, 0, 0]), Matrix([0, 1, 0]), "Rz i->j")

# Worked example 1
A = M([2, -1], [3, 0]); B = M([1, 4], [-2, 1]); C = M([1, 0, 2], [-1, 3, 1]); D = M([2, 1], [0, -1], [1, 3])
eq(A * B, M([4, 7], [3, 12]), "WE1 AB"); eq(B * A, M([14, -1], [-1, 2]), "WE1 BA")
eq(C * D, M([4, 7], [-1, -1]), "WE1 CD"); assert (D * C).shape == (3, 3) and (A * C).shape == (2, 3)
# Worked example 2
S = M([Rational(1, 2), -sqrt(3) / 2], [sqrt(3) / 2, Rational(1, 2)])
eq(S, R2(pi / 3), "WE2 S rot 60"); eq(M([1, 2], [0, 1]) * Matrix([0, 1]), Matrix([2, 1]), "WE2 shear")
# Worked example 3
Mr = M([0, 1], [1, 0]); Rr = M([0, -1], [1, 0])
eq(Rr * Mr, M([-1, 0], [0, 1]), "WE3 RM"); eq(Mr * Rr, M([1, 0], [0, -1]), "WE3 MR")
# Worked example 4
eq(S ** 2, M([-Rational(1, 2), -sqrt(3) / 2], [sqrt(3) / 2, -Rational(1, 2)]), "WE4 S2")
eq(S ** 3, -eye(2), "WE4 S3"); eq(S ** 6, eye(2), "WE4 S6")
assert all(simplify(S ** k - eye(2)) != zeros(2, 2) for k in range(1, 6))
eq(S ** 100, M([-Rational(1, 2), sqrt(3) / 2], [-sqrt(3) / 2, -Rational(1, 2)]), "WE4 S100")
# Worked example 5
A3 = M([1, 0, 0], [0, -1, 0], [0, 0, 1]); B3 = Rz(pi / 2)
eq(B3, M([0, -1, 0], [1, 0, 0], [0, 0, 1]), "WE5 B"); C3 = B3 * A3
eq(C3, M([0, 1, 0], [1, 0, 0], [0, 0, 1]), "WE5 C"); eq(C3 * Matrix([1, 2, 3]), Matrix([2, 1, 3]), "WE5 image")
eq(C3 * Matrix([1, 1, 5]), Matrix([1, 1, 5]), "WE5 plane y=x fixed")

# Practice
A = M([3, -2], [1, 4]); B = M([0, 5], [-1, 2])
eq(A + 2 * B, M([3, 8], [-1, 8]), "P1a"); eq(3 * A - B, M([9, -11], [4, 10]), "P1b"); eq(A * B, M([2, 11], [-4, 13]), "P1c")
P = M([1, 2, 0], [-1, 0, 3]); Q = Matrix([2, -1, 4]); eq(P * Q, Matrix([0, 10]), "P2")
A, B = A1, B1
eq((A + B) ** 2, M([10, 8], [12, 10]), "P3 lhs"); eq(A ** 2 + 2 * A * B + B ** 2, M([16, 8], [12, 4]), "P3 rhs")
eq(A ** 2, M([1, 4], [0, 1]), "P3 A2"); eq(2 * A * B, M([14, 4], [6, 2]), "P3 2AB"); eq(B ** 2, M([1, 0], [6, 1]), "P3 B2")
Mm = M([1, 1], [0, 1])
for k in range(1, 8):
    eq(Mm ** k, M([1, k], [0, 1]), "P4")
eq(Ref(-pi / 4), M([0, -1], [-1, 0]), "P5a"); eq(R2(-pi / 2), M([0, 1], [-1, 0]), "P5b")
eq(R2(pi), M([-1, 0], [0, -1]), "P6a"); eq(R2(-pi / 4), M([1 / sqrt(2), 1 / sqrt(2)], [-1 / sqrt(2), 1 / sqrt(2)]), "P6d")
eq(M([1, 0], [-2, 1]) * Matrix([1, 0]), Matrix([1, -2]), "P6c")
T = M([2, -1], [1, 3]); eq(T * Matrix([4, -2]), Matrix([10, -2]), "P7b")
eq(T * Matrix([1, 1]), Matrix([1, 4]), "P7c")
Rf = Ref(pi / 6); eq(Rf, M([Rational(1, 2), sqrt(3) / 2], [sqrt(3) / 2, -Rational(1, 2)]), "P8")
assert simplify(tan(pi / 6) - 1 / sqrt(3)) == 0
eq(Rf * Matrix([2, 0]), Matrix([1, sqrt(3)]), "P8 image")
Pp = M([2, 0], [0, 1]); Qq = R2(pi / 2)
eq(Qq * Pp, M([0, -1], [2, 0]), "P9a"); eq(Pp * Qq, M([0, -2], [1, 0]), "P9b")
eq(Qq * Pp * Matrix([1, 1]), Matrix([-1, 2]), "P9c1"); eq(Pp * Qq * Matrix([1, 1]), Matrix([-2, 1]), "P9c2")
Rr = Rx(pi / 2); eq(Rr, M([1, 0, 0], [0, 0, -1], [0, 1, 0]), "P10 R"); eq(Rr * Matrix([2, -1, 5]), Matrix([2, -5, -1]), "P10 img")
X = M([-1, 0, 0], [0, 1, 0], [0, 0, 1]); eq(X * Rr, M([-1, 0, 0], [0, 0, -1], [0, 1, 0]), "P10 comp")
aa, bb = symbols("a b", positive=True)
Aab = M([aa, 2], [1, bb])
sol = solve(list(Aab ** 2 - M([11, 10], [5, 6])), [aa, bb], dict=True)
assert sol == [{aa: 3, bb: 2}], sol; n_checks += 1
eq(Ref(a) * Ref(b), R2(2 * (a - b)), "P12")

# Exam 1
k = symbols("k")
Mk = M([k, 2], [3, -1]); eq(Mk ** 2, M([k ** 2 + 6, 2 * k - 2], [3 * k - 3, 7]), "E1a")
M1 = Mk.subs(k, 1); eq(M1 ** 2, 7 * eye(2), "E1b"); eq(M1 ** 5, M([49, 98], [147, -49]), "E1c")
assert solve([2 * k - 2, 3 * k - 3], k) == {k: 1}
# Exam 2
A = Ref(-pi / 4); B = 3 * eye(2); C = B * A; eq(C, M([0, -3], [-3, 0]), "E2b")
for p, im in [((1, 0), (0, -3)), ((3, 0), (0, -9)), ((1, 2), (-6, -3))]:
    eq(C * Matrix(p), Matrix(im), "E2c")
assert abs(C.det()) == 9; n_checks += 1
# Exam 3
P = M([0, 0, 1], [0, 1, 0], [-1, 0, 0]); eq(P, Ry(pi / 2), "E3a")
Q = M([1, 0, 0], [0, 1, 0], [0, 0, -1]); R = Q * P
eq(R, M([0, 0, 1], [0, 1, 0], [1, 0, 0]), "E3c"); eq(R * Matrix([2, -3, 1]), Matrix([1, -3, 2]), "E3d"); eq(R ** 2, eye(3), "E3e")
eq(R * Matrix([1, 4, 1]), Matrix([1, 4, 1]), "E3e plane x=z fixed")
# Exam 4
S = M([1, 2], [0, 1]); R = M([0, -1], [1, 0])
eq(S ** 2, M([1, 4], [0, 1]), "E4b"); eq(S ** 3, M([1, 6], [0, 1]), "E4b")
for n in range(1, 8):
    eq(S ** n, M([1, 2 * n], [0, 1]), "E4 Sn")
eq(R * S, M([0, -1], [1, 2]), "E4c RS"); eq(S * R, M([2, -1], [1, 0]), "E4c SR")
eq((R * S).inv() * Matrix([-3, 5]), Matrix([-1, 3]), "E4d")

print(f"pa05: all {n_checks} checks passed")
