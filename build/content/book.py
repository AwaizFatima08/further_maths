"""Book structure: front matter, the AS and A2 parts, and back matter."""

TITLE = "Further Mathematics: Statistics"
SUBTITLE = "A complete AS and A2 workbook: notes, worked examples, practice, exam-style questions and answers"
COVER_NOTES = [
    "Covers the statistics content of Pearson Edexcel (9FM0/8FM0 and IAL S3), AQA (7367/7366), "
    "OCR A (H245/H235), OCR B MEI (H645/H635) and Cambridge International 9231 Paper 4.",
    "Use the coverage map at the start to see exactly which units your exam board needs.",
]

BOARDS = ["Edexcel", "IAL S3", "AQA", "OCR A", "OCR MEI", "CAIE 9231"]

# Unit module name -> (short title, coverage per board in BOARDS order).
# "AS" = AS and A level; "A" = A level only; "S3" = IAL unit S3; "P4" = CAIE Paper 4;
# "P" = assumed prior knowledge from single Mathematics (useful revision); "" = not on the specification.
COVERAGE = [
    ("as01", "Discrete random variables", ["AS", "P", "AS", "AS", "AS", "P"]),
    ("as02", "Binomial, Poisson and discrete uniform", ["AS", "P", "AS", "AS", "AS", "P"]),
    ("as03", "The geometric distribution", ["A", "", "", "AS", "AS", "P"]),
    ("as04", "Permutations and combinations", ["", "", "", "AS", "", "P"]),
    ("as05", "Sampling methods", ["", "S3", "", "", "AS", "P"]),
    ("as06", "Hypothesis tests: binomial and Poisson", ["AS", "P", "AS", "", "", ""]),
    ("as07", "Chi-squared goodness of fit", ["AS", "S3", "", "AS", "AS", "P4"]),
    ("as08", "Chi-squared contingency tables", ["AS", "S3", "AS", "AS", "AS", "P4"]),
    ("as09", "Correlation", ["AS", "S3", "", "AS", "AS", ""]),
    ("as10", "Regression", ["AS", "P", "", "AS", "AS", ""]),
    ("as11", "Continuous random variables", ["AS", "P", "AS", "A", "A", "P4"]),
    ("as12", "Confidence intervals with the normal distribution", ["A", "S3", "AS", "A", "A", "P"]),
    ("a201", "Cumulative distribution functions and functions of X", ["AS", "P", "A", "A", "A", "P4"]),
    ("a202", "The exponential distribution", ["", "", "A", "A", "", ""]),
    ("a203", "Negative binomial distribution and geometric tests", ["A", "", "", "", "", ""]),
    ("a204", "Probability generating functions", ["A", "", "", "", "", "P4"]),
    ("a205", "Quality of tests: Type I and II errors and power", ["A", "", "A", "", "", ""]),
    ("a206", "Linear combinations of random variables", ["A", "S3", "AS", "A", "A", "P"]),
    ("a207", "Sampling distributions, the CLT and estimators", ["A", "S3", "", "A", "A", "P"]),
    ("a208", "z-tests and intervals: one and two samples", ["A", "S3", "P", "A", "A", "P4"]),
    ("a209", "The t distribution: one-sample tests and intervals", ["A", "", "A", "", "A", "P4"]),
    ("a210", "Two-sample t-tests: pooled and paired", ["A", "", "", "", "A", "P4"]),
    ("a211", "Variances: chi-squared intervals and the F-test", ["A", "", "", "", "", ""]),
    ("a212", "Non-parametric tests 1: the sign test", ["", "", "", "A", "", "P4"]),
    ("a213", "Non-parametric tests 2: Wilcoxon tests", ["", "", "", "A", "A", "P4"]),
    ("a214", "Normal probability plots, software output and simulation", ["", "", "", "", "A", ""]),
]


def label(module):
    """as01 -> 'AS1', a207 -> 'A2.7'."""
    return f"AS{int(module[2:])}" if module.startswith("as") else f"A2.{int(module[2:])}"

FRONT = [
    {
        "title": "How to use this workbook",
        "notes": [
            ("p", "Each unit has three parts: notes with key results in boxes, worked examples to study with a pencil in hand, "
                  "and a practice page. Section A of the practice builds skills one at a time; Section B contains exam-style "
                  "questions with marks. Full answers, written in mark-scheme style for Section B, are at the back."),
            ("bullets", [
                "Read the notes once quickly, then again slowly, copying each boxed result into your own formula notebook.",
                "Cover each worked example's solution and try it yourself first.",
                "Attempt the practice without notes. Mark it, then redo every question you got wrong a week later.",
                "Amber boxes list the mistakes examiners report most often. Read them before every exam.",
            ]),
            ("h2", "Part A and Part B"),
            ("p", "Part A contains AS content (the first year of Further Mathematics). Part B contains the A2 content "
                  "needed for the full A level. Boards split topics differently, so always check the coverage map below."),
            ("h2", "Calculator and tables"),
            ("p", "Every board expects a calculator with statistical distribution functions. The statistical tables at the back "
                  "were computed exactly and match the published booklets, but in the exam use your board's own booklet."),
        ],
    },
    {
        "title": "Coverage map by exam board",
        "notes": [
            ("p", "AS = needed for AS and A level. A = A level only. S3 = in IAL unit S3. P4 = in Cambridge 9231 Paper 4. "
                  "P = assumed prior knowledge from the single Mathematics course (useful revision). A blank cell means the "
                  "unit is not on that specification. Some units contain sections only one board needs; these are marked in the unit."),
            ("table", ["Unit"] + BOARDS, [[f"{label(m)}  {t}"] + c for m, t, c in COVERAGE]),
            ("p", "Edexcel = Pearson Edexcel A level 9FM0 Further Statistics 1 and 2 (AS: 8FM0). IAL S3 = Pearson Edexcel "
                  "International A level Statistics 3 (WST03). AQA = 7367 statistics option (AS: 7366). OCR A = H245 Y542 "
                  "(AS: H235 Y532). OCR MEI = H645 Statistics Major Y422 or Minor Y432 (AS: H635 Y412). CAIE 9231 = Cambridge "
                  "International Further Mathematics Paper 4, Further Probability and Statistics."),
        ],
    },
]

PARTS = [
    {
        "title": "Part A: AS Further Statistics",
        "intro": "Discrete distributions, hypothesis tests, chi-squared tests, correlation, regression and continuous random variables.",
        "units": [m for m, _, _ in COVERAGE if m.startswith("as")],
    },
    {
        "title": "Part B: A2 Further Statistics",
        "intro": "Further distributions, generating functions, the quality of tests, inference with z, t, χ² and F, and non-parametric tests.",
        "units": [m for m, _, _ in COVERAGE if m.startswith("a2")],
    },
]

from content.formulae import SECTION as FORMULA_SHEET  # noqa: E402

BACK = [FORMULA_SHEET]
