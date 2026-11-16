UNIT = {
    "number": "B7",
    "title": "Improper integrals and integrals as limits of sums",
    "tag": "Edexcel CP 5.2 (A level) · AQA E1, E9 (A level) · OCR A 4.08c · OCR MEI Pc1 · CAIE 9231 P2 2.4 (rectangles, bounds "
           "and limits of sums: B7.5–B7.7) · not in the IAL FP units",
    "notes": [
        ("h2", "B7.1 What makes an integral improper"),
        ("p", "The definite integral ∫ₐᵇ f(x) dx was defined for a function that is continuous on a finite interval [a, b]. An "
              "integral is <b>improper</b> if either"),
        ("bullets", [
            "<b>the range is infinite</b>: one or both limits is ∞ or −∞, as in ∫₀<sup>∞</sup> e⁻ˣ dx; or",
            "<b>the integrand is undefined</b> (and unbounded) at a point of the interval: at an end, as in ∫₀² 1/√x dx, or inside it, "
            "as in ∫<sub>−1</sub><sup>1</sup> 1/x² dx.",
        ]),
        ("p", "An improper integral is defined as a <b>limit</b> of ordinary integrals. If the limit exists and is finite, the integral "
              "<b>converges</b> and its value is the limit. If not, the integral <b>diverges</b> (it has no value). Always replace the "
              "troublesome limit by a letter, integrate, and then let the letter tend to its value."),
        ("box", "Definitions (Edexcel CP 5.2, AQA E1, OCR A 4.08c, MEI Pc1)", [
            "Infinite range: ∫ₐ<sup>∞</sup> f(x) dx = lim<sub>t→∞</sub> ∫ₐᵗ f(x) dx. Similarly ∫<sub>−∞</sub><sup>b</sup> f(x) dx = "
            "lim<sub>t→−∞</sub> ∫<sub>t</sub><sup>b</sup> f(x) dx.",
            "f undefined at x = a: ∫ₐᵇ f(x) dx = lim<sub>t→a⁺</sub> ∫ₜᵇ f(x) dx (t approaches a from inside the interval).",
            "f undefined at an interior point c: split, ∫ₐᵇ = ∫ₐᶜ + ∫<sub>c</sub><sup>b</sup>, and treat each part separately. The "
            "integral converges only if <b>both</b> parts converge.",
            "∫<sub>−∞</sub><sup>∞</sup> f(x) dx: split at any convenient point, e.g. 0; both halves must converge.",
        ]),
        ("figure", "pb07_improper.png", "Left: the region under y = 1/x² for x ≥ 1 is infinitely long but has finite area 1. "
                                        "Right: the region under y = 1/√x for 0 < x ≤ 4 is infinitely tall but has finite area 4.", 130),
        ("h2", "B7.2 Infinite ranges"),
        ("p", "∫₁<sup>∞</sup> 1/x² dx = lim<sub>t→∞</sub> [−1/x]₁ᵗ = lim (1 − 1/t) = 1, so it converges. But ∫₁<sup>∞</sup> 1/x dx = lim ln t, which "
              "is infinite, so it diverges, even though 1/x → 0. The integrand tending to 0 is necessary but not enough: it must "
              "tend to 0 fast enough. Comparing powers gives a useful rule."),
        ("box", "Powers of x", [
            "∫₁<sup>∞</sup> x⁻ᵖ dx converges if p > 1 (value 1/(p − 1)) and diverges if p ≤ 1.",
            "∫₀¹ x⁻ᵖ dx converges if p < 1 (value 1/(1 − p)) and diverges if p ≥ 1.",
            "So ∫₀<sup>∞</sup> x⁻ᵖ dx diverges for every p: one end or the other fails.",
        ]),
        ("p", "Exponentials decay faster than any power, so integrals such as ∫₀<sup>∞</sup> e⁻ˣ dx = lim (1 − e⁻ᵗ) = 1 and ∫₀<sup>∞</sup> xⁿe⁻ˣ dx "
              "converge (B7.4). Inverse trigonometric functions also give finite values: ∫₀<sup>∞</sup> 1/(1 + x²) dx = lim arctan t = π/2."),
        ("h2", "B7.3 Integrands that are undefined at a point"),
        ("p", "∫₀² 1/√x dx = lim<sub>t→0⁺</sub> [2√x]ₜ² = 2√2 − 0 = 2√2, so it converges. But ∫₀¹ 1/x dx = lim (0 − ln t) = ∞ "
              "diverges. Watch for points where the integrand is undefined <b>inside</b> the interval, because the integral then "
              "looks ordinary. Working ∫<sub>−1</sub><sup>1</sup> 1/x² dx naively gives [−1/x]<sub>−1</sub><sup>1</sup> = −2, which is "
              "nonsense for a positive integrand. Splitting at 0 shows that both halves diverge, so the integral diverges."),
        ("h2", "B7.4 Two standard limits (AQA E9; used by every board)"),
        ("box", "For any constant k > 0", [
            "xᵏe⁻ˣ → 0 as x → ∞   (an exponential beats any power).",
            "xᵏ ln x → 0 as x → 0⁺   (any positive power beats the logarithm).",
            "Equivalent forms: xᵏ/eˣ → 0 and (ln x)/xᵏ → 0 as x → ∞.",
        ]),
        ("p", "Why they are true: for x > 0, eˣ > x<sup>m</sup>/m! for every positive integer m (it is one term of the series for eˣ). "
              "Choose m > k; then 0 < xᵏe⁻ˣ < m! x<sup>k−m</sup>, which tends to 0. For the second, put x = e⁻ᵘ: as x → 0⁺, "
              "u → ∞ and xᵏ ln x = −u e<sup>−ku</sup> → 0 by the first limit. No board asks for a formal proof."),
        ("p", "These limits are what make integration by parts work on improper integrals. For example ∫₀ᵗ xe⁻ˣ dx = "
              "[−xe⁻ˣ − e⁻ˣ]₀ᵗ = 1 − te⁻ᵗ − e⁻ᵗ → 1, using te⁻ᵗ → 0. And ∫ₜ¹ ln x dx = [x ln x − x]ₜ¹ = −1 − t ln t + t → −1, using "
              "t ln t → 0. Always <b>state</b> the limit you use: it earns a mark."),
        ("h2", "B7.5 Rectangles and areas (CAIE 9231 P2 2.4)"),
        ("p", "Suppose f is positive and <b>decreasing</b> for x ≥ 1. On [r, r + 1] the curve lies between the heights f(r + 1) and "
              "f(r). So a rectangle of width 1 and height f(r) lies above the curve, and one of height f(r + 1) lies below it:"),
        ("box", "Bounding a sum by an integral (f decreasing)", [
            "f(r + 1) < ∫<sub>r</sub><sup>r+1</sup> f(x) dx < f(r).",
            "Adding: Σ<sub>r=2</sub><sup>n</sup> f(r) < ∫₁ⁿ f(x) dx < Σ<sub>r=1</sub><sup>n−1</sup> f(r).",
            "Rearranged: ∫<sub>1</sub><sup>n+1</sup> f(x) dx < Σ<sub>r=1</sub><sup>n</sup> f(r) < f(1) + ∫₁ⁿ f(x) dx.",
            "For an increasing f the inequalities reverse. Always draw the diagram, and say whether the rectangles are above or "
            "below the curve.",
        ]),
        ("figure", "pb07_rect.png", "For the decreasing function y = 1/x, rectangles of width 1 on [r, r + 1] with height 1/r lie "
                                    "above the curve (outlined) and with height 1/(r + 1) lie below it (shaded).", 115),
        ("p", "With f(x) = 1/x this gives the CAIE example: ln(n + 1) < 1 + ½ + ⅓ + … + 1/n < 1 + ln n. Since ln n → ∞, the "
              "harmonic series Σ 1/r diverges, but very slowly: the sum of the first million terms is less than 15."),
        ("h2", "B7.6 Integrals as limits of sums (CAIE 9231 P2 2.4)"),
        ("p", "Split [0, 1] into n strips of width 1/n. The rectangles with heights f(r/n), r = 1, …, n, have total area "
              "(1/n) Σ f(r/n). As n → ∞ the strips get thinner and the total tends to the area under the curve. The same idea gives "
              "the formula for a volume of revolution in Unit A14."),
        ("box", "Limit of a sum", [
            "lim<sub>n→∞</sub> (1/n) Σ<sub>r=1</sub><sup>n</sup> f(r/n) = ∫₀¹ f(x) dx   (f continuous on [0, 1]).",
            "More generally, lim<sub>n→∞</sub> Σ<sub>r=1</sub><sup>n</sup> f(a + rh)h = ∫ₐᵇ f(x) dx, where h = (b − a)/n.",
            "To use it: take out a factor 1/n, write each term as a function of r/n, then replace r/n by x and (1/n)Σ by ∫₀¹.",
        ]),
        ("p", "Example: Σ<sub>r=1</sub><sup>n</sup> 1/(n + r) = (1/n) Σ 1/(1 + r/n) → ∫₀¹ 1/(1 + x) dx = ln 2. This is the CAIE "
              "example Σ (1/n)(1 + r/n)⁻¹ → ∫₀¹ (1 + x)⁻¹ dx."),
        ("h2", "B7.7 Estimating a sum (CAIE)"),
        ("p", "The same inequalities give quick estimates of sums. For an increasing f, such as f(x) = √x, the rectangles reverse: "
              "∫₀ⁿ √x dx < Σ<sub>r=1</sub><sup>n</sup> √r < ∫<sub>1</sub><sup>n+1</sup> √x dx. With n = 100 this gives "
              "666.7 < Σ √r < 676.0; the true value is 671.5 (1 d.p.)."),
        ("warn", "Common mistakes", [
            "Substituting ∞ as if it were a number. Write a limit: replace ∞ by t and let t → ∞.",
            "Missing an interior point where the integrand is undefined, e.g. ∫<sub>−1</sub><sup>2</sup> 1/x² dx. Check the "
            "denominator for zeros inside the interval before integrating.",
            "Claiming convergence because the integrand tends to 0: ∫₁<sup>∞</sup> 1/x dx diverges.",
            "Not stating the standard limit used (te⁻ᵗ → 0 or t ln t → 0); mark schemes usually reward it.",
            "Rectangles: putting the inequality the wrong way round, or using the wrong limits of summation. Draw the diagram.",
        ]),
    ],
    "examples": [
        {
            "title": "Infinite ranges",
            "question": "Determine whether each integral converges, and find its value if it does.\n"
                        "(a) ∫₂<sup>∞</sup> 1/(x² − 1) dx\n(b) ∫₁<sup>∞</sup> 1/√x dx",
            "steps": [
                "(a) 1/(x² − 1) = ½(1/(x − 1) − 1/(x + 1)), so ∫₂ᵗ 1/(x² − 1) dx = ½[ln((x − 1)/(x + 1))]₂ᵗ = "
                "½ ln((t − 1)/(t + 1)) − ½ ln(⅓).",
                "As t → ∞, (t − 1)/(t + 1) = (1 − 1/t)/(1 + 1/t) → 1, so ln((t − 1)/(t + 1)) → 0.",
                "The integral converges to −½ ln(⅓) = <b>½ ln 3</b>.",
                "(b) ∫₁ᵗ x<sup>−½</sup> dx = [2√x]₁ᵗ = 2√t − 2, which → ∞ as t → ∞. The integral <b>diverges</b> (p = ½ ≤ 1).",
            ],
        },
        {
            "title": "Integrands that are undefined at a point",
            "question": "Evaluate, if they exist,\n(a) ∫₀² x/√(4 − x²) dx\n(b) ∫₀³ 1/(x − 1)^(2/3) dx.",
            "steps": [
                "(a) The integrand is undefined at x = 2. ∫₀ᵗ x(4 − x²)<sup>−½</sup> dx = [−√(4 − x²)]₀ᵗ = 2 − √(4 − t²).",
                "As t → 2⁻, √(4 − t²) → 0, so the integral converges to <b>2</b>.",
                "(b) The integrand is undefined at x = 1, inside the interval, so split: ∫₀¹ + ∫₁³. An antiderivative is "
                "3(x − 1)^(1/3).",
                "∫₀ᵗ = 3(t − 1)^(1/3) − 3(−1) → 0 + 3 = 3 as t → 1⁻.  ∫ₛ³ = 3 × 2^(1/3) − 3(s − 1)^(1/3) → 3∛2 as s → 1⁺.",
                "Both parts converge, so the integral converges to <b>3 + 3∛2</b> ≈ 6.78.",
            ],
        },
        {
            "title": "Using the limit xᵏe⁻ˣ → 0",
            "question": "Show that ∫₀<sup>∞</sup> xe^(−2x) dx = ¼, stating any limits you use.",
            "steps": [
                "By parts with u = x, dv/dx = e^(−2x): ∫ xe^(−2x) dx = −½xe^(−2x) + ½∫ e^(−2x) dx = −½xe^(−2x) − ¼e^(−2x).",
                "∫₀ᵗ xe^(−2x) dx = −½te^(−2t) − ¼e^(−2t) + ¼.",
                "As t → ∞, e^(−2t) → 0, and te^(−2t) → 0 because an exponential beats any power (put s = 2t: te^(−2t) = ½se⁻ˢ → 0).",
                "So the integral converges to <b>¼</b>.",
            ],
        },
        {
            "title": "Using the limit xᵏ ln x → 0",
            "question": "Show that ∫₀¹ x ln x dx = −¼.",
            "steps": [
                "ln x is undefined at x = 0, so the integral is improper. Use ∫ₜ¹ with 0 < t < 1.",
                "By parts with u = ln x, dv/dx = x: ∫ x ln x dx = ½x² ln x − ∫ ½x dx = ½x² ln x − ¼x².",
                "∫ₜ¹ x ln x dx = (0 − ¼) − (½t² ln t − ¼t²).",
                "As t → 0⁺, t² ln t → 0 (the standard limit with k = 2) and t² → 0. So the integral converges to <b>−¼</b>.",
                "The value is negative because ln x < 0 on (0, 1).",
            ],
        },
        {
            "title": "Bounding the harmonic series with rectangles (CAIE)",
            "question": "(a) By considering rectangles under and over the curve y = 1/x, show that ln(n + 1) < Σ<sub>r=1</sub><sup>n</sup> "
                        "1/r < 1 + ln n for n ≥ 2.\n(b) Hence find bounds for Σ<sub>r=1</sub><sup>1000</sup> 1/r.",
            "steps": [
                "(a) See the diagram in B7.5. 1/x is decreasing for x > 0. On [r, r + 1] the rectangle of height 1/r lies above the curve, so "
                "Σ<sub>r=1</sub><sup>n</sup> 1/r > ∫<sub>1</sub><sup>n+1</sup> (1/x) dx = ln(n + 1).",
                "The rectangle of height 1/(r + 1) lies below the curve, so Σ<sub>r=2</sub><sup>n</sup> 1/r < ∫₁ⁿ (1/x) dx = ln n. "
                "Add the first term 1 to both sides: Σ<sub>r=1</sub><sup>n</sup> 1/r < 1 + ln n.",
                "(b) ln 1001 < Σ < 1 + ln 1000, i.e. <b>6.909 < Σ < 7.908</b> (3 d.p.). The true value is 7.485 (3 d.p.).",
            ],
        },
        {
            "title": "A limit of a sum (CAIE)",
            "question": "Find lim<sub>n→∞</sub> Σ<sub>r=1</sub><sup>n</sup> n/(n² + r²).",
            "steps": [
                "Take out 1/n: n/(n² + r²) = (1/n) × n²/(n² + r²) = (1/n) × 1/(1 + (r/n)²).",
                "So the sum is (1/n) Σ f(r/n) with f(x) = 1/(1 + x²).",
                "As n → ∞ it tends to ∫₀¹ 1/(1 + x²) dx = [arctan x]₀¹ = <b>π/4</b>.",
                "Check with n = 100: the sum is 0.78289, close to π/4 = 0.78540.",
            ],
        },
    ],
    "practice": [
        "Evaluate ∫₁<sup>∞</sup> 1/x³ dx.",
        "Evaluate ∫₀<sup>∞</sup> e^(−3x) dx.",
        "Show that ∫₁<sup>∞</sup> 1/√x dx diverges, and explain why ∫₁<sup>∞</sup> 1/x^1.5 dx converges.",
        "Evaluate ∫₀⁹ 1/√x dx.",
        "Evaluate ∫₀¹ x^(−1/3) dx.",
        "Evaluate ∫₀<sup>∞</sup> 1/(4 + x²) dx.",
        "Evaluate ∫₀¹ 1/√(1 − x²) dx, explaining why it is improper.",
        "Explain why ∫<sub>−1</sub><sup>1</sup> 1/x³ dx is improper, and determine whether it converges.",
        "Show that ∫₀<sup>∞</sup> xe⁻ˣ dx = 1.",
        "Show that ∫₀¹ ln x dx = −1.",
        "Show that ∫₁<sup>∞</sup> (ln x)/x² dx = 1.",
        "(CAIE) Find (a) lim<sub>n→∞</sub> (1/n³) Σ<sub>r=1</sub><sup>n</sup> r² (b) lim<sub>n→∞</sub> Σ<sub>r=1</sub><sup>n</sup> 1/(n + r).",
    ],
    "answers": [
        "lim [−1/(2x²)]₁ᵗ = ½.",
        "lim [−⅓e^(−3x)]₀ᵗ = ⅓.",
        "∫₁ᵗ x<sup>−½</sup> dx = 2√t − 2 → ∞, so it diverges. For p = 1.5 > 1: ∫₁ᵗ x<sup>−1.5</sup> dx = 2 − 2/√t → 2, converges.",
        "lim [2√x]ₜ⁹ = 6.",
        "lim [(3/2)x^(2/3)]ₜ¹ = 3/2.",
        "lim ½ arctan(t/2) = ½ × π/2 = π/4.",
        "The integrand is undefined at x = 1. lim arcsin t (t → 1⁻) = π/2.",
        "1/x³ is undefined at 0, inside the interval. ∫ₜ¹ x⁻³ dx = ½(1/t² − 1) → ∞ as t → 0⁺, so that part diverges and the "
        "integral diverges (even though the naive answer is 0).",
        "∫₀ᵗ xe⁻ˣ dx = [−xe⁻ˣ − e⁻ˣ]₀ᵗ = 1 − te⁻ᵗ − e⁻ᵗ → 1, since te⁻ᵗ → 0.",
        "∫ₜ¹ ln x dx = [x ln x − x]ₜ¹ = −1 − t ln t + t → −1, since t ln t → 0.",
        "By parts: ∫₁ᵗ (ln x)/x² dx = [−(ln x)/x − 1/x]₁ᵗ = 1 − (ln t)/t − 1/t → 1, since (ln t)/t → 0.",
        "(a) (1/n) Σ (r/n)² → ∫₀¹ x² dx = ⅓ (b) (1/n) Σ 1/(1 + r/n) → ∫₀¹ 1/(1 + x) dx = ln 2.",
    ],
    "exam": [
        "(a) Express 1/(x(x + 2)) in partial fractions. [2]\n"
        "(b) Hence show that ∫₁<sup>∞</sup> 1/(x(x + 2)) dx = ½ ln 3, showing the limiting process clearly. [5]\n"
        "(c) Explain why ∫₁<sup>∞</sup> 1/(x + 2) dx diverges, although the integral in part (b) converges. [2]",
        "(a) Show that ∫₀ᵗ x²e⁻ˣ dx = 2 − (t² + 2t + 2)e⁻ᵗ. [5]\n"
        "(b) Hence evaluate ∫₀<sup>∞</sup> x²e⁻ˣ dx, stating clearly any limits you use. [3]",
        "(a) Explain why ∫₀¹ √x ln x dx is an improper integral. [1]\n"
        "(b) Show that ∫₀¹ √x ln x dx = −4/9. [5]\n"
        "(c) Evaluate ∫₀¹ (ln x)/√x dx. [4]",
        "(CAIE) (a) By considering rectangles and the curve y = 1/√x, show that 2√(n + 1) − 2 < Σ<sub>r=1</sub><sup>n</sup> 1/√r "
        "< 2√n − 1. [5]\n"
        "(b) Hence find bounds for Σ<sub>r=1</sub><sup>10000</sup> 1/√r, giving each to 2 decimal places. [2]\n"
        "(c) By writing (1/√n) Σ<sub>r=1</sub><sup>n</sup> 1/√r as a sum of the form (1/n) Σ f(r/n), or otherwise, find "
        "lim<sub>n→∞</sub> (1/√n) Σ<sub>r=1</sub><sup>n</sup> 1/√r. [3]",
    ],
    "exam_answers": [
        "(a) ½(1/x − 1/(x + 2)) [M1 A1].\n"
        "(b) ∫₁ᵗ = ½[ln(x/(x + 2))]₁ᵗ [M1 A1] = ½ ln(t/(t + 2)) − ½ ln(⅓) [M1]; t/(t + 2) = 1/(1 + 2/t) → 1, so ln → 0 [M1]; "
        "value ½ ln 3 [A1].\n"
        "(c) ∫₁ᵗ 1/(x + 2) dx = ln(t + 2) − ln 3 → ∞ [B1]. In (b) the integrand behaves like 1/x², which falls fast enough, and "
        "the two logarithms cancel as t → ∞ [B1].",
        "(a) ∫ x²e⁻ˣ dx = −x²e⁻ˣ + 2∫ xe⁻ˣ dx [M1 A1] = −x²e⁻ˣ − 2xe⁻ˣ − 2e⁻ˣ [M1 A1]; from 0 to t: 2 − (t² + 2t + 2)e⁻ᵗ [A1].\n"
        "(b) As t → ∞, t²e⁻ᵗ → 0, te⁻ᵗ → 0 and e⁻ᵗ → 0 [B1 B1]; value 2 [A1].",
        "(a) ln x is undefined at x = 0 (and → −∞) [B1].\n"
        "(b) ∫ √x ln x dx = ⅔x^(3/2) ln x − ∫ ⅔x^(1/2) dx [M1 A1] = ⅔x^(3/2) ln x − (4/9)x^(3/2) [A1]; ∫ₜ¹ = −4/9 − ⅔t^(3/2) ln t + "
        "(4/9)t^(3/2) [M1]; t^(3/2) ln t → 0 as t → 0⁺, so the value is −4/9 [A1].\n"
        "(c) ∫ x^(−1/2) ln x dx = 2√x ln x − ∫ 2x^(−1/2) dx = 2√x ln x − 4√x [M1 A1]; ∫ₜ¹ = −4 − 2√t ln t + 4√t [M1]; → −4 as "
        "√t ln t → 0 [A1].",
        "(a) 1/√x is decreasing for x > 0 [B1]. Rectangles of height 1/√r on [r, r + 1] lie above the curve: Σ<sub>1</sub><sup>n</sup> "
        "1/√r > ∫<sub>1</sub><sup>n+1</sup> x<sup>−½</sup> dx = 2√(n + 1) − 2 [M1 A1]. Rectangles of height 1/√r on [r − 1, r] lie "
        "below: Σ<sub>2</sub><sup>n</sup> 1/√r < ∫₁ⁿ x<sup>−½</sup> dx = 2√n − 2, so Σ<sub>1</sub><sup>n</sup> 1/√r < 2√n − 1 [M1 A1].\n"
        "(b) 2√10001 − 2 = 198.01 and 2√10000 − 1 = 199.00, so 198.01 < Σ < 199.00 [B1 B1]. (True value 198.54.)\n"
        "(c) (1/√n) Σ 1/√r = (1/n) Σ (r/n)<sup>−½</sup> [M1] → ∫₀¹ x<sup>−½</sup> dx [M1] = 2 (an improper integral) [A1]. "
        "(Or divide the inequalities in (a) by √n and let n → ∞.)",
    ],
}
