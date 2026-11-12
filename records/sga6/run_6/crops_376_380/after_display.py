"""List the text lines that follow a display directly (no blank line) in page_NNN.tex files.
usage: python -I after_display.py FILE..."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
END = re.compile(r"^(\\\]|\\end\{equation\*?\}|\\end\{align\*?\}|\\end\{gather\*?\})\s*$")
for fn in sys.argv[1:]:
    lines = open(fn, encoding="utf-8").read().split("\n")
    for i, l in enumerate(lines[:-1]):
        if END.match(l.strip()) and lines[i + 1].strip() and not lines[i + 1].startswith("%"):
            print(fn.split("\\")[-1].split("/")[-1], i + 2, repr(lines[i + 1][:60]))
