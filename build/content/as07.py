UNIT = {
    "number": "AS7",
    "title": "Chi-squared goodness-of-fit tests",
    "tag": "AS · Edexcel FS1, OCR A, OCR MEI · IAL S3 · CAIE 9231 P4 · not on AQA "
           "(geometric fits: Edexcel A level, OCR A A level, CAIE; continuous fits: IAL S3, OCR A A level, CAIE)",
    "notes": [
        ("h2", "7.1 What a goodness-of-fit test does"),
        ("p", "You have a frequency table of data and a proposed probability model, such as “the die is fair” or "
              "“the number of flaws per metre has a Poisson distribution”. A <b>goodness-of-fit test</b> asks whether the "
              "observed frequencies O are close enough to the frequencies E that the model predicts. Large differences are "
              "evidence against the model."),
        ("box", "The test statistic", [
            "X² = Σ (O − E)²/E, summed over all classes (after any combining).",
            "Equivalent form, often quicker: X² = Σ O²/E − N, where N = ΣO = ΣE is the total frequency.",
            "If H₀ is true and every E is large enough, X² has approximately a χ² distribution with ν degrees of freedom: X² ≈ χ²<sub>ν</sub>.",
            "H₀: the proposed distribution is a suitable model for the data.  H₁: it is not a suitable model.",
            "Reject H₀ if X² > the upper-tail critical value (or if the p-value is below the significance level).",
        ]),
        ("p", "Each term (O − E)²/E is the <b>contribution</b> of that class. Squaring makes every term positive, so both "
              "too many and too few observations increase X². Dividing by E scales the difference: a shortfall of 5 matters "
              "more when 10 are expected than when 100 are expected. Because any disagreement makes X² larger, the test always "
              "uses the <b>upper tail</b> of χ², even though H₁ is just “not a good model”."),
        ("p", "Write hypotheses in words and name both the distribution and the context, for example "
              "“H₀: a Poisson distribution is a suitable model for the number of flaws per length of cloth”. "
              "Cambridge examiners report that vague hypotheses such as “the data fit” lose marks."),
        ("h2", "7.2 Expected frequencies"),
        ("p", "Under H₀, the expected frequency of a class is E = N × P(class), where N is the total number of observations "
              "and the probability comes from the model. Keep the expected frequencies unrounded in your calculator, and write "
              "them to 2 decimal places. Never round them to whole numbers: they are long-run averages, not counts."),
        ("bullets", [
            "The final class must be open, such as “5 or more”, so that the probabilities add to 1. Find it by subtraction: "
            "P(X ≥ 5) = 1 − P(X ≤ 4), and E(last class) = N − (sum of the other E).",
            "For a continuous model, the first and last classes are extended to −∞ and +∞ (or to the ends of the range of X), "
            "for the same reason.",
            "Check that ΣE = ΣO = N. This is a good check on your arithmetic.",
        ]),
        ("h2", "7.3 Combining classes so that every E ≥ 5"),
        ("p", "The χ² distribution is only a good approximation to the distribution of X² when the expected frequencies are "
              "not too small. A tiny E in the denominator can give one class a huge, misleading contribution. The rule used by "
              "every board is: <b>combine adjacent classes until each expected frequency is at least 5</b>. Combine the matching "
              "observed frequencies too. Usually it is the tail classes that are small."),
        ("bullets", [
            "Combine <b>adjacent</b> classes (for example 4, 5 and “6 or more” into “4 or more”), so the classes still make sense.",
            "Decide on combining using E only, never O.",
            "Count the classes <b>after</b> combining when you find the degrees of freedom.",
            "OCR MEI: you must know that classes are combined, but you will not have to decide how in the exam (SH3).",
        ]),
        ("h2", "7.4 Degrees of freedom and estimated parameters"),
        ("box", "Degrees of freedom", [
            "ν = k − 1 − m, where k = number of classes after combining and m = number of parameters estimated from the data.",
            "The “− 1” is there because the expected frequencies are forced to have the same total N as the data.",
            "Each parameter estimated from the data makes the model fit the data more closely, so another degree of freedom is lost.",
            "A parameter that is given by H₀ (for example “λ = 2” or “p = 0.25”) is not estimated, so it costs nothing.",
        ]),
        ("table", ["Model", "Parameter(s) and usual estimate", "ν if the parameters are given", "ν if estimated from the data"], [
            ["Discrete uniform, or a given ratio such as 9 : 3 : 3 : 1", "none", "k − 1", "–"],
            ["Binomial B(n, p), n known", "p̂ = x̄/n", "k − 1", "k − 2"],
            ["Poisson Po(λ)", "λ̂ = x̄", "k − 1", "k − 2"],
            ["Geometric Geo(p)", "p̂ = 1/x̄ (since E(X) = 1/p)", "k − 1", "k − 2"],
            ["Normal N(μ, σ²)", "μ̂ = x̄, σ̂ = s", "k − 1", "k − 2 (one estimated), k − 3 (both)"],
            ["Continuous uniform U(a, b), a and b known", "none", "k − 1", "–"],
            ["Given pdf with constants found from f integrating to 1", "none from the data", "k − 1", "k − 1 − (constants found from the data)"],
        ]),
        ("p", "For a binomial model, n is the fixed number of trials and is never estimated. For a Poisson model, a useful "
              "preliminary check is that the sample mean and variance are similar, because E(X) = Var(X) = λ."),
        ("h2", "7.5 Critical values, p-values and conclusions"),
        ("p", "Find the critical value from the χ² table (Table 4 of this book) using the upper-tail probability equal to the "
              "significance level. Most calculators also give the p-value P(χ²<sub>ν</sub> ≥ X²) directly, which every board accepts."),
        ("table", ["ν", "10%", "5%", "2.5%", "1%"], [
            ["1", "2.706", "3.841", "5.024", "6.635"],
            ["2", "4.605", "5.991", "7.378", "9.210"],
            ["3", "6.251", "7.815", "9.348", "11.345"],
            ["4", "7.779", "9.488", "11.143", "13.277"],
            ["5", "9.236", "11.070", "12.833", "15.086"],
            ["6", "10.645", "12.592", "14.449", "16.812"],
            ["7", "12.017", "14.067", "16.013", "18.475"],
            ["8", "13.362", "15.507", "17.535", "20.090"],
        ]),
        ("bullets", [
            "X² > critical value: reject H₀. “There is sufficient evidence at the 5% level that the Poisson distribution is not a suitable model for …”",
            "X² < critical value: do not reject H₀. “There is insufficient evidence at the 5% level to reject the Poisson model; it may be a suitable model for …”",
            "Never say the test proves the model is correct. Not rejecting H₀ only means the data are consistent with it.",
        ]),
        ("h2", "7.6 Fitting discrete distributions"),
        ("bullets", [
            "<b>Discrete uniform and given ratios</b> (all boards; OCR A AS): each E = N × (share of the ratio). E.g. for 9 : 3 : 3 : 1 "
            "and N = 160, E = 90, 30, 30, 10.",
            "<b>Binomial</b> (Edexcel, IAL S3, OCR A A level, MEI, CAIE): E = N × C(n, x) pˣ(1 − p)ⁿ⁻ˣ. If p is estimated, use p̂ = Σfx/(nN).",
            "<b>Poisson</b> (Edexcel, IAL S3, OCR A A level, MEI, CAIE): E = N × e^(−λ)λˣ/x!. If λ is estimated, use λ̂ = x̄.",
            "<b>Geometric</b> (Edexcel A level only, OCR A A level, CAIE): E = N × (1 − p)^(x−1) p for x = 1, 2, …, and "
            "the last class uses P(X ≥ k) = (1 − p)^(k−1). If p is estimated, use p̂ = 1/x̄.",
        ]),
        ("p", "Recurrence relations save time. For the Poisson, P(X = x + 1) = P(X = x) × λ/(x + 1). For the binomial, "
              "P(X = x + 1) = P(X = x) × (n − x)p/((x + 1)(1 − p)). For the geometric, each probability is (1 − p) times the one before."),
        ("h2", "7.7 Fitting continuous distributions (IAL S3, OCR A A level, CAIE)"),
        ("p", "For grouped continuous data, find the probability of each class interval from the model and multiply by N. "
              "For a normal model use Φ: P(a < X < b) = Φ((b − μ)/σ) − Φ((a − μ)/σ). For a continuous uniform model on [a, b], "
              "the probability of an interval is its length divided by (b − a). For a given pdf f, integrate f over each interval. "
              "Extend the end classes to the ends of the range so that the probabilities total 1."),
        ("p", "OCR MEI excludes a χ² test for a normal model. Instead MEI students interpret a Normal probability plot "
              "(points close to a straight line suggest normality) and software output for the Kolmogorov–Smirnov test, where "
              "a small p-value is evidence against normality."),
        ("h2", "7.8 Interpreting the result"),
        ("bullets", [
            "Look at the contributions. The classes with the largest (O − E)²/E show where the model fails, and comparing O with "
            "E says how (for example “more zeros than a Poisson model predicts”).",
            "Software (OCR MEI SH4) often prints X², ν and the p-value. Compare the p-value with the significance level.",
            "A very small X² (in the lower tail, e.g. below the 0.995 point of χ²<sub>ν</sub>) means the data fit “too well”. This may "
            "suggest the data were invented or the observations were not independent.",
            "The conclusion depends on the significance level, so always state it. A result can be significant at 10% but not at 5%.",
        ]),
        ("warn", "Common mistakes", [
            "Rounding expected frequencies to whole numbers, or using rounded probabilities that do not add to 1.",
            "Forgetting the open-ended last class, so ΣE is less than N.",
            "Combining classes because O is small; the rule is about E.",
            "Counting classes before combining, or forgetting to subtract one for each estimated parameter.",
            "Subtracting a degree of freedom for a parameter that was given in H₀, not estimated.",
            "Using the 5% value for the wrong ν, or using a lower-tail value.",
            "Writing “the data prove the model” or “accept that it is Poisson”. Say the model may be suitable.",
        ]),
    ],
    "examples": [
        {
            "title": "A discrete uniform model",
            "question": "A school records the number of student absences on each weekday over one term: Monday 38, Tuesday 22, "
                        "Wednesday 25, Thursday 27, Friday 38. Test, at the 5% level, whether absences are equally likely on each "
                        "weekday.",
            "steps": [
                "H₀: a discrete uniform distribution over the five weekdays is a suitable model for the day of an absence. "
                "H₁: it is not a suitable model.",
                "N = 150, so each E = 150/5 = 30. All E ≥ 5, so no classes are combined.",
                "Contributions: 64/30 = 2.133, 64/30 = 2.133, 25/30 = 0.833, 9/30 = 0.300, 64/30 = 2.133. X² = 226/30 = 7.53 (3 s.f.).",
                "k = 5 classes, no parameters estimated, so ν = 5 − 1 = 4. The 5% critical value is 9.488.",
                "7.53 < 9.488, so do not reject H₀. There is insufficient evidence at the 5% level that absences are not "
                "equally likely on each weekday. (The large Monday and Friday contributions might be worth watching.)",
            ],
        },
        {
            "title": "A binomial model with a given p, combining classes",
            "question": "A quiz has 6 multiple-choice questions, each with 4 options. 120 students who had not studied the topic "
                        "took the quiz. The numbers of correct answers were: 0: 12, 1: 36, 2: 42, 3: 19, 4: 8, 5: 2, 6: 1. "
                        "Test, at the 5% level, whether the students were simply guessing.",
            "steps": [
                "If they guess, the number correct X ~ B(6, 0.25). H₀: B(6, 0.25) is a suitable model for the number of correct "
                "answers. H₁: it is not.",
                "P(X = 0, …, 6) = 0.1780, 0.3560, 0.2966, 0.1318, 0.0330, 0.0044, 0.0002. Multiply by 120: "
                "E = 21.36, 42.71, 35.60, 15.82, 3.96, 0.53, 0.03.",
                "The last three are below 5, and their total, 4.51 (from the unrounded values), is still below 5, so combine 3, 4, 5 and 6 into "
                "“3 or more”: E = 20.33, O = 19 + 8 + 2 + 1 = 30.",
                "Classes 0, 1, 2, 3+: O = 12, 36, 42, 30; E = 21.36, 42.71, 35.60, 20.33. Contributions 4.100, 1.056, 1.152, 4.597. "
                "X² = 10.9 (3 s.f.).",
                "k = 4 and p = 0.25 is given, not estimated, so ν = 4 − 1 = 3. The 5% critical value is 7.815.",
                "10.9 > 7.815, so reject H₀. There is sufficient evidence at the 5% level that the students were not just guessing. "
                "The biggest contributions show fewer scores of 0 and more scores of 3 or more than guessing predicts, "
                "suggesting some knowledge.",
            ],
        },
        {
            "title": "A Poisson model with λ estimated",
            "question": "The numbers of flaws in 100 lengths of cloth were: 0: 22, 1: 25, 2: 22, 3: 14, 4: 10, 5: 5, 6: 2. "
                        "(a) Find the mean and variance of the data and comment. (b) Test, at the 5% level, whether a Poisson "
                        "distribution is a suitable model. (c) Would the conclusion change at the 10% level?",
            "steps": [
                "(a) Σfx = 188, so x̄ = 1.88. Σfx² = 596, so the variance is 596/100 − 1.88² = 2.43 (3 s.f.). The variance is "
                "rather larger than the mean, which casts some doubt on a Poisson model.",
                "(b) H₀: a Poisson distribution is a suitable model for the number of flaws per length. H₁: it is not. "
                "Estimate λ by x̄ = 1.88.",
                "P(X = 0) = e^(−1.88) = 0.1526, then use P(X = x + 1) = P(X = x) × 1.88/(x + 1). E = 15.26, 28.69, 26.97, 16.90, 7.94 "
                "for 0 to 4, and E(5 or more) = 4.25.",
                "4.25 < 5, so combine 5+ with 4: E(4 or more) = 12.19, O = 10 + 5 + 2 = 17.",
                "Contributions for 0, 1, 2, 3, 4+: 2.978, 0.474, 0.914, 0.497, 1.898. X² = 6.76 (3 s.f.).",
                "k = 5 and λ was estimated, so ν = 5 − 1 − 1 = 3. The 5% critical value is 7.815. 6.76 < 7.815, so do not reject "
                "H₀: there is insufficient evidence at the 5% level that the Poisson model is unsuitable.",
                "(c) The 10% critical value is 6.251, and 6.76 > 6.251, so H₀ would be rejected at the 10% level. The large "
                "contributions from 0 and 4+ (more of each than predicted) match the variance being larger than the mean.",
            ],
        },
        {
            "title": "A geometric model with p estimated (Edexcel A level, OCR A, CAIE)",
            "question": "A games designer thinks the number of attempts X a player needs to complete a level has a geometric "
                        "distribution. For 80 players: 1 attempt: 34, 2: 14, 3: 12, 4: 10, 5: 4, and the other six players needed "
                        "6, 6, 7, 7, 8 and 8 attempts. Test the designer's model at the 5% level.",
            "steps": [
                "Σx = 34 + 28 + 36 + 40 + 20 + 42 = 200, so x̄ = 2.5. Since E(X) = 1/p, estimate p̂ = 1/2.5 = 0.4.",
                "H₀: Geo(p) is a suitable model for the number of attempts. H₁: it is not.",
                "P(X = x) = 0.6^(x−1) × 0.4. E = 80 × 0.4 = 32, 80 × 0.24 = 19.2, 11.52, 6.912 for x = 1 to 4. "
                "E(5) = 4.147 is below 5, so use “5 or more”: P(X ≥ 5) = 0.6⁴ = 0.1296, E = 10.37, O = 4 + 6 = 10.",
                "Contributions: 0.125, 1.408, 0.020, 1.380, 0.013. X² = 2.95 (3 s.f.).",
                "k = 5, one parameter estimated, so ν = 5 − 1 − 1 = 3. The 5% critical value is 7.815.",
                "2.95 < 7.815, so do not reject H₀. There is insufficient evidence at the 5% level against the designer's "
                "geometric model; it appears to be a suitable model, with p ≈ 0.4.",
            ],
        },
        {
            "title": "A normal model with μ and σ estimated (IAL S3, OCR A A level, CAIE)",
            "question": "The masses of 200 apples were grouped: under 90 g: 12, 90–100: 26, 100–110: 64, 110–120: 55, 120–130: 33, "
                        "130 g and over: 10. The sample mean and standard deviation were 110 g and 12 g. Test, at the 5% level, "
                        "whether a normal distribution is a suitable model.",
            "steps": [
                "H₀: a normal distribution is a suitable model for the masses. H₁: it is not. Use X ~ N(110, 12²).",
                "Standardise the boundaries: z = (90 − 110)/12 = −1.667, (100 − 110)/12 = −0.833, 0, 0.833, 1.667. "
                "The end classes are extended to −∞ and +∞.",
                "P(X < 90) = Φ(−1.667) = 0.0478, P(90 < X < 100) = 0.2023 − 0.0478 = 0.1545, P(100 < X < 110) = 0.5 − 0.2023 = 0.2977, "
                "and the other three are the same by symmetry.",
                "E = 200 × P = 9.56, 30.91, 59.53, 59.53, 30.91, 9.56. All are at least 5.",
                "Contributions: 0.624, 0.779, 0.335, 0.345, 0.142, 0.020. X² = 2.25 (3 s.f.).",
                "k = 6, two parameters estimated, so ν = 6 − 1 − 2 = 3. The 5% critical value is 7.815.",
                "2.25 < 7.815, so do not reject H₀. There is insufficient evidence at the 5% level that the masses are not normally "
                "distributed; N(110, 12²) may be a suitable model.",
            ],
        },
    ],
    "practice": [
        "X ~ B(4, 0.3) is proposed as a model for 200 observations. (a) Find the expected frequencies for x = 0, 1, 2, 3, 4 to "
        "2 decimal places. (b) Which classes must be combined before a χ² test? (c) How many degrees of freedom would the test have?",
        "Find the number of degrees of freedom in each case. (a) A discrete uniform model for the digits 0 to 9. (b) A Poisson model "
        "with λ estimated from the data, 7 classes, of which the last three are combined into one. (c) A binomial B(5, 0.4) model "
        "with 6 classes, of which the last two are combined. (d) A normal model with μ and σ both estimated, 8 classes. "
        "(e) A geometric model with p estimated, 6 classes.",
        "A die is rolled 120 times. The scores 1 to 6 occur 17, 21, 18, 19, 24 and 21 times. Test at the 5% level whether the die is fair.",
        "Genetic theory predicts that four types of plant occur in the ratio 9 : 3 : 3 : 1. In a sample of 160 plants the numbers "
        "were 98, 30, 22 and 10. Test the theory at the 5% level.",
        "Three coins are tossed together 200 times. The numbers of heads were: 0 heads 22 times, 1 head 95 times, 2 heads 61 times, "
        "3 heads 22 times. Test, at the 5% level and then at the 1% level, whether B(3, 0.5) is a suitable model.",
        "A model with one parameter estimated from the data gives expected frequencies 2.4, 6.8, 12.5, 15.1, 9.7, 3.5 for six "
        "ordered classes. The observed frequencies are 4, 5, 14, 13, 10, 4. Combine classes as necessary and carry out the test at "
        "the 5% level.",
        "A help desk claims that emails arrive at a mean rate of 2 per hour, following a Poisson distribution. Over 120 one-hour "
        "periods the numbers of emails were: 0: 12, 1: 30, 2: 35, 3: 24, 4: 12, 5 or more: 7. Test the claim at the 5% level.",
        "(OCR MEI style) 100 customers each choose one of five ice-cream flavours: A 18, B 24, C 30, D 18, E 10. Software tests "
        "whether all flavours are equally popular and prints: Chi-squared = 11.2, DF = 4, p-value = 0.0244. (a) State the "
        "conclusion at the 5% and the 1% levels. (b) Which flavours contribute most to the statistic, and what does this show?",
        "A Poisson model with λ estimated from the data is fitted. After combining there are 7 classes and X² = 13.9. State the "
        "degrees of freedom and the conclusion at the 5% level and at the 1% level.",
        "(Edexcel A level, OCR A, CAIE) X ~ Geo(0.3) is proposed for 100 observations, grouped as x = 1, 2, 3, 4 and “5 or more”. "
        "Find the expected frequencies and the degrees of freedom of the test.",
        "(IAL S3, OCR A A level, CAIE) The times past the hour (in minutes) at which 90 buses arrived at a stop were grouped into "
        "intervals 0–10, 10–20, …, 50–60 with frequencies 12, 18, 11, 19, 14, 16. Test, at the 5% level, whether a continuous "
        "uniform distribution on [0, 60] is a suitable model.",
        "A student tests a model with 6 classes and no estimated parameters and finds X² = 0.21. Use the lower-tail values in the "
        "χ² table to comment on this result.",
    ],
    "answers": [
        "(a) E = 48.02, 82.32, 52.92, 15.12, 1.62. (b) E(4) = 1.62 < 5, so combine x = 3 and 4: E = 16.74. (c) 4 classes and "
        "p is given, so ν = 4 − 1 = 3.",
        "(a) 10 − 1 = 9. (b) 5 classes after combining, 1 estimated: 5 − 1 − 1 = 3. (c) 5 classes, nothing estimated: 4. "
        "(d) 8 − 1 − 2 = 5. (e) 6 − 1 − 1 = 4.",
        "H₀: the die is fair (discrete uniform model). E = 20 each. X² = (9 + 1 + 4 + 1 + 16 + 1)/20 = 1.6. ν = 5, critical value "
        "11.070. 1.6 < 11.070: do not reject H₀; insufficient evidence that the die is biased.",
        "E = 90, 30, 30, 10. X² = 64/90 + 0 + 64/30 + 0 = 2.84 (3 s.f.). ν = 3, critical value 7.815. Do not reject H₀: the data "
        "are consistent with the 9 : 3 : 3 : 1 ratio.",
        "E = 25, 75, 75, 25. X² = 0.36 + 5.333 + 2.613 + 0.36 = 8.67 (3 s.f.). ν = 3. At 5%: 8.67 > 7.815, reject H₀, evidence the "
        "coins are not fair (too many single heads). At 1%: 8.67 < 11.345, do not reject H₀.",
        "Combine the first two (E = 9.2, O = 9) and the last two (E = 13.2, O = 14). Contributions 0.004, 0.180, 0.292, 0.048; "
        "X² = 0.525 (3 s.f.). ν = 4 − 1 − 1 = 2, critical value 5.991. Do not reject H₀: the model may be suitable.",
        "H₀: Po(2) is a suitable model. E = 16.24, 32.48, 32.48, 21.65, 10.83, 6.32 (last by subtraction). All ≥ 5. "
        "X² = 1.95 (3 s.f.). λ is given, so ν = 6 − 1 = 5, critical value 11.070. Do not reject H₀: no evidence against the claim.",
        "(a) 0.0244 < 0.05, so reject H₀ at 5%: evidence that the flavours are not equally popular. 0.0244 > 0.01, so H₀ is not "
        "rejected at 1%. (b) E = 20 each; contributions A 0.2, B 0.8, C 5.0, D 0.2, E 5.0 (total 11.2). C is chosen more often, "
        "and E less often, than equal popularity predicts.",
        "ν = 7 − 1 − 1 = 5. At 5%: 13.9 > 11.070, reject H₀ (Poisson not suitable). At 1%: 13.9 < 15.086, do not reject H₀.",
        "E = 100 × 0.3 × 0.7^(x−1) = 30, 21, 14.7, 10.29, and E(5 or more) = 100 × 0.7⁴ = 24.01. All ≥ 5, p is given, so "
        "ν = 5 − 1 = 4.",
        "H₀: U[0, 60] is a suitable model. E = 15 each. X² = (9 + 9 + 16 + 16 + 1 + 1)/15 = 3.47 (3 s.f.). ν = 5, critical value "
        "11.070. Do not reject H₀: arrival times may be uniformly distributed over the hour.",
        "ν = 6 − 1 = 5. The 0.995 point (lower 0.5%) of χ²₅ is 0.412, and 0.21 < 0.412, so P(X² ≤ 0.21) < 0.005. The fit is "
        "suspiciously good: the data may have been invented or adjusted, or the observations may not be independent.",
    ],
    "exam": [
        "The numbers of customers arriving at a kiosk in 150 five-minute intervals were: 0: 10, 1: 36, 2: 38, 3: 36, 4: 15, 5: 10, "
        "6 or more: 5 (each of these five intervals had exactly 6 arrivals). (a) Show that the mean is 2.4, find the variance, "
        "and explain why these values support a Poisson model. [3] (b) A Poisson model with λ = 2.4 is fitted. The expected "
        "frequencies for 1, 2, 3, 4 and 5 arrivals are 32.66, 39.19, 31.35, 18.81 and 9.03. Find the expected frequencies for 0 "
        "and for 6 or more. [3] (c) Test, at the 5% level, whether a Poisson distribution is a suitable model. [6]",
        "Seeds are sold in packets of 5. For 100 packets the numbers of seeds that germinated were: 0: 2, 1: 5, 2: 17, 3: 32, 4: 30, "
        "5: 14. (a) State two conditions needed for a binomial model to be suitable, in context. [2] (b) Show that an estimate of "
        "the probability that a seed germinates is 0.65. [2] (c) Using B(5, 0.65), the expected frequencies for 3, 4 and 5 are "
        "33.64, 31.24 and 11.60. Find the other expected frequencies. [2] (d) Test, at the 5% level, whether a binomial model is "
        "suitable. [6] (e) State how the test would change if the supplier had stated that p = 0.65. [1]",
        "(IAL S3, OCR A A level, CAIE) The reaction times of 100 adults were: under 0.20 s: 12, 0.20–0.25 s: 30, 0.25–0.30 s: 31, "
        "0.30–0.35 s: 19, 0.35 s and over: 8. A published study says the mean reaction time is 0.27 s. The standard deviation is "
        "estimated from the sample as 0.05 s. (a) Explain why the first and last classes are treated as extending to −∞ and +∞. [1] "
        "(b) Calculate the expected frequencies for a N(0.27, 0.05²) model. [4] (c) Test, at the 10% level, whether this normal "
        "model is suitable. [6]",
        "(CAIE, OCR A A level) A continuous random variable X has pdf f(x) = kx for 0 ≤ x ≤ 4, and 0 otherwise. (a) Find k. [1] "
        "(b) Show that P(1 ≤ X < 2) = 3/16, and find the expected frequencies for the intervals [0, 1), [1, 2), [2, 3), [3, 4] in a "
        "sample of 80. [3] (c) In a sample of 80 the observed frequencies were 9, 17, 22, 32. Test, at the 5% level, whether f is a "
        "suitable model. [5] (d) A colleague suggests a continuous uniform model on [0, 4] instead. Test this at the 5% level and "
        "comment. [3]",
    ],
    "exam_answers": [
        "(a) Σfx = 36 + 76 + 108 + 60 + 50 + 30 = 360, x̄ = 360/150 = 2.4 B1. Σfx² = 1182, variance = 1182/150 − 2.4² = 2.12 "
        "(s² = 2.13) M1 A1. Mean ≈ variance, as for a Poisson distribution. (b) E(0) = 150e^(−2.4) = 13.61 M1 A1. "
        "E(6+) = 150 − (13.61 + 32.66 + 39.19 + 31.35 + 18.81 + 9.03) = 5.35 A1. (c) H₀: Poisson is a suitable model for the "
        "number of arrivals; H₁: not suitable B1. All E ≥ 5, so 7 classes. X² = 2.92 (3 s.f.) M1 A1. ν = 7 − 1 − 1 = 5 B1 "
        "(λ estimated). Critical value 11.070 B1. 2.92 < 11.070: do not reject H₀; insufficient evidence that a Poisson model is "
        "unsuitable for the arrivals A1.",
        "(a) Seeds germinate independently of each other; the probability of germinating is the same for every seed (5 seeds, "
        "fixed n). B1 B1. (b) Σfx = 5 + 34 + 96 + 120 + 70 = 325 M1; p̂ = 325/(5 × 100) = 0.65 A1. (c) E(0) = 100 × 0.35⁵ = 0.53, "
        "E(1) = 100 × 5 × 0.65 × 0.35⁴ = 4.88, E(2) = 18.11 B1 B1. (d) H₀: B(5, p) is a suitable model; H₁: not B1. E(0) + E(1) = "
        "5.40 ≥ 5, so combine 0 and 1: O = 7 M1. Classes ≤1, 2, 3, 4, 5: contributions 0.473, 0.069, 0.080, 0.049, 0.495, "
        "X² = 1.17 (3 s.f.) A1. ν = 5 − 1 − 1 = 3 B1, critical value 7.815 B1. Do not reject H₀: a binomial model may be suitable A1. "
        "(e) p would not be estimated, so ν = 4 (critical value 9.488) B1.",
        "(a) The normal distribution covers all real values, so the probabilities must total 1 B1. (b) z = −1.4, −0.4, 0.6, 1.6 M1; "
        "Φ = 0.0808, 0.3446, 0.7257, 0.9452 M1; E = 8.08, 26.38, 38.12, 21.95, 5.48 A2 (A1 for three correct). (c) H₀: N(0.27, σ²) "
        "is a suitable model for reaction times B1. Contributions 1.907, 0.496, 1.329, 0.395, 1.159; X² = 5.29 (3 s.f.) M1 A1. "
        "Only σ estimated (μ given), so ν = 5 − 1 − 1 = 3 B1. 10% critical value 6.251 B1. 5.29 < 6.251: do not reject H₀; "
        "the normal model may be suitable A1.",
        "(a) ∫₀⁴ kx dx = 8k = 1, so k = 1/8 B1. (b) ∫₁² x/8 dx = (4 − 1)/16 = 3/16 M1 A1. Probabilities 1/16, 3/16, 5/16, 7/16, "
        "so E = 5, 15, 25, 35 A1. (c) H₀: f is a suitable model. All E ≥ 5 (E = 5 is allowed). X² = 3.2 + 0.267 + 0.36 + 0.257 = "
        "4.08 (3 s.f.) M1 A1. ν = 4 − 1 = 3 B1, critical value 7.815 B1. 4.08 < 7.815: do not reject H₀; f may be a suitable "
        "model A1. (d) E = 20 each; X² = (121 + 9 + 4 + 144)/20 = 13.9 M1 A1. 13.9 > 7.815: reject H₀; the uniform model is not "
        "suitable, because small values are rarer and large values more common than it predicts, as the linear pdf allows A1.",
    ],
}
