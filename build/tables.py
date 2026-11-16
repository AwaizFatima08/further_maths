"""Statistical tables for the workbook appendix, computed exactly with scipy (no values typed by hand)."""
import itertools
import json
import math
from pathlib import Path

import numpy as np
from scipy import stats

# Spearman critical values are found by full enumeration, so keep n small.
SPEARMAN_MAX_N = 10


def normal_cdf_table():
    header = ["z"] + [f"{d:.2f}"[-2:] for d in np.arange(0, 0.1, 0.01)]
    rows = []
    for z0 in np.arange(0, 3.5, 0.1):
        rows.append([f"{z0:.1f}"] + [f"{stats.norm.cdf(z0 + d):.4f}" for d in np.arange(0, 0.1, 0.01)])
    return header, rows


def normal_points_table():
    ps = [0.5, 0.4, 0.3, 0.2, 0.15, 0.1, 0.05, 0.025, 0.02, 0.01, 0.005, 0.001]
    header = ["Upper-tail p"] + [f"{p}" for p in ps]
    row = ["z"] + [f"{stats.norm.isf(p):.4f}" for p in ps]
    return header, [row]


def t_table():
    tails = [0.10, 0.05, 0.025, 0.01, 0.005, 0.0005]
    header = ["ν"] + [f"{p}" for p in tails]
    rows = []
    for v in list(range(1, 31)) + [40, 60, 120]:
        rows.append([str(v)] + [f"{stats.t.isf(p, v):.3f}" for p in tails])
    rows.append(["∞"] + [f"{stats.norm.isf(p):.3f}" for p in tails])
    return header, rows


def chi2_table():
    tails = [0.995, 0.99, 0.975, 0.95, 0.90, 0.10, 0.05, 0.025, 0.01, 0.005]
    header = ["ν"] + [f"{p}" for p in tails]
    rows = []
    for v in list(range(1, 31)) + [40, 50]:
        rows.append([str(v)] + [f"{stats.chi2.isf(p, v):.3f}" for p in tails])
    return header, rows


def f_table(alpha):
    v1s = [1, 2, 3, 4, 5, 6, 8, 10, 12, 24]
    header = ["ν₂ \\ ν₁"] + [str(v) for v in v1s]
    rows = []
    for v2 in list(range(1, 13)) + [15, 20, 24, 30, 40, 60]:
        rows.append([str(v2)] + [f"{stats.f.isf(alpha, v1, v2):.2f}" for v1 in v1s])
    return header, rows


def poisson_table(lams):
    header = ["x"] + [f"{l:g}" for l in lams]
    rows = []
    for x in range(0, 21):
        vals = [stats.poisson.cdf(x, l) for l in lams]
        if all(v > 0.99995 for v in vals) and x > 0:
            break
        rows.append([str(x)] + [f"{v:.4f}" if v < 0.99995 else "1.0000" for v in vals])
    return header, rows


def binomial_table(n):
    ps = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
    header = [f"n = {n}, x"] + [f"{p:g}" for p in ps]
    rows = []
    for x in range(0, n + 1):
        vals = [stats.binom.cdf(x, n, p) for p in ps]
        if all(v > 0.99995 for v in vals):
            break
        rows.append([str(x)] + [f"{v:.4f}" if v < 0.99995 else "1.0000" for v in vals])
    return header, rows


def pmcc_table():
    one_tail = [0.05, 0.025, 0.01, 0.005]
    header = ["n", "5% (1-t) / 10% (2-t)", "2.5% / 5%", "1% / 2%", "0.5% / 1%"]
    rows = []
    for n in list(range(4, 31)) + [40, 50, 60, 80, 100]:
        vals = []
        for p in one_tail:
            t = stats.t.isf(p, n - 2)
            vals.append(f"{t / math.sqrt(t * t + n - 2):.4f}")
        rows.append([str(n)] + vals)
    return header, rows


def spearman_table():
    one_tail = [0.05, 0.025, 0.01, 0.005]
    header = ["n", "5% (1-t) / 10% (2-t)", "2.5% / 5%", "1% / 2%", "0.5% / 1%"]
    rows = []
    for n in range(4, SPEARMAN_MAX_N + 1):
        base = np.arange(n)
        counts = {}
        for perm in itertools.permutations(range(n)):
            d2 = int(((base - np.array(perm)) ** 2).sum())
            counts[d2] = counts.get(d2, 0) + 1
        total = math.factorial(n)
        # rs = 1 - 6 D / (n(n^2-1)); large rs <=> small D.
        ds = sorted(counts)
        cum, tail = 0, {}
        for d in ds:
            cum += counts[d]
            tail[d] = cum / total  # P(D <= d)
        vals = []
        for p in one_tail:
            ok = [d for d in ds if tail[d] <= p]
            if not ok:
                vals.append("–")
            else:
                d = max(ok)
                vals.append(f"{1 - 6 * d / (n * (n * n - 1)):.4f}")
        rows.append([str(n)] + vals)
    return header, rows


def wilcoxon_signed_rank_table():
    """Largest T with P(T ≤ t) ≤ α under H₀ (reject H₀ when T ≤ the tabulated value)."""
    one_tail = [0.05, 0.025, 0.01, 0.005]
    header = ["n", "5% (1-t) / 10% (2-t)", "2.5% / 5%", "1% / 2%", "0.5% / 1%"]
    rows = []
    for n in range(5, 31):
        maxs = n * (n + 1) // 2
        dist = np.zeros(maxs + 1)
        dist[0] = 1
        for k in range(1, n + 1):
            new = dist.copy()
            new[k:] += dist[:-k]
            dist = new
        cdf = np.cumsum(dist) / 2 ** n
        vals = []
        for p in one_tail:
            ok = np.where(cdf <= p)[0]
            vals.append(str(int(ok.max())) if len(ok) else "–")
        rows.append([str(n)] + vals)
    return header, rows


def wilcoxon_rank_sum_table(alpha):
    """Critical value W for the smaller sample (size m): reject H₀ when the rank sum of that sample ≤ W.
    Entries are the largest w with P(W ≤ w) ≤ α (one tail)."""
    header = ["m \\ n"] + [str(n) for n in range(3, 11)]
    rows = []
    for m in range(3, 11):
        row = [str(m)]
        for n in range(3, 11):
            if n < m:
                row.append("")
                continue
            # count subsets of size m from 1..m+n by rank sum
            N = m + n
            maxsum = sum(range(N - m + 1, N + 1))
            dp = np.zeros((m + 1, maxsum + 1))
            dp[0][0] = 1
            for r in range(1, N + 1):
                for k in range(min(r, m), 0, -1):
                    dp[k][r:] += dp[k - 1][:maxsum + 1 - r]
            dist = dp[m]
            cdf = np.cumsum(dist) / math.comb(N, m)
            ok = np.where(cdf <= alpha)[0]
            row.append(str(int(ok.max())) if len(ok) else "–")
        rows.append(row)
    return header, rows


ALL = [
    ("Table 1: The normal distribution function Φ(z) = P(Z ≤ z)", normal_cdf_table),
    ("Table 2: Percentage points of the normal distribution, P(Z > z) = p", normal_points_table),
    ("Table 3: Percentage points of the t distribution (upper-tail probability p)", t_table),
    ("Table 4: Percentage points of the χ² distribution (upper-tail probability p)", chi2_table),
    ("Table 5: Upper 5% points of the F distribution", lambda: f_table(0.05)),
    ("Table 6: Upper 1% points of the F distribution", lambda: f_table(0.01)),
    ("Table 7: Poisson cumulative probabilities P(X ≤ x), λ = 0.5 to 5", lambda: poisson_table([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])),
    ("Table 8: Poisson cumulative probabilities P(X ≤ x), λ = 5.5 to 10", lambda: poisson_table([5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10])),
] + [
    (f"Table {9 + i}: Binomial cumulative probabilities P(X ≤ x), n = {n}", (lambda n=n: binomial_table(n)))
    for i, n in enumerate([5, 6, 8, 10, 12, 15, 20, 25, 30])
] + [
    ("Table 18: Critical values of the product moment correlation coefficient r (bivariate normal)", pmcc_table),
    ("Table 19: Critical values of Spearman's rank correlation coefficient (exact)", spearman_table),
    ("Table 20: Wilcoxon signed-rank test: reject H₀ if T ≤ the tabulated value", wilcoxon_signed_rank_table),
    ("Table 21: Wilcoxon rank-sum test, 5% one-tailed (10% two-tailed): reject H₀ if W ≤ value", lambda: wilcoxon_rank_sum_table(0.05)),
    ("Table 22: Wilcoxon rank-sum test, 2.5% one-tailed (5% two-tailed): reject H₀ if W ≤ value", lambda: wilcoxon_rank_sum_table(0.025)),
]

CACHE = Path(__file__).resolve().parent / "tables_cache.json"


def compute_all():
    """Returns [(title, header, rows)], cached on disk because the Spearman enumeration is slow."""
    if CACHE.exists():
        return [tuple(t) for t in json.loads(CACHE.read_text())]
    out = []
    for title, fn in ALL:
        header, rows = fn()
        out.append((title, header, rows))
    CACHE.write_text(json.dumps(out, ensure_ascii=False))
    return out
