"""Recomputes every number stated in content/a202.py and checks it appears in the unit text."""
import importlib
import math
import sys
from fractions import Fraction
from pathlib import Path

from scipy import integrate, optimize

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
MODULE = "a202"
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


from scipy import stats

E = lambda lam: stats.expon(scale=1 / lam)
# WE1, WE2
X = E(0.4)
ok(X.mean(), "2.5"); ok(X.std(), "2.5"); ok(X.sf(3), "0.3012"); ok(X.cdf(4) - X.cdf(1), "0.4684")
ok(math.exp(-0.4), "0.67032"); ok(math.exp(-1.6), "0.20190")
ok(X.median(), "1.73"); ok(X.ppf(0.75), "3.47"); ok(X.ppf(0.9), "5.76")
# WE3
T = E(0.1)
ok(T.mean(), "10"); ok(T.sf(15), "0.2231"); ok(stats.poisson(1.5).pmf(0), "0.2231"); ok(T.cdf(5), "0.3935")
p = T.sf(15); B = stats.binom(5, p)
ok(B.pmf(0), "0.2830"); ok(B.pmf(1), "0.4064"); ok(B.sf(1), "0.311")
# WE4
X = E(1 / 1000)
ok(X.sf(1100) / X.sf(600), "0.6065"); ok(X.sf(500), "0.6065")
# WE5
lam = -math.log(0.3) / 2; ok(lam, "0.602"); ok(1 / lam, "1.66"); assert abs(E(lam).sf(2) - 0.3) < 1e-12
lam = math.log(2) / 5; ok(lam, "0.1386"); ok(1 / lam, "7.21")
# WE6
lam = 1 / 4.2; ok(lam, "0.238"); ok(math.exp(-10 / 4.2), "0.09246"); ok(80 * math.exp(-10 / 4.2), "7.40"); ok(1 - math.exp(-1), "0.632")

# Practice
X = E(2); ok(X.sf(1), "0.1353"); ok(X.cdf(0.25), "0.3935")
X = E(0.25); ok(X.mean(), "4"); ok(X.var(), "16"); ok(X.sf(4), "0.3679")
X = E(1 / 8); ok(X.cdf(10) - X.cdf(5), "0.2488")
X = E(0.5); ok(X.median(), "1.39"); ok(X.ppf(0.75) - X.ppf(0.25), "2.20")
lam = math.log(5) / 3; assert abs(E(lam).sf(3) - 0.2) < 1e-12; ok(lam, "0.536"); ok(1 / lam, "1.86")
X = E(0.2); ok(X.sf(10), "0.1353"); ok(X.cdf(2), "0.3297")
X = E(0.1); ok(X.sf(15) / X.sf(5), "0.3679"); ok(X.sf(10), "0.3679")
X = E(3)
E2 = I(lambda x: x * x * 3 * math.exp(-3 * x), 0, 60); okf(E2, "2/9")
okf(2 * E2 - 3 * X.mean() + 1, "4/9"); ok(2 * E2 - 3 * X.mean() + 1, "0.444")
okf(I(lambda x: math.exp(x) * 3 * math.exp(-3 * x), 0, 60), "3/2")
X = E(0.2); ok(X.mean(), "5"); ok(X.isf(0.01), "23.0")

# Section B
ok(math.log(2), "0.693")
T = E(3 / 7)
ok(T.sf(4), "0.180"); ok(stats.poisson(12 / 7).pmf(0), "0.180")
ok(T.sf(5) / T.sf(3), "0.424"); ok(T.sf(2), "0.424")
N = stats.poisson(12); ok(N.cdf(15), "0.8444"); ok(N.sf(15), "0.156")
lam = -math.log(0.6) / 500; ok(lam, "0.00102"); X = E(lam)
ok(X.mean(), "979"); ok(X.median(), "678"); ok(X.sf(200) ** 4, "0.442"); ok(0.6 ** 1.6, "0.442")
assert abs(X.sf(200) - 0.6 ** 0.4) < 1e-12
ok(I(lambda x: math.exp(x) * 2 * math.exp(-2 * x), 0, 80), "2")
X = E(2)
for y in (0.1, 0.5, 0.8):
    assert abs(X.sf(-math.log(y) / 2) - y) < 1e-12
ok(X.cdf(-math.log(0.8) / 2), "0.2")

print(f"{MODULE}: all {COUNT} checks passed")
