"""Recomputes every number stated in content/a214.py (Normal probability plots, software output, simulation).

All simulated output is regenerated from fixed numpy seeds (np.random.default_rng(seed)), so it is reproducible.
"""
import json
from math import sqrt
from pathlib import Path

import numpy as np
from scipy import stats
from scipy.integrate import quad
from scipy.stats import chi2, norm, t

TABLES = json.loads((Path(__file__).resolve().parents[1] / "tables_cache.json").read_text())
FAILS = []


def chk(label, value, stated, dp=None, sig=3):
    got = round(float(value), dp) if dp is not None else float(f"{float(value):.{sig}g}")
    ok = abs(got - stated) < 1e-9
    print(("ok  " if ok else "FAIL"), label, value, "stated", stated)
    if not ok:
        FAILS.append(label)


def eq(label, value, stated):
    ok = value == stated
    print(("ok  " if ok else "FAIL"), label, value, "stated", stated)
    if not ok:
        FAILS.append(label)


def nscores(n):
    return norm.ppf((np.arange(1, n + 1) - 0.5) / n)


def ks(x):
    x = np.asarray(x, float)
    return stats.kstest(x, "norm", args=(x.mean(), x.std(ddof=1)))


def wtab(n, col):
    header, rows = TABLES[19][1], TABLES[19][2]
    return int(next(r for r in rows if r[0] == str(n))[col])


# ---------- Example 1 ----------
x = np.array([41, 45, 47, 48, 50, 51, 52, 54, 56, 60.])
z = nscores(10)
for zi, s in zip(z, [-1.645, -1.036, -0.674, -0.385, -0.126, 0.126, 0.385, 0.674, 1.036, 1.645]):
    chk("ex1 z", zi, s, dp=3)
chk("ex1 mean", x.mean(), 50.4, dp=1)
chk("ex1 s", x.std(ddof=1), 5.522, dp=3)
chk("ex1 line low", 50.4 - 5.522 * 1.645, 41.3, dp=1)
chk("ex1 line high", 50.4 + 5.522 * 1.645, 59.5, dp=1)
chk("ex1 line -0.674", 50.4 - 5.522 * 0.674, 46.7, dp=1)
chk("ex1 line 0.674", 50.4 + 5.522 * 0.674, 54.1, dp=1)
chk("ex1 r", np.corrcoef(z, x)[0, 1], 0.998, dp=3)

# ---------- Example 2 ----------
A = np.sort(np.round(np.random.default_rng(2).normal(152, 9, 40)))
B = np.sort(np.round(2 + np.random.default_rng(103).exponential(6, 40), 1))
z40 = nscores(40)
idx = [1, 10, 20, 21, 31, 40]
for i, s in zip(idx, [-2.241, -0.714, -0.031, 0.031, 0.714, 2.241]):
    chk(f"ex2 z{i}", z40[i - 1], s, dp=3)
eq("ex2 A pts", [float(A[i - 1]) for i in idx], [130, 147, 153, 154, 159, 171])
eq("ex2 B pts", [float(B[i - 1]) for i in idx], [2.0, 3.1, 4.5, 4.7, 10.9, 19.2])
chk("ex2 B gap low", B[19] - B[9], 1.4, dp=1)
chk("ex2 B gap high", B[30] - B[20], 6.2, dp=1)
chk("ex2 A mean", A.mean(), 152.1, dp=1)
chk("ex2 A sd", A.std(ddof=1), 8.666, dp=3)
ka, kb = ks(A), ks(B)
chk("ex2 A D", ka.statistic, 0.093, dp=3)
chk("ex2 A p", ka.pvalue, 0.852, dp=3)
chk("ex2 B mean", B.mean(), 6.60, dp=2)
chk("ex2 B sd", B.std(ddof=1), 4.792, dp=3)
chk("ex2 B D", kb.statistic, 0.290, dp=3)
chk("ex2 B p", kb.pvalue, 0.002, dp=3)
eq("ex2 B min", float(B.min()), 2.0)

# ---------- Example 3 ----------
d = np.round(np.random.default_rng(16).normal(496.5, 5, 12), 1)
m, s = d.mean(), d.std(ddof=1)
se = s / sqrt(12)
r = stats.ttest_1samp(d, 500)
chk("ex3 mean", m, 496.85, dp=2)
chk("ex3 sd", s, 4.797, dp=3)
chk("ex3 se", se, 1.385, dp=3)
chk("ex3 t", r.statistic, -2.275, dp=3)
chk("ex3 p2", r.pvalue, 0.0439, dp=4)
chk("ex3 p1", r.pvalue / 2, 0.0220, sig=3)
chk("ex3 ks", ks(d).pvalue, 0.808, dp=3)
tc = t.isf(0.025, 11)
chk("ex3 t crit", tc, 2.201, dp=3)
chk("ex3 CI lo", m - tc * se, 493.80, dp=2)
chk("ex3 CI hi", m + tc * se, 499.90, dp=2)
chk("ex3 hand t", (496.85 - 500) / 1.385, -2.27, dp=2)
chk("ex3 margin", 2.201 * 1.385, 3.05, dp=2)

# ---------- Example 4 ----------
pmf = np.array([0] + [1 / 6] * 6)
tot = np.array([1.0])
for _ in range(10):
    tot = np.convolve(tot, pmf)
p40, p50 = tot[41:].sum(), tot[51:].sum()
chk("ex4 P(T>40)", p40, 0.1565, dp=4)
chk("ex4 P(T>50)", p50, 0.00148, sig=3)
exp40 = {100: [17, 15, 13], 1000: [156, 149, 158], 10000: [1594, 1573, 1550]}
exp50 = {1000: [1, 6, 1]}
for N, counts in exp40.items():
    got40, got50 = [], []
    for seed in (1, 2, 3):
        tt = np.random.default_rng(seed).integers(1, 7, (N, 10)).sum(1)
        got40.append(int((tt > 40).sum()))
        got50.append(int((tt > 50).sum()))
    eq(f"ex4 counts N={N}", got40, counts)
    if N in exp50:
        eq(f"ex4 >50 counts N={N}", got50, exp50[N])
chk("ex4 combined", (1594 + 1573 + 1550) / 30000, 0.157)
eq("ex4 combined count", 1594 + 1573 + 1550, 4717)
chk("ex4 se100", sqrt(0.1565 * 0.8435 / 100), 0.0363, dp=4)
chk("ex4 se10000", sqrt(0.1565 * 0.8435 / 10000), 0.00363, sig=3)
chk("ex4 2se100", 2 * sqrt(0.1565 * 0.8435 / 100), 0.073, dp=3)
chk("ex4 2se10000", 2 * sqrt(0.1565 * 0.8435 / 10000), 0.0073, dp=4)
chk("ex4 exp count", 1000 * 0.00148, 1.48, dp=2)
chk("ex4 se rare", sqrt(0.00148 * 0.99852 / 1000), 0.00122, sig=3)
chk("ex4 N rare", (1 - 0.00148) / (0.01 * 0.00148), 67500, sig=3)

# ---------- Example 5 ----------
rng = np.random.default_rng(5)
u1, u2 = rng.random(1000), rng.random(1000)
X = 2 + 4 * u1
Y = norm.ppf(u2, 9, 1.5)
D = 2 * X - Y
rows = [(0.8050, 5.220, 0.8673, 10.670, -0.230), (0.8079, 5.232, 0.0564, 6.621, 3.843), (0.5153, 4.061, 0.5215, 9.081, -0.958)]
for i, (a, b, c, dd, e) in enumerate(rows):
    chk(f"ex5 r{i} A", u1[i], a, dp=4)
    chk(f"ex5 r{i} B", X[i], b, dp=3)
    chk(f"ex5 r{i} C", u2[i], c, dp=4)
    chk(f"ex5 r{i} D", Y[i], dd, dp=3)
    chk(f"ex5 r{i} E", D[i], e, dp=3)
chk("ex5 row1 hand", 2 + 4 * 0.8050, 5.220, dp=3)
chk("ex5 row1 hand E", 2 * 5.220 - 10.670, -0.230, dp=3)
eq("ex5 count", int((D > 0).sum()), 377)
chk("ex5 mean", D.mean(), -1.042, dp=3)
chk("ex5 sd", D.std(ddof=1), 2.741, dp=3)
chk("ex5 se", sqrt(0.377 * 0.623 / 1000), 0.0153)
chk("ex5 var", 4 * 4 / 3 + 2.25, 7.583, dp=3)
chk("ex5 sdD", sqrt(4 * 4 / 3 + 2.25), 2.754, dp=3)
exact5 = quad(lambda v: 0.25 * norm.cdf((2 * v - 9) / 1.5), 2, 6)[0]
chk("ex5 exact", exact5, 0.3766, dp=4)
assert abs(0.377 - exact5) < 0.0153

# ---------- Example 6 ----------
W = 12 * np.random.default_rng(6).random((1000, 20))
T = W.sum(1)
chk("ex6 mean", T.mean(), 119.44, dp=2)
chk("ex6 sd", T.std(ddof=1), 15.89, dp=2)
eq("ex6 count", int((T > 140).sum()), 103)
chk("ex6 ks", ks(T).pvalue, 0.906, dp=3)
chk("ex6 sdT", sqrt(240), 15.49, dp=2)
chk("ex6 z", 20 / sqrt(240), 1.291, dp=3)
chk("ex6 clt", norm.sf(140, 120, sqrt(240)), 0.0984)
chk("ex6 se", sqrt(0.103 * 0.897 / 1000), 0.0096, dp=4)
chk("ex6 diff", 0.103 - 0.0984, 0.0046, dp=4)

# ---------- Practice ----------
x8 = np.array([3.1, 3.8, 4.0, 4.4, 4.5, 4.9, 5.3, 6.6])
for zi, s8 in zip(nscores(8), [-1.534, -0.887, -0.489, -0.157, 0.157, 0.489, 0.887, 1.534]):
    chk("p1 z", zi, s8, dp=3)
chk("p1 mean", x8.mean(), 4.575, dp=3)
chk("p1 s", x8.std(ddof=1), 1.061, dp=3)
chk("p1 line", 4.575 + 1.061 * 1.534, 6.20, dp=2)

rr, n = 0.412, 25
tr = rr * sqrt(n - 2) / sqrt(1 - rr * rr)
chk("p5 p2", 2 * t.sf(tr, n - 2), 0.0407, dp=4)
chk("p5 p1", t.sf(tr, n - 2), 0.0204, dp=4)

chk("p6 p", chi2.sf(11.87, 4), 0.0183, dp=4)
chk("p6 crit", chi2.isf(0.05, 4), 9.488, dp=3)

chk("p7 mean", (12.31 + 14.07) / 2, 13.19, dp=2)
chk("p7 margin", (14.07 - 12.31) / 2, 0.88, dp=2)

chk("p9 se", sqrt(0.212 * 0.788 / 500), 0.0183, dp=4)
chk("p9 lo", 0.212 - 2 * 0.0183, 0.175, dp=3)
chk("p9 hi", 0.212 + 2 * 0.0183, 0.249, dp=3)
chk("p9 N", 0.212 * 0.788 / 0.01 ** 2, 1670.6, dp=1)

us = [0.731, 0.052, 0.918, 0.402]
eq("p10 die", [int(6 * u) + 1 for u in us], [5, 1, 6, 3])
for u, s10 in zip(us, [4.193, 2.156, 4.754, 3.206]):
    chk("p10 unif", 2 + 3 * u, s10, dp=3)
for u, s10 in zip(us, [21.85, 15.12, 24.18, 19.26]):
    chk("p10 norm", norm.ppf(u, 20, 3), s10, dp=2)

chk("p11 p2", 2 * t.sf(2.31, 14), 0.0366, dp=4)
chk("p11 p1", t.sf(2.31, 14), 0.0183, dp=4)
chk("p11 other", 1 - 0.0183, 0.982, dp=3)

dw = np.round(np.random.default_rng(22).normal(1.2, 2.5, 15), 1)
assert len(set(np.abs(dw))) == 15 and not (dw == 0).any()
sr = np.sign(dw) * stats.rankdata(np.abs(dw))
eq("p12 W+", float(sr[sr > 0].sum()), 92.0)
eq("p12 W-", float(-sr[sr < 0].sum()), 28.0)
chk("p12 p", stats.wilcoxon(dw).pvalue, 0.0730, dp=4)
chk("p12 p1", stats.wilcoxon(dw).pvalue / 2, 0.0365, dp=4)
eq("p12 total", 92 + 28, 15 * 16 // 2)
eq("p12 table 5% 1-t", wtab(15, 1), 30)
eq("p12 table 5% 2-t", wtab(15, 2), 25)

# ---------- Exam 1 ----------
b1 = np.round(np.random.default_rng(32).normal(41.6, 2.8, 15), 1)
m, s = b1.mean(), b1.std(ddof=1)
se = s / sqrt(15)
r = stats.ttest_1samp(b1, 40)
chk("B1 ks", ks(b1).pvalue, 0.808, dp=3)
chk("B1 mean", m, 41.553, dp=3)
chk("B1 sd", s, 3.040, dp=3)
chk("B1 se", se, 0.785, dp=3)
chk("B1 t", r.statistic, 1.979, dp=3)
chk("B1 p2", r.pvalue, 0.0678, dp=4)
chk("B1 p1", r.pvalue / 2, 0.0339, dp=4)
tc = t.isf(0.025, 14)
chk("B1 lo", m - tc * se, 39.87, dp=2)
chk("B1 hi", m + tc * se, 43.24, dp=2)
assert m - t.isf(0.05, 14) * se > 40  # 90% CI excludes 40, matching the one-tailed 5% result

# ---------- Exam 2 ----------
exact2 = quad(lambda v: (1 / 6) * norm.sf((50 / v - 6) / 1.0), 4, 10)[0]
chk("B2 exact", exact2, 0.2700, dp=4)
res = []
for seed in (7, 8):
    g = np.random.default_rng(seed)
    a1, a2 = g.random(1000), g.random(1000)
    area = (4 + 6 * a1) * norm.ppf(a2, 6, 1)
    res.append((int((area > 50).sum()), area.mean()))
eq("B2 run1", res[0][0], 273)
eq("B2 run2", res[1][0], 264)
chk("B2 mean", res[0][1], 41.95, dp=2)
chk("B2 se", sqrt(0.273 * 0.727 / 1000), 0.0141)
chk("B2 comb", 537 / 2000, 0.2685, dp=4)
chk("B2 N", 0.27 * 0.73 / 0.005 ** 2, 7884, dp=0)

# ---------- Exam 3 ----------
d3 = np.round(np.random.default_rng(44).normal(3.0, 2.0, 11), 1)
d3 = np.append(d3, -14.0)
eq("B3 data", sorted(float(v) for v in d3), [-14.0, 1.0, 2.0, 2.2, 3.2, 3.7, 3.8, 4.2, 4.6, 4.7, 5.3, 5.9])
r = stats.ttest_1samp(d3, 0)
chk("B3 ks", ks(d3).pvalue, 0.123, dp=3)
chk("B3 mean", d3.mean(), 2.217, dp=3)
chk("B3 sd", d3.std(ddof=1), 5.300, dp=3)
chk("B3 t", r.statistic, 1.449, dp=3)
chk("B3 p2", r.pvalue, 0.1753, dp=4)
chk("B3 p1", r.pvalue / 2, 0.0877, dp=4)
sr = np.sign(d3) * stats.rankdata(np.abs(d3))
eq("B3 W+", float(sr[sr > 0].sum()), 66.0)
eq("B3 W-", float(-sr[sr < 0].sum()), 12.0)
wp = stats.wilcoxon(d3).pvalue
chk("B3 wp", wp, 0.0342, dp=4)
chk("B3 wp1", wp / 2, 0.0171, dp=4)
eq("B3 table", wtab(12, 1), 17)
d11 = d3[d3 > 0]
chk("B3 mean11", d11.mean(), 3.69, dp=2)
chk("B3 t11", stats.ttest_1samp(d11, 0).statistic, 8.23, dp=2)

# ---------- Exam 4 ----------
EX = 10 * quad(lambda u: u ** 2, 0, 1)[0]
EX2 = 100 * quad(lambda u: u ** 4, 0, 1)[0]
chk("B4 E", EX, 10 / 3, dp=9)
chk("B4 EX2", EX2, 20, dp=9)
chk("B4 Var", EX2 - EX ** 2, 80 / 9, dp=9)
sig = sqrt(80 / 9)
chk("B4 sigma", sig, 2.981, dp=3)
chk("B4 sd5", sig / sqrt(5), 1.333, dp=3)
chk("B4 sd30", sig / sqrt(30), 0.544, dp=3)
out = {1: (18, 3.301, 2.999, None, 188), 5: (19, 3.343, 1.322, 0.226, 150), 30: (14, 3.337, 0.562, 0.824, 60)}
for nn, (seed, mm, sd, kp, cnt) in out.items():
    M = (10 * np.random.default_rng(seed).random((500, nn)) ** 2).mean(1)
    chk(f"B4 n={nn} mean", M.mean(), mm, dp=3)
    chk(f"B4 n={nn} sd", M.std(ddof=1), sd, dp=3)
    p = ks(M).pvalue
    if kp is None:
        assert p < 0.001, p
        print("ok   B4 n=1 ks p < 0.001", p)
    else:
        chk(f"B4 n={nn} ks", p, kp, dp=3)
    eq(f"B4 n={nn} count", int((M > 4).sum()), cnt)
    if nn == 1:
        assert stats.skew(M) > 0.5  # clearly positively skewed: plot curves upwards
chk("B4 sim", 60 / 500, 0.12, dp=2)
chk("B4 z", (4 - 10 / 3) / (sig / sqrt(30)), 1.225, dp=3)
chk("B4 clt", norm.sf(4, 10 / 3, sig / sqrt(30)), 0.110)
chk("B4 se", sqrt(0.12 * 0.88 / 500), 0.015, dp=3)

print()
print("FAILURES:", FAILS if FAILS else "none")
raise SystemExit(1 if FAILS else 0)
