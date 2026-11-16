"""Unit AS6: Hypothesis tests for binomial and Poisson parameters (expands the checked draft u08)."""

PO4_TABLE = [
    # x, P(X = x), P(X <= x), P(X >= x) for X ~ Po(4)
    ["0", "0.0183", "0.0183", "1.0000"],
    ["1", "0.0733", "0.0916", "0.9817"],
    ["2", "0.1465", "0.2381", "0.9084"],
    ["3", "0.1954", "0.4335", "0.7619"],
    ["4", "0.1954", "0.6288", "0.5665"],
    ["5", "0.1563", "0.7851", "0.3712"],
    ["6", "0.1042", "0.8893", "0.2149"],
    ["7", "0.0595", "0.9489", "0.1107"],
    ["8", "0.0298", "0.9786", "0.0511"],
    ["9", "0.0132", "0.9919", "0.0214"],
    ["10", "0.0053", "0.9972", "0.0081"],
]

UNIT = {
    "number": "AS6",
    "title": "Hypothesis tests: binomial and Poisson",
    "tag": "AS · Edexcel FS1 (AS 2.4, A level 4.1), AQA SB5 and SC1 (Type I errors) · binomial tests are prior knowledge "
           "from A level Mathematics for every board; useful revision for IAL S3, OCR A, OCR MEI and CAIE 9231",
    "notes": [
        ("p", "A hypothesis test uses sample evidence to decide between two statements about a population parameter. In "
              "single Mathematics you met tests for a binomial proportion p. Further Mathematics adds tests for the mean λ "
              "of a Poisson distribution, more careful use of critical regions and actual significance levels, and the "
              "probability of making a wrong decision. Everything here uses exact binomial or Poisson probabilities from "
              "a calculator or tables."),

        ("h2", "6.1 The language of hypothesis tests"),
        ("bullets", [
            "<b>Parameter</b>: the population quantity being tested, e.g. the probability p of a success, or the mean "
            "number λ of events per interval. Always define it in context.",
            "<b>Null hypothesis H₀</b>: the parameter takes a particular value, e.g. H₀: λ = 4. It is assumed true while the test is carried out.",
            "<b>Alternative hypothesis H₁</b>: the parameter has changed. A <b>one-tailed</b> test uses H₁: λ > 4 or H₁: λ < 4; "
            "a <b>two-tailed</b> test uses H₁: λ ≠ 4. The choice must come from the question, before looking at the data.",
            "<b>Test statistic</b>: the quantity calculated from the sample to test H₀, here the observed number of successes "
            "or events X. Its distribution assuming H₀ is true is the <b>null distribution</b>.",
            "<b>Significance level α</b>: the threshold probability for rejecting H₀ (e.g. 5%). It is the largest probability "
            "of rejecting H₀ when it is true that you are prepared to accept.",
            "<b>Critical region</b> (rejection region): the values of the test statistic that lead to rejecting H₀. The first "
            "value in it is the <b>critical value</b>. The other values form the <b>acceptance region</b>.",
            "<b>Actual significance level</b>: the true probability of the test statistic falling in the critical region when "
            "H₀ is true. For discrete distributions it is usually less than α.",
            "<b>p-value</b>: the probability, assuming H₀ is true, of a result at least as extreme as the one observed (in the "
            "direction of H₁). Reject H₀ if the p-value ≤ α.",
        ]),
        ("box", "The steps of every test", [
            "1. Define the parameter in context (e.g. λ = mean number of calls per hour).",
            "2. State H₀ and H₁ in terms of the parameter, and the significance level.",
            "3. State the distribution of the test statistic under H₀, e.g. X ~ Po(4).",
            "4. Either find the p-value P(X ≥ x) or P(X ≤ x), or find the critical region.",
            "5. Compare: p-value with α (or with α/2 in each tail for a two-tailed test), or observed value with the critical region.",
            "6. Conclude in context, without certainty: \"There is sufficient evidence at the 5% level to suggest that the mean "
            "number of calls per hour has decreased.\"",
        ]),

        ("h2", "6.2 Binomial tests (recap from A level Mathematics)"),
        ("p", "If X is the number of successes in n independent trials, each with probability p of success, then under "
              "H₀: p = p₀ the test statistic is X ~ B(n, p₀). For H₁: p > p₀, large values of X are evidence against H₀, so "
              "the p-value is P(X ≥ x). For H₁: p < p₀ it is P(X ≤ x). Cumulative tables give P(X ≤ x), so use "
              "P(X ≥ x) = 1 − P(X ≤ x − 1)."),

        ("h2", "6.3 Testing the mean of a Poisson distribution (Edexcel AS 2.4 and A level 4.1; AQA SB5)"),
        ("p", "If events occur singly, independently and at a constant average rate, the number X of events in a fixed "
              "interval is Poisson. To test whether the rate has changed, take a single observation of X and test "
              "H₀: λ = λ₀, where λ is the mean number of events in that interval. Under H₀, X ~ Po(λ₀)."),
        ("box", "Scaling λ and combining observations", [
            "If events occur at a mean rate of λ per unit, then the number in t units is Po(λt). Example: 2.5 per week gives "
            "Po(10) for 4 weeks. Always use the distribution for the interval that was actually observed.",
            "If X ~ Po(λ) and Y ~ Po(μ) are independent, then X + Y ~ Po(λ + μ) (Edexcel 2.1, AQA SB4). So the total of n "
            "independent observations from Po(λ) is Po(nλ), and two independent sources of events can be combined.",
            "Hypotheses may be written in terms of the rate per unit (H₀: λ = 2.5 per week) even when the test uses Po(10).",
        ]),

        ("h2", "6.4 Critical regions and the actual significance level"),
        ("p", "Because X is discrete, you usually cannot find a critical region with probability exactly α. For a one-tailed "
              "test at level α choose the largest region whose probability under H₀ does not exceed α. The table shows "
              "X ~ Po(4)."),
        ("table", ["x", "P(X = x)", "P(X ≤ x)", "P(X ≥ x)"], PO4_TABLE),
        ("bullets", [
            "Upper tail at 5% (H₁: λ > 4): P(X ≥ 9) = 0.0214 ≤ 0.05 but P(X ≥ 8) = 0.0511 > 0.05. Critical region X ≥ 9; "
            "critical value 9; actual significance level 0.0214.",
            "Lower tail at 5% (H₁: λ < 4): P(X ≤ 0) = 0.0183 ≤ 0.05 but P(X ≤ 1) = 0.0916 > 0.05. Critical region X = 0; "
            "actual significance level 0.0183.",
            "Two-tailed at 5%: put at most 2.5% in each tail. Lower: X = 0 (0.0183). Upper: P(X ≥ 10) = 0.0081, "
            "P(X ≥ 9) = 0.0214, so X ≥ 9. Critical region X = 0 or X ≥ 9; actual significance level 0.0183 + 0.0214 = 0.0397.",
        ]),
        ("p", "Some questions ask instead for a tail probability \"as close as possible to\" a given value. Then compare the two "
              "candidates on either side and take the closer one, even if it is slightly above the target. Read the wording carefully."),

        ("h2", "6.5 p-values and two-tailed tests"),
        ("p", "The p-value is computed in the direction of H₁ only. In a two-tailed test, first decide which tail the observation "
              "is in (compare x with the mean under H₀), find that one tail probability, and compare it with α/2. "
              "(Equivalently, double it and compare with α.) A smaller p-value means stronger evidence against H₀: if the "
              "p-value is 0.03, the result is significant at 5% but not at 1%."),

        ("h2", "6.6 Type I and Type II errors (AQA SC1; Edexcel)"),
        ("table", ["", "H₀ is true", "H₀ is false"], [
            ["Reject H₀", "Type I error", "Correct decision"],
            ["Do not reject H₀", "Correct decision", "Type II error"],
        ]),
        ("box", "Probability of a Type I error", [
            "A Type I error is rejecting H₀ when H₀ is true. A Type II error is not rejecting H₀ when H₀ is false.",
            "P(Type I error) = P(test statistic in critical region | H₀ true) = the actual significance level.",
            "For the Po(4) upper-tail test above, P(Type I error) = P(X ≥ 9 | λ = 4) = 0.0214, not 0.05.",
            "P(Type II error) needs a particular value of the parameter under H₁; this, and the power of a test, are in unit A2.5.",
        ]),
        ("p", "Define errors in context: for a test of H₀: λ = 4 calls per hour against H₁: λ > 4, a Type I error is concluding "
              "that the call rate has increased when in fact it is still 4 per hour."),
        ("warn", "Common mistakes", [
            "Using P(X = x) instead of the tail probability P(X ≥ x) or P(X ≤ x). The p-value includes everything more extreme.",
            "Computing P(X ≥ x) as 1 − P(X ≤ x). It is 1 − P(X ≤ x − 1).",
            "Using the wrong interval: a rate of 2.5 per week tested over 4 weeks needs Po(10), not Po(2.5).",
            "Comparing a one-tail probability with α in a two-tailed test. Each tail gets α/2.",
            "Writing hypotheses with x̄, X or a number instead of the parameter: write H₀: λ = 4, not H₀: X = 4.",
            "Over-certain conclusions such as \"this proves the rate has increased\", or no context at all. Say \"there is "
            "(in)sufficient evidence to suggest…\", and do not say H₀ is accepted as true.",
            "Quoting the significance level as the probability of a Type I error when the distribution is discrete. Give the "
            "actual significance level.",
        ]),
    ],
    "examples": [
        {
            "title": "Binomial test with a p-value",
            "question": "A café owner believes that 25% of customers buy a cake with their coffee. After a new display is installed, "
                        "9 of a random sample of 20 customers buy a cake. Test, at the 5% level, whether the proportion has increased.",
            "steps": [
                "Let p = the proportion of all customers who buy a cake. H₀: p = 0.25, H₁: p > 0.25. Significance level 5%.",
                "Let X = number in the sample who buy a cake. Under H₀, X ~ B(20, 0.25).",
                "p-value = P(X ≥ 9) = 1 − P(X ≤ 8) = 1 − 0.9591 = 0.0409.",
                "0.0409 < 0.05, so reject H₀.",
                "There is sufficient evidence at the 5% level to suggest that the proportion of customers buying a cake has increased.",
            ],
        },
        {
            "title": "Lower-tail Poisson test and the critical region",
            "question": "Calls to a helpline arrive at a mean rate of 4 per hour. After a change to the website, 1 call arrives in a "
                        "randomly chosen hour. (a) Find the critical region for a test at the 5% level of whether the rate has "
                        "fallen, and state its actual significance level. (b) Carry out the test.",
            "steps": [
                "(a) Let λ = mean number of calls per hour. H₀: λ = 4, H₁: λ < 4. Under H₀, X ~ Po(4).",
                "P(X = 0) = e⁻⁴ = 0.0183 ≤ 0.05, but P(X ≤ 1) = 5e⁻⁴ = 0.0916 > 0.05.",
                "Critical region: X = 0. Actual significance level 0.0183 (1.83%).",
                "(b) The observed value 1 is not in the critical region, so do not reject H₀. There is insufficient evidence at the "
                "5% level to suggest that the mean number of calls per hour has fallen.",
            ],
        },
        {
            "title": "Scaling the Poisson mean",
            "question": "A shop sells a mean of 1.5 telescopes per week. After an advertising campaign it sells 15 telescopes in 6 weeks. "
                        "Test, at the 5% level, whether the mean weekly sales have increased. State any assumption you make.",
            "steps": [
                "Let λ = mean number of telescopes sold per week. H₀: λ = 1.5, H₁: λ > 1.5.",
                "Assume sales occur singly, independently and at a constant rate, so the number Y sold in 6 weeks is Poisson.",
                "Under H₀, Y ~ Po(6 × 1.5) = Po(9).",
                "p-value = P(Y ≥ 15) = 1 − P(Y ≤ 14) = 1 − 0.9585 = 0.0415 < 0.05, so reject H₀.",
                "There is sufficient evidence at the 5% level to suggest that the mean weekly sales of telescopes have increased.",
            ],
        },
        {
            "title": "Two-tailed critical region",
            "question": "The number of emergency call-outs a garage receives per day has a Poisson distribution with mean 8. Find the "
                        "critical region for a two-tailed test of H₀: λ = 8 at the 5% level, with the probability in each tail "
                        "not exceeding 2.5%. State the actual significance level.",
            "steps": [
                "Under H₀, X ~ Po(8). Each tail must have probability ≤ 0.025.",
                "Lower tail: P(X ≤ 2) = 0.0138 ≤ 0.025, but P(X ≤ 3) = 0.0424 > 0.025, so X ≤ 2.",
                "Upper tail: P(X ≥ 15) = 1 − P(X ≤ 14) = 1 − 0.9827 = 0.0173 ≤ 0.025, but P(X ≥ 14) = 0.0342 > 0.025, so X ≥ 15.",
                "Critical region: X ≤ 2 or X ≥ 15.",
                "Actual significance level = P(X ≤ 2) + P(X ≥ 15) = 0.0310 to 4 d.p. (about 3.1%). Adding the rounded values 0.0138 + 0.0173 gives 0.0311, which is also acceptable.",
            ],
        },
        {
            "title": "Probability of a Type I error in a binomial test",
            "question": "A seed company claims that 40% of its seeds produce red flowers. A gardener plants 20 seeds to test the claim, "
                        "using a two-tailed test at the 10% level. (a) Find the critical region, with at most 5% in each tail. "
                        "(b) Find the probability of a Type I error, and describe a Type I error in context.",
            "steps": [
                "(a) Let p = the proportion of the company's seeds that produce red flowers. H₀: p = 0.4, H₁: p ≠ 0.4. Under H₀, X ~ B(20, 0.4).",
                "Lower: P(X ≤ 3) = 0.0160 ≤ 0.05, P(X ≤ 4) = 0.0510 > 0.05, so X ≤ 3.",
                "Upper: P(X ≥ 13) = 1 − P(X ≤ 12) = 1 − 0.9790 = 0.0210 ≤ 0.05, P(X ≥ 12) = 0.0565 > 0.05, so X ≥ 13.",
                "Critical region: X ≤ 3 or X ≥ 13.",
                "(b) P(Type I error) = P(X ≤ 3) + P(X ≥ 13) when p = 0.4, which is 0.0160 + 0.0210 = 0.0370.",
                "A Type I error is concluding that the proportion of red-flowered seeds is not 40% when in fact it is 40%.",
            ],
        },
        {
            "title": "Combining two Poisson sources (exam standard)",
            "question": "A machine has two kinds of breakdown. Electrical breakdowns occur at a mean rate of 1.2 per day and mechanical "
                        "breakdowns at a mean rate of 0.8 per day, independently. After a service, there are 4 breakdowns in "
                        "total in 5 days. Test, at the 5% level, whether the total breakdown rate has decreased.",
            "steps": [
                "Total breakdowns per day: Po(1.2) + Po(0.8) = Po(2.0), by the additive property for independent Poisson variables.",
                "Let λ = mean total number of breakdowns per day. H₀: λ = 2, H₁: λ < 2.",
                "Let T = total breakdowns in 5 days. Under H₀, T ~ Po(5 × 2) = Po(10).",
                "p-value = P(T ≤ 4) = 0.0293 < 0.05, so reject H₀.",
                "There is sufficient evidence at the 5% level to suggest that the mean total breakdown rate has decreased since the service.",
            ],
        },
    ],
    "practice": [
        "X ~ B(20, 0.3). Find the critical region for a test of H₀: p = 0.3 against H₁: p > 0.3 at the 5% level. Give the probabilities you use to 4 decimal places and state the actual significance level.",
        "A dice is thought to be biased towards 6. It is rolled 12 times and 6 appears 5 times. Test H₀: p = 1/6 against H₁: p > 1/6 at the 5% level, showing the probability you use.",
        "The number of faults per metre of cable has a Poisson distribution with mean 0.8. A 5 metre length of cable from a new supplier has 9 faults. Test, at the 5% level, whether the new supplier's cable has a higher fault rate.",
        "X ~ Po(5). Find the critical region for a test of H₀: λ = 5 against H₁: λ ≠ 5 at the 5% level, with at most 2.5% in each tail. State the actual significance level.",
        "Explain the difference between a Type I error and a Type II error in the context of a test of whether a coin is fair.",
        "A town has a mean of 6 burglaries a month. In the month after a police campaign there are 2 burglaries. Test, at the 5% level, whether the mean number of burglaries has fallen.",
        "A spinner is thought to land on red with probability 0.5. In 15 spins it lands on red 3 times. Test, at the 5% level, whether the spinner is biased.",
        "Cars arrive at a car park at a mean rate of 3 every 10 minutes. On a wet day, 4 cars arrive in 30 minutes. Test, at the 5% level, whether the arrival rate is lower on wet days.",
        "A test of H₀: λ = 2.5 against H₁: λ > 2.5 uses a single observation of X ~ Po(λ) at the 5% level. Find the critical region and the probability of a Type I error.",
        "A test of H₀: p = 0.5 against H₁: p < 0.5 uses X ~ B(10, p) at the 5% level. Find the critical region, and the probability of a Type I error as an exact fraction.",
        "In a test of H₀: λ = 3 against H₁: λ > 3 the observed value is 8. Find the p-value, and state at which of the significance levels 10%, 5%, 2% and 1% the result is significant.",
        "Explain why, for a test based on a Poisson or binomial distribution, the probability of a Type I error is usually less than the stated significance level.",
    ],
    "answers": [
        "Under H₀, X ~ B(20, 0.3). P(X ≥ 10) = 1 − 0.9520 = 0.0480 ≤ 0.05 and P(X ≥ 9) = 0.1133 > 0.05. Critical region X ≥ 10; actual significance level 0.0480.",
        "X ~ B(12, 1/6). P(X ≥ 5) = 0.0364 < 0.05, so reject H₀: there is sufficient evidence at the 5% level that the dice is biased towards 6. (P(X ≥ 4) = 0.1252 > 0.05, so 4 sixes would not have been significant.)",
        "λ = mean faults per metre; H₀: λ = 0.8, H₁: λ > 0.8. For 5 m, Y ~ Po(4). P(Y ≥ 9) = 1 − 0.9786 = 0.0214 < 0.05, so reject H₀. There is sufficient evidence that the new supplier's fault rate is higher than 0.8 per metre.",
        "Lower: P(X ≤ 0) = 0.0067 ≤ 0.025, P(X ≤ 1) = 0.0404 > 0.025, so X = 0. Upper: P(X ≥ 11) = 0.0137 ≤ 0.025, P(X ≥ 10) = 0.0318 > 0.025, so X ≥ 11. Critical region X = 0 or X ≥ 11; actual significance level 0.0067 + 0.0137 = 0.0204.",
        "A Type I error is concluding that the coin is biased when it is actually fair. A Type II error is concluding that there is no evidence of bias (not rejecting fairness) when the coin is actually biased.",
        "λ = mean burglaries per month; H₀: λ = 6, H₁: λ < 6. X ~ Po(6). P(X ≤ 2) = 0.0620 > 0.05, so do not reject H₀. There is insufficient evidence at the 5% level that the mean number of burglaries has fallen.",
        "p = P(red); H₀: p = 0.5, H₁: p ≠ 0.5. X ~ B(15, 0.5). 3 is below the mean 7.5, so find P(X ≤ 3) = 0.0176 < 0.025, so reject H₀. There is sufficient evidence at the 5% level that the spinner is biased.",
        "λ = mean arrivals per 10 minutes; H₀: λ = 3, H₁: λ < 3. In 30 minutes Y ~ Po(9). P(Y ≤ 4) = 0.0550 > 0.05, so do not reject H₀. Insufficient evidence at the 5% level that arrivals are lower on wet days.",
        "X ~ Po(2.5). P(X ≥ 6) = 1 − 0.9580 = 0.0420 ≤ 0.05 and P(X ≥ 5) = 0.1088 > 0.05. Critical region X ≥ 6; P(Type I error) = 0.0420.",
        "P(X ≤ 1) = 11/1024 = 0.0107 ≤ 0.05 and P(X ≤ 2) = 56/1024 = 0.0547 > 0.05. Critical region X ≤ 1; P(Type I error) = 11/1024.",
        "p-value = P(X ≥ 8 | λ = 3) = 1 − 0.9881 = 0.0119. Since 0.0119 ≤ 0.1, 0.05 and 0.02, the result is significant at 10%, 5% and 2%; since 0.0119 > 0.01, it is not significant at 1%.",
        "The test statistic takes only whole-number values, so the tail probabilities jump in steps. The critical region is chosen so that its probability under H₀ does not exceed α, and usually no region has probability exactly α, so P(Type I error) = P(critical region | H₀) is less than α.",
    ],
    "exam": [
        "Cars pass a checkpoint on a quiet road at a mean rate of 1.5 per minute.\n"
        "(a) State two conditions needed for the number of cars passing in a fixed time to be modelled by a Poisson distribution. [2]\n"
        "(b) Find the probability that in a randomly chosen minute (i) no cars pass, (ii) at least 3 cars pass. [3]\n"
        "After a new junction opens, a council officer wants to test whether the rate has changed, using the number of cars in a randomly chosen 5-minute period.\n"
        "(c) Find the critical region for a two-tailed test at the 5% level, with the probability in each tail as small as possible but not more than 2.5%. [4]\n"
        "(d) State the actual significance level of the test. [1]\n"
        "(e) 13 cars pass in the 5-minute period. Comment on this result. [2]",
        "Emails arrive in a company inbox at a mean rate of 3.5 per hour.\n"
        "(a) Find the probability that fewer than 5 emails arrive in a given hour. [2]\n"
        "The manager believes the rate has increased. She counts the emails in a randomly chosen 2-hour period and tests at the 5% level.\n"
        "(b) Write down suitable hypotheses, defining your parameter. [2]\n"
        "(c) Find the critical region. [3]\n"
        "(d) She counts 12 emails. State, with a reason, the conclusion of the test. [2]\n"
        "(e) Find the probability of a Type I error and describe a Type I error in this context. [2]",
        "A politician claims that 40% of voters support a new policy. A researcher asks a random sample of 25 voters.\n"
        "(a) Find the critical region for a two-tailed test of the claim at the 5% level, with each tail probability as small as possible but not more than 2.5%. [4]\n"
        "(b) Find the actual significance level of the test. [1]\n"
        "(c) 15 of the 25 voters support the policy. Find the p-value and state the conclusion in context. [3]\n"
        "(d) Explain why the conclusion would be unreliable if the sample was taken outside the politician's own office. [1]",
        "The number of faults in a day on a production line is the sum of type A faults, mean 0.6 per day, and type B faults, mean 0.4 per day, which occur independently and at random.\n"
        "(a) Write down the distribution of the total number of faults in a day, and find the probability of at least 3 faults in a day. [3]\n"
        "After maintenance, the manager records the total number of faults over 7 days to test, at the 5% level, whether the mean daily total has decreased.\n"
        "(b) Find the critical region for this test. [3]\n"
        "(c) There are 2 faults in the 7 days. Complete the test. [2]\n"
        "(d) Find the probability of a Type I error. [1]",
    ],
    "exam_answers": [
        "(a) Any two: cars pass singly (one at a time); independently of each other; at a constant mean rate (randomly in time) [B1 B1].\n"
        "(b) X ~ Po(1.5). (i) P(X = 0) = e^(−1.5) = 0.2231 [B1]. (ii) P(X ≥ 3) = 1 − P(X ≤ 2) [M1] = 1 − 0.8088 = 0.1912 [A1].\n"
        "(c) Y ~ Po(7.5) for 5 minutes [B1]. Lower: P(Y ≤ 2) = 0.0203, P(Y ≤ 3) = 0.0591, so Y ≤ 2 [M1 A1]. Upper: P(Y ≥ 14) = 0.0216, P(Y ≥ 13) = 0.0427, so Y ≥ 14. Critical region Y ≤ 2 or Y ≥ 14 [A1].\n"
        "(d) P(Y ≤ 2) + P(Y ≥ 14) = 0.0418 (0.0419 from the rounded values) [B1].\n"
        "(e) 13 is not in the critical region, so do not reject H₀ [M1]. There is insufficient evidence at the 5% level that the rate of cars has changed since the junction opened [A1].",
        "(a) X ~ Po(3.5): P(X ≤ 4) [M1] = 0.7254 [A1].\n"
        "(b) λ = mean number of emails per hour [B1]. H₀: λ = 3.5, H₁: λ > 3.5 [B1].\n"
        "(c) Y ~ Po(7) for 2 hours [B1]. P(Y ≥ 13) = 0.0270 ≤ 0.05 and P(Y ≥ 12) = 0.0533 > 0.05 [M1], so the critical region is Y ≥ 13 [A1].\n"
        "(d) 12 is not in the critical region [M1], so there is insufficient evidence at the 5% level that the rate of emails has increased [A1].\n"
        "(e) P(Type I) = P(Y ≥ 13 | λ = 3.5 per hour) = 0.0270 [B1]. Concluding that the email rate has increased when it is still 3.5 per hour [B1].",
        "(a) H₀: p = 0.4, H₁: p ≠ 0.4, where p is the proportion of all voters who support the policy; X ~ B(25, 0.4) [B1]. Lower: P(X ≤ 4) = 0.0095, P(X ≤ 5) = 0.0294, so X ≤ 4 [M1 A1]. Upper: P(X ≥ 16) = 0.0132, P(X ≥ 15) = 0.0344, so X ≥ 16. Critical region X ≤ 4 or X ≥ 16 [A1].\n"
        "(b) P(X ≤ 4) + P(X ≥ 16) = 0.0226 (0.0227 from the rounded values) [B1].\n"
        "(c) p-value = P(X ≥ 15) = 0.0344 [M1]; 0.0344 > 0.025 (or 15 not in the critical region) so do not reject H₀ [M1]. Insufficient evidence at the 5% level to doubt the claim that 40% of voters support the policy [A1].\n"
        "(d) The sample would not be random (people near the office are more likely to share his views), so it may be biased and the binomial model would not apply [B1].",
        "(a) Po(0.6 + 0.4) = Po(1) [B1]. P(X ≥ 3) = 1 − P(X ≤ 2) [M1] = 1 − 0.9197 = 0.0803 [A1].\n"
        "(b) H₀: λ = 1, H₁: λ < 1 (λ = mean faults per day); T ~ Po(7) for 7 days [B1]. P(T ≤ 2) = 0.0296 ≤ 0.05 and P(T ≤ 3) = 0.0818 > 0.05 [M1], so the critical region is T ≤ 2 [A1].\n"
        "(c) 2 is in the critical region, so reject H₀ [M1]. There is sufficient evidence at the 5% level that the mean daily number of faults has decreased since the maintenance [A1].\n"
        "(d) P(Type I error) = P(T ≤ 2 | λ = 1) = 0.0296 [B1].",
    ],
}
