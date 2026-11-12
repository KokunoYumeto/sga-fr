"""Checks of the CONT pass on SGA 7 I, Exposé IX (read-only).

For each layer: no CONT>> / <<CONT / CONT{>}{>} left; marker lines unchanged (same lines, same order); LF only and
UTF-8; replaying the pass's log lines on the backup (each old found exactly once on its page, as process_sga.py does)
gives exactly the edited file, so the diff to the backup consists only of the logged edits. Across the layers: the
same edits (same folios, kinds, tags and removed text).

usage: python -I verify_cont.py [--preview]
"""
import difflib
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
TAGS = re.compile(r"CONT>>|<<CONT|CONT\{>\}\{>\}")
SOURCE = "CONT pass 8 Nov 2026"
preview = "--preview" in sys.argv
LAYERS = {"diplomatic": ("FIXLOG_7I.jsonl", W / "sga7i" / "diplomatic" / "expose_IX_body.tex"),
          "current": ("FIXLOG_7I_CURRENT.jsonl", W / "sga7i" / "current" / "expose_IX_body.tex")}


def spans(t):
    ms = list(MARK.finditer(t))
    out = {}
    if t[:ms[0].start()].strip():
        out.setdefault(int(ms[0].group(2)) - 1, []).append((0, ms[0].start()))
    for i, m in enumerate(ms):
        out.setdefault(int(m.group(2)), []).append((m.start(), ms[i + 1].start() if i + 1 < len(ms) else len(t)))
    return out


ok_all = True
logs = {}
for layer, (logname, edition) in LAYERS.items():
    before = (HERE / f"expose_IX_body.{layer}.before_cont.tex").read_bytes().decode("utf-8")
    after_path = HERE / f"preview_{layer}.tex" if preview else edition
    raw = after_path.read_bytes()
    after = raw.decode("utf-8")
    if preview:
        lines = [json.loads(x) for x in open(HERE / f"preview_{layer}.jsonl", encoding="utf-8")]
    else:
        lines = [json.loads(x) for x in open(W / logname, encoding="utf-8")]
        lines = [x for x in lines if x.get("source") == SOURCE and x.get("file") == "expose_IX_body.tex"]
    logs[layer] = lines
    problems = []
    if TAGS.search(after):
        problems.append(f"tags left: {len(TAGS.findall(after))}")
    mb, ma = [m.group(0) for m in MARK.finditer(before)], [m.group(0) for m in MARK.finditer(after)]
    if mb != ma:
        problems.append("marker lines differ")
    lb = [ln for ln in before.split("\n") if MARK.search(ln)]
    la = [ln for ln in after.split("\n") if MARK.search(ln)]
    if lb != la or any(ln != MARK.search(ln).group(0) for ln in la):
        problems.append("a marker line is not on its own line or changed")
    if b"\r" in raw:
        problems.append("CR in file")
    # replay the log on the backup, page by page
    t = before
    for k, x in enumerate(lines):
        hits = []
        for s, e in spans(t).get(x["page"], []):
            i = t.find(x["old"], s, e)
            while i >= 0 and i + len(x["old"]) <= e:
                hits.append(i)
                i = t.find(x["old"], i + 1, e)
        if len(hits) != 1 or MARK.search(x["old"]) or MARK.search(x["new"]) or x["kind"] != "marker":
            problems.append(f"log line {k}: old found {len(hits)} times on p. {x['page']}")
            continue
        i = hits[0]
        t = t[:i] + x["new"] + t[i + len(x["old"]):]
    if t != after:
        problems.append("replay of the log does not give the edited file")
    diff = list(difflib.unified_diff(before.split("\n"), after.split("\n"), lineterm="", n=0))
    minus = sum(1 for d in diff if d.startswith("-") and not d.startswith("---"))
    plus = sum(1 for d in diff if d.startswith("+") and not d.startswith("+++"))
    print(f"{layer}: {len(lines)} log lines; tags before {len(TAGS.findall(before))}, after "
          f"{len(TAGS.findall(after))}; marker lines {len(mb)} -> {len(ma)}; diff -{minus} +{plus} lines; "
          f"{'OK' if not problems else 'PROBLEMS: ' + '; '.join(problems)}")
    ok_all &= not problems
same = [(x["page"], x["kind"]) for x in logs["diplomatic"]] == [(x["page"], x["kind"]) for x in logs["current"]]
E = {k: json.loads((HERE / f"edits_{k}.json").read_text(encoding="utf-8")) for k in LAYERS}
key = lambda r: (r["folio"], r["side"], r["tag"], r["rule"], r["removed"], r["replacement"])  # noqa: E731
same_edits = [key(r) for r in E["diplomatic"]] == [key(r) for r in E["current"]]
print(f"layers: same folios and kinds {same}; same tags, rules and removed text {same_edits}")
ok_all &= same and same_edits
print("ALL OK" if ok_all else "FAILED")
