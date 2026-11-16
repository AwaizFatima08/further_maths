UNIT = {
    "number": "A14",
    "title": "Volumes of revolution and the mean value of a function",
    "tag": "Edexcel CP 5.1 (AS: volumes), CP 5.3 (A level: mean value) · AQA E2, E3 (AS) · OCR A 4.08d, 4.08e (A level) · "
           "OCR MEI Pc2, Pc3 (A level) · not in the IAL FP units (volumes are in IAL P4) · not on CAIE 9231",
    "notes": [
        ("h2", "A14.1 Volumes of revolution about the x-axis"),
        ("p", "Take the region under the curve y = f(x) between x = a and x = b and rotate it through 2π radians (one full turn) "
              "about the x-axis. It sweeps out a <b>solid of revolution</b>. Every cross-section of the solid at right angles to "
              "the x-axis is a circle, and the radius of the circle at position x is the height y of the curve there."),
        ("p", "<b>Deriving the formula</b> (AQA E2 asks you to derive it). Cut the region into thin vertical strips of width δx. "
              "When a strip of height y is rotated it gives, very nearly, a thin disc (a cylinder) of radius y and thickness δx, "
              "with volume πy²δx. Adding the discs, V ≈ Σ πy²δx. As δx → 0 the error tends to zero and the sum becomes an "
              "integral (Unit B7 explains why a limit of sums is an integral):"),
        ("box", "Volumes of revolution (learn these: no English booklet prints them)", [
            "About the x-axis: V = π∫ₐᵇ y² dx, with x-limits a and b.",
            "About the y-axis: V = π∫<sub>c</sub><sup>d</sup> x² dy, with y-limits c and d.",
            "Parametric curve x = x(t), y = y(t): about the x-axis V = π∫ y² (dx/dt) dt; about the y-axis V = π∫ x² (dy/dt) dt, "
            "with limits for t.",
            "Region between an outer curve y₁ and an inner curve y₂ (washers): V = π∫ (y₁² − y₂²) dx.",
            "Volumes are in cubic units. Leave π in an exact answer.",
        ]),
        ("figure", "pa14_disc.png", "Rotating a thin strip of height y and width δx about the x-axis gives a disc of volume "
                                    "about πy²δx. The dashed curve is the reflection of the curve, showing the edge of the solid.", 120),
        ("figure", "pa14_solid3d.png", "The solid formed by rotating the region under y = x² + 1, 0 ≤ x ≤ 2, about the x-axis "
                                       "(Worked example A14.1).", 75),
        ("h2", "A14.2 Rotating about the y-axis"),
        ("p", "Rotating about the y-axis works in the same way with the roles of x and y swapped. The region must be bounded by the "
              "curve, the <b>y-axis</b> and two horizontal lines y = c and y = d. Horizontal strips of thickness δy become discs of "
              "radius x, so V = π∫ x² dy. Rearrange the equation to give x² in terms of y, and use y-limits."),
        ("p", "If the region you are given touches the x-axis instead, for example the region under y = ln x from x = 1 to x = e, "
              "find its volume about the y-axis as a <b>cylinder minus a disc volume</b>: the cylinder of radius e and height 1, "
              "minus the solid formed by the region between the curve and the y-axis. No board requires the 'shell' method."),
        ("h2", "A14.3 Regions between two curves and composite solids (all boards; OCR A 4.08d names it)"),
        ("p", "Suppose a region lies between an upper curve y = y₁ and a lower curve y = y₂, with y₁ ≥ y₂ ≥ 0, from x = a to x = b. "
              "Rotating it about the x-axis gives a solid with a hole in it. Each thin strip now sweeps out a <b>washer</b> "
              "(a disc with a hole), with volume π(y₁² − y₂²)δx. So V = π∫ₐᵇ (y₁² − y₂²) dx: the outer volume minus the inner volume."),
        ("bullets", [
            "Find the limits first, by solving y₁ = y₂ for the points of intersection.",
            "Square each function separately: y₁² − y₂² is <b>not</b> (y₁ − y₂)².",
            "The method needs the whole region on one side of the axis of rotation. If part of the region is below the x-axis, "
            "sketch it and split it, because only the distance from the axis matters.",
            "Where a boundary is a straight line through the origin or parallel to an axis, the solid it makes is a cone or a "
            "cylinder. You may use V = ⅓πr²h or V = πr²h instead of integrating.",
        ]),
        ("h2", "A14.4 Parametric curves (Edexcel A level, OCR A 4.08d)"),
        ("p", "If the curve is given by x = x(t), y = y(t), substitute dx = (dx/dt) dt in V = π∫ y² dx. Then V = π∫ y² (dx/dt) dt, "
              "where the limits are the values of t at the two ends of the region. Work out which t gives which end. If x decreases "
              "as t increases, then dx/dt < 0, so put the t-value for the left-hand end at the bottom of the integral, even if it is "
              "the larger value. Your answer must come out positive."),
        ("h2", "A14.5 Modelling with volumes of revolution"),
        ("p", "Many containers are solids of revolution: bowls, vases, glasses, barrels and nose cones. Choose the axis of symmetry "
              "as the axis of rotation, state the units, and say what the model ignores (the thickness of the walls, a base that is "
              "not exactly the shape of the curve, measurement error). For a container standing on the y-axis, the volume of liquid "
              "when it is filled to depth h is V(h) = π∫₀ʰ x² dy. Setting V(h) equal to a given volume gives an equation for h."),
        ("h2", "A14.6 The mean value of a function (Edexcel A level, AQA AS, OCR A, MEI)"),
        ("box", "Mean value of f(x) over a ≤ x ≤ b", [
            "f̄ = (1/(b − a)) ∫ₐᵇ f(x) dx.",
            "Geometric meaning: a rectangle of width b − a and height f̄ has the same (signed) area as the region under y = f(x).",
            "Rules: the mean value of f(x) + k is f̄ + k; the mean value of kf(x) is kf̄; the mean value of f(x) + g(x) is f̄ + ḡ.",
            "Given in the OCR A and MEI booklets; Edexcel and AQA students must learn it.",
        ]),
        ("p", "The mean value is the continuous version of an average. Think of sampling f at n equally spaced points: their average "
              "is (1/n)Σf(xᵢ) = (1/(b − a)) Σ f(xᵢ)δx, and as n → ∞ this tends to the integral formula. It is <b>not</b> the average "
              "of the end values ½(f(a) + f(b)), unless f is linear. Parts of the curve below the x-axis count negatively, so a mean "
              "value can be negative or zero: the mean value of sin x over 0 ≤ x ≤ 2π is 0. For a continuous function there is at "
              "least one point c in the interval where f(c) = f̄."),
        ("p", "The variable matters. The mean speed of a car with respect to time, (1/T)∫v dt, is the distance travelled divided by the "
              "time taken. A mean taken with respect to distance would be a different number. Always say which variable the mean is "
              "taken over."),
        ("h2", "A14.7 Given or learn: formulae by board"),
        ("table", ["Formula", "Edexcel 9FM0/8FM0", "AQA", "OCR A", "OCR MEI"], [
            ["Volume about either axis", "learn (Appendix 1)", "learn (Appendix B)", "learn", "learn"],
            ["Mean value", "learn", "learn", "given in booklet", "given in booklet"],
            ["Stage", "volumes AS; mean value A level", "both AS", "both A level", "both A level"],
        ]),
        ("warn", "Common mistakes", [
            "Leaving out π, or squaring after integrating: V = π∫y² dx, so square y first, then integrate.",
            "Squaring term by term: (x² + 1)² = x⁴ + 2x² + 1, not x⁴ + 1.",
            "About the y-axis: using x-limits, or integrating x instead of x². Rearrange to x² = g(y) and use y-limits.",
            "Washers: writing π∫(y₁ − y₂)² dx. The correct integrand is y₁² − y₂².",
            "Parametric volumes: forgetting the factor dx/dt, or leaving the limits as x-values.",
            "Mean value: dividing by b instead of b − a, or by the wrong interval when the interval does not start at 0.",
        ]),
    ],
    "examples": [
        {
            "title": "Volume about the x-axis",
            "question": "The region R is bounded by the curve y = x² + 1, the x-axis, the y-axis and the line x = 2. R is rotated "
                        "through 2π radians about the x-axis. Find the exact volume of the solid generated.",
            "steps": [
                "V = π∫₀² y² dx = π∫₀² (x² + 1)² dx.",
                "Expand before integrating: (x² + 1)² = x⁴ + 2x² + 1.",
                "V = π[x⁵/5 + 2x³/3 + x]₀² = π(32/5 + 16/3 + 2).",
                "= π(96 + 80 + 30)/15 = <b>206π/15</b> cubic units (≈ 43.1).",
            ],
        },
        {
            "title": "Volume about the y-axis, and a cylinder minus a disc volume",
            "question": "(a) The region bounded by the curve y = ln x, the y-axis, the x-axis and the line y = 2 is rotated through "
                        "2π about the y-axis. Find the exact volume generated.\n"
                        "(b) The region bounded by y = ln x, the x-axis and the line x = e is rotated through 2π about the y-axis. "
                        "Find the exact volume generated.",
            "steps": [
                "(a) Rearrange: y = ln x gives x = eʸ, so x² = e²ʸ. The region runs from y = 0 to y = 2.",
                "V = π∫₀² e²ʸ dy = π[½e²ʸ]₀² = <b>½π(e⁴ − 1)</b> (≈ 84.2).",
                "(b) This region lies between the curve and the line x = e, for 0 ≤ y ≤ 1. Rotating the rectangle 0 ≤ x ≤ e, 0 ≤ y ≤ 1 "
                "gives a cylinder of radius e and height 1, volume πe².",
                "Remove the solid made by the region between the y-axis and the curve for 0 ≤ y ≤ 1: π∫₀¹ e²ʸ dy = ½π(e² − 1).",
                "V = πe² − ½π(e² − 1) = <b>½π(e² + 1)</b> (≈ 13.2).",
            ],
        },
        {
            "title": "The region between two curves",
            "question": "The finite region R is bounded by the curve y = 3x − x² and the line y = x. Find the exact volume of the "
                        "solid formed when R is rotated through 2π about the x-axis.",
            "figure": "pa14_washer.png",
            "caption": "R lies between the parabola (outer radius y₁ = 3x − x²) and the line (inner radius y₂ = x) for 0 ≤ x ≤ 2.",
            "width_mm": 85,
            "steps": [
                "Intersections: 3x − x² = x gives x² − 2x = 0, so x = 0 or x = 2. On 0 < x < 2 the parabola is above the line "
                "(at x = 1: 2 > 1), and both are above the x-axis.",
                "V = π∫₀² [(3x − x²)² − x²] dx = π∫₀² (9x² − 6x³ + x⁴ − x²) dx = π∫₀² (8x² − 6x³ + x⁴) dx.",
                "= π[8x³/3 − 3x⁴/2 + x⁵/5]₀² = π(64/3 − 24 + 32/5) = π(320 − 360 + 96)/15.",
                "V = <b>56π/15</b> cubic units (≈ 11.7).",
            ],
        },
        {
            "title": "A parametric curve: the ellipsoid",
            "question": "The curve C has parametric equations x = 4 cos t, y = 3 sin t, 0 ≤ t ≤ π/2. The region bounded by C and the "
                        "coordinate axes is rotated through 2π about the x-axis.\n(a) Find the exact volume of the solid formed.\n"
                        "(b) Deduce the volume of the ellipsoid formed by rotating the whole ellipse x²/16 + y²/9 = 1 about the x-axis.",
            "steps": [
                "(a) dx/dt = −4 sin t. At t = 0, x = 4 (right-hand end); at t = π/2, x = 0 (left-hand end).",
                "V = π∫ y² dx with x from 0 to 4, so t runs from π/2 to 0: V = π∫<sub>π/2</sub><sup>0</sup> 9 sin²t (−4 sin t) dt "
                "= 36π∫<sub>0</sub><sup>π/2</sup> sin³t dt.",
                "sin³t = sin t (1 − cos²t) = sin t − sin t cos²t, so ∫ sin³t dt = −cos t + ⅓cos³t.",
                "∫<sub>0</sub><sup>π/2</sup> sin³t dt = (0 + 0) − (−1 + ⅓) = ⅔. So V = 36π × ⅔ = <b>24π</b>.",
                "(b) The ellipsoid is symmetric about the y-axis, so its volume is 2 × 24π = <b>48π</b>. Check: the formula ⁴⁄₃πabc "
                "gives ⁴⁄₃π × 4 × 3 × 3 = 48π.",
            ],
        },
        {
            "title": "Modelling a bowl",
            "question": "The inside of a bowl is modelled by rotating the curve y = x²/8, 0 ≤ y ≤ 8, through 2π about the y-axis, where "
                        "units are centimetres.\n(a) Find the capacity of the bowl.\n(b) Water is poured into the empty bowl until it is "
                        "half full. Find the depth of the water.\n(c) Give one limitation of the model.",
            "steps": [
                "(a) x² = 8y, so V = π∫₀⁸ 8y dy = π[4y²]₀⁸ = <b>256π cm³</b> ≈ 804 cm³ (3 s.f.).",
                "(b) To depth h: V(h) = π∫₀ʰ 8y dy = 4πh². Half full: 4πh² = 128π, so h² = 32 and h = 4√2 ≈ <b>5.66 cm</b>.",
                "The depth is more than half the height (4 cm), because the bowl is narrow at the bottom.",
                "(c) For example: a real bowl is not exactly parabolic; the model gives the inside only and ignores the thickness "
                "of the bowl.",
            ],
        },
        {
            "title": "Mean values",
            "question": "(a) Find the mean value of f(x) = x(4 − x) over 0 ≤ x ≤ 4.\n(b) Hence write down the mean value of "
                        "3 + 2x(4 − x) over the same interval.\n(c) The temperature T °C in a greenhouse t hours after 6 am is modelled "
                        "by T = 15 + 5 sin(πt/12), 0 ≤ t ≤ 12. Find the mean temperature between 6 am and 6 pm.",
            "figure": "pa14_mean.png",
            "caption": "The rectangle of height 8/3 on 0 ≤ x ≤ 4 has the same area, 32/3, as the region under the curve.",
            "width_mm": 85,
            "steps": [
                "(a) ∫₀⁴ (4x − x²) dx = [2x² − x³/3]₀⁴ = 32 − 64/3 = 32/3. Mean value = (1/4)(32/3) = <b>8/3</b>.",
                "(b) Mean of 3 + 2f = 3 + 2 × 8/3 = <b>25/3</b>. No new integration is needed.",
                "(c) T̄ = (1/12)∫₀¹² (15 + 5 sin(πt/12)) dt = 15 + (5/12)[−(12/π) cos(πt/12)]₀¹².",
                "= 15 + (5/12)(12/π)(1 − (−1)) = 15 + 10/π ≈ <b>18.2 °C</b> (3 s.f.).",
                "This is higher than the end values of 15 °C, because the greenhouse is warmer than 15 °C all day.",
            ],
        },
    ],
    "practice": [
        "The region bounded by y = 2x + 1, the x-axis, the y-axis and x = 3 is rotated through 2π about the x-axis. Find the exact "
        "volume generated.",
        "The region bounded by y = 1/x, the x-axis and the lines x = 1 and x = 4 is rotated through 2π about the x-axis. Find the "
        "exact volume.",
        "The region bounded by y = x² (x ≥ 0), the y-axis and the line y = 9 is rotated through 2π about the y-axis. Find the exact "
        "volume.",
        "The region under y = eˣ from x = 0 to x = 1 is rotated through 2π about the x-axis. Find the exact volume.",
        "By rotating the region under y = rx/h for 0 ≤ x ≤ h about the x-axis, prove that a cone of base radius r and height h has "
        "volume ⅓πr²h.",
        "By rotating the region between the semicircle y = √(r² − x²) and the x-axis about the x-axis, prove that a sphere of radius "
        "r has volume ⁴⁄₃πr³.",
        "The finite region between y = x² and y = 2x is rotated through 2π about the x-axis. Find the exact volume.",
        "The same region as in question 7 is rotated through 2π about the y-axis. Find the exact volume.",
        "A curve has parametric equations x = t³, y = t², 0 ≤ t ≤ 1. The region between the curve, the x-axis and the line x = 1 "
        "is rotated through 2π about the x-axis. Find the exact volume.",
        "Find the mean value of f(x) = 3x² − 2x over the interval 1 ≤ x ≤ 3.",
        "Find the exact mean value of cos x over 0 ≤ x ≤ π/2. Hence write down the mean value of 5 − 2 cos x over the same interval.",
        "Find the exact mean value of 1/x over 1 ≤ x ≤ e, and show that it is between the values of 1/x at the ends of the interval.",
    ],
    "answers": [
        "π∫₀³ (4x² + 4x + 1) dx = π[4x³/3 + 2x² + x]₀³ = π(36 + 18 + 3) = 57π.",
        "π∫₁⁴ x⁻² dx = π[−1/x]₁⁴ = π(1 − ¼) = 3π/4.",
        "x² = y, V = π∫₀⁹ y dy = 81π/2.",
        "π∫₀¹ e²ˣ dx = ½π(e² − 1).",
        "V = π∫₀ʰ r²x²/h² dx = π(r²/h²)(h³/3) = ⅓πr²h.",
        "V = π∫<sub>−r</sub><sup>r</sup> (r² − x²) dx = π[r²x − x³/3]<sub>−r</sub><sup>r</sup> = π(⅔r³ + ⅔r³) = ⁴⁄₃πr³.",
        "Intersect at x = 0, 2; 2x ≥ x² there. V = π∫₀² (4x² − x⁴) dx = π(32/3 − 32/5) = 64π/15.",
        "x from y/2 to √y for 0 ≤ y ≤ 4: V = π∫₀⁴ (y − y²/4) dy = π(8 − 16/3) = 8π/3.",
        "V = π∫₀¹ t⁴ × 3t² dt = 3π/7.",
        "(1/2)[x³ − x²]₁³ = (1/2)(18 − 0) = 9.",
        "(2/π)∫<sub>0</sub><sup>π/2</sup> cos x dx = 2/π; mean of 5 − 2 cos x = 5 − 4/π.",
        "(1/(e − 1))∫₁ᵉ (1/x) dx = 1/(e − 1) ≈ 0.582, which lies between 1/e ≈ 0.368 and 1.",
    ],
    "exam": [
        "The curve C has equation y = 4 − x² and the line L has equation y = x + 2.\n"
        "(a) Find the x-coordinates of the points where C and L meet. [2]\n"
        "(b) The finite region R bounded by C and L is rotated through 2π radians about the x-axis. Show that the volume of the solid "
        "generated is 108π/5. [5]\n"
        "(c) Find the mean value of 4 − x² over the interval −2 ≤ x ≤ 1. [3]\n"
        "(d) Find the values of x in this interval at which 4 − x² equals its mean value. [2]",
        "A glass vase is modelled by rotating the curve x = 2 + sin(y/2), 0 ≤ y ≤ 2π, through 2π radians about the y-axis. The units "
        "are centimetres and the vase has a flat base on the x-axis.\n"
        "(a) Show that the volume of the vase, according to the model, is π(9π + 16) cm³. [6]\n"
        "(b) Find the mean radius of the vase with respect to height, giving your answer to 3 significant figures. [3]\n"
        "(c) State one way in which the model may not be realistic. [1]",
        "The curve C has parametric equations x = t², y = t − t³, 0 ≤ t ≤ 1.\n"
        "(a) Show that a Cartesian equation of C is y² = x(1 − x)². [2]\n"
        "(b) The region bounded by C and the x-axis is rotated through 2π radians about the x-axis. Use the parametric equations to "
        "find the exact volume of the solid formed. [5]\n"
        "(c) Find the exact mean value of y with respect to x over 0 ≤ x ≤ 1. [3]",
        "A sphere of radius r is formed by rotating the circle x² + y² = r² about the y-axis.\n"
        "(a) By rotating the region between the circle, the y-axis and the lines y = r − h and y = r, show that a cap of depth h cut "
        "from the sphere has volume ⅓πh²(3r − h). [5]\n"
        "(b) A hemispherical bowl of radius 10 cm contains water to a depth of 4 cm. Find the volume of water. [2]\n"
        "(c) Find the depth of water when the bowl contains 1 litre (1000 cm³), to 3 significant figures. [3]",
    ],
    "exam_answers": [
        "(a) 4 − x² = x + 2 ⇒ x² + x − 2 = 0 ⇒ x = −2, 1. [M1 A1]\n"
        "(b) On −2 ≤ x ≤ 1 both are ≥ 0 and 4 − x² ≥ x + 2. V = π∫<sub>−2</sub><sup>1</sup> [(4 − x²)² − (x + 2)²] dx [M1] "
        "= π∫ (x⁴ − 9x² − 4x + 12) dx [A1] = π[x⁵/5 − 3x³ − 2x² + 12x]<sub>−2</sub><sup>1</sup> [M1] = π(36/5 + 72/5) [A1] "
        "= 108π/5 [A1].\n"
        "(c) (1/3)∫<sub>−2</sub><sup>1</sup> (4 − x²) dx [M1] = (1/3)[4x − x³/3]<sub>−2</sub><sup>1</sup> = (1/3)(11/3 + 16/3) [A1] = 3 [A1].\n"
        "(d) 4 − x² = 3 ⇒ x = ±1; both lie in the interval, so x = −1 and x = 1. [M1 A1]",
        "(a) V = π∫<sub>0</sub><sup>2π</sup> (2 + sin(y/2))² dy [M1] = π∫ (4 + 4 sin(y/2) + sin²(y/2)) dy [A1]; "
        "sin²(y/2) = ½(1 − cos y) [M1]; = π[4y − 8 cos(y/2) + y/2 − ½ sin y]<sub>0</sub><sup>2π</sup> [A1] "
        "= π[(8π + 8 + π) − (−8)] [M1] = π(9π + 16) [A1] (≈ 139 cm³).\n"
        "(b) (1/(2π))∫<sub>0</sub><sup>2π</sup> (2 + sin(y/2)) dy [M1] = (1/(2π))[2y − 2 cos(y/2)]<sub>0</sub><sup>2π</sup> = "
        "(1/(2π))(4π + 4) [A1] = 2 + 2/π ≈ 2.64 cm [A1].\n"
        "(c) e.g. the glass has thickness, so the inside volume is less; a real vase is not exactly this shape. [B1]",
        "(a) t = √x, so y = √x(1 − x) [M1] and y² = x(1 − x)² [A1].\n"
        "(b) V = π∫ y² (dx/dt) dt = π∫₀¹ (t − t³)² 2t dt [M1 A1] = 2π∫₀¹ (t³ − 2t⁵ + t⁷) dt [M1] = 2π(¼ − ⅓ + ⅛) [A1] "
        "= π/12 [A1].\n"
        "(c) Mean = ∫₀¹ √x(1 − x) dx ÷ 1 [M1] = [⅔x^(3/2) − ⅖x^(5/2)]₀¹ [A1] = 4/15 [A1].",
        "(a) x² = r² − y² [B1]. V = π∫<sub>r−h</sub><sup>r</sup> (r² − y²) dy [M1] = π[r²y − y³/3]<sub>r−h</sub><sup>r</sup> [A1] "
        "= π[⅔r³ − r²(r − h) + ⅓(r − h)³] [M1] = π(rh² − ⅓h³) = ⅓πh²(3r − h) [A1].\n"
        "(b) The water is a cap of depth 4 of a sphere of radius 10 [M1]: V = ⅓π(16)(26) = 416π/3 ≈ 436 cm³ [A1].\n"
        "(c) ⅓πh²(30 − h) = 1000 [M1] ⇒ h³ − 30h² + 3000/π = 0 [M1]; the root with 0 < h < 10 is h ≈ 6.36 cm [A1].",
    ],
}
