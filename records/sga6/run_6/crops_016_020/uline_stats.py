"""Count \\uline groups in the SGA 6 diplomatic main.tex with inner commas, math, or a final full stop (read-only)."""
import pathlib

t = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex").read_text(
    encoding="utf-8")
groups = []
i = 0
key = "\\uline{"
while True:
    k = t.find(key, i)
    if k < 0:
        break
    j = k + len(key)
    depth = 1
    while depth and j < len(t):
        if t[j] == "{":
            depth += 1
        elif t[j] == "}":
            depth -= 1
        j += 1
    groups.append(t[k + len(key):j - 1])
    i = j
print("uline groups", len(groups))
print("with inner ', '", sum(1 for g in groups if ", " in g))
print("with math $", sum(1 for g in groups if "$" in g))
print("ending in . , ; :", sum(1 for g in groups if g.rstrip()[-1:] in ".,;:"))
