UNIT = {
    "number": "C2",
    "title": "Taylor series, limits, L'Hôpital's rule and Leibnitz's theorem",
    "tag": "Option · Edexcel Further Pure 1 (A level 9FM0 FP1 2.1, 2.2, 2.3, 2.4) · IAL FP2 6.3 (Taylor series) · "
           "AQA D7 (A level, compulsory: limits by Maclaurin series or l'Hôpital's rule)",
    "notes": [
        ("h2", "2.1 Taylor series about x = a"),
        ("p", "A Maclaurin series (unit B3) approximates f(x) by a polynomial built from the derivatives of f at 0. It is accurate "
              "only near x = 0, and it does not exist at all for functions such as ln x or √x, which are not defined or not "
              "differentiable at 0. A <b>Taylor series</b> does the same job near any point x = a: it is a power series in (x − a)."),
        ("box", "Taylor series (printed in the Edexcel and IAL booklets)", [
            "f(x) = f(a) + (x − a)f′(a) + (x − a)²/2! f″(a) + … + (x − a)ʳ/r! f⁽ʳ⁾(a) + …",
            "Equivalent form, putting x = a + h:  f(a + h) = f(a) + h f′(a) + h²/2! f″(a) + … + hʳ/r! f⁽ʳ⁾(a) + …",
            "a = 0 gives the Maclaurin series. The series is valid for x near a (within the interval of convergence).",
        ]),
        ("p", "<b>Why it works.</b> Suppose f(x) = c₀ + c₁(x − a) + c₂(x − a)² + c₃(x − a)³ + …. Putting x = a gives c₀ = f(a). "
              "Differentiating once and putting x = a gives c₁ = f′(a); twice gives 2c₂ = f″(a); r times gives r! cᵣ = f⁽ʳ⁾(a). "
              "So the coefficient of (x − a)ʳ is f⁽ʳ⁾(a)/r!."),
        ("p", "<b>Method.</b> Make a table of f, f′, f″, f‴ and their values at x = a, then substitute. Alternatively, write "
              "x = a + h and use a known Maclaurin series in h: for example ln x = ln(2 + h) = ln 2 + ln(1 + h/2), and "
              "eˣ = eᵃ × eʰ. This second method is often quicker and gives the general term."),
        ("figure", "pc02_sin_taylor.png", "Near x = π the Taylor polynomials of sin x in powers of (x − π) fit the curve closely; the cubic "
                                          "is much better than the linear one, but both drift away as |x − π| grows.", 100),
        ("p", "<b>Approximations.</b> Taylor polynomials give good estimates of values close to a, such as ln 2.1 (about 2) or "
              "√4.2 (about 4). The closer x is to a, the faster the terms shrink and the fewer terms you need."),
        ("figure", "pc02_ln_taylor.png", "ln x and its Taylor polynomials about x = 2. The cubic is accurate to 6 decimal places at x = 2.1.", 95),
        ("h2", "2.2 Limits using series expansions"),
        ("p", "A limit such as lim (x → 0) (sin x − x)/x³ has the <b>indeterminate form</b> 0/0: substituting x = 0 gives no "
              "information. Replace each function by its Maclaurin (or Taylor) series, simplify, cancel the lowest power of x, and "
              "only then let x → 0. Keep enough terms: you need every term up to the power of x in the denominator."),
        ("p", "For example (sin x − x)/x³ = (x − x³/6 + x⁵/120 − … − x)/x³ = −1/6 + x²/120 − … → −1/6."),
        ("table", ["Limit as x → 0", "Series reasoning", "Value"], [
            ["(sin x)/x", "1 − x²/6 + …", "1"],
            ["(1 − cos x)/x²", "(x²/2 − x⁴/24 + …)/x²", "½"],
            ["(eˣ − 1)/x", "1 + x/2 + …", "1"],
            ["(eˣ − 1 − x)/x²", "(x²/2 + x³/6 + …)/x²", "½"],
            ["(ln(1 + x) − x)/x²", "(−x²/2 + x³/3 − …)/x²", "−½"],
            ["(tan x − x)/x³", "(x³/3 + 2x⁵/15 + …)/x³", "⅓"],
        ]),
        ("h2", "2.3 L'Hôpital's rule"),
        ("box", "L'Hôpital's rule (learn it: it is not in any booklet)", [
            "If f(x) → 0 and g(x) → 0 as x → a (or both → ±∞), f and g are differentiable near a with g′(x) ≠ 0 near a, "
            "and lim f′(x)/g′(x) exists, then lim (x → a) f(x)/g(x) = lim (x → a) f′(x)/g′(x).",
            "Differentiate the numerator and the denominator <b>separately</b>, not the quotient. Repeat if the result is still 0/0 or ∞/∞.",
            "a may be finite or ±∞. Edexcel writes “L'Hospital”; AQA writes “l'Hôpital”. They are the same rule.",
        ]),
        ("p", "<b>Why it is true (simple case).</b> If f(a) = g(a) = 0 and g′(a) ≠ 0, then f(x)/g(x) = [f(x) − f(a)]/[g(x) − g(a)] "
              "= {[f(x) − f(a)]/(x − a)}/{[g(x) − g(a)]/(x − a)}, and as x → a this tends to f′(a)/g′(a). A Taylor expansion gives the "
              "same picture: near a, f and g behave like f′(a)(x − a) and g′(a)(x − a)."),
        ("p", "<b>Other indeterminate forms</b> must first be rearranged into 0/0 or ∞/∞."),
        ("bullets", [
            "<b>0 × ∞</b>: write the product as a quotient. x ln x = (ln x)/(1/x) → (1/x)/(−1/x²) = −x → 0 as x → 0⁺.",
            "<b>∞ − ∞</b>: combine into a single fraction, e.g. 1/x − 1/sin x = (sin x − x)/(x sin x).",
            "<b>1^∞, 0⁰, ∞⁰</b> (a power where both base and index vary): take logarithms. If L = lim f(x)^g(x), then ln L = lim g(x) ln f(x), "
            "which is a 0 × ∞ form. Find it, then L = e^(ln L). The classic result is lim (x → ∞) (1 + a/x)ˣ = eᵃ.",
            "<b>Substitution</b> can help: for x → ∞ put u = 1/x, so u → 0⁺.",
            "Standard results (also AQA E9): xᵏe⁻ˣ → 0 as x → ∞, and xᵏ ln x → 0 as x → 0⁺, for any k > 0. Exponentials beat powers, "
            "and powers beat logarithms.",
        ]),
        ("h2", "2.4 Leibnitz's theorem"),
        ("p", "The product rule (uv)′ = u′v + uv′ extends to the nth derivative in the same pattern as the binomial expansion of (a + b)ⁿ."),
        ("box", "Leibnitz's theorem (learn it: it is not in the booklet)", [
            "dⁿ/dxⁿ (uv) = Σ (r = 0 to n) ⁿCᵣ u⁽ⁿ⁻ʳ⁾ v⁽ʳ⁾ = u⁽ⁿ⁾v + n u⁽ⁿ⁻¹⁾v′ + [n(n − 1)/2!] u⁽ⁿ⁻²⁾v″ + … + u v⁽ⁿ⁾",
            "Here u⁽ᵏ⁾ means the kth derivative of u, and u⁽⁰⁾ = u.",
        ]),
        ("p", "Choose v to be the factor whose derivatives run out quickly (a polynomial), so that the sum has only a few non-zero "
              "terms, and u to be the factor whose nth derivative is easy (eᵏˣ, sin x, cos x). For example, with u = eˣ and v = x²: "
              "dⁿ/dxⁿ (x²eˣ) = x²eˣ + n(2x)eˣ + [n(n − 1)/2](2)eˣ = eˣ[x² + 2nx + n(n − 1)]."),
        ("p", "The theorem can be proved by induction on n, using ⁿCᵣ₋₁ + ⁿCᵣ = ⁿ⁺¹Cᵣ, exactly as for the binomial theorem."),
        ("p", "<b>Leibnitz and Maclaurin series.</b> If y satisfies a differential equation such as (1 − x²)y″ − xy′ − y = 0, apply "
              "Leibnitz to each product (n times), then put x = 0. This gives a <b>recurrence relation</b> between y⁽ⁿ⁺²⁾(0) and "
              "lower derivatives, from which as many Maclaurin coefficients as you like follow quickly."),
        ("box", "Given or learn? (by board)", [
            "Taylor series: printed in the Edexcel A level and IAL booklets (with the Maclaurin series).",
            "L'Hôpital's rule and Leibnitz's theorem: learn (not printed by Edexcel; AQA does not print l'Hôpital).",
            "Standard Maclaurin series (eˣ, sin x, cos x, ln(1 + x), (1 + x)ⁿ, arctan x): printed by every board.",
        ]),
        ("warn", "Common mistakes", [
            "Using the quotient rule when applying L'Hôpital's rule: differentiate top and bottom separately.",
            "Applying L'Hôpital's rule when the limit is not of the form 0/0 or ∞/∞, e.g. to (1 + x)/x as x → 0.",
            "Stopping a series too early: for a limit with x³ in the denominator, every series must go up to its x³ term.",
            "Writing the Taylor coefficient as f⁽ʳ⁾(a) without dividing by r!, or using f⁽ʳ⁾(0) instead of f⁽ʳ⁾(a).",
            "In Leibnitz's theorem, forgetting the binomial coefficients or pairing derivatives wrongly (orders must add to n).",
            "For 1^∞ limits, concluding the answer is 1. Take logarithms: (1 + 1/x)ˣ → e, not 1.",
        ]),
    ],
    "examples": [
        {
            "title": "Taylor series of sin x about π",
            "question": "Find the Taylor series expansion of sin x in ascending powers of (x − π), up to and including the term in (x − π)³.",
            "steps": [
                "f(x) = sin x, f(π) = 0. f′(x) = cos x, f′(π) = −1. f″(x) = −sin x, f″(π) = 0. f‴(x) = −cos x, f‴(π) = 1.",
                "sin x = 0 + (x − π)(−1) + (x − π)²/2! × 0 + (x − π)³/3! × 1 + …",
                "sin x ≈ −(x − π) + (x − π)³/6.",
                "Check: sin x = −sin(x − π), and the Maclaurin series of −sin h is −h + h³/6 − …, which agrees.",
            ],
        },
        {
            "title": "Taylor series of ln x about 2, and an approximation",
            "question": "(a) Find the Taylor series of ln x in powers of (x − 2) up to the term in (x − 2)³. "
                        "(b) Use it to estimate ln 2.1, and compare with the calculator value.",
            "steps": [
                "(a) f(x) = ln x, f′(x) = 1/x, f″(x) = −1/x², f‴(x) = 2/x³. At x = 2: ln 2, ½, −¼, ¼.",
                "ln x ≈ ln 2 + ½(x − 2) − (¼)(x − 2)²/2 + (¼)(x − 2)³/6 = ln 2 + (x − 2)/2 − (x − 2)²/8 + (x − 2)³/24.",
                "(Or: ln x = ln 2 + ln(1 + (x − 2)/2), then the series for ln(1 + u) with u = (x − 2)/2.)",
                "(b) x − 2 = 0.1: ln 2.1 ≈ 0.693147 + 0.05 − 0.00125 + 0.0000417 = 0.741939 (6 d.p.).",
                "The calculator gives ln 2.1 = 0.741937 (6 d.p.), so the error is only about 2 × 10⁻⁶.",
            ],
        },
        {
            "title": "Limits by series expansion",
            "question": "Use series expansions to find (a) lim (x → 0) (x cos x − sin x)/x³, (b) lim (x → 0) (e²ˣ − 1 − 2x)/(x sin x).",
            "steps": [
                "(a) x cos x = x − x³/2 + …, sin x = x − x³/6 + …. Numerator = −x³/2 + x³/6 + (terms in x⁵) = −x³/3 + ….",
                "So (x cos x − sin x)/x³ = −1/3 + (terms in x²) → −1/3.",
                "(b) e²ˣ = 1 + 2x + 2x² + (4/3)x³ + …, so the numerator is 2x² + (4/3)x³ + ….",
                "x sin x = x² − x⁴/6 + …. Divide top and bottom by x²: (2 + (4/3)x + …)/(1 − x²/6 + …) → 2.",
            ],
        },
        {
            "title": "L'Hôpital's rule, including repeated use",
            "question": "Use L'Hôpital's rule to find (a) lim (x → 0) (1 − cos 2x)/x², (b) lim (x → ∞) x²/eˣ, (c) lim (x → 0⁺) x ln x.",
            "steps": [
                "(a) 0/0 form. Differentiate top and bottom: lim 2 sin 2x/(2x), still 0/0. Again: lim 4 cos 2x/2 = 2.",
                "(b) ∞/∞ form. lim 2x/eˣ, still ∞/∞. lim 2/eˣ = 0. (Exponentials grow faster than any power.)",
                "(c) 0 × (−∞) form. Rewrite as (ln x)/(1/x), which is −∞/∞.",
                "L'Hôpital: lim (1/x)/(−1/x²) = lim (−x) = 0. So x ln x → 0 as x → 0⁺.",
            ],
        },
        {
            "title": "A limit of the form 1^∞",
            "question": "Show that lim (x → ∞) (1 + a/x)ˣ = eᵃ, where a is a constant. Hence find lim (x → 0) (1 + 3x)^(1/x).",
            "steps": [
                "Let L be the limit. ln L = lim x ln(1 + a/x), an ∞ × 0 form. Put u = 1/x, so u → 0⁺.",
                "ln L = lim (u → 0) ln(1 + au)/u, a 0/0 form. L'Hôpital: lim [a/(1 + au)]/1 = a.",
                "So L = eᵃ. (Series check: ln(1 + au)/u = a − a²u/2 + … → a.)",
                "For the second limit put x = 1/w with w → ∞ (for x → 0⁺; x → 0⁻ is similar): (1 + 3/w)ʷ → e³.",
            ],
        },
        {
            "title": "Leibnitz's theorem and a Maclaurin series from a differential equation",
            "question": "Given y = e^(arcsin x): (a) show that (1 − x²)y″ − xy′ − y = 0; (b) use Leibnitz's theorem to show that "
                        "(1 − x²)y⁽ⁿ⁺²⁾ − (2n + 1)xy⁽ⁿ⁺¹⁾ − (n² + 1)y⁽ⁿ⁾ = 0; (c) find the Maclaurin series of y up to the term in x⁵.",
            "steps": [
                "(a) y′ = y/√(1 − x²), so √(1 − x²) y′ = y. Differentiate: √(1 − x²) y″ − xy′/√(1 − x²) = y′.",
                "Multiply by √(1 − x²): (1 − x²)y″ − xy′ = √(1 − x²) y′ = y. So (1 − x²)y″ − xy′ − y = 0.",
                "(b) Leibnitz on (1 − x²)y″ (v = 1 − x², v′ = −2x, v″ = −2): (1 − x²)y⁽ⁿ⁺²⁾ − 2nxy⁽ⁿ⁺¹⁾ − n(n − 1)y⁽ⁿ⁾.",
                "Leibnitz on xy′: xy⁽ⁿ⁺¹⁾ + ny⁽ⁿ⁾. So (1 − x²)y⁽ⁿ⁺²⁾ − (2n + 1)xy⁽ⁿ⁺¹⁾ − [n(n − 1) + n + 1]y⁽ⁿ⁾ = 0, and n(n − 1) + n + 1 = n² + 1.",
                "(c) At x = 0: y⁽ⁿ⁺²⁾(0) = (n² + 1)y⁽ⁿ⁾(0). y(0) = 1, y′(0) = 1.",
                "y″(0) = 1 × y(0) = 1; y‴(0) = 2y′(0) = 2; y⁗(0) = 5y″(0) = 5; y⁽⁵⁾(0) = 10y‴(0) = 20.",
                "y = 1 + x + x²/2! + 2x³/3! + 5x⁴/4! + 20x⁵/5! + … = 1 + x + x²/2 + x³/3 + 5x⁴/24 + x⁵/6 + ….",
            ],
        },
    ],
    "practice": [
        "Find the Taylor series of eˣ in powers of (x − 1), up to and including the term in (x − 1)³.",
        "Find the Taylor series of cos x in powers of (x − π/3), up to and including the term in (x − π/3)².",
        "(a) Find the Taylor series of √x in powers of (x − 4) up to the term in (x − 4)². "
        "(b) Use it to estimate √4.2, and find the error compared with the calculator value.",
        "Show that the Taylor series of tan x about x = π/4, up to the term in (x − π/4)², is 1 + 2(x − π/4) + 2(x − π/4)².",
        "Use the expansion of ln(1 + u) to write ln(3 + x) as a series in ascending powers of x up to x³.",
        "Use series expansions to find (a) lim (x → 0) (1 − cos x)/x², (b) lim (x → 0) (eˣ − 1 − x)/x².",
        "Use series expansions to find lim (x → 0) (ln(1 + x) − x)/x².",
        "Use L'Hôpital's rule to find lim (x → 0) (tan x − x)/x³.",
        "Find (a) lim (x → 1) (ln x)/(x − 1), (b) lim (x → 0) (eˣ − e⁻ˣ)/sin x.",
        "Find (a) lim (x → ∞) (ln x)/√x, (b) lim (x → 0⁺) x² ln x.",
        "Find (a) lim (x → 0⁺) xˣ, (b) lim (x → ∞) (1 + 2/x)^(3x).",
        "(a) Use Leibnitz's theorem to find d⁴/dx⁴ (x³e²ˣ). (b) Show that dⁿ/dxⁿ (xeˣ) = (x + n)eˣ.",
    ],
    "answers": [
        "eˣ = e × e^(x − 1) ≈ e[1 + (x − 1) + (x − 1)²/2 + (x − 1)³/6].",
        "cos x ≈ ½ − (√3/2)(x − π/3) − ¼(x − π/3)².",
        "(a) f = x^(1/2), f′ = ½x^(−1/2), f″ = −¼x^(−3/2): at 4, values 2, ¼, −1/32. √x ≈ 2 + (x − 4)/4 − (x − 4)²/64. "
        "(b) √4.2 ≈ 2 + 0.05 − 0.000625 = 2.049375; calculator 2.0493902, error about 1.5 × 10⁻⁵.",
        "f = tan x, f′ = sec²x, f″ = 2sec²x tan x. At π/4: 1, 2, 4. tan x ≈ 1 + 2(x − π/4) + (4/2)(x − π/4)².",
        "ln(3 + x) = ln 3 + ln(1 + x/3) = ln 3 + x/3 − x²/18 + x³/81 − …, valid for −3 < x ≤ 3.",
        "(a) (x²/2 − x⁴/24 + …)/x² → ½. (b) (x²/2 + x³/6 + …)/x² → ½.",
        "(x − x²/2 + x³/3 − … − x)/x² = −½ + x/3 − … → −½.",
        "0/0: (sec²x − 1)/(3x²) = tan²x/(3x²) → ⅓ (using tan x/x → 1, or apply the rule twice more).",
        "(a) (1/x)/1 → 1. (b) (eˣ + e⁻ˣ)/cos x → 2/1 = 2.",
        "(a) (1/x)/(1/(2√x)) = 2/√x → 0. (b) (ln x)/(x⁻²) → (1/x)/(−2x⁻³) = −x²/2 → 0.",
        "(a) ln(xˣ) = x ln x → 0, so xˣ → e⁰ = 1. (b) ln L = lim 3x ln(1 + 2/x) = 3 × 2 = 6, so the limit is e⁶.",
        "(a) u = e²ˣ, v = x³: 16x³e²ˣ + 4(8)(3x²)e²ˣ + 6(4)(6x)e²ˣ + 4(2)(6)e²ˣ = e²ˣ(16x³ + 96x² + 144x + 48). "
        "(b) u = eˣ, v = x: only two terms, x eˣ + n(1)eˣ = (x + n)eˣ.",
    ],
    "exam": [
        "f(x) = tan x.\n"
        "(a) Show that f″(x) = 2sec²x tan x and f‴(x) = 2sec⁴x + 4sec²x tan²x. [4]\n"
        "(b) Hence find the Taylor series expansion of tan x in powers of (x − π/4), up to and including the term in (x − π/4)³. [3]\n"
        "(c) Use your answer to (b) to estimate tan 0.8 to 4 decimal places. [2]",

        "(a) Use Maclaurin series to find lim (x → 0) (eˣ − 1 − sin x)/x². [3]\n"
        "(b) Use L'Hôpital's rule to find lim (x → 0) (cosh x − cos x)/x². [3]\n"
        "(c) Find lim (x → ∞) (1 − 3/x)^(2x). [4]",

        "(a) Use Leibnitz's theorem to show that dⁿ/dxⁿ (x²e²ˣ) = 2ⁿ⁻²e²ˣ[4x² + 4nx + n(n − 1)] for n ≥ 2. [4]\n"
        "(b) Hence find the value of the 10th derivative of x²e²ˣ at x = 0. [2]\n"
        "(c) Verify the formula in (a) directly for n = 2. [2]",

        "Let y = (arcsin x)², −1 < x < 1.\n"
        "(a) Show that (1 − x²)(d²y/dx²) − x(dy/dx) = 2. [3]\n"
        "(b) Use Leibnitz's theorem to show that, for n ≥ 1, (1 − x²)y⁽ⁿ⁺²⁾ − (2n + 1)xy⁽ⁿ⁺¹⁾ − n²y⁽ⁿ⁾ = 0. [4]\n"
        "(c) Hence find the Maclaurin series of y up to and including the term in x⁶. [4]",
    ],
    "exam_answers": [
        "(a) f′ = sec²x; f″ = 2 sec x × sec x tan x = 2sec²x tan x M1 A1; f‴ = 4sec²x tan x × tan x + 2sec²x × sec²x M1 "
        "= 2sec⁴x + 4sec²x tan²x A1.\n"
        "(b) At π/4: f = 1, f′ = 2, f″ = 4, f‴ = 2(4) + 4(2)(1) = 16 M1 A1; "
        "tan x ≈ 1 + 2(x − π/4) + 2(x − π/4)² + (8/3)(x − π/4)³ A1.\n"
        "(c) x − π/4 = 0.0146018 M1; tan 0.8 ≈ 1.0296 A1 (calculator 1.0296386).",

        "(a) eˣ − 1 − sin x = (x + x²/2 + x³/6) − (x − x³/6) + … = x²/2 + x³/3 + … M1 A1; limit ½ A1.\n"
        "(b) 0/0: (sinh x + sin x)/(2x), still 0/0 M1; (cosh x + cos x)/2 M1 → 1 A1.\n"
        "(c) ln L = lim 2x ln(1 − 3/x) M1; with u = 1/x: lim 2 ln(1 − 3u)/u M1 = lim 2(−3/(1 − 3u)) = −6 A1; L = e⁻⁶ A1.",

        "(a) u = e²ˣ, v = x²: u⁽ᵏ⁾ = 2ᵏe²ˣ, v′ = 2x, v″ = 2, higher derivatives 0 M1; "
        "2ⁿe²ˣx² + n2ⁿ⁻¹e²ˣ(2x) + [n(n − 1)/2]2ⁿ⁻²e²ˣ(2) M1 A1 = 2ⁿ⁻²e²ˣ[4x² + 4nx + n(n − 1)] A1.\n"
        "(b) n = 10, x = 0: 2⁸ × 90 M1 = 23040 A1.\n"
        "(c) Direct: y′ = e²ˣ(2x² + 2x), y″ = e²ˣ(4x² + 8x + 2) M1; formula: 2⁰e²ˣ(4x² + 8x + 2), the same A1.",

        "(a) y′ = 2 arcsin x/√(1 − x²), so √(1 − x²) y′ = 2 arcsin x M1; differentiate: √(1 − x²) y″ − xy′/√(1 − x²) = 2/√(1 − x²) M1; "
        "multiply by √(1 − x²): (1 − x²)y″ − xy′ = 2 A1.\n"
        "(b) Differentiate n times (n ≥ 1, the right side gives 0): (1 − x²)y⁽ⁿ⁺²⁾ − 2nxy⁽ⁿ⁺¹⁾ − n(n − 1)y⁽ⁿ⁾ M1 A1, "
        "minus [xy⁽ⁿ⁺¹⁾ + ny⁽ⁿ⁾] M1; combine: −(2n + 1)xy⁽ⁿ⁺¹⁾ − n²y⁽ⁿ⁾ A1.\n"
        "(c) y(0) = 0, y′(0) = 0, and from (a) y″(0) = 2 B1. y⁽ⁿ⁺²⁾(0) = n²y⁽ⁿ⁾(0) M1: odd derivatives 0, y⁗(0) = 4 × 2 = 8, "
        "y⁽⁶⁾(0) = 16 × 8 = 128 A1. y = x² + 8x⁴/24 + 128x⁶/720 = x² + x⁴/3 + 8x⁶/45 A1.",
    ],
}
