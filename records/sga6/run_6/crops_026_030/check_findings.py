"""Check a findings file: JSON parses, required keys, each fix's old occurs exactly once in its page file,
and show the edited context (in memory only).
usage: python -I check_findings.py FINDINGS BATCH_DIR"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
findings = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
batch = pathlib.Path(sys.argv[2])
keys = {"page", "where", "scan", "tex", "kind", "confidence", "fix", "note"}
kinds = {"word", "formula", "symbol", "font", "underline", "missing", "extra", "number", "punctuation", "accent",
         "misprint_in_print", "marker", "other"}
counts = {}
for i, f in enumerate(findings):
    miss = keys - set(f)
    assert not miss, (i, miss)
    assert f["kind"] in kinds, (i, f["kind"])
    assert f["confidence"] in {"high", "medium", "low"}, i
    if f["kind"] == "misprint_in_print":
        assert "corrected" in f, i
    else:
        assert "corrected" not in f, i
    n, m = counts.get(f["page"], (0, 0))
    counts[f["page"]] = (n + (f["kind"] != "misprint_in_print"), m + (f["kind"] == "misprint_in_print"))
    if f["fix"] is None:
        continue
    t = (batch / f"page_{f['page']:03d}.tex").read_text(encoding="utf-8")
    old, new = f["fix"]["old"], f["fix"]["new"]
    c = t.count(old)
    print(f"#{i} p{f['page']} occurrences={c}", "OK" if c == 1 else "PROBLEM")
    assert "%%%%%%%%%%" not in old
    k = t.find(old)
    t2 = t[:k] + new + t[k + len(old):]
    print("   new context:", t2[max(0, k - 60):k + len(new) + 60].replace("\n", "\\n"))
    for name, s in (("before", t), ("after", t2)):
        print("   braces", name, s.count("{") - s.count("}"))
print("counts (normal/misprint):", dict(sorted(counts.items())))
