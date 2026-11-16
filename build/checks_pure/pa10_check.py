"""SymPy checks for Unit A10 (vector product, scalar triple product)."""
from sympy import Matrix, Rational as R, acos, asin, deg, sqrt, symbols, solve, simplify, Eq, Abs, expand

V = lambda *c: Matrix(c)  # noqa: E731
i, j, k = V(1, 0, 0), V(0, 1, 0), V(0, 0, 1)


def close(x, y, tol=0.05):
    assert abs(float(x) - y) < tol, (float(x), y)


def stp(a, b, c):
    t = a.dot(b.cross(c))
    assert t == Matrix.hstack(a, b, c).T.det()
    return t


n = 0
# Notes: basis products and general identities
assert i.cross(j) == k and j.cross(k) == i and k.cross(i) == j and j.cross(i) == -k and i.cross(i) == V(0, 0, 0)
a1, a2, a3, b1, b2, b3, c1, c2, c3 = symbols("a1 a2 a3 b1 b2 b3 c1 c2 c3")
a, b, c = V(a1, a2, a3), V(b1, b2, b3), V(c1, c2, c3)
assert a.cross(b) == V(a2 * b3 - a3 * b2, a3 * b1 - a1 * b3, a1 * b2 - a2 * b1)
assert simplify(a.cross(b) + b.cross(a)) == V(0, 0, 0)
assert simplify(a.cross(b + c) - a.cross(b) - a.cross(c)) == V(0, 0, 0)
assert expand(a.cross(b).dot(a)) == 0 and expand(a.cross(b).dot(b)) == 0
assert expand((a + b).cross(a - b) - 2 * b.cross(a)) == V(0, 0, 0)
assert expand(a.dot(b.cross(c)) - b.dot(c.cross(a))) == 0 and expand(a.dot(b.cross(c)) - c.dot(a.cross(b))) == 0
assert expand(a.dot(b.cross(c)) - Matrix.hstack(a, b, c).T.det()) == 0
# |a x b|^2 = |a|^2|b|^2 - (a.b)^2 (Lagrange) -> |a||b| sin(theta)
assert expand(a.cross(b).dot(a.cross(b)) - (a.dot(a) * b.dot(b) - a.dot(b) ** 2)) == 0
# non-associativity example
assert (i.cross(i)).cross(j) != i.cross(i.cross(j))
n += 1

# WE1
A, B = V(2, -1, 3), V(1, 4, -2)
assert A.cross(B) == V(-10, 7, 9) and B.cross(A) == V(10, -7, -9)
assert A.cross(B).dot(A) == 0 and A.cross(B).dot(B) == 0
# WE2
A, B, C = V(1, 0, 2), V(3, 1, 1), V(0, 2, 4)
cr = (B - A).cross(C - A)
assert cr == V(4, -3, 5) and cr.norm() == 5 * sqrt(2)
close(cr.norm() / 2, 3.54, 0.005)
close(cr.norm() / ((B - A).norm() * (C - A).norm()), 0.962, 0.0005)
assert (B - A).dot(C - A) == -2
close(deg(acos(R(-2) / (3 * sqrt(6)))), 105.8)
close(180 - deg(asin(cr.norm() / ((B - A).norm() * (C - A).norm()))), 105.8)
close(deg(asin(cr.norm() / ((B - A).norm() * (C - A).norm()))), 74.2)
# WE3
P, Q, Rr = V(1, 2, -1), V(2, 0, 1), V(-1, 1, 3)
assert (Q - P).cross(Rr - P) == V(-6, -8, -5)
nn = V(6, 8, 5)
assert all(nn.dot(X) == 17 for X in (P, Q, Rr))
# WE4
a0, bb = V(1, 2, 3), V(2, -1, 1)
assert a0.cross(bb) == V(5, 5, -5)
x, y, z = symbols("x y z")
assert V(x, y, z).cross(bb) == V(y + z, 2 * z - x, -x - 2 * y)
assert V(-5, 5, 0).cross(bb) == V(5, 5, -5) and V(-5, 5, 0) == a0 - 3 * bb
assert (bb / bb.norm()).dot(bb / bb.norm()) == 1
close(deg(acos(2 / sqrt(6))), 35.3)
# WE5
A, B, C, D = V(1, 1, 0), V(3, 2, 1), V(0, 3, 2), V(2, 0, 4)
assert stp(B - A, C - A, D - A) == 25
close(R(25, 6), 4.17, 0.005)
# WE6
kk = symbols("k")
A, B, C, D = V(2, 1, 0), V(4, 3, 1), V(1, 5, 3), V(kk, 2, 1)
cr = (B - A).cross(C - A)
assert cr == V(2, -7, 10) and cr.norm() == 3 * sqrt(17)
close(cr.norm() / 2, 6.18, 0.005)
assert expand((D - A).dot(cr)) == 2 * kk - 1
assert sorted(solve((2 * kk - 1) ** 2 - 81, kk)) == [-4, 5]  # |2k - 1|/6 = 3/2
n += 6

# Practice
assert V(3, 1, -2).cross(V(1, -1, 4)) == V(2, -14, -4)
assert V(1, 2, 0).cross(V(3, 0, -1)) == V(-2, 1, -6)
cr = V(1, 2, 2).cross(V(2, -2, 1))
assert cr == V(6, 3, -6) and cr.norm() == 9
cr = V(2, 0, 1).cross(V(1, 3, -1))
assert cr == V(-3, 3, 6) and cr.norm() == 3 * sqrt(6)
close(cr.norm(), 7.35, 0.005)
P, Q, Rr = V(1, 1, 1), V(2, 3, 0), V(4, 0, 2)
cr = (Q - P).cross(Rr - P)
assert cr == V(1, -4, -7) and cr.norm() == sqrt(66)
close(sqrt(66) / 2, 4.06, 0.005)
A, B, C = V(1, 0, 1), V(2, 1, 3), V(0, 2, 2)
assert (B - A).cross(C - A) == V(-3, -3, 3)
assert all(V(1, 1, -1).dot(X) == 0 for X in (A, B, C))
assert V(2, -1, 0).cross(V(3, 1, -2)) == V(2, 4, 5)
d = V(2, -3, 6)
assert d.norm() == 7
close(deg(acos(R(6, 7))), 31.0)
assert stp(V(1, 2, 0), V(0, 1, 3), V(2, 0, 1)) == 13
assert expand(stp(V(1, 2, 3), V(2, -1, 1), V(kk, 1, 4))) == 5 * kk - 15
assert V(1, 2, 3) + V(2, -1, 1) == V(3, 1, 4)
p, q = symbols("p q")
assert solve(list(V(2, -4, 6).cross(V(-3, p, q))), [p, q], dict=True) == [{p: 6, q: -9}]
n += 12

# Section B
A, B, C, D = V(1, 2, 1), V(3, 3, -1), V(2, 5, 2), V(4, 1, 6)
cr = (B - A).cross(C - A)
assert cr == V(7, -4, 5) and all(cr.dot(X) == 4 for X in (A, B, C))
assert cr.norm() == 3 * sqrt(10)
assert (D - A).dot(cr) == 50
# B2
t = symbols("t")
a0, bb, nn = V(3, -1, 2), V(1, 2, -2), V(2, -1, 1)
close(deg(acos(R(1, 3))), 70.5)
lam = symbols("lam")
assert solve(Eq((a0 + lam * bb).dot(nn), 5), lam) == [2]
P = a0 + 2 * bb
assert P == V(5, 3, -2)
assert bb.cross(nn) == V(0, -5, -5)
dd = V(0, 1, 1)
assert dd.dot(nn) == 0 and dd.dot(bb) == 0 and P.dot(nn) == 5
# B3
a, b, c = V(1, 1, 0), V(0, 1, 1), V(1, 0, t)
assert b.cross(c) == V(t, 1, -1)
assert expand(a.dot(b.cross(c))) == t + 1
assert sorted(solve((t + 1) ** 2 - 36, t)) == [-7, 5]
assert b.cross(c).subs(t, 5).norm() == 3 * sqrt(3)
n += 3
print(f"pa10 checks passed ({n} groups)")
