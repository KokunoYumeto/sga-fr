"""Check findings_181_185.json: every fix's old occurs exactly once in its page_NNN.tex, never touches a marker line;
apply all fixes of a page in JSON order to a copy (in memory) and report failures; count entries per page."""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
R = r"C:\Users\user\Documents\sga_scan_check_20261105\run_6"
F = json.load(open(R + r"\findings_181_185.json", encoding="utf-8"))
pages = {}
ok = True
for i, x in enumerate(F):
    p = x["page"]
    if p not in pages:
        pages[p] = open(R + rf"\b181_185\page_{p:03d}.tex", encoding="utf-8").read()
    t = pages[p]
    for key in ("page", "where", "scan", "tex", "kind", "confidence", "fix", "note"):
        if key not in x:
            print("missing key", key, "in entry", i)
            ok = False
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        print("misprint without corrected:", i)
        ok = False
    fx = x["fix"]
    if fx is None:
        continue
    old = fx["old"]
    n = t.count(old)
    if n != 1:
        print(f"entry {i} p.{p}: old occurs {n} times: {old!r}")
        ok = False
    if "%%%%%%%%%%" in old or "%%%%%%%%%%" in fx["new"]:
        print(f"entry {i}: touches a marker line")
        ok = False
    if "\r" in old:
        print(f"entry {i}: CR in old")
        ok = False
# sequential application per page
for p, t in sorted(pages.items()):
    cur = t
    for i, x in enumerate(F):
        if x["page"] != p or x["fix"] is None:
            continue
        old, new = x["fix"]["old"], x["fix"]["new"]
        if cur.count(old) != 1:
            print(f"sequential: entry {i} p.{p} old found {cur.count(old)} times after earlier fixes")
            ok = False
            continue
        cur = cur.replace(old, new, 1)
    if "\r" in t:
        print("page", p, "has CR line ends")
# control characters
for i, x in enumerate(F):
    s = json.dumps(x, ensure_ascii=False)
    for ch in s:
        if ord(ch) < 32 and ch not in "\n":
            print("control char in entry", i, repr(ch))
            ok = False
cnt = {}
for x in F:
    k = "m" if x["kind"] == "misprint_in_print" else "n"
    cnt.setdefault(x["page"], {"n": 0, "m": 0})[k] += 1
print(cnt)
print("OK" if ok else "PROBLEMS")
