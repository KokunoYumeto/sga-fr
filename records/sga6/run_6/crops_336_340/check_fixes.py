"""Check findings_336_340.json: every fix old occurs exactly once in its page file; apply all fixes in memory (in list order and reversed) to check that they do not interfere; count per page."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
F = json.loads((RUN / "findings_336_340.json").read_text(encoding="utf-8"))
pages = {p: (RUN / "b336_340" / f"page_{p}.tex").read_text(encoding="utf-8") for p in range(336, 341)}
ok = True
counts = {}
for i, x in enumerate(F):
    p = x["page"]
    c = counts.setdefault(p, [0, 0])
    c[1 if x["kind"] == "misprint_in_print" else 0] += 1
    fx = x.get("fix")
    if fx:
        n = pages[p].count(fx["old"])
        bad = "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]
        print(i, p, x["kind"], "count", n, "MARKER!" if bad else "")
        ok &= (n == 1) and not bad
    if x["kind"] == "misprint_in_print" and "corrected" not in x:
        print(i, "misprint without corrected"); ok = False
for order in ("forward", "reverse"):
    seq = F if order == "forward" else list(reversed(F))
    t = dict(pages)
    for x in seq:
        fx = x.get("fix")
        if fx:
            p = x["page"]
            if t[p].count(fx["old"]) != 1:
                print(order, "conflict at", p, repr(fx["old"][:40])); ok = False
            t[p] = t[p].replace(fx["old"], fx["new"], 1)
    if order == "forward":
        final = t
    else:
        for p in pages:
            if t[p] != final[p]:
                print("order-dependent result on page", p); ok = False
print("counts", counts)
print("ALL OK" if ok else "PROBLEMS")
