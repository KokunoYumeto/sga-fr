"""Simulate (in memory only, nothing written) the folio-141 and folio-145 marker moves of move_marker.py on both
layers, with and without the text fixes of findings_141_145 applied first."""
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\sga5"


def move(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return None, None
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2, k


for layer in ("diplomatic", "current"):
    t = open(rf"{BASE}\{layer}\s5.tex", encoding="utf-8").read()
    lines = t.split("\n")
    for folio in (141, 145):
        i = next(i for i, l in enumerate(lines) if MARK.search(l) and int(MARK.search(l).group(2)) == folio)
        print(layer, "folio", folio, "marker at line", i + 1, "| previous line ends:", repr(lines[i - 1][-90:]))
    for label, fixes in (("as is", []),
                         ("after text fixes", [("(resp. $E\\in\\ob D_{\\ctf}(Y)$)", "(resp. $D_{\\ctf}(Y)$)"),
                                               ("(loc. cit.), ", "(loc. cit.) "),
                                               ("$u$ la", "$u=$ la")])):
        tt = t
        for o, n in fixes:
            c = tt.count(o)
            tt = tt.replace(o, n, 1) if c == 1 else tt
            if c != 1:
                print("   ", label, "fix old occurs", c, "times in", layer, ":", o)
        for folio, anchor in ((141, "$D_{\\ctf}(X)$ (resp. $D_{\\ctf}(Y)$) est dualisant"), (145, "$u")):
            t2, k = move(tt, folio, anchor, True)
            if t2 is None:
                print("   ", layer, label, folio, "anchor not found")
                continue
            ls = t2.split("\n")
            j = next(j for j, l in enumerate(ls) if MARK.search(l) and int(MARK.search(l).group(2)) == folio)
            print("   ", layer, label, "folio", folio, ": anchor count before marker", tt[:tt.find("folio %d " % folio)].count(anchor),
                  "| line before marker:", repr(ls[j - 1][-70:]), "| page starts:", repr(ls[j + 1][:70]))
