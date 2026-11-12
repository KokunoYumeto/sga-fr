"""Verify findings_401_405.json against the page files (read-only):
- every fix's old occurs exactly once in its page file at the time it is applied (fixes applied in list order),
  and report olds that do not occur in the untouched page file (dependent fixes);
- no old or new touches a marker line;
- every old is also unique in the whole text of pp. 401-405 (so it stays unique after the marker moves);
- which olds also match the current layer (informational)."""
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = "C:/Users/user/Documents/sga_scan_check_20261105/run_5"
BASE = "C:/Users/user/Documents/sga_scan_check_20261105/sga5"
MARK = re.compile(r"%%%%%%%%%%  scan idx (\d+)  \|  folio (\d+)  %%%%%%%%%%")
F = json.load(open(RUN + "/findings_401_405.json", encoding="utf-8"))
pages = {p: open(f"{RUN}/b401_405/page_{p}.tex", encoding="utf-8", newline="").read() for p in range(401, 406)}
orig = dict(pages)
whole = "".join(pages[p] for p in range(401, 406))
cur_t = open(f"{BASE}/current/s5.tex", encoding="utf-8", newline="").read()
ms = list(MARK.finditer(cur_t))
i0 = next(j for j, m in enumerate(ms) if int(m.group(2)) == 401)
cur = cur_t[ms[i0].start(): ms[i0 + 5].end() + 200]   # current layer, pp. 401-405 plus a little of 406

problems = 0
counts = {}
for k, f in enumerate(F):
    p = f["page"]
    key = (p, f["kind"] == "misprint_in_print")
    counts[key] = counts.get(key, 0) + 1
    for fld in ("page", "where", "scan", "tex", "kind", "confidence", "fix", "note"):
        if fld not in f:
            print("MISSING FIELD", fld, k)
            problems += 1
    if f["kind"] == "misprint_in_print" and "corrected" not in f:
        print("MISSING corrected", k)
        problems += 1
    if f["kind"] != "misprint_in_print" and "corrected" in f:
        print("corrected on a non-misprint", k)
        problems += 1
    if f["fix"] is None:
        continue
    old, new = f["fix"]["old"], f["fix"]["new"]
    if "%%%%" in old or "%%%%" in new:
        print("MARKER IN FIX", k)
        problems += 1
    n_now = pages[p].count(old)
    n_orig = orig[p].count(old)
    n_whole = whole.count(old)
    n_cur = cur.count(old)
    flag = "" if n_now == 1 else "  <-- NOT UNIQUE AT APPLICATION"
    if n_now != 1:
        problems += 1
    extra = []
    if n_orig != 1:
        extra.append(f"in untouched page file: {n_orig}")
    if n_whole > 1:
        extra.append(f"in pp. 401-405: {n_whole}")
    if n_cur != 1:
        extra.append(f"current layer: {n_cur}")
    print(f"{k:2d} p{p} {f['kind'][:10]:10s} {repr(old)[:60]:62s} now={n_now}{flag} {'; '.join(extra)}")
    pages[p] = pages[p].replace(old, new, 1)
    whole = "".join(pages[q] for q in range(401, 406))

print()
print("problems:", problems)
for p in range(401, 406):
    print(p, "normal", counts.get((p, False), 0), "misprint", counts.get((p, True), 0))
# sanity: braces balance in every page after all fixes
for p in range(401, 406):
    t = pages[p]
    print(p, "braces", t.count("{") - t.count("}"), "emph", t.count("\\emph{"), "dollars", t.count("$") % 2)
