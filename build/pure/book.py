"""Book structure for the Further Pure workbook: front matter, Parts A–C and back matter."""

TITLE = "Further Mathematics: Pure"
SUBTITLE = "A complete AS and A2 Further Pure workbook: notes, worked examples, practice, exam-style questions and answers"
COVER_NOTES = [
    "Covers the pure content of Pearson Edexcel (9FM0/8FM0 Core Pure and Further Pure options, and IAL FP1–FP3), "
    "AQA (7367/7366), OCR A (H245/H235 Pure Core and Additional Pure), OCR B MEI (H645/H635 Core Pure and Extra Pure) "
    "and Cambridge International 9231 Papers 1 and 2.",
    "Use the coverage map at the start to see exactly which units your exam board needs.",
]

BOARDS = ["Edexcel", "IAL", "AQA", "OCR A", "OCR MEI", "CAIE 9231"]

# Unit module -> (short title, coverage per board in BOARDS order).
# "AS" = AS and A level core; "A" = A level core only; "opt" = optional Further Pure paper (Edexcel FP1/FP2,
# OCR A Additional Pure, MEI Extra Pure); "FP1"/"FP2"/"FP3" = IAL unit; "P1"/"P2" = Cambridge paper;
# "pre" = assumed prior knowledge; "" = not on the specification.
COVERAGE = [
    ("pa01", "Complex numbers I: arithmetic and complex roots", ["AS", "FP1", "AS", "AS", "AS", "pre"]),
    ("pa02", "Complex numbers II: Argand diagrams, modulus–argument form and loci", ["AS", "FP1", "AS", "AS", "AS", "pre"]),
    ("pa03", "Roots of polynomial equations", ["AS", "FP1", "AS", "AS", "AS", "P1"]),
    ("pa04", "Summation of series and the method of differences", ["AS", "FP1/FP2", "AS", "A", "AS", "P1"]),
    ("pa05", "Matrices and linear transformations", ["AS", "FP1/FP3", "AS", "AS", "AS", "P1"]),
    ("pa06", "Determinants and inverses", ["AS", "FP1/FP3", "AS", "AS", "AS", "P1"]),
    ("pa07", "Invariant points and invariant lines", ["AS", "", "AS", "AS", "AS", "P1"]),
    ("pa08", "Proof by induction and other methods of proof", ["AS", "FP1", "AS", "AS", "AS", "P1"]),
    ("pa09", "Lines and planes in three dimensions", ["AS", "FP3", "AS", "AS", "AS", "P1"]),
    ("pa10", "The vector product and scalar triple product", ["opt", "FP3", "A", "AS", "A", "P1"]),
    ("pa11", "Three equations in three unknowns and three planes", ["AS", "", "A", "AS", "AS", "P2"]),
    ("pa12", "Distances and intersections in three dimensions", ["AS", "FP3", "AS", "A", "A", "P1"]),
    ("pa13", "Curve sketching, rational functions and inequalities", ["opt", "FP2", "AS", "", "", "P1"]),
    ("pa14", "Volumes of revolution and the mean value of a function", ["AS", "", "AS", "A", "A", ""]),
    ("pb01", "Euler's form and de Moivre's theorem", ["A", "FP2", "A", "A", "A", "P2"]),
    ("pb02", "nth roots and roots of unity", ["A", "FP2", "A", "A", "A", "P2"]),
    ("pb03", "Higher derivatives and Maclaurin series", ["A", "FP2", "AS", "A", "A", "P2"]),
    ("pb04", "Hyperbolic functions", ["A", "FP3", "AS", "A", "A", "P2"]),
    ("pb05", "Calculus of hyperbolic and inverse functions", ["A", "FP3", "A", "A", "A", "P2"]),
    ("pb06", "Further integration techniques", ["A", "FP3", "A", "A", "A", "P2"]),
    ("pb07", "Improper integrals and integrals as limits of sums", ["A", "", "A", "A", "A", "P2"]),
    ("pb08", "Polar coordinates", ["A", "FP2", "AS", "A", "A", "P1"]),
    ("pb09", "First-order differential equations", ["A", "FP2", "A", "A", "A", "P2"]),
    ("pb10", "Second-order differential equations", ["A", "FP2", "A", "A", "A", "P2"]),
    ("pb11", "Modelling with differential equations: SHM, damping and coupled systems", ["A", "", "A", "A", "A", ""]),
    ("pb12", "Eigenvalues, eigenvectors and diagonalisation", ["opt", "FP3", "A", "", "opt", "P2"]),
    ("pb13", "Reduction formulae, arc length and surface area", ["opt", "FP3", "A", "opt", "", "P2"]),
    ("pb14", "Numerical methods", ["opt", "FP1", "A", "", "", ""]),
    ("pc01", "Further trigonometry and the t-substitution", ["opt", "", "", "", "", ""]),
    ("pc02", "Taylor series, limits, L'Hôpital's rule and Leibnitz's theorem", ["opt", "FP2", "A", "", "", ""]),
    ("pc03", "Further differential equations: substitutions and series solutions", ["opt", "FP2", "", "", "", "P2"]),
    ("pc04", "Conics I: the parabola and the rectangular hyperbola", ["opt", "FP1", "AS", "", "", ""]),
    ("pc05", "Conics II: the ellipse and the hyperbola", ["opt", "FP3", "", "", "", ""]),
    ("pc06", "Further complex numbers: loci and transformations", ["opt", "FP2", "", "", "", ""]),
    ("pc07", "Groups I: axioms, subgroups and Lagrange's theorem", ["opt", "", "", "opt", "opt", ""]),
    ("pc08", "Groups II: structure and isomorphism", ["opt", "", "", "opt", "opt", ""]),
    ("pc09", "Number theory I: division, Euclid's algorithm and counting", ["opt", "", "", "opt", "", ""]),
    ("pc10", "Number theory II: modular arithmetic and Fermat's little theorem", ["opt", "", "", "opt", "", ""]),
    ("pc11", "Recurrence relations", ["opt", "", "", "opt", "opt", ""]),
    ("pc12", "Surfaces and partial differentiation", ["", "", "", "opt", "opt", ""]),
]


def label(module):
    """pa01 -> 'A1', pb12 -> 'B12', pc03 -> 'C3'."""
    return f"{module[1].upper()}{int(module[2:])}"


ROUTES = [
    "Edexcel AS (8FM0): Core Pure A1–A9, A11, A12, A14 (A4 sums only, A14 volumes only). AS Further Pure 1 adds A10, A13, "
    "B14, C1, C4. AS Further Pure 2 adds B12 (2 × 2 only), C6, C7, C9, C10, C11.",
    "Edexcel A level (9FM0): Core Pure is all of Part A except A10 and A13, plus B1–B11. Further Pure 1 adds A10, A13, B14, "
    "C1–C5. Further Pure 2 adds B12, B13, C6–C11.",
    "IAL: FP1 = A1–A6, A8, B14, C4. FP2 = A4 (differences), A13, B1–B3, B8–B10, C2, C3, C6. FP3 = A5–A6 (3 × 3 parts), "
    "A9, A10, A12, B4–B6, B12, B13, C5.",
    "AQA AS: A1–A9, A12–A14 (A9 and A12 for lines only), with B3 (standard series), B4 (definitions and log forms), B8 "
    "(sketching) and C4 (sketching conics). A level adds A10, A11, B1–B14 and C2.",
    "OCR A AS: A1–A3, A5–A11 (A9 lines, A10 vector product, A11 one point only). A level adds A4, A12, A14, B1–B11. "
    "Additional Pure (Y545) adds A10 (triple product), B13 (8.06), C7–C12.",
    "OCR MEI AS (Y410): A1–A9 and A11 (A9 planes only). Core Pure (Y420) adds A10, A12, A14, B1–B11. Extra Pure (Y435) "
    "adds B12, C7, C8, C11, C12.",
    "Cambridge 9231: revise A1, A2 and lines (A9) from 9709. Paper 1 = A3–A10, A12, A13, B8. Paper 2 = A11, B1–B7, B9, B10, "
    "B12, B13, C3.",
]

FRONT = [
    {
        "title": "How to use this workbook",
        "notes": [
            ("p", "Each unit has three parts: notes with key results in boxes, worked examples to study with a pencil in hand, "
                  "and a practice page. Section A of the practice builds skills one at a time; Section B contains exam-style "
                  "questions with marks. Full answers, in mark-scheme style for Section B, are at the back."),
            ("bullets", [
                "Read the notes once quickly, then again slowly, copying each boxed result into your own formula notebook.",
                "Cover each worked example's solution and try it yourself first. Draw every diagram yourself.",
                "Attempt the practice without notes. Mark it, then redo every question you got wrong a week later.",
                "Amber boxes list the mistakes examiners report most often. Read them before every exam.",
            ]),
            ("h2", "Parts A, B and C"),
            ("p", "Part A contains AS Core Pure content (the first year). Part B contains A2 Core Pure content. Part C contains "
                  "the optional Further Pure papers and single-board topics. Boards split topics differently, so always check "
                  "the coverage map and route list that follow."),
            ("h2", "Notation"),
            ("p", "Matrices are written row by row inside brackets with rows separated by semicolons, so M = (2 1; 0 3) has first "
                  "row 2, 1 and second row 0, 3. When entries are expressions, commas separate the entries in a row, as in "
                  "(2n + 1, −4n; n, 1 − 2n). Vectors are written in bold, as column vectors (1, 2, −3)ᵀ, or with i, j, k."),
        ],
    },
    {
        "title": "Coverage map by exam board",
        "notes": [
            ("p", "AS = AS and A level core. A = A level core only. opt = an optional Further Pure paper (Edexcel FP1/FP2, "
                  "OCR A Additional Pure, MEI Extra Pure). FP1, FP2, FP3 = IAL unit. P1, P2 = Cambridge Paper 1 or 2. "
                  "pre = assumed prior knowledge (useful revision). Blank = not on that specification. Units whose sections "
                  "differ by board are labelled inside the unit."),
            ("table", ["Unit"] + BOARDS, [[f"{label(m)}  {t}"] + c for m, t, c in COVERAGE]),
            ("h2", "Route through the book for each board"),
            ("bullets", ROUTES),
        ],
    },
]

PARTS = [
    {
        "title": "Part A: AS Core Pure",
        "intro": "Complex numbers, roots of polynomials, series, matrices, proof, vectors, curve sketching and volumes.",
        "units": [m for m, _, _ in COVERAGE if m.startswith("pa")],
    },
    {
        "title": "Part B: A2 Core Pure",
        "intro": "De Moivre's theorem, Maclaurin series, hyperbolic functions, further calculus, polar coordinates, "
                 "differential equations, eigenvalues and numerical methods.",
        "units": [m for m, _, _ in COVERAGE if m.startswith("pb")],
    },
    {
        "title": "Part C: Further Pure options",
        "intro": "Further trigonometry and calculus, conics, further complex numbers, groups, number theory, recurrence "
                 "relations and surfaces.",
        "units": [m for m, _, _ in COVERAGE if m.startswith("pc")],
    },
]

try:
    from pure.formulae import SECTION as FORMULA_SHEET
    BACK = [FORMULA_SHEET]
except ModuleNotFoundError:
    BACK = []
