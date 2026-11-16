"""Writes the YouTube lecture series plan (Markdown) from the workbook units, so episode
references to sections and worked examples always match the book."""
import importlib
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "YouTube_Lecture_Series_Plan.md"
sys.path.insert(0, str(HERE))

from content import book  # noqa: E402

BOARD_NAMES = dict(zip(book.BOARDS, ["Edexcel", "IAL S3", "AQA", "OCR A", "OCR MEI", "Cambridge 9231"]))

# (module, episode title, section numbers (1-based within the unit), worked example numbers, minutes, focus line)
EPISODES = [
    ("as01", "Discrete random variables: distributions, expectation and variance", [1, 2, 3], [1, 2], 25,
     "Build a probability distribution, use cumulative tables, and find E(X) and Var(X)."),
    ("as01", "Functions of X, coding, sums and the discrete uniform", [4, 5, 6, 7], [3, 4, 5, 6], 28,
     "E(g(X)), E(aX + b), Var(aX + b), sums of independent variables and the discrete uniform."),
    ("as02", "The binomial distribution, with proof of its mean and variance", [1, 2, 7], [1, 6], 24,
     "Conditions for B(n, p), cumulative tables, and why E(X) = np and Var(X) = np(1 − p)."),
    ("as02", "The Poisson distribution: modelling, rescaling and adding", [3, 4], [2, 3], 25,
     "When a Poisson model fits, changing the interval, and the additive property."),
    ("as02", "Poisson approximation to the binomial, and choosing a model", [5, 6], [4, 5], 22,
     "B(n, p) ≈ Po(np), the discrete uniform, and checking a model against data."),
    ("as03", "The geometric distribution", [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5], 30,
     "Waiting for the first success: probabilities, mean, variance, memoryless property and mode."),
    ("as04", "Permutations: arrangements, repeats and restrictions", [1, 2, 3, 4], [1, 2, 5], 26,
     "The counting principle, nPr, repeated objects, and 'together' and 'apart' restrictions."),
    ("as04", "Combinations and probability by counting", [5, 6, 7], [3, 4, 6], 25,
     "Selections with nCr, 'at least' problems, and probability by counting outcomes."),
    ("as05", "Sampling I: populations, bias, simple random and systematic samples", [1, 2, 3, 4], [1, 2, 3], 24,
     "Why we sample, what makes a sample biased, and two random methods."),
    ("as05", "Sampling II: stratified, quota, cluster and opportunity samples", [5, 6, 7, 8], [4, 5, 6], 25,
     "Proportional allocation, non-random methods, sample size and choosing a method."),
    ("as06", "Hypothesis testing I: the language of tests and binomial tests", [1, 2, 5], [1, 4], 26,
     "H₀, H₁, significance level, p-values, one- and two-tailed binomial tests."),
    ("as06", "Hypothesis testing II: Poisson tests, critical regions and Type I errors", [3, 4, 6], [2, 3, 5, 6], 29,
     "Testing a Poisson mean, critical regions, actual significance level and P(Type I error)."),
    ("as07", "χ² goodness of fit I: expected frequencies and degrees of freedom", [1, 2, 3, 4, 5], [1, 2], 26,
     "The χ² statistic, combining classes so E ≥ 5, and counting degrees of freedom."),
    ("as07", "χ² goodness of fit II: fitting Poisson, geometric and normal models", [6, 7, 8], [3, 4, 5], 30,
     "Estimating parameters from data and losing degrees of freedom."),
    ("as08", "Contingency tables I: testing for association", [1, 2, 3, 4], [1, 2, 3], 27,
     "Expected frequencies, ν = (r − 1)(c − 1) and combining rows or columns."),
    ("as08", "Contingency tables II: contributions and Yates' correction", [5, 6, 7], [4, 5], 23,
     "Finding where the association is, and the 2 × 2 continuity correction."),
    ("as09", "Correlation I: the product moment correlation coefficient", [1, 2, 3, 4, 5], [1, 2], 28,
     "Sxx, Syy, Sxy, the PMCC, coding, interpretation and testing ρ = 0."),
    ("as09", "Correlation II: Spearman's rank correlation", [6, 7, 8], [3, 4, 5], 26,
     "Ranking, tied ranks, testing ρₛ = 0, effect size and choosing the right coefficient."),
    ("as10", "Regression I: the least squares regression line", [1, 2, 3, 4], [1, 2], 25,
     "Explanatory and response variables, b = Sxy/Sxx, interpolation, extrapolation and coding."),
    ("as10", "Regression II: residuals, RSS and the line of x on y", [5, 6, 7, 8], [3, 4, 5], 26,
     "Residual analysis, the residual sum of squares, outliers and the second regression line."),
    ("as11", "Continuous random variables I: pdfs, mean and variance", [1, 2, 3, 4], [1, 3], 26,
     "Valid pdfs, piecewise pdfs, sketching, E(X) and Var(X) by integration."),
    ("as11", "Continuous random variables II: medians, modes and E(g(X))", [5, 6, 7], [2, 4, 5, 6], 29,
     "E(g(X)), median and quartiles, the mode by differentiation, and mixed distributions."),
    ("as12", "Confidence intervals with the normal distribution", [1, 2, 3, 4, 5, 6, 7], [1, 3, 4, 5], 30,
     "Building and interpreting intervals for μ, choosing a sample size, and testing with an interval."),
    ("a201", "Cumulative distribution functions", [1, 2, 3, 4], [1, 2, 3], 27,
     "Writing F(x) in full, moving between f and F, and percentiles from F."),
    ("a201", "The continuous uniform distribution, skewness and Y = g(X)", [5, 6, 7], [4, 5, 6], 28,
     "Rectangular distribution proofs, skewness, and the cdf method for a function of X."),
    ("a202", "The exponential distribution", [1, 2, 3, 4, 5, 6], [1, 2, 3, 4], 30,
     "Waiting times, proofs of the mean and variance, the Poisson link and the memoryless property."),
    ("a203", "The negative binomial distribution", [1, 2, 3], [1, 2, 3], 25,
     "Waiting for the r-th success: probabilities, mean and variance as a sum of geometrics."),
    ("a203", "Hypothesis tests for a geometric parameter", [4, 5], [4, 5, 6], 24,
     "Critical regions and actual significance levels for tests on p."),
    ("a204", "Probability generating functions I: definition and standard PGFs", [1, 2, 3], [1, 2, 3], 28,
     "G(t) = E(tˣ), mean and variance from G′(1) and G″(1), and deriving standard PGFs."),
    ("a204", "Probability generating functions II: sums and transformations", [4, 5, 6], [4, 5, 6], 26,
     "Products of PGFs for sums, the PGF of aX + b, and probabilities by expansion."),
    ("a205", "Quality of tests I: Type I and II errors, size and power", [1, 2, 3], [1, 2], 26,
     "Size of a test, P(Type II error) and power for discrete tests."),
    ("a205", "Quality of tests II: power functions", [4, 5, 6], [3, 4, 5, 6], 29,
     "Power functions, normal-mean tests, sample size, and comparing tests."),
    ("a206", "Linear combinations of random variables", [1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6], 30,
     "E and Var of aX ± bY, 2X versus X₁ + X₂, and combinations of normal and Poisson variables."),
    ("a207", "The sampling distribution of X̄ and the Central Limit Theorem", [1, 2, 3], [1, 2, 3], 27,
     "Statistics versus parameters, the distribution of the sample mean, and the CLT."),
    ("a207", "Estimators, bias and standard error", [4, 5], [4, 5, 6], 25,
     "Unbiased estimators of μ and σ², bias, and choosing between estimators."),
    ("a208", "One-sample z-tests and confidence intervals", [1, 2, 3], [1, 2], 25,
     "When z is valid, the one-sample test, and the link between intervals and tests."),
    ("a208", "Two-sample z-tests and intervals for a difference of means", [4, 5, 6], [3, 4, 5], 28,
     "Comparing two means with known variances or large samples."),
    ("a209", "The t distribution and reading t tables", [1, 2, 3, 4], [1], 22,
     "Why t is needed, degrees of freedom, reading tables, and finding x̄ and s."),
    ("a209", "One-sample t-tests and t confidence intervals", [5, 6, 7], [2, 3, 4, 5], 29,
     "Testing a mean and building an interval when σ is unknown, and t versus z."),
    ("a210", "The paired t-test", [1, 2], [1, 2], 24,
     "Paired versus independent samples, and testing the mean difference."),
    ("a210", "The pooled two-sample t-test", [3, 4, 5, 6], [3, 4, 5, 6], 30,
     "The pooled variance estimate, the two-sample test, and choosing the right test."),
    ("a211", "Inference for a variance: χ² intervals and tests", [1, 2, 3], [2, 3, 4], 27,
     "(n − 1)S²/σ² ~ χ²(n − 1), intervals for σ² and σ, and testing a variance."),
    ("a211", "The F distribution and the F-test for two variances", [4, 5, 6], [1, 5, 6], 27,
     "Reading F tables, the reciprocal property, and checking variances before pooling."),
    ("a212", "The sign test", [1, 2, 3, 4], [1, 2, 3], 26,
     "What non-parametric means, single-sample and paired sign tests with the binomial."),
    ("a212", "The sign test for large samples, and its power", [5, 6], [4, 5], 22,
     "The normal approximation and how the sign test compares with parametric tests."),
    ("a213", "The Wilcoxon signed-rank test", [1, 2, 3], [1, 2], 27,
     "Ranks, the symmetry assumption, and the distribution of T under H₀."),
    ("a213", "The Wilcoxon matched-pairs test and its normal approximation", [4, 5], [3, 5], 24,
     "Signed-rank tests on paired data and for large samples."),
    ("a213", "The Wilcoxon rank-sum test and choosing a test", [6, 7, 8, 9], [4, 6], 28,
     "Comparing two independent samples, the normal approximation, ties and test choice."),
    ("a214", "Normal probability plots, software output and simulation", None, None, 26,
     "Judging normality from a plot, reading software output, and simulation."),
]

SPECIALS = {
    "intro": ("Course introduction: what Further Statistics covers and how to use this series", 20, [
        "What Further Statistics is, and how AS and A2 fit together.",
        "The coverage map: which episodes each exam board needs (show the workbook's coverage map on screen).",
        "How to use the workbook alongside the videos: pause, attempt, check answers at the back.",
        "Calculator functions and statistical tables used throughout the series.",
    ]),
    "as_review": ("AS review: writing hypothesis tests that score full marks", 25, [
        "The five-step structure for every test, with a model write-up.",
        "Common examiner-report errors: hypotheses without 'population', certain conclusions, wrong tails.",
        "Quick-fire choice of test: binomial, Poisson, χ² goodness of fit, contingency, PMCC, Spearman.",
        "Mixed AS exam-style question walkthrough, using one Section B question from each of AS6–AS10.",
    ]),
    "a2_review": ("A2 review: choosing the right test", 30, [
        "Decision flowchart: data type, one or two samples, paired or independent, σ known, normality.",
        "z, t, pooled t, paired t, F, χ² for variance, sign, Wilcoxon signed-rank and rank-sum side by side.",
        "Three exam-style questions where choosing the test is the first mark.",
        "Revision plan and how to use the formula sheet and tables in the exam.",
    ]),
}


def h2s(unit):
    return [n[1] for n in unit["notes"] if n[0] == "h2"]


def boards_for(module):
    row = next(c for m, _, c in book.COVERAGE if m == module)
    labels = {"AS": "AS", "A": "A level", "S3": "S3", "P4": "Paper 4", "P": "prior knowledge"}
    return ", ".join(f"{BOARD_NAMES[b]} ({labels[v]})" for b, v in zip(book.BOARDS, row) if v)


def episode_block(n, module, title, sections, examples, minutes, focus, unit):
    heads = h2s(unit)
    sections = sections or list(range(1, len(heads) + 1))
    examples = examples or list(range(1, len(unit["examples"]) + 1))
    sec_titles = [heads[i - 1] for i in sections]
    ex_titles = [f"Example {unit['number']}.{i} ({unit['examples'][i - 1]['title']})" for i in examples]
    teach = max(6, round(minutes * 0.38))
    work = max(6, round(minutes * 0.36))
    lines = [
        f"### Episode {n}: {title}",
        "",
        f"- **Length:** {minutes} min  ·  **Workbook:** Unit {unit['number']} ({unit['title']})",
        f"- **Exam boards:** {boards_for(module)}",
        f"- **In one sentence:** {focus}",
        f"- **Sections taught:** " + "; ".join(sec_titles),
        f"- **Worked examples on screen:** " + "; ".join(ex_titles),
        "",
        "| Time | Segment |",
        "|---|---|",
        "| 0:00–1:30 | Hook: a real situation the topic answers, then the episode's learning objectives |",
        "| 1:30–3:00 | Quick recap of the prerequisite idea (from the previous episode or unit) |",
        f"| 3:00–{3 + teach}:00 | Teach the sections above from the workbook notes; build each boxed result on screen |",
        f"| {3 + teach}:00–{3 + teach + work}:00 | Worked examples above, step by step; pause point before each solution |",
        f"| {3 + teach + work}:00–{minutes - 2}:00 | Common mistakes (the amber box) and one 'pause and try' question from Section A |",
        f"| {minutes - 2}:00–{minutes}:00 | Summary of key results, homework (Unit {unit['number']} practice on these sections), next episode |",
        "",
    ]
    return lines


def special_block(n, key):
    title, minutes, points = SPECIALS[key]
    lines = [f"### Episode {n}: {title}", "", f"- **Length:** {minutes} min  ·  **Type:** overview / exam technique", ""]
    lines += [f"- {p}" for p in points]
    return lines + [""]


def main():
    units = {}
    missing = []
    for m, _, _ in book.COVERAGE:
        try:
            units[m] = importlib.import_module(f"content.{m}").UNIT
        except ModuleNotFoundError:
            missing.append(m)

    episodes = [("special", "intro")]
    episodes += [("ep", e) for e in EPISODES if e[0].startswith("as")]
    episodes.append(("special", "as_review"))
    episodes += [("ep", e) for e in EPISODES if e[0].startswith("a2")]
    episodes.append(("special", "a2_review"))
    episodes = [e for e in episodes if e[0] == "special" or e[1][0] in units]

    total_min = sum(SPECIALS[e[1]][1] if e[0] == "special" else e[1][4] for e in episodes)
    out = [
        "# Further Mathematics Statistics: YouTube lecture series plan",
        "",
        "A complete lecture series built on the workbook *Further Mathematics: Statistics* "
        "(`Further_Statistics_Workbook.pdf`). Each video teaches **one topic** in **20–30 minutes** and maps to named "
        "sections and worked examples of the workbook, so students can pause, work along and practise.",
        "",
        f"**Size:** {len(episodes)} episodes, about {total_min // 60} hours {total_min % 60} minutes in total. "
        "Part A (AS) and Part B (A2) follow the workbook's order.",
        "",
        "## 1. Audience and promise",
        "",
        "- A-level Further Mathematics students on any board: Edexcel, IAL, AQA, OCR A, OCR MEI or Cambridge 9231.",
        "- Promise to viewers: every Further Statistics topic, taught from first principles to exam standard, with a free "
        "workbook to practise from.",
        "- Each episode lists its exam boards, so students can skip what their board does not examine.",
        "",
        "## 2. Standard episode format (20–30 minutes)",
        "",
        "| Segment | Share | Purpose |",
        "|---|---|---|",
        "| Hook and objectives | ~5% | A real problem the topic solves; 2–3 objectives on screen |",
        "| Prerequisite recap | ~5% | One idea from an earlier episode, so each video stands alone |",
        "| Core teaching | ~38% | Workbook notes: definitions, boxed results, derivations required by the boards |",
        "| Worked examples | ~36% | Workbook examples solved live, with a pause point before each solution |",
        "| Common mistakes and 'pause and try' | ~10% | The amber 'Common mistakes' box, then one Section A question |",
        "| Summary and homework | ~6% | Key results recap, homework from the unit's practice pages, next episode teaser |",
        "",
        "## 3. Production workflow (per episode)",
        "",
        "1. **Script** from the workbook sections and examples listed in the episode card (no new content: the book is "
        "the single source of truth, so numbers on screen always match the answers).",
        "2. **Slides / board:** one slide per boxed result; worked examples written live (tablet) so viewers see the method.",
        "3. **Record** in chapters matching the run sheet; re-record a chapter rather than patching a single line.",
        "4. **Check** every number on screen against the workbook before publishing (the workbook's values were verified with SciPy).",
        "5. **Edit:** add YouTube chapters from the run sheet times, captions (auto-captions corrected for symbols such as "
        "μ, σ, λ, χ²), and an end screen linking the next episode.",
        "6. **Publish** with the description template below and add to the playlists.",
        "",
        "## 4. Playlists and release schedule",
        "",
        "- **Playlists:** 'Further Statistics: complete course' (all episodes in order), 'AS Further Statistics', "
        "'A2 Further Statistics', and one playlist per board (built from the 'Exam boards' line of each card).",
        "- **Release:** two episodes a week takes about six months for the full series. Releasing the AS episodes first "
        "lets Year 12 students follow along during the school year.",
        "- **Batch recording:** record one unit's episodes together (same slides and examples), then edit and release in order.",
        "",
        "## 5. Titles, thumbnails and descriptions",
        "",
        "- **Title pattern:** `<Topic> | A Level Further Maths Statistics | Ep <n>`, e.g. "
        "`The Geometric Distribution | A Level Further Maths Statistics | Ep 6`.",
        "- **Thumbnail:** topic name in large type, the key formula, an 'AS' or 'A2' badge and the episode number; one "
        "consistent colour scheme for the whole series.",
        "- **Description template:** one-paragraph summary · chapter timestamps · exam boards covered · workbook unit and "
        "page reference · link to the workbook · links to the previous and next episodes.",
        "",
        "## 6. Episode guide",
        "",
    ]
    n = 0
    part_heading_done = set()
    for kind, item in episodes:
        if kind == "ep":
            part = "Part A: AS" if item[0].startswith("as") else "Part B: A2"
            if part not in part_heading_done:
                out += [f"## {part}", ""]
                part_heading_done.add(part)
        out += special_block(n, item) if kind == "special" else episode_block(n, *item, units[item[0]])
        n += 1
    out += [
        "## 7. Summary table",
        "",
        "| Ep | Title | Workbook unit | Minutes |",
        "|---|---|---|---|",
    ]
    n = 0
    for kind, item in episodes:
        if kind == "special":
            title, minutes, _ = SPECIALS[item]
            out.append(f"| {n} | {title} | – | {minutes} |")
        else:
            out.append(f"| {n} | {item[1]} | {units[item[0]]['number']} | {item[4]} |")
        n += 1
    if missing:
        out += ["", f"_Units not yet written when this plan was generated: {', '.join(missing)}._"]
    OUT.write_text("\n".join(out) + "\n")
    print("wrote", OUT, len(episodes), "episodes", total_min, "minutes", "missing:", missing)


if __name__ == "__main__":
    main()
