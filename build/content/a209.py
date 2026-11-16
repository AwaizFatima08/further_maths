UNIT = {
    "number": "A2.9",
    "title": "The t distribution: one-sample tests and intervals",
    "tag": "A2 · Edexcel FS2, AQA (SG1, SH4), OCR MEI (SI9, SH6), CAIE 9231 P4 · not on OCR A or IAL S3",
    "notes": [
        ("p", "In Unit A2.8 every test used the normal distribution, because either σ was known or the sample was large enough for s "
              "to be a reliable estimate of σ. Often neither is true: we have a <b>small sample</b> from a normal population and must "
              "estimate σ from the same data. The extra uncertainty in s changes the distribution of the test statistic from N(0, 1) "
              "to Student's t distribution. This unit covers the t distribution and its use for one mean; Unit A2.10 extends it to "
              "two means."),

        ("h2", "9.1 Why a new distribution is needed"),
        ("p", "If X ~ N(μ, σ²), then (X̄ − μ)/(σ/√n) ~ N(0, 1) exactly. When σ is replaced by the sample standard deviation S, the "
              "denominator S/√n also varies from sample to sample. When S happens to be small the ratio becomes large, so extreme values "
              "are more likely than in N(0, 1). W. S. Gosset, who published under the name \"Student\" in 1908, found the exact "
              "distribution of this ratio."),
        ("box", "The t statistic (all four boards)", [
            "If X₁, ..., Xₙ is a random sample from N(μ, σ²), then T = (X̄ − μ)/(S/√n) has the t distribution with ν = n − 1 degrees of freedom, written T ~ t(n − 1) or tₙ₋₁.",
            "S² = Σ(Xᵢ − X̄)²/(n − 1) is the unbiased estimator of σ².",
            "The result is exact only if the population is normal. No proof is required by any board.",
        ]),

        ("h2", "9.2 Properties of the t distribution and degrees of freedom"),
        ("bullets", [
            "It is a continuous distribution, symmetric about 0 and bell-shaped, so its mean (for ν > 1), median and mode are 0.",
            "It has heavier tails than N(0, 1): more of its probability lies far from 0, so its critical values are larger than z values.",
            "Its shape depends on one parameter, the degrees of freedom ν. As ν increases, t(ν) gets closer to N(0, 1); t(∞) is N(0, 1).",
            "Its variance is ν/(ν − 2) for ν > 2, which is greater than 1 and tends to 1 as ν grows (for interest; not examined).",
        ]),
        ("p", "<b>Degrees of freedom.</b> The deviations x₁ − x̄, ..., xₙ − x̄ always add up to 0, so once n − 1 of them are known the "
              "last is fixed. Only n − 1 pieces of information about spread are free to vary, which is why s² divides by n − 1 and why "
              "the t statistic has n − 1 degrees of freedom. Each estimated mean used in calculating s² costs one degree of freedom."),
        ("table", ["ν", "5", "10", "20", "30", "60", "∞ (normal)"], [
            ["Two-tailed 5% (upper 2.5%) point", "2.571", "2.228", "2.086", "2.042", "2.000", "1.960"],
            ["One-tailed 5% (upper 5%) point", "2.015", "1.812", "1.725", "1.697", "1.671", "1.645"],
        ]),

        ("h2", "9.3 Reading t tables"),
        ("p", "The table in this book (Table 3) gives t such that P(T > t) = p, the <b>upper-tail</b> probability, for p = 0.10, 0.05, "
              "0.025, 0.01, 0.005 and 0.0005. Because t is symmetric, P(T < −t) = p as well."),
        ("bullets", [
            "One-tailed test at α: use the column p = α. For H₁: μ < μ₀ the critical value is negative.",
            "Two-tailed test at α, or a 100(1 − α)% confidence interval: use p = α/2. For 95%, p = 0.025; for 99%, p = 0.005; for 90%, p = 0.05.",
            "Board tables differ in layout. Edexcel gives upper-tail p. CAIE (MF19) gives P(T ≤ t) = p, so the 95% two-sided point is in the 0.975 column. MEI gives two-tailed percentages. Check the heading before reading off a value.",
            "If ν is not in the table (e.g. ν = 45), use a calculator (inverse t) or the nearest smaller ν in the table, which gives a slightly cautious value.",
        ]),

        ("h2", "9.4 Finding x̄ and s from raw or summary data"),
        ("box", "Sample statistics (all boards)", [
            "x̄ = Σx/n,   Sₓₓ = Σ(x − x̄)² = Σx² − (Σx)²/n,   s² = Sₓₓ/(n − 1).",
            "If a calculator or question gives the variance with divisor n (σₙ², \"the sample variance\" in some books), convert: s² = n/(n − 1) × σₙ².",
            "Coded data y = x − a: ȳ = Σy/n and x̄ = ȳ + a; the variance is unchanged by coding, so s is the same for x and y.",
        ]),

        ("h2", "9.5 The one-sample t-test"),
        ("bullets", [
            "1. Define μ in context, and state H₀: μ = μ₀ and H₁ (μ > μ₀, μ < μ₀ or μ ≠ μ₀).",
            "2. State the assumption: the sample is random and comes from a normal population (variance unknown).",
            "3. Under H₀, T = (X̄ − μ₀)/(S/√n) ~ t(n − 1). Calculate t = (x̄ − μ₀)/(s/√n).",
            "4. Find the critical value from t(n − 1) at the right tail probability, or find the p-value on a calculator.",
            "5. Decide and conclude in context without certainty.",
        ]),
        ("p", "Calculator: the \"1-sample t test\" mode gives t and the p-value from raw data or from x̄, s and n. "
              "Show the formula and the substituted values in an exam; a bare calculator answer can lose method marks."),

        ("h2", "9.6 The t confidence interval for μ"),
        ("box", "Confidence interval for a mean, σ unknown, normal population", [
            "100(1 − α)% interval:  x̄ ± t × s/√n,  where P(T > t) = α/2 and T ~ t(n − 1).",
            "Example: n = 10, 95%: t = 2.262 (ν = 9). n = 10, 99%: t = 3.250.",
            "AQA SH4 and MEI SI9 ask only for symmetric two-sided intervals; one-sided intervals are not set.",
        ]),
        ("p", "The interpretation and the link with tests are the same as in Unit A2.8: about 95% of such intervals contain μ, and a "
              "two-tailed test at 5% rejects H₀: μ = μ₀ exactly when μ₀ is outside the 95% interval. If an interval (a, b) is given, "
              "the sample mean is the midpoint (a + b)/2, and the half-width (b − a)/2 = t × s/√n can be solved for s."),

        ("h2", "9.7 When to use t and when to use z"),
        ("table", ["Population", "σ", "Sample size", "Use"], [
            ["Normal", "known", "any", "z: N(0, 1) exactly"],
            ["Normal", "unknown", "small", "t(n − 1)"],
            ["Normal", "unknown", "large", "t(n − 1), or z as a good approximation (CLT, s ≈ σ)"],
            ["Not normal or unknown", "known or unknown", "large", "z, approximately, by the CLT"],
            ["Not normal or unknown", "unknown", "small", "neither: use a non-parametric test (Units A2.12 and A2.13)"],
        ]),
        ("p", "For large ν the t and z critical values are very close (t = 2.000 at ν = 60 against z = 1.960), so for large samples "
              "the choice hardly matters. For small samples it matters a lot: with n = 6 the 95% point is 2.571, not 1.96, so a z interval "
              "would be about 24% too narrow and a z test would reject H₀ far too often."),
        ("p", "<b>Checking normality.</b> The t procedures assume the population is normal. With a small sample you cannot prove this, "
              "but a dot plot or stem-and-leaf diagram that is roughly symmetric with no outliers makes it reasonable. MEI students may "
              "also be shown a Normal probability plot: points close to a straight line support normality. The t-test is fairly robust "
              "to mild skewness, but outliers in a small sample can change x̄ and s a great deal."),
        ("warn", "Common mistakes", [
            "Using z (1.645, 1.96) for a small sample with σ unknown. Examiners (CAIE 2023) report this every year, along with using the wrong row of the t table.",
            "Using ν = n instead of ν = n − 1.",
            "Using the one-tailed column for a two-tailed test or a confidence interval (for 95% use p = 0.025, not 0.05).",
            "Calculating s with divisor n. Check that your calculator value is sₓ (σₙ₋₁).",
            "Forgetting to state that the population is assumed normal, or saying the sample must be normal.",
            "Forgetting to undo coding for the mean, or wrongly \"undoing\" it for the standard deviation.",
        ]),
    ],
    "examples": [
        {
            "title": "Reading the t table and comparing with z",
            "question": "T has a t distribution. Find: (a) t such that P(T > t) = 0.05 when ν = 9; (b) t such that P(−t < T < t) = 0.95 "
                        "when ν = 15; (c) t such that P(T < t) = 0.01 when ν = 20. (d) Compare the 95% two-sided points for ν = 5, 10, 20, 30 with z.",
            "steps": [
                "(a) Upper-tail p = 0.05, ν = 9: t = 1.833.",
                "(b) 0.95 in the middle leaves 0.025 in each tail. Upper-tail p = 0.025, ν = 15: t = 2.131.",
                "(c) P(T < t) = 0.01 is a lower tail, so t is negative. By symmetry t = −(upper 1% point for ν = 20) = −2.528.",
                "(d) The points are 2.571, 2.228, 2.086 and 2.042 for ν = 5, 10, 20 and 30, compared with 1.960 for N(0, 1).",
                "They decrease towards 1.960 as ν increases, because s becomes a more reliable estimate of σ and the heavier tails of t become less pronounced.",
            ],
        },
        {
            "title": "One-sample t-test from raw data",
            "question": "Chocolate bars are labelled 50 g. A trading-standards officer weighs a random sample of 8 bars: "
                        "49.2, 50.1, 48.7, 49.5, 49.9, 48.8, 49.6, 50.0 (grams). Assuming the masses are normally distributed, test at "
                        "the 5% significance level whether the mean mass is less than 50 g.",
            "steps": [
                "Σx = 395.8, Σx² = 19 584.2, so x̄ = 49.475 and s² = (19 584.2 − 395.8²/8)/7 = 0.285, s = 0.53385.",
                "Let μ be the population mean mass in grams. H₀: μ = 50, H₁: μ < 50 (one-tailed, 5%).",
                "The population is normal and σ is unknown with a small sample, so under H₀, T = (X̄ − 50)/(S/√8) ~ t(7).",
                "t = (49.475 − 50)/(0.53385/√8) = −0.525/0.18875 = −2.78 (3 s.f.).",
                "Critical value: P(T < −t) = 0.05 with ν = 7 gives −1.895. Since −2.78 < −1.895, reject H₀ (p-value 0.0136).",
                "There is sufficient evidence at the 5% level that the mean mass of the bars is less than 50 g.",
            ],
        },
        {
            "title": "A t confidence interval from summary data",
            "question": "The lengths, x cm, of a random sample of 12 leaves from a tree give Σx = 186.0 and Σx² = 2898.5. Assuming "
                        "lengths are normally distributed, find a 99% confidence interval for the mean length.",
            "steps": [
                "x̄ = 186.0/12 = 15.5. s² = (2898.5 − 186.0²/12)/11 = (2898.5 − 2883)/11 = 1.4091, so s = 1.1871.",
                "σ is unknown and n is small, so use t with ν = 11. For 99%, P(T > t) = 0.005: t = 3.106.",
                "Standard error s/√12 = 0.34267. Half-width 3.106 × 0.34267 = 1.0643.",
                "The 99% confidence interval is 15.5 ± 1.0643 = (14.44, 16.56) cm (2 d.p.).",
            ],
        },
        {
            "title": "Working back from a given interval (CAIE style)",
            "question": "A 95% confidence interval for the mean μ of a normal population, based on a random sample of size 10 and "
                        "using a t distribution, is (14.2, 16.6). Find the sample mean and the unbiased estimate s of the standard "
                        "deviation, and hence a 90% confidence interval for μ.",
            "steps": [
                "x̄ is the midpoint: (14.2 + 16.6)/2 = 15.4. The half-width is 1.2.",
                "ν = 9 and 95% gives t = 2.262. So 2.262 × s/√10 = 1.2 and s = 1.2√10/2.262 = 1.68 (3 s.f.).",
                "For 90%, P(T > t) = 0.05 with ν = 9: t = 1.833. Half-width 1.833 × 1.6776/√10 = 0.97241.",
                "The 90% interval is 15.4 ± 0.97241 = (14.43, 16.37) (2 d.p.). It is narrower, as a lower confidence level should give.",
            ],
        },
        {
            "title": "Exam standard: coded data, and the cost of using z by mistake",
            "question": "A psychologist claims that the mean reaction time to a signal is 100 milliseconds. The reaction times, x ms, of a "
                        "random sample of 14 adults are summarised by Σ(x − 100) = 31.5 and Σ(x − 100)² = 182.25. Reaction times are "
                        "assumed to be normally distributed. (a) Test the claim at the 1% significance level. (b) A student used z = 2.5758 "
                        "as the critical value. Explain why this is wrong and how it changes the conclusion. (c) Find the set of values of "
                        "μ₀ for which H₀: μ = μ₀ would not be rejected by a two-tailed test at the 1% level.",
            "steps": [
                "(a) Let y = x − 100. ȳ = 31.5/14 = 2.25, so x̄ = 102.25. s² = (182.25 − 31.5²/14)/13 = 111.375/13 = 8.5673, s = 2.9270.",
                "Let μ be the population mean reaction time in ms. H₀: μ = 100, H₁: μ ≠ 100 (two-tailed, 1%).",
                "Under H₀, T = (X̄ − 100)/(S/√14) ~ t(13). t = 2.25/(2.9270/√14) = 2.25/0.78227 = 2.88 (3 s.f.).",
                "Critical values: upper 0.5% point of t(13) is 3.012. Since |2.88| < 3.012, do not reject H₀ (p-value 0.0130).",
                "There is insufficient evidence at the 1% level to doubt the claim that the mean reaction time is 100 ms.",
                "(b) σ is unknown and the sample is small, so the statistic has a t(13) distribution, not N(0, 1). Using 2.5758 < 2.88 would wrongly reject H₀: the z critical value is too small because it ignores the extra uncertainty in s.",
                "(c) These are the values inside the 99% t interval: 102.25 ± 3.012 × 0.78227 = 102.25 ± 2.3562, i.e. 99.89 < μ₀ < 104.61 (2 d.p.). 100 lies inside, agreeing with (a).",
            ],
        },
    ],
    "practice": [
        "T has a t distribution. Find t when: (a) P(T > t) = 0.025 and ν = 7; (b) P(T < t) = 0.01 and ν = 18; (c) P(|T| > t) = 0.10 and ν = 24.",
        "Describe two similarities and two differences between the t distribution with 4 degrees of freedom and the standard normal distribution. Explain why the critical values of t are larger.",
        "A random sample of 6 measurements from a normal population is 12.4, 11.8, 13.1, 12.9, 12.2, 12.6. Find x̄ and s, and a 95% confidence interval for the population mean.",
        "The times, x seconds, taken by a random sample of 10 children to complete a task give Σx = 84.0 and Σx² = 712.6. Assuming a normal distribution, test at the 5% level whether the mean time is more than 8 seconds.",
        "A calculator gives the mean and standard deviation of a random sample of 9 values as 30.4 and σₙ = 2.1 (divisor n). Find s, and a 95% confidence interval for the population mean, assuming a normal population.",
        "A random sample of 16 values from a normal population has mean 72.6 and s = 4.8. Test H₀: μ = 75 against H₁: μ ≠ 75 at the 5% level.",
        "A 95% t confidence interval for μ, from a random sample of size 8 from a normal population, is (3.42, 4.58). Find the sample mean and s.",
        "State which distribution should be used for a test about μ in each case, giving a reason: (a) n = 12 from a normal population with known σ; (b) n = 12 from a normal population with unknown σ; (c) n = 200 from a population of unknown shape; (d) n = 10 from a population known to be strongly skewed.",
        "A one-tailed test (H₁: μ > μ₀) gives t = 2.21 with ν = 9. Using tables, state the conclusion at the 5% and at the 2.5% levels. A calculator gives the p-value; what is it, to 4 decimal places?",
        "Two 95% t intervals are calculated from samples with the same value of s, one with n = 9 and one with n = 31. Find the ratio (width with n = 9)/(width with n = 31), and explain the two reasons why the first is wider.",
        "(AQA) A random sample of 15 measurements from a normal population has mean 2.84 and s = 0.35. Construct a 90% confidence interval for the population mean.",
        "The yields, in kg, of 7 randomly chosen plants of a new variety are 5.8, 6.4, 6.1, 7.0, 6.6, 6.3, 6.9. Assuming a normal population, test at the 1% level whether the mean yield is greater than 6 kg.",
    ],
    "answers": [
        "(a) 2.365. (b) −2.552. (c) 1.711 (0.05 in each tail).",
        "Similarities: both are symmetric about 0 and bell-shaped (both have mean 0, and are continuous). Differences: t(4) has heavier tails and a lower peak, and its variance (2) is larger than 1. Because s is estimated from the sample, extreme values of t are more likely, so a larger value is needed to cut off the same tail probability.",
        "x̄ = 12.5, s = 0.473 (3 s.f.). ν = 5, t = 2.571. 12.5 ± 2.571 × 0.47329/√6 = 12.5 ± 0.49676, giving (12.00, 13.00) (2 d.p.).",
        "x̄ = 8.4, s² = (712.6 − 84²/10)/9 = 0.77778, s = 0.88192. H₀: μ = 8, H₁: μ > 8. t = 0.4/(0.88192/√10) = 1.43 (3 s.f.). Critical value t(9) = 1.833. 1.43 < 1.833, so do not reject H₀: insufficient evidence at 5% that the mean time is more than 8 seconds.",
        "s = 2.1 × √(9/8) = 2.23 (3 s.f.). ν = 8, t = 2.306. 30.4 ± 2.306 × 2.2274/3 = 30.4 ± 1.7121, giving (28.69, 32.11) (2 d.p.).",
        "t = (72.6 − 75)/(4.8/4) = −2.00. Critical values ±2.131 (ν = 15). |−2.00| < 2.131, so do not reject H₀: insufficient evidence at 5% that μ differs from 75.",
        "x̄ = 4.00. Half-width 0.58 = 2.365 × s/√8, so s = 0.58√8/2.365 = 0.694 (3 s.f.).",
        "(a) z: population normal and σ known. (b) t(11): normal population, σ unknown, small sample. (c) z (approximately): large sample, so by the CLT X̄ is approximately normal and s ≈ σ. (d) Neither: the sample is small and the population is not normal, so a non-parametric test (e.g. a sign test or Wilcoxon test) is needed.",
        "Upper 5% point 1.833 < 2.21 < 2.262 (upper 2.5% point). Reject H₀ at 5%; do not reject at 2.5%. p-value = P(T > 2.21) = 0.0272.",
        "Ratio = (2.306/√9)/(2.042/√31) = 2.10 (3 s.f.). The first is wider because its t value is larger (fewer degrees of freedom) and because its standard error s/√n is larger (smaller n).",
        "ν = 14, t = 1.761. 2.84 ± 1.761 × 0.35/√15 = 2.84 ± 0.15914, giving (2.68, 3.00) (2 d.p.).",
        "x̄ = 6.4429, s = 0.42762. H₀: μ = 6, H₁: μ > 6. t = 0.44286/(0.42762/√7) = 2.74 (3 s.f.). Critical value t(6) = 3.143. 2.74 < 3.143, so do not reject H₀: insufficient evidence at 1% that the mean yield is greater than 6 kg (p-value 0.0169, so it would be significant at 5%).",
    ],
    "exam": [
        "(AQA, Edexcel FS2) The volumes, in ml, of a random sample of 10 cans of drink are: 328.4, 331.2, 327.9, 329.5, 330.1, 326.8, 329.0, 328.2, 330.6, 327.5. "
        "The volumes are normally distributed. "
        "(a) Find the mean and an unbiased estimate of the variance of the volumes. [2] "
        "(b) The cans are labelled 330 ml. Test, at the 5% significance level, whether the mean volume is less than 330 ml. [5] "
        "(c) Construct a 99% confidence interval for the mean volume. [3] "
        "(d) Explain why the interval in (c) contains 330 even though H₀ was rejected in (b). [2]",
        "(CAIE 9231) A 95% confidence interval for the mean, μ, of a normal population, calculated from a random sample of 12 observations using a t distribution, is (41.36, 46.84). "
        "(a) Find the sample mean and the unbiased estimate of the population variance. [4] "
        "(b) Find a 90% confidence interval for μ. [2] "
        "(c) Hence, without calculating a test statistic, state the conclusion of a test of H₀: μ = 46 against H₁: μ ≠ 46 at the 10% significance level. Give a reason. [2] "
        "(d) State the assumption needed about the sample for the interval to be valid. [1]",
        "(OCR MEI) A researcher records the heart rates of a random sample of 11 athletes and tests whether the population mean differs from 15 beats per 15 seconds. "
        "Software output: One-sample t test; null mean 15.0; n 11; mean 16.12; SD 1.75; SE mean 0.52764; t 2.1226; df 10; p (two-tailed) 0.0598. "
        "(a) State the null and alternative hypotheses being tested. [1] "
        "(b) Show how the values of SE mean and t were calculated. [2] "
        "(c) State the conclusion of the test at the 5% level. [2] "
        "(d) Another researcher believed beforehand that athletes' mean rate is higher than 15. State the p-value for her one-tailed test and her conclusion at the 5% level. [2] "
        "(e) Calculate a 95% confidence interval for the population mean. [3] "
        "(f) State the distributional assumption needed, and how it could be checked. [2]",
        "(Edexcel FS2) The time, x minutes, that a random sample of 9 customers wait for a tram is recorded. The results are summarised by Σ(x − 20) = 13.5 and Σ(x − 20)² = 58.77. "
        "Waiting times are assumed to be normally distributed. "
        "(a) Calculate unbiased estimates of the mean and variance of the waiting times. [3] "
        "(b) Find a 98% confidence interval for the mean waiting time. [4] "
        "(c) The tram company states that the mean waiting time is 20 minutes. Use your interval to comment on this statement. [2] "
        "(d) Explain why a t distribution, not a normal distribution, is used in (b). [2]",
    ],
    "exam_answers": [
        "(a) x̄ = 3289.2/10 = 328.92 ml [B1]; s² = (1 081 901.76 − 3289.2²/10)/9 = 2.01 (3 s.f.) [B1]. "
        "(b) H₀: μ = 330, H₁: μ < 330 [B1]. Under H₀, T ~ t(9) [B1]. t = (328.92 − 330)/(1.4180/√10) = −1.08/0.44840 = −2.41 (3 s.f.) [M1 A1]. "
        "Critical value −1.833 (p-value 0.0197). −2.41 < −1.833, so reject H₀: sufficient evidence at 5% that the mean volume is less than 330 ml [A1]. "
        "(c) t(9) upper 0.5% point 3.250 [B1]. 328.92 ± 3.250 × 0.44840 [M1] = (327.46, 330.38) ml (2 d.p.) [A1]. "
        "(d) The 99% interval matches a two-tailed test at 1% [B1], whereas (b) was a one-tailed test at 5%, a much less demanding level, so the results are consistent [B1].",
        "(a) x̄ = (41.36 + 46.84)/2 = 44.1 [B1]. t(11) upper 2.5% point = 2.201 [B1]. 2.201 × s/√12 = 2.74 [M1], so s = 4.3124 and s² = 18.6 (3 s.f.) [A1]. "
        "(b) t(11) upper 5% point 1.796 [B1]: 44.1 ± 1.796 × 4.3124/√12 = 44.1 ± 2.2358, giving (41.86, 46.34) (2 d.p.) [A1]. "
        "(c) 46 lies inside the 90% interval [M1], so do not reject H₀ at the 10% level: insufficient evidence that μ ≠ 46 [A1]. "
        "(d) The sample is a random sample (of independent observations from the normal population) [B1].",
        "(a) H₀: μ = 15, H₁: μ ≠ 15, where μ is the population mean heart rate of athletes (beats per 15 s) [B1]. "
        "(b) SE = s/√n = 1.75/√11 = 0.52764 [B1]; t = (16.12 − 15)/0.52764 = 2.1226 [B1]. "
        "(c) p = 0.0598 > 0.05 [M1], so do not reject H₀: insufficient evidence at 5% that the mean heart rate differs from 15 [A1]. "
        "(d) p = 0.0598/2 = 0.0299 [B1] < 0.05, so reject H₀: sufficient evidence at 5% that the mean is greater than 15 [B1]. "
        "(e) t(10) upper 2.5% point = 2.228 [B1]. 16.12 ± 2.228 × 0.52764 [M1] = (14.94, 17.30) (2 d.p.) [A1]. "
        "(f) Heart rates are normally distributed in the population [B1]; check with a dot plot or Normal probability plot of the data (roughly straight line, no outliers) [B1].",
        "(a) ȳ = 13.5/9 = 1.5, so x̄ = 21.5 minutes [B1]. s² = (58.77 − 13.5²/9)/8 [M1] = 4.815 [A1]. "
        "(b) ν = 8, upper 1% point 2.896 [B1]. Standard error √4.815/3 = 0.73144 [M1]. 21.5 ± 2.896 × 0.73144 [M1] = (19.38, 23.62) minutes (2 d.p.) [A1]. "
        "(c) 20 lies inside the interval [M1], so the data are consistent with the company's statement (no evidence at the 2% two-tailed level against it) [A1]. "
        "(d) The population variance is unknown and must be estimated by s² [B1]; the sample is small (n = 9), so the extra uncertainty in s² is not negligible and the t distribution with 8 degrees of freedom must be used [B1].",
    ],
}
