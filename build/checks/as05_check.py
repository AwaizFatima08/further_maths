"""Checks every number stated in content/as05.py (Sampling methods)."""
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from content.as05 import RANDOM_ROWS, UNIT  # noqa: E402

FAILS = []


def chk(label, value, stated):
    """Assert value rounds to the stated string (precision taken from the string)."""
    dp = len(stated.split(".")[1]) if "." in stated else 0
    ok = abs(value - float(stated)) <= 0.5 * 10 ** (-dp) + 1e-12
    print(("ok  " if ok else "FAIL"), label, value, stated)
    if not ok:
        FAILS.append(label)


def eq(label, value, expected):
    ok = value == expected
    print(("ok  " if ok else "FAIL"), label, value, expected)
    if not ok:
        FAILS.append(label)


def pick(row, width, lo, hi, n):
    digits = RANDOM_ROWS[row - 1].replace(" ", "")
    out = []
    for i in range(0, len(digits) - width + 1, width):
        v = int(digits[i:i + width])
        if lo <= v <= hi and v not in out:
            out.append(v)
        if len(out) == n:
            break
    return out


def alloc(sizes, n):
    N = sum(sizes)
    return [s * n / N for s in sizes]


# Example 2: 6 pupils from 01-80, row 1
eq("Ex2 SRS", pick(1, 2, 1, 80, 6), [31, 63, 73, 11, 48, 22])
# Example 3: systematic
eq("Ex3 k", 600 // 30, 20)
eq("Ex3 last", 7 + 29 * 20, 587)
# Example 4: stratified
raw = alloc([240, 220, 210, 180, 150], 60)
for r, s in zip(raw, ["14.4", "13.2", "12.6", "10.8", "9.0"]):
    chk("Ex4 raw", r, s)
eq("Ex4 rounded", [round(r) for r in raw], [14, 13, 13, 11, 9])
eq("Ex4 total", sum(round(r) for r in raw), 60)
# Example 5: quotas
eq("Ex5 quotas", [x * 50 / 400 for x in [168, 144, 32, 56]], [21, 18, 4, 7])
# Example 6: standard error
chk("Ex6 SE", 12 / math.sqrt(36), "2")
eq("Ex6 n", (12 / 1) ** 2, 144)

# Practice
eq("P4", pick(2, 2, 1, 60, 5), [52, 1, 48, 49, 36])
eq("P5", pick(3, 3, 1, 450, 5), [166, 189, 321, 202, 179])
eq("P6 k", 1200 // 40, 30)
eq("P6 2nd", 18 + 30, 48)
eq("P6 40th", 18 + 39 * 30, 1188)
raw = alloc([330, 270, 150], 40)
for r, s in zip(raw, ["17.6", "14.4", "8.0"]):
    chk("P7 raw", r, s)
eq("P7 total", sum(round(r + 1e-9) for r in raw), 40)
raw = alloc([35, 35, 30], 10)
eq("P8 raw", raw, [3.5, 3.5, 3.0])
eq("P8 nearest-total", sum(math.floor(r + 0.5) for r in raw), 11)
chk("P12a", 8 / math.sqrt(16), "2")
eq("P12b", (8 / 0.5) ** 2, 256)

# Section B
raw = alloc([180, 140], 40)
eq("B1 raw", raw, [22.5, 17.5])
eq("B1 round-up total", sum(math.floor(r + 0.5) for r in raw), 41)
chk("B2 quota", 0.52 * 0.30 * 200, "31.2")
eq("B3 k", 2400 // 60, 40)
chk("B3 prob", 1 / 40, "0.025")
chk("B3 SE", 4.5 / math.sqrt(60), "0.581")
eq("B3 n", math.ceil((4.5 / 0.3) ** 2 - 1e-9), 225)
raw = alloc([520, 410, 300, 270], 75)
eq("B4 raw", [round(r, 6) for r in raw], [26.0, 20.5, 15.0, 13.5])
eq("B4 round-up total", sum(math.floor(r + 0.5) for r in raw), 76)
eq("B4 adjusted", 26 + 21 + 15 + 13, 75)

assert len(UNIT["practice"]) == len(UNIT["answers"]) == 12
assert len(UNIT["exam"]) == len(UNIT["exam_answers"]) == 4
print("\nALL OK" if not FAILS else f"\nFAILURES: {FAILS}")
sys.exit(1 if FAILS else 0)
