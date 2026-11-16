UNIT = {
    "number": "AS12",
    "title": "Confidence intervals with the normal distribution",
    "tag": "AQA AS (SH1–SH3) · A level: Edexcel FS2 (5.2–5.3, 5.5), OCR A (5.05d), OCR MEI Major (SI7–SI9) · IAL S3 (3.3–3.6) · CAIE 9709 S2 prior knowledge",
    "notes": [
        ("h2", "12.1 Point estimates and interval estimates"),
        ("p", "A sample mean x̄ is a <b>point estimate</b> of the population mean μ: a single best guess. It will almost never equal μ "
              "exactly, and on its own it says nothing about how far off it might be. An <b>interval estimate</b> gives a range of "
              "plausible values for μ, together with a level of confidence. Its width reflects how precise the estimate is."),
        ("p", "The precision depends on the <b>standard error</b> of the mean, σ/√n: the standard deviation of the sampling distribution "
              "of X̄ (see Unit A2.7). If X ~ N(μ, σ²), then X̄ ~ N(μ, σ²/n) exactly; for a large sample from any population, X̄ is "
              "approximately N(μ, σ²/n) by the Central Limit Theorem."),
        ("h2", "12.2 Building the interval for μ when σ is known"),
        ("p", "Standardise X̄: Z = (X̄ − μ)/(σ/√n) ~ N(0, 1). Since P(−1.96 < Z < 1.96) = 0.95, "
              "P(X̄ − 1.96σ/√n < μ < X̄ + 1.96σ/√n) = 0.95. The interval X̄ ± 1.96σ/√n is a <b>random interval</b>: its centre "
              "changes from sample to sample. When you put in the observed x̄, you get one particular interval, the 95% confidence interval."),
        ("box", "Confidence interval for μ (σ known)", [
            "x̄ ± z × σ/√n, where z is the critical value with P(−z < Z < z) equal to the confidence level.",
            "Valid exactly if the population is normal (any n), and approximately for a large sample from any population (CLT).",
            "The interval is symmetrical about x̄. Its half-width z σ/√n is called the margin of error; its width is 2zσ/√n.",
        ]),
        ("table", ["Confidence level", "90%", "95%", "98%", "99%"], [
            ["z (two-tailed critical value)", "1.6449", "1.9600", "2.3263", "2.5758"],
            ["Tail area in each end", "0.05", "0.025", "0.01", "0.005"],
        ]),
        ("p", "These values agree with Table 2 (percentage points of the normal distribution). AQA, OCR MEI and Edexcel students will "
              "usually take them from the calculator's inverse normal function; Cambridge students use the tables. "
              "In written work 1.645, 1.96, 2.326 and 2.576 are all acceptable."),
        ("h2", "12.3 Large samples when σ is unknown (AQA SH2, IAL S3 3.6, OCR A 5.05d, MEI SI9)"),
        ("p", "Usually σ is not known. For a <b>large</b> sample, replace σ by the sample estimate s (with divisor n − 1, Unit A2.7) and "
              "use the normal distribution: x̄ ± z × s/√n. Two approximations are involved: the CLT (if the population is not normal) and "
              "using s for σ. Both are good when n is large. MEI uses n > 30 as a rule of thumb and OCR A says n > about 25; many textbooks use n ≥ 30."),
        ("p", "For a <b>small</b> sample from a normal population with unknown σ, the extra uncertainty in s matters, and the t distribution "
              "is used instead (Unit A2.9: AQA A level, Edexcel, MEI, CAIE). OCR A and IAL S3 do not use t at all."),
        ("box", "Which interval?", [
            "Normal population, σ known (any n):  x̄ ± z σ/√n  (exact).",
            "Any population, σ known, n large:  x̄ ± z σ/√n  (approximate, CLT).",
            "Any population, σ unknown, n large:  x̄ ± z s/√n  (approximate).",
            "Normal population, σ unknown, n small:  x̄ ± t s/√n with n − 1 degrees of freedom (Unit A2.9).",
        ]),
        ("h2", "12.4 What a confidence interval means"),
        ("p", "μ is a fixed (unknown) number, not a random variable. Once an interval such as (11.42, 13.38) has been calculated, μ either "
              "is or is not inside it; there is no probability left. The 95% describes the <b>method</b>: if many random samples were "
              "taken and an interval calculated from each, about 95% of those intervals would contain μ (MEI SI7: a long-run proportion)."),
        ("bullets", [
            "Correct: \"95% of intervals constructed in this way would contain μ\" or \"we are 95% confident that μ lies between 11.42 and 13.38\".",
            "Wrong: \"there is a 95% probability that μ lies between 11.42 and 13.38\", or \"95% of the data lie in the interval\".",
            "Each interval misses μ with probability 1 − (confidence level). For k independent 95% intervals, the number containing μ is B(k, 0.95). "
            "This is a favourite exam question.",
        ]),
        ("h2", "12.5 Width and sample size (MEI SI8)"),
        ("bullets", [
            "Width = 2zσ/√n. A higher confidence level means a larger z and a <b>wider</b> interval: more confidence costs precision.",
            "A larger sample gives a narrower interval, but only in proportion to 1/√n: to halve the width you need four times as many observations.",
            "A more variable population (larger σ) gives a wider interval.",
            "Sample size for a margin of error at most E: z σ/√n ≤ E, so n ≥ (zσ/E)². Always round <b>up</b> to the next whole number.",
            "Working backwards: given an interval (L, U), x̄ = (L + U)/2 and the half-width (U − L)/2 = zσ/√n, which can be solved for σ, n or z.",
        ]),
        ("h2", "12.6 Using a confidence interval to test a hypothesis (Edexcel 5.2, IAL 3.3, AQA SH3)"),
        ("p", "A 95% confidence interval contains exactly those values μ₀ that would <b>not</b> be rejected by a two-tailed z-test of "
              "H₀: μ = μ₀ against H₁: μ ≠ μ₀ at the 5% level. So: if μ₀ lies outside the 95% interval, there is evidence at the 5% level "
              "that μ ≠ μ₀; if μ₀ lies inside, there is insufficient evidence to reject H₀. In general a 100(1 − α)% interval corresponds "
              "to a two-tailed test at significance level α. State the conclusion in context and without certainty."),
        ("h2", "12.7 Interval for a proportion (CAIE 9709 S2 prior knowledge only)"),
        ("p", "For a large sample with sample proportion p̂ = x/n, an approximate interval for the population proportion p is "
              "p̂ ± z√(p̂(1 − p̂)/n). It uses the normal approximation to the binomial, so n must be large. No Further Mathematics "
              "specification examines this directly; it is included because Cambridge 9709 Paper 6 covers it."),
        ("warn", "Common mistakes", [
            "Using the wrong z: 1.645 is for a 90% two-sided interval (or a 5% one-tailed test), not 95%.",
            "Using σ/n or σ²/n instead of σ/√n for the standard error.",
            "Using the divisor n instead of n − 1 when estimating σ from a sample.",
            "Rounding a required sample size down. If n ≥ 138.3, the answer is 139.",
            "Saying \"there is a 95% chance that μ is in this interval\". The probability statement is about the method, not one interval.",
            "Using z with a small sample and unknown σ (t is needed), or forgetting to say that the CLT justifies a large-sample interval from a non-normal population.",
            "Rounding x̄ or s early, which shifts the end points. Keep full accuracy and give end points to 3 or 4 significant figures.",
        ]),
    ],
    "examples": [
        {
            "title": "An interval with known σ",
            "question": "A random sample of 25 values from N(μ, 2.5²) has mean 12.4. Find a 95% confidence interval for μ.",
            "steps": [
                "The population is normal with known σ, so X̄ ~ N(μ, 2.5²/25) exactly. Standard error = 2.5/√25 = 0.5.",
                "x̄ ± 1.96 × 0.5 = 12.4 ± 0.98.",
                "The 95% confidence interval for μ is (11.42, 13.38).",
            ],
        },
        {
            "title": "Different confidence levels and a claim",
            "question": "The masses of bags of flour are N(μ, 4²) grams. A random sample of 20 bags has mean 502.1 g. "
                        "(a) Find 95% and 99% confidence intervals for μ. (b) The label says the mean mass is 500 g. Comment.",
            "steps": [
                "(a) Standard error = 4/√20 = 0.8944. 95%: 502.1 ± 1.96 × 0.8944 = 502.1 ± 1.753, giving (500.35, 503.85).",
                "99%: 502.1 ± 2.5758 × 0.8944 = 502.1 ± 2.304, giving (499.80, 504.40). The 99% interval is wider.",
                "(b) 500 lies outside the 95% interval, so at the 5% level there is evidence that μ ≠ 500 (the mean appears to be higher). "
                "500 lies inside the 99% interval, so at the 1% level there is insufficient evidence to reject μ = 500.",
            ],
        },
        {
            "title": "A large sample with σ unknown",
            "question": "The times, x minutes, that 80 randomly chosen customers spend in a shop give Σx = 3896 and Σx² = 191 200. "
                        "Find a 95% confidence interval for the mean time, stating any approximations used.",
            "steps": [
                "x̄ = 3896/80 = 48.7. s² = (Σx² − n x̄²)/(n − 1) = (191 200 − 80 × 48.7²)/79 = 1464.8/79 = 18.54, so s = 4.306.",
                "n = 80 is large, so by the CLT X̄ is approximately normal, and s can be used in place of σ.",
                "48.7 ± 1.96 × 4.306/√80 = 48.7 ± 0.9436, giving (47.76, 49.64) minutes.",
            ],
        },
        {
            "title": "Choosing the sample size",
            "question": "A population has standard deviation 3. How large a sample is needed for the 95% confidence interval for μ to "
                        "have a width of at most 1?",
            "steps": [
                "Width = 2 × 1.96 × 3/√n ≤ 1, so √n ≥ 11.76 and n ≥ 138.3.",
                "Round up: the sample must contain at least 139 observations.",
            ],
        },
        {
            "title": "Working backwards from an interval",
            "question": "A 95% confidence interval for μ, from a sample of 16 observations from a normal population with known σ, is "
                        "(24.12, 27.88). Find x̄ and σ, and hence find the 90% confidence interval from the same sample.",
            "steps": [
                "x̄ = (24.12 + 27.88)/2 = 26. Half-width = 1.88 = 1.96 × σ/√16, so σ = 1.88 × 4/1.96 = 3.837 (4 s.f.).",
                "90% interval: 26 ± 1.6449 × 3.837/4 = 26 ± 1.578, giving (24.42, 27.58).",
            ],
        },
        {
            "title": "Interpreting several intervals",
            "question": "Ten independent random samples are taken and a 95% confidence interval for μ is calculated from each. "
                        "(a) Find the expected number of intervals that contain μ. (b) Find the probability that at least 9 of them contain μ.",
            "steps": [
                "Each interval contains μ with probability 0.95, independently, so the number N that contain μ is B(10, 0.95).",
                "(a) E(N) = 10 × 0.95 = 9.5.",
                "(b) P(N ≥ 9) = 0.95¹⁰ + 10 × 0.05 × 0.95⁹ = 0.5987 + 0.3151 = 0.914 (3 s.f.).",
            ],
        },
    ],
    "practice": [
        "A random sample of 36 values from a normal population with standard deviation 6 has mean 72. Find a 99% confidence interval for the population mean.",
        "A random sample of 50 observations from N(μ, 9) has mean 15.2. Find a 95% confidence interval for μ.",
        "The lengths of a component are N(μ, 0.5²) cm. A random sample of 10 has mean 8.43 cm. Find a 90% confidence interval for μ.",
        "A random sample of 100 values gives Σx = 2340 and Σx² = 56 100. Find unbiased estimates of the population mean and variance, "
        "and an approximate 95% confidence interval for the population mean.",
        "A population has standard deviation 12. Find the smallest sample size for which a 99% confidence interval for μ has a margin of error of at most 2.",
        "Explain how the width of a confidence interval for μ changes when (a) the sample size is increased from 25 to 100, (b) the confidence level is increased from 95% to 99%.",
        "A 95% confidence interval for μ, based on a sample of 40 observations with known σ, is (31.2, 34.6). Find x̄ and σ.",
        "A 95% confidence interval for μ is (4.82, 5.36). Test H₀: μ = 5 against H₁: μ ≠ 5 at the 5% level, stating your conclusion.",
        "A student says: \"The 95% confidence interval is (11.42, 13.38), so the probability that μ is between 11.42 and 13.38 is 0.95.\" Explain why this is wrong, and give a correct interpretation.",
        "Ten independent 90% confidence intervals for μ are calculated. Find the expected number that contain μ and the probability that all ten contain μ.",
        "(CAIE prior knowledge) In a random sample of 400 people, 136 support a proposal. Find an approximate 95% confidence interval for the proportion of all people who support it.",
        "A 95% confidence interval for μ (σ known) is (40.2, 45.8). Find the 99% confidence interval from the same sample.",
    ],
    "answers": [
        "72 ± 2.5758 × 6/6 = 72 ± 2.576, giving (69.42, 74.58).",
        "σ = 3. 15.2 ± 1.96 × 3/√50 = 15.2 ± 0.8315, giving (14.37, 16.03).",
        "8.43 ± 1.6449 × 0.5/√10 = 8.43 ± 0.2601, giving (8.17, 8.69).",
        "x̄ = 23.4; s² = (56 100 − 100 × 23.4²)/99 = 1344/99 = 13.58, s = 3.685. n is large, so 23.4 ± 1.96 × 3.685/10 = 23.4 ± 0.7222, giving (22.68, 24.12).",
        "2.5758 × 12/√n ≤ 2, so n ≥ (2.5758 × 6)² = 238.9; n = 239.",
        "(a) Width is proportional to 1/√n, so it halves. (b) z increases from 1.96 to 2.576, so the interval becomes 2.576/1.96 ≈ 1.31 times as wide.",
        "x̄ = 32.9. Half-width 1.7 = 1.96σ/√40, so σ = 1.7√40/1.96 = 5.49 (3 s.f.).",
        "5 lies inside the interval, so there is insufficient evidence at the 5% level to reject H₀: there is no evidence that μ differs from 5.",
        "μ is a fixed number, so it either is or is not in this particular interval. The 95% refers to the method: in repeated sampling, "
        "95% of intervals constructed this way would contain μ.",
        "Expected number = 10 × 0.9 = 9. P(all ten) = 0.9¹⁰ = 0.349 (3 s.f.).",
        "p̂ = 0.34. Margin = 1.96√(0.34 × 0.66/400) = 0.0464. Interval (0.294, 0.386).",
        "x̄ = 43, half-width 2.8 = 1.96 × SE. 99% half-width = 2.8 × 2.5758/1.96 = 3.680, giving (39.32, 46.68).",
    ],
    "exam": [
        "The lengths of bolts made by a machine are normally distributed with standard deviation 0.15 cm. A random sample of 12 bolts "
        "has total length 60.84 cm. (a) Find a 95% confidence interval for the mean length μ, giving the limits to 4 significant figures. [4] "
        "(b) The machine is supposed to make bolts with mean length 5.00 cm. Comment on this, using your interval. [2] "
        "(c) Find the smallest sample size that would make the width of a 95% confidence interval less than 0.1 cm. [3] "
        "(d) Eight independent samples are taken and a 95% confidence interval for μ is found from each. Find the probability that exactly one of them does not contain μ. [3]",
        "The times, x minutes, spent by a random sample of 60 visitors in a museum gallery give Σx = 1530 and Σx² = 42 300. "
        "(a) Find unbiased estimates of the mean and variance of the time spent. [3] "
        "(b) Find a 98% confidence interval for the mean time. [4] "
        "(c) Explain why it is not necessary to assume that the times are normally distributed. [2] "
        "(d) The manager believes that visitors spend 28 minutes on average. Comment on this belief. [2]",
        "A 90% confidence interval for the mean μ of a normal population with known standard deviation σ, based on a random sample of 25 "
        "observations, is (12.36, 14.04). (a) Find the sample mean and σ. [4] (b) Find a 95% confidence interval for μ from the same sample. [3] "
        "(c) A researcher claims that μ = 12.3. Use your intervals to test this claim at the 10% and at the 5% significance levels. [3] "
        "(d) Explain what is meant by a 90% confidence interval for μ. [2]",
        "The masses of hens' eggs on a farm are normally distributed with standard deviation 6 g. A random sample of 40 eggs has mean mass 61.8 g. "
        "(a) Find a 99% confidence interval for the mean mass. [3] "
        "(b) Find the smallest number of eggs needed for the width of a 99% confidence interval to be at most 3 g. [3] "
        "(c) A 99% interval is calculated from a new sample each day for 5 days. Find the probability that at least 4 of the intervals contain the mean mass. [3] "
        "(d) State, with a reason, whether the interval in (a) would still be approximately valid if the masses were not normally distributed. [2]",
    ],
    "exam_answers": [
        "(a) x̄ = 60.84/12 = 5.07 [B1]; 5.07 ± 1.96 × 0.15/√12 [M1 B1 for 1.96] = 5.07 ± 0.08487, giving (4.985, 5.155) [A1]. "
        "(b) 5.00 lies inside the interval [B1], so there is no evidence at the 5% level that the mean length differs from 5.00 cm [B1]. "
        "(c) 2 × 1.96 × 0.15/√n < 0.1 [M1], √n > 5.88, n > 34.57 [A1], so n = 35 [A1]. "
        "(d) Number not containing μ ~ B(8, 0.05) [M1]; P(exactly 1) = 8 × 0.05 × 0.95⁷ [M1] = 0.279 (3 s.f.) [A1].",
        "(a) x̄ = 1530/60 = 25.5 [B1]; s² = (42 300 − 60 × 25.5²)/59 [M1] = 3285/59 = 55.68 (4 s.f.) [A1]. "
        "(b) z = 2.3263 [B1]; 25.5 ± 2.3263 × √55.68/√60 [M1] = 25.5 ± 2.241 [A1], giving (23.26, 27.74) [A1]. "
        "(c) The sample is large (n = 60) [B1], so by the Central Limit Theorem the sample mean is approximately normally distributed whatever the distribution of the times [B1]. "
        "(d) 28 lies above the interval [B1], so there is evidence (at the 2% level) that the mean time is less than 28 minutes; the belief is not supported [B1].",
        "(a) x̄ = (12.36 + 14.04)/2 = 13.2 [B1]; half-width 0.84 = 1.6449 × σ/5 [M1 B1 for 1.6449], σ = 2.55 (3 s.f.) [A1]. "
        "(b) 13.2 ± 1.96 × 2.553/5 [M1] = 13.2 ± 1.001 [A1], giving (12.20, 14.20) [A1]. "
        "(c) 12.3 is outside the 90% interval, so reject μ = 12.3 at the 10% level [B1]; 12.3 is inside the 95% interval, so do not reject at the 5% level [B1]; "
        "there is some evidence against the claim, but it is not strong [B1]. "
        "(d) If many samples of 25 were taken and a 90% interval were calculated from each in the same way [B1], about 90% of these intervals would contain μ [B1].",
        "(a) 61.8 ± 2.5758 × 6/√40 [M1 B1] = 61.8 ± 2.444, giving (59.36, 64.24) [A1]. "
        "(b) 2 × 2.5758 × 6/√n ≤ 3 [M1], √n ≥ 10.30, n ≥ 106.2 [A1], so n = 107 [A1]. "
        "(c) Number containing μ ~ B(5, 0.99) [M1]; P(≥ 4) = 0.99⁵ + 5 × 0.01 × 0.99⁴ [M1] = 0.999 (3 s.f.) [A1]. "
        "(d) Yes [B1]: n = 40 is large, so by the Central Limit Theorem the sample mean is approximately normal [B1].",
    ],
}
