import pathlib
p = pathlib.Path(__file__).resolve().parent / 'build_findings.py'
t = p.read_text(encoding='utf-8')
reps = [
    ("CONVENTION of the Exposé X TeX (every statement from Définition 1.1.1 on is in roman)",
     "CONVENTION of the Exposé X TeX (its labelled statements, from Définition 1.1.1 on, are set in roman)"),
    (r"CONVENTION of Exposé X pp. 519-563: the print's raised dot is written \circ (main.tex: \cl^\circ 28 times on pp. 522-551, K^\circ 54 times on pp. 519-564, \Gro on pp. 538-540), while pp. 564-594 write K^\bullet and \Gr^\bullet.",
     r"CONVENTION of Exposé X up to p. 564: the print's raised dot is written \circ (main.tex: \cl^\circ 28 times on pp. 522-551, K^\circ 54 times on pp. 522-564, \Gro on pp. 538-540), while pp. 564-594 write K^\bullet (66) and \Gr^\bullet (35)."),
    ("once the batches of pp. 519-563 confirm the dot.", "once the batches of pp. 519-564 confirm the dot."),
    (r"(Exposé X pp. 519-563 write the raised dot as \circ)", r"(Exposé X up to p. 564 writes the raised dot as \circ)"),
]
for a, b in reps:
    n = t.count(a)
    assert n == 1, (n, a[:70])
    t = t.replace(a, b)
p.write_text(t, encoding='utf-8')
print('patched')
