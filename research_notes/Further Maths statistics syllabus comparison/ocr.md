# OCR A Level Further Mathematics statistics components: OCR FM A (H245 Y542, AS H235 Y532) and OCR FM B (MEI) (H645 Y422 Statistics Major, Y432 Statistics Minor; AS H635 Y412)

Research date: 16 Nov 2026. All content below was taken from the current OCR PDFs, downloaded directly from ocr.org.uk and converted with pdftotext. Spec versions in force:
- H245 A Level FM A spec, **Version 2 (October 2025)**: https://www.ocr.org.uk/Images/308752-specification-accredited-a-level-gce-further-mathematics-a-h245.pdf
- H235 AS FM A spec, **Version 2 (October 2025)**: https://www.ocr.org.uk/Images/308750-specification-accredited-as-level-gce-further-mathematics-a-h235.pdf
- H645 A Level FM B (MEI) spec, **Version 2.1 (March 2026)**: https://www.ocr.org.uk/Images/308768-specification-accredited-a-level-gce-further-mathematics-b-mei-h645.pdf
- H635 AS FM B (MEI) spec, **Version 2 (October 2025)**: https://www.ocr.org.uk/Images/308764-specification-accredited-as-level-gce-further-mathematics-b-mei-h635.pdf
- H245 Formulae Booklet (© OCR 2022): https://www.ocr.org.uk/Images/308765-a-level-further-mathematics-a-formulae-booklet.pdf
- H235 Formulae Booklet (© OCR 2022): https://www.ocr.org.uk/Images/308766-as-level-further-mathematics-a-formulae-booklet.pdf
- H635/H645 MEI Formulae Booklet (© OCR 2020, one booklet for AS and A level): https://www.ocr.org.uk/Images/752530-formulae-booklet.pdf (same file as https://www.ocr.org.uk/Images/667004-formulae-booklet.pdf)
- Qualification "assessment" pages that list the booklets: https://www.ocr.org.uk/qualifications/as-and-a-level/further-mathematics-a-h235-h245-from-2017/assessment/ and https://www.ocr.org.uk/qualifications/as-and-a-level/further-mathematics-b-mei-h635-h645-from-2017/assessment/

## Q1. Exact sub-topic content lists (spec reference codes)

### Takeaway
OCR FM A Statistics (Y542) has nine sections, 5.01–5.09. The AS paper (Y532) is the "Stage 1" subset: 5.01, 5.02, 5.06a/b/d, 5.08 and 5.09. Y542 adds continuous random variables, linear combinations, the CLT with z-tests and z-confidence intervals, fitting other distributions with chi-squared, and non-parametric tests (sign test, Wilcoxon signed-rank and rank-sum). MEI Statistics Major (Y422) has (a) content, which is identical to Statistics Minor Y432 and AS Statistics a Y412: sampling, discrete random variables, bivariate data, chi-squared. Its (b) content covers continuous random variables, inference (CLT, z- and t-confidence intervals, z-, t- and Wilcoxon single-sample tests) and spreadsheet simulation. None of these components contains PGFs, Markov chains, the gamma or beta distributions, or a two-sample t-test.

### Cited Findings

**OCR FM A (H245) Y542 Statistics: full spec-reference list.** Source for all items: [H245 spec v2, section 2d, pp.36–49](https://www.ocr.org.uk/Images/308752-specification-accredited-a-level-gce-further-mathematics-a-h245.pdf). "Stage 1" means the content shared with AS H235; "Stage 2" means A level only. Stage membership was confirmed by checking which refs appear in the [H235 spec section 2d](https://www.ocr.org.uk/Images/308750-specification-accredited-as-level-gce-further-mathematics-a-h235.pdf). The H235 statistics section contains exactly 5.01a–b, 5.02a–n, 5.06a, 5.06b, 5.06d, 5.08a–g and 5.09a–e.

- **5.01 Probability** (Stage 1)
  - 5.01a: probabilities by calculation using permutations and combinations, with the notation nPr and nCr.
  - 5.01b: probabilities in contexts of selections and arrangements. Examples are 3 vowels and 2 consonants from 'CALCULATOR', and arrangements in a line with repetition (e.g. 'STRAIT'→'ARTIST') or restriction (consonants adjacent or not adjacent in 'TRAITS'). Arrangements are in a line only.
- **5.02 Discrete Random Variables** (Stage 1)
  - 5.02a: general discrete distributions, using and constructing tables. Any non-standard distribution will be finite.
  - 5.02b: E(X)=Σxp and Var(X)=Σx²p−μ². Proof excluded.
  - 5.02c: effect of linear coding on the mean and variance.
  - 5.02d: binomial mean np and variance np(1−p). Proof excluded.
  - 5.02e: discrete uniform U(n) on [1, n]: conditions, probabilities, mean and variance.
  - 5.02f–h: geometric Geo(p), where X is the number of trials up to and including the first success. Includes P(X=x)=(1−p)^(x−1)p, P(X>x)=(1−p)^x, mean 1/p and variance (1−p)/p². Proof excluded.
  - 5.02i–n: Poisson Po(λ):
    - informal relevance to random events, and use as a model;
    - the formula, and calculator probabilities;
    - **Poisson approximation to the binomial is excluded**;
    - modelling conditions explained in context;
    - mean = variance = λ;
    - the sum of independent Poissons is Poisson.
- **5.03 Continuous Random Variables** (Stage 2)
  - 5.03a: the concept of a CRV, p.d.f. and c.d.f. Includes the normal, continuous uniform and **exponential** distributions, an informal link between the exponential and Poisson distributions, and knowing the mean and variance of the continuous uniform and exponential distributions.
  - 5.03b: piecewise p.d.f.s, ∫f=1.
  - 5.03c: E(X) and Var(X) by integration.
  - 5.03d: E(g(X))=∫g(x)f(x)dx.
  - 5.03e: c.d.f. (including piecewise), F(x)=∫f(t)dt.
  - 5.03f: relationship between the p.d.f. and c.d.f.; median, quartiles and percentiles.
  - 5.03g: **c.d.f. of related variables**, e.g. Y = X³.
- **5.04 Linear Combinations of Random Variables** (Stage 2)
  - 5.04a: E(aX+bY+c) and Var(aX+bY+c) for independent X and Y.
  - 5.04b: if X is normal then aX+b is normal; aX+bY is normal for independent normal X and Y.
- **5.05 Hypothesis Tests and Confidence Intervals** (Stage 2)
  - 5.05a: distribution of X̄ and the **CLT**: E(X̄)=μ, Var(X̄)=σ²/n, approximately normal for n > about 25. Proof excluded.
  - 5.05b: unbiased estimates of the mean and variance. An informal understanding of "unbiased" is enough.
  - 5.05c: **normal (z) hypothesis test for a population mean** in three cases: a normal population with known or assumed variance; a large sample from any population with known variance; a large sample with unknown variance.
  - 5.05d: **z confidence intervals** for the mean in the same cases.
  - **No t-distribution** appears anywhere in Y542.
- **5.06 Chi-squared Tests**
  - 5.06a (Stage 1): χ² test for independence in a contingency table. Combine cells so that each expected frequency is ≥5, and use **Yates' correction for 2×2 tables**. Includes expected frequencies and contributions.
  - 5.06b (Stage 1): fit a distribution given by a ratio, a proportion or the discrete uniform.
  - 5.06c (**Stage 2**): extend to fitting other known or given discrete and continuous distributions.
  - 5.06d (Stage 1): goodness-of-fit test with the correct degrees of freedom, combining adjacent classes.
- **5.07 Non-parametric tests** (Stage 2)
  - 5.07a: what a non-parametric test is, and selecting an appropriate test.
  - 5.07b: basis of the **sign test, Wilcoxon signed-rank test, and Wilcoxon rank-sum (Mann-Whitney U) test**. Tables of T and W are provided, and the notation W+ and W− is used.
  - 5.07c: single-sample sign test and single-sample Wilcoxon signed-rank test for a population median. Observations equal to the hypothesised median are excluded.
  - 5.07d: the difference between paired-sample and two-sample tests.
  - 5.07e: paired-sample sign test, Wilcoxon matched-pairs signed-rank test, and Wilcoxon rank-sum test for unpaired samples. **Tied ranks are excluded.**
  - 5.07f: **normal approximations for large samples**: T ~ N(n(n+1)/4, n(n+1)(2n+1)/24) and W ~ N(m(m+n+1)/2, mn(m+n+1)/12), with continuity corrections.
- **5.08 Correlation** (Stage 1)
  - 5.08a: pmcc from raw or summarised data by calculator.
  - 5.08b: pmcc is unaffected by linear coding.
  - 5.08c: pmcc measures closeness to a straight line.
  - 5.08d: pmcc hypothesis test using a critical value, or a p-value and tables. Assumes a bivariate normal distribution.
  - 5.08e: Spearman's rs for at most 10 pairs. Includes when rank correlation is appropriate. **Tied ranks are excluded.**
  - 5.08f: Spearman test for association (non-parametric).
  - 5.08g: choosing between pmcc and Spearman; linear correlation versus association.
- **5.09 Linear Regression** (Stage 1)
  - 5.09a: independent (controlled) versus dependent (response) variables.
  - 5.09b: least squares concept.
  - 5.09c: regression line of y on x from raw or summarised data. **x on y is excluded when x is independent.**
  - 5.09d: effect of linear coding on the regression line.
  - 5.09e: estimating y and interpreting the uncertainty.
- Hypothesis-test conventions (both H245 and H235): hypotheses are stated in terms of parameters, with the meaning of symbols defined. Conclusions must be non-assertive, e.g. "There is evidence at the 5% level to reject H0. It is likely that…". "Accept H0. Plants … have the same height" is given as an incorrect conclusion. — [H245 spec 2d](https://www.ocr.org.uk/Images/308752-specification-accredited-a-level-gce-further-mathematics-a-h245.pdf)
- "Use of technology" suggestions in H245 2d are advisory, not spec refs: spreadsheets for tables and tests, random number generators to simulate coins and dice, simulations to investigate the CLT, and exploring data sets. "No particular data set is expected to be studied, and there will not be any pre-release data." — [H245 spec 2d](https://www.ocr.org.uk/Images/308752-specification-accredited-a-level-gce-further-mathematics-a-h245.pdf)
- Assumed knowledge: GCSE, all of A Level Mathematics (H240) and Pure Core (Y540/Y541). Several refs cross-reference H240, e.g. 2.03 for probability, 2.04b/c for binomial and 2.04e–g for normal. — [H245 spec 2d](https://www.ocr.org.uk/Images/308752-specification-accredited-a-level-gce-further-mathematics-a-h245.pdf)
- AS Y532 introduction: "This area covers probability involving combinatorics, probability distributions for discrete random variables, chi-squared tests, correlation and regression." Assumed knowledge is AS Level Mathematics plus Y531 Pure Core. — [H235 spec 2d](https://www.ocr.org.uk/Images/308750-specification-accredited-as-level-gce-further-mathematics-a-h235.pdf)
- The only statistics-specific spec change in recent versions was v1.5 (April 2022): "Correction of minor typographical errors" in 2d, plus changes to 5d. v2 (Oct 2025) was a rebrand to "Cambridge OCR" with no content change. — [H245 spec, Summary of updates](https://www.ocr.org.uk/Images/308752-specification-accredited-a-level-gce-further-mathematics-a-h245.pdf)

**OCR FM B (MEI) (H645) Y422 Statistics Major: full spec-reference list.** Source: [H645 spec v2.1, section 2e, pp.51–70](https://www.ocr.org.uk/Images/308768-specification-accredited-a-level-gce-further-mathematics-b-mei-h645.pdf). Ref prefixes are as follows: Sx is sampling, SR is random variables, Sb is bivariate data, SH is hypothesis tests, SI is inference and SZ is simulation. (a) is unshaded content, which is the same as Y432 and AS Y412. (b) is A level Major only.

- **Sampling (a)**
  - Sx1: importance of sample size in experimental design, linked informally to effect size.
  - Sx2: why sampling is necessary, and desirable features of a sample (unbiased, representative).
  - Sx3: advantage of a random sample for inference.
- **Discrete random variables (a)**
  - SR1: probability functions given algebraically or in tables. Calculate probabilities, and draw and interpret graphs. The variable is finite except for the Poisson and geometric distributions.
  - SR2: E(X).
  - SR3: Var(X)=E(X²)−μ².
  - SR4: E(a+bX).
  - SR5: Var(a+bX)=b²Var(X).
  - SR6: E and Var of linear combinations of **independent** RVs, e.g. Var(aX ± bY)=a²Var(X)+b²Var(Y). Proofs excluded.
  - SR7–SR9: discrete uniform on any set of values, e.g. {4,…,9}. Mean (n+1)/2 and variance (n²−1)/12 for {1,…,n} are given, **but derivations may be asked for**.
  - SR10: binomial. Know μ=np and σ²=np(1−p), and **prove these results in particular cases** (as a sum of Bernoulli variables).
  - SR11: Poisson model conditions in context. Mean ≈ variance in the data is a check.
  - SR12: situations where both the Poisson and binomial apply (n large, p small). **Formal criteria, and the Poisson as a numerical approximation to the binomial, are excluded.**
  - SR13: Poisson probabilities by calculator, including cumulative.
  - SR14: Poisson mean and variance λ. Proof excluded.
  - SR15: the sum of independent Poissons is Poisson. Proof excluded.
  - SR16: geometric Geo(p) as the number of trials up to and including the first success, and its link with the binomial. The "number of failures" definition is excluded.
  - SR17: P(X=r)=(1−p)^(r−1)p and P(X>r)=(1−p)^r.
  - SR18: geometric mean 1/p and variance (1−p)/p². Proof excluded.
- **Bivariate data (a)**: the spec explains "random on non-random" (Case A) versus "random on random" (Case B).
  - Sb1: bivariate data and axis conventions.
  - Sb2: interpret scatter diagrams and outliers.
  - Sb3: interpret software scatter diagrams, trendlines and r or r².
  - Sb4: pmcc from raw data (calculator) or summary statistics.
  - Sb5: when a pmcc test is valid: random on random, bivariate Normal, elliptical scatter.
  - Sb6: pmcc hypothesis test of H0 "no correlation", using tables or a p-value from software, one- or two-sided.
  - Sb7: **pmcc as an effect size**. Any formal rules, e.g. Cohen's, are given.
  - Sb8: Spearman's rs from raw data or summary statistics. **Tied ranks are excluded.**
  - Sb9: Spearman test of H0 "no association", using tables or software.
  - Sb10: choose r, rs or neither (monotonic relationship; ranking loses information).
  - Sb11: least-squares regression line for a random variable on a non-random variable, from raw data or summary statistics. Derivation is excluded.
  - Sb12: estimation, interpolation versus extrapolation, and **residuals** (calculate and interpret).
  - Sb13: **both regression lines, y on x and x on y**, for random-on-random data.
  - Sb14: informal checking of fit by scatter diagram or r².
  - Sb15: the relationship between the two lines. Both pass through (x̄, ȳ), and which to use depends on what is estimated.
- **Chi-squared tests (a)**
  - Sb16: interpret contingency tables.
  - SH1: χ² test on a contingency table with H0 "no association" or "independent". Calculate degrees of freedom. **Yates' correction is not expected**, but its appropriate use will not be penalised.
  - SH2: interpret results using tables or a software p-value, including the individual cell contributions.
  - SH3: χ² goodness of fit for a **uniform, binomial or Poisson** model. Learners should be aware that cells are combined, but "will not have to make such decisions in examination questions".
  - SH4: interpret goodness-of-fit results, including from software.
- **Continuous random variables (b)**
  - SR19: a simple CRV as a model, including the continuous uniform (rectangular) and Normal distributions. Learners should be aware of t_n, χ²_n and the **exponential distribution, but "knowledge of these is not expected and any necessary details will be provided"**. Mixed discrete and continuous distributions are excluded.
  - SR20: pdf meaning, including piecewise pdfs. Write down the integral, and a calculator may evaluate it.
  - SR21: properties f≥0 and ∫f=1, and sketching. Improper integrals are excluded.
  - SR22: mean and variance from a pdf, with integrations over finite domains. Continuous uniform mean and variance are given, but derivations may be required.
  - SR23: mode (where it exists) and median from a pdf.
  - SR24: cdf from a pdf, and sketching.
  - SR25: pdf from a cdf, f=F′.
  - SR26: median and percentiles from a cdf.
  - SR27: expectation algebra for linear combinations.
  - SR28: Normal distribution as a model, with probabilities by calculator. Marked †, meaning it overlaps or depends on non-AS A Level Maths content.
  - SR29: linear combinations of independent Normals, including more than two.
  - SR30: Normal as a model and as an approximation via the CLT.
  - SR31: **interpret a Normal probability plot and Kolmogorov-Smirnov software output (p-value)**. A χ² goodness-of-fit test for the Normal is excluded, as are K-S calculations.
  - SR32: Normal used in confidence intervals.
- **Inference (b)**
  - SI1: point estimate of the mean.
  - SI2: sample variance s² with divisor n−1.
  - SI3: sampling distribution of the mean: mean μ, variance σ²/n.
  - SI4: **standard error of the mean**.
  - SI5: X̄ is Normal if the parent distribution is Normal.
  - SI6: **CLT** (n > 30 as a rule of thumb), with continuity correction where appropriate. Also applied to the sum of n i.i.d. RVs. A formal statement or derivation is excluded.
  - SI7: meaning of a confidence interval (long-run proportion).
  - SI8: factors affecting the width.
  - SI9: **CI for a single mean using the Normal or t distribution**. Use z for a large sample, or a small Normal sample with known σ. Use t with n−1 degrees of freedom for a small Normal sample with unknown σ.
  - SI10: when samples are paired.
  - SI11: **paired-sample CI for the difference in means (z or t)**. A known population variance for the differences is not examined.
  - SI12: interpret CIs from software, including unfamiliar distributions, with details given.
  - SI13: use a CI to make a decision about a hypothesised value.
  - Asymmetric and one-sided CIs are excluded.
  - SH5: **Wilcoxon signed rank test for a single population median**. It is non-parametric and assumes a symmetric distribution. W+ and W− notation is used. H0 is that the median equals a value; one- or two-sided.
  - SH6: **hypothesis test for a single mean using the Normal or t distribution**, with the same rules as SI9.
- **Simulation (b)**
  - SZ1: spreadsheets can simulate probability distributions; do so for the discrete uniform, continuous uniform and Normal.
  - SZ2: use simulation to approximate distributions and estimate probabilities where the theory is hard. Examples include P(2X−Y>0), investigating the CLT, a 10-dice total >50, and train waiting times. Learners **interpret spreadsheet output**.

**MEI Y432 Statistics Minor.** "This is the same content as the unshaded sections, labelled (a), of Statistics Major (Y422)", i.e. Sx1–Sx3, SR1–SR18, Sb1–Sb16 and SH1–SH4. Assumed knowledge is A Level Maths plus Core Pure Y420. Learners may not enter both Y422 and Y432. — [H645 spec 2g, p.80](https://www.ocr.org.uk/Images/308768-specification-accredited-a-level-gce-further-mathematics-b-mei-h645.pdf)

**MEI AS H635 Y412 Statistics a.** "This option comprises the same content as Statistics Minor (Y432) and the same content as the sections labelled (a) in Statistics Major (Y422)". Its assumed knowledge is **AS** Level Maths plus Core Pure Y410. — [H635 spec 2e, p.32](https://www.ocr.org.uk/Images/308764-specification-accredited-as-level-gce-further-mathematics-b-mei-h635.pdf)

**MEI calculators and technology.** The Y422 calculator must compute means, SDs, correlation coefficients, regression lines and binomial, Poisson and Normal probabilities, including cumulative. Learners should gain experience of software for hypothesis tests, CIs and simulation, and "in the examination learners will be assessed on the interpretation of output from such software". The Y432 calculator list omits the Normal. — [H645 spec 2e/2g](https://www.ocr.org.uk/Images/308768-specification-accredited-a-level-gce-further-mathematics-b-mei-h645.pdf)

### Inferences
- Topics on the requested checklist that are **absent** from all four components (searched in the extracted text): PGFs, Markov chains, the negative binomial, gamma and beta distributions, a two-sample t-test, F-tests, and confidence intervals for proportions. The H245 permutations/combinations topic (5.01) has **no MEI equivalent** in Y422/Y432.
- Key differences between OCR A Y542 and MEI Y422:
  - **OCR A has:** sign tests; the Wilcoxon rank-sum (Mann-Whitney) test with normal approximations; the exponential distribution as examinable; c.d.f.s of related variables (Y=g(X)); χ² fitting of continuous distributions; Yates' correction required; and permutations and combinations.
  - **MEI Major has:** the **t-distribution** (CIs and tests); paired CIs; Normal probability plots; Kolmogorov-Smirnov output; effect size; residuals; the x-on-y regression line; sampling; and explicit **simulation** content (SZ1–2).
  - **Both have:** discrete uniform, binomial (mean and variance), geometric, Poisson, pmcc and Spearman tests, χ² independence and goodness of fit, CRVs (pdf and cdf), linear combinations, the CLT, and Wilcoxon signed-rank for a single median.
- OCR A's CLT rule of thumb is n > about 25 (5.05a); MEI's is n > 30 (SI6). This is a minor difference that teaching materials should reflect.

### Gaps
- I did not cross-check the MEI website (mei.org.uk) scheme of work in this pass, so there is no secondary confirmation of the MEI content beyond the OCR spec itself. Since OCR publishes the spec, it is the authoritative source.
- Stage 1 versus Stage 2 labelling for H245 was inferred from the AS H235 ref list, because the two-column table layout did not survive text extraction reliably. The inference is consistent with H245's statement that "the OCR reference lists 'Stage 1' statements before 'Stage 2' statements".

## Q2. Formulae booklets and statistical tables: what is given and what must be memorised

### Takeaway
Both suites give a formulae booklet with statistics formulae and critical-value tables. Each spec's section 5d lists only two statistics items learners must recall without them being provided: the data mean x̄ = Σx/n = Σfx/Σf, and Z = (X−μ)/σ. However, several spec refs say "know and be able to use" results that are in fact printed in the booklet. OCR A gives χ², pmcc, Spearman, Wilcoxon T and W tables plus normal percentage points, but no t-table. The MEI booklet gives pmcc, Spearman, χ², t, Normal and Wilcoxon single-sample tables, but no rank-sum table.

### Cited Findings
- H245 spec 5d: "Learners must be able to use the following formulae and identities … without these formulae and identities being provided". Its Statistics entries are only the mean of a set of data x̄ = Σx/n = Σfx/Σf and the standard Normal variable Z=(X−μ)/σ where X~N(μ,σ²). — [H245 spec section 5d, pp.103–107](https://www.ocr.org.uk/Images/308752-specification-accredited-a-level-gce-further-mathematics-a-h245.pdf)
- The MEI H645 spec 5d has identical statistics memorise items: x̄ and Z. "The same formula booklet will be used for AS and A Level Further Mathematics B (MEI)." — [H645 spec section 5d, pp.145–149](https://www.ocr.org.uk/Images/308768-specification-accredited-a-level-gce-further-mathematics-b-mei-h645.pdf)
- **H245 Formulae Booklet (© OCR 2022, 16 pp), Statistics section**:
  - **Formulae:** probability addition and conditional rules; standard deviation formulae; sampling distributions (E(X̄)=μ, Var(X̄)=σ²/n, approximately normal for n > about 25, X̄~N(μ,σ²/n) and the z statistic); unbiased estimates of the mean and variance; expectation algebra; discrete E and Var.
  - **Distribution table:** P(X=x), E(X) and Var(X) for the binomial, uniform U(n), geometric Geo(p) and Poisson Po(λ). Continuous E and Var, and the c.d.f. Table of p.d.f., E and Var for the continuous uniform [a,b], **exponential λe^(−λx)** and normal.
  - **Normal percentage points:** p = 0.75, 0.90, 0.95, 0.975, 0.99, 0.995, 0.9975, 0.999, 0.9995.
  - **Non-parametric:** χ² statistic Σ(O−E)²/E; large-sample normal approximations for Wilcoxon signed-rank T and rank-sum W.
  - **Correlation and regression:** Sxx, Syy, Sxy; r; b=Sxy/Sxx; y=a+bx; rs=1−6Σd²/(n(n²−1)).
  - **Tables:** critical values of r and rs; χ² critical values; **Wilcoxon signed rank critical values of T** (with definitions of W+, W− and T); **Wilcoxon rank sum critical values of W** (m, n ≤ 10, with W = the smaller of Rm and m(m+n+1)−Rm).

  — [H245 Formulae Booklet](https://www.ocr.org.uk/Images/308765-a-level-further-mathematics-a-formulae-booklet.pdf)
- Table ranges as extracted from the H245 booklet:
  - pmcc and rs tables in two blocks: rows seen for n = 1–30 alongside n = 31–60.
  - χ² table for ν = 1–25, then 30, 40, …, 100, with p = 0.01, 0.025, 0.05, 0.90, 0.95, 0.975, 0.99, 0.995, 0.999.
  - T table from n = 6 to n = 20 (n=20: 60, 52, 43, 37).
  - W table for m = 3–10 and n up to 10.

  — [H245 Formulae Booklet](https://www.ocr.org.uk/Images/308765-a-level-further-mathematics-a-formulae-booklet.pdf)
- **H235 AS FM A booklet (© OCR 2022, 8 pp), Statistics**:
  - **Formulae:** standard deviation; the discrete distributions table (binomial, uniform, geometric, Poisson); the χ² statistic; Sxx, Syy, Sxy, r, regression and rs.
  - **Tables:** critical values of r and rs; χ² critical values.
  - **Not included:** no normal percentage points, no Wilcoxon tables and no continuous distributions, in line with the AS content.

  — [H235 Formulae Booklet](https://www.ocr.org.uk/Images/308766-as-level-further-mathematics-a-formulae-booklet.pdf)
- **MEI H635/H645 booklet (© OCR 2020, 16 pp)**:
  - **"A level Mathematics" section:** probability rules; sample variance s² = Sxx/(n−1); binomial; the Normal mean test statistic; Normal percentage points (10, 5, 2, 1%).
  - **"Statistics" section:**
    - discrete distributions: E and Var formulae; uniform 1..n; geometric P(X=r)=q^(r−1)p, mean 1/p and variance (1−p)/p²; Poisson;
    - correlation and regression: Sxx, Syy, Sxy, r, regression lines **y on x and x on y**, rs;
    - a **confidence intervals table**: x̄ ± k σ/√n with N(0,1); x̄ ± k s/√n with t_(n−1); the paired case treated as a single distribution;
    - a **hypothesis tests table**: pmcc test, Spearman test, χ² test, Normal test for a mean, **t-test for a mean (t_(n−1))** and Wilcoxon single sample test ("A statistic T is calculated from the ranked data");
    - continuous distributions: E, Var, cdf, and the continuous uniform mean and variance.
  - **Statistical tables:** critical values of r and rs; χ² percentage points (ν = 1–30, 35, 40, 50, 100); **t-distribution percentage points** (ν = 1–15, 20, 30, 50, 100, ∞; 10/5/2/1% two-tail); Normal percentage points; **Wilcoxon single sample critical values** for n = 2–50.

  — [MEI Formulae Booklet](https://www.ocr.org.uk/Images/752530-formulae-booklet.pdf)
- The spec notes many formulae will be given, but some also require derivation. Examples: SR9 says the uniform mean and variance "will be given but their derivations may be asked for"; SR10 says "Prove these results in particular cases" for the binomial; SR22 covers the continuous uniform. — [H645 spec 2e](https://www.ocr.org.uk/Images/308768-specification-accredited-a-level-gce-further-mathematics-b-mei-h645.pdf)
- OCR A has no MEI-style "derivation" requirement: proofs of E, Var, binomial, geometric and CLT results are explicitly "[Proof … excluded]" in 5.02b, 5.02d, 5.02h and 5.05a/b. — [H245 spec 2d](https://www.ocr.org.uk/Images/308752-specification-accredited-a-level-gce-further-mathematics-a-h245.pdf)
- OCR noted amended formulae booklets for FM A and FM B (MEI) on its qualification pages. The listed fixes included a binomial series form and a revised variance formula. — [OCR subject update](https://ocr-live-prd95.cambridgeassessment.org.uk/administration/support-and-tools/subject-updates/as-a-level-further-maths-210218/) (seen via search snippet only; page not opened)

### Inferences
- For practical "must memorise" lists, the material is not in the H245 booklet and so must be known:
  - permutations and combinations formulae;
  - Yates' corrected χ² statistic Σ(|O−E|−0.5)²/E (not seen in the booklet extract);
  - E(g(X))=∫g(x)f(x)dx;
  - the median and quartile definitions via F;
  - sign test procedure and binomial basis;
  - continuity corrections;
  - degrees-of-freedom rules.
- For MEI, the definitions of the Poisson and geometric conditions, standard error, and residual = observed − predicted must be known.
- The newest MEI booklet listed against past papers is still the © 2020 edition. The AS FM A booklet served at 308766 is a © 2022 edition, while the past-paper-linked copy (752815) is © 2020. Teachers should use the 2022 FM A editions.

### Gaps
- I could not reliably extract from the PDF text whether the H245 booklet prints Yates' formula or the sign-test procedure. Absence is inferred, not confirmed visually.
- MEI pmcc/rs table n-range was not extracted.
- I did not open the OCR amendment notice directly.

## Q3. Paper structure (marks, time, weighting)

### Takeaway
OCR A Y542 is 75 marks in 1 h 30 min, worth 25% of the A level. AS Y532 is 60 marks in 1 h 15 min, worth 33⅓% of the AS. MEI Y422 Statistics Major is 120 marks in 2 h 15 min, worth 33⅓%, with Section A of 25–35 marks and Section B of 85–95 marks. Y432 Statistics Minor is 60 marks in 1 h 15 min, worth 16⅔%. AS Y412 is 60 marks in 1 h 15 min, worth 33⅓% of the AS.

### Cited Findings
- H245 structure:
  - Learners take mandatory Pure Core 1 (Y540) and Pure Core 2 (Y541), each 75 marks in 90 minutes, plus any two of Statistics (Y542), Mechanics (Y543), Discrete Mathematics (Y544) and Additional Pure Mathematics (Y545).
  - Each paper is "75 marks, 90 minute written paper, 25% of total A Level".
  - Y542: "All questions are compulsory and there are 75 marks in total. The paper assesses content from the Statistics section of the specification, and synoptically from the Pure Core … increasing gradient of difficulty … mix of short and long questions."
  - Learners may take more than two options.

  — [H245 spec 2a & 3a](https://www.ocr.org.uk/Images/308752-specification-accredited-a-level-gce-further-mathematics-a-h245.pdf)
- H235 structure: mandatory Pure Core (Y531) plus any two of Y532 Statistics, Y533, Y534 and Y535. Each paper is 60 marks in 75 minutes and worth 33⅓% of the AS. "All examinations have a duration of 75 minutes." Y532 questions are all compulsory and assess Statistics content plus Pure Core synoptically. — [H235 spec 2a & 3a](https://www.ocr.org.uk/Images/308750-specification-accredited-as-level-gce-further-mathematics-a-h235.pdf)
- H645 structure:
  - Core Pure (Y420): 144 raw marks (180 scaled), 2 h 40 min, 50%.
  - Major option: 120 raw marks (120 scaled), 2 h 15 min, 33⅓%.
  - Minor option: 60 raw marks (60 scaled), 1 h 15 min, 16⅔%. Further Pure with Technology Y436 is 1 h 45 min.
  - Routes: A is Core Pure + Mechanics Major + 1 minor (not Mechanics Minor). B is Core Pure + **Statistics Major** + 1 minor (not Statistics Minor). C is Core Pure + 3 minors.
  - Y421 and Y422 cannot both be taken, and Y422 and Y432 cannot both be taken.

  — [H645 spec 2a](https://www.ocr.org.uk/Images/308768-specification-accredited-a-level-gce-further-mathematics-b-mei-h645.pdf)
- Y422: "Length of paper 2 hour 15 minutes; Number of marks 120; Section A will have between 25 and 35 marks and will comprise more straightforward questions. Section B will have between 85 and 95 marks"; 33⅓% of H645. — [H645 spec 2e](https://www.ocr.org.uk/Images/308768-specification-accredited-a-level-gce-further-mathematics-b-mei-h645.pdf)
- Y432: "1 hour 15 minutes; 60 marks; The examination paper will not have sections"; 16⅔% of H645. — [H645 spec 2g](https://www.ocr.org.uk/Images/308768-specification-accredited-a-level-gce-further-mathematics-b-mei-h645.pdf)
- H635 AS: Core Pure (Y410) plus any two of Y411 Mechanics a, **Y412 Statistics a**, Y413 Modelling with Algorithms and Y414 Numerical Methods. Each paper is 60 marks in 1 h 15 min and worth 33⅓%. Y412 has no sections. — [H635 spec 2a & 2e](https://www.ocr.org.uk/Images/308764-specification-accredited-as-level-gce-further-mathematics-b-mei-h635.pdf)
- The March 2026 H645 v2.1 change: the Further Pure with Technology (Y436) minor is being withdrawn. The final first teaching is September 2026 and the final assessment is Summer 2028, with no resit. This does not affect the statistics papers, but it narrows Route B and C minor choices from 2028. — [H645 spec v2.1 front matter](https://www.ocr.org.uk/Images/308768-specification-accredited-a-level-gce-further-mathematics-b-mei-h645.pdf)

### Inferences
- Time per mark: OCR A Y542 allows 1.2 min/mark (90/75), MEI Y422 1.125 min/mark (135/120) and MEI Y432 1.25 min/mark (75/60). MEI Statistics Major carries about 1.6× the marks of OCR A Y542 for broadly comparable content breadth.
- A Route B MEI student does Statistics Major (33⅓%). An OCR A student does Y542 (25%) as one of two options. An MEI Route C student can take Statistics Minor at 16⅔%, which covers only the (a) content: no continuous RVs and no inference.

### Gaps
- Assessment-objective weightings per paper were not extracted.
- Grade boundaries were out of scope.
