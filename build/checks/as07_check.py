"""Recomputes every number in content/as07.py (chi-squared goodness of fit) and asserts agreement."""
import json
import os

import numpy as np
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
TABLES = json.load(open(os.path.join(HERE, "..", "tables_cache.json")))
CHI2 = {int(r[0]): dict(zip(TABLES[3][1][1:], r[1:])) for r in TABLES[3][2]}
n_checks = 0


def close(value, stated, dp):
    """Assert value rounds to the stated number at dp decimal places."""
    global n_checks
    n_checks += 1
    assert abs(round(float(value), dp) - stated) < 1e-9, f"computed {value}, stated {stated} ({dp} dp)"


def sf3(value, stated):
    global n_checks
    n_checks += 1
    assert float(f"{value:.3g}") == stated, f"computed {value}, stated {stated} (3 s.f.)"


def cv(nu, level):
    """Critical value from the book's table, and check it against scipy."""
    s = CHI2[nu][{0.10: "0.1", 0.05: "0.05", 0.025: "0.025", 0.01: "0.01", 0.995: "0.995"}[level]]
    p = level if level < 0.5 else level
    exact = stats.chi2.isf(p, nu)
    assert abs(float(s) - exact) < 6e-4
    return float(s)


def x2(O, E):
    O, E = np.asarray(O, float), np.asarray(E, float)
    assert abs(O.sum() - E.sum()) < 1e-6, (O.sum(), E.sum())
    c = (O - E) ** 2 / E
    return c, c.sum()


# Notes table of critical values
for nu in range(1, 9):
    for lvl in (0.10, 0.05, 0.025, 0.01):
        cv(nu, lvl)
# formula equivalence X2 = sum O^2/E - N
O, E = np.array([12, 36, 42, 30.]), np.array([3, 5, 7, 4.])
E = E / E.sum() * O.sum()
assert abs(x2(O, E)[1] - ((O ** 2 / E).sum() - O.sum())) < 1e-9

# Example 1
c, X = x2([38, 22, 25, 27, 38], [30] * 5)
for v, s in zip(c, [2.133, 2.133, 0.833, 0.300, 2.133]):
    close(v, s, 3)
sf3(X, 7.53)
assert cv(4, 0.05) == 9.488 and X < 9.488

# Example 2
P = stats.binom.pmf(range(7), 6, 0.25)
for v, s in zip(P, [0.1780, 0.3560, 0.2966, 0.1318, 0.0330, 0.0044, 0.0002]):
    close(v, s, 4)
E = 120 * P
for v, s in zip(E, [21.36, 42.71, 35.60, 15.82, 3.96, 0.53, 0.03]):
    close(v, s, 2)
close(E[4:].sum(), 4.51, 2)
Ec = [E[0], E[1], E[2], E[3:].sum()]
close(Ec[3], 20.33, 2)
assert 19 + 8 + 2 + 1 == 30 and 12 + 36 + 42 + 19 + 8 + 2 + 1 == 120
c, X = x2([12, 36, 42, 30], Ec)
for v, s in zip(c, [4.100, 1.056, 1.152, 4.597]):
    close(v, s, 3)
sf3(X, 10.9)
assert X > cv(3, 0.05) == 7.815

# Example 3
obs = np.array([22, 25, 22, 14, 10, 5, 2]); x = np.arange(7); n = obs.sum()
assert n == 100 and (x * obs).sum() == 188 and (x * x * obs).sum() == 596
lam = 1.88
sf3(596 / 100 - lam ** 2, 2.43)
P = stats.poisson.pmf(range(5), lam)
close(P[0], 0.1526, 4)
E = n * P
for v, s in zip(E, [15.26, 28.69, 26.97, 16.90, 7.94]):
    close(v, s, 2)
close(n * (1 - P.sum()), 4.25, 2)
Ec = list(E[:4]) + [n * (1 - P[:4].sum())]
close(Ec[4], 12.19, 2)
c, X = x2([22, 25, 22, 14, 17], Ec)
for v, s in zip(c, [2.978, 0.474, 0.914, 0.497, 1.898]):
    close(v, s, 3)
sf3(X, 6.76)
assert X < cv(3, 0.05) and X > cv(3, 0.10) == 6.251

# Example 4
assert 34 + 28 + 36 + 40 + 20 + (6 + 6 + 7 + 7 + 8 + 8) == 200 and 34 + 14 + 12 + 10 + 4 + 6 == 80
p = 1 / 2.5
E = [80 * p * (1 - p) ** (k - 1) for k in range(1, 5)]
for v, s in zip(E, [32, 19.2, 11.52, 6.912]):
    close(v, s, 3)
close(80 * p * (1 - p) ** 4, 4.147, 3)
close((1 - p) ** 4, 0.1296, 4)
E.append(80 * (1 - p) ** 4)
close(E[4], 10.37, 2)
c, X = x2([34, 14, 12, 10, 10], E)
for v, s in zip(c, [0.125, 1.408, 0.020, 1.380, 0.013]):
    close(v, s, 3)
sf3(X, 2.95)
assert X < 7.815

# Example 5
b = [-np.inf, 90, 100, 110, 120, 130, np.inf]
P = np.diff(stats.norm.cdf(b, 110, 12))
close(stats.norm.cdf(-5 / 3), 0.0478, 4); close(stats.norm.cdf(-5 / 6), 0.2023, 4)
for v, s in zip(P[:3], [0.0478, 0.1545, 0.2977]):
    close(v, s, 4)
E = 200 * P
for v, s in zip(E, [9.56, 30.91, 59.53, 59.53, 30.91, 9.56]):
    close(v, s, 2)
c, X = x2([12, 26, 64, 55, 33, 10], E)
for v, s in zip(c, [0.624, 0.779, 0.335, 0.345, 0.142, 0.020]):
    close(v, s, 3)
sf3(X, 2.25)
assert X < 7.815

# Practice 1
E = 200 * stats.binom.pmf(range(5), 4, 0.3)
for v, s in zip(E, [48.02, 82.32, 52.92, 15.12, 1.62]):
    close(v, s, 2)
close(E[3] + E[4], 16.74, 2)
# Practice 3
c, X = x2([17, 21, 18, 19, 24, 21], [20] * 6); close(X, 1.6, 4); assert cv(5, 0.05) == 11.070
# Practice 4
c, X = x2([98, 30, 22, 10], [90, 30, 30, 10]); sf3(X, 2.84); assert X < 7.815
# Practice 5
c, X = x2([22, 95, 61, 22], [25, 75, 75, 25])
for v, s in zip(c, [0.36, 5.333, 2.613, 0.36]):
    close(v, s, 3)
sf3(X, 8.67); assert 7.815 < X < cv(3, 0.01) == 11.345
# Practice 6
assert abs(sum([2.4, 6.8, 12.5, 15.1, 9.7, 3.5]) - 50) < 1e-9 and sum([4, 5, 14, 13, 10, 4]) == 50
c, X = x2([9, 14, 13, 14], [9.2, 12.5, 15.1, 13.2])
for v, s in zip(c, [0.004, 0.180, 0.292, 0.048]):
    close(v, s, 3)
close(X, 0.525, 3); assert X < cv(2, 0.05) == 5.991
# Practice 7
P = stats.poisson.pmf(range(5), 2); E = list(120 * P) + [120 * (1 - P.sum())]
for v, s in zip(E, [16.24, 32.48, 32.48, 21.65, 10.83, 6.32]):
    close(v, s, 2)
c, X = x2([12, 30, 35, 24, 12, 7], E); sf3(X, 1.95); assert X < 11.070
# Practice 8
c, X = x2([18, 24, 30, 18, 10], [20] * 5)
for v, s in zip(c, [0.2, 0.8, 5.0, 0.2, 5.0]):
    close(v, s, 4)
close(X, 11.2, 4); close(stats.chi2.sf(11.2, 4), 0.0244, 4)
# Practice 9
assert cv(5, 0.05) < 13.9 < cv(5, 0.01) == 15.086
# Practice 10
E = [100 * 0.3 * 0.7 ** (k - 1) for k in range(1, 5)] + [100 * 0.7 ** 4]
for v, s in zip(E, [30, 21, 14.7, 10.29, 24.01]):
    close(v, s, 2)
# Practice 11
c, X = x2([12, 18, 11, 19, 14, 16], [15] * 6); sf3(X, 3.47); assert X < 11.070
# Practice 12
assert float(CHI2[5]["0.995"]) == 0.412 and abs(stats.chi2.ppf(0.005, 5) - 0.412) < 6e-4
assert stats.chi2.cdf(0.21, 5) < 0.005

# Exam 1
obs = np.array([10, 36, 38, 36, 15, 10, 5]); x = np.arange(7); n = obs.sum()
assert n == 150 and (x * obs).sum() == 360 and (x * x * obs).sum() == 1182
close(1182 / 150 - 2.4 ** 2, 2.12, 2); close((1182 - 150 * 2.4 ** 2) / 149, 2.13, 2)
P = stats.poisson.pmf(range(6), 2.4); E = list(n * P) + [n * (1 - P.sum())]
for v, s in zip(E, [13.61, 32.66, 39.19, 31.35, 18.81, 9.03, 5.35]):
    close(v, s, 2)
close(150 - (13.61 + 32.66 + 39.19 + 31.35 + 18.81 + 9.03), 5.35, 2)
c, X = x2(obs, E); sf3(X, 2.92); assert X < 11.070
# Exam 2
obs = np.array([2, 5, 17, 32, 30, 14]); assert obs.sum() == 100 and (np.arange(6) * obs).sum() == 325
P = stats.binom.pmf(range(6), 5, 0.65); E = 100 * P
for v, s in zip(E, [0.53, 4.88, 18.11, 33.64, 31.24, 11.60]):
    close(v, s, 2)
close(E[0] + E[1], 5.40, 2)
c, X = x2([7, 17, 32, 30, 14], [E[0] + E[1]] + list(E[2:]))
for v, s in zip(c, [0.473, 0.069, 0.080, 0.049, 0.495]):
    close(v, s, 3)
sf3(X, 1.17); assert X < 7.815 and cv(4, 0.05) == 9.488
# Exam 3
z = (np.array([0.2, 0.25, 0.3, 0.35]) - 0.27) / 0.05
for v, s in zip(z, [-1.4, -0.4, 0.6, 1.6]):
    close(v, s, 6)
for v, s in zip(stats.norm.cdf(z), [0.0808, 0.3446, 0.7257, 0.9452]):
    close(v, s, 4)
E = 100 * np.diff(stats.norm.cdf(np.r_[-np.inf, z, np.inf]))
for v, s in zip(E, [8.08, 26.38, 38.12, 21.95, 5.48]):
    close(v, s, 2)
c, X = x2([12, 30, 31, 19, 8], E)
for v, s in zip(c, [1.907, 0.496, 1.329, 0.395, 1.159]):
    close(v, s, 3)
sf3(X, 5.29); assert X < cv(3, 0.10) == 6.251
# Exam 4
from scipy.integrate import quad
k = 1 / quad(lambda t: t, 0, 4)[0]; close(k, 0.125, 6)
probs = [quad(lambda t: k * t, a, a + 1)[0] for a in range(4)]
for v, s in zip(probs, [1 / 16, 3 / 16, 5 / 16, 7 / 16]):
    close(v, s, 9)
c, X = x2([9, 17, 22, 32], [80 * q for q in probs])
for v, s in zip(c, [3.2, 0.267, 0.36, 0.257]):
    close(v, s, 3)
sf3(X, 4.08); assert X < 7.815
c, X = x2([9, 17, 22, 32], [20] * 4); close(X, 13.9, 4); assert X > 7.815

print(f"as07: all {n_checks} numerical checks passed")
