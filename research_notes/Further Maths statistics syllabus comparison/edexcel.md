# Pearson Edexcel Further Mathematics statistics content: 9FM0 FS1/FS2, 8FM0 FS1, IAL S3 (and the "S4" question)

Research date: 16 Nov 2026. All content below was read directly from the official Pearson PDFs (downloaded and text-extracted), not from aggregator sites.

**Primary sources used (exact URLs):**
- [9FM0 A level Further Mathematics specification, Issue 4, June 2023](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/a-level-l3-further-mathematics-specification.pdf). Abbreviated below as **[9FM0 spec]**.
- [8FM0 AS Further Mathematics specification, Issue 5, July 2025](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/as-l3-further-mathematics-specification.pdf). Abbreviated as **[8FM0 spec]**.
- [Mathematical formulae and statistical tables booklet for 8MA0/9MA0/8FM0/9FM0, code X54458A, ISBN 978 1 4469 4857 6, © 2017](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/X_18pt_A4_Formulae_Booklet_and_Statistical_Tables.pdf). This is the official 18pt large-print copy on Pearson's site. I could not find the URL for the standard-print copy, but the content and booklet code are the same. Abbreviated as **[GCE booklet]**.
- [IAL Mathematics, Further Mathematics and Pure Mathematics specification (XMA01/YMA01/XFM01/YFM01/XPM01/YPM01), first teaching Sept 2018, Issue 3, April 2019](https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/Mathematics/2018/Specification-and-Sample-Assessment/international-a-level-maths-spec.pdf). Abbreviated as **[IAL spec]**.
- IAL Mathematical Formulae and Statistical Tables, Issue 2, January 2021 (code P59773RA). I could not find this on Pearson's own site. I used a third-party copy whose cover, issue page and copyright are Pearson's: [publit.io copy](https://media.publit.io/file/formularsheetas/alevelmaths/IAL-Mathematics-Formula-Book.pdf). Abbreviated as **[IAL booklet]**. Check it against the copy in Pearson's exam papers before relying on it.
- [Previous IAL specification (first teaching 2013), Issue 3](https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/Mathematics/2013/Specification%20and%20sample%20assessments/9781446925201_IAL_Maths_Iss3.pdf). Used only to check whether an S4 unit ever existed.
- [IAL Mathematics (2018) qualification page](https://qualifications.pearson.com/en/qualifications/edexcel-international-advanced-levels/mathematics-2018.html). On 16 Nov 2026 it listed only the 2018 specification and showed no notice of a replacement specification.
- Past papers used to confirm marks: [9FM0/3B Oct 2020 QP](https://qualifications.pearson.com/content/dam/pdf/A-Level/Mathematics/2017/Exam-materials/9FM0_3B_que_20201017.pdf) and [8FM0/23 May 2022 QP](https://qualifications.pearson.com/content/dam/pdf/A-Level/Mathematics/2017/Exam-materials/8fm0-23-que-20220524.pdf).

---

## Q1. 9FM0 Further Statistics 1 (9FM0/3B) and Further Statistics 2 (9FM0/4B): every section and sub-point

### Takeaway
FS1 (Paper 3B) has 8 topics: discrete distributions, Poisson/binomial, geometric and negative binomial, hypothesis tests (Poisson, geometric), the Central Limit Theorem, χ² tests, PGFs, and quality of tests. FS2 (Paper 4B) has 7 topics: regression, continuous distributions, correlation, combinations of normal random variables, estimation/CIs/normal tests, χ² and F tests for variance, and t-tests. FS2 can only be taken paired with FS1. FS1 can also be sat as a Paper 4 option.

### Cited Findings

**Specification version.** 9FM0 spec Issue 4 (June 2023) is the current issue. First teaching Sept 2017, first certification 2019. The Issue 4 changes are typo corrections only, all in pure-maths guidance; none affect FS1 or FS2. — [9FM0 spec](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/a-level-l3-further-mathematics-specification.pdf), pp. cover–iii

**Paper 3B: Further Statistics 1** (spec pp. 25–27) — [9FM0 spec](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/a-level-l3-further-mathematics-specification.pdf)
- **1 Discrete probability distributions**
  - 1.1 Calculation of the mean and variance of discrete probability distributions, using E(X)=Σx P(X=x) and Var(X)=Σx²P(X=x)−µ². Extension of the expected value function to include E(g(X)). Questions may require using these to assess the suitability of models.
- **2 Poisson & binomial distributions**
  - 2.1 The Poisson distribution: model real-world situations and comment critically on appropriateness, and calculate probabilities (including cumulative ones) on the calculator. The additive property: if X~Po(λ) and Y~Po(µ) are independent, then X+Y~Po(λ+µ); rescaling the interval (e.g. per 5 minutes ~ Po(5λ)). No proofs.
  - 2.2 Mean and variance of B(n,p) (np, np(1−p)) and Po(λ) (λ, λ). Knowledge and use only; derivations not required.
  - 2.3 Poisson approximation to the binomial: when n is large and p is small, B(n,p) ≈ Po(np). No derivation.
- **3 Geometric and negative binomial distributions**
  - 3.1 Models leading to p(x)=p(1−p)^(x−1), x=1,2,…, and to the negative binomial p(x)=C(x−1,r−1)p^r(1−p)^(x−r), x=r,r+1,…
  - 3.2 Mean and variance of the geometric distribution: µ=1/p, σ²=(1−p)/p².
  - 3.3 Mean and variance of the negative binomial distribution: µ=r/p, σ²=r(1−p)/p².
- **4 Hypothesis testing**
  - 4.1 Hypothesis tests for the mean of a Poisson distribution (hypotheses in terms of µ or λ).
  - 4.2 Hypothesis tests for the parameter p of a geometric distribution.
- **5 Central Limit Theorem**
  - 5.1 Applications of the CLT to other distributions: X̄ ≈ N(µ, σ²/n) for large n. Applies to any distribution in A level Mathematics or FS1. No proofs.
- **6 Chi-squared tests**
  - 6.1 Goodness of fit tests and contingency tables, with null and alternative hypotheses. Σ(O−E)²/E as an approximate χ² statistic, and degrees of freedom.
  - Goodness of fit applies to the discrete uniform, binomial, Poisson and geometric distributions.
  - Candidates must find the degrees of freedom when parameters are estimated, and combine cells when Eᵢ<5.
  - Lengthy calculations will not be required. p-values may come from the calculator, or critical values from tables.
- **7 Probability generating functions**
  - 7.1 Definitions, derivations and applications. Use of the PGF for the negative binomial, geometric, binomial and Poisson distributions.
  - 7.2 Use of the PGF to find the mean and variance. Proofs of standard results may be required.
  - 7.3 PGF of a sum of independent random variables: G_{X+Y}(t)=G_X(t)×G_Y(t). Derivation not required.
- **8 Quality of tests**
  - 8.1 Type I and Type II errors, size and power of a test, and the power function.
  - Candidates calculate P(Type I) and P(Type II), and use errors and the power function to judge how effective a test is.
  - Questions may use any distribution in A level Mathematics or FS1.
- Spec footnote: "This paper is also the Paper 4 option 4B paper and will have the title 'Paper 4, Option 4B: Further Statistics 1'". The AO tables (Route B) list "Paper 4 Further Statistics 1", so FS1 can fill the Paper 4 slot when two Option 1 papers are taken. — [9FM0 spec](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/a-level-l3-further-mathematics-specification.pdf), pp. 27, 48–49

**Paper 4B: Further Statistics 2** (spec pp. 28–31) — [9FM0 spec](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/a-level-l3-further-mathematics-specification.pdf)
- **1 Linear regression**
  - 1.1 Least squares linear regression: the concept of residuals and of minimising the sum of squares of residuals. Calculate the y-on-x regression coefficients using standard formulae.
  - 1.2 Residuals: intuitive use to check the reasonableness of a linear fit, find possible outliers and refine models. Residual sum of squares RSS = S_yy − (S_xy)²/S_xx. Derivations not required.
- **2 Continuous probability distributions**
  - 2.1 Concept of a continuous random variable, linked to histograms and frequency polygons. The pdf, with P(a<X≤b)=∫f(x)dx, and the cdf F(x₀)=∫_{−∞}^{x₀}f(x)dx. The functions and calculus used are at the level of A level Mathematics and Further Mathematics.
  - 2.2 Relationship between pdf and cdf: f(x)=dF/dx.
  - 2.3 Mean and variance of continuous random variables, and E(g(X)). Mode, median and percentiles. Idea of skewness: describe it as positive, negative or zero, with justification.
  - 2.4 Continuous uniform (rectangular) distribution, including derivation of its mean, variance and cdf.
- **3 Correlation**
  - 3.1 Use of formulae to calculate the PMCC, including from summary statistics. Conditions for using the PMCC, and the effects of coding.
  - 3.2 Spearman's rank correlation coefficient: use and interpretation, with rs = 1 − 6Σd²/(n(n²−1)). Numerical questions involving ties may be set, and how to deal with ties is expected knowledge. The coefficient may be found on the calculator or by formula.
  - 3.3 Testing that a correlation is zero using Spearman's or the PMCC (H₀: ρ=0 or ρs=0), with tables of critical values. Candidates must know that the PMCC critical values require a bivariate normal population; formal verification is not required.
- **4 Combinations of random variables**
  - 4.1 Distribution of linear combinations of independent normal random variables: aX±bY ~ N(aµx±bµy, a²σx²+b²σy²). No proofs.
- **5 Estimation, confidence intervals and tests using a normal distribution**
  - 5.1 Concepts of standard error, estimator and bias. x̄ and s² (with divisor n−1) as unbiased estimates of the population parameters. Quality of estimators: compare them for unbiasedness and small variance.
  - 5.2 Concept and interpretation of a confidence interval, and its link with hypothesis tests.
  - 5.3 Confidence limits for a normal mean with known variance, using the standard error; no theoretical derivations.
  - 5.4 Hypothesis test for the difference between the means of two normal distributions with known variances, using a z statistic ~N(0,1).
  - 5.5 Large-sample results (CLT) for the case where population variances are unknown, using S_x², S_y² in place of the variances, ≈N(0,1).
- **6 Other hypothesis tests and confidence intervals**
  - 6.1 Hypothesis test and confidence interval for the variance of a normal distribution: (n−1)S²/σ² ~ χ²_{n−1}. χ² tables or calculator.
  - 6.2 Hypothesis test that two independent samples come from normal populations with equal variances: S₁²/S₂² ~ F_{n₁−1,n₂−1} under H₀. F tables or calculator.
- **7 Confidence intervals and tests using the t-distribution**
  - 7.1 Hypothesis test and confidence interval for the mean of a normal distribution with unknown variance: (X̄−µ)/(S/√n) ~ t_{n−1}. t-tables or calculator.
  - 7.2 Paired t-test.
  - 7.3 Hypothesis test and confidence interval for the difference between two means from independent normal distributions with equal but unknown variances: t with nx+ny−2 degrees of freedom. Pooled variance estimate s² = [(n₁−1)s₁²+(n₂−1)s₂²]/(n₁+n₂−2).

**Option rules.** Students take two options, either any two Option 1 papers (3A–3D) or a matching Option 1 and Option 2 pair, giving ten routes. 4B (FS2) therefore requires 3B (FS1). — [9FM0 spec](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/a-level-l3-further-mathematics-specification.pdf), p. 4

**AO weighting** (% of the A level) — [9FM0 spec](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/a-level-l3-further-mathematics-specification.pdf), Appendix, pp. 48–49
- FS1: AO1 11.67–13.00, AO2 5.00–6.33, AO3 6.33–7.67, total 23–27%.
- FS2: AO1 11.67–13.00, AO2 7.00–8.33, AO3 3.67–5.00.

### Inferences
- FS1 and FS2 together cover what the legacy (pre-2017) Edexcel S2, S3 and S4 units covered, plus PGFs, quality of tests, and geometric/negative binomial distributions.
- Content that was in legacy S2 and is now in A level Mathematics (normal approximation to the binomial, binomial hypothesis tests) is assumed knowledge. The spec repeatedly says "any of the distributions in A level Mathematics".
- The FS1 χ² goodness-of-fit list (discrete uniform, binomial, Poisson, geometric) does **not** include normal or continuous uniform fits. IAL S3 does include them (see Q2).

### Gaps
- The spec gives no per-topic mark allocation. The weighting of topics within a paper is only discoverable from past papers.

---

## Q1b. AS 8FM0 Further Statistics 1 (and AS FS2)

### Takeaway
AS FS1 is a reduced version of A level FS1 with three topics. It omits geometric/negative binomial, the CLT, PGFs and quality of tests, and adds the Poisson hypothesis test as 2.4. AS FS2 matches A level FS2 topics 1–3 only. Each AS option is half of Paper 2.

### Cited Findings
- 8FM0 spec Issue 5 (July 2025) is current. Its changes affect only Core Pure and Further Mechanics 2. — [8FM0 spec](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/as-l3-further-mathematics-specification.pdf), p. ii
- **Structure.** Paper 1 Core Pure and Paper 2 Further Mathematics Options (8FM0/2A–2K) are each 1 h 40 min, 80 marks and 50% of the qualification. Students take one of ten option pairs; the pairs containing statistics are 2B FP1+FS1, 2E FS1+FM1, 2F FS1+D1 and 2G FS1+FS2. — [8FM0 spec](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/as-l3-further-mathematics-specification.pdf), p. 4
- The 8FM0/23 Further Statistics 1 paper states: "The total mark for this part of the examination is 40". — [8FM0/23 May 2022 QP](https://qualifications.pearson.com/content/dam/pdf/A-Level/Mathematics/2017/Exam-materials/8fm0-23-que-20220524.pdf)
- **AS Further Statistics 1 content** — [8FM0 spec](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/as-l3-further-mathematics-specification.pdf), Paper 2 FS1 pages
  - 1.1 Mean and variance of discrete distributions, and E(g(X)), at the AS Maths/AS Further Maths level.
  - 2.1 Poisson distribution and its additive property.
  - 2.2 Mean and variance of the binomial and Poisson distributions.
  - 2.3 Poisson approximation to the binomial.
  - 2.4 Hypothesis tests for the mean of a Poisson distribution.
  - 3.1 χ² goodness of fit and contingency tables, with degrees of freedom. Goodness of fit applies to the discrete uniform, binomial and Poisson distributions (geometric is not included at AS). Cells are combined when E<5.
- **AS Further Statistics 2 content** — [8FM0 spec](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/as-l3-further-mathematics-specification.pdf)
  - 1.1–1.2 Least squares regression, residuals and RSS.
  - 2.1–2.4 Continuous random variables. The pdf is limited to the form kxⁿ (rational n≠−1), possibly piecewise. Covers mean, variance, E(g(X)), mode, median, percentiles, skewness and the continuous uniform.
  - 3.1–3.3 PMCC, Spearman (ties may be set), and tests that ρ or ρs = 0.
- The AS uses the same booklet. Its AS Further Mathematics statistics section lists the tables required for AS FM: binomial cdf, Poisson cdf, χ², PMCC and Spearman critical values, and random numbers (no t or F). — [GCE booklet](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/X_18pt_A4_Formulae_Booklet_and_Statistical_Tables.pdf), p. 38

### Inferences
- AS FS1 maps to A level FS1 topics 1, 2, 4.1 and 6. AS FS2 maps to A level FS2 topics 1–3.
- The paper reference 8FM0/23 (FS1) shows that each option is set as a separately coded 40-mark component inside Paper 2.

### Gaps
- The 8FM0 spec does not state a separate time per option, only 1 h 40 min for the whole of Paper 2. I did not confirm the AS FS2 component code (expected 8FM0/24 by analogy, but not verified).

---

## Q2. IAL S3 (WST03) and "S4 (WST04)": content, and which IAL statistics units count towards IAL Further Mathematics

### Takeaway
**There is no IAL S4 / WST04 unit.** The current (2018) IAL suite has only S1 (WST01), S2 (WST02) and S3 (WST03), and so did the 2013 suite. S1, S2 and S3 can all count towards IAL Further Mathematics. S3 can count **only** towards Further Mathematics, never IAL Mathematics. S3 covers combinations of normal random variables, sampling, normal-based estimation/CIs/tests (no t-distribution), χ² goodness of fit/contingency tables, and Spearman and correlation tests.

### Cited Findings
- **Units in the suite.** The 2018 IAL spec (Issue 3, April 2019) lists statistics units S1 WST01/01, S2 WST02/01 and S3 WST03/01 only. — [IAL spec](https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/Mathematics/2018/Specification-and-Sample-Assessment/international-a-level-maths-spec.pdf), pp. 7–8
- The 2013 IAL spec also lists only S1 WST01, S2 WST02 and S3 WST03. — [IAL 2013 spec](https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/Mathematics/2013/Specification%20and%20sample%20assessments/9781446925201_IAL_Maths_Iss3.pdf), unit table
- The IAL formulae booklet cover reads "Statistics S1 – S3". — [IAL booklet (third-party copy)](https://media.publit.io/file/formularsheetas/alevelmaths/IAL-Mathematics-Formula-Book.pdf)
- **Unit format.** Each unit is 1 h 30 min and 75 marks, worth 33⅓% of an IAS and 16⅔% of an IAL. S1 and S2 are available in January, June and October; S3 in January and June only. S3 was first assessed in June 2020. — [IAL spec](https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/Mathematics/2018/Specification-and-Sample-Assessment/international-a-level-maths-spec.pdf), pp. 7–9
- **Counting rules.** Each rule below is from [IAL spec](https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/Mathematics/2018/Specification-and-Sample-Assessment/international-a-level-maths-spec.pdf), pp. 9–10:
  - IAS Further Mathematics: FP1 compulsory plus two from FP2, FP3, M1, M2, M3, S1, S2, S3, D1.
  - IAL Further Mathematics: FP1 and either FP2 or FP3 compulsory; the other units come from FP2, FP3, M1, M2, M3, S1, S2, S3, D1.
  - IAL Mathematics: P1–P4 plus one optional pair (M1+S1, M1+D1, M1+M2, S1+D1 or S1+S2). S3 is not an option.
  - A unit result cannot be reused: Maths plus Further Maths together need 12 different units.
- The S3 unit page is headed "Optional unit for IAS Further Mathematics / Optional unit for IAL Further Mathematics". S2 is headed "Optional unit for IAS Further Mathematics / Optional unit for IAL Mathematics and Further Mathematics". — [IAL spec](https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/Mathematics/2018/Specification-and-Sample-Assessment/international-a-level-maths-spec.pdf), S2 and S3 pages
- On 16 Nov 2026 the IAL qualification page showed only the 2018 spec (first teaching Sept 2018) and no notice of a replacement. — [Pearson IAL Maths page](https://qualifications.pearson.com/en/qualifications/edexcel-international-advanced-levels/mathematics-2018.html)

**Unit S3: Statistics 3 (WST03/01) content** (spec section S3.3) — [IAL spec](https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/Mathematics/2018/Specification-and-Sample-Assessment/international-a-level-maths-spec.pdf)
- Prerequisites: "A knowledge of the specifications for S1 and S2, and their prerequisites and associated formulae, is assumed and may be tested."
- **1 Combinations of random variables**
  - 1.1 Linear combinations of independent normal random variables: aX±bY ~ N(aµx±bµy, a²σx²+b²σy²). No proofs.
- **2 Sampling**
  - 2.1 Methods for collecting data: simple random sampling and the use of random numbers.
  - 2.2 Stratified, systematic and quota sampling: when each might be used, and their advantages and disadvantages.
- **3 Estimation, confidence intervals and tests**
  - 3.1 Standard error, estimator and bias. x̄ and s² (with divisor n−1) as unbiased estimates.
  - 3.2 Distribution of X̄: mean µ, variance σ²/n. If X~N(µ,σ²) then X̄~N(µ,σ²/n). No proofs.
  - 3.3 Concept and interpretation of a confidence interval, and its link with hypothesis tests.
  - 3.4 Confidence limits for a normal mean with known variance.
  - 3.5 Hypothesis tests for the mean of a normal distribution with known variance, using (X̄−µ)/(σ/√n) ~ N(0,1).
  - 3.6 CLT to extend tests and CIs to non-normal samples, and large-sample results when the variance is unknown: (X̄−µ)/(S/√n) treated as N(0,1). "A knowledge of the t-distribution is not required."
  - 3.7 Test for the difference between two normal means with known variances.
  - 3.8 Large-sample extension of 3.7 to unknown variances. t-distribution not required.
- **4 Goodness of fit and contingency tables**
  - 4.1 Null and alternative hypotheses, with Σ(O−E)²/E as an approximate χ² statistic. Applies to the discrete uniform, binomial, **normal**, Poisson and **continuous uniform** distributions. No lengthy calculations.
  - 4.2 Degrees of freedom, including when parameters are estimated. Cells are combined when Eᵢ<5. "Yates' correction is not required."
- **5 Regression and correlation**
  - 5.1 Spearman's rank correlation coefficient: use, interpretation and limitations. "Numerical questions involving ties will not be set. Some understanding of how to deal with ties will be expected."
  - 5.2 Testing the hypothesis that a correlation is zero, using tables for Spearman's and product moment coefficients.
- Formula students must know for S3 (not in the booklet): aX ± bY ~ N(aµx ± bµy, a²σx² + b²σy²) for independent normal X, Y. — [IAL spec](https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/Mathematics/2018/Specification-and-Sample-Assessment/international-a-level-maths-spec.pdf), S3.2

**Unit S2 (WST02) content, for comparison** (it also counts towards IAL Further Mathematics) — [IAL spec](https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/Mathematics/2018/Specification-and-Sample-Assessment/international-a-level-maths-spec.pdf)
- 1.1–1.3 Binomial and Poisson: modelling, additive property, mean and variance, Poisson approximation to the binomial.
- 2.1–2.5 Continuous random variables: pdf limited to simple polynomials (possibly piecewise), cdf, f=dF/dx, mean, variance, mode, median and quartiles.
- 3.1–3.2 Continuous uniform (with derivations), and normal approximations to the binomial and Poisson with continuity correction.
- 4.1–4.6 Hypothesis tests: population, census and sample; sampling unit and frame; statistic and sampling distribution; null and alternative hypotheses; critical region; one- and two-tailed tests; tests for binomial p and Poisson mean.
- Formulae to remember: P(a<X≤b)=∫f(x)dx and f(x)=dF/dx.

### Inferences
- "S4" most likely comes from the legacy UK Edexcel GCE (pre-2017) unit S4. That unit held the t-test, F-test, χ² for variance, paired t and quality-of-tests content that now sits in 9FM0 FS1/FS2. In the IAL suite, that content (t, F, χ² intervals for variance, PGFs, geometric and negative binomial, Type II errors and power) is **not examined at all**.
- An IAL Further Mathematics student can take at most S1+S2+S3 as statistics. S1 and S2 can each count towards either IAL Mathematics or IAL Further Mathematics, but not both.

### Gaps
- I did not establish whether Pearson has announced a successor IAL Maths specification (some third-party sites reference unit codes like "WST11/WST12"). Neither the Pearson qualification page nor the spec showed one on 16 Nov 2026, so treat that as unconfirmed.

---

## Q3. Formula booklets and statistical tables: what is given, and what must be memorised

### Takeaway
The GCE booklet (one booklet for all of 8MA0/9MA0/8FM0/9FM0) gives A level FM students most distribution formulae (including PGFs and the t, χ² and F sampling results) plus all tables, including t and F. The 9FM0 spec's Appendix 1 statistics memorisation list is short. The IAL booklet has no t or F tables, and S3 students must memorise the linear-combination-of-normals result.

### Cited Findings

**GCE booklet: "A Level Further Mathematics – Statistics" section (pp. 53–63)** — [GCE booklet](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/X_18pt_A4_Formulae_Booklet_and_Statistical_Tables.pdf)
- Discrete: E(X), Var(X), E(g(X)). The PGF G_X(t)=E(t^X), E(X)=G′(1), Var(X)=G″(1)+G′(1)−[G′(1)]², and G_{X+Y}=G_X·G_Y for independent X, Y.
- Table of standard discrete distributions giving P(X=x), mean, variance and PGF for:
  - binomial: (1−p+pt)ⁿ
  - Poisson: e^{λ(t−1)}
  - geometric on 1,2,…: pt/(1−(1−p)t)
  - negative binomial on r,r+1,…: [pt/(1−(1−p)t)]^r
- Continuous: E(X), Var(X), E(g(X)) and cdf. Normal and continuous uniform pdf, mean and variance: (a+b)/2 and (b−a)²/12.
- Correlation and regression: Sxx, Syy, Sxy, PMCC r, regression coefficient b, the line y=a+bx, RSS = Syy − Sxy²/Sxx = Syy(1−r²), and Spearman's rs.
- Expectation algebra: E(XY)=E(X)E(Y) and Var(aX±bY)=a²Var(X)+b²Var(Y) for independent X, Y.
- Sampling distributions:
  - X̄ unbiased, with Var σ²/n; S² unbiased.
  - (X̄−µ)/(σ/√n) ~ N(0,1), and the two-sample z statistic.
  - (n−1)S²/σ² ~ χ²_{n−1}.
  - (X̄−µ)/(S/√n) ~ t_{n−1}, "also valid in matched-pairs situations".
  - (Sx²/σx²)/(Sy²/σy²) ~ F_{nx−1,ny−1}.
  - Pooled two-sample t with Sp² = [(nx−1)Sx²+(ny−1)Sy²]/(nx+ny−2), with nx+ny−2 degrees of freedom.
- Non-parametric: Σ(Oᵢ−Eᵢ)²/Eᵢ ~ χ²_ν.
- **Tables required for A level Further Mathematics** (booklet p. 63):
  - Binomial cumulative distribution function (pp. 66–100)
  - Poisson cumulative distribution function (pp. 102–109)
  - Percentage points of the χ² distribution (pp. 110–115)
  - Critical values for correlation coefficients, PMCC and Spearman's (pp. 116–119)
  - Random numbers (pp. 120–121)
  - Percentage points of Student's t distribution (pp. 122–124)
  - Percentage points of the F distribution (pp. 125–132)
- The booklet also contains Percentage Points of the Normal Distribution (p. 101), which is listed among the A level Mathematics tables.
- **Tables required for AS Further Mathematics** (p. 38): binomial cdf, Poisson cdf, χ², correlation critical values and random numbers.
- Booklet introduction: "Students sitting AS or A Level Further Mathematics papers may be required to use the formulae that were introduced in AS or A Level Mathematics papers."

**9FM0 Appendix 1, "Formulae which students are expected to know"** (not in the booklet) — [9FM0 spec](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/a-level-l3-further-mathematics-specification.pdf), Appendix 1, pp. 61–66
- The statistics heading lists only:
  - the mean of a data set, x̄ = Σx/n = Σfx/Σf
  - the standard normal variable Z = (X−µ)/σ where X~N(µ,σ²)
- The rest of Appendix 1 is pure maths and mechanics.
- Spec content rows also give formulae that do not appear in the booklet, and candidates must know them:
  - geometric and negative binomial means and variances (these are in the booklet's PGF table)
  - B(n,p) and Po(λ) means and variances
  - the Poisson additive property
  - aX±bY for normals (FS2 4.1; the booklet gives only the Var(aX±bY) expectation algebra, not the normal distribution result)
  - the two-sample large-sample z with S² (FS2 5.5)
- The notation appendix includes Geo(p), G_X(t), χ²_ν, t_n and F_{ν1,ν2} (items 11.33–11.37). — [9FM0 spec](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/a-level-l3-further-mathematics-specification.pdf), Appendix notation section 11

**IAL booklet (Issue 2, Jan 2021), arranged by unit** — [IAL booklet (third-party copy)](https://media.publit.io/file/formularsheetas/alevelmaths/IAL-Mathematics-Formula-Book.pdf)
- S1 (p. 14 on): probability, discrete and continuous distributions, correlation and regression, the Normal Distribution Function table and Percentage Points of the Normal Distribution.
- S2 (p. 18 on): discrete and continuous distributions, binomial cdf tables and Poisson cdf tables.
- S3 (p. 25 on): "Candidates sitting S3 may also require those formulae listed under Statistics S1 and S2, and Pure Mathematics P1, P2, P3 and P4". It gives:
  - expectation algebra (E(XY), Var(aX±bY))
  - sampling distributions (X̄ and S² unbiased, one- and two-sample z)
  - Spearman's rs
  - Σ(O−E)²/E ~ χ²_ν
- S3 tables: Percentage Points of the χ² Distribution (p. 26), Critical Values for Correlation Coefficients (p. 27) and Random Numbers (p. 28).
- **No t or F tables.** This is consistent with the spec's statement "A knowledge of the t-distribution is not required."

### Inferences
- A 9FM0 FS2 candidate is given the t, χ² and F test statistics. What they must supply from understanding is when each applies, the degrees of freedom, and the confidence-interval constructions.
- An IAL S3 candidate must memorise the normal linear-combination result.
- In practice, both specs state that calculators may be used to find p-values and critical values for χ², t and F (9FM0) or that tables are used (IAL).

### Gaps
- The standard-print 9FM0 booklet URL was not found. The 18pt version has the same booklet code (X54458A), but I could not rule out a later reprint of the standard version with minor changes.
- The IAL booklet was read from a third-party copy, because no official Pearson URL was found.

---

## Q4. Exam structure: paper length and marks

### Takeaway
9FM0: 3B and 4B are each 1 h 30 min, 75 marks, 25% of the A level. 8FM0: FS1 is a 40-mark component of the 80-mark, 1 h 40 min Paper 2. IAL S3 (and S1, S2): 1 h 30 min, 75 marks, 16⅔% of the IAL.

### Cited Findings
- **9FM0 options.** Each optional paper is "Written examination: 1 hour and 30 minutes, 25% of the qualification, 75 marks". All questions are compulsory, calculators are allowed and the booklet is provided. First assessment May/June 2019. The papers assess synopticity. — [9FM0 spec](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/a-level-l3-further-mathematics-specification.pdf), pp. 4–5, 20
- The Oct 2020 9FM0/3B paper confirms 1 h 30 min and "The total mark for this paper is 75" (7 questions). — [9FM0/3B Oct 2020 QP](https://qualifications.pearson.com/content/dam/pdf/A-Level/Mathematics/2017/Exam-materials/9FM0_3B_que_20201017.pdf)
- **9FM0 overall.** Core Pure 1 and Core Pure 2 (9FM0/01, 9FM0/02) are compulsory, plus two optional papers. — [9FM0 spec](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/a-level-l3-further-mathematics-specification.pdf), Appendix 9, p. 85
- **8FM0.** Paper 2 options: 1 h 40 min, 80 marks, 50%. The FS1 part (8FM0/23) is 40 marks. — [8FM0 spec](https://qualifications.pearson.com/content/dam/pdf/A%20Level/Mathematics/2017/specification-and-sample-assesment/as-l3-further-mathematics-specification.pdf); [8FM0/23 QP](https://qualifications.pearson.com/content/dam/pdf/A-Level/Mathematics/2017/Exam-materials/8fm0-23-que-20220524.pdf)
- **IAL S3.** 1 h 30 min, 75 marks, all questions compulsory, calculators allowed, booklet provided. First assessment June 2020; sat in January and June. — [IAL spec](https://qualifications.pearson.com/content/dam/pdf/International%20Advanced%20Level/Mathematics/2018/Specification-and-Sample-Assessment/international-a-level-maths-spec.pdf), S3.2

### Inferences
- The IAL is modular: each unit is a separate sitting, and units can be sat in January, June or October. The 9FM0 is linear, with all papers in the May/June series (an October series has existed for some years, e.g. the Oct 2020 paper above).

### Gaps
- None material for the structure question.
