"""Unit B14: Numerical methods — root finding (IAL), mid-ordinate and Simpson's rules, step-by-step solution of DEs."""

UNIT = {
    "number": "B14",
    "title": "Numerical methods",
    "tag": "AQA J1–J3 (A level) · Edexcel FP1 6.1–6.2 (A level option); AS FP1 4.1 (no Simpson's rule) "
           "· IAL FP1 3.1 (root finding only) · not in OCR A, OCR MEI or CAIE 9231 pure",
    "notes": [
        ("p", "Many equations, integrals and differential equations cannot be solved exactly. Numerical methods give "
              "approximate answers to any accuracy we need, by repeating simple arithmetic. This unit covers three "
              "families of method. Check the heading of each section against your board: they differ more here than "
              "anywhere else in the course."),
        ("table", ["Section", "IAL FP1", "AQA", "Edexcel FP1 (A level)", "Edexcel AS FP1"], [
            ["14.1 Bisection, linear interpolation, Newton–Raphson", "3.1", "—", "—", "—"],
            ["14.2 Mid-ordinate rule", "—", "J1", "—", "—"],
            ["14.2 Simpson's rule", "—", "J1", "6.2", "—"],
            ["14.3 Euler's method, first-order DEs", "—", "J2", "6.1", "4.1"],
            ["14.4 Improved Euler / central difference", "—", "J3", "6.1", "4.1"],
            ["14.5 Second-order DEs by finite differences", "—", "—", "6.1", "4.1"],
        ]),
        ("p", "Work with at least two more decimal places than the answer needs, keep full calculator values between "
              "steps, and round only at the end. Set the calculator to radians for any trigonometric function."),

        ("h2", "14.1 Solving f(x) = 0 numerically (IAL FP1)"),
        ("p", "<b>Change of sign.</b> If f is continuous on [a, b] and f(a) and f(b) have opposite signs, then f(x) = 0 has "
              "at least one root between a and b. Continuity matters: f(x) = 1/x changes sign on [−1, 1] but has no root. "
              "To show that a root α equals 2.095 to 3 decimal places, show that f changes sign on [2.0945, 2.0955]."),
        ("box", "Three iterative methods for a root of f(x) = 0", [
            "<b>Interval bisection.</b> Start with [a, b] where f changes sign. Find m = (a + b)/2. Keep the half "
            "[a, m] or [m, b] on which f still changes sign. Each step halves the interval.",
            "<b>Linear interpolation</b> (false position). Join (a, f(a)) and (b, f(b)) with a straight line; it crosses the "
            "x-axis at x = a + (b − a) × |f(a)|/(|f(a)| + |f(b)|) = (a f(b) − b f(a))/(f(b) − f(a)). Replace the end "
            "with the same sign of f by this value and repeat.",
            "<b>Newton–Raphson.</b> xₙ₊₁ = xₙ − f(xₙ)/f′(xₙ). Geometrically, xₙ₊₁ is where the tangent at (xₙ, f(xₙ)) "
            "crosses the x-axis.",
        ]),
        ("p", "<b>Deriving Newton–Raphson.</b> The tangent at x = xₙ is y − f(xₙ) = f′(xₙ)(x − xₙ). Put y = 0: "
              "x = xₙ − f(xₙ)/f′(xₙ). The method converges very fast near a simple root (roughly doubling the number of "
              "correct decimal places each step), but it can fail: if f′(xₙ) = 0 the tangent is horizontal and xₙ₊₁ is "
              "undefined; if f′(xₙ) is small, xₙ₊₁ is thrown far away, possibly towards a different root; and a poor "
              "starting value can lead to oscillation. Bisection is slow but always works once a sign change is found."),
        ("figure", "pb14_newton.png",
         "Newton–Raphson for f(x) = x³ − 2x − 5 from x₀ = 2.5: each tangent meets the x-axis at the next approximation.", 100),

        ("h2", "14.2 Numerical integration: mid-ordinate and Simpson's rules"),
        ("p", "Divide [a, b] into n strips of width h = (b − a)/n, with xᵣ = a + rh and ordinates yᵣ = f(xᵣ)."),
        ("box", "Integration rules", [
            "<b>Mid-ordinate rule</b> (AQA): ∫ₐᵇ y dx ≈ h(y₁/₂ + y₃/₂ + … + y₍ₙ₋₁/₂₎), where y₁/₂ = f(a + h/2) and so on: "
            "the sum of rectangles whose heights are taken at the middle of each strip.",
            "<b>Simpson's rule</b> (AQA; Edexcel FP1 A level), n even: ∫ₐᵇ y dx ≈ (h/3)[y₀ + yₙ + 4(y₁ + y₃ + … + yₙ₋₁) "
            "+ 2(y₂ + y₄ + … + yₙ₋₂)]. Pattern of weights: 1, 4, 2, 4, 2, …, 4, 1.",
            "Simpson's rule is not in the Edexcel formula booklet; learn it. AQA prints both rules.",
        ]),
        ("p", "<b>Where Simpson's rule comes from.</b> Over each pair of strips, it replaces the curve by the parabola "
              "through the three points. For the parabola through (−h, y₀), (0, y₁), (h, y₂) the exact area is "
              "(h/3)(y₀ + 4y₁ + y₂). Adding these over n/2 pairs gives the rule. Because it fits curves, it is usually far "
              "more accurate than the trapezium or mid-ordinate rule for the same n, and it is exact for cubics."),
        ("p", "Increasing the number of strips improves the accuracy of every rule. For a curve that bends one way only, "
              "the mid-ordinate rule and the trapezium rule err in opposite directions: for a convex curve the "
              "mid-ordinate rule underestimates and the trapezium rule overestimates."),
        ("figure", "pb14_strips.png",
         "∫₀¹ √(1 + x³) dx with four strips. Left: mid-ordinate rectangles. Right: Simpson's rule fits a parabola over "
         "each pair of strips (dashed), almost indistinguishable from the curve.", 150),

        ("h2", "14.3 Euler's method for first-order differential equations"),
        ("p", "To solve dy/dx = f(x, y) with y = y₀ at x = x₀, step along the tangent. The gradient at (xᵣ, yᵣ) is "
              "f(xᵣ, yᵣ), so over a step of length h the change in y is approximately h f(xᵣ, yᵣ). Equivalently, use the "
              "forward-difference approximation (dy/dx)ᵣ ≈ (yᵣ₊₁ − yᵣ)/h (Edexcel's form)."),
        ("box", "Euler's step-by-step method (AQA J2, Edexcel 6.1)", [
            "yᵣ₊₁ = yᵣ + h f(xᵣ, yᵣ),  xᵣ₊₁ = xᵣ + h.",
            "Set out the work in a table of r, xᵣ, yᵣ, f(xᵣ, yᵣ). The error grows with each step, because each step "
            "starts from an approximate point. Halving h roughly halves the error.",
        ]),
        ("figure", "pb14_euler.png",
         "Euler's method for dy/dx = x + y, y(0) = 1 with h = 0.1 (straight steps) and the exact solution y = 2eˣ − x − 1. "
         "The curve is convex, so the tangent steps fall below it and the error grows.", 100),

        ("h2", "14.4 The improved Euler (central-difference) method"),
        ("p", "A better approximation to the gradient at xᵣ uses the points either side: (dy/dx)ᵣ ≈ (yᵣ₊₁ − yᵣ₋₁)/(2h), the "
              "<b>central difference</b>. Rearranging gives AQA's improved Euler formula."),
        ("box", "Improved Euler method (AQA J3; Edexcel 6.1 central difference)", [
            "yᵣ₊₁ = yᵣ₋₁ + 2h f(xᵣ, yᵣ),  xᵣ₊₁ = xᵣ + h.",
            "It needs two starting values. y₀ is given; y₁ is usually found by one step of Euler's method (or is given).",
            "The error per step is much smaller than for Euler's method.",
        ]),
        ("p", "Other books use the name \"improved Euler\" for a predictor–corrector method (Heun's method) that averages "
              "the gradients at both ends of a step. That is not the method in these specifications: use the formula above."),

        ("h2", "14.5 Second-order equations by finite differences (Edexcel)"),
        ("p", "Combining forward and backward steps gives an approximation to the second derivative: "
              "(d²y/dx²)ᵣ ≈ (yᵣ₊₁ − 2yᵣ + yᵣ₋₁)/h². It follows from the Taylor series yᵣ₊₁ = yᵣ + hyᵣ′ + ½h²yᵣ″ + … and "
              "yᵣ₋₁ = yᵣ − hyᵣ′ + ½h²yᵣ″ − …: adding them cancels the odd terms."),
        ("box", "Edexcel FP1 6.1 approximations", [
            "(dy/dx)ₙ ≈ (yₙ₊₁ − yₙ)/h",
            "(dy/dx)ₙ ≈ (yₙ₊₁ − yₙ₋₁)/(2h)",
            "(d²y/dx²)ₙ ≈ (yₙ₊₁ − 2yₙ + yₙ₋₁)/h²",
            "These are not in the formula booklet: learn them.",
        ]),
        ("p", "<b>Method.</b> Replace each derivative in the DE by its approximation at x = xₙ and rearrange for yₙ₊₁ in "
              "terms of yₙ and yₙ₋₁ (a recurrence relation). To start, you need y₁. Either use y₁ ≈ y₀ + h y₀′, or "
              "use the central difference (y₁ − y₋₁)/(2h) = y₀′ to eliminate the imaginary value y₋₁ from the recurrence "
              "at n = 0. The question will say which."),

        ("warn", "Common mistakes", [
            "Using degrees instead of radians in trigonometric functions.",
            "Rounding intermediate values: carry at least 5 or 6 significant figures and round only the final answers.",
            "Counting strips wrongly: n strips need n + 1 ordinates for Simpson's rule (n even), but only n mid-ordinates.",
            "In Simpson's rule, swapping the 4s and 2s: the odd-numbered ordinates get weight 4.",
            "In the improved Euler method, using yᵣ instead of yᵣ₋₁ as the starting value, i.e. writing "
            "yᵣ₊₁ = yᵣ + 2h f(xᵣ, yᵣ).",
            "Using Newton–Raphson without f′ and f evaluated at the same xₙ, or not checking that the answer is a root "
            "by a sign change when asked to justify its accuracy.",
            "Linear interpolation: replacing the wrong end point. Keep the two ends with opposite signs of f.",
        ]),
    ],

    "examples": [
        {
            "title": "Interval bisection and linear interpolation (IAL)",
            "question": "f(x) = x³ − 2x − 5. (a) Show that f(x) = 0 has a root α in [2, 3]. (b) Use interval bisection "
                        "three times to find an interval of width 0.125 containing α. (c) Starting from [2, 3], apply linear "
                        "interpolation twice to estimate α, giving answers to 4 decimal places.",
            "steps": [
                "(a) f(2) = −1 < 0 and f(3) = 16 > 0. f is continuous (a polynomial), so there is a root in [2, 3].",
                "(b) f(2.5) = 5.625 > 0: root in [2, 2.5]. f(2.25) = 1.890625 > 0: root in [2, 2.25]. f(2.125) = 0.345703 > 0: "
                "root in [2, 2.125].",
                "(c) x₁ = 2 + 1 × 1/(1 + 16) = 2.0588 (4 d.p.). f(2.0588…) = −0.3908 < 0, so α lies in [2.0588, 3].",
                "x₂ = 2.0588 + (3 − 2.0588) × 0.3908/(0.3908 + 16) = 2.0813 (4 d.p.). The estimates creep up towards α from "
                "one side; the method is reliable but slow here because f is far from linear on [2, 3].",
            ],
        },
        {
            "title": "Newton–Raphson (IAL)",
            "question": "Use Newton–Raphson with x₀ = 2 to find the root α of x³ − 2x − 5 = 0 correct to 3 decimal places. "
                        "Justify the accuracy. Explain why x₀ = 0.8165 would be a poor choice.",
            "steps": [
                "f′(x) = 3x² − 2. x₁ = 2 − (−1)/10 = 2.1.",
                "x₂ = 2.1 − f(2.1)/f′(2.1) = 2.1 − 0.061/11.23 = 2.094568.",
                "x₃ = 2.094568 − f(2.094568)/f′(2.094568) = 2.094551. Successive values agree to 4 d.p., suggesting α = 2.095.",
                "Check: f(2.0945) = −0.000575 < 0 and f(2.0955) = 0.0106 > 0. Sign change and f continuous, so "
                "2.0945 < α < 2.0955 and α = 2.095 to 3 d.p.",
                "f′(x) = 0 at x = √(2/3) = 0.8165, so the tangent there is (almost) horizontal: f′(x₀) ≈ 0 and x₁ would be "
                "undefined or very far from α.",
            ],
        },
        {
            "title": "Mid-ordinate rule and Simpson's rule (AQA; Simpson also Edexcel FP1)",
            "question": "Estimate ∫₀¹ √(1 + x³) dx using four strips with (a) the mid-ordinate rule and (b) Simpson's "
                        "rule, giving answers to 4 decimal places. (c) The value to 4 decimal places is 1.1114. Comment.",
            "steps": [
                "h = 0.25. (a) Mid-ordinates at x = 0.125, 0.375, 0.625, 0.875: y = 1.000976, 1.026028, 1.115411, 1.292255.",
                "Mid-ordinate estimate = 0.25 × 4.434670 = 1.1087 (4 d.p.).",
                "(b) Ordinates: y₀ = 1, y₁ = √1.015625 = 1.007782, y₂ = √1.125 = 1.060660, y₃ = √1.421875 = 1.192424, "
                "y₄ = √2 = 1.414214.",
                "Simpson: (0.25/3)[1 + 1.414214 + 4(1.007782 + 1.192424) + 2(1.060660)] = (0.25/3)(13.336359) = 1.1114 (4 d.p.).",
                "(c) Simpson's rule is correct to 4 d.p. with only four strips; the mid-ordinate rule is 0.0028 too small "
                "(the curve is convex on [0, 1], so the mid-ordinate rule underestimates).",
            ],
        },
        {
            "title": "Euler's method",
            "question": "dy/dx = x + y with y = 1 when x = 0. Use Euler's method with h = 0.1 to estimate y at x = 0.3. "
                        "Compare with the exact solution y = 2eˣ − x − 1.",
            "steps": [
                "yᵣ₊₁ = yᵣ + 0.1(xᵣ + yᵣ).",
                "y₁ = 1 + 0.1(0 + 1) = 1.1.",
                "y₂ = 1.1 + 0.1(0.1 + 1.1) = 1.22.",
                "y₃ = 1.22 + 0.1(0.2 + 1.22) = 1.362.",
                "Exact y(0.3) = 2e^0.3 − 1.3 = 1.3997 (4 d.p.). Euler's estimate is 0.0377 too small (2.7% error).",
            ],
        },
        {
            "title": "The improved Euler method (AQA J3)",
            "question": "For the same equation, dy/dx = x + y with y(0) = 1, use the improved Euler formula "
                        "yᵣ₊₁ = yᵣ₋₁ + 2h f(xᵣ, yᵣ) with h = 0.1 to estimate y at x = 0.3, finding y₁ by one Euler step.",
            "steps": [
                "y₁ = 1.1 (from Example B14.4).",
                "y₂ = y₀ + 0.2 f(0.1, 1.1) = 1 + 0.2(1.2) = 1.24.",
                "y₃ = y₁ + 0.2 f(0.2, 1.24) = 1.1 + 0.2(1.44) = 1.388.",
                "Error 1.3997 − 1.388 = 0.0117, about a third of Euler's error, for the same step length.",
            ],
        },
        {
            "title": "A second-order equation by finite differences (Edexcel FP1 6.1)",
            "question": "d²y/dx² = x² − y, with y = 1 and dy/dx = 0 at x = 0. (a) Use (d²y/dx²)ₙ ≈ (yₙ₊₁ − 2yₙ + yₙ₋₁)/h² "
                        "with h = 0.1 to show that yₙ₊₁ = 2yₙ − yₙ₋₁ + 0.01(xₙ² − yₙ). (b) Use (dy/dx)₀ ≈ (y₁ − y₋₁)/(2h) to "
                        "find y₁. (c) Estimate y at x = 0.3, to 4 decimal places, and compare with the exact value "
                        "y = x² − 2 + 3 cos x.",
            "steps": [
                "(a) (yₙ₊₁ − 2yₙ + yₙ₋₁)/0.01 = xₙ² − yₙ, so yₙ₊₁ = 2yₙ − yₙ₋₁ + 0.01(xₙ² − yₙ).",
                "(b) (dy/dx)₀ = 0 gives y₋₁ = y₁. With n = 0: y₁ = 2(1) − y₁ + 0.01(0 − 1), so 2y₁ = 1.99 and y₁ = 0.995.",
                "(c) y₂ = 2(0.995) − 1 + 0.01(0.01 − 0.995) = 0.98015.",
                "y₃ = 2(0.98015) − 0.995 + 0.01(0.04 − 0.98015) = 0.955899, so y(0.3) ≈ 0.9559.",
                "Exact: 0.09 − 2 + 3 cos 0.3 = 0.9560 (4 d.p.). The estimate is correct to 3 d.p.",
            ],
        },
    ],

    "practice": [
        "(IAL) Show that x³ + x − 3 = 0 has a root in [1, 2]. Use interval bisection three times to find an interval of "
        "width 0.125 containing the root.",
        "(IAL) For the equation in the previous question, apply linear interpolation twice, starting from [1, 2], giving "
        "each answer to 4 decimal places.",
        "(IAL) Use Newton–Raphson with x₀ = 1.5 to find the larger root of eˣ = 3x, giving x₁ and x₂ to 4 decimal places "
        "and the root to 3 decimal places.",
        "(IAL) Show that Newton–Raphson for f(x) = x² − 7 gives xₙ₊₁ = ½(xₙ + 7/xₙ). Find x₁ and x₂ when x₀ = 3, to 4 "
        "decimal places.",
        "(IAL) For f(x) = x³ − 3x + 1, explain why Newton–Raphson fails with x₀ = 1. Use x₀ = 1.5 to find x₁, to 4 "
        "decimal places.",
        "(AQA) Use the mid-ordinate rule with four strips to estimate ∫₀² 1/(1 + x²) dx, to 4 decimal places.",
        "(AQA, Edexcel) Use Simpson's rule with four strips to estimate the integral in the previous question. Compare both "
        "estimates with the exact value arctan 2.",
        "(AQA, Edexcel) Use Simpson's rule with four strips to estimate ∫₁² ln x dx to 5 decimal places, and find the "
        "error by comparing with the exact value 2 ln 2 − 1.",
        "Use Euler's method with h = 0.1 to estimate y at x = 1.2, given dy/dx = xy and y = 2 at x = 1. Compare with the "
        "exact value 2e^0.22.",
        "Use Euler's method with h = 0.25 to estimate y at x = 0.5, given dy/dx = √(x + y) and y = 1 at x = 0. Give "
        "your answer to 4 decimal places.",
        "(AQA) dy/dx = x² + y, y(0) = 1. Use one Euler step with h = 0.1 to find y₁, then the improved Euler formula "
        "yᵣ₊₁ = yᵣ₋₁ + 2h f(xᵣ, yᵣ) to estimate y at x = 0.3. Compare with the exact value 3e^0.3 − 2.69.",
        "(Edexcel) d²y/dx² = −4y, with y = 1 and dy/dx = 0 at x = 0. Use (d²y/dx²)ₙ ≈ (yₙ₊₁ − 2yₙ + yₙ₋₁)/h² with "
        "h = 0.1, and y₋₁ = y₁ (from the central difference for dy/dx at x = 0), to estimate y at x = 0.2. Compare "
        "with cos 0.4.",
    ],
    "answers": [
        "f(1) = −1, f(2) = 7: sign change. f(1.5) = 1.875 > 0 → [1, 1.5]; f(1.25) = 0.203 > 0 → [1, 1.25]; "
        "f(1.125) = −0.451 < 0 → [1.125, 1.25]. (Root 1.2134.)",
        "x₁ = 1 + 1/8 = 1.125, f(1.125) = −0.451 < 0, so use [1.125, 2]: x₂ = 1.1780.",
        "f(x) = eˣ − 3x, f′(x) = eˣ − 3. x₁ = 1.5124, x₂ = 1.5121; root 1.512 (f(1.5115) < 0, f(1.5125) > 0).",
        "xₙ₊₁ = xₙ − (xₙ² − 7)/(2xₙ) = ½(xₙ + 7/xₙ). x₁ = 2.6667, x₂ = 2.6458 (√7 = 2.6458).",
        "f′(x) = 3x² − 3 = 0 at x = 1, so x₁ = x₀ − f(x₀)/0 is undefined (the tangent is horizontal). From 1.5: "
        "f(1.5) = −0.125, f′(1.5) = 3.75, x₁ = 1.5333.",
        "h = 0.5, mid-ordinates at 0.25, 0.75, 1.25, 1.75: 0.5(0.941176 + 0.64 + 0.390244 + 0.246154) = 1.1088.",
        "(0.5/3)[1 + 0.2 + 4(0.8 + 0.307692) + 2(0.5)] = 1.1051. arctan 2 = 1.1071: errors +0.0016 (mid-ordinate) and "
        "−0.0020 (Simpson). With so few strips over a strongly curved region neither is very accurate.",
        "(0.25/3)[0 + ln 2 + 4(ln 1.25 + ln 1.75) + 2 ln 1.5] = 0.38626. Exact 0.38629, error 0.00003.",
        "y₁ = 2 + 0.1(1 × 2) = 2.2; y₂ = 2.2 + 0.1(1.1 × 2.2) = 2.442. Exact 2.4922; Euler underestimates by 0.050.",
        "y₁ = 1 + 0.25√1 = 1.25; y₂ = 1.25 + 0.25√1.5 = 1.5562.",
        "y₁ = 1.1; y₂ = 1 + 0.2(0.01 + 1.1) = 1.222; y₃ = 1.1 + 0.2(0.04 + 1.222) = 1.3524. Exact 1.3596 (error 0.0072).",
        "yₙ₊₁ = 2yₙ − yₙ₋₁ − 0.04yₙ. n = 0: 2y₁ = 2 − 0.04, y₁ = 0.98. y₂ = 1.96(0.98) − 1 = 0.9208. cos 0.4 = 0.9211.",
    ],

    "exam": [
        "(IAL) f(x) = x³ − 5x + 3.\n"
        "(a) Show that the equation f(x) = 0 has a root α in the interval [1.8, 1.9]. [2]\n"
        "(b) Use linear interpolation once on [1.8, 1.9] to find an approximation to α, to 4 decimal places. [3]\n"
        "(c) Taking 1.8 as a first approximation, apply the Newton–Raphson procedure once to find a second "
        "approximation to α, to 4 decimal places. [4]\n"
        "(d) Given that α = 1.8342 to 4 decimal places, state which of your approximations is closer. [1]\n"
        "(e) Explain why x₀ = √(5/3) cannot be used as a starting value for the Newton–Raphson procedure. [2]",

        "(AQA) I = ∫₀² √(1 + x³) dx.\n"
        "(a) Use the mid-ordinate rule with four strips to estimate I, to 4 decimal places. [3]\n"
        "(b) Use Simpson's rule with four strips to estimate I, to 4 decimal places. [4]\n"
        "(c) Given that I = 3.2413 to 4 decimal places, find the percentage error in each estimate and comment. [2]\n"
        "(d) State how either estimate could be improved. [1]",

        "(Edexcel) y satisfies d²y/dx² + x dy/dx + y = 2, with y = 1 and dy/dx = 1 at x = 0.\n"
        "(a) Use the approximations (d²y/dx²)ₙ ≈ (yₙ₊₁ − 2yₙ + yₙ₋₁)/h² and (dy/dx)ₙ ≈ (yₙ₊₁ − yₙ₋₁)/(2h) with h = 0.1 "
        "to show that (20 + xₙ)yₙ₊₁ = 39.8yₙ − (20 − xₙ)yₙ₋₁ + 0.4. [4]\n"
        "(b) Use (dy/dx)₀ ≈ (y₁ − y₋₁)/(2h) to show that y₋₁ = y₁ − 0.2, and hence find y₁. [3]\n"
        "(c) Find estimates of y at x = 0.2 and x = 0.3, to 4 decimal places. [4]",

        "(AQA) The function y satisfies dy/dx = √(x² + y), with y = 3 when x = 1.\n"
        "(a) Use Euler's method with h = 0.1 to estimate y at x = 1.1. [2]\n"
        "(b) Use the improved Euler formula yᵣ₊₁ = yᵣ₋₁ + 2h f(xᵣ, yᵣ), with h = 0.1 and your answer to (a), to estimate y "
        "at x = 1.2 and at x = 1.3, to 4 decimal places. [4]\n"
        "(c) State how the accuracy of the estimates could be improved. [1]\n"
        "(d) Explain why the improved Euler method is generally more accurate than Euler's method. [1]",
    ],
    "exam_answers": [
        "(a) f(1.8) = −0.168 < 0, f(1.9) = 0.359 > 0 (M1); sign change and f continuous, so a root lies in [1.8, 1.9] (A1). "
        "(b) α ≈ 1.8 + 0.1 × 0.168/(0.168 + 0.359) (M1 A1) = 1.8319 (A1). (c) f′(x) = 3x² − 5 (B1), f′(1.8) = 4.72 (M1); "
        "x₁ = 1.8 − (−0.168)/4.72 (M1) = 1.8356 (A1). (d) Newton–Raphson: |1.8356 − 1.8342| = 0.0014 < 0.0023 (B1). "
        "(e) f′(√(5/3)) = 3(5/3) − 5 = 0 (M1), so the formula would divide by zero: the tangent is horizontal and never "
        "meets the x-axis (A1).",
        "(a) h = 0.5; mid-ordinates at 0.25, 0.75, 1.25, 1.75 (M1): 1.007782, 1.192424, 1.718466, 2.521780 (A1); "
        "I ≈ 0.5 × 6.440452 = 3.2202 (A1). (b) Ordinates 1, 1.060660, 1.414214, 2.091650, 3 (M1 A1); "
        "(0.5/3)[1 + 3 + 4(1.060660 + 2.091650) + 2(1.414214)] (M1) = 3.2396 (A1). (c) Mid-ordinate: (3.2413 − 3.2202)/3.2413 "
        "= 0.65%; Simpson: 0.05%; Simpson's rule is much more accurate (B1 B1). (d) Use more strips (B1).",
        "(a) (yₙ₊₁ − 2yₙ + yₙ₋₁)/0.01 + xₙ(yₙ₊₁ − yₙ₋₁)/0.2 + yₙ = 2 (M1 A1); multiply by 0.2: "
        "20yₙ₊₁ − 40yₙ + 20yₙ₋₁ + xₙyₙ₊₁ − xₙyₙ₋₁ + 0.2yₙ = 0.4 (M1), which rearranges to the given result (A1). "
        "(b) (y₁ − y₋₁)/0.2 = 1, y₋₁ = y₁ − 0.2 (B1); n = 0: 20y₁ = 39.8 − 20(y₁ − 0.2) + 0.4 (M1), 40y₁ = 44.2, "
        "y₁ = 1.105 (A1). (c) n = 1: 20.1y₂ = 39.8(1.105) − 19.9(1) + 0.4 (M1), y₂ = 1.2179 (A1); n = 2: "
        "20.2y₃ = 39.8(1.217861) − 19.8(1.105) + 0.4 (M1), y₃ = 1.3362 (A1).",
        "(a) y₁ = 3 + 0.1√(1 + 3) (M1) = 3.2 (A1). (b) y₂ = y₀ + 0.2√(1.1² + 3.2) = 3 + 0.2√4.41 (M1) = 3.42 (A1); "
        "y₃ = y₁ + 0.2√(1.2² + 3.42) = 3.2 + 0.2√4.86 (M1) = 3.6409 (A1). (c) Use a smaller step length h (B1). "
        "(d) It uses the gradient at the middle of a step of length 2h (a central difference) rather than at its start (B1).",
    ],
}
