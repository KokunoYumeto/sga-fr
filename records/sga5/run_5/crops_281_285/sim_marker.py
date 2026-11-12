"""In-memory simulation of the marker moves of pp. 282 and 284 on both layers (nothing is written), and a check that
each fix's 'old' occurs once in its page span of the live s5.tex of both layers."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")


def move(t, folio, anchor, before):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
    if k < 0:
        return None
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2


def show(t, folio, n=180):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    a = t[max(0, m.start() - n):m.start()]
    b = t[m.end():m.end() + n]
    print("   ...", repr(a[-n:]))
    print("   MARK", folio)
    print("   >>>", repr(b))


def span(t, folio):
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        if int(m.group(2)) == folio:
            return t[m.start():ms[i + 1].start() if i + 1 < len(ms) else len(t)]


findings = json.loads((W / "run_5" / "findings_281_285.json").read_text(encoding="utf-8"))
for ed in ("diplomatic", "current"):
    t = (W / "sga5" / ed / "s5.tex").read_text(encoding="utf-8")
    print("=====", ed)
    # p. 282, before and after the EXPOSÉ VII capitals fix
    for variant in ("as is", "after capitals fix"):
        tt = t if variant == "as is" else t.replace("\\section*{Exposé VII}", "\\section*{EXPOSÉ VII}", 1)
        t2 = move(tt, 282, "\\section*{E", True)
        print("p. 282", variant)
        show(t2, 282, 120)
    # p. 284, anchor before / after the underline fix of 'composé du morphisme bord'
    t2 = move(t, 284, "composé du morphisme", False)
    print("p. 284 before the underline fix")
    show(t2, 284, 150)
    tt = t.replace("composé du morphisme bord", "\\emph{composé du morphisme ``bord''},", 1)
    t2 = move(tt, 284, "\\emph{composé du morphisme", False)
    print("p. 284 after the underline fix")
    show(t2, 284, 150)
    # uniqueness of each old in the live page spans
    for d in findings:
        if d["fix"]:
            s = span(t, d["page"])
            c = s.count(d["fix"]["old"])
            if c != 1:
                print("  live span count", d["page"], c, repr(d["fix"]["old"][:60]))
print("done")
