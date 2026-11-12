import pathlib

base = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\b081_085")
for p in ("084", "085"):
    t = (base / f"page_{p}.tex").read_text(encoding="utf-8")
    t = t.split("% Additional macro definitions")[0]
    counts = {k: t.count(k) for k in ("\\(S\\)", "\\ob(S)", "\\Ob S", "S_{/X}", "\\(S\\)-")}
    print(p, counts, "total", counts["\\(S\\)"] + counts["\\ob(S)"] + counts["\\Ob S"] + counts["S_{/X}"])
