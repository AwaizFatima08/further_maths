UNIT = {
    "number": "C1",
    "title": "Further trigonometry and the t-substitution",
    "tag": "Option · Edexcel Further Pure 1 (A level 9FM0 FP1 1.1, 1.2, 1.3, 2.5; AS 8FM0 FP1 1.1, 1.2, 1.3) · "
           "useful for CAIE 9231 P2 integration (the t-results are printed in MF19)",
    "notes": [
        ("h2", "1.1 sec, cosec and cot"),
        ("p", "Edexcel FP1 assumes knowledge of the three reciprocal trigonometric functions from A level Mathematics:"),
        ("box", "Reciprocal trigonometric functions", [
            "sec x = 1/cos x  (cos x ≠ 0);   cosec x = 1/sin x  (sin x ≠ 0);   cot x = 1/tan x = cos x/sin x  (sin x ≠ 0)",
            "1 + tan²x ≡ sec²x;   1 + cot²x ≡ cosec²x   (divide sin²x + cos²x ≡ 1 by cos²x or by sin²x)",
        ]),
        ("table", ["Function", "Domain", "Range", "Period and asymptotes"], [
            ["sec x", "x ≠ π/2 + kπ", "y ≤ −1 or y ≥ 1", "period 2π; asymptotes where cos x = 0"],
            ["cosec x", "x ≠ kπ", "y ≤ −1 or y ≥ 1", "period 2π; asymptotes where sin x = 0"],
            ["cot x", "x ≠ kπ", "all real y", "period π; asymptotes where sin x = 0; cot x = 0 where cos x = 0"],
        ]),
        ("figure", "pc01_reciprocal.png", "y = sec x, y = cosec x and y = cot x for −2π ≤ x ≤ 2π. The dotted curves are y = cos x and y = sin x; "
                                          "dashed lines are the vertical asymptotes.", 105),
        ("h2", "1.2 The t-formulae"),
        ("p", "Every trigonometric function of θ can be written as a <b>rational</b> function of the single quantity t = tan(θ/2). "
              "This turns trigonometric identities and equations into algebra, and integrals of rational functions of sin x and "
              "cos x into integrals of rational functions of t."),
        ("p", "<b>Derivation.</b> Write θ = 2 × (θ/2) and use the double-angle formulae with cos²(θ/2) = 1/sec²(θ/2) = 1/(1 + t²):"),
        ("bullets", [
            "sin θ = 2 sin(θ/2) cos(θ/2) = 2 tan(θ/2) cos²(θ/2) = 2t/(1 + t²).",
            "cos θ = cos²(θ/2) − sin²(θ/2) = cos²(θ/2)(1 − tan²(θ/2)) = (1 − t²)/(1 + t²).",
            "tan θ = 2 tan(θ/2)/(1 − tan²(θ/2)) = 2t/(1 − t²), which is also sin θ/cos θ.",
        ]),
        ("box", "The t-formulae, t = tan(θ/2) (learn these for Edexcel: they are not in the booklet; Cambridge MF19 prints sin and cos)", [
            "sin θ = 2t/(1 + t²);   cos θ = (1 − t²)/(1 + t²);   tan θ = 2t/(1 − t²)",
            "So cosec θ = (1 + t²)/(2t), sec θ = (1 + t²)/(1 − t²), cot θ = (1 − t²)/(2t).",
            "Valid whenever t is defined, i.e. θ ≠ π + 2kπ (and t ≠ ±1 for tan θ, t ≠ 0 for cosec θ and cot θ).",
        ]),
        ("figure", "pc01_triangle.png", "The right-angled triangle with sides 1 − t², 2t and 1 + t² (check: (1 − t²)² + (2t)² = (1 + t²)²) "
                                         "shows all three formulae at once.", 60),
        ("h2", "1.3 Proving identities"),
        ("p", "Replace every function of θ by its t-form, simplify the algebraic fraction, and recognise the result. Multiplying "
              "numerator and denominator by (1 + t²) clears the inner fractions in one step. Work from one side to the other, as in "
              "any proof. Useful results that come out this way include (1 − cos θ)/sin θ ≡ tan(θ/2), "
              "cosec θ + cot θ ≡ cot(θ/2) and sec θ + tan θ ≡ (1 + t)/(1 − t) ≡ tan(π/4 + θ/2)."),
        ("h2", "1.4 Solving a cos x + b sin x = c"),
        ("p", "At A level you solved this by writing a cos x + b sin x = R cos(x − α). The t-substitution gives an alternative that "
              "leads straight to a quadratic. Substitute and multiply by (1 + t²):"),
        ("p", "a(1 − t²) + 2bt = c(1 + t²), which rearranges to (a + c)t² − 2bt + (c − a) = 0."),
        ("bullets", [
            "Solve the quadratic for t, then x/2 = arctan t + kπ, so x = 2 arctan t + 2kπ. Choose k to land in the required interval.",
            "Each value of t gives exactly one x in any interval of length 2π, such as 0 ≤ x < 2π.",
            "The quadratic has real roots exactly when b² − (c + a)(c − a) ≥ 0, i.e. a² + b² ≥ c², the same condition as |c| ≤ R.",
            "<b>The lost root.</b> t = tan(x/2) does not exist at x = π (or 180°). So always test x = π in the original equation. It "
            "is a solution precisely when −a = c, i.e. a + c = 0, which is exactly when the t² term vanishes and the quadratic "
            "becomes linear. If the question's interval contains π, check it.",
        ]),
        ("figure", "pc01_lost_root.png", "2 sin x − cos x = 1 has two roots in [0, 2π). The t-method finds only x ≈ 0.927; "
                                          "the root x = π is lost because tan(π/2) is undefined.", 95),
        ("h2", "1.5 The Weierstrass substitution t = tan(x/2) in integration (Edexcel A level FP1 2.5)"),
        ("p", "For an integral of a rational function of sin x and cos x, substitute t = tan(x/2). Then x = 2 arctan t, so "
              "dx/dt = 2/(1 + t²). The integrand becomes a rational function of t, which you can integrate with partial fractions, "
              "arctan or logarithms. Change the limits as well: x = 0 → t = 0, x = π/3 → t = 1/√3, x = π/2 → t = 1, x = 2π/3 → t = √3. "
              "The substitution only works on intervals that do not contain x = π (or any odd multiple of π)."),
        ("box", "Weierstrass substitution", [
            "t = tan(x/2):   sin x = 2t/(1 + t²),   cos x = (1 − t²)/(1 + t²),   dx = 2 dt/(1 + t²).",
            "Example: ∫ sec x dx = ∫ (1 + t²)/(1 − t²) × 2/(1 + t²) dt = ∫ 2/(1 − t²) dt = ln|(1 + t)/(1 − t)| + C = ln|sec x + tan x| + C.",
            "Example: ∫ cosec x dx = ∫ (1 + t²)/(2t) × 2/(1 + t²) dt = ∫ 1/t dt = ln|tan(x/2)| + C.",
        ]),
        ("p", "When the integrand involves only even powers such as sin²x and cos²x, or tan x, the substitution t = tan x (with "
              "dx = dt/(1 + t²), sin²x = t²/(1 + t²), cos²x = 1/(1 + t²)) is usually simpler. Cambridge 9231 questions may need either "
              "substitution as a technique, with the t-results taken from MF19."),
        ("warn", "Common mistakes", [
            "Losing the root x = π when solving with t = tan(x/2). Always check it in the original equation.",
            "Forgetting to double: x/2 = arctan t gives x = 2 arctan t, and the second solution comes from x/2 + π, not x + π.",
            "Writing dx = 2 dt or dx = dt/(1 + t²): the correct factor is dx = 2 dt/(1 + t²).",
            "Not changing the limits, or using t-limits that pass through x = π.",
            "Misremembering the cos formula as (1 + t²)/(1 − t²) (that is sec θ). Check with θ = 0: cos 0 = 1 needs (1 − 0)/(1 + 0).",
            "In identity proofs, cancelling a factor such as (1 + t) without noting it is non-zero.",
        ]),
    ],
    "examples": [
        {
            "title": "Deriving the t-formulae",
            "question": "Given t = tan(θ/2), show that sin θ = 2t/(1 + t²) and cos θ = (1 − t²)/(1 + t²), and deduce tan θ.",
            "steps": [
                "sin θ = 2 sin(θ/2) cos(θ/2) = 2 [sin(θ/2)/cos(θ/2)] cos²(θ/2) = 2t cos²(θ/2).",
                "cos²(θ/2) = 1/sec²(θ/2) = 1/(1 + tan²(θ/2)) = 1/(1 + t²). So sin θ = 2t/(1 + t²).",
                "cos θ = cos²(θ/2) − sin²(θ/2) = cos²(θ/2)[1 − tan²(θ/2)] = (1 − t²)/(1 + t²).",
                "tan θ = sin θ/cos θ = [2t/(1 + t²)] × [(1 + t²)/(1 − t²)] = 2t/(1 − t²).",
            ],
        },
        {
            "title": "Proving an identity with the t-formulae",
            "question": "Prove that (1 + sin θ − cos θ)/(1 + sin θ + cos θ) ≡ tan(θ/2).",
            "steps": [
                "Let t = tan(θ/2). Multiply numerator and denominator of the left-hand side by (1 + t²).",
                "Numerator: (1 + t²) + 2t − (1 − t²) = 2t² + 2t = 2t(t + 1).",
                "Denominator: (1 + t²) + 2t + (1 − t²) = 2 + 2t = 2(1 + t).",
                "Left-hand side = 2t(1 + t)/(2(1 + t)) = t = tan(θ/2), as required (where 1 + t ≠ 0 and the expression is defined).",
            ],
        },
        {
            "title": "Solving a cos x + b sin x = c",
            "question": "Solve 3 cos x + 4 sin x = 2 for 0 ≤ x < 2π, giving answers to 3 significant figures.",
            "steps": [
                "First check x = π: 3(−1) + 0 = −3 ≠ 2, so no root is lost.",
                "Substitute: 3(1 − t²)/(1 + t²) + 8t/(1 + t²) = 2. Multiply by (1 + t²): 3 − 3t² + 8t = 2 + 2t².",
                "5t² − 8t − 1 = 0, so t = (8 ± √84)/10 = (4 ± √21)/5, i.e. t ≈ 1.7165 or t ≈ −0.1165.",
                "t = 1.7165: x/2 = arctan 1.7165 = 1.0433, so x = 2.09.",
                "t = −0.1165: x/2 = −0.1160 + π = 3.0256 (to put x in range), so x = 6.05.",
                "Answers: x = 2.09 or x = 6.05. Check: 3 cos 2.09 + 4 sin 2.09 ≈ −1.48 + 3.48 = 2.",
            ],
        },
        {
            "title": "An equation with a lost root",
            "question": "Solve 2 sin x − cos x = 1 for 0 ≤ x < 2π.",
            "steps": [
                "Substitute: 4t/(1 + t²) − (1 − t²)/(1 + t²) = 1, so 4t − 1 + t² = 1 + t².",
                "The t² terms cancel, leaving 4t = 2, t = ½. (A linear equation is the warning sign: here a + c = −1 + 1 = 0.)",
                "x = 2 arctan ½ = 0.927 (3 s.f.). Here sin x = 4/5 and cos x = 3/5, and 2(4/5) − 3/5 = 1.",
                "Check x = π: 2 sin π − cos π = 0 + 1 = 1. So x = π is also a solution.",
                "Answers: x = 0.927 or x = π.",
            ],
        },
        {
            "title": "A definite integral giving a logarithm",
            "question": "Use the substitution t = tan(x/2) to show that ∫₀<sup>π/2</sup> 1/(1 + sin x + cos x) dx = ln 2.",
            "steps": [
                "dx = 2 dt/(1 + t²). Limits: x = 0 → t = 0; x = π/2 → t = 1.",
                "1 + sin x + cos x = [(1 + t²) + 2t + (1 − t²)]/(1 + t²) = (2 + 2t)/(1 + t²).",
                "Integrand × dx = (1 + t²)/(2(1 + t)) × 2/(1 + t²) dt = 1/(1 + t) dt.",
                "∫₀¹ 1/(1 + t) dt = [ln(1 + t)]₀¹ = ln 2.",
            ],
        },
        {
            "title": "A definite integral giving arctan",
            "question": "Find the exact value of ∫₀<sup>π/2</sup> 1/(2 + cos x) dx.",
            "steps": [
                "With t = tan(x/2): 2 + cos x = [2(1 + t²) + 1 − t²]/(1 + t²) = (3 + t²)/(1 + t²).",
                "The integral becomes ∫₀¹ (1 + t²)/(3 + t²) × 2/(1 + t²) dt = ∫₀¹ 2/(3 + t²) dt.",
                "= (2/√3)[arctan(t/√3)]₀¹ = (2/√3)(π/6) = π/(3√3).",
                "= π√3/9 ≈ 0.605.",
            ],
        },
    ],
    "practice": [
        "Write down the exact values of (a) sec(π/3), (b) cosec(5π/6), (c) cot(3π/4).",
        "Given that tan(θ/2) = 1/3, find the exact values of sin θ, cos θ and tan θ.",
        "Given that tan(θ/2) = 2, find the exact values of sec θ, cosec θ and cot θ.",
        "Use the t-formulae to prove that (1 − cos θ)/sin θ ≡ tan(θ/2).",
        "(a) Prove that sec θ + tan θ ≡ (1 + t)/(1 − t), where t = tan(θ/2). "
        "(b) Hence show that sec θ + tan θ ≡ tan(π/4 + θ/2).",
        "(a) Prove that (1 + cos θ)/(1 − cos θ) ≡ cot²(θ/2). "
        "(b) Show that cosec x + cot x ≡ cot(x/2), and hence solve cosec x + cot x = 3 for 0 < x < 2π.",
        "Solve 5 cos x + 12 sin x = 13 for 0 ≤ x < 2π, giving your answer to 3 significant figures. Explain why there is only one solution.",
        "Solve 2 cos x + sin x = 1 for 0 ≤ x < 2π.",
        "Solve 3 sin x + cos x + 1 = 0 for 0° ≤ x < 360°, giving answers to 1 decimal place.",
        "Use t = tan(x/2) to show that ∫ 1/(1 + cos x) dx = tan(x/2) + C.",
        "Use t = tan(x/2) to find the exact value of ∫₀<sup>π/2</sup> 1/(1 + sin x) dx.",
        "Use t = tan(x/2) to show that ∫₀<sup>π/3</sup> 1/(5 − 4 cos x) dx = 2π/9.",
    ],
    "answers": [
        "(a) 2. (b) 2. (c) −1.",
        "1 + t² = 10/9: sin θ = (2/3)/(10/9) = 3/5, cos θ = (8/9)/(10/9) = 4/5, tan θ = (2/3)/(8/9) = 3/4.",
        "sin θ = 4/5, cos θ = −3/5, tan θ = −4/3. So sec θ = −5/3, cosec θ = 5/4, cot θ = −3/4.",
        "(1 − (1 − t²)/(1 + t²))/(2t/(1 + t²)) = (2t²)/(2t) = t = tan(θ/2).",
        "(a) (1 + t²)/(1 − t²) + 2t/(1 − t²) = (1 + t)²/((1 − t)(1 + t)) = (1 + t)/(1 − t). "
        "(b) tan(π/4 + θ/2) = (1 + tan(θ/2))/(1 − tan(θ/2)) = (1 + t)/(1 − t), using tan(π/4) = 1.",
        "(a) (2/(1 + t²))/(2t²/(1 + t²)) = 1/t² = cot²(θ/2). "
        "(b) cosec x + cot x = (1 + t²)/(2t) + (1 − t²)/(2t) = 2/(2t) = 1/t = cot(x/2). So tan(x/2) = 1/3, x = 2 arctan(1/3) = 0.644 (3 s.f.).",
        "5(1 − t²) + 24t = 13(1 + t²) gives 9t² − 12t + 4 = 0, (3t − 2)² = 0, t = 2/3, x = 2 arctan(2/3) = 1.18. "
        "x = π gives −5 ≠ 13. One solution because 5² + 12² = 13² (R = 13 = c, so the line y = 13 just touches the maximum).",
        "2(1 − t²) + 2t = 1 + t² gives 3t² − 2t − 1 = 0, (3t + 1)(t − 1) = 0. t = 1: x = π/2. t = −1/3: x = 2π − 2 arctan(1/3) = 5.64 (3 s.f.). "
        "x = π gives −2 ≠ 1.",
        "6t + (1 − t²) + (1 + t²) = 0 gives t = −1/3, x = 360° − 2 arctan(1/3) = 323.1°. Check x = 180°: 0 − 1 + 1 = 0, so x = 180° "
        "is also a solution (here a = 1 and c = −1, so a + c = 0 and the t² terms cancel). Answers: 180°, 323.1°.",
        "1 + cos x = 2/(1 + t²), so ∫ (1 + t²)/2 × 2/(1 + t²) dt = ∫ 1 dt = t + C = tan(x/2) + C.",
        "1 + sin x = (1 + t)²/(1 + t²), so ∫₀¹ 2/(1 + t)² dt = [−2/(1 + t)]₀¹ = −1 + 2 = 1.",
        "5 − 4 cos x = (1 + 9t²)/(1 + t²), so ∫₀<sup>1/√3</sup> 2/(1 + 9t²) dt = (2/3)[arctan 3t] from 0 to 1/√3 = (2/3) arctan √3 = (2/3)(π/3) = 2π/9.",
    ],
    "exam": [
        "(a) Given that t = tan(x/2), show that cos x = (1 − t²)/(1 + t²). [3]\n"
        "(b) Show that the equation 4 sin x − 3 cos x = 2 can be written as t² + 8t − 5 = 0. [3]\n"
        "(c) Hence solve 4 sin x − 3 cos x = 2 for 0 ≤ x < 2π, giving answers to 3 significant figures. [4]\n"
        "(d) Explain why x = π need not be checked separately in this case, and show that it is not a solution. [1]",

        "(a) Use the t-formulae to prove that cosec θ − cot θ ≡ tan(θ/2). [3]\n"
        "(b) Hence find the exact value of tan(π/8). [2]\n"
        "(c) Use the substitution t = tan(x/2) to show that ∫ cosec x dx = ln|tan(x/2)| + C. [3]\n"
        "(d) Hence find the exact value of ∫<sub>π/3</sub><sup>π/2</sup> cosec x dx. [2]",

        "(a) Use the substitution t = tan(x/2) to show that ∫₀<sup>π/2</sup> 1/(3 + 5 cos x) dx = ∫₀¹ 1/(4 − t²) dt. [5]\n"
        "(b) Hence show that ∫₀<sup>π/2</sup> 1/(3 + 5 cos x) dx = ¼ ln 3. [4]",

        "(a) Use the substitution t = tan(x/2) to show that ∫₀<sup>π/2</sup> 1/(2 − sin x) dx = ∫₀¹ 1/(t² − t + 1) dt. [4]\n"
        "(b) Hence find the exact value of ∫₀<sup>π/2</sup> 1/(2 − sin x) dx. [4]\n"
        "(c) Solve the equation 2 − sin x = 2 cos x for 0 ≤ x < 2π, giving answers to 3 significant figures where appropriate. [4]",
    ],
    "exam_answers": [
        "(a) cos x = cos²(x/2) − sin²(x/2) M1 = cos²(x/2)(1 − tan²(x/2)) M1, and cos²(x/2) = 1/(1 + t²), giving (1 − t²)/(1 + t²) A1.\n"
        "(b) 8t/(1 + t²) − 3(1 − t²)/(1 + t²) = 2 M1; 8t − 3 + 3t² = 2 + 2t² M1; t² + 8t − 5 = 0 A1.\n"
        "(c) t = −4 ± √21 M1 A1; t = 0.5826: x = 2 arctan t = 1.06 A1; t = −8.583: x/2 = π + arctan t, x = 3.37 A1.\n"
        "(d) The t² coefficient is non-zero (a + c = −3 + 2 ≠ 0), so π cannot be a root; directly 4(0) − 3(−1) = 3 ≠ 2 B1.",

        "(a) (1 + t²)/(2t) − (1 − t²)/(2t) M1 = 2t²/(2t) A1 = t = tan(θ/2) A1.\n"
        "(b) θ = π/4: tan(π/8) = cosec(π/4) − cot(π/4) M1 = √2 − 1 A1.\n"
        "(c) dx = 2 dt/(1 + t²) B1; cosec x dx = (1 + t²)/(2t) × 2/(1 + t²) dt = dt/t M1; ln|t| + C = ln|tan(x/2)| + C A1.\n"
        "(d) ln tan(π/4) − ln tan(π/6) M1 = 0 − ln(1/√3) = ½ ln 3 A1.",

        "(a) dx = 2 dt/(1 + t²), limits 0 and 1 B1 B1; 3 + 5 cos x = (3 + 3t² + 5 − 5t²)/(1 + t²) = (8 − 2t²)/(1 + t²) M1 A1; "
        "integrand 2/(8 − 2t²) = 1/(4 − t²) A1.\n"
        "(b) 1/(4 − t²) = ¼[1/(2 − t) + 1/(2 + t)] M1 A1; ¼[ln((2 + t)/(2 − t))]₀¹ M1 = ¼ ln 3 A1.",

        "(a) dx = 2 dt/(1 + t²), limits 0 and 1 B1; 2 − sin x = (2 + 2t² − 2t)/(1 + t²) M1 A1; "
        "integrand 2/(2t² − 2t + 2) = 1/(t² − t + 1) A1.\n"
        "(b) t² − t + 1 = (t − ½)² + ¾ M1; (2/√3)[arctan((2t − 1)/√3)]₀¹ M1 A1 = (2/√3)(π/6 + π/6) = 2π/(3√3) = 2π√3/9 A1 (≈ 1.21).\n"
        "(c) 2 cos x + sin x = 2 M1; 2(1 − t²) + 2t = 2(1 + t²), so 4t² − 2t = 0 M1, t = 0 or ½ A1; "
        "x = 0 or x = 2 arctan ½ = 0.927 A1 (x = π: −2 ≠ 2).",
    ],
}
