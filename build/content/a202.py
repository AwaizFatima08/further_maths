UNIT = {
    "number": "A2.2",
    "title": "The exponential distribution",
    "tag": "AQA A level (SF1–SF4, with proofs) · OCR A (5.03a, proofs excluded) · OCR MEI: awareness only, details given in questions · not Edexcel, IAL or CAIE",
    "notes": [
        ("h2", "2.1 Waiting for the next event"),
        ("p", "The Poisson distribution counts how many events happen in a fixed interval when events occur singly, at random, "
              "independently of each other, and at a constant average rate λ per unit time. The exponential distribution answers "
              "the companion question: how long do we wait until the next event? The waiting time (or distance) between consecutive "
              "events of such a process is a continuous random variable X with an exponential distribution, written X ~ Exp(λ)."),
        ("box", "X ~ Exp(λ), λ > 0", [
            "pdf: f(x) = λe^(−λx) for x ≥ 0, and f(x) = 0 for x < 0.",
            "cdf: F(x) = 1 − e^(−λx) for x ≥ 0, and F(x) = 0 for x < 0.   So P(X > x) = e^(−λx).",
            "E(X) = 1/λ    Var(X) = 1/λ²    standard deviation = 1/λ (the same as the mean).",
            "median = (ln 2)/λ;  kth percentile = −ln(1 − k/100)/λ;  mode = 0.",
        ]),
        ("p", "The pdf starts at height λ when x = 0 and decays towards 0 as x increases; it never reaches 0. It has a long tail to "
              "the right, so the distribution has positive skew: mode 0 < median (ln 2)/λ ≈ 0.693/λ < mean 1/λ. Note that λ is a rate "
              "(events per unit time), so the mean waiting time 1/λ has the reciprocal units: 4 calls per hour gives a mean wait of "
              "1/4 hour = 15 minutes."),
        ("h2", "2.2 The cdf and probabilities"),
        ("p", "For x ≥ 0, F(x) = ∫₀ˣ λe^(−λt) dt = [−e^(−λt)]₀ˣ = 1 − e^(−λx). The total area is 1 because e^(−λx) → 0 as x → ∞. "
              "Most probabilities are quickest from the survival function P(X > x) = e^(−λx):"),
        ("bullets", [
            "P(X > a) = e^(−λa);   P(X < a) = 1 − e^(−λa);   P(a < X < b) = e^(−λa) − e^(−λb).",
            "To find λ from a given probability, take logarithms: P(X > a) = p gives λ = −(ln p)/a.",
            "P(X < mean) = 1 − e^(−1) ≈ 0.632 for every exponential distribution, so most waits are shorter than the mean.",
        ]),
        ("h2", "2.3 Proofs of the mean and variance (AQA SF3)"),
        ("p", "AQA requires these proofs; OCR A gives the results in its formula booklet and excludes proofs; MEI students are "
              "given any details they need. Both proofs use integration by parts and the fact that xⁿe^(−λx) → 0 as x → ∞ for λ > 0."),
        ("box", "Proofs", [
            "E(X) = ∫₀^∞ x λe^(−λx) dx. Parts with u = x, dv/dx = λe^(−λx): = [−xe^(−λx)]₀^∞ + ∫₀^∞ e^(−λx) dx = 0 + [−e^(−λx)/λ]₀^∞ = 1/λ.",
            "E(X²) = ∫₀^∞ x² λe^(−λx) dx = [−x²e^(−λx)]₀^∞ + ∫₀^∞ 2x e^(−λx) dx = 0 + (2/λ)∫₀^∞ x λe^(−λx) dx = (2/λ) × E(X) = 2/λ².",
            "Var(X) = E(X²) − [E(X)]² = 2/λ² − 1/λ² = 1/λ², so the standard deviation is 1/λ.",
            "Median: F(m) = 1 − e^(−λm) = 0.5 gives e^(−λm) = 0.5, so m = (ln 2)/λ.",
        ]),
        ("h2", "2.4 The link with the Poisson process (AQA SF4, OCR A informal)"),
        ("p", "Suppose events occur at random at constant rate λ per unit time, so the number of events in time t is N(t) ~ Po(λt). "
              "Let T be the time from now until the next event. The next event is later than t exactly when there are no events "
              "in the interval of length t:"),
        ("box", "Exponential gaps in a Poisson process", [
            "P(T > t) = P(N(t) = 0) = e^(−λt)(λt)⁰/0! = e^(−λt), so P(T ≤ t) = 1 − e^(−λt): T ~ Exp(λ).",
            "Number of events in time t ~ Po(λt)  ⟷  time between events ~ Exp(λ), with the same rate λ in the same time units.",
            "Always convert the rate to the time unit the question uses: 6 calls per hour = 0.1 calls per minute.",
        ]),
        ("table", ["", "Poisson Po(λt)", "Exponential Exp(λ)"], [
            ["Random variable", "number of events in a fixed time t", "time (or distance) between events"],
            ["Type", "discrete: 0, 1, 2, …", "continuous: x ≥ 0"],
            ["Mean", "λt", "1/λ"],
            ["Variance", "λt", "1/λ²"],
            ["Key probability", "P(N = 0) = e^(−λt)", "P(T > t) = e^(−λt)"],
        ]),
        ("h2", "2.5 The memoryless (no-memory) property"),
        ("p", "If X ~ Exp(λ), then for any s, t ≥ 0: P(X > s + t | X > s) = P(X > t). Proof: P(X > s + t | X > s) = P(X > s + t and X > s)/P(X > s) "
              "= P(X > s + t)/P(X > s) = e^(−λ(s + t))/e^(−λs) = e^(−λt) = P(X > t). In words: if you have already waited s minutes, the "
              "extra time you must wait has the same distribution as a fresh wait. The process does not \"remember\" how long it has "
              "been since the last event. The exponential is the only continuous distribution with this property."),
        ("p", "This is the main test of whether the model is sensible. Radioactive decay, random calls to a help line and breakdowns "
              "caused by random shocks have no memory. Lifetimes of things that <b>wear out</b> (tyres, light bulb filaments, people) do: "
              "an old component is more likely to fail soon than a new one, so the exponential model is poor."),
        ("h2", "2.6 Modelling with the exponential distribution"),
        ("bullets", [
            "Conditions (AQA SF1): the variable is the time or distance between events that occur singly, independently, at random and at a constant average rate.",
            "Estimate λ by 1/x̄ from data. Since the mean equals the standard deviation, a sample whose standard deviation is close to its mean supports the model; a much smaller standard deviation does not.",
            "Check the shape: a histogram of the data should be highest near 0 and decrease steadily, with positive skew.",
            "Expected frequencies: if n intervals are observed, the expected number longer than a is n e^(−λa).",
            "A constant rate is often unrealistic over long periods (rush hours, seasons), so the model may only hold over short spans.",
        ]),
        ("p", "OCR MEI students: the exponential distribution is \"awareness only\"; any question will give you the pdf, so the methods "
              "of Units AS11 and A2.1 (integration, cdf, median) are what you need."),
        ("warn", "Common mistakes", [
            "Mixing time units: using a rate per hour with a time in minutes. Convert λ first.",
            "Using λ as the mean. The mean is 1/λ; for a mean of 8 minutes, λ = 0.125 per minute.",
            "Writing P(X > a) = 1 − e^(−λa). That is P(X ≤ a); the upper tail is e^(−λa).",
            "Losing the limits in the proofs: say why [−xe^(−λx)] tends to 0 as x → ∞.",
            "Applying the memoryless property to a conditional probability that is not of the form P(X > s + t | X > s), or using an exponential model for an item that wears out without comment.",
            "Rounding λ early when it comes from a logarithm: keep λ = −ln(0.6)/500 in the calculator.",
        ]),
    ],
    "examples": [
        {
            "title": "Probabilities, mean and standard deviation",
            "question": "The lifetime X years of a type of smoke-alarm battery is modelled as Exp(0.4). Find the mean and standard "
                        "deviation of X, P(X > 3) and P(1 < X < 4).",
            "steps": [
                "E(X) = 1/0.4 = 2.5 years and the standard deviation is also 1/0.4 = 2.5 years.",
                "P(X > 3) = e^(−0.4 × 3) = e^(−1.2) = 0.3012 (4 d.p.).",
                "P(1 < X < 4) = e^(−0.4) − e^(−1.6) = 0.67032 − 0.20190 = 0.4684 (4 d.p.).",
            ],
        },
        {
            "title": "Median, quartile and percentile",
            "question": "For X ~ Exp(0.4), find the median, the upper quartile and the 90th percentile, and compare the median with the mean.",
            "steps": [
                "Median: 1 − e^(−0.4m) = 0.5, so e^(−0.4m) = 0.5 and m = (ln 2)/0.4 = 1.73 years (3 s.f.).",
                "Upper quartile: e^(−0.4q) = 0.25, q = (ln 4)/0.4 = 3.47 years (3 s.f.).",
                "90th percentile: e^(−0.4x) = 0.1, x = (ln 10)/0.4 = 5.76 years (3 s.f.).",
                "The median (1.73) is less than the mean (2.5): the long right tail pulls the mean up, showing positive skew.",
            ],
        },
        {
            "title": "The Poisson link",
            "question": "Calls arrive at a help desk at random at an average rate of 6 per hour. Let T minutes be the time from now until the "
                        "next call. (a) State the distribution of T. (b) Find P(T > 15) in two ways. (c) Find P(T < 5). "
                        "(d) Find the probability that, of the next 5 gaps between calls, at least 2 are longer than 15 minutes.",
            "steps": [
                "(a) The rate is 6 per hour = 0.1 per minute, so T ~ Exp(0.1), with mean 10 minutes.",
                "(b) P(T > 15) = e^(−0.1 × 15) = e^(−1.5) = 0.2231. Equivalently, the number of calls in 15 minutes is Po(1.5), and P(no calls) = e^(−1.5) = 0.2231.",
                "(c) P(T < 5) = 1 − e^(−0.5) = 0.3935 (4 d.p.).",
                "(d) Gaps are independent, each longer than 15 minutes with probability p = e^(−1.5). Let Y ~ B(5, p). "
                "P(Y ≥ 2) = 1 − (1 − p)⁵ − 5p(1 − p)⁴ = 1 − 0.2830 − 0.4064 = 0.311 (3 s.f.).",
            ],
        },
        {
            "title": "The memoryless property",
            "question": "The lifetime of a type of electronic component is exponential with mean 1000 hours. A component has already worked "
                        "for 600 hours. Find the probability that it works for at least another 500 hours, and comment on the model.",
            "steps": [
                "λ = 1/1000. Required: P(X > 1100 | X > 600) = P(X > 1100)/P(X > 600) = e^(−1.1)/e^(−0.6) = e^(−0.5).",
                "= 0.6065 (4 d.p.), which equals P(X > 500) for a new component: the memoryless property.",
                "Comment: the model says a used component is as good as a new one. This is reasonable if failures are caused by random "
                "shocks (e.g. power surges), but not if the component wears out with age.",
            ],
        },
        {
            "title": "Finding λ from given information",
            "question": "(a) X ~ Exp(λ) and P(X > 2) = 0.3. Find λ and E(X). (b) Y is exponential with median 5. Find the mean of Y.",
            "steps": [
                "(a) e^(−2λ) = 0.3, so −2λ = ln 0.3 and λ = −(ln 0.3)/2 = 0.602 (3 s.f.). E(X) = 1/λ = 1.66 (3 s.f.).",
                "(b) (ln 2)/λ = 5, so λ = (ln 2)/5 = 0.1386 (4 s.f.), and E(Y) = 1/λ = 5/ln 2 = 7.21 (3 s.f.).",
            ],
        },
        {
            "title": "Assessing a model from data",
            "question": "The times, in minutes, between 80 consecutive arrivals at a petrol station have mean 4.2 and standard deviation 4.0. "
                        "(a) Explain why an exponential model may be suitable, and estimate λ. (b) Use the model to find the expected number "
                        "of the 80 gaps that are longer than 10 minutes. (c) Find the probability that a gap is shorter than the mean.",
            "steps": [
                "(a) For an exponential distribution the mean equals the standard deviation; here 4.2 and 4.0 are close. Arrivals at "
                "random at a roughly constant rate fit the conditions. λ = 1/4.2 = 0.238 per minute (3 s.f.).",
                "(b) P(gap > 10) = e^(−10/4.2) = 0.09246, so the expected number is 80 × 0.09246 = 7.40 (3 s.f.).",
                "(c) P(X < 4.2) = 1 − e^(−1) = 0.632 (3 s.f.).",
            ],
        },
    ],
    "practice": [
        "X ~ Exp(2). Find P(X > 1) and P(X < 0.25).",
        "X ~ Exp(0.25). Write down E(X) and Var(X), and find P(X > E(X)).",
        "X is exponential with mean 8. Find P(5 < X < 10).",
        "X ~ Exp(0.5). Find the median and the interquartile range of X.",
        "X ~ Exp(λ) and P(X > 3) = 0.2. Find λ and the mean of X.",
        "Emails arrive at random at an average rate of 12 per hour. T minutes is the time between consecutive emails. State the "
        "distribution of T, and find P(T > 10) and P(T < 2).",
        "X ~ Exp(0.1). Find P(X > 15 | X > 5) and explain why it equals P(X > 10).",
        "Prove that if X ~ Exp(λ), then P(X > s + t | X > s) = P(X > t) for all s, t ≥ 0.",
        "Prove that if X ~ Exp(λ), then E(X) = 1/λ.",
        "X ~ Exp(3). Find E(X²), E(2X² − 3X + 1) and E(e^X).",
        "A random variable has cdf F(x) = 1 − e^(−x/5) for x ≥ 0. Identify its distribution, state its mean, and find the value of x for which P(X > x) = 0.01.",
        "The distances (in thousands of km) that 50 car tyres last before needing replacement have mean 30 and standard deviation 8. "
        "Give two reasons why an exponential model is unsuitable.",
    ],
    "answers": [
        "P(X > 1) = e^(−2) = 0.1353. P(X < 0.25) = 1 − e^(−0.5) = 0.3935 (4 d.p.).",
        "E(X) = 4, Var(X) = 16. P(X > 4) = e^(−1) = 0.3679 (4 d.p.).",
        "λ = 1/8. P(5 < X < 10) = e^(−0.625) − e^(−1.25) = 0.2488 (4 d.p.).",
        "Median = (ln 2)/0.5 = 1.39. Q₁ = ln(4/3)/0.5, Q₃ = (ln 4)/0.5, so IQR = (ln 3)/0.5 = 2.20 (3 s.f.).",
        "e^(−3λ) = 0.2, λ = (ln 5)/3 = 0.536; mean = 3/ln 5 = 1.86 (3 s.f.).",
        "12 per hour = 0.2 per minute, so T ~ Exp(0.2). P(T > 10) = e^(−2) = 0.1353. P(T < 2) = 1 − e^(−0.4) = 0.3297 (4 d.p.).",
        "P(X > 15 | X > 5) = e^(−1.5)/e^(−0.5) = e^(−1) = 0.3679 = P(X > 10), by the memoryless property: having already waited 5, "
        "the further wait of at least 10 has the same probability as for a fresh start.",
        "P(X > s + t | X > s) = P(X > s + t)/P(X > s) (since X > s + t implies X > s) = e^(−λ(s + t))/e^(−λs) = e^(−λt) = P(X > t).",
        "E(X) = ∫₀^∞ λxe^(−λx) dx = [−xe^(−λx)]₀^∞ + ∫₀^∞ e^(−λx) dx = 0 + 1/λ, since xe^(−λx) → 0 as x → ∞.",
        "E(X²) = 2/λ² = 2/9. E(2X² − 3X + 1) = 4/9 − 1 + 1 = 4/9 = 0.444. E(e^X) = ∫₀^∞ 3e^(−2x) dx = 3/2.",
        "X ~ Exp(0.2), mean 5. e^(−x/5) = 0.01 gives x = 5 ln 100 = 23.0 (3 s.f.).",
        "Tyres wear out, so an old tyre is more likely to need replacing soon than a new one: the memoryless property fails. "
        "Also the standard deviation (8) is far smaller than the mean (30), whereas for an exponential they are equal.",
    ],
    "exam": [
        "The continuous random variable X has pdf f(x) = λe^(−λx) for x ≥ 0, where λ > 0. "
        "(a) Show that the cdf of X is F(x) = 1 − e^(−λx) for x ≥ 0. [2] (b) Prove that E(X) = 1/λ. [3] "
        "(c) Prove that Var(X) = 1/λ². [4] (d) Show that the median of X is (ln 2)/λ, and hence show that the median is less than the mean. [2]",
        "A machine breaks down at random at an average rate of 3 times per week (7 days). T days is the time between breakdowns. "
        "(a) State the distribution of T, giving its parameter. [2] (b) Find P(T > 4). [2] "
        "(c) Show how the answer to (b) can also be found using a Poisson distribution. [2] "
        "(d) The machine has run for 3 days without a breakdown. Find the probability that it runs for at least 2 more days without a breakdown. [3] "
        "(e) Find the probability that there are more than 15 breakdowns in a 4-week period. [2]",
        "The lifetime X hours of an electronic component is modelled by an exponential distribution with P(X > 500) = 0.6. "
        "(a) Find the parameter λ, giving your answer to 3 significant figures. [3] (b) Find the mean and the median lifetime. [3] "
        "(c) A device contains 4 such components, which fail independently. The device stops working as soon as one component fails. "
        "Find the probability that the device works for more than 200 hours. [3] "
        "(d) State one assumption needed for the exponential model, and comment on whether it is realistic. [2]",
        "X ~ Exp(2). (a) Find E(e^X). [3] (b) Y = e^(−2X). Find the cdf of Y and identify the distribution of Y. [5] "
        "(c) Hence find P(Y > 0.8), and check your answer using the distribution of X. [2] "
        "(d) Explain how a random number U from U(0, 1) on a calculator could be used to simulate a value of X. [2]",
    ],
    "exam_answers": [
        "(a) F(x) = ∫₀ˣ λe^(−λt) dt = [−e^(−λt)]₀ˣ [M1] = 1 − e^(−λx) [A1]. "
        "(b) E(X) = ∫₀^∞ λxe^(−λx) dx; parts with u = x [M1]: [−xe^(−λx)]₀^∞ + ∫₀^∞ e^(−λx) dx [A1] = 0 + 1/λ, as xe^(−λx) → 0 [A1]. "
        "(c) E(X²) = [−x²e^(−λx)]₀^∞ + ∫₀^∞ 2xe^(−λx) dx [M1 A1] = (2/λ)E(X) = 2/λ² [A1]; Var(X) = 2/λ² − 1/λ² = 1/λ² [A1]. "
        "(d) 1 − e^(−λm) = 1/2 gives m = (ln 2)/λ [B1]; ln 2 ≈ 0.693 < 1, so m < 1/λ = mean [B1].",
        "(a) T ~ Exp(3/7) [B1 B1] (rate 3/7 per day). "
        "(b) P(T > 4) = e^(−12/7) = 0.180 (3 s.f.) [M1 A1]. "
        "(c) Breakdowns in 4 days ~ Po(12/7) [M1]; P(T > 4) = P(no breakdowns in 4 days) = e^(−12/7) [A1]. "
        "(d) P(T > 5 | T > 3) = P(T > 2) by the memoryless property [M1] = e^(−6/7) [M1] = 0.424 (3 s.f.) [A1]. "
        "(e) Breakdowns in 28 days ~ Po(12) [M1]; P(N > 15) = 1 − P(N ≤ 15) = 1 − 0.8444 = 0.156 (3 s.f.) [A1].",
        "(a) e^(−500λ) = 0.6 [M1], λ = −(ln 0.6)/500 [M1] = 0.00102 (3 s.f.) [A1]. "
        "(b) Mean = 1/λ = 979 hours [B1]; median = (ln 2)/λ [M1] = 678 hours (3 s.f.) [A1]. "
        "(c) P(one component lasts > 200) = e^(−200λ) = 0.6^0.4 [M1]; all four: (e^(−200λ))⁴ = e^(−800λ) = 0.6^1.6 [M1] = 0.442 (3 s.f.) [A1]. "
        "(d) e.g. failures occur at random at a constant rate, so the component does not wear out [B1]; this is doubtful for long periods, "
        "as electronic components do age, so the model is better for shorter times [B1].",
        "(a) E(e^X) = ∫₀^∞ e^x × 2e^(−2x) dx [M1] = ∫₀^∞ 2e^(−x) dx [A1] = 2 [A1]. "
        "(b) 0 < Y ≤ 1 [B1]. G(y) = P(e^(−2X) ≤ y) = P(−2X ≤ ln y) = P(X ≥ −(ln y)/2) [M1 A1] = e^(−2 × (−(ln y)/2)) = e^(ln y) = y [A1]. "
        "G(y) = 0 for y < 0, y for 0 ≤ y ≤ 1, 1 for y > 1, so Y ~ U(0, 1) [A1]. "
        "(c) P(Y > 0.8) = 0.2 [B1]. Check: P(e^(−2X) > 0.8) = P(X < −(ln 0.8)/2) = 1 − e^(ln 0.8) = 1 − 0.8 = 0.2 [B1]. "
        "(d) By (b), e^(−2X) behaves like U, so X = −(ln U)/2 [M1]; generate U and compute −(ln U)/2 to obtain a value from Exp(2) [A1].",
    ],
}
