"""Unit A2.5: Quality of tests — Type I and II errors, size and power (Edexcel FS1 topic 8, AQA SC1–SC2)."""

POWER_TABLE = [
    # Test of H0: lambda = 5 against H1: lambda > 5, critical region X >= 10. Power = P(X >= 10 | lambda).
    ["5", "0.0318"], ["6", "0.0839"], ["7", "0.1695"], ["8", "0.2834"],
    ["9", "0.4126"], ["10", "0.5421"], ["11", "0.6595"], ["12", "0.7576"],
]

UNIT = {
    "number": "A2.5",
    "title": "Quality of tests: Type I and II errors and power",
    "tag": "A level · Edexcel FS1 topic 8 (8.1), with geometric tests from FS1 4.2; AQA SC1 (A level part: normal Type I) "
           "and SC2 · CAIE 9231 assumes the meaning of Type I and II errors (from 9709 S2)",
    "notes": [
        ("p", "A hypothesis test can never be certain to give the right decision. This unit measures how good a test is: "
              "how often it wrongly rejects a true null hypothesis, how often it fails to detect a real change, and how its "
              "ability to detect a change depends on the size of the change, the sample size and the significance level. "
              "These ideas are how statisticians compare tests and decide how much data to collect."),

        ("h2", "5.1 Type I and Type II errors"),
        ("table", ["Decision", "H₀ true", "H₀ false (H₁ true)"], [
            ["Reject H₀", "Type I error, probability α (the size)", "Correct, probability 1 − β (the power)"],
            ["Do not reject H₀", "Correct, probability 1 − α", "Type II error, probability β"],
        ]),
        ("bullets", [
            "A <b>Type I error</b> is rejecting H₀ when H₀ is true: a \"false alarm\".",
            "A <b>Type II error</b> is failing to reject H₀ when H₀ is false: a \"missed change\".",
            "Always describe errors in context, e.g. \"concluding that the machine is producing more defectives when it is not\".",
        ]),

        ("h2", "5.2 The size of a test and P(Type I error)"),
        ("box", "Size", [
            "Size of a test = P(Type I error) = P(reject H₀ | H₀ true) = P(test statistic in critical region | H₀ true).",
            "For a discrete distribution (binomial, Poisson, geometric) this is the actual significance level, usually less than the nominal α.",
            "For a test based on a continuous distribution (e.g. a normal-mean test, AQA SC1), the critical region is chosen to "
            "have probability exactly α, so P(Type I error) = α.",
        ]),

        ("h2", "5.3 P(Type II error) and power"),
        ("p", "H₁ is a whole range of values (e.g. p > 0.3), so P(Type II error) can only be calculated for one particular "
              "value of the parameter in that range. The critical region is always the one found using H₀; only the "
              "distribution changes."),
        ("box", "Type II error and power", [
            "P(Type II error) = P(do not reject H₀ | the parameter has a particular value θ₁ in H₁) = P(test statistic NOT in critical region | θ = θ₁).",
            "Power = P(reject H₀ | θ = θ₁) = 1 − P(Type II error). Power is the probability that the test detects that H₀ is false.",
            "A good test has small size and large power.",
        ]),
        ("p", "Method: (1) find the critical region using the null distribution; (2) change the parameter to the given "
              "alternative value; (3) find the probability of the acceptance region (Type II) or the critical region (power)."),

        ("h2", "5.4 Power functions"),
        ("p", "The <b>power function</b> gives the power for every possible value of the parameter: for a test of θ it is "
              "P(reject H₀ | θ), regarded as a function of θ. At the null value it equals the size of the test. For an "
              "upper-tail test it increases from (almost) 0 to 1 as θ increases; for a lower-tail test it decreases; for a "
              "two-tailed test it has a U-shape with its minimum near the null value. You may be asked to complete a table "
              "of values, sketch the graph, or use it to compare tests."),
        ("p", "The table shows the power function of the test of H₀: λ = 5 against H₁: λ > 5 with critical region X ≥ 10 "
              "(size 0.0318). Plotted against λ it is an S-shaped curve rising from 0.0318 at λ = 5 towards 1."),
        ("table", ["λ", "Power P(X ≥ 10 | λ)"], POWER_TABLE),
        ("p", "Reading the table: if the true mean is 8, the test detects the increase only 28% of the time; the true mean has "
              "to be about 10 before the test is more likely than not to reject H₀. Small changes are hard to detect with a "
              "single observation."),

        ("h2", "5.5 Tests on binomial, Poisson, geometric and normal parameters"),
        ("bullets", [
            "<b>Binomial and Poisson</b> (AQA SC1–SC2, Edexcel): critical regions from cumulative probabilities, exactly as in AS6.",
            "<b>Geometric</b> (Edexcel FS1 4.2): X ~ Geo(p) is the number of trials up to and including the first success. A "
            "small p makes large X likely, so for H₁: p < p₀ the critical region is X ≥ c, with P(X ≥ c) = (1 − p)^(c−1). "
            "For H₁: p > p₀ the critical region is X ≤ c, with P(X ≤ c) = 1 − (1 − p)ᶜ. The power function for "
            "X ≥ c is (1 − p)^(c−1), a formula you can use directly.",
            "<b>Normal mean with known variance</b> (AQA SC1–SC2; Edexcel via A level Mathematics and the CLT): "
            "X̄ ~ N(μ, σ²/n). For H₁: μ > μ₀ at level α the critical region is x̄ > μ₀ + z σ/√n, where P(Z > z) = α. "
            "Then P(Type II | μ = μ₁) = P(X̄ ≤ μ₀ + zσ/√n | μ = μ₁) = Φ((μ₀ + zσ/√n − μ₁)/(σ/√n)).",
        ]),

        ("h2", "5.6 What affects power: sample size, significance level and effect size"),
        ("box", "Trade-offs", [
            "Making α smaller (e.g. 5% to 1%) shrinks the critical region, so P(Type I) falls but P(Type II) rises and power falls.",
            "For a fixed α, increasing the sample size (or observing for longer) makes the test statistic less variable "
            "relative to the change, so power increases. This is the only way to reduce both errors at once.",
            "The further the true parameter is from the null value (the larger the effect size), the greater the power.",
        ]),
        ("p", "To compare two tests with the same size, prefer the one with the higher power across the values in H₁ (its "
              "power curve lies above the other). If one test has both smaller size and higher power, it is better on both "
              "counts, though it may cost more (e.g. a larger sample). If the curves cross, the choice depends on which "
              "alternative values matter most."),
        ("p", "For a normal-mean test you can find the smallest n that gives a required power: write the critical value in "
              "terms of n, set P(reject | μ₁) ≥ the required power, and solve for √n. Always round n <b>up</b>."),
        ("warn", "Common mistakes", [
            "Finding the critical region using the H₁ value instead of the H₀ value.",
            "Giving the nominal level (e.g. 0.05) as P(Type I error) for a discrete test, instead of the actual significance level.",
            "For P(Type II error), using the probability of the critical region rather than of the acceptance region. Power "
            "uses the critical region; Type II uses the rest.",
            "Forgetting that P(X ≥ c) for a geometric variable is (1 − p)^(c−1), not (1 − p)ᶜ.",
            "In a two-tailed test, P(Type II) is the probability of the whole acceptance region between the two tails.",
            "Rounding n down in a sample-size calculation, or using √n where n is needed.",
            "Saying power is the probability that H₁ is true. It is the probability of rejecting H₀ given a particular true value.",
        ]),
    ],
    "examples": [
        {
            "title": "Size, Type II error and power for a binomial test",
            "question": "A test of H₀: p = 0.3 against H₁: p > 0.3 uses X ~ B(20, p) at the 5% level. (a) Find the critical "
                        "region and the size of the test. (b) Find P(Type II error) when p = 0.4, and the power. "
                        "(c) The power when p = 0.5, 0.6 and 0.7 is 0.5881, 0.8725 and 0.9829. Describe the power function.",
            "steps": [
                "(a) Under H₀, X ~ B(20, 0.3). P(X ≥ 10) = 0.0480 ≤ 0.05, P(X ≥ 9) = 0.1133 > 0.05. Critical region X ≥ 10; size 0.0480.",
                "(b) If p = 0.4, X ~ B(20, 0.4). P(Type II) = P(X ≤ 9 | p = 0.4) = 0.7553.",
                "Power = 1 − 0.7553 = 0.2447.",
                "(c) The power rises from 0.0480 at p = 0.3 through 0.2447 (p = 0.4) and 0.5881 (p = 0.5) to nearly 1 at p = 0.7. "
                "The test rarely detects a small increase but almost always detects a large one.",
            ],
        },
        {
            "title": "Power of a Poisson test",
            "question": "The number of complaints a call centre receives per day is Poisson, with mean 5. A manager tests "
                        "H₀: λ = 5 against H₁: λ > 5 at the 5% level using one day's count. (a) Find the critical region and "
                        "the size. (b) Find the power of the test if in fact λ = 8, and interpret it.",
            "steps": [
                "(a) X ~ Po(5). P(X ≥ 10) = 1 − 0.9682 = 0.0318 ≤ 0.05 and P(X ≥ 9) = 0.0681 > 0.05. Critical region X ≥ 10; size 0.0318.",
                "(b) If λ = 8: power = P(X ≥ 10 | λ = 8) = 1 − P(X ≤ 9 | λ = 8) = 1 − 0.7166 = 0.2834.",
                "Even if the mean has risen to 8 complaints a day, the test will detect it on only about 28% of occasions; "
                "P(Type II error) = 0.7166. Counting over several days would give a more powerful test.",
            ],
        },
        {
            "title": "A geometric test and its power function (Edexcel)",
            "question": "A trainee succeeds at a task with probability 0.3 on each attempt. After a change in method, the supervisor "
                        "suspects the probability has fallen. X is the number of attempts up to and including the first success. "
                        "(a) Find the critical region for a test of H₀: p = 0.3 against H₁: p < 0.3 at the 5% level, and its size. "
                        "(b) Write down the power function and find the power when p = 0.1.",
            "steps": [
                "(a) Under H₀, X ~ Geo(0.3) and P(X ≥ c) = 0.7^(c−1). We need 0.7^(c−1) ≤ 0.05.",
                "(c − 1) ≥ ln 0.05 / ln 0.7 = 8.40, so c − 1 = 9 and c = 10. Check: 0.7⁹ = 0.0404 ≤ 0.05 and 0.7⁸ = 0.0576 > 0.05.",
                "Critical region X ≥ 10; size 0.0404.",
                "(b) Power = P(X ≥ 10 | p) = (1 − p)⁹ for 0 < p < 0.3.",
                "When p = 0.1, power = 0.9⁹ = 0.387 (3 s.f.).",
            ],
        },
        {
            "title": "Type II error for a normal-mean test (AQA SC2)",
            "question": "The lengths of bolts are N(μ, 4²) mm. A random sample of 25 is used to test H₀: μ = 50 against H₁: μ > 50 "
                        "at the 5% level. (a) Find the critical region for x̄. (b) Find P(Type I error). (c) Find P(Type II error) "
                        "when μ = 52, and the power.",
            "steps": [
                "(a) Under H₀, X̄ ~ N(50, 4²/25) = N(50, 0.8²). Reject H₀ if x̄ > 50 + 1.6449 × 0.8 = 51.316 (51.3 to 3 s.f.).",
                "(b) The distribution is continuous, so P(Type I error) = 0.05 exactly.",
                "(c) If μ = 52, X̄ ~ N(52, 0.8²). P(Type II) = P(X̄ ≤ 51.316) = Φ((51.316 − 52)/0.8) = Φ(−0.855) = 0.196 (3 s.f.).",
                "Power = 1 − 0.196 = 0.804.",
            ],
        },
        {
            "title": "Choosing the sample size",
            "question": "For the bolts in the previous example, how large a sample is needed so that the test (still at the 5% level) "
                        "has power at least 0.9 when μ = 52?",
            "steps": [
                "With sample size n, the critical value is c = 50 + 1.6449 × 4/√n.",
                "Power when μ = 52 is P(X̄ > c) ≥ 0.9, i.e. (52 − c)/(4/√n) ≥ 1.2816.",
                "So 2√n/4 − 1.6449 ≥ 1.2816, giving √n ≥ 2 × (1.6449 + 1.2816) = 5.853, so n ≥ 34.26.",
                "The smallest sample size is n = 35 (always round up).",
            ],
        },
        {
            "title": "Comparing two tests",
            "question": "A batch of items is accepted if the proportion p of defectives is 0.1, and the buyer wants to detect p > 0.1. "
                        "Test A: inspect 10 items and reject the batch if at least 3 are defective. Test B: inspect 20 items and "
                        "reject if at least 5 are defective. (a) Find the size of each test. (b) Find the power of each test when "
                        "p = 0.3. (c) Which test is better? Give one disadvantage of it.",
            "steps": [
                "(a) Size A = P(X ≥ 3 | B(10, 0.1)) = 0.0702. Size B = P(Y ≥ 5 | B(20, 0.1)) = 0.0432.",
                "(b) Power A = P(X ≥ 3 | B(10, 0.3)) = 0.6172. Power B = P(Y ≥ 5 | B(20, 0.3)) = 0.7625.",
                "(c) Test B has the smaller size and the larger power (it is also more powerful at p = 0.2: 0.3704 against "
                "0.3222), so it is better.",
                "Its disadvantage is cost: it needs twice as many items to be inspected.",
            ],
        },
    ],
    "practice": [
        "A test is carried out to see whether a new drug cures a higher proportion of patients than the current drug. Describe a Type I error and a Type II error in this context, and say which you think is more serious.",
        "A test of H₀: p = 0.5 against H₁: p < 0.5 uses X ~ B(10, p) at the 5% level. (a) Find the critical region and the size. (b) Find P(Type II error) when p = 0.3.",
        "A test of H₀: λ = 4 against H₁: λ > 4 uses one observation of X ~ Po(λ) at the 5% level, with critical region X ≥ 9. Find the power of the test when (a) λ = 6, (b) λ = 8.",
        "A two-tailed test of H₀: λ = 5 uses the critical region X = 0 or X ≥ 11. Find P(Type II error) if in fact λ = 8.",
        "X ~ Geo(p). Show that, at the 5% level, there is no critical region for a test of H₀: p = 0.2 against H₁: p > 0.2 based on a single observation of X.",
        "X ~ N(μ, 9). A random sample of 16 is used to test H₀: μ = 20 against H₁: μ < 20 at the 1% level. (a) Find the critical region. (b) Find P(Type II error) when μ = 18.",
        "X ~ N(μ, 25). A test of H₀: μ = 50 against H₁: μ > 50, based on a sample of 10, rejects H₀ if x̄ > 52. Find the probability of a Type I error.",
        "Sketch, and describe in words, the shape of the power function for (a) an upper-tail test, (b) a two-tailed test. State the value of the power function at the null value of the parameter.",
        "Breakdowns occur at a mean rate λ per hour, and H₀: λ = 2 is tested against H₁: λ > 2 at the 5% level. (a) Using a 1-hour count, find the critical region and the power when λ = 3. (b) Using a 4-hour count, find the critical region and the power when λ = 3. (c) Comment.",
        "For X ~ B(20, p), the test of H₀: p = 0.3 against H₁: p > 0.3 is carried out at the 1% level instead of 5%. Find the new critical region and P(Type II error) when p = 0.4. Compare with Worked example A2.5.1.",
        "For the geometric test in Worked example A2.5.3 (critical region X ≥ 10), (a) find the power when p = 0.2, (b) find the value of p for which the power is 0.5.",
        "Two tests of the same hypotheses have the same size. At every value in H₁, test P has power at least as large as test Q. Explain which test should be used, and why.",
    ],
    "answers": [
        "Type I: concluding the new drug cures a higher proportion when it does not (patients switched to a drug that is no better). Type II: concluding there is no evidence of improvement when the new drug really is better (a better treatment is missed). Either can be argued as more serious; e.g. a Type I error may be more serious if the new drug is costly or has side effects.",
        "(a) P(X ≤ 1 | p = 0.5) = 0.0107 ≤ 0.05, P(X ≤ 2) = 0.0547 > 0.05. Critical region X ≤ 1; size 0.0107. (b) P(Type II) = P(X ≥ 2 | p = 0.3) = 1 − 0.1493 = 0.8507.",
        "(a) P(X ≥ 9 | λ = 6) = 0.1528. (b) P(X ≥ 9 | λ = 8) = 0.4075.",
        "P(Type II) = P(1 ≤ X ≤ 10 | λ = 8) = P(X ≤ 10) − P(X = 0) = 0.8159 − 0.0003 = 0.8156.",
        "For H₁: p > 0.2, small values of X are evidence against H₀, so the critical region has the form X ≤ c. The smallest possible region is X = 1, with P(X = 1) = 0.2 > 0.05. So no critical region exists at the 5% level; a single observation can never be significant.",
        "(a) X̄ ~ N(20, 0.75²). Reject if x̄ < 20 − 2.3263 × 0.75 = 18.255 (18.3 to 3 s.f.). (b) P(X̄ ≥ 18.255 | μ = 18) = 1 − Φ(0.340) = 0.367 (3 s.f.).",
        "Under H₀, X̄ ~ N(50, 2.5). P(X̄ > 52) = 1 − Φ(2/√2.5) = 1 − Φ(1.265) = 0.103 (3 s.f.).",
        "(a) An S-shaped curve increasing from close to 0 (equal to the size at the null value) towards 1 as the parameter increases. (b) A U-shaped curve with its minimum near the null value, rising towards 1 on both sides. At the null value the power function equals the size of the test (P(Type I error)).",
        "(a) X ~ Po(2): P(X ≥ 6) = 0.0166, P(X ≥ 5) = 0.0527, so X ≥ 6; power = P(X ≥ 6 | Po(3)) = 0.0839. (b) Y ~ Po(8): P(Y ≥ 14) = 0.0342, P(Y ≥ 13) = 0.0638, so Y ≥ 14; power = P(Y ≥ 14 | Po(12)) = 0.3185. (c) Observing for longer (a larger sample) gives much greater power for the same significance level.",
        "P(X ≥ 12 | p = 0.3) = 0.0051 ≤ 0.01, P(X ≥ 11) = 0.0171 > 0.01, so the critical region is X ≥ 12. P(Type II | p = 0.4) = P(X ≤ 11) = 0.9435, compared with 0.7553 at 5%. Reducing the significance level reduces P(Type I) but increases P(Type II).",
        "(a) 0.8⁹ = 0.134 (3 s.f.). (b) (1 − p)⁹ = 0.5, so 1 − p = 0.5^(1/9) = 0.9259 and p = 0.0741 (3 s.f.).",
        "Use test P. Both have the same probability of a Type I error, but P is at least as likely to detect any given false null hypothesis, so its probability of a Type II error is never larger. (Its power curve lies on or above Q's.)",
    ],
    "exam": [
        "A factory tests batches for the proportion p of defective items, using H₀: p = 0.1 and H₁: p > 0.1. A sample of 10 is taken. If it has 3 or more defectives the batch is rejected; if it has 0 or 1 the batch is accepted; if it has exactly 2, a second sample of 10 is taken and the batch is rejected if this sample has 2 or more defectives. (Edexcel)\n"
        "(a) Show that the size of this test is 0.121 to 3 significant figures. [4]\n"
        "(b) Find the power of the test when p = 0.3. [3]\n"
        "(c) Find the expected total number of items inspected when p = 0.1. [2]\n"
        "(d) The powers for p = 0.2 and p = 0.4 are 0.511 and 0.948. Describe what these values show about the test. [2]",
        "A machine fills bags of flour whose masses are N(μ, 4²) grams. A random sample of 16 bags is taken to test H₀: μ = 500 against H₁: μ < 500 at the 5% level. (AQA)\n"
        "(a) Find the critical region for x̄. [3]\n"
        "(b) State the probability of a Type I error, and describe a Type I error in this context. [2]\n"
        "(c) Find the probability of a Type II error when μ = 497. [3]\n"
        "(d) Find the smallest sample size for which the power of the test at the 5% level is at least 0.95 when μ = 497. [4]",
        "Accidents at a junction occur at a mean rate of λ per day. A council records the number X of accidents over 2 days to test H₀: λ = 3 against H₁: λ > 3 at the 5% level.\n"
        "(a) Find the critical region and the size of the test. [4]\n"
        "(b) Copy and complete the table of the power function. λ: 3, 4, 5, 6; power: …, 0.1841, …, 0.6528. [3]\n"
        "(c) Describe how the power changes as λ increases, and explain what this means for the council. [2]\n"
        "(d) Suggest how the council could make the test more powerful without changing the significance level. [1]",
        "In a game, X is the number of turns a player takes up to and including the first time they win a prize. The prize probability is claimed to be p = 0.25 per turn. (Edexcel)\n"
        "(a) Find the critical region for a test of H₀: p = 0.25 against H₁: p < 0.25 at the 5% level, using one value of X. [3]\n"
        "(b) Find the size of the test. [1]\n"
        "(c) Show that the power function is (1 − p)¹¹, and find the power when p = 0.1. [3]\n"
        "(d) Explain why a test of H₀: p = 0.25 against H₁: p > 0.25 at the 5% level based on one value of X can never reject H₀. [2]",
    ],
    "exam_answers": [
        "(a) Under p = 0.1, X ~ B(10, 0.1): P(X ≥ 3) = 0.0702 [B1], P(X = 2) = 0.1937 [B1], P(Y ≥ 2) = 0.2639 [B1]. "
        "Size = 0.0702 + 0.1937 × 0.2639 = 0.1213, so 0.121 [M1 A1].\n"
        "(b) p = 0.3: P(X ≥ 3) + P(X = 2)P(Y ≥ 2) [M1] = 0.6172 + 0.2335 × 0.8507 [M1] = 0.816 (3 s.f.) [A1].\n"
        "(c) 10 + 10 × P(X = 2) [M1] = 10 + 1.937 = 11.9 items (3 s.f.) [A1].\n"
        "(d) The power increases from 0.121 at p = 0.1 to 0.948 at p = 0.4 [B1]: the test is likely to detect a large increase in the defective rate but often misses a small one (only about half the time at p = 0.2) [B1].",
        "(a) X̄ ~ N(500, 4²/16) = N(500, 1) under H₀ [B1]. Reject if x̄ < 500 − 1.6449 × 1 [M1] = 498.355, i.e. x̄ < 498.4 (to 4 s.f.) [A1].\n"
        "(b) 0.05 [B1]: concluding that the mean mass is less than 500 g when it is 500 g [B1].\n"
        "(c) If μ = 497, X̄ ~ N(497, 1). P(X̄ ≥ 498.355) [M1] = 1 − Φ(1.355) [M1] = 0.0877 (3 s.f.) [A1].\n"
        "(d) Need P(X̄ < 500 − 1.6449 × 4/√n | μ = 497) ≥ 0.95 [M1], i.e. (3 − 1.6449 × 4/√n)/(4/√n) ≥ 1.6449 [M1]. "
        "3√n/4 ≥ 3.2897, √n ≥ 4.386, n ≥ 19.24 [A1], so n = 20 [A1].",
        "(a) X ~ Po(6) under H₀ [B1]. P(X ≥ 11) = 0.0426 ≤ 0.05 and P(X ≥ 10) = 0.0839 > 0.05 [M1], so the critical region is X ≥ 11 [A1]; size 0.0426 [A1].\n"
        "(b) Power = P(X ≥ 11 | X ~ Po(2λ)) [M1]: λ = 3: 0.0426 [A1]; λ = 5: P(X ≥ 11 | Po(10)) = 0.4170 [A1].\n"
        "(c) The power increases with λ, from 0.0426 to 0.6528 at λ = 6 [B1]. Even if the accident rate doubles to 6 a day, there is about a 35% chance the test will not detect it, so a real increase could easily be missed [B1].\n"
        "(d) Record accidents over more days (a longer period gives a larger mean and a more powerful test) [B1].",
        "(a) X ~ Geo(0.25); reject for large X: P(X ≥ c) = 0.75^(c−1) ≤ 0.05 [M1]. c − 1 ≥ ln 0.05/ln 0.75 = 10.4, so c = 12 [M1]; critical region X ≥ 12 [A1].\n"
        "(b) Size = 0.75¹¹ = 0.0422 [B1].\n"
        "(c) Power = P(X ≥ 12 | p) = P(first 11 turns all fail) = (1 − p)¹¹ [M1 A1]. At p = 0.1, 0.9¹¹ = 0.314 (3 s.f.) [A1].\n"
        "(d) For H₁: p > 0.25, small X is evidence, so the critical region would be X ≤ c [B1]. The smallest possible region X = 1 has probability 0.25 > 0.05, so no critical region exists [B1].",
    ],
}
