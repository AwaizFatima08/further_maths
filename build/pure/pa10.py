"""Unit A10: The vector product and scalar triple product."""

UNIT = {
    "number": "A10",
    "title": "The vector product and scalar triple product",
    "tag": "Edexcel FP1 5.1–5.3 (A level option) and AS FP1 3.1–3.3 · IAL FP3 5.1, 5.2 · AQA F5 (A level) · OCR A 4.04g (AS, "
           "magnitude excluded), Additional Pure 8.04a–d (Y535/Y545), 8.04e (Y545) · OCR MEI Pv7, Pv8 (A level) · CAIE 9231 P1 1.6",
    "notes": [
        ("p", "The scalar product of two vectors is a number. The <b>vector product</b> (or cross product) of two vectors is a "
              "<b>vector</b>, perpendicular to both. It gives normals to planes in one step, areas of triangles and parallelograms, "
              "a new form of the equation of a line, and, combined with the scalar product, volumes. Unit A9 is assumed."),
        ("bullets", [
            "OCR A AS (4.04g) needs only the component formula to find a vector perpendicular to two given vectors.",
            "Sections 10.6 (direction cosines) and 10.7 (scalar triple product) are needed by Edexcel, IAL and OCR A Y545 only; "
            "the line (r − a) × b = 0 is needed by Edexcel, IAL, AQA and OCR A Additional Pure.",
        ]),

        ("h2", "10.1 Definition of the vector product (Ed FP1 5.1, OCR 8.04a, MEI Pv8, CAIE 1.6)"),
        ("p", "For vectors <b>a</b> and <b>b</b> with angle θ between them (0 ≤ θ ≤ π), the vector product is"),
        ("box", "Geometric definition", [
            "<b>a</b> × <b>b</b> = |<b>a</b>||<b>b</b>| sin θ <b>n̂</b>,",
            "where <b>n̂</b> is the unit vector perpendicular to both <b>a</b> and <b>b</b> chosen so that <b>a</b>, <b>b</b>, <b>n̂</b> form a "
            "<b>right-handed set</b>: point the first finger of your right hand along <b>a</b> and the second finger along <b>b</b>; "
            "the thumb then points along <b>n̂</b> (equivalently, turning a screw from <b>a</b> towards <b>b</b> drives it along <b>n̂</b>).",
            "|<b>a</b> × <b>b</b>| = |<b>a</b>||<b>b</b>| sin θ, which is the area of the parallelogram with sides <b>a</b> and <b>b</b>.",
        ]),
        ("figure", "pa10_cross.png", "a × b is perpendicular to a and b, and its length is the area of the parallelogram they span.", 80),
        ("p", "The coordinate axes are right-handed, so <b>i</b> × <b>j</b> = <b>k</b>, <b>j</b> × <b>k</b> = <b>i</b>, <b>k</b> × <b>i</b> = <b>j</b> "
              "(cyclic order), while <b>j</b> × <b>i</b> = −<b>k</b>, <b>k</b> × <b>j</b> = −<b>i</b>, <b>i</b> × <b>k</b> = −<b>j</b>, and "
              "<b>i</b> × <b>i</b> = <b>j</b> × <b>j</b> = <b>k</b> × <b>k</b> = <b>0</b> because sin 0 = 0."),

        ("h2", "10.2 The component formula (Ed FP1 5.1, IAL 5.1, AQA F5, OCR 4.04g, MEI Pv7, CAIE 1.6)"),
        ("p", "Expanding (a₁<b>i</b> + a₂<b>j</b> + a₃<b>k</b>) × (b₁<b>i</b> + b₂<b>j</b> + b₃<b>k</b>) term by term with the rules above gives the "
              "formula below. It is in the Edexcel, OCR and MEI formula booklets; Cambridge requires you to recall it."),
        ("box", "Vector product in components", [
            "<b>a</b> × <b>b</b> = (a₂b₃ − a₃b₂)<b>i</b> + (a₃b₁ − a₁b₃)<b>j</b> + (a₁b₂ − a₂b₁)<b>k</b>.",
            "As a determinant: <b>a</b> × <b>b</b> = | <b>i</b> <b>j</b> <b>k</b> ; a₁ a₂ a₃ ; b₁ b₂ b₃ |, expanded along the top row "
            "(remember the minus sign on the <b>j</b> term).",
            "Check every answer: (<b>a</b> × <b>b</b>)·<b>a</b> = 0 and (<b>a</b> × <b>b</b>)·<b>b</b> = 0.",
        ]),
        ("p", "Calculators with a vector mode will find vector products; OCR A explicitly allows this. You must still be able to do it "
              "by hand, and in “show that” questions every step must be seen."),

        ("h2", "10.3 Properties (OCR 8.04b, 8.04d, MEI Pv8)"),
        ("box", "Algebra of the vector product", [
            "<b>Anti-commutative</b>: <b>b</b> × <b>a</b> = −(<b>a</b> × <b>b</b>). Order matters.",
            "<b>Distributive</b>: <b>a</b> × (<b>b</b> + <b>c</b>) = <b>a</b> × <b>b</b> + <b>a</b> × <b>c</b>.",
            "Scalars: (k<b>a</b>) × <b>b</b> = <b>a</b> × (k<b>b</b>) = k(<b>a</b> × <b>b</b>).",
            "<b>a</b> × <b>a</b> = <b>0</b>. For non-zero vectors, <b>a</b> × <b>b</b> = <b>0</b> ⇔ <b>a</b> and <b>b</b> are parallel (θ = 0 or π).",
            "Not associative in general: (<b>a</b> × <b>b</b>) × <b>c</b> ≠ <b>a</b> × (<b>b</b> × <b>c</b>).",
        ]),
        ("p", "These rules let you simplify expressions without components. For example (<b>a</b> + <b>b</b>) × (<b>a</b> − <b>b</b>) = "
              "<b>a</b> × <b>a</b> − <b>a</b> × <b>b</b> + <b>b</b> × <b>a</b> − <b>b</b> × <b>b</b> = 0 + <b>b</b> × <b>a</b> + <b>b</b> × <b>a</b> − 0 = "
              "2(<b>b</b> × <b>a</b>)."),

        ("h2", "10.4 Perpendicular vectors, normals and sin θ (Ed AS FP1 3.1, OCR 4.04g)"),
        ("bullets", [
            "A vector perpendicular to both <b>b</b> and <b>c</b> is <b>b</b> × <b>c</b>. Any non-zero multiple will do, so cancel common factors.",
            "Normal to the plane <b>r</b> = <b>a</b> + λ<b>b</b> + μ<b>c</b>: <b>n</b> = <b>b</b> × <b>c</b>. Normal to the plane through A, B, C: "
            "<b>n</b> = AB→ × AC→. Then the Cartesian equation is <b>r</b>·<b>n</b> = <b>a</b>·<b>n</b>.",
            "Direction of the line where two planes meet: <b>n₁</b> × <b>n₂</b> (used in Unit A12).",
            "sin θ = |<b>a</b> × <b>b</b>| / (|<b>a</b>||<b>b</b>|) gives only sin θ, which cannot tell an acute angle from an obtuse one. "
            "To find an angle, use the scalar product.",
        ]),

        ("h2", "10.5 Areas of triangles and parallelograms (Ed AS FP1 3.2, OCR 8.04c, AQA F5)"),
        ("box", "Areas", [
            "Parallelogram with adjacent sides <b>a</b>, <b>b</b>: area = |<b>a</b> × <b>b</b>|.",
            "Triangle ABC: area = ½|AB→ × AC→|. Any two sides from one vertex will do.",
            "This is the vector form of area = ½ab sin C.",
        ]),

        ("h2", "10.6 The line (r − a) × b = 0; direction ratios and direction cosines (Ed FP1 5.3, IAL 5.2, AQA F5, OCR 8.04d)"),
        ("p", "R lies on the line through A with direction <b>b</b> exactly when AR→ = <b>r</b> − <b>a</b> is parallel to <b>b</b>, that is when "
              "(<b>r</b> − <b>a</b>) × <b>b</b> = <b>0</b>. Expanding gives the equivalent form <b>r</b> × <b>b</b> = <b>a</b> × <b>b</b>."),
        ("p", "To convert <b>r</b> × <b>b</b> = <b>c</b> back to the form <b>r</b> = <b>a</b> + λ<b>b</b>, put <b>r</b> = (x, y, z)ᵀ, expand <b>r</b> × <b>b</b>, "
              "equate components with <b>c</b>, choose a convenient value of one coordinate (say z = 0) and solve for the other two. "
              "Only two of the three equations are independent. A solution exists only when <b>b</b>·<b>c</b> = 0."),
        ("box", "Direction ratios and cosines", [
            "If a line has direction <b>b</b> = (b₁, b₂, b₃)ᵀ, the numbers b₁ : b₂ : b₃ are its <b>direction ratios</b>.",
            "The <b>direction cosines</b> are l = b₁/|<b>b</b>|, m = b₂/|<b>b</b>|, n = b₃/|<b>b</b>|: the components of the unit vector <b>b̂</b>.",
            "They are the cosines of the angles α, β, γ that the line makes with the x-, y- and z-axes: l = cos α, m = cos β, n = cos γ.",
            "l² + m² + n² = 1, that is cos²α + cos²β + cos²γ = 1.",
        ]),

        ("h2", "10.7 The scalar triple product and volumes (Ed FP1 5.2, AS FP1 3.3, IAL 5.1, OCR 8.04e)"),
        ("p", "The <b>scalar triple product</b> of <b>a</b>, <b>b</b>, <b>c</b> is the number <b>a</b>·(<b>b</b> × <b>c</b>). Writing it out in "
              "components shows that it equals a 3 × 3 determinant."),
        ("box", "Scalar triple product", [
            "<b>a</b>·(<b>b</b> × <b>c</b>) = | a₁ a₂ a₃ ; b₁ b₂ b₃ ; c₁ c₂ c₃ |.",
            "Cyclic order leaves it unchanged: <b>a</b>·(<b>b</b> × <b>c</b>) = <b>b</b>·(<b>c</b> × <b>a</b>) = <b>c</b>·(<b>a</b> × <b>b</b>); swapping two "
            "vectors changes its sign.",
            "Volume of the <b>parallelepiped</b> with edges <b>a</b>, <b>b</b>, <b>c</b>: V = |<b>a</b>·(<b>b</b> × <b>c</b>)|.",
            "Volume of the <b>tetrahedron</b> ABCD: V = ⅙|AB→·(AC→ × AD→)|.",
            "<b>a</b>·(<b>b</b> × <b>c</b>) = 0 ⇔ <b>a</b>, <b>b</b>, <b>c</b> are coplanar (the parallelepiped is flat). So four points A, B, C, D "
            "are coplanar exactly when AB→·(AC→ × AD→) = 0.",
        ]),
        ("figure", "pa10_volumes.png", "The parallelepiped has volume |a·(b × c)|; a tetrahedron on three of its edges has one sixth of it.", 140),
        ("p", "<b>Why it works.</b> |<b>b</b> × <b>c</b>| is the area of the base parallelogram and <b>b</b> × <b>c</b> is perpendicular to the base. "
              "The height is the component of <b>a</b> along this normal, |<b>a</b>| |cos φ|, where φ is the angle between <b>a</b> and "
              "<b>b</b> × <b>c</b>. So volume = base × height = |<b>b</b> × <b>c</b>||<b>a</b>||cos φ| = |<b>a</b>·(<b>b</b> × <b>c</b>)|. A tetrahedron is a "
              "pyramid: ⅓ × base triangle × height, and the base triangle is half the parallelogram, giving ⅓ × ½ = ⅙."),
        ("warn", "Common mistakes", [
            "Losing the minus sign in the middle (<b>j</b>) component of the determinant: (a₃b₁ − a₁b₃), not (a₁b₃ − a₃b₁).",
            "Writing <b>a</b> × <b>b</b> = <b>b</b> × <b>a</b>. The vector product is anti-commutative.",
            "Forgetting the ½ for a triangle or the ⅙ for a tetrahedron; leaving a negative volume (take the modulus).",
            "Using |<b>a</b> × <b>b</b>| to find an angle that may be obtuse: sin θ has two solutions between 0° and 180°.",
            "Using position vectors OA, OB, OC instead of edge vectors AB→, AC→ when the triangle or tetrahedron does not have a vertex at O.",
            "Not checking the answer: a correct <b>a</b> × <b>b</b> always has zero scalar product with <b>a</b> and with <b>b</b>.",
        ]),
    ],

    "examples": [
        {
            "title": "Computing a vector product",
            "question": "Given <b>a</b> = 2<b>i</b> − <b>j</b> + 3<b>k</b> and <b>b</b> = <b>i</b> + 4<b>j</b> − 2<b>k</b>, find <b>a</b> × <b>b</b> and <b>b</b> × <b>a</b>, and verify "
                        "that <b>a</b> × <b>b</b> is perpendicular to <b>a</b> and to <b>b</b>.",
            "steps": [
                "<b>i</b>: a₂b₃ − a₃b₂ = (−1)(−2) − (3)(4) = 2 − 12 = −10.",
                "<b>j</b>: a₃b₁ − a₁b₃ = (3)(1) − (2)(−2) = 3 + 4 = 7.",
                "<b>k</b>: a₁b₂ − a₂b₁ = (2)(4) − (−1)(1) = 8 + 1 = 9.",
                "So <b>a</b> × <b>b</b> = −10<b>i</b> + 7<b>j</b> + 9<b>k</b>, and <b>b</b> × <b>a</b> = 10<b>i</b> − 7<b>j</b> − 9<b>k</b>.",
                "Check: (−10, 7, 9)·(2, −1, 3) = −20 − 7 + 27 = 0 and (−10, 7, 9)·(1, 4, −2) = −10 + 28 − 18 = 0.",
            ],
        },
        {
            "title": "Area of a triangle, and why sin θ is not enough",
            "question": "A(1, 0, 2), B(3, 1, 1) and C(0, 2, 4). Find the area of triangle ABC and the angle BAC.",
            "steps": [
                "AB→ = (2, 1, −1)ᵀ, AC→ = (−1, 2, 2)ᵀ. AB→ × AC→ = (1·2 − (−1)·2, (−1)(−1) − 2·2, 2·2 − 1·(−1))ᵀ = (4, −3, 5)ᵀ.",
                "|AB→ × AC→| = √(16 + 9 + 25) = √50 = 5√2. Area = ½ × 5√2 = 5√2/2 ≈ 3.54 square units.",
                "From the vector product, sin A = 5√2/(√6 × 3) = 0.962, which gives A = 74.2° <b>or</b> 105.8°.",
                "The scalar product decides: AB→·AC→ = −2 + 2 − 2 = −2 < 0, so angle A is obtuse. cos A = −2/(3√6) gives A = 105.8° (1 d.p.).",
                "(Compare Worked example A9.4: (4, −3, 5)ᵀ is also the normal to the plane ABC.)",
            ],
        },
        {
            "title": "Plane through three points using the vector product",
            "question": "Find a Cartesian equation of the plane through P(1, 2, −1), Q(2, 0, 1) and R(−1, 1, 3).",
            "steps": [
                "PQ→ = (1, −2, 2)ᵀ, PR→ = (−2, −1, 4)ᵀ.",
                "PQ→ × PR→ = ((−2)(4) − (2)(−1), (2)(−2) − (1)(4), (1)(−1) − (−2)(−2))ᵀ = (−6, −8, −5)ᵀ.",
                "Take <b>n</b> = (6, 8, 5)ᵀ. Then <b>p</b>·<b>n</b> = 6 + 16 − 5 = 17, so the plane is 6x + 8y + 5z = 17.",
                "Check: Q gives 12 + 0 + 5 = 17 and R gives −6 + 8 + 15 = 17.",
            ],
        },
        {
            "title": "The form (r − a) × b = 0 and direction cosines",
            "question": "The line l passes through (1, 2, 3) and has direction 2<b>i</b> − <b>j</b> + <b>k</b>. (a) Write l in the form "
                        "<b>r</b> × <b>b</b> = <b>c</b>. (b) Starting from your answer, find a point of l with z = 0. (c) Find the direction cosines "
                        "of l and the angle it makes with the x-axis.",
            "steps": [
                "(a) <b>a</b> × <b>b</b> = (1, 2, 3)ᵀ × (2, −1, 1)ᵀ = (2·1 − 3·(−1), 3·2 − 1·1, 1·(−1) − 2·2)ᵀ = (5, 5, −5)ᵀ. "
                "So l: <b>r</b> × (2<b>i</b> − <b>j</b> + <b>k</b>) = 5<b>i</b> + 5<b>j</b> − 5<b>k</b>.",
                "(b) With <b>r</b> = (x, y, z)ᵀ: <b>r</b> × <b>b</b> = (y + z, 2z − x, −x − 2y)ᵀ. Equate to (5, 5, −5)ᵀ with z = 0: y = 5, x = −5, "
                "and the third equation 5 − 10 = −5 is satisfied. The point is (−5, 5, 0).",
                "Check: (−5, 5, 0) = (1, 2, 3) − 3(2, −1, 1), so it is on l.",
                "(c) |<b>b</b>| = √6. Direction cosines 2/√6, −1/√6, 1/√6 (sum of squares 4/6 + 1/6 + 1/6 = 1).",
                "Angle with the x-axis: cos α = 2/√6, α = 35.3° (1 d.p.).",
            ],
        },
        {
            "title": "Volumes of a parallelepiped and a tetrahedron",
            "question": "A(1, 1, 0), B(3, 2, 1), C(0, 3, 2), D(2, 0, 4). Find the volume of the tetrahedron ABCD and of the "
                        "parallelepiped with edges AB→, AC→, AD→.",
            "steps": [
                "AB→ = (2, 1, 1)ᵀ, AC→ = (−1, 2, 2)ᵀ, AD→ = (1, −1, 4)ᵀ.",
                "AB→·(AC→ × AD→) = | 2 1 1 ; −1 2 2 ; 1 −1 4 | = 2(8 + 2) − 1(−4 − 2) + 1(1 − 2) = 20 + 6 − 1 = 25.",
                "Parallelepiped: V = |25| = 25 cubic units.",
                "Tetrahedron: V = 25/6 ≈ 4.17 cubic units.",
            ],
        },
        {
            "title": "Area and volume with an unknown (exam standard)",
            "question": "A(2, 1, 0), B(4, 3, 1), C(1, 5, 3) and D(k, 2, 1). (a) Find AB→ × AC→. (b) Find the area of triangle ABC. "
                        "(c) The tetrahedron ABCD has volume 3/2. Find the possible values of k.",
            "steps": [
                "(a) AB→ = (2, 2, 1)ᵀ, AC→ = (−1, 4, 3)ᵀ. AB→ × AC→ = (2·3 − 1·4, 1·(−1) − 2·3, 2·4 − 2·(−1))ᵀ = (2, −7, 10)ᵀ.",
                "(b) |(2, −7, 10)ᵀ| = √(4 + 49 + 100) = √153 = 3√17. Area = 3√17/2 ≈ 6.18.",
                "(c) AD→ = (k − 2, 1, 1)ᵀ. AD→·(AB→ × AC→) = 2(k − 2) − 7 + 10 = 2k − 1.",
                "V = ⅙|2k − 1| = 3/2, so |2k − 1| = 9: 2k − 1 = 9 or 2k − 1 = −9.",
                "k = 5 or k = −4. (Both are valid: the modulus allows D on either side of the plane ABC.)",
            ],
        },
    ],

    "practice": [
        "Find (3<b>i</b> + <b>j</b> − 2<b>k</b>) × (<b>i</b> − <b>j</b> + 4<b>k</b>).",
        "Using only <b>i</b> × <b>j</b> = <b>k</b> and the rules of the vector product, simplify (<b>i</b> + 2<b>j</b>) × (3<b>i</b> − <b>k</b>). Check your "
        "answer with the component formula.",
        "Prove that (<b>a</b> + <b>b</b>) × (<b>a</b> − <b>b</b>) = 2(<b>b</b> × <b>a</b>).",
        "Find a unit vector perpendicular to both <b>i</b> + 2<b>j</b> + 2<b>k</b> and 2<b>i</b> − 2<b>j</b> + <b>k</b>.",
        "Find the area of the parallelogram with adjacent sides 2<b>i</b> + <b>k</b> and <b>i</b> + 3<b>j</b> − <b>k</b>, to 3 s.f.",
        "Find the exact area of the triangle with vertices P(1, 1, 1), Q(2, 3, 0) and R(4, 0, 2).",
        "Use a vector product to find a Cartesian equation of the plane through (1, 0, 1), (2, 1, 3) and (0, 2, 2).",
        "Write the line (x − 2)/3 = (y + 1)/1 = z/(−2) in the form <b>r</b> × <b>b</b> = <b>c</b>.",
        "Find the direction cosines of the line <b>r</b> = (1, 0, 5)ᵀ + t(2, −3, 6)ᵀ, and the angle it makes with the z-axis to 0.1°.",
        "Find the volume of the parallelepiped with edges <b>i</b> + 2<b>j</b>, <b>j</b> + 3<b>k</b> and 2<b>i</b> + <b>k</b>.",
        "Find k for which the vectors (1, 2, 3)ᵀ, (2, −1, 1)ᵀ and (k, 1, 4)ᵀ are coplanar.",
        "Given <b>a</b> = (2, −4, 6)ᵀ and <b>b</b> = (−3, p, q)ᵀ with <b>a</b> × <b>b</b> = <b>0</b>, find p and q.",
    ],
    "answers": [
        "(1·4 − (−2)(−1), (−2)(1) − 3·4, 3(−1) − 1·1)ᵀ = 2<b>i</b> − 14<b>j</b> − 4<b>k</b>.",
        "3(<b>i</b> × <b>i</b>) − <b>i</b> × <b>k</b> + 6(<b>j</b> × <b>i</b>) − 2(<b>j</b> × <b>k</b>) = 0 + <b>j</b> − 6<b>k</b> − 2<b>i</b> = −2<b>i</b> + <b>j</b> − 6<b>k</b>; "
        "the formula gives (−2, 1, −6)ᵀ.",
        "Expand: <b>a</b> × <b>a</b> − <b>a</b> × <b>b</b> + <b>b</b> × <b>a</b> − <b>b</b> × <b>b</b> = 0 + <b>b</b> × <b>a</b> + <b>b</b> × <b>a</b> − 0 = 2(<b>b</b> × <b>a</b>), "
        "using <b>a</b> × <b>a</b> = 0 and −<b>a</b> × <b>b</b> = <b>b</b> × <b>a</b>.",
        "Cross product (6, 3, −6)ᵀ, magnitude 9; ±(2/3, 1/3, −2/3)ᵀ.",
        "(−3, 3, 6)ᵀ, area √54 = 3√6 ≈ 7.35.",
        "PQ→ × PR→ = (1, −4, −7)ᵀ; area ½√66 ≈ 4.06.",
        "(1, 1, 2)ᵀ × (−1, 2, 1)ᵀ = (−3, −3, 3)ᵀ, so <b>n</b> = (1, 1, −1)ᵀ; x + y − z = 0.",
        "<b>a</b> = (2, −1, 0)ᵀ, <b>b</b> = (3, 1, −2)ᵀ, <b>a</b> × <b>b</b> = (2, 4, 5)ᵀ: <b>r</b> × (3<b>i</b> + <b>j</b> − 2<b>k</b>) = 2<b>i</b> + 4<b>j</b> + 5<b>k</b>.",
        "|<b>b</b>| = 7: 2/7, −3/7, 6/7. cos γ = 6/7, γ = 31.0°.",
        "| 1 2 0 ; 0 1 3 ; 2 0 1 | = 1(1) − 2(0 − 6) + 0 = 13.",
        "| 1 2 3 ; 2 −1 1 ; k 1 4 | = 5k − 15 = 0, k = 3 (indeed (3, 1, 4)ᵀ is the sum of the other two).",
        "<b>b</b> must be parallel to <b>a</b>: <b>b</b> = −(3/2)<b>a</b>, so p = 6, q = −9.",
    ],

    "exam": [
        "The points A, B, C and D have coordinates (1, 2, 1), (3, 3, −1), (2, 5, 2) and (4, 1, 6).\n"
        "(a) Find AB→ × AC→. [3]\n"
        "(b) Hence find a Cartesian equation of the plane ABC. [2]\n"
        "(c) Find the exact area of triangle ABC. [2]\n"
        "(d) Find the volume of the tetrahedron ABCD. [3]",
        "The line l has equation (<b>r</b> − (3<b>i</b> − <b>j</b> + 2<b>k</b>)) × (<b>i</b> + 2<b>j</b> − 2<b>k</b>) = <b>0</b>, and the plane Π has equation "
        "<b>r</b>·(2<b>i</b> − <b>j</b> + <b>k</b>) = 5.\n"
        "(a) Write down a vector equation of l in the form <b>r</b> = <b>a</b> + λ<b>b</b>. [1]\n"
        "(b) Find the direction cosines of l, and the acute angle between l and the x-axis to 0.1°. [3]\n"
        "(c) Find the coordinates of the point P where l meets Π. [3]\n"
        "(d) Find a vector equation of the line through P which lies in Π and is perpendicular to l. [4]",
        "Relative to an origin O, the points A, B and C have position vectors <b>a</b> = <b>i</b> + <b>j</b>, <b>b</b> = <b>j</b> + <b>k</b> and "
        "<b>c</b> = <b>i</b> + t<b>k</b>, where t is a constant.\n"
        "(a) Find <b>b</b> × <b>c</b> in terms of t. [2]\n"
        "(b) Find, in terms of t, the volume of the parallelepiped with edges OA, OB and OC. [2]\n"
        "(c) State the value of t for which O, A, B and C are coplanar. [1]\n"
        "(d) The tetrahedron OABC has volume 1. Find the possible values of t. [3]\n"
        "(e) For the positive value of t found in (d), find the exact area of the triangle OBC. [2]",
    ],
    "exam_answers": [
        "(a) AB→ = (2, 1, −2)ᵀ, AC→ = (1, 3, 1)ᵀ M1; AB→ × AC→ = (7, −4, 5)ᵀ. M1 A1\n"
        "(b) (1, 2, 1)·(7, −4, 5) = 4 M1; 7x − 4y + 5z = 4. A1\n"
        "(c) |(7, −4, 5)ᵀ| = √90 = 3√10 M1; area = 3√10/2. A1\n"
        "(d) AD→ = (3, −1, 5)ᵀ; AD→·(7, −4, 5)ᵀ = 21 + 4 + 25 = 50 M1 A1; V = 50/6 = 25/3. A1",
        "(a) <b>r</b> = (3, −1, 2)ᵀ + λ(1, 2, −2)ᵀ. B1\n"
        "(b) |<b>b</b>| = 3 M1: 1/3, 2/3, −2/3 A1; cos α = 1/3, α = 70.5°. A1\n"
        "(c) 2(3 + λ) − (−1 + 2λ) + (2 − 2λ) = 5 M1, so 9 − 2λ = 5, λ = 2 A1; P(5, 3, −2). A1\n"
        "(d) Direction perpendicular to <b>b</b> and to <b>n</b>: <b>b</b> × <b>n</b> M1 = (1, 2, −2)ᵀ × (2, −1, 1)ᵀ = (0, −5, −5)ᵀ A1, so use (0, 1, 1)ᵀ. "
        "<b>r</b> = (5, 3, −2)ᵀ + μ(0, 1, 1)ᵀ. M1 A1",
        "(a) <b>b</b> × <b>c</b> = (0, 1, 1)ᵀ × (1, 0, t)ᵀ = (t, 1, −1)ᵀ. M1 A1\n"
        "(b) <b>a</b>·(<b>b</b> × <b>c</b>) = t + 1 M1; volume |t + 1|. A1\n"
        "(c) t = −1. B1\n"
        "(d) |t + 1|/6 = 1 M1; t + 1 = ±6 M1; t = 5 or t = −7. A1\n"
        "(e) t = 5: |<b>b</b> × <b>c</b>| = √(25 + 1 + 1) = 3√3 M1; area = 3√3/2. A1",
    ],
}
