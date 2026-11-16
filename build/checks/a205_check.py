"""Checks every number stated in content/a205.py (Type I/II errors, size and power)."""
import math
import sys
from pathlib import Path

from scipy.stats import binom, norm, poisson

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from content.a205 import POWER_TABLE, UNIT  # noqa: E402

FAILS = []


def chk(label, value, stated):
    dp = len(stated.split(".")[1]) if "." in stated else 0
    ok = abs(float(value) - float(stated)) <= 0.5 * 10 ** (-dp) + 1e-12
    print(("ok  " if ok else "FAIL"), label, round(float(value), 6), stated)
    if not ok:
        FAILS.append(label)


def eq(label, value, expected):
    ok = value == expected
    print(("ok  " if ok else "FAIL"), label, value, expected)
    if not ok:
        FAILS.append(label)


def sf3(x):
    return float(f"{x:.3g}")


ge = lambda d, x: d.sf(x - 1)


def upper_cr(dist, a):
    c = 0
    while dist.sf(c - 1) > a:
        c += 1
    return c


def lower_cr(dist, a):
    c = -1
    while dist.cdf(c + 1) <= a:
        c += 1
    return c


Z95, Z90, Z99 = norm.ppf(0.95), norm.ppf(0.90), norm.ppf(0.99)
chk("z 5%", Z95, "1.6449")
chk("z 10%", Z90, "1.2816")
chk("z 1%", Z99, "2.3263")

# Notes power table
eq("notes CR", upper_cr(poisson(5), 0.05), 10)
for lam, s in POWER_TABLE:
    chk(f"power table {lam}", ge(poisson(int(lam)), 10), s)

# Ex1
B = binom(20, 0.3)
eq("Ex1 CR", upper_cr(B, 0.05), 10)
chk("Ex1 size", ge(B, 10), "0.0480")
chk("Ex1 ge9", ge(B, 9), "0.1133")
chk("Ex1 typeII", binom.cdf(9, 20, 0.4), "0.7553")
chk("Ex1 power", ge(binom(20, 0.4), 10), "0.2447")
for p, s in [(0.5, "0.5881"), (0.6, "0.8725"), (0.7, "0.9829")]:
    chk(f"Ex1 power {p}", ge(binom(20, p), 10), s)
# Ex2
P5 = poisson(5)
chk("Ex2 cdf9", P5.cdf(9), "0.9682")
chk("Ex2 size", ge(P5, 10), "0.0318")
chk("Ex2 ge9", ge(P5, 9), "0.0681")
chk("Ex2 cdf9 l=8", poisson.cdf(9, 8), "0.7166")
chk("Ex2 power", ge(poisson(8), 10), "0.2834")
# Ex3
chk("Ex3 log ratio", math.log(0.05) / math.log(0.7), "8.40")
chk("Ex3 0.7^9", 0.7 ** 9, "0.0404")
chk("Ex3 0.7^8", 0.7 ** 8, "0.0576")
eq("Ex3 c", 1 + math.ceil(math.log(0.05) / math.log(0.7)), 10)
chk("Ex3 power", 0.9 ** 9, "0.387")
# Ex4
c = 50 + Z95 * 0.8
chk("Ex4 c", c, "51.316")
chk("Ex4 z", (c - 52) / 0.8, "-0.855")
chk("Ex4 typeII", norm.cdf((c - 52) / 0.8), "0.196")
chk("Ex4 power", 1 - norm.cdf((c - 52) / 0.8), "0.804")
# Ex5
chk("Ex5 sqrt n", 2 * (Z95 + Z90), "5.853")
chk("Ex5 n", (2 * (Z95 + Z90)) ** 2, "34.26")
eq("Ex5 n int", math.ceil((2 * (Z95 + Z90)) ** 2), 35)
n = 35
eq("Ex5 n=35 power>=0.9", 1 - norm.cdf((50 + Z95 * 4 / math.sqrt(n) - 52) / (4 / math.sqrt(n))) >= 0.9, True)
n = 34
eq("Ex5 n=34 power<0.9", 1 - norm.cdf((50 + Z95 * 4 / math.sqrt(n) - 52) / (4 / math.sqrt(n))) < 0.9, True)
# Ex6
chk("Ex6 size A", ge(binom(10, 0.1), 3), "0.0702")
chk("Ex6 size B", ge(binom(20, 0.1), 5), "0.0432")
chk("Ex6 power A .3", ge(binom(10, 0.3), 3), "0.6172")
chk("Ex6 power B .3", ge(binom(20, 0.3), 5), "0.7625")
chk("Ex6 power A .2", ge(binom(10, 0.2), 3), "0.3222")
chk("Ex6 power B .2", ge(binom(20, 0.2), 5), "0.3704")

# Practice
B = binom(10, 0.5)
eq("P2 CR", lower_cr(B, 0.05), 1)
chk("P2 size", B.cdf(1), "0.0107")
chk("P2 cdf2", B.cdf(2), "0.0547")
chk("P2 cdf1 p=.3", binom.cdf(1, 10, 0.3), "0.1493")
chk("P2 typeII", 1 - binom.cdf(1, 10, 0.3), "0.8507")
chk("P3a", ge(poisson(6), 9), "0.1528")
chk("P3b", ge(poisson(8), 9), "0.4075")
P8 = poisson(8)
chk("P4 cdf10", P8.cdf(10), "0.8159")
chk("P4 P0", P8.pmf(0), "0.0003")
chk("P4 typeII", P8.cdf(10) - P8.cdf(0), "0.8156")
eq("P5 no CR", 0.2 > 0.05, True)
c = 20 - Z99 * 0.75
chk("P6 c", c, "18.255")
chk("P6 z", (c - 18) / 0.75, "0.340")
chk("P6 typeII", 1 - norm.cdf((c - 18) / 0.75), "0.367")
chk("P7 z", 2 / math.sqrt(2.5), "1.265")
chk("P7", 1 - norm.cdf(2 / math.sqrt(2.5)), "0.103")
P2 = poisson(2)
eq("P9a CR", upper_cr(P2, 0.05), 6)
chk("P9a ge6", ge(P2, 6), "0.0166")
chk("P9a ge5", ge(P2, 5), "0.0527")
chk("P9a power", ge(poisson(3), 6), "0.0839")
eq("P9b CR", upper_cr(P8, 0.05), 14)
chk("P9b ge14", ge(P8, 14), "0.0342")
chk("P9b ge13", ge(P8, 13), "0.0638")
chk("P9b power", ge(poisson(12), 14), "0.3185")
B = binom(20, 0.3)
eq("P10 CR", upper_cr(B, 0.01), 12)
chk("P10 ge12", ge(B, 12), "0.0051")
chk("P10 ge11", ge(B, 11), "0.0171")
chk("P10 typeII", binom.cdf(11, 20, 0.4), "0.9435")
chk("P11a", 0.8 ** 9, "0.134")
chk("P11b root", 0.5 ** (1 / 9), "0.9259")
chk("P11b p", 1 - 0.5 ** (1 / 9), "0.0741")

# Section B
def two_stage(p):
    return ge(binom(10, p), 3) + binom.pmf(2, 10, p) * ge(binom(10, p), 2)


chk("B1 P(X>=3)", ge(binom(10, 0.1), 3), "0.0702")
chk("B1 P(X=2)", binom.pmf(2, 10, 0.1), "0.1937")
chk("B1 P(Y>=2)", ge(binom(10, 0.1), 2), "0.2639")
chk("B1 size 4dp", two_stage(0.1), "0.1213")
chk("B1 size", sf3(two_stage(0.1)), "0.121")
chk("B1 X>=3 p=.3", ge(binom(10, 0.3), 3), "0.6172")
chk("B1 X=2 p=.3", binom.pmf(2, 10, 0.3), "0.2335")
chk("B1 Y>=2 p=.3", ge(binom(10, 0.3), 2), "0.8507")
chk("B1 power", sf3(two_stage(0.3)), "0.816")
chk("B1 E(n)", 10 + 10 * binom.pmf(2, 10, 0.1), "11.937")
chk("B1 E(n) 3sf", sf3(10 + 10 * binom.pmf(2, 10, 0.1)), "11.9")
chk("B1 p=.2", two_stage(0.2), "0.511")
chk("B1 p=.4", two_stage(0.4), "0.948")
c = 500 - Z95 * 1
chk("B2 c", c, "498.355")
chk("B2 z", c - 497, "1.355")
chk("B2 typeII", 1 - norm.cdf(c - 497), "0.0877")
chk("B2 3.2897", 2 * Z95, "3.2897")
chk("B2 sqrt n", 4 * 2 * Z95 / 3, "4.386")
chk("B2 n", (4 * 2 * Z95 / 3) ** 2, "19.24")
eq("B2 n int", math.ceil((4 * 2 * Z95 / 3) ** 2), 20)
P6 = poisson(6)
eq("B3 CR", upper_cr(P6, 0.05), 11)
chk("B3 size", ge(P6, 11), "0.0426")
chk("B3 ge10", ge(P6, 10), "0.0839")
for lam, s in [(3, "0.0426"), (4, "0.1841"), (5, "0.4170"), (6, "0.6528")]:
    chk(f"B3 power {lam}", ge(poisson(2 * lam), 11), s)
chk("B4 log ratio", math.log(0.05) / math.log(0.75), "10.4")
eq("B4 c", 1 + math.ceil(math.log(0.05) / math.log(0.75)), 12)
chk("B4 size", 0.75 ** 11, "0.0422")
chk("B4 power", 0.9 ** 11, "0.314")

assert len(UNIT["practice"]) == len(UNIT["answers"]) == 12
assert len(UNIT["exam"]) == len(UNIT["exam_answers"]) == 4
print("\nALL OK" if not FAILS else f"\nFAILURES: {FAILS}")
sys.exit(1 if FAILS else 0)
