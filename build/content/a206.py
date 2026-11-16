"""Unit A2.6: Linear combinations of random variables (expands the checked draft u05)."""

UNIT = {
    "number": "A2.6",
    "title": "Linear combinations of random variables",
    "tag": "A level · Edexcel FS2 4.1 (and FS1 2.1 Poisson sums), IAL S3 1.1, AQA SD8 (AS and A level), OCR A 5.04, "
           "OCR MEI SR6, SR27, SR29 · prior knowledge for CAIE 9231 Paper 4",
    "notes": [
        ("p", "Many real quantities are built from several random parts: the total mass of a box of chocolates, the time to "
              "complete two tasks, the difference between two people's scores. This unit gives the mean and variance of "
              "any linear combination of independent random variables, and the key fact that combinations of independent "
              "normal variables are themselves normal. These results also underpin the distribution of the sample mean."),

        ("h2", "6.1 Recap: a single variable, aX + b"),
        ("box", "Coding a single variable", [
            "E(aX + b) = aE(X) + b.",
            "Var(aX + b) = a²Var(X). Adding a constant shifts the distribution but does not change its spread; "
            "multiplying by a multiplies the standard deviation by |a|.",
            "If X ~ N(μ, σ²) then aX + b ~ N(aμ + b, a²σ²) (OCR A 5.04b).",
        ]),

        ("h2", "6.2 Sums and differences of independent variables (AQA SD8, OCR A 5.04a, OCR MEI SR6)"),
        ("box", "Expectation and variance of a linear combination", [
            "E(aX + bY + c) = aE(X) + bE(Y) + c, for <b>any</b> X and Y (independence is not needed).",
            "If X and Y are <b>independent</b>: Var(aX + bY + c) = a²Var(X) + b²Var(Y).",
            "In particular E(X ± Y) = E(X) ± E(Y) and Var(X ± Y) = Var(X) + Var(Y). Variances add even when you subtract, "
            "because Var(−Y) = (−1)²Var(Y).",
            "These extend to any number of independent variables: Var(a₁X₁ + … + aₙXₙ) = a₁²Var(X₁) + … + aₙ²Var(Xₙ).",
        ]),
        ("p", "Why the variance result needs independence: Var(X + Y) = E[(X + Y)²] − [E(X + Y)]² expands to "
              "Var(X) + Var(Y) + 2[E(XY) − E(X)E(Y)]. For independent X and Y, E(XY) = E(X)E(Y) (a result printed in the "
              "Edexcel and IAL formula booklets), so the last bracket is zero. If X and Y are not independent, the "
              "variance formula can fail badly: for example Var(X + X) = 4Var(X), not 2Var(X). Proofs are not required by "
              "any board, but this explains when the result can be used."),
        ("p", "These results hold for discrete and continuous variables alike, so you can combine, say, a binomial count "
              "with a continuous uniform time. The mean and variance of the combination are found exactly, but its "
              "<i>distribution</i> may be awkward unless the parts are normal (or Poisson, for sums)."),

        ("h2", "6.3 2X is not the same as X₁ + X₂"),
        ("p", "2X means one observation of X, doubled. X₁ + X₂ means two <b>independent</b> observations of X, added. They have "
              "the same mean, 2μ, but different variances:"),
        ("table", ["Combination", "Meaning", "Mean", "Variance"], [
            ["2X", "one value, doubled (e.g. twice the mass of one bag)", "2μ", "4σ²"],
            ["X₁ + X₂", "two independent values (e.g. the mass of two bags)", "2μ", "2σ²"],
            ["nX", "one value, multiplied by n", "nμ", "n²σ²"],
            ["X₁ + X₂ + … + Xₙ", "total of n independent values", "nμ", "nσ²"],
            ["X̄ = (X₁ + … + Xₙ)/n", "mean of a random sample of n", "μ", "σ²/n"],
            ["X − Y", "difference of independent values", "μ<sub>X</sub> − μ<sub>Y</sub>", "σ<sub>X</sub>² + σ<sub>Y</sub>²"],
        ]),
        ("p", "A total of independent values is <b>less</b> variable than a single value scaled up, because high and low "
              "values tend to balance out. The same idea gives Var(X̄) = σ²/n, the basis of all sampling theory in A2.7."),

        ("h2", "6.4 Linear combinations of independent normal variables"),
        ("box", "Normal combinations (Edexcel FS2 4.1, IAL S3 1.1, OCR A 5.04b, OCR MEI SR29)", [
            "If X ~ N(μ<sub>X</sub>, σ<sub>X</sub>²) and Y ~ N(μ<sub>Y</sub>, σ<sub>Y</sub>²) are independent, then aX ± bY ~ N(aμ<sub>X</sub> ± bμ<sub>Y</sub>, a²σ<sub>X</sub>² + b²σ<sub>Y</sub>²).",
            "The same holds for any number of independent normal variables: every linear combination is normal.",
            "If X₁, …, Xₙ are independent N(μ, σ²): ΣXᵢ ~ N(nμ, nσ²) and X̄ ~ N(μ, σ²/n).",
            "This result is not in the IAL or Edexcel formula booklets: learn it. No proof is required.",
        ]),
        ("p", "To answer a comparison question such as \"find the probability that X is greater than Y\", rewrite it with "
              "everything on one side: P(X > Y) = P(X − Y > 0). Find the distribution of X − Y, then standardise. "
              "Similarly P(X > 2Y) = P(X − 2Y > 0), and P(|X − Y| < 3) = P(−3 < X − Y < 3)."),

        ("h2", "6.5 Sums of Poisson (and binomial) variables"),
        ("bullets", [
            "If X ~ Po(λ) and Y ~ Po(μ) are independent, then X + Y ~ Po(λ + μ) (Edexcel FS1 2.1, AQA SB4, OCR MEI SR15).",
            "The difference X − Y is <b>not</b> Poisson: it can be negative, and its variance λ + μ is not equal to its mean λ − μ.",
            "2X is <b>not</b> Poisson either: its mean is 2λ but its variance is 4λ, and it takes only even values. "
            "X₁ + X₂ ~ Po(2λ), however, is Poisson.",
            "If X ~ B(m, p) and Y ~ B(n, p) are independent with the <b>same</b> p, then X + Y ~ B(m + n, p).",
            "The general rules for E and Var in 6.2 still apply to every combination, Poisson or not.",
        ]),

        ("h2", "6.6 Method for applied questions"),
        ("box", "Steps", [
            "1. Define the random variables, with their distributions, and state that they are independent.",
            "2. Write the event in terms of one linear combination, e.g. P(A₁ + A₂ + A₃ > 2B) = P(A₁ + A₂ + A₃ − 2B > 0).",
            "3. Find its mean and variance using 6.2, taking care over 2X versus X₁ + X₂.",
            "4. State its distribution (normal if all parts are normal), standardise and find the probability.",
        ]),
        ("warn", "Common mistakes", [
            "Subtracting variances: Var(X − Y) = Var(X) + Var(Y), never Var(X) − Var(Y).",
            "Using Var(3X) = 3Var(X) (it is 9Var(X)) or, worse, writing 3σ instead of √3σ for the standard deviation of a total of 3 values.",
            "Treating the total of n values as nX: the total of 5 bags has variance 5σ², not 25σ².",
            "Forgetting to square the coefficient when it is negative: Var(2X − 3Y) = 4Var(X) + 9Var(Y).",
            "Standardising with the variance instead of the standard deviation.",
            "Applying Var(X + Y) = Var(X) + Var(Y) without stating (or checking) that X and Y are independent.",
            "Saying X − Y is Poisson when X and Y are Poisson.",
        ]),
    ],
    "examples": [
        {
            "title": "Mean and variance of a combination of discrete variables",
            "question": "X ~ B(10, 0.4) and Y ~ Po(3) are independent. Find E(3X − 2Y + 1) and Var(3X − 2Y + 1).",
            "steps": [
                "E(X) = 10 × 0.4 = 4 and Var(X) = 10 × 0.4 × 0.6 = 2.4. E(Y) = Var(Y) = 3.",
                "E(3X − 2Y + 1) = 3 × 4 − 2 × 3 + 1 = 7.",
                "Var(3X − 2Y + 1) = 3² × 2.4 + (−2)² × 3 = 21.6 + 12 = 33.6. The constant 1 does not affect the variance.",
            ],
        },
        {
            "title": "2X compared with X₁ + X₂",
            "question": "The mass of a bag of sugar is X ~ N(500, 15²) grams. Find (a) the probability that twice the mass of one "
                        "bag exceeds 1030 g, (b) the probability that the total mass of two randomly chosen bags exceeds 1030 g.",
            "steps": [
                "(a) 2X ~ N(1000, 4 × 225) = N(1000, 30²). P(2X > 1030) = 1 − Φ(30/30) = 1 − Φ(1) = 0.159 (3 s.f.).",
                "(b) X₁ + X₂ ~ N(1000, 2 × 225) = N(1000, 450). P(X₁ + X₂ > 1030) = 1 − Φ(30/√450) = 1 − Φ(1.414) = 0.0786 (3 s.f.).",
                "The total of two independent bags is less variable than double one bag, so the probability is smaller.",
            ],
        },
        {
            "title": "Probability that one variable exceeds another",
            "question": "X ~ N(12, 4) and Y ~ N(10, 9) are independent. Find P(X > Y).",
            "steps": [
                "Let D = X − Y. E(D) = 12 − 10 = 2 and Var(D) = 4 + 9 = 13, so D ~ N(2, 13).",
                "P(X > Y) = P(D > 0) = 1 − Φ((0 − 2)/√13) = Φ(0.555) = 0.710 (3 s.f.; the exact value is 0.71045).",
            ],
        },
        {
            "title": "A total against a limit",
            "question": "The masses of adults are N(75, 12²) kg. A lift carries 10 adults chosen at random and has a safe load of 800 kg. "
                        "Find the probability that the safe load is exceeded. State an assumption you have made.",
            "steps": [
                "Let T = X₁ + … + X₁₀, with the Xᵢ independent N(75, 144).",
                "E(T) = 10 × 75 = 750 and Var(T) = 10 × 144 = 1440, so T ~ N(750, 1440).",
                "P(T > 800) = 1 − Φ(50/√1440) = 1 − Φ(1.318) = 0.0938 (3 s.f.).",
                "Assumption: the masses of the 10 adults are independent (e.g. they are not members of one family or one sports team).",
            ],
        },
        {
            "title": "Several variables with different coefficients",
            "question": "Apples have masses A ~ N(150, 20²) g and oranges B ~ N(180, 25²) g, all independent. Find the probability that "
                        "4 randomly chosen apples weigh more than 3 times the mass of a randomly chosen orange.",
            "steps": [
                "We need P(A₁ + A₂ + A₃ + A₄ > 3B) = P(D > 0), where D = A₁ + A₂ + A₃ + A₄ − 3B.",
                "E(D) = 4 × 150 − 3 × 180 = 600 − 540 = 60.",
                "Var(D) = 4 × 20² + 3² × 25² = 1600 + 5625 = 7225, so the standard deviation is 85. Note 3B uses 3², not 3.",
                "P(D > 0) = 1 − Φ(−60/85) = Φ(0.706) = 0.760 (3 s.f.).",
            ],
        },
        {
            "title": "Combining Poisson variables",
            "question": "Calls to desk A arrive as Po(3) per hour and to desk B as Po(2) per hour, independently. (a) Find the probability "
                        "that the two desks receive at least 8 calls in total in an hour. (b) Find E(X − Y) and Var(X − Y), where X "
                        "and Y are the numbers of calls in an hour at A and B, and explain why X − Y is not Poisson.",
            "steps": [
                "(a) X + Y ~ Po(3 + 2) = Po(5). P(X + Y ≥ 8) = 1 − P(X + Y ≤ 7) = 1 − 0.8666 = 0.1334.",
                "(b) E(X − Y) = 3 − 2 = 1 and Var(X − Y) = 3 + 2 = 5.",
                "X − Y can take negative values and its variance (5) is not equal to its mean (1), so it cannot be Poisson.",
            ],
        },
    ],
    "practice": [
        "X and Y are independent with E(X) = 5, Var(X) = 2, E(Y) = 3 and Var(Y) = 4. Find E(2X − 3Y + 4) and Var(2X − 3Y + 4).",
        "The masses of bags of flour are independent, each with mean 2 kg and standard deviation 0.1 kg, and are normally distributed. Find the probability that three bags together weigh more than 6.2 kg.",
        "X ~ N(30, 16) and Y ~ N(25, 9) are independent. Find P(X < Y).",
        "X ~ N(1, 1) and Y ~ N(2, 1) are independent. Let T = 2X + 3Y. Find the distribution of T and P(T < 5).",
        "Show that if X and Y are independent with Var(X) = σ<sub>X</sub>² and Var(Y) = σ<sub>Y</sub>², then Var(X − Y) = σ<sub>X</sub>² + σ<sub>Y</sub>².",
        "X ~ Po(4). Find the mean and variance of (a) 2X, (b) X₁ + X₂, where X₁ and X₂ are independent observations of X. Which of these has a Poisson distribution? Explain.",
        "X ~ N(40, 36). Find the distribution of the mean X̄ of a random sample of 9 observations, and P(X̄ > 42).",
        "X ~ N(50, 36) and Y ~ N(20, 4) are independent. Find P(X > 2Y).",
        "S is the total score on three fair dice and T is three times the score on one fair die. Find E(S), Var(S), E(T) and Var(T). (One die has mean 3.5 and variance 35/12.)",
        "Emails arrive from company A at a mean rate of 2.5 per day and from company B at 1.5 per day, independently and at random. Find the probability that (a) exactly 3 emails arrive in total on one day, (b) at most 5 arrive in total over 2 days.",
        "Cups have capacity C ~ N(250, 4²) ml. A machine pours V ~ N(240, σ²) ml into each cup, independently. Find the largest value of σ for which the probability that a cup overflows is at most 0.01.",
        "X and Y are independent with Var(X) = 3 and Var(Y) = 5. Find Var(4 − 2X + Y). Explain why E(X + Y) = E(X) + E(Y) does not require independence, but the corresponding result for variances does.",
    ],
    "answers": [
        "E = 2 × 5 − 3 × 3 + 4 = 5. Var = 4 × 2 + 9 × 4 = 44.",
        "Total T ~ N(6, 3 × 0.01) = N(6, 0.03). P(T > 6.2) = 1 − Φ(0.2/√0.03) = 1 − Φ(1.155) = 0.124 (3 s.f.).",
        "X − Y ~ N(5, 25). P(X < Y) = P(X − Y < 0) = Φ(−5/5) = Φ(−1) = 0.159 (3 s.f.).",
        "T ~ N(2 + 6, 4 + 9) = N(8, 13). P(T < 5) = Φ(−3/√13) = Φ(−0.832) = 0.203 (3 s.f.).",
        "Var(X − Y) = Var(X + (−1)Y) = Var(X) + (−1)²Var(Y) = σ<sub>X</sub>² + σ<sub>Y</sub>², using the independence result Var(aX + bY) = a²Var(X) + b²Var(Y) with a = 1, b = −1.",
        "(a) E(2X) = 8, Var(2X) = 16. (b) E = 8, Var = 8. X₁ + X₂ ~ Po(8) by the additive property. 2X is not Poisson: its variance (16) is not equal to its mean (8), and it only takes even values.",
        "X̄ ~ N(40, 36/9) = N(40, 4). P(X̄ > 42) = 1 − Φ(1) = 0.159 (3 s.f.).",
        "X − 2Y ~ N(50 − 40, 36 + 4 × 4) = N(10, 52). P(X − 2Y > 0) = Φ(10/√52) = Φ(1.387) = 0.917 (3 s.f.).",
        "E(S) = 10.5, Var(S) = 3 × 35/12 = 8.75. E(T) = 10.5, Var(T) = 9 × 35/12 = 26.25.",
        "(a) Total per day ~ Po(4): P(= 3) = e⁻⁴4³/3! = 0.1954. (b) Total over 2 days ~ Po(8): P(≤ 5) = 0.1912.",
        "Overflow if V > C. D = C − V ~ N(10, 16 + σ²). Need P(D < 0) ≤ 0.01: 10/√(16 + σ²) ≥ 2.3263, so 16 + σ² ≤ 18.48, σ² ≤ 2.48 and σ ≤ 1.57 ml (3 s.f.).",
        "Var(4 − 2X + Y) = 4 × 3 + 5 = 17. Expectation is linear for any variables, because E(X + Y) = Σ(x + y)P(x, y) splits into two sums. Var(X + Y) contains the extra term 2[E(XY) − E(X)E(Y)], which is zero only when X and Y are independent (more precisely, uncorrelated).",
    ],
    "exam": [
        "The masses of chocolates are N(20, 1.2²) grams and the masses of empty boxes are N(40, 3²) grams. A full box holds 24 chocolates. All masses are independent. (Edexcel FS2, IAL S3)\n"
        "(a) Find the distribution of the total mass T of a full box. [3]\n"
        "(b) Find P(T < 510). [2]\n"
        "(c) Find the mass m such that 95% of full boxes weigh more than m grams. [2]\n"
        "(d) Two full boxes are chosen at random. Find the probability that their masses differ by more than 5 g. [4]",
        "X ~ B(12, 0.25) and T has a continuous uniform distribution on [0, 6], with X and T independent. (AQA, OCR A)\n"
        "(a) Write down E(X), Var(X), E(T) and Var(T). [3]\n"
        "(b) Find E(X + 2T) and Var(X + 2T). [3]\n"
        "(c) A student says that Var(X − T) = Var(X) − Var(T). Explain the error and give the correct value. [2]\n"
        "(d) Explain why the result in (b) cannot be used if T is replaced by a variable that depends on X. [1]",
        "The time A minutes for a technician to complete task A is N(30, 2²) and the time B minutes for task B is N(48, 3²), independently. (Edexcel FS2, IAL S3)\n"
        "(a) Find the probability that the two tasks together take more than 85 minutes. [3]\n"
        "(b) Find the probability that task B takes more than 1.5 times as long as task A. [4]\n"
        "(c) Task A is carried out on 5 separate days. Find the probability that the mean time for these 5 is more than 31 minutes. [3]\n"
        "(d) Explain why the variance of the total time for the 5 task-A jobs is not 25 × 2². [1]",
        "Rods have lengths R ~ N(100, 0.5²) mm. Holes have diameters H ~ N(100.8, 0.3²) mm. A rod fits a hole if R < H. All values are independent. (OCR A, OCR MEI)\n"
        "(a) Find the probability that a randomly chosen rod fits a randomly chosen hole. [3]\n"
        "(b) A good fit needs 0 < H − R < 1.5. Find the probability of a good fit. [2]\n"
        "(c) Three rods are placed end to end in a slot of length G ~ N(301, 1) mm. Find the probability that they fit. [3]\n"
        "(d) Ten rods are each paired with a randomly chosen hole. Find the probability that at least 9 of the rods fit their holes. [3]",
    ],
    "exam_answers": [
        "(a) E(T) = 40 + 24 × 20 = 520 [B1]; Var(T) = 3² + 24 × 1.2² = 9 + 34.56 = 43.56 [M1]; T ~ N(520, 6.6²) [A1].\n"
        "(b) P(T < 510) = Φ(−10/6.6) = Φ(−1.515) [M1] = 0.0649 (3 s.f.) [A1].\n"
        "(c) m = 520 − 1.6449 × 6.6 [M1] = 509 g (3 s.f.) [A1].\n"
        "(d) D = T₁ − T₂ ~ N(0, 2 × 43.56) = N(0, 87.12) [M1 A1]. P(|D| > 5) = 2[1 − Φ(5/√87.12)] = 2[1 − Φ(0.536)] [M1] = 0.592 (3 s.f.) [A1].",
        "(a) E(X) = 3, Var(X) = 12 × 0.25 × 0.75 = 2.25 [B1]; E(T) = 3 [B1]; Var(T) = 6²/12 = 3 [B1].\n"
        "(b) E(X + 2T) = 3 + 6 = 9 [B1]. Var(X + 2T) = 2.25 + 2² × 3 [M1] = 14.25 [A1].\n"
        "(c) Variances add for a difference of independent variables, since Var(−T) = (−1)²Var(T) [B1]: Var(X − T) = 2.25 + 3 = 5.25 [B1].\n"
        "(d) Var(X + 2T) = Var(X) + 4Var(T) needs X and T to be independent [B1].",
        "(a) A + B ~ N(78, 4 + 9) = N(78, 13) [M1 A1]. P(A + B > 85) = 1 − Φ(7/√13) = 1 − Φ(1.941) = 0.0261 (3 s.f.) [A1].\n"
        "(b) P(B > 1.5A) = P(B − 1.5A > 0) [M1]. B − 1.5A ~ N(48 − 45, 9 + 1.5² × 4) = N(3, 18) [M1 A1]. P = Φ(3/√18) = Φ(0.707) = 0.760 (3 s.f.) [A1].\n"
        "(c) Ā ~ N(30, 4/5) [M1 A1]. P(Ā > 31) = 1 − Φ(1/√0.8) = 1 − Φ(1.118) = 0.132 (3 s.f.) [A1].\n"
        "(d) The five times are independent observations A₁ + … + A₅, with variance 5 × 2² = 20; 25 × 2² would be Var(5A), five times one single job's time [B1].",
        "(a) D = H − R ~ N(0.8, 0.3² + 0.5²) = N(0.8, 0.34) [M1 A1]. P(D > 0) = Φ(0.8/√0.34) = Φ(1.372) = 0.915 (3 s.f.) [A1].\n"
        "(b) P(0 < D < 1.5) = Φ(0.7/0.5831) − Φ(−0.8/0.5831) = Φ(1.200) − Φ(−1.372) [M1] = 0.800 (3 s.f.) [A1].\n"
        "(c) S = R₁ + R₂ + R₃ ~ N(300, 0.75) [B1]; G − S ~ N(1, 1.75) [M1]; P(G − S > 0) = Φ(1/√1.75) = Φ(0.756) = 0.775 (3 s.f.) [A1].\n"
        "(d) Number that fit ~ B(10, 0.915) [M1]. P(≥ 9) = 0.915¹⁰ + 10 × 0.915⁹ × 0.085 [M1] = 0.793 (3 s.f.) [A1].",
    ],
}
