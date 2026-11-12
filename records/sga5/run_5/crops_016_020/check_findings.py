# Checks findings_016_020.json without writing any .tex file:
#  1. every fix's old occurs exactly once in its page_NNN.tex (as given in b016_020);
#  2. applying the fixes in list order to those page files, each old is unique when its turn comes;
#  3. the same sequential application on the live s5.tex page spans (diplomatic: all fixes; current: all but
#     misprint reversions, as process_sga.py replays them);
#  4. no marker line in old/new, no control characters, "corrected" exactly on misprints.
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
RUN = W / "run_5"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
d = json.loads((RUN / "findings_016_020.json").read_text(encoding="utf-8"))
ok = True


def bad(*a):
    global ok
    ok = False
    print("PROBLEM", *a)


for i, x in enumerate(d):
    for k, v in x.items():
        if isinstance(v, str) and re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", v):
            bad("control char", i, k)
    if (x["kind"] == "misprint_in_print") != ("corrected" in x):
        bad("corrected field", i)
    if x["fix"]:
        if MARK.search(x["fix"]["old"]) or MARK.search(x["fix"]["new"]) or "%%%%%%%%%%" in x["fix"]["old"]:
            bad("marker in fix", i)
    assert set(x) <= {"page", "where", "scan", "tex", "kind", "confidence", "fix", "corrected", "note"}, x.keys()
    assert x["kind"] in "word formula symbol font underline missing extra number punctuation accent " \
                        "misprint_in_print marker other".split(), x["kind"]
    assert x["confidence"] in ("high", "medium", "low")

# 1 + 2: the page files of the batch
pages = {}
for i, x in enumerate(d):
    p = x["page"]
    if p not in pages:
        pages[p] = (RUN / "b016_020" / f"page_{p:03d}.tex").read_text(encoding="utf-8")
orig = dict(pages)
for i, x in enumerate(d):
    if not x["fix"]:
        continue
    p, old, new = x["page"], x["fix"]["old"], x["fix"]["new"]
    n0 = orig[p].count(old)
    if n0 != 1:
        bad("original page file count", n0, "finding", i, "page", p, repr(old))
    n = pages[p].count(old)
    if n != 1:
        bad("sequential count", n, "finding", i, "page", p, repr(old))
        continue
    pages[p] = pages[p].replace(old, new)


# 3: live s5.tex spans
def spans(edition):
    t = (W / "sga5" / edition / "s5.tex").read_text(encoding="utf-8")
    ms = {int(m.group(2)): m for m in MARK.finditer(t)}
    return {p: t[ms[p].end():ms[p + 1].start()] for p in range(16, 21)}


for edition in ("diplomatic", "current"):
    sp = spans(edition)
    applied = 0
    for i, x in enumerate(d):
        if not x["fix"]:
            continue
        if edition == "current" and x["kind"] == "misprint_in_print":
            continue
        p, old, new = x["page"], x["fix"]["old"], x["fix"]["new"]
        n = sp[p].count(old)
        if n != 1:
            bad(edition, "live count", n, "finding", i, "page", p, repr(old))
            continue
        sp[p] = sp[p].replace(old, new)
        applied += 1
    print(edition, "applied in memory:", applied)
    if edition == "diplomatic":
        # leftovers of the families fixed here
        for p in range(16, 21):
            print("  page", p, "xrightarrow{\\sim} left:", sp[p].count("\\xrightarrow{\\sim}"),
                  "| \\uH left:", sp[p].count("\\uH"), "| begin/end proof:",
                  sp[p].count("\\begin{proof}"), sp[p].count("\\end{proof}"))
        i = sp[20].find(", donc que l'on a")
        print("  p20 after fix:", repr(sp[20][i - 60:i + 30]))

cnt = {}
for x in d:
    c = cnt.setdefault(x["page"], [0, 0])
    c[1 if x["kind"] == "misprint_in_print" else 0] += 1
print("counts (normal/misprint):", {p: f"{a}/{b}" for p, (a, b) in sorted(cnt.items())})
print("total", len(d))
print("OK" if ok else "PROBLEMS")
