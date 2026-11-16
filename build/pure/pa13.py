"""Unit A13: Curve sketching, rational functions and inequalities (AQA D8-D14, D16, CAIE 1.2, Ed FP1 7.1 / AS FP1 5.1,
IAL FP2 1.1)."""

UNIT = {
    "number": "A13",
    "title": "Curve sketching, rational functions and inequalities",
    "tag": "AQA D8, D9, D12, D14 (AS), D13 and D16 (AS; oblique asymptotes and composite transformations A), D10, D11 (A) · "
           "CAIE 9231 P1 1.2 · Edexcel FP1 7.1 (A level option), AS FP1 5.1 (no modulus) · IAL FP2 1.1 · "
           "not on OCR A or OCR MEI",
    "notes": [
        ("p", "A sketch is not an accurate plot. It shows the shape of a curve and its significant features: where it "
              "meets the axes, its asymptotes, its turning points and how it behaves near the asymptotes and for large |x|. "
              "This unit covers sketching rational functions (a polynomial divided by a polynomial) and the related "
              "curves y = |f(x)|, y = 1/f(x) and y² = f(x), transforming curves, and solving inequalities algebraically. "
              "A sketch and an algebraic solution support each other: the sketch tells you what to expect, the algebra "
              "gives exact values."),

        ("h2", "13.1 Graphs of y = (ax + b)/(cx + d) (AQA D12, CAIE)"),
        ("bullets", [
            "<b>Vertical asymptote</b> where the denominator is zero: x = −d/c. Near it, y → ±∞; check the sign on each "
            "side.",
            "<b>Horizontal asymptote</b>: as x → ±∞, y → a/c (divide top and bottom by x).",
            "<b>Intercepts</b>: y-axis at (0, b/d); x-axis where ax + b = 0, at (−b/a, 0).",
            "The curve is a rectangular hyperbola: dividing gives y = a/c + k/(cx + d) for a constant k, which is y = 1/x "
            "stretched and translated. It has no turning points, so each branch is increasing or each is decreasing.",
            "Intersections with a line y = mx + c: solve (ax + b) = (mx + c)(cx + d), a quadratic. This links sketches to "
            "inequalities (13.6).",
        ]),
        ("figure", "pa13_linear.png", "y = (2x + 1)/(x − 3): asymptotes x = 3 and y = 2; intercepts (0, −1/3) and (−1/2, 0).",
         100),

        ("h2", "13.2 Quadratic over quadratic, and oblique asymptotes (AQA D13, CAIE)"),
        ("p", "For y = (ax² + bx + c)/(dx² + ex + f), possibly with some coefficients zero:"),
        ("bullets", [
            "Vertical asymptotes at real zeros of the denominator (unless the numerator is zero there too, when the factor "
            "cancels and the graph has a hole). A quadratic denominator gives 0, 1 or 2 vertical asymptotes.",
            "If the degrees of numerator and denominator are equal, the horizontal asymptote is y = (leading coefficient "
            "of top)/(leading coefficient of bottom). If the top has lower degree, it is y = 0.",
            "<b>Oblique asymptote (AQA A level, CAIE)</b>: if the top has degree one more than the bottom, divide: "
            "y = mx + k + R(x), where R(x) → 0 as x → ±∞. The line y = mx + k is the asymptote. The sign of R(x) tells "
            "you whether the curve is above or below it.",
            "A curve may cross a horizontal or oblique asymptote (it can never cross a vertical one). To find where, set "
            "the function equal to the asymptote and solve.",
            "Sign analysis: the factors of the top and bottom tell you the sign of y in each interval, so you know which "
            "way each branch goes at an asymptote.",
        ]),

        ("h2", "13.3 Range and turning points without calculus (AQA D14, CAIE)"),
        ("p", "To find the set of values that y = f(x) can take, put y = k and ask for which k the equation f(x) = k has a "
              "real solution. Multiplying out gives a quadratic in x; it has real roots exactly when its discriminant is "
              "≥ 0. Solving that inequality in k gives the range."),
        ("box", "The discriminant method", [
            "Write y = N(x)/D(x), rearrange to y D(x) − N(x) = 0, a quadratic Ax² + Bx + C = 0 whose coefficients involve y.",
            "Real x exists ⇔ B² − 4AC ≥ 0. Solve this inequality for y: this is the range (exclude values where A = 0 "
            "only if they fail separately).",
            "At an end-point of the range the quadratic has a repeated root x = −B/(2A): that point is a turning point. "
            "So the method gives the turning points' coordinates without differentiating.",
            "If the range is y ≤ p or y ≥ q, the curve takes no values strictly between p and q.",
        ]),
        ("figure", "pa13_range.png", "y = (x + 1)/(x² + 3) takes every value from −1/6 to 1/2 and no others (Worked example 2).",
         100),

        ("h2", "13.4 Graphs of |f(x)|, 1/f(x) and y² = f(x) (AQA D10–D11 A level; CAIE 1.2)"),
        ("table", ["New curve", "How to get it from y = f(x)"], [
            ["y = |f(x)|", "Keep the parts on or above the x-axis; reflect the parts below the x-axis in the x-axis. "
                           "Sharp corners appear where f crosses the axis."],
            ["y = 1/f(x)", "Same sign as f. Zeros of f become vertical asymptotes; vertical asymptotes of f become zeros "
                           "(approached, the curve meets the axis); y → 0 where f → ±∞. A maximum of f becomes a minimum "
                           "with y-value 1/(value), and vice versa. Points with f = ±1 are unchanged."],
            ["y² = f(x) (CAIE)", "Exists only where f(x) ≥ 0. It is y = ±√f(x): symmetric about the x-axis. Where f(x) = 0 "
                                 "at a simple root, the curve crosses the x-axis vertically. Values of f between 0 and 1 "
                                 "get larger (√0.25 = 0.5); values above 1 get smaller. Asymptote y = c with c > 0 becomes "
                                 "y = ±√c. Turning points of f with f > 0 stay at the same x."],
        ]),
        ("figure", "pa13_ysq.png", "f(x) = (x + 1)(x − 1)(x − 3). The curve y² = f(x) is a closed loop over −1 ≤ x ≤ 1 (where "
                                   "f ≥ 0) and an open branch for x ≥ 3; it is vertical where it meets the x-axis.", 150),
        ("p", "These sketches are used to solve equations and inequalities. For example, |f(x)| = k has as many solutions "
              "as there are intersections of y = |f(x)| with y = k; and |f(x)| > k is where the curve lies above the line."),

        ("h2", "13.5 Transformations of curves (AQA D16; CAIE uses them informally)"),
        ("table", ["Transformation", "Replace", "y = f(x) becomes"], [
            ["Translation by (p, q)ᵀ", "x by x − p, y by y − q", "y = f(x − p) + q"],
            ["Stretch, scale factor s, parallel to the y-axis", "y by y/s", "y = s f(x)"],
            ["Stretch, scale factor s, parallel to the x-axis", "x by x/s", "y = f(x/s)"],
            ["Reflection in the x-axis", "y by −y", "y = −f(x)"],
            ["Reflection in the y-axis", "x by −x", "y = f(−x)"],
            ["Reflection in y = x", "swap x and y", "x = f(y)"],
            ["Reflection in y = −x", "x by −y and y by −x", "−x = f(−y)"],
            ["Enlargement, centre O, scale factor s (A level)", "x by x/s and y by y/s", "y/s = f(x/s)"],
            ["Rotation 90° anticlockwise about O (A level)", "x by y and y by −x", "−x = f(y)"],
        ]),
        ("p", "The rule: to apply a transformation to a curve, replace x and y in its equation by the expressions for the "
              "<i>original</i> coordinates in terms of the new ones (the inverse map). For a composite transformation "
              "(AQA A level) do one transformation at a time, in order. Rational functions are often best described "
              "this way: y = (2x + 1)/(x − 3) = 2 + 7/(x − 3) is y = 1/x stretched by scale factor 7 parallel to the y-axis, "
              "then translated by (3, 2)ᵀ."),

        ("h2", "13.6 Solving inequalities algebraically (AQA D8–D10, Edexcel FP1, IAL FP2, CAIE)"),
        ("p", "<b>Polynomial inequalities (AQA D8).</b> Bring everything to one side, factorise fully and find the "
              "critical values (the roots). Draw a sign diagram or a sketch of the polynomial: a cubic with positive "
              "leading coefficient is negative to the left of its smallest root and the sign changes at each simple root."),
        ("p", "<b>Rational inequalities.</b> Never multiply both sides by an expression that might be negative: the "
              "inequality would reverse for some x and not others. Two safe methods:"),
        ("bullets", [
            "<b>Multiply by the square of the denominator</b>, which is positive (where it is defined). E.g. for "
            "(x + 3)/(x − 1) ≥ x − 3, multiply by (x − 1)²: (x + 3)(x − 1) ≥ (x − 3)(x − 1)², then collect terms and "
            "factorise: (x − 1)[(x + 3) − (x − 3)(x − 1)] ≥ 0.",
            "<b>Move everything to one side</b> and combine into a single fraction N(x)/D(x) > 0, then use a sign table "
            "of the factors of N and D.",
            "Critical values are the zeros of N and of D. Values making D = 0 are always excluded, even with ≥ or ≤.",
            "Check your answer against a sketch of both sides (graphs of the two sides meet at the zeros of N).",
        ]),
        ("p", "<b>Modulus inequalities (Edexcel FP1 A level, IAL FP2, AQA A level, CAIE).</b> Useful facts:"),
        ("box", "Modulus inequalities", [
            "|A| < B ⇔ −B < A < B.   |A| > B ⇔ A > B or A < −B.",
            "If both sides are non-negative, |A| < |B| ⇔ A² < B². (Squaring is safe only when both sides are ≥ 0.)",
            "Otherwise sketch both sides, find the critical values by solving the equations on each piece of the "
            "modulus, and read the solution set from the sketch.",
        ]),
        ("warn", "Common mistakes", [
            "Multiplying an inequality by x − a (or any expression that can be negative) without considering the sign.",
            "Including a value that makes a denominator zero in a “≤” or “≥” solution.",
            "Sketches without asymptotes drawn and labelled with their equations, or without intercepts. Examiners want "
            "the behaviour at each asymptote (which way each branch goes) and the coordinates of turning points.",
            "Drawing a curve crossing a vertical asymptote, or failing to notice it can cross a horizontal one.",
            "For y² = f(x), drawing parts where f(x) < 0, or drawing a sharp point instead of a vertical tangent where "
            "the curve meets the x-axis.",
            "CAIE reports: for |f(x)| inequalities, missing an isolated solution such as x = 0, and writing "
            "overlapping regions. Give the final answer as clear, non-overlapping intervals.",
            "Squaring both sides of an inequality when one side can be negative.",
        ]),
    ],
    "examples": [
        {
            "title": "Sketching (ax + b)/(cx + d) and finding intersections",
            "question": "Sketch y = (2x + 1)/(x − 3), showing its asymptotes and intercepts. Find the coordinates of the "
                        "points where the curve meets the line y = x + 1.",
            "figure": "pa13_linear.png",
            "caption": "y = (2x + 1)/(x − 3)",
            "width_mm": 90,
            "steps": [
                "Vertical asymptote x = 3. Horizontal asymptote y = 2 (divide top and bottom by x).",
                "Intercepts: x = 0 gives y = −1/3; y = 0 gives x = −1/2.",
                "Behaviour: y = 2 + 7/(x − 3). For x just above 3, y → +∞; just below 3, y → −∞. For large positive x the "
                "curve is above y = 2, and for large negative x it is below.",
                "Intersection with y = x + 1: 2x + 1 = (x + 1)(x − 3) = x² − 2x − 3, so x² − 4x − 4 = 0 and "
                "x = 2 ± 2√2.",
                "Points: (2 + 2√2, 3 + 2√2) and (2 − 2√2, 3 − 2√2), approximately (4.83, 5.83) and (−0.828, 0.172).",
            ],
        },
        {
            "title": "Range and turning points by the discriminant",
            "question": "Find the set of values taken by y = (x + 1)/(x² + 3), and hence the coordinates of its turning "
                        "points. Sketch the curve.",
            "figure": "pa13_range.png",
            "caption": "y = (x + 1)/(x² + 3)",
            "width_mm": 95,
            "steps": [
                "x² + 3 > 0 for all x, so there are no vertical asymptotes. The top has lower degree, so y → 0 as x → ±∞.",
                "Put y(x² + 3) = x + 1: yx² − x + (3y − 1) = 0.",
                "If y ≠ 0, for real x we need discriminant ≥ 0: 1 − 4y(3y − 1) ≥ 0, i.e. 12y² − 4y − 1 ≤ 0, "
                "(6y + 1)(2y − 1) ≤ 0, so −1/6 ≤ y ≤ 1/2. (y = 0 is taken, at x = −1.)",
                "Range: −1/6 ≤ y ≤ 1/2.",
                "At the end-points the root is repeated: x = 1/(2y). y = 1/2 gives x = 1; y = −1/6 gives x = −3.",
                "Turning points: maximum (1, 1/2) and minimum (−3, −1/6). Intercepts (0, 1/3) and (−1, 0).",
            ],
        },
        {
            "title": "An oblique asymptote (AQA A level, CAIE)",
            "question": "The curve C has equation y = (x² + x − 2)/(x − 2). (a) Find the equations of the asymptotes of C. "
                        "(b) Show that C has no points with 1 < y < 9, and find the turning points. (c) Sketch C.",
            "figure": "pa13_oblique.png",
            "caption": "y = (x² + x − 2)/(x − 2)",
            "width_mm": 95,
            "steps": [
                "(a) Divide: x² + x − 2 = (x − 2)(x + 3) + 4, so y = x + 3 + 4/(x − 2). Asymptotes x = 2 and y = x + 3.",
                "(b) y(x − 2) = x² + x − 2 gives x² + (1 − y)x + (2y − 2) = 0. Real x needs (1 − y)² − 4(2y − 2) ≥ 0:",
                "y² − 10y + 9 ≥ 0, (y − 1)(y − 9) ≥ 0, so y ≤ 1 or y ≥ 9. Hence no points with 1 < y < 9.",
                "Repeated root x = (y − 1)/2: y = 1 gives x = 0, y = 9 gives x = 4. Turning points (0, 1) (maximum) and "
                "(4, 9) (minimum).",
                "(c) Intercepts: x² + x − 2 = (x + 2)(x − 1) = 0 gives (−2, 0) and (1, 0); x = 0 gives (0, 1). For x > 2, "
                "4/(x − 2) > 0, so the curve is above the oblique asymptote; for x < 2 it is below.",
            ],
        },
        {
            "title": "Sketching |f(x)|, 1/f(x) and y² = f(x) (CAIE)",
            "question": "Let f(x) = (x − 1)/(x + 2). Sketch, on separate diagrams, (a) y = |f(x)|, (b) y = 1/f(x), "
                        "(c) y² = f(x), showing asymptotes and the points where each curve meets the axes.",
            "figure": "pa13_modrecip.png",
            "caption": "Left to right: y = |f(x)|, y = 1/f(x) and y² = f(x), with y = f(x) in grey.",
            "width_mm": 165,
            "steps": [
                "y = f(x): asymptotes x = −2, y = 1; meets the axes at (1, 0) and (0, −1/2). f(x) = 1 − 3/(x + 2), so "
                "f < 0 for −2 < x < 1 and f > 0 otherwise.",
                "(a) Reflect the part with −2 < x < 1 in the x-axis. Asymptotes x = −2, y = 1; touches the x-axis at "
                "(1, 0) with a corner; meets the y-axis at (0, 1/2).",
                "(b) 1/f(x) = (x + 2)/(x − 1): the zero x = 1 of f becomes the asymptote x = 1; the asymptote x = −2 of f "
                "becomes the zero (−2, 0); y = 1 stays an asymptote (1/1 = 1). y-intercept (0, −2).",
                "(c) Only where f(x) ≥ 0: x < −2 or x ≥ 1. y = ±√f(x), symmetric in the x-axis. Asymptotes x = −2 and "
                "y = ±1. The curve meets the x-axis only at (1, 0), where its tangent is vertical; it does not meet the "
                "y-axis because f(0) < 0.",
            ],
        },
        {
            "title": "A rational inequality (Edexcel FP1, IAL FP2)",
            "question": "Use algebra to find the set of values of x for which 1/(x − 1) > x/(x + 2).",
            "figure": "pa13_ineq.png",
            "caption": "The solution set (green) is where the blue curve is above the red one.",
            "width_mm": 90,
            "steps": [
                "Critical values from the denominators: x = 1 and x = −2. Do not cross-multiply.",
                "1/(x − 1) − x/(x + 2) > 0 ⇔ [(x + 2) − x(x − 1)]/((x − 1)(x + 2)) > 0 ⇔ (−x² + 2x + 2)/((x − 1)(x + 2)) > 0.",
                "Multiply by −1 (reversing the sign): (x² − 2x − 2)/((x − 1)(x + 2)) < 0. The numerator is zero at "
                "x = 1 ± √3.",
                "Critical values in order: −2, 1 − √3 ≈ −0.732, 1, 1 + √3 ≈ 2.732. Test one value in each interval: "
                "x = −3 gives +; x = −1 gives −; x = 0 gives +; x = 2 gives −; x = 3 gives +.",
                "Solution: <b>−2 < x < 1 − √3 or 1 < x < 1 + √3</b>.",
            ],
        },
        {
            "title": "A modulus inequality (Edexcel FP1, IAL FP2, AQA, CAIE)",
            "question": "Find the set of values of x for which |x² − 1| > 2(x + 1).",
            "figure": "pa13_modineq.png",
            "caption": "y = |x² − 1| lies above y = 2(x + 1) for x < −1 and for x > 3.",
            "width_mm": 90,
            "steps": [
                "Use |A| > B ⇔ A > B or A < −B (valid whatever the sign of B).",
                "A > B: x² − 1 > 2x + 2 ⇔ x² − 2x − 3 > 0 ⇔ (x − 3)(x + 1) > 0 ⇔ x < −1 or x > 3.",
                "A < −B: x² − 1 < −2x − 2 ⇔ x² + 2x + 1 < 0 ⇔ (x + 1)² < 0, which has no solutions.",
                "So the solution set is <b>x < −1 or x > 3</b>.",
                "Check with the sketch: the graphs meet at (−1, 0) (where the line meets the curve at its corner) and at "
                "(3, 8). At x = 0, |−1| = 1 < 2, so 0 is correctly excluded.",
            ],
        },
    ],
    "practice": [
        "Sketch y = (3x − 2)/(x + 1), stating the equations of the asymptotes and the coordinates of the intercepts.",
        "(AQA D9) Solve the inequality (x + 3)/(x − 1) ≥ x − 3.",
        "Solve x³ − 2x² − 5x + 6 > 0, given that x = 1 is a root of x³ − 2x² − 5x + 6 = 0.",
        "Solve the inequality x⁴ − 13x² + 36 ≤ 0.",
        "The curve C has equation y = (2x² − 3x + 1)/(x² − 4). Write down the equations of its asymptotes, find where C "
        "meets the axes, and find the point where C crosses its horizontal asymptote.",
        "(AQA A level, CAIE) Find the asymptotes of y = (2x² + 3x − 1)/(x + 2), and state whether the curve lies above or "
        "below its oblique asymptote for large positive x.",
        "Use the discriminant to find the range of y = (x − 2)/(x² + 5) and the coordinates of its turning points.",
        "Show that y = (x² + 3)/(x − 1) takes no values between −2 and 6, and find the coordinates of its turning points.",
        "Solve |2x − 3| > |x + 1|.",
        "Solve |x² − 4| < 3x.",
        "(CAIE) Let f(x) = x² − 2x − 3. (a) Sketch y = 1/f(x), giving the asymptotes, the y-intercept and the "
        "coordinates of the turning point. (b) Sketch y² = f(x), showing where it meets the axes.",
        "(AQA) (a) Describe a sequence of two transformations that maps y = 1/x onto y = (2x + 1)/(x − 3).\n"
        "(b) The curve y = x³ − x is enlarged by scale factor 2, centre O. Find the equation of the image.\n"
        "(c) Find the equation of the image of y = x³ − x after reflection in the line y = x.",
    ],
    "answers": [
        "Asymptotes x = −1 and y = 3; intercepts (0, −2) and (2/3, 0). y = 3 − 5/(x + 1): branches in the top-left and "
        "bottom-right regions formed by the asymptotes.",
        "(x + 3)/(x − 1) − (x − 3) = −x(x − 5)/(x − 1) ≥ 0 ⇔ x(x − 5)/(x − 1) ≤ 0. Critical values 0, 1, 5: "
        "x ≤ 0 or 1 < x ≤ 5.",
        "(x − 1)(x + 2)(x − 3) > 0: −2 < x < 1 or x > 3.",
        "(x² − 4)(x² − 9) ≤ 0 ⇔ 4 ≤ x² ≤ 9: −3 ≤ x ≤ −2 or 2 ≤ x ≤ 3.",
        "Asymptotes x = 2, x = −2, y = 2. Meets the axes at (0, −1/4), (1/2, 0), (1, 0). 2x² − 3x + 1 = 2x² − 8 gives x = 3: "
        "crosses y = 2 at (3, 2).",
        "y = 2x − 1 + 1/(x + 2): asymptotes x = −2 and y = 2x − 1. For large positive x, 1/(x + 2) > 0, so the curve is "
        "above the asymptote.",
        "yx² − x + 5y + 2 = 0; 1 − 4y(5y + 2) ≥ 0 ⇔ 20y² + 8y − 1 ≤ 0 ⇔ −1/2 ≤ y ≤ 1/10. Turning points x = 1/(2y): "
        "maximum (5, 1/10), minimum (−1, −1/2).",
        "x² − yx + (y + 3) = 0; y² − 4y − 12 ≥ 0 ⇔ (y − 6)(y + 2) ≥ 0 ⇔ y ≤ −2 or y ≥ 6. Turning points x = y/2: "
        "maximum (−1, −2), minimum (3, 6).",
        "Both sides ≥ 0, so square: 4x² − 12x + 9 > x² + 2x + 1 ⇔ 3x² − 14x + 8 > 0 ⇔ (3x − 2)(x − 4) > 0: x < 2/3 or x > 4.",
        "Need −3x < x² − 4 < 3x. x² − 3x − 4 < 0 gives −1 < x < 4; x² + 3x − 4 > 0 gives x < −4 or x > 1. Both: 1 < x < 4.",
        "(a) Asymptotes x = −1, x = 3, y = 0; y-intercept (0, −1/3); f has minimum (1, −4), so 1/f has maximum (1, −1/4) "
        "between the asymptotes; 1/f > 0 and → 0 for x < −1 and x > 3. (b) Exists for x ≤ −1 or x ≥ 3; meets the x-axis "
        "vertically at (−1, 0) and (3, 0); does not meet the y-axis; symmetric about the x-axis, with |y| growing like |x| "
        "for large |x|.",
        "(a) y = 2 + 7/(x − 3): stretch parallel to the y-axis, scale factor 7, then translation by (3, 2)ᵀ. "
        "(b) y/2 = (x/2)³ − x/2 ⇔ y = ¼x³ − x. (c) x = y³ − y.",
    ],
    "exam": [
        "(CAIE) The curve C has equation y = (x² − 3)/(x − 2).\n"
        "(a) Find the equations of the asymptotes of C. [3]\n"
        "(b) Show that there is no point on C for which 2 < y < 6, and find the coordinates of the turning points. [4]\n"
        "(c) Sketch C, showing the asymptotes and the points where C meets the axes. [3]\n"
        "(d) Find the set of values of x for which |(x² − 3)/(x − 2)| > 2. [4]",
        "(Edexcel FP1, IAL FP2) (a) Use algebra to find the set of values of x for which x/(x + 2) ≤ 2/(x − 1). [6]\n"
        "(b) Find the set of values of x for which |x² − 2x − 3| < x + 1. [5]",
        "(AQA A level, CAIE) Let f(x) = x³ + x² − 2x.\n"
        "(a) Factorise f(x) and find the x-coordinates of its stationary points, giving exact answers. [3]\n"
        "(b) Sketch y = |f(x)|. [2]\n"
        "(c) Sketch y² = f(x). Give the coordinates of the points where the curve meets the x-axis, and find the greatest "
        "value of |y| on the closed loop, to 3 significant figures. [4]\n"
        "(d) Sketch y = 1/f(x), stating the equations of its asymptotes. [3]",
        "(AQA) The curve C has equation y = (4x − 3)/(x − 1).\n"
        "(a) Show that y = 4 + 1/(x − 1), and describe a single transformation that maps y = 1/x onto C. [3]\n"
        "(b) Find the exact coordinates of the points where C meets the line y = x + 2. [3]\n"
        "(c) Hence solve (4x − 3)/(x − 1) > x + 2. [3]",
    ],
    "exam_answers": [
        "(a) x = 2 B1; x² − 3 = (x − 2)(x + 2) + 1, so y = x + 2 + 1/(x − 2) M1; oblique asymptote y = x + 2 A1.\n"
        "(b) x² − yx + (2y − 3) = 0 M1; real x ⇔ y² − 8y + 12 ≥ 0 M1 ⇔ (y − 2)(y − 6) ≥ 0 ⇔ y ≤ 2 or y ≥ 6 A1. "
        "Turning points (1, 2) and (3, 6) A1.\n"
        "(c) Two branches with asymptotes x = 2 and y = x + 2 B1; maximum (1, 2) on the left branch, minimum (3, 6) on the "
        "right B1; meets the axes at (±√3, 0) and (0, 3/2) B1.\n"
        "(d) f(x) > 2 ⇔ (x − 1)²/(x − 2) > 0 ⇔ x > 2 M1 A1. f(x) < −2 ⇔ (x² + 2x − 7)/(x − 2) < 0 ⇔ x < −1 − 2√2 or "
        "−1 + 2√2 < x < 2 M1. Solution: x < −1 − 2√2 or x > −1 + 2√2, x ≠ 2 A1. (x = 1 is excluded: there |f| = 2.)",
        "(a) x/(x + 2) − 2/(x − 1) ≤ 0 M1 ⇔ (x² − 3x − 4)/((x + 2)(x − 1)) ≤ 0 A1 ⇔ (x − 4)(x + 1)/((x + 2)(x − 1)) ≤ 0 M1. "
        "Critical values −2, −1, 1, 4 A1; −2 < x ≤ −1 or 1 < x ≤ 4 A1 A1.\n"
        "(b) Need x + 1 > 0 B1. Then |x − 3||x + 1| < x + 1 ⇔ |x − 3| < 1 M1 A1 (or by cases: −(x + 1) < (x − 3)(x + 1) "
        "< x + 1 M1), giving 2 < x < 4 A1.",
        "(a) f(x) = x(x − 1)(x + 2) B1; f′(x) = 3x² + 2x − 2 = 0 M1, x = (−1 ± √7)/3 A1 (≈ 0.549 and −1.22).\n"
        "(b) Cubic with zeros −2, 0, 1; parts for x < −2 and 0 < x < 1 reflected above the axis, corners at the zeros B2.\n"
        "(c) f ≥ 0 on −2 ≤ x ≤ 0 and x ≥ 1 M1: closed loop between (−2, 0) and (0, 0), branch from (1, 0), symmetric "
        "in the x-axis, vertical tangents at all three points A1. Greatest |y| on the loop at x = (−1 − √7)/3: "
        "f = 2.11 (3 s.f.) M1, |y| = √2.113… = 1.45 A1.\n"
        "(d) Asymptotes x = −2, x = 0, x = 1 and y = 0 B1; same sign as f, branches → ±∞ at each asymptote B1; turning "
        "points at the same x as f: (−1.22, 0.473) local minimum and (0.549, −1.58) local maximum B1.",
        "(a) 4 + 1/(x − 1) = (4(x − 1) + 1)/(x − 1) = (4x − 3)/(x − 1) B1; translation M1 by (1, 4)ᵀ A1.\n"
        "(b) 4x − 3 = (x + 2)(x − 1) M1 ⇔ x² − 3x + 1 = 0, x = (3 ± √5)/2 A1; points ((3 + √5)/2, (7 + √5)/2) and "
        "((3 − √5)/2, (7 − √5)/2) A1.\n"
        "(c) (x² − 3x + 1)/(x − 1) < 0 M1; critical values (3 − √5)/2, 1, (3 + √5)/2 M1; x < (3 − √5)/2 or "
        "1 < x < (3 + √5)/2 A1.",
    ],
}
