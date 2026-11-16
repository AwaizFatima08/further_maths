UNIT = {
    "number": "A2",
    "title": "Complex numbers II: Argand diagrams, modulus–argument form and loci",
    "tag": "AS · Edexcel CP 2.4–2.7 · IAL FP1 1.1–1.3 (loci in FP2 3.3) · AQA B4–B7 (AS) · OCR A 4.02b, e, f, k, l, o, p (AS) · "
           "OCR MEI Pj6–Pj11 (AS) · CAIE 9231: assumed from 9709 P3 (revise it here) · builds on A1",
    "notes": [
        ("p", "A real number is a point on a line. A complex number x + iy needs two real numbers, so it is a point in a plane. "
              "Drawing complex numbers as points turns algebra into geometry: addition becomes vector addition, the modulus "
              "becomes a distance, and simple equations in z describe circles, lines and half-lines. This unit covers the "
              "Argand diagram, the modulus–argument form, products and quotients, and loci and regions."),

        ("h2", "2.1 The Argand diagram (Edexcel 2.4; AQA B4; OCR A 4.02k; MEI Pj9; IAL 1.3)"),
        ("p", "In an <b>Argand diagram</b> the complex number z = x + iy is shown as the point (x, y). The horizontal axis is the "
              "<b>real axis</b> and the vertical axis is the <b>imaginary axis</b>. We can also think of z as the position vector "
              "of that point, an arrow from O to (x, y). Real numbers lie on the real axis; purely imaginary numbers lie on the "
              "imaginary axis."),

        ("h2", "2.2 Conjugation, addition and subtraction (Edexcel 2.4; OCR A 4.02l; MEI Pj9, Pj10)"),
        ("bullets", [
            "<b>Conjugation</b>: z* = x − iy is the reflection of z in the real axis.",
            "<b>Negation</b>: −z is the rotation of z through π about O (a half-turn).",
            "<b>Addition</b>: z + w is found by adding position vectors. O, z, z + w and w form a parallelogram.",
            "<b>Subtraction</b>: z − w is the vector from the point w to the point z. So |z − w| is the <b>distance</b> between "
            "the points z and w. This single fact is the key to all of the loci in this unit.",
            "Multiplying by a real number k > 0 is an enlargement, scale factor k, centre O. Multiplying by i rotates through "
            "π/2 anticlockwise about O, because i(x + iy) = −y + ix, and (x, y) ↦ (−y, x) is that rotation.",
        ]),
        ("figure", "pa02_addsub.png",
         "z = 4 + i and w = 1 + 3i. The sum z + w = 5 + 4i completes the parallelogram. The difference z − w = 3 − 2i is the "
         "same vector as the arrow from w to z. The conjugate z* = 4 − i is the reflection of z in the real axis.", 100),

        ("h2", "2.3 Modulus and argument (Edexcel 2.2, 2.5; AQA B5; OCR A 4.02a–c; MEI Pj6, Pj7; IAL 1.1)"),
        ("p", "The <b>modulus</b> |z| of z = x + iy is its distance from O: |z| = √(x² + y²). It is real and non-negative, and "
              "|z| = 0 only when z = 0. From Unit A1, zz* = x² + y², so <b>zz* = |z|²</b>."),
        ("p", "The <b>argument</b> arg z is the angle between the positive real axis and the line from O to z, measured "
              "anticlockwise in <b>radians</b>. Angles that differ by 2π give the same point, so we choose one value: the "
              "<b>principal argument</b>, with −π < arg z ≤ π. OCR A also allows 0 ≤ arg z < 2π, and a question will make the "
              "range clear. The argument of 0 is not defined."),
        ("p", "To find arg z, <b>sketch z first</b> to see its quadrant, find the acute angle α = arctan(|y|/|x|), then adjust."),
        ("table", ["Position of z = x + iy", "Principal argument (−π < arg z ≤ π)", "Example"], [
            ["first quadrant (x > 0, y > 0)", "α", "arg(1 + √3 i) = π/3"],
            ["second quadrant (x < 0, y > 0)", "π − α", "arg(−√3 + i) = 5π/6"],
            ["third quadrant (x < 0, y < 0)", "−(π − α) = −π + α", "arg(−2 − 2i) = −3π/4"],
            ["fourth quadrant (x > 0, y < 0)", "−α", "arg(3 − 4i) = −arctan(4/3) ≈ −0.927"],
            ["on the axes", "0, π/2, π or −π/2", "arg(−5) = π, arg(−2i) = −π/2"],
        ]),
        ("figure", "pa02_args.png",
         "Modulus and argument. For −√3 + i, r = 2 and θ = 5π/6. For −2 − 2i, r = 2√2 and θ = −3π/4: an angle measured "
         "clockwise from the positive real axis is negative.", 95),

        ("h2", "2.4 Modulus–argument form (Edexcel 2.5; AQA B5; OCR A 4.02b, 4.02f; MEI Pj7)"),
        ("p", "If |z| = r and arg z = θ, then x = r cos θ and y = r sin θ, so z = r(cos θ + i sin θ). This is the "
              "<b>modulus–argument form</b> (or polar form)."),
        ("box", "Converting between forms", [
            "Cartesian → modulus–argument: r = √(x² + y²), θ from a sketch and tan θ = y/x (section 2.3).",
            "Modulus–argument → Cartesian: x = r cos θ, y = r sin θ.",
            "OCR A notation: r(cos θ + i sin θ) is also written [r, θ] or r cis θ. Unit B1 adds the exponential form re<sup>iθ</sup>.",
            "The form needs r > 0 and the <b>same</b> angle in both terms with a plus sign: 2(cos π/3 − i sin π/3) is not in "
            "modulus–argument form; rewrite it as 2(cos(−π/3) + i sin(−π/3)).",
        ]),

        ("h2", "2.5 Multiplying and dividing in modulus–argument form (Edexcel 2.6; AQA B6; OCR A 4.02e; MEI Pj8, Pj10; IAL 1.2)"),
        ("p", "Let z₁ = r₁(cos θ₁ + i sin θ₁) and z₂ = r₂(cos θ₂ + i sin θ₂). Multiply out and use the compound angle formulae:"),
        ("p", "z₁z₂ = r₁r₂[(cos θ₁ cos θ₂ − sin θ₁ sin θ₂) + i(sin θ₁ cos θ₂ + cos θ₁ sin θ₂)] = r₁r₂[cos(θ₁ + θ₂) + i sin(θ₁ + θ₂)]."),
        ("p", "For the quotient, multiply top and bottom of z₁/z₂ by (cos θ₂ − i sin θ₂); the denominator becomes "
              "cos²θ₂ + sin²θ₂ = 1, and the same formulae give z₁/z₂ = (r₁/r₂)[cos(θ₁ − θ₂) + i sin(θ₁ − θ₂)]."),
        ("box", "Products and quotients", [
            "|z₁z₂| = |z₁||z₂|   and   arg(z₁z₂) = arg z₁ + arg z₂ (± 2π if needed to return to the principal range).",
            "|z₁/z₂| = |z₁|/|z₂|   and   arg(z₁/z₂) = arg z₁ − arg z₂ (± 2π if needed).",
            "To multiply, multiply the moduli and add the arguments. To divide, divide the moduli and subtract the arguments.",
            "IAL FP1 requires |z₁z₂| = |z₁||z₂| but not the argument rule; learn both anyway.",
        ]),
        ("p", "<b>On the Argand diagram</b>, multiplying z by w stretches the length of z by the factor |w| and turns it through "
              "the angle arg w. Units B1 and C6 develop this geometric view."),

        ("h2", "2.6 Loci in the Argand diagram (Edexcel 2.7; AQA B7; OCR A 4.02o; MEI Pj11; IAL FP2 3.3)"),
        ("p", "A <b>locus</b> is the set of points z that satisfy a condition. Read every condition as a statement about distances "
              "and angles, using “|z − a| is the distance from z to a”."),
        ("table", ["Condition", "Meaning", "Locus", "Cartesian form (a = p + iq)"], [
            ["|z − a| = r", "distance from a is r", "circle, centre a, radius r", "(x − p)² + (y − q)² = r²"],
            ["|z − a| = |z − b|", "equidistant from a and b", "perpendicular bisector of the segment from a to b",
             "square both sides and simplify: a straight line"],
            ["arg(z − a) = θ", "direction from a to z is θ", "half-line from a at angle θ to the real direction; the "
             "point a itself is <b>excluded</b>", "y − q = tan θ (x − p), on one side of a only"],
            ["Re(z) = k, Im(z) = k", "fixed real or imaginary part", "vertical line x = k; horizontal line y = k", "x = k; y = k"],
        ]),
        ("p", "Rewrite the condition so that it has the form |z − a|: for example |z + 3 − i| = |z − (−3 + i)|, so the centre "
              "is −3 + i, not 3 − i. Similarly |2z − 4| = 6 means 2|z − 2| = 6, a circle centre 2, radius 3."),
        ("figure", "pa02_loci.png",
         "The three basic loci from worked example A2.4: a circle |z − 3 + 2i| = 4, a perpendicular bisector |z + 1| = |z − 3i|, "
         "and a half-line arg(z − 2) = π/4 (open circle: 2 itself is not on the locus).", 150),
        ("p", "Edexcel A level and IAL also need |z − a| = k|z − b| with k ≠ 1 (a circle) and arg((z − a)/(z − b)) = θ (an "
              "arc). These are in Unit C6. MEI excludes them."),

        ("h2", "2.7 Regions and set notation (Edexcel 2.7; OCR A 4.02o, 4.02p; MEI Pj11)"),
        ("bullets", [
            "|z − a| < r: inside the circle. |z − a| > r: outside it.",
            "|z − a| < |z − b|: the half-plane of points closer to a than to b (the side of the perpendicular bisector "
            "containing a).",
            "α < arg(z − a) < β: the region between two half-lines from a, like a slice of pie with no crust.",
            "Draw a boundary that is <b>included</b> (≤, ≥) as a solid line and a boundary that is <b>excluded</b> (<, >) as a "
            "dashed line. Shade the region you want, and say which region you mean.",
        ]),
        ("p", "<b>Set notation.</b> A locus or region is written {z : condition}, read “the set of z such that…”. The "
              "<b>intersection</b> A ∩ B contains the points in both sets (both conditions hold); the <b>union</b> A ∪ B contains "
              "the points in at least one. For example {z : |z| < 2} ∩ {z : Re(z) > 0} is the right half of the disc of radius 2."),

        ("h2", "2.8 Greatest and least values on a locus"),
        ("p", "Questions often ask for the greatest or least value of |z| or arg z when z lies on (or in) a locus. Draw the "
              "diagram and use geometry."),
        ("box", "Two standard results", [
            "If z lies on the circle |z − a| = r and O is outside it, then the greatest |z| is |a| + r and the least |z| is "
            "|a| − r, both on the line through O and the centre a.",
            "The greatest and least arg z on a circle occur where the half-lines from O <b>touch</b> the circle. The radius to "
            "the point of contact is perpendicular to the tangent, so sin α = r/|a|, where α is the angle between the tangent "
            "and the line from O to the centre. Then arg z = arg a ± α.",
        ]),

        ("warn", "Common mistakes", [
            "Reading arg z from tan⁻¹(y/x) without a sketch. For −2 − 2i the calculator gives π/4, but z is in the third quadrant, "
            "so arg z = −3π/4.",
            "Giving arguments in degrees, or outside the principal range (e.g. 13π/12 instead of −11π/12).",
            "Taking the centre of |z + 3 − i| = 2 as 3 − i. Write it as |z − (−3 + i)| first.",
            "Drawing arg(z − a) = θ as a full line, or including the end point a.",
            "Using solid boundaries for strict inequalities, or not making clear which region is shaded.",
            "Forgetting that |z − w| is a distance, and so expanding into x and y when a sketch would answer the question at once.",
        ]),
        ("box", "Given or learn? (formula booklets)", [
            "Edexcel, AQA, OCR A and OCR MEI: learn |z₁z₂| = |z₁||z₂|, arg(z₁z₂) = arg z₁ + arg z₂ and the quotient versions, and "
            "the meaning of the basic loci (OCR A also prints the loci in its booklet).",
            "IAL: learn the rules for modulus and argument; they are not printed. Cambridge 9231: all of this is assumed from "
            "9709 Paper 3.",
        ]),
    ],
    "examples": [
        {
            "title": "Modulus, argument and modulus–argument form",
            "question": "Find the modulus and principal argument of (a) −√3 + i, (b) −2 − 2i, (c) 3 − 4i, and write each in "
                        "modulus–argument form.",
            "figure": "pa02_args.png", "caption": "Sketch first: (a) is in the second quadrant, (b) in the third.", "width_mm": 80,
            "steps": [
                "(a) r = √(3 + 1) = 2. Second quadrant; α = arctan(1/√3) = π/6, so θ = π − π/6 = 5π/6. "
                "−√3 + i = 2(cos(5π/6) + i sin(5π/6)).",
                "(b) r = √(4 + 4) = 2√2. Third quadrant; α = arctan(2/2) = π/4, so θ = −(π − π/4) = −3π/4. "
                "−2 − 2i = 2√2(cos(−3π/4) + i sin(−3π/4)).",
                "(c) r = √(9 + 16) = 5. Fourth quadrant; α = arctan(4/3) = 0.9273, so θ = −0.927 (3 s.f.). "
                "3 − 4i = 5(cos(−0.927) + i sin(−0.927)).",
            ],
        },
        {
            "title": "Products and quotients in modulus–argument form",
            "question": "z = 4(cos(π/3) + i sin(π/3)) and w = 2(cos(3π/4) + i sin(3π/4)).\n(a) Find zw and z/w in modulus–argument "
                        "form, using principal arguments.\n(b) By also finding z/w in Cartesian form, show that "
                        "cos(5π/12) = (√6 − √2)/4.",
            "steps": [
                "(a) |zw| = 4 × 2 = 8 and arg(zw) = π/3 + 3π/4 = 13π/12. This is more than π, so subtract 2π: −11π/12.",
                "zw = 8(cos(−11π/12) + i sin(−11π/12)).",
                "|z/w| = 4/2 = 2 and arg(z/w) = π/3 − 3π/4 = −5π/12, which is in range. z/w = 2(cos(−5π/12) + i sin(−5π/12)).",
                "(b) In Cartesian form z = 2 + 2√3 i and w = −√2 + √2 i = √2(−1 + i).",
                "z/w = (2 + 2√3 i)(−1 − i)/(√2 × 2) = [(2√3 − 2) − (2 + 2√3)i]/(2√2) = [(√3 − 1) − (√3 + 1)i]/√2.",
                "Comparing real parts with (a): 2cos(−5π/12) = (√3 − 1)/√2, so cos(5π/12) = (√3 − 1)/(2√2) = (√6 − √2)/4.",
            ],
        },
        {
            "title": "Geometry of conjugation and of multiplying by i",
            "question": "z = 3 + i. Show z, z*, iz and z + iz on an Argand diagram. Describe the quadrilateral with vertices O, z, "
                        "z + iz and iz, and find its area.",
            "figure": "pa02_square.png", "caption": "Multiplying by i rotates z through π/2 about O.", "width_mm": 80,
            "steps": [
                "z* = 3 − i (reflection in the real axis). iz = 3i + i² = −1 + 3i (rotation of z through π/2). "
                "z + iz = 2 + 4i.",
                "|z| = |iz| = √10, and the arrows to z and iz are at right angles, because multiplying by i turns through π/2.",
                "O, z, z + iz, iz is a parallelogram (vector addition) with two equal adjacent sides at right angles, so it is a "
                "<b>square</b> of side √10.",
                "Area = (√10)² = 10 square units.",
            ],
        },
        {
            "title": "Loci and their Cartesian equations",
            "question": "Sketch each locus and find its Cartesian equation: (a) |z − 3 + 2i| = 4, (b) |z + 1| = |z − 3i|, "
                        "(c) arg(z − 2) = π/4.",
            "figure": "pa02_loci.png", "caption": "The three loci of worked example A2.4.", "width_mm": 150,
            "steps": [
                "(a) |z − (3 − 2i)| = 4: a circle with centre 3 − 2i and radius 4. With z = x + iy: (x − 3)² + (y + 2)² = 16.",
                "(b) Points equidistant from −1 and 3i: the perpendicular bisector of the segment joining (−1, 0) and (0, 3).",
                "|x + 1 + iy|² = |x + i(y − 3)|² ⇒ (x + 1)² + y² = x² + (y − 3)² ⇒ 2x + 1 = −6y + 9 ⇒ x + 3y = 4.",
                "Check: the midpoint (−1/2, 3/2) satisfies x + 3y = 4. ✓",
                "(c) The half-line from 2 at angle π/4: y = x − 2 with x > 2. The point z = 2 is excluded, since arg 0 is undefined.",
            ],
        },
        {
            "title": "A region in set notation, with greatest and least |z|",
            "question": "R = {z : |z − 2 − 2i| ≤ 2} ∩ {z : 0 ≤ arg z ≤ π/4}.\n(a) Shade R on an Argand diagram and find its "
                        "area.\n(b) Find the greatest and least values of |z| for z in R.",
            "figure": "pa02_region.png", "caption": "R is the half of the disc below the line y = x (boundaries included).",
            "width_mm": 85,
            "steps": [
                "(a) The disc has centre 2 + 2i and radius 2; it touches both axes. 0 ≤ arg z ≤ π/4 is the region between the "
                "positive real axis and the half-line y = x (x > 0), boundaries included.",
                "The line y = x passes through the centre 2 + 2i, so R is exactly half the disc: area = ½ × π × 2² = 2π.",
                "(b) |z| is the distance from O. The line from O through the centre is y = x, and it lies on the boundary of R.",
                "Greatest |z| = |2 + 2i| + 2 = 2√2 + 2 ≈ 4.83, at z = (2 + √2)(1 + i).",
                "Least |z| = 2√2 − 2 ≈ 0.828, at z = (2 − √2)(1 + i). Both points are in R because the boundaries are included.",
            ],
        },
        {
            "title": "Greatest and least argument on a circle",
            "question": "z lies on the circle |z − 5i| = 3.\n(a) Find the greatest and least values of |z|.\n(b) Find the greatest "
                        "and least values of arg z, and the complex number z where arg z is least.",
            "figure": "pa02_tangent.png", "caption": "The extreme arguments occur on the tangents from O.", "width_mm": 75,
            "steps": [
                "(a) The centre is 5i, at distance 5 from O; the radius is 3. Greatest |z| = 5 + 3 = 8 (at 8i); least |z| = 5 − 3 = 2 "
                "(at 2i).",
                "(b) The radius to a point of contact is perpendicular to the tangent, so sin α = 3/5, α = 0.6435.",
                "arg(5i) = π/2, so arg z ranges from π/2 − 0.6435 = 0.927 to π/2 + 0.6435 = 2.21 (3 s.f.).",
                "At the lower tangent point, the distance from O is √(5² − 3²) = 4 and arg z = 0.9273, with cos = 3/5 and sin = 4/5.",
                "So z = 4(3/5 + (4/5)i) = 2.4 + 3.2i. Check: |2.4 − 1.8i| = √(5.76 + 3.24) = 3. ✓",
            ],
        },
    ],
    "practice": [
        "z = 2 − 5i and w = −3 + i. Show z, w, z + w, z − w and z* on one Argand diagram, labelling each point with its "
        "coordinates.",
        "Find the modulus and principal argument of each number, exactly where possible, otherwise to 3 s.f.:\n"
        "(a) 1 + i (b) −5 (c) −2i (d) −3 + 4i (e) −1 − √3 i.",
        "Write in the form x + iy, with exact values:\n(a) 6(cos(π/6) + i sin(π/6)) (b) √2(cos(−3π/4) + i sin(−3π/4)) "
        "(c) [4, 2π/3].",
        "Express √3 − i in modulus–argument form.",
        "z = 6(cos(5π/6) + i sin(5π/6)) and w = 2(cos(π/3) + i sin(π/3)). Find, in modulus–argument form with principal "
        "arguments:\n(a) zw (b) z/w (c) z².",
        "Without multiplying out, find (a) |(3 + 4i)(1 − i)| (b) arg((1 + i)/(1 − i)). Check (b) by division.",
        "Sketch each locus and describe it in words:\n(a) |z − 2i| = 3 (b) |z − 1| = |z + i| (c) arg(z + 1 − i) = −π/4.",
        "Find the Cartesian equation of the locus |z + 2 − i| = |z − 4 + 3i|, and verify that it passes through the midpoint "
        "of the two fixed points.",
        "Shade the region {z : |z| ≤ 3} ∩ {z : π/6 ≤ arg z ≤ π/2} and find its area.",
        "Write in set notation: the points that are inside the circle with centre 2 + i and radius 3 and are closer to 0 than "
        "to 4. Sketch the region, using dashed boundaries.",
        "z lies on the locus |z − 3 − 4i| = 2. Find the greatest and least values of |z|.",
        "z lies on the circle |z − 6i| = 3. Find the greatest and least values of arg z, and the value of z where arg z is "
        "least, in the form a + bi.",
    ],
    "answers": [
        "z = (2, −5), w = (−3, 1), z + w = −1 − 4i at (−1, −4), z − w = 5 − 6i at (5, −6), z* = 2 + 5i at (2, 5).",
        "(a) √2, π/4 (b) 5, π (c) 2, −π/2 (d) 5, π − arctan(4/3) = 2.21 (e) 2, −2π/3.",
        "(a) 3√3 + 3i (b) −1 − i (c) −2 + 2√3 i.",
        "2(cos(−π/6) + i sin(−π/6)).",
        "(a) 12(cos(−5π/6) + i sin(−5π/6)) [7π/6 − 2π] (b) 3(cos(π/2) + i sin(π/2)) = 3i (c) 36(cos(−π/3) + i sin(−π/3)) "
        "[5π/3 − 2π].",
        "(a) 5 × √2 = 5√2 (b) π/4 − (−π/4) = π/2. Check: (1 + i)/(1 − i) = (1 + i)²/2 = 2i/2 = i, and arg i = π/2.",
        "(a) circle, centre 2i, radius 3 (b) perpendicular bisector of 1 and −i: the line y = −x (c) half-line from −1 + i "
        "(excluded) going down to the right at −π/4: y = −x with x > −1. It lies along the line in (b).",
        "(x + 2)² + (y − 1)² = (x − 4)² + (y + 3)² ⇒ 12x − 8y − 20 = 0 ⇒ 3x − 2y = 5. Midpoint (1, −1): 3 + 2 = 5. ✓",
        "A sector of radius 3 and angle π/2 − π/6 = π/3: area ½ × 9 × π/3 = 3π/2.",
        "{z : |z − 2 − i| < 3} ∩ {z : |z| < |z − 4|}: the part of the open disc to the left of the dashed line x = 2.",
        "|3 + 4i| = 5, so greatest |z| = 7 and least |z| = 3.",
        "sin α = 3/6, α = π/6. Greatest arg z = π/2 + π/6 = 2π/3, least = π/3. Tangent length √(36 − 9) = 3√3, so "
        "z = 3√3(cos(π/3) + i sin(π/3)) = 3√3/2 + (9/2)i.",
    ],
    "exam": [
        "z = 1 + √3 i and w = 1 − i.\n(a) Find |z|, arg z, |w| and arg w. [3]\n(b) Hence write zw and z/w in "
        "modulus–argument form. [3]\n(c) By writing z/w in the form a + bi, show that cos(7π/12) = (√2 − √6)/4. [4]",
        "C is the locus |z − 4 − 2i| = 2 and L is the locus arg(z − 2) = π/4.\n(a) Sketch C and L on the same Argand "
        "diagram. [4]\n(b) Find, in exact form, the complex numbers represented by the points where L meets C. [4]\n"
        "(c) Shade the region {z : |z − 4 − 2i| ≤ 2} ∩ {z : π/4 ≤ arg(z − 2) ≤ π} and find its exact area. [3]",
        "The complex number z satisfies |z − 6 − 8i| = 4.\n(a) Sketch the locus of z. [2]\n(b) Find the greatest and least "
        "values of |z|. [3]\n(c) Find the value of z for which |z| is least, in the form a + bi. [3]\n(d) Find the greatest "
        "value of arg z, giving your answer in radians to 3 s.f. [3]",
        "(a) By writing z₁ = r₁(cos θ₁ + i sin θ₁) and z₂ = r₂(cos θ₂ + i sin θ₂), prove that |z₁z₂| = r₁r₂ and that "
        "θ₁ + θ₂ is an argument of z₁z₂. [4]\n(b) The points P and Q represent p = 4 + 2i and q = (1 + i)p. Describe "
        "geometrically how Q is obtained from P, and find q. [2]\n(c) Show that triangle OPQ is right-angled and isosceles, "
        "and find its area. [3]",
    ],
    "exam_answers": [
        "(a) |z| = 2, arg z = π/3 [B1]; |w| = √2 [B1]; arg w = −π/4 [B1]. (b) zw = 2√2(cos(π/12) + i sin(π/12)) [B1 ft]; "
        "z/w = √2(cos(7π/12) + i sin(7π/12)) [M1 A1]. (c) z/w = (1 + √3 i)(1 + i)/2 = [(1 − √3) + (1 + √3)i]/2 [M1 A1]; "
        "equating real parts, √2 cos(7π/12) = (1 − √3)/2 [M1]; cos(7π/12) = (1 − √3)/(2√2) = (√2 − √6)/4 [A1].",
        "(a) Circle centre (4, 2), radius 2, touching the real axis at 4 [B1 B1]; half-line from (2, 0), excluded, at π/4 [B1], "
        "passing through the centre (4, 2) [B1]. (b) L passes through the centre, so the points are 4 + 2i ± 2(cos π/4 + "
        "i sin π/4) [M1 A1]: (4 + √2) + (2 + √2)i and (4 − √2) + (2 − √2)i [A1 A1]. (c) The half of the disc on or above L "
        "[B1]; L is a diameter [M1], so area = ½π(2²) = 2π [A1].",
        "(a) Circle centre 6 + 8i, radius 4, not enclosing O [B1 B1]. (b) |6 + 8i| = 10 [B1]; greatest 14, least 6 [B1 B1]. "
        "(c) On the line from O through the centre: z = 6 × (6 + 8i)/10 [M1 A1] = 3.6 + 4.8i [A1]. (d) arg(6 + 8i) = "
        "arctan(4/3) = 0.9273 [B1]; half-angle arcsin(4/10) = 0.4115 [M1]; greatest arg z = 1.34 [A1].",
        "(a) z₁z₂ = r₁r₂[(cos θ₁cos θ₂ − sin θ₁sin θ₂) + i(sin θ₁cos θ₂ + cos θ₁sin θ₂)] [M1 A1] = r₁r₂[cos(θ₁ + θ₂) + "
        "i sin(θ₁ + θ₂)] by the compound angle formulae [M1]; this is modulus–argument form, so |z₁z₂| = r₁r₂ and θ₁ + θ₂ is "
        "an argument [A1]. (b) |1 + i| = √2, arg = π/4: enlarge OP by factor √2 and rotate through π/4 anticlockwise about O "
        "[B1]; q = 4 + 2i + 4i − 2 = 2 + 6i [B1]. (c) OP = |4 + 2i| = √20, PQ = |−2 + 4i| = √20, OQ = √40 [M1]; OP = PQ and "
        "OP² + PQ² = OQ², so the right angle is at P [A1]; area = ½ × 20 = 10 [A1].",
    ],
}
