"""Checks every result stated in pure/pb11.py (SHM, damping, forced vibration, coupled systems)."""
import math
import sys
from pathlib import Path

import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pure.pb11 import UNIT  # noqa: E402,F401

FAILS = []
t, A, B = sp.symbols("t A B", real=True)
E = sp.exp


def ok(label, cond):
    print(("ok  " if cond else "FAIL"), label)
    if not cond:
        FAILS.append(label)


def sf3(label, value, stated):
    ok(f"{label}: {float(value):.6g} vs {stated}", float(f"{float(value):.3g}") == float(stated))


def zero(e):
    return sp.simplify(e) == 0


def ode2(label, x, p, q, f=0, m=1):
    ok(label, zero(m * sp.diff(x, t, 2) + p * sp.diff(x, t) + q * x - f))


def ic(label, x, x0, v0):
    ok(label, zero(x.subs(t, 0) - x0) and zero(sp.diff(x, t).subs(t, 0) - v0))


# 11.1 v^2 = w^2(a^2 - x^2) for x = a sin(wt + phi)
a, w, ph = sp.symbols("a omega phi", positive=True)
xx = a * sp.sin(w * t + ph)
ok("v^2 identity", zero(sp.diff(xx, t) ** 2 - w ** 2 * (a ** 2 - xx ** 2)))
ok("SHM general", zero(sp.diff(A * sp.cos(w * t) + B * sp.sin(w * t), t, 2) + w ** 2 * (A * sp.cos(w * t) + B * sp.sin(w * t))))
# damping figure
for p, q, kind in [(2, 17, "light"), (8, 16, "critical"), (10, 16, "heavy")]:
    disc = p * p - 4 * q
    ok(f"figure {kind}", (disc < 0 and kind == "light") or (disc == 0 and kind == "critical") or (disc > 0 and kind == "heavy"))
# 11.4 undamped PI
P, pp = sp.symbols("P p", positive=True)
ok("undamped PI", zero(sp.diff(P / (w ** 2 - pp ** 2) * sp.cos(pp * t), t, 2) + w ** 2 * P / (w ** 2 - pp ** 2) * sp.cos(pp * t)
                   - P * sp.cos(pp * t)))
ok("resonance PI", zero(sp.diff(P / (2 * w) * t * sp.sin(w * t), t, 2) + w ** 2 * P / (2 * w) * t * sp.sin(w * t) - P * sp.cos(w * t)))

# E1
x = 2 * sp.sqrt(2) * sp.sin(3 * t + sp.pi / 4)
ode2("E1", x, 0, 9); ic("E1 ic", x, 2, 6)
ok("E1 expand", zero(x - (2 * sp.cos(3 * t) + 2 * sp.sin(3 * t))))
sf3("E1 amp", 2 * math.sqrt(2), "2.83"); sf3("E1 period", 2 * math.pi / 3, "2.09"); sf3("E1 vmax", 6 * math.sqrt(2), "8.49")
ok("E1 zero", zero(x.subs(t, sp.pi / 4)) and all(float(x.subs(t, s)) > 0 for s in [0.01 * i for i in range(1, 78)]))
# E2
ok("E2 e0", abs(0.5 * 9.8 / 20 - 0.245) < 1e-12)
sf3("E2 period", 2 * math.pi / math.sqrt(40), "0.993"); sf3("E2 vmax", 0.1 * math.sqrt(40), "0.632")
# E3
ok("E3 critical c", 20 ** 2 == 4 * 2 * 50)
x = E(-3 * t) * (sp.Rational(1, 5) * sp.cos(4 * t) + sp.Rational(3, 20) * sp.sin(4 * t))
ode2("E3b", x, 12, 50, m=2); ic("E3b ic", x, sp.Rational(1, 5), 0)
al = sp.atan(sp.Rational(3, 4))
ok("E3b phase", zero(sp.expand_trig(sp.Rational(1, 4) * E(-3 * t) * sp.cos(4 * t - al)) - x))
ok("E3c heavy", 13 ** 2 - 100 == 69 and (-13 + math.sqrt(69)) / 2 < 0)
# E4
x = sp.sin(2 * t) - 2 * t * E(-2 * t)
ode2("E4", x, 4, 4, 8 * sp.cos(2 * t)); ic("E4 ic", x, 0, 0)
# E5
x = 200 + 100 * sp.cos(t) + 100 * sp.sin(t)
y = 150 + 100 * sp.sin(t)
ok("E5 eq1", zero(sp.diff(x, t) - (x - 2 * y + 100)))
ok("E5 eq2", zero(sp.diff(y, t) - (x - y - 50)))
ok("E5 ic", x.subs(t, 0) == 300 and y.subs(t, 0) == 150)
ode2("E5 x''+x=200", x, 0, 1, 200)
sf3("E5 min prey", 200 - 100 * math.sqrt(2), "58.6")
ok("E5 min pred", min(150 + 100 * math.sin(s / 100) for s in range(0, 629)) - 50 < 1e-3)

# Practice
x = 3 * sp.cos(4 * t); ode2("P1", x, 0, 16); ic("P1 ic", x, 3, 0)
sf3("P2 phi", math.atan(3 / 4), "0.644")
ok("P2", zero(sp.expand_trig(5 * sp.sin(2 * t + sp.atan(sp.Rational(3, 4)))) - (3 * sp.cos(2 * t) + 4 * sp.sin(2 * t))))
sf3("P3 vmax", math.pi / 4, "0.785"); sf3("P3 v", math.pi / 2 * math.sqrt(0.25 - 0.09), "0.628")
sf3("P5 period", 2 * math.pi / math.sqrt(80 / 0.2), "0.314")
ok("P6 classes", (6 ** 2 - 36 == 0) and (4 - 40 < 0) and (100 - 64 > 0))
x = E(-t) * (sp.cos(3 * t) + sp.sin(3 * t) / 3); ode2("P6b", x, 2, 10); ic("P6b ic", x, 1, 0)
ok("P7", 8 ** 2 == 4 * 16)
x = E(-t) - E(-4 * t); ode2("P8", x, 5, 4); ic("P8 ic", x, 0, 3)
tm = math.log(4) / 3
sf3("P8 t", tm, "0.462"); sf3("P8 x", float(x.subs(t, tm)), "0.472")
x = sp.cos(2 * t) - sp.cos(3 * t); ode2("P9", x, 0, 9, 5 * sp.cos(2 * t)); ic("P9 ic", x, 0, 0)
ode2("P10", -sp.Rational(3, 4) * t * sp.cos(2 * t), 0, 4, 3 * sp.sin(2 * t))
x = 3 * E(3 * t) + E(-t); y = 3 * E(3 * t) - E(-t)
ok("P11", zero(sp.diff(x, t) - x - 2 * y) and zero(sp.diff(y, t) - 2 * x - y) and x.subs(t, 0) == 4 and y.subs(t, 0) == 2)
x = 20 * E(t) + 10 * E(3 * t); y = 20 * E(t) - 10 * E(3 * t)
ok("P12", zero(sp.diff(x, t) - 2 * x + y) and zero(sp.diff(y, t) + x - 2 * y) and x.subs(t, 0) == 30 and y.subs(t, 0) == 10)
ode2("P12 x eq", x, -4, 3)
sf3("P12 t", 0.5 * math.log(2), "0.347")

# Section B
x = E(-2 * t) * (sp.Rational(3, 10) * sp.cos(3 * t) + sp.Rational(1, 5) * sp.sin(3 * t))
ode2("Q13", x, 8, 26, m=2); ic("Q13 ic", x, sp.Rational(3, 10), 0)
t1 = (math.pi - math.atan(1.5)) / 3
ok("Q13 first zero", abs(float(x.subs(t, t1))) < 1e-12 and all(float(x.subs(t, s * t1 / 200)) > 0 for s in range(200)))
sf3("Q13 t", t1, "0.720")
x = 5 * E(-t) - 3 * E(t); y = 5 * E(-t) - E(t)
ok("Q14 system", zero(sp.diff(x, t) - 2 * x + 3 * y) and zero(sp.diff(y, t) - x + 2 * y) and x.subs(t, 0) == 2 and y.subs(t, 0) == 4)
ode2("Q14 x''=x", x, 0, -1)
te = 0.5 * math.log(5 / 3)
sf3("Q14 t", te, "0.255"); sf3("Q14 y", float(y.subs(t, te)), "2.58")
ok("Q15 e0", abs(0.5 * 9.8 / 49 - 0.1) < 1e-12)
sf3("Q15 period", 2 * math.pi / math.sqrt(98), "0.635"); sf3("Q15 vmax", 0.05 * math.sqrt(98), "0.495")
sf3("Q15 t", (2 * math.pi / 3) / math.sqrt(98), "0.212")
x = E(-t) * (sp.cos(2 * t) - sp.sin(2 * t) / 2) + 2 * sp.sin(t) - sp.cos(t)
ode2("Q16", x, 2, 5, 10 * sp.sin(t)); ic("Q16 ic", x, 0, 0)
sf3("Q16 amp", math.sqrt(5), "2.24")

print()
print("PASS pb11" if not FAILS else f"FAILED pb11: {FAILS}")
sys.exit(1 if FAILS else 0)
