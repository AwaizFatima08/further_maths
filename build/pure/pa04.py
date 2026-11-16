"""Unit A4: Summation of series and the method of differences (Ed CP 4.3-4.4, IAL FP1 7.1 / FP2 2.1, AQA D3-D4,
OCR 4.06a-b, MEI Ps1-Ps2, CAIE 1.3)."""

UNIT = {
    "number": "A4",
    "title": "Summation of series and the method of differences",
    "tag": "AS and A · Edexcel CP 4.3 (AS), CP 4.4 (A) · IAL FP1 7.1 (standard sums), FP2 2.1 (differences) · "
           "AQA D3, D4 (AS; partial fractions A) · OCR A 4.06a–b (A) · OCR MEI Ps1 (AS), Ps2 and convergence (A) · "
           "CAIE 9231 P1 1.3",
    "notes": [
        ("p", "This unit is about adding up many terms quickly and exactly. There are two main tools: the standard "
              "formulae for Σr, Σr² and Σr³, which handle any series whose terms are polynomials in r; and the method of "
              "differences, which handles series whose terms can be written as a difference f(r) − f(r + 1), so that "
              "almost everything cancels. The method of differences also lets you decide whether an infinite series "
              "converges and find its sum."),

        ("h2", "4.1 Sigma notation, sequences and series"),
        ("p", "A <b>sequence</b> is an ordered list of terms u₁, u₂, u₃, …. A <b>series</b> is the sum of the terms of a "
              "sequence. The sum of the first n terms is Sₙ = u₁ + u₂ + … + uₙ = Σ<sub>r=1</sub>ⁿ uᵣ, read “the sum of uᵣ from "
              "r = 1 to r = n”. The letter r is a dummy variable: Σ<sub>r=1</sub>ⁿ r² and Σ<sub>k=1</sub>ⁿ k² mean the same."),
        ("bullets", [
            "Number of terms: Σ<sub>r=a</sub><sup>b</sup> uᵣ has b − a + 1 terms. For example Σ<sub>r=n+1</sub>²ⁿ has n terms.",
            "Linearity: Σ(a uᵣ + b vᵣ) = aΣuᵣ + bΣvᵣ for constants a and b. You may split sums and take constants out.",
            "Constants: Σ<sub>r=1</sub>ⁿ c = cn (n copies of c), not c.",
            "Changing the start: Σ<sub>r=a</sub><sup>b</sup> uᵣ = Σ<sub>r=1</sub><sup>b</sup> uᵣ − Σ<sub>r=1</sub><sup>a−1</sup> uᵣ. Note the a − 1 in the second sum.",
            "You cannot split products: Σ r(r + 1) ≠ Σr × Σ(r + 1). Expand first.",
        ]),

        ("h2", "4.2 The standard results (all boards)"),
        ("box", "Standard sums", [
            "Σ<sub>r=1</sub>ⁿ r = ½n(n + 1)",
            "Σ<sub>r=1</sub>ⁿ r² = ⅙n(n + 1)(2n + 1)",
            "Σ<sub>r=1</sub>ⁿ r³ = ¼n²(n + 1)² = (Σr)²",
            "Σr must be learnt (all boards list it as a formula to know). Σr² and Σr³ are printed in every booklet "
            "(CAIE MF19 included), but OCR A may ask you to prove them.",
        ]),
        ("p", "<b>Why Σr = ½n(n + 1).</b> Write the sum forwards and backwards: S = 1 + 2 + … + n and S = n + (n − 1) + … + 1. "
              "Adding term by term gives n pairs, each summing to n + 1, so 2S = n(n + 1)."),
        ("p", "<b>Proof of Σr² (OCR A: proof may be required).</b> Use the identity (r + 1)³ − r³ = 3r² + 3r + 1 and add it "
              "for r = 1 to n. The left side cancels down to (n + 1)³ − 1 (the method of differences, 4.4). So "
              "(n + 1)³ − 1 = 3Σr² + 3 × ½n(n + 1) + n. Rearranging gives Σr² = ⅙n(n + 1)(2n + 1) (Worked example 3). "
              "The same idea with (r + 1)⁴ − r⁴ proves Σr³. All three results can also be proved by induction (Unit A8)."),

        ("h2", "4.3 Using the standard results"),
        ("p", "To sum a polynomial in r: expand the general term, split the sum, use the standard results, then factorise. "
              "Take out common factors such as n(n + 1) early; it keeps the algebra short. Examiners usually give the "
              "answer in a factorised form, so aim for that."),
        ("table", ["Series", "Sum to n terms"], [
            ["Σ r(r + 1)", "⅓n(n + 1)(n + 2)"],
            ["Σ r(r + 1)(r + 2)", "¼n(n + 1)(n + 2)(n + 3)"],
            ["Σ (2r − 1)", "n²"],
            ["Σ (2r − 1)²", "⅓n(2n − 1)(2n + 1)"],
            ["Σ r²(r + 2) (Edexcel example)", "(1/12)n(n + 1)(3n² + 11n + 4)"],
        ]),
        ("p", "For a sum that does not start at r = 1, subtract: Σ<sub>r=n+1</sub>²ⁿ f(r) = S(2n) − S(n), where S(m) is the sum "
              "from 1 to m. Replace n by 2n carefully in every factor."),

        ("h2", "4.4 The method of differences (Edexcel A level, IAL FP2, AQA, OCR A, MEI, CAIE)"),
        ("p", "Suppose each term can be written as a difference uᵣ = f(r) − f(r + 1). Then"),
        ("p", "Σ<sub>r=1</sub>ⁿ uᵣ = [f(1) − f(2)] + [f(2) − f(3)] + … + [f(n) − f(n + 1)] = f(1) − f(n + 1),"),
        ("p", "because every inner term appears once with + and once with −. The series is said to <b>telescope</b>. In an "
              "exam, write out the first three terms and the last two (in columns, so the cancelling is visible) before "
              "stating the result. A bare answer gains little credit."),
        ("box", "Method of differences", [
            "If uᵣ = f(r) − f(r + 1), then Σ<sub>r=1</sub>ⁿ uᵣ = f(1) − f(n + 1).",
            "If uᵣ = f(r) − f(r + 2), two terms survive at each end: Σ<sub>r=1</sub>ⁿ uᵣ = f(1) + f(2) − f(n + 1) − f(n + 2).",
            "If uᵣ = f(r + 1) − f(r − 1), Σ<sub>r=1</sub>ⁿ uᵣ = f(n + 1) + f(n) − f(1) − f(0).",
            "Always list terms from both ends to see exactly which survive.",
        ]),

        ("h2", "4.5 Partial fractions (Edexcel, IAL FP2, AQA A level, OCR A, MEI A level, CAIE)"),
        ("p", "Many differences appear only after splitting a fraction into partial fractions. The common types are:"),
        ("table", ["General term", "Partial fractions", "Sum to n terms"], [
            ["1/(r(r + 1))", "1/r − 1/(r + 1)", "1 − 1/(n + 1) = n/(n + 1)"],
            ["1/((2r − 1)(2r + 1))", "½[1/(2r − 1) − 1/(2r + 1)]", "n/(2n + 1)"],
            ["1/(r(r + 2))", "½[1/r − 1/(r + 2)]", "¾ − (2n + 3)/(2(n + 1)(n + 2))"],
            ["1/(r(r + 1)(r + 2))", "½[1/(r(r + 1)) − 1/((r + 1)(r + 2))]", "¼ − 1/(2(n + 1)(n + 2))"],
            ["r × r!", "(r + 1)! − r!", "(n + 1)! − 1"],
            ["ln((r + 1)/r)", "ln(r + 1) − ln r", "ln(n + 1)"],
        ]),
        ("p", "Not every difference is a fraction: r × r! = (r + 1)! − r! because (r + 1)! = (r + 1) r! = r × r! + r!. "
              "Logarithms split using ln(a/b) = ln a − ln b."),

        ("h2", "4.6 Convergence and the sum to infinity (CAIE, OCR A, MEI A level, Edexcel A level)"),
        ("p", "An infinite series Σ<sub>r=1</sub><sup>∞</sup> uᵣ <b>converges</b> if its partial sums Sₙ approach a finite limit S as n → ∞. "
              "This limit is the <b>sum to infinity</b>. If Sₙ grows without bound, or does not settle to one value, the "
              "series <b>diverges</b>. Note the difference: a sequence converges if its terms approach a limit; a series "
              "converges if its partial sums do. The terms 1/r of a sequence tend to 0, but the series Σ1/r diverges."),
        ("bullets", [
            "From a method-of-differences formula, let n → ∞: Σ 1/(r(r + 1)) has Sₙ = 1 − 1/(n + 1) → 1, so the sum to "
            "infinity is 1.",
            "Σ ln((r + 1)/r) has Sₙ = ln(n + 1) → ∞, so this series diverges, even though its terms tend to 0.",
            "If uᵣ does not tend to 0, the series certainly diverges (for example Σ r/(r + 1)).",
            "uᵣ → 0 is necessary for convergence but not sufficient. Always argue from Sₙ.",
            "If you are given Sₙ, you can recover the terms: uₙ = Sₙ − Sₙ₋₁ for n ≥ 2, and u₁ = S₁.",
        ]),
        ("warn", "Common mistakes", [
            "Σ<sub>r=1</sub>ⁿ 3 = 3n, not 3. Constant terms are summed n times.",
            "For Σ<sub>r=n+1</sub>²ⁿ, subtract the sum to n terms, not n + 1 terms; and for Σ<sub>r=a</sub><sup>b</sup> subtract the sum to "
            "a − 1. CAIE examiners report this off-by-one error every year, and miscounting the terms from n + 1 to 2n.",
            "Not showing the cancellation. Write enough terms at the start and the end to justify which terms survive, "
            "especially when two terms remain at each end.",
            "Losing a factor: if you write 1/(r(r + 2)) = ½[1/r − 1/(r + 2)], keep the ½ to the end (a common CAIE error).",
            "Claiming convergence because the terms tend to zero. Find the limit of Sₙ.",
        ]),
    ],
    "examples": [
        {
            "title": "Summing a polynomial series",
            "question": "Show that Σ<sub>r=1</sub>ⁿ r²(r + 2) = (1/12)n(n + 1)(3n² + 11n + 4).",
            "steps": [
                "Expand and split: Σ r²(r + 2) = Σr³ + 2Σr².",
                "= ¼n²(n + 1)² + 2 × ⅙n(n + 1)(2n + 1) = ¼n²(n + 1)² + ⅓n(n + 1)(2n + 1).",
                "Take out (1/12)n(n + 1): = (1/12)n(n + 1)[3n(n + 1) + 4(2n + 1)].",
                "= (1/12)n(n + 1)[3n² + 3n + 8n + 4] = (1/12)n(n + 1)(3n² + 11n + 4), as required.",
                "Check with n = 1: the series is 1² × 3 = 3, and (1/12)(1)(2)(18) = 3. ✓",
            ],
        },
        {
            "title": "A sum that does not start at r = 1",
            "question": "(a) Show that Σ<sub>r=n+1</sub>²ⁿ r² = ⅙n(2n + 1)(7n + 1). (b) Hence evaluate 11² + 12² + … + 20².",
            "steps": [
                "(a) Σ<sub>r=n+1</sub>²ⁿ r² = Σ<sub>r=1</sub>²ⁿ r² − Σ<sub>r=1</sub>ⁿ r².",
                "Replace n by 2n in the formula: Σ<sub>r=1</sub>²ⁿ r² = ⅙(2n)(2n + 1)(4n + 1).",
                "So the sum is ⅙n(2n + 1)[2(4n + 1) − (n + 1)] = ⅙n(2n + 1)(7n + 1).",
                "(b) 11² + … + 20² is the case n = 10: ⅙ × 10 × 21 × 71 = 2485.",
                "Check: Σ<sub>r=1</sub>²⁰ r² − Σ<sub>r=1</sub>¹⁰ r² = 2870 − 385 = 2485. ✓",
            ],
        },
        {
            "title": "Proving Σr² by the method of differences (OCR A)",
            "question": "By considering Σ<sub>r=1</sub>ⁿ [(r + 1)³ − r³], and using Σr = ½n(n + 1), prove that "
                        "Σ<sub>r=1</sub>ⁿ r² = ⅙n(n + 1)(2n + 1).",
            "steps": [
                "Left side: the terms are (2³ − 1³) + (3³ − 2³) + … + ((n + 1)³ − n³). All terms cancel except "
                "(n + 1)³ − 1³.",
                "Right side: (r + 1)³ − r³ = 3r² + 3r + 1, so the sum is 3Σr² + 3Σr + Σ1 = 3Σr² + (3/2)n(n + 1) + n.",
                "So 3Σr² = (n + 1)³ − 1 − (3/2)n(n + 1) − n = n³ + 3n² + 3n − (3/2)n² − (3/2)n − n = n³ + (3/2)n² + ½n.",
                "Hence Σr² = ⅓n³ + ½n² + ⅙n = ⅙n(2n² + 3n + 1) = ⅙n(n + 1)(2n + 1). ∎",
            ],
        },
        {
            "title": "Method of differences with partial fractions",
            "question": "(a) Express 1/((2r − 1)(2r + 1)) in partial fractions. (b) Hence find Σ<sub>r=1</sub>ⁿ "
                        "1/((2r − 1)(2r + 1)), simplifying your answer. (c) Deduce the sum to infinity.",
            "steps": [
                "(a) 1/((2r − 1)(2r + 1)) = A/(2r − 1) + B/(2r + 1), so 1 = A(2r + 1) + B(2r − 1). r = ½: A = ½. "
                "r = −½: B = −½. So the term is ½[1/(2r − 1) − 1/(2r + 1)].",
                "(b) Write out the terms (r = 1, 2, 3, …, n − 1, n):",
                "½[1/1 − 1/3]  +  ½[1/3 − 1/5]  +  ½[1/5 − 1/7]  +  …  +  ½[1/(2n − 3) − 1/(2n − 1)]  +  "
                "½[1/(2n − 1) − 1/(2n + 1)].",
                "Everything cancels except the first and last fractions: sum = ½[1 − 1/(2n + 1)] = ½ × 2n/(2n + 1) "
                "= <b>n/(2n + 1)</b>.",
                "(c) n/(2n + 1) = 1/(2 + 1/n) → ½ as n → ∞. The series converges and its sum to infinity is ½.",
            ],
        },
        {
            "title": "Two terms surviving at each end",
            "question": "Find Σ<sub>r=1</sub>ⁿ 1/(r(r + 2)) and state the sum to infinity.",
            "steps": [
                "1/(r(r + 2)) = ½[1/r − 1/(r + 2)].",
                "List the brackets: r = 1: 1/1 − 1/3; r = 2: 1/2 − 1/4; r = 3: 1/3 − 1/5; r = 4: 1/4 − 1/6; …; "
                "r = n − 1: 1/(n − 1) − 1/(n + 1); r = n: 1/n − 1/(n + 2).",
                "Each negative term cancels the positive term two rows below it. Survivors: +1 and +1/2 at the start; "
                "−1/(n + 1) and −1/(n + 2) at the end.",
                "Σ = ½[1 + ½ − 1/(n + 1) − 1/(n + 2)] = ¾ − ½[(2n + 3)/((n + 1)(n + 2))] = ¾ − (2n + 3)/(2(n + 1)(n + 2)).",
                "As n → ∞ the fraction tends to 0, so the sum to infinity is ¾.",
            ],
        },
        {
            "title": "A three-factor denominator (exam standard)",
            "question": "(a) Show that 1/(r(r + 1)) − 1/((r + 1)(r + 2)) = 2/(r(r + 1)(r + 2)). (b) Hence show that "
                        "Σ<sub>r=1</sub>ⁿ 1/(r(r + 1)(r + 2)) = n(n + 3)/(4(n + 1)(n + 2)). (c) Find the sum to infinity, and the "
                        "least n for which Sₙ is within 0.001 of it.",
            "steps": [
                "(a) Common denominator r(r + 1)(r + 2): [(r + 2) − r]/(r(r + 1)(r + 2)) = 2/(r(r + 1)(r + 2)). ✓",
                "(b) So uᵣ = ½[f(r) − f(r + 1)] with f(r) = 1/(r(r + 1)). Terms: ½[1/(1×2) − 1/(2×3)] + ½[1/(2×3) − 1/(3×4)] "
                "+ … + ½[1/(n(n + 1)) − 1/((n + 1)(n + 2))].",
                "Sum = ½[½ − 1/((n + 1)(n + 2))] = [(n + 1)(n + 2) − 2]/(4(n + 1)(n + 2)) = (n² + 3n)/(4(n + 1)(n + 2)) "
                "= n(n + 3)/(4(n + 1)(n + 2)). ✓",
                "(c) Sₙ = ¼ − 1/(2(n + 1)(n + 2)) → ¼. We need 1/(2(n + 1)(n + 2)) < 0.001, i.e. (n + 1)(n + 2) > 500.",
                "n = 20: 21 × 22 = 462 (too small); n = 21: 22 × 23 = 506 > 500. So the least n is 21.",
            ],
        },
    ],
    "practice": [
        "Evaluate Σ<sub>r=1</sub>²⁰ (3r − 1).",
        "Show that Σ<sub>r=1</sub>ⁿ (6r² + 2r) = 2n(n + 1)².",
        "Show that Σ<sub>r=1</sub>ⁿ r(r + 1)(r + 2) = ¼n(n + 1)(n + 2)(n + 3).",
        "Show that Σ<sub>r=1</sub>ⁿ (2r − 1)² = ⅓n(2n − 1)(2n + 1).",
        "Find Σ<sub>r=1</sub>ⁿ r²(r − 1), giving your answer as a product of linear factors.",
        "Show that Σ<sub>r=n+1</sub>²ⁿ r³ = ¼n²(3n + 1)(5n + 3).",
        "Evaluate Σ<sub>r=10</sub>³⁰ r².",
        "Use the method of differences to show that Σ<sub>r=1</sub>ⁿ 1/((3r − 1)(3r + 2)) = n/(2(3n + 2)).",
        "(a) Show that Σ<sub>r=1</sub>ⁿ ln(1 + 1/r) = ln(n + 1). (b) What does this tell you about the series "
        "Σ<sub>r=1</sub><sup>∞</sup> ln(1 + 1/r)?",
        "Find Σ<sub>r=2</sub>ⁿ 1/(r² − 1) and deduce the sum to infinity of Σ<sub>r=2</sub><sup>∞</sup> 1/(r² − 1).",
        "Show that r × r! = (r + 1)! − r!, and hence find Σ<sub>r=1</sub>ⁿ r × r!.",
        "The sum of the first n terms of a series is Sₙ = n/(2n + 1). Find the nth term uₙ, simplifying your answer, and "
        "state the sum to infinity.",
    ],
    "answers": [
        "3 × 210 − 20 = 610.",
        "6 × ⅙n(n + 1)(2n + 1) + 2 × ½n(n + 1) = n(n + 1)(2n + 1 + 1) = 2n(n + 1)².",
        "Σ(r³ + 3r² + 2r) = ¼n²(n + 1)² + ½n(n + 1)(2n + 1) + n(n + 1) = ¼n(n + 1)[n(n + 1) + 2(2n + 1) + 4] "
        "= ¼n(n + 1)(n² + 5n + 6) = ¼n(n + 1)(n + 2)(n + 3).",
        "Σ(4r² − 4r + 1) = ⅔n(n + 1)(2n + 1) − 2n(n + 1) + n = ⅓n[2(n + 1)(2n + 1) − 6(n + 1) + 3] = ⅓n(4n² − 1) "
        "= ⅓n(2n − 1)(2n + 1).",
        "Σr³ − Σr² = (1/12)n(n + 1)[3n(n + 1) − 2(2n + 1)] = (1/12)n(n + 1)(3n² − n − 2) = (1/12)(n − 1)n(n + 1)(3n + 2).",
        "S(2n) − S(n) = n²(2n + 1)² − ¼n²(n + 1)² = ¼n²[(4n + 2)² − (n + 1)²] = ¼n²(3n + 1)(5n + 3).",
        "S(30) − S(9) = 9455 − 285 = 9170.",
        "1/((3r − 1)(3r + 2)) = ⅓[1/(3r − 1) − 1/(3r + 2)]; terms telescope to ⅓[1/2 − 1/(3n + 2)] = n/(2(3n + 2)).",
        "(a) ln(1 + 1/r) = ln(r + 1) − ln r; sum = ln(n + 1) − ln 1 = ln(n + 1). (b) ln(n + 1) → ∞, so the series "
        "diverges (even though its terms tend to 0).",
        "1/(r² − 1) = ½[1/(r − 1) − 1/(r + 1)]; survivors 1 + ½ − 1/n − 1/(n + 1), so Σ = ¾ − (2n + 1)/(2n(n + 1)). "
        "Sum to infinity ¾.",
        "(r + 1)! − r! = (r + 1)r! − r! = r × r!. Telescopes to (n + 1)! − 1! = (n + 1)! − 1.",
        "uₙ = Sₙ − Sₙ₋₁ = n/(2n + 1) − (n − 1)/(2n − 1) = 1/((2n − 1)(2n + 1)) (also true for n = 1: u₁ = S₁ = ⅓). "
        "Sₙ → ½, so the sum to infinity is ½.",
    ],
    "exam": [
        "(a) Show that Σ<sub>r=1</sub>ⁿ r(r + 3) = ⅓n(n + 1)(n + 5). [4]\n"
        "(b) Hence find the value of Σ<sub>r=11</sub>²⁰ r(r + 3). [3]\n"
        "(c) Given that Σ<sub>r=1</sub>ⁿ r(r + 3) = 884, find the value of n. [2]",
        "(a) Show that (2r + 1)/(r²(r + 1)²) = 1/r² − 1/(r + 1)². [2]\n"
        "(b) Hence find Σ<sub>r=1</sub>ⁿ (2r + 1)/(r²(r + 1)²) in terms of n. [3]\n"
        "(c) Deduce the sum to infinity of the series. [1]\n"
        "(d) Show that Σ<sub>r=n+1</sub>²ⁿ (2r + 1)/(r²(r + 1)²) = n(3n + 2)/((n + 1)²(2n + 1)²). [3]",
        "(OCR A) (a) Show that (r + 1)⁴ − r⁴ = 4r³ + 6r² + 4r + 1. [1]\n"
        "(b) Using the method of differences and the standard results for Σr and Σr², prove that "
        "Σ<sub>r=1</sub>ⁿ r³ = ¼n²(n + 1)². [5]\n"
        "(c) Hence show that Σ<sub>r=1</sub>ⁿ (2r − 1)³ = n²(2n² − 1). [4]",
        "(CAIE) Let uᵣ = ln( r(r + 2)/(r + 1)² ).\n"
        "(a) Show that uᵣ = f(r) − f(r + 1), where f(r) = ln( r/(r + 1) ). [2]\n"
        "(b) Hence find Σ<sub>r=1</sub>ⁿ uᵣ in terms of n. [3]\n"
        "(c) Explain why the series Σ<sub>r=1</sub><sup>∞</sup> uᵣ is convergent and state its sum to infinity. [2]\n"
        "(d) Find the least value of n for which the sum to n terms differs from the sum to infinity by less than 0.01. [3]",
    ],
    "exam_answers": [
        "(a) Σr² + 3Σr M1 = ⅙n(n + 1)(2n + 1) + (3/2)n(n + 1) A1 = ⅙n(n + 1)(2n + 1 + 9) M1 = ⅓n(n + 1)(n + 5) A1.\n"
        "(b) S(20) − S(10) M1 = (20 × 21 × 25)/3 − (10 × 11 × 15)/3 = 3500 − 550 A1 = 2950 A1.\n"
        "(c) n(n + 1)(n + 5) = 2652 M1; n = 12 (12 × 13 × 17 = 2652; the left side is increasing, so this is the only "
        "solution) A1.",
        "(a) [(r + 1)² − r²]/(r²(r + 1)²) M1 = (2r + 1)/(r²(r + 1)²) A1.\n"
        "(b) (1 − 1/4) + (1/4 − 1/9) + … + (1/n² − 1/(n + 1)²) M1 (terms shown cancelling) A1; sum = 1 − 1/(n + 1)² A1.\n"
        "(c) 1/(n + 1)² → 0, so the sum to infinity is 1 B1.\n"
        "(d) S(2n) − S(n) = 1/(n + 1)² − 1/(2n + 1)² M1 = [(2n + 1)² − (n + 1)²]/((n + 1)²(2n + 1)²) M1 "
        "= n(3n + 2)/((n + 1)²(2n + 1)²) A1.",
        "(a) (r + 1)⁴ = r⁴ + 4r³ + 6r² + 4r + 1 B1.\n"
        "(b) Σ<sub>r=1</sub>ⁿ[(r + 1)⁴ − r⁴] = (n + 1)⁴ − 1 by cancellation M1 A1. So 4Σr³ = (n + 1)⁴ − 1 − n(n + 1)(2n + 1) "
        "− 2n(n + 1) − n M1. (n + 1)⁴ − (n + 1) = (n + 1)(n³ + 3n² + 3n) = n(n + 1)(n² + 3n + 3), so 4Σr³ "
        "= n(n + 1)[n² + 3n + 3 − 2n − 1 − 2] M1 = n(n + 1)(n² + n) = n²(n + 1)², giving Σr³ = ¼n²(n + 1)² A1.\n"
        "(c) Σ<sub>r=1</sub>ⁿ(2r − 1)³ = Σ<sub>k=1</sub>²ⁿ k³ − Σ<sub>r=1</sub>ⁿ (2r)³ M1 = ¼(2n)²(2n + 1)² − 8 × ¼n²(n + 1)² A1 "
        "= n²[(2n + 1)² − 2(n + 1)²] M1 = n²(2n² − 1) A1.",
        "(a) f(r) − f(r + 1) = ln(r/(r + 1)) − ln((r + 1)/(r + 2)) M1 = ln( r(r + 2)/(r + 1)² ) A1.\n"
        "(b) Telescoping: Σ = f(1) − f(n + 1) M1 = ln(1/2) − ln((n + 1)/(n + 2)) A1 = ln( (n + 2)/(2(n + 1)) ) A1.\n"
        "(c) (n + 2)/(n + 1) → 1, so Sₙ → ln(1/2): convergent, sum to infinity −ln 2 B1 B1.\n"
        "(d) Sₙ − (−ln 2) = ln((n + 2)/(n + 1)) = ln(1 + 1/(n + 1)) < 0.01 M1; 1/(n + 1) < e<sup>0.01</sup> − 1 = 0.010050…, "
        "so n + 1 > 99.5 M1; least n = 99 A1 (check: n = 98 gives 0.01005, n = 99 gives 0.00995).",
    ],
}
