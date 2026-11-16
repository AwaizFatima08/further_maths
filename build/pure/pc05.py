"""Unit C5: Conics II, the ellipse and the hyperbola."""

UNIT = {
    "number": "C5",
    "title": "Conics II: the ellipse and the hyperbola",
    "tag": "Edexcel A level FP1 4.1–4.4 (option; ellipse and hyperbola parts) · IAL FP3 2.1–2.4 · AQA D15 sketching is in Unit C4",
    "notes": [
        ("p", "Unit C4 met the parabola, defined by SP = PM. Changing the ratio SP : PM from 1 to a number e gives the other conics: an "
              "<b>ellipse</b> when e < 1 and a <b>hyperbola</b> when e > 1. This unit covers their Cartesian and parametric equations, "
              "eccentricity, foci and directrices, tangents and normals (including the condition for a line to be a tangent), and loci. "
              "You will need the hyperbolic functions of Unit B4 for the parametrisation (a cosh t, b sinh t)."),

        ("h2", "5.1 The ellipse (Ed FP1 4.1; IAL FP3 2.1)"),
        ("box", "The ellipse x²/a² + y²/b² = 1 (a > b > 0)", [
            "Centre O; it meets the axes at (±a, 0) and (0, ±b). The <b>major axis</b> has length 2a, the <b>minor axis</b> 2b.",
            "<b>Parametric form</b>: x = a cos t, y = b sin t (0 ≤ t < 2π), since cos²t + sin²t = 1.",
            "The parameter t is not the angle POx: it is the angle for the point (a cos t, a sin t) on the <b>auxiliary circle</b> "
            "x² + y² = a²; the ellipse is this circle stretched by factor b/a parallel to the y-axis.",
            "If b > a, the same formulae apply with the roles of x and y exchanged (major axis vertical).",
        ]),

        ("h2", "5.2 The hyperbola (Ed FP1 4.1; IAL FP3 2.1)"),
        ("box", "The hyperbola x²/a² − y²/b² = 1", [
            "Two branches, meeting the x-axis at (±a, 0); no y-intercepts. Asymptotes <b>y = ±(b/a)x</b>, i.e. x²/a² − y²/b² = 0.",
            "<b>Parametric form 1</b>: x = a sec t, y = b tan t, using sec²t − tan²t = 1. Values −π/2 < t < π/2 give the right branch; "
            "π/2 < t < 3π/2 give the left branch.",
            "<b>Parametric form 2</b>: x = a cosh t, y = b sinh t, using cosh²t − sinh²t = 1. Since cosh t ≥ 1 this gives only the "
            "<b>right branch</b>; use x = −a cosh t for the left branch.",
            "If a = b the hyperbola x² − y² = a² is <b>rectangular</b> (perpendicular asymptotes y = ±x); it is the curve xy = c² of "
            "Unit C4 turned through 45°, with a² = 2c².",
        ]),
        ("p", "<b>Why the asymptotes?</b> Solving for y gives y = ±(b/a)√(x² − a²) = ±(b/a)x √(1 − a²/x²). As |x| → ∞ the square root "
              "tends to 1, so the curve approaches y = ±(b/a)x."),

        ("h2", "5.3 Eccentricity, foci and directrices (Ed FP1 4.2; IAL FP3 2.2)"),
        ("p", "A conic is the locus of a point P whose distance from a fixed point S (the <b>focus</b>) is e times its distance PM from a "
              "fixed line (the <b>directrix</b>): <b>PS = e × PM</b>. The constant e > 0 is the <b>eccentricity</b>."),
        ("figure", "pc05_eccentricity.png", "Same focus S and directrix, three eccentricities: PS = e × PM.", 80),
        ("p", "<b>Derivation for the ellipse.</b> Take S(ae, 0) and directrix x = a/e with 0 < e < 1. PS² = e²PM² gives "
              "(x − ae)² + y² = e²(a/e − x)² = (a − ex)². Expanding, x² − 2aex + a²e² + y² = a² − 2aex + e²x², so "
              "x²(1 − e²) + y² = a²(1 − e²), that is x²/a² + y²/(a²(1 − e²)) = 1. Writing b² = a²(1 − e²) gives the standard ellipse. "
              "The same algebra with e > 1 gives x²/a² − y²/(a²(e² − 1)) = 1, the hyperbola with b² = a²(e² − 1). By symmetry each "
              "curve has a second focus S′(−ae, 0) and a second directrix x = −a/e."),
        ("figure", "pc05_ellipse.png", "Ellipse: foci S and S′ inside, directrices outside; PS = e·PM and PS + PS′ = 2a.", 95),
        ("figure", "pc05_hyperbola.png", "Hyperbola: foci outside the vertices, directrices between them, asymptotes y = ±(b/a)x.", 95),
        ("table", ["", "Ellipse", "Parabola", "Hyperbola", "Rectangular hyperbola"], [
            ["Standard form", "x²/a² + y²/b² = 1", "y² = 4ax", "x²/a² − y²/b² = 1", "xy = c²"],
            ["Parametric form", "(a cos t, b sin t)", "(at², 2at)", "(a sec t, b tan t), (±a cosh t, b sinh t)", "(ct, c/t)"],
            ["Eccentricity", "e < 1, b² = a²(1 − e²)", "e = 1", "e > 1, b² = a²(e² − 1)", "e = √2"],
            ["Foci", "(±ae, 0)", "(a, 0)", "(±ae, 0)", "(±√2 c, ±√2 c)"],
            ["Directrices", "x = ±a/e", "x = −a", "x = ±a/e", "x + y = ±√2 c"],
            ["Asymptotes", "none", "none", "x/a = ±y/b", "x = 0, y = 0"],
        ]),
        ("box", "Focal distance properties", [
            "Ellipse: PS = e(a/e − x) = a − ex and PS′ = a + ex, so <b>PS + PS′ = 2a</b> for every point P (a “string” property).",
            "Hyperbola (right branch, x ≥ a): PS = ex − a and PS′ = ex + a, so <b>|PS′ − PS| = 2a</b>.",
            "To find e from an equation: ellipse e² = 1 − b²/a²; hyperbola e² = 1 + b²/a².",
        ]),

        ("h2", "5.4 Tangents and normals (Ed FP1 4.3; IAL FP3 2.3)"),
        ("p", "Use implicit differentiation for a point given in coordinates, or parametric differentiation for a general point. For "
              "the ellipse, 2x/a² + (2y/b²)dy/dx = 0 gives dy/dx = −b²x/(a²y); for the hyperbola dy/dx = b²x/(a²y)."),
        ("box", "Standard results (derive them when asked to show)", [
            "Ellipse at (x₁, y₁): tangent <b>xx₁/a² + yy₁/b² = 1</b>. Hyperbola at (x₁, y₁): tangent <b>xx₁/a² − yy₁/b² = 1</b>.",
            "Ellipse at (a cos t, b sin t): gradient −b cos t/(a sin t); tangent <b>bx cos t + ay sin t = ab</b>; normal "
            "<b>ax sin t − by cos t = (a² − b²) sin t cos t</b>.",
            "Hyperbola at (a sec t, b tan t): gradient b/(a sin t); tangent <b>bx sec t − ay tan t = ab</b>; normal "
            "<b>ax sin t + by = (a² + b²) tan t</b>.",
            "Hyperbola at (a cosh t, b sinh t): gradient b cosh t/(a sinh t); tangent <b>bx cosh t − ay sinh t = ab</b>; normal "
            "<b>ax sinh t + by cosh t = (a² + b²) sinh t cosh t</b>.",
        ]),
        ("p", "<b>Derivation of the ellipse tangent.</b> dx/dt = −a sin t and dy/dt = b cos t, so dy/dx = −b cos t/(a sin t). The tangent "
              "is y − b sin t = −(b cos t/(a sin t))(x − a cos t). Multiply by a sin t: ay sin t − ab sin²t = −bx cos t + ab cos²t, so "
              "bx cos t + ay sin t = ab(sin²t + cos²t) = ab."),
        ("box", "Condition for y = mx + c to be a tangent (Ed FP1 4.3; IAL FP3 2.3)", [
            "Ellipse: substituting gives (b² + a²m²)x² + 2a²mcx + a²(c² − b²) = 0. A tangent gives a repeated root, so the "
            "discriminant is zero, which simplifies to <b>c² = a²m² + b²</b>. Contact point (−a²m/c, b²/c).",
            "Hyperbola: (b² − a²m²)x² − 2a²mcx − a²(c² + b²) = 0; repeated root ⇔ <b>c² = a²m² − b²</b>. Contact point (−a²m/c, −b²/c).",
            "Parabola y² = 4ax (Unit C4): c = a/m.",
        ]),
        ("figure", "pc05_ellipse_tangent.png", "Worked example C5.3: tangent and normal to x²/25 + y²/9 = 1 at P(4, 9/5).", 85),

        ("h2", "5.5 Loci (Ed FP1 4.4; IAL FP3 2.4)"),
        ("bullets", [
            "<b>From a distance rule</b>: write the rule in coordinates, square to remove roots, and simplify; compare with the "
            "focus–directrix form to recognise the conic and its eccentricity.",
            "<b>From a parameter</b>: express the moving point's coordinates in terms of t, then eliminate t using cos²t + sin²t = 1, "
            "sec²t − tan²t = 1 or cosh²t − sinh²t = 1.",
            "<b>From the tangency condition</b>: tangents from a point (h, k) have gradients m satisfying (k − mh)² = a²m² + b²; a "
            "condition on the gradients (such as m₁m₂ = −1) then gives a locus for (h, k).",
        ]),
        ("warn", "Common mistakes", [
            "Mixing up the eccentricity relations: b² = a²(1 − e²) for the ellipse, b² = a²(e² − 1) for the hyperbola.",
            "Putting the directrices at x = ±ae (that is where the foci are) instead of x = ±a/e.",
            "Forgetting that (a cosh t, b sinh t) traces only the right-hand branch.",
            "Treating the parameter t of the ellipse as the polar angle of P.",
            "Using c² = a²m² + b² for a hyperbola: the hyperbola condition has a minus sign.",
            "Leaving a locus in terms of the parameter, or ignoring a restriction (e.g. x > 0) that the parametrisation imposes.",
        ]),
    ],

    "examples": [
        {
            "title": "Eccentricity, foci and directrices of an ellipse",
            "question": "The ellipse E has equation 9x² + 25y² = 225. (a) Find its eccentricity, foci and directrices. (b) Show that "
                        "P(3, 12/5) lies on E and verify that PS + PS′ = 2a.",
            "steps": [
                "(a) Divide by 225: x²/25 + y²/9 = 1, so a = 5, b = 3.",
                "b² = a²(1 − e²): 9 = 25(1 − e²), e² = 16/25, e = 4/5.",
                "Foci (±ae, 0) = (±4, 0). Directrices x = ±a/e = ±25/4.",
                "(b) 9/25 + (144/25)/9 = 9/25 + 16/25 = 1, so P is on E.",
                "PS = a − ex = 5 − (4/5)(3) = 13/5 and PS′ = a + ex = 37/5 (directly: PS = √(1 + 144/25) = 13/5). Sum 50/5 = 10 = 2a.",
            ],
        },
        {
            "title": "Features of a hyperbola",
            "question": "For the hyperbola H: x²/16 − y²/9 = 1, find the eccentricity, the foci, the directrices and the asymptotes.",
            "steps": [
                "a = 4, b = 3. b² = a²(e² − 1): 9 = 16(e² − 1), e² = 25/16, e = 5/4.",
                "Foci (±ae, 0) = (±5, 0). Directrices x = ±a/e = ±16/5.",
                "Asymptotes y = ±(b/a)x = ±¾x.",
                "Check the order on the x-axis: directrix 3.2 < vertex 4 < focus 5, as in the figure for 5.3.",
            ],
        },
        {
            "title": "Tangent and normal to an ellipse",
            "question": "Find the equations of the tangent and normal to x²/25 + y²/9 = 1 at P(4, 9/5).",
            "steps": [
                "Tangent with xx₁/a² + yy₁/b² = 1: 4x/25 + (9/5)y/9 = 1, i.e. 4x/25 + y/5 = 1, so 4x + 5y = 25.",
                "Gradient of tangent −4/5, so the normal has gradient 5/4: y − 9/5 = (5/4)(x − 4).",
                "Multiply by 20: 20y − 36 = 25x − 100, so 25x − 20y = 64.",
                "Check with the parametric form: cos t = 4/5, sin t = 3/5. ax sin t − by cos t = (a² − b²) sin t cos t gives "
                "3x − (12/5)y = 16 × 12/25 = 192/25; multiplying by 25/3 gives 25x − 20y = 64.",
            ],
        },
        {
            "title": "Using the tangency condition",
            "question": "(a) Find the equations of the tangents to x²/4 + y² = 1 that pass through (0, 3). (b) Find the tangents to the "
                        "same ellipse with gradient 1.",
            "steps": [
                "a² = 4, b² = 1. A line through (0, 3) is y = mx + 3, so c = 3.",
                "(a) c² = a²m² + b²: 9 = 4m² + 1, m² = 2, m = ±√2. Tangents y = √2 x + 3 and y = −√2 x + 3.",
                "Check (m = √2): x²/4 + (√2 x + 3)² = 1 gives 9x² + 24√2 x + 32 = 0, discriminant 1152 − 1152 = 0.",
                "(b) m = 1: c² = 4 + 1 = 5, c = ±√5. Tangents y = x + √5 and y = x − √5.",
            ],
        },
        {
            "title": "A tangent to a hyperbola and its asymptotes",
            "question": "P(3 cosh t, 2 sinh t) lies on H: x²/9 − y²/4 = 1. The tangent at P meets the asymptotes at A and B. Show that "
                        "the area of triangle OAB is independent of t.",
            "figure": "pc05_asymptote_triangle.png",
            "caption": "The tangent at P cuts off triangle OAB, of area ab = 6 for every t.",
            "width_mm": 85,
            "steps": [
                "dy/dx = (2 cosh t)/(3 sinh t). Tangent: y − 2 sinh t = (2 cosh t/(3 sinh t))(x − 3 cosh t); × 3 sinh t and use "
                "cosh²t − sinh²t = 1: 2x cosh t − 3y sinh t = 6.",
                "Asymptote y = 2x/3: 2x cosh t − 2x sinh t = 6, so x = 3/(cosh t − sinh t) = 3eᵗ. A = (3eᵗ, 2eᵗ).",
                "Asymptote y = −2x/3: 2x(cosh t + sinh t) = 6, x = 3e⁻ᵗ. B = (3e⁻ᵗ, −2e⁻ᵗ).",
                "Area OAB = ½|x_A y_B − x_B y_A| = ½|3eᵗ(−2e⁻ᵗ) − 3e⁻ᵗ(2eᵗ)| = ½|−6 − 6| = 6, independent of t (and equal to ab).",
            ],
        },
        {
            "title": "A locus from a focus–directrix rule (exam standard)",
            "question": "A point P moves so that its distance from S(3, 0) is half its distance from the line x = 12. Find the "
                        "equation of the locus of P, identify the curve, and state its eccentricity and its other focus and directrix.",
            "steps": [
                "PS = ½ PM: √((x − 3)² + y²) = ½|x − 12|. Square: 4(x² − 6x + 9 + y²) = x² − 24x + 144.",
                "So 3x² + 4y² = 108, that is x²/36 + y²/27 = 1: an ellipse with a = 6, b = 3√3.",
                "Eccentricity ½ (the ratio). Check: ae = 3 is the focus and a/e = 12 is the directrix; b² = 36(1 − ¼) = 27.",
                "By symmetry the other focus is (−3, 0) and the other directrix is x = −12.",
            ],
        },
    ],

    "practice": [
        "Find the eccentricity, foci and directrices of the ellipse x²/16 + y²/7 = 1.",
        "Find the eccentricity, foci, directrices and asymptotes of the hyperbola x²/9 − y²/16 = 1.",
        "An ellipse with centre O has foci (±2, 0) and directrices x = ±8. Find its equation.",
        "A hyperbola of the form x²/a² − y²/b² = 1 has asymptotes y = ±2x and passes through (3, 4). Find its equation.",
        "Find Cartesian equations for (a) x = 4 cos t, y = 3 sin t; (b) x = 2 sec t, y = 5 tan t; (c) x = 3 cosh t, y = 2 sinh t, "
        "stating any restriction in (c).",
        "Find the equations of the tangent and normal to x²/8 + y²/2 = 1 at (2, 1).",
        "Find the equations of the tangent and normal to x²/4 − y²/3 = 1 at (4, 3).",
        "Show that the tangent to x²/a² − y²/b² = 1 at (a sec t, b tan t) has equation bx sec t − ay tan t = ab.",
        "Find the values of c for which y = 2x + c is a tangent to x²/9 + y²/4 = 1.",
        "Find the equations of the tangents to x²/9 − y²/4 = 1 that pass through (0, 2).",
        "P moves so that its distance from (4, 0) is twice its distance from the line x = 1. Show that the locus of P is a hyperbola "
        "and find its equation.",
        "A is (4, 0) and P is a variable point on x²/16 + y²/9 = 1. Find the locus of the midpoint of AP.",
    ],
    "answers": [
        "7 = 16(1 − e²): e = 3/4; foci (±3, 0); directrices x = ±16/3.",
        "16 = 9(e² − 1): e = 5/3; foci (±5, 0); directrices x = ±9/5; asymptotes y = ±(4/3)x.",
        "ae = 2, a/e = 8: a² = 16, e = ½, b² = 16 × ¾ = 12: x²/16 + y²/12 = 1.",
        "b = 2a: 9/a² − 16/(4a²) = 5/a² = 1, so a² = 5, b² = 20: x²/5 − y²/20 = 1.",
        "(a) x²/16 + y²/9 = 1. (b) x²/4 − y²/25 = 1. (c) x²/9 − y²/4 = 1 with x > 0 (right branch only; x ≥ 3).",
        "Tangent 2x/8 + y/2 = 1, i.e. x + 2y = 4. Normal gradient 2: y = 2x − 3.",
        "Tangent 4x/4 − 3y/3 = 1, i.e. x − y = 1. Normal gradient −1: x + y = 7.",
        "dy/dx = (b sec²t)/(a sec t tan t) = b/(a sin t). y − b tan t = (b/(a sin t))(x − a sec t); × a sin t: ay sin t − ab tan t sin t = "
        "bx − ab sec t; divide by cos t and use sec²t − tan²t = 1: bx sec t − ay tan t = ab(sec²t − tan²t) = ab.",
        "c² = 9 × 4 + 4 = 40, c = ±2√10.",
        "c = 2: 4 = 9m² − 4, m² = 8/9, m = ±2√2/3: y = ±(2√2/3)x + 2.",
        "(x − 4)² + y² = 4(x − 1)² gives 3x² − y² = 12, i.e. x²/4 − y²/12 = 1 (e = 2, a = 2, ae = 4, a/e = 1).",
        "Midpoint (2 + 2 cos t, (3/2) sin t): (x − 2)²/4 + 4y²/9 = 1, an ellipse with centre (2, 0).",
    ],

    "exam": [
        "The ellipse E has equation x²/a² + y²/b² = 1, where a > b > 0. P(a cos θ, b sin θ) is a general point on E.\n"
        "(a) Show that the normal to E at P has equation ax sin θ − by cos θ = (a² − b²) sin θ cos θ. [4]\n"
        "(b) The normal at P meets the x-axis at G and the y-axis at H. Show that, as θ varies, the midpoint M of GH lies on the "
        "curve 4a²x² + 4b²y² = (a² − b²)². [5]\n"
        "(c) Write down the equation of this locus when E is x²/25 + y²/9 = 1. [2]",
        "The hyperbola H has equation x²/4 − y²/5 = 1.\n"
        "(a) Find the eccentricity of H, the coordinates of its foci S and S′, and the equations of its directrices. [4]\n"
        "(b) P is a point on the right branch of H. Using the focus–directrix property, show that PS′ − PS = 4. [3]\n"
        "(c) Find the equations of the tangents to H that are parallel to the line y = 3x/2. [3]\n"
        "(d) Find the coordinates of the points of contact of these tangents. [2]",
        "The ellipse E has equation x²/a² + y²/b² = 1.\n"
        "(a) Show that the line y = mx + c is a tangent to E if and only if c² = a²m² + b². [4]\n"
        "(b) Hence show that the gradients m of the tangents to E from the point (h, k), with h ≠ ±a, satisfy "
        "(h² − a²)m² − 2hkm + k² − b² = 0. [3]\n"
        "(c) Deduce that if the two tangents from (h, k) are perpendicular, then (h, k) lies on the circle x² + y² = a² + b². [3]",
    ],
    "exam_answers": [
        "(a) dy/dx = (b cos θ)/(−a sin θ) M1; normal gradient a sin θ/(b cos θ) A1; y − b sin θ = (a sin θ/(b cos θ))(x − a cos θ) M1; "
        "× b cos θ: by cos θ − b² sin θ cos θ = ax sin θ − a² sin θ cos θ, giving the result. A1\n"
        "(b) y = 0: G((a² − b²) cos θ/a, 0); x = 0: H(0, −(a² − b²) sin θ/b) M1 A1. M = ((a² − b²) cos θ/(2a), −(a² − b²) sin θ/(2b)) A1. "
        "cos θ = 2ax/(a² − b²), sin θ = −2by/(a² − b²) M1; cos²θ + sin²θ = 1 gives 4a²x² + 4b²y² = (a² − b²)². A1\n"
        "(c) a² − b² = 16: 100x² + 36y² = 256, i.e. 25x² + 9y² = 64. M1 A1",
        "(a) 5 = 4(e² − 1) M1, e = 3/2 A1; foci (±3, 0) A1; directrices x = ±4/3. A1\n"
        "(b) PS = e × (x − 4/3) = 3x/2 − 2 and PS′ = e(x + 4/3) = 3x/2 + 2 M1 A1; difference 4 (= 2a). A1\n"
        "(c) c² = a²m² − b² = 4 × 9/4 − 5 = 4 M1 A1; y = 3x/2 + 2 and y = 3x/2 − 2. A1\n"
        "(d) (−a²m/c, −b²/c): c = 2 gives (−3, −5/2); c = −2 gives (3, 5/2). B1 B1",
        "(a) Substitute: b²x² + a²(mx + c)² = a²b² M1, so (b² + a²m²)x² + 2a²mcx + a²(c² − b²) = 0 A1. Tangent ⇔ repeated root ⇔ "
        "4a⁴m²c² − 4a²(b² + a²m²)(c² − b²) = 0 M1 ⇔ 4a²b²(a²m² + b² − c²) = 0 ⇔ c² = a²m² + b². A1\n"
        "(b) Through (h, k): c = k − mh M1; (k − mh)² = a²m² + b² M1; expand: (h² − a²)m² − 2hkm + k² − b² = 0. A1\n"
        "(c) Perpendicular: m₁m₂ = −1 B1; product of roots (k² − b²)/(h² − a²) = −1 M1; so h² + k² = a² + b². A1",
    ],
}
