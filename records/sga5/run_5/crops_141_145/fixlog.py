import json, sys
sys.stdout.reconfigure(encoding="utf-8")
rows = [json.loads(l) for l in open(r"C:\Users\user\Documents\sga_scan_check_20261105\FIXLOG_5.jsonl", encoding="utf-8") if l.strip()]
n = 0
for r in rows:
    o = r.get("old") or ""
    if "\[" in o and "\]" in o:
        n += 1
        if n <= 5:
            print(json.dumps(r, ensure_ascii=False)[:500]); print()
print("display-to-inline fixes logged:", n)
pages = sorted({r.get("page") for r in rows if isinstance(r.get("page"), int)})
print("pages in FIXLOG_5:", pages[:3], "...", pages[-5:])
