# Simulates move_marker.py --before in memory (no file is written) and prints the context.
import re, pathlib
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga5")
BS = chr(92)
moves = [(11, BS + "item[b)] Si"), (12, "d)"), (13, "Si en"),
         (14, "$" + BS + "underline{D}_X$ et $" + BS + "underline{D}_Y$"),
         (15, BS + "item[b)]"), (16, BS + "begin{proof}[")]
for ed in ("diplomatic", "current"):
    t = (W / ed / "s5.tex").read_text(encoding="utf-8")
    for folio, anchor in moves:
        m = next((m for m in MARK.finditer(t) if int(m.group(2)) == folio), None)
        line = m.group(0)
        end = m.end() + (1 if t[m.end():m.end() + 1] == "\n" else 0)
        t2 = t[:m.start()] + t[end:]
        k = t2.rfind(anchor, 0, m.start())
        ls = t2.rfind("\n", 0, k) + 1
        own = t2[ls:k].strip() == ""
        if own:
            t3 = t2[:ls] + line + "\n" + t2[ls:]
        else:
            t3 = t2[:k] + "\n" + line + "\n" + t2[k:]
        lineno_before = t[:m.start()].count("\n") + 1
        lineno_anchor = t2[:k].count("\n") + 1
        p = t3.find(line)
        print(f"== {ed} folio {folio}: marker at line {lineno_before}, anchor at line {lineno_anchor} "
              f"(distance {m.start() - k} chars), own line: {own}, anchor {anchor!r}")
        print(repr(t3[p - 100:p + len(line) + 70]))
