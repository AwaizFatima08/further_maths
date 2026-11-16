UNIT = {
    "number": "C6",
    "title": "Further complex numbers: loci and transformations",
    "tag": "Option · Edexcel FP2 4.1, 4.2 (A level); AS FP2 3.1 (loci and regions only) · IAL FP2 3.3, 3.4 · "
           "not on AQA, OCR A, OCR MEI (excluded by Pj11) or CAIE · builds on A2 and B1",
    "notes": [
        ("p", "Unit A2 met three basic loci: circles |z − a| = r, perpendicular bisectors |z − a| = |z − b| and half-lines "
              "arg(z − a) = θ. This unit adds two more: the circle |z − a| = k|z − b| and the arc arg((z − a)/(z − b)) = β. It "
              "then studies <b>transformations</b> w = f(z), which map a locus in the z-plane to a locus in a second Argand "
              "diagram, the w-plane. Edexcel AS Further Pure 2 needs sections 6.1–6.4 only."),

        ("h2", "6.1 Review: the basic loci (IAL FP2 3.3)"),
        ("p", "IAL FP2 students meet loci for the first time here, so revise Unit A2 sections 2.6–2.8 first. The key idea is "
              "unchanged: |z − a| is the distance from z to a, and arg(z − a) is the direction of the line from a to z. "
              "Throughout, write z = x + iy to turn a locus into a Cartesian equation, and write w = u + iv in the w-plane."),

        ("h2", "6.2 The circle |z − a| = k|z − b| (Edexcel FP2 4.1, AS FP2 3.1; IAL FP2 3.3)"),
        ("p", "This locus is the set of points whose distance from a is k times their distance from b. When k = 1 it is the "
              "perpendicular bisector of a and b. When k ≠ 1 (k > 0) it is a <b>circle</b>, called a circle of Apollonius. To find "
              "it, substitute z = x + iy, square both sides, and complete the square."),
        ("p", "For example, |z + 3| = 2|z| gives (x + 3)² + y² = 4(x² + y²), so 3x² + 3y² − 6x − 9 = 0, i.e. "
              "x² + y² − 2x − 3 = 0, or (x − 1)² + y² = 4: a circle with centre 1 and radius 2."),
        ("box", "Facts about |z − a| = k|z − b|, k > 0, k ≠ 1", [
            "It is a circle. Its centre lies on the line through a and b, but it is <b>not</b> the midpoint, and in general "
            "neither a nor b is the centre.",
            "Check formula (not on any specification): centre (a − k²b)/(1 − k²), radius k|a − b|/|1 − k²|.",
            "The circle crosses the line through a and b at the two points dividing the segment from a to b internally and "
            "externally in the ratio k : 1; these are quick checks on your answer.",
            "Regions: |z − a| < k|z − b| is one side of the circle. Test a convenient point, such as a itself: |a − a| = 0 < "
            "k|a − b|, so a always lies in the region |z − a| < k|z − b|.",
        ]),
        ("figure", "pc06_apollonius.png",
         "|z + 3| = 2|z| is the circle centre 1, radius 2. At z = 1 + 2i, for example, the distance to −3 (√20) is twice "
         "the distance to 0 (√5).", 90),

        ("h2", "6.3 The arc arg((z − a)/(z − b)) = β (Edexcel FP2 4.1, AS FP2 3.1; IAL FP2 3.3)"),
        ("p", "By the argument rules, arg((z − a)/(z − b)) = arg(z − a) − arg(z − b). This is the angle at z between the "
              "lines joining z to b and to a, measured anticlockwise from the direction of z − b to the direction of z − a. So the "
              "locus is the set of points from which the segment AB subtends a fixed angle β, where A and B represent a and b. "
              "By the circle theorem “angles in the same segment are equal”, the locus is an <b>arc of a circle</b> through A "
              "and B, with A and B themselves excluded."),
        ("box", "Sketching arg((z − a)/(z − b)) = β, with 0 < β < π", [
            "Draw the chord from B (the point b) to A (the point a). The arc lies on the <b>left</b> of the direction from B to A. "
            "(For −π < β < 0 it lies on the right.)",
            "β = π/2: a semicircle on diameter AB. β < π/2: a major arc (more than a semicircle). β > π/2: a minor arc.",
            "The radius is R = |a − b|/(2 sin β) (sine rule), and the centre is on the perpendicular bisector of AB.",
            "β = 0 gives the line through A and B outside the segment AB; β = π gives the segment AB itself (both without the "
            "end points).",
        ]),
        ("p", "<b>Cartesian method.</b> Write (z − a)/(z − b) in the form X + iY by multiplying top and bottom by the conjugate of "
              "the denominator. Then arg = β means Y/X = tan β with X and Y having the signs that put the argument in the "
              "correct quadrant. For β = π/2 the condition is simply X = 0 with Y > 0."),
        ("figure", "pc06_arcs.png",
         "arg((z − 1)/(z + 1)) = β for β = π/4 (major arc), π/2 (semicircle) and 3π/4 (minor arc). Each arc lies above the real "
         "axis, to the left of the direction from −1 to 1. The end points ±1 are excluded.", 95),

        ("h2", "6.4 Further regions (Edexcel FP2 4.1, AS FP2 3.1; IAL FP2 3.3)"),
        ("bullets", [
            "α ≤ arg(z − z₁) ≤ β: the region between two half-lines from z₁ (z₁ itself excluded).",
            "p ≤ Re(z) ≤ q: a vertical strip; p ≤ Im(z) ≤ q: a horizontal strip.",
            "|z − a| ≤ k|z − b|: inside or outside an Apollonius circle (test a point).",
            "β ≤ arg((z − a)/(z − b)) < π (0 < β < π): the region enclosed by the arc and the chord AB. Points inside the circle "
            "on the arc's side see AB at an angle bigger than β, and points outside it see AB at a smaller angle. So "
            "0 < arg((z − a)/(z − b)) < β is the part of that side of the line AB lying outside the circle. Check with a test "
            "point.",
            "As in Unit A2, use solid lines for included boundaries, dashed lines for excluded ones, and shade the required "
            "region.",
        ]),

        ("h2", "6.5 Transformations from the z-plane to the w-plane (Edexcel FP2 4.2; IAL FP2 3.4)"),
        ("p", "A function w = f(z) sends each point z of one Argand diagram (the z-plane) to a point w of another (the w-plane). "
              "To find the image of a locus, use this standard method:"),
        ("box", "Finding the image of a locus under w = f(z)", [
            "1. Rearrange to make z the subject: z = g(w).",
            "2. Substitute into the equation of the z-locus.",
            "3. Simplify, using |p/q| = |p|/|q| for moduli, or write w = u + iv and find the Cartesian equation.",
            "4. Describe the image, and say which points (if any) are missed or excluded.",
        ]),
        ("table", ["Transformation", "Geometric meaning", "Lines and circles map to"], [
            ["w = z + b", "translation by b", "lines and circles of the same size"],
            ["w = kz, k > 0 real", "enlargement, factor k, centre O", "lines; circles with radius × k"],
            ["w = az, a = re<sup>iα</sup>", "enlargement factor r with rotation α, about O (Unit B1)", "lines; circles with radius × r"],
            ["w = az + b", "the above, then translation by b", "lines; circles"],
            ["w = 1/z", "inversion in the unit circle combined with reflection in the real axis",
             "circles and lines, but a circle or line through O becomes a line, and one not through O becomes a circle"],
            ["w = z²", "squares the modulus and doubles the argument", "a line not through O becomes a parabola; |z| = r → |w| = r²"],
        ]),
        ("p", "<b>Möbius transformations.</b> w = (az + b)/(cz + d), with ad − bc ≠ 0, map circles and lines to circles and lines. "
              "The point z = −d/c has no image, and w = a/c is never reached. A circle or line through z = −d/c maps to a "
              "straight line; every other circle or line maps to a circle. Knowing this tells you in advance what kind of answer "
              "to expect."),
        ("p", "<b>Useful shortcut.</b> When the rearranged z-locus has the form |w − p| = k|w − q|, read the image straight from "
              "section 6.2: a perpendicular bisector if k = 1, a circle otherwise. For example, under w = 1/z the circle "
              "|z − 1| = 1 becomes |1/w − 1| = 1, i.e. |1 − w| = |w|, the line Re(w) = ½."),

        ("h2", "6.6 Images of regions and of w = z² (Edexcel FP2 4.2; IAL FP2 3.4)"),
        ("p", "To find the image of a region, find the image of its boundary, then test one interior point to see which side of "
              "the image boundary is the image region. For w = z², write z = re<sup>iθ</sup>, so w = r²e<sup>2iθ</sup>: the "
              "sector |z| ≤ r, α ≤ arg z ≤ β maps to the sector |w| ≤ r², 2α ≤ arg w ≤ 2β. For a line such as Re(z) = 1, use "
              "z = 1 + iy, so w = (1 − y²) + 2iy, i.e. u = 1 − y², v = 2y. Eliminating y gives u = 1 − v²/4, a parabola. "
              "Note that z and −z have the same image, so w = z² is two-to-one (except at 0)."),
        ("figure", "pc06_zsquared.png",
         "Under w = z², the line Re(z) = 1 (left) maps to the parabola u = 1 − v²/4 (right), and the quarter disc |z| ≤ 1, "
         "0 ≤ arg z ≤ π/2 maps to the half disc |w| ≤ 1, 0 ≤ arg w ≤ π.", 150),

        ("warn", "Common mistakes", [
            "Assuming the centre of |z − a| = k|z − b| is a or b, or the midpoint of ab. Complete the square every time.",
            "Forgetting to divide by the coefficient of x² before completing the square.",
            "Drawing the full circle for an arg((z − a)/(z − b)) locus. It is one arc only, without its end points.",
            "Putting the arc on the wrong side. Use a test point, or the rule “left of the direction from b to a when β > 0”.",
            "In transformations, substituting z = f(w) instead of rearranging for z first.",
            "Leaving an image as an unsimplified equation. Give the centre and radius of a circle, or the equation of a line, and "
            "state any excluded point.",
            "For a region, transforming only the boundary and shading the wrong side. Always test a point.",
        ]),
        ("box", "Given or learn? (formula booklets)", [
            "Nothing in this unit is printed in the Edexcel or IAL booklets. Learn the methods: square both sides for "
            "|z − a| = k|z − b|, use circle theorems for the arc, and rearrange for z for transformations.",
        ]),
    ],
    "examples": [
        {
            "title": "An Apollonius circle and its region",
            "question": "(a) Show that the locus |z + 3| = 2|z| is a circle, and find its centre and radius.\n(b) Shade the region "
                        "|z + 3| ≥ 2|z|.",
            "figure": "pc06_apollonius.png", "caption": "The region |z + 3| ≥ 2|z| is the disc (boundary included).",
            "width_mm": 80,
            "steps": [
                "(a) |x + 3 + iy|² = 4|x + iy|² ⇒ (x + 3)² + y² = 4x² + 4y².",
                "⇒ 3x² + 3y² − 6x − 9 = 0 ⇒ x² + y² − 2x − 3 = 0 ⇒ (x − 1)² + y² = 4.",
                "A circle with centre 1 (the point (1, 0)) and radius 2.",
                "Checks: z = 3 gives |6| = 2 × 3 and z = −1 gives |2| = 2 × 1, the two points where the circle meets the real axis.",
                "(b) Test z = 1: |4| = 4 ≥ 2|1| = 2, true. So the region is the disc (x − 1)² + y² ≤ 4, drawn with a solid "
                "boundary.",
            ],
        },
        {
            "title": "An arc: arg((z − 1)/(z + 1)) = π/4",
            "question": "Sketch the locus arg((z − 1)/(z + 1)) = π/4 and find the Cartesian equation of the circle on which it lies.",
            "figure": "pc06_arcs.png", "caption": "The outer arc is β = π/4.", "width_mm": 80,
            "steps": [
                "Geometry: the chord joins −1 to 1. β = π/4 > 0, so the arc lies to the left of the direction from −1 to 1, i.e. "
                "above the real axis. β < π/2, so it is a major arc.",
                "Radius R = |1 − (−1)|/(2 sin(π/4)) = 2/√2 = √2. The centre is on the imaginary axis at height h with "
                "h² + 1 = 2, so h = 1 (above the chord, since the arc is major).",
                "Algebra: (z − 1)/(z + 1) = (x − 1 + iy)(x + 1 − iy)/|z + 1|² = [(x² + y² − 1) + 2iy]/|z + 1|².",
                "Argument π/4 means real part = imaginary part > 0: x² + y² − 1 = 2y with y > 0.",
                "So the locus is the arc of x² + (y − 1)² = 2, centre i, radius √2, with y > 0 (the points ±1 excluded).",
            ],
        },
        {
            "title": "w = 1/z maps a circle through O to a line",
            "question": "Find the image of the circle |z − 1| = 1 under the transformation w = 1/z, z ≠ 0.",
            "steps": [
                "Rearrange: z = 1/w. Substitute: |1/w − 1| = 1 ⇒ |1 − w|/|w| = 1 ⇒ |w − 1| = |w|.",
                "This is the perpendicular bisector of 0 and 1 in the w-plane: the line Re(w) = ½, i.e. u = ½.",
                "This matches section 6.5: the circle passes through O (the point with no image), so its image is a line.",
                "Check: z = 2 is on the circle and w = ½; z = 1 + i is on the circle and w = (1 − i)/2, which has real part ½.",
            ],
        },
        {
            "title": "A Möbius transformation of a circle",
            "question": "T is given by w = (2z + 1)/(z − 1), z ≠ 1. Show that T maps the circle |z| = 2 onto a circle in the "
                        "w-plane, and find its centre and radius.",
            "steps": [
                "Rearrange: w(z − 1) = 2z + 1 ⇒ wz − 2z = w + 1 ⇒ z = (w + 1)/(w − 2).",
                "|z| = 2 ⇒ |w + 1| = 2|w − 2|.",
                "(u + 1)² + v² = 4[(u − 2)² + v²] ⇒ u² + 2u + 1 + v² = 4u² − 16u + 16 + 4v².",
                "⇒ 3u² + 3v² − 18u + 15 = 0 ⇒ u² + v² − 6u + 5 = 0 ⇒ (u − 3)² + v² = 4.",
                "A circle with centre 3 and radius 2. Check: z = 2 → w = 5, and z = −2 → w = 1; both lie on it.",
            ],
        },
        {
            "title": "Images under w = z²",
            "question": "Under w = z², find the image of (a) the half-line arg z = π/3, (b) the circle |z| = 3, (c) the line "
                        "Re(z) = 1.",
            "figure": "pc06_zsquared.png", "caption": "The line Re(z) = 1 and its image, a parabola.", "width_mm": 140,
            "steps": [
                "(a) z = re<sup>iπ/3</sup> ⇒ w = r²e<sup>2iπ/3</sup>: the half-line arg w = 2π/3 (O excluded).",
                "(b) |w| = |z|² = 9: the circle |w| = 9 (each point is reached twice, from z and −z).",
                "(c) z = 1 + iy ⇒ w = 1 + 2iy − y², so u = 1 − y² and v = 2y.",
                "Eliminate y = v/2: u = 1 − v²/4, a parabola with vertex at w = 1, opening towards negative u.",
            ],
        },
        {
            "title": "A line mapped to a circle, and the image of a half-plane",
            "question": "T is given by w = z/(z + i), z ≠ −i.\n(a) Show that the real axis in the z-plane maps to a circle C, and "
                        "find its centre and radius.\n(b) Find the image of the region Im(z) > 0.",
            "steps": [
                "(a) Rearrange: wz + iw = z ⇒ z(1 − w) = iw ⇒ z = iw/(1 − w).",
                "z is real ⇔ z = z*: iw/(1 − w) = −iw*/(1 − w*).",
                "⇒ iw(1 − w*) = −iw*(1 − w) ⇒ w − ww* = −w* + ww* ⇒ w + w* = 2ww*.",
                "With w = u + iv: 2u = 2(u² + v²) ⇒ u² + v² − u = 0 ⇒ (u − ½)² + v² = ¼.",
                "C is the circle centre ½, radius ½. (The point w = 1 is missed: it would need z = ∞.)",
                "(b) Test z = i: w = i/(2i) = ½, the centre of C. So the upper half-plane maps to the interior of C: "
                "|w − ½| < ½.",
            ],
        },
    ],
    "practice": [
        "Find the Cartesian equation of the locus |z − 2| = 3|z + 2|, and give its centre and radius.",
        "(a) Show that |z − i| = 2|z − 4i| is a circle, and find its centre and radius.\n(b) Describe the region "
        "|z − i| < 2|z − 4i|.",
        "Sketch the locus arg((z − 2i)/(z + 2i)) = π/2 and give its Cartesian equation.",
        "Find the centre and radius of the circle on which the locus arg((z − 3)/(z + 1)) = π/3 lies, and state which part of "
        "the circle is the locus.",
        "Shade the region {z : 1 ≤ Re(z) ≤ 3} ∩ {z : 0 ≤ arg(z − 1) ≤ π/4} and find its area.",
        "Find the image of the circle |z − 1| = 2 under w = 2z + i.",
        "Describe the transformation w = iz + 1 geometrically, and find the image of the line Re(z) = 2.",
        "Find the image of the line Re(z) = 2 under w = 1/z.",
        "Find the image of the circle |z − 2i| = 2 under w = 1/z, z ≠ 0.",
        "Under w = z², find:\n(a) the image of the line Im(z) = 1, as a Cartesian equation in u and v\n(b) the image of "
        "the quarter disc {z : |z| ≤ 2, 0 ≤ arg z ≤ π/2}.",
        "T is given by w = (z − 1)/(z + 1), z ≠ −1. Show that T maps the imaginary axis to the circle |w| = 1, and find the "
        "image of the region Re(z) > 0.",
    ],
    "answers": [
        "(x − 2)² + y² = 9[(x + 2)² + y²] ⇒ 8x² + 8y² + 40x + 32 = 0 ⇒ (x + 5/2)² + y² = 9/4: centre −5/2, radius 3/2.",
        "(a) x² + (y − 1)² = 4[x² + (y − 4)²] ⇒ x² + y² − 10y + 21 = 0 ⇒ x² + (y − 5)² = 4: centre 5i, radius 2. "
        "(b) z = i satisfies it (0 < 6), so it is the region outside the circle (dashed boundary).",
        "β = π/2: semicircle on the diameter from −2i to 2i, on the left of the upward direction: x² + y² = 4 with x < 0.",
        "R = 4/(2 sin(π/3)) = 4/√3; centre 1 + (2/√3)i; the major arc above the real axis (y > 0), ends 3 and −1 excluded. "
        "Equation (x − 1)² + (y − 2/√3)² = 16/3.",
        "The triangle with vertices 1, 3 and 3 + 2i: area ½ × 2 × 2 = 2.",
        "z = (w − i)/2 ⇒ |w − i − 2| = 4: circle centre 2 + i, radius 4.",
        "Rotation through π/2 about O, then translation by 1. z = 2 + iy ⇒ w = (1 − y) + 2i: the line Im(w) = 2.",
        "z = 1/w; Re(1/w) = u/(u² + v²) = 2 ⇒ u² + v² − u/2 = 0 ⇒ (u − ¼)² + v² = 1/16: circle centre ¼, radius ¼ (w = 0 "
        "excluded).",
        "|1/w − 2i| = 2 ⇒ |1 − 2iw| = 2|w|; 1 − 2iw = −2i(w + i/2), so |w + i/2| = |w|: the line Im(w) = −¼.",
        "(a) z = x + i ⇒ u = x² − 1, v = 2x ⇒ u = v²/4 − 1. (b) the half disc |w| ≤ 4, 0 ≤ arg w ≤ π (with 0).",
        "z = iy: |iy − 1| = |iy + 1|, so |w| = 1 (w = 1 is missed). Re(z) > 0 means z is closer to 1 than to −1, so "
        "|z − 1| < |z + 1|, i.e. |w| < 1: the inside of the unit circle.",
    ],
    "exam": [
        "(a) Show that the locus |z − 6| = 2|z − 3i| is a circle, and find its centre and radius. [5]\n(b) Find the greatest "
        "value of |z| for points on this locus. [2]\n(c) Shade the region {z : |z − 6| ≥ 2|z − 3i|} ∩ {z : Re(z) ≥ 0} and "
        "find its area, correct to 3 significant figures. [4]",
        "The locus L is given by arg((z − 3i)/(z + 3)) = π/4.\n(a) Show that L is an arc of a circle, and find the Cartesian "
        "equation, centre and radius of the circle. [6]\n(b) Sketch L. [2]\n(c) Find the exact greatest value of |z| for z "
        "on L. [3]",
        "The transformation T from the z-plane to the w-plane is given by w = (z + 1)/(z − 2), z ≠ 2.\n(a) Show that T maps "
        "the circle |z| = 1 onto a circle C, and find its centre and radius. [5]\n(b) Show that T maps the line Re(z) = ½ "
        "onto the circle |w| = 1. [3]\n(c) Shade on an Argand diagram the image under T of the region "
        "{z : |z| ≤ 1} ∩ {z : Re(z) ≥ ½}. [3]",
        "The transformation T is given by w = z².\n(a) Show that T maps the line x + y = 1 onto the parabola "
        "v = ½(1 − u²). [4]\n(b) Find the point where the half-line arg z = π/4 meets x + y = 1, and verify that its image lies "
        "on the parabola. [2]\n(c) Explain why T is not one-to-one on the whole z-plane. [1]\n(d) Find the image of "
        "{z : |z| ≤ 1, 0 ≤ arg z ≤ π/4} and its area. [3]",
    ],
    "exam_answers": [
        "(a) (x − 6)² + y² = 4[x² + (y − 3)²] [M1]; 3x² + 3y² + 12x − 24y = 0 [A1]; x² + y² + 4x − 8y = 0 [M1]; "
        "(x + 2)² + (y − 4)² = 20 [A1]; centre −2 + 4i, radius 2√5 [A1]. (b) |−2 + 4i| = 2√5 = radius, so the circle passes "
        "through O [M1]; greatest |z| = 2√5 + 2√5 = 4√5 [A1]. (c) z = −2 + 4i satisfies the inequality, so it is the inside of "
        "the circle [B1]; Re(z) = 0 cuts it at 0 and 8i; the segment to the right of the chord has d = 2, r = √20 [M1]; "
        "area = r² arccos(d/r) − d√(r² − d²) = 20 arccos(1/√5) − 8 [M1] = 14.1 [A1].",
        "(a) Angle subtended by the chord from −3 to 3i is π/4, so L is an arc of a circle through −3 and 3i [B1]; "
        "R = |3i + 3|/(2 sin(π/4)) = 3√2/√2 = 3 [M1 A1]; centre on y = −x at distance √(9 − 9/2) = 3/√2 from the midpoint "
        "(−3/2, 3/2), on the arc's side: −3 + 3i [M1 A1]; (x + 3)² + (y − 3)² = 9 [A1]. (b) Major arc from −3 to 3i "
        "(both excluded), on the side away from O [B1 B1]. (c) |−3 + 3i| + 3 [M1]; the farthest point is on L [M1]; "
        "greatest |z| = 3√2 + 3 [A1].",
        "(a) z = (2w + 1)/(w − 1) [M1 A1]; |2w + 1| = |w − 1| [M1]; 4(u² + u) + 1 + 4v² = u² − 2u + 1 + v² ⇒ "
        "3u² + 3v² + 6u = 0 [M1]; (u + 1)² + v² = 1: centre −1, radius 1 [A1]. (b) Re(z) = ½ is the perpendicular bisector "
        "of −1 and 2, so |z + 1| = |z − 2| [M1 A1]; dividing, |w| = 1 [A1]. (c) z = 0 → w = −½, inside C, so |z| ≤ 1 maps to "
        "(u + 1)² + v² ≤ 1 [B1]; z = 1 → w = −2, |w| = 2, so Re(z) ≥ ½ maps to |w| ≥ 1 [B1]; the part of the disc C "
        "outside the unit circle, shaded [B1].",
        "(a) z = x + i(1 − x) [M1]; w = x² − (1 − x)² + 2x(1 − x)i, so u = 2x − 1, v = 2x − 2x² [A1]; x = (u + 1)/2 [M1]; "
        "v = (u + 1)(1 − u)/2 = ½(1 − u²) [A1]. (b) z = ½ + ½i [B1]; w = ½i, and ½(1 − 0) = ½ ✓ [B1]. (c) z and −z have "
        "the same image (for example 1 and −1 both map to 1) [B1]. (d) |w| ≤ 1, 0 ≤ arg w ≤ π/2 [M1 A1]: a quarter disc of "
        "area π/4 [A1].",
    ],
}
