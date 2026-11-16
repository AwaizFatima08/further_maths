"""Recomputes every number in content/as10.py (regression) and asserts agreement."""
import numpy as np
from scipy import stats

n_checks = 0


def close(value, stated, dp):
    global n_checks
    n_checks += 1
    assert abs(round(float(value), dp) - stated) < 1e-9, f"computed {value}, stated {stated} ({dp} dp)"


def sf3(value, stated):
    global n_checks
    n_checks += 1
    assert float(f"{value:.3g}") == stated, f"computed {value}, stated {stated} (3 s.f.)"


def reg(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    n = len(x)
    Sxx = (x * x).sum() - x.sum() ** 2 / n
    Syy = (y * y).sum() - y.sum() ** 2 / n
    Sxy = (x * y).sum() - x.sum() * y.sum() / n
    b = Sxy / Sxx
    a = y.mean() - b * x.mean()
    lr = stats.linregress(x, y)
    assert abs(lr.slope - b) < 1e-10 and abs(lr.intercept - a) < 1e-10
    e = y - (a + b * x)
    assert abs(e.sum()) < 1e-9
    assert abs((e * e).sum() - (Syy - Sxy ** 2 / Sxx)) < 1e-9          # RSS formula
    r = Sxy / np.sqrt(Sxx * Syy)
    assert abs((e * e).sum() - Syy * (1 - r * r)) < 1e-9                # RSS = Syy(1 - r^2)
    return dict(Sxx=Sxx, Syy=Syy, Sxy=Sxy, a=a, b=b, e=e, r=r, RSS=(e * e).sum(), xbar=x.mean(), ybar=y.mean())


# Example 1
x = [10, 15, 20, 25, 30, 35, 40]; y = [12.1, 14.8, 17.2, 19.9, 21.5, 25.0, 26.9]
close(sum(y), 137.4, 6); close(sum(p * q for p, q in zip(x, y)), 3780.5, 6); assert sum(v * v for v in x) == 5075
R = reg(x, y)
close(R["Sxx"], 700, 6); close(R["Sxy"], 345.5, 6); close(R["b"], 0.4936, 4); close(R["ybar"], 19.629, 3)
close(R["a"], 7.289, 3); sf3(R["a"], 7.29); sf3(R["b"], 0.494)
sf3(R["a"] + R["b"] * 28, 21.1); sf3(7.29 + 0.494 * 28, 21.1)
sf3(R["a"] + R["b"] * 60, 36.9); sf3(7.29 + 0.494 * 60, 36.9); sf3(R["r"], 0.998)
# Example 2
Suu = 140 - 28 ** 2 / 8; Suv = 158 - 28 * 36 / 8; Svv = 200 - 36 ** 2 / 8
close(Suu, 42, 9); close(Suv, 32, 9); close(Svv, 38, 9)
d = Suv / Suu; c = 4.5 - d * 3.5; close(d, 0.7619, 4); close(c, 1.833, 3)
B = 4 / 5 * d; A = 100 + 4 * c - B * 20
close(B, 0.6095, 4); close(4 * c, 7.333, 3); close(B * 20, 12.190, 3); sf3(A, 95.1); sf3(B, 0.610)
close(A + B * 37.5, 118, 9)
sf3(Suv / np.sqrt(Suu * Svv), 0.801)
# brute-force check of the coding rule with random data
rng = np.random.default_rng(3)
xs = rng.uniform(20, 60, 8); ys = 100 + 0.6 * xs + rng.normal(0, 2, 8)
R1 = reg(xs, ys); R2 = reg((xs - 20) / 5, (ys - 100) / 4)
assert np.isclose(R1["b"], 4 / 5 * R2["b"]) and np.isclose(R1["a"], 100 + 4 * R2["a"] - 4 / 5 * R2["b"] * 20)
# Example 3
x = list(range(1, 9)); y = [3.1, 4.9, 7.2, 8.8, 15.0, 13.1, 15.2, 16.8]
close(sum(y), 84.1, 6); close(sum(v * v for v in y), 1072.79, 6); close(sum(p * q for p, q in zip(x, y)), 464.1, 6)
R = reg(x, y)
close(R["Sxx"], 42, 9); close(R["Sxy"], 85.65, 6); close(R["Syy"], 188.69, 2)
close(R["b"], 2.039, 3); close(R["a"], 1.336, 3); sf3(R["a"], 1.34); sf3(R["b"], 2.04)
for v, s in zip(R["e"], [-0.275, -0.514, -0.254, -0.693, 3.468, -0.471, -0.411, -0.850]):
    close(v, s, 3)
sf3(R["RSS"], 14.0); sf3(R["e"][4] ** 2, 12.0)
R = reg(x[:4] + x[5:], y[:4] + y[5:]); sf3(R["a"], 1.05); sf3(R["b"], 1.99); sf3(R["RSS"], 0.186)
# Example 4
by = 1500 / 1600; bx = 1500 / 2500
close(by, 0.9375, 9); close(55 - by * 60, -1.25, 9); close(bx, 0.6, 9); close(60 - bx * 55, 27, 9)
sf3(-1.25 + by * 70, 64.4); close(27 + 0.6 * 40, 51, 9); sf3((40 + 1.25) / by, 44.0)
r = 1500 / np.sqrt(1600 * 2500); close(r, 0.75, 9); close(by * bx, 0.5625, 9); close(r * r, 0.5625, 9)
# Example 5
Sxx = 2700 - 150 ** 2 / 10; Sxy = 6000 - 150 * 360 / 10; Syy = 14200 - 360 ** 2 / 10
close(Sxx, 450, 9); close(Sxy, 600, 9); close(Syy, 1240, 9)
b = Sxy / Sxx; a = 36 - b * 15; close(b, 1.333, 3); close(a, 16, 9)
close(a + b * 20, 42.67, 2); close(38 - (a + b * 20), -4.67, 2)
RSS = Syy - Sxy ** 2 / Sxx; close(RSS, 440, 9)
r = Sxy / np.sqrt(Sxx * Syy); sf3(r, 0.803); close(Syy * (1 - r * r), 440, 9); close(Sxx * Syy, 558000, 9)
assert Sxy ** 2 <= Sxx * Syy

# Practice 1
R = reg([2, 4, 6, 8], [3, 5, 8, 9]); close(R["Sxy"], 21, 9); close(R["Sxx"], 20, 9); close(R["b"], 1.05, 9); close(R["a"], 1, 9)
# Practice 2
close(-80 / 40, -2, 9); close(20 - (-2) * 4, 28, 9)
# Practice 3
close(0.9 * 5 / 2, 2.25, 9)
# Practice 4
close(5 - (1 + 1.05 * 4), -0.2, 9)
# Practice 7
assert np.isclose(50 + 2 * 2.5 - 2 * 0.08 * 100, 39) and np.isclose(2 * 0.8 / 10, 0.16)
# Practice 8
close(250 - 120 ** 2 / 80, 70, 9); close(120 ** 2 / (80 * 250), 0.72, 9); close(250 * 0.28, 70, 9)
# Practice 11
close(150 / 200, 0.75, 9); close(12 - 0.75 * 30, -10.5, 9); close(-10.5 + 0.75 * 34, 15, 9)

# Exam 1
x = [4, 6, 8, 10, 12, 14, 14, 16]; y = [52, 60, 63, 71, 75, 82, 79, 88]
assert (sum(x), sum(y), sum(v * v for v in x), sum(v * v for v in y), sum(p * q for p, q in zip(x, y))) == (84, 570, 1008, 41648, 6344)
R = reg(x, y)
close(R["Sxx"], 126, 9); close(R["Syy"], 1035.5, 9); close(R["Sxy"], 359, 9)
close(R["b"], 2.849, 3); close(R["a"], 41.33, 2); sf3(R["a"], 41.3); sf3(R["b"], 2.85)
close(R["a"] + R["b"] * 14, 81.22, 2); close(R["e"][6], -2.22, 2)
sf3(R["RSS"], 12.6); sf3(R["a"] + R["b"] * 9, 67.0); sf3(R["r"], 0.994)
# Exam 2
Suu = 60 - 18 ** 2 / 9; Suv = 72 - 18 * 45 / 9; close(Suu, 24, 9); close(Suv, -18, 9)
d = Suv / Suu; c = 5 - d * 2; close(d, -0.75, 9); close(c, 6.5, 9)
B = 10 * d / 100; A = 10 * c - B * 1500; close(B, -0.075, 9); close(A, 177.5, 9)
close(A + B * 1800, 42.5, 9); close(A + B * 3500, -85, 9); close(1500 + 100 * 2, 1700, 9)
# Exam 3
by = 330 / 480; bx = 330 / 520; xbar, ybar = 2100 / 12, 2124 / 12
close(xbar, 175, 9); close(ybar, 177, 9); close(by, 0.6875, 9); close(bx, 0.6346, 4)
sf3(ybar - by * xbar, 56.7); sf3(xbar - bx * ybar, 62.7); sf3(bx, 0.635); sf3(by, 0.688)
sf3(ybar + by * (185 - xbar), 184); sf3(xbar + bx * (170 - ybar), 171)
sf3(330 / np.sqrt(480 * 520), 0.661)
# Exam 4
x = list(range(1, 8)); y = [2.0, 3.1, 4.4, 5.1, 9.0, 7.2, 8.1]
close(sum(y), 38.9, 6); close(sum(v * v for v in y), 257.43, 6); close(sum(p * q for p, q in zip(x, y)), 186.7, 6)
R = reg(x, y)
close(R["Sxx"], 28, 9); close(R["Sxy"], 31.1, 6); close(R["b"], 1.111, 3); close(R["a"], 1.114, 3); close(R["ybar"], 5.557, 3)
sf3(R["a"], 1.11); sf3(R["b"], 1.11)
for i, s in zip([0, 2, 3, 5, 6], [-0.225, -0.046, -0.457, -0.579, -0.789]):
    close(R["e"][i], s, 3)
close(R["a"] + R["b"] * 2, 3.336, 3); close(R["e"][1], -0.236, 3)
close(R["a"] + R["b"] * 5, 6.668, 3); close(R["e"][4], 2.332, 3)
close(R["Syy"], 41.257, 3); sf3(R["RSS"], 6.71)
R = reg(x[:4] + x[5:], y[:4] + y[5:]); sf3(R["a"], 1.11); sf3(R["b"], 1.01); close(R["RSS"], 0.0927, 4)
close(R["a"], 1.114, 3); close(R["b"], 1.009, 3); sf3(R["a"] + R["b"] * 5, 6.16)

print(f"as10: all {n_checks} numerical checks passed")
