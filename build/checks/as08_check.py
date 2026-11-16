"""Recomputes every number in content/as08.py (contingency tables) and asserts agreement."""
import json
import os

import numpy as np
from scipy import stats
from scipy.stats import chi2_contingency

HERE = os.path.dirname(os.path.abspath(__file__))
TABLES = json.load(open(os.path.join(HERE, "..", "tables_cache.json")))
CHI2 = {int(r[0]): dict(zip(TABLES[3][1][1:], r[1:])) for r in TABLES[3][2]}
n_checks = 0


def close(value, stated, dp):
    global n_checks
    n_checks += 1
    assert abs(round(float(value), dp) - stated) < 1e-9, f"computed {value}, stated {stated} ({dp} dp)"


def sf3(value, stated):
    global n_checks
    n_checks += 1
    assert float(f"{value:.3g}") == stated, f"computed {value}, stated {stated} (3 s.f.)"


def cv(nu, key):
    v = float(CHI2[nu][key])
    assert abs(v - stats.chi2.isf(float(key), nu)) < 6e-4
    return v


def table(O, yates=False):
    O = np.asarray(O, float)
    E = np.outer(O.sum(1), O.sum(0)) / O.sum()
    c = ((np.abs(O - E) - 0.5) ** 2 if yates else (O - E) ** 2) / E
    nu = (O.shape[0] - 1) * (O.shape[1] - 1)
    # cross-check with scipy's own routine
    X_sp, _, nu_sp, E_sp = chi2_contingency(O, correction=yates)
    assert abs(X_sp - c.sum()) < 1e-9 and nu_sp == nu and np.allclose(E_sp, E)
    return E, c, c.sum(), nu


def all_close(values, stated, dp):
    values = np.ravel(values)
    assert len(values) == len(stated)
    for v, s in zip(values, stated):
        close(v, s, dp)


# Notes table of critical values
for nu, a, b in [(1, 3.841, 6.635), (2, 5.991, 9.210), (3, 7.815, 11.345), (4, 9.488, 13.277), (6, 12.592, 16.812),
                 (9, 16.919, 21.666)]:
    assert cv(nu, "0.05") == a and cv(nu, "0.01") == b

# Example 1
E, c, X, nu = table([[30, 20], [20, 30]]); assert np.allclose(E, 25); close(X, 4, 6); assert X > cv(1, "0.05")
E, c, X, nu = table([[30, 20], [20, 30]], True); close(X, 3.24, 6); assert X < 3.841
# Example 2
E, c, X, nu = table([[20, 25, 15], [30, 15, 25]])
all_close(E, [23.08, 18.46, 18.46, 26.92, 21.54, 21.54], 2)
all_close(c, [0.410, 2.316, 0.649, 0.352, 1.985, 0.556], 3)
sf3(X, 6.27); assert nu == 2 and X > 5.991
# Example 3
O = np.array([[20, 45, 2], [30, 35, 4], [40, 15, 6]])
assert O.sum() == 197 and list(O.sum(1)) == [67, 69, 61] and list(O.sum(0)) == [90, 95, 12]
E, c, X, nu = table(O)
all_close(E[:, 2], [4.08, 4.20, 3.72], 2)
assert (E[:, 2] < 5).all()
E, c, X, nu = table([[22, 45], [34, 35], [46, 15]])
all_close(E, [34.69, 32.31, 35.73, 33.27, 31.58, 29.42], 2)
all_close(c, [4.642, 4.984, 0.083, 0.090, 6.580, 7.065], 3)
sf3(X, 23.4); assert nu == 2 and X > cv(2, "0.01") == 9.210
# Example 4
E, c, X, nu = table([[30, 25, 35, 10], [35, 15, 40, 10], [15, 10, 45, 30]])
all_close(E[0], [26.67, 16.67, 40.00, 16.67], 2)
all_close(c, [0.417, 4.167, 0.625, 2.667, 2.604, 0.167, 0.000, 2.667, 5.104, 2.667, 0.625, 10.667], 3)
sf3(X, 32.4); assert nu == 6 and X > 12.592
# Example 5
E, c, X, nu = table([[28, 14, 3], [18, 22, 5]]); all_close(E[:, 2], [4.0, 4.0], 6)
E, c, X, nu = table([[28, 17], [18, 27]]); all_close(E, [23, 22, 23, 22], 6); assert np.allclose(np.abs([[28, 17], [18, 27]] - E), 5)
sf3(X, 4.45); assert X > 3.841
E, c, X, nu = table([[28, 17], [18, 27]], True); sf3(X, 3.60); assert X < 3.841

# Practice 1
E, c, X, nu = table([[12, 18, 10], [28, 22, 30]])
all_close(E, [13.33] * 3 + [26.67] * 3, 2); all_close(c, [0.133, 1.633, 0.833, 0.067, 0.817, 0.417], 3)
close(X, 3.90, 2); assert X < 5.991
# Practice 3
E, c, X, nu = table([[40, 10], [30, 20]]); all_close(E, [35, 15, 35, 15], 6); sf3(X, 4.76); assert X > 3.841
E, c, X, nu = table([[40, 10], [30, 20]], True); sf3(X, 3.86); assert X > 3.841
# Practice 4
E, c, X, nu = table([[50, 30, 20], [10, 40, 30]])
all_close(E, [33.33, 38.89, 27.78, 26.67, 31.11, 22.22], 2)
all_close(c, [8.333, 2.032, 2.178, 10.417, 2.540, 2.722], 3)
sf3(X, 28.2)
# Practice 7
X = sum([0.42, 3.10, 1.25, 0.08, 0.95, 0.31, 2.60, 0.07, 4.45]); close(X, 13.23, 2); assert X > cv(4, "0.05") == 9.488
# Practice 8
assert cv(2, "0.05") == 5.991
# Practice 9
assert 0.01 < 0.031 < 0.05
# Practice 10
E, c, X, nu = table([[12, 8], [6, 14]]); all_close(E, [9, 11, 9, 11], 6); sf3(X, 3.64)
E, c, X2, nu = table([[12, 8], [6, 14]], True); sf3(X2, 2.53); assert max(X, X2) < 3.841
close(2.5 ** 2 * (2 / 9 + 2 / 11), 2.53, 2)
# Practice 12
E, *_ = table([[12, 28], [18, 42]]); all_close(E, [12, 28, 18, 42], 6)

# Exam 1
E, c, X, nu = table([[40, 25, 15], [30, 20, 20], [10, 15, 25]])
all_close(E, [32, 24, 24, 28, 21, 21, 20, 15, 15], 6)
all_close(c, [2.000, 0.042, 3.375, 0.143, 0.048, 0.048, 5.000, 0.000, 6.667], 3)
sf3(X, 17.3); assert nu == 4 and X > cv(4, "0.01") == 13.277
# Exam 2
E, c, X, nu = table([[18, 42], [22, 118]]); all_close(E, [12, 48, 28, 112], 6); sf3(X, 5.36)
E, c, XY, nu = table([[18, 42], [22, 118]], True)
all_close(c, [2.521, 0.630, 1.080, 0.270], 3); sf3(XY, 4.50)
assert XY < cv(1, "0.025") == 5.024 < X
# Exam 3
O = np.array([[45, 10, 2], [50, 12, 3], [40, 15, 4], [25, 18, 6]])
E, c, X, nu = table(O); all_close(E[:, 2], [3.72, 4.24, 3.85, 3.20], 2); assert (E[:, 2] < 5).all()
close(X, 12.50, 2); assert nu == 6 and X < 12.592
E, c, X, nu = table([[45, 12], [50, 15], [40, 19], [25, 24]])
all_close(E[:, 0], [39.65, 45.22, 41.04, 34.09], 2); all_close(E[:, 1], [17.35, 19.78, 17.96, 14.91], 2)
all_close(c, [0.721, 1.649, 0.506, 1.156, 0.027, 0.061, 2.422, 5.537], 3)
sf3(X, 12.1); assert nu == 3 and X > 7.815
# Exam 4
E, c, X, nu = table([[30, 25, 15, 10], [20, 25, 30, 25]])
all_close(E, [22.22, 22.22, 20.00, 15.56, 27.78, 27.78, 25.00, 19.44], 2)
all_close(c, [2.722, 0.347, 1.250, 1.984, 2.178, 0.278, 1.000, 1.587], 3)
close(X, 11.35, 2); assert nu == 3
p = stats.chi2.sf(X, nu); close(p, 0.00999, 5); assert p < 0.01

print(f"as08: all {n_checks} numerical checks passed")
