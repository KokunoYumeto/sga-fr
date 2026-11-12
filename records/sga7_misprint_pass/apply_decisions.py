"""Apply the misprint-pass decisions to a corrected French SGA layer (sga7i/current, sga7ii/current), as
ega_scan_check_20261101/apply_misprint_decisions.py does for EGA: an "apply" edit is made when "old" occurs exactly
once in the page (marker to marker, the file's opening text going to the page before its first marker) of the named
file, keeps the brace balance and touches no page marker. Every decision is logged in MISPRINT_PASS_LOG_<vol>.jsonl;
applied edits also go to FIXLOG_<vol>_CURRENT.jsonl (source "misprint_pass"), so that they reach the translations.
Rejected edits: MISPRINT_PASS_LEFT_<vol>.json.
usage: python -I apply_decisions.py VOL DECISIONS.json [...] [--dry] [--why]"""
import collections
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
sys.path.insert(0, str(W))
import sga_config as C  # noqa: E402

vol = sys.argv[1]
dry = "--dry" in sys.argv
paths = [pathlib.Path(a) for a in sys.argv[2:] if not a.startswith("--")]
HERE = W / "misprint_pass"
mis = {f"{vol}:{k}": x for k, x in enumerate(json.loads((W / f"MISPRINTS_{vol}.json").read_text(encoding="utf-8")))}
LOG = HERE / f"MISPRINT_PASS_LOG_{vol}.jsonl"
LEFT = HERE / f"MISPRINT_PASS_LEFT_{vol}.json"
done = {json.loads(l)["id"] for l in LOG.read_text(encoding="utf-8").splitlines() if l.strip()} if LOG.exists() else set()
segs = C.pages(vol, "current")
texts = {f: f.read_text(encoding="utf-8") for f in C.files(vol, "current")}


def bal(s):
    s = s.replace(chr(92) * 2, "").replace(chr(92) + "{", "").replace(chr(92) + "}", "")
    return s.count("{") - s.count("}")


stats = collections.Counter()
left = json.loads(LEFT.read_text(encoding="utf-8")) if LEFT.exists() else []
edits, logrecs = [], []
for path in paths:
    for d in json.loads(path.read_text(encoding="utf-8")):
        i = str(d.get("id"))
        if i in done or i not in mis:
            stats["skipped"] += 1
            continue
        x = mis[i]
        page = int(x["page"])
        rec = dict(id=i, page=page, decision=d.get("decision"), note=d.get("note"), batch=path.stem)
        if d.get("decision") == "apply":
            old = (d.get("old") or "").replace("\r\n", "\n")
            new = (d.get("new") or "").replace("\r\n", "\n")
            why, hit = None, None
            if not old or old == new:
                why = "empty or unchanged"
            elif bal(old) != bal(new):
                why = "brace balance"
            elif C.MARK.search(old) or C.MARK.search(new):
                why = "page marker"
            else:
                hits = [(f, k) for f, a, b in segs.get(page, []) if f.name == (d.get("file") or f.name)
                        for k in range(a, b) if texts[f].startswith(old, k) and k + len(old) <= b]
                if len(hits) != 1:
                    hits = [(f, k) for f, a, b in segs.get(page, [])
                            for k in range(a, b) if texts[f].startswith(old, k) and k + len(old) <= b]
                if len(hits) == 1:
                    hit = hits[0]
                else:
                    why = f"old occurs {len(hits)} times on page {page}"
            if hit and any(f == hit[0] and k < hit[1] + len(old) and hit[1] < k + len(o) for f, k, o, _ in edits):
                hit, why = None, "overlaps another edit"
            if hit is None:
                rec.update(outcome="left", why=why)
                left.append(dict(d, page=page, why=why))
            else:
                edits.append((hit[0], hit[1], old, new))
                rec.update(outcome="applied", file=hit[0].name, old=old, new=new)
        else:
            rec["outcome"] = d.get("decision")
        stats[rec["outcome"]] += 1
        logrecs.append(rec)
if "--why" in sys.argv:
    for r in logrecs:
        if r.get("outcome") == "left":
            print("  left", r["id"], r.get("why"))
if not dry:
    changed = set()
    for f, k, old, new in sorted(edits, key=lambda e: (str(e[0]), -e[1])):
        assert texts[f][k:k + len(old)] == old
        texts[f] = texts[f][:k] + new + texts[f][k + len(old):]
        changed.add(f)
    for f in changed:
        f.write_text(texts[f], encoding="utf-8", newline="")
    with open(LOG, "a", encoding="utf-8") as fh:
        for r in logrecs:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(W / f"FIXLOG_{vol}_CURRENT.jsonl", "a", encoding="utf-8") as fh:
        for r in logrecs:
            if r.get("outcome") == "applied":
                fh.write(json.dumps(dict(vol=vol, file=r["file"], page=r["page"], old=r["old"], new=r["new"],
                                         kind="misprint_pass", source="misprint_pass", id=r["id"]),
                                    ensure_ascii=False) + "\n")
    LEFT.write_text(json.dumps(left, ensure_ascii=False, indent=1), encoding="utf-8")
print(("dry run " if dry else "") + ", ".join(f"{k} {v}" for k, v in sorted(stats.items())))
