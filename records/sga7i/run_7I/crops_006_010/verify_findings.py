import json
import pathlib

RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_7I")
FOLDER = RUN / "b006_010"
findings = json.loads((RUN / "findings_006_010.json").read_text(encoding="utf-8"))
ok = True
for i, f in enumerate(findings):
    tex = (FOLDER / f"page_{f['page']:03d}.tex").read_text(encoding="utf-8")
    tq = f.get("tex", "")
    tc = tex.count(tq) if tq else -1
    line = f"{i} p{f['page']} {f['kind']} {f['confidence']} tex-quote count={tc}"
    fix = f.get("fix")
    if fix is not None:
        n = tex.count(fix["old"])
        line += f" old count={n}"
        if n != 1:
            ok = False
        if "scan idx" in fix["old"]:
            ok = False
            line += " MARKER!"
        # apply in a copy to make sure the result is as intended
        new_tex = tex.replace(fix["old"], fix["new"], 1)
        idx = new_tex.find(fix["new"])
        line += " -> ..." + new_tex[max(0, idx - 30): idx + len(fix["new"]) + 20].replace("\n", "\\n") + "..."
    else:
        line += " fix=null"
    if f["kind"] == "misprint_in_print" and "corrected" not in f:
        ok = False
        line += " MISSING corrected"
    if tc < 1:
        ok = False
        line += " TEX QUOTE NOT FOUND"
    print(line)
print("ALL OK" if ok else "PROBLEMS")
