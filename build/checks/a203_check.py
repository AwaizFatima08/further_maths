"""Recomputes every number stated in content/a203.py (Unit A2.3) and checks it appears in the unit text."""
import os
import sys
from math import ceil, comb, floor, log, sqrt

from scipy import stats

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.a203 import UNIT  # noqa: E402


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
    global COUNT
    if sf:
        assert float(f"{v:.{sf}g}") == float(s), f"{s} != {v}"
    else:
        d = len(s.split(".")[1]) if "." in s else 0
        assert abs(round(float(v), d) - float(s)) < 1e-9, f"{s} != {v}"
    assert s in TEXT, f"{s} not found in unit text"
    COUNT += 1


B, P, G = stats.binom, stats.poisson, stats.geom


class NB:
    """Trials up to and including the r-th success (scipy's nbinom counts failures, so shift by r)."""

    @staticmethod
    def pmf(x, r, p):
        v = comb(x - 1, r - 1) * p ** r * (1 - p) ** (x - r)
        assert abs(v - stats.nbinom.pmf(x - r, r, p)) < 1e-12
        return v

    @staticmethod
    def cdf(x, r, p):
        return stats.nbinom.cdf(x - r, r, p)

    @staticmethod
    def mean(r, p):
        return stats.nbinom.mean(r, p) + r

    @staticmethod
    def var(r, p):
        return stats.nbinom.var(r, p)


def upper_cr(p0, alpha):
    """Smallest c with P(X >= c) <= alpha for X ~ Geo(p0)."""
    c = 1 + ceil(log(alpha) / log(1 - p0))
    assert G.sf(c - 1, p0) <= alpha + 1e-15 < G.sf(c - 2, p0)
    return c


def lower_cr(p0, alpha):
    """Largest c with P(X <= c) <= alpha (0 if none)."""
    c = floor(log(1 - alpha) / log(1 - p0))
    assert (c == 0 or G.cdf(c, p0) <= alpha) and G.cdf(c + 1, p0) > alpha
    return c


# Example 1
num("0.20736", NB.pmf(5, 3, .6)); num("0.207", NB.pmf(5, 3, .6), 3); assert NB.mean(3, .6) == 5
num("3.33", NB.var(3, .6), 3)
# Example 2
num("0.3758", B.cdf(1, 10, .2)); assert abs(1 - NB.cdf(10, 2, .2) - B.cdf(1, 10, .2)) < 1e-12
num("0.6554", B.cdf(1, 6, .2)); num("0.3446", NB.cdf(6, 2, .2)); num("0.34464", NB.cdf(6, 2, .2))
for x, s in zip(range(2, 7), ["0.04", "0.064", "0.0768", "0.08192", "0.08192"]):
    num(s, NB.pmf(x, 2, .2))
# Example 3
assert abs(NB.mean(4, 1 / 3) - 12) < 1e-9 and abs(NB.var(4, 1 / 3) - 24) < 1e-9
assert abs(G.mean(1 / 3) - 3) < 1e-12 and abs(G.var(1 / 3) - 6) < 1e-9
# Example 4
num("0.0798", G.sf(24, .1), 3); num("28.43", log(.05) / log(.9)); assert upper_cr(.1, .05) == 30
num("0.0523", .9 ** 28, 3); num("0.0471", .9 ** 29, 3)
# Example 5
num("2.58", log(.9) / log(.96)); assert lower_cr(.04, .1) == 2; num("0.0784", G.cdf(2, .04)); num("0.115", G.cdf(3, .04), 3)
# Example 6
assert lower_cr(.25, .05) == 0 and G.pmf(1, .25) > .05
num("10.41", log(.05) / log(.75)); assert upper_cr(.25, .05) == 12
num("0.0422", G.sf(11, .25), 3); num("0.0563", G.sf(10, .25), 3)

# Practice
num("0.15625", NB.pmf(6, 4, .5)); assert NB.mean(4, .5) == 8 and NB.var(4, .5) == 8
num("0.12348", NB.pmf(5, 2, .3)); num("0.123", NB.pmf(5, 2, .3), 3); num("0.6517", B.cdf(1, 4, .3)); num("0.3483", NB.cdf(4, 2, .3))
num("0.0465", NB.pmf(10, 3, 1 / 6), 3); assert abs(NB.mean(3, 1 / 6) - 18) < 1e-9 and abs(NB.var(3, 1 / 6) - 90) < 1e-9
assert abs(NB.mean(4, .4) - 10) < 1e-9 and abs(NB.var(4, .4) - 15) < 1e-9
num("0.6785", B.cdf(2, 8, .25)); assert abs(1 - NB.cdf(8, 3, .25) - B.cdf(2, 8, .25)) < 1e-12
num("8.40", log(.05) / log(.7)); assert upper_cr(.3, .05) == 10; num("0.0404", .7 ** 9, 3); num("0.0576", .7 ** 8, 3)
num("2.54", log(.95) / log(.98)); assert lower_cr(.02, .05) == 2; num("0.0396", G.cdf(2, .02), 3); num("0.0588", G.cdf(3, .02), 3)
num("0.0456", G.sf(19, .15), 3)
num("2.52", log(.975) / log(.99)); assert lower_cr(.01, .025) == 2; num("0.0199", G.cdf(2, .01), 3)
num("367.04", log(.025) / log(.99)); assert upper_cr(.01, .025) == 369; num("0.0248", G.sf(368, .01), 3)
num("0.0447", round(G.cdf(2, .01), 4) + round(G.sf(368, .01), 4))
for x, s in zip(range(3, 7), ["0.125", "0.1875", "0.1875", "0.15625"]):
    num(s, NB.pmf(x, 3, .5))
assert NB.pmf(7, 3, .5) < NB.pmf(6, 3, .5)
num("0.9489", P.cdf(7, 4)); num("0.0511", 1 - round(P.cdf(7, 4), 4))

# Exam 1
num("0.0604", NB.pmf(10, 3, .2), 3); assert abs(NB.mean(3, .2) - 15) < 1e-9 and abs(NB.var(3, .2) - 60) < 1e-9
num("7.75", sqrt(60), 3); num("0.2061", B.cdf(2, 20, .2)); assert abs(1 - NB.cdf(20, 3, .2) - B.cdf(2, 20, .2)) < 1e-12
num("0.685", 1 - (1 - round(B.cdf(2, 20, .2), 4)) ** 5, 3); num("0.685", 1 - (1 - B.cdf(2, 20, .2)) ** 5, 3)
# Exam 2
num("22.43", log(.05) / log(.875)); assert upper_cr(.125, .05) == 24
num("0.0464", .875 ** 23, 3); num("0.0692", G.sf(20, .125), 3); num("0.307", G.sf(23, .05), 3)
# Exam 3
assert lower_cr(.2, .05) == 0
num("13.43", log(.05) / log(.8)); assert upper_cr(.2, .05) == 15; num("0.0440", .8 ** 14, 3)
num("0.0687", G.sf(12, .2), 3)
num("0.0829", B.cdf(1, 19, .2), 3); assert abs(1 - NB.cdf(19, 2, .2) - B.cdf(1, 19, .2)) < 1e-12
# Exam 4
num("8.57", 3 / .35)
probs = {x: NB.pmf(x, 4, .35) for x in range(4, 60)}; assert max(probs, key=probs.get) == 9
for x in range(4, 30):
    assert abs(probs[x + 1] / probs[x] - x * .65 / (x - 3)) < 1e-12
num("11.4", NB.mean(4, .35), 3); num("21.2", NB.var(4, .35), 3); num("0.0975", NB.pmf(9, 4, .35), 3)

print(f"a203 check: all {COUNT} stated values verified")
