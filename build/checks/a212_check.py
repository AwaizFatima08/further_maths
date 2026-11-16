"""Checks every number in content/a212.py (sign test). Run with the scipy venv python."""
import math
from fractions import Fraction

import numpy as np
from scipy.stats import binom, norm


def r4(x):
    return round(float(x), 4)


def up(x, n, p=0.5):
    """P(X >= x) for X ~ B(n, p)."""
    return binom.sf(x - 1, n, p)


def lo(x, n, p=0.5):
    return binom.cdf(x, n, p)


def signs(values, m0):
    d = [round(v - m0, 9) for v in values]
    return sum(x > 0 for x in d), sum(x < 0 for x in d), sum(x == 0 for x in d)


def crit_upper(n, alpha):
    """Smallest c with P(X >= c) <= alpha."""
    c = next(c for c in range(n + 1) if up(c, n) <= alpha)
    return c, up(c, n)


def crit_lower(n, alpha):
    c = max(c for c in range(n + 1) if lo(c, n) <= alpha)
    return c, lo(c, n)


# ---- Notes: power table (n = 20, sign test CR X >= 15, z-test of same size)
assert crit_upper(20, 0.05) == (15, up(15, 20))
size = up(15, 20)
assert r4(size) == 0.0207
za = norm.isf(size)
table = {0.25: (0.5987, 0.1232, 0.1784), 0.5: (0.6915, 0.3841, 0.5779),
         0.75: (0.7734, 0.7094, 0.9057), 1.0: (0.8413, 0.9158, 0.9925)}
for dl, (pp, ps, pz) in table.items():
    p = norm.cdf(dl)
    assert r4(p) == pp, dl
    assert r4(up(15, 20, p)) == ps, dl
    assert r4(norm.sf(za - dl * math.sqrt(20))) == pz, dl
assert round(2 / math.pi, 2) == 0.64 and round(3 / math.pi, 2) == 0.95

# ---- Worked example 1
times = [27, 31, 24, 29, 25, 33, 28, 26, 30, 22, 35, 27]
assert signs(times, 25) == (9, 2, 1)
assert Fraction(1 + 11 + 55, 2048) == Fraction(int(round(lo(2, 11) * 2048)), 2048)
assert r4(up(9, 11)) == 0.0327 and up(9, 11) * 2048 == 67

# ---- Worked example 2
assert r4(lo(3, 16)) == 0.0106 and r4(lo(4, 16)) == 0.0384
assert crit_lower(16, 0.025)[0] == 3 and crit_upper(16, 0.025)[0] == 13
assert r4(2 * lo(3, 16)) == 0.0213

# ---- Worked example 3
before = [312, 285, 298, 330, 276, 301, 290, 315, 288, 305]
after = [296, 280, 301, 318, 276, 289, 284, 309, 292, 291]
d = [b - a for b, a in zip(before, after)]
assert d == [16, 5, -3, 12, 0, 12, 6, 6, -4, 14]
assert signs(d, 0) == (7, 2, 1)
assert up(7, 9) * 512 == 46 and r4(up(7, 9)) == 0.0898
assert up(7, 9) < 0.10

# ---- Worked example 4
n = 60 - 5
assert n == 55
z = (37.5 - 27.5) / math.sqrt(13.75)
assert round(z, 3) == 2.697 and r4(norm.sf(z)) == 0.0035 and z > 2.3263
assert r4(up(38, 55)) == 0.0032

# ---- Worked example 5
assert r4(up(15, 20)) == 0.0207 and r4(up(14, 20)) == 0.0577
assert r4(lo(14, 20, 0.7)) == 0.5836 and r4(1 - lo(14, 20, 0.7)) == 0.4164

# ---- Practice
q2 = [42, 38, 45, 40, 47, 51, 39, 44, 40, 49]
assert signs(q2, 40) == (6, 2, 2)
assert up(6, 8) * 256 == 37 and r4(up(6, 8)) == 0.1445
assert crit_lower(14, 0.05) == (3, lo(3, 14)) and r4(lo(3, 14)) == 0.0287 and r4(lo(4, 14)) == 0.0898
assert crit_lower(18, 0.05)[0] == 5 and r4(lo(5, 18)) == 0.0481 and r4(lo(6, 18)) == 0.1189
assert crit_upper(18, 0.05)[0] == 13 and r4(2 * lo(5, 18)) == 0.0963
t1 = [54, 61, 48, 70, 66, 59, 72, 50]
t2 = [60, 65, 47, 78, 69, 64, 75, 58]
d5 = [b - a for a, b in zip(t1, t2)]
assert d5 == [6, 4, -1, 8, 3, 5, 3, 8] and signs(d5, 0) == (7, 1, 0)
assert up(7, 8) * 256 == 9 and r4(up(7, 8)) == 0.0352
z6 = (32.5 - 25) / math.sqrt(12.5)
assert round(z6, 3) == 2.121 and r4(norm.sf(z6)) == 0.0169 and r4(up(33, 50)) == 0.0164
assert r4(lo(7, 25)) == 0.0216
q9 = [3.1, 1.4, 2.6, 4.0, 2.0, 2.9, 1.8, 3.5, 2.7, 3.3]
assert [round(x - 2, 1) for x in q9] == [1.1, -0.6, 0.6, 2.0, 0.0, 0.9, -0.2, 1.5, 0.7, 1.3]
assert signs(q9, 2) == (7, 2, 1) and r4(up(7, 9)) == 0.0898
assert r4(up(14, 18)) == 0.0154 and r4(lo(4, 18)) == 0.0154
assert crit_upper(10, 0.05) == (9, up(9, 10)) and up(9, 10) * 1024 == 11
assert r4(up(9, 10)) == 0.0107 and r4(up(8, 10)) == 0.0547 and r4(up(9, 10, 0.8)) == 0.3758

# ---- Section B
prices = [185, 240, 172, 410, 198, 225, 168, 205, 950, 192, 215, 162]
assert signs(prices, 175) == (9, 3, 0)
assert up(9, 12) * 4096 == 299 and r4(up(9, 12)) == 0.0730 and r4(up(8, 12)) == 0.1938
assert crit_upper(12, 0.10)[0] == 9
zb2 = (28.5 - 21) / math.sqrt(10.5)
assert 45 - 3 == 42 and round(zb2, 3) == 2.315 and r4(norm.sf(zb2)) == 0.0103 and r4(up(29, 42)) == 0.0098
assert crit_upper(15, 0.05) == (12, up(12, 15)) and r4(up(12, 15)) == 0.0176 and r4(up(11, 15)) == 0.0592
assert r4(lo(11, 15, 0.75)) == 0.5387
ja = [7.2, 6.8, 8.1, 5.9, 7.5, 6.4, 8.3, 7.0, 6.6, 7.8, 5.5, 7.1]
jb = [6.9, 6.1, 7.6, 6.2, 7.0, 6.4, 7.7, 6.5, 6.3, 7.9, 5.0, 6.6]
d4 = [round(a - b, 1) for a, b in zip(ja, jb)]
assert d4 == [0.3, 0.7, 0.5, -0.3, 0.5, 0.0, 0.6, 0.5, 0.3, -0.1, 0.5, 0.5]
assert signs(d4, 0) == (9, 2, 1)
assert up(9, 11) * 2048 == 67 and r4(up(9, 11)) == 0.0327 and r4(2 * up(9, 11)) == 0.0654
assert 2 * up(9, 11) > 0.05 and 2 * up(9, 11) < 0.10

print("a212 checks passed")
