UNIT = {
    "number": "B12",
    "title": "Eigenvalues, eigenvectors and diagonalisation",
    "tag": "A level · AQA C10–C11 (no Cayley–Hamilton) · CAIE 9231 P2 2.2 (real distinct eigenvalues) · IAL FP3 6.7–6.8 "
           "(no Cayley–Hamilton) · Edexcel FP2 3.1–3.3 (option; AS FP2 2.1–2.3, 2 × 2 only) · OCR MEI Extra Pure Xm1–Xm6 · "
           "not on OCR A",
    "notes": [
        ("h2", "12.1 Eigenvectors and eigenvalues"),
        ("p", "Matrix notation is as in Unit A5. Most vectors change direction when multiplied by a matrix M. An <b>eigenvector</b> of "
              "a square matrix M is a <b>non-zero</b> vector v whose direction is unchanged (or exactly reversed): Mv = λv for some "
              "scalar λ, called the <b>eigenvalue</b> belonging to v. Any non-zero multiple of an eigenvector is also an eigenvector "
              "with the same eigenvalue, so an eigenvector really describes a direction."),
        ("box", "Definitions", [
            "Mv = λv with v ≠ 0: v is an eigenvector of M and λ is the corresponding eigenvalue.",
            "Geometrically (AQA C10, MEI Xm6): the line through O in the direction of v is an <b>invariant line</b> (Unit A7). Points "
            "on it are scaled by the factor λ; if λ < 0 they are also sent to the other side of O.",
            "If λ = 1, the line through O in the direction of v is a line of invariant points.",
            "A <b>normalised</b> eigenvector has length 1: divide v by |v| (Edexcel 3.1, IAL 6.7).",
        ]),
        ("figure", "pb12_directions.png", "M = (4 1; 2 3) applied to vectors round the unit circle. Most vectors turn, but those along "
                   "(1, 1) are stretched by 5 and those along (1, −2) by 2: these are the eigenvector directions.", 95),
        ("h2", "12.2 The characteristic equation"),
        ("p", "Mv = λv can be written (M − λI)v = 0. A non-zero solution v exists only when M − λI is singular (Unit A6), so the "
              "eigenvalues are the roots of the <b>characteristic equation</b> det(M − λI) = 0 (MEI Xm2, CAIE 2.2)."),
        ("box", "Characteristic equations", [
            "2 × 2: for M = (a b; c d), det(M − λI) = λ² − (a + d)λ + (ad − bc) = 0, i.e. λ² − (tr M)λ + det M = 0.",
            "3 × 3: expand det(M − λI) = 0 to get a cubic. Multiplying by −1 it reads λ³ − (tr M)λ² + c₁λ − det M = 0, where c₁ is "
            "the sum of the three 2 × 2 minors on the leading diagonal.",
            "Checks: the eigenvalues add up to the trace tr M (the sum of the leading-diagonal entries) and multiply to det M.",
            "A 3 × 3 cubic usually has an obvious integer root: try factors of det M, then factorise.",
        ]),
        ("h2", "12.3 Finding eigenvectors"),
        ("p", "For each eigenvalue λ, solve (M − λI)v = 0. The equations are dependent (that is why λ is an eigenvalue), so in 2-D you "
              "use just one of them; in 3-D you use two. A quick 3-D method: v is perpendicular to every row of M − λI, so the "
              "vector product of two non-parallel rows of M − λI is an eigenvector. Always check by computing Mv."),
        ("p", "Example: M = (4 1; 2 3) has λ² − 7λ + 10 = 0, so λ = 2 or 5. For λ = 2, M − 2I = (2 1; 2 1) gives 2x + y = 0, "
              "v = (1, −2)ᵀ. For λ = 5, M − 5I = (−1 1; 2 −2) gives y = x, v = (1, 1)ᵀ. Normalised: (1/√5)(1, −2)ᵀ and (1/√2)(1, 1)ᵀ."),
        ("h2", "12.4 Repeated and complex eigenvalues (Edexcel FP2; real eigenvalues only for CAIE, MEI and AQA)"),
        ("p", "A <b>repeated</b> eigenvalue may have a whole plane of eigenvectors or only a single direction. For (2 0; 0 2) every "
              "non-zero vector is an eigenvector with λ = 2; for (2 1; 0 2), λ = 2 is repeated but (M − 2I)v = 0 gives y = 0, a single "
              "direction (1, 0)ᵀ. In 3-D a reflection in a plane has λ = 1 repeated, and every vector in the mirror plane is an "
              "eigenvector (Worked example B12.4)."),
        ("p", "If the characteristic equation has <b>complex</b> roots, there is no real eigenvector and so no real invariant line "
              "through O. For the rotation (0 −1; 1 0), λ² + 1 = 0 gives λ = ±i, with eigenvectors (1, −i)ᵀ for i and (1, i)ᵀ for −i "
              "(check: M(1, −i)ᵀ = (i, 1)ᵀ = i(1, −i)ᵀ). Complex eigenvalues of a real matrix come in conjugate pairs."),
        ("h2", "12.5 Simple properties from Mv = λv (CAIE 2.2)"),
        ("box", "If Mv = λv, then", [
            "Mⁿv = λⁿv for every positive integer n, so λⁿ is an eigenvalue of Mⁿ with the same eigenvector.",
            "Proof by induction: true for n = 1. If Mᵏv = λᵏv, then Mᵏ⁺¹v = M(λᵏv) = λᵏ(Mv) = λᵏ⁺¹v. So it is true for n = k + 1, "
            "and by induction for all n ≥ 1.",
            "(M + kI)v = (λ + k)v, and (kM)v = (kλ)v.",
            "If M is non-singular, then λ ≠ 0 and M⁻¹v = (1/λ)v: multiply Mv = λv by M⁻¹ to get v = λM⁻¹v.",
            "M is singular exactly when 0 is an eigenvalue.",
        ]),
        ("h2", "12.6 Diagonalisation and powers"),
        ("p", "Suppose an n × n matrix M has n independent eigenvectors v₁, …, vₙ with eigenvalues λ₁, …, λₙ (this is always true "
              "when the eigenvalues are distinct). Put the eigenvectors as the columns of a matrix U, and the eigenvalues, in the "
              "same order, on the diagonal of D. Then MU = (λ₁v₁ … λₙvₙ) = UD. Since U is non-singular:"),
        ("box", "Diagonalisation", [
            "M = UDU⁻¹ and U⁻¹MU = D. (AQA writes M = UDU⁻¹; CAIE writes QDQ⁻¹; Edexcel writes P⁻¹MP = D: all the same idea.)",
            "The order of the eigenvectors in U must match the order of the eigenvalues in D.",
            "Powers: Mⁿ = UDⁿU⁻¹, because the inner U⁻¹U pairs cancel, and Dⁿ just raises each diagonal entry to the power n.",
            "AQA C11 and MEI Xm3 require real eigenvalues (MEI: distinct); CAIE restricts to real, distinct eigenvalues.",
        ]),
        ("h2", "12.7 Symmetric matrices and orthogonal diagonalisation (Edexcel FP2 3.2, IAL FP3 6.8)"),
        ("p", "A matrix is <b>symmetric</b> if Aᵀ = A. A real symmetric matrix has real eigenvalues, and eigenvectors belonging to "
              "different eigenvalues are perpendicular. Proof of the second fact: if Av₁ = λ₁v₁ and Av₂ = λ₂v₂, then "
              "λ₁v₂ᵀv₁ = v₂ᵀAv₁ = (Av₂)ᵀv₁ = λ₂v₂ᵀv₁, so (λ₁ − λ₂)v₂·v₁ = 0, and v₂·v₁ = 0 when λ₁ ≠ λ₂."),
        ("box", "Orthogonal diagonalisation", [
            "Use <b>normalised</b> eigenvectors as the columns of P. The columns are then perpendicular unit vectors, so PᵀP = I: "
            "P is an <b>orthogonal</b> matrix and P⁻¹ = Pᵀ.",
            "Then PᵀAP = D, and A = PDPᵀ. No inverse needs to be calculated.",
        ]),
        ("h2", "12.8 The Cayley–Hamilton theorem (Edexcel FP2 3.3, MEI Xm5, CAIE 2.2; not AQA or IAL)"),
        ("p", "Every square matrix satisfies its own characteristic equation. For M = (a b; c d) this says "
              "M² − (a + d)M + (ad − bc)I = 0, which you can check by multiplying out. (A full proof is not required: MEI "
              "excludes it, and Cambridge uses the result without naming it.)"),
        ("box", "Using Cayley–Hamilton", [
            "2 × 2: M² = (tr M)M − (det M)I. Multiply by M repeatedly to write any power as pM + qI.",
            "Inverse (2 × 2): M(M − (tr M)I) = −(det M)I, so M⁻¹ = ((tr M)I − M)/det M.",
            "3 × 3: if the characteristic equation is λ³ − pλ² + qλ − r = 0, then M³ = pM² − qM + rI, and "
            "M⁻¹ = (M² − pM + qI)/r when r = det M ≠ 0.",
        ]),
        ("h2", "12.9 Eigenvectors and transformations in 3-D (MEI Xm6, AQA C10)"),
        ("bullets", [
            "Reflection in a plane through O: eigenvalue −1 with eigenvector normal to the plane, and eigenvalue 1 (repeated) with "
            "every vector in the plane as an eigenvector. So the eigenvector for −1 gives the normal, and hence the equation, of "
            "the mirror plane.",
            "Rotation about an axis through O: the axis direction is an eigenvector with eigenvalue 1 (a line of invariant points). "
            "Unless the angle is 180°, the other two eigenvalues are complex.",
            "Stretch or enlargement: the eigenvectors are the directions of the stretch, and the eigenvalues are the scale factors.",
        ]),
        ("warn", "Common mistakes", [
            "Giving the zero vector as an eigenvector. Eigenvectors are non-zero by definition.",
            "Putting the eigenvectors in U in a different order from the eigenvalues in D.",
            "Writing Mⁿ = U⁻¹DⁿU. The eigenvectors are the columns of U, so Mⁿ = UDⁿU⁻¹.",
            "Using un-normalised eigenvectors in P and then claiming P⁻¹ = Pᵀ.",
            "Dividing the characteristic polynomial by λ, losing the eigenvalue 0.",
            "Not checking: Mv = λv takes one line and catches almost every slip. Also check the trace and determinant.",
        ]),
    ],
    "examples": [
        {
            "title": "Diagonalising a 2 × 2 matrix and finding powers",
            "question": "M = (4 1; 2 3). (a) Find the eigenvalues and eigenvectors of M. (b) Find U and D with M = UDU⁻¹. "
                        "(c) Hence find Mⁿ.",
            "steps": [
                "(a) λ² − 7λ + (12 − 2) = 0, so (λ − 2)(λ − 5) = 0: λ = 2 or 5 (sum 7 = trace, product 10 = det).",
                "λ = 2: 2x + y = 0, v₁ = (1, −2)ᵀ. λ = 5: −x + y = 0, v₂ = (1, 1)ᵀ. Check: M(1, −2)ᵀ = (2, −4)ᵀ and M(1, 1)ᵀ = (5, 5)ᵀ.",
                "(b) U = (1 1; −2 1), D = (2 0; 0 5). det U = 3, so U⁻¹ = ⅓(1 −1; 2 1).",
                "(c) Mⁿ = UDⁿU⁻¹ = (1 1; −2 1)(2ⁿ 0; 0 5ⁿ) × ⅓(1 −1; 2 1) = ⅓(2ⁿ  5ⁿ; −2ⁿ⁺¹  5ⁿ)(1 −1; 2 1)",
                "= ⅓(2ⁿ + 2 × 5ⁿ  −2ⁿ + 5ⁿ; −2ⁿ⁺¹ + 2 × 5ⁿ  2ⁿ⁺¹ + 5ⁿ).",
                "Check n = 1: ⅓(2 + 10, −2 + 5; −4 + 10, 4 + 5) = (4 1; 2 3). Correct.",
            ],
        },
        {
            "title": "A 3 × 3 matrix",
            "question": "M = (3 2 −2; 1 3 −1; 1 2 0). (a) Show that the characteristic equation is λ³ − 6λ² + 11λ − 6 = 0, and solve "
                        "it. (b) Find an eigenvector for each eigenvalue. (c) Write down U and D such that M = UDU⁻¹, and find Mⁿ.",
            "steps": [
                "(a) det(M − λI) = (3 − λ)[(3 − λ)(−λ) + 2] − 2[(−λ) + 1] − 2[2 − (3 − λ)] = (3 − λ)(λ² − 3λ + 2) + 2λ − 2 − 2λ + 2 "
                "= (3 − λ)(λ − 1)(λ − 2). Setting this to 0 and multiplying by −1: λ³ − 6λ² + 11λ − 6 = 0, with roots 1, 2, 3.",
                "Checks: 1 + 2 + 3 = 6 = trace, 1 × 2 × 3 = 6 = det M.",
                "(b) λ = 2: M − 2I = (1 2 −2; 1 1 −1; 1 2 −2). Rows 1 and 2: (1, 2, −2) × (1, 1, −1) = (0, −1, −1), so v = (0, 1, 1)ᵀ.",
                "λ = 1: M − I = (2 2 −2; 1 2 −1; 1 2 −1): (2, 2, −2) × (1, 2, −1) = (2, 0, 2), so v = (1, 0, 1)ᵀ.",
                "λ = 3: M − 3I = (0 2 −2; 1 0 −1; 1 2 −3): (0, 2, −2) × (1, 0, −1) = (−2, −2, −2), so v = (1, 1, 1)ᵀ.",
                "Check: M(1, 0, 1)ᵀ = (1, 0, 1)ᵀ, M(0, 1, 1)ᵀ = (0, 2, 2)ᵀ, M(1, 1, 1)ᵀ = (3, 3, 3)ᵀ.",
                "(c) U = (1 0 1; 0 1 1; 1 1 1), D = (1 0 0; 0 2 0; 0 0 3). det U = −1 and U⁻¹ = (0 −1 1; −1 0 1; 1 1 −1).",
                "Mⁿ = U diag(1, 2ⁿ, 3ⁿ) U⁻¹ = (3ⁿ  3ⁿ − 1  1 − 3ⁿ; 3ⁿ − 2ⁿ  3ⁿ  2ⁿ − 3ⁿ; "
                "3ⁿ − 2ⁿ  3ⁿ − 1  2ⁿ − 3ⁿ + 1). With n = 1 this gives M back.",
            ],
        },
        {
            "title": "Orthogonal diagonalisation of a symmetric matrix",
            "question": "A = (2 2; 2 −1). Find an orthogonal matrix P and a diagonal matrix D such that PᵀAP = D.",
            "steps": [
                "λ² − λ − 6 = 0, so λ = 3 or −2.",
                "λ = 3: −x + 2y = 0, v = (2, 1)ᵀ. λ = −2: 4x + 2y = 0, v = (1, −2)ᵀ. These are perpendicular: 2 × 1 + 1 × (−2) = 0.",
                "Normalise: each has length √5. P = (1/√5)(2 1; 1 −2), D = (3 0; 0 −2).",
                "Check: AP = (1/√5)(6 −2; 3 4) and PᵀAP = (1/5)(2 1; 1 −2)(6 −2; 3 4) = (1/5)(15 0; 0 −10) = (3 0; 0 −2). Correct.",
            ],
            "figure": "pb12_symmetric.png",
            "caption": "A = (2 2; 2 −1) maps the unit circle to an ellipse whose axes lie along the perpendicular eigenvectors (2, 1) and (1, −2).",
            "width_mm": 80,
        },
        {
            "title": "Finding the plane of a reflection (MEI Xm6; Edexcel repeated eigenvalues)",
            "question": "M = ⅓(1 −2 2; −2 1 2; 2 2 1). (a) Show that (1, 1, −1)ᵀ is an eigenvector and find its eigenvalue. "
                        "(b) Show that M² = I. (c) Find the characteristic equation and the eigenvectors for λ = 1. "
                        "(d) Describe the transformation M.",
            "steps": [
                "(a) M(1, 1, −1)ᵀ = ⅓(1 − 2 − 2, −2 + 1 − 2, 2 + 2 − 1)ᵀ = ⅓(−3, −3, 3)ᵀ = −(1, 1, −1)ᵀ: eigenvalue −1.",
                "(b) 3M is symmetric, each of its rows has length 3 and different rows are perpendicular, so (3M)(3M) = (3M)(3M)ᵀ = 9I and M² = I.",
                "(c) The trace is 1 and det M = −1. If λ is an eigenvalue then λ² is an eigenvalue of M² = I, so λ = ±1. With sum 1 "
                "and product −1, the eigenvalues are 1, 1, −1: (λ − 1)²(λ + 1) = 0, i.e. λ³ − λ² − λ + 1 = 0.",
                "λ = 1: M − I = ⅓(−2 −2 2; −2 −2 2; 2 2 −2). Every row gives x + y − z = 0, so every vector in the plane "
                "x + y − z = 0 is an eigenvector, e.g. (1, −1, 0)ᵀ and (1, 0, 1)ᵀ.",
                "(d) Points of the plane x + y − z = 0 are fixed, and the normal direction (1, 1, −1) is reversed: M is the "
                "reflection in the plane x + y − z = 0.",
            ],
        },
        {
            "title": "Cayley–Hamilton for powers and inverses (Edexcel FP2, MEI, CAIE)",
            "question": "M = (3 −1; 2 0). (a) Use the Cayley–Hamilton theorem to find M⁻¹. (b) Express M⁴ in the form pM + qI. "
                        "(c) B = (2 1 0; 0 1 −1; 0 2 4) has characteristic equation λ³ − 7λ² + 16λ − 12 = 0. Find B⁻¹.",
            "steps": [
                "(a) Trace 3, det 2: λ² − 3λ + 2 = 0, so M² − 3M + 2I = 0. Then M(3I − M) = 2I, so M⁻¹ = ½(3I − M) = ½(0 1; −2 3).",
                "(b) M² = 3M − 2I. M³ = 3M² − 2M = 3(3M − 2I) − 2M = 7M − 6I. M⁴ = 7M² − 6M = 7(3M − 2I) − 6M = 15M − 14I.",
                "So M⁴ = 15M − 14I = (31 −15; 30 −14).",
                "(c) B³ − 7B² + 16B − 12I = 0, so B(B² − 7B + 16I) = 12I and B⁻¹ = (1/12)(B² − 7B + 16I).",
                "B² = (4 3 −1; 0 −1 −5; 0 10 14), so B² − 7B + 16I = (6 −4 −1; 0 8 2; 0 −4 2) and B⁻¹ = (1/12)(6 −4 −1; 0 8 2; 0 −4 2).",
            ],
        },
    ],
    "practice": [
        "Find the eigenvalues and corresponding eigenvectors of (a) (5 4; 1 2) (b) (1 2; 2 1).",
        "Show that (3 1; 0 3) has a repeated eigenvalue but only one independent eigenvector, and explain why it cannot be "
        "diagonalised.",
        "(Edexcel FP2) Find the eigenvalues of (1 −2; 1 3), and an eigenvector for the eigenvalue with positive imaginary part.",
        "Find normalised eigenvectors of (4 −2; −2 1).",
        "Find the eigenvalues and eigenvectors of (2 0 0; 1 3 0; 4 −1 1).",
        "M = (2 1 1; 1 2 1; 1 1 2). Show that (1, 1, 1)ᵀ is an eigenvector and state its eigenvalue. Show that (1, −1, 0)ᵀ and "
        "(1, 0, −1)ᵀ are eigenvectors with the same eigenvalue, and interpret this geometrically.",
        "M = (3 2; 1 4). Find U and D with M = UDU⁻¹, and hence find M⁴.",
        "(CAIE) Mv = λv with v ≠ 0. (a) Prove that λ³ is an eigenvalue of M³. (b) Given that the eigenvalues of a matrix N are "
        "1, 2 and 3, write down the eigenvalues of N² + 2N and of N⁻¹.",
        "M = (2 1; 3 4). Use the Cayley–Hamilton theorem to (a) find M⁻¹ (b) express M³ in the form pM + qI.",
        "A = (1 1 0; 0 2 1; 0 0 3). Find the characteristic equation and use the Cayley–Hamilton theorem to find A⁻¹.",
        "(Edexcel FP2, IAL FP3) Find an orthogonal matrix P and a diagonal matrix D with PᵀAP = D, where A = (5 2; 2 2).",
        "(MEI Xm6) M = ⅓(1 2 2; 2 1 −2; 2 −2 1). Show that (1, −1, −1)ᵀ is an eigenvector with eigenvalue −1, and that every "
        "point of the plane x − y − z = 0 is invariant. Describe M.",
    ],
    "answers": [
        "(a) λ² − 7λ + 6 = 0: λ = 1, (1, −1)ᵀ; λ = 6, (4, 1)ᵀ. (b) λ² − 2λ − 3 = 0: λ = 3, (1, 1)ᵀ; λ = −1, (1, −1)ᵀ.",
        "(λ − 3)² = 0, λ = 3 twice. (M − 3I)v = 0 gives y = 0 only: eigenvectors are multiples of (1, 0)ᵀ. U would need two "
        "independent eigenvector columns, so no invertible U exists.",
        "λ² − 4λ + 5 = 0, λ = 2 ± i. For 2 + i: (−1 − i)x − 2y = 0, e.g. v = (2, −1 − i)ᵀ.",
        "λ² − 5λ = 0: λ = 0, (1/√5)(1, 2)ᵀ; λ = 5, (1/√5)(2, −1)ᵀ.",
        "Lower triangular, so λ = 2, 3, 1. λ = 1: (0, 0, 1)ᵀ; λ = 2: (1, −1, 5)ᵀ; λ = 3: (0, 2, −1)ᵀ.",
        "M(1, 1, 1)ᵀ = 4(1, 1, 1)ᵀ: λ = 4. M(1, −1, 0)ᵀ = (1, −1, 0)ᵀ and M(1, 0, −1)ᵀ = (1, 0, −1)ᵀ: λ = 1 for both, so every vector "
        "in the plane x + y + z = 0 is an eigenvector with λ = 1: that plane consists of invariant points, and M stretches by "
        "factor 4 along the perpendicular direction (1, 1, 1).",
        "λ = 5, (1, 1)ᵀ; λ = 2, (2, −1)ᵀ. U = (1 2; 1 −1), D = (5 0; 0 2), U⁻¹ = ⅓(1 2; 1 −1). "
        "M⁴ = UD⁴U⁻¹ = ⅓(625 + 32  1250 − 32; 625 − 16  1250 + 16) = (219 406; 203 422).",
        "(a) M³v = M²(λv) = λM(λv) = λ²Mv = λ³v, and v ≠ 0. (b) N² + 2N: 1 + 2 = 3, 4 + 4 = 8, 9 + 6 = 15. N⁻¹: 1, ½, ⅓.",
        "λ² − 6λ + 5 = 0, so M² = 6M − 5I. (a) M⁻¹ = (6I − M)/5 = (1/5)(4 −1; −3 2). (b) M³ = 6M² − 5M = 31M − 30I.",
        "λ³ − 6λ² + 11λ − 6 = 0 (eigenvalues 1, 2, 3). A⁻¹ = (A² − 6A + 11I)/6 = (1/6)(6 −3 1; 0 3 −1; 0 0 2) "
        "= (1\u00a0\u00a0−½\u00a0\u00a01/6; 0\u00a0\u00a0½\u00a0\u00a0−1/6; 0\u00a0\u00a00\u00a0\u00a0⅓).",
        "λ² − 7λ + 6 = 0: λ = 6, (2, 1)ᵀ; λ = 1, (1, −2)ᵀ. P = (1/√5)(2 1; 1 −2), D = (6 0; 0 1).",
        "M(1, −1, −1)ᵀ = ⅓(1 − 2 − 2, 2 − 1 + 2, 2 + 2 − 1)ᵀ = (−1, 1, 1)ᵀ. For (x, y, z) with x = y + z: "
        "M(y + z, y, z)ᵀ = ⅓(3y + 3z, 3y, 3z)ᵀ = (y + z, y, z)ᵀ. M is the reflection in the plane x − y − z = 0.",
    ],
    "exam": [
        "M = (5 −2; 4 −1).\n"
        "(a) Find the eigenvalues of M and a corresponding eigenvector for each. [5]\n"
        "(b) Write down a matrix U and a diagonal matrix D such that M = UDU⁻¹. [2]\n"
        "(c) Hence show that Mⁿ = (2 × 3ⁿ − 1  1 − 3ⁿ; 2 × 3ⁿ − 2  2 − 3ⁿ) for every positive integer n. [4]\n"
        "(d) State the equations of the invariant lines of M through the origin, and say which is a line of invariant points. [2]",
        "(Edexcel FP2, IAL FP3) A = (1 1 0; 1 2 1; 0 1 1).\n"
        "(a) Show that 3 is an eigenvalue of A, and find the other eigenvalues. [4]\n"
        "(b) Find a normalised eigenvector for each eigenvalue. [4]\n"
        "(c) Write down an orthogonal matrix P and a diagonal matrix D such that PᵀAP = D. [2]",
        "(Edexcel FP2, MEI, CAIE) B = (2 1 0; 0 1 −1; 0 2 4).\n"
        "(a) Show that the characteristic equation of B is λ³ − 7λ² + 16λ − 12 = 0. [3]\n"
        "(b) Hence find the eigenvalues of B. [2]\n"
        "(c) Use the Cayley–Hamilton theorem to find B⁻¹. [4]\n"
        "(d) Express B⁴ in the form pB² + qB + rI, where p, q and r are integers. [3]",
        "(MEI Xm6, AQA C10) M = (0 0 1; 1 0 0; 0 1 0).\n"
        "(a) Show that (1, 1, 1)ᵀ is an eigenvector of M and state its eigenvalue. [2]\n"
        "(b) Show that M³ = I, and deduce that 1 is the only real eigenvalue of M. [3]\n"
        "(c) Find the characteristic equation of M. [2]\n"
        "(d) Given that a rotation through θ about an axis through O has trace 1 + 2 cos θ, describe fully the transformation "
        "represented by M. [3]",
    ],
    "exam_answers": [
        "(a) λ² − 4λ + 3 = 0 (M1), λ = 1 or 3 (A1). λ = 1: 4x − 2y = 0, (1, 2)ᵀ (M1 A1). λ = 3: 2x − 2y = 0, (1, 1)ᵀ. A1\n"
        "(b) U = (1 1; 2 1), D = (1 0; 0 3) (or the columns in the other order, consistently). B1 B1\n"
        "(c) U⁻¹ = (−1 1; 2 −1) (B1). Mⁿ = UDⁿU⁻¹ (M1) = (1  3ⁿ; 2  3ⁿ)(−1 1; 2 −1) (M1) "
        "= (−1 + 2 × 3ⁿ  1 − 3ⁿ; −2 + 2 × 3ⁿ  2 − 3ⁿ). A1\n"
        "(d) y = 2x (λ = 1: a line of invariant points) and y = x (points scaled by 3). B1 B1",
        "(a) det(A − 3I) = det(−2 1 0; 1 −1 1; 0 1 −2) = −2(2 − 1) − 1(−2 − 0) + 0 = 0 (M1 A1). Characteristic equation "
        "λ³ − 4λ² + 3λ = 0, i.e. λ(λ − 1)(λ − 3) = 0 (M1): the others are 0 and 1. A1\n"
        "(b) λ = 3: (1, 2, 1)ᵀ/√6; λ = 1: (1, 0, −1)ᵀ/√2; λ = 0: (1, −1, 1)ᵀ/√3. M1 A1 A1 A1\n"
        "(c) P = (1/√6  1/√2  1/√3; 2/√6  0  −1/√3; 1/√6  −1/√2  1/√3), "
        "D = (3 0 0; 0 1 0; 0 0 0) (B1 B1; any consistent order).",
        "(a) det(B − λI) = (2 − λ)[(1 − λ)(4 − λ) + 2] − 1 × 0 + 0 (M1) = (2 − λ)(λ² − 5λ + 6) (A1); expanding and multiplying "
        "by −1 gives λ³ − 7λ² + 16λ − 12 = 0. A1\n"
        "(b) (2 − λ)(λ − 2)(λ − 3) = 0 (M1): λ = 2 (repeated) and λ = 3. A1\n"
        "(c) B³ − 7B² + 16B − 12I = 0 (M1), so B(B² − 7B + 16I) = 12I and B⁻¹ = (1/12)(B² − 7B + 16I) (M1). "
        "B² = (4 3 −1; 0 −1 −5; 0 10 14) (B1), B⁻¹ = (1/12)(6 −4 −1; 0 8 2; 0 −4 2). A1\n"
        "(d) B⁴ = 7B³ − 16B² + 12B (M1) = 7(7B² − 16B + 12I) − 16B² + 12B (M1) = 33B² − 100B + 84I. A1",
        "(a) M(1, 1, 1)ᵀ = (1, 1, 1)ᵀ (M1): eigenvalue 1. A1\n"
        "(b) M² = (0 1 0; 0 0 1; 1 0 0) and M³ = I (B1). If Mv = λv then v = M³v = λ³v (M1), so λ³ = 1, whose only real root "
        "is 1. A1\n"
        "(c) det(M − λI) = −λ(λ²) + 1 = 1 − λ³ (M1), so λ³ − 1 = 0. A1\n"
        "(d) (1, 1, 1) is fixed, so M is a rotation about the line x = y = z (B1). Trace 0 = 1 + 2 cos θ gives cos θ = −½, "
        "θ = 120° (M1); M³ = I confirms a rotation through 120° (equivalently 240° in the other sense) about x = y = z. A1",
    ],
}
