"""Unit B9: First-order differential equations (separable, integrating factor, families of curves, modelling)."""

UNIT = {
    "number": "B9",
    "title": "First-order differential equations",
    "tag": "A level · Edexcel CP 9.1–9.3 · IAL FP2 4.1–4.2 · AQA I1–I3 · OCR A 4.10a–c · OCR MEI Pp19–Pp22, Pc7–Pc10 "
           "· CAIE 9231 P2 2.6 (integrating factor)",
    "notes": [
        ("p", "A differential equation (DE) is an equation that connects a function with its derivatives. Most laws of "
              "science describe how fast something changes, not what it is, so a model usually arrives as a DE. Solving it "
              "means finding the function itself. This unit covers first-order equations: the variables-separable type from "
              "A level Mathematics, and the new integrating-factor method for linear equations. It also shows how to form "
              "DEs from a description, including Newton's second law."),

        ("h2", "9.1 The language of differential equations"),
        ("bullets", [
            "The <b>order</b> of a DE is the order of the highest derivative in it. dy/dx = 3xy is first order; "
            "d²y/dx² + y = 0 is second order.",
            "A DE is <b>linear</b> if y and its derivatives appear only to the first power and are not multiplied together, "
            "e.g. x dy/dx + 2y = sin x. The equation dy/dx = y² is not linear.",
            "The <b>general solution</b> contains arbitrary constants: one for a first-order DE, two for a second-order DE. "
            "It describes a whole <b>family</b> of curves.",
            "A <b>particular solution</b> is one member of the family, picked out by a given condition such as y = 2 when "
            "x = 0 (an <b>initial condition</b> or boundary condition).",
            "To <b>verify</b> a solution, differentiate it and substitute into the DE: both sides must agree for every x.",
        ]),
        ("p", "For example, y = Ae²ˣ − x − ½ is the general solution of dy/dx = 2y + 2x. Check: dy/dx = 2Ae²ˣ − 1, and "
              "2y + 2x = 2Ae²ˣ − 2x − 1 + 2x = 2Ae²ˣ − 1. The two sides agree for every A."),

        ("h2", "9.2 Separating the variables (IAL FP2 4.1; revision for other boards)"),
        ("p", "If a DE can be written as dy/dx = f(x)g(y), divide by g(y) and integrate both sides with respect to x:"),
        ("box", "Separable equations", [
            "dy/dx = f(x)g(y)  ⟹  ∫ 1/g(y) dy = ∫ f(x) dx.",
            "Put one constant on the right-hand side only. Use it straight away if a condition is given.",
            "Where possible make y the subject. If ln|y| = kx + c, then y = Aeᵏˣ with A = ±eᶜ (A may be any constant).",
        ]),
        ("p", "Dividing by g(y) loses any solution with g(y) = 0. For instance y = 0 also satisfies dy/dx = xy² but is not "
              "of the form found by separating. Such constant solutions are rarely asked for, but you should know they exist."),

        ("h2", "9.3 Linear equations and the integrating factor"),
        ("p", "A first-order linear DE can always be put in the <b>standard form</b> dy/dx + P(x)y = Q(x). The left-hand side "
              "looks almost like the derivative of a product. Multiply through by a function I(x) chosen so that it is "
              "exactly one."),
        ("box", "The integrating factor (CP 9.1, IAL 4.2, AQA I1, OCR 4.10c, MEI Pc8–Pc10, CAIE 2.6)", [
            "1. Write the DE in standard form dy/dx + P(x)y = Q(x). The coefficient of dy/dx must be 1.",
            "2. Find the integrating factor I(x) = e^(∫P(x) dx). No constant is needed in this integral.",
            "3. Multiply through: the left-hand side becomes d/dx(I y), so d/dx(I y) = I Q.",
            "4. Integrate: I y = ∫ I Q dx + c. Remember the constant, then divide by I.",
        ]),
        ("p", "<b>Why it works.</b> If I = e^(∫P dx) then dI/dx = P e^(∫P dx) = PI by the chain rule. By the product rule, "
              "d/dx(Iy) = I dy/dx + (dI/dx)y = I dy/dx + PIy = I(dy/dx + Py). So multiplying the standard form by I turns "
              "the left-hand side into an exact derivative. Edexcel says the factor may be quoted without proof."),
        ("p", "Useful simplifications: e^(ln f(x)) = f(x), so ∫P dx = 2 ln x gives I = x², ∫P dx = −ln x gives I = 1/x, "
              "∫tan x dx = ln sec x gives I = sec x, and ∫coth x dx = ln sinh x gives I = sinh x. Take x > 0 (or the "
              "relevant interval) so that the modulus signs can be dropped."),
        ("table", ["Equation", "Standard form P(x)", "Integrating factor"], [
            ["dy/dx − 2y = x²", "−2", "e⁻²ˣ"],
            ["x dy/dx − y = x⁴", "−1/x", "1/x"],
            ["x dy/dx + 2y = 3x", "2/x", "x²"],
            ["dy/dx + y tan x = sec x", "tan x", "sec x"],
            ["dy/dx + y coth x = cosh x", "coth x", "sinh x"],
        ]),
        ("p", "Sometimes the left-hand side is already an exact derivative, e.g. x dy/dx + y = d/dx(xy) or "
              "(1 + x²) dy/dx + 2xy = d/dx((1 + x²)y). Spot these and integrate at once; the integrating factor method "
              "would give the same answer."),

        ("h2", "9.4 General and particular solutions; families of solution curves"),
        ("p", "Each value of the constant gives one <b>solution curve</b>. Sketching several members shows the family "
              "(CP 9.2, IAL 4.1). Look for: the behaviour as x → ±∞, any asymptote, the curve given by c = 0, points "
              "common to all curves, and stationary points (where dy/dx = 0, which you can read from the DE itself). "
              "Through each point where the DE is defined there passes exactly one solution curve, so different members "
              "of the family never cross there."),
        ("figure", "pb09_family_field.png",
         "Direction field of dy/dx + y = x with the solution curves y = x − 1 + ce⁻ˣ for c = −2, −1, 0, 1, 2, 3. "
         "Every curve approaches the line y = x − 1 (the member with c = 0).", 112),

        ("h2", "9.5 Forming differential equations: modelling"),
        ("p", "Translate words into symbols carefully (Edexcel 9.3, AQA I3, OCR 4.10b, MEI Pp19–Pp22). Define every "
              "variable with its units first."),
        ("table", ["Words", "Differential equation"], [
            ["The rate of increase of P is proportional to P", "dP/dt = kP, k > 0"],
            ["θ decreases at a rate proportional to the excess temperature over 20 °C", "dθ/dt = −k(θ − 20), k > 0"],
            ["The depth h decreases at a rate proportional to √h", "dh/dt = −k√h, k > 0"],
            ["Salt flows in at 0.6 kg min⁻¹ and out at (concentration) × (outflow rate)", "dS/dt = 0.6 − 2S/(100 + t)"],
            ["Newton's second law, resultant force F on mass m", "m dv/dt = F, with v = dx/dt"],
        ]),
        ("box", "Kinematics and Newton's second law", [
            "Velocity v = dx/dt; acceleration a = dv/dt = d²x/dt².",
            "a = v dv/dx (chain rule: dv/dt = (dv/dx)(dx/dt)). Use this form when the force depends on displacement x or "
            "you want v in terms of x. (MEI Pp; OCR A excludes this form.)",
            "Newton's second law: F = ma, where F is the resultant force in the direction of motion. Resistances act against "
            "the motion, so enter with a minus sign: m dv/dt = (driving force) − (resistance).",
            "Typical resistances are kv (small speeds) or kv² (high speeds). A variable force such as 6t N or 10e⁻ᵗ N "
            "gives a DE needing the integrating factor.",
        ]),
        ("p", "<b>Mixing problems.</b> If liquid flows into a tank at rate r<sub>in</sub> with concentration c<sub>in</sub> and out at rate "
              "r<sub>out</sub>, and the tank is well stirred, then the amount S of dissolved substance satisfies "
              "dS/dt = r<sub>in</sub>c<sub>in</sub> − r<sub>out</sub> × S/V, where V(t) is the volume at time t. If the flow rates differ, V changes "
              "with t."),
        ("p", "<b>Interpreting and refining.</b> After solving, comment on what the model predicts: long-term behaviour "
              "(e.g. a terminal speed, a steady concentration), whether values stay realistic, and which assumptions "
              "(constant rates, resistance proportional to speed, perfect mixing) might need refining. In an exam, a "
              "criticism must refer to the context."),

        ("h2", "9.6 First-order linear equations with constant coefficients (CAIE link)"),
        ("p", "For dy/dx + ay = f(x) with a constant, the integrating factor is eᵃˣ. Its general solution always splits as "
              "y = Ae⁻ᵃˣ + (a particular function). The first term solves dy/dx + ay = 0 and is the <b>complementary "
              "function</b> (CF); the second is a <b>particular integral</b> (PI). Cambridge asks you to recognise this "
              "structure, which is developed fully for second-order equations in B10."),

        ("warn", "Common mistakes", [
            "Using the integrating factor before dividing by the coefficient of dy/dx: x dy/dx − y = x⁴ must first become "
            "dy/dx − y/x = x³, so P = −1/x, not −1.",
            "Writing e^(∫P dx) = e^(ln x²) as e^(x²), or keeping a modulus that makes the factor awkward. Simplify e^(ln f) = f.",
            "Forgetting the constant when integrating I Q, or adding it after dividing by I. Ixy = ∫IQ dx + c, then divide "
            "every term (including c) by I.",
            "Sign errors with resistance: a resistive force acts against the direction of motion, so it is subtracted.",
            "Giving an expression instead of an equation: the answer is \"y = …\", never just \"x⁴/3 + cx\" (Cambridge "
            "examiners penalise this).",
            "Not using the boundary condition, or using it before the constant has been introduced.",
        ]),
    ],

    "examples": [
        {
            "title": "Integrating factor with an exponential",
            "question": "Find the particular solution of dy/dx + 3y = e²ˣ for which y = 1 when x = 0.",
            "steps": [
                "Standard form already: P = 3, Q = e²ˣ. Integrating factor I = e^(∫3 dx) = e³ˣ.",
                "Multiply through: e³ˣ dy/dx + 3e³ˣ y = e⁵ˣ, i.e. d/dx(y e³ˣ) = e⁵ˣ.",
                "Integrate: y e³ˣ = ⅕e⁵ˣ + c, so y = ⅕e²ˣ + ce⁻³ˣ (general solution).",
                "y(0) = 1: 1 = ⅕ + c, so c = ⅘.",
                "Particular solution: y = ⅕(e²ˣ + 4e⁻³ˣ).",
            ],
        },
        {
            "title": "Putting the equation into standard form",
            "question": "Solve x dy/dx − 2y = x³ sin x for x > 0, given that y = 3π² when x = π.",
            "steps": [
                "Divide by x: dy/dx − (2/x)y = x² sin x, so P = −2/x.",
                "∫P dx = −2 ln x = ln x⁻², so I = x⁻².",
                "Multiply: d/dx(y/x²) = x⁻² × x² sin x = sin x.",
                "Integrate: y/x² = −cos x + c, so y = x²(c − cos x).",
                "x = π: 3π² = π²(c + 1), so c = 2. Hence y = x²(2 − cos x).",
                "Check: dy/dx = 2x(2 − cos x) + x² sin x, so x dy/dx − 2y = 2x²(2 − cos x) + x³ sin x − 2x²(2 − cos x) = x³ sin x. ✓",
            ],
        },
        {
            "title": "A family of solution curves",
            "question": "(a) Find the general solution of x dy/dx + y = 3x² for x ≠ 0. (b) Sketch the members of the "
                        "family for c = −2, 0 and 2, for x > 0. (c) Find the member that passes through (1, 4).",
            "figure": "pb09_family_example.png",
            "caption": "Solution curves y = x² + c/x for c = −2, 0, 2 (x > 0).",
            "width_mm": 95,
            "steps": [
                "(a) The left-hand side is exact: x dy/dx + y = d/dx(xy). So d/dx(xy) = 3x², xy = x³ + c, and y = x² + c/x.",
                "(b) c = 0 gives the parabola y = x². For c > 0, y → +∞ as x → 0⁺ (asymptote x = 0) and the curve has a "
                "minimum where dy/dx = 2x − c/x² = 0, i.e. x = ∛(c/2): for c = 2 this is (1, 3). For c < 0, y → −∞ as "
                "x → 0⁺, the curve is increasing and crosses the x-axis at x = ∛(−c): for c = −2 at x = ∛2 ≈ 1.26. "
                "For large x every curve approaches y = x².",
                "(c) 4 = 1 + c, so c = 3 and the curve is y = x² + 3/x.",
            ],
        },
        {
            "title": "Newton's second law with a variable force",
            "question": "A particle of mass 2 kg moves along a horizontal straight line. At time t seconds it has speed "
                        "v m s⁻¹. It is driven by a force of 6t N in its direction of motion and resisted by a force of "
                        "4v N. It starts from rest. (a) Show that dv/dt + 2v = 3t. (b) Find v in terms of t. (c) Find the "
                        "distance travelled in the first 2 seconds, to 3 significant figures.",
            "steps": [
                "(a) F = ma: 6t − 4v = 2 dv/dt, so dv/dt + 2v = 3t.",
                "(b) I = e²ᵗ. d/dt(v e²ᵗ) = 3t e²ᵗ. By parts, ∫3t e²ᵗ dt = (3t/2)e²ᵗ − ∫(3/2)e²ᵗ dt = (3t/2 − 3/4)e²ᵗ + c.",
                "So v = 3t/2 − 3/4 + ce⁻²ᵗ. v(0) = 0 gives c = 3/4: v = 3t/2 − 3/4 + ¾e⁻²ᵗ.",
                "(c) dv/dt = 3/2 − (3/2)e⁻²ᵗ > 0 for t > 0, so v increases from 0 and never changes sign. Distance = ∫₀² v dt "
                "= [3t²/4 − 3t/4 − ⅜e⁻²ᵗ]₀² = (3 − 1.5 − ⅜e⁻⁴) − (−⅜) = 1.875 − 0.375e⁻⁴ = 1.87 m (3 s.f.).",
                "Interpretation: for large t, v ≈ 1.5t − 0.75, so the speed grows without limit. The model is only "
                "realistic while the driving force 6t can actually be supplied.",
            ],
        },
        {
            "title": "A mixing problem",
            "question": "A tank holds 100 litres of water in which 5 kg of salt is dissolved. Brine containing 0.2 kg of "
                        "salt per litre flows in at 3 litres per minute, and the well-stirred mixture flows out at 2 litres "
                        "per minute. The tank holds 200 litres. Let S kg be the salt in the tank after t minutes. (a) Show "
                        "that dS/dt = 0.6 − 2S/(100 + t). (b) Find S in terms of t. (c) Find the amount of salt when the "
                        "tank becomes full.",
            "steps": [
                "(a) Volume after t minutes: 100 + 3t − 2t = 100 + t litres. Salt in: 3 × 0.2 = 0.6 kg min⁻¹. Salt out: "
                "2 × S/(100 + t) kg min⁻¹. So dS/dt = 0.6 − 2S/(100 + t).",
                "(b) Standard form: dS/dt + 2S/(100 + t) = 0.6. I = e^(2 ln(100 + t)) = (100 + t)².",
                "d/dt(S(100 + t)²) = 0.6(100 + t)², so S(100 + t)² = 0.2(100 + t)³ + c, i.e. S = 0.2(100 + t) + c/(100 + t)².",
                "S(0) = 5: 5 = 20 + c/10 000, so c = −150 000. S = 0.2(100 + t) − 150 000/(100 + t)².",
                "(c) Full when 100 + t = 200, i.e. t = 100: S = 40 − 150 000/40 000 = 36.25 kg.",
                "Check of sense: the concentration 36.25/200 = 0.181 kg per litre is approaching, but still below, the "
                "inflow concentration 0.2 kg per litre.",
            ],
        },
        {
            "title": "Using a = v dv/dx (MEI; Edexcel and AQA mechanics)",
            "question": "A boat of mass 500 kg moving at 10 m s⁻¹ cuts its engine. The water resistance is 20v² N. "
                        "(a) Find the distance it travels while its speed falls to 5 m s⁻¹. (b) Find the time this takes.",
            "steps": [
                "(a) Distance is wanted, so use a = v dv/dx: 500v dv/dx = −20v², i.e. dv/dx = −0.04v (v > 0).",
                "Separate: ∫dv/v = −∫0.04 dx, ln v = −0.04x + c. At x = 0, v = 10, so v = 10e^(−0.04x).",
                "v = 5: e^(−0.04x) = ½, x = 25 ln 2 = 17.3 m (3 s.f.).",
                "(b) Time is wanted, so use a = dv/dt: 500 dv/dt = −20v², dv/dt = −0.04v².",
                "Separate: ∫v⁻² dv = −∫0.04 dt, so −1/v = −0.04t + c. t = 0, v = 10 gives c = −0.1, so 1/v = 0.1 + 0.04t.",
                "v = 5: 0.2 = 0.1 + 0.04t, t = 2.5 s.",
            ],
        },
    ],

    "practice": [
        "Show that y = Ae²ˣ − x − ½ satisfies dy/dx = 2y + 2x for every constant A. State the order of the equation and "
        "explain why one arbitrary constant is expected.",
        "Solve dy/dx = xy², given that y = 1 when x = 0. State the interval of x on which your solution is valid.",
        "Find the particular solution of dy/dx = (1 + y²) cos x for which y = 1 when x = 0.",
        "Find the general solution of dy/dx − 2y = x².",
        "Find the general solution of x dy/dx − y = x⁴, for x > 0.",
        "Find the general solution of dy/dx + y coth x = cosh x, for x > 0.",
        "Solve dy/dx + y tan x = sec x for 0 ≤ x < π/2, given that y = 2 when x = 0.",
        "By recognising an exact derivative, find y in terms of x given (1 + x²) dy/dx + 2xy = 6x² and y = 1 when x = 0.",
        "(a) Find the general solution of dy/dx + y/x = 2 for x > 0. (b) Sketch the solution curves for c = −1, 0 and 1. "
        "(c) Find the member of the family that passes through (2, 3).",
        "A cup of tea at 90 °C is placed in a room at 20 °C. Its temperature θ °C after t minutes satisfies "
        "dθ/dt = −k(θ − 20). After 10 minutes it is at 60 °C. Find k to 3 significant figures, and the time taken for the "
        "tea to cool to 30 °C.",
        "Water leaks from a tank so that the depth h cm decreases at a rate proportional to √h. Initially h = 100, and "
        "after 10 minutes h = 64. Form and solve a differential equation, and find when the tank is empty.",
        "A particle of mass 4 kg moves along a horizontal line from rest. A force of (8 − 2v) N acts in the direction of "
        "motion, where v m s⁻¹ is its speed at time t s. (a) Find v in terms of t and state the terminal speed. (b) Find the "
        "time taken to reach 3 m s⁻¹ and the distance travelled in that time, each to 3 significant figures.",
    ],
    "answers": [
        "dy/dx = 2Ae²ˣ − 1 and 2y + 2x = 2Ae²ˣ − 2x − 1 + 2x = 2Ae²ˣ − 1, equal for all A. First order (highest derivative "
        "dy/dx); a first-order DE needs one integration, giving one constant.",
        "∫y⁻² dy = ∫x dx: −1/y = x²/2 + c, c = −1. y = 2/(2 − x²), valid for −√2 < x < √2.",
        "∫dy/(1 + y²) = ∫cos x dx: arctan y = sin x + c, c = π/4. y = tan(sin x + π/4).",
        "I = e⁻²ˣ; d/dx(ye⁻²ˣ) = x²e⁻²ˣ. ∫x²e⁻²ˣ dx = −e⁻²ˣ(x²/2 + x/2 + 1/4). y = ce²ˣ − x²/2 − x/2 − 1/4.",
        "dy/dx − y/x = x³, I = 1/x; d/dx(y/x) = x², y/x = x³/3 + c, y = x⁴/3 + cx.",
        "I = sinh x; d/dx(y sinh x) = sinh x cosh x; y sinh x = ½sinh²x + c; y = ½sinh x + c cosech x.",
        "I = sec x; d/dx(y sec x) = sec²x; y sec x = tan x + c; y = sin x + c cos x; c = 2: y = sin x + 2 cos x.",
        "d/dx((1 + x²)y) = 6x², (1 + x²)y = 2x³ + c, c = 1: y = (2x³ + 1)/(1 + x²).",
        "(a) I = x: d/dx(xy) = 2x, y = x + c/x. (b) c = 0: the line y = x. c = 1: above the line, y → +∞ as x → 0⁺, "
        "minimum at (1, 2). c = −1: below the line, y → −∞ as x → 0⁺, increasing, crosses the x-axis at x = 1. All approach "
        "y = x as x → ∞. (c) 3 = 2 + c/2, c = 2: y = x + 2/x.",
        "θ = 20 + 70e⁻ᵏᵗ. 40 = 70e⁻¹⁰ᵏ gives k = (1/10) ln(7/4) = 0.0560. 10 = 70e⁻ᵏᵗ: t = (ln 7)/k = 34.8 minutes.",
        "dh/dt = −k√h; ∫h^(−1/2) dh = −∫k dt: 2√h = c − kt. t = 0: c = 20. t = 10: 16 = 20 − 10k, k = 0.4. "
        "So √h = 10 − 0.2t, h = (10 − 0.2t)². Empty when t = 50 minutes.",
        "(a) 4 dv/dt = 8 − 2v, dv/dt + v/2 = 2. I = e^(t/2): v = 4 + ce^(−t/2), c = −4: v = 4(1 − e^(−t/2)). Terminal speed "
        "4 m s⁻¹. (b) 3 = 4 − 4e^(−t/2): t = 2 ln 4 = 2.77 s. x = ∫₀ᵗ v dt = 4t + 8e^(−t/2) − 8 = 8 ln 4 − 6 = 5.09 m.",
    ],

    "exam": [
        "(a) Find the general solution of cos x dy/dx + y sin x = cos³x, for 0 ≤ x < π/2. [5]\n"
        "(b) Find the particular solution for which y = 1 when x = 0. [2]\n"
        "(c) Show that this particular solution has a stationary point at x = π/6, and find the exact value of y there. [4]",

        "A drug is given to a patient through a drip. At time t hours the amount of drug in the body is x mg. The drug "
        "enters at a rate of 6e^(−0.1t) mg per hour and is removed at a rate of 0.25x mg per hour. Initially there is no "
        "drug in the body.\n"
        "(a) Show that dx/dt + 0.25x = 6e^(−0.1t). [2]\n"
        "(b) Solve this differential equation to find x in terms of t. [6]\n"
        "(c) Find the maximum amount of drug in the body, and the time at which it occurs, to 3 significant figures. [4]\n"
        "(d) Describe what the model predicts in the long term. [1]",

        "A skydiver of mass 70 kg falls vertically from rest. While falling she experiences air resistance of magnitude "
        "14v N, where v m s⁻¹ is her speed at time t seconds. Take g = 9.8 m s⁻².\n"
        "(a) Show that dv/dt = 9.8 − 0.2v. [2]\n"
        "(b) Find v in terms of t and state her terminal speed. [5]\n"
        "(c) Find the distance she falls in the first 10 seconds, to 3 significant figures. [3]\n"
        "(d) Suggest one way in which the model for air resistance could be refined. [1]",

        "(a) Find the general solution of x dy/dx + 2y = 4x², for x > 0. [4]\n"
        "(b) Show that for c > 0 each solution curve has a single stationary point, at x = c^(1/4), with y-value 2√c. [4]\n"
        "(c) Sketch on one diagram the solution curves for c = 1, c = 0 and c = −1. [3]",
    ],
    "exam_answers": [
        "(a) Divide by cos x: dy/dx + y tan x = cos²x (M1). I = e^(∫tan x dx) = sec x (M1 A1). d/dx(y sec x) = cos x, "
        "y sec x = sin x + c (M1), y = sin x cos x + c cos x (A1). (b) c = 1: y = cos x(1 + sin x) (M1 A1). "
        "(c) dy/dx = cos²x − sin x(1 + sin x) = 1 − sin x − 2sin²x = (1 − 2 sin x)(1 + sin x) (M1 A1). Zero when "
        "sin x = ½, x = π/6 (A1). y = (√3/2)(3/2) = 3√3/4 (A1).",
        "(a) Rate of change = rate in − rate out: dx/dt = 6e^(−0.1t) − 0.25x (B1 B1). (b) I = e^(0.25t) (M1 A1). "
        "d/dt(xe^(0.25t)) = 6e^(0.15t) (M1), xe^(0.25t) = 40e^(0.15t) + c (A1). x(0) = 0 gives c = −40 (M1). "
        "x = 40(e^(−0.1t) − e^(−0.25t)) (A1). (c) dx/dt = 40(−0.1e^(−0.1t) + 0.25e^(−0.25t)) = 0 (M1) gives "
        "e^(0.15t) = 2.5 (A1), t = (ln 2.5)/0.15 = 6.11 hours (A1); x = 13.0 mg (A1). (d) x → 0 as t → ∞: the drug is "
        "eventually removed completely (B1).",
        "(a) 70 dv/dt = 70 × 9.8 − 14v (M1), dv/dt = 9.8 − 0.2v (A1). (b) Separate or use I = e^(0.2t) (M1): "
        "ve^(0.2t) = 49e^(0.2t) + c (A1), c = −49 (M1), v = 49(1 − e^(−0.2t)) (A1). Terminal speed 49 m s⁻¹ (B1). "
        "(c) x = ∫₀¹⁰ 49(1 − e^(−0.2t)) dt (M1) = [49t + 245e^(−0.2t)]₀¹⁰ = 490 + 245e⁻² − 245 (A1) = 278 m (A1). "
        "(d) e.g. resistance proportional to v² at high speeds; or g varies; or resistance changes when the parachute "
        "opens (B1).",
        "(a) dy/dx + 2y/x = 4x, I = x² (M1 A1); d/dx(x²y) = 4x³, x²y = x⁴ + c (M1), y = x² + c/x² (A1). "
        "(b) dy/dx = 2x − 2c/x³ = 0 (M1) gives x⁴ = c, x = c^(1/4) (one positive root) (A1). y = √c + c/√c (M1) = 2√c (A1). "
        "(c) c = 0: y = x². c = 1: U-shaped, y → ∞ as x → 0⁺, minimum (1, 2), above y = x². c = −1: increasing from −∞, "
        "crosses the x-axis at x = 1, below y = x². All approach y = x² for large x (B3: one mark for each correct curve "
        "with key features).",
    ],
}
