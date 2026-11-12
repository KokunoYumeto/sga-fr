"""Compare the batch's page_NNN.tex with the present diplomatic s5.tex spans (read only)."""
import pathlib
import sys

sys.path.insert(0, r"C:\Users\user\Documents\sga_scan_check_20261105")
from sga_config import pages  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8")
B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_5\b056_060")
pg = pages("5")
for n in range(56, 61):
    parts = []
    for i, (f, s, e) in enumerate(pg[n]):
        t = f.read_text(encoding="utf-8")
        head = f"% from {f.name}\n" if i == 0 else f"\n% (continued in {f.name}, before its first page marker)\n"
        parts.append(head + t[s:e])
    now = "".join(parts)
    old = (B / f"page_{n:03d}.tex").read_text(encoding="utf-8")
    print(n, "same" if now == old else "DIFFERENT")
    if now != old:
        import difflib
        for l in difflib.unified_diff(old.splitlines(), now.splitlines(), lineterm=""):
            print(l)
