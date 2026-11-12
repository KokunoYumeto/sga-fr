"""Check findings_126_130.json: every old occurs exactly once in its page_NNN.tex; applied in JSON order (in memory,
nothing written) on both layers of main.tex, every old occurs exactly once on its page when its turn comes
(misprint fixes on the diplomatic layer only); print brace/delimiter balance and the resulting pages.
usage: python -I check_findings.py [--show]"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
RUN = HERE.parent
W = RUN.parent
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
sys.stdout.reconfigure(encoding="utf-8")
items = json.loads((RUN / "findings_126_130.json").read_text(encoding="utf-8"))


def span(t, folio):
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        if int(m.group(2)) == folio:
            return m.start(), (ms[i + 1].start() if i + 1 < len(ms) else len(t))
    raise SystemExit(f"no folio {folio}")


ok = True
for i, x in enumerate(items):
    fx = x.get("fix")
    if not fx:
        continue
    src = (RUN / "b126_130" / f"page_{x['page']}.tex").read_text(encoding="utf-8")
    n = src.count(fx["old"])
    if n != 1 or MARK.search(fx["old"]) or MARK.search(fx["new"]):
        ok = False
        print(f"[{i}] p.{x['page']} old occurs {n} times in page file: {fx['old'][:60]!r}")
print("page-file check:", "all olds occur once" if ok else "PROBLEMS")


def balance(s):
    s2 = s.replace("\\{", "").replace("\\}", "")
    return dict(br=s2.count("{") - s2.count("}"), inl=s.count("\\(") - s.count("\\)"),
                disp=s.count("\\[") - s.count("\\]"))


for edition in ("diplomatic", "current"):
    t = (W / "sga6" / edition / "main.tex").read_text(encoding="utf-8")
    before = {f: balance(t[slice(*span(t, f))]) for f in range(126, 131)}
    bad = 0
    for i, x in enumerate(items):
        fx = x.get("fix")
        if not fx:
            continue
        if edition == "current" and x["kind"] == "misprint_in_print":
            continue
        s, e = span(t, x["page"])
        seg = t[s:e]
        n = seg.count(fx["old"])
        if n != 1:
            bad += 1
            print(f"  {edition}: [{i}] p.{x['page']} old occurs {n} times at its turn: {fx['old'][:60]!r}")
            continue
        t = t[:s] + seg.replace(fx["old"], fx["new"]) + t[e:]
    print(f"{edition}: sequential application", "clean" if not bad else f"{bad} problems")
    for f in range(126, 131):
        b = balance(t[slice(*span(t, f))])
        print(f"   p.{f} balance before {before[f]} after {b}")
    if "--show" in sys.argv and edition == "diplomatic":
        for f in range(126, 131):
            s, e = span(t, f)
            print(f"===== p. {f} (diplomatic, after the fixes)")
            print(t[s:e])
