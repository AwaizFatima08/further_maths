# Writing guide for workbook units

The workbook is an A-level Further Mathematics **Statistics** course covering every major exam board
(Pearson Edexcel 9FM0/8FM0 and IAL S3, AQA 7367/7366, OCR A H245/H235, OCR B MEI H645/H635, Cambridge 9231 Paper 4).
Part A = AS units (`as01`–`as12`), Part B = A2 units (`a201`–`a213`). The unit list and board coverage
are in `content/book.py` (`COVERAGE`). The goal is a **thorough, exam-accurate, error-free** workbook a student
can learn the whole topic from, and a teacher can turn into a 20–30 minute lecture per unit.

## Sources you must use
- Board-by-board spec content: `/mnt/storage/projects/further_maths/research_notes/Further Maths statistics syllabus comparison/`
  (`edexcel.md`, `aqa.md`, `ocr.md`, `cambridge.md`). Cover **every** spec point any board lists for your unit.
  Where only some boards need a section, mark the heading, e.g. `"4.3 Yates' correction (AQA A level, OCR A)"`.
- Earlier draft units `content/u01.py` … `content/u13.py` may be reused and expanded (their answers were checked).
- Statistical tables in the book: `tables_cache.json` (built by `tables.py`). Any critical value you quote must agree
  with these tables (to the precision printed), or with scipy.

## File format
One Python module per unit: `content/<module>.py` defining `UNIT = {...}` with these keys (all required):

```python
UNIT = {
    "number": "AS1",            # label: as01 -> "AS1", a207 -> "A2.7"
    "title": "...",             # matches COVERAGE title (you may lengthen slightly)
    "tag": "AS · Edexcel FS1, AQA, OCR A, OCR MEI · prior knowledge for IAL S3, CAIE 9231 P4",
    "notes": [ ... ],           # see kinds below
    "examples": [ {"title": ..., "question": ..., "steps": [..]} , ...],
    "practice": [ "...", ... ], # Section A skills questions
    "answers": [ "...", ... ],  # one per practice question, same order
    "exam": [ "...", ... ],     # Section B exam-style questions with marks
    "exam_answers": [ "...", ... ],  # one per exam question, mark-scheme style
}
```

Note kinds (tuples):
- `("h2", "3.2 Heading")` — numbered sub-heading.
- `("p", "paragraph")`
- `("bullets", ["...", "..."])`
- `("box", "Title", ["line", "line"])` — key results/definitions (teal box).
- `("warn", "Common mistakes", ["...", "..."])` — examiner-report style pitfalls (amber box). At least one per unit.
- `("table", ["header", ...], [["cell", ...], ...])` — every row must have the same number of cells as the header.

Run `python preview_unit.py <out.pdf> <module>`; it validates the structure (e.g. practice/answers counts).

## Text conventions
- Plain British English, short sentences, active voice. Explain *why*, not just *what*. Define every term on first use.
- Maths in Unicode, not LaTeX: x̄, μ, σ², λ, ρ, χ², Σ, ≤, ≥, ≠, √, ∫, Φ, ×, −, ±, ≈, subscripts (X₁, H₀) and superscripts (x², e⁻²).
  Write exponents of expressions as e^(−λt) or (1 − p)^(x−1). Use “−” (minus sign), not “-”, in maths.
- Inline tags allowed: `<b>`, `<i>`, `<sub>`, `<sup>` (anything else is escaped). Do not use `&` entities.
- Hypothesis tests: always define the parameter, state H₀ and H₁ with “population” where boards require it, state the
  distribution under H₀, compare, and conclude in context without certainty (“There is sufficient evidence at the 5% level…”).
- Give final answers to 3 significant figures (probabilities 4 d.p. where natural), and say so.

## Required depth per unit
- **Notes:** cover every spec point for the unit across boards: definitions, results with derivations/proofs where any
  spec requires them (say which), conditions/assumptions, interpretation, calculator use, links to other units.
  Typically 4–8 numbered sub-sections, 2–3 boxes, ≥ 1 table where helpful, ≥ 1 warn box.
- **Worked examples:** 4–6, from routine to full exam standard, with every step shown and a context conclusion.
- **Practice Section A:** 10–12 graded questions.
- **Section B:** 3–4 multi-part exam-style questions, each part with marks, e.g. “(a) ... [3]”, total ≈ 8–14 marks each.
- **Answers:** concise but complete; Section B answers in mark-scheme style (method and key values), final answers clear.

## Accuracy (non-negotiable)
- Every numerical value in examples and answers must be **verified with scipy/numpy**. For each unit write
  `checks/<module>_check.py` that recomputes every number you state and asserts it matches to the stated precision;
  run it with `/tmp/claude-1000/-home-humayun--claude-spares-spare-6mcEcv/427967dc-a307-4d51-8e58-671e5acb832a/scratchpad/pdfenv/bin/python` (has scipy, numpy, reportlab).
- Check every question is solvable from the data given, and that question and answer agree (same numbers, same rounding).
- Render your preview PDF to PNG (`pdftoppm -r 70 -png`) and look at a few pages to confirm symbols render and nothing overflows.

## Scope discipline
- Only create/edit your own `content/<module>.py` and `checks/<module>_check.py` files. Do not edit `build_workbook.py`,
  `book.py`, `tables.py`, or other writers' units. Use scratch output paths for preview PDFs/PNGs, not the project root.
