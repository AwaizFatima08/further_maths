UNIT = {
    "number": "A2.8",
    "title": "z-tests and intervals: one and two samples",
    "tag": "A2 · Edexcel FS2, IAL S3, OCR A, OCR MEI, CAIE 9231 P4 · two-sample sections: Edexcel, IAL S3, CAIE only",
    "notes": [
        ("p", "This unit collects every inference about means that uses the normal distribution: a test and an interval for a "
              "single mean, and a test and an interval for the difference between two means. Unit AS12 introduced confidence "
              "intervals and Unit A2.7 the Central Limit Theorem (CLT); here we turn them into full hypothesis tests. The statistic "
              "is always called z, because under H₀ it has (exactly or approximately) the standard normal distribution N(0, 1)."),

        ("h2", "8.1 When is a z statistic valid?"),
        ("p", "Let X̄ be the mean of a random sample of size n from a population with mean μ and variance σ². "
              "Then E(X̄) = μ and Var(X̄) = σ²/n. The standard deviation of X̄, σ/√n, is called the <b>standard error</b> of the mean. "
              "A z statistic needs X̄ to be normal (or nearly normal) and needs a value for σ. There are three situations in which this works."),
        ("table", ["Case", "Why X̄ is normal", "Value used for σ", "Distribution of z under H₀"], [
            ["1. Normal population, σ known", "X̄ ~ N(μ, σ²/n) exactly, for any n", "σ", "exactly N(0, 1)"],
            ["2. Any population, σ known, n large", "CLT: X̄ ≈ N(μ, σ²/n)", "σ", "approximately N(0, 1)"],
            ["3. Any population, σ unknown, n large", "CLT: X̄ ≈ N(μ, σ²/n)", "s, the unbiased estimate", "approximately N(0, 1)"],
            ["Normal population, σ unknown, n small", "X̄ is normal, but s is unreliable", "s", "use t(n − 1): Unit A2.9"],
        ]),
        ("p", "In case 3 two approximations are made: the CLT makes X̄ approximately normal, and because n is large, s is close to σ. "
              "\"Large\" is a rule of thumb: OCR A uses n more than about 25; MEI, Edexcel and CAIE usually use n ≥ 30. "
              "IAL S3 does not use the t distribution at all, so its large-sample tests are always z tests."),
        ("box", "Unbiased estimates from data (all boards)", [
            "x̄ = Σx / n.",
            "s² = Σ(x − x̄)²/(n − 1) = [Σx² − (Σx)²/n]/(n − 1) = (Σx² − n x̄²)/(n − 1).",
            "s² (divisor n − 1) is an unbiased estimate of σ². On a calculator it is the square of sₓ (or σₙ₋₁), not σₓ.",
        ]),

        ("h2", "8.2 The one-sample z-test for a mean"),
        ("p", "The test asks whether a sample mean is far enough from a claimed value μ₀ to doubt the claim. The steps are the same "
              "for every test in this book."),
        ("bullets", [
            "1. Define the parameter: \"μ is the population mean mass, in grams, of ...\".",
            "2. State H₀: μ = μ₀ and H₁: μ > μ₀, μ < μ₀ (one-tailed) or μ ≠ μ₀ (two-tailed). Hypotheses are about μ, never about x̄.",
            "3. Under H₀, Z = (X̄ − μ₀)/(σ/√n) ~ N(0, 1). Calculate z = (x̄ − μ₀)/(σ/√n), using s for σ in case 3.",
            "4. Compare z with the critical value (or compare the p-value with the significance level).",
            "5. Decide: reject H₀, or do not reject H₀. Then conclude in context, without certainty.",
        ]),
        ("table", ["Significance level", "One-tailed critical value", "Two-tailed critical values"], [
            ["10%", "1.2816", "±1.6449"],
            ["5%", "1.6449", "±1.9600"],
            ["2.5%", "1.9600", "±2.2414 (calculator)"],
            ["1%", "2.3263", "±2.5758"],
        ]),
        ("p", "The <b>p-value</b> is the probability, if H₀ is true, of a result at least as extreme as the one observed. "
              "For an upper-tailed test p = P(Z ≥ z); for a two-tailed test p = 2 × P(Z ≥ |z|). Reject H₀ if p is less than the "
              "significance level. The <b>critical region</b> can also be written in terms of x̄: for H₁: μ > μ₀ at 5%, "
              "reject H₀ if x̄ > μ₀ + 1.6449σ/√n."),

        ("h2", "8.3 Confidence intervals for μ and the link with tests"),
        ("box", "Confidence interval for a mean", [
            "Symmetric 100(1 − α)% confidence interval for μ:  x̄ ± z × σ/√n, where P(Z > z) = α/2.",
            "90%: z = 1.6449.   95%: z = 1.9600.   98%: z = 2.3263.   99%: z = 2.5758.",
            "Use s for σ when σ is unknown and n is large (case 3).",
        ]),
        ("p", "Interpretation: if many samples were taken and an interval calculated from each, about 95% of the 95% intervals would "
              "contain the true value of μ. A single calculated interval either contains μ or it does not; the 95% describes the method. "
              "An interval is narrower when n is larger, when σ is smaller or when the confidence level is lower."),
        ("p", "<b>Link with tests.</b> A two-tailed test of H₀: μ = μ₀ at the α significance level rejects H₀ exactly when μ₀ lies "
              "outside the 100(1 − α)% confidence interval. So a 95% interval contains all the values of μ₀ that a two-tailed 5% test "
              "would not reject. A one-tailed test at 5% matches a 90% two-sided interval, not a 95% one."),

        ("h2", "8.4 Two-sample z-test (Edexcel FS2, IAL S3, CAIE)"),
        ("p", "Two <b>independent</b> random samples, of sizes nₓ and n<sub>y</sub>, are taken from populations with means μₓ, μ<sub>y</sub> and variances "
              "σₓ², σ<sub>y</sub>². By the result for linear combinations (Unit A2.6), Var(X̄ − Ȳ) = σₓ²/nₓ + σ<sub>y</sub>²/n<sub>y</sub>. The variances add, even "
              "though the means are subtracted."),
        ("box", "Two-sample z statistic", [
            "If both populations are normal: X̄ − Ȳ ~ N(μₓ − μ<sub>y</sub>, σₓ²/nₓ + σ<sub>y</sub>²/n<sub>y</sub>).",
            "Under H₀: μₓ − μ<sub>y</sub> = c, the test statistic is  z = [(x̄ − ȳ) − c] / √(σₓ²/nₓ + σ<sub>y</sub>²/n<sub>y</sub>)  ~ N(0, 1).",
            "Usually c = 0. A claim such as \"X exceeds Y by more than 2 on average\" gives H₀: μₓ − μ<sub>y</sub> = 2, H₁: μₓ − μ<sub>y</sub> > 2.",
            "Large samples, variances unknown (Edexcel 5.5, IAL S3 3.8, CAIE): replace σₓ², σ<sub>y</sub>² by sₓ², s<sub>y</sub>². By the CLT the result is approximately N(0, 1) and the populations need not be normal.",
        ]),
        ("p", "Do <b>not</b> pool the two sample variances in a z test. Pooling assumes the population variances are equal, which is "
              "only needed for the two-sample t-test of Unit A2.10. In a large-sample z test each sample keeps its own variance."),

        ("h2", "8.5 Confidence interval for a difference of means (Edexcel, IAL S3, CAIE)"),
        ("p", "In the same situations, a 100(1 − α)% confidence interval for μₓ − μ<sub>y</sub> is "
              "(x̄ − ȳ) ± z √(σₓ²/nₓ + σ<sub>y</sub>²/n<sub>y</sub>), with sₓ², s<sub>y</sub>² in place of the variances for large samples. If the interval contains 0 "
              "there is no evidence, at the matching two-tailed level, of a difference between the means. If it lies entirely above 0, "
              "the evidence suggests μₓ > μ<sub>y</sub>."),

        ("h2", "8.6 Conditions, justification and paired data"),
        ("bullets", [
            "Random and independent: each sample must be random, and in a two-sample test the samples must be independent of each other.",
            "Normality: needed for small samples (case 1). For large samples, quote the CLT: \"the samples are large, so by the CLT the sample means are approximately normally distributed\". Examiners (CAIE 2023) do not accept \"n > 30\" on its own.",
            "Unknown variances: say that because the samples are large, sₓ² and s<sub>y</sub>² are good estimates of σₓ² and σ<sub>y</sub>².",
            "The CLT is about the distribution of X̄, not of X. Never write \"by the CLT, X is normal\".",
            "Paired data (the same subjects measured twice) are not two independent samples. Work with the differences d and use a one-sample method on them. MEI (SI11) asks for a z interval for the mean difference when the number of pairs is large: d̄ ± z s<sub>d</sub>/√n. Small paired samples use t (Unit A2.10).",
        ]),
        ("p", "Calculator: most calculators run a \"1-sample Z test\" and \"2-sample Z test\" directly and give z and the p-value. "
              "You must still write the hypotheses, the value of the test statistic, the comparison and the conclusion in context."),
        ("warn", "Common mistakes", [
            "Writing hypotheses in terms of x̄ or using the sample value: H₀ must be about the population parameter μ.",
            "Using the two-tailed value 1.96 in a one-tailed 5% test (the correct value is 1.6449), or the other way round.",
            "Forgetting to square standard deviations in √(σₓ²/nₓ + σ<sub>y</sub>²/n<sub>y</sub>), or subtracting the variances.",
            "Using σₙ (divisor n) from the calculator instead of s (divisor n − 1) when estimating σ².",
            "Pooling the variances in a large-sample z test, or treating paired data as two independent samples.",
            "Concluding with certainty (\"this proves the mean has increased\") or without context. Write \"there is sufficient evidence at the 5% level that the mean ... has increased\".",
        ]),
    ],
    "examples": [
        {
            "title": "One-sample z-test with a known standard deviation",
            "question": "The masses of bags of rice filled by a machine are normally distributed with standard deviation 4.2 g. "
                        "The label says the mean mass is 500 g. A random sample of 20 bags has mean mass 497.8 g. Test, at the 5% "
                        "significance level, whether the mean mass is less than 500 g. Give the p-value and the critical region for x̄.",
            "steps": [
                "Let μ be the population mean mass of bags filled by the machine, in grams.",
                "H₀: μ = 500, H₁: μ < 500 (one-tailed, 5%).",
                "The population is normal with σ known, so under H₀, X̄ ~ N(500, 4.2²/20) and Z = (X̄ − 500)/(4.2/√20) ~ N(0, 1).",
                "z = (497.8 − 500)/(4.2/√20) = −2.2/0.93915 = −2.34 (3 s.f.).",
                "Critical value: −1.6449. Since −2.34 < −1.6449, z is in the critical region. The p-value is P(Z ≤ −2.3425) = 0.0096 < 0.05.",
                "Critical region for x̄: x̄ < 500 − 1.6449 × 0.93915 = 498.455, so x̄ < 498.46 g. The observed 497.8 g lies inside it.",
                "Reject H₀. There is sufficient evidence at the 5% level that the mean mass of the bags is less than 500 g.",
            ],
        },
        {
            "title": "Large sample, unknown variance, from summary data",
            "question": "The times, x minutes, taken by a random sample of 60 adults to complete a puzzle give Σx = 1830 and "
                        "Σx² = 57 240. (a) Find unbiased estimates of the population mean and variance. (b) Test, at the 5% level, "
                        "whether the mean time differs from 29 minutes. (c) Find a 95% confidence interval for the mean and comment.",
            "steps": [
                "(a) x̄ = 1830/60 = 30.5. s² = (57 240 − 1830²/60)/59 = (57 240 − 55 815)/59 = 1425/59 = 24.2 (3 s.f.), so s = 4.9145.",
                "(b) Let μ be the population mean time in minutes. H₀: μ = 29, H₁: μ ≠ 29 (two-tailed, 5%).",
                "The sample is large, so by the CLT X̄ is approximately normal, and s is a good estimate of σ. Under H₀, Z = (X̄ − 29)/(σ/√60) ≈ N(0, 1).",
                "Standard error: 4.9145/√60 = 0.63446. z = (30.5 − 29)/0.63446 = 2.36 (3 s.f.).",
                "Critical values ±1.96. Since 2.36 > 1.96, reject H₀ (p-value = 2 × P(Z > 2.364) = 0.0181).",
                "There is sufficient evidence at the 5% level that the mean time to complete the puzzle is not 29 minutes.",
                "(c) 30.5 ± 1.96 × 0.63446 = 30.5 ± 1.2435, giving (29.26, 31.74) minutes (2 d.p.).",
                "29 lies outside the interval, which agrees with the two-tailed 5% test in (b).",
            ],
        },
        {
            "title": "Two-sample z-test with known variances",
            "question": "The lengths of rods from machine A are normally distributed with standard deviation 1.2 cm, and from machine B "
                        "with standard deviation 1.5 cm. A random sample of 15 rods from A has mean 25.4 cm and an independent random "
                        "sample of 12 rods from B has mean 24.3 cm. Test, at the 5% level, whether the mean lengths differ.",
            "steps": [
                "Let μ<sub>A</sub> and μ<sub>B</sub> be the population mean lengths, in cm, of rods from A and B.",
                "H₀: μ<sub>A</sub> = μ<sub>B</sub>, H₁: μ<sub>A</sub> ≠ μ<sub>B</sub> (two-tailed, 5%).",
                "Both populations are normal with known variances and the samples are independent, so under H₀, X̄<sub>A</sub> − X̄<sub>B</sub> ~ N(0, 1.2²/15 + 1.5²/12).",
                "Standard error: √(1.44/15 + 2.25/12) = √(0.096 + 0.1875) = √0.2835 = 0.53245.",
                "z = (25.4 − 24.3)/0.53245 = 2.07 (3 s.f.).",
                "Critical values ±1.96. Since 2.07 > 1.96, reject H₀ (p-value 0.0388).",
                "There is sufficient evidence at the 5% level that the mean lengths of rods from the two machines are different.",
            ],
        },
        {
            "title": "Large samples: testing a claimed difference, and an interval",
            "question": "A random sample of 50 brand A batteries had mean lifetime 42.8 hours and standard deviation 5.1 hours. "
                        "An independent random sample of 40 brand B batteries had mean 39.1 hours and standard deviation 4.3 hours. "
                        "(a) Test, at the 5% level, the claim that brand A batteries last more than 2 hours longer on average. "
                        "(b) Find a 95% confidence interval for the difference in mean lifetimes. (c) Explain why you did not need to "
                        "assume that lifetimes are normally distributed.",
            "steps": [
                "(a) Let μ<sub>A</sub> and μ<sub>B</sub> be the population mean lifetimes in hours. H₀: μ<sub>A</sub> − μ<sub>B</sub> = 2, H₁: μ<sub>A</sub> − μ<sub>B</sub> > 2 (one-tailed, 5%).",
                "Standard error: √(5.1²/50 + 4.3²/40) = √(0.5202 + 0.46225) = √0.98245 = 0.99119.",
                "z = (42.8 − 39.1 − 2)/0.99119 = 1.7/0.99119 = 1.72 (3 s.f.).",
                "Critical value 1.6449. Since 1.72 > 1.6449, reject H₀ (p-value 0.0432).",
                "There is sufficient evidence at the 5% level to support the claim that brand A batteries last more than 2 hours longer on average.",
                "(b) 3.7 ± 1.96 × 0.99119 = 3.7 ± 1.9427, so the interval is (1.76, 5.64) hours (3 s.f.).",
                "(c) Both samples are large, so by the CLT the sample means are approximately normal whatever the distribution of lifetimes, and the sample variances are good estimates of the population variances.",
            ],
        },
        {
            "title": "Exam standard: summary data from two large samples (CAIE style)",
            "question": "The weekly distances, x km, run by 80 randomly chosen members of club P and the distances, y km, run by 100 "
                        "randomly chosen members of club Q are summarised by: Σx = 3376, Σx² = 146 700, Σy = 4050, Σy² = 168 900. "
                        "(a) Test, at the 5% level, whether members of P run further on average than members of Q. "
                        "(b) Find the p-value and state the smallest one-tailed significance level, from 10%, 5%, 2.5% and 1%, at which H₀ would be rejected. "
                        "(c) Explain why a two-sample t-test with a pooled variance is not used here.",
            "steps": [
                "(a) x̄ = 3376/80 = 42.2; sₓ² = (146 700 − 3376²/80)/79 = 53.580. ȳ = 4050/100 = 40.5; s<sub>y</sub>² = (168 900 − 4050²/100)/99 = 49.242.",
                "Let μ<sub>P</sub> and μ<sub>Q</sub> be the population mean weekly distances in km. H₀: μ<sub>P</sub> = μ<sub>Q</sub>, H₁: μ<sub>P</sub> > μ<sub>Q</sub> (one-tailed, 5%).",
                "Both samples are large, so by the CLT X̄ − Ȳ is approximately normal, and sₓ², s<sub>y</sub>² estimate the population variances well.",
                "Standard error: √(53.580/80 + 49.242/100) = √(0.66975 + 0.49242) = 1.0780.",
                "z = (42.2 − 40.5)/1.0780 = 1.58 (3 s.f.). Critical value 1.6449. Since 1.58 < 1.6449, do not reject H₀.",
                "There is insufficient evidence at the 5% level that members of club P run further on average than members of club Q.",
                "(b) p-value = P(Z > 1.5769) = 0.0574. This is less than 0.10 but more than 0.05, so H₀ would be rejected at the 10% level but not at 5%.",
                "(c) A pooled test assumes the population variances are equal (and normal populations for small samples). Nothing says the variances are equal, and the samples are large, so each sample's own variance is used in a z test.",
            ],
        },
    ],
    "practice": [
        "The lengths of bolts are normally distributed with standard deviation 0.8 mm. A random sample of 16 bolts has mean length 25.42 mm. Test, at the 1% level, whether the mean length of bolts is greater than 25 mm.",
        "Marks in an exam are normally distributed with standard deviation 12. A random sample of 30 marks has mean 58.1. Test H₀: μ = 62 against H₁: μ ≠ 62. Find the p-value and state your conclusion at the 5% level.",
        "The delivery times, x minutes, of a random sample of 50 deliveries give Σx = 1612 and Σx² = 54 080. (a) Find unbiased estimates of the population mean and variance. (b) Test, at the 5% level, whether the mean delivery time is more than 31 minutes.",
        "A population is normal with standard deviation 3. A test of H₀: μ = 40 against H₁: μ < 40 uses a random sample of 25 values at the 5% level. Find the critical region for x̄.",
        "A random sample of 64 observations has mean 12.6 and unbiased standard deviation estimate 2.4. (a) Find a 95% confidence interval for the population mean. (b) A manufacturer claims the mean is 13. Comment on the claim.",
        "A 95% confidence interval for a population mean, calculated from a large random sample of 50 observations, is (12.1, 13.5). (a) Find the sample mean and the value of s used. (b) Find the corresponding 99% confidence interval.",
        "(Edexcel, IAL S3, CAIE) Population A is normal with standard deviation 6 and population B is normal with standard deviation 8. A random sample of 36 from A has mean 71.2, and an independent random sample of 40 from B has mean 67.9. Test, at the 5% level, whether the mean of A is greater than the mean of B.",
        "(Edexcel, IAL S3, CAIE) Independent random samples give n₁ = 45, x̄₁ = 58.3, s₁ = 6.2 and n₂ = 55, x̄₂ = 51.1, s₂ = 5.4. Test H₀: μ₁ − μ₂ = 5 against H₁: μ₁ − μ₂ ≠ 5 at the 5% level.",
        "(Edexcel, IAL S3, CAIE) Independent random samples give n₁ = 70, x̄₁ = 14.6, s₁ = 3.1 and n₂ = 80, x̄₂ = 13.2, s₂ = 2.7. Find a 90% confidence interval for μ₁ − μ₂ and say what it suggests about the two means.",
        "For each of the following, state whether the population must be assumed normal for the z-test to be valid, with a reason: (a) question 1; (b) question 3; (c) question 7.",
        "A population has standard deviation 5. A test of H₀: μ = 80 against H₁: μ > 80 at the 5% level gives a sample mean of 81.2. Find the least sample size n for which H₀ would be rejected.",
        "(OCR MEI) Forty randomly chosen runners each ran a 5 km time trial on two different shoes. The differences d = (time in shoe A) − (time in shoe B), in seconds, have mean 1.35 and standard deviation 2.8. Find a 95% confidence interval for the population mean difference and comment.",
    ],
    "answers": [
        "H₀: μ = 25, H₁: μ > 25. z = (25.42 − 25)/(0.8/√16) = 0.42/0.2 = 2.10. 2.10 < 2.3263, so do not reject H₀. There is insufficient evidence at the 1% level that the mean length is greater than 25 mm.",
        "z = (58.1 − 62)/(12/√30) = −3.9/2.1909 = −1.78. p-value = 2 × P(Z < −1.780) = 0.0751 > 0.05, so do not reject H₀. There is insufficient evidence at the 5% level that the mean mark differs from 62.",
        "(a) x̄ = 32.24, s² = (54 080 − 1612²/50)/49 = 43.0 (3 s.f.). (b) H₀: μ = 31, H₁: μ > 31. Large sample, so by the CLT z = (32.24 − 31)/(6.5607/√50) = 1.34. 1.34 < 1.6449, so do not reject H₀: insufficient evidence at 5% that the mean delivery time is more than 31 minutes.",
        "Reject H₀ if x̄ < 40 − 1.6449 × 3/√25 = 39.013, i.e. the critical region is x̄ < 39.01 (2 d.p.).",
        "(a) Standard error 2.4/8 = 0.3. 12.6 ± 1.96 × 0.3 = (12.01, 13.19) (2 d.p.). (b) 13 lies inside the interval, so there is no evidence at the 5% (two-tailed) level against the claim.",
        "(a) x̄ = (12.1 + 13.5)/2 = 12.8. Half-width 0.7 = 1.96 × s/√50, so s = 0.7√50/1.96 = 2.53 (3 s.f.). (b) 12.8 ± 2.5758 × 0.7/1.96 = 12.8 ± 0.91993, giving (11.88, 13.72) (2 d.p.).",
        "H₀: μ<sub>A</sub> = μ<sub>B</sub>, H₁: μ<sub>A</sub> > μ<sub>B</sub>. Standard error √(36/36 + 64/40) = √2.6 = 1.6125. z = 3.3/1.6125 = 2.05 (3 s.f.). 2.05 > 1.6449, so reject H₀: sufficient evidence at 5% that the mean of A is greater than the mean of B.",
        "Standard error √(6.2²/45 + 5.4²/55) = √1.3844 = 1.1766. z = (7.2 − 5)/1.1766 = 1.87 (3 s.f.). |1.87| < 1.96, so do not reject H₀: insufficient evidence at 5% that the difference in means is not 5.",
        "Standard error √(3.1²/70 + 2.7²/80) = 0.47792. 1.4 ± 1.6449 × 0.47792 = 1.4 ± 0.78614, giving (0.614, 2.19) (3 s.f.). The interval lies entirely above 0, which suggests μ₁ > μ₂ (a two-tailed test at 10% would reject μ₁ = μ₂).",
        "(a) Yes: n = 16 is small, so X̄ is only known to be normal if the population is normal (it is given as normal). (b) No: n = 50 is large, so X̄ is approximately normal by the CLT and s estimates σ. (c) The populations are given as normal, so X̄<sub>A</sub> − X̄<sub>B</sub> is exactly normal; with samples of 36 and 40 the CLT would also make it approximately normal.",
        "Need (81.2 − 80)/(5/√n) > 1.6449, so √n > 1.6449 × 5/1.2 = 6.8538, n > 46.97. The least sample size is n = 47.",
        "1.35 ± 1.96 × 2.8/√40 = 1.35 ± 0.86773, giving (0.482, 2.22) seconds (3 s.f.). The number of pairs is large, so the CLT applies to d̄. The interval does not contain 0, so there is evidence (two-tailed 5% level) that times in shoe A are longer on average.",
    ],
    "exam": [
        "(Edexcel FS2, OCR A) The waiting times, x minutes, of a random sample of 45 customers at a café are summarised by Σx = 283.5 and Σx² = 1946.25. "
        "(a) Calculate unbiased estimates of the mean and the variance of the waiting times. [3] "
        "(b) The owner claims that the mean waiting time is 6 minutes. A customer believes it is longer. Test, at the 5% significance level, whether the mean waiting time is more than 6 minutes. [5] "
        "(c) Find a 95% confidence interval for the mean waiting time. [3] "
        "(d) Explain why it was not necessary to assume that waiting times are normally distributed. [2]",
        "(IAL S3, Edexcel FS2) The masses of apples from orchard A are normally distributed with standard deviation 18 g, and from orchard B with standard deviation 15 g. "
        "A random sample of 20 apples from A has mean mass 162.4 g and an independent random sample of 25 apples from B has mean mass 151.8 g. "
        "(a) Test, at the 1% significance level, whether apples from orchard A are heavier on average than apples from orchard B. [6] "
        "(b) State one assumption, other than normality, that you made in carrying out the test. [1] "
        "(c) In a second study, random samples of equal size n are taken from each orchard. Find the least value of n for which a difference in sample means of 8 g would be significant at the 1% level in the test in (a). [4]",
        "(CAIE 9231, Edexcel FS2) The commuting times, x minutes, of a random sample of 60 workers in city M and the times, y minutes, of an independent random sample of 75 workers in city N are summarised by: "
        "n = 60, Σx = 2052, Σx² = 74 610; n = 75, Σy = 2370, Σy² = 80 180. "
        "(a) Calculate unbiased estimates of the population means and variances. [3] "
        "(b) Test, at the 5% significance level, whether the mean commuting time in city M is greater than in city N. [5] "
        "(c) Find a 90% confidence interval for the difference between the population means. [3] "
        "(d) Explain why a normal distribution can be used for the test even though the distributions of commuting times are unknown. [2]",
        "(OCR A, OCR MEI) A manufacturer states that the mean lifetime of its phone battery, on a standard test, is 20 hours. Lifetimes are normally distributed with standard deviation 1.5 hours. "
        "A random sample of 12 batteries has mean lifetime 19.1 hours. "
        "(a) Test, at the 5% significance level, whether the mean lifetime differs from 20 hours. [5] "
        "(b) Calculate a 98% confidence interval for the mean lifetime. [3] "
        "(c) Explain why the fact that 20 lies inside the interval in (b) does not contradict your conclusion in (a). [2] "
        "(d) State what assumption about the standard deviation was made in your calculations. [1]",
    ],
    "exam_answers": [
        "(a) x̄ = 283.5/45 = 6.3 [B1]. s² = (1946.25 − 283.5²/45)/44 = 160.2/44 [M1] = 3.64 (3 s.f.) [A1]. "
        "(b) H₀: μ = 6, H₁: μ > 6, μ the population mean waiting time [B1]. z = (6.3 − 6)/(√3.6409/√45) [M1] = 0.3/0.28445 = 1.05 (3 s.f.) [A1]. "
        "Critical value 1.6449 (or p-value 0.146) [B1]. 1.05 < 1.6449: do not reject H₀; insufficient evidence at 5% that the mean waiting time is more than 6 minutes [A1]. "
        "(c) 6.3 ± 1.96 × 0.28445 [M1 B1] = (5.74, 6.86) minutes [A1]. "
        "(d) n = 45 is large, so by the CLT the sample mean is approximately normally distributed [B1], and s² is a good estimate of σ² [B1].",
        "(a) H₀: μ<sub>A</sub> = μ<sub>B</sub>, H₁: μ<sub>A</sub> > μ<sub>B</sub> [B1]. Under H₀, X̄<sub>A</sub> − X̄<sub>B</sub> ~ N(0, 18²/20 + 15²/25) [M1]. Standard error √(16.2 + 9) = 5.0200 [A1]. "
        "z = 10.6/5.0200 = 2.11 (3 s.f.) [A1]. Critical value 2.3263 [B1]. 2.11 < 2.3263: do not reject H₀. Insufficient evidence at 1% that apples from A are heavier on average [A1]. "
        "(b) The two samples are random and independent of each other [B1]. "
        "(c) Need 8/√(549/n) > 2.3263 [M1 B1]. √n > 2.3263√549/8 = 6.8134 [M1], n > 46.4, so n = 47 [A1].",
        "(a) x̄ = 34.2, sₓ² = (74 610 − 2052²/60)/59 = 75.1; ȳ = 31.6, s<sub>y</sub>² = (80 180 − 2370²/75)/74 = 71.5 (3 s.f.) [B1 M1 A1]. "
        "(b) H₀: μ<sub>M</sub> = μ<sub>N</sub>, H₁: μ<sub>M</sub> > μ<sub>N</sub> [B1]. Standard error √(75.112/60 + 71.459/75) = √2.2047 = 1.4848 [M1]. z = 2.6/1.4848 = 1.75 (3 s.f.) [A1]. "
        "1.75 > 1.6449 [B1]: reject H₀. Sufficient evidence at 5% that the mean commuting time in M is greater than in N [A1]. "
        "(c) 2.6 ± 1.6449 × 1.4848 [M1 B1] = (0.158, 5.04) minutes [A1]. "
        "(d) Both samples are large, so by the CLT the sample means (and their difference) are approximately normally distributed [B1], and the sample variances are good estimates of the population variances [B1].",
        "(a) H₀: μ = 20, H₁: μ ≠ 20 [B1]. z = (19.1 − 20)/(1.5/√12) [M1] = −0.9/0.43301 = −2.08 (3 s.f.) [A1]. "
        "Critical values ±1.96 (or p-value 0.0377 < 0.05) [B1]. Reject H₀: sufficient evidence at 5% that the mean lifetime differs from 20 hours [A1]. "
        "(b) 19.1 ± 2.3263 × 0.43301 [M1 B1] = (18.09, 20.11) hours (2 d.p.) [A1]. "
        "(c) A 98% interval matches a two-tailed test at the 2% level, not 5% [B1]; at the 2% level H₀ would not be rejected (|−2.08| < 2.3263), which is consistent [B1]. "
        "(d) The standard deviation of 1.5 hours is assumed to be correct (unchanged) for this sample of batteries [B1].",
    ],
}
