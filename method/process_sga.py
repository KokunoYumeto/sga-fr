"""Process one finished SGA checker batch: apply its fixes to the diplomatic edition and replay the transcription
fixes on the corrected edition ("current").

- A fix is applied when its "old" occurs exactly once in the page's text (marker to next marker, plus the opening text
  of a file that continues the page). Leftovers go to MANUAL_<vol>_<findings stem>.json.
- Misprints of the print are recorded in MISPRINTS_<vol>.json (page, print, correct reading, what the TeX did); the
  corrected edition keeps the correct reading, so reversions to a printed misprint are not replayed there.
- Every change is logged: FIXLOG_<vol>.jsonl (diplomatic) and FIXLOG_<vol>_CURRENT.jsonl (corrected edition).
- Marker lines are never changed: a fix whose old or new contains one is left for the coordinator.

usage: python -I process_sga.py VOL FINDINGS.json [--dry]
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from sga_config import MARK, W, pages  # noqa: E402

vol, findings = sys.argv[1], pathlib.Path(sys.argv[2])
dry = "--dry" in sys.argv
mis_path = W / f"MISPRINTS_{vol}.json"
misprints = json.loads(mis_path.read_text(encoding="utf-8")) if mis_path.exists() else []
items = json.loads(findings.read_text(encoding="utf-8"))
manual, applied, replayed, rep_manual = [], 0, 0, []


def apply_on_page(edition, page, old, new):
    """Apply old -> new on the page of the edition when old occurs exactly once there; returns (file, ok, count)."""
    spans = pages(vol, edition).get(page, [])
    hits = []
    for f, s, e in spans:
        t = f.read_text(encoding="utf-8")
        k = t.find(old, s, e)
        while k >= 0 and k + len(old) <= e:
            hits.append((f, k))
            k = t.find(old, k + 1, e)
    if len(hits) != 1:
        return None, False, len(hits)
    f, k = hits[0]
    t = f.read_text(encoding="utf-8")
    if not dry:
        f.write_text(t[:k] + new + t[k + len(old):], encoding="utf-8", newline="")
    return f, True, 1


for x in items:
    page = int(x["page"])
    if x.get("kind") == "misprint_in_print":
        misprints.append(dict(vol=vol, page=page, where=x.get("where"), print=x.get("scan"), correct=x.get("corrected"),
                              tex_did=x.get("tex"), note=x.get("note"), source=findings.name))
    fix = x.get("fix")
    if not fix or not fix.get("old") or fix.get("old") == fix.get("new"):
        continue
    old = fix["old"].replace("\r\n", "\n")
    new = (fix.get("new") or "").replace("\r\n", "\n")
    if MARK.search(old) or MARK.search(new):
        manual.append(dict(x, why="touches a marker line"))
        continue
    f, ok, n = apply_on_page("diplomatic", page, old, new)
    if not ok:
        manual.append(dict(x, why=f"old occurs {n} times on the page"))
        continue
    applied += 1
    rec = dict(vol=vol, file=f.name, page=page, old=old, new=new, kind=x.get("kind"), source=findings.name)
    if not dry:
        with open(W / f"FIXLOG_{vol}.jsonl", "a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    if x.get("kind") == "misprint_in_print":
        continue  # a reversion to the printed misprint: the corrected edition keeps the correct reading
    f2, ok2, n2 = apply_on_page("current", page, old, new)
    if ok2:
        replayed += 1
        if not dry:
            with open(W / f"FIXLOG_{vol}_CURRENT.jsonl", "a", encoding="utf-8") as fh:
                fh.write(json.dumps(dict(rec, file=f2.name), ensure_ascii=False) + "\n")
    else:
        rep_manual.append(dict(rec, why=f"old occurs {n2} times on the current page"))

if not dry:
    mis_path.write_text(json.dumps(misprints, ensure_ascii=False, indent=1), encoding="utf-8")
    (W / f"MANUAL_{vol}_{findings.stem}.json").write_text(json.dumps(manual, ensure_ascii=False, indent=1),
                                                           encoding="utf-8")
    if rep_manual:
        p = W / f"REPLAY_MANUAL_{vol}.json"
        prev = json.loads(p.read_text(encoding="utf-8")) if p.exists() else []
        p.write_text(json.dumps(prev + rep_manual, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"{findings.name}: applied {applied}, manual {len(manual)}, replayed on current {replayed}, "
      f"current by hand {len(rep_manual)}, misprints now {len(misprints)}" + (" (dry run)" if dry else ""))
