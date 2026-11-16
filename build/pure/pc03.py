"""Unit C3: Further differential equations — reduction by substitution and Taylor-series solutions."""

UNIT = {
    "number": "C3",
    "title": "Further differential equations: substitutions and series solutions",
    "tag": "Edexcel FP1 3.1–3.2 (A level option) · IAL FP2 4.3, 5.2, 6.4 · CAIE 9231 P2 2.6 (substitutions) "
           "· builds on B9, B10 and B3 (Maclaurin series)",
    "notes": [
        ("p", "Many differential equations are not of the types in B9 and B10, but a well-chosen substitution turns them "
              "into one that is: separable, linear first order, or second order with constant coefficients. In an exam the "
              "substitution is given; your job is to carry it through accurately. When no method gives an exact solution, "
              "a Taylor series gives a polynomial approximation near a known point."),

        ("h2", "3.1 The method of substitution"),
        ("box", "Reducing a DE by a given substitution", [
            "1. Differentiate the substitution to express dy/dx (and d²y/dx² if needed) in terms of the new variable.",
            "2. Substitute everything, so that only the new variables remain. Simplify fully.",
            "3. Recognise and solve the new equation (separable, integrating factor, or auxiliary equation).",
            "4. Substitute back to give the answer in the original variables, then apply any conditions.",
        ]),
        ("p", "Questions often say \"show that the substitution … transforms the equation into …\". Every step of that "
              "working must be shown, because the answer is given."),

        ("h2", "3.2 First-order equations"),
        ("table", ["Type of equation", "Substitution", "Resulting equation"], [
            ["homogeneous: dy/dx = f(y/x), e.g. dy/dx = (x + y)/(x − y)", "y = ux, so dy/dx = u + x du/dx",
             "x du/dx = f(u) − u (separable)"],
            ["Bernoulli: dy/dx + P(x)y = Q(x)yⁿ", "z = y^(1−n)", "dz/dx + (1 − n)Pz = (1 − n)Q (linear)"],
            ["dy/dx = f(ax + by + c)", "u = ax + by + c, du/dx = a + b dy/dx", "du/dx = a + b f(u) (separable)"],
        ]),
        ("p", "<b>y = ux.</b> The product rule gives dy/dx = u + x du/dx; never write dy/dx = x du/dx. An equation is "
              "<b>homogeneous</b> in this sense when every term in the numerator and denominator has the same total "
              "degree, so dividing through by a power of x leaves a function of y/x only (CAIE example: y = ux for "
              "dy/dx = (x + y)/(x − y))."),
        ("p", "<b>z = 1/y</b> (a Bernoulli equation with n = 2): dz/dx = −y⁻² dy/dx. Dividing the original equation by y² "
              "puts it in a form where this substitution can be made directly."),

        ("h2", "3.3 Second-order equations: the substitution x = eᵗ"),
        ("p", "An equation of the form ax² d²y/dx² + bx dy/dx + cy = f(x) (an Euler or Cauchy–Euler equation) becomes a "
              "constant-coefficient equation when x = eᵗ, i.e. t = ln x, for x > 0 (CAIE example; IAL 5.2; Edexcel FP1 3.2)."),
        ("box", "Derivatives under x = eᵗ", [
            "dx/dt = eᵗ = x, so dy/dt = (dy/dx)(dx/dt) = x dy/dx. Hence x dy/dx = dy/dt.",
            "d²y/dt² = d/dt(x dy/dx) = (dx/dt) dy/dx + x (d²y/dx²)(dx/dt) = x dy/dx + x² d²y/dx².",
            "Hence x² d²y/dx² = d²y/dt² − dy/dt.",
            "So ax²y″ + bxy′ + cy = f(x) becomes a d²y/dt² + (b − a) dy/dt + cy = f(eᵗ).",
        ]),
        ("p", "After solving in t, replace eᵗ by x, e^(kt) by xᵏ and t by ln x. For example Ae²ᵗ + Be³ᵗ = Ax² + Bx³, and "
              "A cos(3t) = A cos(3 ln x)."),

        ("h2", "3.4 Other second-order substitutions"),
        ("bullets", [
            "<b>y = z/x</b> (or y = zx, y = z eˣ, …): change the dependent variable. For example, x d²y/dx² + 2 dy/dx + 4xy = 0 "
            "becomes d²z/dx² + 4z = 0 with y = z/x, because x d²y/dx² + 2 dy/dx = d²z/dx² (check by differentiating).",
            "<b>z = dy/dx</b>: if y itself does not appear, as in x d²y/dx² + dy/dx = 4x, put z = dy/dx to get a first-order "
            "equation in z (here d/dx(xz) = 4x). Integrate twice.",
            "<b>u = a function of x</b>, given in the question, such as x = sin u or x = eᵗ: change the independent "
            "variable using the chain rule as in 3.3.",
        ]),

        ("h2", "3.5 Taylor-series solutions (Edexcel FP1 3.1, IAL 6.4)"),
        ("p", "If a solution passes through a known point, its Taylor series about that point can be built from the DE "
              "itself. Recall (B3 and C2): y = y(a) + (x − a)y′(a) + (x − a)²y″(a)/2! + (x − a)³y‴(a)/3! + …, which "
              "becomes the Maclaurin series when a = 0."),
        ("box", "The Taylor-series method", [
            "1. Use the given conditions for y(a) (and y′(a) for a second-order DE).",
            "2. Use the DE to find the next derivative at x = a.",
            "3. Differentiate the DE (implicitly, with the product and chain rules) to get y‴, y⁗, …; substitute the values "
            "already found at x = a each time.",
            "4. Write out the series to the required power and use it to estimate y near x = a.",
        ]),
        ("p", "The approximation is good only close to x = a; the error usually grows quickly as |x − a| increases. "
              "An alternative method is to substitute y = a₀ + a₁x + a₂x² + … into the DE and compare coefficients; "
              "it gives the same series."),
        ("figure", "pc03_series.png",
         "The solution of dy/dx = x² + y², y(1) = 1 (solid, found numerically) and its Taylor polynomial of degree 3 "
         "about x = 1 (dashed). They agree closely near x = 1 and then separate.", 105),

        ("warn", "Common mistakes", [
            "With y = ux, writing dy/dx = x du/dx and losing the u term.",
            "Not finishing the job: after a substitution, separate the variables and integrate, and give the answer in the "
            "form asked for (Cambridge examiners' comment).",
            "Under x = eᵗ, writing x² d²y/dx² = d²y/dt² and forgetting the −dy/dt term.",
            "Leaving the answer in t: convert back to x using t = ln x.",
            "In Taylor series, dividing by n instead of n! for the nth term, or forgetting to differentiate a product such "
            "as xy′ with the product rule.",
            "Substituting x = a before differentiating: differentiate the general relation first, then substitute.",
        ]),
    ],

    "examples": [
        {
            "title": "A homogeneous equation with y = ux (CAIE)",
            "question": "Use the substitution y = ux to solve dy/dx = (x + y)/(x − y) for x > 0, given that y = 0 when x = 1.",
            "steps": [
                "dy/dx = u + x du/dx, and (x + y)/(x − y) = (1 + u)/(1 − u).",
                "x du/dx = (1 + u)/(1 − u) − u = (1 + u − u + u²)/(1 − u) = (1 + u²)/(1 − u).",
                "Separate: ∫(1 − u)/(1 + u²) du = ∫1/x dx, so arctan u − ½ ln(1 + u²) = ln x + c.",
                "Substitute u = y/x: arctan(y/x) − ½ ln((x² + y²)/x²) = ln x + c, i.e. arctan(y/x) = ½ ln(x² + y²) + c.",
                "x = 1, y = 0: 0 = 0 + c, so c = 0. Solution: arctan(y/x) = ½ ln(x² + y²).",
                "In polar coordinates this is θ = ln r, i.e. r = e^θ: an equiangular spiral.",
            ],
        },
        {
            "title": "A Bernoulli equation with z = 1/y",
            "question": "Use the substitution z = 1/y to find the general solution of dy/dx + y/x = xy² for x > 0.",
            "steps": [
                "Divide by y²: y⁻² dy/dx + y⁻¹/x = x.",
                "z = y⁻¹ gives dz/dx = −y⁻² dy/dx, so −dz/dx + z/x = x, i.e. dz/dx − z/x = −x.",
                "Integrating factor e^(−ln x) = 1/x: d/dx(z/x) = −1, so z/x = −x + c and z = cx − x².",
                "y = 1/(cx − x²).",
            ],
        },
        {
            "title": "An Euler equation with x = eᵗ",
            "question": "(a) Show that the substitution x = eᵗ transforms x² d²y/dx² − 2x dy/dx + 2y = x³ into "
                        "d²y/dt² − 3 dy/dt + 2y = e³ᵗ. (b) Hence find y in terms of x.",
            "steps": [
                "(a) dy/dt = (dy/dx)(dx/dt) = eᵗ dy/dx = x dy/dx.",
                "d²y/dt² = d/dt(x dy/dx) = (dx/dt)(dy/dx) + x(d²y/dx²)(dx/dt) = x dy/dx + x² d²y/dx².",
                "So x² d²y/dx² = d²y/dt² − dy/dt and x dy/dx = dy/dt. Substituting: d²y/dt² − dy/dt − 2 dy/dt + 2y = e³ᵗ, "
                "i.e. d²y/dt² − 3 dy/dt + 2y = e³ᵗ, as required.",
                "(b) Auxiliary equation m² − 3m + 2 = 0, m = 1, 2: CF Aeᵗ + Be²ᵗ. PI λe³ᵗ: (9 − 9 + 2)λ = 1, λ = ½.",
                "y = Aeᵗ + Be²ᵗ + ½e³ᵗ = Ax + Bx² + ½x³.",
            ],
        },
        {
            "title": "Changing the dependent variable: y = z/x",
            "question": "Show that the substitution y = z/x transforms x d²y/dx² + 2 dy/dx + 4xy = 0 into d²z/dx² + 4z = 0, "
                        "and hence find the general solution for y.",
            "steps": [
                "y = z/x: dy/dx = z′/x − z/x², d²y/dx² = z″/x − 2z′/x² + 2z/x³ (where z′ = dz/dx).",
                "x d²y/dx² = z″ − 2z′/x + 2z/x²; 2 dy/dx = 2z′/x − 2z/x²; 4xy = 4z.",
                "Adding: z″ + 4z = 0, as required.",
                "z = A cos 2x + B sin 2x, so y = (A cos 2x + B sin 2x)/x.",
            ],
        },
        {
            "title": "Taylor series for a second-order equation (Edexcel FP1 3.1)",
            "question": "Given that y″ + xy′ + y = 0 with y = 1 and y′ = 2 at x = 0, find the series solution for y in "
                        "ascending powers of x up to the term in x⁴.",
            "steps": [
                "From the DE, y″ = −xy′ − y, so y″(0) = −0 − 1 = −1.",
                "Differentiate: y‴ = −y′ − xy″ − y′ = −2y′ − xy″, so y‴(0) = −4.",
                "Differentiate again: y⁗ = −2y″ − y″ − xy‴ = −3y″ − xy‴, so y⁗(0) = 3.",
                "y = 1 + 2x + (−1)x²/2! + (−4)x³/3! + 3x⁴/4! = 1 + 2x − ½x² − ⅔x³ + ⅛x⁴.",
            ],
        },
        {
            "title": "Taylor series about a point other than 0",
            "question": "y satisfies dy/dx = x² + y² with y = 1 at x = 1. (a) Find the Taylor series for y in powers of "
                        "(x − 1) up to the term in (x − 1)³. (b) Use it to estimate y at x = 1.1, to 4 decimal places.",
            "steps": [
                "(a) y′(1) = 1 + 1 = 2.",
                "y″ = 2x + 2yy′, so y″(1) = 2 + 2(1)(2) = 6.",
                "y‴ = 2 + 2(y′)² + 2yy″, so y‴(1) = 2 + 8 + 12 = 22.",
                "y = 1 + 2(x − 1) + 3(x − 1)² + (11/3)(x − 1)³.",
                "(b) x − 1 = 0.1: y ≈ 1 + 0.2 + 0.03 + 0.003667 = 1.2337 (4 d.p.). An accurate numerical solution gives "
                "1.2342, so the estimate is good to about 3 decimal places.",
            ],
        },
    ],

    "practice": [
        "Use y = ux to find the general solution of dy/dx = (x² + y²)/(xy) for x > 0, giving y² in terms of x.",
        "Use y = ux to solve x² dy/dx = xy + y² for x > 0, given that y = 1 when x = 1.",
        "Use the substitution z = 1/y to solve dy/dx + y = y²eˣ.",
        "Use the substitution u = x + y to find the general solution of dy/dx = (x + y)².",
        "Show that if x = eᵗ then x dy/dx = dy/dt and x² d²y/dx² = d²y/dt² − dy/dt.",
        "Use x = eᵗ to find the general solution of x² d²y/dx² − 4x dy/dx + 6y = 0 for x > 0.",
        "Use x = eᵗ to find the general solution of x² d²y/dx² + x dy/dx + 9y = 0 for x > 0.",
        "Use x = eᵗ to find the general solution of x² d²y/dx² − x dy/dx + y = ln x for x > 0.",
        "Given dy/dx = x + y² and y = 1 when x = 0, find the Maclaurin series for y up to the term in x³.",
        "Given d²y/dx² = xy, with y = 1 and dy/dx = 0 at x = 0, find the series for y up to the term in x⁶.",
        "y satisfies dy/dx = y/x + x with y = 2 when x = 1. Find the Taylor series of y about x = 1 up to the term in "
        "(x − 1)³. Solve the equation exactly and explain why your series is exact.",
        "Use z = dy/dx to find the general solution of x d²y/dx² + dy/dx = 4x for x > 0.",
    ],
    "answers": [
        "u + xu′ = 1/u + u, so u du = dx/x, u²/2 = ln x + c. y² = 2x² ln x + cx².",
        "u + xu′ = u + u², so du/u² = dx/x, −1/u = ln x + c, c = −1. y = x/(1 − ln x).",
        "Divide by y²: −dz/dx + z = eˣ, so dz/dx − z = −eˣ; d/dx(ze⁻ˣ) = −1; z = (c − x)eˣ. y = e⁻ˣ/(c − x).",
        "du/dx = 1 + u², arctan u = x + c, so y = tan(x + c) − x.",
        "dy/dt = (dy/dx)eᵗ = x dy/dx. d²y/dt² = d/dt(x dy/dx) = x dy/dx + x² d²y/dx² (product and chain rules), so "
        "x² d²y/dx² = d²y/dt² − dy/dt.",
        "d²y/dt² − 5 dy/dt + 6y = 0, m = 2, 3: y = Ax² + Bx³.",
        "d²y/dt² + 9y = 0: y = A cos(3 ln x) + B sin(3 ln x).",
        "d²y/dt² − 2 dy/dt + y = t. CF (A + Bt)eᵗ; PI t + 2. y = (A + B ln x)x + ln x + 2.",
        "y′(0) = 1, y″ = 1 + 2yy′ gives 3, y‴ = 2y′² + 2yy″ gives 8. y = 1 + x + (3/2)x² + (4/3)x³.",
        "y‴ = y + xy′, y⁗ = 2y′ + xy″, y⁽⁵⁾ = 3y″ + xy‴, y⁽⁶⁾ = 4y‴ + xy⁗. At 0: y″ = 0, y‴ = 1, y⁗ = 0, y⁽⁵⁾ = 0, "
        "y⁽⁶⁾ = 4. y = 1 + x³/6 + x⁶/180.",
        "y′(1) = 3, y″ = (xy′ − y)/x² + 1 gives 2, y‴(1) = 0. Series 2 + 3(x − 1) + (x − 1)². Exact: I = 1/x, "
        "d/dx(y/x) = 1, y = x² + x = 2 + 3(x − 1) + (x − 1)². The solution is a quadratic, so every higher derivative is 0.",
        "x dz/dx + z = d/dx(xz) = 4x, xz = 2x² + c, dy/dx = 2x + c/x, y = x² + c ln x + d.",
    ],

    "exam": [
        "(a) Show that the substitution y = ux transforms the differential equation x dy/dx = y + xe^(−y/x) into "
        "x du/dx = e^(−u). [3]\n"
        "(b) Hence find the solution for which y = 0 when x = 1, giving y in terms of x. [5]\n"
        "(c) Find the value of y when x = e, to 3 significant figures. [2]",

        "(a) Show that the substitution x = eᵗ transforms x² d²y/dx² + 3x dy/dx + y = x into "
        "d²y/dt² + 2 dy/dt + y = eᵗ. [5]\n"
        "(b) Find the general solution of the transformed equation, and hence y in terms of x. [5]\n"
        "(c) Find the particular solution for which y = 1 and dy/dx = 0 when x = 1. [3]",

        "The function y satisfies d²y/dx² − 2x dy/dx − 2y = 0, with y = 1 and dy/dx = 1 at x = 0.\n"
        "(a) Show that d³y/dx³ = 2x d²y/dx² + 4 dy/dx. [2]\n"
        "(b) Find a series solution for y in ascending powers of x up to the term in x⁴. [5]\n"
        "(c) Use your series to estimate y at x = 0.2, to 4 decimal places. [2]\n"
        "(d) Explain why the estimate at x = 2 would be unreliable. [1]",

        "(a) Show that the substitution y = z/x transforms x d²y/dx² + 2(x + 1) dy/dx + (x + 2)y = 4eˣ into "
        "d²z/dx² + 2 dz/dx + z = 4eˣ. [5]\n"
        "(b) Hence find the general solution for y. [4]\n"
        "(c) Describe the behaviour of y as x → ∞. [1]",
    ],
    "exam_answers": [
        "(a) dy/dx = u + x du/dx (B1); x(u + x du/dx) = ux + xe^(−u) (M1); x du/dx = e^(−u) (A1). (b) ∫eᵘ du = ∫1/x dx (M1); "
        "eᵘ = ln x + c (A1); x = 1, u = 0: c = 1 (M1); u = ln(1 + ln x) (A1); y = x ln(1 + ln x) (A1). "
        "(c) y = e ln 2 = 1.88 (M1 A1).",
        "(a) dy/dt = x dy/dx (M1 A1); d²y/dt² = x dy/dx + x² d²y/dx² (M1 A1); substituting: d²y/dt² − dy/dt + 3 dy/dt + y "
        "= eᵗ, giving d²y/dt² + 2 dy/dt + y = eᵗ (A1). (b) m = −1 repeated: CF (A + Bt)e⁻ᵗ (M1 A1); PI λeᵗ with 4λ = 1, "
        "λ = ¼ (M1 A1); y = (A + B ln x)/x + x/4 (A1). (c) y(1) = A + ¼ = 1, A = ¾ (B1); "
        "dy/dx = (B − A − B ln x)/x² + ¼, so B − A + ¼ = 0, B = ½ (M1); y = (3 + 2 ln x)/(4x) + x/4 (A1).",
        "(a) Differentiate y″ = 2xy′ + 2y (M1): y‴ = 2y′ + 2xy″ + 2y′ = 2xy″ + 4y′ (A1). (b) y″(0) = 2 (B1); "
        "y‴(0) = 4 (B1); y⁗ = 6y″ + 2xy‴ (M1), y⁗(0) = 12 (A1); y = 1 + x + x² + ⅔x³ + ½x⁴ (A1). "
        "(c) y(0.2) ≈ 1 + 0.2 + 0.04 + 0.005333 + 0.0008 = 1.2461 (M1 A1). (d) The series is truncated; x = 2 is far from "
        "0, so the omitted terms (powers of 2) are large (B1).",
        "(a) dy/dx = z′/x − z/x², d²y/dx² = z″/x − 2z′/x² + 2z/x³ (M1 A1); x d²y/dx² = z″ − 2z′/x + 2z/x²; "
        "2(x + 1) dy/dx = 2z′ − 2z/x + 2z′/x − 2z/x²; (x + 2)y = z + 2z/x (M1 A1); adding gives z″ + 2z′ + z = 4eˣ (A1). "
        "(b) CF (A + Bx)e⁻ˣ (M1 A1); PI eˣ since (1 + 2 + 1)λ = 4 (A1); y = ((A + Bx)e⁻ˣ + eˣ)/x (A1). "
        "(c) The e⁻ˣ terms vanish, so y ≈ eˣ/x, which tends to infinity (B1).",
    ],
}
