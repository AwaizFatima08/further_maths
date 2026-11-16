"""Unit C4: Conics I, the parabola and the rectangular hyperbola."""

UNIT = {
    "number": "C4",
    "title": "Conics I: the parabola and the rectangular hyperbola",
    "tag": "Edexcel AS FP1 2.1–2.5 and A level FP1 4.1–4.4 (parabola and rectangular hyperbola parts; options) · IAL FP1 4.1–4.4 · "
           "AQA D15 (AS: sketching the four standard conics only, section 4.1)",
    "notes": [
        ("p", "The <b>conics</b> are the curves you get by slicing a double cone with a plane: the circle, ellipse, parabola and "
              "hyperbola. This unit studies the parabola y² = 4ax and the rectangular hyperbola xy = c² in detail: their "
              "parametric forms, the focus–directrix property of the parabola, tangents and normals, and simple loci. Unit C5 "
              "does the same for the ellipse and the general hyperbola. AQA students need only section 4.1."),

        ("h2", "4.1 The four standard conics and their sketches (AQA D15; all boards)"),
        ("figure", "pc04_four_conics.png", "The four standard conics, with intercepts and asymptotes.", 130),
        ("table", ["Conic", "Equation", "Intercepts", "Asymptotes", "Symmetry"], [
            ["Parabola", "y² = 4ax (a > 0)", "(0, 0) only", "none", "x-axis"],
            ["Ellipse", "x²/a² + y²/b² = 1", "(±a, 0), (0, ±b)", "none", "both axes"],
            ["Hyperbola", "x²/a² − y²/b² = 1", "(±a, 0); none on the y-axis", "y = ±(b/a)x", "both axes"],
            ["Rectangular hyperbola", "xy = c²", "none", "x = 0 and y = 0", "y = x and y = −x"],
        ]),
        ("bullets", [
            "<b>Parabola</b>: x = y²/(4a) ≥ 0, so the curve lies to the right of the y-axis, opening rightwards with vertex O.",
            "<b>Ellipse</b>: |x| ≤ a and |y| ≤ b. If a = b it is the circle x² + y² = a². If b > a the long axis is vertical.",
            "<b>Hyperbola</b>: x²/a² = 1 + y²/b² ≥ 1, so |x| ≥ a and there are two branches. For large |x|, y ≈ ±(b/a)x; sketch the "
            "asymptotes first as dashed lines through O.",
            "<b>Rectangular hyperbola</b>: y = c²/x, the reciprocal graph scaled, in the first and third quadrants, with the axes as "
            "asymptotes. It passes through (c, c) and (−c, −c). Its asymptotes are perpendicular, hence “rectangular”.",
            "AQA sketches must show intercepts and the equations of asymptotes. Translations such as (x − 2)² /9 + y²/4 = 1 move "
            "the centre to (2, 0); stretches change a and b (link with Unit A13 curve sketching).",
        ]),

        ("h2", "4.2 The parabola y² = 4ax and its focus–directrix property (Ed AS FP1 2.1, 2.3; IAL 4.1, 4.3)"),
        ("p", "A <b>parabola</b> is the locus of points that are the same distance from a fixed point, the <b>focus</b> S, and a fixed "
              "line, the <b>directrix</b>. With S(a, 0) and directrix x = −a, a point P(x, y) is at distance √((x − a)² + y²) from S "
              "and at distance x + a from the directrix (measured along PM, perpendicular to the directrix)."),
        ("figure", "pc04_parabola_focus.png", "For every point P of the parabola, SP = PM.", 85),
        ("box", "The parabola y² = 4ax", [
            "Focus S(a, 0); directrix x = −a; vertex O; axis of symmetry the x-axis.",
            "<b>Derivation</b>: SP² = PM² gives (x − a)² + y² = (x + a)², so x² − 2ax + a² + y² = x² + 2ax + a², that is y² = 4ax.",
            "<b>Focal distance</b>: SP = PM = x + a for any point P(x, y) on the curve.",
            "<b>Parametric form</b>: x = at², y = 2at. Check: (2at)² = 4a²t² = 4a(at²). Each value of t gives one point, and "
            "t = y/(2a).",
        ]),
        ("p", "To identify a parabola, write it as y² = 4ax and read off a: y² = 12x has 4a = 12, a = 3, focus (3, 0) and directrix "
              "x = −3. The <b>eccentricity</b> of every parabola is 1 (ratio SP : PM = 1); this links to the ellipse and hyperbola in Unit C5."),

        ("h2", "4.3 The rectangular hyperbola xy = c² (Ed AS FP1 2.1–2.2; IAL 4.1)"),
        ("box", "The rectangular hyperbola xy = c²", [
            "<b>Parametric form</b>: x = ct, y = c/t (t ≠ 0). Check: ct × c/t = c².",
            "t > 0 gives the branch in the first quadrant; t < 0 gives the third-quadrant branch.",
            "Asymptotes: the coordinate axes. Vertices (c, c) and (−c, −c), at t = ±1.",
            "It is the hyperbola x² − y² = 2c² rotated through 45°, so its eccentricity is √2 and its foci are (±c√2, ±c√2). "
            "(Foci and directrices of xy = c² are “not required” by Edexcel and IAL.)",
        ]),

        ("h2", "4.4 Tangents and normals (Ed AS FP1 2.4, A level FP1 4.3; IAL 4.4)"),
        ("p", "Find the gradient by any of three methods; IAL FP1 expects the first, and does not require parametric differentiation."),
        ("bullets", [
            "<b>Explicit</b>: y = 2√a x^½ gives dy/dx = √a x^(−½) (upper half); y = c²/x gives dy/dx = −c²/x².",
            "<b>Implicit</b>: 2y dy/dx = 4a gives dy/dx = 2a/y (Edexcel allows this to be quoted); x dy/dx + y = 0 gives dy/dx = −y/x.",
            "<b>Parametric</b>: dy/dx = (dy/dt)/(dx/dt). For (at², 2at): 2a/(2at) = 1/t. For (ct, c/t): (−c/t²)/c = −1/t².",
            "The <b>normal</b> is perpendicular to the tangent, so its gradient is −1/(tangent gradient).",
        ]),
        ("box", "Standard tangents and normals (derive them; do not just quote)", [
            "Parabola at P(at², 2at): tangent <b>ty = x + at²</b>; normal <b>y + tx = 2at + at³</b>.",
            "Rectangular hyperbola at P(ct, c/t): tangent <b>x + t²y = 2ct</b>; normal <b>t³x − ty = c(t⁴ − 1)</b>.",
            "Derivation of the parabola tangent: y − 2at = (1/t)(x − at²); multiply by t: ty − 2at² = x − at², so ty = x + at².",
            "Derivation of the hyperbola normal: gradient t², so y − c/t = t²(x − ct); multiply by t: ty − c = t³x − ct⁴, so "
            "t³x − ty = ct⁴ − c.",
        ]),
        ("p", "<b>Second intersections.</b> To find where a normal meets the curve again, substitute the curve's parametric form into "
              "the line and solve. Because the known point is a root, the resulting equation factorises. For the normal to y² = 4ax at "
              "t, substituting (as², 2as) gives a(s − t)(ts + t² + 2) = 0, so the normal meets the curve again at s = −t − 2/t. For "
              "xy = c² the normal at t meets the curve again at s = −1/t³."),
        ("box", "Condition for y = mx + k to be a tangent (Ed AS FP1 2.4, A level FP1 4.3)", [
            "Parabola y² = 4ax: substitute x = (y − k)/m to get my² − 4ay + 4ak = 0. A tangent meets the curve at exactly one point, so "
            "the discriminant is zero: 16a² − 16amk = 0, giving <b>k = a/m</b>. The point of contact is (a/m², 2a/m).",
            "Rectangular hyperbola xy = c²: x(mx + k) = c² gives mx² + kx − c² = 0; discriminant zero gives <b>k² + 4mc² = 0</b>, so a "
            "tangent must have m < 0.",
            "Edexcel writes y = mx + c; for the hyperbola we use k to avoid a clash with the constant c in xy = c².",
        ]),
        ("figure", "pc04_parabola_tangent.png", "Worked example C4.2: tangent and normal to y² = 8x at P(2, 4); the normal meets the curve again at Q.", 90),

        ("h2", "4.5 Simple loci (Ed AS FP1 2.5, A level FP1 4.4; IAL 4.1)"),
        ("p", "A <b>locus</b> is the path of a point that moves according to a rule. With parameters the method is always the same:"),
        ("bullets", [
            "Write the coordinates of the moving point in terms of the parameter t: x = f(t), y = g(t).",
            "Eliminate t (often t from the simpler equation, substituted into the other) to get a Cartesian equation.",
            "Describe the locus in words if asked (for example “a parabola with vertex (a/2, 0)”), and note any restrictions.",
        ]),
        ("box", "Useful results for P(ap², 2ap) and Q(aq², 2aq) on y² = 4ax", [
            "Chord PQ: gradient 2/(p + q), equation (p + q)y = 2x + 2apq.",
            "PQ passes through the focus S(a, 0) (a <b>focal chord</b>) exactly when pq = −1.",
            "Tangents at P and Q meet at R(apq, a(p + q)).",
            "So the tangents at the ends of a focal chord meet on the directrix x = −a, and are perpendicular (gradients 1/p and 1/q "
            "multiply to 1/(pq) = −1).",
        ]),
        ("figure", "pc04_focal_chord.png", "Tangents at the ends of a focal chord PQ meet at R on the directrix.", 85),
        ("warn", "Common mistakes", [
            "Reading the focus of y² = 12x as (12, 0): the focus is (a, 0) where 4a = 12.",
            "Using dy/dx = 1/t for the rectangular hyperbola (it is −1/t²), or forgetting that the normal gradient is the negative reciprocal.",
            "Dividing by t when t might be zero, or by (s − t) without saying s ≠ t.",
            "Giving a locus in terms of t: the answer must be an equation in x and y only.",
            "Writing the second point of a normal by guesswork instead of solving and factorising.",
            "Sketches without the asymptote equations, intercepts or the correct shape near the vertex (a parabola is not V-shaped).",
        ]),
    ],

    "examples": [
        {
            "title": "Focus, directrix and focal distance",
            "question": "The parabola C has equation y² = 12x. (a) Write down the focus and directrix of C. (b) The point P on C has "
                        "x-coordinate 3. Find the possible coordinates of P and verify that SP equals the distance from P to the directrix. "
                        "(c) Write down a parametric form of C.",
            "steps": [
                "(a) 4a = 12, so a = 3. Focus S(3, 0); directrix x = −3.",
                "(b) y² = 36, so P = (3, 6) or (3, −6).",
                "SP = √((3 − 3)² + 6²) = 6; distance to x = −3 is 3 − (−3) = 6. They agree, as SP = x + a = 3 + 3.",
                "(c) x = 3t², y = 6t.",
            ],
        },
        {
            "title": "Tangent and normal to a parabola, and a second intersection",
            "question": "Find the equations of the tangent and the normal to y² = 8x at P(2, 4). The normal meets the curve again at Q. "
                        "Find Q.",
            "steps": [
                "Implicit differentiation: 2y dy/dx = 8, so dy/dx = 4/y = 1 at P.",
                "Tangent: y − 4 = 1(x − 2), so y = x + 2. (Check with ty = x + at², a = 2, t = 1: y = x + 2.)",
                "Normal: gradient −1, so y − 4 = −(x − 2), that is x + y = 6.",
                "Substitute x = y²/8: y²/8 + y = 6, so y² + 8y − 48 = 0, (y + 12)(y − 4) = 0.",
                "y = 4 is P, so y = −12 and x = 144/8 = 18. Q = (18, −12). (Check: s = −t − 2/t = −3 gives (2 × 9, 4 × (−3)) = (18, −12).)",
            ],
        },
        {
            "title": "Deriving the general tangent and normal to y² = 4ax",
            "question": "Show that the tangent to y² = 4ax at P(at², 2at) is ty = x + at², and find the equation of the normal at P. "
                        "Find also the point where the tangent meets the x-axis.",
            "steps": [
                "dx/dt = 2at, dy/dt = 2a, so dy/dx = 2a/(2at) = 1/t (t ≠ 0).",
                "Tangent: y − 2at = (1/t)(x − at²). Multiply by t: ty − 2at² = x − at², so ty = x + at². (This also holds at t = 0, "
                "where the tangent is x = 0.)",
                "Normal: gradient −t, so y − 2at = −t(x − at²), giving y + tx = 2at + at³.",
                "Tangent meets the x-axis where y = 0: x = −at², the point (−at², 0).",
            ],
        },
        {
            "title": "Tangent and normal to a rectangular hyperbola",
            "question": "The rectangular hyperbola H has equation xy = 16. Find the equations of the tangent and normal to H at the point "
                        "P with parameter t = 2, and the point Q where the normal meets H again.",
            "figure": "pc04_rect_hyperbola_tangent.png",
            "caption": "Tangent and normal to xy = 16 at P(8, 2); the normal meets the other branch at Q.",
            "width_mm": 85,
            "steps": [
                "c² = 16, c = 4, so P = (ct, c/t) = (8, 2).",
                "y = 16/x gives dy/dx = −16/x² = −1/4 at P. Tangent: y − 2 = −¼(x − 8), so x + 4y = 16.",
                "Normal: gradient 4: y − 2 = 4(x − 8), so 4x − y = 30. (Check with t³x − ty = c(t⁴ − 1): 8x − 2y = 60.)",
                "Substitute y = 16/x: 4x − 16/x = 30, so 4x² − 30x − 16 = 0, 2x² − 15x − 8 = 0, (2x + 1)(x − 8) = 0.",
                "x = 8 is P, so x = −½ and y = −32. Q = (−½, −32), which is on the other branch.",
            ],
        },
        {
            "title": "Using the tangency condition",
            "question": "(a) Find k so that y = 2x + k is a tangent to y² = 8x, and find the point of contact. (b) Find the gradient m for "
                        "which y = mx + 3 is a tangent to y² = 12x.",
            "steps": [
                "(a) Substitute x = (y − k)/2: y² = 4(y − k), so y² − 4y + 4k = 0. For a tangent the discriminant is zero: 16 − 16k = 0, k = 1.",
                "Then y² − 4y + 4 = 0 gives y = 2, x = ½: contact point (½, 2). (Agrees with k = a/m = 2/2 and (a/m², 2a/m).)",
                "(b) a = 3 and k = a/m: 3 = 3/m, so m = 1. Check: y² = 12x and y = x + 3 give x² − 6x + 9 = 0 = (x − 3)², a repeated root.",
            ],
        },
        {
            "title": "A locus problem with a rectangular hyperbola (exam standard)",
            "question": "P(cp, c/p) and Q(cq, c/q) are points on xy = c², p ≠ q. (a) Show that the tangents at P and Q meet at "
                        "R(2cpq/(p + q), 2c/(p + q)). (b) Given that the chord PQ is parallel to the line y = −x, show that R lies on y = x.",
            "steps": [
                "(a) Tangents: x + p²y = 2cp and x + q²y = 2cq. Subtract: (p² − q²)y = 2c(p − q).",
                "Divide by p − q ≠ 0: (p + q)y = 2c, so y = 2c/(p + q). Then x = 2cp − p² × 2c/(p + q) = 2cp(p + q − p)/(p + q) = 2cpq/(p + q).",
                "(b) Gradient of PQ = (c/q − c/p)/(cq − cp) = (p − q)/(pq) ÷ (q − p) = −1/(pq).",
                "Parallel to y = −x means −1/(pq) = −1, so pq = 1.",
                "Then R = (2c/(p + q), 2c/(p + q)): its x- and y-coordinates are equal, so R lies on y = x.",
            ],
        },
    ],

    "practice": [
        "Write down the focus and the equation of the directrix of the parabola y² = 20x.",
        "Find the equation of the parabola with focus (2, 0) and directrix x = −2, by using the focus–directrix definition.",
        "Find Cartesian equations of the curves (a) x = 3t², y = 6t; (b) x = 5t, y = 5/t.",
        "P lies on y² = 16x and has x-coordinate 9. Find the distance from P to the focus.",
        "(AQA) Sketch the curves (a) x²/9 + y²/4 = 1, (b) x²/16 − y²/9 = 1, (c) y² = 6x, (d) xy = 9, showing intercepts and the "
        "equations of any asymptotes.",
        "Find the equations of the tangent and the normal to y² = 4x at (4, 4).",
        "Find the equations of the tangent and the normal to xy = 9 at (9, 1).",
        "Show that the tangent to xy = c² at (ct, c/t) has equation x + t²y = 2ct.",
        "Find k such that y = 3x + k is a tangent to y² = 24x, and find the point of contact.",
        "Find the values of k for which y = −x + k is a tangent to xy = 4.",
        "S is the focus of y² = 4ax and P(at², 2at) is a point on the curve. Find the locus of the midpoint of SP.",
        "The normal to y² = 4ax at P(at², 2at) meets the x-axis at G. Find the locus of the midpoint of PG as t varies.",
    ],
    "answers": [
        "4a = 20, a = 5: focus (5, 0), directrix x = −5.",
        "(x − 2)² + y² = (x + 2)² gives y² = 8x.",
        "(a) y² = 12x. (b) xy = 25.",
        "a = 4: SP = x + a = 13.",
        "(a) Ellipse through (±3, 0), (0, ±2). (b) Hyperbola through (±4, 0), asymptotes y = ±¾x. (c) Parabola through O, focus "
        "(3/2, 0), opening right. (d) Rectangular hyperbola in quadrants 1 and 3 through (3, 3) and (−3, −3), asymptotes the axes.",
        "a = 1, t = 2: tangent 2y = x + 4; normal y + 2x = 12.",
        "c = 3, t = 3: gradient −1/9; tangent x + 9y = 18; normal 9x − y = 80.",
        "dy/dx = (−c/t²)/c = −1/t². y − c/t = −(1/t²)(x − ct); multiply by t²: t²y − ct = −x + ct, so x + t²y = 2ct.",
        "a = 6, k = a/m = 2; contact (a/m², 2a/m) = (2/3, 4).",
        "x(−x + k) = 4 gives x² − kx + 4 = 0; k² − 16 = 0, k = ±4.",
        "Midpoint ((a + at²)/2, at). t = y/a, so 2x = a + y²/a: y² = 2ax − a² = 2a(x − a/2), a parabola with vertex (a/2, 0).",
        "Normal y + tx = 2at + at³ meets y = 0 at G(2a + at², 0). Midpoint (a + at², at): t = y/a, x = a + y²/a, so y² = a(x − a).",
    ],

    "exam": [
        "The points P(ap², 2ap) and Q(aq², 2aq), p ≠ q, lie on the parabola y² = 4ax, whose focus is S.\n"
        "(a) Show that the tangent at P has equation py = x + ap². [3]\n"
        "(b) The tangents at P and Q meet at R. Show that R has coordinates (apq, a(p + q)). [3]\n"
        "(c) Show that the chord PQ has equation (p + q)y = 2x + 2apq, and deduce that if PQ passes through S then pq = −1. [3]\n"
        "(d) Hence show that when PQ passes through S, R lies on the directrix and the tangents at P and Q are perpendicular. [3]",
        "The rectangular hyperbola H has equation xy = 25. The point P(5t, 5/t), t > 0, lies on H.\n"
        "(a) Show that the normal to H at P has equation t³x − ty = 5(t⁴ − 1). [4]\n"
        "(b) The normal at the point where t = ½ meets H again at Q. Find the coordinates of Q. [4]\n"
        "(c) The tangent to H at P meets the x-axis at A and the y-axis at B. Show that the area of triangle OAB does not depend on t. [3]",
        "(a) Show that the line y = mx + k (m ≠ 0) is a tangent to the parabola y² = 4ax if and only if k = a/m. [4]\n"
        "(b) Find the equations of the two tangents to y² = 8x that pass through the point (−1, 1), and their points of contact. [5]\n"
        "(c) Find, to 0.1°, the acute angle between these two tangents. [2]",
    ],
    "exam_answers": [
        "(a) dy/dx = 2a/y = 1/p M1 A1; y − 2ap = (1/p)(x − ap²) gives py = x + ap². A1\n"
        "(b) py = x + ap², qy = x + aq²; subtract: (p − q)y = a(p² − q²), y = a(p + q) M1 A1; then x = pa(p + q) − ap² = apq. A1\n"
        "(c) Gradient (2ap − 2aq)/(ap² − aq²) = 2/(p + q) M1; y − 2ap = 2(x − ap²)/(p + q) gives (p + q)y = 2x + 2apq A1; "
        "through (a, 0): 0 = 2a + 2apq, so pq = −1. A1\n"
        "(d) x-coordinate of R is apq = −a, so R is on x = −a. B1 Tangent gradients 1/p, 1/q M1; product 1/(pq) = −1, so perpendicular. A1",
        "(a) dy/dx = (−5/t²)/5 = −1/t² M1, normal gradient t² A1; y − 5/t = t²(x − 5t) M1; × t: t³x − ty = 5t⁴ − 5. A1\n"
        "(b) t = ½: P(5/2, 10); normal x/8 − y/2 = −75/16, i.e. 2x − 8y + 75 = 0. M1 A1 With y = 25/x: 2x² + 75x − 200 = 0, "
        "(2x − 5)(x + 40) = 0 M1; Q(−40, −5/8). A1\n"
        "(c) Tangent x + t²y = 10t M1: A(10t, 0), B(0, 10/t) A1; area = ½ × 10t × 10/t = 50, independent of t. A1",
        "(a) x = (y − k)/m: my² − 4ay + 4ak = 0 M1. Tangent ⇔ repeated root ⇔ discriminant 16a² − 16amk = 0 M1 A1 ⇔ k = a/m (a ≠ 0). A1\n"
        "(b) a = 2. Line through (−1, 1): k = 1 + m M1; 1 + m = 2/m M1, m² + m − 2 = 0, m = 1 or m = −2 A1. Tangents y = x + 2 and "
        "y = −2x − 1 A1; contacts (a/m², 2a/m) = (2, 4) and (½, −2). A1\n"
        "(c) tan θ = |(1 − (−2))/(1 + (1)(−2))| = 3 M1; θ = 71.6°. A1",
    ],
}
