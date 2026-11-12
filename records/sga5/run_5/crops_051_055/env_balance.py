"""Read-only: check the nesting of \\begin{prooftext} / \\end{prooftext} in both layers of s5.tex; print unmatched ones
with their line and folio."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
TOK = re.compile(r"\\begin\{prooftext\}|\\end\{prooftext\}")
for layer in ("diplomatic", "current"):
    t = (pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5") / layer / "s5.tex").read_text(
        encoding="utf-8")
    marks = [(m.start(), int(m.group(2))) for m in MARK.finditer(t)]

    def where(pos):
        f = None
        for p, fo in marks:
            if p > pos:
                break
            f = fo
        return t.count("\n", 0, pos) + 1, f

    stack, bad = [], []
    nb = ne = 0
    for m in TOK.finditer(t):
        if m.group(0).startswith("\\begin"):
            nb += 1
            stack.append(m.start())
        else:
            ne += 1
            if stack:
                stack.pop()
            else:
                bad.append(("unmatched end",) + where(m.start()))
    bad += [("unclosed begin",) + where(p) for p in stack]
    print(layer, "begin", nb, "end", ne, bad[:10])
