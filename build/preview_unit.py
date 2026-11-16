"""Builds a PDF of one or more units, for checking layout while writing.

Usage: python preview_unit.py <output.pdf> <module> [<module> ...]   e.g. preview_unit.py /tmp/x.pdf as01 as02
Also validates each unit's structure and fails loudly on a problem.
"""
import importlib
import sys

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

import build_workbook as bw

NOTE_KINDS = {"h2", "p", "bullets", "box", "warn", "table"}


def validate(name, unit):
    for key in ("number", "title", "tag", "notes", "examples", "practice", "answers", "exam", "exam_answers"):
        assert key in unit, f"{name}: missing key {key!r}"
    for item in unit["notes"]:
        assert item[0] in NOTE_KINDS, f"{name}: unknown note kind {item[0]!r}"
        if item[0] == "table":
            width = len(item[1])
            assert all(len(r) == width for r in item[2]), f"{name}: table row width mismatch in {item[1]}"
    for ex in unit["examples"]:
        assert {"title", "question", "steps"} <= set(ex), f"{name}: bad example {ex.get('title')}"
    assert len(unit["practice"]) == len(unit["answers"]), \
        f"{name}: {len(unit['practice'])} practice questions but {len(unit['answers'])} answers"
    assert len(unit["exam"]) == len(unit["exam_answers"]), \
        f"{name}: {len(unit['exam'])} exam questions but {len(unit['exam_answers'])} exam answers"


def main():
    out, names = sys.argv[1], sys.argv[2:]
    units, story = [], []
    for name in names:
        unit = importlib.import_module(f"content.{name}").UNIT
        validate(name, unit)
        units.append(unit)
        story += bw.build_unit(unit)
    story += bw.build_answers(units)
    doc = bw.Doc(out, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm, topMargin=18 * mm, bottomMargin=18 * mm)
    doc.multiBuild(story)
    print("ok", out, [u["number"] for u in units])


if __name__ == "__main__":
    main()
