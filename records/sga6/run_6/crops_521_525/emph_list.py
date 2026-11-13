"""emph_list.py: list emph and underline uses (and statement labels) in main.tex lines 13412-15273 (read only)."""
import pathlib, re, sys
sys.stdout.reconfigure(encoding='utf-8')
M = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex")
lines = M.read_text(encoding="utf-8").split("\n")
BS = chr(92)
pat_emph = re.compile(re.escape(BS) + r"(emph|underline)" + re.escape("{"))
pat_label = re.compile(re.escape(BS + "textbf{") + r"(Proposition|Théorème|Corollaire|Lemme|Définition|Remarque)")
for i in range(13412, 15273):
    l = lines[i - 1]
    for m in pat_emph.finditer(l):
        print(i, "|", l[max(0, m.start() - 30):m.start() + 90])
    for m in pat_label.finditer(l):
        print(i, "| LABEL", l[m.start():m.start() + 150])
