"""Recomputes every number in content/as09.py (correlation) and asserts agreement.

Critical values are read from tables_cache.json (Tables 18 and 19) and must match the strings quoted in the unit.
"""
import json
import os

import numpy as np
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
TABLES = json.load(open(os.path.join(HERE, "..", "tables_cache.json")))
PMCC = {int(r[0]): r[1:] for r in TABLES[17][2]}
SPEAR = {int(r[0]): r[1:] for r in TABLES[18][2]}
COL = {0.05: 0, 0.025: 1, 0.01: 2, 0.005: 3}  # one-tailed level -> column
n_checks = 0


def close(value, stated, dp):
    global n_checks
    n_checks += 1
    assert abs(round(float(value), dp) - stated) < 1e-9, f"computed {value}, stated {stated} ({dp} dp)"


def sf3(value, stated):
    global n_checks
    n_checks += 1
    assert float(f"{value:.3g}") == stated, f"computed {value}, stated {stated} (3 s.f.)"


def pmcc_cv(n, one_tail, stated):
    global n_checks
    n_checks += 1
    s = PMCC[n][COL[one_tail]]
    assert s == stated, (n, one_tail, s, stated)
    t = stats.t.isf(one_tail, n - 2)
    assert abs(t / np.sqrt(t * t + n - 2) - float(s)) < 5e-5
    return float(s)


def spear_cv(n, one_tail, stated):
    global n_checks
    n_checks += 1
    s = SPEAR[n][COL[one_tail]]
    assert s == stated, (n, one_tail, s, stated)
    return float(s) if s != "–" else None


def sums(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    n = len(x)
    Sxx = (x * x).sum() - x.sum() ** 2 / n
    Syy = (y * y).sum() - y.sum() ** 2 / n
    Sxy = (x * y).sum() - x.sum() * y.sum() / n
    r = Sxy / np.sqrt(Sxx * Syy)
    assert abs(r - stats.pearsonr(x, y)[0]) < 1e-12
    return Sxx, Syy, Sxy, r


def spearman_formula(rx, ry):
    d = np.asarray(rx, float) - np.asarray(ry, float)
    n = len(d)
    assert abs(d.sum()) < 1e-12
    return (d * d).sum(), 1 - 6 * (d * d).sum() / (n * (n * n - 1))


# Notes tables: every value quoted must equal Table 18 / Table 19 exactly
pmcc_rows = {5: ["0.8054", "0.8783", "0.9343", "0.9587"], 6: ["0.7293", "0.8114", "0.8822", "0.9172"],
             7: ["0.6694", "0.7545", "0.8329", "0.8745"], 8: ["0.6215", "0.7067", "0.7887", "0.8343"],
             9: ["0.5822", "0.6664", "0.7498", "0.7977"], 10: ["0.5494", "0.6319", "0.7155", "0.7646"],
             12: ["0.4973", "0.5760", "0.6581", "0.7079"], 15: ["0.4409", "0.5140", "0.5923", "0.6411"],
             20: ["0.3783", "0.4438", "0.5155", "0.5614"], 25: ["0.3365", "0.3961", "0.4622", "0.5052"],
             30: ["0.3061", "0.3610", "0.4226", "0.4629"]}
for n, row in pmcc_rows.items():
    for lvl, s in zip((0.05, 0.025, 0.01, 0.005), row):
        pmcc_cv(n, lvl, s)
spear_rows = {5: ["0.9000", "1.0000", "1.0000", "–"], 6: ["0.8286", "0.8857", "0.9429", "1.0000"],
              7: ["0.7143", "0.7857", "0.8929", "0.9286"], 8: ["0.6429", "0.7381", "0.8333", "0.8810"],
              9: ["0.6000", "0.7000", "0.7833", "0.8333"], 10: ["0.5636", "0.6485", "0.7455", "0.7939"]}
for n, row in spear_rows.items():
    for lvl, s in zip((0.05, 0.025, 0.01, 0.005), row):
        spear_cv(n, lvl, s)
# coding identities
rng = np.random.default_rng(1)
x, y = rng.normal(size=12), rng.normal(size=12)
a, b, c, d = 3.0, 2.5, -1.0, 4.0
Sxx, Syy, Sxy, r = sums(x, y); Suu, Svv, Suv, ruv = sums((x - a) / b, (y - c) / d)
assert np.isclose(Sxx, b * b * Suu) and np.isclose(Syy, d * d * Svv) and np.isclose(Sxy, b * d * Suv) and np.isclose(r, ruv)
assert np.isclose(sums((x - a) / b, (c - y) / d)[3], -r)

# Example 1
x = [2, 4, 5, 6, 8, 9, 11, 13]; y = [35, 42, 50, 46, 58, 60, 65, 72]
assert (sum(x), sum(y), sum(v * v for v in x), sum(v * v for v in y), sum(p * q for p, q in zip(x, y))) == (58, 428, 516, 23978, 3419)
Sxx, Syy, Sxy, r = sums(x, y)
close(Sxx, 95.5, 6); close(Syy, 1080, 6); close(Sxy, 316, 6); sf3(r, 0.984)
assert r > pmcc_cv(8, 0.01, "0.7887")
# Example 2
n = 10; Suu = 165 - 25 ** 2 / n; Svv = 230 - 40 ** 2 / n; Suv = 40 - 25 * 40 / n
close(Suu, 102.5, 6); close(Svv, 70, 6); close(Suv, -60, 6)
r = Suv / np.sqrt(Suu * Svv); sf3(r, -0.708)
close(100 * Svv, 7000, 6); close(10 * Suv, -600, 6); sf3(-600 / np.sqrt(102.5 * 7000), -0.708)
assert r < -pmcc_cv(10, 0.05, "0.5494") and r > -pmcc_cv(10, 0.01, "0.7155")
# Example 3
D, rs = spearman_formula(range(1, 9), [2, 1, 4, 3, 6, 8, 5, 7]); close(D, 14, 6); sf3(rs, 0.833)
close(stats.spearmanr(range(1, 9), [2, 1, 4, 3, 6, 8, 5, 7])[0], rs, 9)
assert rs > spear_cv(8, 0.025, "0.7381")
# Example 4
x = [12, 15, 15, 18, 20, 22, 22, 22]; y = [30, 28, 35, 40, 38, 45, 50, 42]
rx, ry = stats.rankdata(x), stats.rankdata(y)
assert list(rx) == [1, 2.5, 2.5, 4, 5, 7, 7, 7] and list(ry) == [2, 1, 3, 5, 4, 7, 8, 6]
Sxx, Syy, Sxy, rs = sums(rx, ry); close(Sxx, 39.5, 6); close(Syy, 42, 6); close(Sxy, 37, 6); sf3(rs, 0.908)
close(stats.spearmanr(x, y)[0], rs, 9)
D, rf = spearman_formula(rx, ry); close(D, 7.5, 6); sf3(rf, 0.911)
assert rs > spear_cv(8, 0.05, "0.6429")
# Example 5
r = 162 / np.sqrt(420 * 310); sf3(r, 0.449); assert r < pmcc_cv(12, 0.025, "0.5760")

# Practice 1
Sxx, Syy, Sxy = 310 - 50 ** 2 / 10, 700 - 80 ** 2 / 10, 440 - 50 * 80 / 10
close(Sxx, 60, 6); close(Syy, 60, 6); close(Sxy, 40, 6); sf3(Sxy / np.sqrt(Sxx * Syy), 0.667)
# Practice 2
Sxx, Syy, Sxy, r = sums(range(1, 7), [2, 1, 4, 3, 6, 5]); close(Sxx, 17.5, 6); close(Sxy, 14.5, 6); sf3(r, 0.829)
assert r > pmcc_cv(6, 0.025, "0.8114")
# Practice 3
xs = rng.normal(size=8); ys = xs + rng.normal(size=8)
assert np.isclose(sums((xs - 50) / 2, (100 - ys) / 4)[3], -sums(xs, ys)[3])
# Practice 4
d = np.array([1, -2, 0, 2, -1]); close((d * d).sum(), 10, 6); close(1 - 6 * 10 / (5 * 24), 0.5, 6)
# Practice 5
assert -0.6 < -pmcc_cv(10, 0.05, "0.5494")
# Practice 6
x = [3.1, 4.5, 2.8, 5.0, 3.9, 4.1, 2.2]; y = [12, 15, 14, 18, 11, 16, 9]
assert list(stats.rankdata(x)) == [3, 6, 2, 7, 4, 5, 1] and list(stats.rankdata(y)) == [3, 5, 4, 7, 2, 6, 1]
D, rs = spearman_formula(stats.rankdata(x), stats.rankdata(y)); close(D, 10, 6); sf3(rs, 0.821)
assert rs > spear_cv(7, 0.05, "0.7143")
# Practice 7
assert list(stats.rankdata([7, 9, 9, 12, 15, 15, 15, 20])) == [1, 2.5, 2.5, 4, 6, 6, 6, 8]
assert (stats.rankdata([7, 9, 9, 12, 15, 15, 15, 20]) ** 2).sum() < 8 * 9 * 17 / 6
# Practice 10
Sxx, Syy, Sxy, r = sums([1, 2, 3, 4, 5], [1, 4, 9, 16, 25]); close(Sxx, 10, 6); close(Syy, 374, 6); close(Sxy, 60, 6)
sf3(r, 0.981); close(stats.spearmanr([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])[0], 1, 9)
# Practice 11
assert 0.45 > pmcc_cv(20, 0.025, "0.4438")
assert 0.2 > float(PMCC[100][1]) and PMCC[100][1] == "0.1966"
# Practice 12
assert pmcc_cv(11, 0.05, "0.5214") > 0.5 > pmcc_cv(12, 0.05, "0.4973")

# Exam 1
Suu, Svv, Suv = 478 - 62 ** 2 / 10, 571 - 55 ** 2 / 10, 232 - 62 * 55 / 10
close(Suu, 93.6, 6); close(Svv, 268.5, 6); close(Suv, -109, 6)
r = Suv / np.sqrt(Suu * Svv); sf3(r, -0.688); assert r < -pmcc_cv(10, 0.05, "0.5494")
assert Suv ** 2 <= Suu * Svv  # summary statistics are consistent
# Exam 2
qb = [3, 1, 2, 5, 4, 7, 9, 6, 8]
D, rs = spearman_formula(range(1, 10), qb); close(D, 18, 6); close(rs, 0.85, 6)
assert list(np.arange(1, 10) - np.array(qb)) == [-2, 1, 1, -1, 1, -1, -2, 2, 1]
assert rs > spear_cv(9, 0.01, "0.7833")
# Exam 3
r = 412 / np.sqrt(1250 * 880); sf3(r, 0.393); assert r < pmcc_cv(25, 0.025, "0.3961")
# Exam 4
x = list(range(1, 9)); y = [2, 3, 5, 4, 14, 25, 46, 90]
assert list(stats.rankdata(y)) == [1, 2, 4, 3, 5, 6, 7, 8]
D, rs = spearman_formula(x, stats.rankdata(y)); close(D, 2, 6); sf3(rs, 0.976)
assert rs > spear_cv(8, 0.01, "0.8333")
Sxx, Syy, Sxy, r = sums(x, y); close(Sxx, 42, 6); close(Syy, 6625.875, 6); close(Sxy, 450.5, 6); sf3(r, 0.854)

print(f"as09: all {n_checks} numerical checks passed")
