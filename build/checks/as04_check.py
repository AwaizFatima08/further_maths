"""Recomputes every number stated in content/as04.py (Unit AS4), by formula and by brute-force enumeration where feasible."""
import os
import sys
from fractions import Fraction as Fr
from itertools import combinations, permutations
from math import comb, factorial as f, perm

from scipy import stats

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.as04 import UNIT  # noqa: E402


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


def frac(s, v):
    global COUNT
    assert Fr(s) == Fr(v), f"{s} != {v}"
    assert s in TEXT, f"{s} not found in unit text"
    COUNT += 1


def arrangements(word):
    return set(permutations(word))


def adjacent(seq, a, b):
    return any({seq[i], seq[i + 1]} == {a, b} for i in range(len(seq) - 1))


# Notes
num("336", perm(8, 3)); num("56", comb(8, 3)); num("360", len(arrangements("STRAIT")))
assert sum(1 for w in arrangements("STRAIT") if w[0] in "AI") == 120
tr = arrangements("TRAITS")
cons_together = sum(1 for w in tr if max(i for i, c in enumerate(w) if c not in "AI") - min(i for i, c in enumerate(w) if c not in "AI") == 3)
num("72", cons_together); num("12", f(4) // 2)
num("840", comb(6, 2) * comb(8, 3))
frac("5/21", Fr(comb(4, 3) * comb(6, 2), comb(10, 5))); num("252", comb(10, 5))
tiles = list(range(10)); vowels = {1, 4, 6, 8}  # C A L C U L A T O R: A, U, A, O at positions 1, 4, 6, 8
assert sum(1 for s in combinations(tiles, 5) if len(vowels & set(s)) == 3) == 60
assert comb(6, 2) + comb(6, 3) == comb(7, 3)

# Example 1
num("50400", f(10) // (f(3) * f(3) * f(2))); num("3628800", f(10)); num("3360", f(8) // (f(3) * f(2)))
frac("1/15", Fr(3360, 50400)); num("0.0667", 1 / 15)
# Example 2
num("240", sum(1 for w in tr if not adjacent(w, "A", "I"))); num("120", sum(1 for w in tr if adjacent(w, "A", "I")))
assert perm(5, 2) == 20 and 72 / 360 == 0.2
# Example 3
frac("31/42", 1 - Fr(comb(6, 5) + comb(4, 1) * comb(6, 4), comb(10, 5))); num("0.738", 31 / 42)
# Example 4 done above; 0.238
num("0.238", 5 / 21)
# Example 5: brute force over 8! seatings
people = "ABCDEFGH"
good = tot_c = 0
for s in permutations(people):
    if s[0] == "C" or s[-1] == "C":
        tot_c += 1
        if not adjacent(s, "A", "B"):
            good += 1
num("10080", tot_c); num("2880", tot_c - good); num("7200", good); frac("5/28", Fr(good, f(8))); num("0.179", good / f(8))
# Example 6
num("0.201", stats.binom.pmf(3, 10, .2)); assert comb(10, 3) == 120
circ = [s for s in permutations(range(6)) if s[0] == 0]  # fix person 0 to remove rotations
assert len(circ) == 120
adj = sum(1 for s in circ if (s.index(2) - s.index(1)) % 6 in (1, 5)); assert adj == 48; num("0.4", adj / 120)

# Practice
num("210", perm(7, 3)); num("126", comb(9, 4))
ban = arrangements("BANANA"); assert len(ban) == 60; frac("1/6", Fr(sum(1 for w in ban if w[0] == "B"), 60))
num("840", perm(7, 4)); num("360", sum(1 for s in permutations("1234567", 4) if int(s[-1]) % 2 == 0)); frac("3/7", Fr(360, 840))
num("495", comb(12, 4)); frac("14/33", Fr(comb(5, 2) * comb(7, 2), comb(12, 4))); num("0.424", 14 / 33)
frac("1/3", Fr(120, 360))
seven = list(permutations(range(7)))
tog = sum(1 for s in seven if max(s.index(i) for i in range(3)) - min(s.index(i) for i in range(3)) == 2)
num("720", tog); frac("1/7", Fr(tog, 5040))
apart = sum(1 for s in seven if all(abs(s.index(i) - s.index(j)) > 1 for i in range(3) for j in range(i + 1, 3)))
num("1440", apart); frac("2/7", Fr(apart, 5040))
frac("3/44", Fr(comb(5, 3) + comb(4, 3) + 1, comb(12, 3))); num("0.0682", 3 / 44)
frac("3/11", Fr(5 * 4 * 3, comb(12, 3))); num("0.273", 3 / 11)
assert comb(10, 2) == 45
par = arrangements("PARALLEL"); num("3360", len(par))
ll = sum(1 for w in par if "".join(w).find("LLL") >= 0); assert ll == 360; frac("3/28", Fr(ll, len(par))); num("0.107", 3 / 28)
num("13983816", comb(49, 6)); num("246820", comb(6, 3) * comb(43, 3)); num("12341", comb(43, 3))
num("0.0177", comb(6, 3) * comb(43, 3) / comb(49, 6))
num("5040", f(7)); frac("2/7", Fr(2 * f(6), f(7)))

# Exam 1
arr = arrangements("ARRANGE"); num("1260", len(arr))
assert sum(1 for w in arr if w[0] == "R" and w[-1] == "R") == 60
aa = sum(1 for w in arr if "AA" in "".join(w)); assert aa == 360
frac("5/7", 1 - Fr(aa, len(arr))); num("0.714", 5 / 7)
t = list(range(7)); rr = {1, 2}  # tiles A R R A N G E
assert sum(1 for s in combinations(t, 4) if rr <= set(s)) == 10 and comb(7, 4) == 35
frac("2/7", Fr(10, 35)); num("0.286", 2 / 7)
# Exam 2
num("2002", comb(14, 5)); num("560", comb(6, 3) * comb(8, 2)); frac("40/143", Fr(560, 2002)); num("0.280", 40 / 143)
frac("139/143", 1 - Fr(comb(8, 5), 2002)); num("0.972", 139 / 143)
num("990", 2 * comb(12, 4)); frac("45/91", Fr(990, 2002)); num("0.495", 45 / 91)
dist = {k: Fr(comb(6, k) * comb(8, 5 - k), 2002) for k in range(6)}
for k, s in zip(range(5), ["28/1001", "210/1001", "420/1001", "280/1001", "60/1001"]):
    assert dist[k] == Fr(s) and s in TEXT
frac("3/1001", dist[5]); e = sum(k * p for k, p in dist.items()); frac("15/7", e); frac("2145/1001", e); num("2.14", 15 / 7)
# Exam 3: B = boys 0-3, G = girls 4-6
girls = {4, 5, 6}
gt = sum(1 for s in seven if max(s.index(g) for g in girls) - min(s.index(g) for g in girls) == 2); assert gt == 720
ga = sum(1 for s in seven if all(abs(s.index(a) - s.index(b)) > 1 for a in girls for b in girls if a < b)); assert ga == 1440
alt = sum(1 for s in seven if all((x in girls) == (i % 2 == 1) for i, x in enumerate(s))); num("144", alt)
ends = sum(1 for s in seven if s[0] not in girls and s[-1] not in girls); assert ends == 1440; frac("2/7", Fr(ends, 5040))
# Exam 4
d = {k: Fr(comb(3, k) * comb(7, 4 - k), comb(10, 4)) for k in range(4)}
assert d[1] == Fr(1, 2) and d[0] == Fr(1, 6) and d[2] == Fr(3, 10) and d[3] == Fr(1, 30)
m = sum(k * p for k, p in d.items()); m2 = sum(k * k * p for k, p in d.items())
num("1.2", m); assert m2 == 2; num("0.56", m2 - m * m); num("0.4116", stats.binom.pmf(1, 4, .3))

print(f"as04 check: all {COUNT} stated values verified")
