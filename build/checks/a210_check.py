"""Recomputes every number stated in content/a210.py (pooled and paired t) and checks it to the stated precision."""
import json
from math import sqrt
from pathlib import Path

import numpy as np
from scipy.stats import norm, t

TABLES = json.loads((Path(__file__).resolve().parents[1] / "tables_cache.json").read_text())
FAILS = []


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def chk(label, value, stated, dp=None, sig=None):
    got = round(value, dp) if dp is not None else sf(value, sig or 3)
    ok = abs(got - stated) < 1e-9
    print(("ok  " if ok else "FAIL"), label, value, "stated", stated)
    if not ok:
        FAILS.append(label)


def ttab(nu, p, stated):
    header, rows = TABLES[2][1], TABLES[2][2]
    row = next(r for r in rows if r[0] == str(nu))
    cell = row[header.index(str(p))]
    ok = cell == f"{stated:.3f}" and round(t.isf(p, nu), 3) == stated
    print(("ok  " if ok else "FAIL"), f"t table nu={nu} p={p}", cell, "stated", stated)
    if not ok:
        FAILS.append(f"ttab {nu} {p}")


def dev2(a):
    a = np.asarray(a, float)
    return ((a - a.mean()) ** 2).sum()


# Example 1
before = np.array([52, 61, 47, 70, 58, 65, 49, 55])
after = np.array([56, 63, 52, 71, 62, 64, 55, 59])
d = after - before
assert list(d) == [4, 2, 5, 1, 4, -1, 6, 4]
chk("ex1 sum", d.sum(), 25, dp=0)
chk("ex1 sumsq", (d ** 2).sum(), 115, dp=0)
chk("ex1 mean", d.mean(), 3.125, dp=3)
chk("ex1 var", d.var(ddof=1), 5.2679, dp=4)
chk("ex1 s", d.std(ddof=1), 2.2952, dp=4)
se = d.std(ddof=1) / sqrt(8)
chk("ex1 se", se, 0.81147, dp=5)
tt = d.mean() / se
chk("ex1 t", tt, 3.85)
ttab(7, 0.05, 1.895)
chk("ex1 p", t.sf(tt, 7), 0.0031, dp=4)

# Example 2
db = 23.0 / 10
v = (81.4 - 23.0 ** 2 / 10) / 9
chk("ex2 num", 81.4 - 23.0 ** 2 / 10, 28.5, dp=6)
chk("ex2 var", v, 3.1667, dp=4)
chk("ex2 s", sqrt(v), 1.7795, dp=4)
ttab(9, 0.025, 2.262)
h = 2.262 * sqrt(v) / sqrt(10)
chk("ex2 h", h, 1.2729, dp=4)
chk("ex2 lo", db - h, 1.03)
chk("ex2 hi", db + h, 3.57)

# Example 3
A = [23.1, 25.4, 24.8, 22.9, 26.0, 24.3]
B = [21.8, 23.5, 22.6, 24.1, 21.2, 22.9, 23.0]
chk("ex3 SA", sum(A), 146.5, dp=1)
chk("ex3 SA2", sum(a * a for a in A), 3584.71, dp=2)
chk("ex3 SB", sum(B), 159.1, dp=1)
chk("ex3 SB2", sum(b * b for b in B), 3621.91, dp=2)
chk("ex3 meanA", np.mean(A), 24.417, dp=3)
chk("ex3 meanB", np.mean(B), 22.729, dp=3)
chk("ex3 devA", dev2(A), 7.6683, dp=4)
chk("ex3 devB", dev2(B), 5.7943, dp=4)
sp2 = (dev2(A) + dev2(B)) / 11
chk("ex3 sp2", sp2, 1.2239, dp=4)
chk("ex3 sp", sqrt(sp2), 1.1063, dp=4)
se = sqrt(sp2) * sqrt(1 / 6 + 1 / 7)
chk("ex3 se", se, 0.61548, dp=5)
tt = (np.mean(A) - np.mean(B)) / se
chk("ex3 t", tt, 2.74)
ttab(11, 0.025, 2.201)
chk("ex3 p", 2 * t.sf(tt, 11), 0.0191, dp=4)

# Example 4
Sxx = 23380 - 482 ** 2 / 10
Syy = 25360 - 549.6 ** 2 / 12
chk("ex4 Sxx", Sxx, 147.6, dp=4)
chk("ex4 Syy", Syy, 188.32, dp=4)
sp2 = (Sxx + Syy) / 20
chk("ex4 sp2", sp2, 16.796, dp=3)
chk("ex4 sp2 3sf", sp2, 16.8)
chk("ex4 var", sp2 * (1 / 10 + 1 / 12), 3.0793, dp=4)
se = sqrt(sp2 * (1 / 10 + 1 / 12))
chk("ex4 se", se, 1.7548, dp=4)
chk("ex4 diff", 48.2 - 45.8, 2.4, dp=6)
chk("ex4 t", 2.4 / se, 1.37)
ttab(20, 0.05, 1.725)
ttab(20, 0.025, 2.086)
chk("ex4 h", 2.086 * se, 3.6605, dp=4)
chk("ex4 lo", 2.4 - 2.086 * se, -1.26)
chk("ex4 hi", 2.4 + 2.086 * se, 6.06)

# Example 6
A = np.array([5.2, 6.8, 4.1, 7.5, 5.9, 6.3])
B = np.array([4.6, 6.1, 3.9, 6.8, 5.0, 5.8])
d = A - B
chk("ex6 dbar", d.mean(), 0.6, dp=4)
chk("ex6 sd", d.std(ddof=1), 0.23664, dp=5)
tt = d.mean() / (d.std(ddof=1) / sqrt(6))
chk("ex6 t", tt, 6.21)
ttab(5, 0.01, 3.365)
chk("ex6 meanA", A.mean(), 5.9667, dp=4)
chk("ex6 varA", A.var(ddof=1), 1.4467, dp=4)
chk("ex6 meanB", B.mean(), 5.3667, dp=4)
chk("ex6 varB", B.var(ddof=1), 1.1307, dp=4)
sp2 = (5 * A.var(ddof=1) + 5 * B.var(ddof=1)) / 10
chk("ex6 sp2", sp2, 1.2887, dp=4)
se = sqrt(sp2 * (1 / 6 + 1 / 6))
chk("ex6 se", se, 0.65540, dp=5)
chk("ex6 t2", 0.6 / se, 0.915)
ttab(10, 0.1, 1.372)

# Practice
chk("p1", (7 * 3.2 ** 2 + 10 * 2.7 ** 2) / 17, 8.50)
X = [14, 17, 15, 19, 16]
Y = [12, 15, 13, 14, 11, 13]
chk("p2 x", np.mean(X), 16.2, dp=1)
chk("p2 y", np.mean(Y), 13.0, dp=1)
chk("p2 dx", dev2(X), 14.8, dp=4)
chk("p2 dy", dev2(Y), 10, dp=4)
chk("p2 sp2", (dev2(X) + dev2(Y)) / 9, 2.76)
chk("p3 dx", 1557 - 117 ** 2 / 9, 36, dp=6)
chk("p3 dy", 1078 - 92 ** 2 / 8, 20, dp=6)
chk("p3 sp2", 56 / 15, 3.73)
chk("p4 t", 1.8 / (2.9 / sqrt(12)), 2.15)
ttab(11, 0.05, 1.796)
L = np.array([31, 28, 35, 30, 27, 33, 29])
R = np.array([33, 29, 34, 33, 30, 35, 31])
d = R - L
assert list(d) == [2, 1, -1, 3, 3, 2, 2]
chk("p5 dbar", d.mean(), 1.7143, dp=4)
chk("p5 sd", d.std(ddof=1), 1.3801, dp=4)
chk("p5 t", d.mean() / (d.std(ddof=1) / sqrt(7)), 3.29)
ttab(6, 0.025, 2.447)
sp2 = (8 * 2.1 ** 2 + 10 * 2.4 ** 2) / 18
chk("p6 sp2", sp2, 5.16, dp=4)
se = sqrt(sp2 * (1 / 9 + 1 / 11))
chk("p6 se", se, 1.0210, dp=4)
chk("p6 t", 1.9 / se, 1.86)
ttab(18, 0.05, 1.734)
sp2 = (6 * 5.3 ** 2 + 8 * 6.0 ** 2) / 14
chk("p7 sp2", sp2, 32.61, dp=4)
se = sqrt(sp2 * (1 / 7 + 1 / 9))
chk("p7 se", se, 2.8778, dp=4)
ttab(14, 0.025, 2.145)
chk("p7 lo", 6.3 - 2.145 * se, 0.127)
chk("p7 hi", 6.3 + 2.145 * se, 12.5)
sp2 = (11 * 3.4 ** 2 + 9 * 3.9 ** 2) / 20
chk("p8 sp2", sp2, 13.2025, dp=4)
se = sqrt(sp2 * (1 / 12 + 1 / 10))
chk("p8 se", se, 1.5558, dp=4)
chk("p8 t", (48.6 - 43.2 - 3) / se, 1.54)
ttab(8, 0.05, 1.860)
h = 1.860 * 1.12 / 3
chk("p11 h", h, 0.6944, dp=4)
chk("p11 lo", 0.84 - h, 0.146)
chk("p11 hi", 0.84 + h, 1.53)
ttab(18, 0.025, 2.101)
chk("p12 sp", 2.7 / (2.101 * sqrt(0.2)), 2.87)
chk("p12 root", sqrt(0.2), 0.44721, dp=5)

# Exam 1
sp2 = (6.42 + 7.83) / 16
chk("b1 sp2", sp2, 0.891)
chk("b1 sp2 exact", sp2, 0.890625, dp=6)
chk("b1 pbar", 41.6 / 8, 5.2, dp=4)
chk("b1 qbar", 46.0 / 10, 4.6, dp=4)
se = sqrt(sp2 * (1 / 8 + 1 / 10))
chk("b1 se", se, 0.44765, dp=5)
chk("b1 t", 0.6 / se, 1.34)
ttab(16, 0.05, 1.746)
ttab(16, 0.025, 2.120)
chk("b1 lo", 0.6 - 2.120 * se, -0.349)
chk("b1 hi", 0.6 + 2.120 * se, 1.55)

# Exam 2
O = np.array([62.4, 58.9, 65.1, 60.3, 63.8, 59.6, 61.2, 64.0, 57.5])
N = np.array([61.1, 58.2, 63.0, 60.5, 62.1, 58.3, 60.4, 62.2, 57.6])
d = O - N
assert np.allclose(d, [1.3, 0.7, 2.1, -0.2, 1.7, 1.3, 0.8, 1.8, -0.1])
chk("b2 sum", d.sum(), 9.4, dp=4)
chk("b2 sumsq", (d ** 2).sum(), 15.1, dp=4)
chk("b2 dbar", d.mean(), 1.0444, dp=4)
chk("b2 sd", d.std(ddof=1), 0.81257, dp=5)
se = d.std(ddof=1) / 3
chk("b2 se", se, 0.27086, dp=5)
chk("b2 t", d.mean() / se, 3.86)
ttab(8, 0.01, 2.896)
ttab(8, 0.025, 2.306)
chk("b2 lo", d.mean() - 2.306 * se, 0.420)
chk("b2 hi", d.mean() + 2.306 * se, 1.67)

# Exam 3
A = np.array([18.2, 19.5, 17.8, 18.9, 19.1, 18.4])
B = np.array([17.5, 18.8, 17.2, 18.0, 17.9, 18.3])
chk("b3 mA", A.mean(), 18.65, dp=4)
chk("b3 mB", B.mean(), 17.95, dp=4)
chk("b3 vA", A.var(ddof=1), 0.395, dp=4)
chk("b3 vB", B.var(ddof=1), 0.323, dp=4)
sp2 = (5 * A.var(ddof=1) + 5 * B.var(ddof=1)) / 10
chk("b3 sp2", sp2, 0.359, dp=4)
se = sqrt(sp2 * (1 / 6 + 1 / 6))
chk("b3 se", se, 0.34593, dp=5)
chk("b3 t", 0.7 / se, 2.02)
ttab(10, 0.05, 1.812)
se = sqrt(0.85 ** 2 / 50 + 1.20 ** 2 / 60)
chk("b3b se", se, 0.19609, dp=5)
chk("b3b z", 0.41 / se, 2.09)
assert 0.41 / se > norm.isf(0.025)

# Exam 4
ttab(14, 0.025, 2.145)
h = 2.145 * 3.10 / sqrt(15)
chk("b4 h", h, 1.7169, dp=4)
chk("b4 lo", 2.43 - h, 0.713, dp=3)
chk("b4 hi", 2.43 + h, 4.147, dp=3)
tt = 2.43 / (3.10 / sqrt(15))
chk("b4 t", tt, 3.04)
ttab(14, 0.005, 2.977)
assert tt > 2.977

print("\nFAILED:" if FAILS else "\nALL CHECKS PASSED", FAILS if FAILS else "")
raise SystemExit(1 if FAILS else 0)
