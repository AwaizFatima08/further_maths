"""Unit A9: Lines and planes in three dimensions."""

UNIT = {
    "number": "A9",
    "title": "Lines and planes in three dimensions",
    "tag": "AS · Edexcel CP 6.1–6.4 (AS) · IAL FP3 5.2, 5.3 · AQA F1, F3, F4 (AS, lines), F2 and the plane parts of F3 (A level) · "
           "OCR A 4.04a, c, e (AS), 4.04b, d, f (A level) · OCR MEI vector language, Pv1–Pv3, Pv6 (AS), Pv9–Pv12, Pv14, Pv15 "
           "(A level) · CAIE 9231 P1 1.6 (lines revised from 9709 P3)",
    "notes": [
        ("p", "This unit builds the language of three-dimensional geometry: how to describe a straight line and a flat plane with "
              "an equation, how to measure the angle between them, and how to decide whether lines meet. Unit A10 adds the vector "
              "product, which gives quicker ways to find normals, and Unit A12 uses all of this to find distances. Boards split "
              "the work differently: lines are AS for Edexcel, AQA and OCR A, planes are AS for Edexcel and MEI, and both are "
              "A level elsewhere, so check the tag above."),

        ("h2", "9.1 The language of vectors (all boards; MEI unnumbered statement)"),
        ("bullets", [
            "A <b>vector</b> has magnitude and direction; a <b>scalar</b> has magnitude only. In print vectors are bold "
            "(<b>a</b>); in handwriting underline them (a̲).",
            "The <b>position vector</b> of a point A is <b>a</b> = OA→, the vector from the origin O to A. If A is (2, −1, 3) then "
            "<b>a</b> = 2<b>i</b> − <b>j</b> + 3<b>k</b> = (2, −1, 3)ᵀ. In this book a column vector is written on one line as (x, y, z)ᵀ; "
            "a point is written A(x, y, z) without the ᵀ.",
            "AB→ = <b>b</b> − <b>a</b> (“end minus start”). The midpoint of AB has position vector ½(<b>a</b> + <b>b</b>).",
            "<b>Magnitude</b>: |(x, y, z)ᵀ| = √(x² + y² + z²). The distance AB is |<b>b</b> − <b>a</b>|.",
            "A <b>unit vector</b> has magnitude 1. The unit vector in the direction of <b>a</b> is <b>â</b> = <b>a</b>/|<b>a</b>|.",
            "<b>a</b> and <b>b</b> are <b>parallel</b> if <b>b</b> = k<b>a</b> for some scalar k ≠ 0. Points A, B, C are <b>collinear</b> "
            "if AB→ and AC→ are parallel (they share the point A).",
            "The point dividing AB in the ratio m : n has position vector (n<b>a</b> + m<b>b</b>)/(m + n).",
        ]),

        ("h2", "9.2 Equations of a straight line (Ed 6.1, IAL 5.2, AQA F1, OCR 4.04a, MEI Pv9)"),
        ("p", "A line is fixed by one point on it and its direction. If A is a point on the line with position vector <b>a</b>, and "
              "<b>b</b> is a <b>direction vector</b> (any non-zero vector parallel to the line), then every point R on the line is "
              "reached by going to A and then some multiple λ of <b>b</b>. As the scalar parameter λ runs through all real numbers, "
              "R runs along the whole line."),
        ("figure", "pa09_line.png", "The line through A in direction b: every point R has r = a + λb.", 82),
        ("box", "Equations of a line", [
            "<b>Vector form</b>: <b>r</b> = <b>a</b> + λ<b>b</b>. For the line through A and B use <b>r</b> = <b>a</b> + λ(<b>b</b> − <b>a</b>).",
            "<b>Cartesian form</b> (3-D): with <b>a</b> = (a₁, a₂, a₃)ᵀ and <b>b</b> = (b₁, b₂, b₃)ᵀ, eliminating λ gives "
            "(x − a₁)/b₁ = (y − a₂)/b₂ = (z − a₃)/b₃ (= λ).",
            "If one component is zero, say b₃ = 0, write (x − a₁)/b₁ = (y − a₂)/b₂, z = a₃.",
            "In 2-D the same vector form <b>r</b> = (a₁, a₂)ᵀ + λ(b₁, b₂)ᵀ gives a single Cartesian equation, the familiar y = mx + c type.",
        ]),
        ("p", "To turn a Cartesian equation back into vector form, make every numerator of the form (x − number) with coefficient +1 "
              "on x, y and z. For example (x − 1)/2 = (y + 3)/(−1) = (4 − z)/3 has z-numerator 4 − z = −(z − 4), so it equals "
              "(z − 4)/(−3): the line passes through (1, −3, 4) with direction (2, −1, −3)ᵀ. A line has many correct vector equations: "
              "any point on it and any multiple of the direction vector will do."),

        ("h2", "9.3 The scalar product, angles and perpendicular vectors (Ed 6.3–6.4, AQA F3–F4, OCR 4.04c, MEI Pv1, Pv10)"),
        ("box", "Scalar (dot) product", [
            "<b>a</b>·<b>b</b> = |<b>a</b>||<b>b</b>| cos θ, where θ is the angle between <b>a</b> and <b>b</b> when both point away from a common point.",
            "In components: (a₁, a₂, a₃)ᵀ·(b₁, b₂, b₃)ᵀ = a₁b₁ + a₂b₂ + a₃b₃, a scalar.",
            "So cos θ = <b>a</b>·<b>b</b> / (|<b>a</b>||<b>b</b>|).",
            "<b>Perpendicular</b>: for non-zero vectors, <b>a</b>·<b>b</b> = 0 ⇔ <b>a</b> ⊥ <b>b</b>.",
            "Rules: <b>a</b>·<b>b</b> = <b>b</b>·<b>a</b>; <b>a</b>·(<b>b</b> + <b>c</b>) = <b>a</b>·<b>b</b> + <b>a</b>·<b>c</b>; <b>a</b>·<b>a</b> = |<b>a</b>|²; "
            "<b>i</b>·<b>i</b> = 1, <b>i</b>·<b>j</b> = 0, and so on.",
        ]),
        ("p", "The angle between two lines is the angle between their direction vectors. If the scalar product is negative the "
              "formula gives an obtuse angle θ; the <b>acute</b> angle between the lines is then 180° − θ. Using |<b>b</b>·<b>d</b>| in the "
              "numerator gives the acute angle directly. Lines in 3-D need not meet for an angle between them to be defined: it is "
              "the angle between their directions."),

        ("h2", "9.4 Intersecting, parallel and skew lines (Ed 6.1, AQA F6, OCR 4.04e, MEI Pv11–Pv12)"),
        ("p", "In two dimensions two distinct lines either meet or are parallel. In three dimensions there is a third possibility: "
              "<b>skew</b> lines are not parallel and never meet, like a road and a railway on a bridge above it."),
        ("figure", "pa09_three_cases.png", "Two lines in space intersect, are parallel, or are skew.", 140),
        ("box", "Deciding how two lines are related", [
            "Take l₁: <b>r</b> = <b>a</b> + λ<b>b</b> and l₂: <b>r</b> = <b>c</b> + μ<b>d</b>.",
            "1. If <b>d</b> = k<b>b</b> the lines are parallel (or the same line, if a point of one lies on the other).",
            "2. Otherwise equate the components of <b>a</b> + λ<b>b</b> and <b>c</b> + μ<b>d</b>: three equations in two unknowns.",
            "3. Solve two of the equations for λ and μ, then substitute into the <b>third</b>. If it is satisfied the lines intersect; "
            "substitute λ (or μ) back to get the point. If not, the lines are skew.",
        ]),

        ("h2", "9.5 Equations of a plane (Ed 6.2–6.3, IAL 5.3, AQA F2, OCR 4.04b, MEI Pv2–Pv3, CAIE 1.6)"),
        ("p", "A <b>normal</b> to a plane is a non-zero vector perpendicular to the plane. It is perpendicular to every line lying in the "
              "plane (MEI Pv3). If A is a point of the plane and <b>n</b> a normal, then R lies in the plane exactly when AR→ = <b>r</b> − <b>a</b> "
              "is perpendicular to <b>n</b>."),
        ("figure", "pa09_plane.png", "A plane through A with normal n: R is in the plane exactly when (r − a)·n = 0.", 80),
        ("box", "Four forms of the equation of a plane", [
            "<b>Scalar product form</b>: (<b>r</b> − <b>a</b>)·<b>n</b> = 0, equivalently <b>r</b>·<b>n</b> = p where p = <b>a</b>·<b>n</b>.",
            "<b>Cartesian form</b>: with <b>n</b> = (a, b, c)ᵀ and <b>r</b> = (x, y, z)ᵀ, <b>r</b>·<b>n</b> = p becomes ax + by + cz = p. "
            "The coefficients of x, y, z are the components of a normal. (MEI writes n₁x + n₂y + n₃z + d = 0.)",
            "<b>Vector (parametric) form</b>: <b>r</b> = <b>a</b> + λ<b>b</b> + μ<b>c</b>, where <b>b</b> and <b>c</b> are non-parallel vectors in the "
            "plane (not required by MEI).",
            "If |<b>n</b>| = 1 in <b>r</b>·<b>n</b> = p, then |p| is the perpendicular distance of the plane from O (see Unit A12).",
        ]),
        ("p", "<b>Converting r = a + λb + μc to Cartesian form.</b> Find a normal <b>n</b> = (n₁, n₂, n₃)ᵀ with <b>n</b>·<b>b</b> = 0 and "
              "<b>n</b>·<b>c</b> = 0. These are two equations in three unknowns, so choose one component (for example n₃ = 1) and solve for "
              "the others; any non-zero multiple of the answer is also a normal. Then p = <b>a</b>·<b>n</b>. Unit A10 shows that "
              "<b>n</b> = <b>b</b> × <b>c</b> does this in one step."),
        ("p", "<b>Converting ax + by + cz = p to vector form.</b> Find three non-collinear points on the plane (set two coordinates "
              "and solve for the third), then use one as <b>a</b> and the two differences as <b>b</b> and <b>c</b>. A plane through "
              "three points A, B, C has equation <b>r</b> = <b>a</b> + λ(<b>b</b> − <b>a</b>) + μ(<b>c</b> − <b>a</b>)."),

        ("h2", "9.6 Angles between planes and between a line and a plane (Ed 6.3, AQA F3, OCR 4.04d, MEI Pv6, Pv15)"),
        ("figure", "pa09_line_plane_angle.png", "The angle θ between a line and a plane is 90° minus the angle between the line and the normal.", 80),
        ("table", ["Angle wanted", "Use", "Formula for the acute angle"], [
            ["Between lines with directions <b>b</b>, <b>d</b>", "direction vectors", "cos θ = |<b>b</b>·<b>d</b>| / (|<b>b</b>||<b>d</b>|)"],
            ["Between planes with normals <b>n₁</b>, <b>n₂</b>", "normals", "cos θ = |<b>n₁</b>·<b>n₂</b>| / (|<b>n₁</b>||<b>n₂</b>|)"],
            ["Between a line (direction <b>b</b>) and a plane (normal <b>n</b>)", "direction and normal", "sin θ = |<b>b</b>·<b>n</b>| / (|<b>b</b>||<b>n</b>|)"],
        ]),
        ("p", "Two planes meet in a line, and the angle between the planes is the angle between their normals (or 180° minus it). For "
              "a line and a plane, the scalar product of <b>b</b> and <b>n</b> gives the angle φ between the line and the <b>normal</b>; "
              "the angle with the plane itself is θ = 90° − φ, which is why sine replaces cosine."),

        ("h2", "9.7 A line meeting a plane (Ed 6.5, AQA F6, OCR 4.04f, MEI Pv14, CAIE 1.6)"),
        ("p", "Write the general point of the line in terms of λ, substitute into the Cartesian equation of the plane and solve the "
              "linear equation for λ. Three things can happen:"),
        ("bullets", [
            "One solution for λ: the line meets the plane at one point. Substitute λ back into the line.",
            "No solution (the equation reduces to something like 0 = 3): the line is parallel to the plane and does not meet it.",
            "Every λ works (0 = 0): the line lies in the plane.",
            "Quick test: the line is parallel to or lies in the plane exactly when <b>b</b>·<b>n</b> = 0. Then it lies in the plane if "
            "the point A of the line satisfies the plane's equation.",
        ]),
        ("warn", "Common mistakes", [
            "Using a position vector instead of a direction vector when finding the angle between two lines.",
            "Finding the angle between a line and a plane with cosine and forgetting to take 90° minus the angle with the normal.",
            "Deciding two lines intersect after solving only two of the three equations: the third equation must be checked.",
            "Writing (x − 1)/2 = (y + 3)/(−1) = (4 − z)/3 as having direction (2, −1, 3)ᵀ: the z-numerator must be rewritten as (z − 4)/(−3).",
            "Using the same parameter letter for two different lines. Call them λ and μ.",
            "Giving an obtuse angle when the question asks for the acute angle between lines or planes.",
        ]),
    ],

    "examples": [
        {
            "title": "Vector and Cartesian equations of a line",
            "question": "Find a vector equation and a Cartesian equation of the line l through A(2, −1, 3) and B(5, 1, −1). "
                        "Determine whether C(11, 5, −9) lies on l.",
            "steps": [
                "Direction: AB→ = <b>b</b> − <b>a</b> = (5 − 2, 1 − (−1), −1 − 3)ᵀ = (3, 2, −4)ᵀ.",
                "Vector equation: <b>r</b> = (2, −1, 3)ᵀ + λ(3, 2, −4)ᵀ.",
                "General point: x = 2 + 3λ, y = −1 + 2λ, z = 3 − 4λ. Making λ the subject of each gives the Cartesian equation "
                "(x − 2)/3 = (y + 1)/2 = (z − 3)/(−4).",
                "For C: x = 11 gives λ = 3. Check y: −1 + 2(3) = 5 ✓. Check z: 3 − 4(3) = −9 ✓.",
                "All three coordinates agree with λ = 3, so C lies on l.",
            ],
        },
        {
            "title": "The acute angle between two lines",
            "question": "Find the acute angle between l₁: <b>r</b> = (1, 0, 2)ᵀ + λ(2, −1, 2)ᵀ and l₂: <b>r</b> = (3, 1, −1)ᵀ + μ(1, 4, −1)ᵀ.",
            "steps": [
                "Use the direction vectors only: <b>b</b> = (2, −1, 2)ᵀ, <b>d</b> = (1, 4, −1)ᵀ.",
                "<b>b</b>·<b>d</b> = 2 − 4 − 2 = −4. |<b>b</b>| = √9 = 3, |<b>d</b>| = √18 = 3√2.",
                "cos θ = −4/(9√2), so θ = 108.3°, which is obtuse.",
                "The acute angle between the lines is 180° − 108.3° = 71.7° (3 s.f.). Equivalently, cos θ = 4/(9√2) gives 71.7° directly.",
            ],
        },
        {
            "title": "Do two lines intersect?",
            "question": "Show that the lines l₁: <b>r</b> = (1, 2, −1)ᵀ + λ(1, −1, 2)ᵀ and l₂: <b>r</b> = (2, 5, 0)ᵀ + μ(1, −5, 3)ᵀ intersect, and "
                        "find the point of intersection.",
            "steps": [
                "The directions are not multiples of each other, so the lines are not parallel.",
                "Equate components: x: 1 + λ = 2 + μ (1); y: 2 − λ = 5 − 5μ (2); z: −1 + 2λ = 3μ (3).",
                "(1) + (2): 3 = 7 − 4μ, so μ = 1, and then λ = 2 from (1).",
                "Check in (3): left side −1 + 4 = 3, right side 3(1) = 3 ✓. All three equations hold, so the lines intersect.",
                "Point: λ = 2 in l₁ gives (1 + 2, 2 − 2, −1 + 4) = (3, 0, 3). (Check with μ = 1 in l₂: (3, 0, 3) ✓.)",
            ],
        },
        {
            "title": "The plane through three points",
            "question": "Find a vector equation and a Cartesian equation of the plane through A(1, 0, 2), B(3, 1, 1) and C(0, 2, 4).",
            "steps": [
                "AB→ = (2, 1, −1)ᵀ and AC→ = (−1, 2, 2)ᵀ lie in the plane and are not parallel.",
                "Vector equation: <b>r</b> = (1, 0, 2)ᵀ + λ(2, 1, −1)ᵀ + μ(−1, 2, 2)ᵀ.",
                "Normal <b>n</b> = (n₁, n₂, n₃)ᵀ: 2n₁ + n₂ − n₃ = 0 and −n₁ + 2n₂ + 2n₃ = 0. Take n₃ = 5: 2n₁ + n₂ = 5 and −n₁ + 2n₂ = −10, "
                "giving n₁ = 4, n₂ = −3. So <b>n</b> = (4, −3, 5)ᵀ.",
                "<b>a</b>·<b>n</b> = 4(1) − 3(0) + 5(2) = 14. Cartesian equation: 4x − 3y + 5z = 14.",
                "Check: B gives 12 − 3 − 5 = 14 ✓ and C gives 0 − 6 + 20 = 14 ✓.",
            ],
        },
        {
            "title": "Angles between two planes and between a line and a plane",
            "question": "Planes Π₁: 2x − y + 2z = 9 and Π₂: x + y − z = 1. Line l: <b>r</b> = (1, 2, 0)ᵀ + t(1, 1, 4)ᵀ. Find (a) the acute angle "
                        "between Π₁ and Π₂, (b) the acute angle between l and Π₁.",
            "steps": [
                "(a) Normals <b>n₁</b> = (2, −1, 2)ᵀ, <b>n₂</b> = (1, 1, −1)ᵀ. <b>n₁</b>·<b>n₂</b> = 2 − 1 − 2 = −1, |<b>n₁</b>| = 3, |<b>n₂</b>| = √3.",
                "cos θ = |−1|/(3√3) = 1/(3√3), so θ = 78.9° (3 s.f.).",
                "(b) <b>b</b> = (1, 1, 4)ᵀ, |<b>b</b>| = √18 = 3√2. <b>b</b>·<b>n₁</b> = 2 − 1 + 8 = 9.",
                "sin θ = 9/(3 × 3√2) = 1/√2, so the angle between l and Π₁ is 45°.",
                "(Using cosine here would give the angle between l and the normal, which is also 45° in this special case: always "
                "subtract from 90°.)",
            ],
        },
        {
            "title": "Where a line meets a plane (exam standard)",
            "question": "Using the line l and plane Π₁ of the previous example, find the point where l meets Π₁. Show also that the line "
                        "m: <b>r</b> = (1, −1, 2)ᵀ + s(2, 1, −1)ᵀ lies in the plane x − y + z = 4.",
            "steps": [
                "General point of l: (1 + t, 2 + t, 4t). Substitute into 2x − y + 2z = 9: 2(1 + t) − (2 + t) + 2(4t) = 9.",
                "So 2 + 2t − 2 − t + 8t = 9, giving 9t = 9 and t = 1. The point is (2, 3, 4). Check: 4 − 3 + 8 = 9 ✓.",
                "For m: direction (2, 1, −1)ᵀ and normal (1, −1, 1)ᵀ give 2 − 1 − 1 = 0, so m is parallel to the plane or lies in it.",
                "The point (1, −1, 2) of m gives 1 + 1 + 2 = 4, so it lies in the plane. A line parallel to a plane with one point "
                "in it lies entirely in it.",
                "Equivalently, substituting the general point (1 + 2s, −1 + s, 2 − s) gives 1 + 2s + 1 − s + 2 − s = 4 for every s.",
            ],
        },
    ],

    "practice": [
        "Find a vector equation and a Cartesian equation of the line through (3, −2, 1) parallel to 2<b>i</b> − <b>j</b> + 5<b>k</b>.",
        "The points A and B have coordinates (1, 2, −2) and (4, 6, 10). Find (a) |AB→|, (b) the unit vector in the direction of AB→, "
        "(c) the position vector of the point P dividing AB in the ratio 1 : 2.",
        "Find, to 0.1°, the angle between <b>a</b> = <b>i</b> + 2<b>j</b> + 2<b>k</b> and <b>b</b> = 3<b>i</b> + 4<b>k</b>.",
        "Find the value of p for which (p, 2, −1)ᵀ and (3, p, 4)ᵀ are perpendicular.",
        "Write the line (x − 1)/2 = (y + 3)/(−1) = (4 − z)/3 in vector form. Find also a Cartesian equation of the 2-D line "
        "<b>r</b> = (1, 3)ᵀ + λ(2, −1)ᵀ.",
        "Show that the lines l₁: <b>r</b> = (1, 0, 1)ᵀ + λ(1, 1, 0)ᵀ and l₂: <b>r</b> = (0, 2, 0)ᵀ + μ(0, 1, 1)ᵀ are skew.",
        "The lines <b>r</b> = (1, 2, 3)ᵀ + λ(1, 0, −1)ᵀ and <b>r</b> = (2, p, 1)ᵀ + μ(0, 1, 1)ᵀ intersect. Find p and the point of intersection.",
        "Find a Cartesian equation of the plane <b>r</b> = (1, 1, 0)ᵀ + λ(1, 0, 2)ᵀ + μ(0, 1, −1)ᵀ.",
        "Find the equation of the plane through (2, −1, 4) perpendicular to 3<b>i</b> + <b>j</b> − 2<b>k</b>, in the form <b>r</b>·<b>n</b> = p "
        "and in Cartesian form.",
        "Find, to 0.1°, the acute angle between the planes x + 2y − 2z = 3 and 2x − y + 2z = 0.",
        "Find, to 0.1°, the acute angle between the line (x − 1)/2 = y/(−1) = (z + 2)/2 and the plane x + y + z = 4.",
        "The line l has equation <b>r</b> = (1, −1, 2)ᵀ + t(2, 1, −1)ᵀ. Show that l does not meet the plane x − y + z = 5, and that l lies "
        "in the plane x − y + z = 4.",
    ],
    "answers": [
        "<b>r</b> = (3, −2, 1)ᵀ + λ(2, −1, 5)ᵀ; (x − 3)/2 = (y + 2)/(−1) = (z − 1)/5.",
        "(a) AB→ = (3, 4, 12)ᵀ, |AB→| = 13. (b) (3/13, 4/13, 12/13)ᵀ. (c) <b>p</b> = (2<b>a</b> + <b>b</b>)/3 = (2, 10/3, 2)ᵀ.",
        "<b>a</b>·<b>b</b> = 11, |<b>a</b>| = 3, |<b>b</b>| = 5, cos θ = 11/15, θ = 42.8°.",
        "3p + 2p − 4 = 0, so p = 4/5.",
        "<b>r</b> = (1, −3, 4)ᵀ + λ(2, −1, −3)ᵀ. 2-D: x = 1 + 2λ, y = 3 − λ, so x + 2y = 7.",
        "Directions (1, 1, 0)ᵀ, (0, 1, 1)ᵀ not parallel. x: 1 + λ = 0 gives λ = −1; y: λ = 2 + μ gives μ = −3; z: 1 = μ = −3, "
        "contradiction. Not parallel and do not meet, so skew.",
        "x: 1 + λ = 2, λ = 1; z: 3 − λ = 1 + μ, μ = 1; y: 2 = p + μ, p = 1. Point (2, 2, 2).",
        "Normal (2, −1, −1)ᵀ (perpendicular to both direction vectors); 2x − y − z = 1.",
        "<b>r</b>·(3, 1, −2)ᵀ = −3; 3x + y − 2z = −3.",
        "<b>n₁</b>·<b>n₂</b> = 2 − 2 − 4 = −4, |<b>n₁</b>| = |<b>n₂</b>| = 3, cos θ = 4/9, θ = 63.6°.",
        "<b>b</b> = (2, −1, 2)ᵀ, <b>n</b> = (1, 1, 1)ᵀ, <b>b</b>·<b>n</b> = 3, sin θ = 3/(3√3) = 1/√3, θ = 35.3°.",
        "<b>b</b>·<b>n</b> = 2 − 1 − 1 = 0, so l is parallel to both planes. Substituting (1 + 2t, −1 + t, 2 − t): x − y + z = 4 for "
        "every t. So 4 = 5 is impossible (no intersection with the first plane), and l lies in x − y + z = 4.",
    ],

    "exam": [
        "The line l₁ passes through A(2, 1, −1) and B(4, 0, 1). The line l₂ has equation <b>r</b> = (6, −3, 1)ᵀ + μ(0, 1, 1)ᵀ.\n"
        "(a) Find a vector equation of l₁. [2]\n"
        "(b) Show that l₁ and l₂ intersect, and find the coordinates of the point of intersection P. [5]\n"
        "(c) Find, to 0.1°, the acute angle between l₁ and l₂. [3]\n"
        "(d) Find a Cartesian equation of the plane containing l₁ and l₂. [4]",
        "The plane Π has vector equation <b>r</b> = (1, 0, 2)ᵀ + λ(2, 1, 0)ᵀ + μ(0, 1, −1)ᵀ.\n"
        "(a) Show that the vector <b>i</b> − 2<b>j</b> − 2<b>k</b> is perpendicular to Π. [2]\n"
        "(b) Find a Cartesian equation of Π. [2]\n"
        "(c) The line l has equation (x − 5)/1 = (y + 1)/2 = (z − 4)/(−2). Find the coordinates of the point where l meets Π. [4]\n"
        "(d) Find, to 0.1°, the acute angle between l and Π. [3]",
        "The planes Π₁ and Π₂ have equations x + 2y − z = 4 and 2x − y + z = 3.\n"
        "(a) Find, to 0.1°, the acute angle between Π₁ and Π₂. [3]\n"
        "(b) Show that the line l: <b>r</b> = (1, 4, 5)ᵀ + t(1, −3, −5)ᵀ lies in both planes. [4]\n"
        "(c) The line m passes through A(2, 1, 3) and is perpendicular to Π₁. Find the coordinates of the point where m meets Π₁. [4]",
    ],
    "exam_answers": [
        "(a) AB→ = (2, −1, 2)ᵀ; <b>r</b> = (2, 1, −1)ᵀ + λ(2, −1, 2)ᵀ. B1 B1\n"
        "(b) 2 + 2λ = 6, 1 − λ = −3 + μ, −1 + 2λ = 1 + μ. M1 From the first λ = 2, then μ = 2 from the second. M1 A1 "
        "Third: 3 = 3 ✓, so the lines intersect. A1 P(6, −1, 3). A1\n"
        "(c) (2, −1, 2)ᵀ·(0, 1, 1)ᵀ = 1; cos θ = 1/(3√2) M1 A1; θ = 76.4°. A1\n"
        "(d) Normal perpendicular to (2, −1, 2)ᵀ and (0, 1, 1)ᵀ: (3, 2, −2)ᵀ. M1 A1 Through A: 6 + 2 + 2 = 10. M1 "
        "3x + 2y − 2z = 10. A1",
        "(a) (1, −2, −2)ᵀ·(2, 1, 0)ᵀ = 2 − 2 + 0 = 0 and (1, −2, −2)ᵀ·(0, 1, −1)ᵀ = 0 − 2 + 2 = 0, so it is perpendicular to two "
        "non-parallel vectors in Π. M1 A1\n"
        "(b) (1, 0, 2)·(1, −2, −2) = −3: x − 2y − 2z = −3. M1 A1\n"
        "(c) (5 + t) − 2(−1 + 2t) − 2(4 − 2t) = −3 M1, so −1 + t = −3, t = −2 M1 A1; point (3, −5, 8). A1\n"
        "(d) <b>b</b> = (1, 2, −2)ᵀ, <b>n</b> = (1, −2, −2)ᵀ: <b>b</b>·<b>n</b> = 1, |<b>b</b>| = |<b>n</b>| = 3. M1 sin θ = 1/9 M1; θ = 6.4°. A1",
        "(a) <b>n₁</b>·<b>n₂</b> = 2 − 2 − 1 = −1; |<b>n₁</b>| = |<b>n₂</b>| = √6 M1; cos θ = 1/6 M1; θ = 80.4°. A1\n"
        "(b) Point: 1 + 8 − 5 = 4 ✓ and 2 − 4 + 5 = 3 ✓. M1 A1 Direction: (1, −3, −5)·(1, 2, −1) = 1 − 6 + 5 = 0 and "
        "(1, −3, −5)·(2, −1, 1) = 2 + 3 − 5 = 0, so l is parallel to both planes and has a point in each: it lies in both. M1 A1\n"
        "(c) m: <b>r</b> = (2, 1, 3)ᵀ + s(1, 2, −1)ᵀ. B1 (2 + s) + 2(1 + 2s) − (3 − s) = 4 M1, so 1 + 6s = 4, s = ½ A1; "
        "point (5/2, 2, 5/2). A1",
    ],
}
