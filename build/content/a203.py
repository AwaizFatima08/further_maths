UNIT = {
    "number": "A2.3",
    "title": "The negative binomial distribution and tests for a geometric parameter",
    "tag": "A level · Edexcel FS1 topics 3 and 4 (3.1, 3.3, 4.2; links to 4.1) · not on the other specifications · "
           "builds on AS3 (geometric) and AS6 (hypothesis tests)",
    "notes": [
        ("p", "The geometric distribution (unit AS3) counts the trials up to the first success. Waiting for the r-th success leads "
              "to the <b>negative binomial distribution</b>. This unit develops its probability function, mean and variance, and "
              "then uses a single geometric observation to test a claim about the probability of success p — Edexcel FS1 topic 4.2."),

        ("h2", "3.1 The negative binomial model"),
        ("p", "Independent trials are carried out, each a success with constant probability p. X is the number of trials <b>up to and "
              "including the r-th success</b>. Then X has a negative binomial distribution with parameters r and p. In this book we "
              "write X ~ NB(r, p); Edexcel questions usually describe the distribution in words. The geometric distribution is the "
              "special case r = 1."),
        ("p", "<b>Deriving the probability function.</b> For the r-th success to occur on trial x, two things must happen:"),
        ("bullets", [
            "trial x is a success (probability p), and",
            "the first x − 1 trials contain exactly r − 1 successes, a binomial probability C(x − 1, r − 1) p^(r−1) (1 − p)^(x−r).",
        ]),
        ("p", "These are independent, so multiply. Note that the binomial coefficient chooses positions only among the first x − 1 "
              "trials: the last trial is fixed as a success."),
        ("box", "Negative binomial NB(r, p): number of trials up to and including the r-th success", [
            "P(X = x) = C(x − 1, r − 1) pʳ (1 − p)^(x−r),   x = r, r + 1, r + 2, …",
            "E(X) = r/p,     Var(X) = r(1 − p)/p²",
            "The probability function and the mean and variance are in the Edexcel formulae booklet (with the PGF).",
        ]),
        ("p", "The name comes from the fact that these probabilities are the terms of the binomial expansion of pʳ(1 − q)^(−r), "
              "a binomial series with a negative index, where q = 1 − p."),

        ("h2", "3.2 Mean and variance: a sum of geometric variables"),
        ("p", "Split the trials into r stretches: Y₁ = trials up to and including the 1st success, Y₂ = further trials up to and "
              "including the 2nd success, and so on. Because the trials are independent and p is constant, each stretch starts "
              "afresh (the memoryless property), so Y₁, Y₂, …, Yᵣ are independent, each Geo(p), and X = Y₁ + Y₂ + … + Yᵣ."),
        ("bullets", [
            "E(X) = E(Y₁) + … + E(Yᵣ) = r × 1/p = r/p.",
            "Var(X) = Var(Y₁) + … + Var(Yᵣ) = r(1 − p)/p², using independence.",
            "Edexcel does not require a proof (spec 3.3), but this argument is a common 'explain' question. Unit A2.4 proves the "
            "results again with the PGF [pt/(1 − (1 − p)t)]ʳ, which is the PGF of Geo(p) raised to the power r.",
        ]),
        ("p", "From the two formulas, Var(X)/E(X) = (1 − p)/p, which lets you find p and then r from a given mean and variance."),

        ("h2", "3.3 Calculating probabilities"),
        ("p", "There are no tables for the negative binomial. Individual probabilities come from the formula. For cumulative "
              "probabilities, sum a few terms, or use this link with the binomial:"),
        ("box", "Link with the binomial", [
            "X > x  ⇔  fewer than r successes in the first x trials.",
            "So P(X > x) = P(Y ≤ r − 1), where Y ~ B(x, p), and P(X ≤ x) = P(Y ≥ r).",
            "For r = 1 this gives the geometric result P(X > x) = (1 − p)ˣ.",
        ]),
        ("p", "<b>Mode.</b> The ratio of successive probabilities is P(X = x + 1)/P(X = x) = x(1 − p)/(x − r + 1). This is at least 1 "
              "exactly when x ≤ (r − 1)/p, so the probabilities rise up to that point and then fall. If (r − 1)/p is an integer, "
              "two adjacent values share the highest probability."),

        ("h2", "3.4 Hypothesis tests for p in a geometric distribution (Edexcel 4.2)"),
        ("p", "A single observation x of X ~ Geo(p) can test a claim about p. The parameter is p, the probability of success on each "
              "trial. The key idea is the direction of the tail:"),
        ("table", ["Alternative hypothesis", "Evidence for H₁ is…", "Critical region", "Tail probability under H₀ (q₀ = 1 − p₀)"], [
            ["H₁: p < p₀", "a <b>long</b> wait: large x", "X ≥ c", "P(X ≥ c) = q₀^(c−1)"],
            ["H₁: p > p₀", "a <b>short</b> wait: small x", "X ≤ c", "P(X ≤ c) = 1 − q₀<sup>c</sup>"],
            ["H₁: p ≠ p₀", "either", "both tails, α/2 in each", "as above"],
        ]),
        ("box", "Steps for a geometric test", [
            "1. Define p in context and state H₀: p = p₀ and H₁ (one- or two-tailed).",
            "2. State the test statistic: X ~ Geo(p₀) under H₀.",
            "3. Either find the probability of a result at least as extreme as the observed x (the p-value) and compare with α, "
            "or find the critical region: the most extreme values whose total probability is as large as possible but ≤ α.",
            "4. Conclude in context, without certainty: 'There is (in)sufficient evidence at the 5% level to suggest that…'.",
            "The actual significance level is P(X in the critical region | H₀). It is usually below the nominal α because X is discrete.",
        ]),
        ("p", "<b>Finding a critical value with logarithms.</b> For H₁: p < p₀ we need q₀^(c−1) ≤ α, so c − 1 ≥ ln α/ln q₀ "
              "(the inequality reverses because ln q₀ < 0). Round c − 1 up to an integer. For H₁: p > p₀ we need 1 − q₀<sup>c</sup> ≤ α, so "
              "q₀<sup>c</sup> ≥ 1 − α and c ≤ ln(1 − α)/ln q₀; round c down."),
        ("p", "<b>A test that cannot reject.</b> The smallest possible critical region for H₁: p > p₀ is X = 1, with probability p₀. "
              "If p₀ > α there is no critical region at all in that tail: even an immediate success is not strong evidence that p "
              "has increased. This often happens in two-tailed tests, where only α/2 is available in each tail."),

        ("h2", "3.5 Links with other tests"),
        ("bullets", [
            "<b>Poisson mean (Edexcel 4.1, unit AS6).</b> The same logic applies: H₁: λ > λ₀ uses the upper tail P(X ≥ x), "
            "H₁: λ < λ₀ the lower tail P(X ≤ x), with probabilities from Poisson tables. Note the direction is the opposite way round "
            "from the geometric test: a larger rate gives <i>more</i> events, but a larger p gives a <i>shorter</i> wait.",
            "<b>Negative binomial.</b> The Edexcel specification only names geometric tests, but the method works for a negative "
            "binomial observation too, using the binomial link to find tail probabilities.",
            "<b>Quality of tests (A2.5).</b> The probability of a Type I error is the actual significance level. The power of a "
            "geometric test against a particular value p₁ is P(X in the critical region | p = p₁).",
        ]),
        ("warn", "Common mistakes", [
            "Using C(x, r) or C(x − 1, r) instead of C(x − 1, r − 1): the last trial must be the r-th success.",
            "Writing E(X) = r(1 − p)/p or Var(X) = r/p². The mean is r/p; the variance has the extra factor (1 − p)/p.",
            "Getting the tail the wrong way round. A smaller p means waiting longer, so H₁: p < p₀ uses large values of X.",
            "Using P(X > x) = q<sup>x</sup> for the p-value instead of P(X ≥ x) = q^(x−1): the observed value belongs in the tail.",
            "Giving a critical region whose probability is just above α, or forgetting to state the actual significance level when asked.",
            "Concluding 'p has decreased' or 'H₀ is true'. Conclusions must be non-assertive and in context.",
        ]),
    ],
    "examples": [
        {
            "title": "Negative binomial probabilities, mean and variance",
            "question": "A basketball player scores each free throw with probability 0.6, independently. Find the probability that her "
                        "third score comes on her fifth throw, and the mean and variance of the number of throws needed for three scores.",
            "steps": [
                "X ~ NB(3, 0.6). P(X = 5) = C(4, 2)(0.6)³(0.4)² = 6 × 0.216 × 0.16 = 0.20736 ≈ 0.207 (3 s.f.).",
                "Check the logic: throw 5 is a score; throws 1 to 4 contain exactly 2 scores, in C(4, 2) = 6 possible positions.",
                "E(X) = 3/0.6 = 5 throws.   Var(X) = 3 × 0.4/0.6² = 10/3 ≈ 3.33.",
            ],
        },
        {
            "title": "Cumulative probabilities using the binomial",
            "question": "X ~ NB(2, 0.2). Find P(X > 10) and P(X ≤ 6).",
            "steps": [
                "X > 10 means at most 1 success in the first 10 trials. With Y ~ B(10, 0.2): P(X > 10) = P(Y ≤ 1) = 0.3758 (tables).",
                "X ≤ 6 means at least 2 successes in the first 6 trials. With W ~ B(6, 0.2): P(X ≤ 6) = 1 − P(W ≤ 1) = 1 − 0.6554 = 0.3446.",
                "Check by summing: P(X ≤ 6) = Σ C(x − 1, 1)(0.2)²(0.8)^(x−2) for x = 2 to 6 = 0.04 + 0.064 + 0.0768 + 0.08192 + 0.08192 = 0.34464.",
            ],
        },
        {
            "title": "Finding r and p from the mean and variance",
            "question": "The number of trials up to and including the r-th success has mean 12 and variance 24. Find r and p, and explain "
                        "why X can be written as a sum of geometric variables.",
            "steps": [
                "Var/E = (1 − p)/p = 24/12 = 2, so 1 − p = 2p and p = 1/3.",
                "r/p = 12 gives r = 4.",
                "X = Y₁ + Y₂ + Y₃ + Y₄, where Yᵢ is the number of trials after the (i − 1)th success up to and including the i-th. "
                "The trials are independent with constant p, so each Yᵢ ~ Geo(1/3) independently: mean 3, variance 6. Sum: 12 and 24.",
            ],
        },
        {
            "title": "Testing whether p has decreased",
            "question": "A machine is known to produce defective items with probability 0.1. After a service, the engineer believes the "
                        "probability has decreased. Items are inspected until the first defective one, which is the 25th item. "
                        "(a) Test at the 5% level. (b) Find the critical region and the actual significance level.",
            "steps": [
                "Let p be the probability that an item is defective. H₀: p = 0.1, H₁: p < 0.1. Under H₀, X ~ Geo(0.1).",
                "(a) A lower p means a longer wait, so the p-value is P(X ≥ 25) = 0.9²⁴ = 0.0798 (3 s.f.).",
                "0.0798 > 0.05, so do not reject H₀. There is insufficient evidence at the 5% level to suggest that the probability "
                "of a defective item has decreased.",
                "(b) Need 0.9^(c−1) ≤ 0.05: c − 1 ≥ ln 0.05/ln 0.9 = 28.43, so c − 1 = 29 and c = 30. Check: 0.9²⁸ = 0.0523 > 0.05, 0.9²⁹ = 0.0471 ≤ 0.05.",
                "Critical region X ≥ 30. Actual significance level = 0.9²⁹ = 0.0471 (3 s.f.). The observed 25 is not in it, as in (a).",
            ],
        },
        {
            "title": "Testing whether p has increased",
            "question": "Before a campaign, 4% of visitors to a website made a purchase. After the campaign, the owner tests at the 10% "
                        "level whether the proportion has increased, using X, the number of visitors up to and including the first "
                        "purchaser. Find the critical region and its actual significance level. The first purchase is made by the 2nd visitor. "
                        "Draw a conclusion.",
            "steps": [
                "Let p be the probability that a visitor purchases. H₀: p = 0.04, H₁: p > 0.04. Under H₀, X ~ Geo(0.04).",
                "A higher p means a shorter wait: the critical region is X ≤ c with 1 − 0.96<sup>c</sup> ≤ 0.1, so 0.96<sup>c</sup> ≥ 0.9 and c ≤ ln 0.9/ln 0.96 = 2.58.",
                "So c = 2: P(X ≤ 2) = 1 − 0.96² = 0.0784, while P(X ≤ 3) = 0.115 > 0.1. Critical region X ≤ 2; actual significance level 0.0784.",
                "x = 2 is in the critical region: reject H₀. There is sufficient evidence at the 10% level to suggest that the "
                "proportion of visitors making a purchase has increased.",
            ],
        },
        {
            "title": "A two-tailed test with an empty tail",
            "question": "Test H₀: p = 0.25 against H₁: p ≠ 0.25 at the 10% level using a single observation of X ~ Geo(p). Find the "
                        "critical region and the actual significance level. What can be concluded if x = 1?",
            "steps": [
                "Each tail may have at most 0.05.",
                "Lower tail (evidence p > 0.25): the smallest region is X = 1, with P(X = 1) = 0.25 > 0.05. So there is no lower critical region.",
                "Upper tail: 0.75^(c−1) ≤ 0.05 gives c − 1 ≥ ln 0.05/ln 0.75 = 10.41, so c = 12. P(X ≥ 12) = 0.75¹¹ = 0.0422; P(X ≥ 11) = 0.0563 > 0.05.",
                "Critical region X ≥ 12; actual significance level 0.0422 (3 s.f.).",
                "x = 1 is not in the critical region: there is insufficient evidence at the 10% level that p differs from 0.25. "
                "With a single geometric observation, this test can never detect an increase in p.",
            ],
        },
    ],
    "practice": [
        "X ~ NB(4, 0.5). Find P(X = 6), E(X) and Var(X).",
        "X ~ NB(2, 0.3). Find P(X = 5) and, using a binomial distribution, P(X ≤ 4).",
        "A fair die is rolled until the third six appears. Find the probability that exactly 10 rolls are needed, and the mean and "
        "variance of the number of rolls.",
        "X has a negative binomial distribution with mean 10 and variance 15. Find r and p.",
        "Explain why the number of trials up to and including the r-th success can be written as the sum of r independent Geo(p) "
        "variables, and hence derive E(X) and Var(X).",
        "X ~ NB(3, 0.25). Explain why P(X > 8) = P(Y ≤ 2) where Y ~ B(8, 0.25), and find its value.",
        "X ~ Geo(p). Find the critical region for a test of H₀: p = 0.3 against H₁: p < 0.3 at the 5% level, and its actual "
        "significance level.",
        "X ~ Geo(p). Find the critical region for a test of H₀: p = 0.02 against H₁: p > 0.02 at the 5% level, and its actual "
        "significance level.",
        "It is claimed that 15% of people in a town recognise a logo. A researcher thinks the true proportion is lower. She asks people "
        "at random until someone recognises it; this is the 20th person. Test the claim at the 5% level.",
        "X ~ Geo(p). Find the critical region for a test of H₀: p = 0.01 against H₁: p ≠ 0.01 at the 5% level (2.5% in each tail), "
        "and the actual significance level.",
        "X ~ NB(3, 0.5). Find P(X = x) for x = 3, 4, 5, 6 and hence state the mode(s) of X.",
        "(Link, Edexcel 4.1) The number of faults in a length of cable is Po(λ). Historically λ = 4. After a change of supplier, 8 faults "
        "are found in a length. Test at the 5% level whether the mean number of faults has increased.",
    ],
    "answers": [
        "P(X = 6) = C(5, 3)(0.5)⁴(0.5)² = 10/64 = 0.15625. E(X) = 4/0.5 = 8. Var(X) = 4 × 0.5/0.25 = 8.",
        "P(X = 5) = C(4, 1)(0.3)²(0.7)³ = 0.12348 ≈ 0.123. P(X ≤ 4) = P(Y ≥ 2), Y ~ B(4, 0.3): 1 − 0.6517 = 0.3483.",
        "X ~ NB(3, 1/6). P(X = 10) = C(9, 2)(1/6)³(5/6)⁷ = 0.0465 (3 s.f.). E(X) = 18. Var(X) = 3 × (5/6)/(1/36) = 90.",
        "(1 − p)/p = 15/10 = 1.5, so p = 0.4. r = 10p = 4.",
        "After each success the process starts afresh (independent trials, constant p), so the numbers of trials Y₁, …, Yᵣ between "
        "successive successes are independent Geo(p). X = Σ Yᵢ, so E(X) = r/p and Var(X) = r(1 − p)/p².",
        "X > 8 means the 3rd success has not happened by trial 8, i.e. at most 2 successes in 8 trials. P(Y ≤ 2) = 0.6785.",
        "0.7^(c−1) ≤ 0.05 gives c − 1 ≥ 8.40, so c = 10. Critical region X ≥ 10; actual significance level 0.7⁹ = 0.0404 (0.7⁸ = 0.0576 > 0.05).",
        "1 − 0.98<sup>c</sup> ≤ 0.05 gives c ≤ 2.54, so c = 2. Critical region X ≤ 2; actual significance level 1 − 0.98² = 0.0396 "
        "(P(X ≤ 3) = 0.0588 > 0.05).",
        "p = proportion who recognise the logo. H₀: p = 0.15, H₁: p < 0.15; X ~ Geo(0.15) under H₀. P(X ≥ 20) = 0.85¹⁹ = 0.0456 < 0.05. "
        "Reject H₀: there is sufficient evidence at the 5% level that fewer than 15% of people recognise the logo.",
        "Lower tail: 1 − 0.99<sup>c</sup> ≤ 0.025 gives c ≤ 2.52, so X ≤ 2 with probability 0.0199. Upper tail: 0.99^(c−1) ≤ 0.025 gives "
        "c − 1 ≥ 367.04, so c = 369, with P(X ≥ 369) = 0.99³⁶⁸ = 0.0248. Critical region X ≤ 2 or X ≥ 369; actual significance level "
        "0.0199 + 0.0248 = 0.0447.",
        "P(X = 3) = 0.125, P(X = 4) = 0.1875, P(X = 5) = 0.1875, P(X = 6) = 0.15625. Modes 4 and 5 (here (r − 1)/p = 4 is an integer).",
        "H₀: λ = 4, H₁: λ > 4. Under H₀, X ~ Po(4). P(X ≥ 8) = 1 − P(X ≤ 7) = 1 − 0.9489 = 0.0511 > 0.05. Do not reject H₀: insufficient "
        "evidence at the 5% level that the mean number of faults has increased.",
    ],
    "exam": [
        "A salesperson makes telephone calls. Each call independently results in a sale with probability 0.2. Her daily target is 3 sales, "
        "and she stops calling when she reaches it. X is the number of calls she makes in a day. (a) Find P(X = 10). [3]  "
        "(b) Find E(X) and the standard deviation of X. [3]  (c) By considering a suitable binomial distribution, find the probability "
        "that she needs more than 20 calls. [3]  (d) Find the probability that, in a 5-day week, she needs more than 20 calls on at least "
        "one day. [2]",
        "A gardener claims that 1 in 8 seeds of a particular variety produces a white flower. A biologist believes the proportion is "
        "lower in a new strain. She plants seeds one at a time and records X, the number of seeds up to and including the first one "
        "that produces a white flower. (a) Write suitable hypotheses, defining your parameter. [1]  (b) Find the critical region for a "
        "test at the 5% level. [4]  (c) State the actual significance level. [1]  (d) The first white flower comes from the 21st seed. "
        "State the conclusion of the test in context. [2]  (e) (Link with A2.5) Find the probability that the test rejects H₀ when the "
        "true proportion is 0.05. [2]  (f) Explain why no test of H₁: p > 1/8 at the 5% level is possible with this method. [1]",
        "X ~ Geo(p). A test of H₀: p = 0.2 against H₁: p ≠ 0.2 is carried out at the 10% level, with 5% in each tail. (a) Show that the "
        "lower tail has no critical region. [2]  (b) Find the critical region. [3]  (c) State the actual significance level. [1]  "
        "(d) The observed value is 13. Find the p-value for this tail and state the conclusion. [2]  (e) Instead, the trials are "
        "continued until the 2nd success, which occurs on trial 20. Under H₀, find the probability that the 2nd success needs at "
        "least 20 trials. [3]",
        "X is the number of independent trials, each with success probability p, up to and including the r-th success. "
        "(a) Show that P(X = x) = C(x − 1, r − 1) pʳ (1 − p)^(x−r) for x = r, r + 1, …. [3]  (b) Show that "
        "P(X = x + 1)/P(X = x) = x(1 − p)/(x − r + 1). Hence find the mode of X when r = 4 and p = 0.35. [4]  "
        "(c) For r = 4 and p = 0.35, find E(X) and Var(X). [2]  (d) Find P(X = 9) when r = 4 and p = 0.35. [2]",
    ],
    "exam_answers": [
        "(a) X ~ NB(3, 0.2) (B1). P(X = 10) = C(9, 2)(0.2)³(0.8)⁷ (M1) = 0.0604 (3 s.f.) (A1).  (b) E(X) = 3/0.2 = 15 (B1); "
        "Var(X) = 3 × 0.8/0.04 = 60 (M1); SD = √60 ≈ 7.75 (A1).  (c) More than 20 calls ⇔ at most 2 sales in 20 calls (M1): "
        "Y ~ B(20, 0.2), P(Y ≤ 2) (M1) = 0.2061 (A1).  (d) 1 − (1 − 0.2061)⁵ (M1) = 0.685 (A1), assuming days are independent.",
        "(a) p = probability that a seed produces a white flower. H₀: p = 0.125, H₁: p < 0.125 (B1).  (b) Under H₀ X ~ Geo(0.125); "
        "large X supports H₁ (M1). 0.875^(c−1) ≤ 0.05 (M1) gives c − 1 ≥ 22.43 (A1); critical region X ≥ 24 (A1).  "
        "(c) 0.875²³ = 0.0464 (3 s.f.) (B1).  (d) 21 is not in the critical region (P(X ≥ 21) = 0.875²⁰ = 0.0692 > 0.05) (M1); "
        "insufficient evidence at the 5% level to suggest that the proportion of white flowers is lower in the new strain (A1).  "
        "(e) P(X ≥ 24 | p = 0.05) = 0.95²³ (M1) = 0.307 (A1).  (f) The smallest possible region X = 1 has probability 0.125 > 0.05 (B1).",
        "(a) Lower tail evidence is small X; the smallest region is X = 1 (M1) with P(X = 1) = 0.2 > 0.05, so no critical region (A1).  "
        "(b) 0.8^(c−1) ≤ 0.05 (M1), c − 1 ≥ 13.43 (A1), critical region X ≥ 15 (A1).  (c) 0.8¹⁴ = 0.0440 (3 s.f.) (B1).  "
        "(d) P(X ≥ 13) = 0.8¹² = 0.0687 > 0.05 (M1); not significant, insufficient evidence at the 10% level that p ≠ 0.2 (A1).  "
        "(e) Y ~ NB(2, 0.2). Y ≥ 20 ⇔ at most 1 success in the first 19 trials (M1): W ~ B(19, 0.2), P(W ≤ 1) (M1) = 0.0829 (A1).",
        "(a) Trial x is a success (probability p) (B1); the first x − 1 trials contain r − 1 successes, a binomial probability "
        "C(x − 1, r − 1)p^(r−1)(1 − p)^(x−r) (M1); multiply by independence (A1).  (b) Ratio = [C(x, r − 1)/C(x − 1, r − 1)](1 − p) "
        "(M1) = x(1 − p)/(x − r + 1) (A1). Ratio ≥ 1 ⇔ x(1 − p) ≥ x − r + 1 ⇔ x ≤ (r − 1)/p = 8.57 (M1). So the probabilities increase "
        "up to x = 9 and then decrease: mode 9 (A1).  (c) E(X) = 4/0.35 = 11.4 (3 s.f.) (B1); Var(X) = 4 × 0.65/0.35² = 21.2 (3 s.f.) (B1).  "
        "(d) C(8, 3)(0.35)⁴(0.65)⁵ (M1) = 0.0975 (3 s.f.) (A1).",
    ],
}
