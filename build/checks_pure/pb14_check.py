"""Checks every number stated in pure/pb14.py (root finding, mid-ordinate/Simpson, Euler and finite differences)."""
import math
import sys
from pathlib import Path

import sympy as sp
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pure.pb14 import UNIT  # noqa: E402,F401

FAILS = []


def ok(label, cond):
    print(("ok  " if cond else "FAIL"), label)
    if not cond:
        FAILS.append(label)


def dp(label, value, stated):
    places = len(stated.split(".")[1]) if "." in stated else 0
    ok(f"{label}: {float(value):.8f} vs {stated}", abs(float(value) - float(stated)) <= 0.5 * 10 ** (-places) + 1e-12)


def interp(f, a, b):
    return a - f(a) * (b - a) / (f(b) - f(a))


def newton(f, df, x0, n):
    xs = [x0]
    for _ in range(n):
        xs.append(xs[-1] - f(xs[-1]) / df(xs[-1]))
    return xs


def mid(f, a, b, n):
    h = (b - a) / n
    return h * sum(f(a + (i + 0.5) * h) for i in range(n))


def simpson(f, a, b, n):
    h = (b - a) / n
    ys = [f(a + i * h) for i in range(n + 1)]
    return h / 3 * (ys[0] + ys[-1] + 4 * sum(ys[1:-1:2]) + 2 * sum(ys[2:-1:2]))


def euler(f, x0, y0, h, n):
    ys = [y0]
    for r in range(n):
        ys.append(ys[-1] + h * f(x0 + r * h, ys[-1]))
    return ys


def improved(f, x0, y0, y1, h, n):
    ys = [y0, y1]
    for r in range(1, n):
        ys.append(ys[r - 1] + 2 * h * f(x0 + r * h, ys[r]))
    return ys


# --- E1 / E2: f(x) = x^3 - 2x - 5
f = lambda x: x ** 3 - 2 * x - 5
df = lambda x: 3 * x ** 2 - 2
ok("E1a", f(2) == -1 and f(3) == 16)
ok("E1b values", f(2.5) == 5.625 and f(2.25) == 1.890625 and abs(f(2.125) - 0.345703) < 5e-7)
alpha = brentq(f, 2, 3)
ok("E1b interval", 2 < alpha < 2.125)
x1 = interp(f, 2, 3); dp("E1c x1", x1, "2.0588"); dp("E1c f(x1)", f(x1), "-0.3908")
x2 = interp(f, x1, 3); dp("E1c x2", x2, "2.0813")
xs = newton(f, df, 2, 3)
dp("E2 x1", xs[1], "2.1"); dp("E2 f(2.1)", f(2.1), "0.061"); dp("E2 f'(2.1)", df(2.1), "11.23")
dp("E2 x2", xs[2], "2.094568"); dp("E2 x3", xs[3], "2.094551")
dp("E2 f(2.0945)", f(2.0945), "-0.000575"); dp("E2 f(2.0955)", f(2.0955), "0.0106")
dp("E2 root", alpha, "2.095")
dp("E2 sqrt(2/3)", math.sqrt(2 / 3), "0.8165")
# Newton figure start 2.5 converges
ok("fig newton", abs(newton(f, df, 2.5, 6)[-1] - alpha) < 1e-12)

# --- E3: sqrt(1+x^3) on [0,1]
g = lambda x: math.sqrt(1 + x ** 3)
for xv, s in zip([0.125, 0.375, 0.625, 0.875], ["1.000976", "1.026028", "1.115411", "1.292255"]):
    dp(f"E3 mid y({xv})", g(xv), s)
dp("E3 mid sum", sum(g(v) for v in [0.125, 0.375, 0.625, 0.875]), "4.434670")
dp("E3 mid", mid(g, 0, 1, 4), "1.1087")
for xv, s in zip([0.25, 0.5, 0.75, 1], ["1.007782", "1.060660", "1.192424", "1.414214"]):
    dp(f"E3 y({xv})", g(xv), s)
ys = [g(0.25 * i) for i in range(5)]
dp("E3 bracket", ys[0] + ys[4] + 4 * (ys[1] + ys[3]) + 2 * ys[2], "13.336359")
dp("E3 simpson", simpson(g, 0, 1, 4), "1.1114")
exact = quad(g, 0, 1)[0]
dp("E3 exact", exact, "1.1114")
dp("E3 mid error", exact - mid(g, 0, 1, 4), "0.0028")

# --- E4/E5: y' = x + y
F = lambda x, y: x + y
ye = euler(F, 0, 1, 0.1, 3)
ok("E4 euler", [round(v, 10) for v in ye] == [1, 1.1, 1.22, 1.362])
ex = 2 * math.exp(0.3) - 1.3
dp("E4 exact", ex, "1.3997"); dp("E4 error", ex - ye[3], "0.0377")
ok("E4 percent", round(100 * (ex - ye[3]) / ex, 1) == 2.7)
yi = improved(F, 0, 1, 1.1, 0.1, 3)
ok("E5 improved", [round(v, 10) for v in yi] == [1, 1.1, 1.24, 1.388])
dp("E5 error", ex - yi[3], "0.0117")
x = sp.symbols("x")
ok("E4 exact solves", sp.simplify(sp.diff(2 * sp.exp(x) - x - 1, x) - (x + 2 * sp.exp(x) - x - 1)) == 0)

# --- E6: y'' = x^2 - y, finite differences
h = 0.1
y1 = (2 * 1 - 0.01) / 2
ok("E6 y1", abs(y1 - 0.995) < 1e-12)
y2 = 2 * y1 - 1 + h * h * (0.01 - y1); dp("E6 y2", y2, "0.98015")
y3 = 2 * y2 - y1 + h * h * (0.04 - y2); dp("E6 y3", y3, "0.955899"); dp("E6 y3 4dp", y3, "0.9559")
yex = x ** 2 - 2 + 3 * sp.cos(x)
ok("E6 exact solves", sp.simplify(sp.diff(yex, x, 2) - (x ** 2 - yex)) == 0 and yex.subs(x, 0) == 1
   and sp.diff(yex, x).subs(x, 0) == 0)
dp("E6 exact", float(yex.subs(x, 0.3)), "0.9560")

# --- Practice
f2 = lambda x: x ** 3 + x - 3
ok("P1", f2(1) == -1 and f2(2) == 7 and f2(1.5) == 1.875 and abs(f2(1.25) - 0.203) < 5e-4 and abs(f2(1.125) + 0.451) < 5e-4)
r2 = brentq(f2, 1, 2); ok("P1 interval", 1.125 < r2 < 1.25); dp("P1 root", r2, "1.2134")
a1 = interp(f2, 1, 2); dp("P2 x1", a1, "1.125"); a2 = interp(f2, a1, 2); dp("P2 x2", a2, "1.1780")
F3 = lambda x: math.exp(x) - 3 * x
xs = newton(F3, lambda x: math.exp(x) - 3, 1.5, 2)
dp("P3 x1", xs[1], "1.5124"); dp("P3 x2", xs[2], "1.5121")
r3 = brentq(F3, 1, 2); dp("P3 root", r3, "1.512"); ok("P3 sign", F3(1.5115) < 0 < F3(1.5125))
xs = newton(lambda x: x * x - 7, lambda x: 2 * x, 3, 2)
dp("P4 x1", xs[1], "2.6667"); dp("P4 x2", xs[2], "2.6458"); dp("P4 sqrt7", math.sqrt(7), "2.6458")
f5 = lambda x: x ** 3 - 3 * x + 1
ok("P5 f'(1)=0", 3 * 1 ** 2 - 3 == 0)
dp("P5 f(1.5)", f5(1.5), "-0.125"); dp("P5 x1", 1.5 - f5(1.5) / 3.75, "1.5333")
r = lambda x: 1 / (1 + x * x)
for xv, s in zip([0.25, 0.75, 1.25, 1.75], ["0.941176", "0.64", "0.390244", "0.246154"]):
    dp(f"P6 y({xv})", r(xv), s)
dp("P6", mid(r, 0, 2, 4), "1.1088")
dp("P7 y(1.5)", r(1.5), "0.307692")
dp("P7", simpson(r, 0, 2, 4), "1.1051"); dp("P7 exact", math.atan(2), "1.1071")
dp("P7 mid err", mid(r, 0, 2, 4) - math.atan(2), "0.0016"); dp("P7 simp err", simpson(r, 0, 2, 4) - math.atan(2), "-0.0020")
dp("P8", simpson(math.log, 1, 2, 4), "0.38626"); dp("P8 exact", 2 * math.log(2) - 1, "0.38629")
dp("P8 err", 2 * math.log(2) - 1 - simpson(math.log, 1, 2, 4), "0.00003")
ye = euler(lambda x, y: x * y, 1, 2, 0.1, 2)
dp("P9 y1", ye[1], "2.2"); dp("P9 y2", ye[2], "2.442"); dp("P9 exact", 2 * math.exp(0.22), "2.4922")
dp("P9 err", 2 * math.exp(0.22) - ye[2], "0.050")
ok("P9 exact solves", sp.simplify(sp.diff(2 * sp.exp((x ** 2 - 1) / 2), x) - x * 2 * sp.exp((x ** 2 - 1) / 2)) == 0)
ye = euler(lambda x, y: math.sqrt(x + y), 0, 1, 0.25, 2)
dp("P10", ye[2], "1.5562")
G = lambda x, y: x * x + y
yi = improved(G, 0, 1, euler(G, 0, 1, 0.1, 1)[1], 0.1, 3)
dp("P11 y1", yi[1], "1.1"); dp("P11 y2", yi[2], "1.222"); dp("P11 y3", yi[3], "1.3524")
ex = 3 * math.exp(0.3) - 2.69
dp("P11 exact", ex, "1.3596"); dp("P11 err", ex - yi[3], "0.0072")
ye_ = 3 * sp.exp(x) - x ** 2 - 2 * x - 2
ok("P11 exact solves", sp.simplify(sp.diff(ye_, x) - (x ** 2 + ye_)) == 0 and ye_.subs(x, 0) == 1)
q1 = (2 - 0.04) / 2; q2 = 1.96 * q1 - 1
dp("P12 y1", q1, "0.98"); dp("P12 y2", q2, "0.9208"); dp("P12 cos", math.cos(0.4), "0.9211")

# --- Section B
f3 = lambda x: x ** 3 - 5 * x + 3
dp("Q13 f(1.8)", f3(1.8), "-0.168"); dp("Q13 f(1.9)", f3(1.9), "0.359")
li = interp(f3, 1.8, 1.9); dp("Q13 LI", li, "1.8319")
nr = 1.8 - f3(1.8) / (3 * 1.8 ** 2 - 5); dp("Q13 f'(1.8)", 3 * 1.8 ** 2 - 5, "4.72"); dp("Q13 NR", nr, "1.8356")
root = brentq(f3, 1.8, 1.9); dp("Q13 root", root, "1.8342")
ok("Q13 NR closer", abs(1.8356 - 1.8342) < abs(1.8319 - 1.8342))
ok("Q13 f' zero", abs(3 * (5 / 3) - 5) < 1e-12)
for xv, s in zip([0.25, 0.75, 1.25, 1.75], ["1.007782", "1.192424", "1.718466", "2.521780"]):
    dp(f"Q14 mid y({xv})", g(xv), s)
dp("Q14 mid sum", sum(g(v) for v in [0.25, 0.75, 1.25, 1.75]), "6.440452")
m14, s14 = mid(g, 0, 2, 4), simpson(g, 0, 2, 4)
dp("Q14a", m14, "3.2202")
for xv, s in zip([0.5, 1, 1.5, 2], ["1.060660", "1.414214", "2.091650", "3"]):
    dp(f"Q14 y({xv})", g(xv), s)
dp("Q14b", s14, "3.2396")
I = quad(g, 0, 2)[0]; dp("Q14 exact", I, "3.2413")
dp("Q14 mid %", 100 * (I - m14) / I, "0.65"); dp("Q14 simp %", 100 * (I - s14) / I, "0.05")
# Q15 recurrence
q = sp.symbols("q")
xn, yp, yc, ym = sp.symbols("x_n y_p y_c y_m")
lhs = (yp - 2 * yc + ym) / sp.Rational(1, 100) + xn * (yp - ym) / sp.Rational(2, 10) + yc - 2
target = (20 + xn) * yp - (sp.Rational(398, 10) * yc - (20 - xn) * ym + sp.Rational(4, 10))
ok("Q15a recurrence", sp.simplify(lhs * sp.Rational(2, 10) - target) == 0)
y1 = 44.2 / 40; dp("Q15 y1", y1, "1.105")
y2 = (39.8 * y1 - 19.9 * 1 + 0.4) / 20.1; dp("Q15 y2", y2, "1.2179"); dp("Q15 y2 6dp", y2, "1.217861")
y3 = (39.8 * y2 - 19.8 * y1 + 0.4) / 20.2
# Note: at n = 2, x_n = 0.2, so the coefficient of y_{n-1} is (20 - 0.2) = 19.8
dp("Q15 y3", y3, "1.3362")
# Q16
H = lambda x, y: math.sqrt(x * x + y)
y1 = euler(H, 1, 3, 0.1, 1)[1]; dp("Q16a", y1, "3.2")
yi = improved(H, 1, 3, y1, 0.1, 3)
dp("Q16 y2", yi[2], "3.42"); dp("Q16 y3", yi[3], "3.6409")
dp("Q16 sqrt4.41", math.sqrt(1.21 + 3.2), "2.1")

print()
print("PASS pb14" if not FAILS else f"FAILED pb14: {FAILS}")
sys.exit(1 if FAILS else 0)
