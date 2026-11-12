import json
import pathlib
import sys

run = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
findings = json.loads((run / "findings_286_290.json").read_text(encoding="utf-8"))
counts = {}
ok = True
for i, f in enumerate(findings):
    p = f["page"]
    misprint = f["kind"] == "misprint_in_print"
    counts.setdefault(p, [0, 0])[1 if misprint else 0] += 1
    if misprint and "corrected" not in f:
        print(i, p, "MISPRINT WITHOUT corrected"); ok = False
    if not misprint and "corrected" in f:
        print(i, p, "corrected ON NON-MISPRINT"); ok = False
    fx = f["fix"]
    if fx is None:
        continue
    tex = (run / "b286_290" / f"page_{p}.tex").read_text(encoding="utf-8")
    n = tex.count(fx["old"])
    if n != 1 or "%%%%%%%%%%" in fx["old"] or fx["old"] == fx["new"]:
        print(i, p, "BAD old count", n, repr(fx["old"])); ok = False
    else:
        print(i, p, "ok", repr(fx["old"][:60]))

mark = "%%%%%%%%%%  scan idx {}  |  folio {}  %%%%%%%%%%"
strings = [
    "Celui-ci définit un\n" + mark.format(300, 287) + "\nhomomorphisme\n",
    "Cet homomorphisme est \\(K'(Y)\\)-linéaire",
    "principales des\n" + mark.format(303, 290) + "\nsorites de Exp. I à Exp. IV.\n\n\\section*{3.",
    "de changement de base est\n" + mark.format(304, 291) + "\ndonc définie",
]
for layer in ("diplomatic", "current"):
    t = (run.parent / "sga6" / layer / "main.tex").read_text(encoding="utf-8")
    for s in strings:
        c = t.count(s)
        print(layer, c, repr(s[:50]))
        ok = ok and c == 1
print("counts (normal/misprint):", {k: tuple(v) for k, v in sorted(counts.items())})
print("ALL OK" if ok else "PROBLEMS")
sys.exit(0 if ok else 1)
