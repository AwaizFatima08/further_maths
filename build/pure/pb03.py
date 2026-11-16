UNIT = {
    "number": "B3",
    "title": "Higher derivatives and Maclaurin series",
    "tag": "Edexcel CP 4.5, 4.6 (A level) · IAL FP2 6.1, 6.2 · AQA D5 (A level: general term), D6 (AS: standard series) · "
           "OCR A 4.08a, 4.08b · OCR MEI Ps3, Ps4, Ps5 · CAIE 9231 P2 2.3 (implicit and parametric d²y/dx²; Maclaurin "
           "terms, no general term)",
    "notes": [
        ("h2", "B3.1 Higher derivatives (all boards; IAL FP2 6.1)"),
        ("p", "Differentiating f(x) again and again gives the <b>higher derivatives</b> f′′(x), f′′′(x), f⁽⁴⁾(x), …, f⁽ⁿ⁾(x), also "
              "written d²y/dx², d³y/dx³, …, dⁿy/dxⁿ. For many functions the derivatives follow a pattern, and the pattern gives a "
              "formula for the nth derivative. Such a formula can be proved by induction (Unit A8)."),
        ("box", "Useful nth derivatives", [
            "dⁿ/dxⁿ (e<sup>ax</sup>) = aⁿe<sup>ax</sup>.",
            "dⁿ/dxⁿ (sin x) = sin(x + nπ/2) and dⁿ/dxⁿ (cos x) = cos(x + nπ/2): the cycle sin, cos, −sin, −cos repeats every 4.",
            "If f(x) = ln(1 + x) then f⁽ⁿ⁾(x) = (−1)<sup>n−1</sup>(n − 1)!/(1 + x)ⁿ for n ≥ 1.",
            "If f(x) = (1 + x)<sup>k</sup> then f⁽ⁿ⁾(x) = k(k − 1)(k − 2)…(k − n + 1)(1 + x)<sup>k−n</sup>.",
        ]),
        ("h2", "B3.2 Second derivatives of implicit and parametric functions (CAIE 2.3; useful for all boards)"),
        ("p", "<b>Implicit.</b> Differentiate the relation once to find dy/dx. Then differentiate the <i>differentiated</i> relation "
              "again, using the product and chain rules on every term containing y, and solve for d²y/dx². Substitute numbers as "
              "early as possible: it saves algebra. For example, x² + y² = 25 gives x + y(dy/dx) = 0. Differentiating again gives "
              "1 + (dy/dx)² + y(d²y/dx²) = 0, so d²y/dx² = −(1 + (dy/dx)²)/y = −(x² + y²)/y³ = −25/y³."),
        ("p", "<b>Parametric.</b> If x and y are both functions of t, then dy/dx = (dy/dt)/(dx/dt) is a function of t. To differentiate "
              "it with respect to x, use the chain rule: d/dx = (d/dt) × (dt/dx)."),
        ("box", "Second derivative of a parametric curve", [
            "d²y/dx² = [ d/dt (dy/dx) ] ÷ (dx/dt).",
            "It is <b>not</b> (d²y/dt²) ÷ (d²x/dt²).",
            "At a stationary point dy/dx = 0. If d²y/dx² > 0 there it is a minimum; if d²y/dx² < 0 it is a maximum.",
        ]),
        ("figure", "pb03_param.png", "The curve x = t², y = t³ − 3t of Worked example B3.2, with a maximum at (1, 2) (t = −1) "
                                     "and a minimum at (1, −2) (t = 1).", 90),
        ("h2", "B3.3 Maclaurin series (Edexcel CP 4.5, AQA D5, OCR A 4.08a, MEI Ps3, IAL FP2 6.2, CAIE 2.3)"),
        ("p", "A <b>Maclaurin series</b> writes a function as a power series in x: f(x) = a₀ + a₁x + a₂x² + a₃x³ + … . To find the "
              "coefficients, put x = 0 to get a₀ = f(0). Differentiate: f′(x) = a₁ + 2a₂x + 3a₃x² + …, so a₁ = f′(0). Differentiate "
              "again: f′′(x) = 2a₂ + 6a₃x + …, so a₂ = f′′(0)/2. In general, differentiating r times leaves r! a<sub>r</sub> as "
              "the constant term, so a<sub>r</sub> = f⁽ʳ⁾(0)/r!."),
        ("box", "Maclaurin series (printed in every board's booklet)", [
            "f(x) = f(0) + f′(0)x + f′′(0)x²/2! + f′′′(0)x³/3! + … + f⁽ʳ⁾(0)xʳ/r! + …",
            "The <b>general term</b> is f⁽ʳ⁾(0)xʳ/r!. Edexcel, AQA (A level), OCR A, MEI and IAL can ask for it; CAIE asks only "
            "for the first few terms.",
            "The series exists only if f and all its derivatives are defined at x = 0. So ln x, √x, 1/x and cot x have no "
            "Maclaurin series.",
        ]),
        ("p", "For example, if f(x) = eˣ then every derivative is eˣ, so f⁽ʳ⁾(0) = 1 for all r and eˣ = 1 + x + x²/2! + x³/3! + …, "
              "with general term xʳ/r!."),
        ("h2", "B3.4 The standard series"),
        ("table", ["Function", "Series", "General term", "Valid for"], [
            ["eˣ", "1 + x + x²/2! + x³/3! + …", "xʳ/r!", "all x"],
            ["ln(1 + x)", "x − x²/2 + x³/3 − x⁴/4 + …", "(−1)<sup>r+1</sup>xʳ/r", "−1 < x ≤ 1"],
            ["sin x", "x − x³/3! + x⁵/5! − …", "(−1)ʳx<sup>2r+1</sup>/(2r + 1)!", "all x"],
            ["cos x", "1 − x²/2! + x⁴/4! − …", "(−1)ʳx<sup>2r</sup>/(2r)!", "all x"],
            ["(1 + x)ⁿ", "1 + nx + n(n − 1)x²/2! + …", "n(n − 1)…(n − r + 1)xʳ/r!", "|x| < 1 (all x if n is a positive integer)"],
            ["arctan x (CAIE MF19)", "x − x³/3 + x⁵/5 − …", "(−1)ʳx<sup>2r+1</sup>/(2r + 1)", "−1 ≤ x ≤ 1"],
            ["sinh x, cosh x (CAIE MF19; Unit B4)", "x + x³/3! + …;  1 + x²/2! + …", "x<sup>2r+1</sup>/(2r + 1)!;  x<sup>2r</sup>/(2r)!", "all x"],
            ["artanh x (CAIE MF19; Unit B5)", "x + x³/3 + x⁵/5 + …", "x<sup>2r+1</sup>/(2r + 1)", "−1 < x < 1"],
        ]),
        ("p", "In every series x is in <b>radians</b>. The first five series are printed in all the booklets (and are on the AQA AS "
              "course, D6); you need to recognise them, use them and quote their ranges of validity, but no board asks you to prove "
              "the ranges. Complex x is excluded."),
        ("h2", "B3.5 Convergence and the range of validity (MEI Ps4; all boards)"),
        ("p", "A <b>sequence</b> is a list of terms u₁, u₂, u₃, …; a <b>series</b> is the sum of the terms. The <b>partial sum</b> "
              "Sₙ = u₁ + u₂ + … + uₙ is the sum of the first n terms. A series <b>converges</b> if Sₙ tends to a finite limit S as "
              "n → ∞; S is called the sum to infinity. Otherwise the series <b>diverges</b>."),
        ("p", "A Maclaurin series only equals its function for x in the range of validity. For eˣ, sin x and cos x that is every x. "
              "For ln(1 + x) it is −1 < x ≤ 1: at x = 1 the series 1 − ½ + ⅓ − ¼ + … converges (slowly) to ln 2; at x = −1 it "
              "becomes −(1 + ½ + ⅓ + …), which diverges (Unit B7); and at x = 2 the terms 2, −2, 8/3, −4, … grow, so the partial "
              "sums swing about more and more wildly."),
        ("figure", "pb03_ln.png", "Partial sums of the series for ln(1 + x). Adding terms improves the fit for −1 < x ≤ 1, but "
                                  "for x > 1 the partial sums move further away from ln(1 + x).", 110),
        ("h2", "B3.6 Series of compound functions (Edexcel CP 4.6, AQA D6, OCR A 4.08b, MEI Ps5)"),
        ("bullets", [
            "<b>Substitute</b> into a standard series: replace x by 2x, −x, x², … . For example e^(−x²) = 1 − x² + x⁴/2! − … . "
            "The range of validity changes too: ln(1 − 2x) needs −1 < −2x ≤ 1, that is −½ ≤ x < ½.",
            "<b>Rewrite</b> the function first: ln(2 + x) = ln 2 + ln(1 + x/2), valid for −2 < x ≤ 2; (3 + x)⁻¹ = ⅓(1 + x/3)⁻¹, "
            "valid for |x| < 3.",
            "<b>Use log laws</b>: ln((1 + x)/(1 − x)) = ln(1 + x) − ln(1 − x) = 2(x + x³/3 + x⁵/5 + …), valid for −1 < x < 1.",
            "<b>Multiply</b> two series, keeping every product up to the power you need: eˣ sin x = x + x² + x³/3 + … .",
            "<b>Compose</b>: for e^(sin x), put u = sin x = x − x³/6 + … into e<sup>u</sup> = 1 + u + u²/2 + …, or differentiate "
            "repeatedly. Both are shown in Worked example B3.4.",
            "<b>Use an identity</b>: cos²x = ½(1 + cos 2x) = 1 − x² + x⁴/3 − … .",
            "<b>Differentiate or integrate</b> term by term inside the range of validity: differentiating the ln(1 + x) series "
            "gives 1 − x + x² − … = (1 + x)⁻¹.",
            "When two series are combined, the result is valid where <b>both</b> are valid (the intersection of the ranges).",
        ]),
        ("h2", "B3.7 Approximations and the error (MEI Ps3; all boards)"),
        ("p", "Stopping a series after a few terms gives a polynomial approximation, which is good when x is small. The <b>error</b> "
              "is the exact value minus the approximation; the relative error is error ÷ exact value. For a series whose terms "
              "alternate in sign and decrease in size, the error is smaller than the first term left out. For example "
              "ln 1.2 ≈ 0.2 − 0.2²/2 + 0.2³/3 = 0.182667, while ln 1.2 = 0.182322 (6 d.p.), an error of about −3.4 × 10⁻⁴; the "
              "next term, −0.2⁴/4 = −0.0004, is a little larger in size. Series also give approximate values of integrals that "
              "cannot be found exactly (Worked example B3.6). Using series to find limits is in Unit C2."),
        ("figure", "pb03_sin.png", "sin x and its Maclaurin polynomials of degree 1, 3, 5 and 7. Each extra term extends the "
                                   "interval on which the approximation is good.", 110),
        ("h2", "B3.8 Successive differentiation of a relation (CAIE 2.3)"),
        ("p", "When the derivatives of f become messy, find a simple relation that y = f(x) satisfies and differentiate the relation "
              "instead. For y = tan x, dy/dx = sec²x = 1 + y², so y′ = 1 + y², y′′ = 2yy′, y′′′ = 2(y′)² + 2yy′′, and so on. "
              "Put x = 0 at the end. The same idea works for a function that satisfies a differential equation, such as "
              "y = eˣ cos x, which satisfies y′′ = 2y′ − 2y (Question B3.16)."),
        ("box", "Given or learn", [
            "All boards print the Maclaurin formula and the series for eˣ, ln(1 + x), sin x, cos x and (1 + x)ⁿ with their ranges. "
            "CAIE MF19 also prints arctan x, sinh x, cosh x and artanh x. IAL also prints the Taylor forms (Unit C2).",
            "Learn: the parametric second-derivative formula, and how to combine series and find their ranges of validity.",
        ]),
        ("warn", "Common mistakes", [
            "Forgetting the factorials: the x³ term of sin x is −x³/3! = −x³/6, not −x³/3. (The ln(1 + x) series has r, not r!, "
            "in its denominators.)",
            "Using the wrong range after substituting: the series for ln(1 − 2x) is valid for −½ ≤ x < ½, not −1 < x ≤ 1.",
            "Writing ln(2 + x) = ln 2 + ln x. Take out the factor 2 first: ln(2(1 + x/2)).",
            "Multiplying series and missing cross terms, or keeping terms beyond the power asked for and then truncating wrongly.",
            "Parametric second derivative: dividing by d²x/dt², or forgetting to divide by dx/dt at all.",
            "Using degrees in a trigonometric series. Series need radians.",
            "General term: check it by putting r = 0 (or r = 1) and comparing with the first term you wrote down.",
        ]),
    ],
    "examples": [
        {
            "title": "A Maclaurin series from derivatives, with its general term",
            "question": "Use differentiation to find the Maclaurin series of f(x) = cos 2x up to the term in x⁶, and find its general "
                        "term. State the values of x for which it is valid.",
            "steps": [
                "f(x) = cos 2x, f′(x) = −2 sin 2x, f′′(x) = −4 cos 2x, f′′′(x) = 8 sin 2x, f⁽⁴⁾(x) = 16 cos 2x, and the pattern "
                "repeats with a factor 2 each time, so f⁽⁶⁾(x) = −64 cos 2x.",
                "At x = 0: f = 1, f′ = 0, f′′ = −4, f′′′ = 0, f⁽⁴⁾ = 16, f⁽⁵⁾ = 0, f⁽⁶⁾ = −64.",
                "cos 2x = 1 − 4x²/2! + 16x⁴/4! − 64x⁶/6! + … = <b>1 − 2x² + ⅔x⁴ − (4/45)x⁶ + …</b>",
                "The odd derivatives vanish at 0 and f⁽²ʳ⁾(0) = (−1)ʳ2<sup>2r</sup>, so the general term is "
                "<b>(−1)ʳ 2<sup>2r</sup> x<sup>2r</sup>/(2r)!</b>, valid for all x.",
                "Check: replacing x by 2x in the cos x series gives the same result.",
            ],
        },
        {
            "title": "Second derivatives: implicit and parametric",
            "question": "(a) The curve x² + xy + y² = 7 passes through (1, 2). Find the values of dy/dx and d²y/dx² at this point.\n"
                        "(b) A curve has parametric equations x = t², y = t³ − 3t. Show that d²y/dx² = 3(t² + 1)/(4t³), and find "
                        "the nature of each stationary point.",
            "steps": [
                "(a) 2x + y + xy′ + 2yy′ = 0. At (1, 2): 2 + 2 + y′ + 4y′ = 0, so <b>y′ = −4/5</b>.",
                "Differentiate again: 2 + y′ + y′ + xy′′ + 2(y′)² + 2yy′′ = 0, i.e. (x + 2y)y′′ = −(2 + 2y′ + 2(y′)²).",
                "At (1, 2) with y′ = −4/5: 5y′′ = −(2 − 8/5 + 32/25) = −42/25, so <b>y′′ = −42/125</b>.",
                "(b) dx/dt = 2t, dy/dt = 3t² − 3, so dy/dx = (3t² − 3)/(2t) = 3t/2 − 3/(2t).",
                "d/dt(dy/dx) = 3/2 + 3/(2t²) = 3(t² + 1)/(2t²). Divide by dx/dt = 2t: d²y/dx² = 3(t² + 1)/(4t³), as required.",
                "Stationary points: 3t² − 3 = 0, so t = ±1 (and dx/dt ≠ 0 there). t = 1 gives (1, −2) with d²y/dx² = 3/2 > 0: "
                "a <b>minimum</b>. t = −1 gives (1, 2) with d²y/dx² = −3/2 < 0: a <b>maximum</b>.",
            ],
        },
        {
            "title": "Combining standard series; the range of validity",
            "question": "Find the series expansion of ln((1 + x)/(1 − 2x)) up to the term in x³, find its general term, and state "
                        "the range of values of x for which the expansion is valid.",
            "steps": [
                "Use log laws: ln((1 + x)/(1 − 2x)) = ln(1 + x) − ln(1 − 2x).",
                "ln(1 + x) = x − x²/2 + x³/3 − …, valid for −1 < x ≤ 1.",
                "Replace x by −2x: ln(1 − 2x) = −2x − (−2x)²/2 + (−2x)³/3 − … = −2x − 2x² − (8/3)x³ − …, valid for "
                "−1 < −2x ≤ 1, i.e. −½ ≤ x < ½.",
                "Subtract: <b>3x + (3/2)x² + 3x³ + …</b>",
                "General term: (−1)<sup>r+1</sup>xʳ/r − (−1)<sup>r+1</sup>(−2x)ʳ/r = <b>[(−1)<sup>r+1</sup> + 2ʳ]xʳ/r</b>. "
                "Check: r = 1 gives 3x, r = 2 gives (3/2)x².",
                "Both expansions are needed, so the result is valid where both are: <b>−½ ≤ x < ½</b>.",
            ],
        },
        {
            "title": "A composite function, two ways",
            "question": "Find the Maclaurin series of e^(sin x) up to the term in x⁴\n(a) by differentiation,\n(b) by substituting "
                        "one series into another.",
            "steps": [
                "(a) y = e^(sin x). y′ = y cos x. y′′ = y′ cos x − y sin x. y′′′ = y′′ cos x − 2y′ sin x − y cos x. "
                "y⁽⁴⁾ = y′′′ cos x − 3y′′ sin x − 3y′ cos x + y sin x.",
                "At x = 0, y = 1: y′ = 1, y′′ = 1, y′′′ = 1 − 0 − 1 = 0, y⁽⁴⁾ = 0 − 0 − 3 + 0 = −3.",
                "So e^(sin x) = 1 + x + x²/2! + 0 − 3x⁴/4! = <b>1 + x + ½x² − ⅛x⁴ + …</b>",
                "(b) Let u = sin x = x − x³/6 + … . Then e<sup>u</sup> = 1 + u + u²/2 + u³/6 + u⁴/24 + …, with "
                "u² = x² − x⁴/3 + …, u³ = x³ + …, u⁴ = x⁴ + … .",
                "e<sup>u</sup> = 1 + (x − x³/6) + ½(x² − x⁴/3) + x³/6 + x⁴/24 + … = 1 + x + ½x² + 0x³ − ⅛x⁴ + …, which agrees.",
            ],
        },
        {
            "title": "Successive differentiation for tan x (CAIE style)",
            "question": "Given y = tan x, show that dy/dx = 1 + y². By differentiating this result repeatedly, find the Maclaurin "
                        "series of tan x up to the term in x⁵.",
            "steps": [
                "dy/dx = sec²x = 1 + tan²x = 1 + y².",
                "y′′ = 2yy′; y′′′ = 2(y′)² + 2yy′′; y⁽⁴⁾ = 6y′y′′ + 2yy′′′; y⁽⁵⁾ = 6(y′′)² + 8y′y′′′ + 2yy⁽⁴⁾.",
                "At x = 0: y = 0, y′ = 1, y′′ = 0, y′′′ = 2, y⁽⁴⁾ = 0, y⁽⁵⁾ = 0 + 16 + 0 = 16.",
                "tan x = x + 2x³/3! + 16x⁵/5! + … = <b>x + ⅓x³ + (2/15)x⁵ + …</b>",
                "tan x is an odd function, so only odd powers appear, which is a useful check.",
            ],
        },
        {
            "title": "Approximating an integral, and the error",
            "question": "(a) Write down the Maclaurin series of e^(−x²) up to the term in x⁶.\n(b) Hence find an approximation to "
                        "∫<sub>0</sub><sup>0.5</sup> e^(−x²) dx, giving 6 decimal places.\n(c) The exact value is 0.461281 (6 d.p.). "
                        "Find the error in your approximation and compare it with the next term of the series.",
            "steps": [
                "(a) Replace x by −x² in the eˣ series: e^(−x²) = 1 − x² + x⁴/2 − x⁶/6 + …, valid for all x.",
                "(b) ∫<sub>0</sub><sup>0.5</sup> (1 − x² + x⁴/2 − x⁶/6) dx = [x − x³/3 + x⁵/10 − x⁷/42] from 0 to 0.5",
                "= 0.5 − 0.041667 + 0.003125 − 0.000186 = <b>0.461272</b> (6 d.p.).",
                "(c) Error = 0.461281 − 0.461272 ≈ 9 × 10⁻⁶. The next term, x⁸/24, contributes 0.5⁹/216 ≈ 9.0 × 10⁻⁶, so the size "
                "of the first omitted term is a good estimate of the error.",
            ],
        },
    ],
    "practice": [
        "Find f′′′(x) when f(x) = x³ ln x.",
        "Prove by induction that dⁿ/dxⁿ (xeˣ) = (x + n)eˣ for all positive integers n.",
        "Given y² = 4x, show that d²y/dx² = −4/y³.",
        "A curve has parametric equations x = 3 cos t, y = 3 sin t. Find d²y/dx² in terms of t.",
        "Use differentiation to find the Maclaurin series of sec x up to the term in x⁴.",
        "Write down the series for e^(−2x) up to the term in x³, and its general term.",
        "Find the series for sin 3x up to the term in x⁵, and its general term.",
        "Expand (1 − 3x)^(−1/3) up to the term in x³ and state the range of validity.",
        "Find the series for ln(2 + x) up to the term in x³, and state the range of validity.",
        "Find the series for eˣ sin x up to the term in x⁴.",
        "Use the identity cos²x = ½(1 + cos 2x) to find the series for cos²x up to the term in x⁴.",
        "Use the series for sin x up to the term in x³ to estimate sin 0.2. Find the error, to 3 significant figures, and compare "
        "it with the next term of the series.",
    ],
    "answers": [
        "f′ = 3x² ln x + x², f′′ = 6x ln x + 5x, f′′′ = 6 ln x + 11.",
        "n = 1: d/dx(xeˣ) = (x + 1)eˣ, true. Assume true for n = k: dᵏ/dxᵏ(xeˣ) = (x + k)eˣ. Then d<sup>k+1</sup>/dx<sup>k+1</sup>(xeˣ) "
        "= eˣ + (x + k)eˣ = (x + k + 1)eˣ, the result for n = k + 1. True for n = 1, and true for n = k implies true for n = k + 1, "
        "so true for all positive integers n.",
        "2yy′ = 4 ⇒ y′ = 2/y; y′′ = −2y′/y² = −4/y³.",
        "dy/dx = −cot t; d²y/dx² = cosec²t ÷ (−3 sin t) = −1/(3 sin³t).",
        "f′ = sec x tan x, f′′ = 2sec³x − sec x; f(0) = 1, f′′(0) = 1, f⁽⁴⁾(0) = 5 (odd derivatives are 0): sec x = 1 + x²/2 + 5x⁴/24 + …",
        "1 − 2x + 2x² − (4/3)x³ + …; general term (−2)ʳxʳ/r!.",
        "3x − (9/2)x³ + (81/40)x⁵ − …; general term (−1)ʳ3<sup>2r+1</sup>x<sup>2r+1</sup>/(2r + 1)!.",
        "1 + x + 2x² + (14/3)x³ + …, valid for |x| < ⅓.",
        "ln 2 + x/2 − x²/8 + x³/24 − …, valid for −2 < x ≤ 2.",
        "x + x² + ⅓x³ + 0x⁴ + … (the next term is −x⁵/30).",
        "1 − x² + ⅓x⁴ − …",
        "sin 0.2 ≈ 0.2 − 0.008/6 = 0.198667 (6 d.p.); sin 0.2 = 0.198669, error ≈ 2.66 × 10⁻⁶. The next term, 0.2⁵/120 ≈ 2.67 × 10⁻⁶, "
        "is almost exactly the error.",
    ],
    "exam": [
        "f(x) = ln(cos x), −π/2 < x < π/2.\n"
        "(a) Show that f′(x) = −tan x, and find f′′(x), f′′′(x) and f⁽⁴⁾(x). [4]\n"
        "(b) Hence find the Maclaurin series of f(x) up to and including the term in x⁴. [2]\n"
        "(c) Use your series to find an approximation to ∫<sub>0</sub><sup>0.3</sup> ln(cos x) dx, giving 5 significant figures. [3]\n"
        "(d) Explain why ln(sin x) has no Maclaurin series. [1]",
        "A curve C has equation x² + 2xy + 3y² = 6.\n"
        "(a) Show that dy/dx = −(x + y)/(x + 3y). [3]\n"
        "(b) Find the coordinates of the stationary points of C. [3]\n"
        "(c) Find the value of d²y/dx² at each stationary point and hence determine their nature. [5]",
        "(a) Using the series for ln(1 + x), show that ln((1 + x)/(1 − x)) = 2(x + x³/3 + x⁵/5 + …), write down the general term "
        "and state the range of x for which the expansion is valid. [5]\n"
        "(b) By choosing a suitable value of x, use the first four non-zero terms to find an approximation to ln 2. Give 6 decimal "
        "places and find the error. [4]\n"
        "(c) Explain why putting x = 1 into the series for ln(1 + x) is a poor way to calculate ln 2. [2]",
        "y = eˣ cos x.\n"
        "(a) Show that d²y/dx² − 2 dy/dx + 2y = 0. [4]\n"
        "(b) By differentiating this equation, find the values of d³y/dx³ and d⁴y/dx⁴ at x = 0, and hence find the Maclaurin series "
        "of y up to and including the term in x⁴. [5]\n"
        "(c) Use your series to estimate ∫<sub>0</sub><sup>0.2</sup> eˣ cos x dx, giving 5 decimal places. [3]",
    ],
    "exam_answers": [
        "(a) f′ = (−sin x)/cos x = −tan x [B1]; f′′ = −sec²x [B1]; f′′′ = −2sec²x tan x [B1]; f⁽⁴⁾ = −4sec²x tan²x − 2sec⁴x [B1].\n"
        "(b) f(0) = 0, f′(0) = 0, f′′(0) = −1, f′′′(0) = 0, f⁽⁴⁾(0) = −2 [M1]; ln(cos x) = −x²/2 − x⁴/12 + … [A1].\n"
        "(c) ∫<sub>0</sub><sup>0.3</sup> (−x²/2 − x⁴/12) dx = [−x³/6 − x⁵/60] [M1 A1] = −0.0045 − 0.0000405 = −0.0045405 [A1].\n"
        "(d) ln(sin x) is not defined at x = 0 (sin 0 = 0), so f(0) does not exist. [B1]",
        "(a) 2x + 2y + 2xy′ + 6yy′ = 0 [M1 A1] ⇒ y′(x + 3y) = −(x + y) ⇒ y′ = −(x + y)/(x + 3y) [A1].\n"
        "(b) y′ = 0 ⇒ y = −x [M1]; x² − 2x² + 3x² = 6 ⇒ x² = 3 [M1]; (√3, −√3) and (−√3, √3) [A1].\n"
        "(c) Differentiate again: 2 + 4y′ + 2xy′′ + 6(y′)² + 6yy′′ = 0 [M1 A1]; with y′ = 0, y′′ = −1/(x + 3y) [M1]. "
        "At (√3, −√3): y′′ = 1/(2√3) = √3/6 > 0, minimum [A1]. At (−√3, √3): y′′ = −√3/6 < 0, maximum [A1].",
        "(a) ln(1 + x) = x − x²/2 + x³/3 − …; ln(1 − x) = −x − x²/2 − x³/3 − … [M1 A1]; subtracting, even powers cancel: "
        "2(x + x³/3 + x⁵/5 + …) [A1]. General term 2x<sup>2r+1</sup>/(2r + 1), r ≥ 0 [B1]. Valid for −1 < x < 1 [B1].\n"
        "(b) (1 + x)/(1 − x) = 2 ⇒ x = ⅓ [M1]. ln 2 ≈ 2(1/3 + 1/81 + 1/1215 + 1/15309) [M1] = 0.693135 (6 d.p.) [A1]. "
        "ln 2 = 0.693147, so the error is about 1.2 × 10⁻⁵ [A1].\n"
        "(c) The series 1 − ½ + ⅓ − ¼ + … converges very slowly [B1]: the error after n terms is about 1/(2n), so thousands of "
        "terms are needed for 3 d.p. (four terms give 0.583) [B1].",
        "(a) y′ = eˣ(cos x − sin x) [M1 A1]; y′′ = eˣ(cos x − sin x) + eˣ(−sin x − cos x) = −2eˣ sin x [A1]; "
        "y′′ − 2y′ + 2y = −2eˣ sin x − 2eˣ cos x + 2eˣ sin x + 2eˣ cos x = 0 [A1].\n"
        "(b) y′′′ = 2y′′ − 2y′, y⁽⁴⁾ = 2y′′′ − 2y′′ [M1]. At 0: y = 1, y′ = 1, y′′ = 0 [B1], y′′′ = −2, y⁽⁴⁾ = −4 [A1]. "
        "y = 1 + x − x³/3 − x⁴/6 + … [M1 A1].\n"
        "(c) ∫<sub>0</sub><sup>0.2</sup> (1 + x − x³/3 − x⁴/6) dx = [x + x²/2 − x⁴/12 − x⁵/30] [M1 A1] = 0.21986 (5 d.p.) [A1].",
    ],
}
