"""simulate_apply.py: apply the fixes of findings_521_525.json in memory, in order, page by page (writes nothing)."""
import json, pathlib, sys
sys.stdout.reconfigure(encoding='utf-8')
RUN = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105\run_6")
data = json.loads((RUN / "findings_521_525.json").read_text(encoding="utf-8"))
texts = {n: (RUN / "b521_525" / f"page_{n}.tex").read_text(encoding="utf-8") for n in range(521, 526)}
for f in data:
    if f["fix"] is None:
        continue
    t = texts[f["page"]]
    n = t.count(f["fix"]["old"])
    assert n == 1, (f["page"], f["fix"]["old"], n)
    texts[f["page"]] = t.replace(f["fix"]["old"], f["fix"]["new"], 1)
for n, t in texts.items():
    marker_lines = [l for l in t.split("\n") if l.startswith("%%%%%%%%%%")]
    print(n, "markers intact:", len(marker_lines) == 1)
print(texts[524][texts[524].find("désignons"):texts[524].find("désignons") + 60])
print(texts[524][texts[524].find("rang $n>0$"):texts[524].find("rang $n>0$") + 40])
print("sequential application OK")
