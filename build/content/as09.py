UNIT = {
    "number": "AS9",
    "title": "Correlation: product moment and Spearman's rank",
    "tag": "AS · Edexcel FS2 (AS: 8FM0), OCR A 5.08, OCR MEI Sb1–Sb10 · IAL S3 (Spearman and tests) · not on AQA or CAIE",
    "notes": [
        ("h2", "9.1 Bivariate data and scatter diagrams"),
        ("p", "<b>Bivariate data</b> are pairs (x, y) measured on the same individuals, such as the height and mass of each of "
              "20 students. Plot them on a <b>scatter diagram</b>. Look for the direction (positive or negative), the form "
              "(straight-line, curved, or no pattern), the strength (how tightly the points cluster), and any <b>outliers</b> or "
              "separate clusters."),
        ("p", "OCR MEI distinguishes two situations. In <b>Case A</b> (random on non-random) x is controlled by the "
              "experimenter, e.g. the dose of fertiliser chosen in advance, and only y is random. In <b>Case B</b> (random on "
              "random) both variables are random, e.g. the heights and masses of randomly chosen students. Correlation tests "
              "are designed for Case B. By convention the explanatory or controlled variable goes on the horizontal axis."),
        ("h2", "9.2 The product moment correlation coefficient (PMCC)"),
        ("box", "Sums of squares and the PMCC", [
            "Sxx = Σ(x − x̄)² = Σx² − (Σx)²/n.  Syy = Σ(y − ȳ)² = Σy² − (Σy)²/n.",
            "Sxy = Σ(x − x̄)(y − ȳ) = Σxy − (Σx)(Σy)/n.",
            "r = Sxy/√(Sxx Syy), and −1 ≤ r ≤ 1.",
            "r = 1 or −1: all points lie exactly on a straight line with positive or negative gradient. r = 0: no linear correlation.",
        ]),
        ("p", "Why it works: a point in the top-right or bottom-left quadrant relative to (x̄, ȳ) makes (x − x̄)(y − ȳ) positive, "
              "and a point in the other two quadrants makes it negative. So Sxy is large and positive when points rise from "
              "left to right. Dividing by √(Sxx Syy) removes the units and fixes the scale between −1 and 1. The PMCC "
              "measures how close the points are to a <b>straight line</b> (OCR A 5.08c), not just whether y increases with x."),
        ("p", "Calculators find r from raw data in regression mode; every board expects you to use this. From summary "
              "statistics you must use the formulae above. Keep full calculator accuracy for Sxx, Syy and Sxy and round r at "
              "the end (3 s.f., or 4 d.p. when comparing with a critical value)."),
        ("h2", "9.3 The effect of coding"),
        ("p", "Data are often coded to make numbers easier, e.g. u = (x − a)/b and v = (y − c)/d with b, d > 0. Adding or "
              "subtracting a constant does not change any of the sums of squares. Dividing by b divides the x-deviations by b."),
        ("box", "Coding results", [
            "If u = (x − a)/b and v = (y − c)/d, then Sxx = b² Suu, Syy = d² Svv and Sxy = bd Suv.",
            "So r<sub>xy</sub> = r<sub>uv</sub> when b and d have the same sign: <b>the PMCC is unchanged by linear coding</b>.",
            "If exactly one of b and d is negative, r changes sign but keeps its size.",
        ]),
        ("h2", "9.4 Interpreting r"),
        ("bullets", [
            "Correlation is not causation. A strong correlation may be due to a third (confounding) variable, or be a coincidence.",
            "r only measures linear association. A strong curved relationship can have r close to 0, and a curved but "
            "increasing pattern can still give r close to 1. Always look at the scatter diagram.",
            "One outlier can greatly increase or decrease r. Two separate clusters can produce a large r even when there is "
            "no correlation within either cluster.",
            "r² is the proportion of the variation in y that is explained by a linear relationship with x (OCR MEI Sb3, Sb14).",
            "<b>Effect size</b> (OCR MEI Sb7): r measures the strength of an effect independently of sample size. A commonly "
            "used rule (Cohen's) is |r| ≈ 0.1 small, 0.3 medium, 0.5 large. Any rule needed in an exam will be given.",
        ]),
        ("h2", "9.5 Hypothesis test for zero correlation using the PMCC"),
        ("p", "The sample coefficient r estimates the <b>population</b> correlation coefficient ρ (rho). The test asks whether "
              "the sample gives evidence that ρ is not zero."),
        ("box", "PMCC test", [
            "H₀: ρ = 0. H₁: ρ > 0 (one-tailed), ρ < 0 (one-tailed) or ρ ≠ 0 (two-tailed), where ρ is the population PMCC "
            "between x and y.",
            "Find the critical value for the sample size n and significance level from Table 18. For a two-tailed test at 5%, "
            "use the 2.5% one-tailed column.",
            "Reject H₀ if r ≥ c (H₁: ρ > 0), r ≤ −c (H₁: ρ < 0) or |r| ≥ c (H₁: ρ ≠ 0).",
            "Assumption: the data are a random sample from a <b>bivariate normal</b> distribution. Then the scatter diagram is "
            "roughly elliptical. You must know this condition; formal checks are not required.",
        ]),
        ("table", ["n", "5% one-tailed (10% two-tailed)", "2.5% one-tailed (5% two-tailed)", "1% one-tailed (2% two-tailed)", "0.5% one-tailed (1% two-tailed)"], [
            ["5", "0.8054", "0.8783", "0.9343", "0.9587"],
            ["6", "0.7293", "0.8114", "0.8822", "0.9172"],
            ["7", "0.6694", "0.7545", "0.8329", "0.8745"],
            ["8", "0.6215", "0.7067", "0.7887", "0.8343"],
            ["9", "0.5822", "0.6664", "0.7498", "0.7977"],
            ["10", "0.5494", "0.6319", "0.7155", "0.7646"],
            ["12", "0.4973", "0.5760", "0.6581", "0.7079"],
            ["15", "0.4409", "0.5140", "0.5923", "0.6411"],
            ["20", "0.3783", "0.4438", "0.5155", "0.5614"],
            ["25", "0.3365", "0.3961", "0.4622", "0.5052"],
            ["30", "0.3061", "0.3610", "0.4226", "0.4629"],
        ]),
        ("p", "These are an extract from Table 18 (PMCC critical values for a bivariate normal population). Software often gives a "
              "p-value instead (OCR A 5.08d, OCR MEI Sb6): reject H₀ if p is below the significance level, remembering to "
              "double a one-tailed p-value for a two-tailed test if the software has not done so. With a large sample even a "
              "small r can be significant, so a significant result does not mean a strong relationship: that is why MEI asks "
              "about effect size."),
        ("h2", "9.6 Spearman's rank correlation coefficient"),
        ("p", "Spearman's coefficient rₛ is the PMCC calculated from the <b>ranks</b> of the data instead of the values. Rank the "
              "x values (1 = smallest, or 1 = largest, as long as both variables are ranked the same way) and rank the y values "
              "separately. If there are no ties, the PMCC of the ranks simplifies to a formula in the differences d between "
              "the two ranks of each individual."),
        ("box", "Spearman's rank correlation coefficient", [
            "rₛ = 1 − 6Σd²/(n(n² − 1)), where d = (rank of x) − (rank of y) for each pair.",
            "rₛ = 1: the two rankings agree exactly. rₛ = −1: the rankings are exactly reversed.",
            "rₛ measures <b>association</b>: whether y tends to increase (or decrease) as x increases, linear or not.",
            "Check: Σd = 0 always. If it is not, you have made a ranking error.",
        ]),
        ("p", "<b>Tied ranks</b>: if values are equal, give each the mean of the ranks they would occupy. For example, if the "
              "2nd and 3rd smallest values are equal, both get rank 2.5; if three values share ranks 5, 6 and 7, all get 6. With "
              "ties the shortcut formula is only approximate, so calculate rₛ as the PMCC of the ranks (on a calculator). "
              "Edexcel FS2 may set numerical questions with ties. IAL S3 expects you to know how to deal with ties but sets no "
              "numerical questions with them. OCR A and OCR MEI exclude tied ranks."),
        ("h2", "9.7 Hypothesis test using Spearman's coefficient"),
        ("box", "Spearman test", [
            "H₀: ρₛ = 0 (no association between the variables in the population). H₁: ρₛ > 0, ρₛ < 0 or ρₛ ≠ 0.",
            "Find the critical value for n from Table 19 and compare rₛ as for the PMCC test.",
            "The test is non-parametric: it needs no assumption about the distribution of x and y, only that the data are a "
            "random sample. It can be used for data that are only given as ranks.",
        ]),
        ("table", ["n", "5% one-tailed (10% two-tailed)", "2.5% one-tailed (5% two-tailed)", "1% one-tailed (2% two-tailed)", "0.5% one-tailed (1% two-tailed)"], [
            ["5", "0.9000", "1.0000", "1.0000", "–"],
            ["6", "0.8286", "0.8857", "0.9429", "1.0000"],
            ["7", "0.7143", "0.7857", "0.8929", "0.9286"],
            ["8", "0.6429", "0.7381", "0.8333", "0.8810"],
            ["9", "0.6000", "0.7000", "0.7833", "0.8333"],
            ["10", "0.5636", "0.6485", "0.7455", "0.7939"],
        ]),
        ("p", "Table 19 values are exact: rₛ takes only a few possible values for small n, so each tabulated value is the smallest "
              "rₛ whose upper-tail probability does not exceed the stated level. Reject H₀ if rₛ is at least the tabulated "
              "value. For n above 10, use the value given in the question or your board's booklet."),
        ("h2", "9.8 Choosing between the PMCC and Spearman's coefficient"),
        ("table", ["Use the PMCC when", "Use Spearman's coefficient when"], [
            ["the scatter diagram suggests a linear relationship", "the relationship looks monotonic but not linear"],
            ["the data could come from a bivariate normal distribution (elliptical scatter)", "the data are clearly not bivariate normal, or include outliers"],
            ["both variables are measured on a numerical scale", "the data are ranks or judgements (e.g. judges' orderings)"],
            ["you want to test for linear correlation", "you want to test for association (one increases as the other increases)"],
        ]),
        ("p", "Ranking throws away information about the actual values, so when the PMCC test is valid it is usually more "
              "powerful. If the scatter diagram is not monotonic (e.g. U-shaped), neither coefficient is appropriate (OCR MEI Sb10)."),
        ("warn", "Common mistakes", [
            "Using n − 1 or the number of points minus 2 when reading the table: the tables use n, the number of pairs.",
            "Using the one-tailed column for a two-tailed test (or the reverse).",
            "Writing H₀: r = 0. Hypotheses are about the population parameter ρ (or ρₛ), not the sample value r.",
            "Stating that correlation shows that x causes y.",
            "Forgetting the bivariate normal assumption for the PMCC test, or using it when the scatter is clearly curved.",
            "Ranking one variable from smallest and the other from largest, which reverses the sign of rₛ.",
            "Using the shortcut rₛ formula with tied ranks and calling it exact.",
            "Concluding “there is no correlation” when H₀ is not rejected; there is insufficient evidence of correlation.",
        ]),
    ],
    "examples": [
        {
            "title": "The PMCC from raw data, and a one-tailed test",
            "question": "Eight students recorded the hours x they spent revising and their test score y. "
                        "x: 2, 4, 5, 6, 8, 9, 11, 13. y: 35, 42, 50, 46, 58, 60, 65, 72. (a) Find r. (b) Test, at the 1% level, "
                        "whether there is positive correlation between hours of revision and score.",
            "steps": [
                "(a) Σx = 58, Σy = 428, Σx² = 516, Σy² = 23978, Σxy = 3419, n = 8.",
                "Sxx = 516 − 58²/8 = 95.5. Syy = 23978 − 428²/8 = 1080. Sxy = 3419 − 58 × 428/8 = 316.",
                "r = 316/√(95.5 × 1080) = 0.984 (3 s.f.). This agrees with the calculator.",
                "(b) H₀: ρ = 0, H₁: ρ > 0, where ρ is the population PMCC between revision time and score.",
                "n = 8, 1% one-tailed critical value 0.7887. 0.984 > 0.7887, so reject H₀.",
                "There is sufficient evidence at the 1% level of positive correlation between hours of revision and test score. "
                "(The test assumes the data come from a bivariate normal distribution.)",
            ],
        },
        {
            "title": "Coding and the PMCC (Edexcel FS2, OCR A 5.08b)",
            "question": "For 10 days, the mean temperature x °C and gas used y kWh by a house were coded as u = x − 10 and "
                        "v = (y − 200)/10. The coded data give Σu = 25, Σv = 40, Σu² = 165, Σv² = 230, Σuv = 40. "
                        "(a) Find Suu, Svv and Suv, and hence r. (b) Find Sxx, Syy and Sxy. (c) Test, at the 5% level and then "
                        "the 1% level, whether gas use is negatively correlated with temperature.",
            "steps": [
                "(a) Suu = 165 − 25²/10 = 102.5. Svv = 230 − 40²/10 = 70. Suv = 40 − 25 × 40/10 = −60.",
                "r = −60/√(102.5 × 70) = −0.708 (3 s.f.). Coding does not change r, so this is also the PMCC between x and y.",
                "(b) x = u + 10, so Sxx = Suu = 102.5. y = 10v + 200, so Syy = 10² × 70 = 7000 and Sxy = 1 × 10 × (−60) = −600. "
                "Check: −600/√(102.5 × 7000) = −0.708.",
                "(c) H₀: ρ = 0, H₁: ρ < 0. n = 10. 5% one-tailed critical value 0.5494: −0.708 < −0.5494, so reject H₀. There is "
                "evidence at the 5% level that gas use is negatively correlated with temperature.",
                "1% one-tailed critical value 0.7155: −0.708 > −0.7155, so H₀ is not rejected at the 1% level. The conclusion depends "
                "on the significance level chosen.",
            ],
        },
        {
            "title": "Spearman's coefficient and a two-tailed test",
            "question": "Two judges ranked eight cakes. Judge A: 1, 2, 3, 4, 5, 6, 7, 8. Judge B (same cakes in the same order): "
                        "2, 1, 4, 3, 6, 8, 5, 7. Test, at the 5% level, whether there is any association between the two judges' rankings.",
            "steps": [
                "The data are ranks, so Spearman's coefficient is appropriate.",
                "d = −1, 1, −1, 1, −1, −2, 2, 1 (Σd = 0 as a check). Σd² = 1 + 1 + 1 + 1 + 1 + 4 + 4 + 1 = 14.",
                "rₛ = 1 − 6 × 14/(8 × 63) = 1 − 84/504 = 0.833 (3 s.f.).",
                "H₀: ρₛ = 0, H₁: ρₛ ≠ 0, where ρₛ is the population rank correlation between the judges' rankings.",
                "n = 8, 5% two-tailed critical value (2.5% one-tailed column) 0.7381. 0.833 > 0.7381, so reject H₀.",
                "There is sufficient evidence at the 5% level of an association between the two judges' rankings; they tend to agree.",
            ],
        },
        {
            "title": "Spearman's coefficient with tied ranks (Edexcel FS2)",
            "question": "Eight plants were given x ml of fertiliser per week and their heights y cm measured. x: 12, 15, 15, 18, 20, 22, "
                        "22, 22. y: 30, 28, 35, 40, 38, 45, 50, 42. Find Spearman's rank correlation coefficient and test, at the 5% "
                        "level, for positive association.",
            "steps": [
                "Rank x from smallest: 12 → 1; the two 15s share ranks 2 and 3, so each gets 2.5; 18 → 4; 20 → 5; the three 22s "
                "share 6, 7, 8, so each gets 7. Ranks of x: 1, 2.5, 2.5, 4, 5, 7, 7, 7.",
                "Ranks of y: 2, 1, 3, 5, 4, 7, 8, 6 (no ties).",
                "With ties, find rₛ as the PMCC of the ranks: Sxx = 39.5, Syy = 42, Sxy = 37 for the ranks, so "
                "rₛ = 37/√(39.5 × 42) = 0.908 (3 s.f.).",
                "(The shortcut formula gives 1 − 6 × 7.5/504 = 0.911, which is close but not exact because of the ties.)",
                "H₀: ρₛ = 0, H₁: ρₛ > 0. n = 8, 5% one-tailed critical value 0.6429. 0.908 > 0.6429, so reject H₀.",
                "There is sufficient evidence at the 5% level of positive association between the amount of fertiliser and plant height.",
            ],
        },
        {
            "title": "Significance, effect size and assumptions (OCR MEI)",
            "question": "A researcher measures two random variables, x and y, on a random sample of 12 adults and finds Sxx = 420, "
                        "Syy = 310 and Sxy = 162. The scatter diagram is roughly elliptical. (a) Find r. (b) Test, at the 5% level, "
                        "whether there is any correlation. (c) Comment on the effect size, given the rule 0.1 small, 0.3 medium, "
                        "0.5 large. (d) Explain why the PMCC test is suitable here.",
            "steps": [
                "(a) r = 162/√(420 × 310) = 0.449 (3 s.f.).",
                "(b) H₀: ρ = 0, H₁: ρ ≠ 0. n = 12, 5% two-tailed critical value 0.5760. 0.449 < 0.5760, so do not reject H₀. There "
                "is insufficient evidence at the 5% level of correlation between x and y.",
                "(c) r = 0.449 is a medium-sized effect, close to large. The test may have failed to detect it because the sample is "
                "small. A larger sample would be needed to decide.",
                "(d) Both variables are random (random on random, Case B) and the elliptical scatter suggests the data could come "
                "from a bivariate normal distribution, which is the assumption of the PMCC test.",
            ],
        },
    ],
    "practice": [
        "For 10 pairs, Σx = 50, Σy = 80, Σx² = 310, Σy² = 700 and Σxy = 440. Find Sxx, Syy, Sxy and the PMCC r.",
        "Six pairs have x = 1, 2, 3, 4, 5, 6 and y = 2, 1, 4, 3, 6, 5. Find r and test H₀: ρ = 0 against H₁: ρ ≠ 0 at the 5% level.",
        "The data (x, y) are coded by u = (x − 50)/2 and v = (100 − y)/4. The PMCC between u and v is 0.84. Write down the PMCC "
        "between x and y, explaining your answer.",
        "Five students are ranked by two teachers. The differences between their ranks are d = 1, −2, 0, 2, −1. Find Spearman's rₛ.",
        "A sample of 10 pairs gives r = −0.6. Test, at the 5% level, whether there is negative correlation in the population.",
        "Seven runners recorded their weekly training distance x (tens of km) and a fitness score y: x: 3.1, 4.5, 2.8, 5.0, "
        "3.9, 4.1, 2.2; y: 12, 15, 14, 18, 11, 16, 9. Find Spearman's rₛ and test, at the 5% level, for positive association.",
        "Rank the values 7, 9, 9, 12, 15, 15, 15, 20, giving tied values the mean of their ranks. Explain why the formula "
        "rₛ = 1 − 6Σd²/(n(n² − 1)) is not exact when there are ties.",
        "State, with a reason, whether the PMCC or Spearman's coefficient is more suitable in each case. (a) Two wine experts "
        "place 9 wines in order of preference. (b) Heights and arm spans of 30 adults, with an elliptical scatter diagram. "
        "(c) Data that increase steeply and then level off. (d) Data with one extreme outlier.",
        "A study finds a strong positive correlation between ice-cream sales and the number of drownings at a beach. Explain why "
        "this does not show that ice-cream causes drowning.",
        "Take x = 1, 2, 3, 4, 5 and y = 1, 4, 9, 16, 25. Show that Spearman's rₛ = 1, and find the PMCC r. Explain the difference.",
        "(OCR MEI) (a) A sample of 20 pairs gives r = 0.45. Is this significant at the 5% level (two-tailed)? Describe the effect "
        "size using 0.1 small, 0.3 medium, 0.5 large. (b) A sample of 100 pairs gives r = 0.2. Repeat (a), using the two-tailed "
        "5% critical value 0.1966. What do (a) and (b) show?",
        "Use the PMCC table to find the smallest sample size n for which r = 0.5 would be significant in a one-tailed test at the "
        "5% level.",
    ],
    "answers": [
        "Sxx = 310 − 50²/10 = 60. Syy = 700 − 80²/10 = 60. Sxy = 440 − 50 × 80/10 = 40. r = 40/√(60 × 60) = 0.667 (3 s.f.).",
        "Sxx = Syy = 17.5, Sxy = 14.5. r = 14.5/17.5 = 0.829 (3 s.f.). n = 6, 5% two-tailed critical value 0.8114. 0.829 > 0.8114: "
        "reject H₀; evidence at the 5% level of correlation.",
        "−0.84. Coding with a positive scale for x (divide by 2) and a negative scale for y (v decreases as y increases) keeps the "
        "size of r but reverses its sign.",
        "Σd² = 1 + 4 + 0 + 4 + 1 = 10. rₛ = 1 − 6 × 10/(5 × 24) = 0.5.",
        "H₀: ρ = 0, H₁: ρ < 0. n = 10, 5% one-tailed critical value 0.5494. −0.6 < −0.5494: reject H₀; evidence of negative "
        "correlation.",
        "Ranks of x: 3, 6, 2, 7, 4, 5, 1. Ranks of y: 3, 5, 4, 7, 2, 6, 1. d = 0, 1, −2, 0, 2, −1, 0, Σd² = 10. "
        "rₛ = 1 − 60/336 = 0.821 (3 s.f.). H₀: ρₛ = 0, H₁: ρₛ > 0. n = 7, critical value 0.7143. 0.821 > 0.7143: reject H₀; "
        "evidence of positive association.",
        "Ranks: 1, 2.5, 2.5, 4, 6, 6, 6, 8. The formula is derived from the PMCC of the ranks using Σ(rank²) = n(n + 1)(2n + 1)/6, "
        "which is only true when the ranks are exactly 1, 2, …, n. With ties Σ(rank²) is smaller, so the formula is approximate.",
        "(a) Spearman: the data are rankings only. (b) PMCC: measured data, likely bivariate normal, linear. (c) Spearman: monotonic "
        "but not linear. (d) Spearman: ranks are much less affected by an outlier (or remove the outlier if it is an error).",
        "Both are likely to be caused by a third variable, hot weather, which brings more people to the beach. Correlation does "
        "not show causation.",
        "The ranks of x and y are identical, so Σd² = 0 and rₛ = 1. Sxx = 10, Syy = 374, Sxy = 60, so r = 60/√3740 = 0.981 (3 s.f.). "
        "The relationship is perfectly monotonic but not linear, so rₛ = 1 while r < 1.",
        "(a) n = 20, critical value 0.4438. 0.45 > 0.4438, so significant (just). Medium to large effect. (b) 0.2 > 0.1966, so "
        "significant, but only a small effect. Significance depends on sample size: a large sample can make a weak relationship "
        "significant, so report the effect size as well.",
        "One-tailed 5% critical values: n = 11: 0.5214 > 0.5 (not significant); n = 12: 0.4973 < 0.5 (significant). So n = 12.",
    ],
    "exam": [
        "(Edexcel FS2 style) The engine size x litres and fuel economy y mpg of 10 cars were coded as u = 10x − 10 and v = y − 30. "
        "The coded data give Σu = 62, Σv = 55, Σu² = 478, Σv² = 571 and Σuv = 232. (a) Find Suu, Svv and Suv. [3] "
        "(b) Find the PMCC between u and v. [2] (c) Write down the PMCC between x and y, giving a reason. [1] (d) Test, at the "
        "5% level, whether there is negative correlation between engine size and fuel economy. [4] (e) State an assumption "
        "needed for the test in (d). [1]",
        "Two judges each ranked 9 dancers. Judge P ranked them 1 to 9; Judge Q ranked the same dancers 3, 1, 2, 5, 4, 7, 9, 6, 8. "
        "(a) Calculate Spearman's rank correlation coefficient. [3] (b) Test, at the 1% level, whether the judges' rankings are "
        "positively associated. [4] (c) Give a reason why Spearman's coefficient is used rather than the PMCC. [1] (d) In another "
        "competition Judge Q gives two dancers exactly the same score. Explain how this affects the ranking and the calculation "
        "of rₛ. [2]",
        "(OCR MEI style) A biologist catches 25 fish at random and measures their length x cm and mass y g. Sxx = 1250, Syy = 880, "
        "Sxy = 412. (a) Explain why this is a case of a random variable on a random variable. [1] (b) Calculate r. [2] "
        "(c) The scatter diagram is elliptical. Test, at the 5% level, whether length and mass are correlated. [5] (d) Comment on "
        "the effect size, using 0.1 small, 0.3 medium, 0.5 large, and on what the biologist should do next. [2]",
        "A town's population y (thousands) was recorded in eight successive decades x = 1, 2, …, 8: y = 2, 3, 5, 4, 14, 25, 46, 90. "
        "(a) Calculate Spearman's rank correlation coefficient. [3] (b) Test, at the 1% level, for positive association between "
        "x and y. [3] (c) For these data Sxx = 42, Syy = 6625.875 and Sxy = 450.5. Find the PMCC. [2] (d) A student says that "
        "because r is close to 1, the population grew linearly. Comment, and explain why Spearman's test is more appropriate "
        "than the PMCC test here. [3]",
    ],
    "exam_answers": [
        "(a) Suu = 478 − 62²/10 = 93.6 B1; Svv = 571 − 55²/10 = 268.5 B1; Suv = 232 − 62 × 55/10 = −109 B1. (b) r = −109/√(93.6 × 268.5) "
        "M1 = −0.688 (3 s.f.) A1. (c) −0.688: linear coding with positive scale factors does not change r B1. (d) H₀: ρ = 0, "
        "H₁: ρ < 0 B1. n = 10, critical value −0.5494 B1. −0.688 < −0.5494 M1, so reject H₀: evidence at the 5% level that larger "
        "engines are associated with lower fuel economy A1. (e) The data come from a bivariate normal distribution (random sample) B1.",
        "(a) d = −2, 1, 1, −1, 1, −1, −2, 2, 1; Σd² = 18 M1 A1. rₛ = 1 − 6 × 18/(9 × 80) = 0.85 A1. (b) H₀: ρₛ = 0, H₁: ρₛ > 0 B1. "
        "n = 9, 1% one-tailed critical value 0.7833 B1. 0.85 > 0.7833 M1: reject H₀; strong evidence that the judges' rankings "
        "agree A1. (c) The data are ranks (judgements), not measurements, so the PMCC/bivariate normal assumption is not "
        "appropriate B1. (d) The two dancers share the two ranks, each getting their mean (e.g. 4.5 and 4.5) B1. rₛ should then be "
        "found as the PMCC of the ranks; the Σd² formula is only approximate B1.",
        "(a) Both length and mass vary randomly from fish to fish; neither is controlled by the biologist B1. (b) r = 412/√(1250 × 880) "
        "M1 = 0.393 (3 s.f.) A1. (c) H₀: ρ = 0, H₁: ρ ≠ 0, ρ the population PMCC B1. n = 25, 5% two-tailed critical value 0.3961 B1. "
        "0.393 < 0.3961 M1: do not reject H₀ A1; insufficient evidence at the 5% level of correlation between length and mass A1. "
        "(d) r ≈ 0.39 is a medium effect, and the result is very close to significance B1. The biologist should collect a larger "
        "sample before deciding B1.",
        "(a) Ranks of y: 1, 2, 4, 3, 5, 6, 7, 8 M1; d = 0, 0, −1, 1, 0, 0, 0, 0, Σd² = 2 A1; rₛ = 1 − 12/504 = 0.976 (3 s.f.) A1. "
        "(b) H₀: ρₛ = 0, H₁: ρₛ > 0. n = 8, 1% one-tailed critical value 0.8333 B1. 0.976 > 0.8333 M1: reject H₀; strong "
        "evidence of positive association A1. (c) r = 450.5/√(42 × 6625.875) M1 = 0.854 (3 s.f.) A1. (d) A high r does not show "
        "linearity: the growth is clearly curved (exponential-like, increasing ever faster) B1. The data are not bivariate normal, "
        "so the PMCC test is not valid B1; Spearman tests for a monotonic association with no distributional assumption B1.",
    ],
}
