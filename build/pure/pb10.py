"""Unit B10: Second-order linear differential equations with constant coefficients."""

UNIT = {
    "number": "B10",
    "title": "Second-order differential equations",
    "tag": "A level · Edexcel CP 9.4–9.6 · IAL FP2 5.1 · AQA I4–I6 · OCR A 4.10d–e · OCR MEI Pc11–Pc14 "
           "· CAIE 9231 P2 2.6",
    "notes": [
        ("p", "Second-order linear equations with constant coefficients model vibrating springs, electrical circuits, "
              "swinging pendulums and suspension systems. They can all be solved by one method: an algebraic "
              "<b>auxiliary equation</b> gives the general solution of the homogeneous equation (the complementary "
              "function), and a sensible guess gives one particular solution of the full equation (the particular "
              "integral). Throughout, a, b, c are real constants and y′ = dy/dx, y″ = d²y/dx²."),

        ("h2", "10.1 Homogeneous equations and the principle of superposition"),
        ("p", "The equation ay″ + by′ + cy = 0 is <b>homogeneous</b> (right-hand side zero). If y₁ and y₂ are solutions, so "
              "is Ay₁ + By₂ for any constants A, B, because differentiation is linear: "
              "a(Ay₁ + By₂)″ + b(Ay₁ + By₂)′ + c(Ay₁ + By₂) = A(ay₁″ + by₁′ + cy₁) + B(ay₂″ + by₂′ + cy₂) = 0. "
              "If y₁ and y₂ are not multiples of each other, Ay₁ + By₂ is the <b>general solution</b>: it has the two "
              "arbitrary constants that a second-order equation needs."),

        ("h2", "10.2 The auxiliary equation"),
        ("p", "Try y = eᵐˣ. Then y′ = meᵐˣ and y″ = m²eᵐˣ, so ay″ + by′ + cy = (am² + bm + c)eᵐˣ. Since eᵐˣ ≠ 0, y = eᵐˣ "
              "is a solution exactly when <b>am² + bm + c = 0</b>, the auxiliary (or characteristic) equation. Its "
              "discriminant b² − 4ac decides the form of the solution (Edexcel 9.6, AQA I6)."),
        ("table", ["Discriminant", "Roots of am² + bm + c = 0", "General solution"], [
            ["b² − 4ac > 0", "real, distinct α, β", "y = Aeᵅˣ + Beᵝˣ"],
            ["b² − 4ac = 0", "real, repeated α", "y = (A + Bx)eᵅˣ"],
            ["b² − 4ac < 0", "complex p ± qi", "y = eᵖˣ(A cos qx + B sin qx)"],
            ["special case b = 0, c/a = ω² > 0", "±ωi", "y = A cos ωx + B sin ωx"],
        ]),
        ("p", "<b>Repeated root.</b> When b² = 4ac and α = −b/(2a), the second solution is xeᵅˣ. Check: if y = xeᵅˣ, "
              "y′ = (1 + αx)eᵅˣ and y″ = (2α + α²x)eᵅˣ, so ay″ + by′ + cy = [x(aα² + bα + c) + (2aα + b)]eᵅˣ = 0, since "
              "α is a root and 2aα + b = 0."),
        ("p", "<b>Complex roots.</b> The roots p ± qi give e^((p+qi)x) = eᵖˣ(cos qx + i sin qx) and its conjugate (Euler's "
              "formula, B1). Adding and subtracting suitable multiples gives the two real solutions eᵖˣ cos qx and "
              "eᵖˣ sin qx. The factor eᵖˣ controls growth (p > 0) or decay (p < 0), and q sets the frequency of "
              "oscillation. The form R eᵖˣ cos(qx − φ) with R = √(A² + B²) is equivalent and useful for interpretation."),
        ("figure", "pb10_three_cases.png",
         "The three cases, each with y(0) = 1, y′(0) = 0: y″ − y′ − 2y = 0 (distinct real roots 2, −1), y″ + 2y′ + y = 0 "
         "(repeated root −1) and y″ + 2y′ + 10y = 0 (complex roots −1 ± 3i).", 110),

        ("h2", "10.3 Non-homogeneous equations: CF + PI"),
        ("box", "General solution of ay″ + by′ + cy = f(x)", [
            "Complementary function (CF): the general solution of ay″ + by′ + cy = 0, with two arbitrary constants.",
            "Particular integral (PI): any one function that satisfies ay″ + by′ + cy = f(x). It has no arbitrary constants.",
            "General solution: y = CF + PI.",
        ]),
        ("p", "<b>Why.</b> If y<sub>p</sub> is a PI and y is any solution, then y − y<sub>p</sub> satisfies the homogeneous equation (subtract "
              "the two equations), so y − y<sub>p</sub> is in the CF. Conversely CF + y<sub>p</sub> is always a solution. Only after the general "
              "solution is complete may initial conditions be used: they must be applied to CF + PI, never to the CF alone."),

        ("h2", "10.4 Choosing the trial particular integral"),
        ("p", "Guess a function of the same type as f(x) with unknown coefficients, substitute, and compare coefficients."),
        ("table", ["f(x)", "Trial PI"], [
            ["k (constant)", "λ"],
            ["kx + c, or any linear polynomial", "λx + μ"],
            ["kx² + px + q", "λx² + μx + ν (include every lower power)"],
            ["keᵖˣ", "λeᵖˣ"],
            ["m cos ωx, n sin ωx or m cos ωx + n sin ωx", "λ cos ωx + μ sin ωx (always both terms)"],
            ["a sum such as x + e²ˣ", "the sum of the separate trials, (λx + μ) + νe²ˣ"],
        ]),
        ("p", "Edexcel lists f(x) = keᵖˣ, A + Bx, p + qx + cx² and m cos ωx + n sin ωx; AQA, OCR A, MEI and Cambridge "
              "say polynomial, exponential or trigonometric. Cambridge may also give you the form of a PI (for example "
              "kx cos 2x) and ask you to find the coefficient."),

        ("h2", "10.5 When the trial PI is part of the CF"),
        ("p", "If the trial PI already appears in the CF, it satisfies the homogeneous equation, so substituting it gives 0, "
              "not f(x). Multiply the trial by x; if that is still in the CF (a repeated root), multiply by x² "
              "(OCR 4.10e, AQA I5, MEI Pc14)."),
        ("table", ["Equation", "CF", "Trial PI"], [
            ["y″ − y′ − 2y = 6e²ˣ", "Ae²ˣ + Be⁻ˣ", "λxe²ˣ"],
            ["y″ − 6y′ + 9y = e³ˣ", "(A + Bx)e³ˣ", "λx²e³ˣ"],
            ["y″ + 4y = sin 2x", "A cos 2x + B sin 2x", "x(λ cos 2x + μ sin 2x)"],
            ["y″ − 3y′ = 6", "A + Be³ˣ", "λx"],
        ]),
        ("p", "The case y″ + ω²y = k sin ωx gives a PI containing x cos ωx, whose amplitude grows without limit. In a "
              "mechanical model this is <b>resonance</b>, studied in B11."),

        ("h2", "10.6 Initial and boundary conditions, and interpretation"),
        ("bullets", [
            "Two conditions are needed to fix A and B: usually y and y′ at x = 0 (initial conditions), or y at two "
            "different values of x (boundary conditions).",
            "Differentiate the whole general solution (CF + PI) before substituting the value of y′.",
            "Interpret the solution: as x → ∞, terms with negative exponents die away, so the PI often describes the "
            "long-term behaviour; terms like e^(px) with p > 0 grow; sine and cosine terms oscillate.",
        ]),

        ("h2", "10.7 First-order equations with constant coefficients (CAIE)"),
        ("p", "The same CF + PI method works for dy/dx + ay = f(x). The auxiliary equation m + a = 0 gives the CF Ae⁻ᵃˣ, "
              "and a trial function gives the PI. For dy/dx + 2y = 4x + 1: CF Ae⁻²ˣ; trial λx + μ gives λ + 2λx + 2μ = 4x + 1, "
              "so λ = 2 and μ = −½, and y = Ae⁻²ˣ + 2x − ½. The integrating factor (B9) gives the same answer."),

        ("warn", "Common mistakes", [
            "Writing the complex case as Ae^((p+qi)x) + Be^((p−qi)x) and stopping: give the real form eᵖˣ(A cos qx + B sin qx).",
            "Using (A + B)eᵅˣ, which has only one constant, for a repeated root. The correct form is (A + Bx)eᵅˣ.",
            "Using a trial λ sin ωx alone when f(x) = sin ωx and there is a y′ term: the cosine term is needed too.",
            "Not spotting that the trial PI is already in the CF; substitution then gives 0 = f(x), a sure sign.",
            "Applying initial conditions to the CF before adding the PI.",
            "Arithmetic slips when comparing coefficients (Cambridge examiners' most common comment), and writing "
            "expressions or arrows instead of equations: always finish with \"y = …\".",
        ]),
    ],

    "examples": [
        {
            "title": "Distinct real roots with initial conditions",
            "question": "Solve y″ − y′ − 6y = 0 given that y = 3 and y′ = −1 when x = 0.",
            "steps": [
                "Auxiliary equation m² − m − 6 = 0, (m − 3)(m + 2) = 0, m = 3 or −2.",
                "General solution y = Ae³ˣ + Be⁻²ˣ, so y′ = 3Ae³ˣ − 2Be⁻²ˣ.",
                "x = 0: A + B = 3 and 3A − 2B = −1. Adding 2 × (first) gives 5A = 5, so A = 1, B = 2.",
                "y = e³ˣ + 2e⁻²ˣ.",
            ],
        },
        {
            "title": "Repeated and complex roots",
            "question": "(a) Find the general solution of y″ + 6y′ + 9y = 0. (b) Solve y″ + 4y′ + 13y = 0 given that y = 1 "
                        "and y′ = 4 when x = 0.",
            "steps": [
                "(a) m² + 6m + 9 = (m + 3)² = 0, repeated root −3. y = (A + Bx)e⁻³ˣ.",
                "(b) m² + 4m + 13 = 0: m = (−4 ± √(16 − 52))/2 = −2 ± 3i. y = e⁻²ˣ(A cos 3x + B sin 3x).",
                "x = 0: y = A = 1. y′ = e⁻²ˣ[(−2A + 3B) cos 3x + (−2B − 3A) sin 3x], so y′(0) = −2A + 3B = 4 and B = 2.",
                "y = e⁻²ˣ(cos 3x + 2 sin 3x). The oscillations decay to zero as x → ∞.",
            ],
        },
        {
            "title": "A sum of a polynomial and an exponential",
            "question": "Find the general solution of y″ − 3y′ + 2y = 4x + e³ˣ.",
            "steps": [
                "CF: m² − 3m + 2 = 0, m = 1, 2: y = Aeˣ + Be²ˣ.",
                "PI for 4x: try λx + μ. Then 0 − 3λ + 2λx + 2μ = 4x, so 2λ = 4 and 2μ − 3λ = 0: λ = 2, μ = 3.",
                "PI for e³ˣ: try νe³ˣ (3 is not a root). (9 − 9 + 2)ν = 1, ν = ½.",
                "y = Aeˣ + Be²ˣ + 2x + 3 + ½e³ˣ.",
            ],
        },
        {
            "title": "When the trial PI is in the CF",
            "question": "Solve y″ − y′ − 2y = 6e²ˣ, given y = 0 and y′ = 1 when x = 0.",
            "steps": [
                "CF: m² − m − 2 = 0, m = 2, −1: y = Ae²ˣ + Be⁻ˣ. The term e²ˣ is in the CF, so try y = λxe²ˣ.",
                "y′ = λ(1 + 2x)e²ˣ, y″ = λ(4 + 4x)e²ˣ. Then y″ − y′ − 2y = λe²ˣ(4 + 4x − 1 − 2x − 2x) = 3λe²ˣ = 6e²ˣ, so λ = 2.",
                "General solution y = Ae²ˣ + Be⁻ˣ + 2xe²ˣ; y′ = 2Ae²ˣ − Be⁻ˣ + (2 + 4x)e²ˣ.",
                "x = 0: A + B = 0 and 2A − B + 2 = 1. So 3A = −1: A = −⅓, B = ⅓.",
                "y = ⅓(e⁻ˣ − e²ˣ) + 2xe²ˣ.",
            ],
        },
        {
            "title": "Resonance: finding a given form of PI (CAIE, IAL)",
            "question": "(a) Find k given that kx cos 2x is a particular integral of y″ + 4y = sin 2x. (b) Hence solve the "
                        "equation given y = 0 and y′ = 0 when x = 0, and describe the solution for large x.",
            "figure": "pb10_resonance.png",
            "caption": "y = ⅛ sin 2x − ¼x cos 2x. The oscillations grow, staying close to the dashed lines y = ±x/4.",
            "width_mm": 95,
            "steps": [
                "(a) y = kx cos 2x: y′ = k cos 2x − 2kx sin 2x; y″ = −4k sin 2x − 4kx cos 2x.",
                "y″ + 4y = −4k sin 2x = sin 2x, so k = −¼.",
                "(b) CF: m² + 4 = 0, m = ±2i, so y = A cos 2x + B sin 2x − ¼x cos 2x.",
                "y(0) = A = 0. y′ = 2B cos 2x − ¼cos 2x + ½x sin 2x (with A = 0), so y′(0) = 2B − ¼ = 0, B = ⅛.",
                "y = ⅛ sin 2x − ¼x cos 2x. The term ¼x cos 2x dominates: the solution oscillates with period π and "
                "an amplitude that grows roughly like x/4, without limit.",
            ],
        },
        {
            "title": "Trigonometric forcing and long-term behaviour",
            "question": "Find the general solution of y″ + 2y′ + 5y = 10 cos x and describe y for large x.",
            "steps": [
                "CF: m² + 2m + 5 = 0, m = −1 ± 2i: y = e⁻ˣ(A cos 2x + B sin 2x).",
                "PI: try y = λ cos x + μ sin x. y′ = −λ sin x + μ cos x, y″ = −λ cos x − μ sin x.",
                "cos x: −λ + 2μ + 5λ = 10, i.e. 4λ + 2μ = 10. sin x: −μ − 2λ + 5μ = 0, i.e. 4μ = 2λ.",
                "So λ = 2μ, 10μ = 10: μ = 1, λ = 2.",
                "y = e⁻ˣ(A cos 2x + B sin 2x) + 2 cos x + sin x.",
                "As x → ∞, e⁻ˣ → 0, so y ≈ 2 cos x + sin x = √5 cos(x − α) with tan α = ½: an oscillation of amplitude √5 "
                "and period 2π, whatever the initial conditions.",
            ],
        },
    ],

    "practice": [
        "Find the general solution of y″ − 5y′ + 6y = 0.",
        "Find the general solution of 4y″ + 4y′ + y = 0.",
        "Find the general solution of y″ + 9y = 0.",
        "Find the general solution of y″ − 2y′ + 5y = 0.",
        "Solve y″ − 4y = 0 given y = 2 and y′ = 0 when x = 0. Express your answer using a hyperbolic function.",
        "Find the general solution of y″ + 2y′ − 3y = 9x².",
        "Find the general solution of y″ + y′ − 2y = 5e⁻²ˣ.",
        "Find the general solution of y″ − 6y′ + 9y = e³ˣ.",
        "Find the general solution of y″ + y = 3 cos 2x.",
        "Given that kx cos x is a particular integral of y″ + y = 2 sin x, find k and write down the general solution.",
        "Solve y″ + 3y′ + 2y = 10 sin x given y = 0 and y′ = 0 when x = 0. Describe the solution for large x.",
        "Use a complementary function and a particular integral to find the general solution of dy/dx + 2y = 4x + 1.",
    ],
    "answers": [
        "m = 2, 3: y = Ae²ˣ + Be³ˣ.",
        "4m² + 4m + 1 = (2m + 1)² = 0, m = −½ (repeated): y = (A + Bx)e^(−x/2).",
        "m = ±3i: y = A cos 3x + B sin 3x.",
        "m = 1 ± 2i: y = eˣ(A cos 2x + B sin 2x).",
        "y = Ae²ˣ + Be⁻²ˣ; A + B = 2, 2A − 2B = 0: A = B = 1. y = e²ˣ + e⁻²ˣ = 2 cosh 2x.",
        "CF Aeˣ + Be⁻³ˣ. Trial λx² + μx + ν: −3λ = 9, 4λ − 3μ = 0, 2λ + 2μ − 3ν = 0, so λ = −3, μ = −4, ν = −14/3. "
        "y = Aeˣ + Be⁻³ˣ − 3x² − 4x − 14/3.",
        "CF Aeˣ + Be⁻²ˣ contains e⁻²ˣ, so try λxe⁻²ˣ: −3λ = 5, λ = −5/3. y = Aeˣ + Be⁻²ˣ − (5/3)xe⁻²ˣ.",
        "CF (A + Bx)e³ˣ, so try λx²e³ˣ: 2λ = 1. y = (A + Bx)e³ˣ + ½x²e³ˣ.",
        "CF A cos x + B sin x. Trial λ cos 2x + μ sin 2x: −3λ = 3, −3μ = 0. y = A cos x + B sin x − cos 2x.",
        "y = kx cos x: y″ + y = −2k sin x = 2 sin x, k = −1. y = A cos x + B sin x − x cos x.",
        "CF Ae⁻ˣ + Be⁻²ˣ. PI λ cos x + μ sin x: λ + 3μ = 0, μ − 3λ = 10, so λ = −3, μ = 1. A + B − 3 = 0 and "
        "−A − 2B + 1 = 0 give A = 5, B = −2. y = 5e⁻ˣ − 2e⁻²ˣ − 3 cos x + sin x. For large x, y ≈ sin x − 3 cos x = "
        "√10 sin(x − α), tan α = 3: an oscillation of amplitude √10.",
        "CF Ae⁻²ˣ; trial λx + μ: λ + 2λx + 2μ = 4x + 1, λ = 2, μ = −½. y = Ae⁻²ˣ + 2x − ½.",
    ],

    "exam": [
        "(a) Find the general solution of d²y/dx² + 4 dy/dx + 5y = 65 sin 2x. [8]\n"
        "(b) Find the particular solution for which y = 0 and dy/dx = 0 when x = 0. [4]\n"
        "(c) For large values of x, the solution is approximately R sin(2x − α). Find R, giving your answer as an exact "
        "value. [2]",

        "The differential equation d²y/dx² + 2k dy/dx + 9y = 0, where k is a real constant, is given.\n"
        "(a) Find the set of values of k for which the general solution contains trigonometric functions. [3]\n"
        "(b) Write down the general solution when k = 3. [2]\n"
        "(c) Given that k = 5, find the particular solution for which y = 0 and dy/dx = 8 when x = 0. [4]\n"
        "(d) For the solution in part (c), find the maximum value of y, to 3 significant figures. [3]",

        "Consider the differential equation d²y/dx² − 4 dy/dx + 4y = 8e²ˣ.\n"
        "(a) Explain why neither λe²ˣ nor λxe²ˣ can be a particular integral. [2]\n"
        "(b) Find a particular integral. [4]\n"
        "(c) Find the solution for which y = 1 and dy/dx = 0 when x = 0. [4]\n"
        "(d) Show that y > 0 for all real x. [2]",

        "(a) Given that kx sin 3x is a particular integral of d²y/dx² + 9y = 12 cos 3x, find k. [3]\n"
        "(b) Hence write down the general solution. [2]\n"
        "(c) Find the solution for which y = 1 when x = 0 and y = π/3 when x = π/6. [3]\n"
        "(d) Describe the behaviour of this solution as x increases. [2]",
    ],
    "exam_answers": [
        "(a) m² + 4m + 5 = 0, m = −2 ± i (M1 A1); CF y = e⁻²ˣ(A cos x + B sin x) (A1). Trial λ cos 2x + μ sin 2x (B1). "
        "Substituting: cos 2x: λ + 8μ = 0; sin 2x: μ − 8λ = 65 (M1 A1) so λ = −8, μ = 1 (A1). "
        "y = e⁻²ˣ(A cos x + B sin x) − 8 cos 2x + sin 2x (A1). (b) y(0) = A − 8 = 0, A = 8 (M1 A1). "
        "y′(0) = −2A + B + 2 = 0, B = 14 (M1 A1). y = e⁻²ˣ(8 cos x + 14 sin x) − 8 cos 2x + sin 2x. "
        "(c) e⁻²ˣ → 0 so y ≈ sin 2x − 8 cos 2x (M1); R = √65 (A1).",
        "(a) m² + 2km + 9 = 0 has complex roots when 4k² − 36 < 0 (M1 A1): −3 < k < 3 (A1). (b) m = −3 repeated: "
        "y = (A + Bx)e⁻³ˣ (B2). (c) m² + 10m + 9 = 0, m = −1, −9 (M1); y = Ae⁻ˣ + Be⁻⁹ˣ (A1); A + B = 0, −A − 9B = 8 (M1), "
        "A = 1, B = −1: y = e⁻ˣ − e⁻⁹ˣ (A1). (d) y′ = −e⁻ˣ + 9e⁻⁹ˣ = 0, e⁸ˣ = 9, x = (ln 9)/8 = 0.275 (M1 A1); "
        "y = 9^(−1/8) − 9^(−9/8) = 0.675 (A1).",
        "(a) The auxiliary equation (m − 2)² = 0 has the repeated root 2, so the CF is (A + Bx)e²ˣ, which contains both "
        "e²ˣ and xe²ˣ; each would give 0 on substitution (B2). (b) Try λx²e²ˣ (M1): y′ = λ(2x + 2x²)e²ˣ, "
        "y″ = λ(2 + 8x + 4x²)e²ˣ (M1); y″ − 4y′ + 4y = 2λe²ˣ = 8e²ˣ (A1); PI = 4x²e²ˣ (A1). (c) y = (A + Bx + 4x²)e²ˣ (M1); "
        "y(0) = A = 1 (A1); y′ = (B + 8x + 2A + 2Bx + 8x²)e²ˣ, y′(0) = B + 2 = 0, B = −2 (M1); y = (4x² − 2x + 1)e²ˣ (A1). "
        "(d) e²ˣ > 0 and 4x² − 2x + 1 has discriminant 4 − 16 < 0 with positive leading coefficient, so it is always "
        "positive (M1 A1).",
        "(a) y = kx sin 3x: y′ = k sin 3x + 3kx cos 3x, y″ = 6k cos 3x − 9kx sin 3x (M1 A1); y″ + 9y = 6k cos 3x, "
        "so k = 2 (A1). (b) y = A cos 3x + B sin 3x + 2x sin 3x (B1 B1). (c) y(0) = A = 1 (B1); x = π/6: cos(π/2) = 0, "
        "sin(π/2) = 1, so B + π/3 = π/3 (M1), B = 0: y = cos 3x + 2x sin 3x (A1). (d) Oscillates with period 2π/3 "
        "and an amplitude that increases without limit (roughly like 2x): resonance (B1 B1).",
    ],
}
