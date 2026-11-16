"""Checks every number stated in content/a204.py (probability generating functions).

PGF facts are checked two ways: from the probability distribution directly (E(X), E[X(X-1)], pmf values)
and by numerically differentiating the PGF formula stated in the text.
"""
import math
import sys
from fractions import Fraction as F
from pathlib import Path

import numpy as np
from scipy.stats import binom, nbinom, poisson

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from content.a204 import UNIT  # noqa: E402

FAILS = []


def chk(label, value, stated, tol=None):
    stated_f = float(F(stated)) if "/" in stated else float(stated)
    if tol is None:
        dp = len(stated.split(".")[1]) if "." in stated else 0
        tol = 0.5 * 10 ** (-dp) + 1e-9 if "/" not in stated else 1e-9
    ok = abs(float(value) - stated_f) <= tol
    print(("ok  " if ok else "FAIL"), label, round(float(value), 8), stated)
    if not ok:
        FAILS.append(label)


def d1(G, t=1.0, h=1e-5):
    return (G(t + h) - G(t - h)) / (2 * h)


def d2(G, t=1.0, h=1e-4):
    return (G(t + h) - 2 * G(t) + G(t - h)) / h ** 2


def moments(G, label, mean, gpp, var, tol=1e-4):
    """Check G(1)=1, G'(1), G''(1) and variance by numerical differentiation of the PGF formula."""
    chk(label + " G(1)", G(1.0), "1", tol)
    chk(label + " G'(1)", d1(G), mean, tol)
    if gpp is not None:
        chk(label + " G''(1)", d2(G), gpp, 1e-3)
    chk(label + " Var", d2(G) + d1(G) - d1(G) ** 2, var, 1e-3)


def coeffs(G, n, r=0.5, m=64):
    """Taylor coefficients of G at 0 up to t^n, via FFT on a circle of radius r."""
    z = r * np.exp(2j * np.pi * np.arange(m) / m)
    c = np.fft.fft(np.array([G(x) for x in z])) / m
    return [(c[k] / r ** k).real for k in range(n + 1)]


# ---------- Notes ----------
for n in [3, 6, 10]:
    xs = np.arange(1, n + 1)
    chk(f"uniform n={n} mean", xs.mean(), str(F(n + 1, 2)))
    chk(f"uniform n={n} G''(1)", (xs * (xs - 1)).mean(), str(F((n - 1) * (n + 1), 3)))
    chk(f"uniform n={n} var", xs.var(), str(F(n * n - 1, 12)))
    moments(lambda t, n=n: sum(t ** k for k in range(1, n + 1)) / n, f"uniform PGF n={n}",
            str(F(n + 1, 2)), None, str(F(n * n - 1, 12)))
for n, p in [(5, 0.3), (8, 0.65)]:
    moments(lambda t: (1 - p + p * t) ** n, f"binomial {n},{p}", str(n * p), str(n * (n - 1) * p * p), str(n * p * (1 - p)))
for lam in [0.7, 3.2]:
    moments(lambda t: math.exp(lam * (t - 1)), f"poisson {lam}", str(lam), str(lam * lam), str(lam))
for p in [0.25, 0.6]:
    q = 1 - p
    moments(lambda t: p * t / (1 - q * t), f"geometric {p}", str(1 / p), str(2 * q / p ** 2), str(q / p ** 2))
    for r in [2, 3]:
        moments(lambda t: (p * t / (1 - q * t)) ** r, f"negbin r={r},{p}", str(r / p), None, str(r * q / p ** 2))
        # pmf check: C(x-1, r-1) p^r q^(x-r) equals scipy nbinom (failures = x - r)
        for x in range(r, r + 5):
            chk(f"negbin pmf r={r} x={x}", math.comb(x - 1, r - 1) * p ** r * q ** (x - r),
                f"{nbinom.pmf(x - r, r, p):.12f}")
# aX+b example in notes: X~B(5,0.2), Y=2X+3
G = lambda t: t ** 3 * (0.8 + 0.2 * t ** 2) ** 5
moments(G, "notes 2X+3", "5", None, "3.2")
# t^2(1+t)^3/8 is 2 + B(3, 1/2)
c = coeffs(lambda t: t ** 2 * (1 + t) ** 3 / 8, 5)
for k in range(6):
    chk(f"shift coeff {k}", c[k], f"{(binom.pmf(k - 2, 3, 0.5) if k >= 2 else 0):.10f}", 1e-9)
# expansions in 4.6
chk("4.6 binomial coeff", math.comb(4, 2) * (2 / 3) ** 2 * (1 / 3) ** 2, "8/27")
c = coeffs(lambda t: 1 / (4 - 3 * t), 6)
for r in range(7):
    chk(f"4.6 1/(4-3t) coeff {r}", c[r], f"{0.25 * 0.75 ** r:.12f}", 1e-9)

# ---------- Examples ----------
G = lambda t: 0.1 * t + 0.2 * t ** 2 + 0.3 * t ** 3 + 0.4 * t ** 4
moments(G, "Ex1", "3", "7", "1")
k = F(1, 81)
chk("Ex2 k", k * 3 ** 4, "1")
chk("Ex2 P(X=2)", binom.pmf(2, 4, 2 / 3), "8/27")
chk("Ex2 P(X=2) 3sf", binom.pmf(2, 4, 2 / 3), "0.296")
c = coeffs(lambda t: (1 + 2 * t) ** 4 / 81, 4)
chk("Ex2 coeff", c[2], "24/81")
moments(lambda t: (1 + 2 * t) ** 4 / 81, "Ex2", "8/3", None, "8/9")
G = lambda t: (0.3 + 0.7 * t) ** 3 * math.e ** (t - 1)
c = coeffs(lambda t: (0.3 + 0.7 * t) ** 3 * np.exp(t - 1), 2)
conv = np.convolve(binom.pmf(np.arange(4), 3, 0.7), poisson.pmf(np.arange(10), 1))
chk("Ex4 P(T=0)", conv[0], "0.0099")
chk("Ex4 P(T=0) via coeff", c[0], "0.0099")
chk("Ex4 0.027e^-1", 0.027 / math.e, "0.0099")
chk("Ex4 P(T=1)", conv[1], "0.0795")
chk("Ex4 0.216e^-1", 0.216 / math.e, "0.0795")
chk("Ex4 0.189", 3 * 0.3 ** 2 * 0.7, "0.189")
moments(G, "Ex4", "3.1", None, str(3 * 0.7 * 0.3 + 1))
G = lambda t: t * math.exp(2 * (t ** 3 - 1))
moments(G, "Ex5", "7", "60", "18")
moments(lambda t: (0.4 * t / (1 - 0.6 * t)) ** 3, "Ex6", "7.5", None, "11.25")
chk("Ex6 P(X=5)", nbinom.pmf(2, 3, 0.4), "0.138")
chk("Ex6 product", 6 * 0.064 * 0.36, "0.13824")

# ---------- Practice ----------
moments(lambda t: (t + 2 * t ** 2 + 3 * t ** 3) / 6, "P1", "7/3", "11/3", "5/9")
moments(lambda t: (0.5 + 0.5 * t) ** 4, "P2", "2", None, "1")
moments(lambda t: 0.4 * t / (1 - 0.6 * t), "P3", "2.5", None, str(0.6 / 0.16))
chk("P5", binom.pmf(2, 5, 0.5), "0.3125")
chk("P6", poisson.pmf(4, 4), "0.1954")
moments(lambda t: sum(t ** k for k in range(1, 7)) / 6, "P7", "3.5", "35/3", "35/12")
moments(lambda t: 1 / (4 - 3 * t), "P8", "3", "18", "12")
chk("P9 k", F(1, 8) * 8, "1")
c = coeffs(lambda t: t ** 2 * (1 + t) ** 3 / 8, 5)
chk("P9 P(X=3)", c[3], "3/8")
moments(lambda t: t ** 2 * (1 + t) ** 3 / 8, "P9", "3.5", None, "0.75")
moments(lambda t: t ** 3 * (0.8 + 0.2 * t ** 2) ** 5, "P10", "5", None, "3.2")

# ---------- Section B ----------
G1 = lambda t: 0.25 * t * (1 + t) ** 2
c = coeffs(G1, 3)
for k_, s in zip(range(4), ["0", "0.25", "0.5", "0.25"]):
    chk(f"B1 P(X={k_})", c[k_], s, 1e-9)
GS = lambda t: t ** 2 * (1 + t) ** 4 / 16
c = coeffs(GS, 6)
chk("B1 P(S=4)", c[4], "3/8")
moments(GS, "B1 S", "4", "13", "1")
moments(lambda t: (0.3 * t / (1 - 0.7 * t)) ** 3, "B2", "10", None, "70/3")
chk("B2 var 3sf", 3 * 0.7 / 0.09, "23.3")
chk("B2 P(X=5)", nbinom.pmf(2, 3, 0.3), "0.0794")
chk("B3 k", F(1, 256) * 4 ** 4, "1")
GY = lambda t: t * (3 + t ** 2) ** 4 / 256
c = coeffs(GY, 9)
chk("B3 P(Y=5)", c[5], "27/128")
chk("B3 P(Y=5) 3sf", binom.pmf(2, 4, 0.25), "0.211")
moments(GY, "B3", "3", "9", "3")
GT = lambda t: math.exp(2 * (t - 1)) * (1 + t + t ** 2) / 3
conv = np.convolve(poisson.pmf(np.arange(20), 2), [1 / 3] * 3)
chk("B4 P(T=0)", conv[0], "0.0451")
chk("B4 P(T=0) exact", math.exp(-2) / 3, "0.0451")
chk("B4 P(T=2)", conv[2], "0.226")
chk("B4 5e^-2/3", 5 * math.exp(-2) / 3, "0.226")
moments(GT, "B4", "3", "26/3", "8/3")

assert len(UNIT["practice"]) == len(UNIT["answers"]) == 12
assert len(UNIT["exam"]) == len(UNIT["exam_answers"]) == 4
print("\nALL OK" if not FAILS else f"\nFAILURES: {FAILS}")
sys.exit(1 if FAILS else 0)
