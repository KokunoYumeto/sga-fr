"""Check that the marker contexts of pp. 18-20 are identical in both layers (read-only)."""
import pathlib

base = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6")
pats = [
    "cet expos\\'e est\n%%%%%%%%%%  scan idx 31  |  folio 18  %%%%%%%%%%\nlogiquement",
    "XI.\n\n\\section*{Bibliographie}\n\\begin{enumerate}[label={[\\arabic*]},leftmargin=2.5em]\n\\item M.\n"
    "%%%%%%%%%%  scan idx 32  |  folio 19  %%%%%%%%%%\nAtiyah",
    "\\clearpage\n\n\n\n\\section*{Appendice à l'Exposé 0 : RRR}\n\\begin{center}\n"
    "%%%%%%%%%%  scan idx 33  |  folio 20  %%%%%%%%%%\n{\\Large",
]
for ed in ("diplomatic", "current"):
    t = (base / ed / "main.tex").read_text(encoding="utf-8")
    for p in pats:
        print(ed, t.count(p), repr(p[:30]))
