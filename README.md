# Further Mathematics: Statistics and Pure

Complete A-level Further Mathematics workbooks for **Statistics** and **Pure**, each with a plan for a YouTube lecture
series built on it. Both cover Pearson Edexcel (9FM0/8FM0 and IAL), AQA (7367/7366), OCR A (H245/H235), OCR B MEI
(H645/H635) and Cambridge International 9231; the coverage map at the front of each book shows which units each board needs.

| Book | Workbook | Lecture series plan |
|---|---|---|
| Statistics: 26 units (12 AS, 14 A2), formula sheet, statistical tables | [Further_Statistics_Workbook.pdf](Further_Statistics_Workbook.pdf) | [YouTube_Lecture_Series_Plan.md](YouTube_Lecture_Series_Plan.md) (52 episodes) |
| Pure: 40 units (14 AS Core, 14 A2 Core, 12 Further Pure options), diagrams, formula sheet | [Further_Pure_Workbook.pdf](Further_Pure_Workbook.pdf) | [YouTube_Pure_Lecture_Series_Plan.md](YouTube_Pure_Lecture_Series_Plan.md) (73 episodes) |

Every unit has notes, worked examples, skills practice, exam-style questions with marks, and full answers.
**[reports/](reports/)** and **[research_notes/](research_notes/)** hold the syllabus comparisons both courses are based
on, with links to the official specifications.

## Rebuilding

Both books and both plans are generated from the Python sources in `build/`:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
cd build
for f in pure/figures/*_figs.py; do ../.venv/bin/python "$f"; done   # draws the pure diagrams (PNGs are not committed)
../.venv/bin/python build_workbook.py stats     # writes ../Further_Statistics_Workbook.pdf
../.venv/bin/python build_workbook.py pure      # writes ../Further_Pure_Workbook.pdf
../.venv/bin/python make_series_plan.py stats   # writes ../YouTube_Lecture_Series_Plan.md
../.venv/bin/python make_series_plan.py pure    # writes ../YouTube_Pure_Lecture_Series_Plan.md
```

- `build/content/` (statistics) and `build/pure/` (pure): one module per unit, plus `book.py` (structure and coverage
  map) and `formulae.py` (formula sheet). Pure diagrams are drawn by `build/pure/figures/<unit>_figs.py`.
- `build/checks/` and `build/checks_pure/`: one script per unit that recomputes every stated result with SciPy or
  SymPy. Run them all after editing a unit.
- `build/tables.py`: computes the statistical tables exactly; results are cached in `build/tables_cache.json`.
- `build/WRITING_GUIDE.md` and `build/PURE_WRITING_GUIDE.md`: the format and accuracy rules every unit follows.
- `build/preview_unit.py`: builds and validates a PDF of selected units, e.g. `preview_unit.py --pure /tmp/x.pdf pa01`.
- `build/check_glyphs.py`: lists any character neither DejaVu font can draw.
- `build/series_pure.py`: the pure episode list (the statistics list is in `make_series_plan.py`).
