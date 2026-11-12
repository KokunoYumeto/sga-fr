"""List lines that consist only of a punctuation mark and follow a display end or a comment line."""
import glob
import os
import sys

folder = sys.argv[1]
for path in sorted(glob.glob(os.path.join(folder, "*.tex"))):
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")
    folio = "?"
    for i, ln in enumerate(lines):
        if ln.startswith("%%%%%%%%%%") and "folio" in ln:
            folio = ln.split("folio")[1].strip(" %")
        if ln.strip() in {",", ".", ";", ":"} and i > 0:
            prev = lines[i - 1].strip()
            nxt = lines[i + 1].strip() if i + 1 < len(lines) else ""
            print(os.path.basename(path), "line", i + 1, "folio", folio, repr(ln.strip()),
                  "| prev:", prev[:50], "| next:", nxt[:50])
