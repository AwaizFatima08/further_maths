"""Recomputes every number stated in content/as11.py and checks it appears in the unit text."""
import importlib
import math
import sys
from fractions import Fraction
from pathlib import Path

from scipy import integrate, optimize

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
MODULE = "as11"
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


# Worked example 1 and 2: f = kx^2 on [0, 2]
k = 1 / I(lambda x: x * x, 0, 2); okf(k, "3/8")
f = lambda x: k * x * x
okf(I(f, 1, 2), "7/8"); ok(I(f, 1, 2), "0.875")
ok(I(f, 0.5, 1.5), "0.40625")
ok(f(2), "1.5")
E = I(lambda x: x * f(x), 0, 2); E2 = I(lambda x: x * x * f(x), 0, 2)
ok(E, "1.5"); ok(E2, "2.4"); ok(E2 - E ** 2, "0.15"); ok(math.sqrt(E2 - E ** 2), "0.387")
ok(root(lambda m: I(f, 0, m) - 0.5, 0, 2), "1.59")
ok(root(lambda m: I(f, 0, m) - 0.25, 0, 2), "1.26")

# Worked example 3: triangular
f = lambda x: x / 6 if x <= 2 else (6 - x) / 12
assert abs(I(f, 0, 2) + I(f, 2, 6) - 1) < 1e-12
okf(f(2), "1/3")
okf(I(lambda x: x * f(x), 0, 2), "4/9"); okf(I(lambda x: x * f(x), 2, 6), "20/9")
E = I(lambda x: x * f(x), 0, 2) + I(lambda x: x * f(x), 2, 6); okf(E, "8/3"); ok(E, "2.67")
okf(I(lambda x: x * x * f(x), 0, 2), "2/3"); ok(I(lambda x: x * x * f(x), 2, 6), "8")
E2 = I(lambda x: x * x * f(x), 0, 2) + I(lambda x: x * x * f(x), 2, 6); okf(E2, "26/3")
okf(E2 - E ** 2, "14/9"); ok(E2 - E ** 2, "1.56")
m = root(lambda m: I(f, 0, 2) + I(f, 2, m) - 0.5, 2, 6); ok(m, "2.54"); assert abs(m - (6 - math.sqrt(12))) < 1e-9
okf(I(f, 4, 6), "1/6")

# Worked example 4: f = 2x/15 on [1, 4]
f = lambda x: 2 * x / 15
assert abs(I(f, 1, 4) - 1) < 1e-12
E = I(lambda x: x * f(x), 1, 4); E2 = I(lambda x: x * x * f(x), 1, 4)
ok(E, "2.8"); ok(E2, "8.5"); ok(E2 - E * E, "0.66"); ok(3 * E - 2, "6.4"); ok(9 * (E2 - E * E), "5.94")
E3 = I(lambda x: x ** 3 * f(x), 1, 4); ok(E3, "27.28"); ok(5 * E3, "136.4")
Ei = I(lambda x: f(x) / x, 1, 4); Ei2 = I(lambda x: f(x) / x ** 2, 1, 4)
ok(Ei, "0.4"); ok(Ei2, "0.1848"); ok(Ei2 - Ei ** 2, "0.024839", tol=1e-6); ok(36 * (Ei2 - Ei ** 2), "0.894")
ok(1 / E, "0.357")

# Worked example 5: f = (4/27) x^2 (3 - x)
f = lambda x: 4 / 27 * x * x * (3 - x)
assert abs(I(f, 0, 3) - 1) < 1e-12
mode = optimize.minimize_scalar(lambda x: -f(x), bounds=(0, 3), method="bounded").x; assert abs(mode - 2) < 1e-5
okf(f(2), "16/27")
E = I(lambda x: x * f(x), 0, 3); E2 = I(lambda x: x * x * f(x), 0, 3)
ok(E, "1.8"); ok(E2, "3.6"); ok(E2 - E * E, "0.36")
m = root(lambda m: m ** 4 - 4 * m ** 3 + 13.5, 0, 3); ok(m, "1.84"); assert abs(I(f, 0, m) - 0.5) < 1e-9
ok(I(f, 0, 1.835), "0.4955", tol=1e-4); ok(I(f, 0, 1.845), "0.5013", tol=1e-4)
okf(I(f, 0, 1), "1/9"); ok(I(f, 0, 1), "0.111")

# Worked example 6: mixed
c = 0.6 / 50; ok(c, "0.012")
ok(0.4 + c * 10, "0.52"); E = I(lambda x: c * x, 0, 50); E2 = I(lambda x: c * x * x, 0, 50)
ok(E, "15"); ok(E2, "500"); ok(E2 - E * E, "275"); ok(math.sqrt(E2 - E * E), "16.6"); ok(0.1 / 0.012, "8.33")

# Practice
k = 1 / I(lambda x: 1 + x, 0, 3); okf(k, "2/15"); ok(I(lambda x: k * (1 + x), 0, 1), "0.2")
f = lambda x: x / 2
okf(I(lambda x: x * f(x), 0, 2), "4/3"); ok(math.sqrt(2), "1.41"); ok(I(f, 1, 1.5), "0.3125")
f = lambda x: 3 * x * x
E = I(lambda x: x * f(x), 0, 1); okf(E, "3/4"); okf(I(lambda x: x * x * f(x), 0, 1) - E * E, "3/80")
f = lambda x: 2 * (1 - x)
okf(I(lambda x: x * f(x), 0, 1), "1/3"); ok(root(lambda m: I(f, 0, m) - 0.5, 0, 1), "0.293"); ok(1 + math.sqrt(0.5), "1.707")
k = 1 / I(lambda x: x ** -2, 1, 2); ok(k, "2")
f = lambda x: 2 / x ** 2
okf(I(f, 1.5, 2), "1/3"); ok(I(lambda x: x * f(x), 1, 2), "1.39"); okf(root(lambda m: I(f, 1, m) - 0.5, 1, 2), "4/3")
k = 1 / (I(lambda x: x, 0, 2) + 2 * 1); okf(k, "1/4")
f = lambda x: x / 4 if x <= 2 else 0.5
ok(I(f, 0, 2), "0.5"); E = I(lambda x: x * f(x), 0, 2) + I(lambda x: x * f(x), 2, 3)
okf(E, "23/12"); ok(E, "1.92")
f = lambda x: x * (4 - x * x) / 4
assert abs(I(f, 0, 2) - 1) < 1e-12
mode = optimize.minimize_scalar(lambda x: -f(x), bounds=(0, 2), method="bounded").x
ok(mode, "1.15", tol=0.005); ok(2 / math.sqrt(3), "1.15")
E = I(lambda x: x * f(x), 0, 2); okf(E, "16/15"); ok(E, "1.07")
f = lambda x: 3 * x * x / 7
Ei = I(lambda x: f(x) / x, 1, 2); Ei2 = I(lambda x: f(x) / x ** 2, 1, 2)
okf(Ei, "9/14"); okf(Ei2, "3/7"); ok(14 * Ei, "9"); okf(Ei2 - Ei ** 2, "3/196"); ok(196 * (Ei2 - Ei ** 2), "3")
ok(5 - 2 * 4, "-3"); ok(4 * 2, "8"); ok(2 + 16, "18"); ok(3 * 18 + 1, "55")
A = I(lambda x: (x - 1) * (5 - x), 1, 5); okf(A, "32/3"); k = 1 / A; okf(k, "3/32")
f = lambda x: k * (x - 1) * (5 - x)
okf(I(lambda x: (x - 1) * (5 - x), 1, 2), "5/3"); okf(I(f, 1, 2), "5/32"); ok(I(f, 1, 2), "0.15625")
E = I(lambda x: x * f(x), 1, 5); E2 = I(lambda x: x * x * f(x), 1, 5)
ok(E, "3"); ok(E2, "9.8"); ok(E2 - E * E, "0.8")
f = lambda x: x ** 3 / 4
assert abs(I(f, 0, 2) - 1) < 1e-12
q1 = root(lambda x: I(f, 0, x) - 0.25, 0, 2); q3 = root(lambda x: I(f, 0, x) - 0.75, 0, 2)
ok(q1, "1.41"); ok(q3, "1.86"); ok(q3, "1.8612"); ok(q1, "1.4142"); ok(q3 - q1, "0.447")
ok(root(lambda x: I(f, 0, x) - 0.9, 0, 2), "1.95")
f = lambda x: 0.008 * (10 - x)
ok(I(f, 0, 10), "0.4", tol=1e-12); ok(0.6 + I(f, 0, 10), "1"); ok(I(f, 5, 10), "0.1"); ok(0.008 * 12.5, "0.1")
E = I(lambda x: x * f(x), 0, 10); okf(E, "4/3"); ok(E, "1.33")

# Section B question 1
k = 1 / (I(lambda x: x * x, 0, 2) + I(lambda x: 6 - x, 2, 6)); okf(k, "3/32")
f = lambda x: k * x * x if x <= 2 else k * (6 - x)
okf(f(2), "3/8"); okf(I(f, 4, 6), "3/16"); ok(I(f, 4, 6), "0.1875")
okf(I(lambda x: 6 * x - x * x, 2, 6), "80/3")
E = I(lambda x: x * f(x), 0, 2) + I(lambda x: x * f(x), 2, 6); okf(E, "23/8"); ok(E, "2.875")
okf(I(f, 0, 2), "1/4")
m = root(lambda m: I(f, m, 6) - 0.5, 2, 6); ok(m, "2.73"); okf((6 - m) ** 2, "32/3")
# Section B question 2
k = 1 / I(lambda x: x ** -3, 1, 2); okf(k, "8/3")
f = lambda x: k / x ** 3
E = I(lambda x: x * f(x), 1, 2); okf(E, "4/3")
E2 = I(lambda x: x * x * f(x), 1, 2); assert abs(E2 - 8 / 3 * math.log(2)) < 1e-10
V = E2 - E * E; assert abs(V - (8 / 3 * math.log(2) - 16 / 9)) < 1e-10
ok(9 * V, "0.636"); assert abs(9 * V - (24 * math.log(2) - 16)) < 1e-10
Em3 = I(lambda x: f(x) / x ** 3, 1, 2); okf(Em3, "31/60"); ok(18 * Em3, "9.3")
m = root(lambda m: I(f, 1, m) - 0.5, 1, 2); okf(m * m, "8/5"); ok(m, "1.26")
# Section B question 3
f = lambda x: 4 / 81 * x * (9 - x * x)
assert abs(I(f, 0, 3) - 1) < 1e-12
mode = optimize.minimize_scalar(lambda x: -f(x), bounds=(0, 3), method="bounded").x; assert abs(mode - math.sqrt(3)) < 1e-5
E = I(lambda x: x * f(x), 0, 3); E2 = I(lambda x: x * x * f(x), 0, 3)
okf(E, "8/5"); ok(E2, "3"); ok(E2 - E * E, "0.44")
m = root(lambda m: m ** 4 - 18 * m * m + 40.5, 0, 3); assert abs(I(f, 0, m) - 0.5) < 1e-9
ok(m * m, "2.636", tol=5e-4); ok(m, "1.62")
assert math.sqrt(9 + math.sqrt(40.5)) > 3
p = I(f, 2, 3); okf(p, "25/81"); ok(p, "0.309"); okf(I(f, 0, 2), "56/81")
# Section B question 4
k = 0.75 / I(lambda x: 4 - x, 0, 4); okf(k, "3/32"); ok(k, "0.09375")
f = lambda x: k * (4 - x)
ok(I(f, 0, 1), "0.328125"); ok(0.25 + I(f, 0, 1), "0.578")
E = I(lambda x: x * f(x), 0, 4); E2 = I(lambda x: x * x * f(x), 0, 4)
ok(E, "1"); ok(E2, "2"); ok(E2 - E * E, "1")
okf(I(lambda x: 4 * x - x * x, 0, 4), "32/3"); okf(I(lambda x: 4 * x * x - x ** 3, 0, 4), "64/3")
m = root(lambda m: 0.25 + I(f, 0, m) - 0.5, 0, 4); ok(m, "0.734"); assert abs(m - (4 - math.sqrt(32 / 3))) < 1e-9

print(f"{MODULE}: all {COUNT} checks passed")
