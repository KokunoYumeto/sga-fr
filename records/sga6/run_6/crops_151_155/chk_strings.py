import json, pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
F = json.loads((RUN / "findings_151_155.json").read_text(encoding="utf-8"))
pages = {}
for p in range(151, 156):
    b = (RUN / "b151_155" / f"page_{p}.tex").read_bytes()
    assert b"\r" not in b, p
    pages[p] = b.decode("utf-8")

bad = 0
counts = {}
for i, f in enumerate(F):
    counts.setdefault(f["page"], [0, 0])
    counts[f["page"]][1 if f["kind"] == "misprint_in_print" else 0] += 1
    fx = f["fix"]
    if fx is None:
        continue
    t = pages[f["page"]]
    n = t.count(fx["old"])
    if n != 1:
        bad += 1
        print("NOT UNIQUE", i, f["page"], n, repr(fx["old"]))
    if "%%%%%%%%%%" in fx["old"] or "%%%%%%%%%%" in fx["new"]:
        bad += 1
        print("MARKER IN FIX", i)
    if re.search(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", fx["old"] + fx["new"]):
        bad += 1
        print("CONTROL CHAR", i)
print("uniqueness problems:", bad)
print("counts (normal, misprint):", counts)

# apply all fixes of each page in JSON order, and in reverse order: every old must still occur exactly once
for order in ("forward", "reverse"):
    for p, t in pages.items():
        fs = [f for f in F if f["page"] == p and f["fix"]]
        if order == "reverse":
            fs = fs[::-1]
        for f in fs:
            o, n = f["fix"]["old"], f["fix"]["new"]
            c = t.count(o)
            if c != 1:
                print(order, "conflict on page", p, repr(o), c)
            t = t.replace(o, n, 1)
        # brace balance and \( \) balance of the result
        if t.count("{") - t.count(r"\{") != t.count("}") - t.count(r"\}"):
            print(order, "brace imbalance", p)
        if t.count(r"\(") != t.count(r"\)"):
            print(order, "inline math imbalance", p)
        if order == "forward":
            (RUN / "crops_151_155" / f"sim_{p}.tex").write_text(t, encoding="utf-8", newline="\n")
print("done")
