UNIT = {
    "number": "A2.7",
    "title": "Sampling distributions, the CLT and estimators",
    "tag": "Edexcel FS1 (5: CLT) and FS2 (5.1: estimators, bias, quality) · IAL S3 (3.1, 3.2, 3.6) · OCR A (5.05a–b) · OCR MEI Major (SI1–SI6) · CAIE 9709 S2 prior knowledge (required)",
    "notes": [
        ("h2", "7.1 Populations, parameters, samples and statistics"),
        ("p", "A <b>population</b> is the whole set of items of interest. A <b>parameter</b> is a numerical property of the population, "
              "such as its mean μ, variance σ² or proportion p; it is fixed but usually unknown. A <b>random sample</b> of size n is a "
              "set of n independent observations X₁, X₂, …, Xₙ, each with the population's distribution. A <b>statistic</b> is any "
              "quantity calculated from the sample alone, with no unknown parameters, for example X̄ = ΣXᵢ/n, the sample maximum, or S²."),
        ("p", "Because a statistic depends on which sample happens to be chosen, it is itself a random variable. Its probability "
              "distribution, over all possible samples, is its <b>sampling distribution</b>. Capital letters (X̄, S²) denote the random "
              "variables; lower-case letters (x̄, s²) denote the values from one observed sample."),
        ("h2", "7.2 The distribution of the sample mean"),
        ("box", "Mean and variance of X̄ (all boards)", [
            "E(X̄) = μ    and    Var(X̄) = σ²/n.",
            "The <b>standard error</b> of the mean is the standard deviation of X̄: σ/√n. If σ is unknown it is estimated by s/√n.",
            "If the population is normal, X ~ N(μ, σ²), then X̄ ~ N(μ, σ²/n) <b>exactly</b>, for every n (IAL S3 3.2, MEI SI5).",
            "The total T = ΣXᵢ has E(T) = nμ and Var(T) = nσ²; if X is normal, T ~ N(nμ, nσ²).",
        ]),
        ("p", "Proof (using the expectation algebra of Unit A2.6): E(X̄) = (1/n)[E(X₁) + … + E(Xₙ)] = (1/n)(nμ) = μ. Because the Xᵢ are "
              "independent, Var(X̄) = (1/n²)[Var(X₁) + … + Var(Xₙ)] = (1/n²)(nσ²) = σ²/n. So the sample mean is centred on μ, and its "
              "spread shrinks as n grows: quadrupling n halves the standard error. No board asks for a proof of the CLT itself."),
        ("h2", "7.3 The Central Limit Theorem"),
        ("box", "Central Limit Theorem (CLT)", [
            "If X₁, …, Xₙ is a random sample from <b>any</b> distribution with mean μ and finite variance σ², then for large n",
            "X̄ ≈ N(μ, σ²/n)    and    ΣXᵢ ≈ N(nμ, nσ²).",
            "\"Large\": MEI uses n > 30 as a rule of thumb, OCR A says n > about 25, and Edexcel and IAL just say \"large\". "
            "The more skewed the population, the larger n must be. If the population is normal, no approximation is needed.",
        ]),
        ("p", "The CLT is why the normal distribution appears so often: means and totals of many independent effects are approximately "
              "normal, whatever the shape of each effect. Edexcel FS1 applies it to any distribution in A level Mathematics or FS1 "
              "(binomial, Poisson, geometric, discrete and continuous uniform, normal); OCR A also uses the exponential."),
        ("table", ["Population", "μ", "σ²", "X̄ for large n"], [
            ["Po(λ)", "λ", "λ", "≈ N(λ, λ/n)"],
            ["B(m, p)", "mp", "mp(1 − p)", "≈ N(mp, mp(1 − p)/n)"],
            ["Geo(p)", "1/p", "(1 − p)/p²", "≈ N(1/p, (1 − p)/(np²))"],
            ["U(a, b)", "(a + b)/2", "(b − a)²/12", "≈ N((a + b)/2, (b − a)²/(12n))"],
            ["Exp(λ)", "1/λ", "1/λ²", "≈ N(1/λ, 1/(nλ²))"],
            ["N(μ, σ²)", "μ", "σ²", "= N(μ, σ²/n) exactly"],
        ]),
        ("p", "<b>Continuity corrections</b> (MEI SI6; Edexcel and IAL do not use them with the CLT). If the population is discrete, "
              "the total ΣXᵢ takes only whole-number values, and a continuity correction improves the approximation: for the total of "
              "50 dice, P(T > 185) = P(T ≥ 186) ≈ P(Y > 185.5) where Y is the normal approximation. The same idea gives the familiar "
              "normal approximations from A level Mathematics: B(n, p) ≈ N(np, np(1 − p)) when np and n(1 − p) are both large (both > 5), "
              "and Po(λ) ≈ N(λ, λ) when λ is large, with P(X ≤ k) ≈ P(Y ≤ k + 0.5) and P(X ≥ k) ≈ P(Y ≥ k − 0.5)."),
        ("h2", "7.4 Estimators and bias"),
        ("p", "An <b>estimator</b> T of a parameter θ is a statistic used to estimate θ; the value it takes for a particular sample is an "
              "<b>estimate</b>. T is <b>unbiased</b> if E(T) = θ for every value of θ: on average, over all samples, it hits the target. "
              "The <b>bias</b> is E(T) − θ. OCR A needs only an informal idea of \"unbiased\"; Edexcel and IAL use the formal definition."),
        ("box", "Standard unbiased estimates (given in the formula booklets)", [
            "Mean: x̄ = Σx/n is an unbiased estimate of μ.",
            "Variance: s² = Σ(x − x̄)²/(n − 1) = (Σx² − n x̄²)/(n − 1) = [Σx² − (Σx)²/n]/(n − 1) is an unbiased estimate of σ².",
            "Proportion: p̂ = x/n is an unbiased estimate of p (since E(X/n) = np/n = p for X ~ B(n, p)).",
            "Standard error of the mean: estimated by s/√n.",
        ]),
        ("p", "<b>Why n − 1?</b> The deviations are measured from x̄, which is fitted to the same data, so they are on average a little "
              "smaller than deviations from μ. Proof that E(S²) = σ² (useful for Edexcel bias questions; no board requires it "
              "in general form): Σ(Xᵢ − X̄)² = ΣXᵢ² − nX̄². Now E(Xᵢ²) = Var(Xᵢ) + μ² = σ² + μ² and E(X̄²) = Var(X̄) + μ² = σ²/n + μ². "
              "So E[Σ(Xᵢ − X̄)²] = n(σ² + μ²) − n(σ²/n + μ²) = (n − 1)σ². Dividing by n − 1 gives E(S²) = σ². Dividing by n instead "
              "gives an estimator with expectation (n − 1)σ²/n, which is biased (too small on average) by −σ²/n."),
        ("h2", "7.5 Comparing estimators (Edexcel FS2 5.1)"),
        ("p", "A good estimator is unbiased and has a small variance, so that individual estimates are usually close to θ. "
              "Given two unbiased estimators, prefer the one with the <b>smaller variance</b> (it is more efficient). A biased estimator "
              "may still be useful if its bias is small and its variance much smaller, but at this level you compare unbiasedness first, "
              "then variance."),
        ("bullets", [
            "To test unbiasedness, find E(T) using E(aX + bY) = aE(X) + bE(Y) and compare with θ.",
            "To find Var(T) for independent observations, use Var(aX + bY) = a²Var(X) + b²Var(Y).",
            "A weighted mean aX₁ + bX₂ + … is unbiased for μ exactly when the weights add up to 1; equal weights give the smallest variance.",
            "If E(T) = kθ, then T/k is an unbiased estimator of θ. For example, for U(0, θ), E(X̄) = θ/2, so 2X̄ is unbiased for θ.",
            "Common sense still matters: an unbiased estimate can be impossible for the observed data (see Worked example A2.7.6).",
        ]),
        ("warn", "Common mistakes", [
            "Confusing the standard deviation of X (σ) with the standard error of X̄ (σ/√n).",
            "Using Var(X̄) = σ²/n² or σ/n.",
            "Applying the CLT to the individual observations: the CLT is about the <b>mean or total</b> of a large sample, not about X itself.",
            "Saying \"n > 30, so X is normal\". Say: \"n is large, so by the CLT X̄ is approximately normal\". Cambridge examiners report that quoting \"n > 30\" alone is not enough.",
            "Using the divisor n when an unbiased estimate of σ² is asked for.",
            "Thinking an unbiased estimator always gives the right answer: it is right on average, not every time.",
            "Comparing estimators by variance before checking they are unbiased.",
        ]),
    ],
    "examples": [
        {
            "title": "Exact distribution of X̄ from a normal population",
            "question": "The lifetimes of a type of battery are N(50, 8²) hours. Find the probability that the mean lifetime of a random sample of 16 batteries exceeds 53 hours.",
            "steps": [
                "The population is normal, so X̄ ~ N(50, 8²/16) = N(50, 4) exactly. Standard error = 2.",
                "P(X̄ > 53) = P(Z > (53 − 50)/2) = P(Z > 1.5) = 1 − 0.9332 = 0.0668 (3 s.f.).",
            ],
        },
        {
            "title": "The CLT for a non-normal population",
            "question": "A population has mean 50 and variance 100; its distribution is not known. A random sample of 40 is taken. Find P(X̄ > 52), justifying your method.",
            "steps": [
                "n = 40 is large, so by the Central Limit Theorem X̄ ≈ N(50, 100/40) = N(50, 2.5).",
                "P(X̄ > 52) ≈ P(Z > 2/√2.5) = P(Z > 1.265) = 0.103 (3 s.f.).",
            ],
        },
        {
            "title": "A total of discrete values with a continuity correction (MEI)",
            "question": "A fair die is rolled 50 times. Use a normal approximation to estimate the probability that the total score is more than 185.",
            "steps": [
                "One roll has mean 3.5 and variance 35/12. The total T has mean 50 × 3.5 = 175 and variance 50 × 35/12 = 145.83.",
                "By the CLT, T ≈ N(175, 145.83). T takes whole-number values, so P(T > 185) = P(T ≥ 186) ≈ P(Y > 185.5).",
                "P(Y > 185.5) = P(Z > 10.5/12.076) = P(Z > 0.8695) = 0.192 (3 s.f.). (The exact probability is 0.1928, so the approximation is very good.)",
            ],
        },
        {
            "title": "Unbiased estimates and the standard error",
            "question": "The masses (g) of a random sample of 6 apples are 12.1, 13.4, 11.8, 12.9, 13.0, 12.6. Find unbiased estimates of the population mean and variance, and estimate the standard error of the mean.",
            "steps": [
                "x̄ = 75.8/6 = 12.63 (4 s.f.).",
                "Σ(x − x̄)² = 1.7733, so s² = 1.7733/5 = 0.355 (3 s.f.).",
                "Estimated standard error = s/√n = √0.35467/√6 = 0.243 (3 s.f.).",
            ],
        },
        {
            "title": "Bias and choosing between estimators",
            "question": "X₁, X₂, X₃ is a random sample from a population with mean μ and variance σ². Consider T₁ = (X₁ + X₂ + X₃)/3, "
                        "T₂ = (2X₁ + X₂ + X₃)/4 and T₃ = (X₁ + X₂ + X₃)/2. (a) Which are unbiased for μ? (b) Find the bias of the other. "
                        "(c) Which unbiased estimator is better?",
            "steps": [
                "(a) E(T₁) = 3μ/3 = μ and E(T₂) = (2 + 1 + 1)μ/4 = μ, so both are unbiased. E(T₃) = 3μ/2 ≠ μ.",
                "(b) Bias of T₃ = 3μ/2 − μ = μ/2.",
                "(c) Var(T₁) = 3σ²/9 = σ²/3. Var(T₂) = (4 + 1 + 1)σ²/16 = 3σ²/8. Since 1/3 < 3/8, T₁ has the smaller variance and is the better estimator.",
            ],
        },
        {
            "title": "An estimator for a uniform distribution (Edexcel style)",
            "question": "X ~ U(0, θ). (a) Show that 2X̄, from a random sample of size n, is an unbiased estimator of θ, and find its variance. "
                        "(b) A sample of 5 gives 1.2, 3.8, 0.7, 2.5, 6.1. Find the estimate of θ, and comment.",
            "steps": [
                "(a) E(X) = θ/2, so E(2X̄) = 2 × θ/2 = θ: unbiased. Var(X) = θ²/12, so Var(2X̄) = 4 × θ²/(12n) = θ²/(3n).",
                "(b) x̄ = 14.3/5 = 2.86, so the estimate is 2 × 2.86 = 5.72.",
                "Comment: one observation is 6.1, so θ must be at least 6.1. The unbiased estimate is impossible for these data: "
                "being right on average does not guarantee a sensible value for every sample.",
            ],
        },
    ],
    "practice": [
        "X ~ N(12, 4²). A random sample of 64 is taken. Find P(X̄ < 11).",
        "A population has mean 30 and standard deviation 5. A random sample of 50 is taken. Find P(29 < X̄ < 31.5), stating the theorem you use.",
        "A fair die is rolled 50 times. Use a normal approximation with a continuity correction to find P(total score > 185).",
        "X ~ Po(3). A random sample of 40 observations is taken. Use the Central Limit Theorem to find P(X̄ > 3.4).",
        "The time between arrivals is exponential with mean 2 minutes. Find the approximate probability that the mean of 36 such times exceeds 2.5 minutes.",
        "A population has standard deviation 6. How large must a sample be for P(|X̄ − μ| < 1) to be at least 0.95?",
        "The masses (g) of a random sample of 6 apples are 12.1, 13.4, 11.8, 12.9, 13.0, 12.6. Find unbiased estimates of the population mean and standard deviation.",
        "A random sample of 20 gives Σx = 310 and Σx² = 4900. Find unbiased estimates of μ and σ², and estimate the standard error of the mean.",
        "X₁ and X₂ are independent observations from a population with mean μ and variance σ². Show that T = (X₁ + 3X₂)/4 is unbiased for μ, find Var(T), and compare it with X̄ = (X₁ + X₂)/2.",
        "Show that aX₁ + bX₂ (notation as in the previous question) is unbiased for μ if and only if a + b = 1, and find the value of a that minimises its variance.",
        "Show that V = Σ(Xᵢ − X̄)²/n is a biased estimator of σ², and find its bias.",
        "X ~ B(80, 0.25). Use a suitable approximation to find P(X ≥ 25), giving your answer to 3 decimal places.",
    ],
    "answers": [
        "X̄ ~ N(12, 0.25) exactly. P(X̄ < 11) = Φ(−1/0.5) = Φ(−2) = 0.0228 (3 s.f.).",
        "By the CLT (n = 50 large), X̄ ≈ N(30, 0.5), standard error 0.7071. P = Φ(2.121) − Φ(−1.414) = 0.904 (3 s.f.).",
        "T ≈ N(175, 145.83). P(T > 185) ≈ P(Y > 185.5) = 1 − Φ(0.8695) = 0.192 (3 s.f.).",
        "X̄ ≈ N(3, 3/40). P(X̄ > 3.4) = 1 − Φ(0.4/√0.075) = 1 − Φ(1.461) = 0.0721 (3 s.f.).",
        "μ = 2, σ = 2, so X̄ ≈ N(2, 4/36). P(X̄ > 2.5) = 1 − Φ(0.5/(1/3)) = 1 − Φ(1.5) = 0.0668 (3 s.f.).",
        "1.96 × 6/√n ≤ 1, so n ≥ 138.3 and n = 139.",
        "x̄ = 12.63 (4 s.f.); s² = 1.7733/5 = 0.3547, so s = 0.596 (3 s.f.).",
        "x̄ = 15.5. s² = (4900 − 20 × 15.5²)/19 = 95/19 = 5. Estimated standard error = √(5/20) = 0.5.",
        "E(T) = (μ + 3μ)/4 = μ. Var(T) = (1 + 9)σ²/16 = 5σ²/8. Var(X̄) = σ²/2 < 5σ²/8, so X̄ is the better (more efficient) estimator.",
        "E(aX₁ + bX₂) = (a + b)μ, which equals μ for all μ if and only if a + b = 1. Var = (a² + (1 − a)²)σ², minimised when 2a − 2(1 − a) = 0, i.e. a = 1/2.",
        "E[Σ(Xᵢ − X̄)²] = (n − 1)σ², so E(V) = (n − 1)σ²/n ≠ σ². Bias = (n − 1)σ²/n − σ² = −σ²/n.",
        "np = 20 and np(1 − p) = 15 are both large, so X ≈ Y ~ N(20, 15). P(X ≥ 25) ≈ P(Y ≥ 24.5) = 1 − Φ(4.5/√15) = 0.123.",
    ],
    "exam": [
        "The masses of parcels handled by a courier have mean 2.4 kg and standard deviation 0.9 kg. The distribution of masses is positively skewed. "
        "A van is loaded with a random sample of 50 parcels. (a) State the Central Limit Theorem. [2] "
        "(b) Find the approximate probability that the total mass of the 50 parcels exceeds 125 kg. [4] "
        "(c) Find the approximate probability that the mean mass of the 50 parcels is within 0.2 kg of 2.4 kg. [3] "
        "(d) Explain why your answers are only approximate, even though the mean and standard deviation are known exactly. [1]",
        "X₁, X₂, X₃ is a random sample from a population with mean μ and variance σ². "
        "T₁ = (X₁ + X₂ + X₃)/3, T₂ = (X₁ + 2X₂ + 3X₃)/6 and T₃ = (2X₁ + 3X₂ + 2X₃)/5. "
        "(a) Show that T₁ and T₂ are unbiased estimators of μ. [3] (b) Find the bias of T₃. [2] "
        "(c) Find Var(T₁) and Var(T₂). [3] (d) State, with a reason, which of T₁ and T₂ is the better estimator. [2] "
        "(e) Find the constant c for which cT₃ is an unbiased estimator of μ. [1]",
        "The random variable X has a continuous uniform distribution on [θ, 2θ], where θ > 0. A random sample X₁, …, Xₙ is taken. "
        "(a) Show that θ̂ = (2/3)X̄ is an unbiased estimator of θ. [3] (b) Show that Var(θ̂) = θ²/(27n). [3] "
        "(c) A sample of 10 observations has Σx = 45.6. Find the estimate of θ. [1] "
        "(d) Estimate the standard error of θ̂. [2] "
        "(e) The largest observation in this sample was 6.3. Comment on your estimate. [2]",
        "A random sample of 12 observations of a random variable X gives Σx = 87.6 and Σx² = 662.04. "
        "(a) Find unbiased estimates of the mean and variance of X. [3] (b) Estimate the standard error of the sample mean. [2] "
        "(c) Prove that, for a random sample of size n from a population with mean μ and variance σ², E[Σ(Xᵢ − X̄)²] = (n − 1)σ². [5] "
        "(d) Hence explain why the divisor n − 1 is used in (a). [1]",
    ],
    "exam_answers": [
        "(a) For a large random sample from any distribution with mean μ and variance σ² [B1], the sample mean is approximately N(μ, σ²/n) (or the total is approximately N(nμ, nσ²)) [B1]. "
        "(b) Total T ≈ N(50 × 2.4, 50 × 0.9²) = N(120, 40.5) [M1 A1]; P(T > 125) = P(Z > 5/√40.5) = P(Z > 0.7857) [M1] = 0.216 (3 s.f.) [A1]. "
        "(c) X̄ ≈ N(2.4, 0.81/50), standard error 0.1273 [M1]; P(|X̄ − 2.4| < 0.2) = 2Φ(1.571) − 1 [M1] = 0.884 (3 s.f.) [A1]. "
        "(d) The population is not normal, so the CLT gives only an approximate normal distribution for X̄ (and for the total) [B1].",
        "(a) E(T₁) = (μ + μ + μ)/3 = μ [B1]. E(T₂) = (μ + 2μ + 3μ)/6 = μ [M1 A1]. "
        "(b) E(T₃) = 7μ/5 [M1], bias = 7μ/5 − μ = 2μ/5 [A1]. "
        "(c) Var(T₁) = 3σ²/9 = σ²/3 [B1]; Var(T₂) = (1 + 4 + 9)σ²/36 [M1] = 7σ²/18 [A1]. "
        "(d) Both are unbiased and σ²/3 = 6σ²/18 < 7σ²/18 [M1], so T₁ is better because it has the smaller variance [A1]. "
        "(e) c = 5/7 [B1].",
        "(a) E(X) = (θ + 2θ)/2 = 3θ/2 [B1]; E(X̄) = 3θ/2 [M1]; E(θ̂) = (2/3)(3θ/2) = θ, so unbiased [A1]. "
        "(b) Var(X) = (2θ − θ)²/12 = θ²/12 [B1]; Var(X̄) = θ²/(12n) [M1]; Var(θ̂) = (4/9)θ²/(12n) = θ²/(27n) [A1]. "
        "(c) θ̂ = (2/3)(4.56) = 3.04 [B1]. "
        "(d) Standard error = θ/√(27n), estimated by 3.04/√270 [M1] = 0.185 (3 s.f.) [A1]. "
        "(e) Every observation must be at most 2θ, so θ ≥ 6.3/2 = 3.15 [M1]; the estimate 3.04 is impossible for this sample, so it is a poor estimate here [A1].",
        "(a) x̄ = 87.6/12 = 7.3 [B1]; s² = (662.04 − 12 × 7.3²)/11 [M1] = 22.56/11 = 2.05 (3 s.f.) [A1]. "
        "(b) s/√12 = √2.0509/√12 [M1] = 0.413 (3 s.f.) [A1]. "
        "(c) Σ(Xᵢ − X̄)² = ΣXᵢ² − nX̄² [M1]. E(Xᵢ²) = σ² + μ² [B1]; E(X̄²) = σ²/n + μ² [B1]. "
        "E[Σ(Xᵢ − X̄)²] = n(σ² + μ²) − n(σ²/n + μ²) [M1] = (n − 1)σ² [A1]. "
        "(d) Dividing by n − 1 gives an estimator whose expectation is σ², i.e. an unbiased estimator of σ² [B1].",
    ],
}
