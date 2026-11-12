"""Validate findings_371_375.json: JSON parses, keys, each fix's old occurs exactly once in its page file,
and the example strings quoted in the convention notes occur once on their pages (read only)."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
F = RUN / "findings_371_375.json"
PAGES = RUN / "b371_375"
d = json.loads(F.read_text(encoding="utf-8"))
kinds = {"word", "formula", "symbol", "font", "underline", "missing", "extra", "number", "punctuation", "accent",
         "misprint_in_print", "marker", "other"}
ok = True
for i, x in enumerate(d):
    need = {"page", "where", "scan", "tex", "kind", "confidence", "fix", "note"}
    if x["kind"] == "misprint_in_print":
        need.add("corrected")
    miss = need - set(x)
    if miss or x["kind"] not in kinds or x["confidence"] not in {"high", "medium", "low"}:
        ok = False
        print("BAD entry", i, miss, x["kind"], x["confidence"])
    if x.get("fix"):
        t = (PAGES / f"page_{x['page']}.tex").read_text(encoding="utf-8")
        old = x["fix"]["old"]
        n = t.count(old)
        marker_cross = "%%%%%%%%%%" in old
        print(i, x["page"], x["kind"], "old count", n, "crosses marker" if marker_cross else "")
        if n != 1 or marker_cross:
            ok = False
        # apply and show
        t2 = t.replace(old, x["fix"]["new"])
        k = t2.find(x["fix"]["new"])
        print("   ->", repr(t2[max(0, k - 30):k + len(x["fix"]["new"]) + 30]))
    else:
        print(i, x["page"], x["kind"], "fix null")
# examples quoted in convention notes
EX = [
    (374, "\\text{avec } E=\\cl E,"),
    (371, "surjectif~: \\(L\\to M\\), où \\(L\\) est"),
    (375, "soient \\(F\\) et \\(G\\) deux"),
    (371, "0\\longrightarrow L_n\\longrightarrow\\cdots"),
    (372, "L_{i-1}\\longrightarrow\\cdots"),
    (374, "\\Projz(L_{r+1})\\longrightarrow\\cdots"),
    (371, "et il est clair qu'il surjectif."),
    (375, "(F(n))-(G(n))=\\sum_i \\bigl((L_i(n))-(M_i(n))+(N_i(n))\\bigr),"),
]
for p, s in EX:
    n = (PAGES / f"page_{p}.tex").read_text(encoding="utf-8").count(s)
    print("example", p, n, s)
    if n != 1:
        ok = False
print("ALL OK" if ok else "PROBLEMS")
