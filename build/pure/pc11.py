"""Unit C11: Recurrence relations (Ed FP2 6.1-6.3 / AS FP2 5.1-5.3, OCR A 8.01a-i, MEI Xs1-Xs9)."""

UNIT = {
    "number": "C11",
    "title": "Recurrence relations",
    "tag": "Option · Edexcel FP2 6.1–6.3 (AS FP2 5.1–5.3: first order only) · OCR A Additional Pure 8.01a–f, h (AS Y535 "
           "and A level Y545), 8.01g, i (A level Y545 only) · OCR MEI Extra Pure Xs1–Xs9 (Y435) · not AQA, IAL or CAIE",
    "notes": [
        ("p", "A recurrence relation defines each term of a sequence from earlier terms, for example uₙ₊₁ = 3uₙ + 2. With "
              "enough starting values it fixes the whole sequence. Recurrences model anything that changes in steps: a "
              "population counted once a year, a loan balance each month, the number of ways to tile a strip. This unit "
              "describes how sequences behave in the long run, then shows how to solve linear recurrences exactly, giving "
              "a <b>closed form</b> uₙ = g(n), and how to prove a closed form by induction. The method mirrors the "
              "complementary function and particular integral for differential equations (Unit B10)."),

        ("h2", "11.1 Language of sequences (OCR A 8.01a, c; MEI Xs2)"),
        ("table", ["Term", "Meaning"], [
            ["Recurrence relation", "A rule giving uₙ₊₁ (or uₙ₊₂) in terms of earlier terms (and possibly n)."],
            ["Closed form", "A formula uₙ = g(n) giving each term directly from n."],
            ["Order", "How far back the rule reaches: uₙ₊₁ = f(uₙ) is first order; uₙ₊₂ = f(uₙ₊₁, uₙ) is second order. "
                      "A kth-order recurrence needs k starting values."],
            ["Linear", "The terms uₙ, uₙ₊₁, … appear only to the first power, multiplied by constants (or functions of n). "
                       "uₙ₊₁ = uₙ² + 1 and uₙ₊₁ = √(uₙ + 6) are non-linear."],
            ["Homogeneous", "A linear recurrence with no term free of u, e.g. uₙ₊₂ = uₙ₊₁ + uₙ. Adding 6, or 2ⁿ, or n makes "
                            "it non-homogeneous."],
            ["General / particular solution", "The general solution contains arbitrary constants (one per order); the "
                                              "particular solution satisfies given starting values."],
            ["Increasing / decreasing", "uₙ₊₁ > uₙ for all n (or < for all n); either is monotonic."],
            ["Periodic, period p", "uₙ₊ₚ = uₙ for all n, with p the smallest such positive integer."],
            ["Oscillating", "The terms go alternately (or repeatedly) up and down."],
            ["Convergent", "uₙ → L, a finite limit, as n → ∞. Otherwise divergent (including oscillating without settling)."],
        ]),
        ("figure", "pc11_behaviour.png", "Four kinds of long-run behaviour.", 150),

        ("h2", "11.2 Limits, fixed points and long-run behaviour (OCR A 8.01d; MEI Xs3, Xs9)"),
        ("p", "If uₙ₊₁ = f(uₙ) and uₙ → L, then letting n → ∞ on both sides gives L = f(L), provided f is continuous. So a "
              "limit, if there is one, must be a <b>fixed point</b> (a steady state) of f. Solve L = f(L), then decide which "
              "solution (if any) is the limit, for instance by sign (√ is never negative) or by computing terms. Solving "
              "L = f(L) does not by itself prove the sequence converges."),
        ("p", "Graphically, draw y = f(x) and y = x. From (u₁, 0) go up to the curve, across to y = x, up or down to the "
              "curve, and so on. If the path closes in on the intersection, the sequence converges to that fixed point. "
              "A <b>staircase</b> shows monotonic convergence; a <b>cobweb</b> shows oscillating convergence. Non-linear "
              "recurrences (MEI Xs3) are usually investigated this way or by computing terms. Rates of convergence are "
              "not required."),
        ("figure", "pc11_cobweb.png", "Fixed points are where y = f(x) meets y = x.", 150),

        ("h2", "11.3 First-order linear recurrences (all three boards)"),
        ("p", "Consider uₙ₊₁ = a uₙ + f(n), with a a constant. The solution is the sum of two parts, exactly as for "
              "differential equations:"),
        ("bullets", [
            "<b>Complementary function (CF)</b>: the general solution of the homogeneous part uₙ₊₁ = a uₙ, which is "
            "uₙ = A aⁿ (each step multiplies by a). The “auxiliary equation” here is just m = a.",
            "<b>Particular solution (PS)</b>: any one sequence satisfying the full recurrence. Try a form like f(n), "
            "substitute, and compare coefficients (table below).",
            "<b>General solution</b>: uₙ = CF + PS. Then use the starting value to find A. Always find A <i>after</i> adding "
            "the PS, never from the CF alone.",
        ]),
        ("table", ["f(n)", "Trial particular solution", "If the trial clashes with the CF"], [
            ["constant c", "λ (a constant)", "if a = 1: λn"],
            ["linear pn + q", "λn + μ", "if a = 1: n(λn + μ)"],
            ["quadratic", "λn² + μn + ν", "if a = 1: multiply by n"],
            ["d kⁿ", "λ kⁿ", "if k = a: λ n kⁿ"],
        ]),
        ("p", "When a = 1, uₙ₊₁ − uₙ = f(n) and the solution is a sum: uₙ = u₁ + Σ<sub>r=1</sub>ⁿ⁻¹ f(r), which can be found with "
              "the standard results of Unit A4. Edexcel's FP2 also writes the general first-order linear form "
              "uₙ₊₁ + f(n)uₙ = g(n) with coefficients depending on n; such questions give or suggest the closed form "
              "(e.g. uₙ₊₁ = (n + 1)uₙ, u₁ = 1 gives uₙ = n!), which you then verify or prove by induction."),
        ("box", "First-order linear recurrence uₙ₊₁ = a uₙ + b (a ≠ 1)", [
            "Fixed point: c = b/(1 − a). General solution: uₙ = c + A aⁿ.",
            "|a| < 1: uₙ → c for every starting value (monotonic if 0 < a < 1, oscillating if −1 < a < 0).",
            "a > 1: uₙ → ±∞ unless u starts exactly at c. a < −1: oscillating and divergent. a = −1: periodic, period 2.",
        ]),

        ("h2", "11.4 Fibonacci and Lucas sequences, and φ (OCR A 8.01e)"),
        ("p", "The Fibonacci sequence is F₁ = 1, F₂ = 1, Fₙ₊₂ = Fₙ₊₁ + Fₙ: 1, 1, 2, 3, 5, 8, 13, … (with F₀ = 0). The Lucas "
              "sequence uses the same rule with L₁ = 1, L₂ = 3: 1, 3, 4, 7, 11, 18, …. The golden ratio φ = (1 + √5)/2 ≈ "
              "1.618 is the positive root of m² = m + 1, so φ² = φ + 1 and 1/φ = φ − 1. The other root is "
              "ψ = (1 − √5)/2 = −1/φ ≈ −0.618."),
        ("box", "Fibonacci, Lucas and φ", [
            "Binet's formula: Fₙ = (φⁿ − ψⁿ)/√5. Lucas: Lₙ = φⁿ + ψⁿ.",
            "Fₙ₊₁/Fₙ → φ as n → ∞, because |ψ/φ| < 1 so (ψ/φ)ⁿ → 0.",
            "φⁿ = Fₙφ + Fₙ₋₁ for n ≥ 1 (proved by induction from φ² = φ + 1).",
            "Since |ψⁿ/√5| < ½, Fₙ is the integer nearest to φⁿ/√5.",
        ]),
        ("figure", "pc11_fibratio.png", "The ratios Fₙ₊₁/Fₙ oscillate about φ and converge to it.", 95),

        ("h2", "11.5 Second-order linear homogeneous recurrences (Edexcel FP2 A level, OCR A 8.01g, MEI Xs7)"),
        ("p", "For a uₙ₊₂ + b uₙ₊₁ + c uₙ = 0, try uₙ = mⁿ: dividing by mⁿ gives the <b>auxiliary equation</b> "
              "am² + bm + c = 0. Any combination of solutions is a solution (the recurrence is linear), which gives:"),
        ("table", ["Roots of am² + bm + c = 0", "General solution"], [
            ["Distinct real α, β", "uₙ = Aαⁿ + Bβⁿ"],
            ["Repeated root α", "uₙ = (A + Bn)αⁿ"],
            ["Complex r e<sup>±iθ</sup> = r(cos θ ± i sin θ)", "uₙ = rⁿ(A cos nθ + B sin nθ) (real A, B)"],
        ]),
        ("p", "The two constants come from two starting values. Examples: uₙ₊₂ = 4uₙ₊₁ − 4uₙ, u₀ = 1, u₁ = 4 has m = 2 "
              "repeated, so uₙ = (A + Bn)2ⁿ; A = 1 and 2(1 + B) = 4 give uₙ = (n + 1)2ⁿ. And uₙ₊₂ = 2uₙ₊₁ − 2uₙ, u₀ = 0, "
              "u₁ = 1 has m = 1 ± i = √2 e<sup>±iπ/4</sup>, so uₙ = 2<sup>n/2</sup>(A cos(nπ/4) + B sin(nπ/4)); A = 0 and B = 1 give "
              "uₙ = 2<sup>n/2</sup> sin(nπ/4). With complex roots of modulus r, the terms oscillate; they converge to 0 if r < 1, "
              "stay bounded (and may be periodic) if r = 1, and diverge if r > 1."),

        ("h2", "11.6 Second-order non-homogeneous recurrences (Edexcel FP2 A level, OCR A 8.01g, MEI Xs8)"),
        ("p", "For a uₙ₊₂ + b uₙ₊₁ + c uₙ = f(n): general solution = CF (from 11.5) + PS, with trial forms as in the "
              "first-order table. If the trial form is already part of the CF (e.g. f(n) = constant and m = 1 is an "
              "auxiliary root, or f(n) = kⁿ with k an auxiliary root), multiply the trial by n (by n² for a repeated "
              "root). Use the two starting values only after writing the full general solution."),

        ("h2", "11.7 Modelling (Edexcel FP2 6.2, OCR A 8.01h–i, MEI Xs1)"),
        ("bullets", [
            "Populations: births and deaths as proportions of the current population, plus fixed migration or harvesting: "
            "Pₙ₊₁ = (1 + b − d)Pₙ − h.",
            "Finance: a loan B with interest rate i per period and repayment R per period: uₙ₊₁ = (1 + i)uₙ − R.",
            "Counting: tilings, arrangements and Fibonacci's rabbits give second-order recurrences.",
            "Whole numbers: populations of animals are integers, so a model may use INT(x), the integer part of x (OCR "
            "A 8.01h). A model with INT cannot usually be solved exactly; compute terms instead and compare with the "
            "continuous model.",
            "Always interpret: what the fixed point means, whether it is reached, and when the model stops being "
            "realistic (e.g. a negative population).",
        ]),

        ("h2", "11.8 Verifying and proving closed forms (Edexcel FP2 6.3, OCR A 8.01b, MEI Xs4, Xs9)"),
        ("p", "To <b>verify</b> a given solution, substitute it into the recurrence and check both sides agree, and check the "
              "starting values. To <b>prove</b> it, use induction (Unit A8): for a first-order recurrence, one basis case "
              "and the step from n = k to n = k + 1; for a second-order recurrence, two basis cases and the step "
              "“true for n = k and n = k + 1 ⇒ true for n = k + 2”. Properties of the solution (that terms are integers, "
              "that uₙ → L, that uₙ > 0) are then deduced from the closed form."),
        ("warn", "Common mistakes", [
            "Finding the constants from the CF before adding the particular solution. Always use the full general solution.",
            "Using a trial PS that is already part of the CF (e.g. λ2ⁿ when 2 is an auxiliary root); the coefficient "
            "equation then has no solution. Multiply by n.",
            "Indexing errors: if the first term is u₁ the general solution uₙ = A aⁿ + … uses n = 1, not n = 0, to find A.",
            "Assuming a sequence converges because L = f(L) has a solution. Check by the form of the solution, a cobweb, "
            "or by computing terms.",
            "Writing the complex-root solution with complex constants and leaving the answer non-real; give real "
            "uₙ = rⁿ(A cos nθ + B sin nθ).",
            "In induction for a second-order recurrence, checking only one starting value or assuming only one previous "
            "case.",
        ]),
    ],
    "examples": [
        {
            "title": "Describing behaviour and finding a limit",
            "question": "Describe the behaviour of each sequence. (a) u₁ = 2, uₙ₊₁ = 1/(1 − uₙ). (b) u₁ = 0, "
                        "uₙ₊₁ = −½uₙ + 3: find the limit and a closed form. (c) u₁ = 0, uₙ₊₁ = √(uₙ + 6): find the limit, "
                        "assuming it exists.",
            "steps": [
                "(a) u₂ = 1/(1 − 2) = −1, u₃ = 1/2, u₄ = 1/(1/2) = 2 = u₁. So the sequence is 2, −1, ½, 2, −1, ½, …: "
                "periodic with period 3.",
                "(b) Terms: 0, 3, 1.5, 2.25, 1.875, 2.0625, …: oscillating. Fixed point: L = −½L + 3 gives L = 2. "
                "General solution uₙ = 2 + A(−½)ⁿ; u₁ = 0 gives 2 − A/2 = 0, A = 4, so uₙ = 2 + 4(−½)ⁿ. As (−½)ⁿ → 0, "
                "uₙ → 2: oscillating and convergent.",
                "(c) Terms 0, √6 ≈ 2.449, 2.907, 2.985, …: increasing. A limit satisfies L = √(L + 6), so L² − L − 6 = 0, "
                "(L − 3)(L + 2) = 0. L = −2 is impossible since square roots are non-negative, so L = 3.",
                "The staircase and cobweb diagrams for (c) and (b) are shown in 11.2.",
            ],
        },
        {
            "title": "First-order recurrence with a linear term, and proof by induction",
            "question": "(a) Solve uₙ₊₁ = 3uₙ − 4n + 2, u₁ = 5. (b) Prove your closed form by induction.",
            "steps": [
                "(a) CF: uₙ = A × 3ⁿ.",
                "PS: try uₙ = λn + μ. Then λ(n + 1) + μ = 3(λn + μ) − 4n + 2. Coefficients of n: λ = 3λ − 4, so λ = 2. "
                "Constants: λ + μ = 3μ + 2, so 2 + μ = 3μ + 2 and μ = 0. PS: uₙ = 2n.",
                "General solution uₙ = A × 3ⁿ + 2n. u₁ = 5: 3A + 2 = 5, A = 1. So <b>uₙ = 3ⁿ + 2n</b>.",
                "Check: u₂ = 3 × 5 − 4 + 2 = 13 and 3² + 4 = 13. ✓",
                "(b) <b>Basis</b>: n = 1: 3 + 2 = 5 = u₁. <b>Assume</b> uₖ = 3ᵏ + 2k for some positive integer k. "
                "<b>Step</b>: uₖ₊₁ = 3(3ᵏ + 2k) − 4k + 2 = 3ᵏ⁺¹ + 2k + 2 = 3ᵏ⁺¹ + 2(k + 1). "
                "<b>Conclusion</b>: true for n = 1, and true for n = k ⇒ true for n = k + 1, so true for all positive "
                "integers n by induction.",
            ],
        },
        {
            "title": "An exponential term, including the clashing case",
            "question": "Solve (a) uₙ₊₁ = 2uₙ + 3ⁿ, u₀ = 3, (b) uₙ₊₁ = 2uₙ + 2ⁿ, u₀ = 1.",
            "steps": [
                "(a) CF A × 2ⁿ. Try PS λ3ⁿ: λ3ⁿ⁺¹ = 2λ3ⁿ + 3ⁿ ⇒ 3λ = 2λ + 1 ⇒ λ = 1.",
                "uₙ = A × 2ⁿ + 3ⁿ; u₀ = 3 ⇒ A + 1 = 3, A = 2. So uₙ = 2ⁿ⁺¹ + 3ⁿ.",
                "(b) Now λ2ⁿ fails (it gives 2λ = 2λ + 1), because 2ⁿ is in the CF. Try λn2ⁿ:",
                "λ(n + 1)2ⁿ⁺¹ = 2λn2ⁿ + 2ⁿ ⇒ 2λ(n + 1) = 2λn + 1 ⇒ λ = ½. PS: n2ⁿ⁻¹.",
                "uₙ = A × 2ⁿ + n2ⁿ⁻¹; u₀ = 1 ⇒ A = 1. So uₙ = 2ⁿ + n2ⁿ⁻¹ = (n + 2)2ⁿ⁻¹.",
                "Check (b): u₁ = 2 + 1 = 3 and (1 + 2) × 2⁰ = 3 ✓; u₂ = 6 + 2 = 8 and 4 × 2 = 8 ✓.",
            ],
        },
        {
            "title": "The Fibonacci sequence and the golden ratio (OCR A)",
            "question": "F₀ = 0, F₁ = 1, Fₙ₊₂ = Fₙ₊₁ + Fₙ. (a) Find a closed form for Fₙ. (b) Show that Fₙ₊₁/Fₙ → φ.",
            "steps": [
                "(a) Auxiliary equation m² = m + 1, i.e. m² − m − 1 = 0, so m = (1 ± √5)/2: φ = (1 + √5)/2 and "
                "ψ = (1 − √5)/2.",
                "General solution Fₙ = Aφⁿ + Bψⁿ. F₀ = 0: A + B = 0. F₁ = 1: Aφ + Bψ = A(φ − ψ) = A√5 = 1.",
                "So A = 1/√5, B = −1/√5 and <b>Fₙ = (φⁿ − ψⁿ)/√5</b> (Binet's formula). Check: F₂ = (φ² − ψ²)/√5 "
                "= (φ − ψ)(φ + ψ)/√5 = √5 × 1/√5 = 1 ✓.",
                "(b) Fₙ₊₁/Fₙ = (φⁿ⁺¹ − ψⁿ⁺¹)/(φⁿ − ψⁿ). Divide top and bottom by φⁿ: = (φ − ψ(ψ/φ)ⁿ)/(1 − (ψ/φ)ⁿ).",
                "|ψ/φ| = 0.618…/1.618… < 1, so (ψ/φ)ⁿ → 0 and Fₙ₊₁/Fₙ → φ ≈ 1.618.",
            ],
        },
        {
            "title": "A second-order non-homogeneous recurrence (Edexcel FP2)",
            "question": "Solve 2uₙ₊₂ + 7uₙ₊₁ − 15uₙ = 6, given u₀ = 2 and u₁ = −3. Describe the long-run behaviour.",
            "steps": [
                "Auxiliary equation 2m² + 7m − 15 = 0 ⇒ (2m − 3)(m + 5) = 0 ⇒ m = 3/2 or −5. CF: A(3/2)ⁿ + B(−5)ⁿ.",
                "PS: try uₙ = c (1 is not an auxiliary root). 2c + 7c − 15c = 6 ⇒ −6c = 6 ⇒ c = −1.",
                "General solution uₙ = A(3/2)ⁿ + B(−5)ⁿ − 1.",
                "u₀ = 2: A + B − 1 = 2, so A + B = 3. u₁ = −3: (3/2)A − 5B − 1 = −3, so 3A − 10B = −4. "
                "Solving: A = 2, B = 1.",
                "<b>uₙ = 2(3/2)ⁿ + (−5)ⁿ − 1</b>. Check: u₂ = (6 − 7u₁ + 15u₀)/2 = (6 + 21 + 30)/2 = 28.5, and "
                "2 × 9/4 + 25 − 1 = 28.5 ✓.",
                "The (−5)ⁿ term dominates, so the terms alternate in sign with rapidly growing size: oscillating and "
                "divergent.",
            ],
        },
        {
            "title": "Modelling a loan (OCR A 8.01h, MEI Xs1)",
            "question": "Sam borrows £5000. At the end of each month, interest of 1% is added to the amount owed and then "
                        "Sam repays £R. Let uₙ be the amount owed after n months. (a) Write down a recurrence for uₙ and "
                        "solve it. (b) Find R, to the nearest penny, if the loan is repaid exactly after 24 months. "
                        "(c) Find the total interest paid.",
            "steps": [
                "(a) uₙ₊₁ = 1.01uₙ − R, u₀ = 5000. Fixed point: c = 1.01c − R ⇒ c = 100R.",
                "General solution uₙ = 100R + A(1.01)ⁿ; u₀ = 5000 ⇒ A = 5000 − 100R. So uₙ = 100R + (5000 − 100R)(1.01)ⁿ.",
                "(b) u₂₄ = 0 ⇒ 100R(1.01²⁴ − 1) = 5000 × 1.01²⁴ ⇒ R = 50 × 1.01²⁴/(1.01²⁴ − 1).",
                "1.01²⁴ = 1.269735 (6 d.p.), so R = 50 × 1.269735/0.269735 = <b>£235.37</b>.",
                "(c) Total repaid 24 × 235.37 = £5648.88, so the interest is about <b>£648.88</b> (using the rounded "
                "payment).",
                "Interpretation: 100R ≈ 23537 is the balance at which interest equals the repayment; because the debt "
                "starts below it, the debt falls, faster and faster.",
            ],
        },
    ],
    "practice": [
        "Write down the first five terms of each sequence and describe its behaviour.\n"
        "(a) u₁ = 1, uₙ₊₁ = 3 − uₙ (b) u₁ = 0, uₙ₊₁ = ½uₙ + 1 (c) uₙ = (−1)ⁿ n",
        "The sequence u₁ = 1, uₙ₊₁ = √(2uₙ + 3) converges. Find its limit, justifying your choice of root.",
        "Solve (a) uₙ₊₁ = 4uₙ, u₀ = 3 (b) uₙ₊₁ = 4uₙ − 6, u₀ = 5.",
        "Solve uₙ₊₁ = 2uₙ + n, u₀ = 0.",
        "Solve uₙ₊₁ = uₙ + 2n + 1, u₁ = 1.",
        "Solve uₙ₊₁ = 3uₙ + 2ⁿ, u₀ = 2.",
        "Solve uₙ₊₁ = 5uₙ + 5ⁿ, u₀ = 1.",
        "Solve uₙ₊₂ = uₙ₊₁ + 6uₙ, u₀ = 0, u₁ = 5.",
        "Solve uₙ₊₂ = 6uₙ₊₁ − 9uₙ, u₀ = 1, u₁ = 6.",
        "(a) Solve uₙ₊₂ = uₙ₊₁ − uₙ, u₀ = 1, u₁ = 1, giving a real closed form. (b) Show that the sequence is periodic and "
        "state its period.",
        "Solve uₙ₊₂ − 5uₙ₊₁ + 6uₙ = 4, u₀ = 0, u₁ = 1.",
        "The Lucas sequence is L₁ = 1, L₂ = 3, Lₙ₊₂ = Lₙ₊₁ + Lₙ. Show that Lₙ = φⁿ + ψⁿ, where φ = (1 + √5)/2 and "
        "ψ = (1 − √5)/2, and find L₁₀.",
    ],
    "answers": [
        "(a) 1, 2, 1, 2, 1: periodic, period 2. (b) 0, 1, 1.5, 1.75, 1.875: increasing, converging to 2. "
        "(c) −1, 2, −3, 4, −5: oscillating and divergent.",
        "L = √(2L + 3) ⇒ L² − 2L − 3 = 0 ⇒ L = 3 or −1. Terms are positive (square roots), so L = 3.",
        "(a) uₙ = 3 × 4ⁿ. (b) Fixed point c = 2; uₙ = 2 + 3 × 4ⁿ.",
        "PS λn + μ: λ = −1, μ = −1. uₙ = A2ⁿ − n − 1, A = 1: uₙ = 2ⁿ − n − 1.",
        "a = 1: uₙ = 1 + Σ<sub>r=1</sub>ⁿ⁻¹(2r + 1) = 1 + (n − 1)n + (n − 1) = n².",
        "PS λ2ⁿ: 2λ = 3λ + 1, λ = −1. uₙ = A3ⁿ − 2ⁿ, A = 3: uₙ = 3ⁿ⁺¹ − 2ⁿ.",
        "Clash, so PS λn5ⁿ: 5λ(n + 1) = 5λn + 1, λ = 1/5. uₙ = A5ⁿ + n5ⁿ⁻¹, A = 1: uₙ = 5ⁿ + n5ⁿ⁻¹ = (n + 5)5ⁿ⁻¹.",
        "m² − m − 6 = 0, m = 3, −2. A + B = 0, 3A − 2B = 5 ⇒ A = 1, B = −1. uₙ = 3ⁿ − (−2)ⁿ.",
        "(m − 3)² = 0. uₙ = (A + Bn)3ⁿ; A = 1, 3(1 + B) = 6 ⇒ B = 1. uₙ = (n + 1)3ⁿ.",
        "(a) m² − m + 1 = 0, m = e<sup>±iπ/3</sup> (modulus 1). uₙ = A cos(nπ/3) + B sin(nπ/3); A = 1, ½ + (√3/2)B = 1 ⇒ "
        "B = 1/√3. uₙ = cos(nπ/3) + (1/√3) sin(nπ/3). (b) Terms 1, 1, 0, −1, −1, 0, 1, 1, …; cos and sin of nπ/3 repeat "
        "when n increases by 6: period 6.",
        "PS c: c − 5c + 6c = 4, c = 2. uₙ = A2ⁿ + B3ⁿ + 2; A + B = −2, 2A + 3B = −1 ⇒ A = −5, B = 3. "
        "uₙ = 3ⁿ⁺¹ − 5 × 2ⁿ + 2.",
        "φ, ψ are the roots of m² = m + 1, so Lₙ = Aφⁿ + Bψⁿ. With A = B = 1: L₁ = φ + ψ = 1 ✓, "
        "L₂ = φ² + ψ² = (φ + ψ)² − 2φψ = 1 + 2 = 3 ✓; two starting values fix the solution. L₁₀ = 123.",
    ],
    "exam": [
        "(Edexcel FP2) A sequence satisfies uₙ₊₂ + uₙ₊₁ − 6uₙ = 4n + 1, n ≥ 0, with u₀ = 0 and u₁ = 0.\n"
        "(a) Find the complementary function. [2]\n"
        "(b) Find a particular solution of the form λn + μ. [3]\n"
        "(c) Hence show that uₙ = 2ⁿ − n − 1. [3]\n"
        "(d) Prove by induction that uₙ = 2ⁿ − n − 1 for all n ≥ 0. [5]",
        "(OCR A) A lake contains 1000 fish. Each year the population grows by 10%, and then 120 fish are removed. Pₙ is "
        "the population n years after the start.\n"
        "(a) Write down a recurrence relation for Pₙ. [1]\n"
        "(b) Solve it to find Pₙ in terms of n. [4]\n"
        "(c) Find the year in which the model predicts the fish will die out. [3]\n"
        "(d) A refined model is Pₙ₊₁ = INT(1.1Pₙ) − 120. Find P₁, P₂ and P₃ in this model and compare with part (b). [2]\n"
        "(e) Describe the long-term behaviour of the original model for different initial populations P₀. [2]",
        "(OCR A) The Fibonacci sequence is F₀ = 0, F₁ = 1, Fₙ₊₂ = Fₙ₊₁ + Fₙ, and φ = (1 + √5)/2.\n"
        "(a) Show that φ² = φ + 1. [1]\n"
        "(b) Prove by induction that φⁿ = Fₙφ + Fₙ₋₁ for all positive integers n. [5]\n"
        "(c) The number ψ = (1 − √5)/2 also satisfies ψⁿ = Fₙψ + Fₙ₋₁. Deduce that Fₙ = (φⁿ − ψⁿ)/√5. [3]\n"
        "(d) Hence show that Fₙ₊₁/Fₙ → φ as n → ∞. [2]",
        "(Edexcel FP2, OCR A, MEI) A sequence satisfies uₙ₊₂ = 2uₙ₊₁ − 4uₙ, with u₀ = 1 and u₁ = 1.\n"
        "(a) Show that uₙ = 2ⁿ cos(nπ/3). [5]\n"
        "(b) Show that uₙ₊₆ = 64uₙ. [2]\n"
        "(c) Find u₃₀. [1]\n"
        "(d) Describe the long-run behaviour of the sequence. [2]",
    ],
    "exam_answers": [
        "(a) m² + m − 6 = 0 ⇒ m = 2, −3 M1; CF A2ⁿ + B(−3)ⁿ A1.\n"
        "(b) λ(n + 2) + μ + λ(n + 1) + μ − 6λn − 6μ = 4n + 1 M1; −4λ = 4 ⇒ λ = −1 A1; 3λ − 4μ = 1 ⇒ μ = −1 A1. "
        "PS −n − 1.\n"
        "(c) uₙ = A2ⁿ + B(−3)ⁿ − n − 1 M1; u₀: A + B = 1; u₁: 2A − 3B = 2 M1; A = 1, B = 0 A1.\n"
        "(d) n = 0: 1 − 0 − 1 = 0 = u₀; n = 1: 2 − 1 − 1 = 0 = u₁ B1. Assume uₖ = 2ᵏ − k − 1 and uₖ₊₁ = 2ᵏ⁺¹ − k − 2 "
        "M1. uₖ₊₂ = −uₖ₊₁ + 6uₖ + 4k + 1 = −2ᵏ⁺¹ + k + 2 + 6 × 2ᵏ − 6k − 6 + 4k + 1 M1 = 4 × 2ᵏ − k − 3 A1 "
        "= 2ᵏ⁺² − (k + 2) − 1. Conclusion: true for n = 0, 1 and for n = k, k + 1 ⇒ n = k + 2, so true for all n ≥ 0 A1.",
        "(a) Pₙ₊₁ = 1.1Pₙ − 120, P₀ = 1000 B1.\n"
        "(b) Fixed point c = 1.1c − 120 ⇒ c = 1200 M1 A1; Pₙ = 1200 + A(1.1)ⁿ, A = −200 M1: Pₙ = 1200 − 200(1.1)ⁿ A1.\n"
        "(c) Pₙ < 0 ⇔ 1.1ⁿ > 6 M1 ⇔ n > ln 6/ln 1.1 = 18.8 M1; during the 19th year (P₁₈ ≈ 88, P₁₉ ≈ −23) A1.\n"
        "(d) P₁ = 980, P₂ = 958, P₃ = INT(1053.8) − 120 = 933 B1; original model gives 980, 958, 933.8: almost the same "
        "B1.\n"
        "(e) P₀ = 1200: constant (equilibrium). P₀ < 1200: decreases, faster and faster, and the fish die out. "
        "P₀ > 1200: increases without bound (unrealistic). The equilibrium is unstable B1 B1.",
        "(a) φ² = (6 + 2√5)/4 = (3 + √5)/2 = φ + 1 B1.\n"
        "(b) n = 1: F₁φ + F₀ = φ ✓ B1. Assume φᵏ = Fₖφ + Fₖ₋₁ M1. φᵏ⁺¹ = Fₖφ² + Fₖ₋₁φ M1 = Fₖ(φ + 1) + Fₖ₋₁φ "
        "= (Fₖ + Fₖ₋₁)φ + Fₖ A1 = Fₖ₊₁φ + Fₖ. Conclusion A1.\n"
        "(c) Subtract: φⁿ − ψⁿ = Fₙ(φ − ψ) M1; φ − ψ = √5 B1; so Fₙ = (φⁿ − ψⁿ)/√5 A1.\n"
        "(d) Fₙ₊₁/Fₙ = (φ − ψ(ψ/φ)ⁿ)/(1 − (ψ/φ)ⁿ) M1; |ψ/φ| < 1 so the ratio → φ A1.",
        "(a) m² − 2m + 4 = 0 ⇒ m = 1 ± i√3 M1 = 2e<sup>±iπ/3</sup> A1; uₙ = 2ⁿ(A cos(nπ/3) + B sin(nπ/3)) M1; u₀ = 1 ⇒ A = 1; "
        "u₁ = 2(½ + (√3/2)B) = 1 ⇒ B = 0 M1; uₙ = 2ⁿ cos(nπ/3) A1.\n"
        "(b) uₙ₊₆ = 2ⁿ⁺⁶ cos(nπ/3 + 2π) M1 = 64 × 2ⁿ cos(nπ/3) = 64uₙ A1.\n"
        "(c) u₃₀ = 2³⁰ cos 10π = 2³⁰ = 1 073 741 824 B1.\n"
        "(d) cos(nπ/3) cycles through 1, ½, −½, −1, −½, ½ (never 0), so the terms change sign in a pattern of period 6 "
        "while |uₙ| grows like 2ⁿ B1: oscillating and divergent B1.",
    ],
}
