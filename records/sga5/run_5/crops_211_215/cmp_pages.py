"""Read-only: compare the page snapshots b211_215/page_NNN.tex with the same pages in both layers of s5.tex now."""
import re
import pathlib

W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
for edition in ("diplomatic", "current"):
    t = (W / "sga5" / edition / "s5.tex").read_text(encoding="utf-8")
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        folio = int(m.group(2))
        if 211 <= folio <= 215:
            end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
            live = t[m.start():end]
            snap = (W / "run_5" / "b211_215" / ("page_%d.tex" % folio)).read_text(encoding="utf-8")
            snap = snap.split("\n", 1)[1]  # drop the '% from s5.tex' line
            print(edition, folio, "same" if live == snap else "DIFFERENT")
            if live != snap:
                import difflib
                for line in difflib.unified_diff(snap.splitlines(), live.splitlines(), lineterm="", n=0):
                    print("   ", line[:200])
