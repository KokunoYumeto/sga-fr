"""Compare the batch's page_NNN.tex snapshots with the present spans of the diplomatic main.tex (read only)."""
import io
import pathlib
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
MAIN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex")
BATCH = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b311_315")
t = MAIN.read_bytes().decode("utf-8").replace("\r\n", "\n")
marks = [(m.start(), int(m.group(2))) for m in MARK.finditer(t)]
for folio in range(311, 316):
    k = next(i for i, (_, f) in enumerate(marks) if f == folio)
    span = t[marks[k][0]:marks[k + 1][0]]
    snap = (BATCH / f"page_{folio}.tex").read_text(encoding="utf-8")
    snap_body = snap.split("\n", 1)[1]  # drop the '% from main.tex' line
    same = snap_body.rstrip() == span.rstrip()
    print(folio, "same as main.tex" if same else "DIFFERS")
    if not same:
        import difflib
        for line in difflib.unified_diff(snap_body.splitlines(), span.splitlines(), lineterm="", n=0):
            print("   ", line[:300])
