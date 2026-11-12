"""In-memory replay of findings_051_055.json on both SGA 6 layers, as process_sga.py would apply it (fix applied when
its old occurs exactly once in the page span; misprint fixes only on the diplomatic layer). Nothing is written.
usage: python -I simulate_process.py"""
import json
import re

MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
BASE = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6\%s\main.tex"
F = json.load(open(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6\findings_051_055.json",
                   encoding="utf-8"))


def span(t, folio):
    ms = list(MARK.finditer(t))
    for i, m in enumerate(ms):
        if int(m.group(2)) == folio:
            return m.start(), (ms[i + 1].start() if i + 1 < len(ms) else len(t))
    raise KeyError(folio)


for layer in ("diplomatic", "current"):
    t = open(BASE % layer, encoding="utf-8").read()
    applied, failed = 0, []
    for x in F:
        fx = x.get("fix")
        if not fx:
            continue
        if layer == "current" and x["kind"] == "misprint_in_print":
            continue
        s, e = span(t, x["page"])
        seg = t[s:e]
        n = seg.count(fx["old"])
        if n != 1:
            failed.append((x["page"], x["where"], n))
            continue
        k = s + seg.find(fx["old"])
        t = t[:k] + fx["new"] + t[k + len(fx["old"]):]
        applied += 1
    print(layer, "applied", applied, "failed", failed)
    for folio in (53, 54):
        s, e = span(t, folio)
        seg = t[s:e]
        print("  folio", folio, "remaining _*:", seg.count("_*"), "| (fg) form:",
              re.findall(r"\(fg\)_?!?=f_[!*]g_[!*]", seg))
