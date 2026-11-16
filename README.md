# Further Mathematics: Statistics

A complete AS and A2 workbook for A-level Further Mathematics Statistics, and a plan for a YouTube lecture series built on it.

- **[Further_Statistics_Workbook.pdf](Further_Statistics_Workbook.pdf)**: 26 units (12 AS, 14 A2) with notes, worked examples,
  practice and exam-style questions, a formula sheet, statistical tables and full answers. Covers Pearson Edexcel
  (9FM0/8FM0 and IAL S3), AQA (7367/7366), OCR A (H245/H235), OCR B MEI (H645/H635) and Cambridge International 9231 Paper 4;
  the coverage map at the front shows which units each board needs.
- **[YouTube_Lecture_Series_Plan.md](YouTube_Lecture_Series_Plan.md)**: 52 episodes of 20–30 minutes, one topic each, mapped to
  workbook sections and worked examples.
- **[reports/](reports/)** and **[research_notes/](research_notes/)**: the syllabus comparison the course is based on, with links
  to the official specifications.

## Rebuilding

The workbook and plan are generated from the Python sources in `build/`:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
cd build
../.venv/bin/python build_workbook.py      # writes ../Further_Statistics_Workbook.pdf
../.venv/bin/python make_series_plan.py    # writes ../YouTube_Lecture_Series_Plan.md
```

- `build/content/`: one module per unit (`as01`–`as12`, `a201`–`a214`), plus `book.py` (structure and coverage map) and `formulae.py`.
- `build/checks/`: one script per unit that recomputes every number stated in it with SciPy. Run them all after editing a unit.
- `build/tables.py`: computes the statistical tables exactly; results are cached in `build/tables_cache.json`
  (delete it to recompute, which takes about a minute).
- `build/WRITING_GUIDE.md`: the format and accuracy rules every unit follows.
- `build/preview_unit.py`: builds and validates a PDF of selected units, e.g. `preview_unit.py /tmp/x.pdf as07`.
