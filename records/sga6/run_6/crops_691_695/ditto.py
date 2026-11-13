import pathlib
p = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex")
lines = p.read_text(encoding="utf-8").split("\n")
start = next(i for i, l in enumerate(lines) if "Index terminologique" in l)
for i in range(start, len(lines)):
    l = lines[i]
    if ("''" in l or '"' in l or "id." in l or "ditto" in l.lower()) and "&" in l:
        print(i + 1, l[:160])
print("index starts at line", start + 1, "of", len(lines))
