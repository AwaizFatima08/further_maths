"""Recomputes every number stated in content/a211.py (chi-squared intervals for variance, F-test) and checks it."""
import json
from math import sqrt
from pathlib import Path

import numpy as np
from scipy.stats import chi2, f, t

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


def _cell(table_index, row_key, col_key):
    header, rows = TABLES[table_index][1], TABLES[table_index][2]
    row = next(r for r in rows if r[0] == str(row_key))
    return row[header.index(str(col_key))]


def report(ok, label, cell, stated):
    print(("ok  " if ok else "FAIL"), label, cell, "stated", stated)
    if not ok:
        FAILS.append(label)


def ttab(nu, p, stated):
    cell = _cell(2, nu, p)
    report(cell == f"{stated:.3f}" and round(t.isf(p, nu), 3) == stated, f"t nu={nu} p={p}", cell, stated)


def ctab(nu, p_upper, stated):
    """chi-squared value x with P(X > x) = p_upper (Table 4 layout)."""
    cell = _cell(3, nu, p_upper)
    report(cell == f"{stated:.3f}" and round(chi2.isf(p_upper, nu), 3) == stated, f"chi2 nu={nu} p={p_upper}", cell, stated)


def ftab(alpha, v1, v2, stated):
    cell = _cell(4 if alpha == 0.05 else 5, v2, v1)
    report(cell == f"{stated:.2f}" and round(f.isf(alpha, v1, v2), 2) == stated, f"F{alpha} ({v1},{v2})", cell, stated)


# Notes
ctab(9, 0.975, 2.700)
ctab(9, 0.025, 19.023)
ftab(0.05, 8, 5, 4.82)
chk("notes lower F(5,8)", 1 / 4.82, 0.2075, sig=4)
chk("notes lower F(5,8) scipy", f.ppf(0.05, 5, 8), 0.2075, sig=4)

# Example 1
ftab(0.05, 5, 8, 3.69)
ftab(0.01, 12, 6, 7.72)
chk("ex1 d", 1 / 7.72, 0.130)
chk("ex1 d scipy", f.ppf(0.01, 6, 12), 0.130)

# Example 2
X = np.array([12.1, 11.8, 12.4, 12.0, 11.6, 12.3, 12.2, 11.9, 12.5, 11.7])
chk("ex2 sum", X.sum(), 120.5, dp=2)
chk("ex2 sumsq", (X ** 2).sum(), 1452.85, dp=2)
Sxx = ((X - X.mean()) ** 2).sum()
chk("ex2 Sxx", Sxx, 0.825, dp=4)
chk("ex2 s2", X.var(ddof=1), 0.091667, dp=6)
chk("ex2 lo", Sxx / 19.023, 0.0434)
chk("ex2 hi", Sxx / 2.700, 0.306)
chk("ex2 lo5", Sxx / 19.023, 0.043369, dp=6)
chk("ex2 hi5", Sxx / 2.700, 0.30556, dp=5)
chk("ex2 slo", sqrt(Sxx / 19.023), 0.208)
chk("ex2 shi", sqrt(Sxx / 2.700), 0.553)
chk("ex2 s", X.std(ddof=1), 0.303)

# Example 3
st = 14 * 0.68 ** 2 / 0.25
chk("ex3 s2", 0.68 ** 2, 0.4624, dp=4)
chk("ex3 stat", st, 25.9)
ctab(14, 0.05, 23.685)
chk("ex3 p", chi2.sf(st, 14), 0.0267, dp=4)

# Example 4
st = 20 * 4.2 / 7.5
chk("ex4 stat", st, 11.2, dp=4)
ctab(20, 0.95, 10.851)
chk("ex4 p", chi2.cdf(st, 20), 0.0591, dp=4)

# Example 5
F = 8.4 / 2.9
chk("ex5 F", F, 2.90)
ftab(0.05, 6, 10, 3.22)
chk("ex5 p", 2 * f.sf(F, 6, 10), 0.133)

# Example 6
F = 5.6 / 3.1
chk("ex6 F", F, 1.81)
ftab(0.05, 8, 12, 2.85)
sp2 = (8 * 5.6 + 12 * 3.1) / 20
chk("ex6 sp2", sp2, 4.1, dp=6)
se = sqrt(sp2 * (1 / 9 + 1 / 13))
chk("ex6 se", se, 0.87803, dp=5)
tt = 2.3 / se
chk("ex6 t", tt, 2.62)
ttab(20, 0.025, 2.086)
chk("ex6 p", 2 * t.sf(tt, 20), 0.0164, dp=4)

# Practice
ctab(12, 0.05, 21.026)
ctab(12, 0.95, 5.226)
ctab(24, 0.99, 10.856)
ctab(15, 0.95, 7.261)
ctab(15, 0.05, 24.996)
chk("p3 lo", 15 * 12.5 / 24.996, 7.50)
chk("p3 hi", 15 * 12.5 / 7.261, 25.8)
ctab(24, 0.995, 9.886)
ctab(24, 0.005, 45.559)
a, b = 24 * 11.56 / 45.559, 24 * 11.56 / 9.886
chk("p4 s2", 3.4 ** 2, 11.56, dp=4)
chk("p4 a", a, 6.0897, dp=4)
chk("p4 b", b, 28.064, dp=3)
chk("p4 slo", sqrt(a), 2.47)
chk("p4 shi", sqrt(b), 5.30)
st = 10 * 0.0413 / 0.02
chk("p5 stat", st, 20.65, dp=4)
ctab(10, 0.975, 3.247)
ctab(10, 0.025, 20.483)
assert st > 20.483
Y = np.array([24.3, 21.8, 26.1, 23.4, 22.0, 25.7, 24.9, 21.6])
chk("p6 mean", Y.mean(), 23.725, dp=3)
chk("p6 s2", Y.var(ddof=1), 3.2221, dp=4)
chk("p6 stat", 7 * Y.var(ddof=1) / 2.25, 10.0)
ctab(7, 0.05, 14.067)
ftab(0.05, 4, 10, 3.48)
ftab(0.01, 10, 4, 14.55)
ftab(0.05, 12, 6, 4.00)
chk("p7c", 1 / 4.00, 0.25, dp=4)
chk("p7c scipy", f.ppf(0.05, 6, 12), 0.25, dp=3)
ftab(0.01, 10, 8, 5.81)
chk("p8", 1 / 5.81, 0.172)
chk("p8 scipy", f.ppf(0.01, 8, 10), 0.172)
chk("p9 F", 0.84 / 0.31, 2.71)
ftab(0.05, 12, 8, 3.28)
chk("p10 F", 4.8 ** 2 / 1.9 ** 2, 6.38)
ftab(0.01, 5, 24, 3.90)
chk("chi2(8) mean", chi2.mean(8), 8, dp=6)
chk("chi2(8) var", chi2.var(8), 16, dp=6)

# Exam 1
X = np.array([2.41, 2.86, 2.53, 2.17, 2.74, 2.95, 2.38, 2.62, 2.80, 2.24])
chk("b1 sum", X.sum(), 25.7, dp=4)
chk("b1 sumsq", (X ** 2).sum(), 66.694, dp=3)
chk("b1 mean", X.mean(), 2.57, dp=4)
Sxx = ((X - X.mean()) ** 2).sum()
chk("b1 Sxx", Sxx, 0.645, dp=4)
chk("b1 s2", X.var(ddof=1), 0.0717)
chk("b1 lo", Sxx / 19.023, 0.033906, dp=6)
chk("b1 hi", Sxx / 2.700, 0.23889, dp=5)
chk("b1 slo", sqrt(Sxx / 19.023), 0.184)
chk("b1 shi", sqrt(Sxx / 2.700), 0.489)
st = 9 * X.var(ddof=1) / 0.04
chk("b1 stat", st, 16.1)
ctab(9, 0.05, 16.919)

# Exam 2
vx = (5976.41 - 231.3 ** 2 / 9) / 8
vy = (6255.84 - 261.8 ** 2 / 11) / 10
chk("b2 Sxx", 5976.41 - 231.3 ** 2 / 9, 32, dp=6)
chk("b2 Syy", 6255.84 - 261.8 ** 2 / 11, 25, dp=6)
chk("b2 vx", vx, 4.0, dp=6)
chk("b2 vy", vy, 2.5, dp=6)
chk("b2 F", vx / vy, 1.6, dp=6)
ftab(0.05, 8, 10, 3.07)
chk("b2 xbar", 231.3 / 9, 25.7, dp=6)
chk("b2 ybar", 261.8 / 11, 23.8, dp=6)
sp2 = (32 + 25) / 18
chk("b2 sp2", sp2, 3.1667, dp=4)
se = sqrt(sp2 * (1 / 9 + 1 / 11))
chk("b2 se", se, 0.79983, dp=5)
chk("b2 t", 1.9 / se, 2.38)
ttab(18, 0.05, 1.734)

# Exam 3
chk("b3 F", 1.2 / 3.9, 0.308)
chk("b3 lower", 1 / 4.82, 0.2075, sig=4)
chk("b3 F2", 3.9 / 1.2, 3.25, dp=4)
ctab(8, 0.95, 2.733)
ctab(8, 0.05, 15.507)
chk("b3 31.2", 8 * 3.9, 31.2, dp=6)
chk("b3 lo", 31.2 / 15.507, 2.0120, dp=4)
chk("b3 hi", 31.2 / 2.733, 11.416, dp=3)
chk("b3 slo", sqrt(31.2 / 15.507), 1.42)
chk("b3 shi", sqrt(31.2 / 2.733), 3.38)
chk("b3 stat", 5 * 1.2 / 3, 2.0, dp=6)
ctab(5, 0.95, 1.145)

print("\nFAILED:" if FAILS else "\nALL CHECKS PASSED", FAILS if FAILS else "")
raise SystemExit(1 if FAILS else 0)
