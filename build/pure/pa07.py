UNIT = {
    "number": "A7",
    "title": "Invariant points and invariant lines",
    "tag": "AS · Edexcel CP 3.4 · AQA C4 (AS) · OCR A 4.03g (AS, 2-D only) · OCR MEI Pm6 (AS) · CAIE 9231 P1 1.4 · "
           "not in IAL · leads to Unit B12 (eigenvectors)",
    "notes": [
        ("h2", "7.1 Invariant points"),
        ("p", "Matrix notation is as in Unit A5: M = (a b; c d). A point P is an <b>invariant point</b> of a transformation if it is "
              "mapped to itself: MP = P. For a matrix transformation the origin is always invariant, because M0 = 0. The question "
              "is whether any other points are."),
        ("box", "Finding invariant points", [
            "Solve M(x, y)ᵀ = (x, y)ᵀ, i.e. ax + by = x and cx + dy = y, which is (M − I)(x, y)ᵀ = 0.",
            "If det(M − I) ≠ 0, the only invariant point is the origin.",
            "If det(M − I) = 0 (and M ≠ I), the two equations are the same line through O: every point of that line is invariant. "
            "It is a <b>line of invariant points</b>.",
            "If M = I, every point is invariant.",
        ]),
        ("p", "Example: for M = (3 −2; 1 0) the equations are 3x − 2y = x and x = y. Both say y = x, so every point on y = x is "
              "invariant (check: M(1, 1)ᵀ = (1, 1)ᵀ). For M = (2 1; 1 3), det(M − I) = det(1 1; 1 2) = 1 ≠ 0, so only O is invariant."),
        ("h2", "7.2 Invariant lines and lines of invariant points"),
        ("p", "A line L is an <b>invariant line</b> if every point of L is mapped to a point of L (possibly a different one). The line "
              "as a whole is unchanged, but its points may slide along it. A <b>line of invariant points</b> is stronger: each "
              "individual point stays where it is. OCR A (4.03g) asks you to explain this difference."),
        ("box", "The difference", [
            "Line of invariant points: for every point P on L, MP = P. (Each point is fixed.)",
            "Invariant line: for every point P on L, MP is on L. (The line is fixed as a set.)",
            "Every line of invariant points is an invariant line, but not conversely. Under the enlargement (2 0; 0 2), the line "
            "y = x is invariant, yet (1, 1) moves to (2, 2).",
            "An invariant line need not pass through O (see Section 7.4).",
        ]),
        ("h2", "7.3 Invariant lines through the origin"),
        ("p", "A line through O (other than the y-axis) is y = mx. Take a general point (x, mx) and require its image to lie on the "
              "same line. The image is (ax + bmx, cx + dmx), so we need cx + dmx = m(ax + bmx) for all x. Dividing by x and "
              "rearranging gives a quadratic in m."),
        ("box", "Invariant lines y = mx of M = (a b; c d)", [
            "Condition: bm² + (a − d)m − c = 0. Each real root m gives an invariant line y = mx.",
            "Check the y-axis (x = 0) separately: its image (by, dy) stays on x = 0 exactly when b = 0.",
            "No real roots (and b ≠ 0): there are no invariant lines through O, e.g. a rotation through 90°.",
            "If the condition holds for every m (b = c = 0, a = d), every line through O is invariant: an enlargement.",
            "Then test whether an invariant line is also a line of invariant points: find the image of one point, e.g. (1, m).",
        ]),
        ("p", "In the language of Unit B12, an invariant line through O is a line in the direction of an <b>eigenvector</b>: M(1, m)ᵀ = "
              "λ(1, m)ᵀ, and λ is the factor by which points on that line are scaled. It is a line of invariant points exactly when "
              "λ = 1. If λ = −1 the line is invariant but each point is sent to the opposite side of O."),
        ("h2", "7.4 Invariant lines not through the origin"),
        ("p", "For a general line y = mx + k, take the point (x, mx + k), find its image (X, Y) in terms of x, and require "
              "Y = mX + k for <b>all</b> x. Comparing the coefficients of x and the constant terms gives two equations for m and k. "
              "Lines x = h (parallel to the y-axis) are checked separately: the image must have X = h for every y."),
        ("p", "For example, the shear (1 3; 0 1) maps (x, k) to (x + 3k, k), which is again on y = k. So every line y = k is "
              "invariant, while only y = 0 is a line of invariant points. Every line parallel to the direction of a shear is invariant."),
        ("h2", "7.5 Standard transformations"),
        ("table", ["Transformation", "Invariant points", "Invariant lines"], [
            ["Reflection in a line L through O", "every point of L", "L, and every line perpendicular to L"],
            ["Rotation about O through θ, 0 < θ < 360°, θ ≠ 180°", "O only", "none"],
            ["Rotation through 180° about O", "O only", "every line through O"],
            ["Enlargement, centre O, scale factor k ≠ 1", "O only", "every line through O"],
            ["Stretch parallel to the x-axis, (k 0; 0 1), k ≠ 1", "every point of the y-axis", "the y-axis, and every line y = c"],
            ["Shear with the x-axis fixed, (1 k; 0 1), k ≠ 0", "every point of the x-axis", "every line y = c"],
        ]),
        ("p", "Each entry can be checked by the methods above, and is worth picturing: in a reflection, a line perpendicular to the "
              "mirror is mapped onto itself with its two halves swapped, but only the point where it meets the mirror stays fixed."),
        ("figure", "pa07_reflection.png", "Reflection in y = 2x. The mirror line is a line of invariant points. The perpendicular "
                   "lines y = −½x + k are invariant lines: P on such a line is mapped to P′ on the same line.", 90),
        ("h2", "7.6 In three dimensions (looking ahead)"),
        ("p", "OCR A and MEI restrict this topic to 2-D. The same idea works in 3-D: invariant points solve (M − I)x = 0. The axis of a "
              "3-D rotation is a line of invariant points, and the mirror plane of a reflection is a plane of invariant points. "
              "Unit B12 uses eigenvectors to find such axes and planes."),
        ("warn", "Common mistakes", [
            "Calling a line “invariant” after checking only that its direction is preserved: y = mx + k is invariant only if the "
            "image of each point satisfies the same equation, constant term included.",
            "Confusing an invariant line with a line of invariant points. State which one you have found, and check with one point.",
            "Dividing by x (or by k) without noting x ≠ 0, or forgetting to test the vertical line x = 0 (or x = h).",
            "Using the condition “Y = mX” for lines not through O. For y = mx + k you need Y = mX + k for every x.",
            "Treating the identity as having no invariant points: every point is invariant under I.",
        ]),
    ],
    "examples": [
        {
            "title": "Invariant points",
            "question": "Find the invariant points of (a) M = (3 −2; 1 0) (b) N = (1 2; 3 1).",
            "steps": [
                "(a) Solve 3x − 2y = x and x + 0y = y. The first gives 2x = 2y, the second x = y. Same equation, so the invariant points "
                "form the line y = x (a line of invariant points). Check: M(2, 2)ᵀ = (6 − 4, 2)ᵀ = (2, 2)ᵀ.",
                "(b) x + 2y = x gives y = 0; 3x + y = y gives x = 0. Only the origin is invariant. "
                "Equivalently det(N − I) = det(0 2; 3 0) = −6 ≠ 0.",
            ],
        },
        {
            "title": "Invariant lines through the origin",
            "question": "Find the invariant lines through the origin of M = (3 2; 1 4). Is either of them a line of invariant points?",
            "steps": [
                "The image of (x, mx) is (3x + 2mx, x + 4mx). For it to lie on y = mx: x + 4mx = m(3x + 2mx).",
                "Divide by x (x ≠ 0): 1 + 4m = 3m + 2m², so 2m² − m − 1 = 0, (2m + 1)(m − 1) = 0, m = 1 or m = −½.",
                "Check x = 0: (0, 1) ↦ (2, 4), not on x = 0. So the invariant lines through O are y = x and y = −½x.",
                "(1, 1) ↦ (5, 5): points on y = x are moved (scaled by 5). (2, −1) ↦ (4, −2): points on y = −½x are scaled by 2. "
                "Neither is a line of invariant points. (Also det(M − I) = det(2 2; 1 3) = 4 ≠ 0, so O is the only invariant point.)",
            ],
        },
        {
            "title": "All the invariant lines of a matrix",
            "question": "M = (2 1; 0 1). (a) Find the invariant points of M. (b) Find all the invariant lines of M.",
            "steps": [
                "(a) 2x + y = x and y = y. So x + y = 0: every point of y = −x is invariant.",
                "(b) Take a point (x, mx + k) on y = mx + k. Its image is (2x + mx + k, mx + k).",
                "We need mx + k = m(2x + mx + k) + k for all x, i.e. mx + k = (2m + m²)x + mk + k.",
                "Coefficients of x: m = 2m + m², so m² + m = 0, m = 0 or m = −1. Constants: k = mk + k, so mk = 0.",
                "If m = 0, k can be anything: every horizontal line y = k is invariant. If m = −1, then k = 0: the line y = −x.",
                "Vertical lines x = h: (h, y) ↦ (2h + y, y), whose x-coordinate changes with y, so none is invariant.",
                "Answer: the line y = −x (a line of invariant points) and every line y = k (invariant lines; on y = k the point "
                "(x, k) moves to (2x + k, k), so only the point where y = k meets y = −x is fixed).",
            ],
            "figure": "pa07_lines.png",
            "caption": "M = (2 1; 0 1): the line of invariant points y = −x (solid) and the invariant lines y = k (dashed). "
                       "Arrows show points sliding along their own line.",
            "width_mm": 90,
        },
        {
            "title": "A reflection and its invariant lines",
            "question": "(a) Find the matrix M of the reflection in the line y = 2x. (b) Verify that y = 2x is a line of invariant "
                        "points. (c) Show that every line y = −½x + k is an invariant line.",
            "steps": [
                "(a) tan θ = 2, so cos 2θ = (1 − tan²θ)/(1 + tan²θ) = −3/5 and sin 2θ = 2 tan θ/(1 + tan²θ) = 4/5. "
                "M = (−3/5  4/5; 4/5  3/5).",
                "(b) M(1, 2)ᵀ = (−3/5 + 8/5, 4/5 + 6/5)ᵀ = (1, 2)ᵀ, so (1, 2), and hence every point t(1, 2) of y = 2x, is fixed.",
                "(c) The image of (x, −½x + k) is X = −⅗x + ⅘(−½x + k) = −x + ⅘k and Y = ⅘x + ⅗(−½x + k) = ½x + ⅗k.",
                "Then −½X + k = ½x − ⅖k + k = ½x + ⅗k = Y. So the image lies on y = −½x + k: the line is invariant.",
            ],
        },
        {
            "title": "An unknown entry",
            "question": "M = (1 a; 3 2). The line y = 2x is invariant under M. (a) Find a. (b) Find the other invariant line through O. "
                        "(c) Show that O is the only invariant point.",
            "steps": [
                "(a) M(1, 2)ᵀ = (1 + 2a, 7)ᵀ must lie on y = 2x: 7 = 2(1 + 2a), so a = 5/4.",
                "(b) bm² + (a − d)m − c = 0 with b = 5/4, a = 1, d = 2, c = 3: (5/4)m² − m − 3 = 0, so 5m² − 4m − 12 = 0, "
                "(m − 2)(5m + 6) = 0. The other line is y = −(6/5)x. (b ≠ 0, so x = 0 is not invariant.)",
                "(c) det(M − I) = det(0  5/4; 3  1) = 0 − 15/4 ≠ 0, so only O is invariant.",
            ],
        },
    ],
    "practice": [
        "Find the invariant points of (a) (4 −3; 1 0) (b) (2 1; 3 4) (c) (1 2; 3 1).",
        "Find the value of k for which (k 2; 3 4) has a line of invariant points, and find that line.",
        "Find the invariant lines through the origin of (a) (4 1; 2 3) (b) (5 −2; 3 0).",
        "Show that the rotation (0 −1; 1 0) has no invariant lines through the origin.",
        "Explain why every line through O is invariant under (3 0; 0 3), and find all its invariant points.",
        "M = (1 0; 3 1). Show that x = 0 is a line of invariant points and that every line x = c is an invariant line.",
        "Find all the invariant lines of the stretch (3 0; 0 1), stating which consist of invariant points.",
        "Find all the invariant lines of the reflection in y = x.",
        "M = (3 4; 4 −3). (a) Find the invariant lines through O. (b) Show that no line y = ½x + k with k ≠ 0 is invariant. "
        "(c) Describe M geometrically as a combination of two standard transformations.",
        "Show that every line with gradient 1 is invariant under (1 1; 0 2), and find the line of invariant points.",
        "M = (1 4; 1 1). Find the invariant lines through O and, for each, the image of a general point (t, mt). Is either a line "
        "of invariant points?",
    ],
    "answers": [
        "(a) 3x − 3y = 0: the line y = x. (b) x + y = 0: the line y = −x. (c) det(M − I) = −6 ≠ 0: only O.",
        "det(M − I) = 3(k − 1) − 6 = 0 gives k = 3; then 2x + 2y = 0: the line y = −x.",
        "(a) m² + m − 2 = 0: y = x and y = −2x. (b) −2m² + 5m − 3 = 0, i.e. 2m² − 5m + 3 = 0: y = x and y = 1.5x. "
        "(b ≠ 0 in both, so x = 0 is not invariant.)",
        "bm² + (a − d)m − c = −m² − 1 = 0 has no real roots, and b = −1 ≠ 0 so x = 0 is not invariant either.",
        "(x, mx) ↦ (3x, 3mx), which is on y = mx; (0, y) ↦ (0, 3y). det(M − I) = 4 ≠ 0, so O is the only invariant point.",
        "(0, y) ↦ (0, y), so x = 0 is a line of invariant points; (c, y) ↦ (c, 3c + y), which still has x = c.",
        "x = 0 (line of invariant points) and every line y = k (invariant; (x, k) ↦ (3x, k)). No other lines: y = mx + k needs "
        "mx + k = 3mx + k, so m = 0, and x = h needs 3h = h, so h = 0.",
        "M = (0 1; 1 0). y = x is a line of invariant points; every line y = −x + k is invariant ((x, k − x) ↦ (k − x, x)).",
        "(a) 4m² + 6m − 4 = 0, (2m − 1)(m + 2) = 0: y = ½x (points scaled by 5) and y = −2x (points scaled by −5). "
        "(b) (x, ½x + k) ↦ (5x + 4k, 2.5x − 3k); need 2.5x − 3k = ½(5x + 4k) + k = 2.5x + 3k, so k = 0. "
        "(c) M = 5(⅗ ⅘; ⅘ −⅗): reflection in y = ½x (tan θ = ½ gives cos 2θ = ⅗, sin 2θ = ⅘) combined with an "
        "enlargement, centre O, scale factor 5 (in either order).",
        "(x, x + k) ↦ (2x + k, 2x + 2k), and (2x + 2k) − (2x + k) = k, so the image is on y = x + k. Invariant points: "
        "x + y = x and 2y = y give y = 0: the x-axis.",
        "4m² − 1 = 0: y = ½x and y = −½x. (t, ½t) ↦ (3t, 1.5t) = 3(t, ½t); (t, −½t) ↦ (−t, ½t) = −(t, −½t). Neither is a "
        "line of invariant points (the factors are 3 and −1, not 1).",
    ],
    "exam": [
        "M = (5 −2; 1 2).\n"
        "(a) Show that the origin is the only invariant point of M. [2]\n"
        "(b) Find the equations of the invariant lines of M that pass through the origin. [4]\n"
        "(c) Show that the line y = x + 1 is not invariant, and find the equation of its image under M. [3]",
        "M = (0.6 0.8; 0.8 −0.6).\n"
        "(a) Show that M² = I and explain what this suggests about the transformation. [2]\n"
        "(b) Find the line of invariant points of M, and hence describe M fully. [3]\n"
        "(c) Show that every line of the form y = −2x + c is an invariant line. [3]\n"
        "(d) Explain the difference between an invariant line and a line of invariant points, referring to your answers. [2]",
        "M = (1 2; p 3), where p is a constant. The line y = 2x is an invariant line of M.\n"
        "(a) Find p. [2]\n"
        "(b) Find the equation of the other invariant line of M through the origin. [3]\n"
        "(c) Determine whether either of these lines is a line of invariant points. [2]\n"
        "(d) Show that M has no invariant lines that do not pass through the origin. [4]",
    ],
    "exam_answers": [
        "(a) (M − I)(x, y)ᵀ = 0: 4x − 2y = 0 and x + y = 0 (M1), which meet only at O (det(M − I) = 6 ≠ 0). A1\n"
        "(b) (x, mx) ↦ (5x − 2mx, x + 2mx) (M1); x + 2mx = m(5x − 2mx) gives 2m² − 3m + 1 = 0 (A1), m = 1 or ½ (A1). "
        "b ≠ 0 so x = 0 is not invariant: y = x and y = ½x. A1\n"
        "(c) (x, x + 1) ↦ (3x − 2, 3x + 2) (M1). Then Y = X + 4, so the image is the line y = x + 4 (A1), which is not "
        "y = x + 1: the line is not invariant (it is mapped to a parallel line). A1",
        "(a) M² = (0.36 + 0.64\u00a0\u00a00; 0\u00a0\u00a00.64 + 0.36) = I (B1); doing M twice returns every point, which suggests a reflection. B1\n"
        "(b) −0.4x + 0.8y = 0 and 0.8x − 1.6y = 0 both give y = ½x (M1 A1). M is the reflection in the line y = ½x. A1\n"
        "(c) (x, −2x + c) ↦ (0.6x − 1.6x + 0.8c, 0.8x + 1.2x − 0.6c) = (−x + 0.8c, 2x − 0.6c) (M1 A1). "
        "−2X + c = 2x − 1.6c + c = 2x − 0.6c = Y, so the image is on the same line. A1\n"
        "(d) On y = ½x every point is fixed (line of invariant points). On y = −2x + c the line maps to itself but points move: "
        "e.g. (0, c) ↦ (0.8c, −0.6c); only the point on the mirror stays put. B1 B1",
        "(a) M(1, 2)ᵀ = (5, p + 6)ᵀ must be on y = 2x (M1): p + 6 = 10, p = 4. A1\n"
        "(b) bm² + (a − d)m − c = 2m² − 2m − 4 = 0 (M1), m² − m − 2 = 0, m = 2 or −1 (A1): the other line is y = −x. A1\n"
        "(c) (1, 2) ↦ (5, 10) and (1, −1) ↦ (−1, 1): points move on both lines, so neither is a line of invariant points. B1 B1\n"
        "(d) Lines of the form y = mx + k need the direction preserved, so m = 2 or −1 (M1). (x, 2x + k) ↦ (5x + 2k, 10x + 3k); "
        "need 10x + 3k = 2(5x + 2k) + k, so k = 0 (A1). (x, −x + k) ↦ (−x + 2k, x + 3k); need x + 3k = x − 2k + k, so k = 0 "
        "(A1). Vertical lines x = h: (h, y) ↦ (h + 2y, 4h + 3y), whose x-coordinate varies, so none. Hence no invariant lines "
        "avoid O. A1",
    ],
}
