"""Simulate move_marker.py in memory (no writes) on both layers of SGA 5 and show the lines around each moved marker."""
import pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
moves = [(406, r"\section*{Références}", True), (407, r"\section*{Exposé XII}", True),
         (408, r"\section*{1.}", True), (411, "\[", True)]
for edition in ("diplomatic", "current"):
    f = W / "sga5" / edition / "s5.tex"
    t = f.read_text(encoding="utf-8")
    for folio, anchor, before in moves:
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        line = m.group(0)
        end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
        t2 = t[:m.start()] + t[end:]
        k = t2.rfind(anchor, 0, m.start()) if before else t2.find(anchor, m.start())
        ls = t2.rfind("\n", 0, k) + 1
        if t2[ls:k].strip() == "":
            t2 = t2[:ls] + line + "\n" + t2[ls:]
        else:
            t2 = t2[:k] + "\n" + line + "\n" + t2[k:]
        moved = m.start() - k
        t = t2
        p = t.find(line)
        lno = t.count("\n", 0, p) + 1
        print(f"== {edition} folio {folio}: anchor {anchor!r} found {moved} chars before the old marker; new marker line {lno}")
        a = t.rfind("\n", 0, max(0, t.rfind("\n", 0, t.rfind("\n", 0, p - 1) - 1) - 1))
        print(t[a + 1:p + len(line) + 120])
        print()
    # a second run of the 411 move: where would it go?
    m = next((m for m in MARK.finditer(t) if int(m.group(2)) == 411), None)
    end = m.end() + 1
    t2 = t[:m.start()] + t[end:]
    k = t2.rfind("\[", 0, m.start())
    print(edition, "second run of the 411 move would stop", m.start() - k, "chars before (current place keeps '\[' right after the marker):", repr(t2[k:k+40]))
