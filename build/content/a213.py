UNIT = {
    "number": "A2.13",
    "title": "Non-parametric tests 2: Wilcoxon tests",
    "tag": "A2 · OCR A (5.07), OCR MEI (single-sample Wilcoxon only), CAIE 9231 P4 (4.4) · follows A2.12 (sign test)",
    "notes": [
        ("h2", "13.1 From signs to ranks"),
        ("p", "The sign test of Unit A2.12 only records whether each observation is above or below the hypothesised median. "
              "A value just above m₀ counts the same as one far above it. The Wilcoxon tests also use the <b>ranks</b> of the "
              "data, so large deviations carry more weight than small ones. They are still non-parametric, since "
              "they make no assumption of normality, but they use more of the information in the data and so are more "
              "powerful than the sign test."),
        ("p", "The extra information comes at a price: the <b>Wilcoxon signed-rank test requires the population (or the "
              "population of differences) to be symmetric</b>. The test compares the sizes of the deviations above m₀ with "
              "those below. Under H₀ these must be balanced, which is only guaranteed if the distribution is symmetric about "
              "its median. For a symmetric distribution the median equals the mean, so the test is also a test of the mean. "
              "CAIE requires you to know that Wilcoxon tests are valid only for symmetrical distributions, and examiners "
              "report that few candidates can state this assumption."),
        ("table", ["Test", "Data", "Assumption", "Null hypothesis"], [
            ["Sign test (A2.12)", "One sample, or pairs", "Continuous population", "Population median = m₀ (or median difference = 0)"],
            ["Wilcoxon signed-rank", "One sample", "Symmetric population", "Population median = m₀"],
            ["Wilcoxon matched-pairs signed-rank", "Pairs", "Differences symmetric", "Population median difference = 0"],
            ["Wilcoxon rank-sum", "Two independent samples", "Same shape (location may differ)", "The two populations are identical"],
        ]),
        ("h2", "13.2 The single-sample Wilcoxon signed-rank test"),
        ("box", "Signed-rank procedure", [
            "H₀: population median m = m₀. H₁: m < m₀, m > m₀ or m ≠ m₀. The population is assumed symmetric.",
            "1. Find each difference d = x − m₀. Discard any d = 0; n is the number left.",
            "2. Rank the absolute values |d| from 1 (smallest) to n (largest), then attach the sign of d to each rank.",
            "3. P (OCR, MEI: W₊) = sum of the ranks of the positive differences. "
            "Q (OCR, MEI: W₋) = sum of the ranks of the negative differences. Check: P + Q = n(n + 1)/2.",
            "4. T = the smaller of P and Q. Reject H₀ if T ≤ the critical value from the table (Table 20).",
        ]),
        ("p", "Small values of T are significant. If H₀ is true, the positive and negative ranks should be well mixed, and "
              "P and Q should both be close to n(n + 1)/4. If the true median is below m₀, most differences are negative "
              "and the few positive ones are small, so P is small."),
        ("table", ["Alternative hypothesis", "Statistic to compare with the table", "Table column"], [
            ["H₁: m < m₀", "P (sum of positive ranks); H₁ predicts it is small", "one-tailed level"],
            ["H₁: m > m₀", "Q (sum of negative ranks); H₁ predicts it is small", "one-tailed level"],
            ["H₁: m ≠ m₀", "T = smaller of P and Q", "two-tailed level"],
        ]),
        ("p", "In a one-tailed test, first check that the data lean the way H₁ says. If H₁: m < m₀ but most differences are "
              "positive, the sum H₁ predicts to be small is the larger one, and there is no evidence for H₁ at all. In most "
              "exam questions the relevant sum is also the smaller, T."),
        ("h2", "13.3 Why the tables work: the distribution of T under H₀"),
        ("p", "Under H₀, with a symmetric population, each of the ranks 1, 2, …, n is equally likely to carry a '+' or a '−' "
              "sign, independently. So all 2ⁿ sign patterns are equally likely, and P is the sum of the ranks that happen "
              "to be '+'. For n = 4 there are 16 patterns and P ranges from 0 to 10:"),
        ("table", ["P", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"], [
            ["Number of patterns", "1", "1", "1", "2", "2", "2", "2", "2", "1", "1", "1"],
        ]),
        ("p", "So P(P ≤ 0) = 1/16 = 0.0625. Even the most extreme result is not significant at 5% one-tailed, which is why "
              "the table starts at n = 5, where P(T ≤ 0) = 1/32 = 0.03125. For n = 6, P(P ≤ 2) = 3/64 = 0.0469 ≤ 0.05 but "
              "P(P ≤ 3) = 5/64 = 0.0781, so the 5% one-tailed critical value is 2. Each table entry is the largest t with "
              "P(T ≤ t) ≤ the stated level, so the actual significance level is at most the nominal one. For a two-tailed "
              "test P(T ≤ t) = 2P(P ≤ t), which is why the two-tailed level is double the one-tailed level."),
        ("box", "Mean and variance of P under H₀ (derivation)", [
            "Write P = 1·I₁ + 2·I₂ + … + n·Iₙ, where Iᵢ = 1 if rank i is '+' and 0 if not. The Iᵢ are independent, each "
            "taking the value 1 with probability ½, so E(Iᵢ) = ½ and Var(Iᵢ) = ¼.",
            "E(P) = ½(1 + 2 + … + n) = n(n + 1)/4.",
            "Var(P) = ¼(1² + 2² + … + n²) = ¼ × n(n + 1)(2n + 1)/6 = n(n + 1)(2n + 1)/24.",
            "Q = n(n + 1)/2 − P has the same distribution, by symmetry.",
        ]),
        ("h2", "13.4 The Wilcoxon matched-pairs signed-rank test"),
        ("p", "For paired data (each individual measured twice, or matched pairs) apply the signed-rank test to the "
              "differences d = x − y. H₀: the population median of the differences is 0; equivalently, CAIE asks you to "
              "test the <b>identity of the two populations</b>. Discard zero differences, rank |d|, and find P, Q and T as "
              "before. The assumption is that the population of <b>differences</b> is symmetric. The individual "
              "measurements need not be symmetric. Paired data must be tested with a paired test: a two-sample test "
              "would ignore the pairing and the reduction in variability that it gives."),
        ("h2", "13.5 Normal approximation for the signed-rank test"),
        ("box", "Large n: signed-rank test", [
            "Under H₀, P and Q are each approximately N(n(n + 1)/4, n(n + 1)(2n + 1)/24).",
            "With a continuity correction: z = (T + 0.5 − n(n + 1)/4) ÷ √(n(n + 1)(2n + 1)/24).",
            "Reject H₀ if z < −1.6449 (5% one-tailed) or z < −1.9600 (5% two-tailed), and so on.",
            "Use it when n is beyond your booklet's table (CAIE MF19: n > 20; this book's Table 20: n > 30; the MEI booklet "
            "goes up to n = 50), or when a question asks for it.",
        ]),
        ("p", "The continuity correction is +0.5 because T takes integer values and we want P(T ≤ t), which becomes "
              "P(Y < t + 0.5) for the continuous normal variable Y."),
        ("h2", "13.6 The Wilcoxon rank-sum test (two independent samples)"),
        ("p", "For two <b>independent</b> samples (OCR: unpaired), of sizes m and n with m ≤ n, rank all m + n values "
              "together from 1 (smallest) upwards. If the two populations are identical, the ranks of the smaller sample "
              "are a random selection of m of the numbers 1 to m + n. If that sample comes from a population with smaller "
              "values, its ranks will be low and their sum R<sub>m</sub> will be small."),
        ("box", "Rank-sum procedure", [
            "H₀: the two populations are identical (in particular, have equal medians). H₁: the medians differ (or one is "
            "smaller). Assume the two distributions have the same shape.",
            "1. Rank all m + n observations together. Let R<sub>m</sub> = sum of the ranks of the smaller sample (size m).",
            "2. Find m(m + n + 1) − R<sub>m</sub>, the rank sum you would get by ranking from the other end.",
            "3. W = the smaller of R<sub>m</sub> and m(m + n + 1) − R<sub>m</sub>. Reject H₀ if W ≤ the critical value (Tables 21 and 22).",
            "If m = n, either sample may be used.",
        ]),
        ("p", "<b>Why m(m + n + 1) − R<sub>m</sub>?</b> If you rank from the largest instead, a value with rank r gets rank m + n + 1 − r. "
              "Summing over the m values of the smaller sample gives the reversed rank sum m(m + n + 1) − R<sub>m</sub>. The two "
              "rank sums add up to m(m + n + 1), and they are equally valid measures. A sample with unusually <i>high</i> "
              "values has a small reversed sum, so taking the smaller of the two makes one table of small critical values "
              "serve both tails. For a one-tailed test use R<sub>m</sub> itself if H₁ says the smaller sample's population has lower "
              "values, and m(m + n + 1) − R<sub>m</sub> if H₁ says higher."),
        ("p", "<b>Where the table comes from.</b> With m = n = 3 there are C(6, 3) = 20 equally likely sets of ranks for the "
              "first sample. R<sub>m</sub> = 6 only for {1, 2, 3} and R<sub>m</sub> = 7 only for {1, 2, 4}. So P(R<sub>m</sub> ≤ 6) = 1/20 = 0.05 and "
              "P(R<sub>m</sub> ≤ 7) = 2/20 = 0.1, and the 5% one-tailed critical value is 6 (Table 21). OCR also names the test after "
              "Mann and Whitney: their statistic U = R<sub>m</sub> − m(m + 1)/2 gives an equivalent test."),
        ("h2", "13.7 Normal approximation for the rank-sum test"),
        ("box", "Large samples: rank-sum test", [
            "Under H₀, R<sub>m</sub> is approximately N(m(m + n + 1)/2, mn(m + n + 1)/12).",
            "With a continuity correction: z = (W + 0.5 − m(m + n + 1)/2) ÷ √(mn(m + n + 1)/12).",
            "Use it when m or n is beyond the table (m, n > 10 in MF19, the OCR booklet and this book).",
        ]),
        ("p", "The mean is easy to justify. Each of the m ranks in the smaller sample is equally likely to be any of 1, 2, …, "
              "m + n, so its expected value is (m + n + 1)/2, and E(R<sub>m</sub>) = m(m + n + 1)/2. The variance is given in the "
              "formula booklets and need not be derived."),
        ("h2", "13.8 Ties and zero differences"),
        ("p", "CAIE and OCR exam questions contain no tied ranks and no zero differences (or values equal to m₀). You should "
              "still know what happens in practice. A zero difference is discarded and n is reduced, as in the sign test. "
              "Tied values are each given the <b>average</b> of the ranks they would occupy. For example, if the 4th and "
              "5th smallest values are equal, each gets rank 4.5. Ties change the null distribution slightly, so the tables "
              "become approximate."),
        ("h2", "13.9 Choosing a test"),
        ("table", ["Situation", "Best test"], [
            ["One sample (or pairs), population normal, σ unknown", "t-test (or paired t-test)"],
            ["One sample (or pairs), symmetric but not known to be normal", "Wilcoxon signed-rank (matched-pairs)"],
            ["One sample (or pairs), skewed or unknown shape, or only signs known", "Sign test"],
            ["Two independent samples, both normal with equal variances", "Two-sample (pooled) t-test"],
            ["Two independent samples, normality doubtful", "Wilcoxon rank-sum test"],
            ["Large samples (CLT applies)", "z-test using the normal distribution"],
        ]),
        ("p", "When its assumptions hold, the parametric test is the most powerful. Of the non-parametric tests, the "
              "Wilcoxon tests are more powerful than the sign test because they use ranks. Choose the most powerful "
              "test whose assumptions you can justify, and say why."),
        ("warn", "Common mistakes", [
            "Using μ, or 'median' without 'population', in hypotheses. Wilcoxon tests are about the population median.",
            "Ranking the signed differences instead of their absolute values |d|.",
            "Forgetting to discard zero differences, or forgetting to reduce n before using the table.",
            "Rejecting H₀ when T is <i>greater</i> than the critical value. Small T (or W) is significant: reject if T ≤ value.",
            "Reading the wrong column: one-tailed and two-tailed levels differ. (CAIE 2023: the correct value was 21, but "
            "many candidates used 17.)",
            "Not stating the symmetry assumption for a signed-rank test, or using a paired test on independent samples.",
            "In the rank-sum test, summing the ranks of the larger sample, or ranking the two samples separately.",
            "Omitting the continuity correction in the normal approximation.",
        ]),
    ],
    "examples": [
        {
            "title": "Single-sample signed-rank test, one-tailed",
            "question": "A manufacturer claims the median life of its batteries is 50 hours. A consumer group suspects it is "
                        "less. The lives, in hours, of 10 batteries are: 47.2, 51.3, 44.8, 49.5, 46.1, 52.7, 43.9, 48.6, "
                        "45.4, 50.8. Assuming the distribution of lives is symmetric, carry out a Wilcoxon signed-rank test "
                        "at the 5% level.",
            "steps": [
                "Let m be the population median life. H₀: m = 50. H₁: m < 50.",
                "d = x − 50: −2.8, 1.3, −5.2, −0.5, −3.9, 2.7, −6.1, −1.4, −4.6, 0.8.",
                "Ranks of |d|: 0.5 (1, −), 0.8 (2, +), 1.3 (3, +), 1.4 (4, −), 2.7 (5, +), 2.8 (6, −), 3.9 (7, −), "
                "4.6 (8, −), 5.2 (9, −), 6.1 (10, −).",
                "P = 2 + 3 + 5 = 10. Q = 55 − 10 = 45. H₁ predicts P is small, and T = 10.",
                "n = 10, 5% one-tailed critical value = 10. Since 10 ≤ 10, reject H₀. "
                "(Exact P(T ≤ 10) = 0.0420.)",
                "There is sufficient evidence at the 5% level that the population median battery life is less than 50 hours.",
            ],
        },
        {
            "title": "Two-tailed signed-rank test, with comparison to the sign test",
            "question": "The pH of 13 soil samples from a field is measured: 6.82, 6.31, 7.14, 6.50, 6.93, 7.38, 6.44, 7.05, "
                        "6.71, 6.97, 6.16, 7.22, 6.59. Test at the 5% level whether the median pH of the field differs from "
                        "6.5, assuming a symmetric distribution. Then compare with a sign test.",
            "steps": [
                "Let m be the population median pH. H₀: m = 6.5. H₁: m ≠ 6.5.",
                "d = x − 6.5: 0.32, −0.19, 0.64, 0 (discard), 0.43, 0.88, −0.06, 0.55, 0.21, 0.47, −0.34, 0.72, 0.09. n = 12.",
                "|d| in order: 0.06 (1, −), 0.09 (2), 0.19 (3, −), 0.21 (4), 0.32 (5), 0.34 (6, −), 0.43 (7), 0.47 (8), "
                "0.55 (9), 0.64 (10), 0.72 (11), 0.88 (12).",
                "Q = 1 + 3 + 6 = 10, P = 78 − 10 = 68, T = 10.",
                "n = 12, two-tailed 5% critical value = 13. Since 10 ≤ 13, reject H₀. There is sufficient evidence at the "
                "5% level that the population median pH differs from 6.5. (Exact two-tailed p-value 0.0210.)",
                "Sign test: 9 '+' and 3 '−', so the two-tailed p-value = 2P(X ≤ 3) = 2 × 0.0730 = 0.1460 for X ~ B(12, 0.5). "
                "This is not significant. The Wilcoxon test detects the shift because the negative differences are all small; "
                "it is the more powerful test when its symmetry assumption is reasonable.",
            ],
        },
        {
            "title": "Matched-pairs signed-rank test",
            "question": "Nine runners each run 5 km in their old shoes and, a week later, in a new design. Times (seconds):\n"
                        "Old: 1534, 1612, 1488, 1570, 1655, 1502, 1590, 1547, 1621.\n"
                        "New: 1522, 1617, 1470, 1563, 1633, 1511, 1575, 1544, 1610.\n"
                        "Test at the 5% level whether runners tend to be faster in the new shoes.",
            "steps": [
                "Paired data: use d = old − new: 12, −5, 18, 7, 22, −9, 15, 3, 11.",
                "Let m be the population median of d. H₀: m = 0. H₁: m > 0 (new shoes faster). "
                "Assume the differences have a symmetric distribution.",
                "Ranks of |d|: 3 (1), 5 (2, −), 7 (3), 9 (4, −), 11 (5), 12 (6), 15 (7), 18 (8), 22 (9).",
                "Q = 2 + 4 = 6, P = 45 − 6 = 39. H₁ predicts Q is small: T = 6.",
                "n = 9, 5% one-tailed critical value = 8. Since 6 ≤ 8, reject H₀. (Exact P(T ≤ 6) = 0.0273.)",
                "There is sufficient evidence at the 5% level that runners tend to be faster in the new shoes. "
                "(At the 2.5% level the critical value is 5, so the result would not be significant there.)",
            ],
        },
        {
            "title": "Rank-sum test for two independent samples",
            "question": "Workers are trained by method A or method B. The times (minutes) to assemble a unit are:\n"
                        "A: 23.1, 19.8, 21.4, 18.6, 24.0, 20.5.\n"
                        "B: 25.3, 22.7, 26.8, 21.9, 27.4, 24.6, 23.8, 28.1.\n"
                        "Test at the 5% level whether workers trained by method A tend to be quicker.",
            "steps": [
                "Two independent samples, normality not known: Wilcoxon rank-sum test. m = 6 (A), n = 8 (B).",
                "H₀: the populations of times for the two methods are identical. H₁: the population median time for "
                "method A is less than for method B.",
                "Combined ranking: 18.6 (1, A), 19.8 (2, A), 20.5 (3, A), 21.4 (4, A), 21.9 (5), 22.7 (6), 23.1 (7, A), "
                "23.8 (8), 24.0 (9, A), 24.6 (10), 25.3 (11), 26.8 (12), 27.4 (13), 28.1 (14).",
                "R<sub>A</sub> = 1 + 2 + 3 + 4 + 7 + 9 = 26. Check: m(m + n + 1) − R<sub>A</sub> = 6 × 15 − 26 = 64, so W = 26. "
                "H₁ predicts low ranks for A, and R<sub>A</sub> is indeed the smaller.",
                "m = 6, n = 8, 5% one-tailed critical value = 31. Since 26 ≤ 31, reject H₀. (Exact P(R<sub>A</sub> ≤ 26) = 0.0063.)",
                "There is sufficient evidence at the 5% level that workers trained by method A tend to assemble units more quickly.",
            ],
        },
        {
            "title": "Signed-rank test with a normal approximation",
            "question": "A matched-pairs experiment gives 34 differences, of which 2 are zero. The sum of the ranks of the "
                        "positive differences is 158. Test at the 5% level whether the population median difference is 0.",
            "steps": [
                "H₀: population median difference = 0. H₁: population median difference ≠ 0.",
                "Discard the zeros: n = 32. P = 158, Q = 32 × 33/2 − 158 = 528 − 158 = 370, so T = 158.",
                "Under H₀, mean = 32 × 33/4 = 264 and variance = 32 × 33 × 65/24 = 2860 (s.d. 53.48).",
                "z = (158 + 0.5 − 264)/√2860 = −1.973 (3 d.p.).",
                "Two-tailed 5% critical value −1.96. Since −1.973 < −1.96, reject H₀.",
                "There is sufficient evidence at the 5% level that the population median difference is not 0. "
                "(The approximate two-tailed p-value is 0.0485; the exact value is 0.0475, so the approximation is good.)",
            ],
        },
        {
            "title": "Rank-sum test with a normal approximation",
            "question": "Samples of 12 plants given fertiliser F and 15 untreated plants are ranked together by height. The "
                        "sum of the ranks of the 12 fertilised plants is 130. Test at the 5% level whether fertilised plants "
                        "tend to be shorter.",
            "steps": [
                "m = 12, n = 15. H₀: the height distributions are identical. H₁: the population median height of fertilised "
                "plants is less than that of untreated plants.",
                "R<sub>m</sub> = 130. m(m + n + 1) − R<sub>m</sub> = 12 × 28 − 130 = 206, so W = 130, which is the sum H₁ predicts to be small.",
                "Under H₀, mean = 12 × 28/2 = 168 and variance = 12 × 15 × 28/12 = 420 (s.d. 20.49).",
                "z = (130 + 0.5 − 168)/√420 = −1.830 (3 d.p.). One-tailed 5% critical value −1.6449.",
                "Since −1.830 < −1.6449, reject H₀ (p ≈ 0.0336). There is sufficient evidence at the 5% level that "
                "fertilised plants tend to be shorter.",
            ],
        },
    ],
    "practice": [
        "Eight differences are: 3.1, −1.2, 4.5, 2.2, −0.7, 5.8, 1.9, −3.6. Find P, Q and T, and check that P + Q = n(n + 1)/2.",
        "A sample of 9 values is: 22.4, 19.1, 25.3, 23.8, 21.2, 17.2, 26.7, 24.1, 20.6. Assuming a symmetric population, "
        "use a Wilcoxon signed-rank test at the 5% level to test H₀: m = 20 against H₁: m > 20.",
        "For n = 15, state the critical region for T in a signed-rank test (a) at the 5% level, two-tailed, (b) at the 1% "
        "level, one-tailed.",
        "For n = 6, list the sign patterns giving P ≤ 2 and find P(P ≤ 2) and P(P ≤ 3) under H₀. Hence explain why the 5% "
        "one-tailed critical value is 2.",
        "Two methods, X and Y, are used to measure the same 8 specimens. X: 14.2, 15.8, 13.1, 16.4, 12.9, 15.0, 14.7, 13.6. "
        "Y: 13.5, 16.9, 11.8, 14.3, 12.4, 13.2, 14.6, 11.1. Test at the 5% level whether the methods differ, using a "
        "Wilcoxon matched-pairs signed-rank test.",
        "Sample A: 34, 41, 29, 45, 38. Sample B: 47, 52, 36, 50, 44, 55, 49. Rank the values together and find R<sub>m</sub> and W.",
        "Sample A (4 values): 8.2, 6.9, 7.5, 9.1. Sample B (6 values): 9.8, 8.7, 10.4, 7.8, 11.2, 9.5. Test at the 5% "
        "level whether population A tends to have smaller values than population B.",
        "In a signed-rank test with n = 40, T = 270. Use a normal approximation to test at the 5% level (a) two-tailed, "
        "(b) one-tailed (in the direction of the data).",
        "In a rank-sum test m = 15, n = 20 and R<sub>m</sub> = 330. Use a normal approximation to test at the 5% level, two-tailed, "
        "whether the populations differ.",
        "Show that if a sample of size m has rank sum R<sub>m</sub> when m + n values are ranked from the smallest, its rank sum when "
        "ranked from the largest is m(m + n + 1) − R<sub>m</sub>.",
        "Assign ranks to these data, using average ranks for ties: 3, 5, 5, 8, 9, 9, 9, 12. Why do the CAIE and OCR "
        "examinations avoid tied ranks?",
        "Name the most suitable test in each case, and give a reason. (a) Before/after blood-pressure readings for "
        "10 patients; the differences are roughly symmetric but not known to be normal. (b) Marks of 7 pupils from one "
        "school and 9 from another; the distributions are skewed. (c) 30 people say whether they prefer tea or coffee. "
        "(d) Masses of 8 items from a normal population with unknown variance.",
    ],
    "answers": [
        "Ranks of |d|: 0.7 (1, −), 1.2 (2, −), 1.9 (3), 2.2 (4), 3.1 (5), 3.6 (6, −), 4.5 (7), 5.8 (8). "
        "P = 3 + 4 + 5 + 7 + 8 = 27, Q = 1 + 2 + 6 = 9, T = 9. P + Q = 36 = 8 × 9/2.",
        "d: 2.4, −0.9, 5.3, 3.8, 1.2, −2.8, 6.7, 4.1, 0.6. Ranks: 0.6 (1), 0.9 (2, −), 1.2 (3), 2.4 (4), 2.8 (5, −), "
        "3.8 (6), 4.1 (7), 5.3 (8), 6.7 (9). Q = 7, P = 38. H₁: m > 20 predicts Q small; T = 7. n = 9, 5% one-tailed "
        "critical value 8. 7 ≤ 8: reject H₀. Sufficient evidence at the 5% level that the population median exceeds 20.",
        "(a) T ≤ 25. (b) T ≤ 19.",
        "P = 0 (no '+'), P = 1 (rank 1 only '+'), P = 2 (rank 2 only '+'): 3 of the 64 patterns. P(P ≤ 2) = 3/64 = 0.0469 "
        "≤ 0.05. P = 3 also arises from {3} and {1, 2}, so P(P ≤ 3) = 5/64 = 0.0781 > 0.05. The largest t with "
        "P(T ≤ t) ≤ 0.05 is 2.",
        "d = X − Y: 0.7, −1.1, 1.3, 2.1, 0.5, 1.8, 0.1, 2.5. Ranks: 0.1 (1), 0.5 (2), 0.7 (3), 1.1 (4, −), 1.3 (5), "
        "1.8 (6), 2.1 (7), 2.5 (8). Q = 4, P = 32, T = 4. H₀: population median difference 0; H₁: ≠ 0. n = 8, two-tailed "
        "5% critical value 3. 4 > 3: do not reject H₀. Insufficient evidence at the 5% level that the methods differ. "
        "(It would be significant at the 10% level, critical value 5.)",
        "Combined order: 29 (1, A), 34 (2, A), 36 (3), 38 (4, A), 41 (5, A), 44 (6), 45 (7, A), 47 (8), 49 (9), 50 (10), "
        "52 (11), 55 (12). R<sub>m</sub> = 1 + 2 + 4 + 5 + 7 = 19; m(m + n + 1) − R<sub>m</sub> = 5 × 13 − 19 = 46; W = 19.",
        "Ranks of A: 6.9 (1), 7.5 (2), 8.2 (4), 9.1 (6), so R<sub>A</sub> = 13 (complement 4 × 11 − 13 = 31). H₀: the populations are "
        "identical; H₁: A's population median is smaller. m = 4, n = 6, 5% one-tailed critical value 13. 13 ≤ 13: reject "
        "H₀. Sufficient evidence at the 5% level that population A tends to have smaller values.",
        "Mean = 40 × 41/4 = 410, variance = 40 × 41 × 81/24 = 5535. z = (270.5 − 410)/√5535 = −1.875. "
        "(a) −1.875 > −1.96: do not reject H₀ at 5% two-tailed. (b) −1.875 < −1.6449: reject H₀ at 5% one-tailed. "
        "Conclusions in context depend on the direction of H₁.",
        "W = smaller of 330 and 15 × 36 − 330 = 210, so W = 210. Mean = 15 × 36/2 = 270, variance = 15 × 20 × 36/12 = 900 "
        "(s.d. 30). z = (210.5 − 270)/30 = −1.983 < −1.96. Reject H₀: sufficient evidence at the 5% level that the "
        "populations differ.",
        "A value of rank r from the bottom has rank m + n + 1 − r from the top. Summing over the m values: "
        "Σ(m + n + 1 − r) = m(m + n + 1) − Σr = m(m + n + 1) − R<sub>m</sub>.",
        "Ranks: 1, 2.5, 2.5, 4, 6, 6, 6, 8. With ties the exact null distribution, on which the tables are based, no "
        "longer applies, so the tabulated critical values would only be approximate.",
        "(a) Wilcoxon matched-pairs signed-rank test: paired data, differences symmetric. (b) Wilcoxon rank-sum test: two "
        "independent samples, not normal. (c) Sign test: only preferences (signs) are known. (d) t-test: normal population, "
        "unknown variance, so the parametric test is most powerful.",
    ],
    "exam": [
        "A café claims that the median time customers wait for their order is 6 minutes. A customer suspects it is less. "
        "She records 11 waiting times, in minutes: 4.2, 5.7, 3.4, 6.4, 4.9, 2.8, 5.1, 6.2, 3.9, 4.5, 6.0.\n"
        "(a) Carry out a Wilcoxon signed-rank test at the 5% level. [6]\n"
        "(b) Carry out a sign test at the 5% level on the same data. [3]\n"
        "(c) Explain why the two tests lead to different conclusions, and say which conclusion you prefer. [2]\n"
        "(d) State the assumption needed for the test in part (a). [1]",
        "Two laboratories each measure the sulphur content (%) of the same 12 fuel samples.\n"
        "Lab A: 2.84, 3.17, 2.95, 3.40, 2.61, 3.08, 2.77, 3.52, 2.99, 3.21, 3.36, 2.70.\n"
        "Lab B: 2.72, 3.22, 2.74, 3.32, 2.61, 2.93, 2.80, 3.25, 2.89, 3.35, 3.18, 2.64.\n"
        "(a) Explain why a paired test is appropriate. [1]\n"
        "(b) Use a Wilcoxon matched-pairs signed-rank test at the 5% level to test whether the laboratories differ. [7]\n"
        "(c) State an assumption needed for the test to be valid. [1]\n"
        "(d) Name a more powerful test that could be used if the differences were known to be normally distributed, and "
        "state why it is more powerful. [2]",
        "Crop yields (kg per plot) with two fertilisers are:\n"
        "Fertiliser A: 31.2, 28.4, 35.6, 27.9, 30.1.\n"
        "Fertiliser B: 33.8, 36.2, 29.5, 38.4, 34.7, 37.1.\n"
        "(a) Use a Wilcoxon rank-sum test at the 5% level to test whether the two fertilisers give different yields. [6]\n"
        "(b) State the smallest two-tailed significance level in the tables (5% or 10%) at which H₀ would be rejected. [1]\n"
        "(c) For samples of sizes m = 3 and n = 4, show that under H₀, P(R₃ ≤ 6) = 1/35 and P(R₃ ≤ 7) = 2/35. Hence explain "
        "why the critical value for a 5% one-tailed test is 6. [4]",
        "Independent random samples of 11 and 14 commuters from two towns record their journey times. All 25 times are "
        "ranked together, and the sum of the ranks of the 11 commuters from the first town is 185.\n"
        "(a) Show that, under H₀, the expected value of the rank sum of the sample of 11 is 143. [2]\n"
        "(b) Find W. [1]\n"
        "(c) Use a normal approximation to test at the 5% level whether journey times differ between the two towns. [5]\n"
        "(d) Would the conclusion change at the 1% level? Justify your answer. [2]",
    ],
    "exam_answers": [
        "(a) Let m = population median waiting time. H₀: m = 6, H₁: m < 6. B1. Discard 6.0: n = 10. M1. "
        "d: −1.8, −0.3, −2.6, 0.4, −1.1, −3.2, −0.9, 0.2, −2.1, −1.5. Ranks of |d|: 0.2 (1, +), 0.3 (2), 0.4 (3, +), "
        "0.9 (4), 1.1 (5), 1.5 (6), 1.8 (7), 2.1 (8), 2.6 (9), 3.2 (10). M1. P = 1 + 3 = 4 (Q = 51), T = 4. A1. "
        "n = 10, 5% one-tailed critical value 10. B1. 4 ≤ 10: reject H₀; sufficient evidence at the 5% level that the "
        "population median waiting time is less than 6 minutes. A1. (Exact P(T ≤ 4) = 0.0068.) "
        "(b) 2 '+', 8 '−'. X ~ B(10, 0.5). M1. P(X ≤ 2) = 56/1024 = 0.0547 > 0.05. A1. Do not reject H₀: insufficient "
        "evidence at the 5% level. A1. "
        "(c) The sign test ignores the sizes of the differences; the two positive differences are the smallest, which only "
        "the Wilcoxon test takes into account, so the Wilcoxon test is more powerful. B1. Prefer the Wilcoxon conclusion "
        "if the symmetry assumption is reasonable. B1. "
        "(d) The distribution of waiting times is symmetric (about its median). B1.",
        "(a) Both labs measure the same samples, so the results are paired, and differences remove sample-to-sample "
        "variation. B1. "
        "(b) H₀: population median of (A − B) = 0; H₁: ≠ 0. B1. d = A − B: 0.12, −0.05, 0.21, 0.08, 0, 0.15, −0.03, 0.27, "
        "0.10, −0.14, 0.18, 0.06. M1. Discard 0: n = 11. B1. Ranks of |d|: 0.03 (1, −), 0.05 (2, −), 0.06 (3), 0.08 (4), "
        "0.10 (5), 0.12 (6), 0.14 (7, −), 0.15 (8), 0.18 (9), 0.21 (10), 0.27 (11). M1. Q = 1 + 2 + 7 = 10, P = 56, "
        "T = 10. A1. Two-tailed 5% critical value for n = 11 is 10. B1. 10 ≤ 10: reject H₀; sufficient evidence at the 5% "
        "level that the laboratories differ (Lab A tends to give higher readings). A1. "
        "(c) The population of differences is symmetric. B1. "
        "(d) A paired t-test. B1. It uses the actual values of the differences, not just their ranks, so it has a lower "
        "probability of a Type II error when the normality assumption holds. B1.",
        "(a) H₀: the two populations of yields are identical; H₁: the population median yields differ. B1. m = 5 (A), "
        "n = 6. Ranks: 27.9 (1, A), 28.4 (2, A), 29.5 (3), 30.1 (4, A), 31.2 (5, A), 33.8 (6), 34.7 (7), 35.6 (8, A), "
        "36.2 (9), 37.1 (10), 38.4 (11). M1. R<sub>A</sub> = 1 + 2 + 4 + 5 + 8 = 20. A1. 5 × 12 − 20 = 40, so W = 20. M1. "
        "Two-tailed 5% (2.5% one-tailed) critical value for m = 5, n = 6 is 18. B1. 20 > 18: do not reject H₀; "
        "insufficient evidence at the 5% level that the fertilisers give different yields. A1. "
        "(b) 10%: critical value 20, and 20 ≤ 20. B1. (Exact two-tailed p-value 0.0823.) "
        "(c) There are C(7, 3) = 35 equally likely sets of 3 ranks under H₀. B1. R₃ = 6 only for {1, 2, 3}, so "
        "P(R₃ ≤ 6) = 1/35. B1. R₃ = 7 only for {1, 2, 4}, so P(R₃ ≤ 7) = 2/35. B1. 1/35 = 0.0286 ≤ 0.05 but "
        "2/35 = 0.0571 > 0.05, so the largest critical value is 6. B1.",
        "(a) Under H₀ each of the 11 ranks is equally likely to be any of 1 to 25, with mean (25 + 1)/2 = 13. M1. "
        "E(R) = 11 × 13 = 143. A1. "
        "(b) W = smaller of 185 and 11 × 26 − 185 = 101: W = 101. B1. "
        "(c) H₀: the distributions of journey times in the two towns are identical; H₁: the population medians differ. B1. "
        "Variance = 11 × 14 × 26/12 = 333.67 (s.d. 18.27). M1. z = (101 + 0.5 − 143)/√333.67 = −2.272. M1 (continuity "
        "correction) A1. −2.272 < −1.96: reject H₀; sufficient evidence at the 5% level that journey times differ between "
        "the towns. A1. "
        "(d) At 1% two-tailed the critical value is −2.5758; −2.272 > −2.5758, so H₀ would not be rejected. M1 A1.",
    ],
}
