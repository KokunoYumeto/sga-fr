"""Check findings_396_400.json: JSON parses, each fix's old occurs exactly once in its page file,
each 'tex' occurs in its page file, misprints carry 'corrected', marker lines are not touched."""
import json
import pathlib
import sys

run = pathlib.Path(sys.argv[1])
batch = run / "b396_400"
findings = json.loads((run / "findings_396_400.json").read_text(encoding="utf-8"))
ok = True
for i, f in enumerate(findings):
    page = f["page"]
    text = (batch / f"page_{page}.tex").read_text(encoding="utf-8")
    tex_n = text.count(f["tex"])
    msg = [f"#{i} p.{page} kind={f['kind']} conf={f['confidence']} tex_count={tex_n}"]
    if tex_n < 1:
        ok = False
        msg.append("TEX NOT FOUND")
    if f["kind"] == "misprint_in_print" and not f.get("corrected"):
        ok = False
        msg.append("NO CORRECTED")
    fix = f.get("fix")
    if fix is not None:
        n = text.count(fix["old"])
        msg.append(f"old_count={n}")
        if n != 1:
            ok = False
            msg.append("OLD NOT UNIQUE")
        if "%%%%%%%%%%" in fix["old"] or "%%%%%%%%%%" in fix["new"]:
            ok = False
            msg.append("TOUCHES MARKER")
        new_text = text.replace(fix["old"], fix["new"], 1)
        msg.append(f"applied_len_delta={len(new_text) - len(text)}")
    print(" ".join(msg))
print("ALL OK" if ok else "PROBLEMS FOUND")
