"""Recomputes every number stated in content/as01.py (Unit AS1) and checks it appears in the unit text."""
import os
import sys
from fractions import Fraction as Fr

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.as01 import UNIT  # noqa: E402


def _text(o):
    if isinstance(o, str):
        return o
    if isinstance(o, dict):
        return " ".join(_text(v) for v in o.values())
    if isinstance(o, (list, tuple)):
        return " ".join(_text(v) for v in o)
    return str(o)


TEXT = _text(UNIT)
COUNT = 0


def num(s, v):
    """Stated decimal string s must equal v rounded to the decimals shown, and must appear in the unit."""
    global COUNT
    d = len(s.split(".")[1]) if "." in s else 0
    assert abs(round(float(v), d) - float(s)) < 1e-9, f"{s} != {v}"
    assert s in TEXT, f"{s} not found in unit text"
    COUNT += 1


def frac(s, v):
    global COUNT
    assert Fr(s) == Fr(v), f"{s} != {v}"
    assert s in TEXT, f"{s} not found in unit text"
    COUNT += 1


def dist(xs, ps):
    xs, ps = [Fr(x) for x in xs], [Fr(p) for p in ps]
    assert sum(ps) == 1
    m = sum(x * p for x, p in zip(xs, ps))
    m2 = sum(x * x * p for x, p in zip(xs, ps))
    return m, m2, m2 - m * m


# Notes table
m, m2, v = dist([0, 1, 2, 3], ["0.3", "0.3", "0.3", "0.1"])
num("1.2", m); num("2.4", m2); num("0.96", v); num("0.980", float(v) ** 0.5)

# Example 1: max of two dice
ps = [Fr(2 * x - 1, 36) for x in range(1, 7)]
m, m2, v = dist(range(1, 7), ps)
frac("161/36", m); num("4.47", m); frac("791/36", m2); frac("2555/1296", v); num("1.97", v)
F = np.cumsum([float(p) for p in ps]); assert F[3] < 0.5 <= F[4]  # median 5

# Example 2
m, m2, v = dist([0, 1, 2, 3], ["0.3", "0.3", "0.3", "0.1"]); assert m == Fr("1.2"); num("0.96", v)

# Example 3: P(X=x)=k/x, x=1,2,3,6
xs = [1, 2, 3, 6]; k = 1 / sum(Fr(1, x) for x in xs); frac("1/2", k)
ps = [k / x for x in xs]
assert sum(x * p for x, p in zip(xs, ps)) == 2
e1 = sum(p / x for x, p in zip(xs, ps)); frac("25/36", e1)
e2 = sum(p / x ** 2 for x, p in zip(xs, ps)); frac("7/12", e2); frac("252/216", e2 * 2)
frac("131/1296", e2 - e1 ** 2); frac("131/36", 36 * (e2 - e1 ** 2)); num("3.64", 36 * (e2 - e1 ** 2))

# Example 4
assert 5 * Fr("1.2") - 2 == 4 and 25 * Fr("0.96") == 24
num("1.92", 2 * 0.96); num("3.84", 4 * 0.96)

# Example 5: uniform 4..9 and even numbers
frac("35/12", Fr(35, 12)); num("2.92", 35 / 12)
assert 2 * 5.5 == 11 and 4 * Fr(99, 12) == 33

# Example 6
m, m2, v = dist([1, 2, 3, 4], [Fr(x, 10) for x in range(1, 5)]); assert (m, v) == (3, 1)
f = np.array([6, 8, 16, 20]); x = np.arange(1, 5)
assert (f * x).sum() / 50 == 3.0; assert (f * x * x).sum() == 502; num("1.04", 502 / 50 - 9)

# Practice
c = Fr(1, 21); assert c * sum(6 - x for x in range(6)) == 1; frac("5/7", c * 15)
m, m2, v = dist([1, 2, 3, 4], ["0.2", "0.4", "0.3", "0.1"]); num("2.3", m); num("6.1", m2); num("0.81", v)
assert (2 * 4 + 5, 4 * 3, 3 + 16) == (13, 12, 19)
k = Fr(1, 14); m, m2, v = dist([1, 2, 3], [k, 4 * k, 9 * k]); frac("18/7", m); num("2.57", m); frac("19/49", v); num("0.388", v)
frac("31/7", m2 - m); num("4.43", m2 - m)
Fv = [0.1, 0.3, 0.45, 0.8, 1]; p = np.diff([0] + Fv); num("0.15", p[2]); num("0.7", Fv[3] - Fv[0]); assert np.argmax(p) == 3
# two d4
s = {}
for a in range(1, 5):
    for b in range(1, 5):
        s[a + b] = s.get(a + b, 0) + Fr(1, 16)
m, m2, v = dist(list(s), list(s.values())); assert m == 5 and m2 == Fr("27.5") and v == Fr("2.5"); assert Fr(15, 12) == Fr("1.25")
num("0.35", 7 / 20); num("10.5", 10.5); num("33.25", 399 / 12); num("5.77", (399 / 12) ** 0.5)
num("8.25", 99 / 12); num("27.5", 5 * 5.5); num("206.25", 25 * 99 / 12)
xs, ps = [1, 2, 4], [Fr("0.5"), Fr("0.3"), Fr("0.2")]
e1 = sum(p / x for x, p in zip(xs, ps)); e2 = sum(p / x ** 2 for x, p in zip(xs, ps))
num("0.7", e1); num("15.7", sum(p * x ** 3 for x, p in zip(xs, ps))); num("0.5875", e2); num("0.0975", e2 - e1 ** 2); num("0.39", 4 * (e2 - e1 ** 2))
assert (2 * 3 - 5 + 1, 4 * 2 + 4, 3 * 2, 9 * 2) == (2, 12, 6, 18)
assert 11 ** 2 - 1 == 120

# Exam 1
k = Fr(1, 18); xs = [1, 2, 3, 4]; ps = [k * (x + 2) for x in xs]
m, m2, v = dist(xs, ps); frac("25/9", m); num("2.78", m); frac("80/9", m2); frac("95/81", v); num("1.17", v)
frac("19/3", 3 * m - 2); num("6.33", 3 * m - 2); frac("95/9", 9 * v); num("10.6", 9 * v)
e = sum(p / x for x, p in zip(xs, ps)); frac("49/108", e); num("0.454", e)
# Exam 2
num("4.5", 4.5); num("49.5", 10 * 4.5 + 4.5); num("833.25", 101 * 8.25); assert (100 ** 2 - 1) / 12 == 833.25
d = np.arange(10); w = (10 * d[:, None] + d[None, :]).ravel(); assert np.isclose(w.var(), 833.25)
# Exam 3
p0 = Fr(2, 5) * Fr(1, 4); p1 = Fr(3, 5) * Fr(2, 4) + Fr(2, 5) * Fr(3, 4); p2 = Fr(3, 5) * Fr(2, 4)
assert (p0, p1, p2) == (Fr("0.1"), Fr("0.6"), Fr("0.3"))
m, m2, v = dist([0, 1, 2], [p0, p1, p2]); num("1.8", m2); num("0.36", v); assert 50 * m == 60 and 50 * v == 18
# Exam 4
ps = [Fr(x, 6) for x in (1, 2, 3)]; m, m2, v = dist([1, 2, 3], ps); frac("7/3", m); frac("5/9", v)
e = 18 * sum(p / Fr(x) ** 3 for x, p in zip([1, 2, 3], ps)); frac("49/12", e); num("4.08", e)
e1 = sum(p / x for x, p in zip([1, 2, 3], ps)); e2 = sum(p / x ** 2 for x, p in zip([1, 2, 3], ps))
frac("11/36", e2); frac("1/18", e2 - e1 ** 2); assert 36 * (e2 - e1 ** 2) == 2
pr = sum(ps[a - 1] * ps[b - 1] for a in (1, 2, 3) for b in (1, 2, 3) if a + b == 4); frac("5/18", pr); num("0.278", pr)

print(f"as01 check: all {COUNT} stated values verified")
