UNIT = {
    "number": "B8",
    "title": "Polar coordinates",
    "tag": "A2 Core Pure (AS for AQA sketching, CAIE Paper 1) · Edexcel CP 7.1, 7.2, 7.3 · IAL FP2 7.1 · AQA G1, G2 (AS), G3 (A level) · "
           "OCR A 4.09a, b, c · OCR MEI PP1, PP2, PP3 · CAIE 9231 P1 1.5",
    "notes": [
        ("h2", "8.1 Polar coordinates"),
        ("p", "Cartesian coordinates locate a point by going across and then up. <b>Polar coordinates</b> locate it by a distance and "
              "a direction. Fix a point O, the <b>pole</b>, and a half-line from O, the <b>initial line</b> (drawn where the positive "
              "x-axis would be). The point P has polar coordinates (r, θ), where r = OP is its distance from the pole and θ is the "
              "angle, measured anticlockwise in radians, from the initial line to OP."),
        ("figure", "pb08_point.png", "The polar coordinates (r, θ) of P and the link to Cartesian coordinates.", 85),
        ("p", "Every point has many polar descriptions, because adding 2π to θ gives the same direction. To make them unique we use "
              "r ≥ 0 and a principal range of θ, either 0 ≤ θ < 2π or −π < θ ≤ π (the question will say which). The pole itself has "
              "r = 0 and any θ. Edexcel, IAL, OCR A and Cambridge state the convention r ≥ 0; AQA and MEI questions normally give the "
              "range of θ, so read the question. With r ≥ 0, if a formula gives r < 0 for some θ, there is simply no point of the curve "
              "in that direction."),
        ("box", "Converting between polar and Cartesian", [
            "x = r cos θ,   y = r sin θ        r² = x² + y²,   tan θ = y/x",
            "To find θ from (x, y), always locate the quadrant first (a quick sketch) and then adjust arctan(y/x) by ±π if needed.",
            "Useful substitutions for curves: x² + y² = r², x = r cos θ, y = r sin θ, xy = ½r² sin 2θ, x² − y² = r² cos 2θ.",
        ]),
        ("h2", "8.2 Polar equations of curves"),
        ("p", "A polar equation r = f(θ) describes the set of points (f(θ), θ) with f(θ) ≥ 0. To convert to Cartesian form, multiply "
              "through by r if that creates r cos θ, r sin θ or r². To convert to polar form, substitute x = r cos θ and y = r sin θ."),
        ("bullets", [
            "<b>r = a</b> is a circle, centre O, radius a. <b>θ = α</b> is a half-line from O (not a whole line, because r ≥ 0).",
            "<b>r = 2a cos θ</b> (−π/2 ≤ θ ≤ π/2): r² = 2ar cos θ, so x² + y² = 2ax, i.e. (x − a)² + y² = a². This is a circle of radius a "
            "through O with centre (a, 0). Similarly r = 2a sin θ is a circle with centre (0, a) in Cartesian terms.",
            "<b>r = p sec(α − θ)</b>: r cos(θ − α) = p, so x cos α + y sin α = p. This is a straight line whose perpendicular distance "
            "from O is p, the perpendicular making angle α with the initial line. For example r = 3 sec(θ − π/3) is x + √3y = 6.",
            "<b>r = kθ</b> is a spiral: r grows steadily as θ increases, crossing the initial line each turn at r = 2πk, 4πk, ….",
        ]),
        ("h2", "8.3 Sketching polar curves"),
        ("p", "No detailed plotting is needed (Cambridge says so explicitly), but a sketch must show the features examiners look for. "
              "Work through this checklist:"),
        ("bullets", [
            "<b>Symmetry.</b> If f(−θ) = f(θ) (for example any function of cos θ), the curve is symmetrical about the initial line. "
            "If f(π − θ) = f(θ) (a function of sin θ), it is symmetrical about the line θ = π/2.",
            "<b>Where r exists.</b> With r ≥ 0, find the θ-intervals where f(θ) ≥ 0. For r = a cos 2θ these are −π/4 ≤ θ ≤ π/4 and "
            "3π/4 ≤ θ ≤ 5π/4, so the curve has <b>two</b> loops (some textbooks that allow r < 0 draw four).",
            "<b>Greatest and least r.</b> Find the maximum and minimum of f(θ), by inspection (cos θ = ±1) or by calculus, and mark them.",
            "<b>The pole.</b> If f(α) = 0, the curve passes through O and approaches it along the half-line θ = α, which is a tangent "
            "at the pole. Mark these directions.",
            "<b>A few values.</b> r at θ = 0, π/2, π, 3π/2 fixes the shape and the points where the curve crosses the axes.",
        ]),
        ("figure", "pb08_standard.png", "Standard polar curves (a, k, p > 0) drawn with r ≥ 0. Each arrow is the initial line from the pole O.", 150),
        ("p", "<b>Limaçons r = a(p + q cos θ), p ≥ q > 0.</b> These are symmetrical about the initial line, with greatest r = a(p + q) at "
              "θ = 0 and least r = a(p − q) at θ = π. Their shape depends on the ratio p : q. If p = q the curve is a <b>cardioid</b> "
              "(heart-shaped), which touches the pole with a cusp. If q < p < 2q the curve has a <b>dimple</b> (it is not convex) near "
              "θ = π. If p ≥ 2q it is <b>convex</b> (egg-shaped). So r = a(3 + 2 cos θ) has a dimple, but r = a(5 + 2 cos θ) is convex."),
        ("figure", "pb08_limacons.png", "Three limaçons r = a(p + q cos θ) scaled to the same width.", 100),
        ("h2", "8.4 Area enclosed by a polar curve"),
        ("p", "Split the region swept out between θ = α and θ = β into thin sectors. A sector with angle δθ at radius r has area "
              "approximately ½r²δθ (the area of a circular sector, ½r²θ). Adding these and letting δθ → 0 gives the area formula."),
        ("box", "Area of a region bounded by a polar curve", [
            "A = ½ ∫ from α to β of r² dθ   (the region bounded by r = f(θ) and the half-lines θ = α and θ = β, with α < β).",
            "Printed in the Edexcel, IAL, AQA, OCR A and MEI booklets. Cambridge says <b>recall</b> it: it is not in MF19.",
        ]),
        ("figure", "pb08_cardioid_area.png", "The area enclosed by r = a(1 + cos θ) is the sum of thin sectors of area ½r²δθ.", 85),
        ("bullets", [
            "Square r <b>before</b> integrating, and use cos²θ = ½(1 + cos 2θ), sin²θ = ½(1 − cos 2θ) to integrate.",
            "Use symmetry: for a curve symmetrical about the initial line, find the area for 0 ≤ θ ≤ π and double it.",
            "For one loop of a rose curve, integrate between two consecutive zeros of r.",
            "<b>Between two curves:</b> find where they meet (solve f(θ) = g(θ), and check the pole separately, because two curves can "
            "both pass through O at different values of θ). Then area = ½∫(r_outer² − r_inner²) dθ over each interval, or add and "
            "subtract sector areas. A sketch is essential to decide which curve bounds which part.",
        ]),
        ("h2", "8.5 Tangents parallel or perpendicular to the initial line (Edexcel, IAL)"),
        ("p", "Treat θ as a parameter: x = r cos θ = f(θ) cos θ and y = r sin θ = f(θ) sin θ. Then dy/dx = (dy/dθ)/(dx/dθ)."),
        ("box", "Tangents to r = f(θ)", [
            "Parallel to the initial line (horizontal): dy/dθ = 0, where y = r sin θ.",
            "Perpendicular to the initial line (vertical): dx/dθ = 0, where x = r cos θ.",
            "Gradient (MEI Further Pure with Technology, and useful generally): dy/dx = (r′ sin θ + r cos θ)/(r′ cos θ − r sin θ), r′ = dr/dθ.",
        ]),
        ("p", "Solve the equation in θ (it is usually a quadratic in cos θ or sin θ after using double-angle identities), keep only "
              "solutions in the given range with r ≥ 0, and give the points in polar form (r, θ). Check each one: if both derivatives "
              "are zero (often at the pole), the simple rule does not decide the direction of the tangent."),
        ("box", "Given or learn? (by board)", [
            "Area ½∫r² dθ: given in the Edexcel, IAL, AQA, OCR A and MEI booklets; learn it for Cambridge (examiners report candidates “missed the ½”).",
            "x = r cos θ, y = r sin θ, r² = x² + y²: learn (not printed anywhere).",
            "Tangent conditions dy/dθ = 0 and dx/dθ = 0: learn (Edexcel and IAL only).",
        ]),
        ("warn", "Common mistakes", [
            "Using the wrong quadrant for θ when converting a point with x < 0, e.g. giving θ = −π/6 instead of 5π/6 for (−√3, 1).",
            "Forgetting the ½ in the area formula, or forgetting to square r (½∫r dθ is not an area).",
            "Integrating over the wrong range: one loop of r = a sin 3θ runs from θ = 0 to π/3, not 0 to π.",
            "Drawing parts of a curve where r < 0, or missing that r = a cos 2θ exists only for some θ when r ≥ 0.",
            "Showing a cardioid with a smooth rounded point at the pole: it has a cusp, and the tangent there is the initial line.",
            "For tangents, differentiating r instead of y = r sin θ (or x = r cos θ).",
            "For areas between curves, not checking which curve is outside on each interval of θ.",
        ]),
    ],
    "examples": [
        {
            "title": "Converting points and equations",
            "question": "(a) Find polar coordinates, with r ≥ 0 and −π < θ ≤ π, of the point with Cartesian coordinates (−√3, 1). "
                        "(b) Find a Cartesian equation of r = 4 cos θ and describe the curve. (c) Find a polar equation of x² − y² = 4. "
                        "(d) Show that r = 3 sec(θ − π/3) is a straight line and find its Cartesian equation.",
            "steps": [
                "(a) r = √(3 + 1) = 2. The point is in the second quadrant; arctan(1/√3) = π/6, so θ = π − π/6 = 5π/6. Answer (2, 5π/6).",
                "(b) Multiply by r: r² = 4r cos θ, so x² + y² = 4x, i.e. (x − 2)² + y² = 4. A circle, centre (2, 0), radius 2, through O.",
                "(c) x² − y² = r²cos²θ − r²sin²θ = r² cos 2θ, so r² cos 2θ = 4, i.e. r² = 4 sec 2θ (only where cos 2θ > 0).",
                "(d) r cos(θ − π/3) = 3, so r cos θ cos(π/3) + r sin θ sin(π/3) = 3, giving ½x + (√3/2)y = 3, i.e. x + √3y = 6.",
                "This is a line at perpendicular distance 3 from O; the perpendicular from O makes angle π/3 with the initial line.",
            ],
        },
        {
            "title": "Sketching a cardioid and a limaçon",
            "question": "On separate diagrams sketch (a) r = a(1 + cos θ), (b) r = a(3 + 2 cos θ), for 0 ≤ θ < 2π, where a > 0. "
                        "Show the polar coordinates of the points where each curve meets the initial line and the half-line θ = π/2.",
            "steps": [
                "(a) cos(−θ) = cos θ, so the curve is symmetrical about the initial line. r ≥ 0 for all θ.",
                "Greatest r = 2a at θ = 0; least r = 0 at θ = π, so the curve passes through the pole, approaching along θ = π: a cusp.",
                "At θ = π/2, r = a. Points: (2a, 0), (a, π/2), (a, 3π/2) and the pole. Shape: cardioid (see the standard curves figure).",
                "(b) Again symmetrical about the initial line. Here r ≥ a > 0 for all θ, so the curve does not reach the pole.",
                "Greatest r = 5a at θ = 0; least r = a at θ = π; at θ = π/2 and 3π/2, r = 3a. Points: (5a, 0), (3a, π/2), (a, π), (3a, 3π/2).",
                "Since p = 3 < 2q = 4, there is a dimple near θ = π: the curve is not convex there.",
            ],
        },
        {
            "title": "Area enclosed by a cardioid",
            "question": "Find the area enclosed by the cardioid r = a(1 + cos θ).",
            "steps": [
                "A = ½ ∫ from 0 to 2π of a²(1 + cos θ)² dθ = ½a² ∫ (1 + 2 cos θ + cos²θ) dθ.",
                "cos²θ = ½(1 + cos 2θ), so the integrand is 3/2 + 2 cos θ + ½ cos 2θ.",
                "∫ from 0 to 2π = [3θ/2 + 2 sin θ + ¼ sin 2θ] from 0 to 2π = 3π.",
                "A = ½a² × 3π = 3πa²/2.",
                "Check: the curve fits inside a circle of radius 2a, area 4πa², and 3πa²/2 ≈ 4.71a² is a sensible fraction of it.",
            ],
        },
        {
            "title": "Area of one loop of a rose curve",
            "question": "The curve C has equation r = 2 sin 3θ, 0 ≤ θ < 2π, with r ≥ 0. Find the area of one loop of C, and the total area enclosed by C.",
            "figure": "pb08_rose.png",
            "caption": "r = 2 sin 3θ has three loops. The shaded loop is swept out for 0 ≤ θ ≤ π/3, with greatest r = 2 at θ = π/6.",
            "width_mm": 80,
            "steps": [
                "r = 0 when sin 3θ = 0, i.e. θ = 0, π/3, 2π/3, π. r ≥ 0 on [0, π/3] (a loop), negative on (π/3, 2π/3) (no points), and so on: loops for [0, π/3], [2π/3, π], [4π/3, 5π/3].",
                "One loop: A = ½ ∫ from 0 to π/3 of 4 sin²3θ dθ = ∫ from 0 to π/3 of (1 − cos 6θ) dθ.",
                "= [θ − (1/6) sin 6θ] from 0 to π/3 = π/3.",
                "The three loops are congruent (rotations of each other through 2π/3), so the total area is 3 × π/3 = π.",
            ],
        },
        {
            "title": "Area between two polar curves",
            "question": "The curves C₁: r = 3 cos θ and C₂: r = 1 + cos θ, for −π/2 ≤ θ ≤ π/2 and −π < θ ≤ π respectively. "
                        "(a) Find the polar coordinates of the points where they meet, other than the pole. "
                        "(b) Find the area of the region R inside C₁ and outside C₂.",
            "figure": "pb08_two_curves.png",
            "caption": "R lies inside the circle r = 3 cos θ and outside the cardioid r = 1 + cos θ, for −π/3 ≤ θ ≤ π/3.",
            "width_mm": 90,
            "steps": [
                "(a) 3 cos θ = 1 + cos θ gives cos θ = ½, so θ = ±π/3 and r = 3/2: the points (3/2, π/3) and (3/2, −π/3).",
                "(Both curves also pass through the pole: C₁ at θ = ±π/2, C₂ at θ = π. Equating r does not find this.)",
                "(b) For −π/3 ≤ θ ≤ π/3 the circle is outside the cardioid. By symmetry, R = 2 × ½ ∫ from 0 to π/3 of [9cos²θ − (1 + cos θ)²] dθ.",
                "The integrand is 8cos²θ − 2 cos θ − 1 = 4(1 + cos 2θ) − 2 cos θ − 1 = 3 + 4 cos 2θ − 2 cos θ.",
                "∫ from 0 to π/3 = [3θ + 2 sin 2θ − 2 sin θ] from 0 to π/3 = π + 2(√3/2) − 2(√3/2) = π.",
                "Area of R = π.",
            ],
        },
        {
            "title": "Tangents parallel and perpendicular to the initial line",
            "question": "For the cardioid r = a(1 + cos θ), −π < θ ≤ π, find the polar coordinates of the points where the tangent is "
                        "(a) parallel to the initial line, (b) perpendicular to the initial line.",
            "figure": "pb08_tangents.png",
            "caption": "Horizontal tangents (red) at (3a/2, ±π/3); vertical tangents (green) at (2a, 0) and (a/2, ±2π/3).",
            "width_mm": 90,
            "steps": [
                "(a) y = r sin θ = a(sin θ + sin θ cos θ) = a(sin θ + ½ sin 2θ). dy/dθ = a(cos θ + cos 2θ).",
                "cos θ + 2cos²θ − 1 = 0 gives (2 cos θ − 1)(cos θ + 1) = 0, so cos θ = ½ or cos θ = −1.",
                "cos θ = ½: θ = ±π/3, r = 3a/2. cos θ = −1: θ = π, r = 0, the pole (the cusp, where dx/dθ is also 0), which we reject.",
                "Points: (3a/2, π/3) and (3a/2, −π/3).",
                "(b) x = r cos θ = a(cos θ + cos²θ). dx/dθ = −a(sin θ + 2 sin θ cos θ) = −a sin θ(1 + 2 cos θ).",
                "sin θ = 0: θ = 0 (r = 2a) or θ = π (the pole again, rejected). 1 + 2 cos θ = 0: θ = ±2π/3, r = a/2.",
                "Points: (2a, 0), (a/2, 2π/3) and (a/2, −2π/3).",
            ],
        },
    ],
    "practice": [
        "Convert to Cartesian coordinates: (a) (4, π/6), (b) (2, 3π/4).",
        "Convert to polar coordinates with r ≥ 0 and −π < θ ≤ π: (a) (3, −3), (b) (−1, −√3).",
        "Find Cartesian equations of (a) r = 5, (b) θ = π/4, (c) r = 6 sin θ, and describe each curve.",
        "Find polar equations of (a) y = 3, (b) x² + y² − 4x = 0, (c) xy = 4.",
        "Show that r = 2 sec(θ − π/6) is a straight line and find its Cartesian equation.",
        "Sketch r = 2θ for 0 ≤ θ ≤ 2π, marking the points where the curve meets the initial line and the half-lines θ = π/2, π, 3π/2.",
        "(a) Sketch r = 3 cos 2θ (r ≥ 0) for 0 ≤ θ < 2π, showing the tangents at the pole and the greatest value of r. "
        "(b) Find the area of one loop.",
        "Sketch the curve r² = 4 cos 2θ and find the total area it encloses.",
        "Show that the area enclosed by r = 2a cos θ, −π/2 ≤ θ ≤ π/2, is πa², and explain why this was to be expected.",
        "Find the area of the region bounded by the spiral r = θ, 0 ≤ θ ≤ π, and the initial line (θ = π gives the other edge).",
        "State whether r = 2 + cos θ is convex or has a dimple, and find the area it encloses.",
        "(Edexcel, IAL) The curve r = a sin 2θ, 0 ≤ θ ≤ π/2, forms a loop. Find the polar coordinates of the point on the loop where "
        "the tangent is parallel to the initial line.",
    ],
    "practice_figures": {14: [("pb08_exam_region.png", "C₁: r = 4 cos θ and C₂: r = 4(1 − cos θ). R (shaded) lies inside both curves.", 85)]},
    "answers": [
        "(a) (4 cos(π/6), 4 sin(π/6)) = (2√3, 2). (b) (2 cos(3π/4), 2 sin(3π/4)) = (−√2, √2).",
        "(a) (3√2, −π/4). (b) r = 2; third quadrant, arctan(√3) = π/3, so θ = −π + π/3 = −2π/3: (2, −2π/3).",
        "(a) x² + y² = 25, circle centre O radius 5. (b) y = x with x ≥ 0: a half-line from O. "
        "(c) r² = 6r sin θ, so x² + y² = 6y, i.e. x² + (y − 3)² = 9: circle centre (0, 3), radius 3.",
        "(a) r sin θ = 3, r = 3 cosec θ (0 < θ < π). (b) r² = 4r cos θ, r = 4 cos θ. "
        "(c) r² sin θ cos θ = 4, so r² = 8 cosec 2θ (for 0 < θ < π/2 or π < θ < 3π/2).",
        "r cos(θ − π/6) = 2 gives (√3/2)x + ½y = 2, i.e. √3x + y = 4, a line at distance 2 from O.",
        "Spiral starting at O, turning anticlockwise, r increasing steadily: (π, π/2), (2π, π), (3π, 3π/2), (4π, 2π) on the initial line.",
        "(a) Two loops (r ≥ 0 only for −π/4 ≤ θ ≤ π/4 and 3π/4 ≤ θ ≤ 5π/4), symmetric about both axes, greatest r = 3 at θ = 0 and π, "
        "tangents at the pole θ = ±π/4, 3π/4, 5π/4. (b) ½∫ from −π/4 to π/4 of 9cos²2θ dθ = 9π/8.",
        "Lemniscate: two loops through O, r ≤ 2 with r = 2 at θ = 0, π; tangents at O along θ = ±π/4. "
        "Total area = 2 × ½∫ from −π/4 to π/4 of 4 cos 2θ dθ = 4.",
        "½∫ 4a²cos²θ dθ from −π/2 to π/2 = 2a² × π/2 = πa². The curve is a circle of radius a (section 8.2), whose area is πa².",
        "½∫₀^π θ² dθ = π³/6 ≈ 5.17.",
        "p = 2 = 2q, so it is convex (just). Area = ½∫₀<sup>2π</sup> (4 + 4 cos θ + cos²θ) dθ = ½(8π + π) = 9π/2.",
        "y = a sin 2θ sin θ = 2a sin²θ cos θ. dy/dθ = 2a sin θ(2cos²θ − sin²θ) = 0 gives tan²θ = 2 (θ = 0 is the pole). "
        "θ = arctan √2 ≈ 0.955, sin 2θ = 2√2/3, so the point is (2√2a/3, arctan √2).",
    ],
    "exam": [
        "The curve C has polar equation r = a(3 + 2 cos θ), 0 ≤ θ < 2π, where a is a positive constant.\n"
        "(a) Sketch C, showing the polar coordinates of the points where C meets the half-lines θ = 0 and θ = π. [3]\n"
        "(b) Find, in terms of a and π, the area enclosed by C. [5]\n"
        "(c) (Edexcel, IAL) Find the polar coordinates of the points on C where the tangent is perpendicular to the initial line, "
        "giving angles to 3 significant figures. [5]",

        "The curves C₁ and C₂ have polar equations C₁: r = 4 cos θ, −π/2 ≤ θ ≤ π/2, and C₂: r = 4(1 − cos θ), 0 ≤ θ < 2π.\n"
        "(a) Find the polar coordinates of the points, other than the pole, where C₁ and C₂ intersect. [3]\n"
        "(b) The region R lies inside both C₁ and C₂. Show that the area of R is 28π/3 − 16√3. [7]",

        "The curve C has polar equation r = 4 cos 2θ, −π/4 ≤ θ ≤ π/4.\n"
        "(a) Show that the area enclosed by C is 2π. [4]\n"
        "(b) (Edexcel, IAL) Find the polar coordinates of the two points on C where the tangent is parallel to the initial line. "
        "Give θ to 3 significant figures. [5]\n"
        "(c) Find the exact distance between these two tangents. [2]",

        "(a) Show that the Cartesian equation (x² + y²)² = 4xy can be written in polar form as r² = 2 sin 2θ. [3]\n"
        "(b) Sketch the curve for 0 ≤ θ < 2π, with r ≥ 0. [3]\n"
        "(c) Find the greatest value of r and the values of θ at which it occurs. [2]\n"
        "(d) Find the total area enclosed by the curve. [3]",
    ],
    "exam_answers": [
        "(a) Closed curve symmetrical about the initial line, not through the pole, with a dimple near θ = π (3 < 2 × 2) B1 B1; "
        "points (5a, 0) and (a, π) B1.\n"
        "(b) A = ½a² ∫₀<sup>2π</sup> (9 + 12 cos θ + 4cos²θ) dθ M1 A1; 4cos²θ = 2 + 2 cos 2θ M1; ½a²[11θ + 12 sin θ + sin 2θ]₀<sup>2π</sup> M1 "
        "= 11πa² A1.\n"
        "(c) x = a(3 cos θ + 2cos²θ) M1; dx/dθ = −a sin θ(3 + 4 cos θ) = 0 M1 A1; sin θ = 0 gives (5a, 0) and (a, π) A1; "
        "cos θ = −3/4 gives r = 3a/2, θ = 2.42 or θ = 2π − 2.42 = 3.86: (3a/2, 2.42) and (3a/2, 3.86) A1.",

        "(a) 4 cos θ = 4 − 4 cos θ M1, cos θ = ½ A1, points (2, π/3) and (2, −π/3) A1.\n"
        "(b) By symmetry, R = 2 × [½∫₀<sup>π/3</sup> 16(1 − cos θ)² dθ + ½∫<sub>π/3</sub><sup>π/2</sup> 16cos²θ dθ] M1 M1 (C₂ bounds R near the pole side for "
        "0 ≤ θ ≤ π/3, C₁ for π/3 ≤ θ ≤ π/2). (1 − cos θ)² = 3/2 − 2 cos θ + ½ cos 2θ M1; "
        "16[3θ/2 − 2 sin θ + ¼ sin 2θ]₀<sup>π/3</sup> = 16(π/2 − 7√3/8) = 8π − 14√3 A1; "
        "16[θ/2 + ¼ sin 2θ]<sub>π/3</sub><sup>π/2</sup> = 16(π/12 − √3/8) = 4π/3 − 2√3 M1 A1; total 28π/3 − 16√3 A1 (≈ 1.61).",

        "(a) A = ½∫ from −π/4 to π/4 of 16cos²2θ dθ M1 = 4∫ (1 + cos 4θ) dθ M1 = 4[θ + ¼ sin 4θ] from −π/4 to π/4 A1 = 4 × π/2 = 2π A1.\n"
        "(b) y = 4 cos 2θ sin θ M1; dy/dθ = 4(cos 2θ cos θ − 2 sin 2θ sin θ) = 4 cos θ(1 − 6sin²θ) M1 A1; cos θ ≠ 0 in the range, "
        "so sin θ = ±1/√6, θ = ±0.421 A1; cos 2θ = 1 − 2/6 = 2/3, r = 8/3: points (8/3, 0.421) and (8/3, −0.421) A1.\n"
        "(c) y = r sin θ = ±(8/3)(1/√6) = ±4√6/9 M1, distance 8√6/9 (≈ 2.18) A1.",

        "(a) (r²)² = 4(r cos θ)(r sin θ) M1 = 2r² sin 2θ A1; divide by r² (r ≠ 0; the pole lies on both): r² = 2 sin 2θ A1.\n"
        "(b) r exists only where sin 2θ ≥ 0: 0 ≤ θ ≤ π/2 and π ≤ θ ≤ 3π/2 B1; two loops through O in the first and third quadrants B1, "
        "touching the initial line and θ = π/2 at O B1.\n"
        "(c) Greatest r = √2 B1 at θ = π/4 and 5π/4 B1.\n"
        "(d) One loop: ½∫₀<sup>π/2</sup> 2 sin 2θ dθ M1 = [−½ cos 2θ]₀<sup>π/2</sup> = 1 A1; total area 2 A1.",
    ],
}
