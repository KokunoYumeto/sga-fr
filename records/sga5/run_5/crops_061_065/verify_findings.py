"""Check findings_061_065.json: every fix's old occurs exactly once in its page file and in the page's section of
both s5.tex layers; all fixes of a page apply one after the other in the listed order; the marker move of folio 62
still works after the fixes. Nothing is written.
usage: python -I verify_findings.py"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
here = pathlib.Path(__file__).resolve().parent
run = here.parent
W = run.parent
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
F = json.loads((run / "findings_061_065.json").read_text(encoding="utf-8"))
keys = {"page", "where", "scan", "tex", "kind", "confidence", "fix", "note"}
kinds = {"word", "formula", "symbol", "font", "underline", "missing", "extra", "number", "punctuation", "accent",
         "misprint_in_print", "marker", "other"}
ok = True


def page_file(p):
    d = "b061_065" if p >= 61 else "b056_060"
    return (run / d / f"page_{p:03d}.tex").read_text(encoding="utf-8").split("\n", 1)[1]


def sections(edition):
    t = (W / "sga5" / edition / "s5.tex").read_text(encoding="utf-8")
    ms = list(MARK.finditer(t))
    out = {}
    for i, m in enumerate(ms):
        out[int(m.group(2))] = t[m.start():ms[i + 1].start() if i + 1 < len(ms) else len(t)]
    return t, out


for i, e in enumerate(F):
    miss = (keys | ({"corrected"} if e["kind"] == "misprint_in_print" else set())) - set(e)
    if miss or e["kind"] not in kinds or e["confidence"] not in ("high", "medium", "low"):
        print("BAD ENTRY", i, miss, e["kind"], e["confidence"])
        ok = False
    if e["fix"] and "%%%%%%%%%%" in e["fix"]["old"]:
        print("OLD CROSSES A MARKER", i)
        ok = False

layers = {ed: sections(ed) for ed in ("diplomatic", "current")}
pages = sorted({e["page"] for e in F})
for p in pages:
    txt = page_file(p)
    fixes = [(i, e["fix"]) for i, e in enumerate(F) if e["page"] == p and e["fix"]]
    for i, fx in fixes:
        n = txt.count(fx["old"])
        if n != 1:
            print(f"p.{p} entry {i}: old occurs {n} times in page_{p:03d}.tex: {fx['old']!r}")
            ok = False
        for ed, (_, secs) in layers.items():
            n2 = secs[p].count(fx["old"])
            if n2 != 1:
                print(f"p.{p} entry {i}: old occurs {n2} times in the {ed} section: {fx['old']!r}")
                ok = False
    t = txt
    for i, fx in fixes:
        if t.count(fx["old"]) != 1:
            print(f"p.{p} entry {i}: sequential application fails")
            ok = False
            continue
        t = t.replace(fx["old"], fx["new"])
    print(f"p.{p}: {len(fixes)} fixes checked")

# folio-62 move after all fixes applied to the diplomatic layer in memory
t, secs = layers["diplomatic"]
for e in F:
    if e["fix"]:
        sec = secs[e["page"]]
        sec2 = sec.replace(e["fix"]["old"], e["fix"]["new"])
        t = t.replace(sec, sec2)
        secs = {k: (sec2 if v == sec else v) for k, v in secs.items()}
m = next(m for m in MARK.finditer(t) if int(m.group(2)) == 62)
end = m.end() + 1
t2 = t[:m.start()] + t[end:]
k = t2.rfind("\\begin{equation}\\tag{4.3}", 0, m.start())
print("folio-62 anchor after fixes:", "found" if k >= 0 else "NOT FOUND")
ok = ok and k >= 0
print("ALL OK" if ok else "PROBLEMS")
