"""Lists characters in unit text that neither DejaVu Serif nor the DejaVu Sans fallback can draw.

Usage: python check_glyphs.py [content|pure]   (default: both)
"""
import importlib
import json
import pkgutil
import sys
from pathlib import Path

from fontTools.ttLib import TTFont

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
FONTS = [Path("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"), Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")]
# Combining marks render as overlays on the previous character, so allow those the font lacks.
ALLOWED = {"\n"}


def main():
    cmap = set()
    for f in FONTS:  # the builder falls back to DejaVu Sans for characters the serif lacks
        cmap |= set(TTFont(str(f)).getBestCmap())
    packages = sys.argv[1:] or ["content", "pure"]
    bad = {}
    for pkg in packages:
        for info in pkgutil.iter_modules([str(HERE / pkg)]):
            if info.name in ("book", "formulae", "__init__"):
                continue
            unit = importlib.import_module(f"{pkg}.{info.name}").UNIT
            text = json.dumps(unit, ensure_ascii=False)
            for ch in set(text):
                if ord(ch) not in cmap and ch not in ALLOWED:
                    bad.setdefault(f"U+{ord(ch):04X} {ch!r}", []).append(f"{pkg}.{info.name}")
    for ch, where in sorted(bad.items()):
        print(ch, sorted(set(where)))
    print("missing glyphs:", len(bad))


if __name__ == "__main__":
    main()
