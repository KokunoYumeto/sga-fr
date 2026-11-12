"""Batches for the misprint pass of a corrected French SGA layer (sga7i/current, sga7ii/current), as for EGA on
5 November (ega_scan_check_20261101/make_misprint_batches.py).

The scan check recorded every misprint of the print in MISPRINTS_<vol>.json (page, where, printed reading, correct
reading, what the TeX did). The diplomatic layer keeps the printed reading; the corrected layer must give the correct
one, but it still holds whatever the TeX had before the check (often the printed reading). Each batch lists, per printed
page, the corrected layer's text of the page, the misprints recorded there, and the diplomatic edits made for misprints
on that page (OLD -> NEW = the TeX before -> the printed reading). Misprints already decided (MISPRINT_PASS_LOG_<vol>)
are left out.
usage: python -I make_batches.py VOL [ITEMS_PER_BATCH=120] [--max-kb=280]"""
import collections
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
sys.path.insert(0, str(W))
import sga_config as C  # noqa: E402

args = [a for a in sys.argv[1:] if not a.startswith("--")]
opts = dict(a[2:].split("=", 1) for a in sys.argv[1:] if a.startswith("--") and "=" in a)
vol = args[0]
per = int(args[1]) if len(args) > 1 else 120
max_kb = int(opts.get("max-kb", 280))
HERE = W / "misprint_pass"
LOG = HERE / f"MISPRINT_PASS_LOG_{vol}.jsonl"
done = {json.loads(l)["id"] for l in LOG.read_text(encoding="utf-8").splitlines() if l.strip()} if LOG.exists() else set()
mis = [dict(x, mid=f"{vol}:{k}") for k, x in enumerate(json.loads((W / f"MISPRINTS_{vol}.json").read_text(encoding="utf-8")))]
mis = [x for x in mis if x["mid"] not in done]
dfix = collections.defaultdict(list)
for line in (W / f"FIXLOG_{vol}.jsonl").read_text(encoding="utf-8").splitlines():
    if line.strip():
        x = json.loads(line)
        if x.get("kind") == "misprint_in_print":
            dfix[int(x["page"])].append((x["old"], x["new"]))
segs = C.pages(vol, "current")
bypage = collections.defaultdict(list)
for x in mis:
    bypage[int(x["page"])].append(x)


def page_text(p):
    return [(f.name, f.read_text(encoding="utf-8")[a:b]) for f, a, b in segs.get(p, [])]


batches, cur, n, kb = [], [], 0, 0
for p in sorted(bypage):
    add = sum(len(t.encode("utf-8")) for _, t in page_text(p)) / 1024 + len(bypage[p]) * 0.6
    if cur and (n + len(bypage[p]) > per or kb + add > max_kb):
        batches.append(cur)
        cur, n, kb = [], 0, 0
    cur.append(p)
    n += len(bypage[p])
    kb += add
if cur:
    batches.append(cur)
out = HERE / f"batches_{vol}"
out.mkdir(parents=True, exist_ok=True)
index = []
for b, ps in enumerate(batches, 1):
    name = f"misprints_{vol}_{b:03d}"
    lines = [f"# Misprint pass of the corrected French SGA {vol[0]} {vol[1:]}, {name}", ""]
    ids = []
    for p in ps:
        lines.append(f"=================== PAGE {p} ===================")
        for fname, txt in page_text(p):
            lines.append(f"----- corrected edition, {fname}, page {p} -----")
            lines.append(txt.rstrip("\n"))
        lines.append(f"----- misprints recorded on page {p} -----")
        for x in bypage[p]:
            ids.append(x["mid"])
            lines.append(f"[id {x['mid']}]")
            for key, label in (("where", "WHERE"), ("print", "PRINT"), ("correct", "CORRECT"), ("tex_did", "TEX BEFORE"),
                               ("note", "NOTE")):
                if x.get(key):
                    lines.append(f"{label}: {x[key]}")
            lines.append("")
        if dfix.get(p):
            lines.append("(diplomatic edits made on this page for misprints, OLD -> NEW = the TeX before -> the printed reading:)")
            for o, nw in dfix[p]:
                lines.append("  OLD: " + o.replace("\n", "\\n") + "\n  NEW: " + nw.replace("\n", "\\n"))
            lines.append("")
    (out / f"{name}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="")
    index.append(dict(batch=name, items=len(ids), ids=ids, pages=[ps[0], ps[-1]]))
(out / "BATCHES.json").write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")
sizes = [(out / f"{x['batch']}.txt").stat().st_size // 1024 for x in index] or [0]
print(vol, len(index), "batches;", sum(x["items"] for x in index), "misprints; KB min/max/mean", min(sizes), max(sizes),
      sum(sizes) // max(1, len(sizes)))
