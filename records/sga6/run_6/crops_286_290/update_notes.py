import json
import pathlib

path = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_286_290.json")
d = json.loads(path.read_text(encoding="utf-8"))
M287 = "%%%%%%%%%%  scan idx 300  |  folio 287  %%%%%%%%%%"
notes = {
    (287, "page start"): (
        "The folio-287 marker stands four TeX lines too early. Exact fix (both layers): "
        r'python -I move_marker.py 6 287 "Cet homomorphisme est" (simulated: the marker then stands after the '
        r"\end{equation} of (2.11.1.1), just before 'Cet homomorphisme est \(K'(Y)\)-linéaire (cf. (2.10))'). "
        r"As text replacements in main.tex: 'Celui-ci définit un\n" + M287 + r"\nhomomorphisme\n' by "
        r"'Celui-ci définit un\nhomomorphisme\n', and 'Cet homomorphisme est \(K'(Y)\)-linéaire' by '"
        + M287 + r"\nCet homomorphisme est \(K'(Y)\)-linéaire' (unique; apply before any K' replacement). "
        "The full-stop fix of (2.11.1.1) below is filed under p. 287 but concerns a display of p. 286: "
        "apply it before moving the marker."),
    (290, "page start"): None,
    (290, "page end"): None,
}
for f in d:
    key = (f["page"], f["where"])
    if key not in notes:
        continue
    if key == (287, "page start"):
        f["note"] = notes[key]
    elif key == (290, "page start"):
        f["note"] += r' Equivalently: python -I move_marker.py 6 290 "\section*{3. Compl".'
    elif key == (290, "page end"):
        f["note"] += " Equivalently: python -I move_marker.py 6 291 est --before (leaves 'base ' and 'est' on their own lines)."
path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
print("updated", len(d), "findings")
