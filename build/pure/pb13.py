UNIT = {
    "number": "B13",
    "title": "Reduction formulae, arc length and surface area",
    "tag": "AQA E7, E8 (A level) · CAIE 9231 P2 2.4 · IAL FP3 4.5, 4.6 · Edexcel FP2 2.1, 2.2 (option paper) · "
           "OCR A Y545 Additional Pure 8.06a, 8.06b · not on OCR MEI",
    "notes": [
        ("h2", "B13.1 Reduction formulae (AQA E8, CAIE 2.4, IAL FP3 4.5, Edexcel FP2 2.1, OCR A 8.06a)"),
        ("p", "Some integrals depend on a whole number n, for example Iₙ = ∫₀¹ xⁿeˣ dx or Iₙ = ∫<sub>0</sub><sup>π/2</sup> sinⁿx dx. "
              "A <b>reduction formula</b> expresses Iₙ in terms of the same integral with a smaller n, such as Iₙ₋₁ or Iₙ₋₂. Using it "
              "again and again brings you down to I₀ or I₁, which you can integrate directly, and then you work back up."),
        ("box", "Deriving and using a reduction formula", [
            "1. Write Iₙ in full, with its limits.",
            "2. Integrate by parts, choosing u so that differentiating it lowers the power (u = xⁿ, u = (ln x)ⁿ, u = sin<sup>n−1</sup>x, …). "
            "Sometimes an identity is enough instead (tanⁿx = tan<sup>n−2</sup>x(sec²x − 1)).",
            "3. Evaluate the boundary term [uv] at the limits. It often simplifies to 0, 1 or e.",
            "4. If Iₙ appears on both sides, collect it. Rearrange into the form asked for, and state the values of n for which it holds.",
            "5. Find I₀ or I₁ directly, then step up. Check a small case by integrating directly.",
        ]),
        ("p", "For example, with Iₙ = ∫₀¹ xⁿeˣ dx, take u = xⁿ and dv/dx = eˣ: Iₙ = [xⁿeˣ]₀¹ − ∫₀¹ nx<sup>n−1</sup>eˣ dx, so "
              "<b>Iₙ = e − nIₙ₋₁</b> for n ≥ 1. OCR A students must learn this method, because it is not in the booklet; on every "
              "board you must be able to derive the formula, not just use it."),
        ("h2", "B13.2 Powers of trigonometric functions"),
        ("p", "<b>Powers of sine or cosine.</b> For Iₙ = ∫<sub>0</sub><sup>π/2</sup> sinⁿx dx write sinⁿx = sin<sup>n−1</sup>x × sin x and "
              "integrate by parts. The boundary term [−cos x sin<sup>n−1</sup>x] is 0 at both limits (n ≥ 2), leaving "
              "(n − 1)∫ sin<sup>n−2</sup>x cos²x dx = (n − 1)(Iₙ₋₂ − Iₙ). Collecting Iₙ gives the Wallis formula."),
        ("box", "Standard reduction formulae", [
            "∫<sub>0</sub><sup>π/2</sup> sinⁿx dx and ∫<sub>0</sub><sup>π/2</sup> cosⁿx dx both satisfy nIₙ = (n − 1)Iₙ₋₂ (n ≥ 2), "
            "with I₀ = π/2 and I₁ = 1.",
            "So I₆ = (5/6)(3/4)(1/2)(π/2) = 5π/32 and I₅ = (4/5)(2/3)(1) = 8/15.",
            "∫<sub>0</sub><sup>π/4</sup> tanⁿx dx: Iₙ + Iₙ₋₂ = 1/(n − 1) (n ≥ 2), with I₀ = π/4 and I₁ = ½ ln 2.",
            "∫₀¹ xⁿeˣ dx: Iₙ = e − nIₙ₋₁. ∫₀¹ e⁻ˣ(1 − x)ⁿ dx: Iₙ = 1 − nIₙ₋₁ (CAIE example).",
        ]),
        ("p", "Harder reduction formulae are set with a hint, for example 'by considering d/dx(tan x sec<sup>n−2</sup>x)' for "
              "∫ secⁿx dx (CAIE), or 'show that sin((n + 2)x) − sin(nx) = 2 cos((n + 1)x) sin x' for ∫ sin(nx)/sin x dx (Edexcel). "
              "Follow the hint: differentiate the given expression, rewrite it in terms of the integrands, and integrate both sides."),
        ("h2", "B13.3 Arc length (AQA E7, CAIE 2.4, IAL FP3 4.6, Edexcel FP2 2.2, OCR A 8.06b)"),
        ("p", "Zoom in on a curve and a short piece of it, of length δs, is almost straight. It is the hypotenuse of a small "
              "triangle with sides δx and δy, so (δs)² ≈ (δx)² + (δy)². Dividing by (δx)² and letting δx → 0 gives "
              "(ds/dx)² = 1 + (dy/dx)². Adding up the pieces (Unit B7) gives the length."),
        ("figure", "pb13_ds.png", "A short arc of length δs is close to the hypotenuse of a triangle with sides δx and δy.", 95),
        ("box", "Arc length s", [
            "Cartesian: s = ∫ₐᵇ √(1 + (dy/dx)²) dx, or s = ∫ √(1 + (dx/dy)²) dy.",
            "Parametric: s = ∫ √((dx/dt)² + (dy/dt)²) dt, with t-limits.",
            "Polar (Edexcel FP2 and CAIE only): s = ∫ √(r² + (dr/dθ)²) dθ, with θ-limits.",
        ]),
        ("p", "Exam curves are chosen so that the square root simplifies. Typically 1 + (dy/dx)² turns out to be a perfect "
              "square: if dy/dx = ½(f − 1/f), then 1 + (dy/dx)² = ¼(f + 1/f)². Other common simplifications are 1 + sinh²x = cosh²x, "
              "1 + tan²x = sec²x and 1 − cos t = 2 sin²(t/2). Expand, simplify, and only then take the square root."),
        ("h2", "B13.4 Area of a surface of revolution"),
        ("p", "When the short arc δs is rotated through 2π about the x-axis it sweeps out a thin band, like a slice of a lampshade, "
              "with radius y and slant width δs. Its area is approximately 2πy δs (circumference × width). Adding the bands gives "
              "the curved surface area. It does not include the flat ends."),
        ("box", "Surface area S (rotation through 2π)", [
            "About the x-axis: S = 2π∫ y ds = 2π∫ₐᵇ y√(1 + (dy/dx)²) dx; parametric S = 2π∫ y√((dx/dt)² + (dy/dt)²) dt.",
            "About the y-axis: replace the radius y by x: S = 2π∫ x ds.",
            "Polar curve about the initial line (Edexcel FP2 only): S = 2π∫ r sin θ √(r² + (dr/dθ)²) dθ.",
        ]),
        ("figure", "pb13_band.png", "Rotating a short arc δs at height y about the x-axis gives a band of area about 2πy δs.", 95),
        ("table", ["Board", "Reduction formulae", "Arc length", "Surface area", "Formulae"], [
            ["Edexcel FP2 (option)", "yes", "Cartesian, parametric, polar", "Cartesian, parametric, polar", "given in booklet"],
            ["IAL FP3", "yes", "Cartesian, parametric", "Cartesian, parametric", "given"],
            ["AQA A level", "yes", "Cartesian, parametric", "Cartesian, parametric", "given"],
            ["OCR A Y545", "yes (method to learn)", "Cartesian, parametric", "Cartesian, parametric", "given"],
            ["CAIE 9231 P2", "yes", "Cartesian, parametric, polar", "Cartesian, parametric", "learn (not in MF19)"],
        ]),
        ("warn", "Common mistakes", [
            "Reduction formulae: losing the boundary term [uv], or evaluating it wrongly (e.g. writing [xⁿeˣ]₀¹ = e − 1 instead of e).",
            "Stepping down the wrong way: with nIₙ = (n − 1)Iₙ₋₂, even n ends at I₀ and odd n at I₁. Do not mix them.",
            "Arc length: forgetting the square root, or the '1 +' in √(1 + (dy/dx)²).",
            "Taking the square root before simplifying: √(a² + b²) is not a + b. Look for a perfect square first.",
            "Surface area: using 2π∫ y dx (that has no ds) or π∫ y² ds (that mixes up area with volume).",
            "Parametric: forgetting the t-limits, or the order of limits; lengths and areas must come out positive.",
            "Polar surface area is Edexcel FP2 only; CAIE asks only for polar arc length.",
        ]),
    ],
    "examples": [
        {
            "title": "A reduction formula by parts",
            "question": "Iₙ = ∫₀¹ xⁿeˣ dx, n ≥ 0.\n(a) Show that Iₙ = e − nIₙ₋₁ for n ≥ 1.\n(b) Hence find I₃ exactly.",
            "steps": [
                "(a) Let u = xⁿ, dv/dx = eˣ, so du/dx = nx<sup>n−1</sup>, v = eˣ.",
                "Iₙ = [xⁿeˣ]₀¹ − ∫₀¹ nx<sup>n−1</sup>eˣ dx = (e − 0) − nIₙ₋₁, as required.",
                "(b) I₀ = ∫₀¹ eˣ dx = e − 1.",
                "I₁ = e − I₀ = 1. I₂ = e − 2I₁ = e − 2. I₃ = e − 3I₂ = e − 3e + 6 = <b>6 − 2e</b> (≈ 0.563).",
                "Check: I₁ = ∫₀¹ xeˣ dx = [xeˣ − eˣ]₀¹ = 0 − (−1) = 1. Also 0 < I₃ < I₂, as expected since 0 ≤ x ≤ 1.",
            ],
        },
        {
            "title": "Wallis's formula",
            "question": "Iₙ = ∫<sub>0</sub><sup>π/2</sup> sinⁿx dx.\n(a) Show that nIₙ = (n − 1)Iₙ₋₂ for n ≥ 2.\n"
                        "(b) Find the exact values of I₆ and I₅.",
            "steps": [
                "(a) Iₙ = ∫ sin<sup>n−1</sup>x sin x dx. Let u = sin<sup>n−1</sup>x, dv/dx = sin x: du/dx = (n − 1)sin<sup>n−2</sup>x cos x, "
                "v = −cos x.",
                "Iₙ = [−cos x sin<sup>n−1</sup>x]<sub>0</sub><sup>π/2</sup> + (n − 1)∫<sub>0</sub><sup>π/2</sup> sin<sup>n−2</sup>x cos²x dx. "
                "The bracket is 0 at both limits.",
                "cos²x = 1 − sin²x, so Iₙ = (n − 1)(Iₙ₋₂ − Iₙ). Collecting: Iₙ + (n − 1)Iₙ = (n − 1)Iₙ₋₂, i.e. nIₙ = (n − 1)Iₙ₋₂.",
                "(b) I₀ = π/2, so I₆ = (5/6)I₄ = (5/6)(3/4)I₂ = (5/6)(3/4)(1/2)(π/2) = <b>5π/32</b>.",
                "I₁ = ∫<sub>0</sub><sup>π/2</sup> sin x dx = 1, so I₅ = (4/5)(2/3)(1) = <b>8/15</b>.",
            ],
        },
        {
            "title": "A reduction formula from an identity",
            "question": "Iₙ = ∫<sub>0</sub><sup>π/4</sup> tanⁿx dx. Show that Iₙ + Iₙ₋₂ = 1/(n − 1) for n ≥ 2, and hence find I₅ exactly.",
            "steps": [
                "tanⁿx = tan<sup>n−2</sup>x(sec²x − 1), so Iₙ = ∫<sub>0</sub><sup>π/4</sup> tan<sup>n−2</sup>x sec²x dx − Iₙ₋₂.",
                "The first integral is [tan<sup>n−1</sup>x/(n − 1)]<sub>0</sub><sup>π/4</sup> = 1/(n − 1) (reverse chain rule). So Iₙ + Iₙ₋₂ = 1/(n − 1).",
                "I₁ = ∫<sub>0</sub><sup>π/4</sup> tan x dx = [ln sec x]<sub>0</sub><sup>π/4</sup> = ln √2 = ½ ln 2.",
                "I₃ = ½ − I₁ = ½ − ½ ln 2. I₅ = ¼ − I₃ = <b>½ ln 2 − ¼</b> (≈ 0.0966).",
            ],
        },
        {
            "title": "Arc length of a Cartesian curve",
            "question": "Find the length of the curve y = x²/4 − ½ ln x from x = 1 to x = e.",
            "steps": [
                "dy/dx = x/2 − 1/(2x), so (dy/dx)² = x²/4 − ½ + 1/(4x²).",
                "1 + (dy/dx)² = x²/4 + ½ + 1/(4x²) = (x/2 + 1/(2x))², a perfect square.",
                "s = ∫₁ᵉ (x/2 + 1/(2x)) dx = [x²/4 + ½ ln x]₁ᵉ = (e²/4 + ½) − ¼ = <b>(e² + 1)/4</b> (≈ 2.10).",
            ],
        },
        {
            "title": "The cycloid: arc length and surface area",
            "question": "The cycloid has parametric equations x = t − sin t, y = 1 − cos t, 0 ≤ t ≤ 2π.\n"
                        "(a) Show that the length of the arch is 8.\n"
                        "(b) The arch is rotated through 2π about the x-axis. Find the area of the surface generated.",
            "figure": "pb13_cycloid.png",
            "caption": "One arch of the cycloid x = t − sin t, y = 1 − cos t.",
            "width_mm": 90,
            "steps": [
                "(a) dx/dt = 1 − cos t, dy/dt = sin t. (dx/dt)² + (dy/dt)² = 1 − 2cos t + cos²t + sin²t = 2(1 − cos t) = 4 sin²(t/2).",
                "For 0 ≤ t ≤ 2π, sin(t/2) ≥ 0, so ds/dt = 2 sin(t/2).",
                "s = ∫<sub>0</sub><sup>2π</sup> 2 sin(t/2) dt = [−4 cos(t/2)]<sub>0</sub><sup>2π</sup> = 4 + 4 = <b>8</b>.",
                "(b) S = 2π∫ y ds = 2π∫<sub>0</sub><sup>2π</sup> (1 − cos t)(2 sin(t/2)) dt = 2π∫ 2 sin²(t/2) × 2 sin(t/2) dt "
                "= 8π∫<sub>0</sub><sup>2π</sup> sin³(t/2) dt.",
                "Put w = t/2: ∫<sub>0</sub><sup>2π</sup> sin³(t/2) dt = 2∫<sub>0</sub><sup>π</sup> sin³w dw = 2[−cos w + ⅓cos³w]<sub>0</sub><sup>π</sup> "
                "= 2 × 4/3 = 8/3.",
                "S = 8π × 8/3 = <b>64π/3</b> (≈ 67.0).",
            ],
        },
        {
            "title": "A polar curve (arc length: Edexcel FP2 and CAIE; surface area: Edexcel FP2 only)",
            "question": "The cardioid C has polar equation r = a(1 + cos θ), where a > 0.\n"
                        "(a) Show that the total length of C is 8a.\n"
                        "(b) The part of C for 0 ≤ θ ≤ π is rotated through 2π about the initial line. Show that the area of the "
                        "surface generated is 32πa²/5.",
            "figure": "pb13_cardioid.png",
            "caption": "The cardioid r = a(1 + cos θ), shown for a = 1.",
            "width_mm": 80,
            "steps": [
                "(a) dr/dθ = −a sin θ. r² + (dr/dθ)² = a²(1 + 2cos θ + cos²θ + sin²θ) = 2a²(1 + cos θ) = 4a²cos²(θ/2).",
                "The curve is symmetric in the initial line, so s = 2∫<sub>0</sub><sup>π</sup> 2a cos(θ/2) dθ (cos(θ/2) ≥ 0 here) "
                "= 2[4a sin(θ/2)]<sub>0</sub><sup>π</sup> = <b>8a</b>.",
                "(b) S = 2π∫<sub>0</sub><sup>π</sup> r sin θ × 2a cos(θ/2) dθ. With r = 2a cos²(θ/2) and sin θ = 2 sin(θ/2)cos(θ/2), "
                "the integrand is 8a² cos⁴(θ/2) sin(θ/2).",
                "∫<sub>0</sub><sup>π</sup> 8a² cos⁴(θ/2) sin(θ/2) dθ = 8a²[−(2/5)cos⁵(θ/2)]<sub>0</sub><sup>π</sup> = 16a²/5.",
                "S = 2π × 16a²/5 = <b>32πa²/5</b>.",
            ],
        },
    ],
    "practice": [
        "Iₙ = ∫ xⁿe²ˣ dx. Show that Iₙ = ½xⁿe²ˣ − ½nIₙ₋₁, and hence find ∫ x²e²ˣ dx.",
        "Iₙ = ∫<sub>0</sub><sup>π/2</sup> cosⁿx dx satisfies nIₙ = (n − 1)Iₙ₋₂. Find the exact values of I₄ and I₃.",
        "Iₙ = ∫₁ᵉ (ln x)ⁿ dx. Show that Iₙ = e − nIₙ₋₁ for n ≥ 1, and find I₃. Explain why your answer equals the value of I₃ in "
        "Worked example B13.1.",
        "(CAIE) Iₙ = ∫₀¹ e⁻ˣ(1 − x)ⁿ dx. Show that Iₙ = 1 − nIₙ₋₁ for n ≥ 1, and find I₃ exactly.",
        "Iₙ = ∫<sub>0</sub><sup>π/2</sup> xⁿ cos x dx. Show that Iₙ = (π/2)ⁿ − n(n − 1)Iₙ₋₂ for n ≥ 2, and find I₂ and I₄.",
        "Find the length of the curve y = ⅔x^(3/2) from x = 0 to x = 3.",
        "Find the exact length of the curve y = ln(cos x) from x = 0 to x = π/4.",
        "Find the length of the curve y = cosh x from x = 0 to x = ln 2.",
        "Find the length of the curve x = t², y = ⅔t³ from t = 0 to t = 2√2.",
        "The astroid x = cos³t, y = sin³t, 0 ≤ t ≤ 2π. (a) Find its total length. (b) The arc for 0 ≤ t ≤ π/2 is rotated through "
        "2π about the x-axis. Find the area of the surface generated.",
        "The arc of y = √x from x = 0 to x = 2 is rotated through 2π about the x-axis. Find the exact surface area.",
        "(Edexcel FP2, CAIE) Find the length of the spiral r = e^θ for 0 ≤ θ ≤ π, to 3 significant figures.",
    ],
    "answers": [
        "u = xⁿ, dv/dx = e²ˣ: Iₙ = ½xⁿe²ˣ − ∫ ½nx<sup>n−1</sup>e²ˣ dx. I₀ = ½e²ˣ, I₁ = ½xe²ˣ − ¼e²ˣ, "
        "I₂ = ½x²e²ˣ − I₁ = e²ˣ(½x² − ½x + ¼) + c.",
        "I₄ = (3/4)(1/2)(π/2) = 3π/16; I₃ = (2/3)(1) = 2/3.",
        "u = (ln x)ⁿ, dv/dx = 1: Iₙ = [x(ln x)ⁿ]₁ᵉ − n∫ (ln x)<sup>n−1</sup> dx = e − nIₙ₋₁. I₀ = e − 1, I₁ = 1, I₂ = e − 2, "
        "I₃ = 6 − 2e. The substitution x = eᵘ turns ∫₁ᵉ (ln x)ⁿ dx into ∫₀¹ uⁿeᵘ du, the integral of Worked example B13.1.",
        "u = (1 − x)ⁿ, dv/dx = e⁻ˣ: Iₙ = [−e⁻ˣ(1 − x)ⁿ]₀¹ − n∫ e⁻ˣ(1 − x)<sup>n−1</sup> dx = 1 − nIₙ₋₁. I₀ = 1 − 1/e, "
        "I₁ = 1/e, I₂ = 1 − 2/e, I₃ = 6/e − 2.",
        "By parts twice; the boundary terms are (π/2)ⁿ and 0. I₀ = 1, I₂ = π²/4 − 2, I₄ = π⁴/16 − 12I₂ = π⁴/16 − 3π² + 24.",
        "∫₀³ √(1 + x) dx = [⅔(1 + x)^(3/2)]₀³ = ⅔(8 − 1) = 14/3.",
        "1 + tan²x = sec²x; ∫<sub>0</sub><sup>π/4</sup> sec x dx = ln(sec x + tan x) = ln(√2 + 1).",
        "1 + sinh²x = cosh²x; ∫ cosh x dx = sinh(ln 2) = ½(2 − ½) = 3/4.",
        "(dx/dt)² + (dy/dt)² = 4t² + 4t⁴, ds/dt = 2t√(1 + t²); s = [⅔(1 + t²)^(3/2)]<sub>0</sub><sup>2√2</sup> = ⅔(27 − 1) = 52/3.",
        "(dx/dt)² + (dy/dt)² = 9sin²t cos²t, so ds/dt = 3|sin t cos t|. (a) 4∫<sub>0</sub><sup>π/2</sup> 3 sin t cos t dt = 6. "
        "(b) 2π∫<sub>0</sub><sup>π/2</sup> sin³t × 3 sin t cos t dt = 6π[sin⁵t/5] = 6π/5.",
        "2π∫₀² √x √(1 + 1/(4x)) dx = 2π∫₀² √(x + ¼) dx = (4π/3)[(x + ¼)^(3/2)]₀² = (4π/3)(27/8 − 1/8) = 13π/3.",
        "r² + (dr/dθ)² = 2e^(2θ); s = ∫<sub>0</sub><sup>π</sup> √2 e^θ dθ = √2(e^π − 1) ≈ 31.3.",
    ],
    "exam": [
        "(CAIE) Iₙ = ∫<sub>0</sub><sup>π/4</sup> secⁿx dx.\n"
        "(a) Show that d/dx(tan x sec<sup>n−2</sup>x) = (n − 1)secⁿx − (n − 2)sec<sup>n−2</sup>x. [3]\n"
        "(b) Hence show that (n − 1)Iₙ = (√2)<sup>n−2</sup> + (n − 2)Iₙ₋₂ for n ≥ 2. [3]\n"
        "(c) Find the exact values of I₄ and I₃. [4]",
        "(Edexcel FP2) Jₙ = ∫<sub>0</sub><sup>π/4</sup> sin(nx)/sin x dx, for positive integers n.\n"
        "(a) Show that sin((n + 2)x) − sin(nx) = 2 cos((n + 1)x) sin x. [2]\n"
        "(b) Hence show that Jₙ₊₂ − Jₙ = (2/(n + 1)) sin((n + 1)π/4). [3]\n"
        "(c) Find the exact value of J₇. [4]\n"
        "(d) Show that ∫<sub>0</sub><sup>π/2</sup> sin(nx)/sin x dx = π/2 for every odd positive integer n. [3]",
        "(a) Find the exact length of the curve y = x²/8 − ln x between x = 1 and x = 4. [5]\n"
        "(b) The arc of the curve y = 2√x between x = 0 and x = 3 is rotated through 2π radians about the x-axis. Find the exact "
        "area of the surface generated. [5]",
        "The curve C has parametric equations x = 3t², y = 3t − t³, −√3 ≤ t ≤ √3. C forms a loop, shown in the diagram.\n"
        "(a) Show that (dx/dt)² + (dy/dt)² = 9(1 + t²)². [3]\n"
        "(b) Find the exact length of the loop. [3]\n"
        "(c) The upper half of the loop (0 ≤ t ≤ √3) is rotated through 2π radians about the x-axis, giving the same surface as rotating the whole loop through π radians. Show that the area of the surface generated is 27π. [5]",
    ],
    "exam_answers": [
        "(a) d/dx = sec²x sec<sup>n−2</sup>x + tan x (n − 2)sec<sup>n−2</sup>x tan x [M1 A1] = secⁿx + (n − 2)sec<sup>n−2</sup>x(sec²x − 1) "
        "= (n − 1)secⁿx − (n − 2)sec<sup>n−2</sup>x [A1].\n"
        "(b) Integrate from 0 to π/4: [tan x sec<sup>n−2</sup>x]<sub>0</sub><sup>π/4</sup> = (n − 1)Iₙ − (n − 2)Iₙ₋₂ [M1]; "
        "the left side is 1 × (√2)<sup>n−2</sup> − 0 [A1]; rearrange [A1].\n"
        "(c) I₂ = [tan x] = 1 [B1]; 3I₄ = 2 + 2I₂ ⇒ I₄ = 4/3 [A1]. I₁ = [ln(sec x + tan x)] = ln(1 + √2) [B1]; 2I₃ = √2 + I₁ ⇒ "
        "I₃ = ½√2 + ½ ln(1 + √2) [A1].",
        "(a) sin A − sin B = 2 cos((A + B)/2) sin((A − B)/2) with A = (n + 2)x, B = nx [M1 A1].\n"
        "(b) Jₙ₊₂ − Jₙ = ∫<sub>0</sub><sup>π/4</sup> 2 cos((n + 1)x) dx [M1] = [2 sin((n + 1)x)/(n + 1)]<sub>0</sub><sup>π/4</sup> [A1] "
        "= (2/(n + 1)) sin((n + 1)π/4) [A1].\n"
        "(c) J₁ = π/4 [B1]; J₃ = J₁ + sin(π/2) = π/4 + 1; J₅ = J₃ + ½ sin π = π/4 + 1 [M1 A1]; J₇ = J₅ + ⅓ sin(3π/2) = π/4 + 2/3 [A1].\n"
        "(d) Over [0, π/2] the same working gives a difference (2/(n + 1)) sin((n + 1)π/2) [M1]; for odd n, n + 1 is even, so this is "
        "0 [A1]; hence every odd n gives the same value as n = 1, which is π/2 [A1].",
        "(a) y′ = x/4 − 1/x [B1]; 1 + y′² = x²/16 + ½ + 1/x² = (x/4 + 1/x)² [M1 A1]; s = ∫₁⁴ (x/4 + 1/x) dx = [x²/8 + ln x]₁⁴ [M1] "
        "= 15/8 + 2 ln 2 [A1].\n"
        "(b) y′ = 1/√x; 1 + y′² = 1 + 1/x [M1]; S = 2π∫₀³ 2√x √(1 + 1/x) dx = 4π∫₀³ √(x + 1) dx [M1 A1] = 4π[⅔(x + 1)^(3/2)]₀³ "
        "[M1] = (8π/3)(8 − 1) = 56π/3 [A1].",
        "(a) dx/dt = 6t, dy/dt = 3 − 3t² [B1]; 36t² + 9 − 18t² + 9t⁴ [M1] = 9(1 + 2t² + t⁴) = 9(1 + t²)² [A1].\n"
        "(b) s = ∫<sub>−√3</sub><sup>√3</sup> 3(1 + t²) dt [M1] = [3t + t³]<sub>−√3</sub><sup>√3</sup> = 2(3√3 + 3√3) [A1] = 12√3 [A1].\n"
        "(c) y ≥ 0 for 0 ≤ t ≤ √3 [B1]: S = 2π∫<sub>0</sub><sup>√3</sup> (3t − t³)·3(1 + t²) dt "
        "[M1] = 6π∫ (3t + 2t³ − t⁵) dt [A1] = 6π[3t²/2 + t⁴/2 − t⁶/6]<sub>0</sub><sup>√3</sup> [M1] = 6π(9/2 + 9/2 − 9/2) = 27π [A1].",
    ],
    "practice_figures": {16: [("pb13_loop.png", "The loop x = 3t², y = 3t − t³, −√3 ≤ t ≤ √3.", 80)]},
}
