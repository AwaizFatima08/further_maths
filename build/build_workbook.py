"""Builds a workbook PDF from unit modules.

Usage: python build_workbook.py [stats|pure]   (default stats)
  stats -> units in content/, writes ../Further_Statistics_Workbook.pdf (with statistical tables)
  pure  -> units in pure/,    writes ../Further_Pure_Workbook.pdf
Figures referenced by units live in <package>/figures/.
"""
import importlib
import re
import sys
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    CondPageBreak, Image, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

# book name -> (unit package, output file, include statistical tables)
BOOKS = {
    "stats": ("content", "Further_Statistics_Workbook.pdf", True),
    "pure": ("pure", "Further_Pure_Workbook.pdf", False),
}
PACKAGE = "content"  # set by main(); used to locate figures

import tables  # noqa: E402

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
for name, file in [("Body", "DejaVuSerif.ttf"), ("BodyB", "DejaVuSerif-Bold.ttf"),
                   ("BodyI", "DejaVuSerif-Italic.ttf"), ("Sans", "DejaVuSans.ttf"),
                   ("SansB", "DejaVuSans-Bold.ttf"), ("Mono", "DejaVuSansMono.ttf")]:
    pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / file)))
registerFontFamily("Body", normal="Body", bold="BodyB", italic="BodyI", boldItalic="BodyB")
registerFontFamily("Sans", normal="Sans", bold="SansB", italic="Sans", boldItalic="SansB")

NAVY = colors.HexColor("#1F3A5F")
TEAL = colors.HexColor("#E8F1F5")
AMBER = colors.HexColor("#FFF5E0")
RED = colors.HexColor("#8A2C1E")
GRID = colors.HexColor("#9AAABB")
LIGHT = colors.HexColor("#F4F6F8")
WIDTH = 170 * mm

S = {
    "title": ParagraphStyle("title", fontName="SansB", fontSize=28, leading=34, alignment=TA_CENTER, textColor=NAVY, spaceAfter=14),
    "subtitle": ParagraphStyle("subtitle", fontName="Sans", fontSize=13, leading=18, alignment=TA_CENTER, spaceAfter=8),
    "part": ParagraphStyle("part", fontName="SansB", fontSize=26, leading=32, alignment=TA_CENTER, textColor=NAVY, spaceBefore=80, spaceAfter=16),
    "h1": ParagraphStyle("h1", fontName="SansB", fontSize=18, leading=23, textColor=NAVY, spaceBefore=4, spaceAfter=6),
    "tag": ParagraphStyle("tag", fontName="Sans", fontSize=8.5, leading=11, textColor=colors.grey, spaceAfter=8),
    "h2": ParagraphStyle("h2", fontName="SansB", fontSize=12.5, leading=16, textColor=NAVY, spaceBefore=10, spaceAfter=4, keepWithNext=1),
    "body": ParagraphStyle("body", fontName="Body", fontSize=10.5, leading=16, spaceAfter=6),
    "bullet": ParagraphStyle("bullet", fontName="Body", fontSize=10.5, leading=15, leftIndent=14, bulletIndent=4, spaceAfter=3),
    "box": ParagraphStyle("box", fontName="Body", fontSize=10.2, leading=15.5),
    "boxh": ParagraphStyle("boxh", fontName="SansB", fontSize=10.5, leading=14, textColor=NAVY),
    "warnh": ParagraphStyle("warnh", fontName="SansB", fontSize=10.5, leading=14, textColor=RED),
    "step": ParagraphStyle("step", fontName="Body", fontSize=10.2, leading=15.5, leftIndent=12, spaceAfter=3),
    "q": ParagraphStyle("q", fontName="Body", fontSize=10.5, leading=16, leftIndent=30, bulletIndent=0, spaceAfter=7),
    "ans": ParagraphStyle("ans", fontName="Body", fontSize=9.8, leading=14.5, leftIndent=30, spaceAfter=4),
    "cell": ParagraphStyle("cell", fontName="Body", fontSize=8.6, leading=10.5),
    "cellh": ParagraphStyle("cellh", fontName="SansB", fontSize=8.6, leading=10.5),
    "tcell": ParagraphStyle("tcell", fontName="Mono", fontSize=6.6, leading=8, alignment=TA_CENTER),
    "tcellh": ParagraphStyle("tcellh", fontName="SansB", fontSize=6.8, leading=8.2, alignment=TA_CENTER),
    "toc0": ParagraphStyle("toc0", fontName="SansB", fontSize=11, leading=16, spaceBefore=6),
    "toc1": ParagraphStyle("toc1", fontName="Body", fontSize=10, leading=14, leftIndent=14),
    "caption": ParagraphStyle("caption", fontName="Sans", fontSize=8.5, leading=11, alignment=TA_CENTER,
                              textColor=colors.HexColor("#444444"), spaceAfter=8),
}

INLINE = {"<b>": "<b>", "</b>": "</b>", "<i>": "<i>", "</i>": "</i>",
          "<sub>": "<sub>", "</sub>": "</sub>", "<sup>": "<super>", "</sup>": "</super>"}


def _cmap(file):
    from fontTools.ttLib import TTFont as FTFont
    return set(FTFont(str(FONT_DIR / file)).getBestCmap())


SERIF_CHARS = _cmap("DejaVuSerif.ttf")
SANS_CHARS = _cmap("DejaVuSans.ttf")


def fallback(text):
    """Draw characters the serif font lacks (e.g. ✓ ≅ ∎) with DejaVu Sans instead of a blank box."""
    return "".join(f'<font name="Sans">{ch}</font>' if ord(ch) not in SERIF_CHARS and ord(ch) in SANS_CHARS
                   else ch for ch in text)


def esc(text):
    out = str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    for tag, repl in INLINE.items():
        out = out.replace(tag.replace("<", "&lt;").replace(">", "&gt;"), repl)
    return fallback(out).replace("\n", "<br/>")


def para(text, style="body"):
    return Paragraph(esc(text), S[style])


def box(title, paras, color=TEAL, title_style="boxh", border=NAVY):
    flow = [para(title, title_style)] + [para(p, "box") for p in paras]
    t = Table([[flow]], colWidths=[WIDTH])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), color), ("BOX", (0, 0), (-1, -1), 0.6, border),
        ("LEFTPADDING", (0, 0), (-1, -1), 8), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))
    return [t, Spacer(1, 6)]


def data_table(header, rows, col_widths=None, cell="cell", cellh="cellh", repeat=1):
    data = [[para(h, cellh) for h in header]] + [[para(c, cell) for c in r] for r in rows]
    t = Table(data, colWidths=col_widths, repeatRows=repeat, hAlign="LEFT")
    t.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.4, GRID), ("BACKGROUND", (0, 0), (-1, 0), TEAL),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
        ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    return [t, Spacer(1, 8)]


PART_RE = re.compile(r"(?<=[\].:?])\s+\(([a-h])\)\s")


def split_parts(text):
    """Put each lettered part (a), (b), ... of an exam question or answer on its own line."""
    if "\n" in text:
        return text
    return PART_RE.sub(lambda m: f"\n({m.group(1)}) ", text)


def figure(filename, caption="", width_mm=110):
    """A centred figure from <package>/figures/, scaled to width_mm, with an optional caption."""
    path = HERE / PACKAGE / "figures" / filename
    if not path.exists():
        raise FileNotFoundError(f"figure not found: {path}")
    img = Image(str(path))
    scale = width_mm * mm / img.imageWidth
    img.drawWidth, img.drawHeight = img.imageWidth * scale, img.imageHeight * scale
    flow = [img]
    if caption:
        flow.append(para(caption, "caption"))
    return [KeepTogether(flow), Spacer(1, 4)]


class Heading(Paragraph):
    """A heading that registers itself in the table of contents."""

    def __init__(self, text, style, level):
        super().__init__(esc(text), S[style])
        self.toc_level = level
        self.toc_text = text


def notes_flow(items):
    story = []
    for item in items:
        kind = item[0]
        if kind == "h2":
            story += [CondPageBreak(40 * mm), para(item[1], "h2")]
        elif kind == "p":
            story.append(para(item[1]))
        elif kind == "bullets":
            story += [Paragraph(esc(b), S["bullet"], bulletText="•") for b in item[1]]
        elif kind == "box":
            story += box(item[1], item[2])
        elif kind == "warn":
            story += box(item[1], item[2], color=AMBER, title_style="warnh", border=RED)
        elif kind == "table":
            n = len(item[1])
            widths = None
            if n >= 5:  # wide tables: give the label column room, share the rest equally
                first = WIDTH * 0.34
                widths = [first] + [(WIDTH - first) / (n - 1)] * (n - 1)
            story += data_table(item[1], item[2], widths)
        elif kind == "figure":
            story += figure(*item[1:])
        else:
            raise ValueError(f"unknown note kind {kind}")
    return story


def build_unit(unit):
    story = [Heading(f"Unit {unit['number']}: {unit['title']}", "h1", 1)]
    tag = unit.get("tag")
    if tag:
        story.append(para(tag, "tag"))
    story += notes_flow(unit["notes"])
    for ex in unit["examples"]:
        flow = [para(f"<b>Worked example {unit['number']}.{unit['examples'].index(ex) + 1}: {ex['title']}</b>", "h2"),
                para(ex["question"])]
        if ex.get("figure"):
            flow += figure(ex["figure"], ex.get("caption", ""), ex.get("width_mm", 100))
        flow += [para(s, "step") for s in ex["steps"]]
        story += [KeepTogether(flow), Spacer(1, 6)]
    story.append(PageBreak())
    story.append(para(f"Unit {unit['number']} practice", "h1"))
    story.append(para("Section A builds skills; Section B is exam style, with marks shown. Answers are at the back."))
    story.append(para("Section A: skills practice", "h2"))
    for i, q in enumerate(unit["practice"], 1):
        story.append(Paragraph(esc(split_parts(q)), S["q"], bulletText=f"{unit['number']}.{i}"))
        for fig in unit.get("practice_figures", {}).get(i, []):
            story += figure(*fig)
    exam = unit.get("exam", [])
    if exam:
        story.append(para("Section B: exam-style questions", "h2"))
        start = len(unit["practice"])
        for j, q in enumerate(exam, start + 1):
            story.append(Paragraph(esc(split_parts(q)), S["q"], bulletText=f"{unit['number']}.{j}"))
            for fig in unit.get("practice_figures", {}).get(j, []):
                story += figure(*fig)
    story.append(PageBreak())
    return story


def build_answers(units):
    story = [Heading("Answers", "h1", 0)]
    for unit in units:
        story.append(CondPageBreak(30 * mm))
        story.append(para(f"Unit {unit['number']}: {unit['title']}", "h2"))
        answers = [split_parts(a) for a in unit["answers"] + unit.get("exam_answers", [])]
        for i, a in enumerate(answers, 1):
            story.append(Paragraph(esc(a), S["ans"], bulletText=f"{unit['number']}.{i}"))
    return story


def build_tables():
    story = [Heading("Statistical tables", "h1", 0),
             para("All values were computed exactly with the SciPy library. Layouts differ slightly "
                  "from exam-board booklets; in the exam, always use the booklet your board provides.")]
    for title, header, rows in tables.compute_all():
        n = len(header)
        widths = [WIDTH / n] * n
        story.append(CondPageBreak(60 * mm))
        story.append(para(title, "h2"))
        story += data_table(header, rows, widths, cell="tcell", cellh="tcellh")
    return story


class Doc(SimpleDocTemplate):
    def afterFlowable(self, flowable):
        if isinstance(flowable, Heading):
            self.notify("TOCEntry", (flowable.toc_level, flowable.toc_text, self.page))


def main():
    global PACKAGE
    name = sys.argv[1] if len(sys.argv) > 1 else "stats"
    PACKAGE, out_name, with_tables = BOOKS[name]
    out = HERE.parent / out_name
    book = importlib.import_module(f"{PACKAGE}.book")
    toc = TableOfContents()
    toc.levelStyles = [S["toc0"], S["toc1"]]

    story = [Spacer(1, 50 * mm), para(book.TITLE, "title"), para(book.SUBTITLE, "subtitle"),
             Spacer(1, 10 * mm)]
    story += [para(p, "subtitle") for p in book.COVER_NOTES]
    story += [PageBreak(), para("Contents", "h1"), toc, PageBreak()]
    for section in book.FRONT:
        story.append(Heading(section["title"], "h1", 0))
        story += notes_flow(section["notes"])
        story.append(PageBreak())

    units = []
    for part in book.PARTS:
        story += [Heading(part["title"], "part", 0), para(part["intro"], "subtitle"), PageBreak()]
        for name in part["units"]:
            unit = importlib.import_module(f"{PACKAGE}.{name}").UNIT
            units.append(unit)
            story += build_unit(unit)

    for section in book.BACK:
        story.append(Heading(section["title"], "h1", 0))
        story += notes_flow(section["notes"])
        story.append(PageBreak())
    if with_tables:
        story += build_tables()
        story.append(PageBreak())
    story += build_answers(units)

    def footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("Sans", 8)
        canvas.setFillColor(colors.grey)
        canvas.drawCentredString(A4[0] / 2, 11 * mm, f"{book.TITLE}  |  page {doc.page}")
        canvas.restoreState()

    doc = Doc(str(out), pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm,
              topMargin=18 * mm, bottomMargin=18 * mm, title=book.TITLE, author="Further Maths")
    doc.multiBuild(story, onFirstPage=lambda c, d: None, onLaterPages=footer)
    print("wrote", out)


if __name__ == "__main__":
    main()
