"""Count literal substrings in the SGA 6 diplomatic main.tex and print the line numbers of the first hits.
usage: python -I count.py SUBSTRING [SUBSTRING ...]"""
import pathlib
import sys

t = (pathlib.Path(__file__).resolve().parents[2] / "sga6" / "diplomatic" / "main.tex").read_text(encoding="utf-8")
for s in sys.argv[1:]:
    hits = []
    k = t.find(s)
    while k >= 0:
        hits.append(t.count("\n", 0, k) + 1)
        k = t.find(s, k + 1)
    print(repr(s), len(hits), hits[:15])
