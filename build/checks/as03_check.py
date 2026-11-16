"""Recomputes every number stated in content/as03.py (Unit AS3) and checks it appears in the unit text."""
import os
import sys
from fractions import Fraction as Fr
from math import ceil, log, sqrt

from scipy import stats

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.as03 import UNIT  # noqa: E402


def _text(o):
    if isinstance(o, str):
        return o
    if isinstance(o, dict):
        return " ".join(_text(v) for v in o.values())
    if isinstance(o, (list, tuple)):
        return " ".join(_text(v) for v in o)
    return str(o)


TEXT = _text(UNIT)
COUNT = 0


def num(s, v, sf=None):
    """s must equal v rounded to the decimals shown (or to sf significant figures) and appear in the unit."""
    global COUNT
    if sf:
        assert float(f"{v:.{sf}g}") == float(s), f"{s} != {v}"
    else:
        d = len(s.split(".")[1]) if "." in s else 0
        assert abs(round(float(v), d) - float(s)) < 1e-9, f"{s} != {v}"
    assert s in TEXT, f"{s} not found in unit text"
    COUNT += 1


G, B = stats.geom, stats.binom  # scipy geom: support 1, 2, ... (trials up to first success)


def smallest_n(q, target):  # smallest n with q**n <= target
    n = ceil(log(target) / log(q))
    assert q ** n <= target < q ** (n - 1)
    return n


# Notes table
for p, row in [(0.5, ["0.875", "0.000977", "2", "2", "1"]), (0.3, ["0.657", "0.0282", "3.33", "7.78", "2"]),
               (1 / 6, ["0.421", "0.162", "6", "30", "4"]), (0.1, ["0.271", "0.349", "10", "90", "7"])]:
    num(row[0], G.cdf(3, p), 3); num(row[1], G.sf(10, p), 3); num(row[2], G.mean(p), 3); num(row[3], G.var(p), 3)
    assert G.median(p) == int(row[4]) and min(k for k in range(1, 50) if G.cdf(k, p) >= 0.5) == int(row[4])
num("0.167", 1 / 6)

# Example 1
q = 0.85
num("0.0783", G.pmf(5, .15), 3); num("0.377", G.sf(6, .15), 3); num("0.478", G.cdf(4, .15), 3)
num("0.7225", q ** 2); num("0.2725", q ** 8); num("0.450", G.cdf(8, .15) - G.cdf(2, .15), 3)
# Example 2
num("14.17", log(.1) / log(q)); assert smallest_n(q, 0.1) == 15; num("0.103", q ** 14, 3); num("0.0874", q ** 15, 3)
# Example 3
assert G.mean(1 / 6) == 6 and abs(G.var(1 / 6) - 30) < 1e-9; num("5.48", sqrt(30))
num("0.335", G.sf(6, 1 / 6), 3); assert abs(G.sf(10, 1 / 6) / G.sf(4, 1 / 6) - G.sf(6, 1 / 6)) < 1e-12
# Example 4
assert abs(G.var(0.25) - 12) < 1e-9; num("0.5625", G.sf(2, .25))
# Example 5
pa = 0.3 / (1 - 0.7 * 0.6); assert Fr(3, 10) / (1 - Fr(42, 100)) == Fr(15, 29); num("0.517", pa)
# brute-force check by summing the series
assert abs(sum(0.3 * 0.42 ** k for k in range(200)) - pa) < 1e-12

# Practice
num("0.128", G.pmf(3, .2)); assert G.mean(.2) == 5 and abs(G.var(.2) - 20) < 1e-9
num("0.0961", G.pmf(4, .35)); num("0.1160", G.sf(5, .35)); num("0.7254", G.cdf(3, .35))
num("0.0387", G.pmf(6, .05), 3); num("0.358", G.sf(20, .05), 3)
num("0.8333", 5 / 6); num("0.4019", (5 / 6) ** 5); num("0.431", G.cdf(5, 1 / 6) - G.cdf(1, 1 / 6), 3)
num("55.23", log(.01) / log(.92)); assert smallest_n(0.92, 0.01) == 56 and 0.92 ** 55 > 0.01  # strict: 0.92^n < 0.01
num("3.75", G.var(.4)); num("0.36", G.sf(2, .4))
num("0.729", G.sf(8, .1) / G.sf(5, .1)); num("0.09", G.pmf(7, .1) / G.sf(5, .1))
num("0.51", G.cdf(2, .3)); assert G.median(.3) == 2
p = Fr(1, 3); assert (1 - p) / p ** 2 == 6; num("0.222", float((1 - p) * p))

# Exam 1
num("0.0277", G.pmf(10, .04), 3); num("0.360", G.sf(25, .04), 3); assert abs(G.mean(.04) - 25) < 1e-9; num("24.5", G.std(.04), 3)
assert abs(G.var(.04) - 600) < 1e-6
num("0.185", G.cdf(5, .04), 3); num("73.39", log(.05) / log(.96)); assert smallest_n(0.96, 0.05) == 74
# Exam 2
num("0.116", (5 / 6) ** 2 / 6, 3); assert abs(sum((1 / 6) * (25 / 36) ** k for k in range(400)) - 6 / 11) < 1e-12
num("0.162", G.sf(10, 1 / 6), 3)
# Exam 3
num("0.4096", G.sf(4, .2))
# Exam 4
num("0.1029", G.pmf(4, .3)); num("0.233", B.pmf(2, 10, .3), 3); assert abs(B.pmf(0, 10, .3) - G.sf(10, .3)) < 1e-12
num("0.0282", G.sf(10, .3), 3); num("3.33", G.mean(.3), 3); num("7.78", G.var(.3), 3)

print(f"as03 check: all {COUNT} stated values verified")
