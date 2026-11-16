"""Checks every number stated in content/a206.py (linear combinations of random variables).

Probabilities are computed from the exact distributions; a Monte Carlo simulation also checks
that the mean/variance rules are applied correctly in the examples.
"""
import math
import sys
from pathlib import Path

import numpy as np
from scipy.stats import binom, norm, poisson

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from content.a206 import UNIT  # noqa: E402

FAILS = []
Phi = norm.cdf
rng = np.random.default_rng(1)
N = 2_000_000


def chk(label, value, stated):
    dp = len(stated.split(".")[1]) if "." in stated else 0
    ok = abs(float(value) - float(stated)) <= 0.5 * 10 ** (-dp) + 1e-12
    print(("ok  " if ok else "FAIL"), label, round(float(value), 6), stated)
    if not ok:
        FAILS.append(label)


def sim(label, samples, mean, var, rel=0.01):
    m, v = samples.mean(), samples.var()
    ok = abs(m - mean) <= rel * max(1, abs(mean)) and abs(v - var) <= rel * 3 * var
    print(("ok  " if ok else "FAIL"), "sim", label, round(m, 4), mean, round(v, 4), var)
    if not ok:
        FAILS.append("sim " + label)


s = math.sqrt
# Ex1
chk("Ex1 E", 3 * 4 - 2 * 3 + 1, "7")
chk("Ex1 Var", 9 * 2.4 + 4 * 3, "33.6")
sim("Ex1", 3 * rng.binomial(10, 0.4, N) - 2 * rng.poisson(3, N) + 1, 7, 33.6)
# Ex2
chk("Ex2a", 1 - Phi(1), "0.159")
chk("Ex2b z", 30 / s(450), "1.414")
chk("Ex2b", 1 - Phi(30 / s(450)), "0.0786")
x = rng.normal(500, 15, (N, 2))
chk("Ex2a sim", (2 * x[:, 0] > 1030).mean(), "0.16")
chk("Ex2b sim", (x.sum(1) > 1030).mean(), "0.08")
# Ex3
chk("Ex3 z", 2 / s(13), "0.555")
chk("Ex3", Phi(2 / s(13)), "0.710")
chk("Ex3 5dp", Phi(2 / s(13)), "0.71045")
# Ex4
chk("Ex4 z", 50 / s(1440), "1.318")
chk("Ex4", 1 - Phi(50 / s(1440)), "0.0938")
# Ex5
chk("Ex5 var", 4 * 400 + 9 * 625, "7225")
chk("Ex5 z", 60 / 85, "0.706")
chk("Ex5", Phi(60 / 85), "0.760")
d = rng.normal(150, 20, (N, 4)).sum(1) - 3 * rng.normal(180, 25, N)
sim("Ex5", d, 60, 7225)
# Ex6
chk("Ex6 cdf7", poisson.cdf(7, 5), "0.8666")
chk("Ex6", poisson.sf(7, 5), "0.1334")
sim("Ex6 X-Y", rng.poisson(3, N) - rng.poisson(2, N), 1, 5)

# Practice
chk("P1 E", 2 * 5 - 3 * 3 + 4, "5")
chk("P1 Var", 4 * 2 + 9 * 4, "44")
chk("P2 z", 0.2 / s(0.03), "1.155")
chk("P2", 1 - Phi(0.2 / s(0.03)), "0.124")
chk("P3", Phi(-1), "0.159")
chk("P4 z", -3 / s(13), "-0.832")
chk("P4", Phi(-3 / s(13)), "0.203")
sim("P6 2X", 2 * rng.poisson(4, N), 8, 16)
sim("P6 X1+X2", rng.poisson(4, N) + rng.poisson(4, N), 8, 8)
chk("P7", 1 - Phi(2 / 2), "0.159")
chk("P8 z", 10 / s(52), "1.387")
chk("P8", Phi(10 / s(52)), "0.917")
dice = rng.integers(1, 7, (N, 3))
sim("P9 S", dice.sum(1), 10.5, 8.75)
sim("P9 T", 3 * dice[:, 0], 10.5, 26.25)
chk("P10a", poisson.pmf(3, 4), "0.1954")
chk("P10b", poisson.cdf(5, 8), "0.1912")
z99 = norm.ppf(0.99)
chk("P11 z", z99, "2.3263")
chk("P11 16+s2", (10 / z99) ** 2, "18.48")
chk("P11 s2", (10 / z99) ** 2 - 16, "2.48")
chk("P11 s", s((10 / z99) ** 2 - 16), "1.57")
sig = s((10 / z99) ** 2 - 16)
chk("P11 check overflow prob", Phi(-10 / s(16 + sig ** 2)), "0.0100")
chk("P12", 4 * 3 + 5, "17")

# Section B
chk("B1 E", 40 + 24 * 20, "520")
chk("B1 Var", 9 + 24 * 1.44, "43.56")
chk("B1 sd", s(43.56), "6.6")
chk("B1b z", -10 / 6.6, "-1.515")
chk("B1b", Phi(-10 / 6.6), "0.0649")
chk("B1c", 520 - norm.ppf(0.95) * 6.6, "509")
chk("B1d z", 5 / s(87.12), "0.536")
chk("B1d", 2 * (1 - Phi(5 / s(87.12))), "0.592")
tot = rng.normal(40, 3, N) + rng.normal(20, 1.2, (N, 24)).sum(1)
sim("B1 T", tot, 520, 43.56)
chk("B2 VarX", 12 * 0.25 * 0.75, "2.25")
chk("B2 VarT", 36 / 12, "3")
chk("B2b Var", 2.25 + 4 * 3, "14.25")
sim("B2b", rng.binomial(12, 0.25, N) + 2 * rng.uniform(0, 6, N), 9, 14.25)
chk("B2c", 2.25 + 3, "5.25")
chk("B3a z", 7 / s(13), "1.941")
chk("B3a", 1 - Phi(7 / s(13)), "0.0261")
chk("B3b var", 9 + 2.25 * 4, "18")
chk("B3b z", 3 / s(18), "0.707")
chk("B3b", Phi(3 / s(18)), "0.760")
chk("B3c z", 1 / s(0.8), "1.118")
chk("B3c", 1 - Phi(1 / s(0.8)), "0.132")
chk("B3d", 5 * 4, "20")
sdD = s(0.34)
chk("B4a sd", sdD, "0.5831")
chk("B4a z", 0.8 / sdD, "1.372")
pfit = Phi(0.8 / sdD)
chk("B4a", pfit, "0.915")
chk("B4b z", 0.7 / sdD, "1.200")
chk("B4b", Phi(0.7 / sdD) - Phi(-0.8 / sdD), "0.800")
chk("B4c z", 1 / s(1.75), "0.756")
chk("B4c", Phi(1 / s(1.75)), "0.775")
chk("B4d exact p", binom.sf(8, 10, pfit), "0.793")
chk("B4d p=0.915", 0.915 ** 10 + 10 * 0.915 ** 9 * 0.085, "0.793")

assert len(UNIT["practice"]) == len(UNIT["answers"]) == 12
assert len(UNIT["exam"]) == len(UNIT["exam_answers"]) == 4
print("\nALL OK" if not FAILS else f"\nFAILURES: {FAILS}")
sys.exit(1 if FAILS else 0)
