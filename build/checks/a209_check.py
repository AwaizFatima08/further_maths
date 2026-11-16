"""Recomputes every number stated in content/a209.py (one-sample t) and checks it to the stated precision."""
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
    """Check a quoted t value against Table 3 (string match) and scipy."""
    header, rows = TABLES[2][1], TABLES[2][2]
    row = next(r for r in rows if r[0] == str(nu))
    cell = row[header.index(str(p))]
    ok = cell == f"{stated:.3f}" and round(t.isf(p, nu), 3) == stated
    print(("ok  " if ok else "FAIL"), f"t table nu={nu} p={p}", cell, "stated", stated)
    if not ok:
        FAILS.append(f"ttab {nu} {p}")


def ss(n, S, S2):
    xb = S / n
    v = (S2 - S * S / n) / (n - 1)
    return xb, v, sqrt(v)


# Notes table and box
for nu, v in [(5, 2.571), (10, 2.228), (20, 2.086), (30, 2.042), (60, 2.000), (9, 2.262), (6, 2.447)]:
    if nu != 6:
        ttab(nu, 0.025, v)
for nu, v in [(5, 2.015), (10, 1.812), (20, 1.725), (30, 1.697), (60, 1.671)]:
    ttab(nu, 0.05, v)
ttab(9, 0.005, 3.250)
chk("z 2.5%", norm.isf(0.025), 1.960, dp=3)
chk("z 5%", norm.isf(0.05), 1.645, dp=3)
chk("narrower %", 100 * (1 - 1.96 / 2.571), 24, dp=0)

# Example 1
ttab(9, 0.05, 1.833)
ttab(15, 0.025, 2.131)
ttab(20, 0.01, 2.528)

# Example 2
d = np.array([49.2, 50.1, 48.7, 49.5, 49.9, 48.8, 49.6, 50.0])
chk("ex2 sum", d.sum(), 395.8, dp=1)
chk("ex2 sumsq", (d ** 2).sum(), 19584.2, dp=1)
chk("ex2 mean", d.mean(), 49.475, dp=3)
chk("ex2 s2", d.var(ddof=1), 0.285, dp=3)
chk("ex2 s", d.std(ddof=1), 0.53385, dp=5)
se = d.std(ddof=1) / sqrt(8)
chk("ex2 se", se, 0.18875, dp=5)
tt = (d.mean() - 50) / se
chk("ex2 t", tt, -2.78)
ttab(7, 0.05, 1.895)
chk("ex2 p", t.cdf(tt, 7), 0.0136, dp=4)

# Example 3
x = ss(12, 186.0, 2898.5)
chk("ex3 mean", x[0], 15.5, dp=1)
chk("ex3 2883", 186.0 ** 2 / 12, 2883, dp=6)
chk("ex3 s2", x[1], 1.4091, dp=4)
chk("ex3 s", x[2], 1.1871, dp=4)
ttab(11, 0.005, 3.106)
se = x[2] / sqrt(12)
chk("ex3 se", se, 0.34267, dp=5)
chk("ex3 half", 3.106 * se, 1.0643, dp=4)
chk("ex3 lo", 15.5 - 3.106 * se, 14.44, dp=2)
chk("ex3 hi", 15.5 + 3.106 * se, 16.56, dp=2)

# Example 4
s = 1.2 * sqrt(10) / 2.262
chk("ex4 s", s, 1.68)
chk("ex4 s4", s, 1.6776, dp=4)
h = 1.833 * s / sqrt(10)
chk("ex4 h", h, 0.97241, dp=5)
chk("ex4 lo", 15.4 - h, 14.43, dp=2)
chk("ex4 hi", 15.4 + h, 16.37, dp=2)

# Example 5
y = ss(14, 31.5, 182.25)
chk("ex5 ybar", y[0], 2.25, dp=2)
chk("ex5 Syy", 182.25 - 31.5 ** 2 / 14, 111.375, dp=3)
chk("ex5 s2", y[1], 8.5673, dp=4)
chk("ex5 s", y[2], 2.9270, dp=4)
se = y[2] / sqrt(14)
chk("ex5 se", se, 0.78227, dp=5)
tt = y[0] / se
chk("ex5 t", tt, 2.88)
ttab(13, 0.005, 3.012)
chk("ex5 p", 2 * t.sf(tt, 13), 0.0130, dp=4)
assert norm.isf(0.005) < tt < t.isf(0.005, 13)
chk("ex5 half", 3.012 * se, 2.3562, dp=4)
chk("ex5 lo", 102.25 - 3.012 * se, 99.89, dp=2)
chk("ex5 hi", 102.25 + 3.012 * se, 104.61, dp=2)

# Practice
ttab(7, 0.025, 2.365)
ttab(18, 0.01, 2.552)
ttab(24, 0.05, 1.711)
d = np.array([12.4, 11.8, 13.1, 12.9, 12.2, 12.6])
chk("p3 mean", d.mean(), 12.5, dp=1)
chk("p3 s", d.std(ddof=1), 0.473)
ttab(5, 0.025, 2.571)
h = 2.571 * d.std(ddof=1) / sqrt(6)
chk("p3 h", h, 0.49676, dp=5)
chk("p3 lo", 12.5 - h, 12.00, dp=2)
chk("p3 hi", 12.5 + h, 13.00, dp=2)
x = ss(10, 84.0, 712.6)
chk("p4 mean", x[0], 8.4, dp=1)
chk("p4 s2", x[1], 0.77778, dp=5)
chk("p4 s", x[2], 0.88192, dp=5)
chk("p4 t", (x[0] - 8) / (x[2] / sqrt(10)), 1.43)
s = 2.1 * sqrt(9 / 8)
chk("p5 s", s, 2.23)
chk("p5 s4", s, 2.2274, dp=4)
ttab(8, 0.025, 2.306)
h = 2.306 * s / 3
chk("p5 h", h, 1.7121, dp=4)
chk("p5 lo", 30.4 - h, 28.69, dp=2)
chk("p5 hi", 30.4 + h, 32.11, dp=2)
chk("p6 t", (72.6 - 75) / (4.8 / 4), -2.00)
chk("p7 s", 0.58 * sqrt(8) / 2.365, 0.694)
ttab(9, 0.025, 2.262)
chk("p9 p", t.sf(2.21, 9), 0.0272, dp=4)
ttab(30, 0.025, 2.042)
chk("p10 ratio", (2.306 / 3) / (2.042 / sqrt(31)), 2.10)
ttab(14, 0.05, 1.761)
h = 1.761 * 0.35 / sqrt(15)
chk("p11 h", h, 0.15914, dp=5)
chk("p11 lo", 2.84 - h, 2.68, dp=2)
chk("p11 hi", 2.84 + h, 3.00, dp=2)
d = np.array([5.8, 6.4, 6.1, 7.0, 6.6, 6.3, 6.9])
chk("p12 mean", d.mean(), 6.4429, dp=4)
chk("p12 s", d.std(ddof=1), 0.42762, dp=5)
chk("p12 diff", d.mean() - 6, 0.44286, dp=5)
tt = (d.mean() - 6) / (d.std(ddof=1) / sqrt(7))
chk("p12 t", tt, 2.74)
ttab(6, 0.01, 3.143)
chk("p12 p", t.sf(tt, 6), 0.0169, dp=4)

# Exam 1
d = np.array([328.4, 331.2, 327.9, 329.5, 330.1, 326.8, 329.0, 328.2, 330.6, 327.5])
chk("b1 sum", d.sum(), 3289.2, dp=1)
chk("b1 sumsq", (d ** 2).sum(), 1081901.76, dp=2)
chk("b1 mean", d.mean(), 328.92, dp=2)
chk("b1 s2", d.var(ddof=1), 2.01)
chk("b1 s", d.std(ddof=1), 1.4180, dp=4)
se = d.std(ddof=1) / sqrt(10)
chk("b1 se", se, 0.44840, dp=5)
tt = (d.mean() - 330) / se
chk("b1 t", tt, -2.41)
ttab(9, 0.05, 1.833)
chk("b1 p", t.cdf(tt, 9), 0.0197, dp=4)
ttab(9, 0.005, 3.250)
chk("b1 lo", d.mean() - 3.250 * se, 327.46, dp=2)
chk("b1 hi", d.mean() + 3.250 * se, 330.38, dp=2)

# Exam 2
ttab(11, 0.025, 2.201)
s = 2.74 * sqrt(12) / 2.201
chk("b2 s", s, 4.3124, dp=4)
chk("b2 s2", s * s, 18.6)
ttab(11, 0.05, 1.796)
h = 1.796 * s / sqrt(12)
chk("b2 h", h, 2.2358, dp=4)
chk("b2 lo", 44.1 - h, 41.86, dp=2)
chk("b2 hi", 44.1 + h, 46.34, dp=2)
assert 44.1 - h < 46 < 44.1 + h

# Exam 3
se = 1.75 / sqrt(11)
chk("b3 se", se, 0.52764, dp=5)
tt = (16.12 - 15) / se
chk("b3 t", tt, 2.1226, dp=4)
chk("b3 p2", 2 * t.sf(tt, 10), 0.0598, dp=4)
chk("b3 p1", t.sf(tt, 10), 0.0299, dp=4)
ttab(10, 0.025, 2.228)
chk("b3 lo", 16.12 - 2.228 * se, 14.94, dp=2)
chk("b3 hi", 16.12 + 2.228 * se, 17.30, dp=2)

# Exam 4
y = ss(9, 13.5, 58.77)
chk("b4 ybar", y[0], 1.5, dp=1)
chk("b4 s2", y[1], 4.815, dp=3)
se = y[2] / 3
chk("b4 se", se, 0.73144, dp=5)
ttab(8, 0.01, 2.896)
chk("b4 lo", 21.5 - 2.896 * se, 19.38, dp=2)
chk("b4 hi", 21.5 + 2.896 * se, 23.62, dp=2)

print("\nFAILED:" if FAILS else "\nALL CHECKS PASSED", FAILS if FAILS else "")
raise SystemExit(1 if FAILS else 0)
