import json
import sys
from pathlib import Path

run = Path(sys.argv[1])
findings = json.loads((run / "findings_506_510_recheck.json").read_text(encoding="utf-8"))
ok = True
for i, f in enumerate(findings):
    page = f["page"]
    tex = (run / "b506_510" / f"page_{page}.tex").read_bytes().decode("utf-8")
    assert "\r" not in tex, "CR found"
    for key in ("page", "where", "scan", "tex", "kind", "confidence", "fix", "note"):
        if key not in f:
            print(i, "missing key", key); ok = False
    if f["kind"] == "misprint_in_print" and "corrected" not in f:
        print(i, "misprint without corrected"); ok = False
    if f["kind"] != "misprint_in_print" and "corrected" in f:
        print(i, "corrected on non-misprint"); ok = False
    fix = f["fix"]
    if fix is not None:
        n = tex.count(fix["old"])
        print(i, page, "fix old count =", n, repr(fix["old"][:60]))
        if n != 1:
            ok = False
        if "%%%%%%%%%%" in fix["old"]:
            print(i, "old touches marker"); ok = False
        # apply and show the result
        new_tex = tex.replace(fix["old"], fix["new"], 1)
        assert new_tex != tex
    else:
        n = tex.count(f["tex"])
        print(i, page, "tex count =", n, repr(f["tex"]))
    for s in [f.get("tex", ""), f.get("corrected", "") or ""] + ([fix["old"], fix["new"]] if fix else []):
        if any(ord(c) < 32 and c != "\n" for c in s):
            print(i, "control character in", repr(s)); ok = False
print("OK" if ok else "PROBLEMS")
