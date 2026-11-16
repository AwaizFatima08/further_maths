"""Recomputes every number stated in content/as02.py (Unit AS2) and checks it appears in the unit text."""
import os
import sys
from math import comb, exp, factorial

import numpy as np
from scipy import stats

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.as02 import UNIT  # noqa: E402


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


def num(s, v):
    global COUNT
    d = len(s.split(".")[1]) if "." in s else 0
    assert abs(round(float(v), d) - float(s)) < 1e-9, f"{s} != {v}"
    assert s in TEXT, f"{s} not found in unit text"
    COUNT += 1


B, P = stats.binom, stats.poisson
r4 = lambda v: round(v, 4)  # table precision

# Notes: n, p from mean and variance
assert abs(6 / 0.3 - 20) < 1e-12
# Notes table Po(3.5)
num("0.7254", P.cdf(4, 3.5)); num("0.5366", P.cdf(3, 3.5)); num("0.1359", P.cdf(1, 3.5))
num("0.8641", 1 - r4(P.cdf(1, 3.5))); num("0.2746", 1 - r4(P.cdf(4, 3.5))); num("0.8576", P.cdf(5, 3.5))
num("0.7217", r4(P.cdf(5, 3.5)) - r4(P.cdf(1, 3.5)))

# Example 1
num("0.6482", B.cdf(3, 15, .2)); num("0.8358", B.cdf(4, 15, .2)); num("0.1642", 1 - r4(B.cdf(4, 15, .2)))
num("0.9819", B.cdf(6, 15, .2)); num("0.3980", B.cdf(2, 15, .2)); num("0.5839", r4(B.cdf(6, 15, .2)) - r4(B.cdf(2, 15, .2)))
# Example 2
num("0.1042", P.pmf(6, 4)); num("0.6767", P.cdf(2, 2)); num("0.3233", 1 - r4(P.cdf(2, 2)))
num("0.8159", P.cdf(10, 8)); num("0.1841", 1 - r4(P.cdf(10, 8)))
# Example 3
num("0.2381", P.cdf(2, 4))
cond = P.pmf(2, 2.5) * P.pmf(2, 1.5) / P.pmf(4, 4)
assert abs(cond - B.pmf(2, 4, 0.625)) < 1e-12; num("0.3296", cond)
# Example 4
num("0.4232", P.cdf(2, 3)); assert abs(exp(-3) * (1 + 3 + 4.5) - P.cdf(2, 3)) < 1e-12; num("0.4215", B.cdf(2, 200, .015))
# Example 5
x = np.arange(6); f = np.array([14, 24, 21, 13, 6, 2])
assert (f * x).sum() == 139 and (f * x * x).sum() == 371
m = 139 / 80; v = 371 / 80 - m * m
num("1.7375", m); num("1.74", m); num("1.6186", v); num("1.62", v); num("0.1760", exp(-m)); num("14.1", 80 * r4(exp(-m)))
# Example 6
assert abs(4.2 / 6 - 0.7) < 1e-12

# Practice
num("0.2367", B.pmf(4, 12, .35)); num("0.5833", B.cdf(4, 12, .35)); num("0.9154", B.cdf(6, 12, .35)); num("0.0846", 1 - r4(B.cdf(6, 12, .35)))
assert abs(2.88 / 4.8 - 0.6) < 1e-12 and abs(4.8 / 0.4 - 12) < 1e-12
num("0.0821", P.pmf(0, 2.5)); num("0.2565", P.pmf(2, 2.5))
num("0.0498", P.pmf(0, 3))
num("0.1490", P.pmf(7, 7)); assert abs(exp(-7) * 7 ** 7 / factorial(7) - P.pmf(7, 7)) < 1e-12
num("0.4060", P.cdf(1, 2)); num("0.4046", B.cdf(1, 200, .01))
num("0.25", 3 / 12); num("6.5", 6.5); num("11.9", 143 / 12)
lam = 3; assert abs(P.pmf(2, lam) - P.pmf(3, lam)) < 1e-12; num("0.6472", P.cdf(3, 3)); assert abs(13 * exp(-3) - P.cdf(3, 3)) < 1e-12

# Exam 1
num("0.1339", P.pmf(4, 6)); num("0.5768", 1 - r4(P.cdf(2, 3))); num("0.1919", r4(1 - P.cdf(2, 3)) ** 3); num("0.1806", P.cdf(30, 36))
# Exam 2
num("0.5321", P.cdf(4, 4.5)); num("0.4679", 1 - r4(P.cdf(4, 4.5)))
c2 = P.pmf(2, 1.8) * P.pmf(4, 2.7) / P.pmf(6, 4.5); assert abs(c2 - B.pmf(2, 6, .4)) < 1e-12; num("0.3110", c2)
num("0.2705", P.cdf(19, 22.5))
# Exam 3
num("0.4209", B.cdf(2, 150, .02)); num("0.8153", P.cdf(4, 3)); q = 1 - r4(P.cdf(4, 3)); num("0.1847", q)
num("0.2940", B.pmf(1, 10, q)); assert abs(10 * q * (1 - q) ** 9 - B.pmf(1, 10, q)) < 1e-12
# Exam 4
x = np.arange(6); f = np.array([22, 33, 25, 13, 5, 2]); assert f.sum() == 100
assert (f * x).sum() == 152 and (f * x * x).sum() == 380
num("1.52", 1.52); num("1.4896", 3.8 - 1.52 ** 2); num("1.49", 3.8 - 1.52 ** 2)
num("0.2187", exp(-1.52)); num("21.9", 100 * exp(-1.52))

print(f"as02 check: all {COUNT} stated values verified")
