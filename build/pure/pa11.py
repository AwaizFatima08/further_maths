UNIT = {
    "number": "A11",
    "title": "Three equations in three unknowns and three planes",
    "tag": "AS · Edexcel CP 3.7–3.8 · AQA C7–C8 (A level) · OCR A 4.03r (AS), 4.03s–t (A level) · OCR MEI Pv4–Pv5 (AS) · "
           "CAIE 9231 P2 2.2 · not in IAL · uses Units A6 (inverses) and A9 (planes)",
    "notes": [
        ("h2", "11.1 Writing a system as a matrix equation"),
        ("p", "Three linear equations in x, y and z can be written as one matrix equation Ax = b, where A is the 3 × 3 matrix of "
              "coefficients (row by row, as in Unit A5), x = (x, y, z)ᵀ and b is the column of constants. For example"),
        ("p", "2x − y + 3z = 7, x + 4z = 1, 3y − z = 0\u00a0\u00a0is\u00a0\u00a0(2 −1 3; 1 0 4; 0 3 −1)(x, y, z)ᵀ = (7, 1, 0)ᵀ."),
        ("p", "Notice the zeros for missing terms. Cambridge (2.2) asks you to go both ways: to set up the matrix equation from a "
              "problem described in words, and to write out the equations represented by a matrix equation."),
        ("h2", "11.2 Unique solutions: using the inverse matrix"),
        ("box", "When det A ≠ 0", [
            "Multiply Ax = b on the left by A⁻¹: x = A⁻¹b. There is exactly one solution (Edexcel 3.7, AQA C7, OCR A 4.03r, MEI Pv5).",
            "Geometrically, the three planes meet at a single point.",
            "With a calculator: enter A, find A⁻¹ (or solve directly) and multiply by b. Show the matrix equation in your working.",
            "Without a calculator: find A⁻¹ by cofactors (Unit A6), or eliminate one variable at a time.",
        ]),
        ("p", "Always check your solution in all three original equations: it takes seconds and catches sign slips."),
        ("h2", "11.3 Each equation is a plane"),
        ("p", "The equation ax + by + cz = d is a plane with normal vector n = (a, b, c)ᵀ (Unit A9). Two planes are parallel when their "
              "normals are parallel (one is a multiple of the other). If the whole equation, constant included, is a multiple of "
              "the other, the two planes are the same plane (<b>coincident</b>). The rows of A are the three normals, so "
              "det A = 0 exactly when the three normals lie in one plane (are linearly dependent); then the three planes cannot "
              "meet at a single point."),
        ("h2", "11.4 The possible arrangements"),
        ("table", ["Arrangement", "det A", "Solutions", "How to recognise it"], [
            ["Three planes meet at a single point", "≠ 0", "exactly one", "det A ≠ 0"],
            ["<b>Sheaf</b>: three planes through one common line", "0", "infinitely many (a line)",
             "no two normals parallel; one equation is a combination of the other two, constants included"],
            ["<b>Triangular prism</b>: each pair meets in a line; the three lines are parallel", "0", "none",
             "no two normals parallel; the left-hand sides combine but the constants do not"],
            ["Two parallel planes, the third cutting both", "0", "none", "exactly two normals parallel; those two equations are "
             "not multiples of each other"],
            ["Three parallel planes (all distinct, or two coincident)", "0", "none", "all three normals parallel, not all coincident"],
            ["Two coincident planes meeting the third in a line", "0", "infinitely many (a line)", "two equations are multiples, "
             "constants included"],
            ["Three coincident planes", "0", "infinitely many (a plane)", "all three equations are multiples"],
        ]),
        ("figure", "pa11_planes.png", "Arrangements of three planes: (a) a single point; (b) a sheaf; (c) a triangular prism; "
                   "(d) two parallel planes cut by a third; (e) three parallel planes; (f) two coincident planes cut by a third.", 160),
        ("p", "A system with at least one solution is <b>consistent</b>; one with none is <b>inconsistent</b>. Edexcel (3.8) uses "
              "the words point, sheaf and prism and calls the rest “otherwise inconsistent”; OCR A (4.03s–t) asks you to decide "
              "between consistent and inconsistent and to interpret the result, including parallel cases; AQA C8 and MEI Pv4 ask you "
              "to interpret “the solution, and failure of solution” geometrically."),
        ("figure", "pa11_endon.png", "Looking along the common direction of the lines of intersection, each plane appears as a line. "
                   "(a) Sheaf: the three meet at one point (the common line seen end on). (b) Prism: they form a triangle.", 120),
        ("h2", "11.5 Deciding the case when det A = 0"),
        ("box", "Method", [
            "1. Compare the normals. If two (or three) are parallel, decide which planes are parallel and which coincide.",
            "2. If no two normals are parallel, the arrangement is a sheaf or a prism. Eliminate the same variable from two pairs of "
            "equations. You get two equations in two unknowns with the same left-hand side (up to a multiple).",
            "3. If they agree (the same equation), the system is consistent: a <b>sheaf</b>. If they contradict each other "
            "(e.g. 3x + y = 4 and 3x + y = 5), it is inconsistent: a <b>prism</b>.",
            "Equivalent test: find α and β with row 3 = α(row 1) + β(row 2) on the left. Then it is a sheaf if d₃ = αd₁ + βd₂ "
            "and a prism otherwise.",
        ]),
        ("h2", "11.6 Solving a consistent singular system (CAIE 2.2; not required by OCR A or MEI)"),
        ("p", "In a sheaf, every point of the common line is a solution. To find the line, use two of the equations (the third adds "
              "nothing), let one variable be a parameter, say z = t, and solve for x and y in terms of t. Write the answer as "
              "r = a + tb. The direction b must be perpendicular to every normal, so b is parallel to n₁ × n₂ (Unit A10): a useful "
              "check. OCR A (4.03t) and MEI (Pv5) explicitly exclude finding this line."),
        ("h2", "11.7 Systems containing a parameter"),
        ("p", "Exam questions often put an unknown k in A or in b. First find the values of k that make det A = 0: for every other k "
              "there is a unique solution, which you can find in terms of k. Then substitute each special value of k and decide, by "
              "Section 11.5, whether the system is consistent and what the planes look like."),
        ("warn", "Common mistakes", [
            "Saying “det A = 0, so there are no solutions”. A zero determinant means no <b>unique</b> solution: the system may "
            "still be consistent (a sheaf, or coincident planes).",
            "Calling every inconsistent singular system a prism. Check first for parallel planes.",
            "Not giving a reason: state the evidence, e.g. “3(row 1) − row 2 gives 5x + 2z = 11, contradicting 5x + 2z = 9, so the "
            "system is inconsistent; no two planes are parallel, so the planes form a prism”.",
            "Multiplying by A⁻¹ on the right (bA⁻¹ is not even defined for a column b).",
            "Forgetting to check the solution in all three equations.",
        ]),
    ],
    "examples": [
        {
            "title": "A unique solution by inverse matrix",
            "question": "Solve x + 2y − z = 3, 2x − y + z = 4, 3x + y + 2z = 9 using an inverse matrix, and interpret the "
                        "solution geometrically.",
            "steps": [
                "Write it as Ax = b with A = (1 2 −1; 2 −1 1; 3 1 2) and b = (3, 4, 9)ᵀ.",
                "det A = 1(−2 − 1) − 2(4 − 3) + (−1)(2 + 3) = −3 − 2 − 5 = −10 ≠ 0, so A⁻¹ exists.",
                "By cofactors (or calculator), A⁻¹ = (1/10)(3 5 −1; 1 −5 3; −5 −5 5).",
                "x = A⁻¹b = (1/10)(9 + 20 − 9, 3 − 20 + 27, −15 − 20 + 45)ᵀ = (1/10)(20, 10, 10)ᵀ = (2, 1, 1)ᵀ.",
                "Check: 2 + 2 − 1 = 3, 4 − 1 + 1 = 4, 6 + 1 + 2 = 9. The three planes meet at the single point (2, 1, 1).",
            ],
        },
        {
            "title": "Sheaf or prism?",
            "question": "The planes Π₁: x + y + z = 6, Π₂: x − y + 2z = 5 and Π₃: 3x + y + 4z = c. (a) Show that the planes do not "
                        "meet at a single point. (b) Given c = 17, show that the planes form a sheaf and (CAIE) find a vector "
                        "equation of the common line. (c) Describe the arrangement when c = 20.",
            "steps": [
                "(a) det(1 1 1; 1 −1 2; 3 1 4) = 1(−4 − 2) − 1(4 − 6) + 1(1 + 3) = −6 + 2 + 4 = 0, so there is no unique point.",
                "(b) The normals (1, 1, 1), (1, −1, 2), (3, 1, 4) are not parallel in pairs. Look for row 3 = α row 1 + β row 2: "
                "α + β = 3 and α − β = 1 give α = 2, β = 1, and then 2 × 1 + 1 × 2 = 4 matches the z-coefficient.",
                "Constants: 2 × 6 + 5 = 17 = c. So Π₃ is 2Π₁ + Π₂: the system is consistent and the planes form a sheaf.",
                "Let z = t. Then x + y = 6 − t and x − y = 5 − 2t, so x = (11 − 3t)/2 and y = (1 + t)/2.",
                "t = 1 gives the point (4, 1, 1), and the direction is (−3/2, 1/2, 1), or (3, −1, −2). Line: r = (4, 1, 1)ᵀ + s(3, −1, −2)ᵀ.",
                "Check: n₁ × n₂ = (1, 1, 1) × (1, −1, 2) = (3, −1, −2). Correct.",
                "(c) If c = 20, then 2Π₁ + Π₂ gives 3x + y + 4z = 17, which contradicts 3x + y + 4z = 20: no solutions. No two "
                "planes are parallel, so each pair meets in a line and the three lines are parallel: a triangular prism.",
            ],
        },
        {
            "title": "Parallel planes",
            "question": "Describe the arrangement of the planes x + 2y − z = 4, 2x + 4y − 2z = 3 and x − y + z = 2.",
            "steps": [
                "Normals: (1, 2, −1), (2, 4, −2) = 2(1, 2, −1) and (1, −1, 1). The first two are parallel; the third is not.",
                "Twice the first equation is 2x + 4y − 2z = 8 ≠ 3, so the first two planes are parallel and distinct.",
                "The third plane cuts both of them, in two parallel lines. There is no point common to all three: the system is "
                "inconsistent (and det A = 0 because two rows are proportional).",
            ],
        },
        {
            "title": "A system with a parameter",
            "question": "kx + y + z = 1, x + ky + z = 1, x + y + kz = −2. (a) Find the values of k for which there is no unique "
                        "solution. (b) For other values of k, solve the system. (c) Interpret geometrically the cases in (a).",
            "steps": [
                "(a) det(k 1 1; 1 k 1; 1 1 k) = k(k² − 1) − (k − 1) + (1 − k) = k³ − 3k + 2 = (k − 1)²(k + 2). No unique solution when "
                "k = 1 or k = −2.",
                "(b) Subtracting the first two equations: (k − 1)(x − y) = 0, so x = y when k ≠ 1. Subtracting the 2nd and 3rd: "
                "(k − 1)(y − z) = 3, so y − z = 3/(k − 1).",
                "Adding all three: (k + 2)(x + y + z) = 0, so x + y + z = 0 when k ≠ −2. With x = y and z = y − 3/(k − 1): "
                "3y − 3/(k − 1) = 0, so x = y = 1/(k − 1) and z = −2/(k − 1).",
                "Check in the first equation: (k + 1 − 2)/(k − 1) = 1. Correct.",
                "(c) k = 1: the equations are x + y + z = 1 (twice) and x + y + z = −2. Two coincident planes and a third plane parallel "
                "to them: inconsistent.",
                "k = −2: the rows (−2, 1, 1), (1, −2, 1), (1, 1, −2) add to 0, and so do the constants 1 + 1 − 2 = 0. The system is "
                "consistent and no two normals are parallel: a sheaf. (The common line is r = (0, 0, 1)ᵀ + t(1, 1, 1)ᵀ.)",
            ],
        },
        {
            "title": "Formulating a problem (CAIE 2.2)",
            "question": "A café sells pastries at £x, sandwiches at £y and coffees at £z. Order A: 2 pastries, 1 sandwich and 3 coffees "
                        "cost £14.10. Order B: 1 pastry, 2 sandwiches and 1 coffee cost £11.20. Order C: 3 pastries, 1 sandwich and "
                        "2 coffees cost £13.10. Write this as a matrix equation and find the prices.",
            "steps": [
                "(2 1 3; 1 2 1; 3 1 2)(x, y, z)ᵀ = (14.10, 11.20, 13.10)ᵀ.",
                "det = 2(4 − 1) − 1(2 − 3) + 3(1 − 6) = 6 + 1 − 15 = −8 ≠ 0, so there is a unique solution.",
                "Using the inverse (calculator), (x, y, z) = (1.50, 3.60, 2.50).",
                "Check: 2(1.50) + 3.60 + 3(2.50) = 14.10, 1.50 + 2(3.60) + 2.50 = 11.20, 3(1.50) + 3.60 + 2(2.50) = 13.10. "
                "A pastry costs £1.50, a sandwich £3.60 and a coffee £2.50.",
            ],
        },
    ],
    "practice": [
        "(a) Write 2x − y + 3z = 7, x + 4z = 1, 3y − z = 0 as a matrix equation. (b) Write out the equations represented by "
        "(1 2 0; 0 1 −1; 3 0 1)(x, y, z)ᵀ = (5, 2, 4)ᵀ.",
        "Use an inverse matrix to solve x + y + z = 6, 2x − y + 3z = 9, x + 2y − z = 2.",
        "Given that (1 2 3; 0 1 4; 5 6 0)⁻¹ = (−24 18 5; 20 −15 −4; −5 4 1), solve x + 2y + 3z = 1, y + 4z = 2, 5x + 6y = 3.",
        "Without a calculator, solve 2x + y − z = 3, x − y + 2z = 5, 3x + 2y + z = 10.",
        "Describe the arrangement of each set of planes. (a) x + 2y − z = 1, 2x + 4y − 2z = 5, x − y + z = 0. "
        "(b) x + y + z = 1, 2x + 2y + 2z = 3, 3x + 3y + 3z = 5.",
        "Show that the planes x + 2y − z = 1, 2x − y + z = 3 and 4x + 3y − z = 5 form a sheaf, and (CAIE) find a vector equation "
        "of the common line.",
        "Show that the planes x + 2y − z = 1, 2x − y + z = 3 and 4x + 3y − z = 6 have no common point, and describe their arrangement.",
        "x + y + z = 2, x + 2y + 3z = 5, 2x + 3y + kz = 7. (a) Find the value of k for which there is no unique solution. "
        "(b) For this value, show that the equations are consistent and describe the planes.",
        "Explain why the planes x − y + 2z = 1, 3x + y − z = 4 and 5x − y + 3z = c cannot meet at a single point, and find the "
        "value of c for which they have a line in common.",
        "Show that x + y = a, y + z = 1, x + z = 2 has a unique solution for every a, and find it in terms of a.",
        "Π₁: x + y − z = 2, Π₂: 2x − y + z = 1, Π₃: x − 2y + 2z = k. Show that the matrix of coefficients is singular, find the value "
        "of k for which the system is consistent, and describe the arrangement for other values of k.",
        "(CAIE 2.2) The sum of three numbers is 20. The first plus twice the second is 19, and the second plus three times the "
        "third is 31. Write this as a matrix equation and solve it.",
    ],
    "answers": [
        "(a) (2 −1 3; 1 0 4; 0 3 −1)(x, y, z)ᵀ = (7, 1, 0)ᵀ. (b) x + 2y = 5, y − z = 2, 3x + z = 4.",
        "det = 5; x = 1, y = 2, z = 3.",
        "(x, y, z) = (−24 + 36 + 15, 20 − 30 − 12, −5 + 8 + 3) = (27, −22, 6).",
        "det = −10; x = 2, y = 1, z = 2.",
        "(a) First two planes parallel (normals (1, 2, −1) and (2, 4, −2); 2 × 1 ≠ 5), third cuts both: no solution. "
        "(b) All normals parallel; 2 × 1 ≠ 3, 3 × 1 ≠ 5, 3/2 ≠ 5/3: three distinct parallel planes, no solution.",
        "Row 3 = 2(row 1) + row 2 and 2 × 1 + 3 = 5, consistent; no normals parallel, so a sheaf. Line: r = (0, 4, 7)ᵀ + t(1, −3, −5)ᵀ "
        "(direction = (1, 2, −1) × (2, −1, 1)).",
        "2(row 1) + row 2 gives 4x + 3y − z = 5 ≠ 6: inconsistent. No two normals are parallel, so the planes form a triangular prism.",
        "(a) det = k − 4, so k = 4. (b) Row 3 = row 1 + row 2 and 2 + 5 = 7: consistent. No normals parallel: a sheaf.",
        "Row 3 = 2(row 1) + row 2 on the left, so det = 0 (no unique point). They share a line (sheaf) when c = 2 × 1 + 4 = 6.",
        "det(1 1 0; 0 1 1; 1 0 1) = 2 ≠ 0. x = (a + 1)/2, y = (a − 1)/2, z = (3 − a)/2.",
        "Row 3 = row 2 − row 1, so det = 0. Consistent when k = 1 − 2 = −1 (a sheaf); for k ≠ −1 inconsistent, and as no normals "
        "are parallel, a triangular prism.",
        "(1 1 1; 1 2 0; 0 1 3)(a, b, c)ᵀ = (20, 19, 31)ᵀ; det = 1(6) − 1(3) + 1(1) = 4; a = 5, b = 7, c = 8.",
    ],
    "exam": [
        "The planes Π₁: x + 2y − z = 1, Π₂: 2x − y + 3z = 7 and Π₃: 3x + y + kz = c, where k and c are constants.\n"
        "(a) Find, in terms of k, the determinant of the matrix of coefficients. [2]\n"
        "(b) Given that k = 3 and c = 10, find the point of intersection of the three planes. [3]\n"
        "(c) Given that k = 2, find the value of c for which the planes have a common line, and describe the arrangement of the "
        "planes for other values of c. [4]\n"
        "(d) (CAIE) For k = 2 and this value of c, find a vector equation of the common line. [3]",
        "3x − y + 2z = 4, x + y − z = 2, 5x + y + az = b.\n"
        "(a) Find the values of a for which the equations have a unique solution. [3]\n"
        "(b) Given that a = 0, find the value of b for which the equations are consistent, and interpret this case "
        "geometrically. [3]\n"
        "(c) Interpret geometrically the case a = 0 with any other value of b. [2]\n"
        "(d) Solve the equations when a = 2 and b = 12. [3]",
        "For each system, determine whether the equations are consistent, and describe the arrangement of the three planes.\n"
        "(a) x + y + z = 3, 2x + 2y + 2z = 5, x − y = 0 [3]\n"
        "(b) x − y + z = 1, 2x + y − z = 2, x + 2y − 2z = 3 [3]\n"
        "(c) x + y + z = 1, x − y + z = 1, 3x + y + 3z = 3 [3]\n"
        "(d) Explain why the matrix of coefficients is singular in all three cases. [1]",
        "A = (1 1 1; 1 −1 2; 2 1 −1).\n"
        "(a) Find A⁻¹ without using a calculator. [4]\n"
        "(b) Hence solve x + y + z = 6, x − y + 2z = 5, 2x + y − z = 1. [2]\n"
        "(c) Interpret your answer to (b) geometrically. [1]",
    ],
    "exam_answers": [
        "(a) det = 1(−k − 3) − 2(2k − 9) − 1(2 + 3) (M1) = 10 − 5k. A1\n"
        "(b) det = −5 ≠ 0; x = A⁻¹(1, 7, 10)ᵀ (M1) = (1, 1, 2)ᵀ (A1 A1): the planes meet at (1, 1, 2).\n"
        "(c) det = 0. Row 3 = row 1 + row 2 on the left (M1), so consistent iff c = 1 + 7 = 8 (A1). Then the planes form a "
        "sheaf (B1). For c ≠ 8: no two normals parallel, so a triangular prism. B1\n"
        "(d) Let z = t: x + 2y = 1 + t, 2x − y = 7 − 3t (M1), so x = 3 − t, y = t − 1 (A1): r = (3, −1, 0)ᵀ + t(−1, 1, 1)ᵀ. "
        "Check: n₁ × n₂ = (5, −5, −5), parallel. A1",
        "(a) det = 3(a + 1) + (a + 5) + 2(1 − 5) (M1) = 4a (A1); unique solution iff a ≠ 0. A1\n"
        "(b) Row 3 = row 1 + 2(row 2) on the left (M1); consistent iff b = 4 + 2 × 2 = 8 (A1); the planes form a sheaf. A1\n"
        "(c) b ≠ 8: inconsistent (B1); no two normals parallel, so a triangular prism. B1\n"
        "(d) Adding the first two: 4x + z = 6; then z = 6 − 4x, y = 2 − x + z = 8 − 5x (M1). Third: 5x + 8 − 5x + 2(6 − 4x) = 12, "
        "so x = 1 (M1): x = 1, y = 3, z = 2. A1",
        "(a) Normals of the first two are parallel and 2 × 3 ≠ 5 (B1), so those planes are parallel and distinct; the third "
        "(normal (1, −1, 0)) cuts both (B1): inconsistent, two parallel planes cut by a third. B1\n"
        "(b) Row 3 = row 2 − row 1 on the left (M1); constants 2 − 1 = 1 ≠ 3, inconsistent (A1); no parallel normals: prism. A1\n"
        "(c) Row 3 = 2(row 1) + row 2 (M1); constants 2 + 1 = 3, consistent (A1); no parallel normals: sheaf. A1\n"
        "(d) In each case one row of A is a combination of the others (the normals are linearly dependent), so det A = 0. B1",
        "(a) det A = 1(1 − 2) − 1(−1 − 4) + 1(1 + 2) = 7 (B1). Cofactors (−1 5 3; 2 −3 1; 3 −1 −2) (M1 A1), "
        "A⁻¹ = (1/7)(−1 2 3; 5 −3 −1; 3 1 −2). A1\n"
        "(b) x = A⁻¹(6, 5, 1)ᵀ (M1) = (1/7)(−6 + 10 + 3, 30 − 15 − 1, 18 + 5 − 2)ᵀ = (1, 2, 3)ᵀ. A1\n"
        "(c) The three planes meet at the single point (1, 2, 3). B1",
    ],
}
