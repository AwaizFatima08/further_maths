UNIT = {
    "number": "AS10",
    "title": "Linear regression: least squares and residuals",
    "tag": "AS · Edexcel FS2 topic 1 (AS: 8FM0), OCR A 5.09 (y on x only), OCR MEI Sb11–Sb15 (y on x and x on y) · "
           "revision for IAL S3 · not on AQA or CAIE",
    "notes": [
        ("h2", "10.1 Explanatory and response variables"),
        ("p", "In regression we use one variable to predict another. The <b>explanatory</b> (independent) variable x is the one "
              "we use to predict; the <b>response</b> (dependent) variable y is the one we predict. Often x is <b>controlled</b>: "
              "its values are chosen by the experimenter, such as fixed oven temperatures. Then only y is random "
              "(“random on non-random”, OCR MEI Case A). Plot x horizontally and y vertically."),
        ("p", "If both variables are random (“random on random”, Case B), such as the heights of fathers and sons, either "
              "could be used to predict the other. That is when the second regression line of 10.8 is needed (OCR MEI only)."),
        ("h2", "10.2 The least squares regression line"),
        ("p", "For each data point the <b>residual</b> is e = y − ŷ, the observed value minus the value predicted by the line "
              "ŷ = a + bx. It is the vertical distance from the point to the line, positive if the point lies above the line. "
              "The <b>least squares</b> line is the line that makes the residual sum of squares Σe² as small as possible. "
              "Squaring stops positive and negative residuals cancelling and penalises large errors most."),
        ("box", "Regression line of y on x", [
            "ŷ = a + bx, with b = Sxy/Sxx and a = ȳ − b x̄.",
            "Sxx = Σx² − (Σx)²/n and Sxy = Σxy − (Σx)(Σy)/n (as in AS9).",
            "The line always passes through the mean point (x̄, ȳ).",
            "b = r × (s<sub>y</sub>/s<sub>x</sub>), so b has the same sign as the PMCC r.",
            "The residuals always add to zero: Σe = 0.",
        ]),
        ("p", "Where the formulae come from (not required by any board): Σe² = Σ(y − a − bx)² is a quadratic in a and in b. "
              "Setting its partial derivatives to zero gives Σ(y − a − bx) = 0, which means the line passes through (x̄, ȳ), and "
              "Σx(y − a − bx) = 0, which gives b = Sxy/Sxx."),
        ("p", "Calculators give a and b directly from raw data in regression mode. From summary statistics, use the formulae. "
              "Keep the unrounded values of a and b in your calculator for predictions; quote them to 3 s.f."),
        ("h2", "10.3 Using and interpreting the line"),
        ("bullets", [
            "<b>Gradient b</b>: the estimated change in y for each increase of 1 unit in x, in context and with units, e.g. "
            "“each extra hour of revision is associated with about 2.85 more marks”.",
            "<b>Intercept a</b>: the estimated value of y when x = 0. Only interpret it if x = 0 is meaningful and near the data.",
            "<b>Interpolation</b>: estimating y for an x inside the range of the data. Usually reliable if the points lie close "
            "to the line (r close to ±1) and n is not tiny.",
            "<b>Extrapolation</b>: estimating y for an x outside the range of the data. Unreliable, because there is no evidence "
            "that the linear relationship continues; it may give impossible values.",
            "Use the y on x line only to estimate y from x. Do not rearrange it to estimate x from y.",
            "Reliability (OCR A 5.09e): comment on whether the estimate is interpolation, how strong the correlation is, and the "
            "sample size. Any estimate has uncertainty because the points do not lie exactly on the line.",
        ]),
        ("h2", "10.4 Coding (Edexcel FS2, OCR A 5.09d)"),
        ("p", "If the data are coded as u = (x − p)/q and v = (y − s)/t, find the regression line of v on u from the coded "
              "values, then substitute u and v back and rearrange to get y in terms of x. This works because coding is "
              "linear, so a straight line in (u, v) is a straight line in (x, y)."),
        ("box", "Coding results", [
            "If v = c + du is the coded line, then (y − s)/t = c + d(x − p)/q, so y = s + tc + (td/q)(x − p).",
            "The gradient in original units is b = (t/q) × d. Adding constants changes only the intercept.",
            "Sxx = q² Suu and Sxy = qt Suv, so b = Sxy/Sxx = (t/q)(Suv/Suu), the same result.",
        ]),
        ("h2", "10.5 Residuals and residual analysis (Edexcel FS2, OCR MEI Sb12)"),
        ("p", "Residuals show how well a linear model fits. Plot the residuals against x. If the linear model is suitable, the "
              "residuals are small and scattered randomly about zero, with no pattern."),
        ("table", ["Residual plot", "What it suggests"], [
            ["Random scatter about 0, roughly constant spread", "A linear model is suitable"],
            ["A curved pattern (e.g. positive, negative, positive)", "The relationship is not linear; a curve would fit better"],
            ["Spread increasing (fan shape)", "Variation in y grows with x; predictions at large x are less reliable"],
            ["One residual much larger in size than the rest", "A possible outlier: check it for an error"],
        ]),
        ("p", "An <b>outlier</b> is a point with an unusually large residual. If it is a recording error, or it comes from a "
              "different situation, remove it and recalculate the line: this <b>refines the model</b>. Do not remove a point just "
              "because it does not fit; give a reason in context."),
        ("h2", "10.6 Residual sum of squares (Edexcel FS2)"),
        ("box", "Residual sum of squares", [
            "RSS = Σe² = Syy − (Sxy)²/Sxx.",
            "Equivalently RSS = Syy(1 − r²), so RSS = 0 exactly when r = ±1 (all points on the line).",
            "A smaller RSS means the points lie closer to the line. RSS is the quantity the least squares line minimises.",
        ]),
        ("p", "RSS has the units of y², and depends on n and on the scale of y, so compare RSS values only for models fitted to "
              "the same y data, e.g. before and after removing an outlier. Derivation of the formula is not required."),
        ("h2", "10.7 Checking the fit"),
        ("bullets", [
            "Look at the scatter diagram first: is the pattern roughly straight?",
            "r² is the proportion of the variation in y explained by the line (OCR MEI Sb14). For example r = 0.9 gives "
            "r² = 0.81: 81% of the variation in y is explained by the linear relationship with x.",
            "Residuals: small, random, no outliers (10.5).",
        ]),
        ("h2", "10.8 The regression line of x on y (OCR MEI only)"),
        ("p", "When both variables are random (Case B), you may want to estimate x from a given y. Then minimise the "
              "<b>horizontal</b> distances from the points to the line instead. This gives the regression line of x on y. "
              "OCR A excludes it, and it should never be used when x is controlled."),
        ("box", "Two regression lines", [
            "y on x: y − ȳ = (Sxy/Sxx)(x − x̄). Use it to estimate y from a given x.",
            "x on y: x − x̄ = (Sxy/Syy)(y − ȳ). Use it to estimate x from a given y.",
            "Both lines pass through (x̄, ȳ), so they cross at the mean point.",
            "The product of the two gradients b<sub>yx</sub> × b<sub>xy</sub> = Sxy²/(Sxx Syy) = r². The lines are the same only when r = ±1, and "
            "they are far apart when r is close to 0.",
        ]),
        ("warn", "Common mistakes", [
            "Using Syy instead of Sxx in b = Sxy/Sxx for the y on x line.",
            "Rounding b too early and then finding a = ȳ − b x̄ with the rounded value.",
            "Calculating residuals as ŷ − y. The residual is observed minus predicted, y − ŷ.",
            "Rearranging the y on x line to estimate x. Use the x on y line (MEI) or state that the estimate is unreliable.",
            "Extrapolating without comment, or interpreting the intercept when x = 0 is far outside the data.",
            "Forgetting to undo the coding, or undoing it in the wrong order.",
            "Interpreting the gradient without context and units, or as proof of cause and effect.",
            "Removing an outlier without giving a reason.",
        ]),
    ],
    "examples": [
        {
            "title": "Finding and using a regression line from raw data",
            "question": "A chemist sets the temperature x °C of a reaction and measures the yield y grams. x: 10, 15, 20, 25, 30, 35, 40. "
                        "y: 12.1, 14.8, 17.2, 19.9, 21.5, 25.0, 26.9. (a) Find the regression line of y on x. (b) Interpret the gradient. "
                        "(c) Estimate the yield at 28 °C and at 60 °C, and comment on the reliability of each estimate.",
            "steps": [
                "(a) x is controlled, so the y on x line is appropriate. Σx = 175, Σy = 137.4, Σx² = 5075, Σxy = 3780.5, n = 7.",
                "Sxx = 5075 − 175²/7 = 700. Sxy = 3780.5 − 175 × 137.4/7 = 345.5.",
                "b = 345.5/700 = 0.4936 (4 s.f.). x̄ = 25, ȳ = 19.629, so a = 19.629 − 0.4936 × 25 = 7.289. Line: ŷ = 7.29 + 0.494x.",
                "(b) Each 1 °C rise in temperature is associated with an increase of about 0.494 g in yield.",
                "(c) x = 28: ŷ = 7.289 + 0.4936 × 28 = 21.1 g. This is interpolation and the points lie very close to a line "
                "(r = 0.998), so it is reliable.",
                "x = 60: ŷ = 36.9 g. This is extrapolation well beyond 40 °C, so it is unreliable: the reaction may behave "
                "differently at higher temperatures.",
            ],
        },
        {
            "title": "A regression line from coded data (Edexcel FS2, OCR A)",
            "question": "The length x mm and mass y mg of 8 beetles are coded as u = (x − 20)/5 and v = (y − 100)/4. The coded data "
                        "give Σu = 28, Σv = 36, Σu² = 140, Σv² = 200, Σuv = 158. (a) Find the regression line of v on u. "
                        "(b) Hence find the regression line of y on x. (c) Find the PMCC between x and y.",
            "steps": [
                "(a) Suu = 140 − 28²/8 = 42. Suv = 158 − 28 × 36/8 = 32. Gradient 32/42 = 0.7619.",
                "ū = 3.5, v̄ = 4.5, so the intercept is 4.5 − 0.7619 × 3.5 = 1.833. Line: v = 1.833 + 0.762u.",
                "(b) Substitute: (y − 100)/4 = 1.8333 + 0.7619(x − 20)/5.",
                "y = 100 + 7.333 + 0.6095(x − 20) = 107.333 − 12.190 + 0.6095x, so y = 95.1 + 0.610x (3 s.f.).",
                "Check: the gradient is (4/5) × 0.7619 = 0.6095, and x̄ = 20 + 5 × 3.5 = 37.5, ȳ = 100 + 4 × 4.5 = 118 lies on the line.",
                "(c) Svv = 200 − 36²/8 = 38. r = 32/√(42 × 38) = 0.801 (3 s.f.), unchanged by coding.",
            ],
        },
        {
            "title": "Residuals, RSS and an outlier (Edexcel FS2)",
            "question": "For x = 1, 2, …, 8 the values of y are 3.1, 4.9, 7.2, 8.8, 15.0, 13.1, 15.2, 16.8. Σy = 84.1, "
                        "Σy² = 1072.79, Σxy = 464.1. (a) Find the regression line of y on x. (b) Find the residuals and identify a "
                        "possible outlier. (c) Find the RSS using the formula and check it. (d) Without the outlier the line is "
                        "ŷ = 1.05 + 1.99x with RSS 0.186. Comment.",
            "steps": [
                "(a) Σx = 36, Σx² = 204. Sxx = 204 − 36²/8 = 42, Sxy = 464.1 − 36 × 84.1/8 = 85.65, Syy = 1072.79 − 84.1²/8 = 188.69.",
                "b = 85.65/42 = 2.039, a = 10.5125 − 2.039 × 4.5 = 1.336. Line: ŷ = 1.34 + 2.04x.",
                "(b) Residuals e = y − ŷ: −0.275, −0.514, −0.254, −0.693, 3.468, −0.471, −0.411, −0.850 (they add to 0).",
                "The residual at x = 5 (3.468) is much larger than all the others, so (5, 15.0) is a possible outlier.",
                "(c) RSS = Syy − Sxy²/Sxx = 188.69 − 85.65²/42 = 14.0 (3 s.f.). Squaring and adding the residuals gives the same value. "
                "The single outlier contributes 3.468² = 12.0 of it.",
                "(d) Removing the point reduces the RSS from 14.0 to 0.186, and the other residuals were all negative because the "
                "outlier pulled the line upwards. If (5, 15.0) is an error, the refined line ŷ = 1.05 + 1.99x is a much better model.",
            ],
        },
        {
            "title": "Both regression lines (OCR MEI)",
            "question": "For 10 students, x is the Maths mark and y the Physics mark; both are random. x̄ = 60, ȳ = 55, Sxx = 1600, "
                        "Syy = 2500, Sxy = 1500. (a) Find the regression line of y on x and the regression line of x on y. "
                        "(b) Estimate the Physics mark of a student who scored 70 in Maths, and the Maths mark of a student who "
                        "scored 40 in Physics. (c) Show that the product of the gradients equals r².",
            "steps": [
                "(a) y on x: gradient 1500/1600 = 0.9375. y − 55 = 0.9375(x − 60), so y = −1.25 + 0.9375x.",
                "x on y: gradient 1500/2500 = 0.6. x − 60 = 0.6(y − 55), so x = 27 + 0.6y.",
                "(b) Physics from Maths uses y on x: y = −1.25 + 0.9375 × 70 = 64.4 (3 s.f.).",
                "Maths from Physics uses x on y: x = 27 + 0.6 × 40 = 51. (Rearranging the y on x line would wrongly give 44.0.)",
                "(c) r = 1500/√(1600 × 2500) = 0.75, so r² = 0.5625. 0.9375 × 0.6 = 0.5625. ✓ Both lines pass through (60, 55).",
            ],
        },
        {
            "title": "A full question from summary statistics",
            "question": "On 10 days a café recorded the maximum temperature x °C and the number y of cold drinks sold. Σx = 150, "
                        "Σy = 360, Σx² = 2700, Σy² = 14200, Σxy = 6000. (a) Find the regression line of y on x. (b) Find the "
                        "residual for the day with x = 20 and y = 38. (c) Find the RSS and the value of r, and show that "
                        "RSS = Syy(1 − r²).",
            "steps": [
                "(a) Sxx = 2700 − 150²/10 = 450, Sxy = 6000 − 150 × 360/10 = 600, Syy = 14200 − 360²/10 = 1240.",
                "b = 600/450 = 1.333, a = 36 − 1.333 × 15 = 16. Line: ŷ = 16 + 1.33x.",
                "(b) ŷ = 16 + (4/3) × 20 = 42.67, so the residual is 38 − 42.67 = −4.67: 4.67 fewer drinks sold than the line predicts.",
                "(c) RSS = 1240 − 600²/450 = 1240 − 800 = 440.",
                "r = 600/√(450 × 1240) = 0.803 (3 s.f.). Syy(1 − r²) = 1240 × (1 − 360000/558000) = 1240 − 800 = 440. ✓",
            ],
        },
    ],
    "practice": [
        "Data: (2, 3), (4, 5), (6, 8), (8, 9). Using Σx = 20, Σy = 25, Σx² = 120 and Σxy = 146, find the regression line of y on x.",
        "For 10 pairs, x̄ = 4, ȳ = 20, Sxx = 40 and Sxy = −80. Find the regression line of y on x.",
        "For a data set, r = 0.9, s<sub>x</sub> = 2 and s<sub>y</sub> = 5. Find the gradient of the regression line of y on x.",
        "Using the line from Question 1, find the residual for the point (4, 5).",
        "A regression line has r² = 0.64. Explain what this means.",
        "A regression of exam mark y on hours of revision x is fitted for x from 2 to 10 hours. Give two reasons why predicting "
        "the mark for 20 hours of revision may not be sensible.",
        "Data are coded by u = (x − 100)/10 and v = (y − 50)/2. The regression line of v on u is v = 2.5 + 0.8u. Find the "
        "regression line of y on x.",
        "(Edexcel FS2) For a data set, Sxx = 80, Syy = 250 and Sxy = 120. Find the RSS, find r², and check that RSS = Syy(1 − r²).",
        "The residuals from a regression line, in order of increasing x, are 1.2, 0.3, −0.6, −1.1, −0.7, 0.2, 1.4. Describe "
        "the pattern and explain what it suggests about the model.",
        "The cost £y of sending a parcel of mass x kg is modelled by ŷ = 4.20 + 0.35x for 0.5 ≤ x ≤ 10. Interpret the values "
        "4.20 and 0.35 in context.",
        "(OCR MEI) For a random sample, x̄ = 12, ȳ = 30, Syy = 200 and Sxy = 150. Find the regression line of x on y and use it "
        "to estimate x when y = 34.",
        "(a) Explain the difference between an explanatory variable and a response variable. (b) Explain why the regression line "
        "of x on y should not be used when the values of x were chosen by the experimenter.",
    ],
    "answers": [
        "x̄ = 5, ȳ = 6.25. Sxy = 146 − 20 × 25/4 = 21. Sxx = 120 − 20²/4 = 20. b = 21/20 = 1.05, a = 6.25 − 1.05 × 5 = 1. "
        "Line: ŷ = 1 + 1.05x.",
        "b = −80/40 = −2. a = 20 − (−2) × 4 = 28. Line: ŷ = 28 − 2x.",
        "b = r × s<sub>y</sub>/s<sub>x</sub> = 0.9 × 5/2 = 2.25.",
        "ŷ = 1 + 1.05 × 4 = 5.2. Residual = 5 − 5.2 = −0.2.",
        "64% of the variation in y is explained by the linear relationship with x; the other 36% is due to other factors or "
        "random variation.",
        "It is extrapolation far beyond the data (up to 10 hours), so there is no evidence the linear pattern continues; marks "
        "are capped at 100% and tiredness may give diminishing returns. The line might even predict an impossible mark.",
        "(y − 50)/2 = 2.5 + 0.8(x − 100)/10, so y = 50 + 5 + 0.16(x − 100) = 39 + 0.16x.",
        "RSS = 250 − 120²/80 = 250 − 180 = 70. r² = 120²/(80 × 250) = 0.72. Syy(1 − r²) = 250 × 0.28 = 70. ✓",
        "The residuals go from positive to negative and back to positive: a curved (U-shaped) pattern. A linear model is not "
        "suitable; the relationship appears to be curved.",
        "4.20: a fixed charge of about £4.20 per parcel (the cost predicted for a mass of 0 kg, only just outside the range). "
        "0.35: each extra kilogram adds about £0.35 to the cost.",
        "Gradient Sxy/Syy = 150/200 = 0.75. x − 12 = 0.75(y − 30), so x = −10.5 + 0.75y. When y = 34, x = 15.",
        "(a) The explanatory variable x is used to predict (it may be controlled); the response y is the variable being "
        "predicted, and it varies randomly. (b) If x is controlled it is not random, so there is no random variation in x to "
        "model; only the y on x line (minimising vertical distances) makes sense.",
    ],
    "exam": [
        "(Edexcel FS2 style) Eight students recorded the hours x they spent practising and their test score y. x: 4, 6, 8, 10, "
        "12, 14, 14, 16. y: 52, 60, 63, 71, 75, 82, 79, 88. Σx = 84, Σy = 570, Σx² = 1008, Σy² = 41648, Σxy = 6344. "
        "(a) Find Sxx, Syy and Sxy. [3] (b) Find the regression line of y on x. [3] (c) Interpret the gradient in context. [1] "
        "(d) Find the residual for the student with x = 14 and y = 79. [2] (e) Find the RSS. [2] (f) Estimate the score for "
        "9 hours of practice, and comment on its reliability. [2]",
        "(OCR A, Edexcel) The engine size x cc and fuel economy y mpg of 9 cars were coded as u = (x − 1500)/100 and v = y/10. "
        "The coded data give Σu = 18, Σv = 45, Σu² = 60 and Σuv = 72. (a) Find the regression line of v on u. [4] (b) Hence show "
        "that the regression line of y on x is y = 177.5 − 0.075x. [3] (c) Estimate the fuel economy of a car with engine size "
        "1800 cc. [1] (d) Use the line to estimate the fuel economy of a 3500 cc car, and explain why this value is not sensible. [2]",
        "(OCR MEI) For a random sample of 12 fathers and their adult sons, x is the father's height and y the son's height in cm. "
        "Σx = 2100, Σy = 2124, Sxx = 480, Syy = 520, Sxy = 330. (a) Explain why both regression lines may be used here. [1] "
        "(b) Find the regression line of y on x. [3] (c) Find the regression line of x on y. [3] (d) Estimate the height of a "
        "son whose father is 185 cm, and the height of a father whose son is 170 cm. [2] (e) Find r and comment on how far apart "
        "the two lines are. [2]",
        "(Edexcel FS2) For x = 1, 2, …, 7 the observed values of y are 2.0, 3.1, 4.4, 5.1, 9.0, 7.2, 8.1. Σy = 38.9, Σy² = 257.43, "
        "Σxy = 186.7. (a) Find the regression line of y on x. [3] (b) The residuals for x = 1, 3, 4, 6, 7 are −0.225, −0.046, "
        "−0.457, −0.579, −0.789. Find the other two residuals. [2] (c) Find the RSS using the formula. [2] (d) Identify a "
        "possible outlier and suggest what should be done. [2] (e) Without the outlier the line is ŷ = 1.11 + 1.01x with RSS "
        "0.0927. Use this to estimate y when x = 5, and comment. [2]",
    ],
    "exam_answers": [
        "(a) Sxx = 1008 − 84²/8 = 126 B1; Syy = 41648 − 570²/8 = 1035.5 B1; Sxy = 6344 − 84 × 570/8 = 359 B1. (b) b = 359/126 = "
        "2.849 M1 A1; a = 71.25 − 2.849 × 10.5 = 41.33; ŷ = 41.3 + 2.85x A1. (c) Each extra hour of practice is associated with "
        "about 2.85 more marks B1. (d) ŷ = 41.33 + 2.849 × 14 = 81.22 M1; residual = 79 − 81.22 = −2.22 A1. (e) RSS = 1035.5 − "
        "359²/126 M1 = 12.6 (3 s.f.) A1. (f) ŷ = 41.33 + 2.849 × 9 = 67.0 B1; interpolation with r = 0.994, so reliable B1.",
        "(a) Suu = 60 − 18²/9 = 24, Suv = 72 − 18 × 45/9 = −18 M1 A1. Gradient −18/24 = −0.75; ū = 2, v̄ = 5, intercept "
        "5 − (−0.75)(2) = 6.5 M1; v = 6.5 − 0.75u A1. (b) y/10 = 6.5 − 0.75(x − 1500)/100 M1; y = 65 − 0.075(x − 1500) M1 "
        "= 177.5 − 0.075x A1 (shown). (c) y = 177.5 − 135 = 42.5 mpg B1. (d) y = 177.5 − 262.5 = −85 mpg B1: impossible, because "
        "3500 cc is far outside the data (x̄ = 1700) and the linear model cannot continue indefinitely (extrapolation) B1.",
        "(a) Both heights are random variables (neither is controlled) B1. (b) x̄ = 175, ȳ = 177 B1; b = 330/480 = 0.6875 M1; "
        "y − 177 = 0.6875(x − 175), y = 56.7 + 0.688x A1. (c) b′ = 330/520 = 0.6346 M1; x − 175 = 0.6346(y − 177) M1; "
        "x = 62.7 + 0.635y A1. (d) Son: y = 56.69 + 0.6875 × 185 = 184 cm B1. Father: x = 62.67 + 0.6346 × 170 = 171 cm B1. "
        "(e) r = 330/√(480 × 520) = 0.661 B1; only moderate correlation, so the two lines are quite different (they meet at "
        "(175, 177)) B1.",
        "(a) Sxx = 140 − 28²/7 = 28, Sxy = 186.7 − 28 × 38.9/7 = 31.1 M1; b = 31.1/28 = 1.111, a = 5.557 − 1.111 × 4 = 1.114 A1; "
        "ŷ = 1.11 + 1.11x A1. (b) x = 2: 3.1 − 3.336 = −0.236 B1; x = 5: 9.0 − 6.668 = 2.332 B1. (c) Syy = 257.43 − 38.9²/7 = "
        "41.257; RSS = 41.257 − 31.1²/28 M1 = 6.71 (3 s.f.) A1. (d) (5, 9.0): its residual is much larger than the others and all "
        "the rest are negative B1. Check it for an error; if it is a mistake, remove it and refit the line B1. (e) ŷ = 1.114 + "
        "1.009 × 5 = 6.16 B1. The RSS falls from 6.71 to 0.0927, so without the outlier the linear model fits very well; 6.16 is "
        "a more reliable estimate than the observed 9.0 if that value was an error B1.",
    ],
}
