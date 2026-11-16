UNIT = {
    "number": "B2",
    "title": "nth roots and roots of unity",
    "tag": "A level · Edexcel CP 2.10, 2.11 · IAL FP2 3.2 (roots of a complex number) · AQA B10, B11 · OCR A 4.02r, 4.02s · "
           "OCR MEI Pj15–Pj17, Pj19, Pj20 · CAIE 9231 P2 2.5 (nth roots of unity; rational exponents) · builds on B1",
    "notes": [
        ("p", "Over the real numbers, x³ = 8 has one solution. Over the complex numbers, every equation zⁿ = w with w ≠ 0 has "
              "exactly n solutions, and they sit at the corners of a regular polygon. This unit finds them with de Moivre's "
              "theorem, studies the special case w = 1 (the roots of unity), and uses them to solve geometric problems."),

        ("h2", "2.1 Solving zⁿ = w (Edexcel 2.10; AQA B10; OCR A 4.02r; MEI Pj16; IAL 3.2)"),
        ("p", "Write w in exponential form, w = Re<sup>iφ</sup>, and look for z = re<sup>iθ</sup>. Then zⁿ = rⁿe<sup>inθ</sup>, "
              "and two complex numbers in exponential form are equal when their moduli are equal and their arguments differ by "
              "a multiple of 2π. So rⁿ = R and nθ = φ + 2kπ for some integer k."),
        ("box", "The n distinct nth roots of w = Re<sup>iφ</sup> (R > 0)", [
            "z = R<sup>1/n</sup> e<sup>i(φ + 2kπ)/n</sup>,   k = 0, 1, 2, …, n − 1,",
            "where R<sup>1/n</sup> is the real positive nth root of R. In modulus–argument form: "
            "z = R<sup>1/n</sup>[cos((φ + 2kπ)/n) + i sin((φ + 2kπ)/n)].",
            "Any n consecutive values of k give the same n roots. To get principal arguments directly, choose k so that "
            "(φ + 2kπ)/n lies in (−π, π].",
        ]),
        ("p", "<b>Why exactly n roots?</b> The arguments (φ + 2kπ)/n for k = 0, 1, …, n − 1 differ by multiples of 2π/n that are "
              "less than 2π, so they give n different points. The next value, k = n, gives (φ + 2nπ)/n = φ/n + 2π: the same "
              "point as k = 0. After that the roots repeat. This matches the fact that a polynomial of degree n has n roots."),
        ("p", "<b>Rational powers (CAIE 2.5).</b> De Moivre's theorem extends to rational exponents in this sense: "
              "(cos θ + i sin θ)<sup>p/q</sup> has q different values, cos((pθ + 2kπp)/q) + i sin((pθ + 2kπp)/q) for k = 0, …, "
              "q − 1 when p/q is in lowest terms. One of them is cos(pθ/q) + i sin(pθ/q). So w<sup>1/n</sup> means “any of the n "
              "nth roots”, and you must find them all."),

        ("h2", "2.2 The roots form a regular n-gon (Edexcel 2.10; AQA B10; OCR A 4.02r; MEI Pj15)"),
        ("p", "All n roots have the same modulus R<sup>1/n</sup>, so they lie on the circle with centre O and that radius. "
              "Consecutive roots differ in argument by exactly 2π/n. So the roots are the <b>vertices of a regular n-gon</b> "
              "centred at O. Once you have one root, you can draw the rest by stepping round the circle in equal angles of 2π/n."),
        ("figure", "pb02_cube8i.png",
         "The cube roots of 8i (worked example B2.1) lie on the circle |z| = 2, spaced 2π/3 apart: an equilateral triangle.", 80),

        ("h2", "2.3 Roots of unity (Edexcel 2.11; AQA B11; OCR A 4.02s; MEI Pj17, Pj19; CAIE 2.5)"),
        ("p", "The nth roots of unity are the solutions of zⁿ = 1. Here R = 1 and φ = 0, so they are e<sup>2kπi/n</sup>, "
              "k = 0, 1, …, n − 1. Write ω = e<sup>2πi/n</sup>. Then the roots are 1, ω, ω², …, ωⁿ⁻¹."),
        ("box", "Properties of the nth roots of unity, ω = e<sup>2πi/n</sup>", [
            "The roots are 1, ω, ω², …, ωⁿ⁻¹; they lie on the unit circle at the vertices of a regular n-gon with one vertex at 1.",
            "ωⁿ = 1, and ωᵏ and ωⁿ⁻ᵏ are complex conjugates (so non-real roots come in conjugate pairs, as they must for the real "
            "polynomial zⁿ − 1).",
            "<b>Sum: 1 + ω + ω² + … + ωⁿ⁻¹ = 0</b> for n ≥ 2.",
            "Cube roots of unity: 1, ω, ω², with ω = −½ + (√3/2)i, ω² = ω* = −½ − (√3/2)i, 1 + ω + ω² = 0 and ω³ = 1.",
        ]),
        ("p", "<b>Three reasons why the sum is zero (MEI Pj17).</b> (1) Algebra: 1 + ω + … + ωⁿ⁻¹ is a geometric series, equal to "
              "(ωⁿ − 1)/(ω − 1) = 0/(ω − 1) = 0, since ω ≠ 1. (2) Polynomials: the roots of zⁿ − 1 = 0 have sum equal to minus the "
              "coefficient of zⁿ⁻¹, which is 0. (3) Geometry: rotating the regular polygon through 2π/n about O maps it onto itself, "
              "so the sum S satisfies ωS = S; since ω ≠ 1, S = 0."),
        ("p", "The same arguments show that the n roots of any equation zⁿ = w (n ≥ 2) add up to zero."),
        ("p", "<b>Real quadratic factors.</b> Pairing each root ωᵏ with its conjugate gives (z − ωᵏ)(z − ω⁻ᵏ) "
              "= z² − 2cos(2kπ/n)z + 1. So zⁿ − 1 factorises over the reals into (z − 1), also (z + 1) if n is even, and quadratic "
              "factors of this form."),
        ("figure", "pb02_unity5.png",
         "The fifth roots of unity form a regular pentagon. ω⁴ = ω* and ω³ = (ω²)*.", 75),

        ("h2", "2.4 All the roots from one root (Edexcel 2.11; MEI Pj19)"),
        ("box", "One root times the roots of unity", [
            "If z₀ is one root of zⁿ = w, then the n roots are z₀, z₀ω, z₀ω², …, z₀ωⁿ⁻¹, where ω = e<sup>2πi/n</sup>.",
            "Reason: (z₀ωᵏ)ⁿ = z₀ⁿ(ωⁿ)ᵏ = w × 1 = w, and these n numbers are all different.",
        ]),
        ("p", "Geometrically, multiplying by ω rotates through 2π/n about O, which carries each vertex of the polygon to the next. "
              "This is often the quickest method when one root is obvious, for example z = 1 + i for z⁴ = −4."),

        ("h2", "2.5 Geometric problems (Edexcel 2.11; AQA B11; OCR A 4.02s; MEI Pj20)"),
        ("p", "A regular polygon need not be centred at O. If a regular n-gon has centre c and one vertex at a, translate so that c "
              "goes to O, rotate, and translate back."),
        ("box", "Vertices of a regular polygon", [
            "Centre c, one vertex a: the vertices are c + (a − c)ωᵏ, k = 0, 1, …, n − 1, where ω = e<sup>2πi/n</sup>.",
            "Square: multiply a − c by i, −1, −i. Equilateral triangle: multiply by ω and ω² (cube roots of unity).",
            "To rotate the point z through angle α about the point c: z′ = c + (z − c)e<sup>iα</sup>.",
        ]),
        ("p", "Other standard problems use the sum property. For example, if ω = e<sup>2πi/5</sup>, then "
              "ω + ω⁴ = 2cos(2π/5) and ω² + ω³ = 2cos(4π/5), and these two numbers have sum −1 and product −1. "
              "This gives exact values of cos(2π/5) (worked example B2.3)."),

        ("h2", "2.6 Equations that reduce to roots of unity (MEI Pj19; CAIE 2.5)"),
        ("p", "An equation such as (z + 1)ⁿ = zⁿ can be written ((z + 1)/z)ⁿ = 1. So (z + 1)/z = ωᵏ, an nth root of unity, and "
              "each value of k gives one equation for z. The value ωᵏ = 1 gives no solution here (1 + 1/z = 1 is impossible); this "
              "matches the fact that the equation is really of degree n − 1, because the zⁿ terms cancel. The identity "
              "e<sup>iθ</sup> − 1 = 2i sin(θ/2)e<sup>iθ/2</sup> from Unit B1 often simplifies the answers."),

        ("warn", "Common mistakes", [
            "Finding only one root (the “principal” one). zⁿ = w always has n roots: show all of them.",
            "Taking the nth root of the modulus but forgetting to divide the argument by n, or dividing 2kπ by n but not φ.",
            "Giving arguments outside the requested range, or listing the same root twice (k and k + n give the same root).",
            "Writing ω = e<sup>2πi/n</sup> but then using a different n. State n and ω clearly at the start.",
            "In polygon problems, rotating a − c about O and forgetting to add c back on.",
            "Saying the roots “form a polygon” without saying it is regular, or without giving the radius and centre.",
        ]),
        ("box", "Given or learn? (formula booklets)", [
            "Edexcel, AQA, OCR A, OCR MEI and IAL print the nth roots of re<sup>iθ</sup> (or of unity) next to de Moivre's "
            "theorem. Learn the method anyway: the marks are for the working.",
            "Cambridge 9231 prints nothing on complex numbers: learn that the nth roots of unity are e<sup>2kπi/n</sup>, "
            "k = 0, 1, …, n − 1.",
        ]),
    ],
    "examples": [
        {
            "title": "Cube roots of an imaginary number",
            "question": "Solve z³ = 8i, giving the roots in the form x + iy, and show them on an Argand diagram.",
            "figure": "pb02_cube8i.png", "caption": "The roots form an equilateral triangle inscribed in |z| = 2.",
            "width_mm": 70,
            "steps": [
                "8i = 8e<sup>iπ/2</sup>. So z = 8<sup>1/3</sup>e<sup>i(π/2 + 2kπ)/3</sup> = 2e<sup>i(π/6 + 2kπ/3)</sup>.",
                "k = 0: 2e<sup>iπ/6</sup> = √3 + i. k = 1: 2e<sup>5iπ/6</sup> = −√3 + i. k = −1: 2e<sup>−iπ/2</sup> = −2i.",
                "(Using k = −1 instead of k = 2 keeps the argument in the principal range.)",
                "Check: the three roots add to 0, as they should. (√3 + i)³ = 3√3 + 9i − 3√3 − i = 8i. ✓",
            ],
        },
        {
            "title": "Fourth roots, in Cartesian form",
            "question": "Solve z⁴ = −8 + 8√3 i, giving the roots in the form x + iy.",
            "steps": [
                "|−8 + 8√3 i| = √(64 + 192) = 16. The number is in the second quadrant, with arg = π − π/3 = 2π/3.",
                "So z = 16<sup>1/4</sup>e<sup>i(2π/3 + 2kπ)/4</sup> = 2e<sup>i(π/6 + kπ/2)</sup>.",
                "k = 0: 2e<sup>iπ/6</sup> = √3 + i. k = 1: 2e<sup>2πi/3</sup> = −1 + √3 i.",
                "k = 2: 2e<sup>7πi/6</sup> = 2e<sup>−5πi/6</sup> = −√3 − i. k = −1: 2e<sup>−πi/3</sup> = 1 − √3 i.",
                "The roots form a square of side 2√2 centred at O. Each root is i times the previous one.",
            ],
        },
        {
            "title": "Fifth roots of unity and an exact cosine",
            "question": "(a) Write down the fifth roots of unity, and show that z⁵ − 1 = (z − 1)(z² − 2cos(2π/5)z + 1)"
                        "(z² − 2cos(4π/5)z + 1).\n(b) Use the sum of the roots to show that cos(2π/5) + cos(4π/5) = −½.\n"
                        "(c) Show that cos(2π/5)cos(4π/5) = −¼, and hence find cos(2π/5) exactly.",
            "steps": [
                "(a) The roots are 1, ω, ω², ω³, ω⁴ with ω = e<sup>2πi/5</sup>; ω⁴ = ω* and ω³ = (ω²)*.",
                "(z − ω)(z − ω⁴) = z² − (ω + ω*)z + ωω* = z² − 2cos(2π/5)z + 1. Similarly (z − ω²)(z − ω³) = "
                "z² − 2cos(4π/5)z + 1. Together with (z − 1) this gives all five linear factors.",
                "(b) 1 + ω + ω² + ω³ + ω⁴ = 0. Now ω + ω⁴ = 2cos(2π/5) and ω² + ω³ = 2cos(4π/5), so "
                "1 + 2cos(2π/5) + 2cos(4π/5) = 0, giving cos(2π/5) + cos(4π/5) = −½.",
                "(c) (ω + ω⁴)(ω² + ω³) = ω³ + ω⁴ + ω⁶ + ω⁷ = ω³ + ω⁴ + ω + ω² = −1, using ω⁵ = 1. So "
                "4cos(2π/5)cos(4π/5) = −1.",
                "So x = cos(2π/5) and cos(4π/5) are the roots of x² + ½x − ¼ = 0, i.e. 4x² + 2x − 1 = 0, x = (−1 ± √5)/4.",
                "cos(2π/5) > 0, so cos(2π/5) = (√5 − 1)/4 ≈ 0.309.",
            ],
        },
        {
            "title": "An equilateral triangle not centred at the origin",
            "question": "An equilateral triangle has its centre at 1 + i and one vertex at 3 + i. Find the other two vertices "
                        "exactly.",
            "figure": "pb02_triangle.png", "caption": "Rotate 3 + i about 1 + i through 2π/3 and 4π/3.", "width_mm": 70,
            "steps": [
                "Relative to the centre, the known vertex is (3 + i) − (1 + i) = 2.",
                "The other vertices are 1 + i + 2ω and 1 + i + 2ω², where ω = e<sup>2πi/3</sup> = −½ + (√3/2)i.",
                "1 + i + 2ω = 1 + i − 1 + √3 i = (1 + √3)i.",
                "1 + i + 2ω² = 1 + i − 1 − √3 i = (1 − √3)i.",
                "Check: the three vertices add to 3(1 + i), three times the centre, as expected for a centroid.",
            ],
        },
        {
            "title": "An equation that reduces to roots of unity",
            "question": "Solve (1 + z)⁴ = z⁴, and show that all the roots have real part −½.",
            "steps": [
                "z = 0 is not a root, so divide by z⁴: ((1 + z)/z)⁴ = 1. So (1 + z)/z = u, where u is a fourth root of unity: "
                "u = 1, i, −1 or −i.",
                "u = 1 gives 1 + z = z, which is impossible. Otherwise z = 1/(u − 1).",
                "u = −1: z = −½. u = i: z = 1/(i − 1) = (−1 − i)/2. u = −i: z = 1/(−i − 1) = (−1 + i)/2.",
                "The equation is a cubic (the z⁴ terms cancel: 4z³ + 6z² + 4z + 1 = 0), so these three roots are all of them.",
                "All have real part −½. Geometrically: (1 + z)⁴ = z⁴ forces |z + 1| = |z|, so z lies on the perpendicular "
                "bisector of 0 and −1, the line Re(z) = −½.",
            ],
        },
        {
            "title": "A rational power (CAIE 2.5)",
            "question": "Find all the values of (−8)<sup>2/3</sup>.",
            "steps": [
                "−8 = 8e<sup>iπ</sup>. Its cube roots are 2e<sup>i(π + 2kπ)/3</sup>: 2e<sup>iπ/3</sup>, 2e<sup>iπ</sup> = −2 and "
                "2e<sup>−iπ/3</sup>.",
                "Square each: 4e<sup>2iπ/3</sup>, 4e<sup>2iπ</sup> = 4 and 4e<sup>−2iπ/3</sup>.",
                "So (−8)<sup>2/3</sup> has three values: 4, −2 + 2√3 i and −2 − 2√3 i.",
                "The real value 4 = ((−8)<sup>1/3</sup>)² is the one a calculator gives for real numbers; the other two are "
                "found only by working with complex numbers.",
            ],
        },
    ],
    "practice": [
        "Solve z³ = 27, giving the roots in the form x + iy.",
        "Solve z⁴ = 16i, giving the roots in the form re<sup>iθ</sup> with −π < θ ≤ π.",
        "Solve z⁵ = −32, giving the roots in the form re<sup>iθ</sup> with −π < θ ≤ π.",
        "Solve z³ = −4√2 + 4√2 i. Give the root in the first quadrant in the form x + iy and the others in the form "
        "re<sup>iθ</sup>.",
        "Find the sixth roots of unity in the form x + iy. Show that they form a regular hexagon and find its side length.",
        "ω is a complex cube root of unity.\n(a) Show that 1 + ω + ω² = 0.\n(b) Simplify (1 + ω)(1 + ω²).\n"
        "(c) Simplify (1 + ω²)⁴.",
        "A square ABCD has its centre at 1 − i, and A is the point 4 + i. Find B, C and D, labelled anticlockwise.",
        "An equilateral triangle has two vertices at 0 and 4. Find the two possible positions of the third vertex.",
        "Use the sixth roots of unity to show that z⁶ − 1 = (z² − 1)(z² + z + 1)(z² − z + 1).",
        "Write down the fourth roots of unity. Hence solve (z − 2)⁴ = 1.",
        "Explain why, for n ≥ 2, the sum of the n roots of zⁿ = w is zero.",
        "Find the three values of (−8i)<sup>1/3</sup> in the form x + iy.",
    ],
    "answers": [
        "z = 3, 3e<sup>±2πi/3</sup> = −3/2 ± (3√3/2)i.",
        "16i = 16e<sup>iπ/2</sup>: z = 2e<sup>iπ/8</sup>, 2e<sup>5iπ/8</sup>, 2e<sup>−3iπ/8</sup>, 2e<sup>−7iπ/8</sup>.",
        "−32 = 32e<sup>iπ</sup>: z = 2e<sup>iπ/5</sup>, 2e<sup>3iπ/5</sup>, 2e<sup>iπ</sup> = −2, 2e<sup>−iπ/5</sup>, "
        "2e<sup>−3iπ/5</sup>.",
        "Modulus 8, argument 3π/4: z = 2e<sup>iπ/4</sup> = √2 + √2 i, 2e<sup>11iπ/12</sup>, 2e<sup>−5iπ/12</sup>.",
        "±1, ½ ± (√3/2)i, −½ ± (√3/2)i. They lie on |z| = 1 with arguments kπ/3, so they form a regular hexagon; each side "
        "joins points 1 apart (for example 1 and ½ + (√3/2)i), so the side is 1.",
        "(a) ω³ − 1 = (ω − 1)(ω² + ω + 1) = 0 and ω ≠ 1. (b) 1 + ω + ω² + ω³ = 0 + 1 = 1. (c) 1 + ω² = −ω, so "
        "(−ω)⁴ = ω⁴ = ω.",
        "A − c = 3 + 2i. B = c + i(3 + 2i) = −1 + 2i; C = c − (3 + 2i) = −2 − 3i; D = c − i(3 + 2i) = 3 − 4i.",
        "4e<sup>±iπ/3</sup> = 2 ± 2√3 i.",
        "Roots ±1 give z² − 1; e<sup>±iπ/3</sup> give z² − 2cos(π/3)z + 1 = z² − z + 1; e<sup>±2iπ/3</sup> give "
        "z² − 2cos(2π/3)z + 1 = z² + z + 1.",
        "1, i, −1, −i. z − 2 = 1, i, −1, −i, so z = 3, 2 + i, 1, 2 − i.",
        "The roots are z₀, z₀ω, …, z₀ωⁿ⁻¹ with ω = e<sup>2πi/n</sup>, so their sum is z₀(1 + ω + … + ωⁿ⁻¹) = 0. "
        "(Or: the coefficient of zⁿ⁻¹ in zⁿ − w is 0.)",
        "−8i = 8e<sup>−iπ/2</sup>: 2e<sup>−iπ/6</sup> = √3 − i, 2e<sup>iπ/2</sup> = 2i, 2e<sup>−5iπ/6</sup> = −√3 − i.",
    ],
    "exam": [
        "(a) Solve z⁷ = 1, giving the roots in exponential form. [3]\n(b) Let w = z + 1/z, where z is one of the roots "
        "other than 1. Show that w³ + w² − 2w − 1 = 0. [4]\n(c) Hence show that cos(2π/7) + cos(4π/7) + cos(6π/7) = −½ [2] "
        "and cos(2π/7)cos(4π/7)cos(6π/7) = ⅛. [2]",
        "(a) Solve z⁶ = −64, giving the roots in the form x + iy. [4]\n(b) Show the roots on an Argand diagram and find the "
        "area of the polygon they form. [3]\n(c) Hence express z⁶ + 64 as a product of three quadratic factors with real "
        "coefficients. [3]",
        "ω = e<sup>2πi/3</sup>.\n(a) Show that 1 + ω + ω² = 0 and that ω² = −e<sup>iπ/3</sup>. [3]\n(b) The points A, B, "
        "C represent a, b, c, and triangle ABC is equilateral with its vertices in anticlockwise order, so that "
        "c − a = (b − a)e<sup>iπ/3</sup>. Show that a + ωb + ω²c = 0. [4]\n(c) Given a = 1 + i and b = 5 + i, find c. [3]",
        "(a) Show that, for θ not a multiple of 2π, 1/(e<sup>iθ</sup> − 1) = −½ − ½i cot(θ/2). [4]\n(b) Explain why the "
        "equation (z + 1)⁵ = z⁵ has exactly four roots. [1]\n(c) Show that the roots are z = −½ − ½i cot(kπ/5) for "
        "k = 1, 2, 3, 4. [4]",
    ],
    "exam_answers": [
        "(a) z = e<sup>2kπi/7</sup> [M1], k = 0, 1, …, 6 (or −3, …, 3) [A1 A1]. (b) z ≠ 1, so z⁶ + z⁵ + … + z + 1 = 0 [M1]; "
        "divide by z³: (z³ + z⁻³) + (z² + z⁻²) + (z + z⁻¹) + 1 = 0 [M1]; z² + z⁻² = w² − 2, z³ + z⁻³ = w³ − 3w [M1]; so "
        "w³ − 3w + w² − 2 + w + 1 = w³ + w² − 2w − 1 = 0 [A1]. (c) The roots of the cubic are w = 2cos(2π/7), 2cos(4π/7), "
        "2cos(6π/7) [M1]; sum of roots = −1, so the cosines sum to −½ [A1]; product of roots = 1, so the product of the "
        "cosines is ⅛ [M1 A1].",
        "(a) −64 = 64e<sup>iπ</sup>; z = 2e<sup>i(π + 2kπ)/6</sup> [M1 A1]; z = ±√3 ± i (all four sign choices) and ±2i "
        "[A1 A1]. (b) Regular hexagon centred at O, vertices on |z| = 2 [B1]; six equilateral triangles of side 2 [M1]; "
        "area 6 × √3 = 6√3 [A1]. (c) Pair conjugates: ±2i give z² + 4; √3 ± i give z² − 2√3z + 4; −√3 ± i give "
        "z² + 2√3z + 4 [M1 A1]; z⁶ + 64 = (z² + 4)(z² − 2√3z + 4)(z² + 2√3z + 4) [A1].",
        "(a) ω³ = 1, ω ≠ 1, ω³ − 1 = (ω − 1)(1 + ω + ω²) [M1 A1]; ω² = e<sup>4πi/3</sup> = e<sup>iπ</sup>e<sup>iπ/3</sup> "
        "= −e<sup>iπ/3</sup> [B1]. (b) c = a + (b − a)e<sup>iπ/3</sup> = a − ω²(b − a) [M1]; a + ωb + ω²c = a + ωb + ω²a − "
        "ω⁴b + ω⁴a [M1]; ω⁴ = ω [M1]; = a(1 + ω + ω²) + b(ω − ω) = 0 [A1]. (c) c = 1 + i + 4e<sup>iπ/3</sup> [M1] "
        "= 1 + i + 2 + 2√3 i [M1] = 3 + (1 + 2√3)i [A1].",
        "(a) e<sup>iθ</sup> − 1 = e<sup>iθ/2</sup>(e<sup>iθ/2</sup> − e<sup>−iθ/2</sup>) = 2i sin(θ/2)e<sup>iθ/2</sup> "
        "[M1 A1]; so 1/(e<sup>iθ</sup> − 1) = e<sup>−iθ/2</sup>/(2i sin(θ/2)) = (cos(θ/2) − i sin(θ/2))/(2i sin(θ/2)) [M1] "
        "= −½ − ½i cot(θ/2) [A1]. (b) The z⁵ terms cancel, so it is a polynomial equation of degree 4 (leading term 5z⁴) "
        "[B1]. (c) z ≠ 0, so ((z + 1)/z)⁵ = 1 and (z + 1)/z = e<sup>2kπi/5</sup>, k = 1, 2, 3, 4 (k = 0 gives no solution) "
        "[M1 A1]; z = 1/(e<sup>2kπi/5</sup> − 1) [M1]; by (a) with θ = 2kπ/5, z = −½ − ½i cot(kπ/5) [A1].",
    ],
}
