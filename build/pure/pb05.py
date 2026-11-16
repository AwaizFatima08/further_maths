UNIT = {
    "number": "B5",
    "title": "Calculus of hyperbolic and inverse functions",
    "tag": "A2 Core Pure · Edexcel CP 5.5, 8.2 · IAL FP3 3.1, 3.2, 4.1, 4.2 · AQA E5, H2 · OCR A 4.07d, 4.08g · "
           "OCR MEI inverse-trig definitions, Pc5, Pa5 · CAIE 9231 P2 2.3 (and the hyperbolic part of 2.4)",
    "notes": [
        ("h2", "5.1 The inverse trigonometric functions"),
        ("p", "sin, cos and tan are not one-to-one, so before inverting each one we restrict its domain to an interval on which it "
              "takes every value exactly once. The resulting <b>principal values</b> are fixed by convention, and you must know them "
              "(MEI lists the definitions explicitly; every other board assumes them from A level Mathematics). "
              "arcsin x is also written sin⁻¹ x, and so on; sin⁻¹ x never means 1/sin x."),
        ("table", ["Function", "Domain", "Range (principal values)", "Defined by"], [
            ["y = arcsin x", "−1 ≤ x ≤ 1", "−π/2 ≤ y ≤ π/2", "sin y = x"],
            ["y = arccos x", "−1 ≤ x ≤ 1", "0 ≤ y ≤ π", "cos y = x"],
            ["y = arctan x", "all real x", "−π/2 < y < π/2", "tan y = x"],
        ]),
        ("figure", "pb05_inverse_trig.png", "y = arcsin x, y = arccos x and y = arctan x. arctan has horizontal asymptotes y = ±π/2.", 105),
        ("p", "Two useful facts follow from the graphs: arcsin x + arccos x = π/2 for −1 ≤ x ≤ 1, and arcsin and arctan are odd "
              "while arccos(−x) = π − arccos x."),
        ("h2", "5.2 Differentiating the inverse trigonometric functions"),
        ("p", "OCR A (4.08g) says “derive and use”; the other boards expect the derivation in a “show that” question. The method is "
              "implicit differentiation, followed by choosing the correct sign of a square root from the range."),
        ("p", "<b>arcsin.</b> Let y = arcsin x, so sin y = x. Differentiate with respect to x: cos y (dy/dx) = 1. On the range "
              "−π/2 ≤ y ≤ π/2, cos y ≥ 0, so cos y = +√(1 − sin²y) = √(1 − x²). Hence dy/dx = 1/√(1 − x²), for −1 < x < 1."),
        ("p", "<b>arccos.</b> cos y = x gives −sin y (dy/dx) = 1. On 0 ≤ y ≤ π, sin y ≥ 0, so sin y = √(1 − x²) and "
              "dy/dx = −1/√(1 − x²)."),
        ("p", "<b>arctan.</b> tan y = x gives sec²y (dy/dx) = 1, and sec²y = 1 + tan²y = 1 + x², so dy/dx = 1/(1 + x²) for all x."),
        ("box", "Derivatives of the inverse trigonometric functions", [
            "d/dx (arcsin x) = 1/√(1 − x²);   d/dx (arccos x) = −1/√(1 − x²);   d/dx (arctan x) = 1/(1 + x²)",
            "With the chain rule: d/dx arcsin(x/a) = 1/√(a² − x²),   d/dx arctan(x/a) = a/(a² + x²),   d/dx arcsin(f(x)) = f′(x)/√(1 − f(x)²).",
        ]),
        ("h2", "5.3 Differentiating the hyperbolic functions"),
        ("p", "Differentiate the exponential definitions: d/dx sinh x = d/dx ½(eˣ − e⁻ˣ) = ½(eˣ + e⁻ˣ) = cosh x, and in the same way "
              "d/dx cosh x = sinh x. Notice that there is <b>no minus sign</b> for cosh, unlike d/dx cos x = −sin x. The rest follow "
              "from the quotient rule and the identity cosh²x − sinh²x ≡ 1:"),
        ("p", "d/dx tanh x = d/dx (sinh x/cosh x) = (cosh x cosh x − sinh x sinh x)/cosh²x = 1/cosh²x = sech²x."),
        ("box", "Derivatives of hyperbolic functions", [
            "d/dx sinh x = cosh x;   d/dx cosh x = sinh x;   d/dx tanh x = sech²x",
            "(IAL, AQA, CAIE) d/dx sech x = −sech x tanh x;   d/dx cosech x = −cosech x coth x;   d/dx coth x = −cosech²x",
            "With a constant k: d/dx sinh kx = k cosh kx, d/dx cosh kx = k sinh kx (on the must-know list of Edexcel, OCR A and MEI).",
        ]),
        ("h2", "5.4 Differentiating the inverse hyperbolic functions"),
        ("p", "The same implicit method works. <b>arsinh:</b> sinh y = x, so cosh y (dy/dx) = 1, and cosh y = +√(1 + sinh²y) = "
              "√(1 + x²) because cosh y > 0. So dy/dx = 1/√(1 + x²). <b>arcosh:</b> cosh y = x with y ≥ 0, so sinh y (dy/dx) = 1, and "
              "sinh y = +√(x² − 1) because y ≥ 0. So dy/dx = 1/√(x² − 1), x > 1. <b>artanh:</b> tanh y = x, so sech²y (dy/dx) = 1, and "
              "sech²y = 1 − tanh²y = 1 − x². So dy/dx = 1/(1 − x²), |x| < 1."),
        ("p", "You can also differentiate the logarithmic forms. For example d/dx ln(x + √(x² + 1)) = (1 + x/√(x² + 1))/(x + √(x² + 1)) "
              "= ((√(x² + 1) + x)/√(x² + 1))/(x + √(x² + 1)) = 1/√(x² + 1)."),
        ("box", "Derivatives of inverse hyperbolic functions", [
            "d/dx (arsinh x) = 1/√(x² + 1);   d/dx (arcosh x) = 1/√(x² − 1), x > 1;   d/dx (artanh x) = 1/(1 − x²), |x| < 1",
            "Compare: arcsin gives 1/√(1 − x²), arsinh gives 1/√(1 + x²), arcosh gives 1/√(x² − 1). The sign pattern inside the root tells them apart.",
        ]),
        ("h2", "5.5 Integrating hyperbolic functions"),
        ("p", "Reversing section 5.3 gives the standard integrals. Beyond these, use the same techniques as for trigonometric "
              "integrals: identities to lower powers, a substitution when one factor is the derivative of another, integration by "
              "parts, or, when all else fails, the exponential definitions."),
        ("box", "Standard hyperbolic integrals (+ C omitted)", [
            "∫ sinh kx dx = (1/k) cosh kx;   ∫ cosh kx dx = (1/k) sinh kx;   ∫ sech²kx dx = (1/k) tanh kx",
            "∫ tanh x dx = ln cosh x;   ∫ coth x dx = ln|sinh x|;   ∫ cosech²x dx = −coth x",
            "∫ sech x tanh x dx = −sech x;   ∫ cosech x coth x dx = −cosech x;   ∫ sech x dx = 2 arctan(eˣ)",
        ]),
        ("bullets", [
            "<b>Even powers:</b> use cosh 2x: sinh²x = ½(cosh 2x − 1) and cosh²x = ½(cosh 2x + 1). "
            "So ∫ sinh²x dx = ¼ sinh 2x − ½x + C. (Osborn's rule warns you: the sign is the opposite of sin²x = ½(1 − cos 2x).)",
            "<b>Odd powers:</b> keep one factor and convert the rest: ∫ cosh³x dx = ∫ cosh x(1 + sinh²x) dx = sinh x + ⅓ sinh³x + C.",
            "<b>Products with eˣ:</b> use the definitions: ∫ eˣ sinh x dx = ∫ ½(e²ˣ − 1) dx = ¼e²ˣ − ½x + C.",
            "<b>By parts:</b> ∫ x cosh x dx = x sinh x − ∫ sinh x dx = x sinh x − cosh x + C.",
            "<b>sech x</b> (an extension): sech x = 2/(eˣ + e⁻ˣ) = 2eˣ/(e²ˣ + 1), and the substitution u = eˣ gives 2 arctan(eˣ) + C.",
        ]),
        ("h2", "5.6 Integrals that give inverse functions, and integrating the inverse functions"),
        ("p", "Reading the boxes of sections 5.2 and 5.4 backwards gives ∫ 1/√(1 − x²) dx = arcsin x, ∫ 1/(1 + x²) dx = arctan x, "
              "∫ 1/√(1 + x²) dx = arsinh x, ∫ 1/√(x² − 1) dx = arcosh x (x > 1) and ∫ 1/(1 − x²) dx = artanh x (|x| < 1). "
              "Unit B6 extends these to a² in place of 1 and to substitutions."),
        ("p", "To integrate an inverse function itself (IAL FP3 4.2), write it as 1 × (the function) and use integration by parts with "
              "u = the inverse function and dv/dx = 1. For example ∫ arctan x dx = x arctan x − ∫ x/(1 + x²) dx = "
              "x arctan x − ½ ln(1 + x²) + C."),
        ("table", ["Integral", "Result (+ C)"], [
            ["∫ arcsin x dx", "x arcsin x + √(1 − x²)"],
            ["∫ arctan x dx", "x arctan x − ½ ln(1 + x²)"],
            ["∫ arsinh x dx", "x arsinh x − √(1 + x²)"],
            ["∫ arcosh x dx", "x arcosh x − √(x² − 1)"],
            ["∫ artanh x dx", "x artanh x + ½ ln(1 − x²)"],
        ]),
        ("box", "Given or learn? (by board)", [
            "Derivatives of arcsin, arccos, arctan: printed by every board's booklet; derivations may still be asked.",
            "Derivatives of arsinh, arcosh, artanh: printed by Edexcel, IAL, AQA and Cambridge; learn them for OCR A and MEI.",
            "Derivatives and integrals of sinh kx and cosh kx: must-know for Edexcel, OCR A and MEI (AQA does not list them, but prints sinh/cosh/tanh derivatives).",
            "sech, cosech, coth derivatives and the integrals of tanh, coth: learn (Edexcel prints ∫ tanh x dx).",
        ]),
        ("warn", "Common mistakes", [
            "Writing d/dx cosh x = −sinh x or ∫ sinh x dx = −cosh x by analogy with trigonometry. There is no minus sign.",
            "Forgetting the chain rule factor: d/dx arsinh(3x) = 3/√(1 + 9x²), not 1/√(1 + 9x²).",
            "Taking the wrong sign of the square root in a derivation, and not justifying the sign from the range.",
            "Confusing 1/√(1 − x²) (arcsin), 1/√(1 + x²) (arsinh) and 1/√(x² − 1) (arcosh), or 1/(1 + x²) (arctan) with 1/(1 − x²) (artanh).",
            "∫ sinh²x dx: using ½(1 − cosh 2x), which is the trigonometric sign pattern, gives the wrong sign.",
            "Leaving answers like cosh(ln 3) unevaluated: use the definitions to get exact numbers, cosh(ln 3) = 5/3.",
        ]),
    ],
    "examples": [
        {
            "title": "Deriving and using the derivative of arcsin",
            "question": "(a) Show that d/dx (arcsin x) = 1/√(1 − x²). (b) Differentiate arcsin x + x√(1 − x²), simplifying your answer.",
            "steps": [
                "(a) Let y = arcsin x, so sin y = x with −π/2 ≤ y ≤ π/2. Differentiating implicitly, cos y (dy/dx) = 1.",
                "On this range cos y ≥ 0, so cos y = √(1 − sin²y) = √(1 − x²). Hence dy/dx = 1/√(1 − x²).",
                "(b) By the product rule, d/dx[x√(1 − x²)] = √(1 − x²) + x × (−x)/√(1 − x²).",
                "Total derivative = 1/√(1 − x²) + √(1 − x²) − x²/√(1 − x²) = (1 + (1 − x²) − x²)/√(1 − x²).",
                "= 2(1 − x²)/√(1 − x²) = 2√(1 − x²).",
                "This shows ∫ 2√(1 − x²) dx = arcsin x + x√(1 − x²) + C, a result used again in unit B6.",
            ],
        },
        {
            "title": "Chain rule with inverse functions",
            "question": "Differentiate (a) artanh(x²), (b) arctan(3x), (c) arcosh(2x), x > ½, (d) ln(tanh x), x > 0, giving (d) in terms of a single hyperbolic function.",
            "steps": [
                "(a) d/dx artanh(x²) = 2x/(1 − (x²)²) = 2x/(1 − x⁴).",
                "(b) d/dx arctan(3x) = 3/(1 + 9x²).",
                "(c) d/dx arcosh(2x) = 2/√(4x² − 1).",
                "(d) d/dx ln(tanh x) = sech²x/tanh x = (1/cosh²x) × (cosh x/sinh x) = 1/(sinh x cosh x).",
                "Since sinh 2x = 2 sinh x cosh x, this is 2/sinh 2x = 2 cosech 2x.",
            ],
        },
        {
            "title": "Deriving the derivative of arcosh two ways",
            "question": "Show that d/dx (arcosh x) = 1/√(x² − 1) for x > 1 (a) by implicit differentiation, (b) from the logarithmic form.",
            "steps": [
                "(a) Let y = arcosh x, so cosh y = x and y ≥ 0. Then sinh y (dy/dx) = 1.",
                "sinh²y = cosh²y − 1 = x² − 1, and sinh y ≥ 0 because y ≥ 0. So sinh y = √(x² − 1) and dy/dx = 1/√(x² − 1).",
                "(b) y = ln(x + √(x² − 1)). By the chain rule, dy/dx = (1 + x/√(x² − 1))/(x + √(x² − 1)).",
                "The numerator is (√(x² − 1) + x)/√(x² − 1), so dy/dx = 1/√(x² − 1), as required.",
            ],
        },
        {
            "title": "Definite integrals of hyperbolic functions",
            "question": "Find the exact values of (a) ∫₀<sup>ln 2</sup> cosh²x dx, (b) ∫₀<sup>ln 3</sup> eˣ sinh x dx.",
            "steps": [
                "(a) cosh²x = ½(1 + cosh 2x), so the integral is [½x + ¼ sinh 2x] from 0 to ln 2.",
                "sinh(2 ln 2) = sinh(ln 4) = (4 − ¼)/2 = 15/8. So the value is ½ ln 2 + ¼ × 15/8 = ½ ln 2 + 15/32.",
                "(b) eˣ sinh x = eˣ × ½(eˣ − e⁻ˣ) = ½(e²ˣ − 1). The integral is [¼e²ˣ − ½x] from 0 to ln 3.",
                "= (¼ × 9 − ½ ln 3) − ¼ = 2 − ½ ln 3.",
            ],
        },
        {
            "title": "Integrating an inverse hyperbolic function by parts",
            "question": "(a) Find ∫ arsinh x dx. (b) Hence find the exact value of ∫₀<sup>3/4</sup> arsinh x dx.",
            "steps": [
                "(a) Write arsinh x = 1 × arsinh x. Take u = arsinh x, dv/dx = 1, so du/dx = 1/√(1 + x²) and v = x.",
                "∫ arsinh x dx = x arsinh x − ∫ x/√(1 + x²) dx = x arsinh x − √(1 + x²) + C.",
                "(b) At x = 3/4: arsinh(3/4) = ln(3/4 + 5/4) = ln 2 and √(1 + 9/16) = 5/4, giving (3/4) ln 2 − 5/4.",
                "At x = 0: 0 − 1 = −1. So the integral is (3/4) ln 2 − 5/4 + 1 = (3/4) ln 2 − ¼ ≈ 0.270.",
            ],
        },
        {
            "title": "Stationary point and area for a hyperbolic curve",
            "question": "The curve C has equation y = 5 cosh x − 3 sinh x. (a) Find the exact coordinates of the stationary point of C and "
                        "show that it is a minimum. (b) The region R is bounded by C, the coordinate axes and the line through the "
                        "stationary point parallel to the y-axis. Find the area of R.",
            "figure": "pb05_area.png",
            "caption": "y = 5 cosh x − 3 sinh x has a minimum at (ln 2, 4). R lies under the curve for 0 ≤ x ≤ ln 2.",
            "width_mm": 95,
            "steps": [
                "(a) dy/dx = 5 sinh x − 3 cosh x = 0 gives tanh x = 3/5.",
                "x = artanh(3/5) = ½ ln((8/5)/(2/5)) = ½ ln 4 = ln 2.",
                "cosh(ln 2) = 5/4, sinh(ln 2) = 3/4, so y = 25/4 − 9/4 = 4. The stationary point is (ln 2, 4).",
                "d²y/dx² = 5 cosh x − 3 sinh x = y = 4 > 0 there, so it is a minimum.",
                "(b) Area = ∫₀<sup>ln 2</sup> (5 cosh x − 3 sinh x) dx = [5 sinh x − 3 cosh x] from 0 to ln 2.",
                "= (15/4 − 15/4) − (0 − 3) = 3.",
            ],
        },
    ],
    "practice": [
        "Differentiate with respect to x: (a) sinh 4x, (b) cosh(x²), (c) tanh 3x.",
        "Differentiate with respect to x: (a) x² sinh x, (b) e²ˣ cosh x.",
        "Prove that d/dx (tanh x) = sech²x.",
        "(IAL, AQA, CAIE) Show that d/dx (sech x) = −sech x tanh x and d/dx (coth x) = −cosech²x.",
        "Show that d/dx (arccos x) = −1/√(1 − x²), justifying the sign of the square root.",
        "Differentiate (a) arcsin 2x, (b) arctan(x/3), (c) arccos(x²).",
        "Differentiate (a) arsinh 3x, (b) arcosh(x²) for x > 1, (c) artanh 2x for |x| < ½.",
        "By differentiating ln(x + √(x² + 1)), prove that d/dx (arsinh x) = 1/√(x² + 1).",
        "Find (a) ∫ cosh 3x dx, (b) ∫ sinh(x/2) dx, (c) ∫ sech²2x dx, (d) ∫ tanh x dx.",
        "Find the exact value of ∫₀<sup>ln 3</sup> sinh x dx.",
        "Find ∫ sinh³x dx.",
        "Find the exact value of ∫₀<sup>1/2</sup> arcsin x dx.",
    ],
    "answers": [
        "(a) 4 cosh 4x. (b) 2x sinh(x²). (c) 3 sech²3x.",
        "(a) 2x sinh x + x² cosh x. (b) e²ˣ(2 cosh x + sinh x).",
        "d/dx(sinh x/cosh x) = (cosh²x − sinh²x)/cosh²x = 1/cosh²x = sech²x.",
        "sech x = (cosh x)⁻¹, so the derivative is −(cosh x)⁻² sinh x = −(1/cosh x)(sinh x/cosh x) = −sech x tanh x. "
        "coth x = cosh x/sinh x: (sinh²x − cosh²x)/sinh²x = −1/sinh²x = −cosech²x.",
        "cos y = x, so −sin y (dy/dx) = 1. For 0 ≤ y ≤ π, sin y ≥ 0, so sin y = √(1 − x²) and dy/dx = −1/√(1 − x²).",
        "(a) 2/√(1 − 4x²). (b) 3/(9 + x²). (c) −2x/√(1 − x⁴).",
        "(a) 3/√(1 + 9x²). (b) 2x/√(x⁴ − 1). (c) 2/(1 − 4x²).",
        "d/dx ln(x + √(x² + 1)) = (1 + x/√(x² + 1))/(x + √(x² + 1)) = ((√(x² + 1) + x)/√(x² + 1))/(x + √(x² + 1)) = 1/√(x² + 1).",
        "(a) ⅓ sinh 3x + C. (b) 2 cosh(x/2) + C. (c) ½ tanh 2x + C. (d) ln cosh x + C.",
        "[cosh x] from 0 to ln 3 = 5/3 − 1 = 2/3.",
        "sinh³x = sinh x(cosh²x − 1), so ∫ sinh³x dx = ⅓ cosh³x − cosh x + C.",
        "∫ arcsin x dx = x arcsin x + √(1 − x²) + C (by parts). Value = (½)(π/6) + √3/2 − 1 = π/12 + √3/2 − 1 ≈ 0.128.",
    ],
    "exam": [
        "(a) Given that y = arctan x, show that dy/dx = 1/(1 + x²). [3]\n"
        "(b) Given that f(x) = x arctan x − ½ ln(1 + x²), show that f′(x) = arctan x. [2]\n"
        "(c) Hence find the exact value of ∫₀<sup>√3</sup> arctan x dx. [3]",

        "Let y = (arsinh x)².\n"
        "(a) Show that (1 + x²)(dy/dx)² = 4y. [3]\n"
        "(b) Hence show that (1 + x²)(d²y/dx²) + x(dy/dx) = 2. [4]\n"
        "(c) Find the Maclaurin series of y up to and including the term in x⁴. [4]",

        "(a) Prove that d/dx (artanh x) = 1/(1 − x²) for |x| < 1. [3]\n"
        "(b) Show that d/dx [artanh(sin x)] = sec x for −π/2 < x < π/2, and hence show that ∫₀<sup>π/6</sup> sec x dx = ½ ln 3. [4]\n"
        "(c) Show that d/dx [x√(x² + 1) + arsinh x] = 2√(x² + 1). [3]\n"
        "(d) Hence find the exact value of ∫₀¹ √(x² + 1) dx. [2]",

        "(a) Show that ∫₀<sup>ln 3</sup> tanh x dx = ln(5/3). [3]\n"
        "(b) Show that ∫ sinh²x dx = ¼ sinh 2x − ½x + C. [3]\n"
        "(c) The region bounded by y = sinh x, the x-axis and the line x = ln 3 is rotated through 2π radians about the x-axis. "
        "Find the exact volume of the solid formed. [4]",
    ],
    "exam_answers": [
        "(a) tan y = x M1; sec²y (dy/dx) = 1 M1; sec²y = 1 + tan²y = 1 + x², so dy/dx = 1/(1 + x²) A1.\n"
        "(b) f′(x) = arctan x + x/(1 + x²) − ½ × 2x/(1 + x²) M1 = arctan x A1.\n"
        "(c) [x arctan x − ½ ln(1 + x²)] from 0 to √3 M1 = √3 × π/3 − ½ ln 4 A1 = π√3/3 − ln 2 A1 (≈ 1.12).",

        "(a) dy/dx = 2 arsinh x × 1/√(1 + x²) M1 A1; squaring, (1 + x²)(dy/dx)² = 4(arsinh x)² = 4y A1.\n"
        "(b) Differentiate (a): 2x(dy/dx)² + (1 + x²) × 2(dy/dx)(d²y/dx²) = 4(dy/dx) M1 A1; divide by 2(dy/dx) (non-zero for x ≠ 0, "
        "and the result extends by continuity) M1, giving (1 + x²)y″ + xy′ = 2 A1. "
        "(Alternatively: √(1 + x²) y′ = 2 arsinh x, then differentiate.)\n"
        "(c) y(0) = 0, y′(0) = 0, y″(0) = 2 B1. Differentiating again: (1 + x²)y‴ + 3xy″ + y′ = 0, so y‴(0) = 0 M1; "
        "(1 + x²)y⁗ + 5xy‴ + 4y″ = 0, so y⁗(0) = −8 A1. y ≈ x² − x⁴/3 A1.",

        "(a) tanh y = x M1; sech²y (dy/dx) = 1 and sech²y = 1 − tanh²y = 1 − x² M1, so dy/dx = 1/(1 − x²) A1.\n"
        "(b) d/dx artanh(sin x) = cos x/(1 − sin²x) M1 = cos x/cos²x = sec x A1. "
        "∫₀<sup>π/6</sup> sec x dx = artanh(sin(π/6)) − artanh 0 M1 = artanh(½) = ½ ln((3/2)/(1/2)) = ½ ln 3 A1.\n"
        "(c) √(x² + 1) + x²/√(x² + 1) + 1/√(x² + 1) M1 A1 = (x² + 1 + x² + 1)/√(x² + 1) = 2√(x² + 1) A1.\n"
        "(d) ½[x√(x² + 1) + arsinh x] from 0 to 1 M1 = ½(√2 + ln(1 + √2)) A1 (≈ 1.15).",

        "(a) [ln cosh x] from 0 to ln 3 M1; cosh(ln 3) = 5/3 B1; ln(5/3) − ln 1 = ln(5/3) A1.\n"
        "(b) sinh²x = ½(cosh 2x − 1) M1 A1; integrate: ¼ sinh 2x − ½x + C A1.\n"
        "(c) V = π∫₀<sup>ln 3</sup> sinh²x dx M1 = π[¼ sinh 2x − ½x] from 0 to ln 3 M1; sinh(2 ln 3) = (9 − 1/9)/2 = 40/9 B1; "
        "V = π(10/9 − ½ ln 3) A1 (≈ 1.765).",
    ],
}
