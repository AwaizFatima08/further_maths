UNIT = {
    "number": "B4",
    "title": "Hyperbolic functions",
    "tag": "A2 Core Pure · Edexcel CP 8.1, 8.3, 8.4 · IAL FP3 1.1, 1.2 · AQA H1, H3, H4, H6 (AS, narrower), H7 (A level) · "
           "OCR A 4.07a, b, c, e, f · OCR MEI Pa3, Pa4, Pa6, Pa7 · CAIE 9231 P2 2.1",
    "notes": [
        ("h2", "4.1 Definitions"),
        ("p", "The <b>hyperbolic functions</b> are built from eˣ and e⁻ˣ. They behave so much like sin, cos and tan that they "
              "share their names, with an h for <i>hyperbolic</i>: sinh is said “shine” or “sinch”, cosh “cosh” and tanh "
              "“than” or “tanch”. Every board requires you to know these definitions without being given them."),
        ("box", "Definitions (learn these: they are on the must-know list of Edexcel, AQA, OCR A and MEI)", [
            "sinh x = (eˣ − e⁻ˣ)/2;   cosh x = (eˣ + e⁻ˣ)/2",
            "tanh x = sinh x / cosh x = (eˣ − e⁻ˣ)/(eˣ + e⁻ˣ) = (e²ˣ − 1)/(e²ˣ + 1)",
            "sinh 0 = 0, cosh 0 = 1, tanh 0 = 0.   cosh is even: cosh(−x) = cosh x.   sinh and tanh are odd: sinh(−x) = −sinh x.",
            "Adding and subtracting the definitions: cosh x + sinh x = eˣ and cosh x − sinh x = e⁻ˣ.",
        ]),
        ("p", "The name comes from the hyperbola. Just as (cos t, sin t) lies on the circle x² + y² = 1, the point (cosh t, sinh t) "
              "lies on the right-hand branch of the hyperbola x² − y² = 1, because cosh²t − sinh²t = 1 (section 4.4) and cosh t > 0."),
        ("figure", "pb04_hyperbola.png", "The point (cosh t, sinh t) traces the right-hand branch of x² − y² = 1 as t runs through all real values.", 95),
        ("h2", "4.2 Graphs, domains and ranges"),
        ("p", "For large positive x, e⁻ˣ is tiny, so both cosh x and sinh x are close to ½eˣ. For large negative x, cosh x ≈ ½e⁻ˣ "
              "and sinh x ≈ −½e⁻ˣ. Sketch the exponential guide curves lightly first, then draw cosh and sinh hugging them. "
              "Because cosh x − sinh x = e⁻ˣ > 0, the graph of cosh always lies above the graph of sinh. As x → ±∞, "
              "tanh x = (1 − e⁻²ˣ)/(1 + e⁻²ˣ) → 1 and tanh x → −1, so y = ±1 are horizontal asymptotes."),
        ("figure", "pb04_basic.png", "y = cosh x (minimum (0, 1)), y = sinh x (odd, through O with gradient 1) and y = tanh x (asymptotes y = ±1). "
                                     "The dotted curves are y = ½eˣ, y = ½e⁻ˣ and y = −½e⁻ˣ.", 115),
        ("table", ["Function", "Domain", "Range", "Key features"], [
            ["sinh x", "all real x", "all real y", "odd; increasing; gradient 1 at O"],
            ["cosh x", "all real x", "y ≥ 1", "even; minimum point (0, 1); U-shaped (a catenary)"],
            ["tanh x", "all real x", "−1 < y < 1", "odd; increasing; asymptotes y = ±1; gradient 1 at O"],
            ["sech x = 1/cosh x", "all real x", "0 < y ≤ 1", "even; maximum (0, 1); asymptote y = 0"],
            ["cosech x = 1/sinh x", "x ≠ 0", "y ≠ 0", "odd; asymptotes x = 0 and y = 0"],
            ["coth x = 1/tanh x", "x ≠ 0", "y < −1 or y > 1", "odd; asymptotes x = 0 and y = ±1"],
        ]),
        ("h2", "4.3 The reciprocal functions (IAL FP3, AQA A level, CAIE)"),
        ("p", "sech x = 1/cosh x, cosech x = 1/sinh x and coth x = 1/tanh x = cosh x/sinh x. Edexcel 9FM0, OCR A and MEI use only "
              "sinh, cosh and tanh, but IAL FP3, AQA (A level, H1) and Cambridge 9231 need all six, including their domains, ranges and "
              "graphs. Sketch a reciprocal graph from the original: where cosh x is large, sech x is small; where sinh x = 0, cosech x "
              "has a vertical asymptote."),
        ("figure", "pb04_reciprocal.png", "y = sech x, y = cosech x and y = coth x.", 105),
        ("h2", "4.4 Identities and their proofs"),
        ("p", "Every hyperbolic identity can be proved straight from the exponential definitions. The basic one is "
              "cosh²x − sinh²x ≡ 1, which every board requires:"),
        ("p", "cosh²x − sinh²x = ¼(e²ˣ + 2 + e⁻²ˣ) − ¼(e²ˣ − 2 + e⁻²ˣ) = ¼ × 4 = 1."),
        ("p", "<b>Osborn's rule</b> turns a trigonometric identity into the matching hyperbolic one: replace each trig function by "
              "its hyperbolic version, and change the sign of every term that contains a product (or implied product) of two sines. "
              "So cos²x + sin²x ≡ 1 becomes cosh²x − sinh²x ≡ 1, and cos 2x ≡ 1 − 2 sin²x becomes cosh 2x ≡ 1 + 2 sinh²x. "
              "tan²x contains sin²x, so 1 + tan²x ≡ sec²x becomes 1 − tanh²x ≡ sech²x. Osborn's rule is a way to <i>guess</i> an "
              "identity; it is not a proof. When a question says “prove” or “using the definitions”, work from exponentials."),
        ("box", "Hyperbolic identities", [
            "cosh²x − sinh²x ≡ 1;   sech²x ≡ 1 − tanh²x;   cosech²x ≡ coth²x − 1",
            "sinh 2x ≡ 2 sinh x cosh x;   cosh 2x ≡ cosh²x + sinh²x ≡ 2cosh²x − 1 ≡ 1 + 2sinh²x",
            "sinh(A ± B) ≡ sinh A cosh B ± cosh A sinh B",
            "cosh(A ± B) ≡ cosh A cosh B ± sinh A sinh B   (compare cos(A ± B) ≡ cos A cos B ∓ sin A sin B)",
            "tanh 2x ≡ 2 tanh x/(1 + tanh²x);   cosh 3x ≡ 4cosh³x − 3cosh x;   sinh 3x ≡ 3 sinh x + 4 sinh³x",
        ]),
        ("p", "<b>Which identities does your board use?</b> AQA AS needs only tanh x ≡ sinh x/cosh x and cosh²x − sinh²x ≡ 1; "
              "AQA A level adds the rest of the first two lines (H6) and proofs (H7). OCR A (4.07c) and MEI (Pa4) list only "
              "cosh²x − sinh²x ≡ 1: any other identity will be given or must be proved in the question. Edexcel and IAL print "
              "cosh²x − sinh²x, sinh 2x and cosh 2x in the booklet; Cambridge (2.1) expects you to prove and use identities that "
              "mirror the trigonometric ones."),
        ("p", "<b>How to set out a proof.</b> Start with one side, usually the more complicated one, replace each function by its "
              "exponential form, simplify, and finish at the other side. Cambridge examiners ask candidates to “work on just one "
              "side at a time” rather than manipulating an equation whose truth is not yet known."),
        ("h2", "4.5 Solving hyperbolic equations"),
        ("p", "There are two standard methods."),
        ("bullets", [
            "<b>Exponential method.</b> For a cosh x + b sinh x = c, substitute the definitions, multiply by 2eˣ and you get a "
            "quadratic in u = eˣ: (a + b)u² − 2cu + (a − b) = 0. Reject any root u ≤ 0, because eˣ > 0. Then x = ln u.",
            "<b>Identity method.</b> When the equation mixes cosh² and sinh (or sinh² and cosh, or cosh 2x and cosh x), use "
            "cosh²x − sinh²x ≡ 1 or a double-angle identity to get a quadratic in one function. Reject cosh x < 1 (impossible). "
            "Then use the logarithmic forms of section 4.7: sinh x = k has the single solution x = ln(k + √(k² + 1)), while "
            "cosh x = k (k > 1) has <b>two</b> solutions, x = ±ln(k + √(k² − 1)).",
            "<b>Harmonic form (useful extension).</b> If a > |b| > 0, then a cosh x + b sinh x ≡ R cosh(x + α) with R = √(a² − b²) "
            "and tanh α = b/a. This gives the minimum value R immediately (at x = −α). Expand R cosh(x + α) and compare "
            "coefficients: R cosh α = a and R sinh α = b.",
        ]),
        ("h2", "4.6 Inverse hyperbolic functions"),
        ("p", "sinh and tanh are one-to-one, so they have inverses on their whole domains. cosh is not one-to-one (cosh(−x) = cosh x), "
              "so, as with arccos, we restrict it to x ≥ 0 before inverting. The inverses are written arsinh, arcosh and artanh "
              "(“ar” for area, because the inverse gives an area linked to the hyperbola); sinh⁻¹, cosh⁻¹ and tanh⁻¹ mean the same "
              "thing and are used by OCR and Cambridge. Their graphs are the reflections of the original graphs in y = x."),
        ("table", ["Inverse function", "Domain", "Range", "Logarithmic form"], [
            ["arsinh x", "all real x", "all real y", "ln(x + √(x² + 1))"],
            ["arcosh x", "x ≥ 1", "y ≥ 0 (principal value)", "ln(x + √(x² − 1))"],
            ["artanh x", "−1 < x < 1", "all real y", "½ ln((1 + x)/(1 − x))"],
        ]),
        ("figure", "pb04_inverse.png", "y = arsinh x, y = arcosh x (starting at (1, 0)) and y = artanh x (asymptotes x = ±1).", 105),
        ("p", "IAL FP3 and AQA also mention the inverses of the reciprocal functions. These follow the same pattern: for example "
              "arsech x = arcosh(1/x) for 0 < x ≤ 1, arcoth x = artanh(1/x) for |x| > 1."),
        ("h2", "4.7 Deriving the logarithmic forms"),
        ("p", "Every board requires you to <b>derive</b> these, even where the booklet prints them. The method is always the same: "
              "write x = sinh y (or cosh y, tanh y), replace by exponentials, solve a quadratic in eʸ, and choose the right root."),
        ("p", "<b>arsinh.</b> Let y = arsinh x, so x = sinh y = (eʸ − e⁻ʸ)/2. Multiply by 2eʸ: e²ʸ − 2xeʸ − 1 = 0. "
              "So eʸ = x ± √(x² + 1). Since √(x² + 1) > |x|, the root x − √(x² + 1) is negative, which is impossible for eʸ. "
              "Hence eʸ = x + √(x² + 1) and arsinh x = ln(x + √(x² + 1)) for all real x."),
        ("p", "<b>arcosh.</b> Let y = arcosh x with x ≥ 1 and y ≥ 0. Then e²ʸ − 2xeʸ + 1 = 0, so eʸ = x ± √(x² − 1). Both roots "
              "are positive, and their product is 1, so their logarithms are ±ln(x + √(x² − 1)). The principal value y ≥ 0 needs "
              "eʸ ≥ 1, which is the larger root. Hence arcosh x = ln(x + √(x² − 1)), x ≥ 1."),
        ("p", "<b>artanh.</b> Let y = artanh x, |x| < 1. Then x = (e²ʸ − 1)/(e²ʸ + 1), so x e²ʸ + x = e²ʸ − 1 and "
              "e²ʸ = (1 + x)/(1 − x). Hence artanh x = ½ ln((1 + x)/(1 − x)) for −1 < x < 1."),
        ("box", "Given or learn? (by board)", [
            "Definitions of sinh, cosh, tanh: learn (must-know list for Edexcel, AQA, OCR A, MEI; not printed by IAL or Cambridge either).",
            "cosh²x − sinh²x, sinh 2x, cosh 2x and the three log forms: printed by Edexcel, IAL, AQA and Cambridge; OCR A and MEI print the log forms only.",
            "sech²x ≡ 1 − tanh²x, cosech²x ≡ coth²x − 1 and the definitions of sech, cosech, coth: learn (not printed anywhere).",
            "Even when a log form is printed, a question may say “show that” or “derive”: you must then produce the derivation.",
        ]),
        ("warn", "Common mistakes", [
            "Solving cosh x = k and giving only the positive root: cosh x = 2 has two solutions, x = ±ln(2 + √3).",
            "Keeping a root with cosh x < 1 or eˣ ≤ 0. State why it is rejected; examiners award a mark for doing so.",
            "Writing sinh x = (eˣ + e⁻ˣ)/2: the minus sign belongs to sinh (s for “subtract” is a useful memory aid).",
            "Applying Osborn's rule without the sign change, e.g. writing cosh²x + sinh²x ≡ 1.",
            "In proofs, writing the identity to be proved as the first line and working on both sides together.",
            "Forgetting the ½ in artanh x = ½ ln((1 + x)/(1 − x)), or squaring the wrong way round inside the logarithm.",
        ]),
    ],
    "examples": [
        {
            "title": "Proving identities from the definitions",
            "question": "Using the definitions of sinh x and cosh x, prove that (a) cosh 2x ≡ 1 + 2sinh²x, (b) sinh 3x ≡ 3 sinh x + 4 sinh³x.",
            "steps": [
                "(a) Start with the right-hand side. 1 + 2sinh²x = 1 + 2 × ¼(eˣ − e⁻ˣ)² = 1 + ½(e²ˣ − 2 + e⁻²ˣ).",
                "= 1 + ½e²ˣ − 1 + ½e⁻²ˣ = ½(e²ˣ + e⁻²ˣ) = cosh 2x, as required.",
                "(b) 4sinh³x = 4 × ⅛(eˣ − e⁻ˣ)³ = ½(e³ˣ − 3eˣ + 3e⁻ˣ − e⁻³ˣ), using the binomial expansion of (a − b)³.",
                "3 sinh x = (3/2)(eˣ − e⁻ˣ).",
                "Adding: 3 sinh x + 4sinh³x = ½e³ˣ − (3/2)eˣ + (3/2)e⁻ˣ − ½e⁻³ˣ + (3/2)eˣ − (3/2)e⁻ˣ = ½(e³ˣ − e⁻³ˣ) = sinh 3x, as required.",
                "Check with Osborn's rule: sin 3x ≡ 3 sin x − 4sin³x; sin³x contains a product of two sines, so its sign changes, which agrees.",
            ],
        },
        {
            "title": "Exact values from one given value",
            "question": "Given that sinh x = 3/4, find the exact values of cosh x, tanh x, sech x, coth x and cosh 2x, and show that x = ln 2.",
            "steps": [
                "cosh²x = 1 + sinh²x = 1 + 9/16 = 25/16. cosh x > 0 always, so cosh x = 5/4.",
                "tanh x = sinh x/cosh x = (3/4)/(5/4) = 3/5. sech x = 1/cosh x = 4/5. coth x = 1/tanh x = 5/3.",
                "cosh 2x = 1 + 2sinh²x = 1 + 2 × 9/16 = 17/8.",
                "x = arsinh(3/4) = ln(3/4 + √(9/16 + 1)) = ln(3/4 + 5/4) = ln 2.",
                "Check: cosh(ln 2) = (2 + ½)/2 = 5/4 and cosh(2 ln 2) = (4 + ¼)/2 = 17/8, as expected.",
            ],
        },
        {
            "title": "a cosh x + b sinh x = c by exponentials",
            "question": "Solve 5 cosh x − 3 sinh x = 5, giving exact answers.",
            "steps": [
                "Substitute the definitions: (5/2)(eˣ + e⁻ˣ) − (3/2)(eˣ − e⁻ˣ) = 5, so eˣ + 4e⁻ˣ = 5.",
                "Multiply by eˣ: e²ˣ − 5eˣ + 4 = 0, i.e. (eˣ − 1)(eˣ − 4) = 0.",
                "eˣ = 1 or eˣ = 4 (both positive, so both are valid).",
                "x = 0 or x = ln 4 = 2 ln 2.",
                "Check x = ln 4: cosh(ln 4) = 17/8, sinh(ln 4) = 15/8, and 5 × 17/8 − 3 × 15/8 = 40/8 = 5, which checks.",
            ],
        },
        {
            "title": "Using an identity to get a quadratic",
            "question": "Solve 2cosh²x − 5 sinh x = 5, giving your answers in logarithmic form.",
            "steps": [
                "Replace cosh²x by 1 + sinh²x: 2 + 2sinh²x − 5 sinh x − 5 = 0, so 2sinh²x − 5 sinh x − 3 = 0.",
                "Factorise: (2 sinh x + 1)(sinh x − 3) = 0, so sinh x = 3 or sinh x = −½.",
                "sinh is one-to-one, so each value gives exactly one x (no ± here, unlike cosh).",
                "sinh x = 3: x = arsinh 3 = ln(3 + √10).",
                "sinh x = −½: x = ln(−½ + √(¼ + 1)) = ln((√5 − 1)/2).",
                "Numerically x ≈ 1.818 and x ≈ −0.481 (3 s.f.).",
            ],
        },
        {
            "title": "Deriving and using the artanh form",
            "question": "(a) Show that artanh x = ½ ln((1 + x)/(1 − x)) for |x| < 1. (b) Hence solve 2 artanh x = ln 3. "
                        "(c) Show that artanh(1/3) + artanh(1/5) = artanh(1/2).",
            "steps": [
                "(a) Let y = artanh x, so x = tanh y = (e²ʸ − 1)/(e²ʸ + 1) (multiply top and bottom of the definition by eʸ).",
                "x e²ʸ + x = e²ʸ − 1, so e²ʸ(1 − x) = 1 + x and e²ʸ = (1 + x)/(1 − x). Since |x| < 1, this is positive.",
                "2y = ln((1 + x)/(1 − x)), so artanh x = ½ ln((1 + x)/(1 − x)), as required.",
                "(b) 2 artanh x = ln((1 + x)/(1 − x)) = ln 3, so 1 + x = 3 − 3x, giving x = ½ (which satisfies |x| < 1).",
                "(c) artanh(1/3) = ½ ln((4/3)/(2/3)) = ½ ln 2 and artanh(1/5) = ½ ln((6/5)/(4/5)) = ½ ln(3/2).",
                "Sum = ½ ln(2 × 3/2) = ½ ln 3. And artanh(1/2) = ½ ln((3/2)/(1/2)) = ½ ln 3, so the two sides are equal.",
            ],
        },
        {
            "title": "Harmonic form, minimum value and an equation",
            "question": "(a) Express 5 cosh x + 4 sinh x in the form R cosh(x + α), where R > 0, giving α as a logarithm. "
                        "(b) State the minimum value of 5 cosh x + 4 sinh x and the value of x where it occurs. "
                        "(c) Solve 5 cosh x + 4 sinh x = 5.",
            "figure": "pb04_rform.png",
            "caption": "y = 5 cosh x + 4 sinh x is a cosh curve with minimum (−ln 3, 3); it meets y = 5 at x = 0 and x = −2 ln 3.",
            "width_mm": 95,
            "steps": [
                "(a) R cosh(x + α) = R cosh α cosh x + R sinh α sinh x. Compare: R cosh α = 5 and R sinh α = 4.",
                "R² = R²cosh²α − R²sinh²α = 25 − 16 = 9, so R = 3. tanh α = 4/5, so α = artanh(4/5) = ½ ln((9/5)/(1/5)) = ½ ln 9 = ln 3.",
                "5 cosh x + 4 sinh x ≡ 3 cosh(x + ln 3).",
                "(b) cosh has minimum 1 when its argument is 0, so the minimum value is 3, when x = −ln 3.",
                "(c) 3 cosh(x + ln 3) = 5 gives cosh(x + ln 3) = 5/3, so x + ln 3 = ±arcosh(5/3) = ±ln(5/3 + 4/3) = ±ln 3.",
                "x = 0 or x = −2 ln 3 (= −ln 9).",
                "Check by exponentials: (9/2)eˣ + ½e⁻ˣ = 5 gives 9e²ˣ − 10eˣ + 1 = 0, so eˣ = 1 or 1/9, which agrees.",
            ],
        },
    ],
    "practice": [
        "Find the exact values of (a) cosh(ln 3), (b) sinh(ln 2), (c) tanh(ln 4).",
        "State the range of each function: (a) y = cosh x, (b) y = tanh x, (c) y = sech x, (d) y = coth x.",
        "Prove, using the definitions, that cosh²x − sinh²x ≡ 1.",
        "Prove, using the definitions, that sinh 2x ≡ 2 sinh x cosh x.",
        "(AQA, IAL, CAIE) Use cosh²x − sinh²x ≡ 1 to prove that sech²x ≡ 1 − tanh²x and that cosech²x ≡ coth²x − 1.",
        "Use Osborn's rule to write down the hyperbolic identity that corresponds to cos(A + B) ≡ cos A cos B − sin A sin B. "
        "Then prove it from the definitions.",
        "Given that cosh x = 13/5 and x < 0, find the exact values of sinh x and tanh x, and show that x = −ln 5.",
        "Solve 3 cosh x − sinh x = 3, giving exact answers.",
        "Solve cosh 2x = 5 cosh x − 3, giving exact answers in logarithmic form.",
        "Write in logarithmic form: (a) arsinh 2, (b) arcosh 2, (c) artanh(1/3).",
        "(a) Prove that arcosh x = ln(x + √(x² − 1)) for x ≥ 1. (b) Solve arcosh x = 2 ln(1 + √2). (c) Solve arsinh x = ln 3.",
        "Sketch, on the same axes, y = tanh x and y = coth x, showing the asymptotes. State the domain and range of y = artanh x.",
    ],
    "answers": [
        "(a) cosh(ln 3) = (3 + 1/3)/2 = 5/3. (b) sinh(ln 2) = (2 − ½)/2 = 3/4. (c) tanh(ln 4) = (16 − 1)/(16 + 1) = 15/17.",
        "(a) y ≥ 1. (b) −1 < y < 1. (c) 0 < y ≤ 1. (d) y < −1 or y > 1.",
        "cosh²x − sinh²x = ¼(e²ˣ + 2 + e⁻²ˣ) − ¼(e²ˣ − 2 + e⁻²ˣ) = ¼(4) = 1.",
        "2 sinh x cosh x = 2 × ½(eˣ − e⁻ˣ) × ½(eˣ + e⁻ˣ) = ½(e²ˣ − e⁻²ˣ) = sinh 2x.",
        "Divide cosh²x − sinh²x ≡ 1 by cosh²x: 1 − tanh²x ≡ sech²x. Divide by sinh²x: coth²x − 1 ≡ cosech²x.",
        "The term sin A sin B is a product of two sines, so its sign changes: cosh(A + B) ≡ cosh A cosh B + sinh A sinh B. "
        "Proof: cosh A cosh B + sinh A sinh B = ¼[(e^A + e^(−A))(e^B + e^(−B)) + (e^A − e^(−A))(e^B − e^(−B))] = ¼[2e^(A+B) + 2e^(−(A+B))] = cosh(A + B).",
        "sinh²x = (13/5)² − 1 = 144/25; x < 0 so sinh x = −12/5. tanh x = −12/13. "
        "x = −arcosh(13/5) = −ln(13/5 + 12/5) = −ln 5.",
        "(3/2)(eˣ + e⁻ˣ) − ½(eˣ − e⁻ˣ) = 3 gives eˣ + 2e⁻ˣ = 3, so e²ˣ − 3eˣ + 2 = 0, eˣ = 1 or 2: x = 0 or x = ln 2.",
        "2cosh²x − 1 = 5 cosh x − 3 gives 2cosh²x − 5 cosh x + 2 = 0, so cosh x = 2 or ½. cosh x ≥ 1 so reject ½. "
        "x = ±ln(2 + √3).",
        "(a) ln(2 + √5). (b) ln(2 + √3). (c) ½ ln((4/3)/(2/3)) = ½ ln 2.",
        "(a) Let y = arcosh x, y ≥ 0: x = (eʸ + e⁻ʸ)/2 gives e²ʸ − 2xeʸ + 1 = 0, eʸ = x ± √(x² − 1). The roots have product 1; "
        "y ≥ 0 needs eʸ ≥ 1, the larger root, so arcosh x = ln(x + √(x² − 1)). "
        "(b) x = cosh(2 ln(1 + √2)) = ½[(1 + √2)² + (1 + √2)⁻²] = ½[(3 + 2√2) + (3 − 2√2)] = 3. "
        "(c) x = sinh(ln 3) = (3 − 1/3)/2 = 4/3.",
        "tanh: through O, increasing, between the asymptotes y = ±1. coth: two branches, asymptotes x = 0 and y = ±1, above y = 1 "
        "for x > 0 and below y = −1 for x < 0. artanh: domain −1 < x < 1, range all real numbers.",
    ],
    "exam": [
        "(a) Using the definitions of cosh x and sinh x, prove that cosh 3x ≡ 4cosh³x − 3 cosh x. [4]\n"
        "(b) Hence solve the equation cosh 3x = 13 cosh x, giving your answers in the form ln(a + √b). [4]",

        "(a) Show that arsinh x = ln(x + √(x² + 1)). [3]\n"
        "(b) Solve 3sinh²x − 13 cosh x + 7 = 0, giving your answers as exact logarithms. [5]\n"
        "(c) Explain why the equation sinh x = k has exactly one real solution for every real k, but cosh x = k has none when k < 1. [2]",

        "(a) Express 13 cosh x + 5 sinh x in the form R cosh(x + α), where R > 0 and α is an exact logarithm. [4]\n"
        "(b) Write down the minimum value of 13 cosh x + 5 sinh x and the exact value of x at which it occurs. [2]\n"
        "(c) Solve 13 cosh x + 5 sinh x = 20, giving exact answers. [4]",

        "(a) Sketch the graph of y = artanh x, stating the equations of its asymptotes. [2]\n"
        "(b) Prove that artanh x = ½ ln((1 + x)/(1 − x)) for −1 < x < 1. [4]\n"
        "(c) Solve artanh x = arsinh(3/4). [3]\n"
        "(d) Show that sech(ln 3) = 3/5 and hence write down, as a fraction, the value of tanh(ln 3). [3]",
    ],
    "exam_answers": [
        "(a) 4cosh³x = 4 × ⅛(eˣ + e⁻ˣ)³ = ½(e³ˣ + 3eˣ + 3e⁻ˣ + e⁻³ˣ) M1 A1; subtract 3 cosh x = (3/2)(eˣ + e⁻ˣ) M1; "
        "= ½(e³ˣ + e⁻³ˣ) = cosh 3x A1.\n"
        "(b) 4cosh³x − 3 cosh x = 13 cosh x gives 4 cosh x(cosh²x − 4) = 0 M1. cosh x ≠ 0 (cosh x ≥ 1) and cosh x ≠ −2, "
        "so cosh x = 2 A1. x = ±ln(2 + √3) M1 A1 (both signs needed).",

        "(a) e²ʸ − 2xeʸ − 1 = 0 from x = sinh y M1; eʸ = x ± √(x² + 1) A1; reject the negative root since eʸ > 0, "
        "so arsinh x = ln(x + √(x² + 1)) A1.\n"
        "(b) 3(cosh²x − 1) − 13 cosh x + 7 = 0 M1, so 3cosh²x − 13 cosh x + 4 = 0 A1, (3 cosh x − 1)(cosh x − 4) = 0 M1. "
        "cosh x = 1/3 rejected (cosh x ≥ 1) A1; cosh x = 4 gives x = ±ln(4 + √15) A1.\n"
        "(c) sinh is continuous, increasing and its range is all real numbers, so it takes each value exactly once B1. "
        "The range of cosh is y ≥ 1, so cosh x = k has no solution for k < 1 B1.",

        "(a) R cosh α = 13, R sinh α = 5 M1; R² = 169 − 25 = 144, R = 12 A1; tanh α = 5/13 M1, "
        "α = ½ ln((18/13)/(8/13)) = ½ ln(9/4) = ln(3/2) A1. So 13 cosh x + 5 sinh x ≡ 12 cosh(x + ln(3/2)).\n"
        "(b) Minimum 12 B1, at x = −ln(3/2) B1.\n"
        "(c) cosh(x + ln(3/2)) = 5/3 M1, x + ln(3/2) = ±ln 3 A1, x = ln 2 A1 or x = −ln(9/2) A1. "
        "(Check: 9e²ˣ − 20eˣ + 4 = 0 gives eˣ = 2 or 2/9.)",

        "(a) Increasing curve through O, gradient 1 there, odd, vertical asymptotes x = 1 and x = −1 B1 B1.\n"
        "(b) x = tanh y = (e²ʸ − 1)/(e²ʸ + 1) M1; e²ʸ(1 − x) = 1 + x M1 A1; y = ½ ln((1 + x)/(1 − x)) A1.\n"
        "(c) arsinh(3/4) = ln(3/4 + 5/4) = ln 2 B1. ½ ln((1 + x)/(1 − x)) = ln 2 gives (1 + x)/(1 − x) = 4 M1, x = 3/5 A1.\n"
        "(d) cosh(ln 3) = (3 + 1/3)/2 = 5/3 M1, so sech(ln 3) = 3/5 A1. tanh²(ln 3) = 1 − 9/25 = 16/25 and ln 3 > 0, "
        "so tanh(ln 3) = 4/5 B1.",
    ],
}
