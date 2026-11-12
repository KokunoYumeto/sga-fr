"""In memory: apply each move once, then once more, and report what the second run would do (no writes)."""
import pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
BR = "\\" + "["
moves = [(406, "\section*{Références}"), (407, "\section*{Exposé XII}"), (408, "\section*{1.}"), (411, BR)]

def move(t, folio, anchor):
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind(anchor, 0, m.start())
    if k < 0:
        return t, "anchor not found"
    ls = t2.rfind("\n", 0, k) + 1
    if t2[ls:k].strip() == "":
        t2 = t2[:ls] + line + "\n" + t2[ls:]
    else:
        t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
    return t2, f"moved back {m.start() - k} chars"

for edition in ("diplomatic", "current"):
    t = (W / "sga5" / edition / "s5.tex").read_text(encoding="utf-8")
    for folio, anchor in moves:
        print(edition, folio, "occurrences of anchor in file:", t.count(anchor) if anchor != BR else "n/a")
        t, r1 = move(t, folio, anchor)
        t3, r2 = move(t, folio, anchor)
        print("   first run:", r1, "| second run would:", r2)
