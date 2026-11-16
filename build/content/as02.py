UNIT = {
    "number": "AS2",
    "title": "Binomial, Poisson and discrete uniform distributions",
    "tag": "AS · Edexcel FS1, AQA, OCR A, OCR MEI · prior knowledge for IAL S3 and CAIE 9231 Paper 4 · "
           "Poisson approximation: Edexcel (and IAL S2) only",
    "notes": [
        ("p", "Three standard models cover most counting situations in this course: the binomial for a fixed number of trials, "
              "the Poisson for events in a fixed interval, and the discrete uniform for equally likely values. This unit recaps "
              "the binomial from A level Mathematics, develops the Poisson distribution fully, and shows how to choose and "
              "criticise a model. The geometric distribution has its own unit (AS3)."),

        ("h2", "2.1 The binomial distribution (recap)"),
        ("p", "X ~ B(n, p) counts the number of successes in n trials. It is the right model when all four conditions hold:"),
        ("bullets", [
            "there is a fixed number n of trials;",
            "each trial has exactly two outcomes, success or failure;",
            "the probability of success p is the same for every trial;",
            "the trials are independent.",
        ]),
        ("box", "Binomial B(n, p)", [
            "P(X = x) = C(n, x) pˣ (1 − p)ⁿ⁻ˣ,  x = 0, 1, …, n,  where C(n, x) = n!/(x!(n − x)!).",
            "E(X) = np,   Var(X) = np(1 − p).",
        ]),
        ("p", "Knowing the mean and variance lets you find n and p: Var(X)/E(X) = 1 − p. For example, mean 6 and variance 4.2 give "
              "1 − p = 0.7, so p = 0.3 and n = 6/0.3 = 20."),

        ("h2", "2.2 Proof of the binomial mean and variance (MEI SR10)"),
        ("p", "MEI asks you to prove the mean and variance in particular cases; the other boards only require you to use them. "
              "Write X = B₁ + B₂ + … + Bₙ, where Bᵢ = 1 if trial i is a success and 0 if not. Each Bᵢ is a <b>Bernoulli</b> variable: "
              "P(Bᵢ = 1) = p and P(Bᵢ = 0) = 1 − p."),
        ("bullets", [
            "E(Bᵢ) = 1 × p + 0 × (1 − p) = p, and E(Bᵢ²) = 1² × p + 0 = p, so Var(Bᵢ) = p − p² = p(1 − p).",
            "Expectations always add: E(X) = p + p + … + p = np.",
            "The trials are independent, so the variances add: Var(X) = np(1 − p).",
        ]),
        ("p", "In a 'particular case', for example n = 2, you can also list the distribution (0, 1, 2 with probabilities (1 − p)², "
              "2p(1 − p), p²) and use E(X) = Σ x P(X = x) directly; this gives 2p and 2p(1 − p)."),

        ("h2", "2.3 The Poisson distribution"),
        ("p", "X ~ Po(λ) counts how many times an event happens in a fixed interval of time or space, such as calls per hour, flaws "
              "per metre of cable, or typing errors per page. The parameter λ (lambda) is the mean number of events per interval."),
        ("box", "Poisson Po(λ)", [
            "P(X = x) = e^(−λ) λˣ / x!,   x = 0, 1, 2, …  (there is no upper limit).",
            "E(X) = λ  and  Var(X) = λ:  the mean equals the variance.",
            "Proofs are not required by any board; unit A2.4 proves them with generating functions.",
        ]),
        ("p", "<b>Conditions for a Poisson model.</b> Events must occur:"),
        ("bullets", [
            "<b>singly</b> — two events cannot happen at exactly the same moment or place;",
            "<b>independently</b> — one event does not make another more or less likely;",
            "<b>at a constant average rate</b> — the mean number per interval does not change over the period studied;",
            "<b>randomly</b> — the timing of individual events cannot be predicted.",
        ]),
        ("p", "Always explain conditions <i>in context</i>. 'Cars pass a point at random' is weak; 'cars arrive independently of each "
              "other and the average rate is constant over the hour, so rush-hour periods should be excluded' earns the mark. "
              "Typical failures: customers arriving in groups (not singly), cars in a queue behind a slow lorry (not independent), "
              "calls that peak at lunchtime (rate not constant)."),
        ("p", "<b>A data check (MEI SR11).</b> Because E(X) = Var(X), data that come from a Poisson distribution should have sample "
              "mean and sample variance roughly equal. A variance much larger than the mean (over-dispersion) suggests clustering, "
              "so a Poisson model is unlikely to fit."),

        ("h2", "2.4 Changing the interval and adding Poisson variables"),
        ("box", "Two key Poisson properties (no proofs required)", [
            "<b>Scaling.</b> If events occur at a mean rate of λ per unit interval, the number in an interval of length t is Po(λt). "
            "So 3 per minute gives Po(15) for 5 minutes and Po(1.5) for 30 seconds.",
            "<b>Additive property.</b> If X ~ Po(λ) and Y ~ Po(μ) are independent, then X + Y ~ Po(λ + μ). It extends to any "
            "number of independent Poisson variables.",
        ]),
        ("p", "Scaling only makes sense if the rate is constant across the whole interval. The additive property needs independence. "
              "Note that X − Y is <i>not</i> Poisson (it can be negative), and 2X is not Poisson either: 2X has mean 2λ but variance 4λ."),
        ("p", "<b>A useful consequence.</b> Given that X + Y = n, the number X from the first source has a binomial distribution "
              "B(n, λ/(λ + μ)), because each of the n events independently came from the first source with probability λ/(λ + μ)."),

        ("h2", "2.5 The Poisson approximation to the binomial (Edexcel; not OCR A, MEI or CAIE)"),
        ("p", "When n is large and p is small, the binomial B(n, p) is close to Po(np). The reason is that the mean np and variance "
              "np(1 − p) are almost equal when p is small, which is the defining feature of a Poisson. A common rule of thumb is "
              "n > 50 and np < 5. Edexcel FS1 (2.3) requires the approximation without derivation. OCR A excludes it, and MEI only "
              "expects you to recognise that both models could apply, not to use the approximation numerically."),
        ("p", "With a modern calculator the exact binomial is easy, so the approximation is mainly tested by asking you to justify "
              "it, use it, and compare it with the exact value."),

        ("h2", "2.6 The discrete uniform distribution and choosing a model"),
        ("p", "The discrete uniform distribution (full treatment in unit AS1) applies when a finite set of values are all equally likely: "
              "on {1, …, n}, P(X = x) = 1/n, E(X) = (n + 1)/2 and Var(X) = (n² − 1)/12. Exam questions often ask which model fits a "
              "situation, or ask you to criticise a proposed model."),
        ("table", ["Model", "What X counts", "Key conditions", "Mean", "Variance"], [
            ["Discrete uniform U(n)", "value from a list of n equally likely values", "finite set, equal probabilities", "(n + 1)/2", "(n² − 1)/12"],
            ["Binomial B(n, p)", "successes in n trials", "fixed n, two outcomes, constant p, independent", "np", "np(1 − p)"],
            ["Poisson Po(λ)", "events in a fixed interval", "singly, independently, constant rate, random", "λ", "λ"],
            ["Geometric Geo(p) (unit AS3)", "trials up to and including the first success", "constant p, independent trials", "1/p", "(1 − p)/p²"],
        ]),
        ("p", "Quick tests: if there is a fixed number of trials, think binomial; if there is no upper limit and events occur in "
              "time or space, think Poisson; if you are waiting for a first success, think geometric; if every value is equally likely, "
              "think uniform. Then check the conditions, and the mean–variance relationship (Var < mean for the binomial, "
              "Var = mean for the Poisson)."),

        ("h2", "2.7 Using cumulative tables and the calculator"),
        ("p", "Tables and calculator 'cumulative' functions give P(X ≤ x). Turn every other inequality into this form first. For a "
              "variable taking integer values:"),
        ("table", ["You need", "Write it as", "Example with X ~ Po(3.5)"], [
            ["P(X ≤ a)", "F(a)", "P(X ≤ 4) = 0.7254"],
            ["P(X < a)", "F(a − 1)", "P(X < 4) = P(X ≤ 3) = 0.5366"],
            ["P(X ≥ a)", "1 − F(a − 1)", "P(X ≥ 2) = 1 − P(X ≤ 1) = 1 − 0.1359 = 0.8641"],
            ["P(X > a)", "1 − F(a)", "P(X > 4) = 1 − 0.7254 = 0.2746"],
            ["P(a ≤ X ≤ b)", "F(b) − F(a − 1)", "P(2 ≤ X ≤ 5) = 0.8576 − 0.1359 = 0.7217"],
        ]),
        ("p", "Edexcel prints binomial and Poisson cumulative tables (Tables 7–17 at the back of this book are in the same form); "
              "AQA, OCR and CAIE candidates use the calculator. Write down the distribution and the probability you want, e.g. "
              "'X ~ Po(3.5), P(X ≥ 2) = 1 − P(X ≤ 1)', before you press any keys: that line earns the method mark."),
        ("warn", "Common mistakes", [
            "P(X ≥ 3) = 1 − P(X ≤ 3). It is 1 − P(X ≤ 2).",
            "Forgetting to rescale λ when the interval changes, or rescaling a binomial n instead of a Poisson mean.",
            "Stating Poisson conditions without context, or giving 'events are independent' when the question asks for two conditions "
            "and then repeating it in other words.",
            "Using the additive property for variables that are not independent, or claiming 2X ~ Po(2λ).",
            "Using the Poisson approximation when p is not small (e.g. B(60, 0.4)); the mean and variance are then very different.",
            "Using the sample variance with divisor n − 1 or n inconsistently: either is acceptable for the mean–variance check, but say which.",
        ]),
    ],
    "examples": [
        {
            "title": "Binomial probabilities from cumulative tables",
            "question": "20% of seeds of a certain type fail to germinate. A packet contains 15 seeds. Assuming the seeds fail "
                        "independently, find the probability that (a) at most 3 fail, (b) at least 5 fail, (c) more than 2 but at most 6 fail.",
            "steps": [
                "Let X be the number that fail. X ~ B(15, 0.2).",
                "(a) P(X ≤ 3) = 0.6482 (tables or calculator).",
                "(b) P(X ≥ 5) = 1 − P(X ≤ 4) = 1 − 0.8358 = 0.1642.",
                "(c) P(2 < X ≤ 6) = P(X ≤ 6) − P(X ≤ 2) = 0.9819 − 0.3980 = 0.5839.",
            ],
        },
        {
            "title": "Poisson probabilities and changing the interval",
            "question": "Emails arrive in an inbox at random at a mean rate of 4 per hour. Find the probability that (a) exactly 6 arrive "
                        "in an hour, (b) at least 3 arrive in a 30-minute period, (c) more than 10 arrive in 2 hours.",
            "steps": [
                "(a) X ~ Po(4). P(X = 6) = e⁻⁴ 4⁶/6! = 0.1042 (4 d.p.).",
                "(b) In 30 minutes the mean is 4 × 0.5 = 2, so Y ~ Po(2). P(Y ≥ 3) = 1 − P(Y ≤ 2) = 1 − 0.6767 = 0.3233.",
                "(c) In 2 hours, W ~ Po(8). P(W > 10) = 1 − P(W ≤ 10) = 1 − 0.8159 = 0.1841.",
            ],
        },
        {
            "title": "The additive property, and a conditional probability",
            "question": "Machine A breaks down a mean of 2.5 times per month and machine B a mean of 1.5 times per month, "
                        "independently, each according to a Poisson distribution. (a) Find the probability of at most 2 breakdowns in "
                        "total in a month. (b) Given there were 4 breakdowns in total in a month, find the probability that exactly 2 were "
                        "on machine A.",
            "steps": [
                "(a) X ~ Po(2.5) and Y ~ Po(1.5) are independent, so T = X + Y ~ Po(4). P(T ≤ 2) = 0.2381.",
                "(b) P(X = 2 | T = 4) = P(X = 2) P(Y = 2)/P(T = 4), using independence of X and Y.",
                "This equals C(4, 2) (2.5/4)² (1.5/4)², the binomial B(4, 0.625) probability of 2: 6 × 0.625² × 0.375² = 0.3296 (4 d.p.).",
            ],
        },
        {
            "title": "Poisson approximation to the binomial (Edexcel)",
            "question": "1.5% of bolts made by a machine are faulty. A box holds 200 bolts. Use a suitable approximation to find the "
                        "probability that a box contains at most 2 faulty bolts, and compare with the exact value.",
            "steps": [
                "X ~ B(200, 0.015). n is large and p is small (np = 3 < 5), so X is approximately Po(3).",
                "P(X ≤ 2) ≈ e⁻³(1 + 3 + 9/2) = 0.4232 (tables: Po(3), x = 2).",
                "Exact binomial: P(X ≤ 2) = 0.4215. The approximation is good to about 0.002.",
            ],
        },
        {
            "title": "Checking a Poisson model against data (MEI, Edexcel)",
            "question": "The number of customers arriving at a kiosk was recorded in 80 one-minute intervals: 0 customers in 14 intervals, "
                        "1 in 24, 2 in 21, 3 in 13, 4 in 6 and 5 in 2. Is a Poisson model reasonable? Use it to estimate the number of "
                        "intervals with no customers.",
            "steps": [
                "Σfx = 24 + 42 + 39 + 24 + 10 = 139, so x̄ = 139/80 = 1.7375 ≈ 1.74.",
                "Σfx² = 24 + 84 + 117 + 96 + 50 = 371, so the variance is 371/80 − 1.7375² = 1.6186 ≈ 1.62 (divisor n).",
                "The mean and variance are close, which supports a Poisson model (customers arriving singly and independently at a constant rate).",
                "Using Po(1.7375): P(X = 0) = e^(−1.7375) = 0.1760, so the expected number of intervals is 80 × 0.1760 ≈ 14.1, close to the 14 observed.",
            ],
        },
        {
            "title": "Finding binomial parameters and criticising a model",
            "question": "X ~ B(n, p) has mean 6 and variance 4.2. Find n and p. Explain why B(n, p) would not be a good model for the "
                        "number of days in a 20-day period on which a particular train is late.",
            "steps": [
                "np = 6 and np(1 − p) = 4.2, so 1 − p = 4.2/6 = 0.7. Hence p = 0.3 and n = 6/0.3 = 20.",
                "Lateness on different days is unlikely to be independent (bad weather or engineering works last several days), and "
                "the probability of being late is unlikely to be constant (it may be higher on Mondays or in winter). Both binomial "
                "conditions are doubtful.",
            ],
        },
    ],
    "practice": [
        "X ~ B(12, 0.35). Find P(X = 4), P(X ≤ 4) and P(X > 6), giving answers to 4 decimal places.",
        "X ~ B(n, p) has mean 4.8 and variance 2.88. Find n and p.",
        "Y ~ Po(2.5). Find P(Y = 0) and P(Y = 2). Give both answers to 4 decimal places.",
        "X ~ Po(3.5). Find P(X ≤ 4), P(X ≥ 2) and P(2 ≤ X ≤ 5).",
        "Flaws occur in a roll of cloth at random at a mean rate of 1.2 per 10 m. Find the probability that a 25 m length has "
        "(a) no flaws, (b) at most 2 flaws.",
        "X ~ Po(3) and Y ~ Po(4) are independent. Find the distribution of X + Y and hence P(X + Y = 7) to 4 decimal places.",
        "A student models the number of cars passing a school gate between 8:00 and 9:00 a.m. by a Poisson distribution. Give two "
        "reasons, in context, why this model may not be suitable.",
        "(Edexcel) X ~ B(200, 0.01). Use a suitable Poisson approximation to find P(X ≤ 1) to 4 decimal places. State the "
        "approximation you use and why it is valid.",
        "In a sample, the number of weeds per square metre of a lawn had mean 2.1 and variance 4.8. Comment on whether a Poisson "
        "distribution is a suitable model, and suggest a reason in context.",
        "A random variable X is uniformly distributed on the integers 1 to 12. Find P(X > 9), E(X) and Var(X).",
        "Name a suitable distribution, with its parameter(s), for each of the following. (a) The number of sixes in 30 rolls of a fair "
        "die. (b) The number of typing errors on a page of a report. (c) The score on one spin of a fair spinner numbered 1 to 10. "
        "(d) The number of rolls of a fair die up to and including the first six.",
        "X ~ Po(λ) and P(X = 2) = P(X = 3). Find λ and hence P(X ≤ 3).",
    ],
    "answers": [
        "P(X = 4) = C(12, 4)(0.35)⁴(0.65)⁸ = 0.2367. P(X ≤ 4) = 0.5833. P(X > 6) = 1 − P(X ≤ 6) = 1 − 0.9154 = 0.0846.",
        "1 − p = 2.88/4.8 = 0.6, so p = 0.4 and n = 4.8/0.4 = 12.",
        "P(Y = 0) = e^(−2.5) = 0.0821. P(Y = 2) = e^(−2.5) × 2.5²/2 = 0.2565.",
        "P(X ≤ 4) = 0.7254. P(X ≥ 2) = 1 − P(X ≤ 1) = 1 − 0.1359 = 0.8641. P(2 ≤ X ≤ 5) = 0.8576 − 0.1359 = 0.7217.",
        "The mean for 25 m is 1.2 × 2.5 = 3, so X ~ Po(3). (a) P(X = 0) = e⁻³ = 0.0498. (b) P(X ≤ 2) = 0.4232.",
        "X + Y ~ Po(7) by the additive property (independence). P(X + Y = 7) = e⁻⁷ × 7⁷/7! = 0.1490.",
        "Any two, in context: cars may arrive in groups or queues, so not singly or independently; the rate is unlikely to be constant "
        "over the hour (a peak just before 9:00 as parents drop children off); traffic lights upstream release cars in batches.",
        "Use Po(2), λ = np = 2. Valid because n is large and p is small (np < 5). P(X ≤ 1) ≈ e⁻²(1 + 2) = 3e⁻² = 0.4060 "
        "(exact binomial 0.4046).",
        "For a Poisson distribution the mean and variance are equal. Here the variance (4.8) is more than twice the mean (2.1), so a "
        "Poisson model is not suitable. Weeds tend to grow in clumps (seeds spread from a parent plant), so they do not occur independently.",
        "P(X > 9) = 3/12 = 0.25. E(X) = 13/2 = 6.5. Var(X) = (144 − 1)/12 = 143/12 ≈ 11.9.",
        "(a) B(30, 1/6). (b) Po(λ), with λ the mean number of errors per page. (c) Discrete uniform on {1, …, 10}. (d) Geo(1/6).",
        "e^(−λ)λ²/2 = e^(−λ)λ³/6 gives λ = 3 (λ > 0). P(X ≤ 3) = e⁻³(1 + 3 + 4.5 + 4.5) = 13e⁻³ = 0.6472.",
    ],
    "exam": [
        "Calls arrive at a booking office at random at a mean rate of 6 per 10 minutes. (a) State two conditions needed for a Poisson "
        "model to be suitable, in context. [2]  (b) Find the probability of exactly 4 calls in a 10-minute period. [2]  (c) Find the "
        "probability of more than 2 calls in a 5-minute period. [2]  (d) Find the probability that each of three separate 5-minute "
        "periods has more than 2 calls. [2]  (e) The manager says the office can deal with at most 30 calls in an hour. Find the "
        "probability that this is enough in a randomly chosen hour. [2]",
        "Shop A sells a particular phone at a mean rate of 1.8 per day and shop B at a mean rate of 2.7 per day. Daily sales at the two "
        "shops are independent Poisson variables. (a) Find the probability that at least 5 phones are sold in total on a given day. [3]  "
        "(b) On one day 6 phones were sold in total. Find the probability that exactly 2 of them were sold by shop A. [4]  "
        "(c) Find the probability that fewer than 20 phones are sold in total over 5 days. [2]  (d) Give a reason why the sales at the "
        "two shops might not be independent. [1]",
        "(Edexcel) 2% of the bolts made in a factory are defective. Bolts are packed in boxes of 150, and defects occur independently. "
        "(a) Explain why a Poisson distribution can be used to approximate the number of defective bolts in a box, and give its "
        "parameter. [3]  (b) Use your approximation to find the probability that a box contains at most 2 defective bolts, and find the "
        "exact binomial probability for comparison. [3]  (c) Use your approximation to find the probability that a box contains more than "
        "4 defective bolts. [2]  (d) A customer buys 10 boxes. Find the probability that exactly one of them contains more than 4 "
        "defective bolts. [3]",
        "The numbers of goals scored by a team in 100 matches were: 0 goals in 22 matches, 1 in 33, 2 in 25, 3 in 13, 4 in 5 and 5 in 2. "
        "(a) Find the mean and the variance (divisor n) of the number of goals per match. [4]  (b) Explain why your answers support a "
        "Poisson model. [2]  (c) Using a Poisson distribution with mean equal to your answer to (a), find the probability of no goals in a "
        "match, and the expected number of matches with no goals. [3]  (d) Give one reason, in context, why the Poisson model might not "
        "be appropriate. [1]",
    ],
    "exam_answers": [
        "(a) Any two in context (B1 B1): calls arrive singly (not two at the same instant); calls are independent of each other; "
        "the mean rate is constant over the period.  (b) X ~ Po(6): P(X = 4) = e⁻⁶ 6⁴/4! = 0.1339 (M1 A1).  "
        "(c) Y ~ Po(3): P(Y > 2) = 1 − P(Y ≤ 2) = 1 − 0.4232 = 0.5768 (M1 A1).  (d) 0.5768³ = 0.1919 (M1 A1), using independence of "
        "non-overlapping periods.  (e) W ~ Po(36) (B1): P(W ≤ 30) = 0.1806 by calculator (B1).",
        "(a) T ~ Po(4.5) (B1). P(T ≥ 5) = 1 − P(T ≤ 4) (M1) = 1 − 0.5321 = 0.4679 (A1).  "
        "(b) P(A = 2 | T = 6) = P(A = 2)P(B = 4)/P(T = 6) (M1 M1); this is B(6, 1.8/4.5) = B(6, 0.4) (A1): "
        "C(6, 2)(0.4)²(0.6)⁴ = 0.3110 (A1).  (c) Over 5 days the total is Po(22.5) (B1); P(total ≤ 19) = 0.2705 (B1).  "
        "(d) For example, the shops are near each other and compete for the same customers, or both are affected by the same "
        "promotions or the day of the week (B1).",
        "(a) X ~ B(150, 0.02) (B1); n is large and p is small, np = 3 < 5 (B1); X ≈ Po(3) (B1).  (b) P(X ≤ 2) ≈ 0.4232 (M1 A1); "
        "exact binomial 0.4209 (B1).  (c) P(X > 4) ≈ 1 − P(X ≤ 4) = 1 − 0.8153 = 0.1847 (M1 A1).  (d) Y ~ B(10, 0.1847) (M1); "
        "P(Y = 1) = 10 × 0.1847 × 0.8153⁹ (M1) = 0.2940 (A1).",
        "(a) Σfx = 33 + 50 + 39 + 20 + 10 = 152 (M1), mean = 1.52 (A1). Σfx² = 33 + 100 + 117 + 80 + 50 = 380 (M1), variance = "
        "3.80 − 1.52² = 1.4896 ≈ 1.49 (A1).  (b) For a Poisson distribution mean = variance (B1); 1.52 and 1.49 are very close (B1).  "
        "(c) P(X = 0) = e^(−1.52) = 0.2187 (M1 A1); expected number 100 × 0.2187 ≈ 21.9 matches, close to the 22 observed (A1).  "
        "(d) For example, the scoring rate depends on the strength of the opponent, so it is not constant from match to match; or one "
        "goal may change how the team plays, so goals are not independent (B1).",
    ],
}
