"""Checks every number and claim stated in pure/pc09.py (division, bases, Euclid, Bezout, tests, counting)."""
import itertools
import sys
from math import comb, factorial, gcd, isqrt, lcm, perm
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pure.pc09 import UNIT  # noqa: E402

N_OK = 0
FAILS = []


def ok(label, cond):
    global N_OK
    if cond:
        N_OK += 1
    else:
        FAILS.append(label)
        print("FAIL", label)


def divalg(a, b, q, r):
    ok(f"divalg {a}={b}*{q}+{r}", a == b * q + r and 0 <= r < b and divmod(a, b) == (q, r))


def euclid_lines(a, b):
    lines = []
    while b:
        q, r = divmod(a, b)
        lines.append((a, q, b, r))
        a, b = b, r
    return lines


def base(n, b):
    digits = "0123456789AB"
    s = ""
    while n:
        s = digits[n % b] + s
        n //= b
    return s


def dsum_alt(n):
    d = [int(c) for c in str(n)][::-1]
    return sum(x * (-1) ** i for i, x in enumerate(d))


def blocks(n):
    out = []
    while n:
        out.append(n % 1000)
        n //= 1000
    return out


# ---------- notes ----------
ok("6|42,-42,0, 6∤15", 42 % 6 == 0 and -42 % 6 == 0 and 15 % 6 != 0)
ok("8,15 coprime", gcd(8, 15) == 1)
ok("360 factor", sp.factorint(360) == {2: 3, 3: 2, 5: 1})
ok("756 factor", sp.factorint(756) == {2: 2, 3: 3, 7: 1})
ok("hcf 360 756", gcd(360, 756) == 36 and lcm(360, 756) == 7560 and 36 * 7560 == 272160 == 360 * 756)
divalg(-17, 5, -4, 3)
ok("38≡3 mod 5, -17≡3", 38 % 5 == 3 and -17 % 5 == 3 and 35 % 5 == 0)
ok("2626_7", int("2626", 7) == 1000 and 2 * 343 == 686 and 6 * 49 == 294)
ok("4A3_12", int("4A3", 12) == 699 == 4 * 144 + 120 + 3)
ok("1000 base 7 table", [divmod(x, 7) for x in (1000, 142, 20, 2)] == [(142, 6), (20, 2), (2, 6), (0, 2)])
ok("binary 1+1+1", 3 == int("11", 2) and 2 == int("10", 2))
ok("Euclid 1071 462", euclid_lines(1071, 462) == [(1071, 2, 462, 147), (462, 3, 147, 21), (147, 7, 21, 0)])
ok("Bezout 1071 462", 7 * 462 - 3 * 1071 == 21 and 3234 - 3213 == 21)
ok("6|4*9 but not 4,9", 36 % 6 == 0 and 4 % 6 and 9 % 6)
# divisibility test reasons
ok("10≡1 mod 9, ≡-1 mod 11", 10 % 9 == 1 and 10 % 11 == 10)
ok("1001=7*11*13", 1001 == 7 * 11 * 13 and 999 == 27 * 37 and 100 == 4 * 25 and 1000 == 8 * 125)
ok("tests brute force n < 200000", all((n % 9 == 0) == (sum(map(int, str(n))) % 9 == 0) and
       (n % 3 == 0) == (sum(map(int, str(n))) % 3 == 0) and
       (n % 11 == 0) == (dsum_alt(n) % 11 == 0) and (n % 4 == 0) == ((n % 100) % 4 == 0) and
       (n % 8 == 0) == ((n % 1000) % 8 == 0) and
       all((n % p == 0) == (sum(b * (-1) ** i for i, b in enumerate(blocks(n))) % p == 0) for p in (7, 11, 13)) and
       (n % 37 == 0) == (sum(blocks(n)) % 37 == 0) for n in range(1, 200000, 7)))
M = {7: -2, 13: 4, 17: -5, 19: 2, 23: 7, 29: 3, 31: -3, 37: -11, 41: -4, 43: 13, 47: -14}
for p, m in M.items():
    ok(f"10m≡1 mod {p}", (10 * m) % p == 1)
    ok(f"last-digit test {p}", all((n % p == 0) == ((n // 10 + m * (n % 10)) % p == 0) for n in range(1, 50000)))
ok("primes below 50 covered", sorted(set(sp.primerange(7, 50)) - {11}) == sorted(M))
ok("21, 39", 21 == 3 * 7 and 39 == 3 * 13 and (10 * -2) % 7 == 1 and 40 % 13 == 1)
# counting notes
ok("PIN", 10 ** 4 == 10000)
ok("3 or 5", (1000 // 3, 1000 // 5, 1000 // 15) == (333, 200, 66) and
   sum(1 for n in range(1, 1001) if n % 3 == 0 or n % 5 == 0) == 467)
ok("LETTER", factorial(6) // (2 * 2) == 180 ==
   len(set(itertools.permutations("LETTER"))))
ok("12P3 12C3", perm(12, 3) == 1320 and comb(12, 3) == 220 and perm(12, 3) == 6 * comb(12, 3))
ok("360 divisors", len(sp.divisors(360)) == 24)

# ---------- examples ----------
divalg(1000, 37, 27, 1)
divalg(-1000, 37, -28, 36)
ok("37*-28", 37 * -28 == -1036)
ok("1000 binary", bin(1000)[2:] == "1111101000" and 512 + 256 + 128 + 64 + 32 + 8 == 1000)
rem = []
x = 1000
while x:
    rem.append(x % 2)
    x //= 2
ok("binary remainders", rem == [0, 0, 0, 1, 0, 1, 1, 1, 1, 1])
ok("699 base 7", base(699, 7) == "2016" and [divmod(v, 7) for v in (699, 99, 14, 2)] == [(99, 6), (14, 1), (2, 0), (0, 2)])
ok("ex2 c", 50 % 21 != 0 and 1071 * -15 + 462 * 35 == 105 and 1071 * 15 == 16065 and 462 * 35 == 16170)
n = sp.symbols("n")
ok("3(2n+1)-2(3n+1)=1", sp.expand(3 * (2 * n + 1) - 2 * (3 * n + 1)) == 1)
ok("hcf(3n+1,2n+1)=1", all(gcd(3 * k + 1, 2 * k + 1) == 1 for k in range(-500, 500)))
ok("4|36, 4∤6", 36 % 4 == 0 and 6 % 4)
N = 2852136
ok("ex4 tests", N % 2 == 0 and N % 5 and N % 4 == 0 and 36 % 4 == 0 and 136 == 8 * 17 and N % 8 == 0 and
   sum(map(int, str(N))) == 27 and N % 9 == 0 and N % 3 == 0 and N % 6 == 0)
ok("ex4 11", dsum_alt(N) == 1 and N % 11 == 1)
ok("ex4 blocks", blocks(N) == [136, 852, 2] and 136 - 852 + 2 == -714 and (N + 714) % 1001 == 0)
ok("ex4 7,13", -714 == -7 * 102 and N % 7 == 0 and -714 == 13 * -55 + 1 and N % 13 == 1)
chain = [N]
while chain[-1] >= 100:
    v = chain[-1]
    chain.append(v // 10 - 2 * (v % 10))
ok("ex4 a-2b chain", chain == [2852136, 285201, 28518, 2835, 273, 21])
ok("ex5", gcd(360, 756) == 36 and lcm(360, 756) == 7560)
d360 = sp.divisors(360)
ok("ex5 even/square", sum(1 for d in d360 if d % 2 == 0) == 18 and
   [d for d in d360 if isqrt(d) ** 2 == d] == [1, 4, 9, 36])
four = range(1000, 10000)
ok("ex6 a", sum(1 for v in four if len(set(str(v))) == 4) == 4536 == 9 * 9 * 8 * 7)
ok("ex6 b", sum(1 for v in four if "7" in str(v)) == 3168 and 8 * 9 ** 3 == 5832)
people = ["W"] * 6 + ["M"] * 5
teams = list(itertools.combinations(range(11), 4))
nm = [sum(1 for i in t if people[i] == "M") for t in teams]
ok("ex6 c", len(teams) == 330 and comb(6, 4) == 15 and sum(1 for k in nm if k >= 1) == 315)
ok("ex6 d", sum(1 for k in nm if k in (1, 3)) == 160 and comb(6, 3) * 5 == 100 and comb(5, 3) * 6 == 60)

# ---------- practice ----------
divalg(500, 17, 29, 7)
divalg(-45, 7, -7, 4)
ok("P2", sp.factorint(2520) == {2: 3, 3: 2, 5: 1, 7: 1} and sp.factorint(3003) == {3: 1, 7: 1, 11: 1, 13: 1}
   and gcd(2520, 3003) == 21 and lcm(2520, 3003) == 360360)
ok("P3", euclid_lines(2024, 1748) == [(2024, 1, 1748, 276), (1748, 6, 276, 92), (276, 3, 92, 0)] and
   lcm(2024, 1748) == 38456)
ok("P4", euclid_lines(43, 17)[:3] == [(43, 2, 17, 9), (17, 1, 9, 8), (9, 1, 8, 1)] and 2 * 43 - 5 * 17 == 1)
ok("P5", euclid_lines(252, 198) == [(252, 1, 198, 54), (198, 3, 54, 36), (54, 1, 36, 18), (36, 2, 18, 0)] and
   4 * 252 - 5 * 198 == 18 and 100 % 18)
ok("P6", base(345, 5) == "2340" and int("101101", 2) == 45 and int("2B7", 12) == 427)
ok("P7", base(int("1011", 2) + int("111", 2), 2) == "10010" and base(int("34", 5) * int("23", 5), 5) == "1442" and
   (int("34", 5), int("23", 5)) == (19, 13) and 19 * 13 == 247)
P = 7380916
ok("P8", P % 4 == 0 and 916 == 8 * 114 + 4 and P % 8 == 4 and sum(map(int, str(P))) == 34 and P % 9 == 7 and
   dsum_alt(P) == 26 and P % 11 == 4)
ok("P9", 4 + 567 + 317 == 888 == 24 * 37 and 4567317 % 37 == 0)
ok("P10", sp.expand(7 * (5 * n + 3) - 5 * (7 * n + 4)) == 1)
ok("P11", perm(8, 3) == 336 == len(list(itertools.permutations("ABCDEFGH", 3))) and 2 ** 8 == 256 and comb(8, 3) == 56)
ok("P12", 26 ** 2 * 1000 == 676000 and 26 ** 2 * 720 == 486720 and 676000 - 486720 == 189280 and
   sum(1 for d in itertools.product(range(10), repeat=3) if len(set(d)) < 3) == 280 and
   len(sp.divisors(1800)) == 36 and sp.factorint(1800) == {2: 3, 3: 2, 5: 2})

# ---------- exam ----------
ok("B1 a", euclid_lines(1001, 357) == [(1001, 2, 357, 287), (357, 1, 287, 70), (287, 4, 70, 7), (70, 10, 7, 0)])
ok("B1 b", 5 * 287 - 4 * 357 == 7 and 5 * 1001 - 14 * 357 == 7 and 5005 - 4998 == 7)
ok("B1 cde", 10 % 7 and 15 * 1001 - 42 * 357 == 21 and lcm(1001, 357) == 51051 == 1001 * 357 // 7)
Q = 6342715
ok("B2 c", blocks(Q) == [715, 342, 6] and 715 - 342 + 6 == 379 and
   [Q % p for p in (7, 11, 13)] == [1, 5, 2] == [379 % 7, 379 % 11, 379 % 13] and
   379 == 7 * 54 + 1 == 11 * 34 + 5 == 13 * 29 + 2)
ok("B3 c", 12 % 6 == 0 and 4 % 6 and 3 % 6)
ok("B3 d", all(2 ** m != 3 ** k for m in range(1, 60) for k in range(1, 40)))
ok("B4", perm(12, 3) == 1320 and comb(12, 4) - comb(7, 4) == 460 and (comb(12, 4), comb(7, 4)) == (495, 35) and
   comb(7, 2) * comb(5, 2) + comb(7, 3) * 5 == 385 and 2 ** 12 - 13 == 4083)
kids = ["B"] * 7 + ["G"] * 5
com = list(itertools.combinations(range(12), 4))
ok("B4 brute", sum(1 for c in com if any(kids[i] == "G" for i in c)) == 460 and
   sum(1 for c in com if sum(kids[i] == "B" for i in c) in (2, 3)) == 385)

ok("counts", len(UNIT["practice"]) == len(UNIT["answers"]) == 12 and len(UNIT["exam"]) == 4)
print(f"pc09: {N_OK} checks passed, {len(FAILS)} failed")
assert not FAILS, FAILS
print("pc09 check PASS")
