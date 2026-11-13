"""count_forms.py: count TeX forms on pp. 521-525 and in the Exposé X part of the diplomatic main.tex (read only)."""
import pathlib, re, sys
sys.stdout.reconfigure(encoding='utf-8')
B = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b521_525")
M = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex")
forms = [r"K^\circ", r"\cl^\circ", r"K_\bullet", r"\cl_\bullet", r"\emph", r"\underline", r"\cdots", r"\ldots", r"\wedge", r"\Lambda"]
for n in range(521, 526):
    t = B.joinpath(f"page_{n}.tex").read_text(encoding="utf-8")
    print(n, {k: t.count(k) for k in forms if t.count(k)})
lines = M.read_text(encoding="utf-8").split("\n")
heads = [(i, l) for i, l in enumerate(lines, 1) if re.search(r"\\(chapter|section|part)\*?\{", l)]
for i, l in heads:
    if 12800 < i < 16000:
        print(i, l[:110])

# Exposé X span: from its heading to the next "Exposé" heading
start = next(i for i, l in heads if "Exposé X." in l)
xi = [i for i, l in enumerate(lines, 1) if i > start and re.search(r"(?i)expos(é|\'e)\s*XI\b", l)]
print("Exposé X starts", start, "first 'Exposé XI' mention after it:", xi[:3])
end = xi[0] if xi else 15273
seg = "\n".join(lines[start - 1:end - 1])
for k in forms + [r"\emph{Démonstration"]:
    print(k, seg.count(k))
