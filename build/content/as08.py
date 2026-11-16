UNIT = {
    "number": "AS8",
    "title": "Chi-squared tests for association (contingency tables)",
    "tag": "AS · Edexcel FS1, AQA (SE1–SE5), OCR A, OCR MEI · IAL S3 · CAIE 9231 P4 "
           "(Yates' correction: AQA A level and OCR A only)",
    "notes": [
        ("h2", "8.1 Contingency tables"),
        ("p", "A <b>contingency table</b> shows how a sample is split by two categorical variables at once, for example "
              "age group (rows) and preferred news source (columns). Each cell holds an observed frequency O, and the table "
              "has row totals, column totals and a grand total N. To construct one from raw data (AQA SE1), tally each "
              "individual into the cell for its row category and column category, then add the totals."),
        ("p", "An r × c table has r rows and c columns of data, not counting the totals. The question of interest is whether "
              "the two variables are <b>associated</b>: does knowing the row category change the probabilities of the column "
              "categories?"),
        ("box", "Hypotheses", [
            "H₀: there is no association between the two variables (they are independent) in the population.",
            "H₁: there is an association between the two variables (they are not independent).",
            "Always name the variables in context, e.g. “H₀: there is no association between age group and preferred news source”.",
        ]),
        ("h2", "8.2 Expected frequencies"),
        ("p", "If the variables are independent, P(row i and column j) = P(row i) × P(column j). Estimating these probabilities "
              "by Rᵢ/N and Cⱼ/N and multiplying by N gives the expected frequency."),
        ("box", "Expected frequency and test statistic", [
            "Eᵢⱼ = (row i total × column j total)/(grand total) = RᵢCⱼ/N.",
            "X² = Σ (O − E)²/E over all cells, approximately χ²<sub>ν</sub> under H₀ if every E is large enough.",
            "ν = (r − 1)(c − 1), where r and c are the numbers of rows and columns after any combining.",
            "Reject H₀ if X² exceeds the upper-tail critical value. The test is always upper-tailed.",
        ]),
        ("p", "Each row of E adds to the same row total as O, and each column adds to the same column total. Use this to check "
              "your arithmetic, or to find the last E in a row or column by subtraction."),
        ("h2", "8.3 Why ν = (r − 1)(c − 1)"),
        ("p", "The expected frequencies are built from the row and column totals, so the table is constrained to have those "
              "totals. Once (r − 1)(c − 1) cells in the top-left block are chosen, every other cell is fixed by the totals. "
              "So there are (r − 1)(c − 1) “free” cells. For example, a 3 × 4 table has 2 × 3 = 6 degrees of freedom, and "
              "a 2 × 2 table has only 1."),
        ("table", ["Table size", "ν", "5% critical value", "1% critical value"], [
            ["2 × 2", "1", "3.841", "6.635"],
            ["2 × 3 or 3 × 2", "2", "5.991", "9.210"],
            ["2 × 4 or 4 × 2", "3", "7.815", "11.345"],
            ["3 × 3, 2 × 5 or 5 × 2", "4", "9.488", "13.277"],
            ["3 × 4 or 4 × 3", "6", "12.592", "16.812"],
            ["4 × 4", "9", "16.919", "21.666"],
        ]),
        ("h2", "8.4 Small expected frequencies: combining rows or columns"),
        ("p", "As in goodness-of-fit tests, the χ² approximation is poor when expected frequencies are small. If any E is "
              "below 5, combine a row (or column) with another, then recalculate the expected frequencies and the degrees of "
              "freedom. AQA states the convention as “all Eᵢ should be greater than 5” (SE3); other boards say at least 5. "
              "In practice the difference rarely matters, but follow your board's wording."),
        ("bullets", [
            "Combine whole rows or whole columns, never single cells, so the table stays rectangular.",
            "Combine categories that make sense together in context (e.g. “minor fault” with “major fault” to make “faulty”), "
            "and say why.",
            "Recalculate ν from the new table. Combining reduces ν, which reduces the critical value.",
            "If you would need to combine a 2 × 2 table, the test cannot be done: collect more data.",
        ]),
        ("h2", "8.5 Contributions and sources of association"),
        ("p", "When H₀ is rejected you should say <b>where</b> the association comes from (AQA SE4, OCR A, OCR MEI SH2). "
              "Look for the cells with the largest contributions (O − E)²/E, then compare O with E in those cells. Write in "
              "context, for example “more students in Business travel by car than would be expected if faculty and "
              "transport were independent”. A cell with a small contribution shows behaviour close to independence."),
        ("p", "OCR MEI questions often show software output: tables of observed values, expected values and contributions, "
              "with X², ν and a p-value. You may have to fill in a missing expected value or contribution, then interpret."),
        ("h2", "8.6 Yates' continuity correction for 2 × 2 tables (AQA A level, OCR A)"),
        ("p", "X² is calculated from discrete counts, but it is compared with the continuous χ² distribution. With ν = 1 this "
              "approximation tends to give X² values that are too large, so H₀ is rejected too often. Yates' correction "
              "reduces each |O − E| by 0.5 before squaring."),
        ("box", "Yates' corrected statistic (2 × 2 tables only)", [
            "X²<sub>Yates</sub> = Σ (|O − E| − 0.5)²/E, with ν = 1.",
            "In a 2 × 2 table |O − E| is the same in all four cells, because each row and column of O − E adds to zero.",
            "The corrected value is always smaller than the uncorrected value, so the corrected test is more cautious.",
        ]),
        ("table", ["Board", "Rule for expected frequencies", "Yates' correction"], [
            ["Edexcel FS1 (9FM0/8FM0)", "Combine when E < 5", "Not on the specification"],
            ["IAL S3", "Combine when E < 5", "Not required"],
            ["AQA 7367/7366", "All E should be greater than 5", "A level only: know when and how to apply it (SE5)"],
            ["OCR A H245/H235", "Combine so that each E ≥ 5", "Required for 2 × 2 tables (AS and A level)"],
            ["OCR MEI H645/H635", "Combine so that each E ≥ 5", "Not expected, but not penalised if used appropriately"],
            ["CAIE 9231 Paper 4", "Combine so that each E ≥ 5", "Not required"],
        ]),
        ("h2", "8.7 Conclusions and p-values"),
        ("bullets", [
            "Reject H₀: “There is sufficient evidence at the 5% level of an association between age group and news source.”",
            "Do not reject H₀: “There is insufficient evidence at the 5% level of an association between …”. Do not write "
            "“insufficient evidence that they are independent” (a Cambridge examiner-report error).",
            "A p-value from software or a calculator: reject H₀ if p < the significance level.",
            "Association is not causation: a significant result does not show that one variable causes the other.",
        ]),
        ("warn", "Common mistakes", [
            "Using (r − 1)(c − 1) with the numbers of rows and columns before combining, or counting the total row and column.",
            "Combining single cells, or combining categories that make no sense together.",
            "Rounding E to whole numbers, or dividing by O instead of E.",
            "Using Yates' correction for tables larger than 2 × 2. It is only for ν = 1.",
            "Forgetting the 0.5 is subtracted from |O − E| before squaring, not from (O − E)².",
            "Stating the source of association without context, or without comparing O and E (more or fewer than expected?).",
            "Concluding “the variables are independent” when H₀ is not rejected. The data are only consistent with independence.",
        ]),
    ],
    "examples": [
        {
            "title": "A 2 × 2 table, with and without Yates' correction",
            "question": "A college compares two revision courses. Of 50 students on course A, 30 passed and 20 failed. Of 50 "
                        "students on course B, 20 passed and 30 failed. Test, at the 5% level, whether there is an association "
                        "between course and result (a) without Yates' correction, (b) with Yates' correction.",
            "steps": [
                "H₀: there is no association between revision course and result. H₁: there is an association.",
                "Row totals 50, 50; column totals pass 50, fail 50; N = 100. Every E = 50 × 50/100 = 25.",
                "(a) Every |O − E| = 5, so each contribution is 25/25 = 1 and X² = 4. ν = (2 − 1)(2 − 1) = 1; critical value 3.841. "
                "4 > 3.841, so reject H₀: there is sufficient evidence at the 5% level of an association between course and "
                "result (Edexcel, IAL S3, OCR MEI, CAIE).",
                "(b) Each corrected contribution is (5 − 0.5)²/25 = 0.81, so X²<sub>Yates</sub> = 3.24. 3.24 < 3.841, so do not reject H₀: "
                "insufficient evidence at the 5% level of an association (AQA A level, OCR A).",
                "The two methods disagree because X² is close to the critical value. Yates' correction is more cautious.",
            ],
        },
        {
            "title": "A 2 × 3 table and interpreting contributions",
            "question": "People choose their favourite of three designs, A, B and C. Under-30s: A 20, B 25, C 15. Over-30s: A 30, "
                        "B 15, C 25. Test, at the 5% level, whether preference is associated with age group, and describe any association.",
            "steps": [
                "H₀: there is no association between age group and preferred design. H₁: there is an association.",
                "Row totals 60 and 70; column totals 50, 40, 40; N = 130. E(under-30, A) = 60 × 50/130 = 23.08.",
                "Under-30s: E = 23.08, 18.46, 18.46. Over-30s: E = 26.92, 21.54, 21.54. All E ≥ 5.",
                "Contributions: 0.410, 2.316, 0.649 and 0.352, 1.985, 0.556. X² = 6.27 (3 s.f.).",
                "ν = (2 − 1)(3 − 1) = 2; critical value 5.991. 6.27 > 5.991, so reject H₀. There is sufficient evidence at the 5% "
                "level of an association between age group and preferred design.",
                "The largest contributions are for design B: under-30s chose B more often than expected (25 against 18.46) "
                "and over-30s less often (15 against 21.54).",
            ],
        },
        {
            "title": "A 3 × 3 table that needs combining",
            "question": "A survey asks 197 adults for their main news source. 16–30: TV 20, Online 45, Print 2. 31–50: TV 30, "
                        "Online 35, Print 4. Over 50: TV 40, Online 15, Print 6. Test, at the 1% level, whether news source is "
                        "associated with age group.",
            "steps": [
                "H₀: no association between age group and main news source. H₁: there is an association.",
                "Row totals 67, 69, 61; column totals TV 90, Online 95, Print 12; N = 197.",
                "E(Print) = 67 × 12/197 = 4.08, 4.20 and 3.72: all below 5. Combine Print with TV as “traditional media” "
                "(TV or print), which makes sense in context. New observed table: 22, 45 / 34, 35 / 46, 15.",
                "E(traditional) = 67 × 102/197 = 34.69, 35.73, 31.58. E(online) = 32.31, 33.27, 29.42.",
                "Contributions: 4.642, 4.984 / 0.083, 0.090 / 6.580, 7.065. X² = 23.4 (3 s.f.).",
                "The table is now 3 × 2, so ν = (3 − 1)(2 − 1) = 2. The 1% critical value is 9.210.",
                "23.4 > 9.210, so reject H₀. There is strong evidence (1% level) of an association between age and news source. "
                "Over-50s use traditional media more than expected and online less; 16–30s show the reverse. The 31–50 group is "
                "close to what independence predicts.",
            ],
        },
        {
            "title": "Finding the sources of association in a 3 × 4 table",
            "question": "100 students from each of three faculties were asked how they usually travel to college (Walk, Cycle, "
                        "Bus, Car). Science: 30, 25, 35, 10. Arts: 35, 15, 40, 10. Business: 15, 10, 45, 30. Test, at the 5% level, "
                        "for an association, and identify the main sources of any association.",
            "steps": [
                "H₀: no association between faculty and method of travel. H₁: there is an association.",
                "Each row total is 100 and N = 300, so every row has the same E: 100 × 80/300 = 26.67 (Walk), 16.67 (Cycle), "
                "40.00 (Bus), 16.67 (Car).",
                "Contributions: Science 0.417, 4.167, 0.625, 2.667; Arts 2.604, 0.167, 0.000, 2.667; Business 5.104, 2.667, 0.625, 10.667.",
                "X² = 32.4 (3 s.f.). ν = (3 − 1)(4 − 1) = 6; 5% critical value 12.592. 32.4 > 12.592, so reject H₀: there is "
                "sufficient evidence at the 5% level of an association between faculty and method of travel.",
                "Largest contributions: Business–Car (10.667): 30 drive against 16.67 expected. Business–Walk (5.104): fewer walk "
                "than expected. Science–Cycle (4.167): more Science students cycle than expected. Bus use (all small "
                "contributions) is about the same in every faculty.",
            ],
        },
        {
            "title": "Combining to a 2 × 2 table and using Yates' correction (AQA A level, OCR A)",
            "question": "In a trial, 45 patients received a new treatment and 45 a placebo. New treatment: improved 28, no change 14, "
                        "worse 3. Placebo: improved 18, no change 22, worse 5. Test, at the 5% level, whether outcome is "
                        "associated with treatment.",
            "steps": [
                "H₀: there is no association between treatment and outcome. H₁: there is an association.",
                "Column total for “worse” is 8, so E = 45 × 8/90 = 4.0 in both rows, below 5. Combine “no change” and "
                "“worse” into “not improved”: New 28, 17; Placebo 18, 27.",
                "Now a 2 × 2 table: column totals 46 and 44, so E = 23, 22, 23, 22 and every |O − E| = 5.",
                "With Yates' correction: X² = (4.5)²/23 + (4.5)²/22 + (4.5)²/23 + (4.5)²/22 = 3.60 (3 s.f.). ν = 1, critical value 3.841.",
                "3.60 < 3.841, so do not reject H₀. There is insufficient evidence at the 5% level of an association between "
                "treatment and outcome.",
                "Note: without the correction X² = 4.45 > 3.841, which would lead to rejecting H₀ (the method for Edexcel, IAL S3, "
                "OCR MEI and CAIE). Close calls like this are exactly where Yates' correction matters.",
            ],
        },
    ],
    "practice": [
        "Students in Year 12 and Year 13 choose one of three clubs. Year 12: Chess 12, Drama 18, Music 10. Year 13: Chess 28, "
        "Drama 22, Music 30. (a) Find all the expected frequencies under independence. (b) Calculate X² and test at the 5% level "
        "whether club choice is associated with year group.",
        "Find ν for a χ² test on (a) a 3 × 4 table, (b) a 5 × 2 table, (c) a 4 × 3 table in which two rows are combined into "
        "one, (d) a 2 × 2 table.",
        "Males and females are asked whether they prefer tea or coffee. Male: tea 40, coffee 10. Female: tea 30, coffee 20. Test, "
        "at the 5% level, whether preference is associated with gender (a) without Yates' correction, (b) with Yates' correction.",
        "Urban (100 people) and rural (80 people) residents were asked how they usually travel. Urban: bus 50, car 30, walk 20. "
        "Rural: bus 10, car 40, walk 30. Test, at the 5% level, whether method of travel is associated with location.",
        "State suitable hypotheses for a test on a 4 × 3 contingency table of hair colour against eye colour. Find the degrees "
        "of freedom and the critical values at the 5% and 1% levels.",
        "Explain why, in any 2 × 2 contingency table, the value of |O − E| is the same for all four cells.",
        "(OCR MEI style) Software output for a 3 × 3 table gives these contributions: row 1: 0.42, 3.10, 1.25; row 2: 0.08, 0.95, "
        "0.31; row 3: 2.60, 0.07, 4.45. (a) Find X² and carry out the test at the 5% level. (b) Which cells contribute most to "
        "the result?",
        "In a 3 × 3 table, the expected frequencies in the third row are 3.2, 4.1 and 2.7, and all other E are above 10. "
        "Explain what should be done before the test, and state the degrees of freedom and the 5% critical value afterwards.",
        "A test on a 2 × 4 contingency table gives a p-value of 0.031. State the degrees of freedom and the conclusions at the "
        "5% and 1% levels.",
        "For the 2 × 2 table with rows (12, 8) and (6, 14), calculate X² both without and with Yates' correction, and test at "
        "the 5% level.",
        "Explain (a) why small expected frequencies are a problem in a χ² test, and (b) why categories that are combined should "
        "make sense together.",
        "A 2 × 2 table has row totals 40 and 60, column totals 30 and 70. Find all four expected frequencies, and explain why the "
        "test has only one degree of freedom.",
    ],
    "answers": [
        "(a) Row totals 40, 80; column totals 40, 40, 40; N = 120. Year 12: E = 13.33 each; Year 13: E = 26.67 each. "
        "(b) Contributions 0.133, 1.633, 0.833, 0.067, 0.817, 0.417; X² = 3.90. ν = 2, critical value 5.991. 3.90 < 5.991: do not "
        "reject H₀; insufficient evidence of an association between club and year group.",
        "(a) 2 × 3 = 6. (b) 4 × 1 = 4. (c) now 3 × 3, so 2 × 2 = 4. (d) 1.",
        "E: male tea 35, coffee 15; female tea 35, coffee 15. |O − E| = 5. (a) X² = 2 × 25/35 + 2 × 25/15 = 4.76 (3 s.f.) > 3.841: "
        "reject H₀; evidence of an association. (b) X² = 2 × 4.5²/35 + 2 × 4.5²/15 = 3.86 (3 s.f.) > 3.841: still reject H₀ "
        "(only just).",
        "E: urban 33.33, 38.89, 27.78; rural 26.67, 31.11, 22.22. Contributions 8.333, 2.032, 2.178, 10.417, 2.540, 2.722. "
        "X² = 28.2 (3 s.f.). ν = 2, critical value 5.991. Reject H₀: strong evidence of an association (rural residents use the "
        "bus much less than expected).",
        "H₀: no association between hair colour and eye colour in the population; H₁: there is an association. ν = 3 × 2 = 6. "
        "Critical values 12.592 (5%) and 16.812 (1%).",
        "The expected totals in each row and column equal the observed totals, so in each row (O − E) for the two cells add to "
        "zero, and similarly for each column. So if O − E = d in the top-left cell, the others are −d, −d and d.",
        "(a) X² = 13.23. ν = 4, 5% critical value 9.488. 13.23 > 9.488: reject H₀; evidence of an association. (b) Row 3 column 3 "
        "(4.45), row 1 column 2 (3.10) and row 3 column 1 (2.60).",
        "Combine row 3 with an adjacent row that makes sense in context (and recalculate E). The table becomes 2 × 3: ν = 2, "
        "5% critical value 5.991.",
        "ν = 1 × 3 = 3. 0.031 < 0.05: reject H₀ at 5%, evidence of an association. 0.031 > 0.01: do not reject H₀ at 1%.",
        "E = 9, 11, 9, 11 and |O − E| = 3. Without Yates: X² = 9/9 + 9/11 + 9/9 + 9/11 = 3.64 (3 s.f.). With Yates: "
        "X² = 2.5²(2/9 + 2/11) = 2.53 (3 s.f.). Both are below 3.841: do not reject H₀ at 5%.",
        "(a) A small E in the denominator can give a very large contribution from a small difference, and the χ² distribution is "
        "then a poor approximation to the distribution of X², so the test is unreliable. (b) The combined table must still answer "
        "a meaningful question, and the conclusion must be interpretable in context.",
        "E = 40 × 30/100 = 12, 40 × 70/100 = 28, 60 × 30/100 = 18, 60 × 70/100 = 42. Given the row and column totals, once one "
        "cell is known the other three are fixed by subtraction, so ν = (2 − 1)(2 − 1) = 1.",
    ],
    "exam": [
        "200 adults were asked their favourite form of exercise. Aged 18–34: gym 40, running 25, swimming 15. Aged 35–54: gym 30, "
        "running 20, swimming 20. Aged 55 and over: gym 10, running 15, swimming 25. (a) Show that the expected frequency for "
        "the over-55s who prefer the gym is 20. [1] (b) Test, at the 5% level, whether favourite exercise is associated with age "
        "group. [6] (c) Identify the two largest contributions and interpret them in context. [3] (d) State, with a reason, "
        "whether your conclusion would be different at the 1% level. [1]",
        "(AQA A level, OCR A) An insurer records whether drivers made a claim last year. Under 25: claim 18, no claim 42. Aged 25 "
        "and over: claim 22, no claim 118. (a) Find the expected frequencies. [2] (b) Using Yates' correction, test at the 2.5% "
        "level whether making a claim is associated with age group. [6] (c) Explain why Yates' correction is used here, and "
        "state what the conclusion would have been without it. [2]",
        "A factory classifies items made on four shifts as good, minor fault or major fault. Early: 45, 10, 2. Day: 50, 12, 3. "
        "Late: 40, 15, 4. Night: 25, 18, 6. (a) Show that some expected frequencies are less than 5, and explain how to deal with "
        "this. [2] (b) Test, at the 5% level, whether quality is associated with shift. [7] (c) Comment on the night shift. [2]",
        "(OCR MEI style) A teacher records the favourite subject of 80 boys and 100 girls. Software output: Observed: boys: Maths 30, "
        "Science 25, English 15, Art 10; girls: 20, 25, 30, 25. Expected: boys: 22.22, 22.22, 20.00, a; girls: 27.78, 27.78, "
        "25.00, 19.44. Contributions: boys: 2.722, 0.347, 1.250, b; girls: 2.178, 0.278, 1.000, 1.587. Chi-squared = 11.35, "
        "p-value = 0.00999. (a) Find a and b. [3] (b) State the degrees of freedom. [1] (c) Carry out the test at the 1% level, "
        "stating your hypotheses. [3] (d) Describe the association shown by the largest contributions. [3]",
    ],
    "exam_answers": [
        "(a) 50 × 80/200 = 20 B1. (b) H₀: no association between age group and favourite exercise; H₁: association B1. "
        "E: 32, 24, 24 / 28, 21, 21 / 20, 15, 15 M1 A1. Contributions 2.000, 0.042, 3.375 / 0.143, 0.048, 0.048 / 5.000, 0.000, "
        "6.667; X² = 17.3 (3 s.f.) A1. ν = 2 × 2 = 4, critical value 9.488 B1. 17.3 > 9.488: reject H₀; sufficient evidence of an "
        "association between age and favourite exercise A1. (c) Over-55s and swimming (6.667): 25 against 15 expected, so more "
        "older adults prefer swimming B1 B1. Over-55s and gym (5.000): 10 against 20, fewer prefer the gym than expected B1. "
        "(d) 1% critical value 13.277 < 17.3, so the conclusion is the same B1.",
        "(a) Row totals 60, 140; column totals 40, 160; N = 200. E = 12, 48, 28, 112 M1 A1. (b) H₀: no association between age group "
        "and making a claim; H₁: association B1. |O − E| = 6 in every cell M1. X²<sub>Yates</sub> = 5.5²(1/12 + 1/48 + 1/28 + 1/112) = "
        "2.521 + 0.630 + 1.080 + 0.270 = 4.50 (3 s.f.) M1 A1. ν = 1, 2.5% critical value 5.024 B1. 4.50 < 5.024: do not reject H₀; "
        "insufficient evidence at the 2.5% level of an association A1. (c) It is a 2 × 2 table (ν = 1), where the continuous χ² "
        "approximation to the discrete statistic is poorest; the correction stops X² being too large B1. Without it, X² = 5.36 "
        "> 5.024 and H₀ would be rejected B1.",
        "(a) Column total for major fault is 15 and N = 230, so e.g. E(early, major) = 57 × 15/230 = 3.72 < 5 (all four are below 5) "
        "B1. Combine minor and major into “faulty”, which makes sense B1. (b) H₀: no association between shift and quality B1. "
        "New table: good 45, 50, 40, 25; faulty 12, 15, 19, 24. E(good) = 39.65, 45.22, 41.04, 34.09; E(faulty) = 17.35, 19.78, "
        "17.96, 14.91 M1 A1. Contributions 0.721, 1.649, 0.506, 1.156, 0.027, 0.061, 2.422, 5.537; X² = 12.1 (3 s.f.) A1. "
        "ν = (4 − 1)(2 − 1) = 3 B1, critical value 7.815 B1. 12.1 > 7.815: reject H₀; evidence of an association between shift "
        "and quality A1. (Using the uncombined 4 × 3 table would wrongly give X² = 12.50 < 12.592 with ν = 6.) (c) The night shift "
        "gives the largest contributions: 24 faulty items against 14.91 expected and fewer good items than expected, so quality "
        "is worse at night B1 B1.",
        "(a) a = 80 × 35/180 = 15.56 M1 A1 (or 35 − 19.44). b = (10 − 15.56)²/15.56 = 1.984 A1. (b) ν = (2 − 1)(4 − 1) = 3 B1. "
        "(c) H₀: no association between gender and favourite subject; H₁: association B1. p = 0.00999 < 0.01 M1, so reject H₀: "
        "sufficient evidence at the 1% level of an association A1. (d) Boys–Maths (2.722) and girls–Maths (2.178): more boys and "
        "fewer girls chose Maths than expected B1. Boys–Art (1.984): fewer boys chose Art than expected B1. Similarly, girls chose "
        "English and Art more than expected; Science is close to independence B1.",
    ],
}
