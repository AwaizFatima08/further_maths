UNIT = {
    "number": "A2.1",
    "title": "Cumulative distribution functions and functions of X",
    "tag": "Edexcel FS2 (AS, 2.1–2.4) · AQA A level (SD6, SD7) · OCR A (5.03e–g) · OCR MEI Major (SR22–SR26) · CAIE 9231 P4 (4.1) · IAL S2 background",
    "notes": [
        ("h2", "1.1 The cumulative distribution function"),
        ("p", "Unit AS11 found medians by working out the area to the left of a point. The function that gives this area for every "
              "x is the <b>cumulative distribution function</b> (cdf) of X. It is defined for discrete and continuous variables alike, "
              "and it turns many probability questions into a single substitution."),
        ("box", "Definition and properties of the cdf", [
            "F(x) = P(X ≤ x) = ∫ from −∞ to x of f(t) dt. (The dummy variable t is used because x is now a limit.)",
            "P(a < X ≤ b) = F(b) − F(a), and P(X > a) = 1 − F(a).",
            "F is non-decreasing, F(x) → 0 as x → −∞ and F(x) → 1 as x → ∞. For a continuous X, F is continuous: there are no jumps.",
            "f(x) = F′(x) = dF/dx wherever F is differentiable (f = 0 where F is constant).",
        ]),
        ("h2", "1.2 Finding the cdf from a pdf: write it in full"),
        ("p", "Suppose f(x) is non-zero only on a ≤ x ≤ b. Then F(x) = 0 for x < a, F(x) = ∫ₐˣ f(t) dt for a ≤ x ≤ b, and F(x) = 1 "
              "for x > b. You must give all three parts. Cambridge examiners report that candidates lose marks every year by writing "
              "\"0 otherwise\": F is 1, not 0, above the range."),
        ("p", "For a <b>piecewise</b> pdf, build F one piece at a time. On the second piece, F(x) = (total area of the first piece) "
              "+ ∫ from the join to x of the second formula. If you integrate indefinitely instead, find the constant of integration "
              "from continuity at the join (or from F = 1 at the top end). Two quick checks: F must equal 0 at the bottom end and 1 at "
              "the top end, and the two formulas must agree at each join."),
        ("table", ["Task", "Method", "Check"], [
            ["cdf from pdf", "F(x) = ∫ from lowest value to x of f(t) dt, piece by piece", "F(bottom) = 0, F(top) = 1, F continuous at joins"],
            ["pdf from cdf", "f(x) = F′(x) on each piece; f(x) = 0 where F is 0 or 1", "f ≥ 0 and the pieces cover the domain"],
            ["probability", "P(a < X ≤ b) = F(b) − F(a)", "answer between 0 and 1"],
            ["median, quartile, percentile", "solve F(x) = 0.5, 0.25, 0.75, p/100 on the correct piece", "root lies inside that piece"],
        ]),
        ("h2", "1.3 Finding the pdf from a cdf"),
        ("p", "Differentiate each piece of F. Where F(x) = 0 or 1 the pdf is 0. At a join the derivative may not exist, but a single "
              "point does not affect any probability, so it does not matter which piece includes the join. A cdf with unknown "
              "constants is usually fixed by F(top) = 1 (or F(bottom) = 0) and one further fact, such as continuity at a join or "
              "a given value of f."),
        ("h2", "1.4 Median, quartiles and percentiles from F"),
        ("p", "The median m solves F(m) = 0.5; the quartiles solve F(Q₁) = 0.25 and F(Q₃) = 0.75; the kth percentile solves F(x) = k/100 "
              "(OCR A 5.03f, MEI SR26, CAIE 4.1, Edexcel FS2 2.3). With a piecewise F, first evaluate F at each join to see which "
              "piece contains the answer. If the equation is quadratic, reject the root outside that piece. A common error is to "
              "set the pdf, not the cdf, equal to 0.5."),
        ("h2", "1.5 The continuous uniform (rectangular) distribution"),
        ("p", "X has a continuous uniform distribution on [a, b], written X ~ U(a, b) or R(a, b), when every value in the interval is "
              "equally likely: the pdf is constant. It is a good model when there is no reason to favour any part of an interval, for "
              "example the rounding error when lengths are measured to the nearest cm (U(−0.5, 0.5)), the waiting time for a bus "
              "that runs every 12 minutes when you arrive at a random time (U(0, 12)), or the position of a break in a rod."),
        ("box", "X ~ U(a, b)", [
            "f(x) = 1/(b − a) for a ≤ x ≤ b, 0 otherwise.",
            "F(x) = 0 for x < a;  F(x) = (x − a)/(b − a) for a ≤ x ≤ b;  F(x) = 1 for x > b.",
            "E(X) = (a + b)/2    Var(X) = (b − a)²/12    standard deviation = (b − a)/√12.",
            "P(c < X < d) = (d − c)/(b − a) for a ≤ c < d ≤ b: probability is proportional to length.",
        ]),
        ("p", "<b>Proofs</b> (required by AQA SD7 and Edexcel FS2 2.4; MEI may ask for the derivation; OCR A excludes proofs). "
              "E(X) = ∫ₐᵇ x/(b − a) dx = (b² − a²)/(2(b − a)) = (b − a)(b + a)/(2(b − a)) = (a + b)/2. "
              "E(X²) = ∫ₐᵇ x²/(b − a) dx = (b³ − a³)/(3(b − a)) = (a² + ab + b²)/3. "
              "Then Var(X) = (a² + ab + b²)/3 − (a + b)²/4 = (4a² + 4ab + 4b² − 3a² − 6ab − 3b²)/12 = (a² − 2ab + b²)/12 = (b − a)²/12. "
              "The cdf comes from F(x) = ∫ₐˣ 1/(b − a) dt = (x − a)/(b − a)."),
        ("h2", "1.6 Skewness (Edexcel FS2)"),
        ("p", "Edexcel asks you to describe the skewness of a distribution as positive, negative or zero (symmetrical) and to justify "
              "it. A sketch of the pdf, or a comparison of the mean, median and mode, is the usual justification."),
        ("table", ["Shape of pdf", "Skewness", "Typical order"], [
            ["long tail to the right", "positive", "mode < median < mean"],
            ["symmetrical", "zero (no skew)", "mode = median = mean"],
            ["long tail to the left", "negative", "mean < median < mode"],
        ]),
        ("p", "Some textbooks also quote the measure 3(mean − median)/standard deviation, whose sign gives the direction of skew. It is "
              "not named in the current Edexcel specification, so use it only if a question asks for it; comparing mean, median and "
              "mode is always acceptable. For example, for f(x) = x/4 on 1 ≤ x ≤ 3: mean = 13/6 ≈ 2.167, median = √5 ≈ 2.236, mode = 3, "
              "standard deviation = √(11/36) ≈ 0.553, so mean < median < mode (negative skew) and 3(mean − median)/sd ≈ −0.377."),
        ("h2", "1.7 The distribution of Y = g(X): the cdf method (OCR A 5.03g, CAIE 4.1)"),
        ("p", "Given the distribution of X, you may need the distribution of a related variable such as Y = X³, Y = 1/X or the area "
              "A = πR². The safe method always goes through the cdf. Questions are limited to \"simple cases\", in practice functions "
              "that are increasing or decreasing over the domain."),
        ("box", "Cdf method for Y = g(X)", [
            "1. Find the range of Y from the range of X.",
            "2. Write G(y) = P(Y ≤ y) = P(g(X) ≤ y) and rearrange the inequality to one about X.",
            "   If g is increasing: P(X ≤ g⁻¹(y)) = F(g⁻¹(y)).  If g is decreasing the inequality reverses: P(X ≥ g⁻¹(y)) = 1 − F(g⁻¹(y)).",
            "3. Write G(y) in full (0 below the range, 1 above it). Check G = 0 and G = 1 at the ends of the range of Y.",
            "4. Differentiate to get the pdf of Y: h(y) = G′(y) (Cambridge examiners note that candidates often forget this step).",
        ]),
        ("p", "Because an increasing g keeps the order of values, the median (and every percentile) of Y is g of the median of X. "
              "This is not true of the mean: E(g(X)) is usually not g(E(X)). You can find E(Y) either as ∫ g(x) f(x) dx (Unit AS11) "
              "or as ∫ y h(y) dy using the new pdf; both give the same answer, which is a useful check."),
        ("warn", "Common mistakes", [
            "Writing the cdf as \"0 otherwise\". Write F(x) = 0 below the range and F(x) = 1 above it.",
            "Omitting the constant of integration on the second piece, so that F does not reach 1 at the top.",
            "Setting f(x) = 0.5 to find a median, instead of F(x) = 0.5.",
            "Solving a quadratic for a percentile and keeping the root outside the piece (or outside the domain).",
            "For Y = g(X) with g decreasing, forgetting to reverse the inequality, so G(y) decreases from 1 to 0.",
            "Stopping at the cdf of Y when the question asks for its pdf.",
            "Describing skew from the sign of the mean rather than from the shape or the order of mean, median and mode.",
        ]),
    ],
    "examples": [
        {
            "title": "The cdf in full, a probability and a quartile",
            "question": "X has pdf f(x) = (3/8)x² for 0 ≤ x ≤ 2, and 0 otherwise. Find the cdf F(x), and use it to find P(0.5 < X ≤ 1.5) "
                        "and the upper quartile.",
            "steps": [
                "For 0 ≤ x ≤ 2: F(x) = ∫₀ˣ (3/8)t² dt = x³/8.",
                "So F(x) = 0 for x < 0;  F(x) = x³/8 for 0 ≤ x ≤ 2;  F(x) = 1 for x > 2. Check: F(0) = 0, F(2) = 1.",
                "P(0.5 < X ≤ 1.5) = F(1.5) − F(0.5) = (3.375 − 0.125)/8 = 0.40625.",
                "Upper quartile: x³/8 = 0.75, so x³ = 6 and Q₃ = 1.82 (3 s.f.).",
            ],
        },
        {
            "title": "The cdf of a piecewise pdf",
            "question": "X has pdf f(x) = x/3 for 0 ≤ x ≤ 2, f(x) = (2/3)(3 − x) for 2 < x ≤ 3, and 0 otherwise. Find F(x), the median "
                        "and the upper quartile.",
            "steps": [
                "First piece: F(x) = ∫₀ˣ t/3 dt = x²/6 for 0 ≤ x ≤ 2. F(2) = 4/6 = 2/3.",
                "Second piece: F(x) = 2/3 + ∫₂ˣ (2/3)(3 − t) dt = 2/3 + (2/3)[3t − t²/2]₂ˣ = 2/3 + (2/3)(3x − x²/2 − 4) = 2x − x²/3 − 2.",
                "Check: at x = 2, 4 − 4/3 − 2 = 2/3 ✓; at x = 3, 6 − 3 − 2 = 1 ✓.",
                "F(x) = 0 for x < 0; x²/6 for 0 ≤ x ≤ 2; 2x − x²/3 − 2 for 2 < x ≤ 3; 1 for x > 3.",
                "Median: F(2) = 2/3 > 0.5, so it is in the first piece: m²/6 = 0.5, m = √3 = 1.73 (3 s.f.).",
                "Upper quartile: 0.75 > 2/3, so use the second piece: 2x − x²/3 − 2 = 0.75, i.e. x² − 6x + 8.25 = 0. "
                "x = 3 ± √0.75. Only 3 − √0.75 = 2.13 (3 s.f.) lies in (2, 3].",
            ],
        },
        {
            "title": "The pdf from a cdf, and skewness",
            "question": "X has cdf F(x) = 0 for x < 1, F(x) = (x² − 1)/8 for 1 ≤ x ≤ 3, F(x) = 1 for x > 3. Find the pdf, P(X > 2), "
                        "the median, the mode and E(X), and describe the skewness of X.",
            "steps": [
                "f(x) = F′(x) = x/4 for 1 ≤ x ≤ 3, and 0 otherwise.",
                "P(X > 2) = 1 − F(2) = 1 − 3/8 = 5/8.",
                "Median: (m² − 1)/8 = 0.5, m² = 5, m = √5 = 2.24 (3 s.f.).",
                "f is increasing on [1, 3], so the mode is 3.",
                "E(X) = ∫₁³ x²/4 dx = (27 − 1)/12 = 13/6 = 2.17 (3 s.f.).",
                "Mean 2.17 < median 2.24 < mode 3, so X has negative skew (the pdf rises to the right, with a longer tail on the left).",
            ],
        },
        {
            "title": "A continuous uniform model",
            "question": "Buses leave a stop every 12 minutes. Ana arrives at a random time, and W minutes is her waiting time. "
                        "(a) State a suitable distribution for W and write down its cdf. (b) Find E(W), the standard deviation of W and "
                        "P(W > 9). (c) Ana catches this bus on 5 independent days. Find the probability that she waits more than 9 minutes on at least 2 days.",
            "steps": [
                "(a) Every waiting time between 0 and 12 is equally likely, so W ~ U(0, 12). F(w) = 0 for w < 0; w/12 for 0 ≤ w ≤ 12; 1 for w > 12.",
                "(b) E(W) = (0 + 12)/2 = 6 minutes. Var(W) = 12²/12 = 12, so the standard deviation is √12 = 3.46 minutes (3 s.f.).",
                "P(W > 9) = 1 − 9/12 = 0.25.",
                "(c) Let N be the number of days with a wait over 9 minutes: N ~ B(5, 0.25).",
                "P(N ≥ 2) = 1 − 0.75⁵ − 5 × 0.25 × 0.75⁴ = 1 − 0.2373 − 0.3955 = 0.367 (3 s.f.).",
            ],
        },
        {
            "title": "The cdf of Y = X³ (an increasing function)",
            "question": "X has pdf f(x) = 2x for 0 ≤ x ≤ 1. Find the cdf and pdf of Y = X³, the median of Y, and E(Y) by two methods.",
            "steps": [
                "F(x) = x² for 0 ≤ x ≤ 1. Since 0 ≤ X ≤ 1, 0 ≤ Y ≤ 1.",
                "G(y) = P(X³ ≤ y) = P(X ≤ y^(1/3)) = (y^(1/3))² = y^(2/3) for 0 ≤ y ≤ 1; G(y) = 0 for y < 0 and 1 for y > 1.",
                "pdf of Y: h(y) = G′(y) = (2/3)y^(−1/3) for 0 < y ≤ 1, and 0 otherwise.",
                "Median of Y: y^(2/3) = 0.5, so y = 0.5^1.5 = 0.354 (3 s.f.). This equals (median of X)³ = (1/√2)³, as it should.",
                "E(Y) = E(X³) = ∫₀¹ x³ × 2x dx = 2/5. Check: ∫₀¹ y × (2/3)y^(−1/3) dy = (2/3) × (3/5) = 2/5 ✓.",
            ],
        },
        {
            "title": "The cdf of Y = 6/X (a decreasing function)",
            "question": "X has pdf f(x) = x/4 for 1 ≤ x ≤ 3 (cdf F(x) = (x² − 1)/8). Let Y = 6/X. Find the cdf and pdf of Y, and E(Y).",
            "steps": [
                "When x runs from 1 to 3, y = 6/x runs from 6 down to 2, so 2 ≤ Y ≤ 6.",
                "G(y) = P(6/X ≤ y) = P(X ≥ 6/y), reversing the inequality because 6/x is decreasing.",
                "G(y) = 1 − F(6/y) = 1 − (36/y² − 1)/8 = 9/8 − 9/(2y²) for 2 ≤ y ≤ 6; G(y) = 0 for y < 2 and 1 for y > 6. Check: G(2) = 0, G(6) = 1.",
                "h(y) = G′(y) = 9/y³ for 2 ≤ y ≤ 6, and 0 otherwise.",
                "E(Y) = ∫₂⁶ 9/y² dy = 9(1/2 − 1/6) = 3. Check: E(6/X) = ∫₁³ (6/x)(x/4) dx = 3 ✓.",
            ],
        },
    ],
    "practice": [
        "X has pdf f(x) = x/2 for 0 ≤ x ≤ 2. Find the cdf of X in full, and use it to find P(0.5 < X < 1.5).",
        "X has pdf f(x) = 3x² for 0 ≤ x ≤ 1. Find F(x), the median and the 90th percentile.",
        "X has cdf F(x) = 0 for x < 0, F(x) = x²(3 − x)/4 for 0 ≤ x ≤ 2, F(x) = 1 for x > 2. Find the pdf, P(X < 0.5), "
        "the median and the mode.",
        "X has cdf F(x) = ax² + bx for 0 ≤ x ≤ 2 (0 below, 1 above), and f(2) = 0. Find a and b, the pdf and the median.",
        "X has pdf f(x) = x/8 for 0 ≤ x ≤ 2, f(x) = 1/4 for 2 < x ≤ 5, and 0 otherwise. Find F(x) in full, the lower quartile, "
        "the median and P(1 < X < 3).",
        "X ~ U(−2, 4). Write down the pdf and cdf, and find E(X), Var(X) and P(X < 0).",
        "X ~ U(a, b) with E(X) = 5 and Var(X) = 3. Find a and b, and P(X > 6.5).",
        "Lengths are measured to the nearest millimetre. The rounding error E mm is modelled as U(−0.5, 0.5). Find the standard "
        "deviation of E and the probability that the error is more than 0.3 mm in size.",
        "X has pdf f(x) = 2(1 − x) for 0 ≤ x ≤ 1. Find the mean, median and mode, and describe the skewness of X, giving a reason.",
        "X ~ U(0, 2) and Y = X². Find the cdf and pdf of Y, P(Y > 1) and E(Y).",
        "X has pdf f(x) = 3x²/8 for 0 ≤ x ≤ 2, and Y = X³. Show that Y has a continuous uniform distribution, and state E(Y) and Var(Y).",
        "X has pdf f(x) = 2x for 0 ≤ x ≤ 1, and Y = 1 − X². Find the cdf of Y and identify its distribution.",
    ],
    "answers": [
        "F(x) = 0 for x < 0; x²/4 for 0 ≤ x ≤ 2; 1 for x > 2. P(0.5 < X < 1.5) = (2.25 − 0.25)/4 = 0.5.",
        "F(x) = 0 for x < 0; x³ for 0 ≤ x ≤ 1; 1 for x > 1. Median = 0.5^(1/3) = 0.794; 90th percentile = 0.9^(1/3) = 0.965 (3 s.f.).",
        "f(x) = F′(x) = (6x − 3x²)/4 = (3/4)x(2 − x) for 0 ≤ x ≤ 2, 0 otherwise. P(X < 0.5) = 0.25 × 2.5/4 = 0.15625. "
        "F(1) = 2/4 = 0.5, so the median is 1. The pdf is symmetrical about 1 with its maximum there, so the mode is 1.",
        "F(2) = 4a + 2b = 1 and f(x) = 2ax + b with f(2) = 4a + b = 0. Subtracting, b = 1, a = −1/4. f(x) = 1 − x/2 for 0 ≤ x ≤ 2. "
        "Median: x − x²/4 = 0.5, x² − 4x + 2 = 0, x = 2 − √2 = 0.586 (3 s.f.).",
        "F(x) = 0 for x < 0; x²/16 for 0 ≤ x ≤ 2; (x − 1)/4 for 2 < x ≤ 5; 1 for x > 5. F(2) = 1/4, so Q₁ = 2. "
        "Median: (x − 1)/4 = 0.5, x = 3. P(1 < X < 3) = F(3) − F(1) = 0.5 − 1/16 = 0.4375.",
        "f(x) = 1/6 for −2 ≤ x ≤ 4; F(x) = 0 for x < −2, (x + 2)/6 for −2 ≤ x ≤ 4, 1 for x > 4. E(X) = 1, Var(X) = 36/12 = 3, P(X < 0) = 1/3.",
        "(a + b)/2 = 5 and (b − a)²/12 = 3, so b − a = 6 and a + b = 10: a = 2, b = 8. P(X > 6.5) = 1.5/6 = 0.25.",
        "Var(E) = 1/12, so the standard deviation is 0.289 mm (3 s.f.). P(|E| > 0.3) = 0.4/1 = 0.4.",
        "Mean = 1/3 ≈ 0.333; median = 1 − √0.5 = 0.293; mode = 0 (f is decreasing). Mode < median < mean, and the pdf has a "
        "long tail to the right, so X has positive skew.",
        "F(x) = x/2. For 0 ≤ y ≤ 4: G(y) = P(X ≤ √y) = √y/2 (0 for y < 0, 1 for y > 4). h(y) = 1/(4√y) for 0 < y ≤ 4. "
        "P(Y > 1) = 1 − 1/2 = 0.5. E(Y) = ∫₀⁴ y/(4√y) dy = 4/3 (check: E(X²) = Var(X) + [E(X)]² = 1/3 + 1).",
        "F(x) = x³/8. For 0 ≤ y ≤ 8: G(y) = P(X ≤ y^(1/3)) = y/8, so h(y) = 1/8: Y ~ U(0, 8). E(Y) = 4, Var(Y) = 64/12 = 16/3.",
        "For 0 ≤ y ≤ 1: G(y) = P(1 − X² ≤ y) = P(X ≥ √(1 − y)) = 1 − F(√(1 − y)) = 1 − (1 − y) = y, with G = 0 below 0 and 1 above 1. "
        "So Y ~ U(0, 1).",
    ],
    "exam": [
        "The continuous random variable X has pdf f(x) = 2x/15 for 0 ≤ x ≤ 3, f(x) = (5 − x)/5 for 3 < x ≤ 5, and f(x) = 0 otherwise. "
        "(a) Sketch the graph of f. [2] (b) Find the cumulative distribution function F(x) for all values of x. [5] "
        "(c) Find the median of X. [2] (d) Find the 90th percentile of X. [3] (e) Find P(2 < X < 4). [2]",
        "The random variable X has a continuous uniform distribution on [a, b]. (a) Prove that E(X) = (a + b)/2. [2] "
        "(b) Prove that Var(X) = (b − a)²/12. [4] A point P is chosen at random on a line AB of length 10 cm, and X = AP in cm. "
        "(c) Find the probability that AP > 3PB. [3] (d) Find the probability that the rectangle with sides AP and PB has an area greater than 21 cm². [3]",
        "The continuous random variable X has cdf F(x) = 0 for x < 1, F(x) = k(x³ − 1) for 1 ≤ x ≤ 3, F(x) = 1 for x > 3. "
        "(a) Find k. [1] (b) Find P(X > 2). [2] (c) Find the pdf of X. [2] (d) Find the median and the lower quartile. [3] "
        "(e) Find E(X), and write down the mode of X. [3] (f) Describe the skewness of X, giving a reason. [2]",
        "The radius R cm of a circular disc is modelled as R ~ U(1, 3). The area of the disc is A = πR² cm². "
        "(a) Write down the cdf of R. [2] (b) Find the cdf of A for all values of a. [4] (c) Hence find the pdf of A. [2] "
        "(d) Find the median of A. [2] (e) Find P(A > 20). [2] (f) Find E(A). [2]",
    ],
    "exam_answers": [
        "(a) A straight line from (0, 0) to (3, 0.4), then a straight line down to (5, 0); zero elsewhere [B2]. "
        "(b) For 0 ≤ x ≤ 3: F(x) = ∫₀ˣ 2t/15 dt = x²/15 [M1 A1]; F(3) = 0.6. For 3 < x ≤ 5: F(x) = 0.6 + ∫₃ˣ (5 − t)/5 dt = x − x²/10 − 1.5 [M1 A1]. "
        "F(x) = 0 for x < 0 and F(x) = 1 for x > 5 [B1]. "
        "(c) F(3) = 0.6 > 0.5, so x²/15 = 0.5 [M1], median = √7.5 = 2.74 (3 s.f.) [A1]. "
        "(d) x − x²/10 − 1.5 = 0.9 [M1], x² − 10x + 24 = 0, (x − 4)(x − 6) = 0 [M1]; 6 is outside the range, so the 90th percentile is 4 [A1]. "
        "(e) F(4) − F(2) = 0.9 − 4/15 = 0.633 (3 s.f.) [M1 A1].",
        "(a) E(X) = ∫ₐᵇ x/(b − a) dx = (b² − a²)/(2(b − a)) [M1] = (a + b)/2 [A1]. "
        "(b) E(X²) = (b³ − a³)/(3(b − a)) = (a² + ab + b²)/3 [M1 A1]; Var(X) = (a² + ab + b²)/3 − (a + b)²/4 [M1] = (b − a)²/12 [A1]. "
        "(c) X ~ U(0, 10) [B1]. AP > 3PB means X > 3(10 − X), so X > 7.5 [M1]; P = 2.5/10 = 0.25 [A1]. "
        "(d) X(10 − X) > 21 gives X² − 10X + 21 < 0, (X − 3)(X − 7) < 0, so 3 < X < 7 [M1 A1]; P = 4/10 = 0.4 [A1].",
        "(a) F(3) = 26k = 1, k = 1/26 [B1]. (b) P(X > 2) = 1 − 7/26 = 19/26 = 0.731 (3 s.f.) [M1 A1]. "
        "(c) f(x) = 3x²/26 for 1 ≤ x ≤ 3, 0 otherwise [M1 A1]. "
        "(d) (m³ − 1)/26 = 0.5, m³ = 14, median = 2.41 [M1 A1]; (q³ − 1)/26 = 0.25, q³ = 7.5, Q₁ = 1.96 (3 s.f.) [A1]. "
        "(e) E(X) = ∫₁³ 3x³/26 dx = 3 × 80/104 = 30/13 = 2.31 (3 s.f.) [M1 A1]; f is increasing, so the mode is 3 [B1]. "
        "(f) Mean (2.31) < median (2.41) < mode (3), so negative skew [M1 A1].",
        "(a) F(r) = 0 for r < 1; (r − 1)/2 for 1 ≤ r ≤ 3; 1 for r > 3 [B2]. "
        "(b) π ≤ A ≤ 9π [B1]. G(a) = P(πR² ≤ a) = P(R ≤ √(a/π)) [M1] = (√(a/π) − 1)/2 for π ≤ a ≤ 9π [A1]; G(a) = 0 for a < π and 1 for a > 9π [A1]. "
        "(c) g(a) = G′(a) = 1/(4√(πa)) for π ≤ a ≤ 9π, 0 otherwise [M1 A1]. "
        "(d) Median of R is 2, so median of A = 4π = 12.6 (3 s.f.) [M1 A1] (or solve G(a) = 0.5). "
        "(e) P(A > 20) = 1 − (√(20/π) − 1)/2 = 0.238 (3 s.f.) [M1 A1]. "
        "(f) E(A) = πE(R²) = π(Var(R) + [E(R)]²) = π(1/3 + 4) = 13π/3 = 13.6 (3 s.f.) [M1 A1].",
    ],
}
