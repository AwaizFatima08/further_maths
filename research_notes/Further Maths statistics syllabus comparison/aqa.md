# AQA AS (7366) and A-level (7367) Further Mathematics: Statistics optional application

Sources used (all downloaded and read in full as text on 16 Nov 2026):
- A-level spec 7367, Version 1.1 (title page dated 20 Oct 2017, footer 19 Oct 2017): https://filestore.aqa.org.uk/resources/mathematics/specifications/AQA-7367-SP-2017.PDF. The AQA spec web page (https://www.aqa.org.uk/subjects/mathematics/a-level/further-mathematics-7367/specification) currently links to https://cdn.sanity.io/files/p28bar15/green/b278377bc36beb9b2e64aea1b373db2605751a15.pdf, which is **byte-identical** to the filestore copy (checked with `cmp`).
- AS spec 7366, Version 1.2, 11 January 2018: https://filestore.aqa.org.uk/resources/mathematics/specifications/AQA-7366-SP-2017.PDF
- Formulae and statistical tables booklet, v1.5 issued February 2018 (PDF built Dec 2019): https://filestore.aqa.org.uk/resources/mathematics/AQA-AS-A-FMATHS-FORMULAE.PDF (modified A3 large-print version: https://filestore.aqa.org.uk/resources/mathematics/AQA-AS-A-FMATHS-FORMULAE-MQP24A3.PDF)
- Past paper covers: A-level 7367/3S June 2022 https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-73673S-QP-JUN22.PDF ; AS 7366/2S June 2022 https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-73662S-QP-JUN22.PDF and June 2023 https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2023/june/AQA-73662S-QP-JUN23.PDF

**Code note:** AQA does NOT use "FS1/FS2" codes. Statistics is "Optional application 2 – statistics", spec section 3.4, with sub-sections **SA to SH** and numbered points (SA1, SA2, ...). Both specs say: "The optional applications are mechanics (MA to ME [AS: MA to MD]), statistics (SA to SH) and discrete (DA to DG)."

## Every numbered spec point in the statistics option, and AS vs A-level

### Takeaway
A-level 7367 statistics has 8 sub-sections (SA–SH) and 36 numbered points. AS 7366 uses the same codes but drops SF (exponential) and SG (t-test) entirely and omits SC2, SD6, SD7, SE5 and SH4. It also cuts back SA5, SC1 and SD1. Point numbers are kept the same in both specs, so AS has gaps (for example SD5 is followed by SD8).

### Cited Findings
Full content list from the A-level spec, section 3.4, pp. 23–27 ([7367 spec](https://filestore.aqa.org.uk/resources/mathematics/specifications/AQA-7367-SP-2017.PDF)). The AS column is checked against section 3.4 of the AS spec, pp. 18–20 ([7366 spec](https://filestore.aqa.org.uk/resources/mathematics/specifications/AQA-7366-SP-2017.PDF)).

**3.4.1 SA: Discrete random variables (DRVs) and expectation**
| Code | Content (A-level wording) | AS? |
|---|---|---|
| SA1 | Understand DRVs with distributions given in the form of a table or function. | AS + A |
| SA2 | Evaluate probabilities for a DRV. | AS + A |
| SA3 | Evaluate measures of average and spread for a DRV to include mean, variance, standard deviation, mode and median. | AS + A |
| SA4 | Understand expectation and know the formulae E(X)=Σxᵢpᵢ; E(X²)=Σxᵢ²pᵢ; Var(X)=E(X²)−(E(X))². | AS + A |
| SA5 | Understand expectation of linear functions of DRVs and know E(aX+b)=aE(X)+b and Var(aX+b)=a²Var(X). **Know E(g(X))=Σg(xᵢ)pᵢ. Find mean, variance, s.d. for functions of a DRV such as E(5X³), E(18X⁻³), Var(6X⁻¹).** | AS has **only the linear-function part**. The bold E(g(X)) part is A-level only (confirmed by re-extracting AS p.18) |
| SA6 | Know the discrete uniform distribution on {1,2,…,n}; understand when it can be used as a model. | AS + A |
| SA7 | Proof of mean and variance of discrete uniform distribution. | AS + A |

**3.4.2 SB: Poisson distribution** (identical in AS and A-level)
| Code | Content | AS? |
|---|---|---|
| SB1 | Understand conditions for a Poisson distribution to model a situation; terminology X ~ Po(λ). | AS + A |
| SB2 | Know the Poisson formula; calculate probabilities using the formula or equivalent calculator function. | AS + A |
| SB3 | Know mean, variance, s.d. of Poisson; use the result that mean and variance are equal. | AS + A |
| SB4 | Understand the distribution of the sum of independent Poisson distributions. | AS + A |
| SB5 | Formulate hypotheses and carry out a hypothesis test of a population mean from a single observation from a Poisson distribution, using direct evaluation of Poisson probabilities. | AS + A |

**3.4.3 SC: Type I and Type II errors**
| Code | Content | AS? |
|---|---|---|
| SC1 | Understand Type I and Type II errors and define in context. Calculate P(Type I error) for tests based on a Poisson or Binomial distribution. **Calculate P(Type I error) for tests based on a normal distribution.** | AS has only the first two sentences (Poisson/Binomial). The normal-based Type I part is A-level only |
| SC2 | Understand the power of a test. Calculate P(Type II error) and power for tests based on a normal, Binomial or Poisson distribution. | **A-level only** |

**3.4.4 SD: Continuous random variables (CRVs)**
| Code | Content | AS? |
|---|---|---|
| SD1 | Understand and use a pdf f(x); differences between discrete and continuous distributions. **Understand and use distributions of random variables that are part discrete and part continuous.** | AS has only the first sentence. Mixed discrete/continuous is A-level only |
| SD2 | Find the probability of an observation lying in a specified interval. | AS + A |
| SD3 | Find the median and quartiles for a given pdf. | AS + A |
| SD4 | Find mean, variance, s.d. for a given pdf; know E(X)=∫x f(x)dx, E(X²)=∫x² f(x)dx, Var(X)=E(X²)−(E(X))². | AS + A |
| SD5 | Expectation/variance of linear functions of CRVs: E(aX+b), Var(aX+b); know E(g(X))=∫g(x)f(x)dx; find mean, variance, s.d. of functions such as E(5X³), E(18X⁻³), Var(6X⁻¹). | AS + A (AS includes the E(g(X)) line here) |
| SD6 | Understand and use a cdf F(x); know F(x)=∫₋∞ˣ f(t)dt and f(x)=dF/dx. | **A-level only** |
| SD7 | Rectangular (continuous uniform) distribution f(x)=1/(b−a), a≤x≤b: conditions for use as a model; probabilities; **proofs of mean, variance and s.d.** | **A-level only** |
| SD8 | If X and Y are independent (discrete or continuous) random variables, E(X+Y)=E(X)+E(Y) and Var(X+Y)=Var(X)+Var(Y). | AS + A |

**3.4.5 SE: Chi squared tests for association**
| Code | Content | AS? |
|---|---|---|
| SE1 | Construction of n × m contingency tables. | AS + A |
| SE2 | Use of Σ(Oᵢ−Eᵢ)²/Eᵢ as an approximate χ² statistic with appropriate degrees of freedom. | AS + A |
| SE3 | Know and use the convention that all Eᵢ should be greater than 5. | AS + A |
| SE4 | Identification of sources of association in the context of a question. | AS + A |
| SE5 | Knowledge of when and how to apply Yates' correction. | **A-level only** |

**3.4.6 SF: Exponential distribution** (A-level only; not in AS spec)
| Code | Content |
|---|---|
| SF1 | Know conditions for an exponential distribution to be used as a model; know its pdf and cdf. |
| SF2 | Calculate probabilities using F(x) or integration of f(x). |
| SF3 | Know proofs of mean, variance and s.d. for an exponential distribution. |
| SF4 | Understand that the lengths of intervals between Poisson events have an exponential distribution. |

**3.4.7 SG: Inference – one sample t-distribution** (A-level only; not in AS spec)
| Code | Content |
|---|---|
| SG1 | Test for the mean of a normal distribution with unknown variance using a t-statistic with appropriate degrees of freedom. |

**3.4.8 SH: Confidence intervals** (AS section number 3.4.6)
| Code | Content | AS? |
|---|---|---|
| SH1 | Construct symmetric CIs for the mean of a normal distribution with known variance. | AS + A |
| SH2 | Construct symmetric CIs from large samples for the mean of a normal distribution with unknown variance. | AS + A |
| SH3 | Make inferences from constructed or given CIs. | AS + A |
| SH4 | Construct symmetric CIs from small samples for the mean of a normal distribution with unknown variance using the t-distribution. | **A-level only** |

- In the AS spec the points are SA1–SA7, SB1–SB5, SC1, SD1–SD5, SD8, SE1–SE4 and SH1–SH3, a total of 25 points. AS sub-sections are numbered 3.4.1 SA to 3.4.6 SH, with no SF or SG — [7366 spec](https://filestore.aqa.org.uk/resources/mathematics/specifications/AQA-7366-SP-2017.PDF)
- Cross-check: PMT's AQA Further Statistics page lists cheat-sheet topics that match these headings: chi-squared tests for association, confidence intervals, continuous and discrete random variables, errors in hypothesis testing, exponential distribution, one-sample t-inference and Poisson. It also has separate AS and A-level formula sheets — [PMT AQA Further Statistics](https://www.physicsandmathstutor.com/maths-revision/a-level-aqa/further-statistics/). ExamSolutions has a separate "AQA Further Statistics AS" tutorial set — [ExamSolutions](https://www.examsolutions.net/as-maths/aqa/further-statistics-as-tutorials/). I did not fetch these pages in full, so treat them as a check that the topics exist, not as content.

### Inferences
- Topics that some other boards cover in Further Statistics are **not** in AQA's statistics option, so this is worth noting in any comparison. They include: geometric/negative binomial distributions, probability generating functions, moment generating functions, chi-squared goodness-of-fit tests (AQA only has contingency tables/association), non-parametric tests (sign, Wilcoxon), Spearman's rank, regression/correlation, two-sample t-tests, paired tests, the central limit theorem as a named spec point, distributions of linear combinations of normals beyond SD8, and estimators/bias. I searched the 7367 section 3.4 text for these and found none. Note that the formulae booklet still prints S² as an unbiased estimator and the PMCC table, because the booklet is shared with A-level Maths.
- The binomial and normal distributions are assumed from A-level Maths (they appear in SC1/SC2 and SH), not taught as new FM content.

### Gaps
- I did not obtain AQA's statistics Teaching Guidance document, which gives example questions per spec point and might clarify scope. Example: whether "sum of independent Poisson" in SB4 includes an approximation to Poisson.

## Formulae and statistical tables booklet: what is given and what must be memorised

### Takeaway
One booklet is shared by AS/A-level Maths and Further Maths, and it is required in all Further Maths exams. For statistics it gives only a few formulae: basic probability, the s.d. formula, binomial and Poisson pmf/mean/variance, sampling distributions (including the t statistic) and the contingency-table χ² statistic. It gives three tables: t percentage points, χ² percentage points and PMCC critical values. There is **no normal table and no Poisson/binomial cumulative tables**; the calculator does this. Nothing is given for the discrete uniform, rectangular or exponential distributions, the E(g(X)) and pdf/cdf formulae, Yates' correction or confidence-interval construction.

### Cited Findings
- Title: "Formulae and statistical tables for A-level Mathematics and A-level Further Mathematics", covering AS Maths 7356, A-level Maths 7357, AS FM 7366 and A-level FM 7367. "v1.5 Issued February 2018". It states that the booklet "is required for all AS and A-level Further Mathematics exams" — [AQA formulae booklet](https://filestore.aqa.org.uk/resources/mathematics/AQA-AS-A-FMATHS-FORMULAE.PDF)
- Contents: Pure mathematics (p.4), Mechanics (p.10), Probability and statistics (p.11), then Statistical tables: Table 1 percentage points of the Student's t-distribution (p.12), Table 2 percentage points of the χ² distribution (p.13), Table 3 critical values of the product moment correlation coefficient (p.14) — [AQA formulae booklet](https://filestore.aqa.org.uk/resources/mathematics/AQA-AS-A-FMATHS-FORMULAE.PDF)
- The "Probability and statistics" page gives these formulae in full — [AQA formulae booklet](https://filestore.aqa.org.uk/resources/mathematics/AQA-AS-A-FMATHS-FORMULAE.PDF):
  - P(A∪B)=P(A)+P(B)−P(A∩B); P(A∩B)=P(A)×P(B|A)
  - Standard deviation: √[Σ(x−x̄)²/n] = √[Σx²/n − x̄²]
  - Discrete distributions table: Binomial B(n,p) with P(X=x)=C(n,x)pˣ(1−p)ⁿ⁻ˣ, mean np, variance np(1−p); Poisson Po(λ) with P(X=x)=e^(−λ)λˣ/x!, mean λ, variance λ
  - Sampling distributions: X̄ is an unbiased estimator of μ with Var(X̄)=σ²/n; S²=Σ(Xᵢ−X̄)²/(n−1) is an unbiased estimator of σ²; for samples from N(μ,σ²), (X̄−μ)/(σ/√n) ~ N(0,1) and (X̄−μ)/(S/√n) ~ t₍ₙ₋₁₎
  - "Distribution-free (non-parametric) tests – Contingency tables: Σ(Oᵢ−Eᵢ)²/Eᵢ is approximately distributed as χ²"
- Table 1 (t): p = 0.9, 0.95, 0.975, 0.99, 0.995 for ν = 1–40, then 45, 50, …, 100, 125, 150, 200 and ∞. Table 2 (χ²): p = 0.005, 0.01, 0.025, 0.05, 0.1, 0.9, 0.95, 0.975, 0.99, 0.995 for ν = 1–40, then 45 to 100 in steps of 5. Table 3 (PMCC): one-tail 10%/5%/2.5%/1%/0.5% for n = 4–50, 60, 70, 80, 90, 100 — [AQA formulae booklet](https://filestore.aqa.org.uk/resources/mathematics/AQA-AS-A-FMATHS-FORMULAE.PDF)
- Spec Appendix B lists formulae students "must be able to use … without these formulae and identities being provided". Its Statistics entries are only the mean of a data set x̄=Σx/n=Σfx/Σf and the standard normal variable Z=(X−μ)/σ where X~N(μ,σ²) — [7367 spec, Appendix B p.56](https://filestore.aqa.org.uk/resources/mathematics/specifications/AQA-7367-SP-2017.PDF)
- In addition, the content points themselves say "know the formula(e)" for: SA4 (E(X), E(X²), Var(X)), SA5 (E(aX+b), Var(aX+b), E(g(X)) discrete), SB2 (Poisson formula), SB3 (Poisson mean/variance), SD4 (E(X), E(X²), Var(X) for a pdf), SD5 (linear functions; E(g(X))=∫g(x)f(x)dx), SD6 (F(x)=∫f(t)dt, f(x)=F′(x)), SD7 (rectangular pdf, with proofs of mean/variance), SF1 (exponential pdf and cdf) and SF3 (proofs of exponential mean/variance) — [7367 spec](https://filestore.aqa.org.uk/resources/mathematics/specifications/AQA-7367-SP-2017.PDF)
- Calculator: A-level FM calculators must at minimum have an iterative function, matrices up to 3×3, and "the ability to compute summary statistics and access probabilities from standard statistical distributions" (spec 5.9) — [7367 spec](https://filestore.aqa.org.uk/resources/mathematics/specifications/AQA-7367-SP-2017.PDF). This is why normal, binomial and Poisson probabilities are not tabulated.
- Exam paper cover: "Unless stated otherwise, you may quote formulae, without proof, from the booklet" — [7367/3S June 2022](https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-73673S-QP-JUN22.PDF)

### Inferences (must be memorised, derived by comparing booklet against spec)
- Memorise or be able to derive: E(X), E(X²), Var(X) and E(g(X)) for DRVs and CRVs; E(aX+b) and Var(aX+b); E(X+Y) and Var(X+Y) for independent X, Y; discrete uniform mean (n+1)/2 and variance (n²−1)/12, with proof (SA7); the rectangular pdf, mean (a+b)/2 and variance (b−a)²/12, with proofs (SD7); the exponential pdf λe^(−λx), cdf 1−e^(−λx), mean 1/λ and variance 1/λ², with proofs (SF1, SF3); the cdf–pdf relationship; the median/quartile definitions via F(x); the Eᵢ = (row total × column total)/grand total rule and degrees of freedom (r−1)(c−1) for contingency tables; the Eᵢ > 5 convention; the Yates' corrected statistic Σ(|Oᵢ−Eᵢ|−0.5)²/Eᵢ for 2×2 tables; confidence interval forms x̄ ± z·σ/√n and x̄ ± t·s/√n; Type I/II error and power definitions (power = 1 − P(Type II)).
- Poisson pmf/mean/variance are printed in the booklet even though SB2/SB3 say "know". Students can rely on the booklet for them.
- The spec's "know" points are my reading of the content text. AQA does not publish a separate "formulae to be memorised" list for the options beyond Appendix B.

### Gaps
- The booklet on the filestore is v1.5 (Feb 2018). I found no later version on the filestore. AQA's news page returned no booklet details when fetched, so I could not confirm from an AQA page that v1.5 is the edition for 2026 exams. However, recent papers (for example the June 2022 cover) still require "the AQA Formulae and statistical tables booklet for A-level Mathematics and A-level Further Mathematics".
- Exact Yates' correction formula and CI formulae are not printed in either the spec or the booklet. The forms above are standard, not AQA-quoted.

## Paper structure (which paper, marks, time)

### Takeaway
At A-level (7367), statistics is examined in **Paper 3**. Paper 3 is 2 hours and 100 marks (33⅓% of A-level). It is made of two 50-mark question paper/answer booklets, one for each chosen option (statistics plus mechanics or discrete), done together within the 2 hours. At AS (7366), statistics is in **Paper 2**: 1 hour 30 minutes and 80 marks (50% of AS), made of two 40-mark booklets. Students must study two of the three options.

### Cited Findings
- 7367 Paper 1 and Paper 2: compulsory pure (A–J), each 2 hours, 100 marks, 33⅓%. Paper 3: "One question paper answer booklet on Discrete and one question paper answer booklet on Statistics" OR Statistics and Mechanics OR Mechanics and Discrete; written exam 2 hours, 100 marks, 33⅓% of A-level — [7367 spec §2.2](https://filestore.aqa.org.uk/resources/mathematics/specifications/AQA-7367-SP-2017.PDF)
- "Students must study two of these options": mechanics, statistics and discrete — [7367 spec §2.1](https://filestore.aqa.org.uk/resources/mathematics/specifications/AQA-7367-SP-2017.PDF)
- 7367/3S cover: "A-level Further Mathematics Paper 3 Statistics", time allowed 2 hours, "You must ensure you have the other optional Question Paper/Answer Book for which you are entered (either Discrete or Mechanics). You will have 2 hours to complete both papers." "The maximum mark for this paper is 50." — [7367/3S June 2022](https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-73673S-QP-JUN22.PDF)
- 7366 Paper 1: pure A–H, 1 h 30 min, 80 marks, 50% of AS. Paper 2: two option booklets (Discrete+Statistics, Statistics+Mechanics, or Mechanics+Discrete), 1 h 30 min, 80 marks, 50% of AS — [7366 spec §2.2](https://filestore.aqa.org.uk/resources/mathematics/specifications/AQA-7366-SP-2017.PDF)
- 7366/2S cover: "AS Paper 2 Statistics", time allowed 1 hour 30 minutes, "The maximum mark for this paper is 40" (June 2022 and Friday 19 May 2023 papers) — [7366/2S June 2022](https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2022/june/AQA-73662S-QP-JUN22.PDF); [7366/2S June 2023](https://filestore.aqa.org.uk/sample-papers-and-mark-schemes/2023/june/AQA-73662S-QP-JUN23.PDF)
- An AQA marketing leaflet (Nov 2023) confirms the same structure: AS FM two papers of 80 marks, 1 h 30 each; A-level FM three papers of 100 marks, 2 h each; Paper 3 assesses two of the applications; calculators allowed on all papers — [AQA "Teach with us" leaflet](https://filestore.aqa.org.uk/resources/mathematics/AQA-7356-7357-7366-7367-FB-TEACH-WITH-US.PDF)
- Component codes from paper footers: 7367/3S (A-level statistics) and 7366/2S (AS statistics) — past paper PDFs above.

### Inferences
- Statistics is therefore 50/300 marks (about 16.7%) of the A-level and 40/160 marks (25%) of the AS. Time is not split between the two booklets; candidates divide the 2 h (A-level) or 1 h 30 (AS) themselves.
- The specs are unchanged since 2017/2018 (7367 v1.1, 7366 v1.2). The copy linked from AQA's live spec page in Nov 2026 is identical to the 2017 v1.1 PDF, so this content list is current for 2026 exams.

### Gaps
- I did not open a 2024 or 2025 paper (the guessed filestore URLs returned 404), so I confirmed 50/40 marks from 2022 and 2023 papers only. I found no announcement of a structural change.
- AQA's spec web page did not show the "Key dates/News" tab content when fetched, so the absence of a 2026 spec revision is inferred from the identical PDF, not from an explicit AQA statement.
