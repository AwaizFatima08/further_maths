UNIT = {
    "number": "A2.11",
    "title": "Variances: chi-squared intervals and the F-test",
    "tag": "A2 · Edexcel FS2 topic 6 (6.1, 6.2) only · not on AQA, OCR A, OCR MEI, IAL S3 or CAIE 9231 (useful background for pooled t-tests)",
    "notes": [
        ("p", "So far every test has been about a mean. Often the <b>spread</b> matters just as much: a machine filling bottles must "
              "be consistent as well as accurate, and a pooled t-test (Unit A2.10) needs two populations with equal variances. This unit "
              "covers inference about one variance, using the χ² distribution, and the comparison of two variances, using the F distribution. "
              "Both methods require the populations to be <b>normal</b>, and they are much more sensitive to this than the t-test."),

        ("h2", "11.1 The sampling distribution of S²"),
        ("box", "Key result (given in the Edexcel formula booklet; no proof required)", [
            "If X₁, ..., Xₙ is a random sample from N(μ, σ²) and S² = Σ(Xᵢ − X̄)²/(n − 1), then (n − 1)S²/σ² ~ χ²(n − 1).",
            "Equivalently Σ(Xᵢ − X̄)²/σ² ~ χ²ₙ₋₁. The degrees of freedom are n − 1 because one is used in estimating μ by x̄.",
        ]),
        ("p", "The χ² distribution with ν degrees of freedom (met in Units AS7 and AS8) takes only positive values. It has mean ν and "
              "variance 2ν, and is positively skewed, especially for small ν. Because (n − 1)S²/σ² has mean n − 1, E(S²) = σ², which "
              "confirms that S² is unbiased. Because the distribution is not symmetric, the two critical values in a two-tailed test "
              "or interval are not equally spaced around the centre."),
        ("p", "<b>Reading χ² tables.</b> Table 4 gives x with P(X > x) = p. The columns p = 0.10, 0.05, 0.025, 0.01, 0.005 give "
              "<b>upper</b> points; the columns p = 0.90, 0.95, 0.975, 0.99, 0.995 give <b>lower</b> points, since P(X > x) = 0.975 means "
              "P(X < x) = 0.025. For example, with ν = 9: the lower 2.5% point is 2.700 and the upper 2.5% point is 19.023."),

        ("h2", "11.2 Confidence intervals for σ² and σ"),
        ("p", "Let a and b be the lower and upper α/2 points of χ²(n − 1), so P(a < (n − 1)S²/σ² < b) = 1 − α. Rearranging the two "
              "inequalities for σ² (taking reciprocals reverses them) gives P((n − 1)S²/b < σ² < (n − 1)S²/a) = 1 − α."),
        ("box", "Confidence interval for a normal variance", [
            "100(1 − α)% interval for σ²:  ( (n − 1)s²/b ,  (n − 1)s²/a ), where P(χ²ₙ₋₁ < a) = α/2 and P(χ²ₙ₋₁ > b) = α/2.",
            "The larger χ² value gives the lower limit. (n − 1)s² = Σ(x − x̄)² = Sₓₓ.",
            "For σ, take the square roots of both limits. The interval is not symmetric about s² (or s).",
        ]),

        ("h2", "11.3 Hypothesis test for a variance"),
        ("bullets", [
            "1. H₀: σ² = σ₀² (equivalently σ = σ₀). H₁: σ² > σ₀² (more variable), σ² < σ₀² (less variable) or σ² ≠ σ₀².",
            "2. Under H₀, (n − 1)S²/σ₀² ~ χ²(n − 1). Calculate the test statistic (n − 1)s²/σ₀².",
            "3. Upper-tailed: reject H₀ if the statistic is greater than the upper α point. Lower-tailed: reject if it is less than the lower α point.",
            "4. Two-tailed at α: find both the lower α/2 point and the upper α/2 point; reject if the statistic is outside them.",
            "5. Assumption: the sample is random and the population is normal. Conclude in context about the variance or standard deviation.",
        ]),
        ("p", "As with means, a two-tailed test at α rejects H₀: σ² = σ₀² exactly when σ₀² lies outside the 100(1 − α)% interval for σ²."),

        ("h2", "11.4 The F distribution"),
        ("box", "The F distribution (given in the Edexcel booklet)", [
            "If independent random samples of sizes n₁ and n₂ are taken from N(μ₁, σ₁²) and N(μ₂, σ₂²), then (S₁²/σ₁²)/(S₂²/σ₂²) ~ F(n₁ − 1, n₂ − 1).",
            "The first parameter ν₁ = n₁ − 1 belongs to the numerator, the second ν₂ = n₂ − 1 to the denominator. Order matters: F(5, 8) ≠ F(8, 5).",
            "Under H₀: σ₁² = σ₂², the ratio simplifies to F = S₁²/S₂² ~ F(n₁ − 1, n₂ − 1).",
        ]),
        ("bullets", [
            "F takes positive values only, is positively skewed, and its values cluster around 1 when both variances are equal.",
            "<b>Reciprocal property:</b> if F ~ F(ν₁, ν₂), then 1/F ~ F(ν₂, ν₁), because swapping numerator and denominator swaps their roles.",
            "So lower points come from upper points: the lower α point of F(ν₁, ν₂) is 1/(upper α point of F(ν₂, ν₁)). For example the lower 5% point of F(5, 8) is 1/4.82 = 0.2075, where 4.82 is the upper 5% point of F(8, 5).",
            "Tables 5 and 6 give upper 5% and 1% points; ν₁ is across the top, ν₂ down the side. A calculator can give any point directly.",
        ]),

        ("h2", "11.5 The F-test for equality of two variances"),
        ("bullets", [
            "1. H₀: σ₁² = σ₂². H₁: σ₁² ≠ σ₂² (two-tailed) or σ₁² > σ₂² (one-tailed).",
            "2. <b>Put the larger sample variance on top</b>, so F = s<sub>larger</sub>²/s<sub>smaller</sub>² ≥ 1 and only the upper tail is needed. The degrees of freedom are (n − 1 for the top sample, n − 1 for the bottom sample).",
            "3. Two-tailed at α: compare F with the upper α/2 point. A 10% two-tailed test uses the 5% table; a 2% two-tailed test uses the 1% table. (Putting the larger variance on top has already looked after the lower tail.)",
            "4. One-tailed H₁: σ₁² > σ₂²: put s₁² on top and compare with the upper α point. If s₁² < s₂², the data cannot support H₁ and H₀ is not rejected without further work.",
            "5. Assumptions: both populations normal; the samples random and independent.",
        ]),
        ("table", ["Test", "Statistic", "Distribution under H₀", "Assumptions"], [
            ["One variance", "(n − 1)s²/σ₀²", "χ²(n − 1)", "normal population, random sample"],
            ["Interval for σ²", "(n − 1)s²/b to (n − 1)s²/a", "χ²(n − 1) points a, b", "normal population, random sample"],
            ["Two variances", "s₁²/s₂² (larger on top)", "F(n₁ − 1, n₂ − 1)", "both normal, independent random samples"],
        ]),

        ("h2", "11.6 Using the F-test before a pooled t-test"),
        ("p", "A pooled two-sample t-test (Unit A2.10) assumes σ₁² = σ₂². Edexcel questions often ask you first to test this with a "
              "two-tailed F-test, then to choose the test for the means. If H₀: σ₁² = σ₂² is not rejected, it is reasonable to pool; "
              "say so explicitly (\"the F-test gives no evidence that the variances differ, so a pooled estimate is justified\"). "
              "If H₀ is rejected, a pooled t-test is not appropriate. A non-significant F-test does not prove the variances are equal; "
              "it only shows the data are consistent with equal variances."),
        ("warn", "Common mistakes", [
            "Using s instead of s² in (n − 1)s²/σ₀² or in the F ratio.",
            "Using n instead of n − 1 for the degrees of freedom, or swapping ν₁ and ν₂ when reading the F table (ν₁ goes with the numerator).",
            "Putting the a and b values the wrong way round in the interval: the upper χ² point gives the lower limit for σ².",
            "In a two-tailed χ² test, using only one tail, or using the α point instead of the α/2 point in each tail.",
            "In a two-tailed F-test at 10%, comparing with the 10% point instead of the 5% point.",
            "Quoting the interval for σ² when the question asks for σ (take square roots), or saying the interval is \"s² ± ...\".",
            "Forgetting that these tests need normal populations. Unlike the t-test, they are not robust when the population is not normal.",
        ]),
    ],
    "examples": [
        {
            "title": "Reading χ² and F tables, and the reciprocal property",
            "question": "(a) For χ²(9), find the values a and b with P(χ² < a) = 0.025 and P(χ² > b) = 0.025. "
                        "(b) Find the upper 5% point of F(5, 8). (c) Find the lower 5% point of F(5, 8). "
                        "(d) Find the value f such that P(F < f) = 0.01 when F ~ F(6, 12).",
            "steps": [
                "(a) Lower point: column p = 0.975, ν = 9: a = 2.700. Upper point: column p = 0.025: b = 19.023.",
                "(b) Table 5, ν₁ = 5 (across), ν₂ = 8 (down): 3.69.",
                "(c) The lower 5% point of F(5, 8) is 1/(upper 5% point of F(8, 5)) = 1/4.82 = 0.2075 (4 s.f.).",
                "(d) P(F < f) = 0.01 is the lower 1% point: f = 1/(upper 1% point of F(12, 6)) = 1/7.72 = 0.130 (3 s.f.).",
            ],
        },
        {
            "title": "Confidence intervals for σ² and σ from raw data",
            "question": "The diameters, in mm, of a random sample of 10 washers are 12.1, 11.8, 12.4, 12.0, 11.6, 12.3, 12.2, 11.9, 12.5, 11.7. "
                        "Assuming diameters are normally distributed, find 95% confidence intervals for the variance and the standard deviation of the diameters.",
            "steps": [
                "Σx = 120.5, Σx² = 1452.85, so Sₓₓ = 1452.85 − 120.5²/10 = 0.825 and s² = 0.825/9 = 0.091667.",
                "(n − 1)S²/σ² ~ χ²(9). From the table: lower 2.5% point 2.700, upper 2.5% point 19.023.",
                "Interval for σ²: (0.825/19.023, 0.825/2.700) = (0.0434, 0.306) mm² (3 s.f.).",
                "Interval for σ: (√0.043369, √0.30556) = (0.208, 0.553) mm (3 s.f.).",
                "Note that s = 0.303 is not at the centre of the interval for σ, because the χ² distribution is skewed.",
            ],
        },
        {
            "title": "Upper-tailed test for a variance",
            "question": "A machine cuts pipes whose lengths should have standard deviation at most 0.5 mm. A random sample of 15 pipes gives "
                        "s = 0.68 mm. Assuming lengths are normally distributed, test at the 5% level whether the standard deviation is greater than 0.5 mm.",
            "steps": [
                "H₀: σ² = 0.25, H₁: σ² > 0.25, where σ is the population standard deviation of lengths in mm.",
                "Under H₀, 14S²/0.25 ~ χ²(14). Test statistic: 14 × 0.68²/0.25 = 14 × 0.4624/0.25 = 25.9 (3 s.f.).",
                "Upper 5% point of χ²(14) = 23.685. Since 25.9 > 23.685, reject H₀ (p-value 0.0267).",
                "There is sufficient evidence at the 5% level that the standard deviation of pipe lengths is greater than 0.5 mm, so the machine needs adjusting.",
            ],
        },
        {
            "title": "Lower-tailed test for a variance",
            "question": "The masses of tablets made by an old process have variance 7.5 mg². A new process is meant to reduce the variability. "
                        "A random sample of 21 tablets from the new process has s² = 4.2 mg². Test at the 5% level whether the variance has been reduced, assuming normality.",
            "steps": [
                "H₀: σ² = 7.5, H₁: σ² < 7.5, where σ² is the population variance of tablet masses from the new process.",
                "Under H₀, 20S²/7.5 ~ χ²(20). Test statistic: 20 × 4.2/7.5 = 11.2.",
                "Lower 5% point of χ²(20): column p = 0.95, giving 10.851. Since 11.2 > 10.851, the statistic is not in the critical region (p-value 0.0591).",
                "Do not reject H₀. There is insufficient evidence at the 5% level that the new process has reduced the variance of tablet masses.",
            ],
        },
        {
            "title": "Two-tailed F-test",
            "question": "Two methods of measuring blood alcohol are compared. Method A gives n₁ = 7 readings with s₁² = 8.4 and method B gives "
                        "n₂ = 11 readings with s₂² = 2.9 (both in suitable units, on independent samples). Assuming normal distributions, test at the 10% level whether the methods differ in variability.",
            "steps": [
                "H₀: σ<sub>A</sub>² = σ<sub>B</sub>², H₁: σ<sub>A</sub>² ≠ σ<sub>B</sub>².",
                "Larger variance on top: F = 8.4/2.9 = 2.90 (3 s.f.), with ν₁ = 6, ν₂ = 10. Under H₀, F ~ F(6, 10).",
                "Two-tailed at 10%, so use the upper 5% point: F₀.₀₅(6, 10) = 3.22.",
                "2.90 < 3.22, so do not reject H₀ (p-value 0.133). There is insufficient evidence at the 10% level that the two methods differ in variability.",
            ],
        },
        {
            "title": "Exam standard: F-test, then a pooled t-test",
            "question": "Independent random samples of plants grown with feeds P and Q give heights (cm): feed P: n = 9, x̄ = 27.2, s² = 5.6; "
                        "feed Q: n = 13, x̄ = 24.9, s² = 3.1. Heights are normally distributed. (a) Test at the 10% level whether the population "
                        "variances are equal. (b) Hence carry out a suitable test, at the 5% level, of whether the mean heights differ.",
            "steps": [
                "(a) H₀: σ<sub>P</sub>² = σ<sub>Q</sub>², H₁: σ<sub>P</sub>² ≠ σ<sub>Q</sub>². F = 5.6/3.1 = 1.81 (3 s.f.) with (8, 12) degrees of freedom.",
                "Upper 5% point F(8, 12) = 2.85. 1.81 < 2.85, so do not reject H₀: no evidence that the variances differ, so pooling is justified.",
                "(b) s<sub>p</sub>² = (8 × 5.6 + 12 × 3.1)/20 = 82/20 = 4.1. Standard error √(4.1 × (1/9 + 1/13)) = 0.87803.",
                "H₀: μ<sub>P</sub> = μ<sub>Q</sub>, H₁: μ<sub>P</sub> ≠ μ<sub>Q</sub>. Under H₀, T ~ t(20). t = (27.2 − 24.9)/0.87803 = 2.62 (3 s.f.).",
                "Critical values ±2.086. 2.62 > 2.086, so reject H₀ (p-value 0.0164).",
                "There is sufficient evidence at the 5% level that the mean heights of plants grown with feeds P and Q are different.",
            ],
        },
    ],
    "practice": [
        "Use Table 4 to find: (a) the upper 5% point and the lower 5% point of χ²(12); (b) x such that P(χ² < x) = 0.01 when ν = 24.",
        "State the mean and variance of χ²(8), and explain why a 95% confidence interval for σ² is not symmetric about s².",
        "A random sample of 16 observations from a normal population has s² = 12.5. Find a 90% confidence interval for σ².",
        "A random sample of 25 observations from a normal population has s = 3.4. Find a 99% confidence interval for σ.",
        "The variance of the thickness of a coating should be 0.02 mm². A random sample of 11 items gives s² = 0.0413 mm². Assuming normality, test at the 5% level whether the variance differs from 0.02 mm².",
        "The times, in seconds, taken by 8 randomly chosen swimmers are 24.3, 21.8, 26.1, 23.4, 22.0, 25.7, 24.9, 21.6. Assuming normality, test at the 5% level whether the standard deviation is greater than 1.5 seconds.",
        "Use Tables 5 and 6 to find: (a) the upper 5% point of F(4, 10); (b) the upper 1% point of F(10, 4); (c) the lower 5% point of F(6, 12).",
        "Explain why, if F ~ F(ν₁, ν₂), then 1/F ~ F(ν₂, ν₁). Hence find the lower 1% point of F(8, 10).",
        "Machine A gives n = 13 items with s² = 0.84 and machine B gives n = 9 items with s² = 0.31. Assuming normality and independent samples, test at the 5% level whether machine A is more variable than machine B.",
        "Independent random samples from normal populations give n₁ = 6, s₁ = 4.8 and n₂ = 25, s₂ = 1.9. Test at the 2% level whether the population variances are equal.",
        "Explain why an F-test is often carried out before a two-sample t-test, and state the assumptions that the F-test itself requires.",
        "A researcher wants to test H₁: σ₁² > σ₂² and finds s₁² = 2.3 (n₁ = 10) and s₂² = 3.0 (n₂ = 12). Explain why no calculation is needed to reach a conclusion, and state it.",
    ],
    "answers": [
        "(a) Upper 5%: 21.026; lower 5% (column 0.95): 5.226. (b) Column 0.99, ν = 24: 10.856.",
        "Mean 8, variance 16. The χ² distribution is positively skewed, so the distances from s² to the two limits (n − 1)s²/b and (n − 1)s²/a are different; the upper limit is further from s².",
        "χ²(15) points: lower 5% 7.261, upper 5% 24.996. (15 × 12.5/24.996, 15 × 12.5/7.261) = (7.50, 25.8) (3 s.f.).",
        "χ²(24) points: lower 0.5% 9.886, upper 0.5% 45.559. σ²: (24 × 11.56/45.559, 24 × 11.56/9.886) = (6.0897, 28.064). σ: (2.47, 5.30) (3 s.f.).",
        "H₀: σ² = 0.02, H₁: σ² ≠ 0.02. Statistic 10 × 0.0413/0.02 = 20.65. χ²(10): lower 2.5% 3.247, upper 2.5% 20.483. 20.65 > 20.483, so reject H₀: sufficient evidence at 5% that the variance differs from 0.02 mm² (it appears larger).",
        "x̄ = 23.725, s² = 3.2221. H₀: σ = 1.5, H₁: σ > 1.5. Statistic 7 × 3.2221/2.25 = 10.0 (3 s.f.). Upper 5% point χ²(7) = 14.067. Do not reject H₀: insufficient evidence at 5% that the standard deviation is greater than 1.5 s.",
        "(a) 3.48. (b) 14.55. (c) 1/(upper 5% point of F(12, 6)) = 1/4.00 = 0.25.",
        "F = (S₁²/σ₁²)/(S₂²/σ₂²) with ν₁ = n₁ − 1 on top and ν₂ = n₂ − 1 below; 1/F is the same kind of ratio with the samples swapped, so it is F(ν₂, ν₁). Lower 1% point of F(8, 10) = 1/(upper 1% point of F(10, 8)) = 1/5.81 = 0.172 (3 s.f.).",
        "H₀: σ<sub>A</sub>² = σ<sub>B</sub>², H₁: σ<sub>A</sub>² > σ<sub>B</sub>². F = 0.84/0.31 = 2.71 (3 s.f.), ν₁ = 12, ν₂ = 8. Upper 5% point F(12, 8) = 3.28. 2.71 < 3.28, so do not reject H₀: insufficient evidence at 5% that machine A is more variable.",
        "H₀: σ₁² = σ₂², H₁: σ₁² ≠ σ₂². F = 4.8²/1.9² = 6.38 (3 s.f.), ν₁ = 5, ν₂ = 24. Two-tailed 2%: upper 1% point F(5, 24) = 3.90. 6.38 > 3.90, so reject H₀: sufficient evidence at 2% that the variances differ.",
        "A pooled t-test assumes the two population variances are equal; the F-test checks whether the data are consistent with this. The F-test requires both populations to be normal and the samples to be random and independent.",
        "H₁ claims σ₁² > σ₂², but the sample variance s₁² is smaller than s₂², so F = s₁²/s₂² < 1 and the data cannot be in the upper critical region. Do not reject H₀: there is no evidence that σ₁² > σ₂².",
    ],
    "exam": [
        "(Edexcel FS2) The thicknesses, in mm, of a random sample of 10 sheets of glass from a production line are: 2.41, 2.86, 2.53, 2.17, 2.74, 2.95, 2.38, 2.62, 2.80, 2.24. "
        "The thicknesses are normally distributed. "
        "(a) Calculate unbiased estimates of the mean and variance of the thicknesses. [2] "
        "(b) Find a 95% confidence interval for the standard deviation of the thicknesses. [4] "
        "(c) The specification requires the variance to be at most 0.04 mm². Test, at the 5% significance level, whether the variance is greater than 0.04 mm². [4] "
        "(d) Explain why the test in (c) would be unreliable if the thicknesses were not normally distributed. [1]",
        "(Edexcel FS2) Two fertilisers are tested on tomato plants. The yields, x kg, of 9 plants given fertiliser A and the yields, y kg, of 11 plants given fertiliser B are summarised by: "
        "Σx = 231.3, Σx² = 5976.41; Σy = 261.8, Σy² = 6255.84. Yields are normally distributed and the samples are independent. "
        "(a) Show that unbiased estimates of the variances are 4.0 and 2.5. [2] "
        "(b) Test, at the 10% significance level, whether the variances of the yields are equal. [4] "
        "(c) Hence, explaining your choice, test at the 5% significance level whether fertiliser A gives a higher mean yield than fertiliser B. [7]",
        "(Edexcel FS2) Independent random samples of sizes 6 and 9 are taken from normal populations. The unbiased estimates of the variances are s₁² = 1.2 and s₂² = 3.9. "
        "(a) A student calculates F = s₁²/s₂². Find both critical values for a two-tailed test of H₀: σ₁² = σ₂² at the 10% level using F(5, 8), and state the conclusion. [4] "
        "(b) Show that putting the larger variance on top leads to the same conclusion. [2] "
        "(c) Find a 90% confidence interval for σ₂. [3] "
        "(d) Test, at the 5% level, whether σ₁² is less than 3. [3]",
    ],
    "exam_answers": [
        "(a) x̄ = 25.7/10 = 2.57 mm [B1]. Sₓₓ = 66.694 − 25.7²/10 = 0.645, s² = 0.0717 (3 s.f.) [B1]. "
        "(b) 9S²/σ² ~ χ²(9) [M1]; points 2.700 and 19.023 [B1]. σ²: (0.645/19.023, 0.645/2.700) = (0.033906, 0.23889) [M1]. "
        "σ: (0.184, 0.489) mm (3 s.f.) [A1]. "
        "(c) H₀: σ² = 0.04, H₁: σ² > 0.04 [B1]. Statistic 9 × 0.071667/0.04 = 16.1 (3 s.f.) [M1 A1]. "
        "Upper 5% point χ²(9) = 16.919; 16.1 < 16.919, so do not reject H₀: insufficient evidence at 5% that the variance exceeds 0.04 mm² [A1]. "
        "(d) The result (n − 1)S²/σ² ~ χ²(n − 1) holds only for a normal population, and the test is not robust to non-normality [B1].",
        "(a) sₓ² = (5976.41 − 231.3²/9)/8 = 32/8 = 4.0 [B1]; s<sub>y</sub>² = (6255.84 − 261.8²/11)/10 = 25/10 = 2.5 [B1]. "
        "(b) H₀: σ<sub>A</sub>² = σ<sub>B</sub>², H₁: σ<sub>A</sub>² ≠ σ<sub>B</sub>² [B1]. F = 4.0/2.5 = 1.6 [M1]. Upper 5% point F(8, 10) = 3.07 [B1]. "
        "1.6 < 3.07, so do not reject H₀: no evidence that the variances differ [A1]. "
        "(c) The populations are normal and the F-test supports equal variances, so a pooled two-sample t-test is used [B1]. "
        "H₀: μ<sub>A</sub> = μ<sub>B</sub>, H₁: μ<sub>A</sub> > μ<sub>B</sub> [B1]. x̄ = 25.7, ȳ = 23.8 [B1]. s<sub>p</sub>² = (32 + 25)/18 = 3.1667 [M1]. "
        "t = 1.9/√(3.1667 × (1/9 + 1/11)) = 1.9/0.79983 = 2.38 (3 s.f.) [M1 A1]. Upper 5% point t(18) = 1.734; 2.38 > 1.734, so reject H₀: "
        "sufficient evidence at 5% that fertiliser A gives a higher mean yield [A1].",
        "(a) F = 1.2/3.9 = 0.308 (3 s.f.) [B1]. Upper 5% point of F(5, 8) = 3.69 [B1]; lower 5% point = 1/F₀.₀₅(8, 5) = 1/4.82 = 0.2075 [M1]. "
        "0.2075 < 0.308 < 3.69, so do not reject H₀: insufficient evidence at 10% that the variances differ [A1]. "
        "(b) F = 3.9/1.2 = 3.25 with (8, 5) degrees of freedom [M1]; upper 5% point 4.82; 3.25 < 4.82, so again do not reject H₀ [A1]. "
        "(c) 8S₂²/σ₂² ~ χ²(8): points 2.733 and 15.507 [B1]. σ₂²: (31.2/15.507, 31.2/2.733) = (2.0120, 11.416) [M1]. σ₂: (1.42, 3.38) (3 s.f.) [A1]. "
        "(d) H₀: σ₁² = 3, H₁: σ₁² < 3. Statistic 5 × 1.2/3 = 2.0 [M1]. Lower 5% point of χ²(5) = 1.145 [B1]. "
        "2.0 > 1.145, so do not reject H₀: insufficient evidence at 5% that σ₁² is less than 3 [A1].",
    ],
}
