import json, glob, os
W = r"C:\Users\user\Documents\sga_scan_check_20261105\run_5"
n1 = n2 = n3 = 0
for fn in sorted(glob.glob(os.path.join(W, "findings_3*.json"))):
    try:
        L = json.load(open(fn, encoding="utf-8"))
    except Exception:
        continue
    for r in L:
        if r.get("kind") == "misprint_in_print" and r.get("fix") is None and n1 < 2:
            print("NULLFIX", os.path.basename(fn), json.dumps(r, ensure_ascii=True)[:600])
            n1 += 1
        if r.get("kind") == "misprint_in_print" and r.get("fix") and n2 < 2:
            print("FIX", os.path.basename(fn), json.dumps(r, ensure_ascii=True)[:600])
            n2 += 1
        if r.get("kind") == "marker" and n3 < 2:
            print("MARKER", os.path.basename(fn), json.dumps(r, ensure_ascii=True)[:900])
            n3 += 1
