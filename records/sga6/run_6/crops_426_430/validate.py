"""Check findings_426_430.json: every fix's old string occurs exactly once in its page file (also after the other
fixes of the page are applied, in file order), no old string crosses a marker line; the main.tex edits quoted in the
marker notes occur once in each layer, and after them each page starts and ends where the print does."""
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6"
SGA6 = r"C:\Users\user\Documents\sga_scan_check_20261105\sga6"
BS = chr(92)
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
KINDS = {"word", "formula", "symbol", "font", "underline", "missing", "extra", "number", "punctuation", "accent",
         "misprint_in_print", "marker", "other"}

d = json.load(open(RUN + r"\findings_426_430.json", encoding="utf-8"))
ok = True
pages = {}
for n in range(426, 431):
    pages[n] = open(RUN + rf"\b426_430\page_{n}.tex", encoding="utf-8", newline="").read()
counts = {}
for i, x in enumerate(d):
    for k in ("page", "where", "scan", "tex", "kind", "confidence", "fix", "note"):
        if k not in x:
            print("missing key", k, "in entry", i); ok = False
    if x["kind"] not in KINDS or x["confidence"] not in ("high", "medium", "low"):
        print("bad kind/confidence", i); ok = False
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        print("misprint without corrected", i); ok = False
    if x["kind"] != "misprint_in_print" and "corrected" in x:
        print("corrected on a non-misprint", i); ok = False
    c = counts.setdefault(x["page"], [0, 0])
    c[1 if x["kind"] == "misprint_in_print" else 0] += 1
    f = x["fix"]
    if f is None:
        continue
    o = f["old"]
    k = pages[x["page"]].count(o)
    if k != 1:
        print("entry", i, "page", x["page"], "old occurs", k, "times:", repr(o)); ok = False
    if MARK.search(o) or MARK.search(f["new"]):
        print("entry", i, "touches a marker line"); ok = False
# apply in order, page by page
work = dict(pages)
for i, x in enumerate(d):
    f = x["fix"]
    if f is None:
        continue
    t = work[x["page"]]
    if t.count(f["old"]) != 1:
        print("after earlier fixes, entry", i, "old occurs", t.count(f["old"])); ok = False
        continue
    work[x["page"]] = t.replace(f["old"], f["new"])
print("page fixes:", "OK" if ok else "PROBLEMS")
print("counts (normal/misprint):", {p: f"{a}/{b}" for p, (a, b) in sorted(counts.items())})

# marker edits quoted in the notes
def unq(s):
    return s.replace(BS + "n", "\n")

edits = {"diplomatic": [], "current": []}
for x in d:
    if x["kind"] != "marker":
        continue
    note = x["note"]
    pairs = re.findall(r"replace '(.*?)' by '(.*?)'", note)
    if x["page"] == 426:
        old = unq(pairs[0][0])
        dip = unq(pairs[0][1])
        cur = unq(re.search(r"Current: the same old string by '(.*?)'\.", note).group(1))
        edits["diplomatic"].append((x["page"], old, dip))
        edits["current"].append((x["page"], old, cur))
    else:
        for o, nw in pairs:
            edits["diplomatic"].append((x["page"], unq(o), unq(nw)))
            edits["current"].append((x["page"], unq(o), unq(nw)))
for layer in ("diplomatic", "current"):
    t = open(SGA6 + "\\" + layer + r"\main.tex", encoding="utf-8", newline="").read()
    for p, o, nw in edits[layer]:
        k = t.count(o)
        print(layer, "marker edit of page", p, "old occurs", k)
        if k != 1:
            ok = False
            continue
        t = t.replace(o, nw)
    # page texts after the moves
    ms = [m for m in MARK.finditer(t)]
    for j, m in enumerate(ms):
        fo = int(m.group(2))
        if 426 <= fo <= 431:
            body = t[m.end():ms[j + 1].start()] if j + 1 < len(ms) else t[m.end():]
            body = body.strip("\n")
            print("  ", layer, fo, "starts", repr(body[:45]), "| ends", repr(body[-45:]))
print("ALL OK" if ok else "PROBLEMS FOUND")
