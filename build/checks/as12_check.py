"""Recomputes every number stated in content/as12.py and checks it appears in the unit text."""
import importlib
import math
import sys
from fractions import Fraction
from pathlib import Path

from scipy import integrate, optimize

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
MODULE = "as12"
UNIT = importlib.import_module(f"content.{MODULE}").UNIT


def _flat(o):
    if isinstance(o, str):
        return [o]
    if isinstance(o, dict):
        return [s for v in o.values() for s in _flat(v)]
    if isinstance(o, (list, tuple)):
        return [s for v in o for s in _flat(v)]
    return [str(o)]


TEXT = "\n".join(_flat(UNIT)).replace("−", "-")
COUNT = 0


def ok(value, stated, tol=None):
    """value rounds to the decimal string `stated`, and `stated` appears in the unit."""
    global COUNT
    s = stated.replace("−", "-")
    dec = len(s.split(".")[1]) if "." in s else 0
    tol = 0.5 * 10 ** (-dec) + 1e-9 if tol is None else tol
    assert abs(value - float(s)) <= tol, f"{stated}: computed {value}"
    assert s in TEXT, f"{stated!r} not found in {MODULE} text"
    COUNT += 1


def okf(value, stated):
    """value equals the fraction `stated` (e.g. '3/8') to 1e-9, and it appears in the unit."""
    global COUNT
    assert abs(value - float(Fraction(stated))) < 1e-9, f"{stated}: computed {value}"
    assert stated in TEXT, f"{stated!r} not found in {MODULE} text"
    COUNT += 1


def I(f, a, b):
    return integrate.quad(f, a, b, epsabs=1e-13, epsrel=1e-13)[0]


def root(f, a, b):
    return optimize.brentq(f, a, b, xtol=1e-14)


import json
from scipy import stats

z = lambda c: stats.norm.ppf(0.5 + c / 2)
# z values agree with tables_cache Table 2
tab = json.load(open(ROOT / "tables_cache.json"))
t2 = [t for t in tab if t[0].startswith("Table 2")][0]
row = dict(zip(t2[1][1:], t2[2][0][1:]))
for c, p, s in ((0.9, "0.05", "1.6449"), (0.95, "0.025", "1.9600"), (0.98, "0.01", "2.3263"), (0.99, "0.005", "2.5758")):
    assert row[p] == s, (p, row[p]); ok(z(c), s)


def ci(x, se, c, lo, hi, half=None):
    h = z(c) * se
    if half:
        ok(h, half)
    ok(x - h, lo); ok(x + h, hi)


# WE1
ci(12.4, 0.5, 0.95, "11.42", "13.38", "0.98")
# WE2
se = 4 / math.sqrt(20); ok(se, "0.8944")
ci(502.1, se, 0.95, "500.35", "503.85", "1.753"); ci(502.1, se, 0.99, "499.80", "504.40", "2.304")
# WE3
xb = 3896 / 80; ok(xb, "48.7"); ok(191200 - 80 * xb ** 2, "1464.8"); s2 = (191200 - 80 * xb ** 2) / 79
ok(s2, "18.54"); ok(math.sqrt(s2), "4.306"); ci(xb, math.sqrt(s2 / 80), 0.95, "47.76", "49.64", "0.9436")
# WE4
ok(2 * 1.96 * 3, "11.76"); ok((2 * 1.96 * 3) ** 2, "138.3"); assert math.ceil((2 * z(0.95) * 3) ** 2) == 139
# WE5
sig = 1.88 * 4 / 1.96; ok(sig, "3.837"); ci(26, sig / 4, 0.90, "24.42", "27.58", "1.578")
# WE6
N = stats.binom(10, 0.95); ok(10 * 0.95, "9.5"); ok(0.95 ** 10, "0.5987"); ok(10 * 0.05 * 0.95 ** 9, "0.3151"); ok(N.sf(8), "0.914")

# Practice
ci(72, 1, 0.99, "69.42", "74.58", "2.576")
ci(15.2, 3 / math.sqrt(50), 0.95, "14.37", "16.03", "0.8315")
ci(8.43, 0.5 / math.sqrt(10), 0.90, "8.17", "8.69", "0.2601")
s2 = (56100 - 100 * 23.4 ** 2) / 99; okf(s2, "1344/99"); ok(s2, "13.58"); ok(math.sqrt(s2), "3.685")
ci(23.4, math.sqrt(s2) / 10, 0.95, "22.68", "24.12", "0.7222")
n = (z(0.99) * 6) ** 2; ok(n, "238.9"); assert math.ceil(n) == 239
ok(z(0.99) / z(0.95), "1.31")
ok(1.7 * math.sqrt(40) / 1.96, "5.49")
ok(0.9 ** 10, "0.349")
p = 0.34; m = 1.96 * math.sqrt(p * (1 - p) / 400); ok(m, "0.0464"); ok(p - m, "0.294"); ok(p + m, "0.386")
h = 2.8 * z(0.99) / 1.96; ok(h, "3.680"); ok(43 - h, "39.32"); ok(43 + h, "46.68")

# Section B
ok(60.84 / 12, "5.07"); ci(5.07, 0.15 / math.sqrt(12), 0.95, "4.985", "5.155", "0.08487")
ok(2 * 1.96 * 0.15 / 0.1, "5.88"); ok((2 * 1.96 * 0.15 / 0.1) ** 2, "34.57"); assert math.ceil((2 * z(0.95) * 0.15 / 0.1) ** 2) == 35
ok(stats.binom(8, 0.05).pmf(1), "0.279")
xb = 1530 / 60; ok(xb, "25.5"); s2 = (42300 - 60 * xb ** 2) / 59; okf(s2, "3285/59"); ok(s2, "55.68")
ci(xb, math.sqrt(s2 / 60), 0.98, "23.26", "27.74", "2.241")
sig = 0.84 * 5 / z(0.90); ok(sig, "2.55"); ok(sig, "2.553", tol=6e-4)
ci(13.2, sig / 5, 0.95, "12.20", "14.20", "1.001")
ci(61.8, 6 / math.sqrt(40), 0.99, "59.36", "64.24", "2.444")
r = 2 * z(0.99) * 6 / 3; ok(r, "10.30"); ok(r * r, "106.2"); assert math.ceil(r * r) == 107
ok(stats.binom(5, 0.99).sf(3), "0.999")

print(f"{MODULE}: all {COUNT} checks passed")
