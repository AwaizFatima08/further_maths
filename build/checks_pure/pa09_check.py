"""SymPy checks for Unit A9 (lines and planes). Run with the project venv; prints a final pass line."""
from sympy import Matrix, Rational as R, acos, asin, deg, sqrt, symbols, solve, simplify, Eq

V = lambda *c: Matrix(c)  # noqa: E731


def ang(x):
    return float(deg(x))


def acute_lines(b, d):
    return ang(acos(abs(b.dot(d)) / (b.norm() * d.norm())))


def line_plane(b, n):
    return ang(asin(abs(b.dot(n)) / (b.norm() * n.norm())))


def close(x, y, tol=0.05):
    assert abs(x - y) < tol, (x, y)


def intersect(a, b, c, d):
    lam, mu = symbols("lam mu")
    sol = solve(list(a + lam * b - c - mu * d), [lam, mu], dict=True)
    return sol[0] if sol else None


lam, mu, t, s = symbols("lam mu t s")
n = 0

# Notes: (x-1)/2 = (y+3)/(-1) = (4-z)/3 -> point (1,-3,4), direction (2,-1,-3)
for k in range(-2, 3):
    x, y, z = 1 + 2 * k, -3 - k, 4 - 3 * k
    assert R(x - 1, 2) == R(y + 3, -1) == R(4 - z, 3)
n += 1

# WE1
A, B = V(2, -1, 3), V(5, 1, -1)
assert B - A == V(3, 2, -4)
assert A + 3 * (B - A) == V(11, 5, -9)
n += 1
# WE2
b, d = V(2, -1, 2), V(1, 4, -1)
assert b.dot(d) == -4 and b.norm() == 3 and d.norm() == 3 * sqrt(2)
close(ang(acos(R(-4) / (9 * sqrt(2)))), 108.3)
close(acute_lines(b, d), 71.7)
n += 1
# WE3
sol = intersect(V(1, 2, -1), V(1, -1, 2), V(2, 5, 0), V(1, -5, 3))
assert sol == {lam: 2, mu: 1}
assert V(1, 2, -1) + 2 * V(1, -1, 2) == V(3, 0, 3)
n += 1
# WE4
A, B, C = V(1, 0, 2), V(3, 1, 1), V(0, 2, 4)
nn = V(4, -3, 5)
assert nn.dot(B - A) == 0 and nn.dot(C - A) == 0
assert all(nn.dot(P) == 14 for P in (A, B, C))
n += 1
# WE5
n1, n2 = V(2, -1, 2), V(1, 1, -1)
assert n1.dot(n2) == -1
close(acute_lines(n1, n2), 78.9)
bl = V(1, 1, 4)
assert bl.dot(n1) == 9
assert simplify(asin(R(9) / (3 * 3 * sqrt(2))) - asin(1 / sqrt(2))) == 0
close(line_plane(bl, n1), 45.0, 1e-9)
n += 1
# WE6
tt = solve(Eq(n1.dot(V(1, 2, 0) + t * bl), 9), t)
assert tt == [1] and V(1, 2, 0) + bl == V(2, 3, 4)
m_pt, m_dir, pn = V(1, -1, 2), V(2, 1, -1), V(1, -1, 1)
assert m_dir.dot(pn) == 0 and m_pt.dot(pn) == 4
assert simplify((m_pt + s * m_dir).dot(pn) - 4) == 0
n += 1

# Practice
# 2
A, B = V(1, 2, -2), V(4, 6, 10)
assert (B - A).norm() == 13 and (B - A) / 13 == V(R(3, 13), R(4, 13), R(12, 13))
assert (2 * A + B) / 3 == V(2, R(10, 3), 2)
# 3
close(ang(acos(R(11, 15))), 42.8)
assert V(1, 2, 2).dot(V(3, 0, 4)) == 11
# 4
p = symbols("p")
assert solve(V(p, 2, -1).dot(V(3, p, 4)), p) == [R(4, 5)]
# 5 2-D
assert all((1 + 2 * k) + 2 * (3 - k) == 7 for k in range(-3, 4))
# 6 skew
assert intersect(V(1, 0, 1), V(1, 1, 0), V(0, 2, 0), V(0, 1, 1)) is None
# 7
sol = solve(list(V(1, 2, 3) + lam * V(1, 0, -1) - V(2, p, 1) - mu * V(0, 1, 1)), [lam, mu, p], dict=True)
assert sol == [{lam: 1, mu: 1, p: 1}]
assert V(1, 2, 3) + V(1, 0, -1) == V(2, 2, 2)
# 8
nn = V(2, -1, -1)
assert nn.dot(V(1, 0, 2)) == 0 and nn.dot(V(0, 1, -1)) == 0 and nn.dot(V(1, 1, 0)) == 1
# 9
assert V(2, -1, 4).dot(V(3, 1, -2)) == -3
# 10
assert V(1, 2, -2).dot(V(2, -1, 2)) == -4
close(acute_lines(V(1, 2, -2), V(2, -1, 2)), 63.6)
# 11
close(line_plane(V(2, -1, 2), V(1, 1, 1)), 35.3)
# 12
pt = V(1, -1, 2) + t * V(2, 1, -1)
assert simplify(pt.dot(V(1, -1, 1)) - 4) == 0
n += 12

# Section B
# B1
A, B = V(2, 1, -1), V(4, 0, 1)
d1, d2 = B - A, V(0, 1, 1)
assert d1 == V(2, -1, 2)
assert intersect(A, d1, V(6, -3, 1), d2) == {lam: 2, mu: 2}
assert A + 2 * d1 == V(6, -1, 3)
close(acute_lines(d1, d2), 76.4)
nn = V(3, 2, -2)
assert nn.dot(d1) == 0 and nn.dot(d2) == 0 and nn.dot(A) == 10 and nn.dot(V(6, -1, 3)) == 10 and nn.dot(V(6, -3, 1)) == 10
# B2
nn = V(1, -2, -2)
assert nn.dot(V(2, 1, 0)) == 0 and nn.dot(V(0, 1, -1)) == 0 and nn.dot(V(1, 0, 2)) == -3
ln = V(5, -1, 4) + t * V(1, 2, -2)
assert solve(Eq(ln.dot(nn), -3), t) == [-2]
assert ln.subs(t, -2) == V(3, -5, 8)
assert V(1, 2, -2).dot(nn) == 1
close(line_plane(V(1, 2, -2), nn), 6.4)
# B3
n1, n2 = V(1, 2, -1), V(2, -1, 1)
assert n1.dot(n2) == -1
close(acute_lines(n1, n2), 80.4)
l = V(1, 4, 5) + t * V(1, -3, -5)
assert simplify(l.dot(n1) - 4) == 0 and simplify(l.dot(n2) - 3) == 0
m = V(2, 1, 3) + s * n1
assert solve(Eq(m.dot(n1), 4), s) == [R(1, 2)]
assert m.subs(s, R(1, 2)) == V(R(5, 2), 2, R(5, 2))
n += 3

print(f"pa09 checks passed ({n} groups)")
