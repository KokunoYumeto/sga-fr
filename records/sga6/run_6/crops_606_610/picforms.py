"""Count the forms of Pic (plain, underlined) in diplomatic main.tex, per folio (read only)."""
import pathlib, sys, re
sys.stdout.reconfigure(encoding='utf-8')
t = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\diplomatic\main.tex").read_text(encoding="utf-8")
marks = [(m.start(), int(m.group(1))) for m in re.finditer(r"%%%%%%%%%%  scan idx \d+  \|  folio (\d+)  %%%%%%%%%%", t)]
BS = "\\"
def folio_at(pos):
    f = None
    for p, fo in marks:
        if p <= pos:
            f = fo
        else:
            break
    return f
pats = {
    "underline{Pic-macro}": re.escape(BS + "underline{" + BS + "Pic}"),
    "underline{operatorname{Pic}}": re.escape(BS + "underline{" + BS + "operatorname{Pic}}"),
    "underline{mathrm{Pic}}": re.escape(BS + "underline{" + BS + "mathrm{Pic}}"),
    "underline{...Pic (any)": re.escape(BS + "underline{") + r"[^}]{0,20}Pic",
    "uline{...Pic": re.escape(BS + "uline{") + r"[^}]{0,20}Pic",
    "Pic-macro (all)": re.escape(BS + "Pic") + r"(?![A-Za-z])",
    "operatorname{Pic} (all)": re.escape(BS + "operatorname{Pic}"),
    "underline{Hom-macro}": re.escape(BS + "underline{" + BS + "Hom}"),
    "underline{operatorname{Hom}}": re.escape(BS + "underline{" + BS + "operatorname{Hom}}"),
}
for name, p in pats.items():
    hits = [folio_at(m.start()) for m in re.finditer(p, t)]
    fs = sorted(set(h for h in hits if h is not None))
    print(name, len(hits), fs[:80])
