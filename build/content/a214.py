UNIT = {
    "number": "A2.14",
    "title": "Normal probability plots, software output and simulation",
    "tag": "A2 · OCR MEI Statistics Major only (SR30–SR32, SI12, SZ1–SZ2) · builds on A2.7–A2.9 and A2.13",
    "notes": [
        ("p", "OCR MEI expects you to use statistical software and spreadsheets during the course, and states that "
              "\"in the examination learners will be assessed on the interpretation of output from such software\". "
              "You are never asked to do a Kolmogorov–Smirnov calculation or to build a simulation in the exam. You are "
              "asked to read output, judge whether a model is reasonable, draw conclusions in context and explain what the "
              "output can and cannot tell you. This unit covers the three kinds of output that appear most: Normal "
              "probability plots and Kolmogorov–Smirnov output (SR31), output for the tests and intervals elsewhere in the "
              "course (SI12, SH2, SH4, Sb6, Sb9), and spreadsheet simulations (SZ1, SZ2). Effect size for correlation (Sb7) "
              "is covered in Unit AS9 and is not repeated here."),

        ("h2", "14.1 Why we check normality"),
        ("p", "Many procedures in this course assume a Normal population: the t-test and t confidence interval for a single "
              "mean (Unit A2.9), the paired t procedures (Unit A2.10), and the z procedures for a small sample with known σ "
              "(Unit A2.8). The Normal distribution is used in two different ways (SR30, SR32):"),
        ("bullets", [
            "<b>As a model for the population.</b> The data themselves are assumed to come from N(μ, σ²). With a small sample this "
            "assumption matters, because X̄ is only guaranteed to be Normal if the population is.",
            "<b>As an approximation through the Central Limit Theorem.</b> For a large sample (MEI's rule of thumb is n > 30), X̄ is "
            "approximately Normal whatever the shape of the population (Unit A2.7). Normality of the population then matters much less.",
        ]),
        ("p", "So the question \"are these data plausibly from a Normal distribution?\" matters most when n is small, which is "
              "exactly when it is hardest to answer. Software gives two tools: a picture (the Normal probability plot) and a "
              "test (Kolmogorov–Smirnov or similar). A χ² goodness-of-fit test for the Normal is not on the MEI specification."),

        ("h2", "14.2 The Normal probability plot"),
        ("p", "A <b>Normal probability plot</b> compares the ordered data with the values you would expect from a Normal "
              "distribution. If the data are from a Normal distribution, the points lie close to a straight line."),
        ("box", "Constructing a Normal probability plot (for understanding; not examined as a calculation)", [
            "1. Put the n data values in order: x₍₁₎ ≤ x₍₂₎ ≤ … ≤ x₍ₙ₎.",
            "2. Give the i-th value the cumulative proportion pᵢ = (i − 0.5)/n. (Some software uses (i − 3/8)/(n + 1/4) or i/(n + 1); the picture is almost the same.)",
            "3. Find the <b>Normal score</b> zᵢ = Φ⁻¹(pᵢ), the value with P(Z ≤ zᵢ) = pᵢ.",
            "4. Plot x₍ᵢ₎ against zᵢ. If X ~ N(μ, σ²), then x₍ᵢ₎ ≈ μ + σzᵢ, so the points lie close to a straight line with intercept ≈ μ and gradient ≈ σ.",
        ]),
        ("p", "Software may label the Normal-score axis with the percentages 100pᵢ instead of zᵢ (\"Normal probability paper\"), "
              "so the scale is stretched at the ends. Some packages put the data on the horizontal axis instead. "
              "<b>Always read the axis labels first</b>: swapping the axes reverses the direction of every curve described below. "
              "In this book the data are on the vertical axis and the Normal scores on the horizontal axis."),
        ("p", "The line is a guide, not a test. Even genuinely Normal data wobble about it, especially at the two ends, and "
              "with a small sample (say n < 15) quite large wobbles are common. Judge the overall pattern, not single points."),

        ("h2", "14.3 Reading the shape of the plot"),
        ("table", ["What you see (data on vertical axis)", "What it means about the distribution"], [
            ["Points close to a straight line", "A Normal model is reasonable"],
            ["A curve bending upwards (concave up): flat at the left, steep at the right", "Positive (right) skew: a long upper tail"],
            ["A curve bending downwards (concave down): steep at the left, flat at the right", "Negative (left) skew: a long lower tail"],
            ["S shape steep at both ends: lowest points below the line, highest points above", "Heavier tails than Normal: more extreme values"],
            ["S shape flat at both ends: lowest points above the line, highest below", "Lighter tails than Normal, e.g. a uniform distribution"],
            ["One or two points far from an otherwise straight line, at one end", "Outlier(s): check them for errors before modelling"],
            ["A jump or flat section in the middle", "Possibly two groups mixed together (bimodal)"],
            ["Horizontal runs of equal values (steps)", "Data rounded or discrete; not in itself evidence against normality"],
        ]),
        ("p", "Why does right skew give an upward curve? In a long upper tail the largest values are much further from the "
              "middle than a Normal distribution predicts, so at large Normal scores the points rise above the line. The lower "
              "values are bunched together, so at the left the points change slowly and the plot is flat. A useful check from "
              "a table of plotted points: in Normal data the gap from the median to the upper quartile is about the same as "
              "the gap from the lower quartile to the median."),

        ("h2", "14.4 Kolmogorov–Smirnov output"),
        ("p", "The Kolmogorov–Smirnov (K–S) test compares the cumulative distribution of the sample with the cdf of the "
              "proposed model. Its test statistic D is the largest vertical distance between the two. Large D means a poor fit. "
              "You only need to interpret the <b>p-value</b> it produces (SR31); calculating D or its p-value is not required."),
        ("box", "Interpreting a K–S test of normality", [
            "H₀: the data come from a Normal distribution (the population is Normal). H₁: the population is not Normal.",
            "If p < significance level: reject H₀. There is evidence that the population is not Normal, so a procedure "
            "that assumes normality (e.g. a t-test on a small sample) may not be valid.",
            "If p ≥ significance level: do not reject H₀. A Normal model is <b>reasonable</b> (the data are consistent with it). "
            "This does <b>not</b> prove the population is Normal.",
            "Always look at the Normal probability plot as well: the two should tell the same story.",
        ]),
        ("p", "Two limits of the test are worth knowing. With a <b>small sample</b> the test has low power: data from a clearly "
              "skewed population, or with an outlier, can still give a large p-value, so the plot is often more informative. "
              "With a <b>very large sample</b> the test detects tiny departures that do not matter in practice. Software also "
              "differs in how it allows for μ and σ being estimated from the same data (some packages apply the Lilliefors "
              "correction), so two packages can give different p-values for the same data. In the exam, simply use the p-value "
              "you are given. Other tests of normality you may meet in output, such as Shapiro–Wilk or Anderson–Darling, are "
              "interpreted in exactly the same way."),

        ("h2", "14.5 Reading software output for tests and intervals"),
        ("p", "The tests in this course all produce the same few pieces of output, whatever the package. The skills are the same "
              "each time: identify the hypotheses, find the p-value or interval, check the tail, check the assumptions, and "
              "conclude in context without certainty."),
        ("table", ["Output label", "Meaning", "Watch out for"], [
            ["Mean, StDev (SD)", "x̄ and s (divisor n − 1)", "Some packages also show σₙ (divisor n); use s for inference"],
            ["SE Mean", "Standard error s/√n (SI4)", "Not the same as SD"],
            ["T (or t Stat), DF", "t = (x̄ − μ₀)/(s/√n), ν = n − 1", "Sign of t shows which side of μ₀ the sample lies"],
            ["P-value (two-tail / one-tail)", "Probability, if H₀ is true, of a result at least this extreme", "Check which tail; halve a two-tail p only if the sample lies on the side H₁ predicts"],
            ["95% CI (lower, upper)", "x̄ ± t × s/√n (or z) (SI9)", "A two-sided 95% CI matches a two-tailed 5% test"],
            ["Chi-squared, DF, contributions", "Σ(O − E)²/E and each cell's share (SH2, Unit AS8)", "Large contributions show where the association lies"],
            ["r (or R), p-value", "pmcc and its test of ρ = 0 (Sb6, Unit AS9)", "Significance is not effect size: see Unit AS9"],
            ["W+, W−, p-value", "Wilcoxon signed-rank sums (SH5, Unit A2.13)", "Assumes a symmetric population"],
        ]),
        ("box", "Using a confidence interval to make a decision (SI13)", [
            "If a hypothesised value μ₀ lies <b>outside</b> a two-sided 100(1 − α)% CI, reject H₀: μ = μ₀ in a two-tailed test at the 100α% level.",
            "If μ₀ lies <b>inside</b>, do not reject H₀ at that level.",
            "A 95% CI corresponds to a two-tailed 5% test, or a one-tailed 2.5% test. It does <b>not</b> correspond to a one-tailed 5% test, so a one-tailed test at 5% can be significant even when μ₀ is inside the 95% CI.",
            "From an interval (L, U): x̄ = (L + U)/2 and the margin of error is (U − L)/2.",
        ]),
        ("p", "Questions may show output for a distribution you have not studied, such as a confidence interval for a median or a "
              "proportion (SI12). Any necessary details will be given. Interpret it exactly as you would a familiar interval: "
              "it is a range of plausible values for the parameter, and in the long run 95% of intervals built this way contain it."),

        ("h2", "14.6 Simulating distributions in a spreadsheet (SZ1)"),
        ("p", "A spreadsheet function such as RAND() returns a random number U ~ U(0, 1), the continuous uniform distribution on "
              "[0, 1]. Every other distribution can be built from it. The values change every time the sheet recalculates, so "
              "each recalculation is a new run of the simulation."),
        ("table", ["Distribution", "Spreadsheet formula (Excel style)", "Why it works"], [
            ["Continuous uniform U(0, 1)", "=RAND()", "Built in"],
            ["Continuous uniform U(a, b)", "=a+(b−a)*RAND()", "Stretches [0, 1] to [a, b]"],
            ["Discrete uniform on {1, …, 6}", "=RANDBETWEEN(1,6) or =INT(6*RAND())+1", "6U lies in [0, 6); INT gives 0, …, 5, each with probability 1/6"],
            ["Discrete uniform on {a, …, b}", "=RANDBETWEEN(a,b) or =INT((b−a+1)*RAND())+a", "Shifts the previous idea to start at a"],
            ["Normal N(μ, σ²)", "=NORM.INV(RAND(),μ,σ)", "Inverse cdf: P(Φ⁻¹(U) ≤ z) = P(U ≤ Φ(z)) = Φ(z)"],
            ["Bernoulli, P(success) = p", "=IF(RAND()<p,1,0)", "P(U < p) = p"],
        ]),
        ("p", "The Normal formula is an example of the <b>inverse cdf method</b>: if F is a continuous cdf and U ~ U(0, 1), then "
              "F⁻¹(U) has cdf F (compare Unit A2.1). A table of simulated values is usually set out with one <b>trial</b> per "
              "row and one random quantity per column, then a column that records whether the event of interest happened "
              "(1 or 0), and finally a count or average at the bottom."),

        ("h2", "14.7 Estimating probabilities and distributions by simulation (SZ2)"),
        ("p", "Simulation is useful when the theory is hard or impossible at this level: for example the distribution of 2X − Y "
              "when X is uniform and Y is Normal, the total of 10 dice, the total waiting time for trains over many journeys, or "
              "the product of two random lengths. The method is always the same."),
        ("box", "Estimating a probability by simulation", [
            "1. Simulate one trial of the situation, using random numbers for each random quantity.",
            "2. Record whether the event A happened.",
            "3. Repeat N times, independently. Estimate P(A) by p̂ = (number of trials in which A happened)/N.",
            "4. Means, variances and the whole shape of a distribution can be estimated in the same way from the N simulated values.",
            "Check a simulation where you can: e.g. compare the simulated mean of 2X − Y with the exact value 2E(X) − E(Y).",
        ]),
        ("p", "Simulation is also how the Central Limit Theorem is usually investigated: simulate many samples of size n from a "
              "non-Normal population, calculate each sample mean, and look at the distribution of the means. As n increases, "
              "the means have standard deviation close to σ/√n, and their Normal probability plot becomes straighter."),

        ("h2", "14.8 The effect of the number of repetitions"),
        ("p", "A simulated probability is an estimate, not the true value. Two runs of the same simulation give different "
              "answers. The number of times A happens in N trials is B(N, p), so the estimate p̂ has mean p and standard "
              "deviation √(p(1 − p)/N), called its <b>standard error</b>."),
        ("box", "Precision of a simulated probability", [
            "Standard error of p̂: √(p(1 − p)/N), estimated by √(p̂(1 − p̂)/N).",
            "About 95% of runs give p̂ within about 2 standard errors of p (Normal approximation, N large).",
            "To halve the standard error, multiply N by 4. To make it 10 times smaller, multiply N by 100.",
            "For a simulated mean the standard error is s/√N, where s is the SD of the simulated values.",
            "Rare events need very many repetitions: if p is small, a run of 100 or 1000 trials may contain no occurrences at all.",
        ]),
        ("p", "In the exam you may be asked why two runs differ, which run is more reliable, how to combine runs (add the counts "
              "and the numbers of trials), or roughly how many repetitions are needed for a given accuracy. Combining runs is "
              "valid because they are independent runs of the same experiment."),

        ("warn", "Common mistakes", [
            "Treating a large K–S p-value as proof that the data are Normal. It only means a Normal model has not been rejected.",
            "Getting H₀ the wrong way round for a normality test. H₀ is \"the population is Normal\", so a small p-value is bad news for the Normal model.",
            "Ignoring the plot. With small samples the K–S test has low power, and an outlier or curve in the plot matters even when p is large.",
            "Reading curvature with the axes swapped. Check which axis holds the data before saying \"skewed to the right\".",
            "Using a two-tailed p-value for a one-tailed test (or the reverse). Halve the two-tailed value only if the sample lies on the side H₁ predicts.",
            "Saying a 95% CI containing μ₀ means a one-tailed 5% test cannot be significant. The CI matches a two-tailed test.",
            "Quoting a simulated probability as if it were exact, or saying a larger N makes the estimate \"correct\". It makes it more precise.",
            "Writing =INT(6*RAND()) for a die: this gives 0 to 5. Add 1.",
            "Concluding with certainty, e.g. \"the data are Normal\" or \"the mean is 40\". Say \"there is (in)sufficient evidence…\" or \"a Normal model is reasonable\".",
        ]),
    ],

    "examples": [
        {
            "title": "Constructing and reading a Normal probability plot",
            "question": "The heights, in mm, of 10 seedlings are\n41, 45, 47, 48, 50, 51, 52, 54, 56, 60.\n"
                        "(a) Find the Normal scores used to plot these data, using pᵢ = (i − 0.5)/n.\n"
                        "(b) Given x̄ = 50.4 and s = 5.522, find where the line x = x̄ + sz is at z = ±1.645, and comment on the plot.",
            "steps": [
                "(a) n = 10, so pᵢ = 0.05, 0.15, 0.25, …, 0.95.",
                "zᵢ = Φ⁻¹(pᵢ): −1.645, −1.036, −0.674, −0.385, −0.126, 0.126, 0.385, 0.674, 1.036, 1.645 (3 d.p.). They are symmetric about 0.",
                "The plotted points are (−1.645, 41), (−1.036, 45), (−0.674, 47), …, (1.645, 60).",
                "(b) At z = −1.645 the line gives 50.4 − 5.522 × 1.645 = 41.3; at z = 1.645 it gives 50.4 + 5.522 × 1.645 = 59.5.",
                "The smallest and largest values, 41 and 60, are very close to these. The middle points also lie close to the line: "
                "e.g. at z = ±0.674 the line gives 46.7 and 54.1, and the data give 47 and 54.",
                "The points lie close to a straight line with no systematic curve, so a Normal model for seedling height is reasonable. "
                "(For interest: the correlation between the zᵢ and the data is 0.998.)",
            ],
        },
        {
            "title": "Comparing two data sets with plots and K–S output",
            "question": "Software analyses two samples of size 40: A, the masses of apples (g), and B, the waiting times (minutes) at a "
                        "clinic. Selected points of each Normal probability plot are shown, with the K–S output.\n"
                        "Normal score z: −2.241, −0.714, −0.031, 0.031, 0.714, 2.241 (points i = 1, 10, 20, 21, 31, 40)\n"
                        "A: 130, 147, 153, 154, 159, 171\n"
                        "B: 2.0, 3.1, 4.5, 4.7, 10.9, 19.2\n"
                        "K–S test for normality:\nA: mean 152.1, SD 8.666, D = 0.093, p = 0.852\nB: mean 6.60, SD 4.792, D = 0.290, p = 0.002.\n"
                        "(a) Describe the shape of each plot and what it suggests.\n"
                        "(b) Interpret each K–S p-value at the 5% level.\n"
                        "(c) A researcher wants a 95% confidence interval for the mean waiting time. Comment.",
            "steps": [
                "(a) A: from i = 10 to i = 20 the values rise by 6, and from i = 21 to i = 31 by 5; the gaps are balanced and the "
                "plot is close to a straight line. A Normal model for apple mass looks reasonable.",
                "B: from i = 10 to 20 the values rise by only 1.4, but from i = 21 to 31 by 6.2, and the top value 19.2 is far above. "
                "The plot is flat on the left and steep on the right: it curves upwards. This shows positive skew, which is typical "
                "of waiting times (there is a lower limit, here about 2 minutes, but no upper limit).",
                "(b) A: H₀: apple masses are Normally distributed. p = 0.852 > 0.05, so do not reject H₀. A Normal model is reasonable.",
                "B: H₀: waiting times are Normally distributed. p = 0.002 < 0.05, so reject H₀. There is strong evidence that waiting "
                "times are not Normally distributed. Both data sets: the test agrees with the plot.",
                "(c) Waiting times are not Normal, so a t interval based on a Normal population is not justified. However, n = 40 > 30, "
                "so by the Central Limit Theorem X̄ is approximately Normal and an interval x̄ ± 1.96 s/√n is a reasonable "
                "approximation. With a strongly skewed population it is wise to treat it with some caution.",
            ],
        },
        {
            "title": "Interpreting one-sample t-test output",
            "question": "A cereal is sold in boxes labelled 500 g. A trading standards officer weighs a random sample of 12 boxes. The "
                        "Normal probability plot of the masses is close to a straight line and the K–S p-value is 0.808. Software output:\n"
                        "One-sample t test | H₀: μ = 500\n"
                        "n = 12 | Mean = 496.85 | SD = 4.797 | SE Mean = 1.385\n"
                        "t = −2.275 | DF = 11 | P-value (two-tailed) = 0.0439\n"
                        "95% CI for μ: (493.80, 499.90)\n"
                        "(a) Explain why a t-test is appropriate.\n"
                        "(b) Test at the 5% level whether the mean mass differs from 500 g.\n"
                        "(c) The officer suspects boxes are underweight. Carry out a test at the 1% level.\n"
                        "(d) Show how the values of SE Mean and the confidence interval are obtained.",
            "steps": [
                "(a) σ is unknown and the sample is small (n = 12). The plot is straight and K–S p = 0.808 > 0.05, so it is reasonable "
                "to assume the masses are Normally distributed, which the t-test requires.",
                "(b) μ = population mean mass of boxes (g). H₀: μ = 500, H₁: μ ≠ 500. Under H₀, T ~ t₁₁.",
                "p = 0.0439 < 0.05, so reject H₀. There is sufficient evidence at the 5% level that the mean mass is not 500 g. "
                "Equivalently, 500 is outside the 95% CI (493.80, 499.90).",
                "(c) H₀: μ = 500, H₁: μ < 500. The sample mean is below 500 (t is negative), so the one-tailed p-value is "
                "0.0439/2 = 0.0220 (3 s.f.).",
                "0.0220 > 0.01, so do not reject H₀. There is insufficient evidence at the 1% level that the boxes are underweight on average.",
                "(d) SE = s/√n = 4.797/√12 = 1.385. t = (496.85 − 500)/1.385 = −2.27 (software: −2.275).",
                "With t₁₁ upper 2.5% point 2.201: 496.85 ± 2.201 × 1.385 = 496.85 ± 3.05, giving (493.80, 499.90).",
            ],
        },
        {
            "title": "Simulating the total of 10 dice: the effect of N",
            "question": "A spreadsheet simulates throwing 10 fair dice. Each row has ten cells =RANDBETWEEN(1,6), their total T, and "
                        "=IF(T>40,1,0). Three runs were made with each number of repetitions N. Number of rows with T > 40:\n"
                        "N = 100: 17, 15, 13\n"
                        "N = 1000: 156, 149, 158\n"
                        "N = 10 000: 1594, 1573, 1550\n"
                        "(a) Give the estimate of P(T > 40) from each run with N = 1000, and a combined estimate from all three runs with N = 10 000.\n"
                        "(b) The exact value is 0.1565. Find the standard error of p̂ for N = 100 and N = 10 000, and comment on the runs.\n"
                        "(c) In the same three runs of 1000, the numbers of rows with T > 50 were 1, 6 and 1. The exact value of P(T > 50) is 0.00148. Comment.",
            "steps": [
                "(a) N = 1000: 0.156, 0.149, 0.158.",
                "Combined: (1594 + 1573 + 1550)/30 000 = 4717/30 000 = 0.157 (3 s.f.).",
                "(b) N = 100: SE = √(0.1565 × 0.8435/100) = 0.0363. N = 10 000: SE = √(0.1565 × 0.8435/10 000) = 0.00363.",
                "With N = 100 the estimates 0.17, 0.15, 0.13 vary by several hundredths, within about 2 SE (±0.073) of 0.1565. "
                "With N = 10 000 they are 0.1594, 0.1573, 0.1550, all within about 2 SE (±0.0073). Multiplying N by 100 made the "
                "standard error 10 times smaller, so the estimates agree much more closely.",
                "(c) Expected count in 1000 rows = 1000 × 0.00148 = 1.48, so counts of 1 and 6 give estimates 0.001 and 0.006, "
                "which differ by a factor of 6. The SE is √(0.00148 × 0.99852/1000) = 0.00122, almost as big as p itself.",
                "Rare events need far more repetitions: for an SE of 10% of p you need N ≥ (1 − p)/(0.01p) ≈ 67 500 trials.",
            ],
        },
        {
            "title": "Estimating P(2X − Y > 0) by spreadsheet simulation",
            "question": "X ~ U(2, 6) is a continuous uniform random variable and Y ~ N(9, 1.5²), independently. A spreadsheet uses "
                        "column A: =RAND(), column B: =2+4*A2, column C: =RAND(), column D: =NORM.INV(C2,9,1.5), column E: =2*B2−D2. "
                        "The first rows are:\n"
                        "A 0.8050 | B 5.220 | C 0.8673 | D 10.670 | E −0.230\n"
                        "A 0.8079 | B 5.232 | C 0.0564 | D 6.621 | E 3.843\n"
                        "A 0.5153 | B 4.061 | C 0.5215 | D 9.081 | E −0.958\n"
                        "Over 1000 rows, E > 0 in 377 rows; the mean of column E is −1.042 and its SD is 2.741.\n"
                        "(a) Explain why columns B and D simulate X and Y.\n"
                        "(b) Estimate P(2X − Y > 0) and give its standard error.\n"
                        "(c) Use exact results to check the simulated mean and SD of 2X − Y.\n"
                        "(d) Explain why P(2X − Y > 0) cannot be found from these exact results by the usual Normal method.",
            "steps": [
                "(a) A2 ~ U(0, 1), so 2 + 4 × A2 is uniform on [2, 6]. NORM.INV(C2, 9, 1.5) is the value d with P(Y ≤ d) = C2; since C2 is "
                "uniform, D2 has the N(9, 1.5²) distribution (inverse cdf method). Using separate RAND() cells makes X and Y independent.",
                "Check row 1: 2 + 4 × 0.8050 = 5.220 and 2 × 5.220 − 10.670 = −0.230 ✓.",
                "(b) p̂ = 377/1000 = 0.377. SE = √(0.377 × 0.623/1000) = 0.0153 (3 s.f.).",
                "(c) E(X) = 4, Var(X) = (6 − 2)²/12 = 4/3. E(2X − Y) = 2 × 4 − 9 = −1.",
                "Var(2X − Y) = 4 × 4/3 + 2.25 = 7.583, so SD = 2.754. The simulated values −1.042 and 2.741 agree well, which gives confidence in the spreadsheet.",
                "(d) 2X − Y is the sum of a uniform and a Normal variable, so it is not Normally distributed. Its exact distribution is hard "
                "to find at this level, which is why simulation is used. (Numerical integration gives the exact value 0.3766, well within one SE of the estimate.)",
            ],
        },
        {
            "title": "Investigating the CLT: waiting for trains",
            "question": "Trains run every 12 minutes. A commuter arrives at random, so each wait W ~ U(0, 12). Her total waiting time "
                        "over 20 independent journeys is T. A spreadsheet simulates 1000 values of T. Output:\n"
                        "Mean of T = 119.44 | SD of T = 15.89 | Number of T > 140: 103\n"
                        "Normal probability plot of the 1000 values: close to a straight line. K–S test: p = 0.906\n"
                        "(a) Find E(T) and SD(T) exactly and compare with the simulation.\n"
                        "(b) Use the CLT to estimate P(T > 140), and compare with the simulated estimate.\n"
                        "(c) What do the plot and the K–S output show?",
            "steps": [
                "(a) E(W) = 6, Var(W) = 12²/12 = 12. So E(T) = 20 × 6 = 120 and Var(T) = 20 × 12 = 240, SD(T) = √240 = 15.49.",
                "The simulated mean 119.44 and SD 15.89 are close to these.",
                "(b) By the CLT, T ≈ N(120, 240). P(T > 140) ≈ P(Z > 20/15.49) = P(Z > 1.291) = 0.0984 (3 s.f.).",
                "Simulation: 103/1000 = 0.103, with SE √(0.103 × 0.897/1000) ≈ 0.0096. The difference 0.0046 is less than one SE, so the two agree.",
                "(c) The straight plot and p = 0.906 > 0.05 show that a Normal model for T is reasonable, even though each W is uniform. "
                "This illustrates the CLT: a sum of 20 independent identically distributed variables is approximately Normal.",
            ],
        },
    ],

    "practice": [
        "Eight values in order are 3.1, 3.8, 4.0, 4.4, 4.5, 4.9, 5.3, 6.6. (a) Find the eight Normal scores Φ⁻¹((i − 0.5)/8) used in a "
        "Normal probability plot. (b) The mean is 4.575 and s = 1.061. Where does the line x = x̄ + sz lie at the largest Normal score? "
        "Comment on the largest value.",

        "Normal probability plots are drawn with the data on the vertical axis. State what each pattern suggests: (a) the points curve "
        "upwards, flat at the left and steep at the right; (b) the points lie on a line except one point far below it at the left; "
        "(c) the points form an S shape that is flat at both ends; (d) the points curve downwards, steep at the left and flat at the right.",

        "A K–S test of normality on 25 measurements of reaction time gives p = 0.003. (a) State the null hypothesis. (b) Interpret the "
        "result at the 5% level. (c) What does this mean for a t-test on the mean reaction time?",

        "A K–S test on a sample of 8 values gives p = 0.41. A student writes: \"This proves the data come from a Normal distribution, "
        "so the t-test is valid.\" Give two criticisms.",

        "Software output for a test of correlation between hours of revision and test score for 25 students: r = 0.412, p-value "
        "(two-tailed) = 0.0407. (a) Test H₀: ρ = 0 against H₁: ρ ≠ 0 at the 5% level. (b) Test H₀: ρ = 0 against H₁: ρ > 0 at the 1% level. "
        "(c) Using the guideline 0.1 small, 0.3 medium, 0.5 large, describe the effect size (see Unit AS9).",

        "Software output for a χ² test on a 3 × 3 contingency table: Chi-squared = 11.87, p-value = 0.0183. (a) State the degrees of "
        "freedom. (b) Interpret the result at the 5% and the 1% levels. (c) Confirm the 5% conclusion using the critical value.",

        "Software gives a 95% confidence interval for the mean length μ cm of a component as (12.31, 14.07). (a) Find the sample mean and "
        "the margin of error. (b) At the 5% level, test H₀: μ = 14 against H₁: μ ≠ 14. (c) At the 5% level, test H₀: μ = 12 against H₁: μ ≠ 12.",

        "Write spreadsheet formulas, using RAND() or RANDBETWEEN, to simulate one value of each of: (a) a score from the discrete uniform "
        "distribution on {4, 5, 6, 7, 8, 9}; (b) X ~ U(3, 8); (c) Y ~ N(50, 4²); (d) a trial that succeeds with probability 0.3 (1 = success).",

        "A simulation with 500 repetitions estimates a probability as 0.212. (a) Find the standard error of the estimate. (b) Give an "
        "approximate range within which the true probability is likely to lie. (c) Roughly how many repetitions are needed for a standard error of at most 0.01?",

        "Four values of RAND() are 0.731, 0.052, 0.918, 0.402. Convert each into (a) a die score using INT(6*RAND())+1; (b) a value of "
        "U(2, 5) using 2+3*RAND(); (c) a value of N(20, 3²) using NORM.INV(RAND(),20,3), to 2 d.p.",

        "Software output for a one-sample t-test of H₀: μ = 60 on 15 observations: Mean = 63.2, t = 2.31, DF = 14, P-value (two-tailed) = 0.0366. "
        "(a) Interpret this for H₁: μ ≠ 60 at the 5% level. (b) Find the p-value for H₁: μ > 60, and interpret it at the 1% level. "
        "(c) What would the p-value be for H₁: μ < 60?",

        "A Wilcoxon signed-rank test of H₀: population median = 25 on 15 values (no zero differences) gives W+ = 92, W− = 28, P-value "
        "(two-tailed) = 0.0730. (a) Check the values of W+ and W− are consistent. (b) Interpret the result for a two-tailed test at 5%. "
        "(c) Interpret it for H₁: median > 25 at 5%, and confirm using Table 20. (d) State the assumption needed about the population.",
    ],

    "answers": [
        "(a) ±0.157, ±0.489, ±0.887, ±1.534 (i.e. −1.534, −0.887, −0.489, −0.157, 0.157, 0.489, 0.887, 1.534). "
        "(b) 4.575 + 1.061 × 1.534 = 6.20; the largest value 6.6 lies above the line, more than the other points, so it may be "
        "a slightly large value (a hint of an upper tail or outlier), but with n = 8 this is weak evidence.",

        "(a) Positive (right) skew. (b) A low outlier; check it for an error. (c) Lighter tails than Normal, e.g. uniform. (d) Negative (left) skew.",

        "(a) H₀: reaction times are Normally distributed (the population is Normal). (b) 0.003 < 0.05: reject H₀; there is strong "
        "evidence that reaction times are not Normally distributed. (c) The t-test assumes a Normal population; with n = 25 (not large) "
        "it may not be valid. Consider a non-parametric test such as Wilcoxon, or a transformation.",

        "Not rejecting H₀ does not prove it: the data are only consistent with a Normal model. With n = 8 the K–S test has low power, "
        "so it would often fail to detect non-normality; the Normal probability plot should also be examined.",

        "(a) 0.0407 < 0.05: reject H₀; there is sufficient evidence of correlation between revision and score. "
        "(b) r > 0 so one-tailed p = 0.0204 > 0.01: do not reject H₀; insufficient evidence at 1% of positive correlation. "
        "(c) 0.412 is between 0.3 and 0.5: a medium effect.",

        "(a) ν = (3 − 1)(3 − 1) = 4. (b) 5%: 0.0183 < 0.05, reject H₀: evidence of association. 1%: 0.0183 > 0.01, do not reject H₀: "
        "insufficient evidence of association. (c) χ²₄ upper 5% point = 9.488; 11.87 > 9.488 so reject H₀ ✓.",

        "(a) x̄ = (12.31 + 14.07)/2 = 13.19 cm; margin = (14.07 − 12.31)/2 = 0.88 cm. (b) 14 is inside the interval: do not reject H₀; "
        "insufficient evidence that μ ≠ 14. (c) 12 is outside the interval: reject H₀; sufficient evidence that μ ≠ 12.",

        "(a) =RANDBETWEEN(4,9) or =INT(6*RAND())+4. (b) =3+5*RAND(). (c) =NORM.INV(RAND(),50,4). (d) =IF(RAND()<0.3,1,0).",

        "(a) SE = √(0.212 × 0.788/500) = 0.0183. (b) About 0.212 ± 2 × 0.0183, i.e. roughly 0.175 to 0.249. "
        "(c) N ≥ 0.212 × 0.788/0.01² = 1670.6, so about 1700 repetitions (at least 1671).",

        "(a) 5, 1, 6, 3. (b) 4.193, 2.156, 4.754, 3.206. (c) 21.85, 15.12, 24.18, 19.26.",

        "(a) 0.0366 < 0.05: reject H₀; sufficient evidence that μ ≠ 60. (b) x̄ > 60, so p = 0.0366/2 = 0.0183 > 0.01: do not reject H₀; "
        "insufficient evidence at 1% that μ > 60. (c) The sample lies on the wrong side for H₁: μ < 60, so p = 1 − 0.0183 = 0.982; no evidence at all for H₁.",

        "(a) W+ + W− = 92 + 28 = 120 = 15 × 16/2 ✓. (b) 0.0730 > 0.05: do not reject H₀; insufficient evidence that the median differs from 25. "
        "(c) W+ > W− so the data lean towards median > 25; one-tailed p = 0.0365 < 0.05: reject H₀; evidence that the median is greater "
        "than 25. Table 20, n = 15, 5% one-tailed: critical value 30; T = W− = 28 ≤ 30 ✓. (d) The population is symmetric.",
    ],

    "exam": [
        "A manufacturer claims that the mean lifetime of its batteries is more than 40 hours. A consumer group tests a random sample of "
        "15 batteries. The Normal probability plot of the lifetimes is close to a straight line. Software output:\n"
        "Kolmogorov–Smirnov test for normality: p = 0.808\n"
        "One-sample t test | H₀: μ = 40\n"
        "n = 15 | Mean = 41.553 | SD = 3.040 | SE Mean = 0.785\n"
        "t = 1.979 | DF = 14 | P-value (two-tailed) = 0.0678\n"
        "95% CI for μ: (39.87, 43.24)\n"
        "(a) Explain how a Normal probability plot is constructed, and what a straight line indicates. [2]\n"
        "(b) Interpret the K–S output, stating the hypotheses. [2]\n"
        "(c) Test the manufacturer's claim at the 5% level. [4]\n"
        "(d) A member of the group says: \"40 is inside the 95% confidence interval, so the test in (c) cannot be significant.\" Explain why this is wrong. [2]\n"
        "(e) Explain why a t distribution is used rather than a Normal distribution. [1]",

        "A garden designer models rectangular plots with length X m and width Y m, where X ~ U(4, 10) and Y ~ N(6, 1²), independently. "
        "She wants P(XY > 50), the probability that a plot has area more than 50 m². She sets up a spreadsheet with columns\n"
        "A: =RAND() | B: =4+6*A2 | C: =RAND() | D: =NORM.INV(C2,6,1) | E: =B2*D2 | F: =IF(E2>50,1,0)\n"
        "and copies them down 1000 rows. In the first run the sum of column F is 273 and the mean of column E is 41.95. A second run gives a sum of 264.\n"
        "(a) Explain why columns B and D give values of X and Y. [2]\n"
        "(b) Explain why simulation is used here. [1]\n"
        "(c) Estimate P(XY > 50) from the first run, and find its standard error. [3]\n"
        "(d) Explain why the second run gives a different value, and give the best estimate from both runs. [2]\n"
        "(e) Find E(XY) exactly and compare with the simulation. [2]\n"
        "(f) Estimate how many repetitions are needed for the standard error to be at most 0.005. [2]",

        "A coach records the times of 12 runners over 5 km before and after a training programme. For each runner, "
        "d = (time before) − (time after), in seconds. The differences are\n"
        "−14.0, 1.0, 2.0, 2.2, 3.2, 3.7, 3.8, 4.2, 4.6, 4.7, 5.3, 5.9.\n"
        "Software output:\n"
        "K–S test for normality of d: p = 0.123\n"
        "Paired t test | H₀: μ<sub>d</sub> = 0 | Mean = 2.217 | SD = 5.300 | t = 1.449 | DF = 11 | P-value (two-tailed) = 0.1753\n"
        "Wilcoxon signed-rank test | H₀: median d = 0 | W+ = 66 | W− = 12 | P-value (two-tailed) = 0.0342\n"
        "(a) Explain why a paired analysis is appropriate. [1]\n"
        "(b) Describe what the Normal probability plot of d would show, and comment on the K–S p-value. [3]\n"
        "(c) Use the t-test output to test, at the 5% level, whether the programme reduces mean time. [3]\n"
        "(d) Use the Wilcoxon output to carry out the corresponding test at the 5% level, stating the assumption required. [3]\n"
        "(e) The coach later learns that the runner with d = −14.0 was injured. Advise the coach. [2]",

        "A random variable is simulated in a spreadsheet by X = 10*RAND()^2, so X = 10U² where U ~ U(0, 1).\n"
        "(a) Show that E(X) = 10/3 and Var(X) = 80/9. [4]\n"
        "500 samples of size n are simulated for n = 1, 5 and 30, and the mean of each sample is calculated. Output for the 500 sample means:\n"
        "n = 1: mean 3.301, SD 2.999, K–S p < 0.001, number of means > 4: 188\n"
        "n = 5: mean 3.343, SD 1.322, K–S p = 0.226, number of means > 4: 150\n"
        "n = 30: mean 3.337, SD 0.562, K–S p = 0.824, number of means > 4: 60\n"
        "(b) Compare the SDs with the theory. [3]\n"
        "(c) Interpret the K–S p-values. For n = 1 the Normal probability plot curves upwards; describe the shape of the distribution of X. [3]\n"
        "(d) For n = 30, compare the simulated estimate of P(X̄ > 4) with the value given by the Central Limit Theorem. [2]",
    ],

    "exam_answers": [
        "(a) Order the data; plot each x₍ᵢ₎ against the Normal score Φ⁻¹((i − 0.5)/n) B1. Points close to a straight line indicate "
        "that a Normal model is reasonable B1.\n"
        "(b) H₀: lifetimes are Normally distributed; H₁: they are not B1. p = 0.808 > 0.05: do not reject H₀; a Normal model is "
        "reasonable (consistent with the plot) B1.\n"
        "(c) μ = population mean lifetime (h). H₀: μ = 40, H₁: μ > 40 B1. x̄ > 40 so one-tailed p = 0.0678/2 = 0.0339 M1 A1. "
        "0.0339 < 0.05: reject H₀; there is sufficient evidence at the 5% level that the mean lifetime is more than 40 hours, "
        "supporting the claim A1.\n"
        "(d) A 95% two-sided CI corresponds to a two-tailed 5% test (2.5% in each tail) B1; the test in (c) is one-tailed at 5%, "
        "so it can be significant even though 40 is inside the interval (it would correspond to a 90% CI) B1.\n"
        "(e) σ is unknown and estimated by s from a small sample (from a Normal population) B1.",

        "(a) A2 ~ U(0, 1), so 4 + 6A2 is uniform on [4, 10] B1. NORM.INV(C2, 6, 1) is the inverse Normal cdf of a "
        "uniform random number, so has the N(6, 1²) distribution; separate RAND() cells give independence B1.\n"
        "(b) XY is a product of a uniform and a Normal variable, whose distribution is too hard to find exactly B1.\n"
        "(c) p̂ = 273/1000 = 0.273 B1. SE = √(0.273 × 0.727/1000) M1 = 0.0141 A1.\n"
        "(d) The random numbers are different in each run, so the estimate varies from run to run B1. Combined: "
        "(273 + 264)/2000 = 537/2000 = 0.2685 (0.269) B1. (Exact value, by integration: 0.2700.)\n"
        "(e) X and Y independent: E(XY) = E(X)E(Y) = 7 × 6 = 42 M1. The simulated mean 41.95 is very close A1.\n"
        "(f) √(0.27 × 0.73/N) ≤ 0.005 M1, so N ≥ 0.27 × 0.73/0.000025 = 7884: about 8000 repetitions A1.",

        "(a) Each runner is measured twice, so the before and after times are not independent; differences remove "
        "variation between runners B1.\n"
        "(b) Eleven points lie close to a straight line, with one point (−14.0) far below the line at the left B1 (a low outlier). "
        "p = 0.123 > 0.05, so the K–S test does not reject normality B1, but with n = 12 the test has low power; the outlier "
        "makes the Normal assumption doubtful B1.\n"
        "(c) H₀: μ<sub>d</sub> = 0, H₁: μ<sub>d</sub> > 0 (μ<sub>d</sub> = population mean of before − after) B1. Mean 2.217 > 0, so one-tailed p = 0.1753/2 = 0.0877 M1. "
        "0.0877 > 0.05: do not reject H₀; insufficient evidence that the programme reduces mean time A1.\n"
        "(d) H₀: population median of d = 0, H₁: median > 0 B1. W+ > W−, one-tailed p = 0.0342/2 = 0.0171 < 0.05: reject H₀; "
        "evidence that the programme reduces times B1. (Table 20, n = 12, 5% one-tailed: 17; T = 12 ≤ 17 ✓.) "
        "Assumes the distribution of differences is symmetric B1.\n"
        "(e) The outlier inflates the SD (5.300) and lowers the mean, which is why the t-test is not significant B1. "
        "Since it has a known cause unrelated to the programme, the coach could remove it and re-analyse: the other 11 "
        "differences are all positive, with mean 3.69 and t = 8.23, strong evidence of improvement; or rely on the Wilcoxon test, "
        "which is less affected by the outlier B1.",

        "(a) E(X) = 10E(U²) = 10∫₀¹ u² du = 10/3 M1 A1. E(X²) = 100E(U⁴) = 100∫₀¹ u⁴ du = 20 M1. "
        "Var(X) = 20 − (10/3)² = 20 − 100/9 = 80/9 A1.\n"
        "(b) σ = √(80/9) = 2.981; theory SD of X̄ = σ/√n: n = 1: 2.981, n = 5: 1.333, n = 30: 0.544 M1 A1. Simulated 2.999, 1.322, "
        "0.562 are close in each case; the means are all close to 3.333 B1.\n"
        "(c) n = 1: p < 0.001, strong evidence that X is not Normal B1; the upward curve shows X is positively skewed (long upper tail) B1. "
        "n = 5 and n = 30: p > 0.05, Normal not rejected; the larger p for n = 30 fits the CLT: X̄ becomes closer to Normal as n increases B1.\n"
        "(d) Simulated: 60/500 = 0.12 B1. CLT: X̄ ≈ N(10/3, (80/9)/30), P(X̄ > 4) = P(Z > (4 − 3.333)/0.5443) = P(Z > 1.225) = 0.110; "
        "close, the difference being within sampling variation (SE ≈ 0.015) B1.",
    ],
}
