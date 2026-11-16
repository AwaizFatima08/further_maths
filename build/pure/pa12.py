"""Unit A12: Distances and intersections in three dimensions."""

UNIT = {
    "number": "A12",
    "title": "Distances and intersections in three dimensions",
    "tag": "AS · Edexcel CP 6.5 (AS) · IAL FP3 5.2 · AQA F6 (AS for lines; planes at A level) · OCR A 4.04h–j (A level) · "
           "OCR MEI Pv13, Pv16, Pv17 (A level) · CAIE 9231 P1 1.6",
    "notes": [
        ("p", "This unit answers two questions about lines and planes: how far apart are they, and where do they meet? Every "
              "distance in this unit is a <b>shortest</b> (perpendicular) distance, and every method rests on one idea from Units A9 "
              "and A10: a perpendicular is detected by a zero scalar product. Formulae for several distances are in the Edexcel, "
              "OCR and MEI formula booklets, but you must know where they come from, and AQA and CAIE expect you to work from first "
              "principles."),

        ("h2", "12.1 The distance from a point to a line (Ed 6.5, IAL 5.2, AQA F6, OCR 4.04i, MEI Pv16)"),
        ("p", "Let l be <b>r</b> = <b>a</b> + λ<b>b</b> and P a point not on l. The shortest distance from P to l is PF, where F is the "
              "<b>foot of the perpendicular</b> from P to l: the point of l with PF→ perpendicular to <b>b</b>."),
        ("figure", "pa12_point_line.png", "F is the foot of the perpendicular from P to l; the distance is |PF|.", 85),
        ("box", "Point to line", [
            "<b>Method 1 (scalar product, all boards).</b> Write F = <b>a</b> + λ<b>b</b>. Solve PF→·<b>b</b> = 0 for λ; then the distance is |PF→|.",
            "<b>Method 2 (vector product).</b> d = |(<b>p</b> − <b>a</b>) × <b>b</b>| / |<b>b</b>|, because |(<b>p</b> − <b>a</b>) × <b>b</b>| = |AP||<b>b</b>| sin θ "
            "and d = |AP| sin θ.",
            "<b>In 2-D</b>, the distance from (x₁, y₁) to the line ax + by + c = 0 is |ax₁ + by₁ + c| / √(a² + b²) (given in the OCR "
            "and MEI booklets).",
            "<b>Parallel lines</b>: the distance between two parallel lines is the distance from any point of one to the other line "
            "(OCR 4.04h, MEI Pv13).",
        ]),
        ("p", "A useful alternative to Method 1 is to minimise |PF|² as a quadratic in λ by completing the square or differentiating; "
              "the minimum occurs at the same λ."),

        ("h2", "12.2 The distance from a point to a plane (Ed 6.5, IAL 5.2, AQA F6, OCR 4.04j, MEI Pv17, CAIE 1.6)"),
        ("figure", "pa12_point_plane.png", "N is the foot of the perpendicular from P to Π; P′ is the reflection of P in Π.", 78),
        ("p", "Let Π be <b>r</b>·<b>n</b> = p (Cartesian ax + by + cz = p) and P a point with position vector <b>p₀</b> = (x₁, y₁, z₁)ᵀ. "
              "The perpendicular from P meets Π at N. The line PN has direction <b>n</b>, so N = <b>p₀</b> + t<b>n</b> for the value of t "
              "that puts N in the plane."),
        ("box", "Point to plane", [
            "d = |ax₁ + by₁ + cz₁ − p| / √(a² + b² + c²) = |<b>p₀</b>·<b>n</b> − p| / |<b>n</b>|.",
            "Edexcel's booklet writes the plane as n₁x + n₂y + n₃z + d = 0 and the point as (α, β, γ): distance "
            "|n₁α + n₂β + n₃γ + d| / √(n₁² + n₂² + n₃²). It is the same formula.",
            "<b>Foot of the perpendicular</b>: substitute <b>p₀</b> + t<b>n</b> into the plane and solve for t (CAIE 1.6).",
            "<b>Reflection</b> of P in Π: P′ = <b>p₀</b> + 2t<b>n</b> with the same t, since N is the midpoint of PP′.",
            "The distance of the plane <b>r</b>·<b>n</b> = p from O is |p|/|<b>n</b>|. Parallel planes <b>r</b>·<b>n</b> = p₁ and <b>r</b>·<b>n</b> = p₂ "
            "(same <b>n</b>) are |p₁ − p₂|/|<b>n</b>| apart.",
        ]),
        ("p", "<b>Proof of the formula.</b> Substituting <b>p₀</b> + t<b>n</b> into <b>r</b>·<b>n</b> = p gives <b>p₀</b>·<b>n</b> + t|<b>n</b>|² = p, so "
              "t = (p − <b>p₀</b>·<b>n</b>)/|<b>n</b>|². The distance is |PN| = |t||<b>n</b>| = |<b>p₀</b>·<b>n</b> − p|/|<b>n</b>|. The sign of "
              "<b>p₀</b>·<b>n</b> − p tells you which side of the plane P lies on: two points are on the same side exactly when these "
              "numbers have the same sign."),

        ("h2", "12.3 Skew lines: shortest distance and common perpendicular (Ed 6.5, IAL 5.2, AQA F6, OCR 4.04h, MEI Pv13, CAIE 1.6)"),
        ("p", "Two skew lines l₁: <b>r</b> = <b>a</b> + λ<b>b</b> and l₂: <b>r</b> = <b>c</b> + μ<b>d</b> have exactly one <b>common perpendicular</b>: a "
              "line meeting both at right angles, at P on l₁ and Q on l₂. The shortest distance between the lines is |PQ|."),
        ("figure", "pa12_skew.png", "The common perpendicular PQ of two skew lines is parallel to b × d.", 80),
        ("box", "Shortest distance between skew lines", [
            "<b>Formula</b>: d = |(<b>c</b> − <b>a</b>)·(<b>b</b> × <b>d</b>)| / |<b>b</b> × <b>d</b>|. (In the OCR and MEI booklets.)",
            "<b>Why</b>: <b>b</b> × <b>d</b> is perpendicular to both lines, so it is the direction of PQ. The distance is the component of "
            "any joining vector <b>c</b> − <b>a</b> along the unit vector (<b>b</b> × <b>d</b>)/|<b>b</b> × <b>d</b>|.",
            "<b>Points P and Q (no vector product needed; AQA AS)</b>: write P = <b>a</b> + λ<b>b</b>, Q = <b>c</b> + μ<b>d</b>, and solve "
            "PQ→·<b>b</b> = 0 and PQ→·<b>d</b> = 0 simultaneously for λ and μ. Then d = |PQ→|.",
            "<b>Common perpendicular (CAIE)</b>: the line through P and Q, <b>r</b> = <b>p</b> + t(<b>b</b> × <b>d</b>).",
            "If the formula gives d = 0, the lines intersect. For parallel lines <b>b</b> × <b>d</b> = <b>0</b> and the formula fails: use 12.1.",
        ]),

        ("h2", "12.4 The line of intersection of two planes (IAL 5.2, CAIE 1.6; also used by Edexcel and OCR)"),
        ("figure", "pa12_two_planes.png", "Two non-parallel planes meet in a line whose direction is perpendicular to both normals.", 78),
        ("p", "Two non-parallel planes meet in a line. The line lies in both planes, so its direction is perpendicular to both normals: "
              "<b>n₁</b> × <b>n₂</b>. (MEI students do not need to find this line.)"),
        ("box", "Finding the line of intersection", [
            "<b>Method 1</b>: direction <b>n₁</b> × <b>n₂</b>. For a point, set one coordinate to a convenient value (often 0) and solve the "
            "two plane equations for the other two. If that gives no solution, set a different coordinate.",
            "<b>Method 2</b>: let one coordinate be the parameter, e.g. z = λ, solve the two equations for x and y in terms of λ, and "
            "read off <b>r</b> = <b>a</b> + λ<b>b</b>.",
            "Check: the point satisfies both equations and the direction has zero scalar product with both normals.",
        ]),
        ("table", ["Question", "Key condition", "Result"], [
            ["Point P to line <b>r</b> = <b>a</b> + λ<b>b</b>", "PF→·<b>b</b> = 0", "d = |(<b>p</b> − <b>a</b>) × <b>b</b>|/|<b>b</b>|"],
            ["Point P to plane <b>r</b>·<b>n</b> = p", "PN parallel to <b>n</b>", "d = |<b>p</b>·<b>n</b> − p|/|<b>n</b>|"],
            ["Skew lines", "PQ→·<b>b</b> = PQ→·<b>d</b> = 0", "d = |(<b>c</b> − <b>a</b>)·(<b>b</b> × <b>d</b>)|/|<b>b</b> × <b>d</b>|"],
            ["Parallel lines", "same as point to line", "d = |(<b>c</b> − <b>a</b>) × <b>b</b>|/|<b>b</b>|"],
            ["Two planes meet", "direction ⊥ both normals", "line <b>r</b> = <b>a</b> + t(<b>n₁</b> × <b>n₂</b>)"],
            ["Line parallel to plane", "<b>b</b>·<b>n</b> = 0", "d = distance from any point of the line"],
        ]),
        ("warn", "Common mistakes", [
            "Forgetting the modulus signs, giving a negative distance.",
            "Using the point-to-plane formula without first writing the plane as ax + by + cz = p (or with the constant on the "
            "wrong side when using the Edexcel form with “+ d”).",
            "Dividing by |<b>b</b>| instead of |<b>b</b> × <b>d</b>| in the skew-lines formula.",
            "Using the skew-line formula for parallel lines, where <b>b</b> × <b>d</b> = <b>0</b>.",
            "Finding the foot of a perpendicular but then reporting its coordinates when the question asks for the distance, or vice versa.",
            "For a reflection, using t instead of 2t: N is only halfway.",
        ]),
    ],

    "examples": [
        {
            "title": "Foot of the perpendicular from a point to a line",
            "question": "Find the foot of the perpendicular from P(5, 3, 4) to the line l: <b>r</b> = (1, 2, 3)ᵀ + λ(2, −1, 2)ᵀ, and the shortest "
                        "distance from P to l.",
            "steps": [
                "F = (1 + 2λ, 2 − λ, 3 + 2λ), so PF→ = (2λ − 4, −λ − 1, 2λ − 1)ᵀ.",
                "PF→·(2, −1, 2)ᵀ = 4λ − 8 + λ + 1 + 4λ − 2 = 9λ − 9 = 0, so λ = 1 and F = (3, 1, 5).",
                "PF→ = (−2, −2, 1)ᵀ, so the distance is √(4 + 4 + 1) = 3.",
                "Check with the vector product: (<b>p</b> − <b>a</b>) × <b>b</b> = (4, 1, 1)ᵀ × (2, −1, 2)ᵀ = (3, −6, −6)ᵀ, magnitude 9, and 9/|<b>b</b>| = 9/3 = 3.",
            ],
        },
        {
            "title": "Distance, foot and reflection for a plane",
            "question": "The plane Π has equation 2x − y + 2z = 2 and P is (3, −1, 2). Find the distance from P to Π, the foot N of the "
                        "perpendicular from P to Π, and the reflection P′ of P in Π.",
            "steps": [
                "Distance = |2(3) − (−1) + 2(2) − 2| / √(4 + 1 + 4) = |11 − 2|/3 = 3.",
                "Line PN: <b>r</b> = (3, −1, 2)ᵀ + t(2, −1, 2)ᵀ. Substitute: 2(3 + 2t) − (−1 − t) + 2(2 + 2t) = 2 gives 11 + 9t = 2, so t = −1.",
                "N = (1, 0, 0). Check: 2 − 0 + 0 = 2, and |PN| = |−1| × |<b>n</b>| = 3.",
                "P′ uses 2t = −2: P′ = (3 − 4, −1 + 2, 2 − 4) = (−1, 1, −2).",
            ],
        },
        {
            "title": "Shortest distance between skew lines and the common perpendicular",
            "question": "l₁: <b>r</b> = (0, −1, 2)ᵀ + λ(1, 1, 0)ᵀ and l₂: <b>r</b> = (3, −3, 3)ᵀ + μ(0, 1, 1)ᵀ. Find the shortest distance between "
                        "the lines, and the points P on l₁ and Q on l₂ at the ends of the common perpendicular.",
            "steps": [
                "<b>b</b> × <b>d</b> = (1, 1, 0)ᵀ × (0, 1, 1)ᵀ = (1, −1, 1)ᵀ, |<b>b</b> × <b>d</b>| = √3. <b>c</b> − <b>a</b> = (3, −2, 1)ᵀ.",
                "d = |(3, −2, 1)·(1, −1, 1)|/√3 = |3 + 2 + 1|/√3 = 6/√3 = 2√3 ≈ 3.46.",
                "Points: PQ→ = (3, −3 + μ, 3 + μ)ᵀ − (λ, −1 + λ, 2)ᵀ = (3 − λ, −2 + μ − λ, 1 + μ)ᵀ.",
                "PQ→·(1, 1, 0)ᵀ = 3 − λ − 2 + μ − λ = 1 − 2λ + μ = 0 and PQ→·(0, 1, 1)ᵀ = −2 + μ − λ + 1 + μ = −1 − λ + 2μ = 0.",
                "Solving: λ = 1, μ = 1. P = (1, 0, 2), Q = (3, −2, 4), PQ→ = (2, −2, 2)ᵀ = 2(1, −1, 1)ᵀ and |PQ→| = 2√3, as before.",
            ],
        },
        {
            "title": "The line of intersection of two planes",
            "question": "Find a vector equation of the line of intersection of Π₁: x + y + z = 6 and Π₂: 2x − y + 3z = 9.",
            "steps": [
                "Direction: <b>n₁</b> × <b>n₂</b> = (1, 1, 1)ᵀ × (2, −1, 3)ᵀ = (1·3 − 1·(−1), 1·2 − 1·3, 1·(−1) − 1·2)ᵀ = (4, −1, −3)ᵀ.",
                "Point: put z = 0. Then x + y = 6 and 2x − y = 9, so 3x = 15, x = 5, y = 1. The point is (5, 1, 0).",
                "Line: <b>r</b> = (5, 1, 0)ᵀ + t(4, −1, −3)ᵀ.",
                "Check: (5 + 4t) + (1 − t) − 3t = 6 for all t, and 2(5 + 4t) − (1 − t) + 3(−3t) = 9 for all t.",
            ],
        },
        {
            "title": "Parallel lines, and a point and a line in 2-D",
            "question": "(a) Find the distance between the parallel lines l₁: <b>r</b> = (1, 0, 1)ᵀ + λ(1, 2, 2)ᵀ and l₂: <b>r</b> = (2, 3, −1)ᵀ + μ(2, 4, 4)ᵀ. "
                        "(b) Find the distance from (3, 4) to the line 3x − 4y + 2 = 0.",
            "steps": [
                "(a) (2, 4, 4)ᵀ = 2(1, 2, 2)ᵀ, so the lines are parallel. Use the point C(2, 3, −1) of l₂ and l₁:",
                "(<b>c</b> − <b>a</b>) × <b>b</b> = (1, 3, −2)ᵀ × (1, 2, 2)ᵀ = (10, −4, −1)ᵀ, magnitude √117 = 3√13.",
                "Distance = 3√13/|<b>b</b>| = 3√13/3 = √13 ≈ 3.61.",
                "(b) |3(3) − 4(4) + 2|/√(9 + 16) = |−5|/5 = 1.",
            ],
        },
        {
            "title": "Common perpendicular of skew lines (exam standard)",
            "question": "l₁: <b>r</b> = (1, 0, 3)ᵀ + λ(2, 1, −2)ᵀ and l₂: <b>r</b> = (1, 9, 3)ᵀ + μ(2, −2, 1)ᵀ. (a) Show that the lines are skew. "
                        "(b) Find the shortest distance between them. (c) Find a vector equation of their common perpendicular.",
            "steps": [
                "(a) Not parallel. x: 1 + 2λ = 1 + 2μ gives λ = μ. y: λ = 9 − 2μ gives 3λ = 9, λ = μ = 3. z: 3 − 6 = −3 but 3 + 3 = 6: "
                "contradiction, so the lines do not meet and are skew.",
                "(b) <b>b</b> × <b>d</b> = (1·1 − (−2)(−2), (−2)(2) − 2·1, 2(−2) − 1·2)ᵀ = (−3, −6, −6)ᵀ; use (1, 2, 2)ᵀ, magnitude 3. "
                "<b>c</b> − <b>a</b> = (0, 9, 0)ᵀ, so d = |18|/3 = 6.",
                "(c) PQ→ = (2μ − 2λ, 9 − 2μ − λ, 2λ + μ)ᵀ. PQ→·(2, 1, −2)ᵀ = 9 − 9λ = 0 and PQ→·(2, −2, 1)ᵀ = −18 + 9μ = 0.",
                "So λ = 1, μ = 2: P = (3, 1, 1), Q = (5, 5, 5), PQ→ = (2, 4, 4)ᵀ (length 6, as in (b)).",
                "Common perpendicular: <b>r</b> = (3, 1, 1)ᵀ + t(1, 2, 2)ᵀ.",
            ],
        },
    ],

    "practice": [
        "Find the distance from (2, −1, 5) to the plane 2x + 2y − z = 3.",
        "Find the foot of the perpendicular from (1, 2, 3) to the plane x + y + z = 0, and the distance from the point to the plane.",
        "Find the reflection of (1, 2, 3) in the plane x + y + z = 0.",
        "Find the distance from (−1, 2) to the line 5x + 12y = 6.",
        "Find the foot of the perpendicular from P(2, 3, 1) to the line <b>r</b> = (0, 1, 1)ᵀ + λ(1, 1, 1)ᵀ, and the exact distance from P to the line.",
        "Show that the planes 2x − y + 2z = 1 and 4x − 2y + 4z = 11 are parallel and find the distance between them.",
        "Find the exact shortest distance between l₁: <b>r</b> = (1, 2, 3)ᵀ + λ(1, 0, 1)ᵀ and l₂: <b>r</b> = (0, 1, −1)ᵀ + μ(0, 1, 1)ᵀ.",
        "Without using a vector product, find the points P on the x-axis and Q on the line <b>r</b> = (0, 1, 2)ᵀ + μ(0, 1, 1)ᵀ for which PQ is "
        "perpendicular to both lines, and hence the shortest distance between the lines.",
        "Find a vector equation of the line of intersection of the planes x − y + z = 1 and x + 2y − z = 2.",
        "Show that the line <b>r</b> = (1, 1, 1)ᵀ + t(1, −1, 0)ᵀ is parallel to the plane x + y + 3z = 2, and find the exact distance between them.",
        "Find the values of k for which the point (k, 1, 2) is a distance 3 from the plane 2x + y − 2z = 1.",
        "Use a vector product to find the exact distance from (3, 0, −1) to the line (x − 1)/2 = (y + 1)/(−2) = z/1.",
    ],
    "answers": [
        "|4 − 2 − 5 − 3|/3 = 6/3 = 2.",
        "(1 + t) + (2 + t) + (3 + t) = 0 gives t = −2; foot (−1, 0, 1); distance 2√3.",
        "2t = −4: (−3, −2, −1).",
        "|−5 + 24 − 6|/13 = 1.",
        "(<b>p</b> − <b>a</b>)·<b>b</b> = 4, so λ = 4/3 and the foot is (4/3, 7/3, 7/3); PF→ = (−2/3, −2/3, 4/3)ᵀ, distance 2√6/3 ≈ 1.63.",
        "Second plane is 2x − y + 2z = 11/2 (same normal). Distance |11/2 − 1|/3 = 3/2.",
        "<b>b</b> × <b>d</b> = (−1, −1, 1)ᵀ, <b>c</b> − <b>a</b> = (−1, −1, −4)ᵀ, scalar product −2; d = 2/√3 = 2√3/3.",
        "P = (λ, 0, 0), Q = (0, 1 + μ, 2 + μ). PQ→·<b>i</b> = −λ = 0; PQ→·(0, 1, 1)ᵀ = 3 + 2μ = 0, μ = −3/2. P(0, 0, 0), Q(0, −1/2, 1/2); "
        "distance √2/2.",
        "Direction (1, 1, 1)ᵀ × (1, 2, −1)ᵀ → (−1, 2, 3)ᵀ; point (0, 3, 4) (x = 0); <b>r</b> = (0, 3, 4)ᵀ + t(−1, 2, 3)ᵀ.",
        "(1, −1, 0)·(1, 1, 3) = 0; (1, 1, 1) is not in the plane (1 + 1 + 3 = 5 ≠ 2); distance |5 − 2|/√11 = 3/√11 ≈ 0.905.",
        "|2k + 1 − 4 − 1|/3 = 3, so |2k − 4| = 9: k = 13/2 or k = −5/2.",
        "(<b>p</b> − <b>a</b>) = (2, 1, −1)ᵀ; × (2, −2, 1)ᵀ = (−1, −4, −6)ᵀ, magnitude √53; distance √53/3 ≈ 2.43.",
    ],

    "exam": [
        "The lines l₁ and l₂ have equations <b>r</b> = (2, −1, 1)ᵀ + λ(1, 2, −1)ᵀ and <b>r</b> = (4, −2, −5)ᵀ + μ(1, 0, 1)ᵀ.\n"
        "(a) Show that l₁ and l₂ are skew. [3]\n"
        "(b) Find the exact shortest distance between l₁ and l₂. [4]\n"
        "(c) Find the coordinates of the points P on l₁ and Q on l₂ such that PQ is perpendicular to both lines. [4]\n"
        "(d) Write down a Cartesian equation of the common perpendicular of l₁ and l₂. [2]",
        "The plane Π has equation x + 2y − 2z = −3 and A is the point (3, 4, −2).\n"
        "(a) Find the distance from A to Π. [2]\n"
        "(b) Find the coordinates of the foot N of the perpendicular from A to Π. [3]\n"
        "(c) Find the coordinates of the reflection A′ of A in Π. [2]\n"
        "(d) The line l passes through A and has direction (1, −1, 1)ᵀ. Find the coordinates of the point B where l meets Π. [3]\n"
        "(e) Find a vector equation of the reflection of l in Π. [3]",
        "The planes Π₁ and Π₂ have equations x − 2y + 2z = 1 and 2x + y + z = 7.\n"
        "(a) Find, to 0.1°, the acute angle between Π₁ and Π₂. [3]\n"
        "(b) Find a vector equation of the line L of intersection of Π₁ and Π₂. [4]\n"
        "(c) Find, to 3 significant figures, the distance from P(4, 2, −1) to L. [4]",
        "(No vector product is needed in this question.) The line l passes through A(1, 3, −2) and B(3, 2, 0). The point C is (6, 3, 2).\n"
        "(a) Find a vector equation of l. [2]\n"
        "(b) Find the coordinates of the point F on l such that CF is perpendicular to l. [4]\n"
        "(c) Find the exact area of triangle ABC. [2]\n"
        "(d) Find the coordinates of the two points on l that are a distance 3 from C. [4]",
    ],
    "exam_answers": [
        "(a) Directions not parallel. B1 2 + λ = 4 + μ, −1 + 2λ = −2, 1 − λ = −5 + μ: from the second λ = −1/2, then μ = −5/2 from the "
        "first M1; third: 3/2 ≠ −15/2, contradiction, so skew. A1\n"
        "(b) <b>b</b> × <b>d</b> = (2, −2, −2)ᵀ ∝ (1, −1, −1)ᵀ M1 A1; <b>c</b> − <b>a</b> = (2, −1, −6)ᵀ, scalar product 2 + 1 + 6 = 9 M1; "
        "d = 9/√3 = 3√3 (≈ 5.20). A1\n"
        "(c) PQ→ = (2 + μ − λ, −1 − 2λ, −6 + μ + λ)ᵀ. PQ→·(1, 2, −1)ᵀ = 6 − 6λ = 0 and PQ→·(1, 0, 1)ᵀ = −4 + 2μ = 0 M1 A1; "
        "λ = 1, μ = 2 A1; P(3, 1, 0), Q(6, −2, −3). A1\n"
        "(d) Direction (1, −1, −1): (x − 3)/1 = (y − 1)/(−1) = z/(−1). M1 A1",
        "(a) |3 + 8 + 4 + 3|/3 = 18/3 = 6. M1 A1\n"
        "(b) (3 + t) + 2(4 + 2t) − 2(−2 − 2t) = −3 M1, 15 + 9t = −3, t = −2 A1; N(1, 0, 2). A1\n"
        "(c) A′ = A + 2(−2)(1, 2, −2) M1 = (−1, −4, 6). A1\n"
        "(d) (3 + s) + 2(4 − s) − 2(−2 + s) = −3 M1, 15 − 3s = −3, s = 6 A1; B(9, −2, 4). A1\n"
        "(e) The reflected line passes through B and A′ M1: direction A′ − B = (−10, −2, 2)ᵀ ∝ (5, 1, −1)ᵀ A1; "
        "<b>r</b> = (9, −2, 4)ᵀ + t(5, 1, −1)ᵀ. A1",
        "(a) <b>n₁</b>·<b>n₂</b> = 2 − 2 + 2 = 2, |<b>n₁</b>| = 3, |<b>n₂</b>| = √6 M1; cos θ = 2/(3√6) M1; θ = 74.2°. A1\n"
        "(b) <b>n₁</b> × <b>n₂</b> = (−4, 3, 5)ᵀ M1 A1; z = 0: x − 2y = 1, 2x + y = 7, so (3, 1, 0) M1; <b>r</b> = (3, 1, 0)ᵀ + t(−4, 3, 5)ᵀ. A1\n"
        "(c) <b>p</b> − <b>a</b> = (1, 1, −1)ᵀ; (1, 1, −1)ᵀ × (−4, 3, 5)ᵀ = (8, −1, 7)ᵀ M1 A1; distance √114/√50 M1 = 1.51. A1",
        "(a) <b>r</b> = (1, 3, −2)ᵀ + λ(2, −1, 2)ᵀ. M1 A1\n"
        "(b) CF→ = (2λ − 5, −λ, 2λ − 4)ᵀ M1; CF→·(2, −1, 2)ᵀ = 9λ − 18 = 0 M1 A1; λ = 2, F(5, 1, 2). A1\n"
        "(c) |CF| = |(−1, −2, 0)| = √5, |AB| = 3 M1; area = ½ × 3 × √5 = 3√5/2. A1\n"
        "(d) Points at parameter λ have distance² = 5 + 9(λ − 2)² M1 = 9 M1, so λ − 2 = ±2/3 A1; λ = 8/3 gives (19/3, 1/3, 10/3); "
        "λ = 4/3 gives (11/3, 5/3, 2/3). A1",
    ],
}
