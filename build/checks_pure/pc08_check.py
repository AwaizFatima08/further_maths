"""Checks every result stated in pure/pc08.py (Groups II: structure and isomorphism)."""
import itertools
import re
import sys
from collections import Counter
from pathlib import Path

import sympy as sp
from sympy.algebras.quaternion import Quaternion

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pure.pc07 import D3  # noqa: E402
from pure.pc08 import D3_TO_F6, D4, F6, Q8, U7, UNIT  # noqa: E402

FAILS = []
COUNT = 0


def ok(label, cond):
    global COUNT
    COUNT += 1
    print(("ok  " if cond else "FAIL"), label)
    if not cond:
        FAILS.append(label)


def op_from_table(table):
    els, rows = table
    return list(els), {(a, b): rows[i][j] for i, a in enumerate(els) for j, b in enumerate(els)}


def op_from_func(els, f):
    els = list(els)
    return els, {(a, b): f(a, b) for a in els for b in els}


def is_group(els, op):
    if any(op[(a, b)] not in els for a in els for b in els):
        return False, None
    if any(op[(op[(a, b)], c)] != op[(a, op[(b, c)])] for a in els for b in els for c in els):
        return False, None
    ids = [e for e in els if all(op[(e, a)] == a == op[(a, e)] for a in els)]
    if len(ids) != 1:
        return False, None
    e = ids[0]
    if any(not any(op[(a, b)] == e == op[(b, a)] for b in els) for a in els):
        return False, None
    return True, e


def order(els, op, a):
    e = is_group(els, op)[1]
    x, n = a, 1
    while x != e:
        x, n = op[(x, a)], n + 1
    return n


def order_counts(G):
    return Counter(order(*G, a) for a in G[0])


def abelian(G):
    els, op = G
    return all(op[(a, b)] == op[(b, a)] for a in els for b in els)


def is_iso(G, H, phi):
    (ge, gop), (he, hop) = G, H
    return (len(set(phi[x] for x in ge)) == len(ge) == len(he) and set(phi[x] for x in ge) == set(he) and
            all(phi[gop[(a, b)]] == hop[(phi[a], phi[b])] for a in ge for b in ge))


def latin(G):
    els, op = G
    return all(sorted(op[(a, b)] for b in els) == sorted(els) == sorted(op[(b, a)] for b in els) for a in els)


def subgroups_of_order(G, n):
    els, op = G
    e = is_group(*G)[1]
    out = []
    for comb in itertools.combinations([x for x in els if x != e], n - 1):
        h = {e, *comb}
        if all(op[(a, b)] in h for a in h for b in h):
            out.append(frozenset(h))
    return out


def mod_group(els, n):
    return op_from_func(els, lambda p, q: p * q % n)


def comp(p, q):
    return tuple(p[q[i]] for i in range(len(q)))


rot = lambda k, n: tuple((i + k) % n for i in range(n))  # noqa: E731
ref = lambda m, n: tuple((m - i) % n for i in range(n))  # noqa: E731

# ---------- printed tables ----------
for name, t in [("U7", U7), ("F6", F6), ("D4", D4), ("Q8", Q8)]:
    G = op_from_table(t)
    ok(f"{name} is a group", is_group(*G)[0])
    ok(f"{name} Latin square", latin(G))
ok("U7 table = x7", all(U7[1][i][j] == str(int(a) * int(b) % 7) for i, a in enumerate(U7[0]) for j, b in enumerate(U7[0])))
ok("U7 listed as powers of 3", U7[0] == [str(pow(3, k, 7)) for k in range(6)])

# F6 from the function definitions (fi o fj = apply fj first)
x = sp.symbols("x")
FUN = {"f₁": x, "f₂": 1 / x, "f₃": 1 - x, "f₄": 1 / (1 - x), "f₅": (x - 1) / x, "f₆": x / (x - 1)}
fname = lambda e: next(k for k, v in FUN.items() if sp.simplify(e - v) == 0)  # noqa: E731
ok("F6 table from composition", all(F6[1][i][j] == fname(FUN[a].subs(x, FUN[b]))
                                    for i, a in enumerate(F6[0]) for j, b in enumerate(F6[0])))
ok("f4 o f4 = (x-1)/x", sp.simplify(1 / (1 - 1 / (1 - x)) - (x - 1) / x) == 0)

# D4 from geometry: corner positions 0 (top right), 1 (top left), 2 (bottom left), 3 (bottom right)
D4P = dict(zip(D4[0], [rot(0, 4), rot(1, 4), rot(2, 4), rot(3, 4), ref(3, 4), ref(1, 4), ref(0, 4), ref(2, 4)]))
inv = {v: k for k, v in D4P.items()}
ok("D4 table matches geometry", all(D4[1][i][j] == inv[comp(D4P[a], D4P[b])]
                                    for i, a in enumerate(D4[0]) for j, b in enumerate(D4[0])))
ok("H swaps top/bottom corners, V left/right, D1 fixes A and C, D2 fixes B and D",
   D4P["H"][0] == 3 and D4P["V"][0] == 1 and D4P["D₁"][0] == 0 and D4P["D₁"][2] == 2 and D4P["D₂"][1] == 1)

# Q8 from quaternion arithmetic
QE = {"1": Quaternion(1, 0, 0, 0), "i": Quaternion(0, 1, 0, 0), "j": Quaternion(0, 0, 1, 0), "k": Quaternion(0, 0, 0, 1)}
for s in ["i", "j", "k"]:
    QE["−" + s] = -QE[s]
QE["−1"] = Quaternion(-1, 0, 0, 0)
key = lambda q: (q.a, q.b, q.c, q.d)  # noqa: E731
qinv = {key(v): k for k, v in QE.items()}
ok("Q8 table from quaternions", all(Q8[1][i][j] == qinv[key(QE[a] * QE[b])]
                                    for i, a in enumerate(Q8[0]) for j, b in enumerate(Q8[0])))
q8 = op_from_table(Q8)
ok("Q8 stated products", [q8[1][p] for p in [("i", "j"), ("j", "k"), ("k", "i"), ("j", "i"), ("k", "j"), ("i", "k")]]
   == ["k", "i", "j", "−k", "−i", "−j"] and all(q8[1][(s, s)] == "−1" for s in "ijk"))

# ---------- isomorphisms ----------
d3 = op_from_table(D3)
f6 = op_from_table(F6)
ok("D3 -> F6 isomorphism", is_iso(d3, f6, D3_TO_F6))
ok("F6 orders", {a: order(*f6, a) for a in F6[0]} == {"f₁": 1, "f₂": 2, "f₃": 2, "f₄": 3, "f₅": 3, "f₆": 2})
ok("b = a o r -> f2 o f4 = f3, c = r o a -> f4 o f2 = f6",
   d3[1][("a", "r")] == "b" and f6[1][("f₂", "f₄")] == "f₃" and d3[1][("r", "a")] == "c" and f6[1][("f₄", "f₂")] == "f₆")

z = lambda n: op_from_func(range(n), lambda p, q: (p + q) % n)  # noqa: E731
u7 = mod_group(range(1, 7), 7)
ok("Z6 -> U7, k -> 3^k", is_iso(z(6), u7, {k: pow(3, k, 7) for k in range(6)}))
ok("Z6 -> U7, k -> 5^k", is_iso(z(6), u7, {k: pow(5, k, 7) for k in range(6)}))
ok("P1 map values", [pow(3, k, 7) for k in range(6)] == [1, 3, 2, 6, 4, 5])
# exactly two isomorphisms Z6 -> C6
cnt = sum(is_iso(z(6), u7, dict(zip(range(6), perm))) for perm in itertools.permutations(range(1, 7)))
ok("exactly two isomorphisms Z6 -> U7", cnt == 2)

# Example 1
I = sp.I
G4c = op_from_func([1, I, -1, -I], lambda p, q: sp.expand(p * q))
ok("Z4 -> {1,i,-1,-i}, k -> i^k", is_iso(z(4), G4c, {k: I**k for k in range(4)}))
u5 = mod_group([1, 2, 3, 4], 5)
ok("Z4 -> U5, k -> 2^k", is_iso(z(4), u5, {k: pow(2, k, 5) for k in range(4)}) and [pow(2, k, 5) for k in range(4)] == [1, 2, 4, 3])
ok("G -> K: 1,i,-1,-i -> 1,2,4,3", is_iso(G4c, u5, {1: 1, I: 2, -1: 4, -I: 3}))
ok("i -> 3 also iso", is_iso(G4c, u5, {1: 1, I: 3, -1: 4, -I: 2}))
ok("order of 4 in U5 is 2", order(*u5, 4) == 2)

# Example 2: Klein group and matrices
mats = {"I": sp.eye(2), "A": sp.diag(1, -1), "B": sp.diag(-1, 1), "-I": -sp.eye(2)}
mname = lambda m: next(k for k, v in mats.items() if v == m)  # noqa: E731
M = op_from_func(mats, lambda p, q: mname(mats[p] * mats[q]))
u8 = mod_group([1, 3, 5, 7], 8)
ok("M is a group", is_group(*M)[0])
ok("M -> U8 iso", is_iso(M, u8, {"I": 1, "A": 3, "B": 5, "-I": 7}))
ok("AB = -I, A(-I) = B, B(-I) = A", M[1][("A", "B")] == "-I" and M[1][("A", "-I")] == "B" and M[1][("B", "-I")] == "A")
ok("U8 not iso to Z4 (order counts)", order_counts(u8) != order_counts(z(4)))

# ---------- order 4 and 6 structure ----------
u12 = mod_group([1, 5, 7, 11], 12)
ok("P2 U12 three of order 2", order_counts(u12) == Counter({1: 1, 2: 3}))
u10 = mod_group([1, 3, 7, 9], 10)
ok("P3 Z4 -> U10, k -> 3^k", is_iso(z(4), u10, {k: pow(3, k, 10) for k in range(4)})
   and [pow(3, k, 10) for k in range(4)] == [1, 3, 9, 7] and [pow(7, k, 10) for k in range(4)] == [1, 7, 9, 3])
mats2 = {"I": sp.eye(2), "P": sp.diag(1, -1), "Q": sp.diag(-1, 1), "-I": -sp.eye(2)}
mn2 = lambda m: next(k for k, v in mats2.items() if v == m)  # noqa: E731
M2 = op_from_func(mats2, lambda p, q: mn2(mats2[p] * mats2[q]))
ok("P4 iso to U12", is_iso(M2, u12, {"I": 1, "P": 5, "Q": 7, "-I": 11}))
ok("P4 any bijection with I -> 1 works", all(is_iso(M2, u12, dict(zip(["I", "P", "Q", "-I"], [1, *p])))
                                            for p in itertools.permutations([5, 7, 11])))
ok("P5 rotations of square cyclic", is_iso(z(4), G4c, {k: I**k for k in range(4)}) and order_counts(u8)[4] == 0)


# all groups of order 4 are abelian: brute force over all 4x4 tables with identity 0
def all_groups(n):
    """Every group table on {0..n-1} with identity 0: backtrack over reduced Latin squares, then test the axioms."""
    tab = [[(i if j == 0 else j if i == 0 else None) for j in range(n)] for i in range(n)]
    cells = [(i, j) for i in range(1, n) for j in range(1, n)]
    found = []

    def fill(k):
        if k == len(cells):
            G = op_from_func(range(n), lambda p, q: tab[p][q])
            if is_group(*G)[0]:
                found.append(G)
            return
        i, j = cells[k]
        for v in range(n):
            if v not in tab[i][:j] and all(tab[r][j] != v for r in range(i)):
                tab[i][j] = v
                fill(k + 1)
                tab[i][j] = None

    fill(0)
    return found


g4 = all_groups(4)
ok("every group of order 4 is abelian, C4 or V4", all(abelian(G) for G in g4)
   and {tuple(sorted(order_counts(G).items())) for G in g4} == {((1, 1), (2, 1), (4, 2)), ((1, 1), (2, 3))})
g6types = {(abelian(G), tuple(sorted(order_counts(G).items()))) for G in all_groups(6)}
ok("groups of order 6: C6 and D3 only", g6types == {(True, ((1, 1), (2, 1), (3, 2), (6, 2))),
                                                    (False, ((1, 1), (2, 3), (3, 2)))})
ok("groups of order 5 are all cyclic", all(max(order_counts(G)) == 5 for G in all_groups(5)))

# ---------- order 8 ----------
d4 = op_from_table(D4)
u16 = mod_group(range(1, 16, 2), 16)
u24 = mod_group([1, 5, 7, 11, 13, 17, 19, 23], 24)
w = sp.exp(sp.pi * I / 4)
roots8 = [sp.nsimplify(sp.expand_complex(w**k)) for k in range(8)]
r8 = op_from_func(range(8), lambda p, q: (p + q) % 8)  # roots of unity w^k <-> k
ok("8th roots: w^k w^j = w^(k+j)", all(sp.simplify(roots8[p] * roots8[q] - roots8[(p + q) % 8]) == 0 for p in range(8) for q in range(8)))


def counts(G):
    c = order_counts(G)
    return [c.get(k, 0) for k in (1, 2, 4, 8)]


ok("C8 counts 1,1,2,4", counts(z(8)) == [1, 1, 2, 4] and counts(r8) == [1, 1, 2, 4])
ok("U16 counts 1,3,4,0 abelian", counts(u16) == [1, 3, 4, 0] and abelian(u16))
ok("U24 counts 1,7,0,0", counts(u24) == [1, 7, 0, 0] and abelian(u24) and is_group(*u24)[0])
ok("D4 counts 1,5,2,0 non-abelian", counts(d4) == [1, 5, 2, 0] and not abelian(d4))
ok("Q8 counts 1,1,6,0 non-abelian", counts(q8) == [1, 1, 6, 0] and not abelian(q8))
ok("U24 squares", [k * k % 24 for k in (5, 7, 11, 13, 17, 19, 23)] == [1] * 7 and [25, 49, 121, 169, 289, 361, 529] == [k * k for k in (5, 7, 11, 13, 17, 19, 23)])
ok("roots of unity orders 1,8,4,8,2,8,4,8", [order(*r8, k) for k in range(8)] == [1, 8, 4, 8, 2, 8, 4, 8])
ok("D4 orders", {a: order(*d4, a) for a in D4[0]} == {"e": 1, "r": 4, "r²": 2, "r³": 4, "H": 2, "V": 2, "D₁": 2, "D₂": 2})
s4 = set(subgroups_of_order(d4, 4))
ok("D4 subgroups of order 4", s4 == {frozenset(s) for s in [{"e", "r", "r²", "r³"}, {"e", "r²", "H", "V"}, {"e", "r²", "D₁", "D₂"}]})
ok("D4 has one cyclic subgroup of order 4, Q8 three",
   sum(any(order(*d4, a) == 4 for a in h) for h in s4) == 1
   and sum(any(order(*q8, a) == 4 for a in h) for h in subgroups_of_order(q8, 4)) == 3)
ok("U16 orders 7,9,15 -> 2", [order(*u16, k) for k in (7, 9, 15)] == [2, 2, 2] and [order(*u16, k) for k in (3, 5, 11, 13)] == [4] * 4)
K = op_from_func([1, 7, 9, 15], lambda p, q: p * q % 16)
L = op_from_func(["e", "r²", "H", "V"], lambda p, q: d4[1][(p, q)])
ok("exam 2(e) K ~ L via 1->e,7->H,9->r2,15->V", is_iso(K, L, {1: "e", 7: "H", 9: "r²", 15: "V"}))

# ---------- abstract group of Example 6 (D4) and exam 4 (Q8) ----------
r, Hh = "r", "H"
ok("D4: r^4 = e, H^2 = e, H o r = r^3 o H = D2",
   d4[1][(d4[1][("r", "r")], d4[1][("r", "r")])] == "e" and d4[1][(Hh, Hh)] == "e"
   and d4[1][(Hh, r)] == d4[1][("r³", Hh)] == "D₂")


def word(G, *xs):
    els, op = G
    out = xs[0]
    for y in xs[1:]:
        out = op[(out, y)]
    return out


# in D4 with a = r, b = H: ba^2 = a^2 b, ba^3 = ab, (ab)^2 = e, (a^2 b)^2 = e
ok("Ex6 relations in D4", word(d4, "H", "r²") == word(d4, "r²", "H") and word(d4, "H", "r³") == word(d4, "r", "H")
   and word(d4, "r", "H", "r", "H") == "e" and word(d4, "r²", "H", "r²", "H") == "e")
ok("Ex6 eight distinct words a^i b^j", len({word(d4, *(["e"] + ["r"] * i + ["H"] * j)) for i in range(4) for j in range(2)}) == 8)
# Q8 with a = i, b = j
ok("Exam 4: a = i, b = j satisfies a^4 = 1, b^2 = a^2, ba = a^3 b",
   word(q8, "i", "i", "i", "i") == "1" and word(q8, "j", "j") == word(q8, "i", "i") and word(q8, "j", "i") == word(q8, "i", "i", "i", "j"))
ok("Exam 4: (a^k b)^2 = a^2 for k = 0..3", all(word(q8, *(["i"] * k + ["j"] + ["i"] * k + ["j"])) == "−1" if k else
                                               word(q8, "j", "j") == "−1" for k in range(4)))
ok("Exam 4: b a^k = a^3k b", all(word(q8, *(["j"] + ["i"] * k)) == word(q8, *(["1"] + ["i"] * (3 * k) + ["j"])) for k in range(1, 6)))

# ---------- infinite groups ----------
a_, b_ = sp.symbols("a b", real=True)
ok("exp(x+y) = exp x exp y", sp.simplify(sp.exp(a_ + b_) - sp.exp(a_) * sp.exp(b_)) == 0)
Ma = lambda t: sp.Matrix([[1, t], [0, 1]])  # noqa: E731
ok("M(a)M(b) = M(a+b), inverse M(-a)", Ma(a_) * Ma(b_) == Ma(a_ + b_) and Ma(a_) * Ma(-a_) == sp.eye(2))
ok("M(2)^n = M(2n)", all(Ma(2)**n == Ma(2 * n) for n in range(1, 6)))
ok("orders in C*: i 4, -1 2, e^(i pi/4) 8",
   [min(n for n in range(1, 20) if sp.simplify(z0**n - 1) == 0) for z0 in (I, -1, (1 + I) / sp.sqrt(2))] == [4, 2, 8])

# ---------- practice 11, 12 ----------
c6 = z(6)
ok("P11 orders of a^2, a^3, a^4 in C6", [order(*c6, k) for k in (2, 3, 4)] == [3, 2, 3])
S3 = {"e": (0, 1, 2), "r": (1, 2, 0), "r²": (2, 0, 1), "a": (0, 2, 1), "b": (2, 1, 0), "c": (1, 0, 2)}


def cycle(*c):  # positions 1..3 -> 0-based permutation tuple
    m = list(range(3))
    for i, v in enumerate(c):
        m[v - 1] = c[(i + 1) % len(c)] - 1
    return tuple(m)


ok("P12 cycles", S3["r"] == cycle(1, 2, 3) and S3["r²"] == cycle(1, 3, 2) and S3["a"] == cycle(2, 3)
   and S3["b"] == cycle(1, 3) and S3["c"] == cycle(1, 2))
s3 = op_from_func(list(S3.values()), comp)
ok("P12 D3 -> S3 iso", is_iso(d3, s3, S3))

# ---------- exam 1 ----------
u9 = mod_group([1, 2, 4, 5, 7, 8], 9)
ok("Exam1 orders", [order(*u9, k) for k in (1, 2, 4, 5, 7, 8)] == [1, 6, 3, 6, 3, 2])
ok("Exam1 iso k -> 2^k", is_iso(z(6), u9, {k: pow(2, k, 9) for k in range(6)}) and [pow(2, k, 9) for k in range(6)] == [1, 2, 4, 8, 7, 5])
ok("Exam1 subgroup of order 3", subgroups_of_order(u9, 3) == [frozenset({1, 4, 7})])

# ---------- structure ----------
ok("counts", len(UNIT["practice"]) == len(UNIT["answers"]) == 12 and len(UNIT["exam"]) == len(UNIT["exam_answers"]) == 4)
marks = [sum(int(m) for m in re.findall(r"\[(\d+)\]", q)) for q in UNIT["exam"]]
ok(f"exam marks {marks} within 8-14", all(8 <= m <= 14 for m in marks))

print(f"\n{COUNT - len(FAILS)}/{COUNT} checks passed")
if FAILS:
    print("FAILED:", FAILS)
    sys.exit(1)
print("pc08: ALL CHECKS PASSED")
