"""Formula sheet for the back of the workbook."""

SECTION = {
    "title": "Formula sheet",
    "notes": [
        ("p", "A summary of every result used in the workbook. Your board's booklet gives some of these; the rest must be "
              "learnt. Check the coverage map for the topics your board examines."),
        ("h2", "Discrete distributions"),
        ("table", ["Distribution", "P(X = x)", "E(X)", "Var(X)", "PGF G(t)"], [
            ["Discrete uniform on 1, …, n", "1/n,  x = 1, …, n", "(n + 1)/2", "(n² − 1)/12", "t(1 − tⁿ) / (n(1 − t))"],
            ["Binomial B(n, p)", "C(n, x) pˣ (1 − p)ⁿ⁻ˣ,  x = 0, …, n", "np", "np(1 − p)", "(1 − p + pt)ⁿ"],
            ["Poisson Po(λ)", "e^(−λ) λˣ / x!,  x = 0, 1, …", "λ", "λ", "e^(λ(t − 1))"],
            ["Geometric Geo(p)", "(1 − p)^(x−1) p,  x = 1, 2, …", "1/p", "(1 − p)/p²", "pt / (1 − (1 − p)t)"],
            ["Negative binomial (r-th success)", "C(x − 1, r − 1) pʳ (1 − p)^(x−r),  x = r, r + 1, …", "r/p", "r(1 − p)/p²", "[pt / (1 − (1 − p)t)]ʳ"],
        ]),
        ("bullets", [
            "Geometric: P(X > x) = (1 − p)ˣ and P(X ≤ x) = 1 − (1 − p)ˣ.",
            "E(X) = Σ x P(X = x);  E(g(X)) = Σ g(x) P(X = x);  Var(X) = E(X²) − [E(X)]².",
        ]),
        ("h2", "Continuous distributions"),
        ("table", ["Distribution", "f(x)", "F(x)", "E(X)", "Var(X)"], [
            ["Continuous uniform U(a, b)", "1/(b − a),  a ≤ x ≤ b", "(x − a)/(b − a)", "(a + b)/2", "(b − a)²/12"],
            ["Exponential, rate λ", "λe^(−λx),  x ≥ 0", "1 − e^(−λx)", "1/λ", "1/λ²"],
            ["Normal N(μ, σ²)", "bell-shaped, symmetric about μ", "Φ((x − μ)/σ)", "μ", "σ²"],
        ]),
        ("bullets", [
            "E(X) = ∫ x f(x) dx;  E(g(X)) = ∫ g(x) f(x) dx;  Var(X) = E(X²) − [E(X)]².",
            "F(x) = P(X ≤ x) = ∫ f(t) dt from the lower limit to x;  f(x) = F′(x).  Median m: F(m) = 0.5.",
            "Exponential: memoryless, P(X > s + t | X > s) = P(X > t). If events follow a Poisson process with rate λ, the "
            "time between events is exponential with rate λ.",
        ]),
        ("h2", "Expectation algebra"),
        ("bullets", [
            "E(aX + b) = aE(X) + b;  Var(aX + b) = a² Var(X).",
            "E(aX ± bY) = aE(X) ± bE(Y);  Var(aX ± bY) = a² Var(X) + b² Var(Y) for independent X, Y.",
            "If X and Y are independent normal variables, aX ± bY is normal.  X₁ + X₂ + … + Xₙ ~ N(nμ, nσ²) but 2X ~ N(2μ, 4σ²).",
            "Independent Poisson: X ~ Po(λ), Y ~ Po(μ) gives X + Y ~ Po(λ + μ).",
        ]),
        ("h2", "Probability generating functions"),
        ("bullets", [
            "G(t) = E(tˣ) = Σ P(X = x) tˣ;  G(1) = 1.",
            "E(X) = G′(1);  Var(X) = G″(1) + G′(1) − [G′(1)]².",
            "Independent X, Y: G<sub>X+Y</sub>(t) = G<sub>X</sub>(t) G<sub>Y</sub>(t).  For Y = aX + b: G<sub>Y</sub>(t) = t<sup>b</sup> G<sub>X</sub>(tᵃ).",
        ]),
        ("h2", "Sampling and estimation"),
        ("bullets", [
            "x̄ = Σx / n;  s² = Σ(x − x̄)² / (n − 1) = (Σx² − n x̄²) / (n − 1)  (unbiased estimate of σ²).",
            "E(X̄) = μ;  Var(X̄) = σ²/n;  standard error σ/√n.  CLT: for large n, X̄ ≈ N(μ, σ²/n).",
            "Confidence interval for μ: x̄ ± z σ/√n (σ known or n large) or x̄ ± t(n − 1) s/√n (normal population, σ unknown).",
            "Confidence interval for p (large n): p̂ ± z √(p̂(1 − p̂)/n).",
            "Interval for σ²: ((n − 1)s²/χ²<sub>upper</sub>, (n − 1)s²/χ²<sub>lower</sub>), using χ²(n − 1) percentage points.",
        ]),
        ("h2", "Test statistics"),
        ("table", ["Test", "Statistic", "Distribution under H₀"], [
            ["Mean, σ known (or n large)", "(x̄ − μ₀) / (σ/√n)", "N(0, 1)"],
            ["Mean, σ unknown, normal population", "(x̄ − μ₀) / (s/√n)", "t(n − 1)"],
            ["Difference of means, σ₁, σ₂ known (or large samples)", "(x̄₁ − x̄₂ − (μ₁ − μ₂)) / √(σ₁²/n₁ + σ₂²/n₂)", "N(0, 1)"],
            ["Difference of means, equal unknown variances", "(x̄₁ − x̄₂ − (μ₁ − μ₂)) / (s<sub>p</sub> √(1/n₁ + 1/n₂))", "t(n₁ + n₂ − 2)"],
            ["Paired samples (differences d)", "(d̄ − μ<sub>d</sub>) / (s<sub>d</sub>/√n)", "t(n − 1)"],
            ["Variance", "(n − 1)s² / σ₀²", "χ²(n − 1)"],
            ["Equality of two variances", "s₁² / s₂²  (larger on top)", "F(n₁ − 1, n₂ − 1)"],
            ["Goodness of fit / contingency table", "Σ (O − E)² / E", "χ²(ν)"],
            ["2 × 2 table with Yates' correction", "Σ (|O − E| − 0.5)² / E", "χ²(1)"],
        ]),
        ("bullets", [
            "Pooled variance: s<sub>p</sub>² = [(n₁ − 1)s₁² + (n₂ − 1)s₂²] / (n₁ + n₂ − 2) = [Σ(x₁ − x̄₁)² + Σ(x₂ − x̄₂)²] / (n₁ + n₂ − 2).",
            "χ² degrees of freedom: goodness of fit ν = (classes after combining) − 1 − (parameters estimated); contingency table ν = (r − 1)(c − 1).",
            "F lower tail: F<sub>1−α</sub>(ν₁, ν₂) = 1 / F<sub>α</sub>(ν₂, ν₁).",
        ]),
        ("h2", "Correlation and regression"),
        ("bullets", [
            "Sxx = Σx² − (Σx)²/n;  Syy = Σy² − (Σy)²/n;  Sxy = Σxy − (Σx)(Σy)/n.",
            "r = Sxy / √(Sxx Syy).  Spearman (no ties): rₛ = 1 − 6Σd² / (n(n² − 1)).",
            "Regression of y on x: y = a + bx, b = Sxy/Sxx, a = ȳ − b x̄.  Of x on y: x = a′ + b′y, b′ = Sxy/Syy.",
            "Residual e = y − (a + bx);  residual sum of squares RSS = Syy − Sxy²/Sxx = Syy(1 − r²).",
        ]),
        ("h2", "Non-parametric tests"),
        ("bullets", [
            "Sign test: under H₀ the number of + signs is B(n, 0.5) (values equal to the median or zero differences are discarded). "
            "For large n use N(n/2, n/4) with a continuity correction.",
            "Wilcoxon signed-rank: T = smaller of the sums of positive and negative ranks. For large n, T ≈ N(n(n + 1)/4, n(n + 1)(2n + 1)/24).",
            "Wilcoxon rank-sum (smaller sample size m, other n): R = sum of ranks of the smaller sample; use W = the smaller of R and "
            "m(m + n + 1) − R. For large samples, R ≈ N(m(m + n + 1)/2, mn(m + n + 1)/12).",
        ]),
    ],
}
