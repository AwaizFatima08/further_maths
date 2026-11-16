UNIT = {
    "number": "A5",
    "title": "Matrices and linear transformations",
    "tag": "AS · Edexcel CP 3.1–3.3 · IAL FP1 5.1–5.3, 6.1–6.3 (2-D); FP3 6.1–6.2 (3-D) · AQA C1–C3 (AS) · "
           "OCR A 4.03a–f (AS) · OCR MEI Pm1–Pm5 (AS) · CAIE 9231 P1 1.4 (2-D only)",
    "notes": [
        ("h2", "5.1 Matrix language and notation"),
        ("p", "A <b>matrix</b> is a rectangular array of numbers, called <b>entries</b> or <b>elements</b>. A matrix with m rows and "
              "n columns has <b>order</b> (or size) m × n, read “m by n”. A <b>square</b> matrix has as many rows as columns. Entries "
              "may be real or complex (OCR A 4.03a). We use capital letters for matrices and write aᵢⱼ for the entry in row i, "
              "column j."),
        ("box", "Notation used in this book", [
            "Matrices are written row by row, with rows separated by semicolons: M = (2 1; 0 3) has first row 2, 1 and second "
            "row 0, 3. A 3 × 3 matrix is written (a b c; d e f; g h i).",
            "A column vector is written (x, y)ᵀ or (x, y, z)ᵀ. The superscript ᵀ (transpose) turns a row into a column; "
            "transposes are studied in Unit A6.",
            "Two matrices are <b>equal</b> when they have the same order and every pair of corresponding entries is equal.",
            "The <b>zero</b> (null) matrix 0 has every entry 0. The <b>identity</b> matrix I (or Iₙ) is square with 1s on the "
            "leading diagonal and 0s elsewhere: I₂ = (1 0; 0 1), I₃ = (1 0 0; 0 1 0; 0 0 1).",
        ]),
        ("h2", "5.2 Adding, subtracting and multiplying by a scalar"),
        ("p", "Matrices of the <b>same order</b> are <b>conformable for addition</b>: add or subtract corresponding entries. To multiply a "
              "matrix by a scalar k, multiply every entry by k. For example, if A = (3 −2; 1 4) and B = (0 5; −1 2) then "
              "A + B = (3 3; 0 6) and 2A − B = (6 −9; 3 6). Matrices of different orders cannot be added."),
        ("p", "These operations behave like ordinary algebra: A + B = B + A, (A + B) + C = A + (B + C), A + 0 = A and "
              "k(A + B) = kA + kB."),
        ("h2", "5.3 Matrix multiplication"),
        ("p", "The product AB is defined only when the number of <b>columns of A</b> equals the number of <b>rows of B</b>; A and B are then "
              "<b>conformable for multiplication</b>. If A is m × n and B is n × p then AB is m × p. The entry in row i, column j of AB "
              "is found by running along row i of A and down column j of B, multiplying pairs and adding."),
        ("box", "Matrix products", [
            "(m × n)(n × p) = (m × p): the inner numbers must match; the outer numbers give the order of the product.",
            "(a b; c d)(e f; g h) = (ae + bg\u00a0\u00a0af + bh; ce + dg\u00a0\u00a0cf + dh).",
            "(a b; c d)(x, y)ᵀ = (ax + by, cx + dy)ᵀ.",
            "Powers of a square matrix: A² = AA, A³ = AAA, and so on for positive integers n (OCR A 4.03b).",
            "Associative: (AB)C = A(BC). Distributive: A(B + C) = AB + AC. Identity: AI = IA = A.",
            "<b>Not commutative:</b> in general AB ≠ BA, and BA may not even exist.",
        ]),
        ("p", "Non-commutativity is the single biggest difference from ordinary algebra. With A = (1 2; 0 1) and B = (1 0; 3 1), "
              "AB = (7 2; 3 1) but BA = (1 2; 3 7). So you must keep the order of factors: (A + B)² = A² + AB + BA + B², "
              "which is not A² + 2AB + B² unless AB = BA. Associativity (OCR A 4.03c, MEI Pm3) is what lets us write ABC without "
              "brackets and is the reason composite transformations work (Section 5.6)."),
        ("p", "Calculators: AQA, OCR A, OCR MEI and Edexcel allow matrix calculations on the calculator, so numerical products may "
              "be done on it (OCR A 4.03b, MEI Pm1). You must still be able to multiply by hand, especially when entries are "
              "algebraic. Cambridge Paper 1 expects products of matrices up to 3 × 3, including non-square ones."),
        ("h2", "5.4 Linear transformations and their matrices"),
        ("p", "A <b>transformation</b> T of the plane maps each point (position vector) to an image point. T is <b>linear</b> when "
              "T(λu + μv) = λT(u) + μT(v) for all vectors u, v and scalars λ, μ. Every 2 × 2 matrix M gives a linear transformation "
              "x ↦ Mx, because M(λu + μv) = λMu + μMv. A linear transformation always maps the origin to itself, maps straight lines "
              "to straight lines (or to a point) and keeps parallel lines parallel."),
        ("p", "Write i = (1, 0)ᵀ and j = (0, 1)ᵀ. Then M i is the first column of M and M j is the second column. Since every vector "
              "is (x, y)ᵀ = x i + y j, its image is x(M i) + y(M j): the images of i and j determine the whole transformation."),
        ("box", "Finding the matrix of a linear transformation", [
            "The first column of M is the image of i = (1, 0)ᵀ; the second column is the image of j = (0, 1)ᵀ.",
            "In 3-D the three columns are the images of i, j and k.",
            "The <b>unit square</b> with vertices O(0, 0), (1, 0), (1, 1), (0, 1) maps to the parallelogram with vertices "
            "O, (a, c), (a + b, c + d), (b, d) under (a b; c d). Sketching it is the quickest way to identify a matrix.",
        ]),
        ("h2", "5.5 Standard transformations in two dimensions"),
        ("p", "Each matrix below comes from drawing the images of i and j. Angles are measured anticlockwise; a clockwise rotation "
              "through θ is a rotation through −θ. All the boards list reflections, rotations about O, enlargements centre O and "
              "stretches. Shears are on OCR A (4.03d), OCR MEI (Pm4) and Cambridge (1.4), but not on Edexcel CP or AQA."),
        ("table", ["Transformation", "Matrix", "How to see it"], [
            ["Reflection in the x-axis", "(1 0; 0 −1)", "i fixed, j ↦ −j"],
            ["Reflection in the y-axis", "(−1 0; 0 1)", "i ↦ −i, j fixed"],
            ["Reflection in y = x", "(0 1; 1 0)", "i and j swap"],
            ["Reflection in y = −x", "(0 −1; −1 0)", "i ↦ −j, j ↦ −i"],
            ["Reflection in y = (tan θ)x", "(cos 2θ\u00a0\u00a0sin 2θ; sin 2θ\u00a0\u00a0−cos 2θ)", "i ↦ at angle 2θ to the x-axis"],
            ["Rotation θ anticlockwise about O", "(cos θ\u00a0\u00a0−sin θ; sin θ\u00a0\u00a0cos θ)", "i ↦ (cos θ, sin θ)ᵀ"],
            ["Enlargement, centre O, scale factor k", "(k 0; 0 k)", "every vector multiplied by k"],
            ["Stretch parallel to the x-axis, factor k", "(k 0; 0 1)", "the y-axis is fixed"],
            ["Stretch parallel to the y-axis, factor k", "(1 0; 0 k)", "the x-axis is fixed"],
            ["Shear, x-axis fixed: (x, y) ↦ (x + ky, y)", "(1 k; 0 1)", "j ↦ (k, 1)ᵀ; points move parallel to the x-axis"],
            ["Shear, y-axis fixed: (x, y) ↦ (x, kx + y)", "(1 0; k 1)", "i ↦ (1, k)ᵀ; points move parallel to the y-axis"],
        ]),
        ("figure", "pa05_square.png", "The unit square (dashed) and its image (shaded): (a) reflection in y = x, (0 1; 1 0); "
                   "(b) rotation through 60°, (1/2 −√3/2; √3/2 1/2); (c) stretch parallel to the x-axis, factor 3, (3 0; 0 1); "
                   "(d) shear with the x-axis fixed, (1 2; 0 1). The arrows Mi and Mj are the columns of each matrix.", 140),
        ("p", "A <b>shear</b> keeps one line of points fixed (the <b>invariant line</b> of the shear, here an axis) and moves every other "
              "point parallel to that line by a distance proportional to its distance from the line. To describe a shear fully, "
              "state the fixed line and the image of one point not on it, for example “shear with the x-axis fixed, mapping (0, 1) "
              "to (2, 1)”. A shear does not change area."),
        ("p", "An enlargement with negative k, such as (−2 0; 0 −2), is an enlargement with scale factor −2: equivalently a "
              "rotation through 180° followed by an enlargement with scale factor 2. The matrix (−1 0; 0 −1) is the rotation through "
              "180° about O (also the enlargement with scale factor −1)."),
        ("h2", "5.6 Successive transformations: AB means B first, then A"),
        ("p", "If B is applied first and then A, a point x goes to Bx and then to A(Bx). By associativity A(Bx) = (AB)x, so the single "
              "matrix for “B followed by A” is the product AB. The matrix applied first is written on the <b>right</b>, next to the "
              "vector. For three transformations, “C, then B, then A” is ABC."),
        ("box", "Composite transformations", [
            "B followed by A is represented by AB (Edexcel 3.3, IAL 6.1, OCR A 4.03e, CAIE 1.4).",
            "Rotations about O combine by adding angles: R(α)R(β) = R(α + β). Hence R(θ)ⁿ = R(nθ).",
            "Two reflections in lines through O make a rotation about O through twice the angle between the lines: "
            "reflection in y = (tan β)x followed by reflection in y = (tan α)x is the rotation through 2(α − β).",
            "Order matters: reflection in y = x then rotation 90° is not the same as rotation 90° then reflection in y = x.",
        ]),
        ("h2", "5.7 Transformations in three dimensions"),
        ("p", "In 3-D a 3 × 3 matrix acts on (x, y, z)ᵀ, and its columns are the images of i, j and k. The boards examine "
              "reflections in the planes x = 0, y = 0 and z = 0 and rotations about the coordinate axes (Edexcel 3.3, AQA C3, OCR A "
              "4.03f, MEI Pm4 with angles that are multiples of 90°; IAL FP3 6.1 asks for 3-D linear maps more generally). "
              "Cambridge 9231 does not examine 3-D transformations."),
        ("table", ["Transformation in 3-D", "Matrix"], [
            ["Reflection in the plane x = 0 (the y–z plane)", "(−1 0 0; 0 1 0; 0 0 1)"],
            ["Reflection in the plane y = 0 (the x–z plane)", "(1 0 0; 0 −1 0; 0 0 1)"],
            ["Reflection in the plane z = 0 (the x–y plane)", "(1 0 0; 0 1 0; 0 0 −1)"],
            ["Rotation θ about the x-axis", "(1 0 0; 0 cos θ\u00a0\u00a0−sin θ; 0 sin θ\u00a0\u00a0cos θ)"],
            ["Rotation θ about the y-axis", "(cos θ\u00a0\u00a00\u00a0\u00a0sin θ; 0 1 0; −sin θ\u00a0\u00a00\u00a0\u00a0cos θ)"],
            ["Rotation θ about the z-axis", "(cos θ\u00a0\u00a0−sin θ\u00a0\u00a00; sin θ\u00a0\u00a0cos θ\u00a0\u00a00; 0 0 1)"],
        ]),
        ("p", "The rotations are in the positive (right-handed) sense: anticlockwise when you look from the positive end of the axis "
              "towards the origin. Note the position of the minus sign in the y-axis matrix: a positive rotation about the y-axis "
              "takes k towards i, so k ↦ (sin θ, 0, cos θ)ᵀ. If unsure, check the image of one unit vector with a quick sketch."),
        ("h2", "5.8 Given or learn?"),
        ("bullets", [
            "Edexcel and AQA formula booklets print the 2-D rotation and reflection matrices and the 3-D axis rotations. "
            "Cambridge, OCR A and OCR MEI students should be able to write them down by finding the images of i, j (and k).",
            "Every board expects you to know that AB means B followed by A, and to multiply matrices by hand.",
        ]),
        ("warn", "Common mistakes", [
            "Writing the composite matrix the wrong way round. “P then Q” is QP: the first transformation is next to the vector.",
            "Assuming AB = BA or expanding (A + B)² as A² + 2AB + B².",
            "Trying to multiply non-conformable matrices, or giving the wrong order: a (2 × 3)(3 × 1) product is 2 × 1.",
            "Mixing up the reflections in y = x and y = −x, or a 90° clockwise rotation (0 1; −1 0) with an anticlockwise one "
            "(0 −1; 1 0). Check with the image of (1, 0).",
            "Incomplete descriptions. A rotation needs centre, angle and sense; a reflection needs the mirror line; a stretch needs "
            "the direction (or fixed axis) and the factor; a shear needs the fixed line and the image of a point.",
            "In 3-D, putting the minus sign in the wrong place in the y-axis rotation matrix.",
        ]),
    ],
    "examples": [
        {
            "title": "Products and their orders",
            "question": "A = (2 −1; 3 0), B = (1 4; −2 1), C = (1 0 2; −1 3 1) and D = (2 1; 0 −1; 1 3). "
                        "(a) Find AB and BA. (b) State the orders of CD and DC and find CD. (c) Explain why AC exists but CA does not.",
            "steps": [
                "(a) AB = (2×1 + (−1)(−2)\u00a0\u00a02×4 + (−1)×1; 3×1 + 0×(−2)\u00a0\u00a03×4 + 0×1) = (4 7; 3 12).",
                "BA = (1×2 + 4×3\u00a0\u00a01×(−1) + 4×0; −2×2 + 1×3\u00a0\u00a0(−2)(−1) + 1×0) = (14 −1; −1 2). So AB ≠ BA.",
                "(b) C is 2 × 3 and D is 3 × 2, so CD is 2 × 2 and DC is 3 × 3.",
                "CD = (1×2 + 0×0 + 2×1\u00a0\u00a01×1 + 0×(−1) + 2×3; −1×2 + 3×0 + 1×1\u00a0\u00a0−1×1 + 3×(−1) + 1×3) = (4 7; −1 −1).",
                "(c) A is 2 × 2 and C is 2 × 3: the inner numbers match (2 and 2), so AC exists and is 2 × 3. "
                "For CA the inner numbers are 3 and 2, which do not match, so CA is not defined.",
            ],
        },
        {
            "title": "Identifying transformations from the unit square",
            "question": "Describe fully the transformation represented by each matrix. "
                        "(a) P = (0 1; 1 0) (b) Q = (3 0; 0 1) (c) R = (1 2; 0 1) (d) S = (1/2\u00a0\u00a0−√3/2; √3/2\u00a0\u00a01/2).",
            "steps": [
                "Find the images of i and j: they are the columns.",
                "(a) i ↦ (0, 1)ᵀ = j and j ↦ i. The unit vectors swap, so P is a reflection in the line y = x.",
                "(b) i ↦ 3i and j is unchanged: a stretch parallel to the x-axis, scale factor 3 (the y-axis is fixed).",
                "(c) i is unchanged and j ↦ (2, 1)ᵀ. Each point (x, y) goes to (x + 2y, y): a shear with the x-axis fixed, "
                "mapping (0, 1) to (2, 1). (Shear: OCR A, MEI, CAIE.)",
                "(d) Compare with (cos θ\u00a0\u00a0−sin θ; sin θ\u00a0\u00a0cos θ): cos θ = 1/2 and sin θ = √3/2, so θ = 60°. S is a rotation "
                "through 60° anticlockwise about the origin.",
            ],
            "figure": "pa05_shear.png",
            "caption": "The shear R = (1 2; 0 1): the unit square becomes a parallelogram with the same base and height.",
            "width_mm": 85,
        },
        {
            "title": "Combining transformations",
            "question": "M represents a reflection in the line y = x and R represents a rotation through 90° anticlockwise about O. "
                        "(a) Find the matrix for M followed by R and describe this single transformation. "
                        "(b) Find the matrix for R followed by M. (c) Comment on your answers.",
            "steps": [
                "M = (0 1; 1 0) and R = (0 −1; 1 0).",
                "(a) M first, then R, is RM = (0 −1; 1 0)(0 1; 1 0) = (0×0 + (−1)×1\u00a0\u00a00×1 + (−1)×0; 1×0 + 0×1\u00a0\u00a01×1 + 0×0) = (−1 0; 0 1).",
                "i ↦ −i and j is unchanged, so RM is a reflection in the y-axis.",
                "(b) R first, then M, is MR = (0 1; 1 0)(0 −1; 1 0) = (1 0; 0 −1), a reflection in the x-axis.",
                "(c) RM ≠ MR: the order of the transformations matters. Both answers are reflections, as expected, because a "
                "reflection reverses orientation and a rotation does not.",
            ],
        },
        {
            "title": "Powers of a rotation matrix",
            "question": "S = (1/2\u00a0\u00a0−√3/2; √3/2\u00a0\u00a01/2). (a) Find S² and S³. (b) Find the smallest positive integer n for which Sⁿ = I, "
                        "and explain your answer geometrically. (c) Write down S¹⁰⁰.",
            "steps": [
                "(a) S² = (1/4 − 3/4\u00a0\u00a0−√3/4 − √3/4; √3/4 + √3/4\u00a0\u00a0−3/4 + 1/4) = (−1/2\u00a0\u00a0−√3/2; √3/2\u00a0\u00a0−1/2), the rotation through 120°.",
                "S³ = S²S = (−1/4 − 3/4\u00a0\u00a0√3/4 − √3/4; √3/4 − √3/4\u00a0\u00a0−3/4 − 1/4) = (−1 0; 0 −1), the rotation through 180°.",
                "(b) S is a rotation through 60°, so Sⁿ is a rotation through 60n°. This is the identity first when 60n = 360, "
                "so n = 6. Check: S⁶ = (S³)² = (−I)² = I.",
                "(c) 100 = 6 × 16 + 4, so S¹⁰⁰ = (S⁶)¹⁶S⁴ = S⁴, the rotation through 240°: S¹⁰⁰ = (−1/2\u00a0\u00a0√3/2; −√3/2\u00a0\u00a0−1/2).",
            ],
        },
        {
            "title": "A composite transformation in three dimensions",
            "question": "A is the reflection in the plane y = 0 and B is the rotation through 90° about the z-axis (positive sense). "
                        "(a) Write down A and B. (b) Find the matrix C of A followed by B. (c) Find the image of (1, 2, 3) under C and "
                        "describe C geometrically.",
            "steps": [
                "(a) A = (1 0 0; 0 −1 0; 0 0 1). With θ = 90°, cos θ = 0 and sin θ = 1, so B = (0 −1 0; 1 0 0; 0 0 1).",
                "(b) A first, then B: C = BA = (0 −1 0; 1 0 0; 0 0 1)(1 0 0; 0 −1 0; 0 0 1) = (0 1 0; 1 0 0; 0 0 1).",
                "(c) C(1, 2, 3)ᵀ = (2, 1, 3)ᵀ. C swaps the x and y coordinates and keeps z: it is the reflection in the plane "
                "y = x (the plane x − y = 0), since every point of that plane is fixed and i and j swap.",
            ],
        },
    ],
    "practice": [
        "A = (3 −2; 1 4) and B = (0 5; −1 2). Find (a) A + 2B (b) 3A − B (c) AB.",
        "P = (1 2 0; −1 0 3) and Q = (2, −1, 4)ᵀ. (a) State the order of PQ and find it. (b) Explain why QP is not defined.",
        "A = (1 2; 0 1) and B = (1 0; 3 1). Find AB and BA, and hence show that (A + B)² ≠ A² + 2AB + B².",
        "M = (1 1; 0 1). Find M², M³ and M⁴, and suggest a formula for Mⁿ. (Unit A8 proves it by induction.)",
        "Write down the matrix of each transformation. (a) Reflection in the line y = −x. (b) Rotation through 90° clockwise about O. "
        "(c) Enlargement, centre O, scale factor −2. (d) Stretch parallel to the y-axis, scale factor 3.",
        "Describe fully the transformation represented by (a) (−1 0; 0 −1) (b) (0 −1; −1 0) (c) (1 0; −2 1) (d) (1/√2\u00a0\u00a01/√2; −1/√2\u00a0\u00a01/√2).",
        "The linear transformation T maps (1, 0) to (2, 1) and (0, 1) to (−1, 3). (a) Write down the matrix of T. "
        "(b) Find the image of (4, −2). (c) Find the images of the vertices of the unit square.",
        "Using the formula for a reflection in y = (tan θ)x, find the matrix of the reflection in the line y = x/√3, and find the "
        "image of the point (2, 0).",
        "P is a stretch parallel to the x-axis with scale factor 2, and Q is a rotation through 90° anticlockwise about O. "
        "(a) Find the matrix of P followed by Q. (b) Find the matrix of Q followed by P. (c) Find the image of (1, 1) under each.",
        "Write down the matrix of the rotation through 90° about the x-axis (positive sense) and find the image of (2, −1, 5). "
        "Then find the matrix of this rotation followed by a reflection in the plane x = 0.",
        "A = (a 2; 1 b), where a and b are positive constants. Given that A² = (11 10; 5 6), find a and b.",
        "M(θ) denotes the reflection in y = (tan θ)x and R(θ) the rotation through θ about O. Show that "
        "M(α)M(β) = R(2(α − β)), and interpret this result.",
    ],
    "answers": [
        "(a) (3 8; −1 8) (b) (9 −11; 4 10) (c) AB = (2 11; −4 13).",
        "(a) (2 × 3)(3 × 1) gives 2 × 1: PQ = (0, 10)ᵀ. (b) Q is 3 × 1 and P is 2 × 3; the inner numbers 1 and 2 differ.",
        "AB = (7 2; 3 1), BA = (1 2; 3 7). (A + B)² = A² + AB + BA + B², which differs from A² + 2AB + B² by BA − AB ≠ 0. "
        "Directly: A + B = (2 2; 3 2), (A + B)² = (10 8; 12 10), while A² + 2AB + B² = (1 4; 0 1) + (14 4; 6 2) + (1 0; 6 1) "
        "= (16 8; 12 4).",
        "M² = (1 2; 0 1), M³ = (1 3; 0 1), M⁴ = (1 4; 0 1); Mⁿ = (1 n; 0 1).",
        "(a) (0 −1; −1 0) (b) (0 1; −1 0) (c) (−2 0; 0 −2) (d) (1 0; 0 3).",
        "(a) Rotation through 180° about O (equivalently enlargement, centre O, scale factor −1). (b) Reflection in y = −x. "
        "(c) Shear with the y-axis fixed, (x, y) ↦ (x, y − 2x), e.g. (1, 0) ↦ (1, −2). (d) Rotation through 45° clockwise "
        "(i.e. −45°) about O.",
        "(a) (2 −1; 1 3) (b) (10, −2) (c) (0, 0), (2, 1), (1, 4), (−1, 3).",
        "tan θ = 1/√3 so θ = 30°, 2θ = 60°: matrix (1/2\u00a0\u00a0√3/2; √3/2\u00a0\u00a0−1/2). Image of (2, 0) is (1, √3).",
        "(a) QP = (0 −1; 2 0) (b) PQ = (0 −2; 1 0) (c) QP: (−1, 2); PQ: (−2, 1).",
        "R = (1 0 0; 0 0 −1; 0 1 0); image (2, −5, −1). Then reflection X = (−1 0 0; 0 1 0; 0 0 1), and the composite is "
        "XR = (−1 0 0; 0 0 −1; 0 1 0).",
        "A² = (a² + 2\u00a0\u00a02a + 2b; a + b\u00a0\u00a02 + b²). So a + b = 5, a² = 9, b² = 4; with a, b > 0: a = 3, b = 2 (and 2a + 2b = 10 checks).",
        "M(α)M(β) = (cos 2α cos 2β + sin 2α sin 2β\u00a0\u00a0cos 2α sin 2β − sin 2α cos 2β; sin 2α cos 2β − cos 2α sin 2β\u00a0\u00a0"
        "sin 2α sin 2β + cos 2α cos 2β) = (cos 2(α − β)\u00a0\u00a0−sin 2(α − β); sin 2(α − β)\u00a0\u00a0cos 2(α − β)) = R(2(α − β)). "
        "Reflecting in the line at angle β and then in the line at angle α is a rotation through twice the angle from the first "
        "mirror to the second.",
    ],
    "exam": [
        "The matrix M = (k 2; 3 −1), where k is a constant.\n"
        "(a) Find M² in terms of k. [2]\n"
        "(b) Find the value of k for which M² is a multiple of the identity matrix, and state M² for this value. [3]\n"
        "(c) For this value of k, find M⁵, showing your method. [2]",
        "A is the matrix of the reflection in the line y = −x, and B is the matrix of the enlargement, centre O, scale factor 3.\n"
        "(a) Write down A and B. [2]\n"
        "(b) Find the matrix C of the transformation A followed by B. [2]\n"
        "(c) Triangle T has vertices (1, 0), (3, 0) and (1, 2). Find the vertices of its image under C. [2]\n"
        "(d) Find the area of the image of T, explaining your reasoning. [2]",
        "P = (0 0 1; 0 1 0; −1 0 0).\n"
        "(a) Describe fully the transformation represented by P. [2]\n"
        "(b) Write down the matrix Q of the reflection in the plane z = 0. [1]\n"
        "(c) Find the matrix R of the transformation P followed by Q. [2]\n"
        "(d) Find the image of the point (2, −3, 1) under R. [1]\n"
        "(e) Show that R² = I and explain this result geometrically. [2]",
        "(OCR A, OCR MEI, CAIE: shears.) S = (1 2; 0 1) and R = (0 −1; 1 0).\n"
        "(a) Describe fully the transformation represented by S. [2]\n"
        "(b) Find S² and S³, and suggest a formula for Sⁿ. [3]\n"
        "(c) Find RS and SR, and state what this shows about the order of the two transformations. [3]\n"
        "(d) The transformation S followed by R maps the point P to (−3, 5). Find the coordinates of P. [3]",
    ],
    "exam_answers": [
        "(a) M² = (k² + 6\u00a0\u00a02k − 2; 3k − 3\u00a0\u00a07). M1 A1\n"
        "(b) Need 2k − 2 = 0 and 3k − 3 = 0, so k = 1 (B1); then k² + 6 = 7 also matches (M1), so M² = 7I = (7 0; 0 7). A1\n"
        "(c) M⁵ = (M²)²M = 49M (M1) = (49 98; 147 −49). A1",
        "(a) A = (0 −1; −1 0), B = (3 0; 0 3). B1 B1\n"
        "(b) C = BA (M1) = (0 −3; −3 0). A1\n"
        "(c) (1, 0) ↦ (0, −3); (3, 0) ↦ (0, −9); (1, 2) ↦ (−6, −3). M1 A1\n"
        "(d) Area of T = ½ × 2 × 2 = 2 (B1). The reflection keeps area and the enlargement multiplies area by 3² = 9, so the image "
        "has area 18. A1",
        "(a) i ↦ −k, k ↦ i, j fixed: rotation through 90° about the y-axis (positive sense: anticlockwise viewed from the positive "
        "y-axis towards O). Compare (cos θ 0 sin θ; 0 1 0; −sin θ 0 cos θ) with θ = 90°. B1 B1\n"
        "(b) Q = (1 0 0; 0 1 0; 0 0 −1). B1\n"
        "(c) R = QP (M1) = (0 0 1; 0 1 0; 1 0 0). A1\n"
        "(d) (1, −3, 2). B1\n"
        "(e) R² = (0 0 1; 0 1 0; 1 0 0)² = I (B1). R swaps x and z and keeps y: it is the reflection in the plane x = z, and "
        "reflecting twice returns every point to where it started. B1",
        "(a) Shear with the x-axis fixed; (x, y) ↦ (x + 2y, y), e.g. (0, 1) ↦ (2, 1). B1 B1\n"
        "(b) S² = (1 4; 0 1), S³ = (1 6; 0 1) (B1 B1); Sⁿ = (1 2n; 0 1). B1\n"
        "(c) RS = (0 −1; 1 2) (B1), SR = (2 −1; 1 0) (B1). RS ≠ SR, so applying the shear and the rotation in different orders "
        "gives different transformations. B1\n"
        "(d) RS(x, y)ᵀ = (−y, x + 2y)ᵀ = (−3, 5)ᵀ (M1), so y = 3 and x = 5 − 6 = −1 (M1): P = (−1, 3). A1",
    ],
}
