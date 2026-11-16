"""Unit B11: Modelling with differential equations — SHM, damping, forced oscillations and coupled systems."""

UNIT = {
    "number": "B11",
    "title": "Modelling with differential equations: SHM, damping and coupled systems",
    "tag": "A level · Edexcel CP 9.7–9.9 · AQA I7–I11 · OCR A 4.10f–h · OCR MEI Pc15–Pc18 · not in IAL or CAIE 9231 "
           "· uses B9 and B10",
    "notes": [
        ("p", "This unit applies the methods of B10 to moving bodies and to interacting populations. Time t is the "
              "independent variable, and dots denote time derivatives: ẋ = dx/dt (velocity) and ẍ = d²x/dt² "
              "(acceleration). The three ideas are simple harmonic motion (no resistance), damped motion (resistance "
              "proportional to velocity, with or without a driving force), and coupled pairs of first-order equations."),

        ("h2", "11.1 Simple harmonic motion"),
        ("box", "SHM (Edexcel 9.7, AQA I7, OCR 4.10f, MEI Pc15)", [
            "A particle moves with <b>simple harmonic motion</b> (SHM) about O if ẍ = −ω²x, where x is its displacement from "
            "O and ω > 0 is constant. The acceleration is always towards O and proportional to the distance from O.",
            "General solution: x = A cos ωt + B sin ωt, which can be written x = R sin(ωt + φ) with R = √(A² + B²).",
            "Amplitude a = R (greatest displacement). Period T = 2π/ω. Frequency 1/T = ω/(2π) oscillations per unit time.",
            "v² = ω²(a² − x²): maximum speed aω at the centre O; maximum acceleration ω²a at the ends x = ±a.",
        ]),
        ("p", "<b>Deriving v² = ω²(a² − x²).</b> Write ẍ = v dv/dx. Then v dv/dx = −ω²x, so ∫v dv = −∫ω²x dx and "
              "½v² = −½ω²x² + c. At the ends of the motion x = ±a and v = 0, so c = ½ω²a², giving v² = ω²(a² − x²)."),
        ("p", "<b>Phase form.</b> x = R sin(ωt + φ): expand to R sin ωt cos φ + R cos ωt sin φ and compare with "
              "A cos ωt + B sin ωt, so R sin φ = A and R cos φ = B, tan φ = A/B. The form x = R cos(ωt − ε) is equally "
              "good. Use whichever makes the question easiest."),
        ("p", "If the centre of oscillation is at x = c rather than at the origin, the equation is ẍ = −ω²(x − c), with "
              "solution x = c + A cos ωt + B sin ωt."),

        ("h2", "11.2 Hooke's law and forming the SHM equation"),
        ("p", "<b>Hooke's law</b> (AQA I10): the tension in a stretched spring or elastic string is proportional to its "
              "extension e: T = ke, where k is the stiffness (N m⁻¹). Mechanics texts also write T = λe/l, where λ is "
              "the modulus of elasticity and l the natural length; then k = λ/l."),
        ("bullets", [
            "<b>Horizontal spring</b>, particle of mass m on a smooth surface, x = extension: the tension pulls back, so "
            "mẍ = −kx, i.e. ẍ = −(k/m)x. This is SHM with ω² = k/m.",
            "<b>Vertical spring</b>: in equilibrium the extension e₀ satisfies ke₀ = mg. Measure x downwards from the "
            "equilibrium position. Then mẍ = mg − k(e₀ + x) = −kx, so again ẍ = −(k/m)x. Gravity only shifts the centre.",
            "Always state the direction you take as positive and draw a force diagram.",
        ]),

        ("h2", "11.3 Damped oscillations"),
        ("p", "Add a resistance proportional to velocity, cẋ (c > 0), acting against the motion (AQA I11). Newton's second "
              "law gives mẍ = −kx − cẋ, so mẍ + cẋ + kx = 0. This is the form ẍ + 2bẋ + ω²x = 0 with 2b = c/m and "
              "ω² = k/m. The auxiliary equation m² + 2bm + ω² = 0 (with roots −b ± √(b² − ω²)) decides the motion "
              "(Edexcel 9.8, AQA I8, OCR 4.10g, MEI Pc16–Pc17)."),
        ("table", ["Condition", "Name", "Solution form", "Motion"], [
            ["b² > ω² (two real negative roots α, β)", "heavy damping (over-damped)", "x = Aeᵅᵗ + Beᵝᵗ",
             "no oscillation; returns slowly to equilibrium, crossing it at most once"],
            ["b² = ω² (repeated root −b)", "critical damping", "x = (A + Bt)e⁻ᵇᵗ",
             "no oscillation; the fastest return to equilibrium without overshooting"],
            ["b² < ω² (roots −b ± qi)", "light damping (under-damped)", "x = e⁻ᵇᵗ(A cos qt + B sin qt)",
             "oscillations with period 2π/q and amplitude decaying like e⁻ᵇᵗ"],
        ]),
        ("figure", "pb11_damping.png",
         "Each solution starts at x = 1 with ẋ = 0. Light damping (ẍ + 2ẋ + 17x = 0) oscillates and decays; critical "
         "damping (ẍ + 8ẋ + 16x = 0) returns fastest without crossing; heavy damping (ẍ + 10ẋ + 16x = 0) returns "
         "slowly.", 112),
        ("p", "In light damping, q = √(ω² − b²) < ω, so damped oscillations are slower than undamped ones. Car "
              "suspensions are designed to be close to critical damping."),

        ("h2", "11.4 Forced vibrations and resonance"),
        ("p", "If a driving force F(t) also acts, mẍ + cẋ + kx = F(t). The general solution is CF + PI (B10). With "
              "damping, the CF decays to zero: it is the <b>transient</b>. The PI remains: it is the <b>steady state</b>, "
              "which oscillates at the driving frequency, not the natural one. Initial conditions affect only the transient."),
        ("p", "Without damping, ẍ + ω²x = P cos pt has PI (P/(ω² − p²)) cos pt when p ≠ ω. The amplitude becomes large as p "
              "approaches ω. When p = ω the PI is (P/(2ω)) t sin ωt, whose amplitude grows without limit: "
              "<b>resonance</b>. In practice, damping or the breakdown of the model limits it (bridges, wine glasses, "
              "engine mounts)."),

        ("h2", "11.5 Coupled first-order systems"),
        ("p", "Two quantities x(t) and y(t) that affect each other's rates of change give a <b>coupled system</b> "
              "(Edexcel 9.9, AQA I9, OCR 4.10h, MEI Pc18):"),
        ("box", "Solving dx/dt = ax + by + f(t), dy/dt = cx + dy + g(t) by elimination", [
            "1. Rearrange the first equation for y: y = (ẋ − ax − f(t))/b.",
            "2. Differentiate it to get ẏ in terms of ẍ, ẋ and t.",
            "3. Substitute both into the second equation to get a second-order DE in x alone. Solve it (CF + PI).",
            "4. Find y from step 1 by differentiating your x. Do not solve a separate DE for y: that would introduce extra, "
            "wrong constants.",
            "5. Use x(0) and y(0) to find the two constants. If needed, ẋ(0) comes from the first equation at t = 0.",
        ]),
        ("p", "<b>Predator–prey models.</b> If x is the number of prey and y the number of predators, the prey are eaten, "
              "so the coefficient of y in ẋ is negative, and predators thrive on prey, so the coefficient of x in ẏ is "
              "positive. Linear models give oscillating populations (complex roots), growth or extinction (real roots). "
              "Plotting y against x gives a <b>trajectory</b> in the phase plane: closed curves mean the populations "
              "repeat periodically. Other coupled models include two connected tanks, competing species, and arms races."),
        ("p", "<b>Interpreting.</b> Numbers of animals must be non-negative: a model predicting x < 0 has broken down at the "
              "time x reaches 0 (extinction). Linear models ignore limits on food and space, and treat populations as "
              "continuous. Expect to criticise models in context."),

        ("warn", "Common mistakes", [
            "Sign errors in forming the equation: tension and resistance both act against the displacement or motion, so "
            "mẍ = −kx − cẋ, not +.",
            "For a vertical spring, measuring x from the natural length instead of from equilibrium and then forgetting the "
            "mg term.",
            "Confusing period 2π/ω with frequency ω/(2π), or using degrees on the calculator for ωt.",
            "Classifying damping with the discriminant of the wrong equation: divide by m first, or use c² compared with 4mk "
            "(heavy if c² > 4mk, critical if c² = 4mk, light if c² < 4mk).",
            "In a coupled system, solving a second DE for y and introducing two new constants. y must come from x.",
            "Forgetting that the steady state of a forced damped system does not depend on the initial conditions.",
        ]),
    ],

    "examples": [
        {
            "title": "Solving the SHM equation",
            "question": "A particle moves on a line with ẍ = −9x. At t = 0, x = 2 m and ẋ = 6 m s⁻¹. (a) Find x in terms of t "
                        "in the form R sin(3t + φ). (b) State the amplitude, period and maximum speed. (c) Find the first "
                        "time at which the particle passes through O.",
            "steps": [
                "(a) ω = 3: x = A cos 3t + B sin 3t, ẋ = −3A sin 3t + 3B cos 3t. t = 0: A = 2, 3B = 6, B = 2.",
                "x = 2 cos 3t + 2 sin 3t = R sin(3t + φ) with R sin φ = 2, R cos φ = 2: R = 2√2, φ = π/4. "
                "x = 2√2 sin(3t + π/4).",
                "(b) Amplitude 2√2 m ≈ 2.83 m; period 2π/3 s ≈ 2.09 s; maximum speed Rω = 6√2 m s⁻¹ ≈ 8.49 m s⁻¹.",
                "(c) x = 0 when 3t + π/4 = π (the first value after π/4), so t = π/4 s ≈ 0.785 s.",
            ],
        },
        {
            "title": "A particle on a vertical spring (Hooke's law)",
            "question": "A particle of mass 0.5 kg hangs in equilibrium from a light spring of stiffness 20 N m⁻¹. It is "
                        "pulled down 0.1 m below equilibrium and released from rest. Take g = 9.8 m s⁻². (a) Find the "
                        "equilibrium extension. (b) Show that the motion is SHM, and find the period and the maximum speed.",
            "steps": [
                "(a) In equilibrium, ke₀ = mg: 20e₀ = 0.5 × 9.8, e₀ = 0.245 m.",
                "(b) Let x m be the displacement below equilibrium (downwards positive). Extension e₀ + x, tension 20(e₀ + x) up.",
                "0.5ẍ = 0.5 × 9.8 − 20(0.245 + x) = −20x, so ẍ = −40x: SHM with ω = √40.",
                "Period 2π/√40 = 0.993 s (3 s.f.). Released from rest at x = 0.1, so x = 0.1 cos(√40 t), amplitude 0.1 m.",
                "Maximum speed aω = 0.1√40 = 0.632 m s⁻¹ (3 s.f.), at the equilibrium position.",
            ],
        },
        {
            "title": "Light, critical and heavy damping",
            "question": "A particle of mass 2 kg is attached to a spring of stiffness 50 N m⁻¹ and moves horizontally "
                        "against a resistance cv N, where v is its speed. (a) Show that 2ẍ + cẋ + 50x = 0 and find the value of c "
                        "for critical damping. (b) For c = 12, find x given x = 0.2 and ẋ = 0 at t = 0. (c) Describe the "
                        "motion when c = 26.",
            "steps": [
                "(a) Spring force −50x and resistance −cẋ: 2ẍ = −50x − cẋ. Critical when the auxiliary equation "
                "2m² + cm + 50 = 0 has a repeated root: c² = 4 × 2 × 50 = 400, c = 20.",
                "(b) c = 12: ẍ + 6ẋ + 25x = 0, m = −3 ± 4i (light damping). x = e⁻³ᵗ(A cos 4t + B sin 4t).",
                "x(0) = A = 0.2; ẋ(0) = −3A + 4B = 0, B = 0.15. x = e⁻³ᵗ(0.2 cos 4t + 0.15 sin 4t) = 0.25e⁻³ᵗ cos(4t − α), "
                "tan α = 0.75. It oscillates with period π/2 s and an amplitude that decays like e⁻³ᵗ.",
                "(c) c = 26: ẍ + 13ẋ + 25x = 0, discriminant 169 − 100 = 69 > 0. Roots (−13 ± √69)/2, both negative: heavy "
                "damping. The particle returns to equilibrium without oscillating.",
            ],
        },
        {
            "title": "Forced damped vibration: transient and steady state",
            "question": "A system is modelled by ẍ + 4ẋ + 4x = 8 cos 2t, with x = 0 and ẋ = 0 when t = 0. Find x and describe "
                        "the motion for large t.",
            "figure": "pb11_forced.png",
            "caption": "x = sin 2t − 2te⁻²ᵗ (solid) and its steady state sin 2t (dashed): the transient dies away within a "
                       "few seconds.",
            "width_mm": 95,
            "steps": [
                "CF: m² + 4m + 4 = 0, m = −2 repeated: x = (A + Bt)e⁻²ᵗ (critical damping).",
                "PI: try λ cos 2t + μ sin 2t. Substituting: cos 2t: −4λ + 8μ + 4λ = 8, so μ = 1; sin 2t: −4μ − 8λ + 4μ = 0, so "
                "λ = 0. PI = sin 2t.",
                "x = (A + Bt)e⁻²ᵗ + sin 2t. x(0) = A = 0. ẋ = (B − 2A − 2Bt)e⁻²ᵗ + 2 cos 2t, ẋ(0) = B + 2 = 0, B = −2.",
                "x = sin 2t − 2te⁻²ᵗ. The transient −2te⁻²ᵗ → 0, so for large t the motion is the steady oscillation "
                "x ≈ sin 2t: amplitude 1, period π, at the driving frequency.",
            ],
        },
        {
            "title": "A predator–prey model",
            "question": "The numbers of prey x and predators y on an island at time t years are modelled by "
                        "ẋ = x − 2y + 100, ẏ = x − y − 50. Initially x = 300 and y = 150. (a) Show that ẍ + x = 200. "
                        "(b) Find x and y in terms of t. (c) Find the smallest number of prey and of predators, and the "
                        "period of the cycle.",
            "figure": "pb11_predator_prey.png",
            "caption": "Left: x and y against t. Right: the trajectory (x, y), an ellipse traced repeatedly, with the "
                       "equilibrium point (200, 150).",
            "width_mm": 150,
            "steps": [
                "(a) From the first equation, y = (x + 100 − ẋ)/2, so ẏ = (ẋ − ẍ)/2.",
                "Substitute in the second: (ẋ − ẍ)/2 = x − (x + 100 − ẋ)/2 − 50. Multiply by 2: ẋ − ẍ = 2x − x − 100 + ẋ − 100, "
                "so ẍ + x = 200.",
                "(b) CF A cos t + B sin t; PI 200. x = 200 + A cos t + B sin t. x(0) = 300: A = 100. "
                "ẋ(0) = 300 − 300 + 100 = 100 from the first equation, so B = 100. x = 200 + 100 cos t + 100 sin t.",
                "y = (x + 100 − ẋ)/2 = (300 + 100 cos t + 100 sin t + 100 sin t − 100 cos t)/2 = 150 + 100 sin t.",
                "(c) 100 cos t + 100 sin t = 100√2 sin(t + π/4), so x varies between 200 ± 100√2: least prey ≈ 58.6, "
                "i.e. about 59 animals. Least number of predators 150 − 100 = 50. Both cycle with period 2π ≈ 6.28 years.",
            ],
        },
    ],

    "practice": [
        "Solve ẍ + 16x = 0 given x = 3 and ẋ = 0 when t = 0. State the period and the maximum speed.",
        "Express 3 cos 2t + 4 sin 2t in the form R sin(2t + φ), with R > 0 and 0 < φ < π/2. State the amplitude of the "
        "motion x = 3 cos 2t + 4 sin 2t.",
        "A particle moves with SHM of amplitude 0.5 m and period 4 s. Find its maximum speed, and its speed when it is "
        "0.3 m from the centre.",
        "Starting from ẍ = −ω²x and using ẍ = v dv/dx, prove that v² = ω²(a² − x²), where a is the amplitude.",
        "A particle of mass 0.2 kg on a smooth horizontal table is attached to a spring of stiffness 80 N m⁻¹. Show that "
        "it moves with SHM and find the period.",
        "Classify the damping in (a) ẍ + 6ẋ + 9x = 0, (b) ẍ + 2ẋ + 10x = 0, (c) ẍ + 10ẋ + 16x = 0. Solve (b) given x = 1 "
        "and ẋ = 0 when t = 0.",
        "The motion of a particle is modelled by ẍ + kẋ + 16x = 0, where k > 0. Find the range of values of k for which "
        "the motion is lightly damped, and the value of k for critical damping.",
        "Solve ẍ + 5ẋ + 4x = 0 given x = 0 and ẋ = 3 when t = 0. Find the greatest displacement and explain why the "
        "particle never passes through the equilibrium position for t > 0.",
        "Solve ẍ + 9x = 5 cos 2t given x = 0 and ẋ = 0 when t = 0.",
        "Find a particular integral of ẍ + 4x = 3 sin 2t, and explain what it shows about the motion.",
        "Solve the coupled system ẋ = x + 2y, ẏ = 2x + y given x = 4 and y = 2 when t = 0.",
        "Two species compete: ẋ = 2x − y, ẏ = −x + 2y, with x(0) = 30, y(0) = 10 (in hundreds). Show that ẍ − 4ẋ + 3x = 0, "
        "find x and y, and describe what happens to each population.",
    ],
    "answers": [
        "ω = 4: x = 3 cos 4t. Period π/2 s; maximum speed 3 × 4 = 12.",
        "R = 5, tan φ = 3/4, φ = 0.644 (3 s.f.): 5 sin(2t + 0.644). Amplitude 5.",
        "ω = 2π/4 = π/2. Maximum speed aω = π/4 = 0.785 m s⁻¹. v = ω√(a² − x²) = (π/2)(0.4) = 0.628 m s⁻¹.",
        "v dv/dx = −ω²x; ½v² = −½ω²x² + c; v = 0 at x = a gives c = ½ω²a²; so v² = ω²(a² − x²).",
        "0.2ẍ = −80x, ẍ = −400x: SHM with ω = 20. Period 2π/20 = π/10 = 0.314 s.",
        "(a) (m + 3)² = 0: critical. (b) m = −1 ± 3i: light. (c) m = −2, −8: heavy. "
        "(b) x = e⁻ᵗ(cos 3t + ⅓ sin 3t).",
        "Light when k² − 64 < 0: 0 < k < 8. Critical when k = 8.",
        "m = −1, −4: x = e⁻ᵗ − e⁻⁴ᵗ. ẋ = 0 when e³ᵗ = 4, t = (ln 4)/3 = 0.462; x = 4^(−1/3) − 4^(−4/3) = 0.472. "
        "x = e⁻ᵗ(1 − e⁻³ᵗ) > 0 for all t > 0, so it never returns to x = 0.",
        "CF A cos 3t + B sin 3t; PI λ cos 2t with 5λ = 5, λ = 1. A + 1 = 0, 3B = 0: x = cos 2t − cos 3t.",
        "Try t(λ cos 2t + μ sin 2t): −4λ sin 2t + 4μ cos 2t = 3 sin 2t, λ = −¾, μ = 0. PI = −¾t cos 2t: the forcing "
        "frequency equals the natural frequency, so the amplitude grows without limit (resonance).",
        "y = (ẋ − x)/2 gives ẍ − 2ẋ − 3x = 0, x = Ae³ᵗ + Be⁻ᵗ, y = Ae³ᵗ − Be⁻ᵗ. A + B = 4, A − B = 2: A = 3, B = 1. "
        "x = 3e³ᵗ + e⁻ᵗ, y = 3e³ᵗ − e⁻ᵗ.",
        "y = 2x − ẋ, ẏ = 2ẋ − ẍ = −x + 4x − 2ẋ, so ẍ − 4ẋ + 3x = 0. x = Aeᵗ + Be³ᵗ, y = 2x − ẋ = Aeᵗ − Be³ᵗ. A + B = 30, "
        "A − B = 10: A = 20, B = 10. x = 20eᵗ + 10e³ᵗ, y = 20eᵗ − 10e³ᵗ. x grows; y = 0 when e²ᵗ = 2, t = ½ ln 2 ≈ 0.347: "
        "species y dies out, after which the model no longer applies.",
    ],

    "exam": [
        "A particle P of mass 2 kg is attached to one end of a horizontal spring of stiffness 26 N m⁻¹ and moves on a "
        "horizontal surface. P experiences a resistance of 8v N, where v m s⁻¹ is its speed. At time t seconds the "
        "displacement of P from its equilibrium position is x m.\n"
        "(a) Show that ẍ + 4ẋ + 13x = 0. [2]\n"
        "(b) State, with a reason, the type of damping. [2]\n"
        "(c) Given that P is released from rest when x = 0.3, find x in terms of t. [5]\n"
        "(d) Find the time at which P first passes through its equilibrium position, to 3 significant figures. [3]\n"
        "(e) State one limitation of the model. [1]",

        "The numbers of prey, x thousand, and predators, y thousand, at time t years are modelled by "
        "ẋ = 2x − 3y, ẏ = x − 2y. Initially x = 2 and y = 4.\n"
        "(a) Show that ẍ = x. [3]\n"
        "(b) Find x in terms of t. [4]\n"
        "(c) Find y in terms of t. [2]\n"
        "(d) Find the time at which the prey die out, and the number of predators at that time, to 3 significant figures. [3]\n"
        "(e) Comment on the model after this time. [1]",

        "A light spring of stiffness 49 N m⁻¹ has one end fixed and a particle of mass 0.5 kg hanging from the other end. "
        "Take g = 9.8 m s⁻².\n"
        "(a) Find the extension of the spring when the particle hangs in equilibrium. [2]\n"
        "The particle is pulled down a further 0.05 m and released from rest. Let x m be its displacement below the "
        "equilibrium position at time t s.\n"
        "(b) Show that ẍ = −98x. [3]\n"
        "(c) Find the period of the motion and the maximum speed, to 3 significant figures. [3]\n"
        "(d) Find the time taken for the particle first to reach a point 0.025 m above the equilibrium position. [3]",

        "A sensor is modelled by ẍ + 2ẋ + 5x = 10 sin t, where x is its displacement at time t, with x = 0 and ẋ = 0 "
        "when t = 0.\n"
        "(a) Find the complementary function and state the type of damping. [3]\n"
        "(b) Find a particular integral. [4]\n"
        "(c) Find x in terms of t. [4]\n"
        "(d) Find the amplitude of the motion for large t. [2]",
    ],
    "exam_answers": [
        "(a) 2ẍ = −26x − 8ẋ (M1) so ẍ + 4ẋ + 13x = 0 (A1). (b) m² + 4m + 13 = 0 has discriminant 16 − 52 < 0 (M1): "
        "light damping (A1). (c) m = −2 ± 3i (M1); x = e⁻²ᵗ(A cos 3t + B sin 3t) (A1); x(0) = A = 0.3 (B1); "
        "ẋ(0) = −2A + 3B = 0 (M1), B = 0.2: x = e⁻²ᵗ(0.3 cos 3t + 0.2 sin 3t) (A1). (d) x = 0 when tan 3t = −1.5 (M1); "
        "3t = π − arctan 1.5 (A1); t = 0.720 s (A1). (e) e.g. resistance may not be proportional to speed; the spring may "
        "not obey Hooke's law for large extensions; friction with the surface ignored (B1).",
        "(a) y = (2x − ẋ)/3 (M1), ẏ = (2ẋ − ẍ)/3 (M1); substituting: 2ẋ − ẍ = 3x − 4x + 2ẋ, so ẍ = x (A1). "
        "(b) x = Aeᵗ + Be⁻ᵗ (M1 A1); y = (2x − ẋ)/3 = ⅓Aeᵗ + Be⁻ᵗ; x(0) = A + B = 2 and y(0) = A/3 + B = 4 (M1) give "
        "A = −3, B = 5: x = 5e⁻ᵗ − 3eᵗ (A1). (c) y = 5e⁻ᵗ − eᵗ (M1 A1). (d) x = 0 when e²ᵗ = 5/3 (M1), "
        "t = ½ ln(5/3) = 0.255 years (A1); y = 5e⁻ᵗ − eᵗ = 2.58, i.e. about 2580 predators (A1). (e) The model would "
        "give negative prey, so it no longer applies; with no prey the predators would decline (B1).",
        "(a) ke₀ = mg: 49e₀ = 0.5 × 9.8 (M1), e₀ = 0.1 m (A1). (b) 0.5ẍ = 0.5 × 9.8 − 49(0.1 + x) (M1 A1) = −49x, so "
        "ẍ = −98x (A1). (c) ω = √98: period 2π/√98 = 0.635 s (M1 A1); maximum speed 0.05√98 = 0.495 m s⁻¹ (A1). "
        "(d) x = 0.05 cos(√98 t) (M1); 0.05 cos(√98 t) = −0.025, cos(√98 t) = −½ (M1); √98 t = 2π/3, t = 0.212 s (A1).",
        "(a) m² + 2m + 5 = 0, m = −1 ± 2i (M1 A1); CF x = e⁻ᵗ(A cos 2t + B sin 2t), light damping (A1). (b) Try "
        "λ cos t + μ sin t (M1): cos t: 4λ + 2μ = 0; sin t: 4μ − 2λ = 10 (M1 A1); λ = −1, μ = 2: PI = 2 sin t − cos t (A1). "
        "(c) x = e⁻ᵗ(A cos 2t + B sin 2t) + 2 sin t − cos t (M1); x(0) = A − 1 = 0, A = 1 (A1); ẋ(0) = −A + 2B + 2 = 0 (M1), "
        "B = −½: x = e⁻ᵗ(cos 2t − ½ sin 2t) + 2 sin t − cos t (A1). (d) The transient decays, x ≈ 2 sin t − cos t (M1); "
        "amplitude √5 ≈ 2.24 (A1).",
    ],
}
