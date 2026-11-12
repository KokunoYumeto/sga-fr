"""Replace the note of the p. 181 marker entry in make_findings.py (the marker was moved in main.tex meanwhile)."""
P = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\crops_181_185\make_findings.py"
lines = open(P, encoding="utf-8").read().split("\n")
i = next(k for k, l in enumerate(lines) if l.startswith('    r"Page 181 really begins'))
assert lines[i + 3].endswith('r"touches these lines.")'), lines[i + 3]
new = [
    r'''    r"Page 181 really begins with 'où $\Lib(A)$'. Already done in main.tex: both layers now have the folio-181 "''',
    r'''    r"marker above that line (the snapshot page_181.tex predates the move; checked at the end of this check with "''',
    r'''    r"crops_181_185/sim_markers.py and chk_main.py: the live span differs from the snapshot only by this line). "''',
    r'''    r"Nothing to do: python -I move_marker.py 6 181 'où $\Lib(A)$' --before now reports 'anchor not found' and "''',
    r'''    r"changes nothing.")''',
]
lines[i:i + 4] = new
open(P, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
print("patched at line", i + 1)
