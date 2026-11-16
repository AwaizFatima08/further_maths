# Writing guide for Further Pure units

Read `WRITING_GUIDE.md` first: everything in it applies (file format, text conventions, depth, scope discipline),
with the differences below. The pure book lives in `build/pure/` (package `pure`); its structure and board coverage
are in `pure/book.py` (`COVERAGE`).

## Sources
- Board-by-board spec content: `/mnt/storage/projects/further_maths/research_notes/Further Maths pure syllabus comparison/`
  and the report `/mnt/storage/projects/further_maths/reports/Further Maths pure syllabus comparison.md`.
  Cover every spec point any board lists for your unit; label board-only sections in the heading.

## Files you create
- `pure/<module>.py` with `UNIT = {...}` (same keys as statistics units; `number` is the label in `pure/book.py`).
- `checks_pure/<module>_check.py` verifying every result (see below).
- `pure/figures/<module>_figs.py` (only if the unit has diagrams): a matplotlib script that writes PNGs named
  `<module>_<name>.png` into `pure/figures/`. Run it so the PNGs exist.

## Figures
- In notes: `("figure", "<module>_<name>.png", "Caption text", width_mm)` (width_mm optional, default 110).
- In a worked example: add keys `"figure": "<module>_<name>.png", "caption": "...", "width_mm": 100` to the example dict.
- Under a practice question: `"practice_figures": {question_number: [("<file>.png", "caption", width_mm)]}` (1-based,
  counting Section A then Section B continuously, as printed).
- Style: white background, dpi 200, figure size about 6 × 4 inches, DejaVu Sans, black/navy (#1F3A5F) lines, axes through
  the origin where natural, labelled axes and key points, grid off, no titles inside the image (use the caption).
- Draw a figure wherever a student would sketch one: Argand diagrams and loci, polar curves, graphs of rational and
  hyperbolic functions with asymptotes, regions for volumes and areas, transformations of the unit square, lines and
  planes, solution curves of differential equations, numerical methods (rectangles, Euler steps).

## Mathematical notation
- Unicode as in the statistics guide. Use 𝐢/i for √−1 consistently as `i`; vectors in bold with `<b>a</b>` or as
  column vectors written (1, 2, −3)ᵀ or as i, j, k components; matrices written row by row, e.g. M = (2 1; 0 3), and
  define this notation once in the unit. Use “arsinh/arcosh/artanh” (and mention sinh⁻¹ alternatives).
- Integrals: ∫₀¹ f(x) dx; limits in subscript/superscript Unicode where possible, otherwise “from a to b”.
- Proofs (induction, de Moivre, standard results) must be complete and set out the way mark schemes expect:
  basis, assumption, inductive step, conclusion sentence.

## Accuracy (non-negotiable)
- Every algebraic and numerical result in notes, examples and answers must be **verified with SymPy (and NumPy/SciPy
  for numerics)** in `checks_pure/<module>_check.py`: simplify differences to zero, check roots, sums, integrals,
  derivatives, eigenvalues, series coefficients, solutions of differential equations (substitute back), and numerical
  answers to the stated precision. Assert each check; print a final pass line.
- Python: `/tmp/claude-1000/-home-humayun--claude-spares-spare-6mcEcv/427967dc-a307-4d51-8e58-671e5acb832a/scratchpad/pdfenv/bin/python`
  (has sympy, numpy, scipy, matplotlib, reportlab).
- Build a preview: `python preview_unit.py --pure <scratch.pdf> <module>`, render with `pdftoppm -r 70 -png`, and
  look at pages with figures, boxes and long formulae to confirm nothing overflows and every symbol renders.

## Scope discipline
Only create/edit your own `pure/<module>.py`, `checks_pure/<module>_check.py` and `pure/figures/<module>_*` files.
