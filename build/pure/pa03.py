"""Unit A3: Roots of polynomial equations (Ed CP 4.1-4.2, IAL FP1 2.1-2.3, AQA D1-D2, OCR 4.05a-b, MEI Pa1-Pa2,
CAIE 1.1)."""

UNIT = {
    "number": "A3",
    "title": "Roots of polynomial equations",
    "tag": "AS · Edexcel CP 4.1–4.2 · IAL FP1 2.1–2.3 (quadratics only) · AQA D1–D2 · OCR A 4.05a–b · "
           "OCR MEI Pa1–Pa2 · CAIE 9231 P1 1.1",
    "notes": [
        ("p", "You can often answer questions about the roots of a polynomial equation without finding the roots. The "
              "coefficients of the polynomial hold the sum of the roots, the sum of their products in pairs, and so on. "
              "From these few numbers you can find many other expressions in the roots, test whether the roots can all be "
              "real, find unknown coefficients, and build new equations whose roots are related to the old ones. Roots may "
              "be real or complex: the results hold either way (see Unit A1 for complex roots and conjugate pairs)."),

        ("h2", "3.1 Quadratic equations (all boards; the whole of IAL FP1 section 2)"),
        ("p", "Suppose ax² + bx + c = 0 (a ≠ 0) has roots α and β. Then ax² + bx + c ≡ a(x − α)(x − β) for every x, "
              "because both sides are quadratics with the same leading coefficient and the same zeros. Expanding gives "
              "a(x − α)(x − β) = ax² − a(α + β)x + aαβ. Comparing coefficients of x and the constant term:"),
        ("box", "Roots and coefficients of a quadratic", [
            "If ax² + bx + c = 0 has roots α and β, then  α + β = −b/a  and  αβ = c/a.",
            "Conversely, a quadratic with roots α and β is x² − (α + β)x + αβ = 0: x² − (sum)x + (product) = 0.",
            "Multiply through by a suitable number to give integer coefficients when a question asks for them.",
        ]),
        ("p", "A <b>symmetric function</b> of the roots is an expression that is unchanged when the roots are swapped, such "
              "as α² + β² or 1/α + 1/β. Every symmetric function can be written in terms of α + β and αβ, so it can be "
              "found from the coefficients alone. The identities below are used constantly; learn how to derive them by "
              "expanding a bracket and subtracting the unwanted terms."),
        ("table", ["Expression", "In terms of α + β and αβ"], [
            ["α² + β²", "(α + β)² − 2αβ"],
            ["α³ + β³", "(α + β)³ − 3αβ(α + β)"],
            ["(α − β)²", "(α + β)² − 4αβ"],
            ["1/α + 1/β", "(α + β)/(αβ)"],
            ["1/α² + 1/β²", "(α² + β²)/(αβ)² = ((α + β)² − 2αβ)/(αβ)²"],
            ["α/β + β/α", "(α² + β²)/(αβ)"],
            ["α⁴ + β⁴", "(α² + β²)² − 2(αβ)²"],
            ["(α + k)(β + k)", "αβ + k(α + β) + k²"],
        ]),

        ("h2", "3.2 Cubic and quartic equations (all boards except IAL)"),
        ("p", "The same argument works for any degree. If az³ + bz² + cz + d = 0 has roots α, β, γ, then "
              "az³ + bz² + cz + d ≡ a(z − α)(z − β)(z − γ) = a[z³ − (α + β + γ)z² + (αβ + βγ + γα)z − αβγ]. "
              "Comparing coefficients gives the cubic results. For a quartic, expand a(z − α)(z − β)(z − γ)(z − δ) in the "
              "same way. The signs alternate, starting with minus."),
        ("p", "The notation Σα means the sum of the roots, Σαβ the sum of the products of the roots taken two at a time "
              "(3 terms for a cubic, 6 for a quartic), and Σαβγ the sum of products three at a time (4 terms for a "
              "quartic). Σα² means α² + β² + γ² (+ δ²)."),
        ("box", "Roots and coefficients of cubics and quartics", [
            "Cubic az³ + bz² + cz + d = 0, roots α, β, γ:  Σα = −b/a,  Σαβ = c/a,  αβγ = −d/a.",
            "Quartic az⁴ + bz³ + cz² + dz + e = 0, roots α, β, γ, δ:  Σα = −b/a,  Σαβ = c/a,  Σαβγ = −d/a,  αβγδ = e/a.",
            "Pattern: the kth coefficient divided by a, with sign (−1)ᵏ, gives the sum of products of the roots k at a time.",
            "These relations are not printed in most formula booklets (AQA, Edexcel, OCR and MEI expect quadratic and "
            "cubic ones from memory; CAIE prints none). Learn them all, including the quartic.",
        ]),

        ("h2", "3.3 Symmetric functions of three or four roots"),
        ("p", "The same tricks extend. Write the expression you want in terms of Σα, Σαβ, Σαβγ and the product, then "
              "substitute. The key identities are:"),
        ("bullets", [
            "Sum of squares: Σα² = (Σα)² − 2Σαβ. This holds for cubics and quartics. If Σα² < 0 for an equation with "
            "real coefficients, the roots cannot all be real (a sum of squares of real numbers is never negative).",
            "Sum of reciprocals: for a cubic, Σ1/α = (βγ + γα + αβ)/(αβγ) = Σαβ/αβγ; for a quartic, Σ1/α = Σαβγ/αβγδ.",
            "Sum of reciprocal squares: Σ1/α² = (Σ1/α)² − 2Σ1/(αβ), where for a cubic Σ1/(αβ) = Σα/αβγ and for a quartic "
            "Σ1/(αβ) = Σαβ/αβγδ.",
            "Sum of cubes (cubic): Σα³ = (Σα)³ − 3ΣαΣαβ + 3αβγ.",
            "Products of shifted roots: since az³ + bz² + cz + d = a(z − α)(z − β)(z − γ), putting z = k gives "
            "(k − α)(k − β)(k − γ) = f(k)/a. So (k + α)(k + β)(k + γ) = −f(−k)/a for a cubic. For a quartic, "
            "(k − α)(k − β)(k − γ)(k − δ) = f(k)/a.",
        ]),
        ("p", "<b>Power sums.</b> Write Sₙ = αⁿ + βⁿ + γⁿ (+ δⁿ), so S₀ is the number of roots. Each root satisfies the "
              "equation, so for the cubic aα³ + bα² + cα + d = 0. Multiplying by αⁿ and adding the three versions gives the "
              "recurrence below. It is the quickest way to find Σα³, Σα⁴ and higher power sums, and CAIE examiners expect "
              "it."),
        ("box", "Power sums by recurrence", [
            "Cubic: aSₙ₊₃ + bSₙ₊₂ + cSₙ₊₁ + dSₙ = 0 for n ≥ 0, with S₀ = 3.",
            "Quartic: aSₙ₊₄ + bSₙ₊₃ + cSₙ₊₂ + dSₙ₊₁ + eSₙ = 0 for n ≥ 0, with S₀ = 4.",
            "Start from S₁ = Σα and S₂ = (Σα)² − 2Σαβ. To go below the degree (e.g. S₂ for a cubic) use the identities "
            "above, or use S₋₁ = Σ1/α and the same recurrence with n = −1.",
        ]),

        ("h2", "3.4 Using the relations to find roots and coefficients"),
        ("p", "Extra information about the roots, together with the relations, often pins down the roots or unknown "
              "coefficients. Choose a notation that builds the information in:"),
        ("bullets", [
            "Roots in arithmetic progression: call them a − d, a, a + d. Then Σα = 3a gives a at once.",
            "Roots in geometric progression: call them a/r, a, ar. Then αβγ = a³ gives a at once.",
            "Roots α, kα, …: substitute into the relations and solve.",
            "A given complex root of a real polynomial: its conjugate is also a root (Unit A1), which gives a real "
            "quadratic factor z² − 2Re(w)z + |w|².",
            "After finding a root a, check it: f(a) = 0 confirms it and often gives an unknown coefficient.",
        ]),

        ("h2", "3.5 Equations whose roots are transformed (Edexcel, AQA, OCR A, MEI: linear; CAIE, OCR A: any simple substitution)"),
        ("p", "To find an equation whose roots are a function of the old roots, use a substitution. If the new root is "
              "w = g(x), where x is an old root, rearrange to x = g⁻¹(w) and substitute into the old equation. Every old "
              "root x gives a value of w that satisfies the new equation, so the new equation has exactly the new roots "
              "(provided the substitution is one-to-one)."),
        ("table", ["New roots", "Substitution", "Board notes"], [
            ["α + k, β + k, …", "x = w − k", "All boards (linear)"],
            ["kα, kβ, …", "x = w/k", "All boards (linear)"],
            ["pα + q, …", "x = (w − q)/p", "All boards (linear)"],
            ["1/α, 1/β, …", "x = 1/w (reverse the order of the coefficients)", "CAIE, OCR A; IAL quadratics"],
            ["α², β², …", "x = √w: put odd powers on one side, square, then replace x² by w", "CAIE, OCR A; IAL quadratics"],
            ["α³, β³ (quadratic)", "Use the sum and product: α³ + β³ and α³β³ = (αβ)³", "IAL FP1"],
        ]),
        ("p", "For quadratics (IAL), the quickest route to a new equation is usually to find the new sum and the new "
              "product and write x² − (sum)x + (product) = 0. For cubics and quartics, a substitution is far quicker than "
              "finding three or four new symmetric functions. MEI excludes non-linear transformations; CAIE expects the "
              "easy substitutions (reciprocals, squares, linear) without being told which to use."),
        ("box", "Squared roots without square roots", [
            "For x³ + px² + qx + r = 0, write x(x² + q) = −(px² + r). Square: x²(x² + q)² = (px² + r)².",
            "Replace x² by w: w(w + q)² = (pw + r)², a cubic in w with roots α², β², γ².",
            "Check: the new sum of roots must equal Σα² = (Σα)² − 2Σαβ.",
        ]),
        ("warn", "Common mistakes", [
            "Sign slips in the relations: Σα = −b/a, not b/a; the product of the roots of a cubic is −d/a but of a quartic "
            "+e/a. Always divide by the leading coefficient a.",
            "Writing Σα² = (Σα)² − Σαβ: the cross terms appear twice, so the correction is −2Σαβ.",
            "Substituting the wrong way round. For roots 2α − 1, the substitution is x = (w + 1)/2, not w = (x + 1)/2. "
            "Check one coefficient, such as the new sum of roots, against a direct calculation.",
            "Forgetting to give integer coefficients when asked, or leaving the answer as an expression rather than an "
            "equation (write “= 0”).",
            "CAIE examiners report candidates substituting power-sum results before simplifying, which makes the algebra "
            "harder; and finding the sum of squares but not the equation asked for (or the reverse). Answer every part.",
        ]),
    ],
    "examples": [
        {
            "title": "Symmetric functions of the roots of a quadratic",
            "question": "The roots of 2x² − 3x + 4 = 0 are α and β. Without solving the equation, find (a) α² + β², "
                        "(b) α³ + β³, (c) a quadratic equation with integer coefficients whose roots are α/β and β/α.",
            "steps": [
                "α + β = −(−3)/2 = 3/2 and αβ = 4/2 = 2.",
                "(a) α² + β² = (α + β)² − 2αβ = 9/4 − 4 = −7/4. (A negative sum of squares shows the roots are not real: "
                "here the discriminant is 9 − 32 < 0.)",
                "(b) α³ + β³ = (α + β)³ − 3αβ(α + β) = 27/8 − 3 × 2 × 3/2 = 27/8 − 9 = −45/8.",
                "(c) Sum of new roots: α/β + β/α = (α² + β²)/(αβ) = (−7/4)/2 = −7/8. Product: (α/β)(β/α) = 1.",
                "Equation: x² − (−7/8)x + 1 = 0, i.e. x² + (7/8)x + 1 = 0. Multiply by 8: <b>8x² + 7x + 8 = 0</b>.",
            ],
        },
        {
            "title": "Symmetric functions of the roots of a cubic",
            "question": "The cubic equation 2x³ + 5x² − 3x + 7 = 0 has roots α, β, γ. Find the values of (a) Σα², "
                        "(b) Σ1/α, (c) Σα³, (d) (1 + α)(1 + β)(1 + γ).",
            "steps": [
                "Here a = 2, b = 5, c = −3, d = 7, so Σα = −5/2, Σαβ = −3/2, αβγ = −7/2.",
                "(a) Σα² = (Σα)² − 2Σαβ = 25/4 + 3 = 37/4.",
                "(b) Σ1/α = Σαβ/αβγ = (−3/2)/(−7/2) = 3/7.",
                "(c) Each root satisfies 2α³ = −5α² + 3α − 7. Adding for the three roots: 2Σα³ = −5Σα² + 3Σα − 21 "
                "= −185/4 − 15/2 − 21 = −299/4, so Σα³ = −299/8. (Check: (Σα)³ − 3ΣαΣαβ + 3αβγ = −125/8 − 45/4 − 21/2 "
                "= −299/8.)",
                "(d) Expand: (1 + α)(1 + β)(1 + γ) = 1 + Σα + Σαβ + αβγ = 1 − 5/2 − 3/2 − 7/2 = −13/2.",
                "Quicker: 2(x − α)(x − β)(x − γ) = f(x), so with x = −1, (−1 − α)(−1 − β)(−1 − γ) = f(−1)/2 = 13/2, "
                "and (1 + α)(1 + β)(1 + γ) = −13/2.",
            ],
        },
        {
            "title": "Roots in arithmetic progression",
            "question": "The roots of x³ − 12x² + kx − 28 = 0 form an arithmetic progression. Find the roots and the "
                        "value of k.",
            "steps": [
                "Let the roots be a − d, a, a + d.",
                "Sum: (a − d) + a + (a + d) = 3a = 12, so a = 4. So x = 4 is a root.",
                "Product: (4 − d) × 4 × (4 + d) = 4(16 − d²) = 28, so 16 − d² = 7 and d = ±3. Either sign gives the same "
                "three roots: <b>1, 4, 7</b>.",
                "k = Σαβ = 1 × 4 + 4 × 7 + 7 × 1 = 4 + 28 + 7 = <b>39</b>.",
                "Check: f(4) = 64 − 192 + 4k − 28 = 4k − 156 = 0 when k = 39. ✓",
            ],
        },
        {
            "title": "A quartic: are the roots real?",
            "question": "The quartic equation x⁴ − 2x³ + 3x² − x + 5 = 0 has roots α, β, γ, δ. (a) Find Σα² and deduce "
                        "that the equation has at least two non-real roots. (b) Find Σ1/α and Σ1/α².",
            "steps": [
                "a = 1, b = −2, c = 3, d = −1, e = 5: Σα = 2, Σαβ = 3, Σαβγ = 1, αβγδ = 5.",
                "(a) Σα² = (Σα)² − 2Σαβ = 4 − 6 = −2. If all four roots were real, Σα² would be ≥ 0. So at least one root "
                "is non-real; the coefficients are real, so non-real roots come in conjugate pairs, giving at least two.",
                "(b) Σ1/α = Σαβγ/αβγδ = 1/5.",
                "Σ1/(αβ) = Σγδ/αβγδ = Σαβ/αβγδ = 3/5, so Σ1/α² = (Σ1/α)² − 2Σ1/(αβ) = 1/25 − 6/5 = −29/25.",
            ],
        },
        {
            "title": "Transformed roots by substitution",
            "question": "The cubic equation x³ − 3x² + 5x − 2 = 0 has roots α, β, γ. Find cubic equations with integer "
                        "coefficients whose roots are (a) 2α − 1, 2β − 1, 2γ − 1, (b) α², β², γ².",
            "steps": [
                "(a) Let w = 2x − 1, so x = (w + 1)/2. Substitute: ((w + 1)/2)³ − 3((w + 1)/2)² + 5(w + 1)/2 − 2 = 0.",
                "Multiply by 8: (w + 1)³ − 6(w + 1)² + 20(w + 1) − 16 = 0.",
                "Expand: w³ + 3w² + 3w + 1 − 6w² − 12w − 6 + 20w + 20 − 16 = 0, giving <b>w³ − 3w² + 11w − 1 = 0</b>.",
                "Check: new sum = 2Σα − 3 = 2(3) − 3 = 3, matching −(−3)/1. ✓",
                "(b) Rearrange so that only even powers are on one side: x³ + 5x = 3x² + 2, i.e. x(x² + 5) = 3x² + 2.",
                "Square: x²(x² + 5)² = (3x² + 2)². Put w = x²: w(w + 5)² = (3w + 2)².",
                "Expand: w³ + 10w² + 25w = 9w² + 12w + 4, giving <b>w³ + w² + 13w − 4 = 0</b>.",
                "Check: Σα² = (Σα)² − 2Σαβ = 9 − 10 = −1, matching the new sum −1/1. ✓",
            ],
        },
        {
            "title": "Power sums of a quartic by recurrence (exam standard)",
            "question": "The quartic equation x⁴ + 2x² − x + 3 = 0 has roots α, β, γ, δ, and Sₙ = αⁿ + βⁿ + γⁿ + δⁿ. "
                        "(a) Find S₁, S₂ and S₃. (b) Show that Sₙ₊₄ = −2Sₙ₊₂ + Sₙ₊₁ − 3Sₙ, and hence find S₄ and S₅.",
            "steps": [
                "a = 1, b = 0, c = 2, d = −1, e = 3: Σα = 0, Σαβ = 2, Σαβγ = 1, αβγδ = 3.",
                "(a) S₁ = Σα = 0. S₂ = (Σα)² − 2Σαβ = 0 − 4 = −4.",
                "For S₃ use the identity Σα³ = (Σα)³ − 3ΣαΣαβ + 3Σαβγ, which holds for any number of roots: "
                "S₃ = 0 − 0 + 3 × 1 = 3.",
                "(b) Each root satisfies α⁴ = −2α² + α − 3. Multiply by αⁿ: αⁿ⁺⁴ = −2αⁿ⁺² + αⁿ⁺¹ − 3αⁿ. Writing the same "
                "for β, γ, δ and adding: Sₙ₊₄ = −2Sₙ₊₂ + Sₙ₊₁ − 3Sₙ.",
                "n = 0 (S₀ = 4): S₄ = −2S₂ + S₁ − 3S₀ = 8 + 0 − 12 = −4.",
                "n = 1: S₅ = −2S₃ + S₂ − 3S₁ = −6 − 4 − 0 = −10.",
            ],
        },
    ],
    "practice": [
        "The roots of 3x² − 5x + 1 = 0 are α and β. Find the exact values of (a) α² + β², (b) 1/α + 1/β, (c) (α − β)².",
        "The roots of x² + 4x − 2 = 0 are α and β. Find a quadratic equation with integer coefficients whose roots are "
        "α² and β².",
        "The roots of 2x² − x + 3 = 0 are α and β. Find a quadratic equation with integer coefficients whose roots are "
        "α + 1/β and β + 1/α.",
        "The cubic equation x³ − 4x² + 2x + 5 = 0 has roots α, β, γ. Write down Σα, Σαβ and αβγ, and find Σα² and Σ1/α.",
        "The cubic equation 2x³ + 3x² − x + 4 = 0 has roots α, β, γ. Find (a) (2 − α)(2 − β)(2 − γ), (b) Σα³.",
        "The quartic equation 2x⁴ − 3x³ + x − 6 = 0 has roots α, β, γ, δ. Write down Σα, Σαβ, Σαβγ and αβγδ, and find "
        "Σα² and Σ1/α.",
        "The roots of x³ − 14x² + kx − 64 = 0 form a geometric progression. Find the roots and the value of k.",
        "The equation x³ − 6x² + px + q = 0 has roots α, 2α and 3α. Find α, p and q.",
        "The cubic equation x³ + 2x² − 5x + 1 = 0 has roots α, β, γ. Find the cubic equation whose roots are "
        "α + 2, β + 2, γ + 2.",
        "The cubic equation 2x³ − x² + 4x − 7 = 0 has roots α, β, γ. Find a cubic equation with integer coefficients "
        "whose roots are 3α, 3β, 3γ.",
        "(CAIE, OCR A) The quartic equation x⁴ + 3x³ − 2x + 5 = 0 has roots α, β, γ, δ. Find the quartic equation whose "
        "roots are 1/α, 1/β, 1/γ, 1/δ, and use it to write down Σ1/α.",
        "The cubic equation x³ − 2x + 3 = 0 has roots α, β, γ, and Sₙ = αⁿ + βⁿ + γⁿ. Find S₂, then use a recurrence "
        "to find S₃ and S₄.",
    ],
    "answers": [
        "α + β = 5/3, αβ = 1/3. (a) 25/9 − 2/3 = 19/9. (b) (5/3)/(1/3) = 5. (c) 25/9 − 4/3 = 13/9.",
        "α + β = −4, αβ = −2. α² + β² = 16 + 4 = 20; α²β² = 4. x² − 20x + 4 = 0.",
        "α + β = 1/2, αβ = 3/2. Sum = (α + β) + (α + β)/(αβ) = 1/2 + 1/3 = 5/6. Product = αβ + 2 + 1/(αβ) "
        "= 3/2 + 2 + 2/3 = 25/6. 6x² − 5x + 25 = 0.",
        "Σα = 4, Σαβ = 2, αβγ = −5. Σα² = 16 − 4 = 12. Σ1/α = 2/(−5) = −2/5.",
        "(a) (2 − α)(2 − β)(2 − γ) = f(2)/2 = (16 + 12 − 2 + 4)/2 = 15. (b) Σα = −3/2, Σαβ = −1/2, αβγ = −2; "
        "Σα³ = −27/8 − 9/4 − 6 = −93/8.",
        "Σα = 3/2, Σαβ = 0, Σαβγ = −1/2, αβγδ = −3. Σα² = 9/4 − 0 = 9/4. Σ1/α = (−1/2)/(−3) = 1/6.",
        "Roots a/r, a, ar: a³ = 64, a = 4. Sum: 4(1/r + 1 + r) = 14 gives 2r² − 5r + 2 = 0, r = 2 or 1/2. Roots 2, 4, 8. "
        "k = 8 + 32 + 16 = 56.",
        "Sum 6α = 6, α = 1; roots 1, 2, 3. p = Σαβ = 2 + 6 + 3 = 11; q = −αβγ = −6.",
        "x = w − 2: (w − 2)³ + 2(w − 2)² − 5(w − 2) + 1 = 0, giving w³ − 4w² − w + 11 = 0.",
        "x = w/3, multiply by 27: 2w³ − 3w² + 36w − 189 = 0.",
        "x = 1/w, multiply by w⁴: 5w⁴ − 2w³ + 3w + 1 = 0. Σ1/α = 2/5 (check: Σαβγ/αβγδ = 2/5).",
        "Σα = 0, Σαβ = −2, αβγ = −3, S₀ = 3. S₂ = 0 + 4 = 4. α³ = 2α − 3, so Sₙ₊₃ = 2Sₙ₊₁ − 3Sₙ. "
        "S₃ = 2S₁ − 3S₀ = −9. S₄ = 2S₂ − 3S₁ = 8.",
    ],
    "exam": [
        "The cubic equation x³ + 3x² − 2x + 6 = 0 has roots α, β, γ.\n"
        "(a) Show that α² + β² + γ² = 13. [2]\n"
        "(b) Find the value of α³ + β³ + γ³. [3]\n"
        "(c) Find a cubic equation with integer coefficients whose roots are 2α − 1, 2β − 1, 2γ − 1. [3]\n"
        "(d) Hence, or otherwise, find the value of (2α − 1)² + (2β − 1)² + (2γ − 1)². [2]",
        "The quartic equation 2x⁴ − 4x³ + 5x² + 6x − 3 = 0 has roots α, β, γ, δ.\n"
        "(a) Write down the values of Σα and Σαβ. [2]\n"
        "(b) Find Σα² and explain what your answer tells you about the roots. [3]\n"
        "(c) Find the value of Σ1/α. [2]\n"
        "(d) Using the substitution x = 1/y, show that 1/α, 1/β, 1/γ, 1/δ are the roots of "
        "3y⁴ − 6y³ − 5y² + 4y − 2 = 0, and verify your answer to part (c). [3]",
        "The cubic equation 4x³ − 12x² + px + q = 0 has three real roots that form an arithmetic progression with common "
        "difference 2.\n"
        "(a) Find the three roots. [3]\n"
        "(b) Find the values of p and q. [3]\n"
        "(c) Using the substitution y = x², or otherwise, find a cubic equation whose roots are the squares of the roots "
        "of the original equation. [3]",
        "(IAL FP1 style) The roots of the equation x² − 3x + 5 = 0 are α and β.\n"
        "(a) Without solving the equation, show that α³ + β³ = −18. [3]\n"
        "(b) Find a quadratic equation with integer coefficients whose roots are α²/β and β²/α. [4]\n"
        "(c) Given that α and β are not real, find |α|. [1]",
    ],
    "exam_answers": [
        "Σα = −3, Σαβ = −2, αβγ = −6.\n"
        "(a) Σα² = (Σα)² − 2Σαβ = 9 + 4 = 13. M1 A1 (given answer: method must be shown)\n"
        "(b) α³ = −3α² + 2α − 6 for each root, so Σα³ = −3Σα² + 2Σα − 18 M1 = −39 − 6 − 18 M1 = −63 A1.\n"
        "(c) x = (w + 1)/2 B1; substitute and multiply by 8: (w + 1)³ + 6(w + 1)² − 8(w + 1) + 48 = 0 M1; "
        "w³ + 9w² + 7w + 47 = 0 A1.\n"
        "(d) New Σα = −9, Σαβ = 7, so Σ(2α − 1)² = 81 − 14 = 67 M1 A1. (Or Σ(4α² − 4α + 1) = 52 + 12 + 3 = 67.)",
        "(a) Σα = 4/2 = 2 B1, Σαβ = 5/2 B1.\n"
        "(b) Σα² = 4 − 5 = −1 M1 A1. A sum of squares of real numbers cannot be negative, so the roots are not all real "
        "(at least two, a conjugate pair, are non-real) E1.\n"
        "(c) Σαβγ = −6/2 = −3, αβγδ = −3/2 B1; Σ1/α = (−3)/(−3/2) = 2 A1.\n"
        "(d) 2/y⁴ − 4/y³ + 5/y² + 6/y − 3 = 0 M1; multiply by y⁴ and by −1: 3y⁴ − 6y³ − 5y² + 4y − 2 = 0 A1 (given). "
        "Sum of roots of this quartic = 6/3 = 2, agreeing with (c) B1.",
        "(a) Roots a − 2, a, a + 2 M1; sum 3a = 12/4 = 3, a = 1 A1; roots −1, 1, 3 A1.\n"
        "(b) Σαβ = −1 − 3 + 3 = −1 = p/4, p = −4 M1 A1; αβγ = −3 = −q/4, q = 12 A1.\n"
        "(c) The equation is x³ − 3x² − x + 3 = 0, i.e. x(x² − 1) = 3(x² − 1). Square and put y = x²: "
        "y(y − 1)² = 9(y − 1)² M1. Expand: y³ − 11y² + 19y − 9 = 0 A1. Check: the new roots are 1, 1, 9, and "
        "(y − 1)²(y − 9) expands to the same cubic B1.",
        "α + β = 3, αβ = 5 B1.\n"
        "(a) α³ + β³ = (α + β)³ − 3αβ(α + β) M1 = 27 − 45 A1 = −18 A1 (given answer).\n"
        "(b) Sum = (α³ + β³)/(αβ) = −18/5 M1 A1; product = (α²/β)(β²/α) = αβ = 5 B1; x² + (18/5)x + 5 = 0, "
        "5x² + 18x + 25 = 0 A1.\n"
        "(c) β = α* (conjugate pair), so |α|² = αα* = αβ = 5 and |α| = √5 B1.",
    ],
}
