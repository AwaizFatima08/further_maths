"""SymPy checks for Unit A12 (distances and intersections)."""
from sympy import Matrix, Rational as R, acos, deg, sqrt, symbols, solve, simplify, Eq, expand, Abs

V = lambda *c: Matrix(c)  # noqa: E731
lam, mu, t, s, k = symbols("lam mu t s k")


def close(x, y, tol=0.005):
    assert abs(float(x) - y) < tol, (float(x), y)


def pt_line(p, a, b):
    """Return (foot, distance) by the scalar-product method, and check the cross-product formula."""
    l0 = solve((a + lam * b - p).dot(b), lam)[0]
    f = a + l0 * b
    dist = (f - p).norm()
    assert simplify(dist - (p - a).cross(b).norm() / b.norm()) == 0
    return f, dist, l0


def pt_plane(p, n, d):
    t0 = solve(Eq((p + t * n).dot(n), d), t)[0]
    dist = Abs(p.dot(n) - d) / n.norm()
    assert simplify((t0 * n).norm() - dist) == 0
    return p + t0 * n, dist, p + 2 * t0 * n


def skew(a, b, c, d):
    sol = solve([(c + mu * d - a - lam * b).dot(b), (c + mu * d - a - lam * b).dot(d)], [lam, mu], dict=True)[0]
    P, Q = a + sol[lam] * b, c + sol[mu] * d
    cr = b.cross(d)
    dist = Abs((c - a).dot(cr)) / cr.norm()
    assert simplify((Q - P).norm() - dist) == 0
    assert (Q - P).cross(cr) == V(0, 0, 0)
    return P, Q, dist, sol


def meets(a, b, c, d):
    return solve(list(a + lam * b - c - mu * d), [lam, mu], dict=True)


n = 0
# Notes: general point-plane formula
x1, y1, z1, A_, B_, C_, D_ = symbols("x1 y1 z1 A B C D", real=True)
nn = V(A_, B_, C_)
p0 = V(x1, y1, z1)
t0 = solve(Eq((p0 + t * nn).dot(nn), D_), t)[0]
assert simplify((t0 * nn).dot(t0 * nn) - (p0.dot(nn) - D_) ** 2 / nn.dot(nn)) == 0
n += 1

# WE1
F, dist, l0 = pt_line(V(5, 3, 4), V(1, 2, 3), V(2, -1, 2))
assert l0 == 1 and F == V(3, 1, 5) and dist == 3
assert V(4, 1, 1).cross(V(2, -1, 2)) == V(3, -6, -6)
# WE2
N, dist, Pr = pt_plane(V(3, -1, 2), V(2, -1, 2), 2)
assert N == V(1, 0, 0) and dist == 3 and Pr == V(-1, 1, -2)
# WE3
P, Q, dist, sol = skew(V(0, -1, 2), V(1, 1, 0), V(3, -3, 3), V(0, 1, 1))
assert sol == {lam: 1, mu: 1} and P == V(1, 0, 2) and Q == V(3, -2, 4) and dist == 2 * sqrt(3)
assert V(1, 1, 0).cross(V(0, 1, 1)) == V(1, -1, 1)
close(dist, 3.46)
# WE4
n1, n2 = V(1, 1, 1), V(2, -1, 3)
assert n1.cross(n2) == V(4, -1, -3)
L = V(5, 1, 0) + t * V(4, -1, -3)
assert expand(L.dot(n1)) == 6 and expand(L.dot(n2)) == 9
# WE5
assert V(1, 3, -2).cross(V(1, 2, 2)) == V(10, -4, -1)
F, dist, _ = pt_line(V(2, 3, -1), V(1, 0, 1), V(1, 2, 2))
assert dist == sqrt(13)
close(dist, 3.61)
assert Abs(3 * 3 - 4 * 4 + 2) / 5 == 1
# WE6
assert meets(V(1, 0, 3), V(2, 1, -2), V(1, 9, 3), V(2, -2, 1)) == []
P, Q, dist, sol = skew(V(1, 0, 3), V(2, 1, -2), V(1, 9, 3), V(2, -2, 1))
assert V(2, 1, -2).cross(V(2, -2, 1)) == V(-3, -6, -6)
assert sol == {lam: 1, mu: 2} and P == V(3, 1, 1) and Q == V(5, 5, 5) and dist == 6
n += 6

# Practice
assert pt_plane(V(2, -1, 5), V(2, 2, -1), 3)[1] == 2
N, dist, Pr = pt_plane(V(1, 2, 3), V(1, 1, 1), 0)
assert N == V(-1, 0, 1) and dist == 2 * sqrt(3) and Pr == V(-3, -2, -1)
assert Abs(5 * -1 + 12 * 2 - 6) / 13 == 1
F, dist, l0 = pt_line(V(2, 3, 1), V(0, 1, 1), V(1, 1, 1))
assert l0 == R(4, 3) and F == V(R(4, 3), R(7, 3), R(7, 3)) and simplify(dist - 2 * sqrt(6) / 3) == 0
close(dist, 1.63)
assert Abs(R(11, 2) - 1) / 3 == R(3, 2)
P, Q, dist, _ = skew(V(1, 2, 3), V(1, 0, 1), V(0, 1, -1), V(0, 1, 1))
assert V(1, 0, 1).cross(V(0, 1, 1)) == V(-1, -1, 1) and simplify(dist - 2 * sqrt(3) / 3) == 0
P, Q, dist, sol = skew(V(0, 0, 0), V(1, 0, 0), V(0, 1, 2), V(0, 1, 1))
assert sol == {lam: 0, mu: R(-3, 2)} and Q == V(0, R(-1, 2), R(1, 2)) and simplify(dist - sqrt(2) / 2) == 0
assert V(1, -1, 1).cross(V(1, 2, -1)) == V(-1, 2, 3)
L = V(0, 3, 4) + t * V(-1, 2, 3)
assert expand(L.dot(V(1, -1, 1))) == 1 and expand(L.dot(V(1, 2, -1))) == 2
assert V(1, -1, 0).dot(V(1, 1, 3)) == 0
assert pt_plane(V(1, 1, 1), V(1, 1, 3), 2)[1] == 3 / sqrt(11)
close(3 / sqrt(11), 0.905, 0.0005)
assert sorted(solve((2 * k - 4) ** 2 - 81, k)) == [R(-5, 2), R(13, 2)]
assert Abs(2 * k + 1 - 4 - 1).subs(k, R(13, 2)) / 3 == 3
assert V(2, 1, -1).cross(V(2, -2, 1)) == V(-1, -4, -6)
F, dist, _ = pt_line(V(3, 0, -1), V(1, -1, 0), V(2, -2, 1))
assert simplify(dist - sqrt(53) / 3) == 0
close(dist, 2.43)
n += 12

# Section B
# B1
assert meets(V(2, -1, 1), V(1, 2, -1), V(4, -2, -5), V(1, 0, 1)) == []
P, Q, dist, sol = skew(V(2, -1, 1), V(1, 2, -1), V(4, -2, -5), V(1, 0, 1))
assert V(1, 2, -1).cross(V(1, 0, 1)) == V(2, -2, -2)
assert sol == {lam: 1, mu: 2} and P == V(3, 1, 0) and Q == V(6, -2, -3) and dist == 3 * sqrt(3)
close(dist, 5.20)
assert (V(4, -2, -5) - V(2, -1, 1)).dot(V(1, -1, -1)) == 9
# B2
N, dist, Ar = pt_plane(V(3, 4, -2), V(1, 2, -2), -3)
assert dist == 6 and N == V(1, 0, 2) and Ar == V(-1, -4, 6)
s0 = solve(Eq((V(3, 4, -2) + s * V(1, -1, 1)).dot(V(1, 2, -2)), -3), s)
assert s0 == [6]
B = V(3, 4, -2) + 6 * V(1, -1, 1)
assert B == V(9, -2, 4) and Ar - B == V(-10, -2, 2)
# reflected line check: reflection of another point of l lies on it
A2 = V(3, 4, -2) + V(1, -1, 1)
_, _, A2r = pt_plane(A2, V(1, 2, -2), -3)
assert (A2r - B).cross(V(5, 1, -1)) == V(0, 0, 0)
# B3
n1, n2 = V(1, -2, 2), V(2, 1, 1)
assert n1.dot(n2) == 2
close(deg(acos(R(2) / (3 * sqrt(6)))), 74.2, 0.05)
assert n1.cross(n2) == V(-4, 3, 5)
L = V(3, 1, 0) + t * V(-4, 3, 5)
assert expand(L.dot(n1)) == 1 and expand(L.dot(n2)) == 7
assert V(1, 1, -1).cross(V(-4, 3, 5)) == V(8, -1, 7)
F, dist, _ = pt_line(V(4, 2, -1), V(3, 1, 0), V(-4, 3, 5))
assert simplify(dist - sqrt(R(114, 50))) == 0
close(dist, 1.51)
# B4
A, B, C = V(1, 3, -2), V(3, 2, 0), V(6, 3, 2)
F, dist, l0 = pt_line(C, A, B - A)
assert B - A == V(2, -1, 2) and l0 == 2 and F == V(5, 1, 2) and dist == sqrt(5)
assert R(1, 2) * (B - A).norm() * dist == 3 * sqrt(5) / 2
assert (B - A).cross(C - A).norm() / 2 == 3 * sqrt(5) / 2
sols = solve(Eq((A + lam * (B - A) - C).dot(A + lam * (B - A) - C), 9), lam)
assert sorted(sols) == [R(4, 3), R(8, 3)]
assert A + R(8, 3) * (B - A) == V(R(19, 3), R(1, 3), R(10, 3)) and A + R(4, 3) * (B - A) == V(R(11, 3), R(5, 3), R(2, 3))
n += 4
print(f"pa12 checks passed ({n} groups)")
