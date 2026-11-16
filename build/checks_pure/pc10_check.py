"""Checks every number and claim stated in pure/pc10.py (congruences, inverses, CRT, Fermat, orders, residues)."""
import sys
from math import comb, gcd
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pure.pc10 import POW7, UNIT  # noqa: E402

N_OK = 0
FAILS = []


def ok(label, cond):
    global N_OK
    if cond:
        N_OK += 1
    else:
        FAILS.append(label)
        print("FAIL", label)


def solve(a, b, n):
    """All x in 0..n-1 with ax ≡ b (mod n), by brute force."""
    return [x for x in range(n) if (a * x - b) % n == 0]


def crt(pairs, lo=0, hi=None):
    m = 1
    for _, n in pairs:
        m = m * n // gcd(m, n)
    hi = m if hi is None else hi
    return [x for x in range(lo, hi) if all(x % n == a % n for a, n in pairs)]


def order(a, p):
    return next(k for k in range(1, p) if pow(a, k, p) == 1)


def qr(p):
    return sorted({x * x % p for x in range(1, p)})


def euclid_lines(a, b):
    out = []
    while b:
        q, r = divmod(a, b)
        out.append((a, q, b, r))
        a, b = b, r
    return out


# ---------- notes ----------
ok("100≡2 mod 7", 100 % 7 == 2 and 98 == 14 * 7 and -23 % 6 == 1)
ok("6^50 mod 7", pow(6, 50, 7) == 1)
ok("2^50 mod 7", pow(2, 3, 7) == 1 and pow(2, 50, 7) == 4 and 50 == 3 * 16 + 2)
ok("mult law identity", sp.expand(sp.Symbol("a") * sp.Symbol("c") - sp.Symbol("b") * sp.Symbol("d") -
                                 (sp.Symbol("a") * (sp.Symbol("c") - sp.Symbol("d")) +
                                  sp.Symbol("d") * (sp.Symbol("a") - sp.Symbol("b")))) == 0)
ok("no cancel", (2 * 3 - 2 * 8) % 10 == 0 and (3 - 8) % 10 != 0)
ok("exponent not reduced", pow(2, 10, 7) != pow(2, 3, 7) and (10 - 3) % 7 == 0)
# linear congruence theory: brute force the box over a range
good = True
for n in range(2, 40):
    for a in range(1, n):
        for b in range(n):
            d = gcd(a, n)
            s = solve(a, b, n)
            if (b % d == 0) != bool(s) or (s and len(s) != d):
                good = False
            if s and any((y - s[0]) % (n // d) for y in s):
                good = False
ok("linear congruence theorem n<40", good)
ok("5x≡3 mod 7", solve(5, 3, 7) == [2])
ok("CRT impossible 1 mod 4, 2 mod 6", crt([(1, 4), (2, 6)]) == [])
ok("FLT brute", all(pow(a, p, p) == a % p for p in sp.primerange(2, 60) for a in range(-30, 60)))
ok("POW7 last col", all(row[-1] == 1 for row in POW7))
ok("POW7 orders/primitive", [order(a, 7) for a in range(1, 7)] == [1, 3, 6, 3, 6, 2])
ok("341 smallest base-2 pseudoprime", [n for n in range(3, 342, 2) if not sp.isprime(n) and pow(2, n - 1, n) == 1] == [341]
   and 341 == 11 * 31)
ok("91 base 3", pow(3, 90, 91) == 1 and 91 == 7 * 13)
ok("order divides p-1", all((p - 1) % order(a, p) == 0 for p in sp.primerange(3, 60) for a in range(1, p)))
ok("(p-1)/2 residues", all(len(qr(p)) == (p - 1) // 2 for p in sp.primerange(3, 80)))
ok("QR table 11", [x * x % 11 for x in range(1, 11)] == [1, 4, 9, 5, 3, 3, 5, 9, 4, 1] and qr(11) == [1, 3, 4, 5, 9])
ok("x^2≡6 mod 11 none", solve_sq := [x for x in range(11) if x * x % 11 == 6] == [])
ok("Euler criterion", all((pow(a, (p - 1) // 2, p) == 1) == (a in qr(p)) for p in sp.primerange(3, 50) for a in range(1, p)))
ok("p | pCr", all(comb(p, r) % p == 0 for p in sp.primerange(2, 60) for r in range(1, p)))
a_, b_ = sp.symbols("a b")
ok("freshman p=5,7 coeffs", all(all(c % p == 0 for c in sp.Poly(sp.expand((a_ + b_) ** p - a_ ** p - b_ ** p), a_, b_).coeffs())
                                for p in (3, 5, 7, 11)))
ok("4C2=6, (1+1)^4 mod 4", comb(4, 2) == 6 and 16 % 4 != 2 % 4)

# ---------- examples ----------
ok("E1 a", 7 ** 4 == 2401 and pow(7, 4, 100) == 1 and pow(7, 100, 100) == 1)
ok("E1 b", all((13 ** k - 6 ** k) % 7 == 0 for k in range(1, 60)))
ok("E1 c", [pow(3, k, 10) for k in range(1, 5)] == [3, 9, 7, 1] and 2026 == 4 * 506 + 2 and pow(3, 2026, 10) == 9)
ok("E2 a", gcd(14, 22) == 2 and 56 == 5 * 11 + 1 and solve(7, 3, 11) == [2] and solve(14, 6, 22) == [2, 13] and
   14 * 13 == 182 == 8 * 22 + 6)
ok("E2 b", gcd(15, 25) == 5 and solve(15, 7, 25) == [])
ok("E3", euclid_lines(60, 17) == [(60, 3, 17, 9), (17, 1, 9, 8), (9, 1, 8, 1), (8, 8, 1, 0)] and
   2 * 60 - 7 * 17 == 1 and pow(17, -1, 60) == 53 and 17 * 53 == 901 == 15 * 60 + 1)
ok("E3 b", 53 * 5 == 265 and 265 % 60 == 25 and solve(17, 5, 60) == [25] and 17 * 25 == 425 == 7 * 60 + 5)
ok("E4", solve(3, 1, 5) == [2] and solve(15, -6, 7) == [1] and crt([(2, 3), (3, 5), (2, 7)]) == [23])
ok("E5 a", pow(4, 20, 7) == 2 and 16 % 7 == 2)
ok("E5 b", 1024 == 3 * 341 + 1 and pow(2, 340, 341) == 1)
ok("E5 c", 340 == 30 * 11 + 10 and pow(3, 10, 31) == 25 and (-64) % 31 == (-2) % 31 and (-6) % 31 == 25 and
   pow(3, 340, 31) == 25 and pow(3, 340, 341) != 1)
ok("E6 a", order(2, 11) == 10 and pow(2, 5, 11) == 10 and order(3, 11) == 5 and 243 == 22 * 11 + 1)
ok("E6 b", [x * x % 11 for x in range(1, 6)] == [1, 4, 9, 5, 3] and [x for x in range(11) if x * x % 11 == 5] == [4, 7])

# ---------- practice ----------
ok("P1", (100 % 7, -23 % 6, pow(3, 100, 4)) == (2, 1, 1))
ok("P2", pow(2, 50, 7) == 4)
ok("P3", [pow(7, k, 10) for k in range(1, 5)] == [7, 9, 3, 1] and pow(7, 2025, 10) == 7 and
   all((11 ** k - 4 ** k) % 7 == 0 for k in range(1, 60)))
ok("P4", solve(5, 3, 7) == [2] and pow(5, -1, 7) == 3)
ok("P5", solve(6, 9, 15) == [4, 9, 14] and solve(2, 3, 5) == [4])
ok("P6", solve(4, 3, 6) == [] and solve(4, 2, 6) == [2, 5] and solve(2, 1, 3) == [2])
ok("P7", euclid_lines(120, 23)[:4] == [(120, 5, 23, 5), (23, 4, 5, 3), (5, 1, 3, 2), (3, 1, 2, 1)] and
   2 * 23 - 9 * 5 == 1 and 47 * 23 - 9 * 120 == 1 and 23 * 47 == 1081 and pow(23, -1, 120) == 47 and
   7 * 47 == 329 and 329 % 120 == 89 and solve(23, 7, 120) == [89])
ok("P8", crt([(3, 4), (5, 9)]) == [23] and pow(4, -1, 9) == 7 and solve(4, 2, 9) == [5])
ok("P9 ab", pow(3, 100, 13) == 3 and 81 % 13 == 3 and pow(5, 2024, 11) == 9 and 625 % 11 == 9)
ok("P9 c", all((k ** 5 - k) % 30 == 0 for k in range(-200, 200)))
ok("P10 a", pow(3, 6, 7) == 1 and pow(3, 3, 13) == 1 and 90 % 6 == 0 and 90 % 3 == 0 and pow(3, 90, 91) == 1)
ok("P10 b", pow(2, 6, 13) == 12 and pow(2, 90, 13) == 12 and pow(2, 90, 91) != 1)
ok("P11", qr(13) == [1, 3, 4, 9, 10, 12] and [x * x % 13 for x in range(1, 7)] == [1, 4, 9, 3, 12, 10] and
   7 not in qr(13) and [x for x in range(13) if x * x % 13 == 10] == [6, 7])
ok("P12", order(2, 13) == 12 and order(3, 13) == 3 and sp.divisors(12) == [1, 2, 3, 4, 6, 12] and
   [pow(2, k, 13) for k in (2, 3, 4, 6)] == [4, 8, 3, 12])

# ---------- exam ----------
ok("B1 a", [r for *_, r in euclid_lines(97, 35)] == [27, 8, 3, 2, 1, 0])
ok("B1 b", 3 * 27 - 10 * 8 == 1 and 13 * 27 - 10 * 35 == 1 and 13 * 97 - 36 * 35 == 1 and pow(35, -1, 97) == 61 and
   35 * 61 == 2135 == 22 * 97 + 1)
ok("B1 c", 4 * 61 == 244 and solve(35, 4, 97) == [50])
ok("B1 d", 200 == 2 * 96 + 8 and 1225 % 97 == 61 and 3721 % 97 == 35 and pow(35, 8, 97) == 61 and pow(35, 200, 97) == 61)
ok("B2 a", crt([(2, 5), (3, 6), (4, 7)], 100, 401) == [207] and crt([(2, 5), (3, 6), (4, 7)]) == [207])
ok("B2 b", crt([(1, 4), (2, 6)]) == [])
ok("B2 c", gcd(12, 30) == 6 and solve(12, 18, 30) == [4, 9, 14, 19, 24, 29] and solve(2, 3, 5) == [4])
ok("B3 b", 2 ** 11 == 2048 == 89 * 23 + 1 and order(2, 23) == 11)
ok("B3 c", 25 % 23 == 2 and [x for x in range(23) if x * x % 23 == 2] == [5, 18])
ok("B3 d", 2047 == 23 * 89 and 2046 == 11 * 186 and pow(2, 2046, 2047) == 1)
ok("B4 d", qr(7) == [1, 2, 4] and [x for x in range(7) if x * x % 7 == 2] == [3, 4])

ok("counts", len(UNIT["practice"]) == len(UNIT["answers"]) == 12 and len(UNIT["exam"]) == len(UNIT["exam_answers"]) == 4)
print(f"pc10: {N_OK} checks passed, {len(FAILS)} failed")
assert not FAILS, FAILS
print("pc10 check PASS")
