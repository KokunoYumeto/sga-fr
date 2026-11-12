"""Simulate move_marker.py (--before) in memory on both layers of SGA 6 for the folio-157 and folio-159 markers, with
and without the heading fix of this batch applied first. Prints the text around each moved marker. Writes nothing."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
W = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6"
A157 = '\\[\n\\begin{tikzcd}[column sep=large,row sep=large]\n A \\arrow[r,"u\\otL v"] \\arrow[dr,"vu"'
A159 = "\\section*{"
moves = [(157, A157), (159, A159)]


def move(t, folio, anchor):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    if k < 0:
        return None, "anchor not found"
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    m2 = next(m for m in MARK.finditer(t2) if int(m.group(2)) == folio)
    return t2, (m.start() - m2.start(), m2)


for ed in ("diplomatic", "current"):
    for pre in (False, True):
        t = open(W + "\\" + ed + "\\main.tex", encoding="utf-8").read()
        if pre:  # this batch's heading fix (page 158) and diagram-label fixes (page 156) applied first
            for old, new in [("\\section*{Bibliographie}\n\\begin{description}", "\\section*{BIBLIOGRAPHIE}\n\\begin{description}"),
                             ('\\arrow[d,"\\Id\\otimes\\tau_F"] \\\\', '\\arrow[d,"\\Id\\otL\\tau_F"] \\\\'),
                             ('\\arrow[d,"\\tau_E\\otimes\\Id"]', '\\arrow[d,"\\tau_E\\otL\\Id"]')]:
                n = t.count(old)
                print(ed, "pre-fix count", n, repr(old[:30]))
                t = t.replace(old, new, 1)
        for folio, anchor in moves:
            t2, info = move(t, folio, anchor)
            if t2 is None:
                print(ed, "pre" if pre else "no-pre", folio, info)
                continue
            dist, m2 = info
            print("=" * 20, ed, "fixes first" if pre else "markers only", "folio", folio, "moved up by", dist, "chars")
            print(t2[m2.start() - 160:m2.end() + 200])
            t = t2
        # check the remaining square option text after the move
        k = t.find("\\begin{tikzcd}[column sep=\nlarge")
        print(ed, "square options split over two lines:", k >= 0)
