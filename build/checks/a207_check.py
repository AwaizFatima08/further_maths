"""Recomputes every number stated in content/a207.py and checks it appears in the unit text."""
import importlib
import math
import sys
from fractions import Fraction
from pathlib import Path

from scipy import integrate, optimize

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
MODULE = "a207"
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


import numpy as np
from scipy import stats

N = stats.norm
# WE1
ok(N.cdf(1.5), "0.9332"); ok(N.sf(53, 50, 2), "0.0668")
# WE2
ok(2 / math.sqrt(2.5), "1.265"); ok(N.sf(52, 50, math.sqrt(2.5)), "0.103")
# WE3 (dice): exact distribution by convolution
d = np.ones(6) / 6; p = d.copy()
for _ in range(49):
    p = np.convolve(p, d)
exact = p[186 - 50:].sum(); ok(exact, "0.1928")
v = 50 * 35 / 12; ok(v, "145.83"); ok(math.sqrt(v), "12.076"); ok(10.5 / math.sqrt(v), "0.8695")
ok(N.sf(185.5, 175, math.sqrt(v)), "0.192")
# WE4
x = np.array([12.1, 13.4, 11.8, 12.9, 13.0, 12.6])
ok(x.sum(), "75.8"); ok(x.mean(), "12.63"); ok(((x - x.mean()) ** 2).sum(), "1.7733"); ok(x.var(ddof=1), "0.355")
ok(x.var(ddof=1), "0.35467", tol=5e-6); ok(x.std(ddof=1) / math.sqrt(6), "0.243")
# WE5
okf(3 / 9, "1/3"); okf(6 / 16, "3/8")
# WE6
d = np.array([1.2, 3.8, 0.7, 2.5, 6.1]); ok(d.sum(), "14.3"); ok(d.mean(), "2.86"); ok(2 * d.mean(), "5.72")
# check Var(2Xbar) = theta^2/(3n) by simulation-free algebra
th, n = 7.0, 5; assert abs(4 * (th ** 2 / 12) / n - th ** 2 / (3 * n)) < 1e-12

# Practice
ok(N.cdf(11, 12, 0.5), "0.0228")
se = 5 / math.sqrt(50); ok(se, "0.7071"); ok(1.5 / se, "2.121"); ok(-1 / se, "-1.414")
ok(N.cdf(31.5, 30, se) - N.cdf(29, 30, se), "0.904")
ok(0.4 / math.sqrt(0.075), "1.461"); ok(N.sf(3.4, 3, math.sqrt(3 / 40)), "0.0721")
ok(N.sf(2.5, 2, 1 / 3), "0.0668")
ok((1.96 * 6) ** 2, "138.3"); assert math.ceil((N.ppf(0.975) * 6) ** 2) == 139
ok(x.var(ddof=1), "0.3547"); ok(x.std(ddof=1), "0.596")
xb = 310 / 20; ok(xb, "15.5"); s2 = (4900 - 20 * xb ** 2) / 19; okf(s2, "95/19"); ok(s2, "5"); ok(math.sqrt(s2 / 20), "0.5")
assert "5σ²/8" in TEXT and abs((1 + 9) / 16 - 5 / 8) < 1e-12
Y = N(20, math.sqrt(15)); ok(Y.sf(24.5), "0.123")
assert abs(stats.binom(80, 0.25).sf(24) - 0.123) < 0.01  # exact value is close to the approximation

# Section B
T = N(120, math.sqrt(40.5)); ok(5 / math.sqrt(40.5), "0.7857"); ok(T.sf(125), "0.216")
se = 0.9 / math.sqrt(50); ok(se, "0.1273"); ok(0.2 / se, "1.571"); ok(2 * N.cdf(0.2 / se) - 1, "0.884")
assert "7σ²/18" in TEXT and abs(14 / 36 - 7 / 18) < 1e-12; okf(6 / 18, "1/3"); okf(1 / (7 / 5), "5/7")
th = 45.6 / 10 * 2 / 3; ok(45.6 / 10, "4.56"); ok(th, "3.04"); ok(th / math.sqrt(270), "0.185"); ok(6.3 / 2, "3.15")
U = stats.uniform(3, 3); assert abs(U.mean() - 4.5) < 1e-12 and abs(U.var() - 9 / 12) < 1e-12
xb = 87.6 / 12; ok(xb, "7.3"); ok(662.04 - 12 * xb ** 2, "22.56"); s2 = (662.04 - 12 * xb ** 2) / 11
ok(s2, "2.05"); ok(s2, "2.0509", tol=5e-5); ok(math.sqrt(s2 / 12), "0.413")

print(f"{MODULE}: all {COUNT} checks passed")
