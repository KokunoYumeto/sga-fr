"""One-off: replace the raw strings with backslash-escaped double quotes in make_findings.py by triple-quoted ones."""
import pathlib

p = pathlib.Path(__file__).with_name("make_findings.py")
s = p.read_text(encoding="utf-8")
BS = "\\"
DQ = '"'
reps = [
    ("r" + DQ + "& X " + BS + "arrow[r," + BS + DQ + "u" + BS + DQ + "'] & Y ." + DQ,
     "r'''& X " + BS + "arrow[r," + DQ + "u" + DQ + "'] & Y .'''"),
    ("r" + DQ + "X' " + BS + "arrow[r," + BS + DQ + "s" + BS + DQ + "] & X" + DQ,
     "r'''X' " + BS + "arrow[r," + DQ + "s" + DQ + "] & X'''"),
    ("r" + DQ + BS + "arrow[r,shift right," + BS + DQ + "g" + BS + DQ + "'] & Y ." + DQ,
     "r'''" + BS + "arrow[r,shift right," + DQ + "g" + DQ + "'] & Y .'''"),
    ("r" + DQ + "X " + BS + "arrow[r," + BS + DQ + "u" + BS + DQ + "'] & Y ." + DQ,
     "r'''X " + BS + "arrow[r," + DQ + "u" + DQ + "'] & Y .'''"),
    ("r" + DQ + "Page 213 really begins at the '" + BS + "[' that opens 'X " + BS + "arrow[r,shift left," + BS + DQ
     + "f" + BS + DQ + "] ... & Z .'; the close of the (D_2) " + DQ,
     "r'''Page 213 really begins at the '" + BS + "[' that opens 'X " + BS + "arrow[r,shift left," + DQ + "f" + DQ
     + "] ... & Z .'; the close of the (D_2) '''"),
]
for a, b in reps:
    print(s.count(a), a[:60])
    s = s.replace(a, b)
p.write_text(s, encoding="utf-8")
