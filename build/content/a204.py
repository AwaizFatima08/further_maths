"""Unit A2.4: Probability generating functions (Edexcel FS1 topic 7, CAIE 9231 4.5). Expands the checked draft u03."""

UNIT = {
    "number": "A2.4",
    "title": "Probability generating functions",
    "tag": "A level · Edexcel FS1 topic 7 (7.1–7.3), CAIE 9231 Paper 4 topic 4.5 · not on AQA, OCR A, OCR MEI or IAL",
    "notes": [
        ("p", "A probability generating function (PGF) stores a whole discrete distribution in a single function. Once you "
              "have it, the mean and variance come from two derivatives, and the distribution of a sum of independent "
              "variables comes from a single multiplication. PGFs are used for variables that take values 0, 1, 2, … only."),

        ("h2", "4.1 Definition and basic properties"),
        ("box", "Definition", [
            "If X takes non-negative integer values, its PGF is G<sub>X</sub>(t) = E(tˣ) = Σ P(X = x) tˣ.",
            "So G<sub>X</sub>(t) = P(X = 0) + P(X = 1)t + P(X = 2)t² + … : the coefficient of tʳ is P(X = r).",
            "G<sub>X</sub>(1) = Σ P(X = x) = 1 for every PGF. G<sub>X</sub>(0) = P(X = 0).",
        ]),
        ("p", "You can go both ways. From a table of probabilities, write each probability as the coefficient of the "
              "matching power of t. From a PGF, expand it as a power series in t (using the binomial expansion, the "
              "exponential series or a geometric series) and read off the coefficients. Equivalently, "
              "P(X = r) = G⁽ʳ⁾(0)/r!, where G⁽ʳ⁾ is the rth derivative; this is useful for small r."),
        ("p", "If a PGF contains an unknown constant k, use G(1) = 1 to find it. In a \"show that\" question you must write "
              "this step out explicitly: examiners report that many candidates lose marks by omitting it."),

        ("h2", "4.2 Mean and variance from the PGF (proof required: Edexcel 7.2)"),
        ("p", "Differentiate G(t) = Σ P(X = x)tˣ term by term: G′(t) = Σ x P(X = x) t^(x−1) and "
              "G″(t) = Σ x(x − 1) P(X = x) t^(x−2). Now put t = 1, so every power of t becomes 1:"),
        ("box", "Mean and variance", [
            "G′(1) = Σ x P(X = x) = E(X).",
            "G″(1) = Σ x(x − 1) P(X = x) = E[X(X − 1)] = E(X²) − E(X).",
            "So E(X²) = G″(1) + G′(1), and Var(X) = E(X²) − [E(X)]² = G″(1) + G′(1) − [G′(1)]².",
        ]),
        ("p", "This proof is short and is in both specifications' formula lists, but Edexcel may ask you to prove it. Note "
              "that G″(1) is <b>not</b> E(X²)."),

        ("h2", "4.3 PGFs of the standard distributions, with derivations"),
        ("p", "Edexcel lists binomial, Poisson, geometric and negative binomial; CAIE lists discrete uniform, binomial, "
              "geometric and Poisson. Derivations of these PGFs, and of the means and variances from them, can be asked for. "
              "Throughout, q = 1 − p."),
        ("bullets", [
            "<b>Discrete uniform on {1, 2, …, n}</b> (CAIE): G(t) = (t + t² + … + tⁿ)/n = t(1 − tⁿ)/(n(1 − t)) for t ≠ 1. "
            "Use the polynomial form to differentiate: G′(1) = (1 + 2 + … + n)/n = (n + 1)/2 and "
            "G″(1) = Σ x(x − 1)/n = (n − 1)(n + 1)/3, giving Var(X) = (n² − 1)/12.",
            "<b>Binomial B(n, p)</b>: G(t) = Σ C(n, x)(pt)ˣ q^(n−x) = (q + pt)ⁿ by the binomial theorem. Then "
            "G′(t) = np(q + pt)^(n−1), G″(t) = n(n − 1)p²(q + pt)^(n−2), so G′(1) = np, G″(1) = n(n − 1)p² and "
            "Var(X) = n(n − 1)p² + np − n²p² = np(1 − p).",
            "<b>Poisson Po(λ)</b>: G(t) = Σ e^(−λ)(λt)ˣ/x! = e^(−λ)e^(λt) = e^(λ(t − 1)), using the exponential series. "
            "G′(t) = λe^(λ(t − 1)) and G″(t) = λ²e^(λ(t − 1)), so E(X) = λ and Var(X) = λ² + λ − λ² = λ.",
            "<b>Geometric Geo(p)</b>, X = number of trials up to and including the first success, x = 1, 2, …: "
            "G(t) = Σ p q^(x−1) tˣ = pt Σ (qt)^(x−1) = pt/(1 − qt), a geometric series valid for |t| < 1/q. "
            "G′(t) = p/(1 − qt)², G″(t) = 2pq/(1 − qt)³, so G′(1) = 1/p, G″(1) = 2q/p² and Var(X) = 2q/p² + 1/p − 1/p² = q/p².",
            "<b>Negative binomial</b> (Edexcel), X = number of trials up to and including the rth success, x = r, r + 1, …: "
            "X is the sum of r independent Geo(p) variables (the waits for each success), so by 4.4 "
            "G(t) = [pt/(1 − qt)]ʳ. Then E(X) = r/p and Var(X) = rq/p².",
        ]),
        ("table", ["Distribution", "P(X = x)", "PGF G(t)", "E(X)", "Var(X)"], [
            ["Discrete uniform {1, …, n}", "1/n, x = 1, …, n", "(t + t² + … + tⁿ)/n", "(n + 1)/2", "(n² − 1)/12"],
            ["Binomial B(n, p)", "C(n, x)pˣq^(n−x), x = 0, …, n", "(q + pt)ⁿ", "np", "npq"],
            ["Poisson Po(λ)", "e^(−λ)λˣ/x!, x = 0, 1, …", "e^(λ(t − 1))", "λ", "λ"],
            ["Geometric Geo(p)", "p q^(x−1), x = 1, 2, …", "pt/(1 − qt)", "1/p", "q/p²"],
            ["Negative binomial (Edexcel)", "C(x − 1, r − 1)pʳq^(x−r), x = r, r + 1, …", "[pt/(1 − qt)]ʳ", "r/p", "rq/p²"],
        ]),

        ("h2", "4.4 Sums of independent random variables"),
        ("box", "The convolution theorem", [
            "If X and Y are independent, G<sub>X+Y</sub>(t) = G<sub>X</sub>(t) × G<sub>Y</sub>(t).",
            "Reason: G<sub>X+Y</sub>(t) = E(t^(X+Y)) = E(tˣ tʸ) = E(tˣ)E(tʸ) = G<sub>X</sub>(t)G<sub>Y</sub>(t), since tˣ and tʸ are independent. "
            "(Edexcel: derivation not required.)",
            "For n independent variables, multiply all n PGFs. If X₁, …, Xₙ are independent with the same PGF G(t), "
            "the total has PGF [G(t)]ⁿ.",
        ]),
        ("p", "A PGF determines its distribution uniquely. So if the product is the PGF of a standard distribution, the sum "
              "has that distribution. For example e^(λ(t−1))e^(μ(t−1)) = e^((λ+μ)(t−1)) shows that the sum of independent "
              "Po(λ) and Po(μ) variables is Po(λ + μ); (q + pt)ᵐ(q + pt)ⁿ = (q + pt)^(m+n) shows that B(m, p) + B(n, p) is "
              "B(m + n, p) when p is the same. The mean of a sum is the sum of the means, so you can check G′(1)."),

        ("h2", "4.5 The PGF of Y = aX + b (Edexcel)"),
        ("box", "Linear transformation", [
            "If Y = aX + b, where a and b are non-negative integers, then G<sub>Y</sub>(t) = E(t^(aX+b)) = t^b E((tᵃ)ˣ) = t^b G<sub>X</sub>(tᵃ).",
            "Example: X ~ B(5, 0.2) and Y = 2X + 3 give G<sub>Y</sub>(t) = t³(0.8 + 0.2t²)⁵.",
            "Differentiating G<sub>Y</sub> gives E(Y) = aE(X) + b and Var(Y) = a²Var(X), as expected.",
        ]),
        ("p", "A factor tᵏ in a PGF therefore shifts the distribution k places to the right. For instance t²(1 + t)³/8 is the "
              "PGF of 2 + W, where W ~ B(3, ½)."),

        ("h2", "4.6 Finding probabilities by expanding"),
        ("bullets", [
            "Binomial-type PGFs: expand with the binomial theorem; (1/3 + 2t/3)⁴ has coefficient of t² equal to C(4, 2)(2/3)²(1/3)² = 8/27.",
            "Geometric-type PGFs: 1/(4 − 3t) = ¼ × 1/(1 − ¾t) = ¼ Σ (¾t)ʳ, so P(X = r) = ¼(¾)ʳ for r = 0, 1, 2, … .",
            "Products: collect only the terms that give the power you need. The coefficient of t in (0.3 + 0.7t)³e^(t − 1) "
            "comes from (constant × t-term) + (t-term × constant).",
            "To find P(X ≤ k), add the coefficients of t⁰ to tᵏ; to find P(X ≥ k), use 1 minus the sum of the others.",
        ]),
        ("warn", "Common mistakes", [
            "Adding PGFs instead of multiplying them for a sum of independent variables (frequently reported by examiners).",
            "Using G″(1) as E(X²), or writing Var(X) = G″(1) − [G′(1)]² without the + G′(1).",
            "Not showing G(1) = 1 when asked to show a value of k, or forgetting that G(0) = P(X = 0).",
            "Mixing up the two geometric forms: Geo(p) counts trials (starts at 1, PGF pt/(1 − qt)); a variable starting at 0 has PGF p/(1 − qt).",
            "Confusing the mean with the mode when asked for the \"most likely value\": the mode comes from the largest coefficient.",
            "Differentiating t(1 − tⁿ)/(n(1 − t)) and substituting t = 1, which gives 0/0. Use the polynomial form instead.",
        ]),
    ],
    "examples": [
        {
            "title": "Mean and variance from a PGF",
            "question": "A random variable X has PGF G(t) = 0.1t + 0.2t² + 0.3t³ + 0.4t⁴. Find E(X) and Var(X).",
            "steps": [
                "Check: G(1) = 0.1 + 0.2 + 0.3 + 0.4 = 1.",
                "G′(t) = 0.1 + 0.4t + 0.9t² + 1.6t³, so E(X) = G′(1) = 3.",
                "G″(t) = 0.4 + 1.8t + 4.8t², so G″(1) = 7.",
                "Var(X) = G″(1) + G′(1) − [G′(1)]² = 7 + 3 − 9 = 1.",
            ],
        },
        {
            "title": "Finding k and identifying the distribution",
            "question": "The PGF of X is G(t) = k(1 + 2t)⁴. (a) Show that k = 1/81. (b) Find P(X = 2). "
                        "(c) Identify the distribution of X and write down E(X) and Var(X).",
            "steps": [
                "(a) G(1) = 1, so k × 3⁴ = 1 and k = 1/81.",
                "(b) The coefficient of t² in (1 + 2t)⁴ is C(4, 2) × 2² = 24, so P(X = 2) = 24/81 = 8/27 = 0.296 (3 s.f.).",
                "(c) G(t) = ((1 + 2t)/3)⁴ = (1/3 + (2/3)t)⁴, which is the PGF of B(4, 2/3).",
                "So E(X) = 4 × 2/3 = 8/3 and Var(X) = 4 × 2/3 × 1/3 = 8/9.",
            ],
        },
        {
            "title": "Deriving the geometric PGF, mean and variance",
            "question": "X ~ Geo(p), with P(X = x) = p(1 − p)^(x−1) for x = 1, 2, … . Show that G(t) = pt/(1 − qt), where q = 1 − p, "
                        "and use it to prove that E(X) = 1/p and Var(X) = q/p².",
            "steps": [
                "G(t) = Σ p q^(x−1) tˣ = pt(1 + qt + (qt)² + …). This is a geometric series with ratio qt, so for |qt| < 1 its sum is pt/(1 − qt).",
                "Quotient rule: G′(t) = [p(1 − qt) + pqt]/(1 − qt)² = p/(1 − qt)². So E(X) = G′(1) = p/(1 − q)² = p/p² = 1/p.",
                "G″(t) = 2pq/(1 − qt)³, so G″(1) = 2pq/p³ = 2q/p².",
                "Var(X) = 2q/p² + 1/p − 1/p² = (2q + p − 1)/p² = (2q − q)/p² = q/p², using p − 1 = −q.",
            ],
        },
        {
            "title": "PGF of a sum, and probabilities from a product",
            "question": "X ~ B(3, 0.7) and Y ~ Po(1) are independent, and T = X + Y. (a) Find the PGF of T. (b) Find P(T = 0) and "
                        "P(T = 1), giving your answers to 4 decimal places. (c) Use the PGF to find E(T).",
            "steps": [
                "(a) G<sub>T</sub>(t) = G<sub>X</sub>(t)G<sub>Y</sub>(t) = (0.3 + 0.7t)³ e^(t − 1).",
                "(b) P(T = 0) = G<sub>T</sub>(0) = 0.3³e⁻¹ = 0.027e⁻¹ = 0.0099.",
                "(0.3 + 0.7t)³ = 0.027 + 0.189t + … and e^(t − 1) = e⁻¹(1 + t + …).",
                "Coefficient of t: e⁻¹(0.027 × 1 + 0.189 × 1) = 0.216e⁻¹, so P(T = 1) = 0.0795.",
                "(c) G<sub>T</sub>′(t) = 2.1(0.3 + 0.7t)² e^(t − 1) + (0.3 + 0.7t)³ e^(t − 1), so E(T) = G<sub>T</sub>′(1) = 2.1 + 1 = 3.1.",
            ],
        },
        {
            "title": "PGF of aX + b (Edexcel)",
            "question": "X ~ Po(2) and Y = 3X + 1. (a) Find G<sub>Y</sub>(t). (b) Use G<sub>Y</sub>(t) to find E(Y) and Var(Y), and check your answers.",
            "steps": [
                "(a) G<sub>Y</sub>(t) = t G<sub>X</sub>(t³) = t e^(2(t³ − 1)).",
                "(b) Write u = 2(t³ − 1), so du/dt = 6t². G<sub>Y</sub>′(t) = e^u + 6t³e^u, so E(Y) = G<sub>Y</sub>′(1) = 1 + 6 = 7.",
                "G<sub>Y</sub>″(t) = 6t²e^u + 18t²e^u + 36t⁵e^u, so G<sub>Y</sub>″(1) = 6 + 18 + 36 = 60.",
                "Var(Y) = 60 + 7 − 7² = 18.",
                "Check: E(Y) = 3 × 2 + 1 = 7 and Var(Y) = 3² × 2 = 18.",
            ],
        },
        {
            "title": "Negative binomial as a sum of geometrics (Edexcel)",
            "question": "A basketball player scores each free throw with probability 0.4, independently. X is the number of throws "
                        "needed to score 3 times. (a) Explain why G<sub>X</sub>(t) = [0.4t/(1 − 0.6t)]³. (b) Find E(X) and Var(X). "
                        "(c) Find P(X = 5).",
            "steps": [
                "(a) X = X₁ + X₂ + X₃, where Xᵢ is the number of throws from the (i − 1)th score up to and including the ith. The Xᵢ "
                "are independent Geo(0.4), each with PGF 0.4t/(1 − 0.6t), so G<sub>X</sub> is the cube.",
                "(b) E(X) = 3 × 1/0.4 = 7.5 and Var(X) = 3 × 0.6/0.4² = 11.25 (these are r/p and rq/p² with r = 3).",
                "(c) X = 5 means exactly 2 scores in the first 4 throws, then a score on the 5th.",
                "P(X = 5) = C(4, 2)(0.4)³(0.6)² = 6 × 0.064 × 0.36 = 0.138 (3 s.f.).",
            ],
        },
    ],
    "practice": [
        "A random variable X has G(t) = (t + 2t² + 3t³)/6. Show that G(1) = 1, and find E(X) and Var(X).",
        "X ~ B(4, 0.5). Write down G(t) and use G′(1) to show that E(X) = 2.",
        "X ~ Geo(0.4). Write down G(t), find G′(t) and hence show that E(X) = 2.5.",
        "Prove that if X ~ B(n, p), then E(X) = np and Var(X) = np(1 − p), using the PGF.",
        "X ~ B(2, 0.5) and Y ~ B(3, 0.5) are independent. Use PGFs to find the distribution of X + Y, and find P(X + Y = 2).",
        "X ~ Po(1.5) and Y ~ Po(2.5) are independent. Use PGFs to find the distribution of X + Y and P(X + Y = 4), giving your answer to 4 decimal places.",
        "X is the score on a fair six-sided die. Write down G<sub>X</sub>(t), and use it to find E(X) and Var(X).",
        "The PGF of X is G(t) = 1/(4 − 3t). (a) Find P(X = r) for r = 0, 1, 2, … . (b) Find E(X) and Var(X).",
        "The PGF of X is G(t) = kt²(1 + t)³. (a) Find k. (b) Find P(X = 3). (c) Find E(X).",
        "X ~ B(5, 0.2) and Y = 2X + 3. Find G<sub>Y</sub>(t), and use it to find E(Y). (Edexcel)",
        "X ~ Po(λ). Use the PGF to show that Var(X) = λ.",
        "Explain why G(t) = 0.5 + 0.3t + 0.3t² cannot be a probability generating function.",
    ],
    "answers": [
        "G(1) = (1 + 2 + 3)/6 = 1. G′(t) = (1 + 4t + 9t²)/6, so E(X) = 14/6 = 7/3. G″(t) = (4 + 18t)/6, so G″(1) = 22/6 = 11/3. Var(X) = 11/3 + 7/3 − (7/3)² = 6 − 49/9 = 5/9.",
        "G(t) = (0.5 + 0.5t)⁴. G′(t) = 4 × 0.5(0.5 + 0.5t)³, so G′(1) = 2 × 1 = 2. Hence E(X) = 2.",
        "G(t) = 0.4t/(1 − 0.6t). G′(t) = 0.4/(1 − 0.6t)², so G′(1) = 0.4/0.16 = 2.5 = E(X).",
        "G(t) = (q + pt)ⁿ, G′(t) = np(q + pt)^(n−1), G″(t) = n(n − 1)p²(q + pt)^(n−2). At t = 1, q + p = 1, so E(X) = np and G″(1) = n(n − 1)p². Var(X) = n(n − 1)p² + np − n²p² = np − np² = np(1 − p).",
        "G<sub>X+Y</sub>(t) = (0.5 + 0.5t)²(0.5 + 0.5t)³ = (0.5 + 0.5t)⁵, so X + Y ~ B(5, 0.5). P(X + Y = 2) = C(5, 2)/32 = 10/32 = 0.3125.",
        "G<sub>X+Y</sub>(t) = e^(1.5(t − 1))e^(2.5(t − 1)) = e^(4(t − 1)), so X + Y ~ Po(4). P(X + Y = 4) = e⁻⁴4⁴/4! = 0.1954.",
        "G(t) = (t + t² + … + t⁶)/6. G′(1) = (1 + 2 + … + 6)/6 = 21/6 = 3.5. G″(1) = (0 + 2 + 6 + 12 + 20 + 30)/6 = 70/6 = 35/3. Var(X) = 35/3 + 7/2 − 49/4 = 35/12.",
        "(a) G(t) = ¼(1 − ¾t)⁻¹ = ¼ Σ (¾)ʳtʳ, so P(X = r) = ¼(¾)ʳ, r = 0, 1, 2, … . (b) G′(t) = 3/(4 − 3t)², so E(X) = 3. G″(t) = 18/(4 − 3t)³, so G″(1) = 18 and Var(X) = 18 + 3 − 9 = 12.",
        "(a) G(1) = k × 8 = 1, so k = 1/8. (b) Coefficient of t³ is k × C(3, 1) = 3/8. (c) X = 2 + W with W ~ B(3, ½), so E(X) = 2 + 1.5 = 3.5 (or G′(t) = (2t(1 + t)³ + 3t²(1 + t)²)/8, G′(1) = (16 + 12)/8 = 3.5).",
        "G<sub>Y</sub>(t) = t³G<sub>X</sub>(t²) = t³(0.8 + 0.2t²)⁵. G<sub>Y</sub>′(t) = 3t²(0.8 + 0.2t²)⁵ + t³ × 5(0.8 + 0.2t²)⁴ × 0.4t, so E(Y) = G<sub>Y</sub>′(1) = 3 + 2 = 5.",
        "G(t) = e^(λ(t−1)), G′(t) = λe^(λ(t−1)), G″(t) = λ²e^(λ(t−1)). G′(1) = λ and G″(1) = λ², so Var(X) = λ² + λ − λ² = λ.",
        "G(1) = 0.5 + 0.3 + 0.3 = 1.1 ≠ 1, so the coefficients (probabilities) do not sum to 1.",
    ],
    "exam": [
        "A bag contains four discs numbered 1, 2, 2 and 3. A disc is chosen at random and X is its number.\n"
        "(a) Show that the PGF of X is G<sub>X</sub>(t) = ¼t(1 + t)². [2]\n"
        "A disc is chosen, replaced, and a second disc is chosen. S is the total of the two numbers.\n"
        "(b) Find the PGF of S, simplifying your answer. [2]\n"
        "(c) Hence find P(S = 4). [2]\n"
        "(d) Use the PGF of S to find E(S) and Var(S). [5]",
        "An archer hits the centre of a target with probability 0.3 on each shot, independently. X is the number of shots needed to hit the centre 3 times. (Edexcel)\n"
        "(a) Show that the PGF of the number of shots needed for one hit is 0.3t/(1 − 0.7t). [3]\n"
        "(b) Hence write down the PGF of X, giving a reason. [2]\n"
        "(c) Use your PGF to find E(X). [3]\n"
        "(d) Find Var(X). [2]\n"
        "(e) Find P(X = 5). [2]",
        "The discrete random variable X has PGF G<sub>X</sub>(t) = k(3 + t)⁴. (Edexcel)\n"
        "(a) Find the value of k. [1]\n"
        "(b) Identify the distribution of X, giving its parameters. [2]\n"
        "Y = 2X + 1.\n"
        "(c) Find G<sub>Y</sub>(t). [2]\n"
        "(d) Find P(Y = 5). [2]\n"
        "(e) Use G<sub>Y</sub>(t) to find E(Y) and Var(Y). [5]",
        "X ~ Po(2). Y is independent of X, and is equally likely to take the values 0, 1 and 2. T = X + Y.\n"
        "(a) Write down the PGFs of X and Y, and hence the PGF of T. [3]\n"
        "(b) Find P(T = 0) and P(T = 2), giving your answers to 3 significant figures. [4]\n"
        "(c) Use the PGF of T to find E(T) and Var(T). [5]",
    ],
    "exam_answers": [
        "(a) P(X = 1) = ¼, P(X = 2) = ½, P(X = 3) = ¼ [M1], so G<sub>X</sub>(t) = ¼t + ½t² + ¼t³ = ¼t(1 + 2t + t²) = ¼t(1 + t)² [A1].\n"
        "(b) G<sub>S</sub>(t) = [G<sub>X</sub>(t)]² [M1] = t²(1 + t)⁴/16 [A1].\n"
        "(c) Coefficient of t⁴ needs the t² term of (1 + t)⁴, which is 6 [M1], so P(S = 4) = 6/16 = 3/8 [A1].\n"
        "(d) G<sub>S</sub>′(t) = [2t(1 + t)⁴ + 4t²(1 + t)³]/16 [M1]; G<sub>S</sub>′(1) = (32 + 32)/16 = 4 = E(S) [A1]. "
        "G<sub>S</sub>″(t) = [2(1 + t)⁴ + 16t(1 + t)³ + 12t²(1 + t)²]/16 [M1]; G<sub>S</sub>″(1) = (32 + 128 + 48)/16 = 13 [A1]. "
        "Var(S) = 13 + 4 − 16 = 1 [A1].",
        "(a) P(Y = y) = 0.3(0.7)^(y−1), y = 1, 2, … [B1]; G(t) = Σ 0.3(0.7)^(y−1)tʸ = 0.3t Σ (0.7t)^(y−1) [M1] = 0.3t/(1 − 0.7t), summing a geometric series, |t| < 1/0.7 [A1].\n"
        "(b) X is the sum of 3 independent such variables [B1], so G<sub>X</sub>(t) = [0.3t/(1 − 0.7t)]³ [B1].\n"
        "(c) G<sub>X</sub>′(t) = 3[0.3t/(1 − 0.7t)]² × 0.3/(1 − 0.7t)² [M1 A1]; G<sub>X</sub>′(1) = 3 × 1 × 0.3/0.09 = 10 [A1].\n"
        "(d) Var(X) = 3 × 0.7/0.3² [M1] = 23.3 (3 s.f.; exactly 70/3) [A1].\n"
        "(e) C(4, 2)(0.3)³(0.7)² [M1] = 0.0794 (3 s.f.) [A1].",
        "(a) G(1) = k × 4⁴ = 1, so k = 1/256 [B1].\n"
        "(b) G<sub>X</sub>(t) = ((3 + t)/4)⁴ = (¾ + ¼t)⁴ [M1], so X ~ B(4, ¼) [A1].\n"
        "(c) G<sub>Y</sub>(t) = t G<sub>X</sub>(t²) [M1] = t(3 + t²)⁴/256 [A1].\n"
        "(d) Y = 5 when X = 2: coefficient of t⁵ is C(4, 2) × 3²/256 [M1] = 54/256 = 27/128 = 0.211 (3 s.f.) [A1].\n"
        "(e) G<sub>Y</sub>′(t) = [(3 + t²)⁴ + 8t²(3 + t²)³]/256 [M1]; E(Y) = (256 + 512)/256 = 3 [A1]. "
        "G<sub>Y</sub>″(t) = [8t(3 + t²)³ + 16t(3 + t²)³ + 48t³(3 + t²)²]/256 [M1]; G<sub>Y</sub>″(1) = (512 + 1024 + 768)/256 = 9 [A1]. "
        "Var(Y) = 9 + 3 − 9 = 3 [A1]. (Check: 2² × Var(X) = 4 × ¾ = 3.)",
        "(a) G<sub>X</sub>(t) = e^(2(t − 1)) [B1], G<sub>Y</sub>(t) = (1 + t + t²)/3 [B1], G<sub>T</sub>(t) = e^(2(t − 1))(1 + t + t²)/3 [B1].\n"
        "(b) P(T = 0) = G<sub>T</sub>(0) = e⁻²/3 = 0.0451 [M1 A1]. e^(2(t − 1)) = e⁻²(1 + 2t + 2t² + …), so the coefficient of t² is "
        "e⁻²(2 + 2 + 1)/3 [M1] = 5e⁻²/3 = 0.226 [A1].\n"
        "(c) G<sub>T</sub>′(t) = e^(2(t−1))[2(1 + t + t²) + (1 + 2t)]/3 [M1]; E(T) = (6 + 3)/3 = 3 [A1]. "
        "G<sub>T</sub>″(t) = e^(2(t−1))[4(1 + t + t²) + 4(1 + 2t) + 2]/3 [M1]; G<sub>T</sub>″(1) = (12 + 12 + 2)/3 = 26/3 [A1]. "
        "Var(T) = 26/3 + 3 − 9 = 8/3 [A1] (= 2 + 2/3, as Var(X) + Var(Y)).",
    ],
}
