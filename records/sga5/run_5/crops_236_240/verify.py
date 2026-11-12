"""Check findings_236_240.json: every old once in its page_NNN.tex; sequential application per page as process_sga.py
does it, on both layers of s5.tex, in memory; then the p. 237 marker move; prooftext balance. Nothing is written."""
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = r"C:/Users/user/Documents/sga_scan_check_20261105/run_5/"
SRC = r"C:/Users/user/Documents/sga_scan_check_20261105/sga5/"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
NL = chr(10)
items = json.load(open(RUN + "findings_236_240.json", encoding="utf-8"))
print(len(items), "findings")
ok = True
# 1. uniqueness in the page files; sequential application on the page files
pagetext = {p: open(RUN + "b236_240/page_%03d.tex" % p, encoding="utf-8").read() for p in range(236, 241)}
work = dict(pagetext)
for i, x in enumerate(items):
    for k in ("page", "where", "scan", "tex", "kind", "confidence", "fix", "note"):
        if k not in x:
            print("missing key", k, "in item", i); ok = False
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        print("misprint without corrected", i); ok = False
    f = x["fix"]
    if not f:
        continue
    p = x["page"]
    n0 = pagetext[p].count(f["old"])
    n1 = work[p].count(f["old"])
    if n0 != 1 or n1 != 1:
        print("ITEM", i, "page", p, "old count original", n0, "at its turn", n1, repr(f["old"][:60])); ok = False
    if MARK.search(f["old"]) or MARK.search(f["new"]):
        print("ITEM", i, "touches a marker"); ok = False
    work[p] = work[p].replace(f["old"], f["new"], 1)
print("page files:", "OK" if ok else "PROBLEMS")


def segments(t):
    ms = list(MARK.finditer(t))
    out = {}
    for i, m in enumerate(ms):
        end = ms[i + 1].start() if i + 1 < len(ms) else len(t)
        out[int(m.group(2))] = (m.start(), end)
    return out


for layer in ("diplomatic", "current"):
    t = open(SRC + layer + "/s5.tex", encoding="utf-8").read()
    bad = 0
    for i, x in enumerate(items):
        f = x["fix"]
        if not f:
            continue
        if layer == "current" and x["kind"] == "misprint_in_print":
            continue
        s, e = segments(t)[x["page"]]
        hits = []
        k = t.find(f["old"], s, e)
        while k >= 0 and k + len(f["old"]) <= e:
            hits.append(k)
            k = t.find(f["old"], k + 1, e)
        if len(hits) != 1:
            print(layer, "ITEM", i, "page", x["page"], "hits", len(hits), repr(f["old"][:60])); bad += 1
            continue
        k = hits[0]
        t = t[:k] + f["new"] + t[k + len(f["old"]):]
    # the marker move of p. 237: '\[' --before
    m = next(m for m in MARK.finditer(t) if int(m.group(2)) == 237)
    line = m.group(0)
    end = m.end() + (1 if t[m.end():m.end() + 1] == NL else 0)
    t2 = t[:m.start()] + t[end:]
    anchor = chr(92) + "["
    k = t2.rfind(anchor, 0, m.start())
    ls = t2.rfind(NL, 0, k) + 1
    t3 = t2[:ls] + line + NL + t2[ls:] if t2[ls:k].strip() == "" else t2[:k] + NL + line + NL + t2[k:]
    seg = segments(t3)
    s, e = seg[236][0], seg[241][0]
    region = t3[s:e]
    b = region.count(chr(92) + "begin{prooftext}")
    en = region.count(chr(92) + "end{prooftext}")
    bs = region.count(chr(92) + "begin{statement}")
    es = region.count(chr(92) + "end{statement}")
    emo = region.count(chr(92) + "emph{")
    print(layer, "applied with", bad, "failures; pp. 236-240 after the move: prooftext", b, "/", en,
          "statement", bs, "/", es, "emph", emo, "braces", region.count("{") - region.count("}"))
    if layer == "diplomatic":
        open(RUN + "crops_236_240/after_236_240.tex", "w", encoding="utf-8", newline="").write(region)
