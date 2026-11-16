UNIT = {
    "number": "A6",
    "title": "Determinants and inverses",
    "tag": "AS · Edexcel CP 3.5–3.6 · IAL FP1 5.4–5.5, 6.4 (2 × 2); FP3 6.3–6.6 (3 × 3, transpose) · AQA C5–C6 (AS 2 × 2; "
           "3 × 3 A level), C9 (A level) · OCR A 4.03h–q (AS) · OCR MEI Pm7–Pm14 (AS), Pm15 (A level) · CAIE 9231 P1 1.4",
    "notes": [
        ("h2", "6.1 The determinant of a 2 × 2 matrix"),
        ("p", "Matrix notation is as in Unit A5: M = (a b; c d) has rows a, b and c, d. The <b>determinant</b> of M is the number "
              "det M = |M| = ad − bc. It tells you how the transformation M changes area, and whether M can be undone."),
        ("p", "Why it is an area scale factor: M maps the unit square to the parallelogram with vertices O, (a, c), (a + b, c + d) "
              "and (b, d). Enclose the parallelogram in the rectangle (a + b) by (c + d) (drawn for positive entries, as in the figure) and "
              "subtract the two triangles and two small rectangles round the edge: "
              "(a + b)(c + d) − ac − bd − 2bc = ad − bc. A linear map scales every small square by the same factor, so every "
              "area is multiplied by |det M|."),
        ("box", "2 × 2 determinants", [
            "det (a b; c d) = ad − bc.",
            "Area of image = |det M| × area of object (Edexcel 3.5, OCR A 4.03i, MEI Pm8, CAIE 1.4, IAL 6.4).",
            "det M > 0: orientation is kept (anticlockwise order of vertices stays anticlockwise).",
            "det M < 0: orientation is reversed, as in a reflection.",
            "det M = 0: the plane is squashed onto a line (or the point O); areas become 0.",
        ]),
        ("figure", "pa06_area.png", "The unit square and its image under M = (3 1; 1 2), a parallelogram of area det M = 5. "
                   "The square's vertices O, (1, 0), (1, 1), (0, 1) and their images O, A′, B′, C′ both run anticlockwise, so orientation is kept.", 95),
        ("h2", "6.2 The determinant of a 3 × 3 matrix"),
        ("p", "For a 3 × 3 matrix, the <b>minor</b> of an entry is the 2 × 2 determinant left when you delete that entry's row and "
              "column. The <b>cofactor</b> is the minor multiplied by the sign from the chessboard pattern (+ − +; − + −; + − +)."),
        ("box", "3 × 3 determinants", [
            "det (a b c; d e f; g h i) = a(ei − fh) − b(di − fg) + c(dh − eg)\u00a0\u00a0(expansion along the first row).",
            "You may expand along any row or column: multiply each entry by its cofactor and add. Choose a row or column with zeros.",
            "Volume of image = |det M| × volume of object; det M < 0 means the orientation of space is reversed (a right-handed "
            "set of axes becomes left-handed), as in a reflection (Edexcel 3.5, OCR A 4.03k, MEI Pm9).",
        ]),
        ("p", "Example: for A = (2 0 1; 1 3 −1; 0 1 1), expand along the first row (it has a zero): "
              "det A = 2(3 × 1 − (−1) × 1) − 0 + 1(1 × 1 − 3 × 0) = 2 × 4 + 1 = 9. Expanding down the first column instead gives "
              "2(3 + 1) − 1(0 − 1) + 0 = 9, as it must."),
        ("p", "Calculators: OCR A (4.03h, 4.03j) requires determinants both with and without a calculator; Edexcel and MEI AS allow "
              "a calculator for 3 × 3 work, but MEI Pm15 (A level), AQA, Cambridge and IAL expect you to work by hand, often with "
              "algebraic entries. Always show the expansion when the entries contain letters."),
        ("h2", "6.3 Properties of determinants"),
        ("box", "Rules you may quote", [
            "det(AB) = det A × det B (OCR A 4.03m, MEI Pm10). Geometrically: B scales volume by det B, then A by det A.",
            "det(Aᵀ) = det A, so every rule about rows also holds for columns.",
            "For an n × n matrix, det(kA) = kⁿ det A: k² for 2 × 2, k³ for 3 × 3 (every row is multiplied by k).",
            "det(A⁻¹) = 1/det A, because det A × det(A⁻¹) = det I = 1.",
            "Swapping two rows (or columns) changes the sign of the determinant.",
            "Adding a multiple of one row to another row leaves the determinant unchanged (likewise for columns).",
            "A common factor of every entry in one row (or column) can be taken outside the determinant.",
            "If two rows (or two columns) are equal or proportional, the determinant is 0.",
        ]),
        ("p", "For 2 × 2 matrices, det(AB) = det A det B can be checked directly: with A = (a b; c d) and B = (p q; r s), "
              "AB = (ap + br\u00a0\u00a0aq + bs; cp + dr\u00a0\u00a0cq + ds), and expanding (ap + br)(cq + ds) − (aq + bs)(cp + dr) gives "
              "(ad − bc)(ps − qr)."),
        ("h2", "6.4 Singular and non-singular matrices"),
        ("p", "A square matrix is <b>singular</b> if its determinant is 0 and <b>non-singular</b> otherwise (all boards; Cambridge "
              "asks you to recall the meaning). A singular matrix has no inverse: a 2 × 2 singular matrix maps the whole plane onto "
              "a line through O (or onto O), so different points share an image and the map cannot be reversed. A 3 × 3 singular "
              "matrix maps space onto a plane or a line through O. To find when a matrix with a parameter is singular, set its "
              "determinant equal to 0 and solve."),
        ("h2", "6.5 The inverse of a 2 × 2 matrix"),
        ("p", "The <b>inverse</b> of a square matrix A is the matrix A⁻¹ with AA⁻¹ = A⁻¹A = I. It exists exactly when det A ≠ 0, and "
              "it is unique."),
        ("box", "2 × 2 inverse", [
            "If A = (a b; c d) and det A = ad − bc ≠ 0, then A⁻¹ = (1/(ad − bc)) (d −b; −c a).",
            "Swap the leading-diagonal entries, change the signs of the other two, divide by the determinant.",
            "Check: (a b; c d)(d −b; −c a) = (ad − bc\u00a0\u00a00; 0\u00a0\u00a0ad − bc) = (ad − bc)I.",
        ]),
        ("h2", "6.6 The inverse of a 3 × 3 matrix"),
        ("p", "By hand (required by AQA, CAIE, IAL FP3 and MEI Pm15; OCR A 4.03o asks for both methods; Edexcel allows a calculator "
              "but the process must be understood), use the following steps."),
        ("box", "3 × 3 inverse by cofactors", [
            "1. Find det A. If it is 0, stop: A has no inverse.",
            "2. Find the matrix of minors (replace each entry by its minor).",
            "3. Apply the sign pattern (+ − +; − + −; + − +) to get the matrix of cofactors C.",
            "4. Transpose: the <b>adjugate</b> (adjoint) is adj A = Cᵀ.",
            "5. A⁻¹ = (1/det A) adj A. Check that one row of A times one column of A⁻¹ gives the right entry of I.",
        ]),
        ("p", "The method works because multiplying a row of A by the cofactors of that same row gives det A (expansion), while "
              "multiplying it by the cofactors of a different row gives the determinant of a matrix with two equal rows, which is 0. "
              "So A adj A = (det A)I."),
        ("h2", "6.7 Properties of inverses and matrix equations"),
        ("box", "Inverse rules", [
            "(AB)⁻¹ = B⁻¹A⁻¹ (all boards). Proof: (AB)(B⁻¹A⁻¹) = A(BB⁻¹)A⁻¹ = AIA⁻¹ = AA⁻¹ = I, and an inverse is unique.",
            "This extends to more factors: (ABC)⁻¹ = C⁻¹B⁻¹A⁻¹ (CAIE notes this).",
            "(A⁻¹)⁻¹ = A, (kA)⁻¹ = (1/k)A⁻¹, (Aᵀ)⁻¹ = (A⁻¹)ᵀ.",
            "To solve AX = B, multiply on the <b>left</b> by A⁻¹: X = A⁻¹B. To solve XA = B, multiply on the <b>right</b>: X = BA⁻¹.",
        ]),
        ("p", "Think of putting on socks then shoes: to undo, take off the shoes first. If B is applied first and then A, the "
              "inverse undoes A first and then B, which is B⁻¹A⁻¹."),
        ("h2", "6.8 Inverse transformations"),
        ("p", "If the matrix M maps P to P′, then M⁻¹ maps P′ back to P (OCR A 4.03q, MEI Pm12–13, CAIE 1.4, IAL 6.4, 6.6). So to "
              "find an object from its image, multiply the image by M⁻¹. Geometrically, the inverse of a rotation through θ is the "
              "rotation through −θ; a reflection is its own inverse (M² = I); the inverse of a stretch with factor k is the "
              "stretch with factor 1/k; the inverse of the shear (1 k; 0 1) is (1 −k; 0 1)."),
        ("h2", "6.9 The transpose (IAL FP3, OCR A language)"),
        ("p", "The <b>transpose</b> Aᵀ of an m × n matrix A is the n × m matrix whose rows are the columns of A. A square matrix with "
              "Aᵀ = A is <b>symmetric</b> (these matter in Unit B12). The key rule (IAL FP3 6.3) reverses the order, like the inverse "
              "rule: (AB)ᵀ = BᵀAᵀ. Also (A + B)ᵀ = Aᵀ + Bᵀ and (Aᵀ)ᵀ = A."),
        ("h2", "6.10 Factorising determinants (AQA C9, MEI Pm15)"),
        ("p", "When the entries are algebraic, simplify with row and column operations before expanding, aiming to create zeros "
              "and common factors. Write each operation, e.g. C₂ → C₂ − C₁, next to your working."),
        ("p", "Example: Δ = |1 1 1; a b c; a² b² c²|. Apply C₂ → C₂ − C₁ and C₃ → C₃ − C₁: Δ = |1 0 0; a\u00a0\u00a0b − a\u00a0\u00a0c − a; a²\u00a0\u00a0b² − a²\u00a0\u00a0"
              "c² − a²|. Take out the factors (b − a) from C₂ and (c − a) from C₃: Δ = (b − a)(c − a)|1 0 0; a 1 1; a²\u00a0\u00a0b + a\u00a0\u00a0c + a|. "
              "Expand along the first row: Δ = (b − a)(c − a)(c + a − b − a) = (b − a)(c − a)(c − b) = (a − b)(b − c)(c − a)."),
        ("p", "A useful shortcut: if putting a = b makes two columns equal, then Δ = 0 when a = b, so (a − b) is a factor (the factor "
              "theorem). By symmetry (b − c) and (c − a) are factors too, and comparing degrees finds what is left."),
        ("warn", "Common mistakes", [
            "Forgetting the minus sign on the middle term of a 3 × 3 expansion, or using the wrong sign pattern for cofactors.",
            "Forgetting to transpose the matrix of cofactors, or forgetting to divide by the determinant.",
            "Writing (AB)⁻¹ = A⁻¹B⁻¹, or solving XA = B as X = A⁻¹B. Pre- and post-multiplication are different.",
            "Using det(kA) = k det A. For a 3 × 3 matrix, det(2A) = 8 det A.",
            "Giving a negative area. Area scale factor = |det M|; the sign only tells you about orientation.",
            "Dividing by an expression that could be zero when solving det = 0, and so losing a value (e.g. k = 0).",
        ]),
    ],
    "examples": [
        {
            "title": "Area scale factor and orientation",
            "question": "M = (4 1; 2 −1). Triangle T has vertices O(0, 0), A(2, 0) and B(1, 3). (a) Find det M. (b) Find the vertices "
                        "and the area of the image of T under M. (c) What does the sign of det M tell you?",
            "steps": [
                "(a) det M = 4 × (−1) − 1 × 2 = −6.",
                "(b) M(2, 0)ᵀ = (8, 4)ᵀ and M(1, 3)ᵀ = (4 + 3, 2 − 3)ᵀ = (7, −1)ᵀ, so the image has vertices O, (8, 4), (7, −1).",
                "Area of T = ½ × 2 × 3 = 3, so the image has area |−6| × 3 = 18.",
                "Check with the shoelace formula: ½|8 × (−1) − 4 × 7| = ½ × 36 = 18. Correct.",
                "(c) det M < 0, so M reverses orientation: O, A, B is anticlockwise but its image is clockwise.",
            ],
        },
        {
            "title": "When is a 3 × 3 matrix singular?",
            "question": "A = (1 k 2; 0 3 k; 2 1 4). Find det A in terms of k, and the values of k for which A is singular.",
            "steps": [
                "Expand down the first column, which contains a zero. The cofactors are +|3 k; 1 4|, −|k 2; 1 4| and +|k 2; 3 k|.",
                "det A = 1 × (12 − k) − 0 + 2 × (k² − 6) = 12 − k + 2k² − 12 = 2k² − k = k(2k − 1).",
                "A is singular when det A = 0: k = 0 or k = ½. (Factorise; do not divide by k.)",
            ],
        },
        {
            "title": "Inverse of a 3 × 3 matrix by cofactors",
            "question": "Find, without a calculator, the inverse of A = (2 0 1; 1 3 −1; 0 1 1).",
            "steps": [
                "det A = 9 (Section 6.2), so A is non-singular.",
                "Minors: row 1: |3 −1; 1 1| = 4, |1 −1; 0 1| = 1, |1 3; 0 1| = 1. Row 2: |0 1; 1 1| = −1, |2 1; 0 1| = 2, |2 0; 0 1| = 2. "
                "Row 3: |0 1; 3 −1| = −3, |2 1; 1 −1| = −3, |2 0; 1 3| = 6.",
                "Matrix of minors (4 1 1; −1 2 2; −3 −3 6). Apply the signs (+ − +; − + −; + − +): cofactors C = (4 −1 1; 1 2 −2; −3 3 6).",
                "Transpose: adj A = (4 1 −3; −1 2 3; 1 −2 6).",
                "A⁻¹ = (1/9)(4 1 −3; −1 2 3; 1 −2 6).",
                "Check row 1 of A with column 1 of adj A: 2 × 4 + 0 × (−1) + 1 × 1 = 9, and with column 2: 2 × 1 + 0 + 1 × (−2) = 0. Correct.",
            ],
        },
        {
            "title": "(AB)⁻¹ and matrix equations",
            "question": "A = (2 1; 5 3) and B = (1 −2; 3 −4). (a) Find A⁻¹ and B⁻¹. (b) Find (AB)⁻¹ in two ways. "
                        "(c) Find the matrix X such that XA = (1 0; 2 1).",
            "steps": [
                "(a) det A = 6 − 5 = 1, so A⁻¹ = (3 −1; −5 2). det B = −4 + 6 = 2, so B⁻¹ = ½(−4 2; −3 1).",
                "(b) Directly: AB = (2 + 3\u00a0\u00a0−4 − 4; 5 + 9\u00a0\u00a0−10 − 12) = (5 −8; 14 −22), det(AB) = −110 + 112 = 2 = det A × det B, "
                "so (AB)⁻¹ = ½(−22 8; −14 5).",
                "Using the rule: B⁻¹A⁻¹ = ½(−4 2; −3 1)(3 −1; −5 2) = ½(−12 − 10\u00a0\u00a04 + 4; −9 − 5\u00a0\u00a03 + 2) = ½(−22 8; −14 5). Correct.",
                "(c) Multiply XA = C on the right by A⁻¹: X = CA⁻¹ = (1 0; 2 1)(3 −1; −5 2) = (3 −1; 1 0).",
                "Check: (3 −1; 1 0)(2 1; 5 3) = (6 − 5\u00a0\u00a03 − 3; 2 1) = (1 0; 2 1). Correct.",
            ],
        },
        {
            "title": "Using an inverse transformation",
            "question": "The transformation M = (3 1; 1 1) maps triangle T onto the triangle with vertices (4, 2), (5, 3) and (2, 2). "
                        "Find the vertices of T, and the areas of T and its image.",
            "steps": [
                "det M = 3 − 1 = 2, so M⁻¹ = ½(1 −1; −1 3).",
                "M⁻¹(4, 2)ᵀ = ½(2, 2)ᵀ = (1, 1)ᵀ; M⁻¹(5, 3)ᵀ = ½(2, 4)ᵀ = (1, 2)ᵀ; M⁻¹(2, 2)ᵀ = ½(0, 4)ᵀ = (0, 2)ᵀ.",
                "T has vertices (1, 1), (1, 2) and (0, 2): a right-angled triangle with legs 1 and 1, area ½.",
                "Image area = |det M| × ½ = 1. Check by the shoelace formula: ½|4(3 − 2) + 5(2 − 2) + 2(2 − 3)| = ½ × 2 = 1. Correct.",
            ],
        },
        {
            "title": "Factorising a determinant (AQA C9, MEI Pm15)",
            "question": "Show that |1 1 1; a b c; bc ca ab| = (a − b)(b − c)(c − a).",
            "steps": [
                "C₁ → C₁ − C₂ and C₂ → C₂ − C₃ (using the original columns): C₁ becomes (0, a − b, bc − ca)ᵀ = (0, a − b, −c(a − b))ᵀ "
                "and C₂ becomes (0, b − c, ca − ab)ᵀ = (0, b − c, −a(b − c))ᵀ.",
                "Take out (a − b) from C₁ and (b − c) from C₂: Δ = (a − b)(b − c)|0 0 1; 1 1 c; −c −a ab|.",
                "Expand along the first row: only the third entry is non-zero, with cofactor +|1 1; −c −a| = −a + c.",
                "So Δ = (a − b)(b − c)(c − a), as required.",
            ],
        },
    ],
    "practice": [
        "Find the determinant of (a) (5 3; 2 4) (b) (−2 7; 1 −3) (c) (a 2a; 3 b). (d) Find the values of k for which "
        "(k 3; 4 k + 1) is singular.",
        "Find the inverses of (a) (5 3; 2 4) (b) (−2 7; 1 −3).",
        "Find, without a calculator, the determinants of (a) (1 2 3; 0 4 5; 1 0 6) (b) (2 −1 0; 3 1 4; −1 2 1).",
        "Find the values of x for which (x 1 0; 1 x 1; 0 1 x) is singular.",
        "M = (2 −3; 1 4). A shape S has area 5 cm². Find the area of the image of S under (a) M (b) M².",
        "N = (1 2 0; 0 1 3; 2 0 1). (a) Find det N. (b) A cuboid measuring 2 cm by 3 cm by 4 cm is transformed by N. Find the "
        "volume of its image, and state whether orientation is preserved.",
        "Find, by the method of cofactors, the inverse of (1 2 3; 0 1 4; 5 6 0).",
        "A and B are 3 × 3 matrices with det A = 3 and det B = −2. Find (a) det(AB) (b) det(A⁻¹) (c) det(2A) (d) det(AᵀB²).",
        "A⁻¹ = (2 1; 1 1) and B⁻¹ = (1 −1; 0 2). Find (AB)⁻¹ and hence AB.",
        "A = (1 2; 0 −1; 3 1) and B = (2 0; 1 4). Find AB, (AB)ᵀ and BᵀAᵀ, and comment.",
        "The transformation T: (x, y) ↦ (x + 2y, 3x + 5y). Write down the matrix of T, find its inverse, and find the point "
        "whose image is (4, 11).",
        "Use row or column operations to factorise |x 1 1; 1 x 1; 1 1 x| completely.",
    ],
    "answers": [
        "(a) 14 (b) −1 (c) ab − 6a = a(b − 6) (d) k² + k − 12 = (k + 4)(k − 3) = 0, so k = −4 or 3.",
        "(a) (1/14)(4 −3; −2 5) (b) det = −1: (3 7; 1 2).",
        "(a) 1(24) − 2(0 − 5) + 3(0 − 4) = 22 (b) 2(1 − 8) + 1(3 + 4) + 0 = −7.",
        "det = x(x² − 1) − 1(x) = x³ − 2x = x(x² − 2) = 0: x = 0, √2, −√2.",
        "det M = 11. (a) 55 cm² (b) det(M²) = 121, so 605 cm².",
        "(a) 1(1) − 2(0 − 6) + 0 = 13 (b) 24 × 13 = 312 cm³; det N > 0, so orientation is preserved.",
        "det = 1. Cofactors (−24 20 −5; 18 −15 4; 5 −4 1); inverse = adjugate = (−24 18 5; 20 −15 −4; −5 4 1).",
        "(a) −6 (b) 1/3 (c) 2³ × 3 = 24 (d) 3 × (−2)² = 12.",
        "(AB)⁻¹ = B⁻¹A⁻¹ = (1 0; 2 2); AB = ((AB)⁻¹)⁻¹ = ½(2 0; −2 1) = (1 0; −1 ½).",
        "AB = (4 8; −1 −4; 7 4); (AB)ᵀ = (4 −1 7; 8 −4 4); BᵀAᵀ = (2 1; 0 4)(1 0 3; 2 −1 1) = (4 −1 7; 8 −4 4). They are equal, "
        "illustrating (AB)ᵀ = BᵀAᵀ. (AᵀBᵀ is not even defined here: 2 × 3 times 2 × 2.)",
        "(1 2; 3 5), det = −1, inverse (−5 2; 3 −1); point (2, 1).",
        "R₁ → R₁ + R₂ + R₃ gives (x + 2)|1 1 1; 1 x 1; 1 1 x|; then C₂ → C₂ − C₁, C₃ → C₃ − C₁ gives (x + 2)|1 0 0; 1 x − 1 0; "
        "1 0 x − 1| = (x + 2)(x − 1)².",
    ],
    "exam": [
        "A = (2 1 −1; 0 k 3; 1 2 1), where k is a constant.\n"
        "(a) Find det A in terms of k. [2]\n"
        "(b) State the value of k for which A is singular. [1]\n"
        "(c) Given that k = 2, find A⁻¹, showing your working. [4]\n"
        "(d) With k = 2, a solid of volume 7 cm³ is transformed by A. Find the volume of the image and describe the effect of A on "
        "orientation. [2]",
        "M = (3 −1; 2 1).\n"
        "(a) Show that M is non-singular and find M⁻¹. [3]\n"
        "(b) Triangle T is mapped by M onto the triangle with vertices (2, 3), (6, 4) and (−1, 1). Find the vertices of T. [3]\n"
        "(c) Find the area of T and the area of its image. [2]\n"
        "(d) N represents a reflection in the y-axis. Find the matrix of M followed by N, find its determinant, and explain the "
        "sign of your answer. [3]",
        "(a) A and B are non-singular square matrices of the same order. Prove that (AB)⁻¹ = B⁻¹A⁻¹. [3]\n"
        "(b) A = (1 2; 1 3) and (AB)⁻¹ = (3 1; 5 2). Find B. [4]\n"
        "(c) Verify that det(AB) = det A × det B for these matrices. [2]",
        "(AQA C9, MEI Pm15.) Δ = |1 1 1; a b c; a³ b³ c³|.\n"
        "(a) Explain why (a − b) is a factor of Δ. [1]\n"
        "(b) Show that Δ = (a − b)(b − c)(c − a)(a + b + c). [5]\n"
        "(c) Hence find the values of t for which the matrix (1 1 1; 1 2 t; 1 8 t³) is singular. [3]",
    ],
    "exam_answers": [
        "(a) det A = 2(k − 6) − 1(0 − 3) − 1(0 − k) (M1) = 3k − 9 = 3(k − 3). A1\n"
        "(b) k = 3. B1\n"
        "(c) det A = −3 (B1). Cofactors (−4 3 −2; −3 3 −3; 5 −6 4) (M1 A1), so A⁻¹ = −⅓(−4 −3 5; 3 3 −6; −2 −3 4) "
        "= (4/3 1 −5/3; −1 −1 2; 2/3 1 −4/3). A1\n"
        "(d) Volume 3 × 7 = 21 cm³ (B1); det A < 0, so orientation is reversed. B1",
        "(a) det M = 3 + 2 = 5 ≠ 0, so non-singular (B1). M⁻¹ = (1/5)(1 1; −2 3). M1 A1\n"
        "(b) M⁻¹(2, 3)ᵀ = (1, 1)ᵀ; M⁻¹(6, 4)ᵀ = (2, 0)ᵀ; M⁻¹(−1, 1)ᵀ = (0, 1)ᵀ. M1 A1 A1\n"
        "(c) T: ½|1(0 − 1) + 2(1 − 1) + 0(1 − 0)| = ½ (B1); image: 5 × ½ = 5/2. B1\n"
        "(d) N = (−1 0; 0 1); NM = (−3 1; 2 1) (M1 A1); det = −3 − 2 = −5: negative because the reflection reverses "
        "orientation (and det N det M = −1 × 5). B1",
        "(a) (AB)(B⁻¹A⁻¹) = A(BB⁻¹)A⁻¹ (M1) = AIA⁻¹ = AA⁻¹ = I (A1). Since the inverse of AB is unique, (AB)⁻¹ = B⁻¹A⁻¹. A1\n"
        "(b) B⁻¹A⁻¹ = C, where C = (3 1; 5 2), so B⁻¹ = CA (M1) = (4 9; 7 16) (A1); det = 64 − 63 = 1 (M1), "
        "B = (16 −9; −7 4). A1\n"
        "(c) AB = (2 −1; −5 3), det(AB) = 6 − 5 = 1 (B1); det A = 1 and det B = 64 − 63 = 1, product 1, as required. B1",
        "(a) If a = b the first two columns are equal, so Δ = 0; by the factor theorem (a − b) is a factor. B1\n"
        "(b) C₁ → C₁ − C₂, C₂ → C₂ − C₃ (M1): Δ = |0 0 1; a − b\u00a0\u00a0b − c\u00a0\u00a0c; a³ − b³\u00a0\u00a0b³ − c³\u00a0\u00a0c³| (A1). "
        "Take out (a − b)(b − c) (M1): Δ = (a − b)(b − c)|0 0 1; 1 1 c; a² + ab + b²\u00a0\u00a0b² + bc + c²\u00a0\u00a0c³| (A1). "
        "Expand along row 1: (b² + bc + c²) − (a² + ab + b²) = c² − a² + b(c − a) = (c − a)(a + b + c), so "
        "Δ = (a − b)(b − c)(c − a)(a + b + c). A1\n"
        "(c) This is Δ with a = 1, b = 2, c = t (M1): (−1)(2 − t)(t − 1)(3 + t) = 0 (A1), so t = 1, 2 or −3. A1",
    ],
}
