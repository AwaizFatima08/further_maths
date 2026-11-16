UNIT = {
    "number": "AS3",
    "title": "The geometric distribution",
    "tag": "AS · OCR A (5.02f–h), OCR MEI (SR16–SR18) · A level · Edexcel FS1 (topic 3) · prior knowledge for CAIE 9231 Paper 4 · "
           "not on AQA or IAL S3",
    "notes": [
        ("p", "The binomial distribution fixes the number of trials and counts successes. The geometric distribution turns this "
              "round: it keeps going until the first success and counts the trials. It models waiting: the number of rolls until a "
              "six, the number of calls until a sale, the number of items inspected until a faulty one is found."),

        ("h2", "3.1 The geometric model"),
        ("p", "Suppose a sequence of trials is carried out, each a success with probability p, and X is the number of trials "
              "<b>up to and including</b> the first success. Then X has a <b>geometric distribution</b>, written X ~ Geo(p). "
              "The conditions are the same as for the binomial except that there is no fixed number of trials:"),
        ("bullets", [
            "each trial has two outcomes, success or failure;",
            "the probability of success p is the same on every trial;",
            "the trials are independent;",
            "X counts the trials up to and including the first success, so X = 1, 2, 3, … with no upper limit.",
        ]),
        ("p", "Some textbooks define a geometric variable as the number of <i>failures</i> before the first success (taking values 0, 1, 2, …). "
              "None of the A level boards uses this; MEI states it is excluded. Here X always starts at 1."),
        ("p", "<b>Link with the binomial (MEI SR16).</b> The event X > x means the first x trials are all failures. That is the same as "
              "Y = 0, where Y ~ B(x, p) counts successes in the first x trials. So P(X > x) = P(Y = 0) = (1 − p)ˣ."),

        ("h2", "3.2 Probabilities"),
        ("p", "For X = x we need x − 1 failures followed by a success. By independence:"),
        ("box", "Geometric Geo(p): probabilities (write q = 1 − p)", [
            "P(X = x) = q^(x−1) p,   x = 1, 2, 3, …",
            "P(X > x) = qˣ   (the first x trials all fail)",
            "P(X ≥ x) = q^(x−1)   (the first x − 1 trials all fail)",
            "P(X ≤ x) = 1 − qˣ",
            "P(a ≤ X ≤ b) = P(X ≥ a) − P(X > b) = q^(a−1) − q<sup>b</sup>",
        ]),
        ("p", "The probabilities form a geometric series with first term p and common ratio q, which is where the name comes from. "
              "They add to 1: Σ q^(x−1) p = p/(1 − q) = p/p = 1. Summing the first x terms gives P(X ≤ x) = p(1 − qˣ)/(1 − q) = 1 − qˣ, "
              "which agrees with the 'all fail' argument."),
        ("p", "<b>Finding the number of trials needed.</b> Questions such as 'find the smallest n so that P(X ≤ n) ≥ 0.9' lead to "
              "qⁿ ≤ 0.1. Take logarithms: n ln q ≤ ln 0.1. Because ln q is negative, dividing by it reverses the inequality: "
              "n ≥ ln 0.1/ln q. Round <i>up</i> to the next integer, and check the values either side."),

        ("h2", "3.3 Mean and variance"),
        ("box", "Mean and variance of Geo(p)", [
            "E(X) = 1/p,     Var(X) = (1 − p)/p²",
            "Proofs are excluded for OCR A and MEI and not required for Edexcel; Edexcel derives them with generating functions in A2.4. "
            "The derivation below is for understanding and for 'show that' questions.",
        ]),
        ("p", "The mean makes sense: if a success happens on 1/4 of trials, on average you wait 4 trials. Note that the variance is "
              "large when p is small: rare events lead to very variable waiting times."),
        ("p", "<b>Derivation of the mean (sum of a series).</b> Differentiate the geometric series Σ qˣ = 1/(1 − q) (for |q| < 1) "
              "with respect to q: Σ x q^(x−1) = 1/(1 − q)². Then E(X) = Σ x q^(x−1) p = p/(1 − q)² = p/p² = 1/p."),
        ("p", "<b>Derivation of the variance.</b> Differentiate again: Σ x(x − 1) q^(x−2) = 2/(1 − q)³. So "
              "E[X(X − 1)] = Σ x(x − 1) q^(x−1) p = pq × 2/p³ = 2q/p². Then E(X²) = E[X(X − 1)] + E(X) = 2q/p² + 1/p, and "
              "Var(X) = 2q/p² + 1/p − 1/p² = (2q + p − 1)/p² = (2q − q)/p² = q/p²."),

        ("h2", "3.4 The memoryless property"),
        ("p", "Because the trials are independent, past failures do not change the chance of future success. Formally, for "
              "non-negative integers a and b:"),
        ("box", "Memoryless (lack of memory) property", [
            "P(X > a + b | X > a) = P(X > b).",
            "Proof: P(X > a + b | X > a) = P(X > a + b)/P(X > a) = q^(a+b)/q<sup>a</sup> = q<sup>b</sup> = P(X > b).",
            "So if the first a trials have all failed, the number of further trials needed is again Geo(p).",
        ]),
        ("p", "In particular P(X = a + k | X > a) = P(X = k). This is why, in a game where players take turns, the position 'nobody "
              "has won yet and it is A's turn' always has the same probability of A winning. The geometric distribution is the only "
              "discrete distribution on 1, 2, 3, … with this property; unit A2.2 shows the exponential plays the same role for "
              "continuous waiting times."),

        ("h2", "3.5 Mode and median"),
        ("p", "Each probability is q times the one before, so P(X = x) decreases as x increases. The <b>mode is always 1</b>, "
              "whatever the value of p. The median is the smallest m with P(X ≤ m) ≥ 0.5, that is 1 − qᵐ ≥ 0.5, or "
              "m ≥ ln 0.5/ln q (rounded up). The mean 1/p is larger than the median: the distribution has a long right tail "
              "(positive skew)."),
        ("table", ["p", "P(X = 1)", "P(X ≤ 3)", "P(X > 10)", "E(X)", "Var(X)", "Median"], [
            ["0.5", "0.5", "0.875", "0.000977", "2", "2", "1"],
            ["0.3", "0.3", "0.657", "0.0282", "3.33", "7.78", "2"],
            ["1/6", "0.167", "0.421", "0.162", "6", "30", "4"],
            ["0.1", "0.1", "0.271", "0.349", "10", "90", "7"],
        ]),

        ("h2", "3.6 Modelling with the geometric distribution"),
        ("p", "When criticising a geometric model, test the two key assumptions in context:"),
        ("bullets", [
            "<b>Constant p.</b> A person learning a skill (passing a driving test, scoring a penalty) improves, so p rises with practice. "
            "Machines may wear, so p of a fault increases.",
            "<b>Independence.</b> A failure may affect the next attempt (nerves, fatigue, a faulty batch of components made together).",
            "<b>Sampling without replacement</b> from a small batch changes p after each item, so the model is only approximate; it is "
            "good when the batch is large.",
        ]),
        ("p", "Links: the number of trials up to the r-th success has the negative binomial distribution (Edexcel, unit A2.3), "
              "which is a sum of r independent geometric variables; Edexcel also tests hypotheses about p using a geometric "
              "observation (A2.3); and the probability generating function of Geo(p) is pt/(1 − qt) (A2.4)."),
        ("warn", "Common mistakes", [
            "Using pˣ⁻¹ q instead of q^(x−1) p: it is the failures that come first.",
            "Confusing P(X > x) = qˣ with P(X ≥ x) = q^(x−1). Ask: how many trials must have failed?",
            "Reading '6 failures before the first success' as X = 6. It means X = 7.",
            "Forgetting to reverse the inequality when dividing by ln q (a negative number), or rounding n down instead of up.",
            "Claiming the mode is 1/p. The mode is always 1.",
            "In a memoryless question, using the original start: given X > 4, P(X > 10) is q⁶, not q¹⁰.",
        ]),
    ],
    "examples": [
        {
            "title": "Geometric probabilities",
            "question": "A darts player hits the bullseye with probability 0.15 on each throw, independently. X is the number of throws "
                        "up to and including the first bullseye. Find (a) P(X = 5), (b) P(X > 6), (c) P(X ≤ 4), (d) P(3 ≤ X ≤ 8).",
            "steps": [
                "X ~ Geo(0.15), q = 0.85.",
                "(a) P(X = 5) = 0.85⁴ × 0.15 = 0.0783 (3 s.f.).",
                "(b) P(X > 6) = 0.85⁶ = 0.377 (3 s.f.): the first six throws all miss.",
                "(c) P(X ≤ 4) = 1 − 0.85⁴ = 0.478 (3 s.f.).",
                "(d) P(3 ≤ X ≤ 8) = P(X ≥ 3) − P(X > 8) = 0.85² − 0.85⁸ = 0.7225 − 0.2725 = 0.450 (3 s.f.).",
            ],
        },
        {
            "title": "How many trials are needed?",
            "question": "For the darts player in Worked example AS3.1, find the smallest number of throws n so that the probability of "
                        "hitting at least one bullseye in n throws is at least 0.9.",
            "steps": [
                "P(at least one bullseye in n throws) = P(X ≤ n) = 1 − 0.85ⁿ ≥ 0.9, so 0.85ⁿ ≤ 0.1.",
                "n ln 0.85 ≤ ln 0.1. Divide by ln 0.85 < 0, reversing the inequality: n ≥ ln 0.1/ln 0.85 = 14.17.",
                "So n = 15. Check: 0.85¹⁴ = 0.103 > 0.1 but 0.85¹⁵ = 0.0874 ≤ 0.1.",
            ],
        },
        {
            "title": "Mean, variance and the memoryless property",
            "question": "A fair die is rolled until a six appears. X is the number of rolls. (a) Find E(X), Var(X) and the standard "
                        "deviation. (b) Find P(X > E(X)). (c) Given that no six appears in the first 4 rolls, find the probability that "
                        "no six appears in the first 10 rolls.",
            "steps": [
                "(a) X ~ Geo(1/6). E(X) = 6. Var(X) = (5/6)/(1/6)² = 30, so the standard deviation is √30 ≈ 5.48.",
                "(b) P(X > 6) = (5/6)⁶ = 0.335 (3 s.f.).",
                "(c) P(X > 10 | X > 4) = P(X > 10)/P(X > 4) = (5/6)¹⁰/(5/6)⁴ = (5/6)⁶ = 0.335.",
                "This is the memoryless property: the 4 failed rolls do not matter, and 6 more failures are needed.",
            ],
        },
        {
            "title": "Finding p from the variance",
            "question": "X ~ Geo(p) and Var(X) = 12. Find p, E(X) and P(X ≥ 3).",
            "steps": [
                "(1 − p)/p² = 12 gives 12p² + p − 1 = 0, so (4p − 1)(3p + 1) = 0.",
                "p > 0, so p = 1/4 = 0.25. Then E(X) = 4.",
                "P(X ≥ 3) = q² = 0.75² = 0.5625.",
            ],
        },
        {
            "title": "Taking turns: who wins?",
            "question": "A and B take turns to throw at a target, A first. A hits with probability 0.3 and B with probability 0.4 on each "
                        "throw, independently. The first to hit wins. Find the probability that A wins.",
            "steps": [
                "A wins on A's first throw with probability 0.3. If both miss (probability 0.7 × 0.6 = 0.42) the game is back where it "
                "started, with A to throw (memoryless).",
                "So P(A wins) = 0.3 + 0.42 × P(A wins), giving P(A wins) = 0.3/(1 − 0.42) = 0.3/0.58 = 15/29 ≈ 0.517.",
                "Equivalently, P(A wins) = 0.3(1 + 0.42 + 0.42² + …), a geometric series with sum 0.3/0.58.",
            ],
        },
    ],
    "practice": [
        "X ~ Geo(0.2). Find P(X = 3), E(X) and Var(X).",
        "X ~ Geo(0.35). Find P(X = 4), P(X > 5) and P(X ≤ 3), giving answers to 4 decimal places.",
        "The probability that a component is faulty is 0.05, independently of other components. Components are tested one at a time. "
        "Find the probability that (a) the first faulty component is the 6th one tested, (b) more than 20 components have to be tested to "
        "find the first faulty one.",
        "A fair die is rolled until a six is obtained. Find the probability that the number of rolls needed is between 2 and 5 inclusive.",
        "The probability that a randomly chosen person in a street agrees to answer a survey is 0.08. Find the smallest number of people "
        "who must be approached so that the probability that at least one agrees is greater than 0.99.",
        "X ~ Geo(p) and E(X) = 2.5. Find p, Var(X) and P(X > E(X)).",
        "X ~ Geo(0.1). Given that X > 5, find (a) P(X > 8), (b) P(X = 7).",
        "Prove that, for X ~ Geo(p) and non-negative integers a and b, P(X > a + b | X > a) = P(X > b). Explain the meaning of this result "
        "in the context of rolling a die until a six appears.",
        "X ~ Geo(p). (a) Show that Σ P(X = x) over x = 1, 2, 3, … equals 1. (b) By summing a geometric series, show that "
        "P(X ≤ x) = 1 − (1 − p)ˣ.",
        "X ~ Geo(0.3). Write down the mode of X and find the median of X.",
        "A student models the number of attempts she needs to pass her driving test by a geometric distribution. Give two reasons why "
        "this model may not be suitable.",
        "X ~ Geo(p) and Var(X) = 6. Find p and P(X = 2).",
    ],
    "answers": [
        "P(X = 3) = 0.8² × 0.2 = 0.128. E(X) = 1/0.2 = 5. Var(X) = 0.8/0.2² = 20.",
        "P(X = 4) = 0.65³ × 0.35 = 0.0961. P(X > 5) = 0.65⁵ = 0.1160. P(X ≤ 3) = 1 − 0.65³ = 0.7254.",
        "X ~ Geo(0.05). (a) P(X = 6) = 0.95⁵ × 0.05 = 0.0387 (3 s.f.). (b) P(X > 20) = 0.95²⁰ = 0.358 (3 s.f.): the first 20 are all good.",
        "P(2 ≤ X ≤ 5) = (5/6)¹ − (5/6)⁵ = 0.8333 − 0.4019 = 0.431 (3 s.f.).",
        "1 − 0.92ⁿ > 0.99 gives 0.92ⁿ < 0.01, so n > ln 0.01/ln 0.92 = 55.23. The smallest number is 56.",
        "1/p = 2.5, so p = 0.4. Var(X) = 0.6/0.16 = 3.75. P(X > 2.5) = P(X ≥ 3) = 0.6² = 0.36.",
        "(a) By the memoryless property P(X > 8 | X > 5) = P(X > 3) = 0.9³ = 0.729. (b) P(X = 7 | X > 5) = P(X = 2) = 0.9 × 0.1 = 0.09.",
        "P(X > a + b | X > a) = P(X > a + b and X > a)/P(X > a) = P(X > a + b)/P(X > a) = q^(a+b)/q<sup>a</sup> = q<sup>b</sup> = P(X > b). Context: if no six "
        "has appeared in the first a rolls, the chance of needing more than b further rolls is the same as at the start; the die "
        "does not 'remember' the earlier failures.",
        "(a) Σ q^(x−1)p = p(1 + q + q² + …) = p/(1 − q) = p/p = 1, since 0 < q < 1. (b) P(X ≤ x) = p(1 + q + … + q^(x−1)) = "
        "p(1 − qˣ)/(1 − q) = 1 − qˣ = 1 − (1 − p)ˣ.",
        "Mode = 1. P(X ≤ 1) = 0.3 and P(X ≤ 2) = 1 − 0.7² = 0.51 ≥ 0.5, so the median is 2.",
        "The probability of passing is unlikely to be constant: she learns from each attempt (p rises) or may become more nervous. "
        "Attempts may not be independent, e.g. a bad experience affects the next test. (Also, she may stop trying, so X need not be finite.)",
        "(1 − p)/p² = 6 gives 6p² + p − 1 = 0, (3p − 1)(2p + 1) = 0, so p = 1/3. P(X = 2) = (2/3)(1/3) = 2/9 ≈ 0.222.",
    ],
    "exam": [
        "Items from a production line are each defective with probability 0.04, independently. An inspector tests items one at a time "
        "until she finds a defective one. X is the number of items tested. (a) State the distribution of X and two assumptions needed. [2]  "
        "(b) Find P(X = 10). [2]  (c) Find P(X > 25). [2]  (d) Find E(X) and the standard deviation of X. [2]  (e) The first 20 items "
        "are all good. Find the probability that a defective item is found among the next 5 items. [2]  (f) Find the smallest n such "
        "that P(X ≤ n) ≥ 0.95. [3]",
        "Ann and Ben take turns to roll a fair die, Ann first. The first to roll a six wins. (a) Find the probability that Ann wins on "
        "her second turn. [2]  (b) Show that the probability that Ann wins is 6/11. [4]  (c) T is the total number of rolls in the game. "
        "State the distribution of T, and find E(T) and P(T > 10). [3]  (d) The first four rolls are not sixes. Find the probability that "
        "Ann wins, explaining your reasoning. [2]",
        "X ~ Geo(p), and q = 1 − p. (a) Show that Σ P(X = x) = 1. [2]  (b) Given that Σ x q^(x−1) = 1/(1 − q)² for |q| < 1, show that "
        "E(X) = 1/p. [3]  (c) Given that E[X(X − 1)] = 2q/p², show that Var(X) = q/p². [3]  (d) A random variable Y has a geometric "
        "distribution with mean 5. Find P(Y ≥ 5). [2]",
        "On each school day, independently, the probability that a particular bus is late is 0.3. Monday is day 1 of the term. "
        "(a) Find the probability that the first late bus is on day 4 (Thursday). [2]  (b) Y is the number of late buses in the first "
        "10 days. Find P(Y = 2). [2]  (c) X is the day of the first late bus. Explain why P(X > 10) = P(Y = 0), and evaluate it. [2]  "
        "(d) Find E(X) and Var(X). [2]  (e) Comment on the assumption of independence in this context. [1]",
    ],
    "exam_answers": [
        "(a) X ~ Geo(0.04) (B1); items are defective independently, with constant probability 0.04 (B1).  (b) 0.96⁹ × 0.04 (M1) = 0.0277 "
        "(3 s.f.) (A1).  (c) 0.96²⁵ (M1) = 0.360 (A1).  (d) E(X) = 25 (B1); SD = √(0.96/0.04²) = √600 ≈ 24.5 (B1).  (e) Memoryless: "
        "P(X ≤ 5) (M1) = 1 − 0.96⁵ = 0.185 (A1).  (f) 0.96ⁿ ≤ 0.05 (M1), n ≥ ln 0.05/ln 0.96 = 73.39 (M1), n = 74 (A1).",
        "(a) Ann's second turn is roll 3: (5/6)²(1/6) (M1) = 25/216 ≈ 0.116 (A1).  (b) Ann wins on rolls 1, 3, 5, …: "
        "P = (1/6)[1 + (5/6)² + (5/6)⁴ + …] (M1 A1) = (1/6)/(1 − 25/36) (M1) = (1/6)(36/11) = 6/11 (A1).  (c) T ~ Geo(1/6) (B1), "
        "E(T) = 6 (B1), P(T > 10) = (5/6)¹⁰ = 0.162 (B1).  (d) After four rolls it is Ann's turn again and the die has no memory (B1), "
        "so P(Ann wins) = 6/11 (B1).",
        "(a) Σ q^(x−1)p = p/(1 − q) (M1) = p/p = 1 (A1).  (b) E(X) = Σ x q^(x−1) p (M1) = p/(1 − q)² (M1) = p/p² = 1/p (A1).  "
        "(c) E(X²) = E[X(X − 1)] + E(X) = 2q/p² + 1/p (M1); Var(X) = 2q/p² + 1/p − 1/p² (M1) = (2q + p − 1)/p² = q/p² since p − 1 = −q (A1).  "
        "(d) p = 0.2 (B1); P(Y ≥ 5) = 0.8⁴ = 0.4096 (B1).",
        "(a) 0.7³ × 0.3 (M1) = 0.1029 (A1).  (b) Y ~ B(10, 0.3): P(Y = 2) = C(10, 2)(0.3)²(0.7)⁸ (M1) = 0.233 (3 s.f.) (A1).  "
        "(c) X > 10 means none of the first 10 buses is late, which is exactly Y = 0 (B1); 0.7¹⁰ = 0.0282 (B1).  (d) E(X) = 1/0.3 = 10/3 "
        "≈ 3.33 (B1); Var(X) = 0.7/0.3² = 70/9 ≈ 7.78 (B1).  (e) Not likely to hold: lateness is affected by weather or roadworks that "
        "last several days, so late days tend to cluster (B1).",
    ],
}
