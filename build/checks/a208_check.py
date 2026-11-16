"""Recomputes every number stated in content/a208.py (z-tests and intervals) and checks it to the stated precision."""
import json
from math import sqrt
from pathlib import Path

from scipy.stats import norm

TABLES = json.loads((Path(__file__).resolve().parents[1] / "tables_cache.json").read_text())
FAILS = []


def sf(x, n=3):
    return float(f"{x:.{n}g}")


def chk(label, value, stated, dp=None, sig=None):
    """stated must equal value rounded to dp decimal places or sig significant figures."""
    got = round(value, dp) if dp is not None else sf(value, sig or 3)
    ok = abs(got - stated) < 1e-9
    print(("ok  " if ok else "FAIL"), label, value, "stated", stated)
    if not ok:
        FAILS.append(label)


def normal_point(p):
    header, rows = TABLES[1][1], TABLES[1][2]
    return float(rows[0][header.index(str(p))])


def ss(n, S, S2):
    xb = S / n
    v = (S2 - S * S / n) / (n - 1)
    return xb, v, sqrt(v)


# Critical values quoted (Table 2 and scipy)
for p, z in [(0.1, 1.2816), (0.05, 1.6449), (0.025, 1.96), (0.01, 2.3263), (0.005, 2.5758)]:
    chk(f"table z {p}", normal_point(p), z, dp=4)
    chk(f"scipy z {p}", norm.isf(p), z, dp=4)
chk("two-tailed 2.5%", norm.isf(0.0125), 2.2414, dp=4)

# Example 1
se = 4.2 / sqrt(20)
chk("ex1 se", se, 0.93915, dp=5)
z = (497.8 - 500) / se
chk("ex1 z", z, -2.34)
chk("ex1 p", norm.cdf(z), 0.0096, dp=4)
chk("ex1 cv xbar", 500 - 1.6449 * se, 498.455, dp=3)
chk("ex1 cv xbar 2dp", 500 - 1.6449 * se, 498.46, dp=2)

# Example 2
xb, v, s = ss(60, 1830, 57240)
chk("ex2 xbar", xb, 30.5, dp=1)
chk("ex2 s2", v, 24.2)
chk("ex2 1425/59", (57240 - 1830 ** 2 / 60), 1425, dp=6)
chk("ex2 s", s, 4.9145, dp=4)
se = s / sqrt(60)
chk("ex2 se", se, 0.63446, dp=5)
z = (xb - 29) / se
chk("ex2 z", z, 2.36)
chk("ex2 p", 2 * norm.sf(z), 0.0181, dp=4)
chk("ex2 half", 1.96 * se, 1.2435, dp=4)
chk("ex2 lo", xb - 1.96 * se, 29.26, dp=2)
chk("ex2 hi", xb + 1.96 * se, 31.74, dp=2)

# Example 3
se = sqrt(1.44 / 15 + 2.25 / 12)
chk("ex3 var", 1.44 / 15 + 2.25 / 12, 0.2835, dp=4)
chk("ex3 se", se, 0.53245, dp=5)
z = 1.1 / se
chk("ex3 z", z, 2.07)
chk("ex3 p", 2 * norm.sf(z), 0.0388, dp=4)

# Example 4
se = sqrt(5.1 ** 2 / 50 + 4.3 ** 2 / 40)
chk("ex4 se", se, 0.99119, dp=5)
z = (42.8 - 39.1 - 2) / se
chk("ex4 z", z, 1.72)
chk("ex4 p", norm.sf(z), 0.0432, dp=4)
chk("ex4 half", 1.96 * se, 1.9427, dp=4)
chk("ex4 lo", 3.7 - 1.96 * se, 1.76)
chk("ex4 hi", 3.7 + 1.96 * se, 5.64)

# Example 5
x = ss(80, 3376, 146700)
y = ss(100, 4050, 168900)
chk("ex5 xbar", x[0], 42.2, dp=1)
chk("ex5 sx2", x[1], 53.580, dp=3)
chk("ex5 ybar", y[0], 40.5, dp=1)
chk("ex5 sy2", y[1], 49.242, dp=3)
chk("ex5 a", x[1] / 80, 0.66975, dp=5)
chk("ex5 b", y[1] / 100, 0.49242, dp=5)
se = sqrt(x[1] / 80 + y[1] / 100)
chk("ex5 se", se, 1.0780, dp=4)
z = (x[0] - y[0]) / se
chk("ex5 z", z, 1.58)
chk("ex5 z4", z, 1.5769, dp=4)
chk("ex5 p", norm.sf(z), 0.0574, dp=4)

# Practice
chk("p1 z", 0.42 / 0.2, 2.10)
z = (58.1 - 62) / (12 / sqrt(30))
chk("p2 se", 12 / sqrt(30), 2.1909, dp=4)
chk("p2 z", z, -1.78)
chk("p2 p", 2 * norm.cdf(z), 0.0751, dp=4)
x = ss(50, 1612, 54080)
chk("p3 xbar", x[0], 32.24, dp=2)
chk("p3 s2", x[1], 43.0)
chk("p3 s", x[2], 6.5607, dp=4)
chk("p3 z", (x[0] - 31) / (x[2] / sqrt(50)), 1.34)
chk("p4", 40 - 1.6449 * 0.6, 39.013, dp=3)
chk("p4 2dp", 40 - 1.6449 * 0.6, 39.01, dp=2)
chk("p5 lo", 12.6 - 1.96 * 0.3, 12.01, dp=2)
chk("p5 hi", 12.6 + 1.96 * 0.3, 13.19, dp=2)
chk("p6 s", 0.7 * sqrt(50) / 1.96, 2.53)
h = 2.5758 * 0.7 / 1.96
chk("p6 h", h, 0.91993, dp=5)
chk("p6 lo", 12.8 - h, 11.88, dp=2)
chk("p6 hi", 12.8 + h, 13.72, dp=2)
se = sqrt(36 / 36 + 64 / 40)
chk("p7 se", se, 1.6125, dp=4)
chk("p7 z", 3.3 / se, 2.05)
se = sqrt(6.2 ** 2 / 45 + 5.4 ** 2 / 55)
chk("p8 var", se ** 2, 1.3844, dp=4)
chk("p8 se", se, 1.1766, dp=4)
chk("p8 z", 2.2 / se, 1.87)
se = sqrt(3.1 ** 2 / 70 + 2.7 ** 2 / 80)
chk("p9 se", se, 0.47792, dp=5)
chk("p9 h", 1.6449 * se, 0.78614, dp=5)
chk("p9 lo", 1.4 - 1.6449 * se, 0.614)
chk("p9 hi", 1.4 + 1.6449 * se, 2.19)
r = 1.6449 * 5 / 1.2
chk("p11 r", r, 6.8538, dp=4)
chk("p11 n", r * r, 46.97, dp=2)
assert (81.2 - 80) / (5 / sqrt(47)) > norm.isf(0.05) > (81.2 - 80) / (5 / sqrt(46)), "p11 n = 47"
h = 1.96 * 2.8 / sqrt(40)
chk("p12 h", h, 0.86773, dp=5)
chk("p12 lo", 1.35 - h, 0.482)
chk("p12 hi", 1.35 + h, 2.22)

# Exam 1
x = ss(45, 283.5, 1946.25)
chk("b1 xbar", x[0], 6.3, dp=1)
chk("b1 num", 1946.25 - 283.5 ** 2 / 45, 160.2, dp=6)
chk("b1 s2", x[1], 3.64)
chk("b1 s2 4dp", x[1], 3.6409, dp=4)
se = x[2] / sqrt(45)
chk("b1 se", se, 0.28445, dp=5)
z = 0.3 / se
chk("b1 z", z, 1.05)
chk("b1 p", norm.sf(z), 0.146)
chk("b1 lo", 6.3 - 1.96 * se, 5.74)
chk("b1 hi", 6.3 + 1.96 * se, 6.86)

# Exam 2
se = sqrt(18 ** 2 / 20 + 15 ** 2 / 25)
chk("b2 se", se, 5.0200, dp=4)
chk("b2 z", 10.6 / se, 2.11)
r = 2.3263 * sqrt(549) / 8
chk("b2 r", r, 6.8134, dp=4)
chk("b2 n", r * r, 46.4, dp=1)
assert 8 / sqrt(549 / 47) > norm.isf(0.01) > 8 / sqrt(549 / 46), "b2 n = 47"

# Exam 3
x = ss(60, 2052, 74610)
y = ss(75, 2370, 80180)
chk("b3 xbar", x[0], 34.2, dp=1)
chk("b3 sx2", x[1], 75.1)
chk("b3 sx2 3dp", x[1], 75.112, dp=3)
chk("b3 ybar", y[0], 31.6, dp=1)
chk("b3 sy2", y[1], 71.5)
chk("b3 sy2 3dp", y[1], 71.459, dp=3)
se = sqrt(x[1] / 60 + y[1] / 75)
chk("b3 var", se ** 2, 2.2047, dp=4)
chk("b3 se", se, 1.4848, dp=4)
chk("b3 z", 2.6 / se, 1.75)
chk("b3 lo", 2.6 - 1.6449 * se, 0.158)
chk("b3 hi", 2.6 + 1.6449 * se, 5.04)

# Exam 4
se = 1.5 / sqrt(12)
chk("b4 se", se, 0.43301, dp=5)
z = -0.9 / se
chk("b4 z", z, -2.08)
chk("b4 p", 2 * norm.cdf(z), 0.0377, dp=4)
chk("b4 lo", 19.1 - 2.3263 * se, 18.09, dp=2)
chk("b4 hi", 19.1 + 2.3263 * se, 20.11, dp=2)

print("\nFAILED:" if FAILS else "\nALL CHECKS PASSED", FAILS if FAILS else "")
raise SystemExit(1 if FAILS else 0)
