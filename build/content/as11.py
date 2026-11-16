UNIT = {
    "number": "AS11",
    "title": "Continuous random variables",
    "tag": "AS · Edexcel FS2, AQA (SD1–SD5) · A level: OCR A (5.03), OCR MEI Major (SR19–SR23) · CAIE 9231 P4 (4.1) · prior knowledge for IAL S3 (from S2)",
    "notes": [
        ("h2", "11.1 Discrete and continuous random variables"),
        ("p", "A discrete random variable takes separate values that you can list, such as 0, 1, 2, … . A continuous random variable "
              "(CRV) can take any value in an interval, such as a time, a length or a mass. Because there are infinitely many values "
              "in any interval, the probability of one exact value is zero. Instead, probability is spread over the interval and "
              "described by a <b>probability density function</b> (pdf), written f(x)."),
        ("p", "Think of a histogram of a very large data set with very narrow classes, scaled so that its total area is 1. "
              "As the classes get narrower, the tops of the bars approach a smooth curve. That curve is the pdf. The area under "
              "the histogram between two values is the proportion of data there, so the area under the pdf between a and b is a probability."),
        ("table", ["", "Discrete random variable", "Continuous random variable"], [
            ["Described by", "probability function P(X = x)", "probability density function f(x)"],
            ["Total probability", "Σ P(X = x) = 1", "∫ f(x) dx = 1 over all x"],
            ["Probability of an interval", "add the probabilities", "area under f: ∫ₐᵇ f(x) dx"],
            ["P(X = a)", "can be positive", "always 0, so P(X < a) = P(X ≤ a)"],
            ["Mean", "E(X) = Σ x P(X = x)", "E(X) = ∫ x f(x) dx"],
            ["E(X²)", "Σ x² P(X = x)", "∫ x² f(x) dx"],
            ["Mode", "value with the largest probability", "value where f(x) is largest"],
        ]),
        ("box", "Probability density function", [
            "P(a ≤ X ≤ b) = ∫ₐᵇ f(x) dx, the area under the graph of f between x = a and x = b.",
            "A function f is a valid pdf if (1) f(x) ≥ 0 for every x, and (2) the total area is 1: ∫ f(x) dx = 1 over all values of x.",
            "f(x) itself is <b>not</b> a probability. It can be bigger than 1, as long as the total area is 1.",
            "For a continuous variable, P(X = a) = 0, so ≤ and < give the same probability.",
        ]),
        ("h2", "11.2 Finding unknown constants and piecewise pdfs"),
        ("p", "A pdf is usually given with an unknown constant k. Use the fact that the total area is 1: integrate over the whole "
              "domain, set the result equal to 1 and solve for k. Always say that f(x) = 0 outside the given interval."),
        ("p", "A <b>piecewise</b> pdf has different formulas on different intervals, for example f(x) = kx for 0 ≤ x ≤ 2 and "
              "f(x) = k(6 − x)/2 for 2 < x ≤ 6. Integrate each piece over its own interval and add the areas. A pdf does not have "
              "to be continuous where the pieces join, but in most exam questions it is, and you can use this as a check or to "
              "find a second unknown. Edexcel AS FS2 restricts pdfs to sums of terms of the form kxⁿ (n rational, n ≠ −1), "
              "possibly piecewise; the A level boards and CAIE also use other functions."),
        ("p", "With two unknowns you need two equations: the total area is 1, and one more fact such as continuity at a join, "
              "a given mean, or a given probability."),
        ("h2", "11.3 Sketching a pdf"),
        ("p", "MEI and OCR expect you to sketch pdfs, and a sketch helps every question. Draw the x-axis over the whole domain, "
              "mark the end points and the value of f there, show where f is zero, and draw each piece. A sketch shows at once "
              "where the mode is, whether the distribution is symmetrical (then mean = median = the centre of symmetry), and "
              "which piece the median lies in."),
        ("bullets", [
            "f(x) = kx² on 0 ≤ x ≤ 2: an increasing curve from (0, 0) to (2, 4k), concave upwards; zero outside.",
            "f(x) = k(x − 1)(5 − x) on 1 ≤ x ≤ 5: an upside-down parabola, zero at x = 1 and x = 5, symmetrical about x = 3.",
            "A triangular pdf: straight lines up to a peak and back down; the mode is at the peak.",
        ]),
        ("h2", "11.4 Mean, variance and standard deviation"),
        ("p", "The expected value (mean) of X is its long-run average. For a discrete variable you multiply each value by its "
              "probability and add. For a continuous variable the sum becomes an integral."),
        ("box", "Mean and variance of a continuous random variable", [
            "E(X) = μ = ∫ x f(x) dx and E(X²) = ∫ x² f(x) dx, each over the whole domain.",
            "Var(X) = E(X²) − [E(X)]² = E(X²) − μ². The standard deviation is √Var(X).",
            "For a piecewise pdf, split each integral into one integral per piece and add.",
            "If the pdf is symmetrical about x = c (and E(X) exists), then E(X) = c.",
        ]),
        ("h2", "11.5 Expectation of a function of X, and linear functions"),
        ("p", "For any function g, the expected value of g(X) is found by weighting g(x) by the density: E(g(X)) = ∫ g(x) f(x) dx. "
              "This is how E(X²) is found, and it also gives quantities such as E(1/X), E(5X³) or E(18X⁻³) (AQA SD5, Edexcel FS2 2.3, "
              "OCR A 5.03d, CAIE 4.1). In general E(g(X)) ≠ g(E(X)): for example E(1/X) is not 1/E(X)."),
        ("box", "Linear functions of X (all boards)", [
            "E(aX + b) = aE(X) + b    and    Var(aX + b) = a²Var(X).",
            "Proof: E(aX + b) = ∫ (ax + b) f(x) dx = a∫ x f(x) dx + b∫ f(x) dx = aE(X) + b, since ∫ f(x) dx = 1.",
            "Then Var(aX + b) = E[(aX + b − aμ − b)²] = E[a²(X − μ)²] = a²Var(X). Adding b shifts the distribution but does not change its spread.",
            "To find Var(g(X)) for a non-linear g, use Var(g(X)) = E(g(X)²) − [E(g(X))]², e.g. Var(1/X) = E(X⁻²) − [E(X⁻¹)]².",
        ]),
        ("h2", "11.6 Median, quartiles, percentiles and mode"),
        ("p", "The median m splits the area under the pdf in half: ∫ from the lowest value to m of f(x) dx = 0.5. In the same way "
              "the lower quartile Q₁ has area 0.25 to its left, the upper quartile Q₃ has area 0.75 to its left, and the kth "
              "percentile has area k/100 to its left. The function that gives the area to the left of x is the cumulative "
              "distribution function F(x); it is developed fully in Unit A2.1."),
        ("bullets", [
            "For a piecewise pdf, first find the area of the first piece. If it is more than 0.5, the median is in the first piece; if not, it is in a later piece.",
            "When the equation for m is a quadratic or quartic, keep only the root that lies inside the domain.",
            "For a later piece it is often quicker to work from the right: area to the right of m = 0.5.",
            "The <b>mode</b> is the value of x where f(x) is largest. If f has a turning point inside the domain, solve f′(x) = 0 and check it is a maximum. "
            "If f is increasing (or decreasing) over the whole domain, the mode is at an end point. A uniform pdf has no unique mode.",
        ]),
        ("h2", "11.7 Mixed distributions (AQA A level only)"),
        ("p", "AQA A level (SD1) includes random variables that are <b>part discrete and part continuous</b>. For example, the time "
              "a driver waits at traffic lights is exactly 0 if the light is green (a probability mass at 0) but otherwise can be "
              "any value in an interval (a density). The discrete probabilities plus the area under the continuous part must "
              "total 1. Expectations are found by adding the discrete sum and the integral: E(X) = Σ x P(X = x) + ∫ x f(x) dx."),
        ("warn", "Common mistakes", [
            "Treating f(x) as a probability. P(X = 2) is 0, not f(2). Probabilities are areas.",
            "Forgetting to state f(x) = 0 outside the domain, or integrating outside it.",
            "Finding the median by setting f(m) = 0.5 instead of the area up to m equal to 0.5. Examiners report this every year.",
            "Writing Var(X) = E(X²) − E(X) (forgetting to square the mean), or Var(aX + b) = aVar(X) + b.",
            "Finding the mode by setting f′(x) = 0 when f is increasing on the whole domain: then the mode is the end point.",
            "For piecewise pdfs, integrating only one piece, or keeping a root of the median equation that lies outside that piece.",
            "Rounding early. Keep exact fractions, or at least 4 significant figures, until the final answer.",
        ]),
        ("p", "Calculator use: every board allows a calculator to evaluate definite integrals, but you must still write down the "
              "integral you are evaluating (MEI states this explicitly). In \"show that\" questions, show the integration by hand. "
              "Cambridge allows only a scientific calculator (no graphical or CAS models), so CAIE students should expect to integrate by hand throughout. "
              "Unless told otherwise, give final answers to 3 significant figures."),
    ],
    "examples": [
        {
            "title": "Finding k and probabilities",
            "question": "A continuous random variable X has pdf f(x) = kx² for 0 ≤ x ≤ 2, and f(x) = 0 otherwise. Find k, "
                        "P(X > 1) and P(0.5 < X < 1.5), and sketch the pdf.",
            "steps": [
                "Total area is 1: ∫₀² kx² dx = k[x³/3]₀² = 8k/3 = 1, so k = 3/8.",
                "P(X > 1) = ∫₁² (3/8)x² dx = (3/8) × (8 − 1)/3 = 7/8 = 0.875.",
                "P(0.5 < X < 1.5) = (3/8) × (1.5³ − 0.5³)/3 = (3.375 − 0.125)/8 = 0.40625 (exactly).",
                "Sketch: an increasing curve from (0, 0) to (2, 1.5), concave upwards, with f = 0 for x < 0 and x > 2.",
            ],
        },
        {
            "title": "Mean, variance, median, quartile and mode",
            "question": "For the pdf f(x) = (3/8)x², 0 ≤ x ≤ 2, of Worked example AS11.1, find E(X), Var(X), the standard deviation, "
                        "the median, the lower quartile and the mode.",
            "steps": [
                "E(X) = ∫₀² x × (3/8)x² dx = (3/8)[x⁴/4]₀² = (3/8) × 4 = 1.5.",
                "E(X²) = ∫₀² (3/8)x⁴ dx = (3/8)[x⁵/5]₀² = (3/8) × 32/5 = 2.4.",
                "Var(X) = 2.4 − 1.5² = 0.15, so the standard deviation is √0.15 = 0.387 (3 s.f.).",
                "Area up to m: ∫₀ᵐ (3/8)x² dx = m³/8. Set m³/8 = 0.5, so m³ = 4 and m = 1.59 (3 s.f.).",
                "Lower quartile: q³/8 = 0.25, so q³ = 2 and Q₁ = 1.26 (3 s.f.).",
                "f is increasing on [0, 2], so the largest value of f is at the end point: the mode is 2.",
            ],
        },
        {
            "title": "A piecewise (triangular) pdf",
            "question": "X has pdf f(x) = kx for 0 ≤ x ≤ 2, f(x) = k(6 − x)/2 for 2 < x ≤ 6, and 0 otherwise. "
                        "(a) Find k. (b) Find E(X) and Var(X). (c) Find the median. (d) Find P(X > 4).",
            "steps": [
                "(a) The graph is a triangle with base 6 and height f(2) = 2k, so the area is ½ × 6 × 2k = 6k = 1, giving k = 1/6. Both pieces give f(2) = 1/3, so f is continuous and the mode is 2.",
                "(b) E(X) = ∫₀² x²/6 dx + ∫₂⁶ x(6 − x)/12 dx = 4/9 + 20/9 = 8/3 = 2.67 (3 s.f.).",
                "E(X²) = ∫₀² x³/6 dx + ∫₂⁶ x²(6 − x)/12 dx = 2/3 + 8 = 26/3. Var(X) = 26/3 − (8/3)² = 14/9 = 1.56 (3 s.f.).",
                "(c) Area of the first piece = ½ × 2 × 1/3 = 1/3 < 0.5, so the median is in the second piece. Work from the right: "
                "area to the right of m = ½(6 − m) × (6 − m)/12 = (6 − m)²/24 = 0.5, so (6 − m)² = 12.",
                "m = 6 − √12 = 2.54 (3 s.f.). The other root, 6 + √12, is outside the domain.",
                "(d) P(X > 4) = (6 − 4)²/24 = 1/6, using the same right-hand area formula.",
            ],
        },
        {
            "title": "Expectations of functions of X",
            "question": "X has pdf f(x) = 2x/15 for 1 ≤ x ≤ 4. Find (a) E(X) and Var(X), (b) E(3X − 2) and Var(3X − 2), "
                        "(c) E(5X³), (d) E(1/X) and Var(6/X).",
            "steps": [
                "(a) E(X) = ∫₁⁴ 2x²/15 dx = (2/15) × (64 − 1)/3 = 2.8. E(X²) = ∫₁⁴ 2x³/15 dx = (2/15) × (256 − 1)/4 = 8.5. "
                "Var(X) = 8.5 − 2.8² = 0.66.",
                "(b) E(3X − 2) = 3 × 2.8 − 2 = 6.4. Var(3X − 2) = 3² × 0.66 = 5.94.",
                "(c) E(X³) = ∫₁⁴ 2x⁴/15 dx = (2/15) × (1024 − 1)/5 = 27.28, so E(5X³) = 136.4.",
                "(d) E(1/X) = ∫₁⁴ (1/x)(2x/15) dx = (2/15) × 3 = 0.4. E(1/X²) = ∫₁⁴ 2/(15x) dx = (2/15) ln 4 = 0.1848 (4 d.p.).",
                "Var(1/X) = (2/15) ln 4 − 0.4² = 0.024839…, so Var(6/X) = 36 × 0.024839… = 0.894 (3 s.f.). Note E(1/X) = 0.4 ≠ 1/E(X) = 0.357.",
            ],
        },
        {
            "title": "Mode by differentiation and the median equation",
            "question": "X has pdf f(x) = (4/27)x²(3 − x) for 0 ≤ x ≤ 3. (a) Find the mode. (b) Find E(X) and Var(X). "
                        "(c) Show that the median m satisfies m⁴ − 4m³ + 13.5 = 0, and find m. (d) Find P(X < 1).",
            "steps": [
                "(a) f(x) = (4/27)(3x² − x³), so f′(x) = (4/27)(6x − 3x²) = (4/27) × 3x(2 − x). f′(x) = 0 at x = 0 and x = 2. "
                "f(0) = 0 = f(3) and f(2) = 16/27 > 0, so the maximum is at x = 2: the mode is 2.",
                "(b) E(X) = (4/27)∫₀³ (3x³ − x⁴) dx = (4/27)(243/4 − 243/5) = 1.8. E(X²) = (4/27)∫₀³ (3x⁴ − x⁵) dx = (4/27)(729/5 − 729/6) = 3.6. "
                "Var(X) = 3.6 − 1.8² = 0.36.",
                "(c) Area up to m: (4/27)(m³ − m⁴/4) = 1/2. Multiply by 27/4: m³ − m⁴/4 = 27/8. Multiply by −4: m⁴ − 4m³ + 13.5 = 0, as required.",
                "Solving on a calculator (or by iteration) for 0 ≤ m ≤ 3 gives m = 1.84 (3 s.f.). Check: area up to 1.835 ≈ 0.4955 and up to 1.845 ≈ 0.5013, so m = 1.84 to 3 s.f.",
                "(d) P(X < 1) = (4/27)(1 − 1/4) = 1/9 = 0.111 (3 s.f.).",
                "Note: mean 1.8 < median 1.84 < mode 2, which shows negative skew (see Unit A2.1).",
            ],
        },
        {
            "title": "A mixed distribution (AQA A level only)",
            "question": "At a set of traffic lights, a driver does not have to wait with probability 0.4. Otherwise the waiting time "
                        "is equally likely to be anywhere between 0 and 50 seconds. Let X seconds be the waiting time. "
                        "Find P(X ≤ 10), E(X), Var(X) and the median waiting time.",
            "steps": [
                "P(X = 0) = 0.4. The continuous part has constant density c on 0 < x ≤ 50 with area 0.6, so 50c = 0.6 and c = 0.012.",
                "P(X ≤ 10) = 0.4 + 0.012 × 10 = 0.52.",
                "E(X) = 0 × 0.4 + ∫₀⁵⁰ 0.012x dx = 0.012 × 1250 = 15 seconds.",
                "E(X²) = ∫₀⁵⁰ 0.012x² dx = 0.012 × 125000/3 = 500, so Var(X) = 500 − 15² = 275 (standard deviation 16.6 s).",
                "Median: 0.4 + 0.012m = 0.5, so m = 0.1/0.012 = 8.33 seconds (3 s.f.).",
            ],
        },
    ],
    "practice": [
        "A random variable X has pdf f(x) = k(1 + x) for 0 ≤ x ≤ 3, and 0 otherwise. Find k and P(X < 1).",
        "X has pdf f(x) = x/2 for 0 ≤ x ≤ 2. Show that this is a valid pdf. Find E(X), the median, and P(1 < X < 1.5).",
        "X has pdf f(x) = 3x² for 0 ≤ x ≤ 1. Find E(X) and Var(X) exactly.",
        "X has pdf f(x) = 2(1 − x) for 0 ≤ x ≤ 1. Find E(X) and the median, giving the median to 3 decimal places.",
        "X has pdf f(x) = k/x² for 1 ≤ x ≤ 2. Find k, P(X > 1.5), E(X) and the median.",
        "X has pdf f(x) = kx for 0 ≤ x ≤ 2, f(x) = 2k for 2 < x ≤ 3, and 0 otherwise. Sketch the pdf, find k, show that the "
        "median is 2, and find E(X).",
        "X has pdf f(x) = (1/4)x(4 − x²) for 0 ≤ x ≤ 2. Show that the total area is 1, find the mode exactly and find E(X).",
        "X has pdf f(x) = 3x²/7 for 1 ≤ x ≤ 2. Find E(14/X) and Var(14/X).",
        "A continuous random variable X has E(X) = 4 and Var(X) = 2. Find E(5 − 2X), Var(5 − 2X), E(X²) and E(3X² + 1).",
        "X has pdf f(x) = k(x − 1)(5 − x) for 1 ≤ x ≤ 5. Sketch the pdf and find k. Write down E(X), the median and the mode, "
        "and find P(X < 2) and Var(X).",
        "X has pdf f(x) = x³/4 for 0 ≤ x ≤ 2. Find the quartiles, the interquartile range and the 90th percentile.",
        "(AQA A level) The daily rainfall X mm in a town is 0 with probability 0.6. Otherwise, for 0 < x ≤ 10 it has density "
        "f(x) = 0.008(10 − x). Show that the total probability is 1, and find P(X > 5) and E(X).",
    ],
    "answers": [
        "∫₀³ k(1 + x) dx = k(3 + 4.5) = 7.5k = 1, so k = 2/15. P(X < 1) = (2/15)(1 + 0.5) = 0.2.",
        "f(x) ≥ 0 and ∫₀² x/2 dx = [x²/4]₀² = 1, so it is valid. E(X) = ∫₀² x²/2 dx = 4/3. Area up to m is m²/4 = 0.5, so m = √2 = 1.41 (3 s.f.). "
        "P(1 < X < 1.5) = 2.25/4 − 1/4 = 0.3125.",
        "E(X) = ∫₀¹ 3x³ dx = 3/4. E(X²) = ∫₀¹ 3x⁴ dx = 3/5, so Var(X) = 3/5 − 9/16 = 3/80.",
        "E(X) = ∫₀¹ 2x(1 − x) dx = 2(1/2 − 1/3) = 1/3. Area up to m is 2m − m² = 0.5, so m² − 2m + 0.5 = 0 and m = 1 − √0.5 = 0.293 (the root 1.707 is outside [0, 1]).",
        "k(1 − 1/2) = 1, so k = 2. P(X > 1.5) = 2(1/1.5 − 1/2) = 1/3. E(X) = ∫₁² 2/x dx = 2 ln 2 = 1.39 (3 s.f.). "
        "Area up to m: 2(1 − 1/m) = 0.5, so 1/m = 0.75 and m = 4/3.",
        "Sketch: a line from (0, 0) to (2, 2k), then a horizontal line at height 2k to x = 3. Area = 2k + 2k = 4k = 1, so k = 1/4. "
        "Area up to 2 = ∫₀² x/4 dx = 0.5, so the median is 2. E(X) = ∫₀² x²/4 dx + ∫₂³ x/2 dx = 2/3 + 5/4 = 23/12 = 1.92 (3 s.f.).",
        "∫₀² (4x − x³)/4 dx = (8 − 4)/4 = 1. f′(x) = (4 − 3x²)/4 = 0 gives x = 2/√3 = 1.15 (3 s.f.), a maximum since f(0) = f(2) = 0. "
        "E(X) = (1/4)∫₀² (4x² − x⁴) dx = (1/4)(32/3 − 32/5) = 16/15 = 1.07 (3 s.f.).",
        "E(1/X) = (3/7)∫₁² x dx = 9/14 and E(1/X²) = (3/7)∫₁² 1 dx = 3/7. So E(14/X) = 14 × 9/14 = 9. "
        "Var(1/X) = 3/7 − (9/14)² = 3/196, so Var(14/X) = 196 × 3/196 = 3.",
        "E(5 − 2X) = 5 − 8 = −3. Var(5 − 2X) = 4 × 2 = 8. E(X²) = Var(X) + [E(X)]² = 2 + 16 = 18. E(3X² + 1) = 3 × 18 + 1 = 55.",
        "Sketch: an upside-down parabola through (1, 0) and (5, 0), peak at x = 3. ∫₁⁵ (x − 1)(5 − x) dx = 32/3, so k = 3/32. "
        "By symmetry E(X) = median = mode = 3. P(X < 2) = (3/32)∫₁² (x − 1)(5 − x) dx = (3/32)(5/3) = 5/32 = 0.15625. "
        "E(X²) = 9.8, so Var(X) = 9.8 − 9 = 0.8.",
        "Area up to x is x⁴/16. Q₁: x⁴ = 4, Q₁ = √2 = 1.41. Q₃: x⁴ = 12, Q₃ = 1.86. IQR = 1.8612 − 1.4142 = 0.447. "
        "90th percentile: x⁴ = 14.4, x = 1.95 (all 3 s.f.).",
        "0.6 + ∫₀¹⁰ 0.008(10 − x) dx = 0.6 + 0.008 × 50 = 1. P(X > 5) = ∫₅¹⁰ 0.008(10 − x) dx = 0.008 × 12.5 = 0.1. "
        "E(X) = ∫₀¹⁰ 0.008x(10 − x) dx = 0.008 × 500/3 = 4/3 = 1.33 mm (3 s.f.).",
    ],
    "exam": [
        "The continuous random variable X has pdf f(x) = kx² for 0 ≤ x ≤ 2, f(x) = k(6 − x) for 2 < x ≤ 6, and f(x) = 0 otherwise. "
        "(a) Show that k = 3/32. [3] (b) Sketch the graph of f and write down the mode of X. [3] (c) Find P(X > 4). [2] "
        "(d) Find E(X). [3] (e) Find the median of X, giving your answer to 3 significant figures. [4]",
        "The continuous random variable X has pdf f(x) = k/x³ for 1 ≤ x ≤ 2, and 0 otherwise. (a) Show that k = 8/3. [2] "
        "(b) Find E(X). [2] (c) Show that Var(X) = (8/3) ln 2 − 16/9. [3] (d) Hence find Var(3X + 2). [2] "
        "(e) Find E(18X⁻³). [3] (f) Find the median of X. [3]",
        "The time, X hours, that a battery lasts in a test has pdf f(x) = (4/81)x(9 − x²) for 0 ≤ x ≤ 3, and 0 otherwise. "
        "(a) Find the mode of X, giving an exact answer. [3] (b) Find E(X) and Var(X). [5] "
        "(c) Show that the median m satisfies m⁴ − 18m² + 40.5 = 0, and hence find m to 3 significant figures. [5] "
        "(d) Find the probability that a battery lasts more than 2 hours. [2]",
        "(AQA A level) The time X minutes that a customer waits to be served at a bank counter is 0 with probability 0.25. "
        "Otherwise X has density f(x) = k(4 − x) for 0 < x ≤ 4. (a) Explain why X is neither a discrete nor a continuous random variable. [1] "
        "(b) Find k. [2] (c) Find P(X ≤ 1). [2] (d) Show that E(X) = 1 and Var(X) = 1. [5] (e) Find the median waiting time. [3]",
    ],
    "exam_answers": [
        "(a) ∫₀² kx² dx = 8k/3 [M1]; ∫₂⁶ k(6 − x) dx = 8k [M1]; 8k/3 + 8k = 32k/3 = 1, so k = 3/32 [A1]. "
        "(b) Curve rising from (0, 0) to (2, 3/8), then a straight line down to (6, 0); f = 0 elsewhere [B2]. Mode = 2 [B1]. "
        "(c) P(X > 4) = ∫₄⁶ (3/32)(6 − x) dx = (3/32) × 2 = 3/16 = 0.1875 [M1 A1]. "
        "(d) E(X) = (3/32)[∫₀² x³ dx + ∫₂⁶ (6x − x²) dx] = (3/32)(4 + 80/3) [M1 M1] = 23/8 = 2.875 [A1]. "
        "(e) Area of first piece = 8k/3 = 1/4 < 0.5, so the median is in the second piece [M1]. Area to the right of m: (3/32)(6 − m)²/2 = 0.5 [M1], "
        "so (6 − m)² = 32/3 [A1], m = 6 − √(32/3) = 2.73 (3 s.f.) [A1].",
        "(a) ∫₁² k x⁻³ dx = k[−1/(2x²)]₁² = k(1/2 − 1/8) = 3k/8 = 1, so k = 8/3 [M1 A1]. "
        "(b) E(X) = (8/3)∫₁² x⁻² dx = (8/3)(1 − 1/2) = 4/3 [M1 A1]. "
        "(c) E(X²) = (8/3)∫₁² x⁻¹ dx = (8/3) ln 2 [M1 A1]; Var(X) = (8/3) ln 2 − (4/3)² = (8/3) ln 2 − 16/9 [A1]. "
        "(d) Var(3X + 2) = 9 Var(X) = 24 ln 2 − 16 = 0.636 (3 s.f.) [M1 A1]. "
        "(e) E(X⁻³) = (8/3)∫₁² x⁻⁶ dx = (8/3)(1/5)(1 − 1/32) = 31/60 [M1 A1]; E(18X⁻³) = 18 × 31/60 = 9.3 [A1]. "
        "(f) (8/3)(1/2)(1 − 1/m²) = 0.5 [M1], 1 − 1/m² = 3/8, m² = 8/5 [A1], m = 1.26 (3 s.f.) [A1].",
        "(a) f′(x) = (4/81)(9 − 3x²) = 0 [M1] gives x = √3 [A1]; f″(x) = (4/81)(−6x) < 0, so a maximum: mode = √3 hours [A1]. "
        "(b) E(X) = (4/81)∫₀³ (9x² − x⁴) dx = (4/81)(81 − 243/5) = 8/5 = 1.6 [M1 A1]. E(X²) = (4/81)∫₀³ (9x³ − x⁵) dx = (4/81)(729/4 − 729/6) = 3 [M1 A1]. "
        "Var(X) = 3 − 1.6² = 0.44 [A1]. "
        "(c) (4/81)(9m²/2 − m⁴/4) = 1/2 [M1 A1]; multiply by 81: 18m² − m⁴ = 40.5, so m⁴ − 18m² + 40.5 = 0 [A1]. "
        "m² = 9 ± √(81 − 40.5); m² = 9 + √40.5 gives m > 3, so m² = 9 − √40.5 = 2.636… [M1], m = 1.62 (3 s.f.) [A1]. "
        "(d) P(X > 2) = 1 − (4/81)(18 − 4) = 1 − 56/81 = 25/81 = 0.309 (3 s.f.) [M1 A1].",
        "(a) It has a non-zero probability at the single value 0 (discrete part) but a density over 0 < x ≤ 4 (continuous part) [B1]. "
        "(b) 0.25 + ∫₀⁴ k(4 − x) dx = 0.25 + 8k = 1 [M1], k = 3/32 = 0.09375 [A1]. "
        "(c) P(X ≤ 1) = 0.25 + (3/32)(4 − 1/2) = 0.25 + 0.328125 = 0.578 (3 s.f.) [M1 A1]. "
        "(d) E(X) = 0 × 0.25 + (3/32)∫₀⁴ (4x − x²) dx = (3/32)(32/3) = 1 [M1 A1]. E(X²) = (3/32)∫₀⁴ (4x² − x³) dx = (3/32)(64/3) = 2 [M1 A1]. "
        "Var(X) = 2 − 1² = 1 [A1]. "
        "(e) 0.25 + (3/32)(4m − m²/2) = 0.5 [M1], so m² − 8m + 16/3 = 0 [A1], m = 4 − √(32/3) = 0.734 minutes (3 s.f.) [A1].",
    ],
}
