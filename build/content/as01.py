UNIT = {
    "number": "AS1",
    "title": "Discrete random variables",
    "tag": "AS · Edexcel FS1, AQA, OCR A, OCR MEI · prior knowledge for IAL S3 and CAIE 9231 Paper 4",
    "notes": [
        ("p", "This unit builds the toolkit used in every later unit on discrete distributions: probability distributions given "
              "as tables or formulae, cumulative probabilities, expectation and variance, expectations of functions of X, the "
              "effect of coding, sums of independent random variables, and the discrete uniform distribution with a full proof "
              "of its mean and variance."),

        ("h2", "1.1 Discrete random variables and their distributions"),
        ("p", "A <b>random variable</b> X is a numerical outcome of a random experiment. Capital X names the variable; lower-case x "
              "stands for a value it can take. X is <b>discrete</b> when its possible values can be listed, such as 0, 1, 2, 3 "
              "or 1, 2, 3, …. The <b>probability distribution</b> of X gives P(X = x) for every possible value x. It can be given "
              "as a table, as a formula (a <b>probability function</b>), or drawn as a vertical line graph."),
        ("p", "In this unit any distribution you are asked to construct is finite. The Poisson and geometric distributions "
              "(units AS2 and AS3) are the standard infinite cases."),
        ("box", "Two rules every probability distribution must satisfy", [
            "1. Each probability is between 0 and 1:  0 ≤ P(X = x) ≤ 1.",
            "2. The probabilities add to 1:  Σ P(X = x) = 1, summing over all possible x.",
            "Use rule 2 to find an unknown constant k. If there are two unknowns you need a second equation, usually from a given E(X).",
        ]),
        ("p", "To <b>construct</b> a distribution from a context, list every possible value of X first, then find each probability, "
              "often from a sample-space diagram or a tree. Always check that your probabilities add to 1."),

        ("h2", "1.2 Cumulative distribution tables, median and mode"),
        ("p", "The <b>cumulative distribution function</b> of X is F(x) = P(X ≤ x). For a discrete variable it is a running total "
              "of the probabilities, so it is a step function that rises from 0 to 1. Individual probabilities are recovered by "
              "subtraction: P(X = x) = F(x) − F(x − 1) when X takes consecutive integer values."),
        ("bullets", [
            "P(a < X ≤ b) = F(b) − F(a).   P(X > a) = 1 − F(a).   P(X ≥ a) = 1 − F(a − 1) for integer values.",
            "The <b>median</b> is the smallest value m with F(m) ≥ 0.5. (If F(m) is exactly 0.5 for a value m, some books give the "
            "median as the midpoint of m and the next value; exam questions avoid this case.)",
            "The <b>mode</b> is the value with the largest probability. A distribution can have more than one mode.",
        ]),

        ("h2", "1.3 Expectation and variance"),
        ("p", "The <b>expectation</b> (mean) of X is a weighted average of its values, with the probabilities as weights. It is the "
              "long-run average value of X over many repeats of the experiment. It need not be a value X can actually take."),
        ("box", "Expectation and variance of a discrete random variable", [
            "E(X) = μ = Σ x P(X = x)",
            "E(X²) = Σ x² P(X = x)",
            "Var(X) = σ² = E[(X − μ)²] = E(X²) − μ²",
            "Standard deviation σ = √Var(X).",
        ]),
        ("p", "Why the shortcut works: E[(X − μ)²] = E(X² − 2μX + μ²) = E(X²) − 2μE(X) + μ² = E(X²) − μ². The shortcut is quicker and "
              "is the formula given in every board's booklet. Set out the working in columns:"),
        ("table", ["x", "P(X = x)", "x P(X = x)", "x² P(X = x)"], [
            ["0", "0.3", "0", "0"],
            ["1", "0.3", "0.3", "0.3"],
            ["2", "0.3", "0.6", "1.2"],
            ["3", "0.1", "0.3", "0.9"],
            ["Total", "1", "E(X) = 1.2", "E(X²) = 2.4"],
        ]),
        ("p", "Here Var(X) = 2.4 − 1.2² = 0.96 and σ = √0.96 ≈ 0.980. A variance can never be negative; a negative answer means an "
              "arithmetic slip, most often squaring the probabilities instead of the values."),

        ("h2", "1.4 Expectation of a function of X (Edexcel; AQA A level)"),
        ("p", "For any function g, the expected value of g(X) is found by applying g to each value and weighting by the same "
              "probabilities: E[g(X)] = Σ g(x) P(X = x). AQA asks for examples such as E(5X³), E(18X⁻³) and Var(6X⁻¹). "
              "To find Var[g(X)], use Var[g(X)] = E[g(X)²] − [E(g(X))]²."),
        ("p", "In general E[g(X)] ≠ g(E(X)). For example E(X²) ≥ [E(X)]², with equality only if X is constant; the difference is "
              "exactly Var(X). Likewise E(1/X) is not 1/E(X)."),
        ("p", "<b>Assessing a model (Edexcel).</b> A proposed probability distribution can be checked against data. Compare the model's "
              "mean and variance with the mean and variance of the observed values, and compare expected frequencies (n × P(X = x)) "
              "with observed ones. Close agreement supports the model; a clear difference in the variance or in one end of the "
              "distribution suggests the model is unsuitable. A formal test of fit comes in unit AS7."),

        ("h2", "1.5 Linear coding: E(aX + b) and Var(aX + b)"),
        ("p", "If every value of X is multiplied by a and then has b added, the mean is transformed in the same way, but the spread is "
              "only affected by the multiplier. Adding b shifts every value, so it changes no distance from the mean. MEI writes "
              "the same results as E(a + bX) = a + bE(X) and Var(a + bX) = b²Var(X)."),
        ("box", "Linear coding (proofs not required by any board)", [
            "E(aX + b) = aE(X) + b,  since Σ(ax + b)P(X = x) = aΣxP(X = x) + bΣP(X = x) = aE(X) + b.",
            "Var(aX + b) = a² Var(X),  since (aX + b) − (aμ + b) = a(X − μ), and squaring gives a²(X − μ)².",
            "SD(aX + b) = |a| SD(X).   Note Var(−X) = Var(X).",
        ]),

        ("h2", "1.6 Sums of independent random variables"),
        ("p", "Two random variables are <b>independent</b> if the value of one does not change the probabilities for the other. "
              "For any X and Y, E(X + Y) = E(X) + E(Y). For variances you need independence."),
        ("box", "Sums and linear combinations (AQA SD8, MEI SR6, OCR A 5.04 at A level)", [
            "E(X + Y) = E(X) + E(Y)  (always).",
            "Var(X + Y) = Var(X) + Var(Y)  (X and Y independent).",
            "More generally E(aX ± bY) = aE(X) ± bE(Y) and, for independent X and Y, Var(aX ± bY) = a²Var(X) + b²Var(Y).",
            "Variances always add, even for a difference: Var(X − Y) = Var(X) + Var(Y).",
        ]),
        ("p", "Do not confuse X₁ + X₂ (two independent observations of X added) with 2X (one observation doubled). Both have mean 2μ, "
              "but Var(X₁ + X₂) = 2σ² while Var(2X) = 4σ². Two independent results partly cancel each other's deviations; a doubled "
              "result doubles its deviation. Unit A2.6 extends this to normal variables."),
        ("p", "For small examples you can also find the distribution of X + Y directly: list every pair (x, y), multiply the "
              "probabilities (independence), and collect the pairs with the same total."),

        ("h2", "1.7 The discrete uniform distribution"),
        ("p", "X has a <b>discrete uniform distribution</b> on {1, 2, …, n} if each of the n values is equally likely: P(X = x) = 1/n "
              "for x = 1, 2, …, n. It models a fair die, a fair spinner, or a number picked at random from a list. Conditions: a "
              "fixed, finite set of values, each with the same probability. OCR A writes X ~ U(n)."),
        ("box", "Discrete uniform on {1, 2, …, n}", [
            "P(X = x) = 1/n,   E(X) = (n + 1)/2,   Var(X) = (n² − 1)/12.",
            "Proof required by AQA (SA7); MEI says derivations may be asked for; OCR A and Edexcel use the results.",
        ]),
        ("p", "<b>Proof of the mean.</b> E(X) = Σ x × (1/n) = (1/n)(1 + 2 + … + n) = (1/n) × n(n + 1)/2 = (n + 1)/2."),
        ("p", "<b>Proof of the variance.</b> Use Σ r² = n(n + 1)(2n + 1)/6. Then E(X²) = (1/n) × n(n + 1)(2n + 1)/6 = (n + 1)(2n + 1)/6. So "
              "Var(X) = (n + 1)(2n + 1)/6 − (n + 1)²/4 = (n + 1)[2(2n + 1) − 3(n + 1)]/12 = (n + 1)(n − 1)/12 = (n² − 1)/12."),
        ("p", "<b>Other sets of equally spaced values (MEI SR7–SR9).</b> If Y is uniform on {a, a + 1, …, b}, write Y = X + (a − 1) with "
              "n = b − a + 1 values. Then E(Y) = (a + b)/2 and Var(Y) = (n² − 1)/12, because adding a constant does not change the "
              "variance. If the values are k, 2k, …, nk, write Y = kX, so Var(Y) = k²(n² − 1)/12. For any other set of equally likely "
              "values, just use the definitions of E and Var."),
        ("table", ["Result", "Formula", "Condition"], [
            ["Mean", "E(X) = Σ x P(X = x)", "any discrete X"],
            ["Variance", "Var(X) = E(X²) − [E(X)]²", "any discrete X"],
            ["Function", "E[g(X)] = Σ g(x) P(X = x)", "any function g"],
            ["Coding", "E(aX + b) = aE(X) + b;  Var(aX + b) = a²Var(X)", "a, b constants"],
            ["Sum", "E(X + Y) = E(X) + E(Y)", "always"],
            ["Sum", "Var(X + Y) = Var(X) + Var(Y)", "X, Y independent"],
            ["Uniform on 1 to n", "mean (n + 1)/2, variance (n² − 1)/12", "values equally likely"],
        ]),
        ("warn", "Common mistakes", [
            "Writing Var(X) = Σ x² P(X = x) and forgetting to subtract μ². Always finish with E(X²) − μ².",
            "Squaring the probabilities, Σ x P(X = x)², instead of squaring the values.",
            "Var(aX + b) = aVar(X) + b. The b vanishes and the a is squared: Var(3X − 2) = 9Var(X).",
            "Var(X − Y) = Var(X) − Var(Y). Variances add for differences too.",
            "Treating 2X and X₁ + X₂ as the same random variable. They have equal means but different variances.",
            "Assuming E(1/X) = 1/E(X) or E(X²) = [E(X)]². Use E[g(X)] = Σ g(x)P(X = x).",
            "Using (n² − 1)/12 for a uniform distribution on values that are not consecutive integers without coding first.",
        ]),
        ("p", "<b>Calculator.</b> Most calculators find E(X) and Var(X) from a distribution if you enter the values as data and the "
              "probabilities as frequencies: the mean x̄ is E(X) and the population variance σ² is Var(X). Show the formula in an exam."),
    ],
    "examples": [
        {
            "title": "Constructing a distribution and its cumulative table",
            "question": "Two fair six-sided dice are rolled. X is the larger of the two scores (or the common score if they are "
                        "equal). Find the distribution of X, its cumulative distribution function, the median and mode, E(X) and Var(X).",
            "steps": [
                "X ≤ x means both dice show x or less, so F(x) = P(X ≤ x) = (x/6)² = x²/36 for x = 1, …, 6.",
                "P(X = x) = F(x) − F(x − 1) = [x² − (x − 1)²]/36 = (2x − 1)/36. The probabilities are 1/36, 3/36, 5/36, 7/36, 9/36, 11/36, which add to 36/36 = 1.",
                "Cumulative table: F(1) = 1/36, F(2) = 4/36, F(3) = 9/36, F(4) = 16/36, F(5) = 25/36, F(6) = 1.",
                "Median: F(4) = 16/36 < 0.5 but F(5) = 25/36 ≥ 0.5, so the median is 5. The mode is 6 (largest probability, 11/36).",
                "E(X) = Σ x(2x − 1)/36 = (1 + 6 + 15 + 28 + 45 + 66)/36 = 161/36 ≈ 4.47.",
                "E(X²) = Σ x²(2x − 1)/36 = (1 + 12 + 45 + 112 + 225 + 396)/36 = 791/36.",
                "Var(X) = 791/36 − (161/36)² = 2555/1296 ≈ 1.97 (3 s.f.).",
            ],
        },
        {
            "title": "Two unknown constants",
            "question": "X takes the values 0, 1, 2, 3 with probabilities a, b, 0.3 and 0.1. Given E(X) = 1.2, find a and b, then Var(X).",
            "steps": [
                "Total probability: a + b + 0.3 + 0.1 = 1, so a + b = 0.6.",
                "Mean: 0a + 1b + 2(0.3) + 3(0.1) = 1.2, so b + 0.9 = 1.2 and b = 0.3. Hence a = 0.3.",
                "E(X²) = 0 + 1(0.3) + 4(0.3) + 9(0.1) = 2.4.",
                "Var(X) = 2.4 − 1.2² = 0.96.",
            ],
        },
        {
            "title": "Expectation and variance of a function of X (AQA A level, Edexcel)",
            "question": "X has probability function P(X = x) = k/x for x = 1, 2, 3, 6. Find k, E(X), E(1/X) and Var(6/X).",
            "steps": [
                "k(1 + 1/2 + 1/3 + 1/6) = 2k = 1, so k = 1/2.",
                "E(X) = Σ x(k/x) = 4k = 2.",
                "E(1/X) = Σ (1/x)(k/x) = k(1 + 1/4 + 1/9 + 1/36) = (1/2)(50/36) = 25/36. Note this is not 1/E(X) = 1/2.",
                "E(1/X²) = k Σ 1/x³ = (1/2)(1 + 1/8 + 1/27 + 1/216) = (1/2)(252/216) = 7/12.",
                "Var(1/X) = 7/12 − (25/36)² = 756/1296 − 625/1296 = 131/1296.",
                "Var(6/X) = 6² Var(1/X) = 36 × 131/1296 = 131/36 ≈ 3.64 (3 s.f.).",
            ],
        },
        {
            "title": "Coding and sums of independent variables",
            "question": "X is the score in Worked example AS1.2 (E(X) = 1.2, Var(X) = 0.96). A player wins W = 5X − 2 points. "
                        "Find E(W) and Var(W). The player then plays twice, independently, with scores X₁ and X₂. Find the mean "
                        "and variance of the total score T = X₁ + X₂, and compare with Var(2X).",
            "steps": [
                "E(W) = 5E(X) − 2 = 6 − 2 = 4.   Var(W) = 5² × 0.96 = 24.",
                "E(T) = E(X₁) + E(X₂) = 2.4.",
                "X₁ and X₂ are independent, so Var(T) = 0.96 + 0.96 = 1.92.",
                "Var(2X) = 4 × 0.96 = 3.84. Doubling one score is more variable than adding two independent scores.",
            ],
        },
        {
            "title": "Discrete uniform on other sets of values (MEI, OCR A)",
            "question": "A ticket is drawn at random from tickets numbered 4, 5, 6, 7, 8, 9. Y is its number. Find P(Y > 6), E(Y) and "
                        "Var(Y). A second ticket scheme uses the even numbers 2, 4, …, 20; find the mean and variance of the number drawn.",
            "steps": [
                "There are n = 6 equally likely values, so P(Y > 6) = 3/6 = 0.5.",
                "Y = X + 3 with X uniform on {1, …, 6}. E(Y) = 3.5 + 3 = 6.5, the midpoint of 4 and 9.",
                "Var(Y) = Var(X) = (6² − 1)/12 = 35/12 ≈ 2.92 (3 s.f.).",
                "Even numbers: V = 2X with X uniform on {1, …, 10}. E(V) = 2 × 5.5 = 11 and Var(V) = 4 × (100 − 1)/12 = 33.",
            ],
        },
        {
            "title": "Is the model suitable? (Edexcel)",
            "question": "A spinner is thought to follow P(X = x) = x/10 for x = 1, 2, 3, 4. In 50 spins the results were 1: 6 times, "
                        "2: 8 times, 3: 16 times, 4: 20 times. Compare the data with the model.",
            "steps": [
                "Model: E(X) = (1 + 4 + 9 + 16)/10 = 3 and E(X²) = (1 + 8 + 27 + 64)/10 = 10, so Var(X) = 10 − 9 = 1.",
                "Data: mean = (6 + 16 + 48 + 80)/50 = 150/50 = 3.0. Σx²f = 6 + 32 + 144 + 320 = 502, so variance = 502/50 − 3² = 1.04.",
                "Expected frequencies 50 × x/10: 5, 10, 15, 20, against observed 6, 8, 16, 20.",
                "The means agree exactly and the variances (1 and 1.04) are very close; the frequencies are close too. The data support the model.",
            ],
        },
    ],
    "practice": [
        "A random variable X has P(X = x) = c(6 − x) for x = 0, 1, 2, 3, 4, 5 and 0 otherwise. Find the value of c and P(X ≤ 2).",
        "The distribution of X is given by the table below.  x: 1, 2, 3, 4;  P(X = x): 0.2, 0.4, a, 0.1.  Find a, E(X) and Var(X).",
        "A random variable X has E(X) = 4 and Var(X) = 3. Find E(2X + 5), Var(2X + 5) and E(X²).",
        "A random variable X has P(X = x) = kx² for x = 1, 2, 3 and 0 otherwise. Find k, E(X) and Var(X). Give E(X) and Var(X) to 3 significant figures.",
        "For the random variable in question AS1.4, find E(X² − X).",
        "The cumulative distribution function of X is F(1) = 0.1, F(2) = 0.3, F(3) = 0.45, F(4) = 0.8, F(5) = 1. Find P(X = 3), "
        "P(2 ≤ X ≤ 4), the median and the mode of X.",
        "A fair four-sided die (faces 1 to 4) is rolled twice. S is the sum of the two scores. (a) Construct the probability distribution of S. "
        "(b) Find E(S) and Var(S) from your table. (c) Check your answers using E(S) = 2E(X) and Var(S) = 2Var(X), where X is the score on one roll.",
        "X is uniformly distributed on the integers 1 to 20. Find P(X ≤ 7), E(X), Var(X) and the standard deviation of X.",
        "Y takes the values 5, 10, 15, …, 50, each with equal probability. By writing Y = 5X for a suitable uniform X, find E(Y) and Var(Y).",
        "X takes the values 1, 2 and 4 with probabilities 0.5, 0.3 and 0.2. Find E(1/X), E(X³) and Var(2/X).",
        "X and Y are independent with E(X) = 3, Var(X) = 2, E(Y) = 5 and Var(Y) = 4. Find E(2X − Y + 1) and Var(2X − Y + 1). "
        "X₁, X₂, X₃ are independent observations of X; find Var(X₁ + X₂ + X₃) and Var(3X).",
        "X is uniform on {1, 2, …, n}. (a) Using Σ r² = n(n + 1)(2n + 1)/6, prove that Var(X) = (n² − 1)/12. (b) Given that Var(X) = 10, find n.",
    ],
    "answers": [
        "c(6 + 5 + 4 + 3 + 2 + 1) = 21c = 1, so c = 1/21. P(X ≤ 2) = (6 + 5 + 4)/21 = 15/21 = 5/7.",
        "a = 0.3 (the probabilities sum to 1). E(X) = 0.2 + 0.8 + 0.9 + 0.4 = 2.3. E(X²) = 6.1, so Var(X) = 6.1 − 2.3² = 0.81.",
        "E(2X + 5) = 2(4) + 5 = 13. Var(2X + 5) = 4(3) = 12. E(X²) = Var(X) + [E(X)]² = 3 + 16 = 19.",
        "k(1 + 4 + 9) = 1, so k = 1/14. E(X) = (1 + 8 + 27)/14 = 18/7 ≈ 2.57. E(X²) = (1 + 16 + 81)/14 = 7, so Var(X) = 7 − (18/7)² = 19/49 ≈ 0.388.",
        "E(X² − X) = E(X²) − E(X) = 7 − 18/7 = 31/7 ≈ 4.43.",
        "P(X = 3) = 0.45 − 0.3 = 0.15. P(2 ≤ X ≤ 4) = F(4) − F(1) = 0.7. Median 4 (F(3) = 0.45 < 0.5 ≤ F(4)). The probabilities are "
        "0.1, 0.2, 0.15, 0.35, 0.2, so the mode is 4.",
        "(a) S = 2, 3, 4, 5, 6, 7, 8 with probabilities 1/16, 2/16, 3/16, 4/16, 3/16, 2/16, 1/16. (b) E(S) = 80/16 = 5; E(S²) = 440/16 = 27.5, "
        "so Var(S) = 27.5 − 25 = 2.5. (c) E(X) = 2.5 and Var(X) = (16 − 1)/12 = 1.25, so E(S) = 5 and Var(S) = 2.5, as found.",
        "P(X ≤ 7) = 7/20 = 0.35. E(X) = 21/2 = 10.5. Var(X) = (400 − 1)/12 = 33.25. SD = √33.25 ≈ 5.77.",
        "X is uniform on {1, …, 10}: E(X) = 5.5 and Var(X) = 99/12 = 8.25. So E(Y) = 27.5 and Var(Y) = 25 × 8.25 = 206.25.",
        "E(1/X) = 0.5 + 0.15 + 0.05 = 0.7. E(X³) = 0.5 + 2.4 + 12.8 = 15.7. E(1/X²) = 0.5 + 0.075 + 0.0125 = 0.5875, so "
        "Var(1/X) = 0.5875 − 0.49 = 0.0975 and Var(2/X) = 4 × 0.0975 = 0.39.",
        "E(2X − Y + 1) = 6 − 5 + 1 = 2. Var(2X − Y + 1) = 4(2) + 4 = 12. Var(X₁ + X₂ + X₃) = 3 × 2 = 6, but Var(3X) = 9 × 2 = 18.",
        "(a) E(X) = (n + 1)/2 and E(X²) = (1/n)Σ r² = (n + 1)(2n + 1)/6, so Var(X) = (n + 1)(2n + 1)/6 − (n + 1)²/4 = "
        "(n + 1)(4n + 2 − 3n − 3)/12 = (n + 1)(n − 1)/12 = (n² − 1)/12. (b) n² − 1 = 120, so n = 11.",
    ],
    "exam": [
        "The random variable X has probability function P(X = x) = k(x + 2) for x = 1, 2, 3, 4, and 0 otherwise. "
        "(a) Show that k = 1/18. [2]  (b) Find E(X). [2]  (c) Find Var(X). [3]  (d) In a game a player scores Y = 3X − 2 points. "
        "Find E(Y) and Var(Y). [2]  (e) Find E(1/X). [2]",
        "(a) The random variable X is uniformly distributed on {1, 2, …, n}. Prove that E(X) = (n + 1)/2 and Var(X) = (n² − 1)/12. "
        "You may use Σ r = n(n + 1)/2 and Σ r² = n(n + 1)(2n + 1)/6. [5]  A random number generator produces a digit D from 0, 1, …, 9, "
        "each equally likely. (b) Find E(D) and Var(D). [2]  Two digits D₁ and D₂ are generated independently and used to form the "
        "two-digit number W = 10D₁ + D₂ (so 07 means 7). (c) Find E(W) and Var(W). [3]  (d) Explain why W is uniformly distributed "
        "on {0, 1, …, 99} and use this to check your answer to (c). [2]",
        "A bag contains 3 red and 2 blue counters. Two counters are taken at random without replacement. X is the number of red "
        "counters taken. (a) Show that P(X = 1) = 0.6 and find the rest of the probability distribution of X. [3]  "
        "(b) Find E(X) and Var(X). [3]  (c) Write down the cumulative distribution function of X and find the median. [2]  "
        "(d) The experiment is carried out 50 times, with the counters returned to the bag each time. S is the total number of red "
        "counters taken. Find E(S) and Var(S), stating the assumption you make. [2]",
        "(AQA A level, Edexcel) The random variable X has P(X = x) = x/6 for x = 1, 2, 3. (a) Show that this is a valid probability "
        "distribution. [1]  (b) Find E(X) and Var(X), giving exact answers. [3]  (c) Find E(18X⁻³). [3]  (d) Find Var(6X⁻¹). [4]  "
        "(e) X₁ and X₂ are independent observations of X. Find P(X₁ + X₂ = 4). [2]",
    ],
    "exam_answers": [
        "(a) k(3 + 4 + 5 + 6) = 18k = 1 (M1), so k = 1/18 (A1).  (b) E(X) = (3 + 8 + 15 + 24)/18 = 50/18 = 25/9 ≈ 2.78 (M1 A1).  "
        "(c) E(X²) = (3 + 16 + 45 + 96)/18 = 160/18 = 80/9 (M1 A1); Var(X) = 80/9 − (25/9)² = 95/81 ≈ 1.17 (A1).  "
        "(d) E(Y) = 3(25/9) − 2 = 19/3 ≈ 6.33; Var(Y) = 9 × 95/81 = 95/9 ≈ 10.6 (B1 B1).  "
        "(e) E(1/X) = (1/18)Σ(x + 2)/x = (1/18)(3 + 2 + 5/3 + 3/2) = (1/18)(49/6) = 49/108 ≈ 0.454 (M1 A1).",
        "(a) E(X) = (1/n)Σ r = (n + 1)/2 (M1 A1). E(X²) = (1/n)Σ r² = (n + 1)(2n + 1)/6 (M1). Var(X) = (n + 1)(2n + 1)/6 − (n + 1)²/4 "
        "= (n + 1)(n − 1)/12 (M1) = (n² − 1)/12 (A1, convincing algebra).  (b) D = X − 1 with X uniform on {1, …, 10}: E(D) = 5.5 − 1 = 4.5, "
        "Var(D) = 99/12 = 8.25 (B1 B1).  (c) E(W) = 10(4.5) + 4.5 = 49.5 (B1). Var(W) = 100(8.25) + 8.25 (M1) = 833.25 (A1).  "
        "(d) Each ordered pair (D₁, D₂) has probability 1/100 and gives a different number from 0 to 99, so each value of W has "
        "probability 1/100 (B1). Then E(W) = 99/2 = 49.5 and Var(W) = (100² − 1)/12 = 833.25, agreeing with (c) (B1).",
        "(a) P(X = 1) = (3/5)(2/4) + (2/5)(3/4) = 0.6 (M1 A1). P(X = 0) = (2/5)(1/4) = 0.1, P(X = 2) = (3/5)(2/4) = 0.3 (B1).  "
        "(b) E(X) = 0.6 + 0.6 = 1.2 (B1). E(X²) = 0.6 + 1.2 = 1.8 (M1), so Var(X) = 1.8 − 1.44 = 0.36 (A1).  "
        "(c) F(0) = 0.1, F(1) = 0.7, F(2) = 1 (B1). Median = 1, since F(0) < 0.5 ≤ F(1) (B1).  "
        "(d) Assuming the 50 repeats are independent: E(S) = 50 × 1.2 = 60 and Var(S) = 50 × 0.36 = 18 (B1 B1).",
        "(a) 1/6 + 2/6 + 3/6 = 1 and every probability is between 0 and 1 (B1).  (b) E(X) = (1 + 4 + 9)/6 = 7/3 (B1). "
        "E(X²) = (1 + 8 + 27)/6 = 6 (M1); Var(X) = 6 − 49/9 = 5/9 (A1).  (c) E(18X⁻³) = 18 Σ x⁻³ (x/6) = 3 Σ x⁻² (M1) = "
        "3(1 + 1/4 + 1/9) (M1) = 49/12 ≈ 4.08 (A1).  (d) E(X⁻¹) = Σ (1/x)(x/6) = 3/6 = 1/2 (B1). E(X⁻²) = (1/6)(1 + 1/2 + 1/3) = 11/36 (M1). "
        "Var(X⁻¹) = 11/36 − 1/4 = 1/18 (A1). Var(6X⁻¹) = 36 × 1/18 = 2 (A1).  (e) Pairs (1, 3), (3, 1), (2, 2): "
        "2(1/6)(3/6) + (2/6)² = 10/36 = 5/18 ≈ 0.278 (M1 A1).",
    ],
}
