UNIT = {
    "number": "A1",
    "title": "Complex numbers I: arithmetic and complex roots",
    "tag": "AS · Edexcel CP 2.1–2.3 · IAL FP1 1.1, 1.4–1.6 · AQA B1–B3 (AS) · OCR A 4.02a, c, g, h, i, j (AS) · "
           "OCR MEI Pj1–Pj5 (AS) · CAIE 9231: assumed from 9709 P3 (revise it here)",
    "notes": [
        ("p", "Some quadratic equations, such as x² + 1 = 0, have no real solutions, because the square of a real number is never "
              "negative. Mathematicians extend the real numbers by adding one new number, i, whose square is −1. Every polynomial "
              "equation then has a full set of roots. This unit sets up the arithmetic of these <b>complex numbers</b> and uses it "
              "to solve quadratic, cubic and quartic equations with real coefficients. Unit A2 adds the geometry."),

        ("h2", "1.1 The language of complex numbers (OCR A 4.02a, 4.02c; MEI Pj1)"),
        ("p", "The <b>imaginary unit</b> i is defined by i² = −1. A <b>complex number</b> is a number of the form z = x + iy (also "
              "written x + yi), where x and y are real. The set of all complex numbers is written ℂ; the real numbers ℝ are the "
              "complex numbers with y = 0."),
        ("box", "Definitions and notation", [
            "z = x + iy, with x, y ∈ ℝ. This is the <b>Cartesian form</b> (or algebraic form).",
            "Re(z) = x is the <b>real part</b>; Im(z) = y is the <b>imaginary part</b>. Note that Im(z) is the real number y, not iy.",
            "If y = 0, z is <b>real</b>. If x = 0 and y ≠ 0, z is <b>purely imaginary</b>. If y ≠ 0, z is <b>non-real</b>.",
            "The <b>complex conjugate</b> of z = x + iy is z* = x − iy (some books write it as z with a bar over it).",
            "Square roots of negative numbers: √(−k) = i√k for k > 0, so √(−9) = 3i and √(−12) = 2√3 i.",
        ]),
        ("p", "<b>Powers of i.</b> Because i² = −1, the powers of i repeat in a cycle of four: i¹ = i, i² = −1, i³ = −i, i⁴ = 1, "
              "i⁵ = i, and so on. To find iⁿ, divide n by 4 and use the remainder: i¹⁰ = i⁸ × i² = −1, i²³ = i²⁰ × i³ = −i. "
              "Also 1/i = −i, because i × (−i) = −i² = 1."),

        ("h2", "1.2 Equality of complex numbers (OCR A 4.02c; MEI Pj5)"),
        ("p", "Two complex numbers are equal exactly when their real parts are equal <b>and</b> their imaginary parts are equal. In "
              "particular, a complex number is zero if and only if both its real and imaginary parts are zero. The reason is that "
              "if a + ib = 0 with b ≠ 0, then i = −a/b would be real, which is impossible because no real number squares to −1."),
        ("box", "Equating real and imaginary parts", [
            "a + ib = c + id  ⇔  a = c and b = d   (a, b, c, d real).",
            "One complex equation gives <b>two</b> real equations. This is how you find unknown real numbers x and y, and how you "
            "find square roots (section 1.5).",
        ]),

        ("h2", "1.3 Adding, subtracting, multiplying and dividing (Edexcel 2.2; AQA B2; MEI Pj4)"),
        ("p", "Complex numbers obey the usual rules of algebra (commutative, associative and distributive laws), with i² replaced "
              "by −1 wherever it appears."),
        ("bullets", [
            "Add or subtract real parts and imaginary parts separately: (3 + 2i) + (1 − 5i) = 4 − 3i.",
            "Multiply by expanding brackets: (3 + 2i)(1 − 5i) = 3 − 15i + 2i − 10i² = 3 − 13i + 10 = 13 − 13i.",
            "Divide by multiplying top and bottom by the <b>conjugate of the denominator</b>. This makes the denominator real, "
            "because (c + id)(c − id) = c² + d².",
        ]),
        ("box", "Division", [
            "(a + ib)/(c + id) = (a + ib)(c − id)/((c + id)(c − id)) = [(ac + bd) + i(bc − ad)]/(c² + d²).",
            "Do not learn this formula: learn the method (“realise the denominator”). Always give the answer in the form x + iy.",
        ]),
        ("p", "Every non-zero complex number has a reciprocal, so you can divide by any complex number except 0. A calculator in "
              "complex mode (CMPLX) does this arithmetic, but exam questions often say “show that” or ask for exact answers, so "
              "set out the working."),

        ("h2", "1.4 The complex conjugate (Edexcel 2.3; AQA B3; OCR A 4.02a)"),
        ("p", "For z = x + iy, the conjugate is z* = x − iy. The conjugate has several useful properties. Each follows by writing "
              "z = x + iy and w = u + iv and expanding."),
        ("box", "Properties of the conjugate", [
            "z + z* = 2x = 2 Re(z) is real;  z − z* = 2iy = 2i Im(z) is purely imaginary (or zero).",
            "zz* = (x + iy)(x − iy) = x² + y², which is real and ≥ 0. (Unit A2 calls √(x² + y²) the modulus |z|, so zz* = |z|².)",
            "(z + w)* = z* + w*,  (zw)* = z*w*,  (z/w)* = z*/w*,  (z*)* = z.",
            "Hence (zⁿ)* = (z*)ⁿ for every positive integer n, and (kz)* = kz* for real k.",
            "z is real ⇔ z* = z;  z is purely imaginary or zero ⇔ z* = −z.",
        ]),
        ("p", "<b>Proof that (zw)* = z*w*.</b> zw = (x + iy)(u + iv) = (xu − yv) + i(xv + yu), so (zw)* = (xu − yv) − i(xv + yu). "
              "Also z*w* = (x − iy)(u − iv) = (xu − yv) − i(xv + yu). These are equal."),

        ("h2", "1.5 Square roots of a complex number (OCR A 4.02h; all boards use it)"),
        ("p", "Every non-zero complex number w has exactly two square roots, and they are negatives of each other. To find them "
              "algebraically, write the root as a + ib with a, b real, square it and equate real and imaginary parts."),
        ("box", "Method: square roots of w = p + iq", [
            "Set (a + ib)² = p + iq. Then a² − b² = p and 2ab = q.",
            "Substitute b = q/(2a) into the first equation to get a quadratic in a²: a⁴ − pa² − q²/4 = 0.",
            "Take the positive value of a² (a is real, so a² ≥ 0), find a = ±…, then b = q/(2a).",
            "Check: a² + b² must equal √(p² + q²). The two roots are ±(a + ib).",
        ]),
        ("p", "Square roots let you solve quadratic equations whose coefficients are themselves complex (an OCR A and MEI "
              "extension): use the quadratic formula and find the square root of the complex discriminant. Worked example A1.3 "
              "shows this. Unit B2 gives a faster method for square roots and higher roots using modulus–argument form."),

        ("h2", "1.6 Quadratic equations with real coefficients (Edexcel 2.1; AQA B1; OCR A 4.02i; MEI Pj2; IAL 1.4)"),
        ("p", "For az² + bz + c = 0 with a, b, c real, the quadratic formula still works. If the discriminant Δ = b² − 4ac is "
              "negative, then √Δ = i√(4ac − b²) and the roots are a pair of complex conjugates."),
        ("box", "Real quadratics", [
            "z = (−b ± √(b² − 4ac))/(2a). If b² − 4ac < 0: z = −b/(2a) ± i√(4ac − b²)/(2a), a conjugate pair p ± iq.",
            "Quadratic with roots p ± iq: (z − p)² + q² = 0, i.e. z² − 2pz + (p² + q²) = 0.",
            "Sum of roots = 2p = 2 Re(α); product = p² + q² = αα* (for the conjugate pair α, α*).",
        ]),
        ("p", "Completing the square gives the same roots and is often quicker: z² − 4z + 13 = 0 ⇒ (z − 2)² = −9 ⇒ z − 2 = ±3i ⇒ "
              "z = 2 ± 3i."),

        ("h2", "1.7 Conjugate pairs for real polynomials (Edexcel 2.3; AQA B3; OCR A 4.02g; MEI Pj3)"),
        ("box", "The conjugate root theorem", [
            "If f(z) is a polynomial with <b>real</b> coefficients and f(α) = 0, then f(α*) = 0.",
            "So non-real roots of a real polynomial occur in conjugate pairs α, α*, and (z − α)(z − α*) = z² − 2Re(α)z + αα* is "
            "a quadratic factor with real coefficients.",
        ]),
        ("p", "<b>Proof.</b> Let f(z) = aₙzⁿ + … + a₁z + a₀ with every aᵣ real. Using the properties in section 1.4, "
              "(f(α))* = aₙ*(α*)ⁿ + … + a₁*α* + a₀* = aₙ(α*)ⁿ + … + a₁α* + a₀ = f(α*), because aᵣ* = aᵣ for a real number. If "
              "f(α) = 0 then f(α*) = 0* = 0."),
        ("p", "Two consequences. First, a real cubic has either three real roots, or one real root and one conjugate pair, so it "
              "always has <b>at least one real root</b> (its graph must cross the x-axis). Second, a real quartic has four real "
              "roots, two real roots and one conjugate pair, or two conjugate pairs. The theorem is false if any coefficient is "
              "non-real: z² − iz = 0 has roots 0 and i, but not −i."),
        ("figure", "pa01_cubic.png",
         "The graph of y = x³ − 6x² + 21x − 26 crosses the x-axis once, at x = 2. The other two roots, 2 ± 3i, are not real, "
         "so they do not appear on the graph (worked example A1.4).", 95),

        ("h2", "1.8 Solving cubic and quartic equations (Edexcel 2.1; AQA B1; OCR A 4.02j; MEI Pj3; IAL 1.5, 1.6)"),
        ("p", "Exam questions give enough information to find one root or one quadratic factor. Use the factor theorem: if f(α) = 0 "
              "then (z − α) is a factor. The strategy depends on what you are given."),
        ("table", ["You are given…", "Method"], [
            ["a real root, or a linear factor (z − k)", "Divide f(z) by (z − k) (or compare coefficients) to get a quadratic factor; "
             "solve it."],
            ["one non-real root α of a real cubic", "α* is also a root. Form the quadratic factor z² − 2Re(α)z + αα*. The third root "
             "is real: find it by comparing constant terms (or the z² terms)."],
            ["one non-real root α of a real quartic", "Form the quadratic factor from α and α*. Divide (or compare coefficients) to "
             "get a second quadratic factor; solve it."],
            ["a root α, but unknown coefficients", "Either substitute α and equate real and imaginary parts, or write "
             "f(z) = (quadratic factor)(z − k) and compare coefficients."],
        ]),
        ("p", "<b>Comparing coefficients</b> is usually faster than long division. For example, if z² − 2z + 5 is a factor of "
              "z³ + z² − z + 15, write z³ + z² − z + 15 = (z² − 2z + 5)(z + k). The constant terms give 5k = 15, so k = 3, and "
              "the z² terms check: −2 + k = 1. The real root is −3."),
        ("p", "<b>Calculator use.</b> Polynomial solvers will find roots of cubics and quartics, and are useful for checking. If a "
              "question says “show that” or “hence”, you must show the algebra; a list of calculator roots earns little credit."),

        ("warn", "Common mistakes", [
            "Writing i² = 1, or forgetting to replace i² by −1 when multiplying out. Check every product term by term.",
            "Dividing by multiplying by the conjugate of the <b>numerator</b>, or only multiplying the denominator. Multiply top and "
            "bottom by the conjugate of the denominator.",
            "Giving Im(3 − 4i) as −4i. The imaginary part is the real number −4.",
            "Finding only one square root, or rejecting the solution a² < 0 too late. There are always two roots ±(a + ib).",
            "Using the conjugate root theorem when some coefficients are non-real. It needs <b>real</b> coefficients.",
            "Stopping too early: “solve the cubic” means give all three roots, including the real one.",
            "Sign slips in the quadratic factor: the roots 2 ± 3i give z² − 4z + 13, not z² + 4z + 13.",
        ]),
        ("box", "Given or learn? (formula booklets)", [
            "No board prints the basic rules of this unit: learn i² = −1, the division method, the conjugate properties and the "
            "quadratic factor z² − 2Re(α)z + |α|².",
            "Cambridge 9231 assumes all of this from 9709 Paper 3 and tests it inside Paper 1 and 2 questions (for example roots "
            "of polynomials in Unit A3).",
        ]),
    ],
    "examples": [
        {
            "title": "Arithmetic in Cartesian form",
            "question": "Given z = 3 − 2i and w = 1 + 4i, find in the form x + iy: (a) zw, (b) z/w, (c) z² − w*.",
            "steps": [
                "(a) zw = (3 − 2i)(1 + 4i) = 3 + 12i − 2i − 8i² = 3 + 10i + 8 = 11 + 10i.",
                "(b) Multiply top and bottom by w* = 1 − 4i: z/w = (3 − 2i)(1 − 4i)/((1 + 4i)(1 − 4i)).",
                "Numerator: 3 − 12i − 2i + 8i² = 3 − 14i − 8 = −5 − 14i. Denominator: 1² + 4² = 17.",
                "So z/w = −5/17 − (14/17)i.",
                "(c) z² = (3 − 2i)² = 9 − 12i + 4i² = 5 − 12i, and w* = 1 − 4i. So z² − w* = 4 − 8i.",
            ],
        },
        {
            "title": "Equating real and imaginary parts",
            "question": "Find the complex number z such that 2z + iz* = 5 + 4i.",
            "steps": [
                "Let z = x + iy, so z* = x − iy and iz* = ix − i²y = y + ix.",
                "Then 2z + iz* = (2x + y) + i(2y + x).",
                "Equate real parts: 2x + y = 5. Equate imaginary parts: x + 2y = 4.",
                "Solving: from the first, y = 5 − 2x; then x + 10 − 4x = 4, so x = 2 and y = 1.",
                "z = 2 + i. Check: 2(2 + i) + i(2 − i) = 4 + 2i + 2i + 1 = 5 + 4i. ✓",
            ],
        },
        {
            "title": "Square roots, and a quadratic with complex coefficients",
            "question": "(a) Find the square roots of 5 − 12i. (b) Hence solve z² − (1 + 2i)z − 2 + 4i = 0.",
            "steps": [
                "(a) Let (a + ib)² = 5 − 12i with a, b real. Then a² − b² = 5 and 2ab = −12, so b = −6/a.",
                "a² − 36/a² = 5 ⇒ a⁴ − 5a² − 36 = 0 ⇒ (a² − 9)(a² + 4) = 0. Since a is real, a² = 9, so a = ±3.",
                "a = 3 gives b = −2; a = −3 gives b = 2. The square roots are ±(3 − 2i).",
                "Check: a² + b² = 13 = √(5² + 12²). ✓",
                "(b) Discriminant: (1 + 2i)² − 4(−2 + 4i) = (1 + 4i − 4) + 8 − 16i = 5 − 12i.",
                "z = [(1 + 2i) ± (3 − 2i)]/2, so z = 4/2 = 2 or z = (−2 + 4i)/2 = −1 + 2i.",
                "The roots are not a conjugate pair; that is fine, because the coefficients are not all real.",
            ],
        },
        {
            "title": "A cubic with a given real root",
            "question": "Show that z = 2 is a root of z³ − 6z² + 21z − 26 = 0, and hence solve the equation.",
            "steps": [
                "f(2) = 8 − 24 + 42 − 26 = 0, so (z − 2) is a factor (factor theorem).",
                "Write z³ − 6z² + 21z − 26 = (z − 2)(z² + pz + q). Constant terms: −2q = −26, so q = 13. "
                "z² terms: p − 2 = −6, so p = −4.",
                "Check the z terms: q − 2p = 13 + 8 = 21. ✓",
                "Solve z² − 4z + 13 = 0: (z − 2)² = −9, so z = 2 ± 3i.",
                "The roots are 2, 2 + 3i and 2 − 3i. (The figure in section 1.7 shows the single real root.)",
            ],
        },
        {
            "title": "Finding unknown coefficients from a complex root",
            "question": "Given that 1 + 2i is a root of z³ + az² + bz + 15 = 0, where a and b are real, find a and b and the other "
                        "two roots.",
            "steps": [
                "The coefficients are real, so 1 − 2i is also a root.",
                "Quadratic factor: (z − 1 − 2i)(z − 1 + 2i) = (z − 1)² + 4 = z² − 2z + 5.",
                "Write z³ + az² + bz + 15 = (z² − 2z + 5)(z + k). Constant terms: 5k = 15, so k = 3.",
                "Expand: (z² − 2z + 5)(z + 3) = z³ + 3z² − 2z² − 6z + 5z + 15 = z³ + z² − z + 15.",
                "So a = 1 and b = −1. The roots are 1 + 2i, 1 − 2i and −3.",
                "Alternative: substitute z = 1 + 2i, using (1 + 2i)² = −3 + 4i and (1 + 2i)³ = −11 − 2i, then equate real and "
                "imaginary parts: −11 − 3a + b + 15 = 0 and −2 + 4a + 2b = 0, giving a = 1, b = −1 again.",
            ],
        },
        {
            "title": "A quartic with two conjugate pairs",
            "question": "Given that 2 − i is a root of z⁴ − 6z³ + 18z² − 30z + 25 = 0, solve the equation.",
            "steps": [
                "Real coefficients, so 2 + i is also a root. Quadratic factor: (z − 2)² + 1 = z² − 4z + 5.",
                "Write z⁴ − 6z³ + 18z² − 30z + 25 = (z² − 4z + 5)(z² + pz + q).",
                "Constant terms: 5q = 25, so q = 5. z³ terms: p − 4 = −6, so p = −2.",
                "Check z² terms: q − 4p + 5 = 5 + 8 + 5 = 18 ✓; z terms: 5p − 4q = −10 − 20 = −30 ✓.",
                "Solve z² − 2z + 5 = 0: (z − 1)² = −4, so z = 1 ± 2i.",
                "The four roots are 2 ± i and 1 ± 2i: two conjugate pairs, and no real roots.",
            ],
        },
    ],
    "practice": [
        "Simplify: (a) i³ (b) i⁴ (c) i¹⁰ (d) 1/i (e) i²³.",
        "Given z = 4 + 3i and w = 2 − i, find in the form x + iy:\n(a) z + w (b) z − 2w (c) zw (d) z*w.",
        "Express in the form x + iy:\n(a) (5 + i)/(2 − 3i) (b) 1/(1 + i)² (c) (3 + 4i)/i.",
        "Find the real numbers x and y such that (x + iy)(3 + i) = 7 + 9i.",
        "Solve z + 3z* = 8 − 6i.",
        "Find the square roots of: (a) −15 + 8i (b) 24i. Give exact answers in the form a + ib.",
        "Solve: (a) z² + 6z + 13 = 0 (b) 2z² − 2z + 5 = 0.",
        "One root of a quadratic equation with real coefficients is 3 − 5i. Find the equation in the form z² + bz + c = 0.",
        "Show that z = −1 is a root of z³ − z² + 2 = 0, and find the other two roots.",
        "Given that −1 + i is a root of z³ + pz + q = 0, where p and q are real, find p, q and the other two roots.",
        "Given that i is a root of z⁴ + 4z³ + 9z² + 4z + 8 = 0, solve the equation.",
        "(a) For z = x + iy, show that zz* = x² + y² and that z + z* = 2x.\n(b) Find the complex numbers z with z + z* = 6 "
        "and zz* = 25.",
    ],
    "answers": [
        "(a) −i (b) 1 (c) −1 (d) −i (e) −i.",
        "(a) 6 + 2i (b) 5i (c) 11 + 2i (d) (4 − 3i)(2 − i) = 5 − 10i.",
        "(a) (5 + i)(2 + 3i)/13 = 7/13 + (17/13)i (b) (1 + i)² = 2i, so 1/(2i) = −(1/2)i (c) (3 + 4i)(−i) = 4 − 3i.",
        "x + iy = (7 + 9i)/(3 + i) = (7 + 9i)(3 − i)/10 = (30 + 20i)/10 = 3 + 2i, so x = 3, y = 2.",
        "With z = x + iy: 4x − 2iy = 8 − 6i, so x = 2, y = 3: z = 2 + 3i.",
        "(a) a² − b² = −15, ab = 4 ⇒ a⁴ + 15a² − 16 = 0 ⇒ a² = 1: ±(1 + 4i). (b) a² − b² = 0, ab = 12 ⇒ a = b = ±2√3: "
        "±(2√3 + 2√3 i) = ±2√3(1 + i).",
        "(a) (z + 3)² = −4, z = −3 ± 2i (b) z = (2 ± √(−36))/4 = 1/2 ± (3/2)i.",
        "The other root is 3 + 5i: z² − 6z + 34 = 0.",
        "f(−1) = −1 − 1 + 2 = 0. z³ − z² + 2 = (z + 1)(z² − 2z + 2), so z = 1 ± i.",
        "−1 − i is also a root; quadratic factor z² + 2z + 2. z³ + pz + q = (z² + 2z + 2)(z + k); z² terms: 2 + k = 0, k = −2. "
        "(z² + 2z + 2)(z − 2) = z³ − 2z − 4, so p = −2, q = −4. Roots −1 ± i and 2.",
        "−i is also a root, so z² + 1 is a factor. z⁴ + 4z³ + 9z² + 4z + 8 = (z² + 1)(z² + 4z + 8). Roots ±i and −2 ± 2i.",
        "(a) zz* = x² − i²y² = x² + y²; z + z* = 2x. (b) 2x = 6 and x² + y² = 25, so x = 3, y = ±4: z = 3 + 4i or 3 − 4i.",
    ],
    "exam": [
        "f(z) = z⁴ − 2z³ + 6z² − 2z + 5.\n(a) Show that z = i is a root of f(z) = 0. [2]\n(b) Hence solve f(z) = 0. [5]\n"
        "(c) Find the sum of the squares of the four roots. [2]",
        "z₁ = 3 + 4i and z₂ = 1 − 2i.\n(a) Find z₁z₂ and z₁/z₂, each in the form a + bi. [4]\n(b) Find the two square roots "
        "of z₁. [4]\n(c) Hence solve w² − 2w − 2 − 4i = 0. [4]",
        "The cubic equation 2z³ + pz² + qz + 39 = 0, where p and q are real, has a root z = 2 − 3i.\n(a) Write down another "
        "root of the equation. [1]\n(b) Find a quadratic factor of 2z³ + pz² + qz + 39 with real coefficients. [2]\n"
        "(c) Find the values of p and q, and solve the equation. [5]\n(d) Explain why every cubic equation with real "
        "coefficients has at least one real root. [2]",
        "(a) Show that (1 + i)⁴ = −4. [2]\n(b) Hence, or otherwise, find the four roots of z⁴ + 4 = 0, explaining your "
        "reasoning. [4]\n(c) Write z⁴ + 4 as the product of two quadratic factors with real coefficients. [3]",
    ],
    "exam_answers": [
        "(a) i⁴ − 2i³ + 6i² − 2i + 5 = 1 + 2i − 6 − 2i + 5 = 0 [M1 A1]. (b) Real coefficients, so −i is a root [B1]; "
        "z² + 1 is a factor [M1]; f(z) = (z² + 1)(z² − 2z + 5) [M1 A1]; roots ±i, 1 ± 2i [A1]. (c) i² + (−i)² + (1 + 2i)² + "
        "(1 − 2i)² = −1 − 1 + (−3 + 4i) + (−3 − 4i) = −8 [M1 A1].",
        "(a) z₁z₂ = 3 − 6i + 4i + 8 = 11 − 2i [M1 A1]; z₁/z₂ = (3 + 4i)(1 + 2i)/5 = (−5 + 10i)/5 = −1 + 2i [M1 A1]. "
        "(b) a² − b² = 3, ab = 2 [M1]; a⁴ − 3a² − 4 = 0 so a² = 4 [M1 A1]; roots ±(2 + i) [A1]. (c) w = [2 ± √(4 + 8 + 16i)]/2 "
        "= 1 ± √(3 + 4i) [M1 A1], since √(12 + 16i) = 2√(3 + 4i); so w = 1 ± (2 + i): w = 3 + i or w = −1 − i [A1 A1].",
        "(a) 2 + 3i [B1]. (b) (z − 2)² + 9 = z² − 4z + 13 [M1 A1]. (c) 2z³ + pz² + qz + 39 = (z² − 4z + 13)(2z + c); 13c = 39, "
        "c = 3 [M1 A1]; expanding gives 2z³ − 5z² + 14z + 39, so p = −5, q = 14 [A1 A1]; roots 2 ± 3i and −3/2 [A1]. "
        "(d) Non-real roots come in conjugate pairs, so the number of non-real roots is even (0 or 2) [B1]; a cubic has three "
        "roots, so at least one is real [B1]. (Or: the graph of a real cubic goes from −∞ to +∞, so it crosses the x-axis.)",
        "(a) (1 + i)² = 2i [M1], so (1 + i)⁴ = (2i)² = −4 [A1]. (b) So 1 + i is a root of z⁴ + 4 = 0 [B1]; real coefficients, "
        "so 1 − i is a root [B1]; only even powers of z appear, so if z is a root so is −z: −1 − i and −1 + i [M1]; roots "
        "±1 ± i [A1]. (c) Pairs 1 ± i give z² − 2z + 2; −1 ± i give z² + 2z + 2 [M1 A1]; z⁴ + 4 = (z² − 2z + 2)(z² + 2z + 2) "
        "[A1].",
    ],
}
