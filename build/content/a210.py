UNIT = {
    "number": "A2.10",
    "title": "Two-sample t-tests: pooled and paired",
    "tag": "A2 · Edexcel FS2 (7.2, 7.3), OCR MEI (paired only: SI10, SI11, SH6), CAIE 9231 P4 (4.2) · pooled sections: Edexcel, CAIE only",
    "notes": [
        ("p", "Many experiments compare two means: a new teaching method against an old one, or a measurement before and after a "
              "treatment. With small samples and unknown variances the comparison uses the t distribution of Unit A2.9. There are two "
              "quite different designs, and the first job is always to decide which one you have."),

        ("h2", "10.1 Paired samples or independent samples?"),
        ("bullets", [
            "<b>Paired (matched) samples:</b> each value in one sample is naturally linked to one value in the other: the same person before and after, the left and right hands of one person, twins, or two methods applied to the same specimen. The two samples have the same size.",
            "<b>Independent samples:</b> two separate groups with no link between individual values, for example 10 plants grown with fertiliser A and 12 different plants grown with fertiliser B. The sizes may differ.",
        ]),
        ("p", "Pairing is powerful because it removes the variation <i>between</i> subjects. Each difference d = x − y compares a subject "
              "with itself, so the differences are usually much less variable than the original measurements. A paired design can "
              "detect a small effect that two independent samples of the same size would miss (see Worked example 10.6)."),

        ("h2", "10.2 The paired t-test (Edexcel 7.2, MEI SH6, CAIE)"),
        ("box", "Paired t-test", [
            "Form the differences dᵢ = xᵢ − yᵢ for the n pairs, and find d̄ and s<sub>d</sub> (divisor n − 1).",
            "H₀: μ<sub>d</sub> = 0 (or μ<sub>d</sub> = c), where μ<sub>d</sub> is the population mean difference. H₁: μ<sub>d</sub> > 0, μ<sub>d</sub> < 0 or μ<sub>d</sub> ≠ 0.",
            "Under H₀, T = (D̄ − μ<sub>d</sub>)/(S<sub>d</sub>/√n) ~ t(n − 1).",
            "Assumption: the <b>differences</b> are a random sample from a normal distribution. The x and y values themselves need not be normal.",
        ]),
        ("p", "This is just the one-sample t-test of Unit A2.9 applied to the differences, which is why the Edexcel formula booklet says "
              "the one-sample t result is \"also valid in matched-pairs situations\". Always state which way round you subtracted, and "
              "make H₁ match it: if d = after − before and you expect an increase, H₁: μ<sub>d</sub> > 0."),
        ("p", "<b>Paired confidence interval (MEI SI11, Edexcel, CAIE).</b> A 100(1 − α)% interval for the mean difference is "
              "d̄ ± t × s<sub>d</sub>/√n with ν = n − 1. If the number of pairs is large, MEI also accepts d̄ ± z × s<sub>d</sub>/√n. "
              "An interval that does not contain 0 is evidence of a real mean difference."),

        ("h2", "10.3 The pooled estimate of a common variance (Edexcel 7.3, CAIE 4.2)"),
        ("p", "For two independent samples from populations with the <b>same</b> variance σ², each sample variance estimates σ². "
              "Combining them uses all n₁ + n₂ observations and gives a better estimate, weighted by the degrees of freedom of each sample."),
        ("box", "Pooled variance estimate", [
            "s<sub>p</sub>² = [(n₁ − 1)s₁² + (n₂ − 1)s₂²] / (n₁ + n₂ − 2) = [Σ(x − x̄)² + Σ(y − ȳ)²] / (n₁ + n₂ − 2).",
            "From summary data: Σ(x − x̄)² = Σx² − (Σx)²/n₁ and Σ(y − ȳ)² = Σy² − (Σy)²/n₂. (CAIE MF19 gives only the deviation form; you must convert.)",
            "s<sub>p</sub>² always lies between s₁² and s₂², closer to the variance of the larger sample. It has n₁ + n₂ − 2 degrees of freedom: one is lost for each estimated mean.",
        ]),

        ("h2", "10.4 The two-sample (pooled) t-test (Edexcel 7.3, CAIE 4.2)"),
        ("box", "Two-sample t statistic", [
            "H₀: μ₁ − μ₂ = c (usually c = 0), with H₁ one- or two-tailed.",
            "Under H₀, T = [(X̄ − Ȳ) − c] / [S<sub>p</sub> √(1/n₁ + 1/n₂)] ~ t(n₁ + n₂ − 2).",
            "Assumptions: (1) both populations are normal; (2) the population variances are equal; (3) the samples are random and independent of each other.",
        ]),
        ("p", "Why s<sub>p</sub>√(1/n₁ + 1/n₂)? If both variances equal σ², then Var(X̄ − Ȳ) = σ²/n₁ + σ²/n₂ = σ²(1/n₁ + 1/n₂), and s<sub>p</sub>² "
              "replaces σ². A confidence interval for μ₁ − μ₂ is (x̄ − ȳ) ± t × s<sub>p</sub>√(1/n₁ + 1/n₂), with ν = n₁ + n₂ − 2."),

        ("h2", "10.5 When is pooling justified?"),
        ("bullets", [
            "The question says the population variances are equal (or \"may be assumed equal\"). Then pool. CAIE examiners report that some candidates ignore this stated assumption and lose marks.",
            "The samples come from the same kind of population measured in the same way, and the sample standard deviations are similar. A common rule of thumb: pooling is reasonable if the larger sample variance is less than about 3 to 4 times the smaller.",
            "Edexcel: an F-test (Unit A2.11) of H₀: σ₁² = σ₂² can be carried out first; if H₀ is not rejected, pooling is supported.",
            "Do <b>not</b> pool when equal variances are not assumed and the samples are large: use the two-sample z test of Unit A2.8 with separate variances, √(s₁²/n₁ + s₂²/n₂). CAIE 2023 penalised pooling in exactly this situation.",
            "Small samples, unequal variances: none of these specifications covers this case (Welch's test). It is not examined.",
        ]),

        ("h2", "10.6 Choosing the correct test (CAIE 4.2 note)"),
        ("table", ["Situation", "Test", "Statistic and distribution"], [
            ["Paired data, differences normal (small n)", "paired t", "d̄/(s<sub>d</sub>/√n) ~ t(n − 1)"],
            ["Paired data, many pairs", "paired z (MEI) or paired t", "d̄/(s<sub>d</sub>/√n) ≈ N(0, 1)"],
            ["Independent, normal, equal variances, small samples", "pooled two-sample t", "(x̄ − ȳ)/(s<sub>p</sub>√(1/n₁ + 1/n₂)) ~ t(n₁ + n₂ − 2)"],
            ["Independent, variances known", "two-sample z", "(x̄ − ȳ)/√(σ₁²/n₁ + σ₂²/n₂) ~ N(0, 1)"],
            ["Independent, large samples, variances unknown", "two-sample z", "(x̄ − ȳ)/√(s₁²/n₁ + s₂²/n₂) ≈ N(0, 1)"],
            ["Small samples, not normal", "non-parametric", "Wilcoxon tests (Unit A2.13)"],
        ]),
        ("p", "Ask three questions in order: Are the data paired? Are the samples large? Can the variances be assumed equal? "
              "Write your reason in the answer, for example \"the same students were tested twice, so the samples are paired\"."),
        ("warn", "Common mistakes", [
            "Using a two-sample test on paired data. The two samples are not independent, and the test loses the benefit of pairing.",
            "Stating that x and y must be normal for a paired test. It is the population of differences that must be normal.",
            "Using ν = n₁ + n₂ − 1, or n − 2 for a paired test. Pooled: n₁ + n₂ − 2. Paired: n − 1, where n is the number of pairs.",
            "Averaging s₁² and s₂² instead of weighting by n − 1, or forgetting to divide Σ(x − x̄)² + Σ(y − ȳ)² by n₁ + n₂ − 2.",
            "Forgetting the square root: the standard error is √(s<sub>p</sub>²(1/n₁ + 1/n₂)), not s<sub>p</sub>²(1/n₁ + 1/n₂).",
            "Pooling when the samples are large and equal variances are not given. Use the z test with separate variances.",
            "Hypotheses written as \"H₀: x̄ = ȳ\" or \"H₀: d̄ = 0\". They must be about population means: μ₁ = μ₂ or μ<sub>d</sub> = 0.",
        ]),
    ],
    "examples": [
        {
            "title": "Paired t-test from raw data",
            "question": "Eight students took a test before and after a revision course. Scores: before 52, 61, 47, 70, 58, 65, 49, 55; "
                        "after 56, 63, 52, 71, 62, 64, 55, 59 (same order of students). Test, at the 5% level, whether the course "
                        "increases the mean score.",
            "steps": [
                "The same students were tested twice, so the data are paired. Let d = after − before: 4, 2, 5, 1, 4, −1, 6, 4.",
                "Σd = 25, Σd² = 115, so d̄ = 3.125 and s<sub>d</sub>² = (115 − 25²/8)/7 = 5.2679, s<sub>d</sub> = 2.2952.",
                "Let μ<sub>d</sub> be the population mean increase in score. H₀: μ<sub>d</sub> = 0, H₁: μ<sub>d</sub> > 0 (one-tailed, 5%).",
                "Assume the differences are normally distributed. Under H₀, T = D̄/(S<sub>d</sub>/√8) ~ t(7).",
                "t = 3.125/(2.2952/√8) = 3.125/0.81147 = 3.85 (3 s.f.). Critical value t(7) upper 5% = 1.895.",
                "3.85 > 1.895, so reject H₀ (p-value 0.0031). There is sufficient evidence at the 5% level that the course increases the mean score.",
            ],
        },
        {
            "title": "Paired confidence interval from summary data (MEI SI11)",
            "question": "Ten volunteers each did a memory task with and without background music. The differences d = (score without "
                        "music) − (score with music) give Σd = 23.0 and Σd² = 81.4. Find a 95% confidence interval for the population "
                        "mean difference, stating the assumption needed, and interpret it.",
            "steps": [
                "d̄ = 2.3, s<sub>d</sub>² = (81.4 − 23.0²/10)/9 = 28.5/9 = 3.1667, s<sub>d</sub> = 1.7795.",
                "ν = 9 and 95% gives t = 2.262. Half-width 2.262 × 1.7795/√10 = 1.2729.",
                "Interval: 2.3 ± 1.2729 = (1.03, 3.57) (3 s.f.).",
                "Assumption: the differences are a random sample from a normal distribution.",
                "The whole interval is above 0, so there is evidence (at the two-tailed 5% level) that scores are higher on average without music.",
            ],
        },
        {
            "title": "Pooled variance from raw data and a two-sample t-test",
            "question": "The heights, in cm, of seedlings grown in compost A were 23.1, 25.4, 24.8, 22.9, 26.0, 24.3 and in compost B were "
                        "21.8, 23.5, 22.6, 24.1, 21.2, 22.9, 23.0. Assume heights are normal with a common variance. Test, at the 5% "
                        "level, whether the mean heights differ.",
            "steps": [
                "A: n₁ = 6, Σx = 146.5, Σx² = 3584.71, x̄ = 24.417, Σ(x − x̄)² = 3584.71 − 146.5²/6 = 7.6683.",
                "B: n₂ = 7, Σy = 159.1, Σy² = 3621.91, ȳ = 22.729, Σ(y − ȳ)² = 3621.91 − 159.1²/7 = 5.7943.",
                "s<sub>p</sub>² = (7.6683 + 5.7943)/11 = 1.2239, s<sub>p</sub> = 1.1063.",
                "Let μ<sub>A</sub>, μ<sub>B</sub> be the population mean heights. H₀: μ<sub>A</sub> = μ<sub>B</sub>, H₁: μ<sub>A</sub> ≠ μ<sub>B</sub> (two-tailed, 5%). Under H₀, T ~ t(11).",
                "Standard error 1.1063 × √(1/6 + 1/7) = 0.61548. t = (24.417 − 22.729)/0.61548 = 2.74 (3 s.f.).",
                "Critical values ±2.201 (upper 2.5% of t(11)). 2.74 > 2.201, so reject H₀ (p-value 0.0191).",
                "There is sufficient evidence at the 5% level that the mean seedling heights in the two composts are different.",
            ],
        },
        {
            "title": "Pooled test and interval from summary data (CAIE style)",
            "question": "Random samples of light bulbs of two types give lifetimes x and y (hundreds of hours): "
                        "type X: n = 10, Σx = 482, Σx² = 23 380; type Y: n = 12, Σy = 549.6, Σy² = 25 360. Lifetimes are normal with a "
                        "common variance. (a) Find the pooled estimate of the common variance. (b) Test, at the 5% level, whether type X "
                        "lasts longer on average. (c) Find a 95% confidence interval for μₓ − μ<sub>y</sub>.",
            "steps": [
                "(a) x̄ = 48.2, Σ(x − x̄)² = 23 380 − 482²/10 = 147.6. ȳ = 45.8, Σ(y − ȳ)² = 25 360 − 549.6²/12 = 188.32.",
                "s<sub>p</sub>² = (147.6 + 188.32)/20 = 16.796 = 16.8 (3 s.f.).",
                "(b) H₀: μₓ = μ<sub>y</sub>, H₁: μₓ > μ<sub>y</sub> (one-tailed, 5%). Under H₀, T ~ t(20).",
                "Standard error √(16.796 × (1/10 + 1/12)) = √3.0793 = 1.7548. t = 2.4/1.7548 = 1.37 (3 s.f.).",
                "Critical value t(20) upper 5% = 1.725. 1.37 < 1.725, so do not reject H₀. There is insufficient evidence at 5% that type X lasts longer on average.",
                "(c) t(20) upper 2.5% = 2.086. 2.4 ± 2.086 × 1.7548 = 2.4 ± 3.6605, giving (−1.26, 6.06) hundred hours (3 s.f.). It contains 0, consistent with (b).",
            ],
        },
        {
            "title": "Choosing the test",
            "question": "For each study, choose the most appropriate test and give a reason. (a) The reaction times of 12 drivers are measured "
                        "before and after drinking coffee. (b) Exam marks of 80 pupils from school P and 95 from school Q are compared; "
                        "nothing is known about the population variances. (c) Masses of 8 eggs from farm R and 10 from farm S are compared; "
                        "masses are normal and the variances may be assumed equal. (d) Five patients' pain scores (very skewed) are compared before and after treatment.",
            "steps": [
                "(a) Paired t-test: the same drivers are measured twice. Assume the differences are normally distributed; ν = 11.",
                "(b) Two-sample z test with separate variances: the samples are large and independent, so by the CLT the difference in means is approximately normal; equal variances are not assumed, so do not pool.",
                "(c) Pooled two-sample t-test with ν = 8 + 10 − 2 = 16: small independent samples, normal populations, equal variances.",
                "(d) A t-test is not appropriate: the sample is tiny and the data are not normal. Use a non-parametric paired test, such as the sign test or Wilcoxon matched-pairs test (Units A2.12 and A2.13).",
            ],
        },
        {
            "title": "Exam standard: why pairing matters",
            "question": "Six pairs of identical twins took part in a diet study. One twin in each pair followed diet A, the other diet B. "
                        "Weight gains (kg): A 5.2, 6.8, 4.1, 7.5, 5.9, 6.3; B 4.6, 6.1, 3.9, 6.8, 5.0, 5.8 (same order of pairs). "
                        "(a) Carry out a paired t-test, at the 1% level, of whether diet A gives a greater mean gain. "
                        "(b) A student wrongly treats the data as two independent samples. Show that a pooled t-test does not find "
                        "evidence even at the 10% level, and explain the difference.",
            "steps": [
                "(a) d = A − B: 0.6, 0.7, 0.2, 0.7, 0.9, 0.5. d̄ = 0.6, s<sub>d</sub> = 0.23664.",
                "H₀: μ<sub>d</sub> = 0, H₁: μ<sub>d</sub> > 0, where μ<sub>d</sub> is the population mean of (gain on A − gain on B) for twin pairs. Under H₀, T ~ t(5).",
                "t = 0.6/(0.23664/√6) = 6.21 (3 s.f.). Critical value t(5) upper 1% = 3.365. 6.21 > 3.365, so reject H₀.",
                "There is sufficient evidence at the 1% level that diet A gives a greater mean weight gain than diet B.",
                "(b) x̄<sub>A</sub> = 5.9667, s<sub>A</sub>² = 1.4467; x̄<sub>B</sub> = 5.3667, s<sub>B</sub>² = 1.1307. s<sub>p</sub>² = (5 × 1.4467 + 5 × 1.1307)/10 = 1.2887.",
                "t = 0.6/√(1.2887 × (1/6 + 1/6)) = 0.6/0.65540 = 0.915 (3 s.f.). Upper 10% point of t(10) = 1.372, and 0.915 < 1.372.",
                "The twins differ a lot from each other (gains range from about 4 to 7.5 kg), and the pooled test counts all that variation. Pairing removes it, leaving only the small, consistent differences within each pair.",
            ],
        },
    ],
    "practice": [
        "(Edexcel, CAIE) Independent samples have n₁ = 8, s₁ = 3.2 and n₂ = 11, s₂ = 2.7. Calculate the pooled estimate of the common population variance.",
        "(Edexcel, CAIE) Sample X: 14, 17, 15, 19, 16. Sample Y: 12, 15, 13, 14, 11, 13. Calculate x̄, ȳ and the pooled estimate s<sub>p</sub>² of the common variance.",
        "(Edexcel, CAIE) Summary data: n₁ = 9, Σx = 117, Σx² = 1557; n₂ = 8, Σy = 92, Σy² = 1078. Find the pooled estimate of the common variance.",
        "For 12 pairs of observations the differences have mean 1.8 and standard deviation (divisor n − 1) 2.9. Assuming the differences are normal, test H₀: μ<sub>d</sub> = 0 against H₁: μ<sub>d</sub> > 0 at the 5% level.",
        "The grip strengths (kg) of the left and right hands of 7 people are: left 31, 28, 35, 30, 27, 33, 29; right 33, 29, 34, 33, 30, 35, 31. Test, at the 5% level, whether there is a difference in mean grip strength between the hands.",
        "(Edexcel, CAIE) Independent random samples from normal populations with a common variance give n₁ = 9, x̄₁ = 15.8, s₁ = 2.1 and n₂ = 11, x̄₂ = 13.9, s₂ = 2.4. Test, at the 5% level, whether μ₁ > μ₂.",
        "(Edexcel, CAIE) Independent random samples from normal populations with a common variance give n₁ = 7, x̄₁ = 82.4, s₁ = 5.3 and n₂ = 9, x̄₂ = 76.1, s₂ = 6.0. Find a 95% confidence interval for μ₁ − μ₂.",
        "(Edexcel, CAIE) Under the same assumptions, samples give n₁ = 12, x̄₁ = 48.6, s₁ = 3.4 and n₂ = 10, x̄₂ = 43.2, s₂ = 3.9. Test H₀: μ₁ − μ₂ = 3 against H₁: μ₁ − μ₂ > 3 at the 5% level.",
        "State, with a reason, whether a paired or a two-sample test is appropriate: (a) the yields of two wheat varieties, each grown on one half of each of 10 fields; (b) the heights of 15 boys and 12 girls in a class; (c) the times taken by 9 workers to do a task using an old and a new tool.",
        "(a) State the assumptions needed for a pooled two-sample t-test. (b) State the assumption needed for a paired t-test, and explain why it is weaker than \"both sets of measurements are normal\".",
        "(OCR MEI) For 9 pairs, the differences have mean 0.84 and s<sub>d</sub> = 1.12. Find a 90% confidence interval for the population mean difference, assuming normality.",
        "(Edexcel, CAIE) A 95% confidence interval for μ₁ − μ₂, based on pooled t with samples of size 10 and 10, is (−0.8, 4.6). Find x̄₁ − x̄₂ and the pooled estimate s<sub>p</sub>.",
    ],
    "answers": [
        "s<sub>p</sub>² = (7 × 3.2² + 10 × 2.7²)/17 = (71.68 + 72.9)/17 = 8.50 (3 s.f.).",
        "x̄ = 16.2, ȳ = 13.0. Σ(x − x̄)² = 14.8, Σ(y − ȳ)² = 10. s<sub>p</sub>² = 24.8/9 = 2.76 (3 s.f.).",
        "Σ(x − x̄)² = 1557 − 117²/9 = 36; Σ(y − ȳ)² = 1078 − 92²/8 = 20. s<sub>p</sub>² = 56/15 = 3.73 (3 s.f.).",
        "t = 1.8/(2.9/√12) = 2.15 (3 s.f.). ν = 11, critical value 1.796. 2.15 > 1.796, so reject H₀: sufficient evidence at 5% that the population mean difference is positive.",
        "Paired data. d = right − left: 2, 1, −1, 3, 3, 2, 2; d̄ = 1.7143, s<sub>d</sub> = 1.3801. H₀: μ<sub>d</sub> = 0, H₁: μ<sub>d</sub> ≠ 0. t = 1.7143/(1.3801/√7) = 3.29 (3 s.f.). Critical values ±2.447 (ν = 6). Reject H₀: sufficient evidence at 5% of a difference in mean grip strength (right hand stronger).",
        "s<sub>p</sub>² = (8 × 2.1² + 10 × 2.4²)/18 = 5.16. t = 1.9/√(5.16 × (1/9 + 1/11)) = 1.9/1.0210 = 1.86 (3 s.f.). Critical value t(18) = 1.734. 1.86 > 1.734, so reject H₀: sufficient evidence at 5% that μ₁ > μ₂.",
        "s<sub>p</sub>² = (6 × 5.3² + 8 × 6.0²)/14 = 32.61. Standard error √(32.61 × (1/7 + 1/9)) = 2.8778. t(14) = 2.145. 6.3 ± 2.145 × 2.8778 = (0.127, 12.5) (3 s.f.).",
        "s<sub>p</sub>² = (11 × 3.4² + 9 × 3.9²)/20 = 13.2025. Standard error √(13.2025 × (1/12 + 1/10)) = 1.5558. t = (5.4 − 3)/1.5558 = 1.54 (3 s.f.). Critical value t(20) = 1.725. Do not reject H₀: insufficient evidence at 5% that μ₁ − μ₂ > 3.",
        "(a) Paired: each field gives one yield for each variety, so fields are matched. (b) Two-sample: different children with no natural pairing (and different sizes). (c) Paired: the same workers use both tools.",
        "(a) Both populations normal; equal population variances; samples random and independent. (b) The population of differences is normal. Differences can be normal even if the separate measurements are not (and are often closer to normal), so it is a weaker requirement.",
        "t(8) upper 5% = 1.860. 0.84 ± 1.860 × 1.12/3 = 0.84 ± 0.6944, giving (0.146, 1.53) (3 s.f.).",
        "x̄₁ − x̄₂ = (−0.8 + 4.6)/2 = 1.9. Half-width 2.7 = 2.101 × s<sub>p</sub> × √(1/10 + 1/10), so s<sub>p</sub> = 2.7/(2.101 × 0.44721) = 2.87 (3 s.f.).",
    ],
    "exam": [
        "(CAIE 9231) The yields, in kg, of a random sample of 8 plants of tomato variety P and an independent random sample of 10 plants of variety Q are summarised by: "
        "Σp = 41.6, Σ(p − p̄)² = 6.42; Σq = 46.0, Σ(q − q̄)² = 7.83. "
        "Yields of both varieties are normally distributed with a common variance. "
        "(a) Calculate a pooled estimate of the common variance. [2] "
        "(b) Test, at the 5% significance level, whether the mean yield of variety P is greater than that of variety Q. [5] "
        "(c) Find a 95% confidence interval for the difference between the mean yields. [3] "
        "(d) Explain why the test in (b) would not be valid if the samples had been taken from the same plants in two different years. [1]",
        "(Edexcel FS2, CAIE) Nine athletes ran 400 m before and after a new training programme. Their times, in seconds, were: "
        "before 62.4, 58.9, 65.1, 60.3, 63.8, 59.6, 61.2, 64.0, 57.5; after 61.1, 58.2, 63.0, 60.5, 62.1, 58.3, 60.4, 62.2, 57.6 (same order of athletes). "
        "(a) Explain why a paired t-test is appropriate. [1] "
        "(b) Test, at the 1% significance level, whether the programme reduces mean 400 m time. [7] "
        "(c) Find a 95% confidence interval for the mean reduction in time. [3] "
        "(d) State an assumption required for your test to be valid. [1]",
        "(CAIE 9231, Edexcel FS2) A consumer group compares the fuel economy, in km per litre, of two car models. "
        "(a) In a pilot study, six cars of each model gave: model A 18.2, 19.5, 17.8, 18.9, 19.1, 18.4; model B 17.5, 18.8, 17.2, 18.0, 17.9, 18.3. "
        "Assuming normal distributions with equal variances, test at the 10% significance level whether the mean fuel economies differ. [7] "
        "(b) In a larger study, 50 cars of model A gave mean 18.62 and standard deviation 0.85, and 60 cars of model B gave mean 18.21 and standard deviation 1.20. "
        "No assumption is made about the population variances. Carry out a suitable test, at the 5% level, of whether the means differ, justifying your choice of test. [5]",
        "(OCR MEI) Fifteen students each sat two versions of a reading test, X and Y, in random order. Software output for the differences d = (score on X) − (score on Y): "
        "n 15; mean 2.43; SD 3.10; 95% confidence interval for the mean difference (0.713, 4.147). "
        "(a) Explain why it is appropriate to use the differences rather than treating the scores as two separate samples. [1] "
        "(b) Show how the confidence interval was calculated. [3] "
        "(c) A teacher says the two versions are equally difficult. Comment on this, using the interval. [2] "
        "(d) State the assumption on which the interval depends. [1] "
        "(e) Without further calculation, state whether a 99% interval would contain 0. Give a reason. [2]",
    ],
    "exam_answers": [
        "(a) s<sub>p</sub>² = (6.42 + 7.83)/(8 + 10 − 2) [M1] = 0.891 (3 s.f.) [A1]. "
        "(b) H₀: μ<sub>P</sub> = μ<sub>Q</sub>, H₁: μ<sub>P</sub> > μ<sub>Q</sub> [B1]. p̄ = 5.2, q̄ = 4.6 [B1]. t = 0.6/√(0.890625 × (1/8 + 1/10)) = 0.6/0.44765 = 1.34 (3 s.f.) [M1 A1]. "
        "Critical value t(16) = 1.746; 1.34 < 1.746, so do not reject H₀: insufficient evidence at 5% that variety P has a higher mean yield [A1]. "
        "(c) t(16) upper 2.5% = 2.120 [B1]. 0.6 ± 2.120 × 0.44765 [M1] = (−0.349, 1.55) kg (3 s.f.) [A1]. "
        "(d) The samples would no longer be independent (they would be paired by plant) [B1].",
        "(a) The same athletes were timed twice, so each before time is matched with an after time [B1]. "
        "(b) d = before − after: 1.3, 0.7, 2.1, −0.2, 1.7, 1.3, 0.8, 1.8, −0.1 [M1]. Σd = 9.4, Σd² = 15.1, d̄ = 1.0444, s<sub>d</sub> = 0.81257 [A1 A1]. "
        "H₀: μ<sub>d</sub> = 0, H₁: μ<sub>d</sub> > 0, μ<sub>d</sub> the population mean reduction [B1]. t = 1.0444/(0.81257/3) = 3.86 (3 s.f.) [M1 A1]. "
        "t(8) upper 1% = 2.896; 3.86 > 2.896, so reject H₀: sufficient evidence at 1% that the programme reduces mean time [A1]. "
        "(c) 1.0444 ± 2.306 × 0.27086 [M1 B1] = (0.420, 1.67) seconds (3 s.f.) [A1]. "
        "(d) The differences in time are normally distributed (and the athletes are a random sample) [B1].",
        "(a) x̄<sub>A</sub> = 18.65, x̄<sub>B</sub> = 17.95 [B1]. s<sub>A</sub>² = 0.395, s<sub>B</sub>² = 0.323 [B1]. s<sub>p</sub>² = (5 × 0.395 + 5 × 0.323)/10 = 0.359 [M1 A1]. "
        "H₀: μ<sub>A</sub> = μ<sub>B</sub>, H₁: μ<sub>A</sub> ≠ μ<sub>B</sub> [B1]. t = 0.7/√(0.359 × (1/6 + 1/6)) = 0.7/0.34593 = 2.02 (3 s.f.) [A1]. "
        "t(10) upper 5% = 1.812; 2.02 > 1.812, so reject H₀: sufficient evidence at 10% that the mean fuel economies differ [A1]. "
        "(b) The samples are large, so by the CLT the sample means are approximately normal, and equal variances are not assumed, so use a two-sample z test with separate variances [B1]. "
        "H₀: μ<sub>A</sub> = μ<sub>B</sub>, H₁: μ<sub>A</sub> ≠ μ<sub>B</sub>. Standard error √(0.85²/50 + 1.20²/60) = 0.19609 [M1]. z = 0.41/0.19609 = 2.09 (3 s.f.) [A1]. "
        "2.09 > 1.96 [M1], so reject H₀: sufficient evidence at 5% that the mean fuel economies differ [A1].",
        "(a) Each student sat both versions, so the scores are paired; using differences removes the large variation in reading ability between students [B1]. "
        "(b) t(14) upper 2.5% point = 2.145 [B1]. 2.43 ± 2.145 × 3.10/√15 [M1] = 2.43 ± 1.7169 = (0.713, 4.147) [A1]. "
        "(c) 0 is not in the interval [M1], so the data suggest the versions are not equally difficult: on average students score higher on X [A1]. "
        "(d) The differences come from a normal distribution (and the students are a random sample) [B1]. "
        "(e) t = 2.43/(3.10/√15) = 3.04 [M1], and the upper 0.5% point of t(14) is 2.977 < 3.04, so the 99% interval would just exclude 0 (it would not contain 0) [A1].",
    ],
}
