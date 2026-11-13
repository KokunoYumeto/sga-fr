"""Check that the strings named in the notes of the fix-null misprints occur once in their page files."""
import pathlib

B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b691_695")
checks = [
    (691, r"d'amplitude \(\mathcal C_0\) parfaite contenue"),
    (691, r"relativement a \(f\)"),
    (694, r"relativement a \(f\)"),
]
for page, s in checks:
    t = (B / f"page_{page}.tex").read_text(encoding="utf-8")
    print(page, t.count(s), repr(s))
