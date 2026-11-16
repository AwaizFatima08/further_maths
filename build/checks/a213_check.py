"""Checks every number in content/a213.py (Wilcoxon tests). Run with the scipy venv python.
Exact null distributions are computed by enumeration; critical values are read from tables_cache.json."""
import json
import math
from itertools import combinations
from pathlib import Path

from scipy.stats import binom, norm, rankdata

ROOT = Path(__file__).resolve().parents[1]
TABLES = json.loads((ROOT / "tables_cache.json").read_text())
SR = {int(r[0]): [int(v) if v.isdigit() else None for v in r[1:]] for r in TABLES[19][2]}   # 5, 2.5, 1, 0.5 % one-tail
RS5 = {int(r[0]): r[1:] for r in TABLES[20][2]}
RS25 = {int(r[0]): r[1:] for r in TABLES[21][2]}
assert "signed-rank" in TABLES[19][0] and "5% one-tailed" in TABLES[20][0] and "2.5% one-tailed" in TABLES[21][0]
COL = {0.05: 0, 0.025: 1, 0.01: 2, 0.005: 3}


def r4(x):
    return round(float(x), 4)


def r3(x):
    return round(float(x), 3)


def sr_counts(n):
    """Number of sign patterns giving each value of P (exact null distribution)."""
    dist = [1] + [0] * (n * (n + 1) // 2)
    for k in range(1, n + 1):
        new = dist[:]
        for s in range(k, len(dist)):
            new[s] += dist[s - k]
        dist = new
    return dist


def sr_cdf(n, t):
    return sum(sr_counts(n)[: t + 1]) / 2 ** n


def sr_crit(n, alpha):
    c = [t for t in range(n * (n + 1) // 2 + 1) if sr_cdf(n, t) <= alpha]
    return max(c) if c else None


def rs_cdf(m, n, w):
    N = m + n
    count = sum(1 for c in combinations(range(1, N + 1), m) if sum(c) <= w) if math.comb(N, m) < 3_000_000 else None
    if count is None:  # dynamic programming for larger cases
        maxs = sum(range(N - m + 1, N + 1))
        dp = [[0] * (maxs + 1) for _ in range(m + 1)]
        dp[0][0] = 1
        for r in range(1, N + 1):
            for k in range(min(r, m), 0, -1):
                for s in range(maxs, r - 1, -1):
                    dp[k][s] += dp[k - 1][s - r]
        count = sum(dp[m][: w + 1])
    return count / math.comb(N, m)


def rs_table(m, n, alpha):
    tab = RS5 if alpha == 0.05 else RS25
    return int(tab[m][n - 3])


def signed(values, m0=0.0, other=None):
    d = [round(a - b, 6) for a, b in zip(values, other)] if other else [round(x - m0, 6) for x in values]
    d = [x for x in d if x != 0]
    ab = [abs(x) for x in d]
    assert len(set(ab)) == len(ab), "tied |d|"
    rk = rankdata(ab)
    P = int(sum(r for r, x in zip(rk, d) if x > 0))
    Q = int(sum(r for r, x in zip(rk, d) if x < 0))
    n = len(d)
    assert P + Q == n * (n + 1) // 2
    return n, P, Q, {x: int(r) for x, r in zip(d, rk)}


def ranksum(a, b):
    allv = a + b
    assert len(set(allv)) == len(allv), "tie"
    rk = rankdata(allv)
    R = int(sum(rk[: len(a)]))
    m, n = len(a), len(b)
    return R, m * (m + n + 1) - R


def z_sr(t, n):
    return (t + 0.5 - n * (n + 1) / 4) / math.sqrt(n * (n + 1) * (2 * n + 1) / 24)


def z_rs(w, m, n):
    return (w + 0.5 - m * (m + n + 1) / 2) / math.sqrt(m * n * (m + n + 1) / 12)


# ---- Tables agree with exact enumeration (spot checks used in the unit)
for n in range(5, 31):
    for a, j in COL.items():
        assert SR[n][j] == sr_crit(n, a), (n, a)
for m, n, a in [(3, 3, 0.05), (3, 4, 0.05), (4, 6, 0.05), (5, 6, 0.025), (5, 6, 0.05), (6, 8, 0.05), (6, 8, 0.025), (5, 7, 0.05)]:
    w = max(w for w in range(200) if rs_cdf(m, n, w) <= a)
    assert w == rs_table(m, n, a), (m, n, a)

# ---- Notes
assert sr_counts(4) == [1, 1, 1, 2, 2, 2, 2, 2, 1, 1, 1]
assert sr_cdf(4, 0) == 1 / 16 == 0.0625 and sr_cdf(5, 0) == 1 / 32 == 0.03125 and SR[5][0] == 0
assert sr_cdf(6, 2) == 3 / 64 and r4(3 / 64) == 0.0469 and sr_cdf(6, 3) == 5 / 64 and r4(5 / 64) == 0.0781
assert SR[6][0] == 2
assert rs_cdf(3, 3, 6) == 0.05 and rs_cdf(3, 3, 7) == 0.1 and rs_table(3, 3, 0.05) == 6
assert math.comb(6, 3) == 20

# ---- Worked example 1
n, P, Q, rk = signed([47.2, 51.3, 44.8, 49.5, 46.1, 52.7, 43.9, 48.6, 45.4, 50.8], 50)
assert (n, P, Q) == (10, 10, 45) and SR[10][0] == 10 and r4(sr_cdf(10, 10)) == 0.0420
assert rk == {-0.5: 1, 0.8: 2, 1.3: 3, -1.4: 4, 2.7: 5, -2.8: 6, -3.9: 7, -4.6: 8, -5.2: 9, -6.1: 10}

# ---- Worked example 2
ph = [6.82, 6.31, 7.14, 6.50, 6.93, 7.38, 6.44, 7.05, 6.71, 6.97, 6.16, 7.22, 6.59]
n, P, Q, rk = signed(ph, 6.5)
assert (n, P, Q) == (12, 68, 10) and SR[12][1] == 13 and r4(2 * sr_cdf(12, 10)) == 0.0210
assert [rk[x] for x in (-0.06, 0.09, -0.19, 0.21, 0.32, -0.34)] == [1, 2, 3, 4, 5, 6]
plus = sum(x > 6.5 for x in ph); minus = sum(x < 6.5 for x in ph)
assert (plus, minus) == (9, 3) and r4(binom.cdf(3, 12, 0.5)) == 0.0730 and r4(2 * binom.cdf(3, 12, 0.5)) == 0.1460

# ---- Worked example 3
old = [1534, 1612, 1488, 1570, 1655, 1502, 1590, 1547, 1621]
new = [1522, 1617, 1470, 1563, 1633, 1511, 1575, 1544, 1610]
assert [a - b for a, b in zip(old, new)] == [12, -5, 18, 7, 22, -9, 15, 3, 11]
n, P, Q, _ = signed(old, other=new)
assert (n, P, Q) == (9, 39, 6) and SR[9][0] == 8 and SR[9][1] == 5 and r4(sr_cdf(9, 6)) == 0.0273

# ---- Worked example 4
A = [23.1, 19.8, 21.4, 18.6, 24.0, 20.5]
B = [25.3, 22.7, 26.8, 21.9, 27.4, 24.6, 23.8, 28.1]
R, C = ranksum(A, B)
assert (R, C) == (26, 64) and rs_table(6, 8, 0.05) == 31 and r4(rs_cdf(6, 8, 26)) == 0.0063

# ---- Worked example 5
n = 32
assert n * (n + 1) // 2 - 158 == 370 and n * (n + 1) / 4 == 264 and n * (n + 1) * (2 * n + 1) / 24 == 2860
assert round(math.sqrt(2860), 2) == 53.48
z = z_sr(158, 32)
assert r3(z) == -1.973 and z < -1.96 and r4(2 * norm.cdf(z)) == 0.0485 and r4(2 * sr_cdf(32, 158)) == 0.0475

# ---- Worked example 6
assert 12 * 28 - 130 == 206 and 12 * 28 / 2 == 168 and 12 * 15 * 28 / 12 == 420 and round(math.sqrt(420), 2) == 20.49
z = z_rs(130, 12, 15)
assert r3(z) == -1.830 and z < -1.6449 and r4(norm.cdf(z)) == 0.0336

# ---- Practice
n, P, Q, _ = signed([3.1, -1.2, 4.5, 2.2, -0.7, 5.8, 1.9, -3.6])
assert (n, P, Q) == (8, 27, 9)
n, P, Q, _ = signed([22.4, 19.1, 25.3, 23.8, 21.2, 17.2, 26.7, 24.1, 20.6], 20)
assert (n, P, Q) == (9, 38, 7) and Q <= SR[9][0]
assert SR[15][1] == 25 and SR[15][2] == 19
n, P, Q, _ = signed([14.2, 15.8, 13.1, 16.4, 12.9, 15.0, 14.7, 13.6], other=[13.5, 16.9, 11.8, 14.3, 12.4, 13.2, 14.6, 11.1])
assert (n, P, Q) == (8, 32, 4) and SR[8][1] == 3 and SR[8][0] == 5
R, C = ranksum([34, 41, 29, 45, 38], [47, 52, 36, 50, 44, 55, 49])
assert (R, C) == (19, 46)
R, C = ranksum([8.2, 6.9, 7.5, 9.1], [9.8, 8.7, 10.4, 7.8, 11.2, 9.5])
assert (R, C) == (13, 31) and rs_table(4, 6, 0.05) == 13
assert 40 * 41 / 4 == 410 and 40 * 41 * 81 / 24 == 5535
z = z_sr(270, 40)
assert r3(z) == -1.875 and -1.96 < z < -1.6449
assert 15 * 36 - 330 == 210 and 15 * 36 / 2 == 270 and 15 * 20 * 36 / 12 == 900
z = z_rs(210, 15, 20)
assert r3(z) == -1.983 and z < -1.96
assert list(rankdata([3, 5, 5, 8, 9, 9, 9, 12])) == [1, 2.5, 2.5, 4, 6, 6, 6, 8]

# ---- Section B
cafe = [4.2, 5.7, 3.4, 6.4, 4.9, 2.8, 5.1, 6.2, 3.9, 4.5, 6.0]
n, P, Q, _ = signed(cafe, 6)
assert (n, P, Q) == (10, 4, 51) and SR[10][0] == 10 and r4(sr_cdf(10, 4)) == 0.0068
assert sum(x > 6 for x in cafe) == 2 and sum(x < 6 for x in cafe) == 8
assert binom.cdf(2, 10, 0.5) * 1024 == 56 and r4(binom.cdf(2, 10, 0.5)) == 0.0547

la = [2.84, 3.17, 2.95, 3.40, 2.61, 3.08, 2.77, 3.52, 2.99, 3.21, 3.36, 2.70]
lb = [2.72, 3.22, 2.74, 3.32, 2.61, 2.93, 2.80, 3.25, 2.89, 3.35, 3.18, 2.64]
assert [round(a - b, 2) for a, b in zip(la, lb)] == [0.12, -0.05, 0.21, 0.08, 0, 0.15, -0.03, 0.27, 0.10, -0.14, 0.18, 0.06]
n, P, Q, _ = signed(la, other=lb)
assert (n, P, Q) == (11, 56, 10) and SR[11][1] == 10

R, C = ranksum([31.2, 28.4, 35.6, 27.9, 30.1], [33.8, 36.2, 29.5, 38.4, 34.7, 37.1])
assert (R, C) == (20, 40) and rs_table(5, 6, 0.025) == 18 and rs_table(5, 6, 0.05) == 20
assert r4(2 * rs_cdf(5, 6, 20)) == 0.0823
assert math.comb(7, 3) == 35 and rs_cdf(3, 4, 6) == 1 / 35 and rs_cdf(3, 4, 7) == 2 / 35
assert r4(1 / 35) == 0.0286 and r4(2 / 35) == 0.0571 and rs_table(3, 4, 0.05) == 6

assert 11 * 26 / 2 == 143 and 11 * 26 - 185 == 101
var = 11 * 14 * 26 / 12
assert round(var, 2) == 333.67 and round(math.sqrt(var), 2) == 18.27
z = z_rs(101, 11, 14)
assert r3(z) == -2.272 and z < -1.96 and z > -2.5758

print("a213 checks passed")
