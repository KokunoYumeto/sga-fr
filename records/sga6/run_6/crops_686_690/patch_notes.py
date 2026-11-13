"""One-off patch of two notes in make_findings.py (helper of the 686-690 check)."""
import pathlib

p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\crops_686_690\make_findings.py")
t = p.read_text(encoding="utf-8")
pairs = [
    ("same form as the other bibliography headings of main.tex (\\subsection*{BIBLIOGRAPHIE}, Exposés I-XII).",
     "same form as eight other bibliography headings of main.tex (\\subsection*{BIBLIOGRAPHIE})."),
    ("The second reading also has Gr', from its own reading of pp. 672-678 (prime there); on this page both scans show the dot.",
     "The second reading also has Gr' here (its image check ended at p. 678, where it reads primes); on this page both scans show the dot."),
]
for a, b in pairs:
    assert t.count(a) == 1, (a, t.count(a))
    t = t.replace(a, b)
p.write_text(t, encoding="utf-8", newline="\n")
print("patched")
