UNIT = {
    "number": "B6",
    "title": "Further integration techniques",
    "tag": "Edexcel CP 5.4, 5.6, 8.5 · IAL FP3 4.3, 4.4 · AQA E4, E6, H5 (A level) · OCR A 4.05c, 4.08f, 4.08h · "
           "OCR MEI Pc4, Pc6, Pa8 · CAIE 9231 P2 2.4 (standard integrals, substitutions, completing the square)",
    "notes": [
        ("p", "This unit collects the integration methods that lead to inverse trigonometric and inverse hyperbolic functions. "
              "It uses the derivatives and logarithmic forms of arcsin, arctan, arsinh (sinh⁻¹), arcosh (cosh⁻¹) and artanh from "
              "Unit B5, and the identities cos²θ + sin²θ = 1, 1 + tan²θ = sec²θ and cosh²u − sinh²u = 1 (Unit B4)."),
        ("h2", "B6.1 Partial fractions with a quadratic factor (Edexcel CP 5.4, AQA E4, OCR A 4.05c and 4.08f, MEI Pc4)"),
        ("p", "In A level Mathematics you split fractions with linear (and repeated linear) factors. A quadratic factor ax² + c with "
              "a and c both positive cannot be factorised over the real numbers, so it stays whole. Its partial fraction needs a "
              "<b>linear numerator</b> Bx + C, because the numerator of a proper fraction can have degree one less than the "
              "denominator."),
        ("box", "Partial fractions with ax² + c (a, c > 0)", [
            "(px² + qx + s)/((dx + e)(ax² + c)) ≡ A/(dx + e) + (Bx + C)/(ax² + c).",
            "Improper fraction (degree of numerator ≥ degree of denominator, OCR A 4.05c): divide first to get a polynomial plus a "
            "proper fraction, then split the proper fraction.",
            "MEI Pc4 limits questions to one linear factor with the ax² + c factor; the other boards may combine more.",
        ]),
        ("p", "Find A by substituting the root of the linear factor, then find B and C by comparing the coefficients of x² and the "
              "constant terms. To integrate (Bx + C)/(ax² + c), split it into two parts:"),
        ("box", "Integrating over ax² + c", [
            "∫ x/(ax² + c) dx = (1/(2a)) ln(ax² + c) + k   (the numerator is a multiple of the derivative of the denominator).",
            "∫ 1/(ax² + c) dx = (1/a)∫ 1/(x² + c/a) dx = (1/√(ac)) arctan(x√(a/c)) + k.",
            "Example: ∫ 1/(4x² + 9) dx = ¼ ∫ 1/(x² + 9/4) dx = ¼ × ⅔ arctan(2x/3) = ⅙ arctan(2x/3) + k.",
        ]),
        ("h2", "B6.2 The standard integrals and where they come from (Edexcel CP 5.6, 8.5; AQA E6, H5; OCR A 4.08h; MEI Pc6, Pa8)"),
        ("box", "Standard integrals (printed in every booklet, including CAIE MF19)", [
            "∫ 1/√(a² − x²) dx = arcsin(x/a) + c,   |x| < a.",
            "∫ 1/(a² + x²) dx = (1/a) arctan(x/a) + c.",
            "∫ 1/√(x² + a²) dx = arsinh(x/a) + c = ln(x + √(x² + a²)) + c.",
            "∫ 1/√(x² − a²) dx = arcosh(x/a) + c = ln(x + √(x² − a²)) + c,   x > a.",
        ]),
        ("p", "Each result comes from a substitution that turns the square root into a single term. You may be asked to show this, "
              "and you must be able to choose such substitutions for related integrals."),
        ("bullets", [
            "x = a sin θ, with −π/2 ≤ θ ≤ π/2: √(a² − x²) = √(a² cos²θ) = a cos θ (cos θ ≥ 0 here) and dx = a cos θ dθ, so "
            "∫ 1/√(a² − x²) dx = ∫ dθ = θ = arcsin(x/a).",
            "x = a tan θ: a² + x² = a² sec²θ and dx = a sec²θ dθ, so ∫ 1/(a² + x²) dx = ∫ (1/a) dθ = (1/a) arctan(x/a).",
            "x = a sinh u: √(x² + a²) = a cosh u and dx = a cosh u du, so ∫ 1/√(x² + a²) dx = ∫ du = arsinh(x/a).",
            "x = a cosh u, u ≥ 0: √(x² − a²) = a sinh u and dx = a sinh u du, so ∫ 1/√(x² − a²) dx = u = arcosh(x/a).",
            "The two forms of the last two results differ by a constant: arsinh(x/a) = ln(x/a + √(x²/a² + 1)) = "
            "ln(x + √(x² + a²)) − ln a, and the −ln a is absorbed into c.",
        ]),
        ("p", "<b>A coefficient on x².</b> Take it out first, or substitute u = kx. For example ∫ 1/√(9 − 4x²) dx = "
              "½ ∫ 1/√(9/4 − x²) dx = ½ arcsin(2x/3) + c, and ∫ 1/√(4x² + 9) dx = ½ arsinh(2x/3) + c."),
        ("table", ["Integrand contains", "Substitution", "Identity used"], [
            ["√(a² − x²)", "x = a sin θ", "1 − sin²θ = cos²θ"],
            ["a² + x², (a² + x²)ⁿ", "x = a tan θ", "1 + tan²θ = sec²θ"],
            ["√(x² + a²)", "x = a sinh u (or a tan θ)", "1 + sinh²u = cosh²u"],
            ["√(x² − a²)", "x = a cosh u (or a sec θ)", "cosh²u − 1 = sinh²u"],
        ]),
        ("figure", "pb06_triangles.png", "Right-angled triangles turn an answer in θ back into x. Left: x = a sin θ gives "
                                         "cos θ = √(a² − x²)/a. Right: x = a tan θ gives sin θ = x/√(a² + x²) and cos θ = a/√(a² + x²).", 120),
        ("h2", "B6.3 Substitutions for related integrals (all boards; IAL FP3 4.3–4.4)"),
        ("p", "When the integrand is not exactly a standard form, for example √(a² − x²), x²/√(1 − x²), 1/(1 + x²)² or √(x² + 9), "
              "use the same substitution. Replace dx as well as x, simplify with the identity, and integrate in θ or u. Then "
              "either change the limits (definite integrals) or convert back to x using the triangle or sinh 2u = 2 sinh u cosh u. "
              "Useful results: cos²θ = ½(1 + cos 2θ), sin²θ = ½(1 − cos 2θ), cosh²u = ½(cosh 2u + 1). In harder cases the "
              "question will give you the substitution."),
        ("box", "Two results worth remembering how to derive", [
            "∫ √(a² − x²) dx = ½a² arcsin(x/a) + ½x√(a² − x²) + c   (x = a sin θ).",
            "∫ √(x² + a²) dx = ½a² arsinh(x/a) + ½x√(x² + a²) + c   (x = a sinh u).",
        ]),
        ("h2", "B6.4 Completing the square (CAIE 2.4; all boards)"),
        ("p", "If the quadratic has an x term, complete the square to reach one of the standard forms, then use u = x + p "
              "(du = dx, so nothing else changes):"),
        ("bullets", [
            "x² + 4x + 13 = (x + 2)² + 9, so ∫ 1/(x² + 4x + 13) dx = ⅓ arctan((x + 2)/3) + c.",
            "3 + 2x − x² = 4 − (x − 1)², so ∫ 1/√(3 + 2x − x²) dx = arcsin((x − 1)/2) + c. Take out the minus sign carefully: "
            "−x² + 2x + 3 = −(x² − 2x) + 3 = −(x − 1)² + 4.",
            "x² + x = (x + ½)² − ¼, so ∫ 1/√(x² + x) dx = arcosh((x + ½)/½) = arcosh(2x + 1) + c = ln(2x + 1 + 2√(x² + x)) + c "
            "for x > 0 (the CAIE example).",
            "If the leading coefficient is not 1, take it out first: 4x² + 8x + 13 = 4(x + 1)² + 9.",
        ]),
        ("h2", "B6.5 Linear numerators and quadratic surds (IAL FP3 4.4; all boards)"),
        ("p", "For ∫ (px + q)/√(ax² + bx + c) dx, write the numerator as a multiple of the derivative of the quadratic plus a "
              "constant: px + q = k(2ax + b) + m. The first part integrates by the reverse chain rule, ∫ k(2ax + b)(ax² + bx + c)^(−½) dx "
              "= 2k√(ax² + bx + c); the constant part needs completing the square. Fractions (px + q)/(ax² + bx + c) split the same way, "
              "into a logarithm and an arctan."),
        ("p", "For example, x + 3 = ½(2x + 2) + 2, so ∫ (x + 3)/√(x² + 2x + 5) dx = √(x² + 2x + 5) + 2 ∫ 1/√((x + 1)² + 4) dx "
              "= √(x² + 2x + 5) + 2 arsinh((x + 1)/2) + c."),
        ("h2", "B6.6 Choosing a method"),
        ("table", ["Integrand", "Method", "Result type"], [
            ["1/(a² + x²)", "standard form", "(1/a) arctan(x/a)"],
            ["1/(x² − a²), 1/(a² − x²)", "factorise, partial fractions (or artanh, Unit B5)", "logarithms"],
            ["x/(a² + x²), x/√(a² − x²)", "reverse chain rule", "½ ln(a² + x²), −√(a² − x²)"],
            ["1/√(a² − x²)", "standard form", "arcsin(x/a)"],
            ["1/√(x² + a²), 1/√(x² − a²)", "standard form", "arsinh, arcosh or ln forms"],
            ["quadratic with an x term", "complete the square", "as above, with x + p"],
            ["(px + q)/quadratic or surd", "split the numerator", "ln or surd, plus arctan, arcsin, arsinh or arcosh"],
            ["√(a² − x²), (a² + x²)⁻², √(x² + a²)", "trig or hyperbolic substitution", "mixed"],
        ]),
        ("box", "Given or learn", [
            "Given: the four standard integrals above, in every board's booklet (with the log forms). Edexcel, IAL, AQA and CAIE also "
            "print the derivatives of the inverse functions.",
            "Learn: the partial-fraction form (Bx + C)/(ax² + c), how to take out a coefficient, completing the square, and which "
            "substitution to choose. Derivations by substitution may be asked for on every board.",
        ]),
        ("warn", "Common mistakes", [
            "Losing the 1/a: ∫ 1/(4 + x²) dx = ½ arctan(x/2) + c, not arctan(x/2) + c.",
            "Not taking out the coefficient of x²: ∫ 1/(9 + 4x²) dx = ⅙ arctan(2x/3) + c.",
            "Treating 1/(x² − 4) like 1/(x² + 4). It factorises, so use partial fractions (logarithms), not arctan.",
            "Writing B/(ax² + c) instead of (Bx + C)/(ax² + c) in partial fractions, or not dividing an improper fraction first.",
            "In a substitution, forgetting to replace dx, or forgetting to change the limits.",
            "Mixing up the log forms: ln(x + √(x² + a²)) goes with arsinh, ln(x + √(x² − a²)) with arcosh (x > a only).",
            "Sign slips when completing the square with a negative x² term.",
        ]),
    ],
    "examples": [
        {
            "title": "Partial fractions with a quadratic factor",
            "question": "(a) Express (5x² − 2x + 7)/((x − 1)(x² + 4)) in partial fractions.\n"
                        "(b) Hence find ∫<sub>2</sub><sup>4</sup> (5x² − 2x + 7)/((x − 1)(x² + 4)) dx in exact form.",
            "steps": [
                "(a) 5x² − 2x + 7 ≡ A(x² + 4) + (Bx + C)(x − 1).",
                "x = 1: 10 = 5A, so A = 2. Coefficients of x²: 5 = A + B, so B = 3. Constants: 7 = 4A − C, so C = 1.",
                "So the fraction is <b>2/(x − 1) + (3x + 1)/(x² + 4)</b>.",
                "(b) ∫ [2/(x − 1) + 3x/(x² + 4) + 1/(x² + 4)] dx = 2 ln|x − 1| + (3/2) ln(x² + 4) + ½ arctan(x/2).",
                "From 2 to 4: 2 ln 3 + (3/2) ln(20/8) + ½(arctan 2 − arctan 1)",
                "= <b>2 ln 3 + (3/2) ln(5/2) + ½ arctan 2 − π/8</b> ≈ 3.73.",
            ],
        },
        {
            "title": "An improper fraction (OCR A 4.05c)",
            "question": "Show that ∫₀¹ (x³ + 2x² + 3x + 4)/(x² + 1) dx = 5/2 + ln 2 + π/2.",
            "steps": [
                "The numerator has degree 3 and the denominator degree 2, so divide first: x³ + 2x² + 3x + 4 = (x + 2)(x² + 1) + (2x + 2).",
                "The integrand is x + 2 + 2x/(x² + 1) + 2/(x² + 1).",
                "∫₀¹ (x + 2) dx = ½ + 2 = 5/2.   ∫₀¹ 2x/(x² + 1) dx = [ln(x² + 1)]₀¹ = ln 2.   ∫₀¹ 2/(x² + 1) dx = 2[arctan x]₀¹ = π/2.",
                "Total: <b>5/2 + ln 2 + π/2</b>, as required.",
            ],
        },
        {
            "title": "Standard forms with coefficients",
            "question": "Find the exact values of\n(a) ∫<sub>0</sub><sup>3/4</sup> 1/√(9 − 4x²) dx\n(b) ∫<sub>0</sub><sup>3/2</sup> 1/(3 + 4x²) dx\n"
                        "(c) ∫₀² 1/√(4x² + 9) dx\n(d) ∫₃⁵ 1/√(x² − 9) dx.",
            "steps": [
                "(a) ½ ∫ 1/√(9/4 − x²) dx = ½ arcsin(2x/3). From 0 to 3/4: ½ arcsin(½) = <b>π/12</b>.",
                "(b) ¼ ∫ 1/(3/4 + x²) dx = ¼ × (2/√3) arctan(2x/√3) = (1/(2√3)) arctan(2x/√3). At 3/2: arctan(√3) = π/3, so the "
                "value is π/(6√3) = <b>π√3/18</b>.",
                "(c) ½ ∫ 1/√(x² + 9/4) dx = ½ arsinh(2x/3). From 0 to 2: ½ arsinh(4/3) = ½ ln(4/3 + √(16/9 + 1)) = ½ ln(4/3 + 5/3) "
                "= <b>½ ln 3</b>.",
                "(d) [arcosh(x/3)]₃⁵ = arcosh(5/3) − arcosh 1 = ln(5/3 + 4/3) − 0 = <b>ln 3</b>.",
            ],
        },
        {
            "title": "A trigonometric substitution",
            "question": "Use the substitution x = 2 sin θ to show that ∫₀¹ √(4 − x²) dx = π/3 + √3/2. Interpret the result "
                        "geometrically.",
            "figure": "pb06_circle.png",
            "caption": "The region under y = √(4 − x²) for 0 ≤ x ≤ 1 is a sector of angle π/6 plus a triangle.",
            "width_mm": 65,
            "steps": [
                "dx = 2 cos θ dθ. Limits: x = 0 gives θ = 0; x = 1 gives sin θ = ½, θ = π/6.",
                "√(4 − 4 sin²θ) = 2 cos θ (cos θ ≥ 0 for 0 ≤ θ ≤ π/6).",
                "∫<sub>0</sub><sup>π/6</sup> 2 cos θ × 2 cos θ dθ = ∫ 4 cos²θ dθ = ∫ 2(1 + cos 2θ) dθ = [2θ + sin 2θ]<sub>0</sub><sup>π/6</sup>.",
                "= π/3 + sin(π/3) = <b>π/3 + √3/2</b>.",
                "The region is part of a disc of radius 2: a sector of angle π/6 (area ½ × 4 × π/6 = π/3) plus a right-angled "
                "triangle with legs 1 and √3 (area √3/2).",
            ],
        },
        {
            "title": "Completing the square",
            "question": "Find the exact values of\n(a) ∫₃⁵ 1/(x² − 6x + 13) dx\n(b) ∫<sub>−2</sub><sup>0</sup> 1/√(x² + 4x + 8) dx\n"
                        "(c) ∫<sub>2</sub><sup>7/2</sup> 1/√(5 + 4x − x²) dx.",
            "steps": [
                "(a) x² − 6x + 13 = (x − 3)² + 4. ∫ = [½ arctan((x − 3)/2)]₃⁵ = ½ arctan 1 = <b>π/8</b>.",
                "(b) x² + 4x + 8 = (x + 2)² + 4. ∫ = [arsinh((x + 2)/2)]<sub>−2</sub><sup>0</sup> = arsinh 1 = <b>ln(1 + √2)</b>.",
                "(c) 5 + 4x − x² = 9 − (x − 2)². ∫ = [arcsin((x − 2)/3)]<sub>2</sub><sup>7/2</sup> = arcsin(½) = <b>π/6</b>.",
            ],
        },
        {
            "title": "A quadratic surd with a linear numerator",
            "question": "Show that ∫<sub>−2</sub><sup>2</sup> (2x + 7)/√(x² + 4x + 13) dx = 4 + 3 ln 3.",
            "steps": [
                "The derivative of x² + 4x + 13 is 2x + 4, so write 2x + 7 = (2x + 4) + 3.",
                "∫ (2x + 4)/√(x² + 4x + 13) dx = 2√(x² + 4x + 13) (reverse chain rule).",
                "x² + 4x + 13 = (x + 2)² + 9, so ∫ 3/√((x + 2)² + 9) dx = 3 arsinh((x + 2)/3).",
                "At x = 2: 2√25 + 3 arsinh(4/3) = 10 + 3 ln 3 (since arsinh(4/3) = ln(4/3 + 5/3) = ln 3). At x = −2: 2√9 + 0 = 6.",
                "Value = 10 + 3 ln 3 − 6 = <b>4 + 3 ln 3</b>, as required.",
            ],
        },
    ],
    "practice": [
        "Express (x + 5)/((x + 1)(x² + 1)) in partial fractions, and hence show that ∫₀¹ (x + 5)/((x + 1)(x² + 1)) dx = ln 2 + 3π/4.",
        "Find ∫ 1/(x(x² + 4)) dx.",
        "Find ∫ (x² + 3)/(x² + 1) dx.",
        "Find the exact value of ∫₀² 1/(4 + x²) dx.",
        "Find the exact values of (a) ∫<sub>0</sub><sup>1/2</sup> 1/√(1 − x²) dx (b) ∫<sub>0</sub><sup>1/3</sup> 1/√(4 − 9x²) dx.",
        "Find ∫ 1/(25 + 9x²) dx.",
        "Show that ∫₀⁴ 1/√(x² + 9) dx = ln 3.",
        "Find the exact value of ∫₂⁴ 1/√(x² − 4) dx, giving your answer as a logarithm.",
        "Find ∫ 1/(x² + 2x + 5) dx.",
        "Find the exact value of ∫₁³ 1/√(3 + 2x − x²) dx.",
        "Use the substitution x = tan θ to show that ∫₀¹ 1/(1 + x²)² dx = π/8 + ¼.",
        "Find ∫ (x + 2)/√(x² + 1) dx.",
    ],
    "answers": [
        "2/(x + 1) + (3 − 2x)/(x² + 1). Integral: [2 ln(x + 1) − ln(x² + 1) + 3 arctan x]₀¹ = 2 ln 2 − ln 2 + 3π/4 = ln 2 + 3π/4.",
        "1/(x(x² + 4)) = ¼(1/x − x/(x² + 4)); integral ¼ ln|x| − ⅛ ln(x² + 4) + c.",
        "1 + 2/(x² + 1); integral x + 2 arctan x + c.",
        "[½ arctan(x/2)]₀² = π/8.",
        "(a) π/6 (b) [⅓ arcsin(3x/2)]<sub>0</sub><sup>1/3</sup> = ⅓ × π/6 = π/18.",
        "(1/15) arctan(3x/5) + c.",
        "arsinh(4/3) = ln(4/3 + 5/3) = ln 3.",
        "arcosh 2 − arcosh 1 = ln(2 + √3).",
        "x² + 2x + 5 = (x + 1)² + 4; ½ arctan((x + 1)/2) + c.",
        "3 + 2x − x² = 4 − (x − 1)²; [arcsin((x − 1)/2)]₁³ = π/2.",
        "dx = sec²θ dθ; ∫<sub>0</sub><sup>π/4</sup> cos²θ dθ = [θ/2 + ¼ sin 2θ]<sub>0</sub><sup>π/4</sup> = π/8 + ¼.",
        "√(x² + 1) + 2 arsinh x + c (or + 2 ln(x + √(x² + 1)) + c).",
    ],
    "exam": [
        "f(x) = (3x² + 4x + 9)/((x + 1)(x² + 3)).\n"
        "(a) Express f(x) in partial fractions. [4]\n"
        "(b) Hence show that ∫₀³ f(x) dx = 5 ln 2 + π√3/3. [6]",
        "(a) Use the substitution x = 3 sinh u to show that ∫ √(x² + 9) dx = (9/2) arsinh(x/3) + (x/2)√(x² + 9) + c. [6]\n"
        "(b) Hence find the exact value of ∫₀⁴ √(x² + 9) dx, giving your answer in the form a + b ln 3. [3]",
        "(a) Express 4x² + 8x + 13 in the form a(x + b)² + c. [2]\n"
        "(b) Find the exact value of ∫<sub>−1</sub><sup>1/2</sup> 1/(4x² + 8x + 13) dx. [3]\n"
        "(c) Show that ∫<sub>−1</sub><sup>1</sup> (8x + 11)/√(4x² + 8x + 13) dx = 4 + (3/2) ln 3. [6]",
        "(a) Use the substitution x = 2 tan θ to show that ∫₀² 1/(4 + x²)^(3/2) dx = √2/8. [5]\n"
        "(b) The region bounded by the curve y = 1/(4 + x²), the x-axis, the y-axis and the line x = 2 is rotated through 2π "
        "radians about the x-axis. Find the exact volume of the solid formed. [6]",
    ],
    "exam_answers": [
        "(a) 3x² + 4x + 9 ≡ A(x² + 3) + (Bx + C)(x + 1) [M1]; x = −1: 8 = 4A, A = 2 [A1]; x²: B = 1; constants: 9 = 3A + C, C = 3 [M1 A1]. "
        "f(x) = 2/(x + 1) + (x + 3)/(x² + 3).\n"
        "(b) ∫ = 2 ln(x + 1) + ½ ln(x² + 3) + (3/√3) arctan(x/√3) [M1 A1 M1 A1]; from 0 to 3: 2 ln 4 + ½ ln 4 + √3 arctan √3 [M1] "
        "= 5 ln 2 + √3 × π/3 = 5 ln 2 + π√3/3 [A1].",
        "(a) dx = 3 cosh u du; √(9 sinh²u + 9) = 3 cosh u [M1 A1]; ∫ 9 cosh²u du = (9/2)∫ (1 + cosh 2u) du [M1] = (9/2)(u + ½ sinh 2u) "
        "[A1] = (9/2)(u + sinh u cosh u) [M1] = (9/2) arsinh(x/3) + (9/2)(x/3)(√(x² + 9)/3) = (9/2) arsinh(x/3) + (x/2)√(x² + 9) + c [A1].\n"
        "(b) At x = 4: (9/2) arsinh(4/3) + 2 × 5 [M1]; arsinh(4/3) = ln 3 [B1]; at 0: 0. Value = 10 + (9/2) ln 3 [A1].",
        "(a) 4(x + 1)² + 9 [B1 B1].\n"
        "(b) ∫ 1/(4(x + 1)² + 9) dx = ⅙ arctan(2(x + 1)/3) [M1 A1]; from −1 to ½: ⅙ arctan 1 = π/24 [A1].\n"
        "(c) 8x + 11 = (8x + 8) + 3 [M1]; ∫ (8x + 8)/√(…) dx = 2√(4x² + 8x + 13) [A1]; ∫ 3/√(4(x + 1)² + 9) dx = (3/2) arsinh(2(x + 1)/3) "
        "[M1 A1]; at 1: 2 × 5 + (3/2) arsinh(4/3) = 10 + (3/2) ln 3; at −1: 2 × 3 + 0 = 6 [M1]; value 4 + (3/2) ln 3 [A1].",
        "(a) dx = 2 sec²θ dθ; (4 + 4 tan²θ)^(3/2) = 8 sec³θ [M1 A1]; limits 0 and π/4 [B1]; ∫ ¼ cos θ dθ [A1] = [¼ sin θ]<sub>0</sub><sup>π/4</sup> "
        "= √2/8 [A1].\n"
        "(b) V = π∫₀² 1/(4 + x²)² dx [M1]; x = 2 tan θ: ∫ 2 sec²θ/(16 sec⁴θ) dθ = ⅛∫ cos²θ dθ [M1 A1] = (1/16)[θ + ½ sin 2θ]<sub>0</sub><sup>π/4</sup> "
        "[M1] = (1/16)(π/4 + ½) = (π + 2)/64 [A1]; V = π(π + 2)/64 [A1].",
    ],
}
