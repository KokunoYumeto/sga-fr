"""Figures of the SGA 4 API pass for the README and the report: pages, categories, applied fixes, app-check pages,
misprints, cost per model (this pass from RUNS.jsonl, the comparison's six batches from its RUNS.jsonl).

usage: python -I summary.py
"""
import json
import pathlib
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
W = HERE.parent


def load(name, default=None):
    p = HERE / name
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else default


pages = load("PAGES.json")
merged = load("MERGED.json", [])
app = load("PAGES_FOR_APP_CHECK.json", [])
cats = Counter(it["category"] for pg in merged for it in pg["items"])
fixlog = [json.loads(x) for x in (W / "FIXLOG_4.jsonl").read_text(encoding="utf-8").splitlines()] \
    if (W / "FIXLOG_4.jsonl").exists() else []
fixcur = [json.loads(x) for x in (W / "FIXLOG_4_CURRENT.jsonl").read_text(encoding="utf-8").splitlines()] \
    if (W / "FIXLOG_4_CURRENT.jsonl").exists() else []
runs = [json.loads(x) for x in (HERE / "RUNS.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
cmp_runs = [json.loads(x) for x in (W / "run_4" / "api_compare" / "RUNS.jsonl").read_text(encoding="utf-8").splitlines()
            if x.strip()]
out = {"pages_with_tex": len(pages), "pages_merged": len(merged),
       "pages_by_tome": dict(Counter(p["tome"] for p in pages)), "categories": dict(cats),
       "fixes_applied_diplomatic": len(fixlog), "fixes_replayed_current": len(fixcur),
       "pages_with_applied_fixes": len({(f["tome"], f["page"]) for f in fixlog}),
       "app_check_pages": len(app), "app_check_items": sum(len(p["items"]) for p in app),
       "app_check_pages_by_reason": dict(Counter(r for p in app for r in p["why"])),
       "app_check_pages_by_tome": dict(Counter(p["tome"] for p in app)),
       "agreed_misprints": len(load("AGREED_MISPRINTS.json", [])),
       "opus_only_misprints": len(load("OPUS_ONLY_MISPRINTS.json", [])),
       "sol_only_misprints": len(load("SOL_ONLY_MISPRINTS.json", [])),
       "one_model_misprints_by_class": {m: dict(Counter(x.get("class") for x in load(f"{m.upper()}_ONLY_MISPRINTS.json",
                                                                                     [])))
                                        for m in ("opus", "sol")},
       "held_agreed_fixes_by_reason": dict(Counter(
           w.split(" (")[0] for p in app for it in p["items"] if it["category"] == "agreed_fix_held"
           for w in it["why"].split(", held: ", 1)[-1].split("; "))),
       "apply_by_hand": len(load("APPLY_MANUAL.json", [])),
       "replay_by_hand": len(json.loads((W / "REPLAY_MANUAL_4.json").read_text(encoding="utf-8")))
       if (W / "REPLAY_MANUAL_4.json").exists() else 0,
       "cut_reports": len(load("CUT_REPORTS.json", []))}
for cfg, cmp_name in (("opus", "opus55-high"), ("sol", "sol61-max")):
    done = [r for r in runs if r["config"] == cfg and r["event"] == "done"]
    reqs = [q for r in done for q in r["requests"]]
    c = next(r for r in cmp_runs if r["event"] == "done" and r["run"] == cmp_name)
    out[cfg] = {"batches_or_chunks": len(done), "requests": len(reqs),
                "answered": sum(1 for q in reqs if q.get("parsed")),
                "input_tokens": sum(r["input_tokens"] for r in done), "output_tokens": sum(r["output_tokens"] for r in done),
                "billed_usd_this_pass": round(sum(r["billed_usd"] for r in done), 2),
                "billed_usd_comparison_batches": c["billed_usd"],
                "billed_usd_all_sga4": round(sum(r["billed_usd"] for r in done) + c["billed_usd"], 2)}
    out[cfg]["per_page_usd"] = round(out[cfg]["billed_usd_all_sga4"] / len(pages), 4)
(HERE / "SUMMARY.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps(out, ensure_ascii=False, indent=1))
