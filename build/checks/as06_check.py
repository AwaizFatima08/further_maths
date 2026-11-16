"""Checks every number stated in content/as06.py (binomial and Poisson hypothesis tests)."""
import sys
from pathlib import Path

from scipy.stats import binom, poisson

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from content.as06 import PO4_TABLE, UNIT  # noqa: E402

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


def upper_cr(dist, a):
    """Smallest c with P(X >= c) <= a."""
    c = 0
    while dist.sf(c - 1) > a:
        c += 1
    return c


def lower_cr(dist, a):
    """Largest c with P(X <= c) <= a (-1 if empty)."""
    c = -1
    while dist.cdf(c + 1) <= a:
        c += 1
    return c


ge = lambda d, x: d.sf(x - 1)  # P(X >= x)

# Notes table Po(4)
P4 = poisson(4)
for x, pm, cd, up in PO4_TABLE:
    x = int(x)
    chk(f"table pmf {x}", P4.pmf(x), pm)
    chk(f"table cdf {x}", P4.cdf(x), cd)
    chk(f"table ge {x}", ge(P4, x), up)
eq("notes upper CR", upper_cr(P4, 0.05), 9)
eq("notes lower CR", lower_cr(P4, 0.05), 0)
eq("notes two-tail upper", upper_cr(P4, 0.025), 9)
eq("notes two-tail lower", lower_cr(P4, 0.025), 0)
chk("notes two-tail size", P4.cdf(0) + ge(P4, 9), "0.0397")

# Ex1
B = binom(20, 0.25)
chk("Ex1 cdf8", B.cdf(8), "0.9591")
chk("Ex1 p", ge(B, 9), "0.0409")
# Ex2
chk("Ex2 P0", P4.pmf(0), "0.0183")
chk("Ex2 P<=1", P4.cdf(1), "0.0916")
# Ex3
P9 = poisson(9)
chk("Ex3 cdf14", P9.cdf(14), "0.9585")
chk("Ex3 p", ge(P9, 15), "0.0415")
# Ex4
P8 = poisson(8)
chk("Ex4 cdf2", P8.cdf(2), "0.0138")
chk("Ex4 cdf3", P8.cdf(3), "0.0424")
chk("Ex4 cdf14", P8.cdf(14), "0.9827")
chk("Ex4 ge15", ge(P8, 15), "0.0173")
chk("Ex4 ge14", ge(P8, 14), "0.0342")
eq("Ex4 CR", (lower_cr(P8, 0.025), upper_cr(P8, 0.025)), (2, 15))
chk("Ex4 size", P8.cdf(2) + ge(P8, 15), "0.0310")
chk("Ex4 size rounded-sum", 0.0138 + 0.0173, "0.0311")
# Ex5
B = binom(20, 0.4)
chk("Ex5 cdf3", B.cdf(3), "0.0160")
chk("Ex5 cdf4", B.cdf(4), "0.0510")
chk("Ex5 cdf12", B.cdf(12), "0.9790")
chk("Ex5 ge13", ge(B, 13), "0.0210")
chk("Ex5 ge12", ge(B, 12), "0.0565")
eq("Ex5 CR", (lower_cr(B, 0.05), upper_cr(B, 0.05)), (3, 13))
chk("Ex5 size", B.cdf(3) + ge(B, 13), "0.0370")
# Ex6
P10 = poisson(10)
chk("Ex6 p", P10.cdf(4), "0.0293")

# Practice
B = binom(20, 0.3)
chk("P1 cdf9", B.cdf(9), "0.9520")
chk("P1 ge10", ge(B, 10), "0.0480")
chk("P1 ge9", ge(B, 9), "0.1133")
eq("P1 CR", upper_cr(B, 0.05), 10)
B = binom(12, 1 / 6)
chk("P2 ge5", ge(B, 5), "0.0364")
chk("P2 ge4", ge(B, 4), "0.1252")
chk("P3 cdf8", P4.cdf(8), "0.9786")
chk("P3 ge9", ge(P4, 9), "0.0214")
P5 = poisson(5)
chk("P4 cdf0", P5.cdf(0), "0.0067")
chk("P4 cdf1", P5.cdf(1), "0.0404")
chk("P4 ge11", ge(P5, 11), "0.0137")
chk("P4 ge10", ge(P5, 10), "0.0318")
eq("P4 CR", (lower_cr(P5, 0.025), upper_cr(P5, 0.025)), (0, 11))
chk("P4 size", P5.cdf(0) + ge(P5, 11), "0.0204")
chk("P6", poisson(6).cdf(2), "0.0620")
chk("P7", binom(15, 0.5).cdf(3), "0.0176")
chk("P8", P9.cdf(4), "0.0550")
P25 = poisson(2.5)
chk("P9 cdf5", P25.cdf(5), "0.9580")
chk("P9 ge6", ge(P25, 6), "0.0420")
chk("P9 ge5", ge(P25, 5), "0.1088")
eq("P9 CR", upper_cr(P25, 0.05), 6)
B = binom(10, 0.5)
eq("P10 cdf1 exact", round(B.cdf(1) * 1024), 11)
eq("P10 cdf2 exact", round(B.cdf(2) * 1024), 56)
chk("P10 cdf1", B.cdf(1), "0.0107")
chk("P10 cdf2", B.cdf(2), "0.0547")
eq("P10 CR", lower_cr(B, 0.05), 1)
P3 = poisson(3)
chk("P11 cdf7", P3.cdf(7), "0.9881")
chk("P11 p", ge(P3, 8), "0.0119")

# Section B
P15 = poisson(1.5)
chk("B1 P0", P15.pmf(0), "0.2231")
chk("B1 cdf2", P15.cdf(2), "0.8088")
chk("B1 ge3", ge(P15, 3), "0.1912")
P75 = poisson(7.5)
chk("B1 cdf2", P75.cdf(2), "0.0203")
chk("B1 cdf3", P75.cdf(3), "0.0591")
chk("B1 ge14", ge(P75, 14), "0.0216")
chk("B1 ge13", ge(P75, 13), "0.0427")
eq("B1 CR", (lower_cr(P75, 0.025), upper_cr(P75, 0.025)), (2, 14))
chk("B1 size", P75.cdf(2) + ge(P75, 14), "0.0418")
chk("B1 size rounded-sum", 0.0203 + 0.0216, "0.0419")
chk("B2 a", poisson(3.5).cdf(4), "0.7254")
P7 = poisson(7)
chk("B2 ge13", ge(P7, 13), "0.0270")
chk("B2 ge12", ge(P7, 12), "0.0533")
eq("B2 CR", upper_cr(P7, 0.05), 13)
B = binom(25, 0.4)
chk("B3 cdf4", B.cdf(4), "0.0095")
chk("B3 cdf5", B.cdf(5), "0.0294")
chk("B3 ge16", ge(B, 16), "0.0132")
chk("B3 ge15", ge(B, 15), "0.0344")
eq("B3 CR", (lower_cr(B, 0.025), upper_cr(B, 0.025)), (4, 16))
chk("B3 size", B.cdf(4) + ge(B, 16), "0.0226")
chk("B3 size rounded-sum", 0.0095 + 0.0132, "0.0227")
P1 = poisson(1)
chk("B4 cdf2", P1.cdf(2), "0.9197")
chk("B4 ge3", ge(P1, 3), "0.0803")
chk("B4 cdf2 Po7", P7.cdf(2), "0.0296")
chk("B4 cdf3 Po7", P7.cdf(3), "0.0818")
eq("B4 CR", lower_cr(P7, 0.05), 2)

assert len(UNIT["practice"]) == len(UNIT["answers"]) == 12
assert len(UNIT["exam"]) == len(UNIT["exam_answers"]) == 4
print("\nALL OK" if not FAILS else f"\nFAILURES: {FAILS}")
sys.exit(1 if FAILS else 0)
