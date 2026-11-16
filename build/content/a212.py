UNIT = {
    "number": "A2.12",
    "title": "Non-parametric tests 1: the sign test",
    "tag": "A2 · OCR A (5.07), CAIE 9231 P4 (4.4) · uses the binomial distribution (AS6) and power (A2.5)",
    "notes": [
        ("h2", "12.1 What is a non-parametric test?"),
        ("p", "Most tests met so far are <b>parametric</b>. They assume the population has a particular distribution "
              "(usually normal) and test a value of one of its parameters, such as the mean μ. A t-test on a small sample, "
              "for example, is only valid if the population is normal. A <b>non-parametric</b> (distribution-free) test makes "
              "no assumption about the shape of the population distribution, or only a weak one such as symmetry. "
              "Non-parametric tests usually test the population <b>median</b>, because the median exists for every "
              "distribution and is not dragged about by extreme values."),
        ("bullets", [
            "Use a non-parametric test when the population cannot be assumed to be normal and the sample is too small "
            "for the central limit theorem to help.",
            "Use one when the data are skewed or contain outliers, so the median describes the centre better than the mean.",
            "Use one when the data are only ordinal (ranks, ratings) or when only the direction of each result is known, "
            "for example 'prefers brand A' or 'prefers brand B'.",
            "The price: non-parametric tests use less of the information in the data, so when the parametric "
            "assumptions <i>are</i> true they are less powerful (Section 12.6).",
        ]),
        ("table", ["", "Parametric test (z, t)", "Non-parametric test (sign, Wilcoxon)"], [
            ["Assumption", "Population normal (or n large)", "None (sign test) or symmetry (Wilcoxon)"],
            ["Parameter tested", "Population mean μ", "Population median m"],
            ["Information used", "Actual values", "Signs only, or signs and ranks"],
            ["Power if population is normal", "Highest", "Lower"],
            ["Effect of an outlier", "Large", "Small or none"],
        ]),
        ("h2", "12.2 The basis of the sign test"),
        ("p", "Suppose a continuous population has median m₀. By the definition of the median, a randomly chosen value "
              "is above m₀ with probability ½ and below m₀ with probability ½. Write '+' for an observation above m₀ and "
              "'−' for one below. In a random sample of n observations the signs are independent, each '+' with "
              "probability ½. So the number of '+' signs has the binomial distribution B(n, 0.5). If the true median "
              "is larger than m₀, '+' signs become more likely; if it is smaller, '−' signs become more likely."),
        ("box", "The sign test", [
            "H₀: the population median m = m₀.  H₁: m > m₀, m < m₀ or m ≠ m₀.",
            "Discard any observation equal to m₀ and reduce n accordingly.",
            "Test statistic: X = number of '+' signs (or of '−' signs). Under H₀, X ~ B(n, 0.5).",
            "Find the probability of a result at least as extreme as the one observed (the p-value) and compare it with "
            "the significance level. For a two-tailed test compare the tail probability with half the level.",
            "Because B(n, 0.5) is symmetric, P(X ≥ x) = P(X ≤ n − x).",
        ]),
        ("p", "Why discard values equal to m₀? For a continuous distribution an observation exactly equal to m₀ has "
              "probability 0 in theory, so it only appears because of rounding. It gives no evidence either way, and "
              "keeping it would spoil the B(n, 0.5) model, so both CAIE and OCR exclude it."),
        ("h2", "12.3 The single-sample sign test"),
        ("bullets", [
            "Define the parameter: 'Let m be the population median journey time.' Examiners expect the word "
            "<i>population</i>, and the median, not μ.",
            "Write down the sign of each value minus m₀, discard zeros, and count the signs.",
            "Choose the tail that H₁ predicts. For H₁: m > m₀ find P(X ≥ x) where x is the number of '+' signs. "
            "For H₁: m < m₀ find P(X ≤ x).",
            "Either compare the p-value with the level, or find the critical region from binomial tables and see whether "
            "x lies in it. Because the binomial is discrete, the actual significance level (the probability of the "
            "critical region under H₀) is usually below the nominal level.",
            "Conclude in context, without certainty: 'There is sufficient evidence at the 5% level that the population "
            "median journey time is more than 25 minutes.'",
        ]),
        ("h2", "12.4 The paired-sample sign test"),
        ("p", "In a <b>paired</b> (matched) design each item gives two linked values, such as a patient before and after "
              "treatment, or the same essay marked by two examiners. Work with the differences d = x − y. If the two "
              "populations are identical, each difference is equally likely to be positive or negative, so the number "
              "of positive differences is B(n, 0.5) after zero differences are discarded. This is the paired-sample "
              "sign test. CAIE describes it as a test for the <b>identity of populations</b>."),
        ("box", "Paired-sample sign test", [
            "H₀: the population median of the differences is 0 (no difference between the populations).",
            "H₁: the median difference is > 0, < 0, or ≠ 0.",
            "Discard zero differences. X = number of positive differences ~ B(n, 0.5) under H₀.",
            "To test a median difference of k (e.g. 'improves by more than 2 seconds'), use the signs of d − k.",
        ]),
        ("p", "Paired and two-sample designs are different (OCR 5.07d). Paired data come from the same or matched "
              "individuals, so each value has a partner and the differences remove variation between individuals. "
              "Two independent samples have no natural pairing, possibly different sizes, and need a two-sample test "
              "(the Wilcoxon rank-sum test of Unit A2.13). The sign test is never used on two independent samples. "
              "The sign test is also the natural test when only preferences are recorded: 'better' or 'worse' is all "
              "it needs."),
        ("h2", "12.5 The normal approximation for large samples"),
        ("p", "For a large sample the binomial B(n, 0.5) can be approximated by a normal distribution with mean np = n/2 and "
              "variance np(1 − p) = n/4. Because p = 0.5, the binomial is symmetric and the approximation is good even for "
              "moderate n (n > 20 or so). Use it when n is beyond your binomial tables (the tables in this book stop at "
              "n = 30), or when a question asks for it. A continuity correction is needed because a discrete "
              "distribution is being approximated by a continuous one."),
        ("box", "Normal approximation for the sign test", [
            "X ~ B(n, 0.5) ≈ N(n/2, n/4).",
            "P(X ≥ x) ≈ P(Y ≥ x − 0.5) = P(Z ≥ (x − 0.5 − n/2) ÷ √(n/4)).",
            "P(X ≤ x) ≈ P(Y ≤ x + 0.5) = P(Z ≤ (x + 0.5 − n/2) ÷ √(n/4)).",
            "Compare z with the normal critical value (1.6449 for 5% one-tailed, 1.9600 for 5% two-tailed), or compare the "
            "p-value with the level.",
        ]),
        ("p", "Your calculator's binomial cumulative function gives the exact p-value for any n. Use the exact value when you "
              "can, unless the question asks for the approximation. CAIE prints no sign-test table: the binomial and its "
              "normal approximation are assumed knowledge."),
        ("h2", "12.6 Power, and choosing the sign test"),
        ("p", "The <b>power</b> of a test is the probability of rejecting H₀ when it is false (Unit A2.5). The sign test "
              "throws away the sizes of the deviations from m₀: an observation just above m₀ and one far above it both "
              "count as '+'. When the population really is normal, a test that uses the actual values is more likely to "
              "detect a shift. The table compares the sign test with a z-test of the same size for samples of 20 from a "
              "normal population with σ = 1. H₀: median (= mean) 0, H₁: greater than 0. The sign test rejects H₀ when "
              "X ≥ 15, which has size P(X ≥ 15) = 0.0207 under H₀, and the z-test uses the same size, 0.0207."),
        ("table", ["True median δ", "P(observation > 0) = Φ(δ)", "Power of sign test", "Power of z-test"], [
            ["0.25", "0.5987", "0.1232", "0.1784"],
            ["0.5", "0.6915", "0.3841", "0.5779"],
            ["0.75", "0.7734", "0.7094", "0.9057"],
            ["1", "0.8413", "0.9158", "0.9925"],
        ]),
        ("p", "For a normal population the sign test needs roughly 1.5 times as many observations as the t-test to "
              "reach the same power (its large-sample efficiency is 2/π ≈ 0.64). The Wilcoxon signed-rank test of Unit A2.13 "
              "uses ranks as well as signs and is almost as powerful as the t-test (efficiency 3/π ≈ 0.95). So:"),
        ("bullets", [
            "Population normal (or n large): use the z- or t-test. It is the most powerful.",
            "Population symmetric but not normal: use the Wilcoxon signed-rank test.",
            "Population skewed or shape unknown, outliers present, or only signs/preferences known: use the sign test.",
            "The sign test assumes only that the observations are independent and that the population is continuous.",
        ]),
        ("warn", "Common mistakes", [
            "Writing hypotheses about μ or about 'the median' without saying <i>population</i> median.",
            "Keeping observations equal to m₀ (or zero differences) instead of discarding them and reducing n.",
            "Finding P(X = x) instead of the tail probability P(X ≥ x) or P(X ≤ x).",
            "In a two-tailed test, comparing the tail probability with α instead of α/2.",
            "Using the sign test on two independent samples: it needs pairs.",
            "Forgetting the continuity correction in the normal approximation, or applying it in the wrong direction.",
            "Concluding 'the median is 25' or 'this proves': a test only gives evidence.",
        ]),
    ],
    "examples": [
        {
            "title": "Single-sample sign test, one-tailed",
            "question": "A bus company says the median journey time on a route is 25 minutes. A passenger thinks it is longer. "
                        "She records 12 journey times, in minutes: 27, 31, 24, 29, 25, 33, 28, 26, 30, 22, 35, 27. "
                        "Carry out a sign test at the 5% level.",
            "steps": [
                "Let m be the population median journey time. H₀: m = 25. H₁: m > 25.",
                "Signs of (time − 25): +, +, −, +, 0, +, +, +, +, −, +, +. Discard the 0, so n = 11, with 9 '+' and 2 '−'.",
                "Under H₀, X = number of '+' signs ~ B(11, 0.5).",
                "p-value = P(X ≥ 9) = P(X ≤ 2) = (1 + 11 + 55)/2048 = 67/2048 = 0.0327 (4 d.p.).",
                "0.0327 < 0.05, so reject H₀.",
                "There is sufficient evidence at the 5% level that the population median journey time is more than 25 minutes.",
            ],
        },
        {
            "title": "Two-tailed test using a critical region",
            "question": "Bags of flour are meant to have median mass 1000 g. In a random sample of 17 bags, 12 weigh more than "
                        "1000 g, 4 weigh less and 1 weighs exactly 1000 g. (a) Find the critical region for a two-tailed "
                        "sign test at the 5% level and its actual significance level. (b) Carry out the test.",
            "steps": [
                "(a) Discard the bag at exactly 1000 g: n = 16. Let X = number of bags below 1000 g; under H₀, X ~ B(16, 0.5).",
                "Each tail must have probability ≤ 0.025. P(X ≤ 3) = 0.0106 and P(X ≤ 4) = 0.0384, so the lower tail is X ≤ 3.",
                "By symmetry the upper tail is X ≥ 13. Critical region: X ≤ 3 or X ≥ 13. "
                "Actual significance level = 2 × 0.0106 = 0.0213 (2.13%).",
                "(b) Let m be the population median mass. H₀: m = 1000. H₁: m ≠ 1000.",
                "Observed x = 4, which is not in the critical region (equivalently, P(X ≤ 4) = 0.0384 > 0.025). Do not reject H₀.",
                "There is insufficient evidence at the 5% level that the population median mass differs from 1000 g.",
            ],
        },
        {
            "title": "Paired-sample sign test",
            "question": "Ten people take a reaction-time test (in ms) before and after drinking a cup of coffee.\n"
                        "Before: 312, 285, 298, 330, 276, 301, 290, 315, 288, 305.\n"
                        "After: 296, 280, 301, 318, 276, 289, 284, 309, 292, 291.\n"
                        "Test at the 5% level whether coffee reduces reaction time.",
            "steps": [
                "The data are paired (same person twice), so use differences d = before − after: "
                "16, 5, −3, 12, 0, 12, 6, 6, −4, 14.",
                "Let m be the population median of d. H₀: m = 0. H₁: m > 0 (reaction time is reduced).",
                "Discard the zero difference: n = 9, with 7 positive and 2 negative. Under H₀, X ~ B(9, 0.5).",
                "p-value = P(X ≥ 7) = P(X ≤ 2) = (1 + 9 + 36)/512 = 46/512 = 0.0898 (4 d.p.).",
                "0.0898 > 0.05, so do not reject H₀.",
                "There is insufficient evidence at the 5% level that coffee reduces the population median reaction time. "
                "(The result would be significant at the 10% level.)",
            ],
        },
        {
            "title": "Preferences and the normal approximation",
            "question": "In a taste test, 60 people each compare a new recipe with the old one. 38 prefer the new recipe, "
                        "17 prefer the old one and 5 have no preference. Use a normal approximation to test, at the 1% level, "
                        "whether people tend to prefer the new recipe. Compare with the exact binomial p-value.",
            "steps": [
                "Only preferences are known, so a sign test is the natural choice. Discard the 5 with no preference: n = 55.",
                "Let p be the probability that a randomly chosen person prefers the new recipe. "
                "H₀: p = 0.5 (no tendency either way). H₁: p > 0.5.",
                "Under H₀, X ~ B(55, 0.5) ≈ N(27.5, 13.75).",
                "P(X ≥ 38) ≈ P(Y ≥ 37.5) = P(Z ≥ (37.5 − 27.5)/√13.75) = P(Z ≥ 2.697) = 0.0035 (4 d.p.).",
                "0.0035 < 0.01 (or 2.697 > 2.3263), so reject H₀. There is sufficient evidence at the 1% level that people "
                "tend to prefer the new recipe.",
                "Exact: P(X ≥ 38) = 0.0032 (4 d.p.) from the binomial. The approximation is close and gives the same conclusion.",
            ],
        },
        {
            "title": "Critical region, Type II error and power",
            "question": "A sign test of H₀: m = 50 against H₁: m > 50 is to be carried out at the 5% level using a random "
                        "sample of 20 observations (none equal to 50). (a) Find the critical region and its actual size. "
                        "(b) In fact P(an observation exceeds 50) = 0.7. Find the probability of a Type II error and the power.",
            "steps": [
                "(a) X = number above 50 ~ B(20, 0.5) under H₀. P(X ≥ 15) = 0.0207 and P(X ≥ 14) = 0.0577.",
                "0.0577 > 0.05, so the critical region is X ≥ 15, with actual significance level 0.0207.",
                "(b) Now X ~ B(20, 0.7). A Type II error means not rejecting H₀: P(X ≤ 14) = 0.5836 (4 d.p.).",
                "Power = 1 − 0.5836 = 0.4164.",
                "So even though the true median is well above 50, this test detects it less than half the time. "
                "A larger sample, or a more powerful test if its assumptions hold, would help.",
            ],
        },
    ],
    "practice": [
        "Explain what is meant by a non-parametric test. Give two situations in which a non-parametric test would be "
        "preferred to a t-test.",
        "A sample of 10 values is: 42, 38, 45, 40, 47, 51, 39, 44, 40, 49. Use a sign test at the 5% level to test "
        "H₀: m = 40 against H₁: m > 40, where m is the population median.",
        "X ~ B(14, 0.5). Find the critical region for a one-tailed sign test of H₁: m < m₀ at the 5% level, where X is the "
        "number of '+' signs, and state its actual significance level.",
        "For a two-tailed sign test with n = 18 at the 10% level, find the critical region and its actual significance level.",
        "Eight students sit two tests. Test 1: 54, 61, 48, 70, 66, 59, 72, 50. Test 2: 60, 65, 47, 78, 69, 64, 75, 58. "
        "Use a paired-sample sign test at the 5% level to test whether students tend to score higher on Test 2.",
        "In a sign test with n = 50 there are 33 '+' signs. Use a normal approximation to test H₀: m = m₀ against "
        "H₁: m ≠ m₀ at the 5% level.",
        "A random sample of 26 values contains 7 above 120, 18 below 120 and 1 equal to 120. Test at the 5% level whether "
        "the population median differs from 120.",
        "Explain why observations equal to the hypothesised median are discarded in a sign test.",
        "A coach claims a training programme improves athletes' times by a median of more than 2 seconds. The improvements "
        "(before − after, in seconds) for 10 athletes are: 3.1, 1.4, 2.6, 4.0, 2.0, 2.9, 1.8, 3.5, 2.7, 3.3. "
        "Test the claim at the 5% level.",
        "Twenty judges compare wines A and B. 14 prefer A, 4 prefer B and 2 cannot decide. Test at the 5% level whether "
        "there is a preference for one of the wines.",
        "A sign test of H₀: p = 0.5 against H₁: p > 0.5 uses n = 10 at the 5% level, where p = P(observation > m₀). "
        "(a) Find the critical region. (b) Find the power of the test if in fact p = 0.8.",
        "A sample is drawn from a normal population. Explain why a t-test is preferable to a sign test. Describe a "
        "situation where the sign test is preferable.",
    ],
    "answers": [
        "A test that makes no assumption about the distribution of the population (for example, normality); it usually "
        "tests the median. Preferred when the population cannot be assumed normal and the sample is small; when the data "
        "are skewed or have outliers; when the data are ordinal or only signs/preferences are recorded.",
        "Discard the two 40s: n = 8, with 6 '+' (42, 45, 47, 51, 44, 49) and 2 '−'. X ~ B(8, 0.5). "
        "P(X ≥ 6) = P(X ≤ 2) = 37/256 = 0.1445 > 0.05. Do not reject H₀: insufficient evidence at the 5% level that the "
        "population median exceeds 40.",
        "P(X ≤ 3) = 0.0287 ≤ 0.05 and P(X ≤ 4) = 0.0898 > 0.05. Critical region X ≤ 3; actual significance level 0.0287.",
        "Each tail ≤ 0.05. P(X ≤ 5) = 0.0481, P(X ≤ 6) = 0.1189. Critical region X ≤ 5 or X ≥ 13; "
        "actual significance level 2 × 0.0481 = 0.0963.",
        "d = Test 2 − Test 1: 6, 4, −1, 8, 3, 5, 3, 8: 7 '+', 1 '−', n = 8. H₀: population median difference 0; "
        "H₁: > 0. P(X ≥ 7) = 9/256 = 0.0352 < 0.05. Reject H₀: sufficient evidence at the 5% level that students tend "
        "to score higher on Test 2.",
        "X ~ B(50, 0.5) ≈ N(25, 12.5). P(X ≥ 33) ≈ P(Z ≥ (32.5 − 25)/√12.5) = P(Z ≥ 2.121) = 0.0169 < 0.025 "
        "(or 2.121 > 1.96). Reject H₀: sufficient evidence at the 5% level that the population median differs from m₀. "
        "(Exact binomial: 0.0164.)",
        "Discard the 120: n = 25. H₀: m = 120, H₁: m ≠ 120. X = number above ~ B(25, 0.5). P(X ≤ 7) = 0.0216 < 0.025. "
        "Reject H₀: sufficient evidence at the 5% level that the population median is not 120.",
        "For a continuous population such a value has probability 0 in theory (it arises from rounding), it gives no "
        "evidence for either '+' or '−', and keeping it would mean the count of '+' signs is no longer B(n, 0.5).",
        "Use d − 2: 1.1, −0.6, 0.6, 2.0, 0, 0.9, −0.2, 1.5, 0.7, 1.3. Discard the 0: n = 9, 7 '+', 2 '−'. "
        "H₀: population median improvement = 2; H₁: > 2. P(X ≥ 7) = 46/512 = 0.0898 > 0.05. Do not reject H₀: "
        "insufficient evidence at the 5% level to support the coach's claim.",
        "n = 18 (2 discarded). H₀: p = 0.5 (no preference), H₁: p ≠ 0.5. P(X ≥ 14) = P(X ≤ 4) = 0.0154 < 0.025. "
        "Reject H₀: sufficient evidence at the 5% level of a preference (for wine A).",
        "(a) P(X ≥ 9) = 11/1024 = 0.0107 ≤ 0.05, P(X ≥ 8) = 0.0547 > 0.05, so critical region X ≥ 9 (actual size 0.0107). "
        "(b) X ~ B(10, 0.8): power = P(X ≥ 9) = 0.3758.",
        "The t-test uses the actual values, not just their signs, so for normal data it is more powerful: it is more "
        "likely to detect a real difference with the same sample size. The sign test is preferable when the population "
        "is clearly skewed or not normal and the sample is small, when there are outliers, or when only preferences "
        "or directions are recorded.",
    ],
    "exam": [
        "The prices, in £1000s, of 12 houses sold recently in a town are: 185, 240, 172, 410, 198, 225, 168, 205, 950, "
        "192, 215, 162.\n"
        "(a) Give two reasons why a t-test for the mean price would not be suitable. [2]\n"
        "(b) An estate agent claims that the median price of houses in the town is more than £175 000. Test this claim "
        "at the 10% level using a sign test. [5]\n"
        "(c) For this test with n = 12, find the critical region and its actual significance level. [2]\n"
        "(d) Explain why a Wilcoxon signed-rank test may also be unsuitable for these data. [1]",
        "In a trial, each of 45 patients tries two pain-relief creams, A and B, on different days, and reports which one "
        "relieved the pain better. 29 say B was better, 13 say A was better and 3 report no difference.\n"
        "(a) Explain why a sign test is appropriate. [1]\n"
        "(b) State suitable hypotheses for testing whether B tends to be better. [1]\n"
        "(c) Use a normal approximation to carry out the test at the 5% level. [5]\n"
        "(d) The exact binomial p-value is 0.0098 to 4 d.p. Comment on the accuracy of the approximation. [1]",
        "A sign test of H₀: m = 8 against H₁: m < 8, where m is the population median, uses a random sample of 15 "
        "observations (none equal to 8) and a 5% significance level. Let X be the number of observations below 8.\n"
        "(a) Find the critical region for X and state the probability of a Type I error. [3]\n"
        "(b) In fact P(an observation is below 8) = 0.75. Find the probability of a Type II error. [2]\n"
        "(c) In the sample, 11 observations are below 8 and 4 are above. State the conclusion of the test. [2]\n"
        "(d) The population is known to be normal. Explain why a t-test would be a better choice. [2]",
        "Two judges each score the same 12 skaters.\n"
        "Judge A: 7.2, 6.8, 8.1, 5.9, 7.5, 6.4, 8.3, 7.0, 6.6, 7.8, 5.5, 7.1.\n"
        "Judge B: 6.9, 6.1, 7.6, 6.2, 7.0, 6.4, 7.7, 6.5, 6.3, 7.9, 5.0, 6.6.\n"
        "(a) Explain why a test for two independent samples would not be appropriate. [1]\n"
        "(b) Use a sign test at the 5% level to test whether the judges differ in their scoring. [6]\n"
        "(c) State the smallest two-tailed significance level, of the form 1%, 2%, 5%, 10%, at which the result would be "
        "significant. [1]\n"
        "(d) State one assumption needed for the test. [1]",
    ],
    "exam_answers": [
        "(a) The sample is small and the prices are skewed with an outlier (950), so the population cannot be assumed "
        "normal; the mean is distorted by the outlier, so the median is a better measure of centre. B1 B1. "
        "(b) Let m = population median price (£1000s). H₀: m = 175, H₁: m > 175. B1. Above 175: 9; below: 3 "
        "(172, 168, 162); n = 12. M1. X ~ B(12, 0.5); P(X ≥ 9) = P(X ≤ 3) = 299/4096 = 0.0730. M1 A1. "
        "0.0730 < 0.10: reject H₀; sufficient evidence at the 10% level that the population median price is more than "
        "£175 000. A1. "
        "(c) P(X ≥ 9) = 0.0730 ≤ 0.1, P(X ≥ 8) = 0.1938 > 0.1. Critical region X ≥ 9; actual level 0.0730. M1 A1. "
        "(d) The Wilcoxon test requires a symmetric population; house prices are clearly skewed. B1.",
        "(a) Only the direction of each preference is known (no sizes), and the data are paired. B1. "
        "(b) H₀: p = 0.5, H₁: p > 0.5, where p is the probability that a randomly chosen patient finds B better "
        "(equivalently, population median difference B − A is 0 against > 0). B1. "
        "(c) Discard 3: n = 42. X ~ B(42, 0.5) ≈ N(21, 10.5). B1 M1. P(X ≥ 29) ≈ P(Z ≥ (28.5 − 21)/√10.5) "
        "= P(Z ≥ 2.315) = 0.0103. M1 (continuity correction) A1. 0.0103 < 0.05 (2.315 > 1.6449): reject H₀. Sufficient "
        "evidence at the 5% level that cream B tends to be better. A1. "
        "(d) 0.0103 against 0.0098: the approximation is good (error about 0.0005), because p = 0.5 makes the binomial "
        "symmetric. B1.",
        "(a) Under H₀, X ~ B(15, 0.5). P(X ≥ 12) = 0.0176 ≤ 0.05, P(X ≥ 11) = 0.0592 > 0.05. M1 A1. Critical region "
        "X ≥ 12; P(Type I error) = 0.0176. A1. "
        "(b) X ~ B(15, 0.75): P(Type II) = P(X ≤ 11) = 0.5387 (4 d.p.). M1 A1. "
        "(c) x = 11 is not in the critical region. Do not reject H₀: insufficient evidence at the 5% level that the "
        "population median is less than 8. M1 A1. "
        "(d) For a normal population the t-test uses the actual values rather than just their signs, so it is more "
        "powerful (a lower probability of a Type II error for the same sample size and level). B1 B1.",
        "(a) The same skaters are scored by both judges, so the scores are paired, not independent. B1. "
        "(b) d = A − B: 0.3, 0.7, 0.5, −0.3, 0.5, 0, 0.6, 0.5, 0.3, −0.1, 0.5, 0.5. M1. Discard the 0: n = 11, 9 '+', "
        "2 '−'. A1. H₀: population median difference = 0; H₁: ≠ 0. B1. X ~ B(11, 0.5); P(X ≥ 9) = 67/2048 = 0.0327. M1. "
        "Two-tailed: 0.0327 > 0.025, so do not reject H₀. A1. Insufficient evidence at the 5% level that the judges "
        "differ in their scoring. A1. "
        "(c) 10% (p-value 2 × 0.0327 = 0.0654 < 0.10). B1. "
        "(d) The skaters are a random sample and the differences are independent (from a continuous distribution). B1.",
    ],
}
