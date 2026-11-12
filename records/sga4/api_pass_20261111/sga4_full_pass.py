"""SGA 4 API pass, 11 Nov 2026: every page of SGA 4 checked against the scans by two models, as agreed with the user
(SGA4_API_COMPARISON_20261110.md; RUNBOOK_20261110.md "SGA 4 METHOD AGREED"):

  opus  Claude Opus 5.5 (claude-opus-5-5), effort high, adaptive thinking, Message Batches API (batch price $2/$10)
  sol   GPT-6.1 Sol (gpt-6.1-sol), reasoning effort max, OpenAI Responses API, Flex tier (Flex price $1/$5)

The prompt is the comparison's API prompt (sga4_api_compare.api_prompt: the subagent prompt of render_sga4_prompt.py
with its tool sentences adapted), rendered for each batch of up to five printed pages of one exposé, with two changes:
the batch paragraph names the scans and the TeX by file name only (no local paths), and the sentence on the page's
first comment line describes the overlaps of the automatic page cut (build_pages.py) instead of the hand cut's shared
lines. Each page is sent as its TeX (batches/<KEY>/page_FFF.tex: one comment line, then whole lines of the working
copy sga4/diplomatic) and its four strips (strips/t<tome>/pFFF_s1..4.png; Exposés XVII-XVIII also the four witness
strips), greyscale JPEG quality 90 at full resolution, as in the comparison. The six batches of the comparison
(30 pages) are not sent again: their opus55-high and sol61-max answers are imported.

Money: one Anthropic batch at a time, each with a worst case (input estimate + requests x output cap) under 45 % of
the credit still assumed left; OpenAI requests in groups, one group at a time. Every batch or group is logged in
RUNS.jsonl and gets a row in compute_cost_ledger/LEDGER.jsonl. The pass stops when a model's billed total passes
1.5 times its expected total (Opus $45, Sol $43).

usage:
  python -I sga4_full_pass.py batches                 write BATCHES.json and the page TeX files (no API call)
  python -I sga4_full_pass.py prompt KEY              print one batch's API prompt
  python -I sga4_full_pass.py import-comparison       copy the comparison's answers for its six batches
  (KEY_NOTE=<note>) python -I ..\\..\\claude_tools\\run_with_note_key.py sga4_full_pass.py run-opus --credit USD [--max-requests N] [--max-batches N]
  python -I sga4_full_pass.py run-sol --credit USD [--group N] [--max-groups N]   (OpenAI key: enr_pilot)
  python -I sga4_full_pass.py run-sol-window --credit USD [--window N] [--chunk N] [--max-tries N] [--queued-limit MIN]
                                                      [--retry-wait SEC] [--vary-key]
                                                      (at most N in flight)
  python -I sga4_full_pass.py status
"""
import base64
import importlib.util
import io
import json
import os
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request
from collections import OrderedDict
from datetime import datetime, timezone

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
W = HERE.parent
DIP = W / "sga4" / "diplomatic"
STRIPS = HERE / "strips"
BDIR = HERE / "batches"
ANS = HERE / "answers"
RUNS = HERE / "RUNS.jsonl"
LEDGER = pathlib.Path(r"C:\Users\user\Documents\compute_cost_ledger\LEDGER.jsonl")

CONFIGS = {
    "opus": {"provider": "anthropic", "model": "claude-opus-5-5", "effort": "high", "price": (2.0, 10.0),
             "list": (4.0, 20.0), "max_out": 64000, "max_out_retry": 128000, "cmp": "opus55-high",
             "name": "Claude Opus 5.5, effort high, Message Batches API", "expected": 45.0},
    "sol": {"provider": "openai", "model": "gpt-6.1-sol", "effort": "max", "price": (1.0, 5.0), "list": (2.0, 10.0),
            "max_out": 128000, "max_out_retry": 128000, "cmp": "sol61-max",
            "name": "GPT-6.1 Sol, reasoning effort max, Flex tier", "expected": 43.0},
}
STOP_FACTOR = 1.5
COMPARISON = {("05", 41): "041_045", ("10", 51): "051_055", ("01", 101): "101_105", ("17", 361): "361_365",
              ("08", 386): "386_390", ("04", 401): "401_405"}
MAX_BODY = 190_000_000  # bytes of one Message Batches request body (the API's limit is 256 MB)


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    argv, sys.argv = sys.argv, [str(path)]
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.argv = argv
    return mod


C = _load("sga4_api_compare", W / "sga4_api_compare.py")  # the comparison: prompt adaptation, JPEG, OpenAI loader
R4, SAB = C.R4, C.SAB
NOTE = (W / "NOTE_4.txt").read_text(encoding="utf-8").strip()

TEX_OLD = ("and says when the first or the last line is shared with the neighbouring page; the page on the far side of "
           "such a line begins at the word just before that line's \\pageoriginale.")
TEX_NEW = ("and says which of its lines may also belong to a neighbouring page: a line that the page break divides "
           "(the break falls one or two words before that line's \\pageoriginale), or a display or heading next to the "
           "break that the TeX alone cannot place. Text in such lines that this page does not print belongs to the "
           "neighbouring page and is checked there: report nothing for it.")


def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


# ---------------------------------------------------------------- batches and page TeX

def pages_table():
    return json.loads((HERE / "PAGES.json").read_text(encoding="utf-8"))


def file_lines(fn, _cache={}):
    if fn not in _cache:
        _cache[fn] = (DIP / fn / f"{fn}.tex").read_text(encoding="utf-8").split("\n")
    return _cache[fn]


def overlap_note(o, a, z):
    x, y = max(o["lines"][0], a), min(o["lines"][1], z)
    if x > y:
        return None
    r1, r2 = x - a + 1, y - a + 1
    rel = f"line {r1}" if r1 == r2 else f"lines {r1}-{r2}"
    src = f"source line {x}" if x == y else f"source lines {x}-{y}"
    if o["where"] == "start" and o["kind"] == "block":
        return (f"its {rel} ({src}; the line after this comment is line 1), before this page's \\pageoriginale, may "
                f"end p. {o['other']} instead of opening this page")
    if o["where"] == "start":
        return (f"its {rel} ({src}) may also hold the last words of p. {o['other']}: this page begins one or two "
                f"words before that line's \\pageoriginale")
    if o["kind"] == "block":
        return (f"its {rel} ({src}), before the \\pageoriginale of p. {o['other']}, may open p. {o['other']} instead "
                f"of ending this page")
    return (f"its last line ({src}) also holds the first words of p. {o['other']}, from one or two words before its "
            f"\\pageoriginale on")


def page_tex(p):
    lines = file_lines(p["file"])
    a, z = p["lines"]
    ts = f" = typescript page {p['typescript']}" if p.get("typescript") else ""
    notes = [n for n in (overlap_note(o, a, z) for o in p["overlaps"]) if n]
    head = (f"% from {p['tex']}, lines {a}-{z} (SGA 4 Tome {p['tome']}, LNM {p['lnm']}, printed page {p['folio']}{ts}"
            + ("; " + "; ".join(notes) if notes else "") + ")\n")
    return head + "\n".join(lines[a - 1:z]) + "\n"


def build_batches():
    groups = OrderedDict()
    for p in pages_table():
        groups.setdefault((p["tome"], p["file"], (p["folio"] - 1) // 5), []).append(p)
    out = []
    for (tome, fn, _), ps in groups.items():
        a, z = ps[0]["folio"], ps[-1]["folio"]
        assert [p["folio"] for p in ps] == list(range(a, z + 1)), (fn, a, z)
        key = f"t{tome}_{fn}_{a:03d}_{z:03d}"
        cmp = COMPARISON.get((fn, a))
        if cmp:
            assert z == a + 4, key
        d = BDIR / key
        d.mkdir(parents=True, exist_ok=True)
        for p in ps:
            (d / f"page_{p['folio']:03d}.tex").write_text(page_tex(p), encoding="utf-8", newline="")
        out.append({"key": key, "tome": tome, "lnm": ps[0]["lnm"], "file": fn, "expose": ps[0]["expose"],
                    "tex": ps[0]["tex"], "first": a, "last": z, "folios": [p["folio"] for p in ps],
                    "witness": all(p.get("witness_pdf_page") for p in ps),
                    "source": f"comparison run_4 {cmp}" if cmp else "this pass"})
    (HERE / "BATCHES.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    return out


def batches():
    return json.loads((HERE / "BATCHES.json").read_text(encoding="utf-8"))


def batch_pages(b):
    idx = {(p["tome"], p["folio"]): p for p in pages_table()}
    return [idx[(b["tome"], f)] for f in b["folios"]]


# ---------------------------------------------------------------- prompt

def batch_text(b, ps):
    """The comparison's batch paragraph (render_sga4_prompt.batch_text), with file names instead of local paths."""
    bullet, scans = "", ""
    if b["witness"]:
        w = ps[0]
        bullet = (f"\n- page_NNN_w1.png ... page_NNN_w4.png: the same page in a second scan, Springer's lossless "
                  f"300-dpi scan of Exposés XVII-XVIII ({w['witness']}, PDF page = printed page - "
                  f"{w['folio'] - w['witness_pdf_page']}). The main scan of this tome stores the text as a JBIG2 mask, "
                  f"whose symbol coding can put a look-alike in place of a character: where a letter, digit, index "
                  f"or prime matters and the main strip is faint, broken or doubtful, read the witness strip before "
                  f"deciding; do not read the witness strips otherwise.")
    elif b["tome"] == "3":
        scans = (" This tome's scan stores the text as a JBIG2 mask, whose symbol coding can put a look-alike in "
                 "place of a character, and there is no second scan of these pages: where a stroke is faint, broken "
                 "or doubtful, say so and do not guess.")
    else:
        scans = " These pages have one scan only: where a stroke is faint or broken, say so and do not guess."
    a, z = b["first"], b["last"]
    printed = f"printed pages {a}-{z}" if a != z else f"printed page {a}"
    t0, t1 = ps[0].get("typescript"), ps[-1].get("typescript")
    ts = (f" (typescript pages {t0} to {t1})" if a != z else f" (typescript page {t0})") if t0 and t1 else ""
    p0, p1 = ps[0]["pdf_page"], ps[-1]["pdf_page"]
    pdf = f"PDF pages {p0}-{p1}" if p0 != p1 else f"PDF page {p0}"
    l0, l1 = ps[0]["lines"][0], ps[-1]["lines"][1]
    para = (f"\n\nThese pages: SGA 4 Tome {b['tome']} (LNM {b['lnm']}), Exposé {b['expose']}, {printed}{ts}; main "
            f"scan {ps[0]['scan']} (300 dpi), {pdf}; TeX from {b['tex']}, lines {l0}-{l1} (read only: labels, "
            f"\\bibitem entries and the neighbouring pages can be looked up there); the edition's macros are defined "
            f"in macros.tex and numerotation.tex in sga4/diplomatic/fichiers-configuration-latex.{scans}")
    return bullet + para


def api_prompt(b):
    ps = batch_pages(b)
    t = R4.template()
    t = (t.replace("{TITLE}", R4.TITLE).replace("{NOTE}", NOTE).replace("{FOLDER}", f"batches/{b['key']}")
         .replace("{PAGES}", ", ".join(str(f) for f in b["folios"]))
         .replace("{OUTFILE}", f"answers/{b['key']}.json"))
    anchor = "\n\nCompare word by word"
    assert t.count(anchor) == 1
    t = t.replace(anchor, batch_text(b, ps) + anchor)
    # the comparison's adaptation for the API (sga4_api_compare.api_prompt), step by step
    folder = re.findall(r"^Folder: [^\n]*\n", t, flags=re.M)
    assert len(folder) == 1
    t = t.replace(folder[0], "")
    pairs = [(C.STRIPS_TOOL, C.STRIPS_API)] + C.REPLACE + (C.WITNESS if "page_NNN_w1.png" in t else [])
    for old, new in pairs:
        assert t.count(old) == 1, "passage not found exactly once in %s: %s" % (b["key"], old[:70])
        t = t.replace(old, new)
    macros = re.findall(r"the edition's macros are defined in macros\.tex and numerotation\.tex in [^\n]*?"
                        r"fichiers-configuration-latex\.", t)
    assert len(macros) == 1
    t = t.replace(macros[0], "the edition's macros are defined in its macros.tex and numerotation.tex (not attached).")
    assert t.count("Write JSON to ") == 1
    t = t[:t.index("Write JSON to ")] + SAB.API_OUT + "\n"
    # this pass: the page cut is automatic, with overlaps named on the first line
    assert t.count(TEX_OLD) == 1
    t = t.replace(TEX_OLD, TEX_NEW)
    left = [w for w in C.LEFTOVERS if w in t]
    assert not left, "tool wording left in %s: %s" % (b["key"], left)
    assert "Users" not in t and "user" not in t
    return t


def user_content(b, provider):
    def text(s):
        return {"type": "text", "text": s} if provider == "anthropic" else {"type": "input_text", "text": s}

    def image(p):
        d = C.jpeg_b64(p)
        if provider == "anthropic":
            return {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": d}}
        return {"type": "input_image", "detail": "high", "image_url": "data:image/jpeg;base64," + d}

    content = [text("Your pages: %s." % ", ".join(str(f) for f in b["folios"]))]
    sd = STRIPS / f"t{b['tome']}"
    for f in b["folios"]:
        tex = (BDIR / b["key"] / f"page_{f:03d}.tex").read_text(encoding="utf-8")
        content.append(text("Page %d. Its TeX:\n```latex\n%s\n```\nIts scan, four strips, top to bottom:" % (f, tex)))
        content += [image(sd / f"p{f:03d}_s{s}.png") for s in range(1, 5)]
        wit = [sd / f"p{f:03d}_w{s}.png" for s in range(1, 5)]
        if all(p.exists() for p in wit):
            content.append(text("The same page in the second scan (the witness), four strips, top to bottom:"))
            content += [image(p) for p in wit]
    content.append(text("Check these pages."))
    return content


# ---------------------------------------------------------------- bookkeeping

def runs():
    if not RUNS.exists():
        return []
    return [json.loads(x) for x in RUNS.read_text(encoding="utf-8").splitlines() if x.strip()]


def log_run(rec):
    with open(RUNS, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def billed(cfg_name):
    return sum(r["billed_usd"] for r in runs() if r["event"] == "done" and r["config"] == cfg_name)


def answered(cfg_name, key):
    return (ANS / cfg_name / f"{key}.json").exists()


def save_answer(cfg_name, b, text, extra):
    """Write the findings list, coordinator message and raw text; check each fix's old against the page TeX."""
    d = ANS / cfg_name
    d.mkdir(parents=True, exist_ok=True)
    key = b["key"]
    (d / f"{key}_raw.txt").write_text(text, encoding="utf-8")
    res = {"batch": key, "parsed": False, "findings": None, **extra}
    try:
        obj = json.loads(text[text.index("{"):text.rindex("}") + 1])
        fl = obj.get("findings", [])
        assert isinstance(fl, list)
        tex = {f: (BDIR / key / f"page_{f:03d}.tex").read_text(encoding="utf-8") for f in b["folios"]}
        fixes = [f for f in fl if isinstance(f.get("fix"), dict)]
        bad = [f for f in fixes if tex.get(int(f.get("page", 0) or 0), "").count(f["fix"].get("old", "\0")) != 1]
        (d / f"{key}_coordinator.md").write_text(str(obj.get("coordinator", "")) + "\n", encoding="utf-8")
        (d / f"{key}.json").write_text(json.dumps(fl, ensure_ascii=False, indent=1), encoding="utf-8")
        res.update(parsed=True, findings=len(fl), fixes=len(fixes),
                   misprints=sum(1 for f in fl if f.get("kind") == "misprint_in_print"), fix_old_not_unique=len(bad))
    except Exception as e:  # noqa: BLE001
        res["parse_error"] = str(e)[:200]
    return res


def ledger_row(cfg_name, rec, n_pages):
    cfg = CONFIGS[cfg_name]
    in_t, out_t = rec["input_tokens"], rec["output_tokens"]
    lp = (in_t * cfg["list"][0] + out_t * cfg["list"][1]) / 1e6
    reqs = rec["requests"]
    row = {"id": f"sga4-pass-{cfg_name}-{rec['seq']:02d}", "date": rec["ended"][:10],
           "project": "SGA 4 scan check: API pass of all pages (sga_scan_check_20261105/sga4_api_pass_20261111)",
           "work": f"{len(reqs)} batches of up to five printed pages ({n_pages} pages): {reqs[0]['batch']} ... "
                   f"{reqs[-1]['batch']}",
           "method": ("Message Batches API" if cfg["provider"] == "anthropic" else "Responses API, Flex tier, background")
           + ", sga4_full_pass.py",
           "model": cfg["model"] if cfg["provider"] == "anthropic" else "GPT-6.1 Sol (OpenAI)", "effort": cfg["effort"],
           "requests": len(reqs), "pages": n_pages, "input_tokens": in_t, "output_tokens": out_t,
           "usd_batch_price": round(rec["billed_usd"], 2), "list_price_usd": round(lp, 2),
           "per_page_billed_usd": round(rec["billed_usd"] / max(1, n_pages), 4),
           "key": "account B ($200 key, Untitled 1939.md)" if cfg["provider"] == "anthropic"
           else "OpenAI project key (Untitled 1936.md)",
           "basis": "measured: usage of each answer; price %s/%s per million (%s)" % (
               cfg["price"][0], cfg["price"][1], "batch" if cfg["provider"] == "anthropic" else "Flex"),
           "wall_minutes": rec["wall_minutes"],
           "result": "%d findings (%d fixes, %d misprints of the print)" % (
               sum(r.get("findings") or 0 for r in reqs), sum(r.get("fixes") or 0 for r in reqs),
               sum(r.get("misprints") or 0 for r in reqs))}
    if rec.get("batch_id"):
        row["batch"] = rec["batch_id"]
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def est_input_tokens(b, prompt):
    """Input estimate for the worst case: 2,000 tokens per image (measured about 1,700 in the comparison) plus text."""
    n_img = len(b["folios"]) * (8 if b["witness"] else 4)
    tex = sum(len((BDIR / b["key"] / f"page_{f:03d}.tex").read_text(encoding="utf-8")) for f in b["folios"])
    return 2000 * n_img + (len(prompt) + tex) // 2


def stop_check(cfg_name):
    cfg = CONFIGS[cfg_name]
    spent = billed(cfg_name)
    if spent > STOP_FACTOR * cfg["expected"]:
        raise SystemExit(f"STOP: {cfg_name} has billed ${spent:.2f}, more than {STOP_FACTOR} x ${cfg['expected']:.0f}")
    return spent


# ---------------------------------------------------------------- Anthropic (Message Batches)

def a_api(method, url, body=None):
    h = {"x-api-key": os.environ.get("ANTHROPIC_API_KEY", ""), "anthropic-version": "2023-06-01",
         "content-type": "application/json"}
    data = body if isinstance(body, (bytes, type(None))) else json.dumps(body).encode("utf-8")
    for attempt in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=h, method=method),
                                        timeout=1800) as r:
                return r.status, r.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            return e.code, e.read().decode("utf-8", "replace")
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            print(time.strftime("%H:%M:%S"), "network error", str(e)[:120], "- retrying", flush=True)
            time.sleep(30 * (attempt + 1))
    return 0, "network error"


def opus_pending():
    open_ids = {r["batch_id"] for r in runs() if r["config"] == "opus" and r["event"] == "submitted"}
    done_ids = {r.get("batch_id") for r in runs() if r["config"] == "opus" and r["event"] == "done"}
    if open_ids - done_ids:
        return sorted(open_ids - done_ids)
    return []


def run_opus(credit, max_requests=60, max_batches=10 ** 6):
    assert os.environ.get("ANTHROPIC_API_KEY"), "run through run_with_note_key.py with KEY_NOTE"
    cfg = CONFIGS["opus"]
    for bid in opus_pending():  # a batch submitted earlier and not collected: collect it first
        collect_opus(bid)
    tried = {}
    for r in runs():
        if r["config"] == "opus" and r["event"] == "done":
            for q in r["requests"]:
                tried[q["batch"]] = q
    n_batches = 0
    while n_batches < max_batches:
        n_batches += 1
        todo = [b for b in batches() if b["source"] == "this pass" and not answered("opus", b["key"])]
        if not todo:
            print("opus: every batch answered", flush=True)
            return
        spent = stop_check("opus")
        left = credit - spent
        cap = 0.45 * left
        reqs, worst, size, n_pages = [], 0.0, 0, 0
        for b in todo:
            prev = tried.get(b["key"])
            mo = cfg["max_out_retry"] if prev and prev.get("stop_reason") == "max_tokens" else cfg["max_out"]
            prompt = api_prompt(b)
            params = {"model": cfg["model"], "max_tokens": mo, "thinking": {"type": "adaptive"},
                      "output_config": {"effort": cfg["effort"]}, "system": prompt,
                      "messages": [{"role": "user", "content": user_content(b, "anthropic")}]}
            w = est_input_tokens(b, prompt) * cfg["price"][0] / 1e6 + mo * cfg["price"][1] / 1e6
            r = {"custom_id": b["key"], "params": params}
            s = len(json.dumps(r))
            if reqs and (worst + w > cap or size + s > MAX_BODY or len(reqs) >= max_requests):
                break
            reqs.append(r)
            worst += w
            size += s
            n_pages += len(b["folios"])
        if worst > cap:
            raise SystemExit(f"opus: the next request's worst case ${worst:.2f} is over 45 % of the credit left "
                             f"(${left:.2f}): not submitted")
        seq = 1 + sum(1 for r in runs() if r["config"] == "opus" and r["event"] == "submitted")
        print(f"opus batch {seq}: {len(reqs)} requests, {n_pages} pages, {size / 1e6:.0f} MB, worst case ${worst:.2f};"
              f" billed so far ${spent:.2f}; credit assumed left ${left:.2f}", flush=True)
        code, body = a_api("POST", "https://api.anthropic.com/v1/messages/batches",
                           json.dumps({"requests": reqs}).encode("utf-8"))
        if code != 200:
            raise SystemExit("batch submit %d: %s" % (code, body[:500]))
        bt = json.loads(body)
        log_run({"event": "submitted", "config": "opus", "seq": seq, "batch_id": bt["id"], "submitted": now(),
                 "keys": [r["custom_id"] for r in reqs], "pages": n_pages, "worst_case_usd": round(worst, 2),
                 "billed_before_usd": round(spent, 2), "credit_assumed_left_usd": round(left, 2)})
        print("batch", bt["id"], flush=True)
        del reqs
        collect_opus(bt["id"])
        for r in runs():
            if r["config"] == "opus" and r["event"] == "done" and r["batch_id"] == bt["id"]:
                for q in r["requests"]:
                    tried[q["batch"]] = q


def collect_opus(bid):
    cfg = CONFIGS["opus"]
    sub = next(r for r in runs() if r["config"] == "opus" and r["event"] == "submitted" and r["batch_id"] == bid)
    while True:
        code, r = a_api("GET", "https://api.anthropic.com/v1/messages/batches/" + bid)
        if code != 200:
            print(time.strftime("%H:%M:%S"), "status", code, r[:200], flush=True)
            time.sleep(120)
            continue
        s = json.loads(r)
        print(time.strftime("%H:%M:%S"), s["processing_status"], json.dumps(s["request_counts"]), flush=True)
        if s["processing_status"] == "ended":
            break
        time.sleep(60)
    code, body = a_api("GET", s["results_url"])
    assert code == 200, (code, body[:300])
    bmap = {b["key"]: b for b in batches()}
    reqs, tin, tout, n_pages = [], 0, 0, 0
    for line in body.splitlines():
        if not line.strip():
            continue
        x = json.loads(line)
        key = x["custom_id"]
        if x["result"]["type"] != "succeeded":
            reqs.append({"batch": key, "result": x["result"]["type"], "detail": json.dumps(x["result"])[:300]})
            print(key, x["result"]["type"], flush=True)
            continue
        m = x["result"]["message"]
        u = m.get("usage") or {}
        i_t = (u.get("input_tokens") or 0) + (u.get("cache_creation_input_tokens") or 0) + (
            u.get("cache_read_input_tokens") or 0)
        tin += i_t
        tout += u.get("output_tokens") or 0
        n_pages += len(bmap[key]["folios"])
        extra = {"result": "succeeded", "stop_reason": m.get("stop_reason"), "input_tokens": i_t,
                 "output_tokens": u.get("output_tokens"), "model": m.get("model")}
        if m.get("stop_reason") != "end_turn":
            (ANS / "opus").mkdir(parents=True, exist_ok=True)
            text = "".join(c.get("text", "") for c in m["content"] if c.get("type") == "text")
            (ANS / "opus" / f"{key}_raw_{m.get('stop_reason')}.txt").write_text(text, encoding="utf-8")
            reqs.append({"batch": key, **extra, "parsed": False})
            print(key, "stop_reason", m.get("stop_reason"), "- not saved, to be sent again", flush=True)
            continue
        text = "".join(c.get("text", "") for c in m["content"] if c.get("type") == "text")
        res = save_answer("opus", bmap[key], text, extra)
        reqs.append(res)
    cost = tin * cfg["price"][0] / 1e6 + tout * cfg["price"][1] / 1e6
    t0 = datetime.fromisoformat(s["created_at"].replace("Z", "+00:00"))
    t1 = datetime.fromisoformat(s["ended_at"].replace("Z", "+00:00"))
    rec = {"event": "done", "config": "opus", "seq": sub["seq"], "batch_id": bid, "ended": s["ended_at"],
           "wall_minutes": round((t1 - t0).total_seconds() / 60, 1), "input_tokens": tin, "output_tokens": tout,
           "billed_usd": round(cost, 4), "requests": sorted(reqs, key=lambda q: q["batch"])}
    log_run(rec)
    ledger_row("opus", rec, n_pages)
    print(f"opus batch {sub['seq']}: tokens in {tin}, out {tout}, ${cost:.2f} at batch price, "
          f"{rec['wall_minutes']} min; opus total ${billed('opus'):.2f}", flush=True)


# ---------------------------------------------------------------- OpenAI (Responses API, Flex tier)

def run_sol(credit, group=25, max_groups=10 ** 6):
    P = C.openai_mod()
    cfg = CONFIGS["sol"]
    tries = {}
    n_groups = 0
    while n_groups < max_groups:
        n_groups += 1
        todo = [b for b in batches() if b["source"] == "this pass" and not answered("sol", b["key"])]
        todo = [b for b in todo if tries.get(b["key"], 0) < 3]
        if not todo:
            print("sol: every batch answered (or tried three times)", flush=True)
            return
        spent = stop_check("sol")
        grp = todo[:group]
        seq = 1 + sum(1 for r in runs() if r["config"] == "sol" and r["event"] == "submitted")
        worst = 0.0
        bodies = {}
        for b in grp:
            prompt = api_prompt(b)
            mo = cfg["max_out"]
            bodies[b["key"]] = {"model": cfg["model"], "instructions": prompt,
                                "input": [{"role": "user", "content": user_content(b, "openai")}],
                                "reasoning": {"effort": cfg["effort"]}, "max_output_tokens": mo,
                                "background": True, "service_tier": "flex"}
            worst += est_input_tokens(b, prompt) * cfg["price"][0] / 1e6 + mo * cfg["price"][1] / 1e6
        if worst > 0.45 * (credit - spent):
            raise SystemExit(f"sol: the group's worst case ${worst:.2f} is over 45 % of the credit assumed left "
                             f"(${credit - spent:.2f}): not submitted")
        log_run({"event": "submitted", "config": "sol", "seq": seq, "submitted": now(), "keys": list(bodies),
                 "pages": sum(len(b["folios"]) for b in grp), "worst_case_usd": round(worst, 2),
                 "billed_before_usd": round(spent, 2), "credit_assumed_left_usd": round(credit - spent, 2)})
        print(f"sol group {seq}: {len(bodies)} requests, worst case ${worst:.2f}; billed so far ${spent:.2f}",
              flush=True)
        state = {k: {"tries": 0} for k in bodies}
        t_start = time.time()
        for k in bodies:
            _sol_submit(P, k, bodies[k], state)
        flying = {k for k, v in state.items() if v.get("id")}
        while flying:
            time.sleep(30)
            for k in sorted(flying):
                code, r = P.call("GET", "%s/%s" % (P.API, state[k]["id"]))
                st = r.get("status")
                if st in ("queued", "in_progress") or code >= 500 or code == 0:
                    continue
                flying.discard(k)
                state[k]["t1"] = time.time()
                if st == "failed" and state[k]["tries"] < 3:
                    print(k, "failed", json.dumps(r.get("error"))[:200], "- resubmitting", flush=True)
                    if "overloaded" in json.dumps(r.get("error")):
                        time.sleep(45)  # Flex capacity: wait before sending it again
                    _sol_submit(P, k, bodies[k], state)
                    if state[k].get("id"):
                        flying.add(k)
                    continue
                state[k]["response"] = r
                u = r.get("usage") or {}
                print(k, st, r.get("service_tier"), "in", u.get("input_tokens"), "out", u.get("output_tokens"),
                      flush=True)
        bmap = {b["key"]: b for b in grp}
        reqs, tin, tout, n_pages = [], 0, 0, 0
        for k in bodies:
            r = state[k].get("response") or {}
            u = r.get("usage") or {}
            tin += u.get("input_tokens") or 0
            tout += u.get("output_tokens") or 0
            tries[k] = tries.get(k, 0) + 1
            extra = {"result": r.get("status"), "incomplete": r.get("incomplete_details"),
                     "service_tier": r.get("service_tier"), "input_tokens": u.get("input_tokens"),
                     "output_tokens": u.get("output_tokens"),
                     "reasoning_tokens": (u.get("output_tokens_details") or {}).get("reasoning_tokens"),
                     "response_id": r.get("id"), "tries": state[k]["tries"],
                     "minutes": round((state[k].get("t1", time.time()) - state[k].get("t0", t_start)) / 60, 1)}
            (ANS / "sol").mkdir(parents=True, exist_ok=True)
            (ANS / "sol" / f"{k}_response.json").write_text(
                json.dumps({x: v for x, v in r.items() if x != "instructions"}, ensure_ascii=False, indent=1)[:2000000],
                encoding="utf-8")
            if r.get("status") != "completed":
                reqs.append({"batch": k, **extra, "parsed": False})
                print(k, "not completed:", r.get("status"), json.dumps(r.get("incomplete_details") or r.get("error"))
                      [:200], flush=True)
                continue
            n_pages += len(bmap[k]["folios"])
            text = "".join(c.get("text", "") for o in r.get("output", []) if o.get("type") == "message"
                           for c in o.get("content", []))
            reqs.append(save_answer("sol", bmap[k], text, extra))
        cost = (tin * cfg["price"][0] + tout * cfg["price"][1]) / 1e6
        rec = {"event": "done", "config": "sol", "seq": seq, "ended": now(),
               "wall_minutes": round((time.time() - t_start) / 60, 1), "input_tokens": tin, "output_tokens": tout,
               "billed_usd": round(cost, 4), "requests": reqs}
        log_run(rec)
        ledger_row("sol", rec, n_pages)
        print(f"sol group {seq}: tokens in {tin}, out {tout}, ${cost:.2f} at the Flex price, {rec['wall_minutes']} "
              f"min; sol total ${billed('sol'):.2f}", flush=True)


def run_sol_window(credit, window=40, chunk=50, max_tries=3, queued_limit=None, retry_wait=None, vary_key=False):
    """Sol with at most `window` requests in flight: a slow Flex request no longer holds up the others. The worst case
    of the requests in flight stays under 45 % of the credit assumed left; requests are logged in chunks of `chunk`
    (RUNS.jsonl and a ledger row per chunk), and each answer is saved as soon as it arrives. A request that the Flex
    tier turns away (overloaded) is sent again, at most `max_tries` times in this run, after a wait that doubles from
    one minute (at most fifteen), or after `retry_wait` seconds each time when given (Flex turns requests away at
    admission, with a retry-after of six seconds). With `vary_key`, each try carries its own prompt_cache_key
    (routing metadata only; the request is otherwise the same), for requests that Flex keeps turning away. With `queued_limit` (minutes), a request that Flex leaves queued that long is
    cancelled (no tokens are billed for a queued request) and sent again, as one of its tries: on 11 Nov five requests
    stayed queued for two to three hours while later ones were answered, and held the first run open."""
    P = C.openai_mod()
    cfg = CONFIGS["sol"]
    bmap = {b["key"]: b for b in batches()}
    rr = runs()
    done_seqs = {r["seq"] for r in rr if r["config"] == "sol" and r["event"] in ("done", "abandoned")}
    still_open = {k for r in rr if r["config"] == "sol" and r["event"] == "submitted" and r["seq"] not in done_seqs
                  for k in r["keys"]}  # requests of a group still running in another process: not sent twice
    todo = [b["key"] for b in batches() if b["source"] == "this pass" and not answered("sol", b["key"])
            and b["key"] not in still_open]
    if not todo:
        print("sol: every batch answered", flush=True)
        return
    seq0 = sum(1 for r in runs() if r["config"] == "sol" and r["event"] == "submitted")
    chunks = [todo[i:i + chunk] for i in range(0, len(todo), chunk)]
    chunk_of = {k: n for n, ks in enumerate(chunks) for k in ks}
    cstate = [{"keys": ks, "seq": seq0 + 1 + n, "logged": False, "reqs": {}, "t0": None} for n, ks in enumerate(chunks)]
    queue = list(todo)
    wait_until = {}
    tries = {k: 0 for k in todo}
    flying = {}
    worst_one = {}

    def finish(k, r, extra):
        cs = cstate[chunk_of[k]]
        (ANS / "sol").mkdir(parents=True, exist_ok=True)
        (ANS / "sol" / f"{k}_response.json").write_text(
            json.dumps({x: v for x, v in r.items() if x != "instructions"}, ensure_ascii=False, indent=1)[:2000000],
            encoding="utf-8")
        if r.get("status") == "completed":
            text = "".join(c.get("text", "") for o in r.get("output", []) if o.get("type") == "message"
                           for c in o.get("content", []))
            cs["reqs"][k] = save_answer("sol", bmap[k], text, extra)
        else:
            cs["reqs"][k] = {"batch": k, **extra, "parsed": False}
            print(k, "not completed:", r.get("status"), json.dumps(r.get("incomplete_details") or r.get("error"))[:200],
                  flush=True)
        if len(cs["reqs"]) == len(cs["keys"]):
            reqs = [cs["reqs"][x] for x in cs["keys"]]
            tin = sum(q.get("input_tokens") or 0 for q in reqs)
            tout = sum(q.get("output_tokens") or 0 for q in reqs)
            cost = (tin * cfg["price"][0] + tout * cfg["price"][1]) / 1e6
            rec = {"event": "done", "config": "sol", "seq": cs["seq"], "ended": now(),
                   "wall_minutes": round((time.time() - cs["t0"]) / 60, 1), "input_tokens": tin, "output_tokens": tout,
                   "billed_usd": round(cost, 4), "requests": reqs, "mode": f"rolling window of {window}"}
            log_run(rec)
            ledger_row("sol", rec, sum(len(bmap[q["batch"]]["folios"]) for q in reqs if q.get("parsed")))
            print(f"sol group {cs['seq']}: tokens in {tin}, out {tout}, ${cost:.2f} at the Flex price, "
                  f"{rec['wall_minutes']} min; sol total ${billed('sol'):.2f}", flush=True)

    while queue or flying:
        spent = stop_check("sol")
        # fill the window
        while queue and len(flying) < window:
            k = next((x for x in queue if wait_until.get(x, 0) <= time.time()), None)
            if k is None:
                break
            b = bmap[k]
            prompt = api_prompt(b)
            w = est_input_tokens(b, prompt) * cfg["price"][0] / 1e6 + cfg["max_out"] * cfg["price"][1] / 1e6
            if sum(worst_one[x] for x in flying) + w > 0.45 * (credit - spent):
                if not flying:
                    raise SystemExit(f"sol: one request's worst case ${w:.2f} is over 45 % of the credit assumed left "
                                     f"(${credit - spent:.2f}): stopped")
                break
            body = {"model": cfg["model"], "instructions": prompt,
                    "input": [{"role": "user", "content": user_content(b, "openai")}],
                    "reasoning": {"effort": cfg["effort"]}, "max_output_tokens": cfg["max_out"],
                    "background": True, "service_tier": "flex"}
            if vary_key:
                body["prompt_cache_key"] = f"sga4-{k}-try{tries[k] + 1}"
            cs = cstate[chunk_of[k]]
            if not cs["logged"]:
                cs["logged"], cs["t0"] = True, time.time()
                wc = sum(est_input_tokens(bmap[x], api_prompt(bmap[x])) * cfg["price"][0] / 1e6 +
                         cfg["max_out"] * cfg["price"][1] / 1e6 for x in cs["keys"])
                log_run({"event": "submitted", "config": "sol", "seq": cs["seq"], "submitted": now(),
                         "keys": cs["keys"], "pages": sum(len(bmap[x]["folios"]) for x in cs["keys"]),
                         "worst_case_usd": round(wc, 2), "billed_before_usd": round(spent, 2),
                         "credit_assumed_left_usd": round(credit - spent, 2), "mode": f"rolling window of {window}"})
                print(f"sol group {cs['seq']}: {len(cs['keys'])} requests in a rolling window of {window}; billed so "
                      f"far ${spent:.2f}", flush=True)
            st = {"tries": 0}
            _sol_submit(P, k, body, {k: st})
            tries[k] += 1
            queue.remove(k)
            if st.get("id"):
                flying[k] = {"id": st["id"], "t0": st["t0"], "body": body}
                worst_one[k] = w
            else:
                finish(k, {"status": "not submitted"}, {"result": "not submitted", "tries": tries[k]})
        time.sleep(30)
        for k in list(flying):
            code, r = P.call("GET", "%s/%s" % (P.API, flying[k]["id"]))
            stt = r.get("status")
            if stt == "queued" and queued_limit and time.time() - flying[k]["t0"] > queued_limit * 60:
                cc, cr = P.call("POST", "%s/%s/cancel" % (P.API, flying[k]["id"]))
                if cr.get("status") != "cancelled":
                    continue  # it started meanwhile, or the cancel failed: polled again in the next round
                fl = flying.pop(k)
                if tries[k] < max_tries:
                    print(k, f"queued for over {queued_limit} min: cancelled, sent again", flush=True)
                    queue.insert(0, k)
                    continue
                print(k, f"queued for over {queued_limit} min: cancelled, no tries left", flush=True)
                finish(k, cr, {"result": "cancelled", "incomplete": None, "service_tier": cr.get("service_tier"),
                               "input_tokens": None, "output_tokens": None, "reasoning_tokens": None,
                               "response_id": cr.get("id"), "tries": tries[k],
                               "minutes": round((time.time() - fl["t0"]) / 60, 1)})
                continue
            if stt in ("queued", "in_progress") or code >= 500 or code == 0:
                continue
            fl = flying.pop(k)
            if stt == "failed" and tries[k] < max_tries:
                pause = retry_wait if retry_wait else min(60 * 2 ** (tries[k] - 1), 900)
                print(k, "failed", json.dumps(r.get("error"))[:160], f"- sent again in {pause / 60:g} min", flush=True)
                queue.insert(0, k)
                wait_until[k] = time.time() + pause
                continue
            u = r.get("usage") or {}
            extra = {"result": stt, "incomplete": r.get("incomplete_details"), "service_tier": r.get("service_tier"),
                     "input_tokens": u.get("input_tokens"), "output_tokens": u.get("output_tokens"),
                     "reasoning_tokens": (u.get("output_tokens_details") or {}).get("reasoning_tokens"),
                     "response_id": r.get("id"), "tries": tries[k], "minutes": round((time.time() - fl["t0"]) / 60, 1)}
            print(k, stt, r.get("service_tier"), "in", u.get("input_tokens"), "out", u.get("output_tokens"), flush=True)
            finish(k, r, extra)
    print("sol: rolling run finished; unanswered:",
          [b["key"] for b in batches() if b["source"] == "this pass" and not answered("sol", b["key"])], flush=True)


def _sol_submit(P, key, body, state):
    for attempt in range(8):
        state[key]["tries"] += 1
        code, r = P.call("POST", P.API, body)
        if code < 300 and r.get("id"):
            state[key].update(id=r["id"], t0=time.time())
            print(key, "submitted", r["id"], r.get("status"), flush=True)
            return
        print(key, "submit failed", code, json.dumps(r.get("error"))[:300], flush=True)
        if code == 400:
            return
        time.sleep(60)


# ---------------------------------------------------------------- comparison import, status

def import_comparison():
    src = W / "run_4" / "api_compare"
    rr = [json.loads(x) for x in (src / "RUNS.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    for cfg_name, cfg in CONFIGS.items():
        done = next(r for r in rr if r["event"] == "done" and r["run"] == cfg["cmp"])
        for b in batches():
            if not b["source"].startswith("comparison"):
                continue
            old = b["source"].split()[-1]
            fl = json.loads((src / cfg["cmp"] / f"findings_{old}.json").read_text(encoding="utf-8"))
            d = ANS / cfg_name
            d.mkdir(parents=True, exist_ok=True)
            for f in fl:
                f["_from"] = f"comparison run_4/api_compare/{cfg['cmp']}/findings_{old}.json"
            (d / f"{b['key']}.json").write_text(json.dumps(fl, ensure_ascii=False, indent=1), encoding="utf-8")
            for suffix in ("_coordinator.md", "_raw.txt"):
                p = src / cfg["cmp"] / f"findings_{old}{suffix}"
                if p.exists():
                    (d / f"{b['key']}{suffix}").write_text(p.read_text(encoding="utf-8"), encoding="utf-8")
        print(cfg_name, "imported from", cfg["cmp"], "billed then $%.2f for 30 pages" % done["billed_usd"])


def status():
    bs = batches()
    new = [b for b in bs if b["source"] == "this pass"]
    for cfg_name in CONFIGS:
        n = sum(1 for b in bs if answered(cfg_name, b["key"]))
        print(f"{cfg_name}: answered {n} of {len(bs)} batches ({len(new)} sent in this pass); billed in this pass "
              f"${billed(cfg_name):.2f}")


if __name__ == "__main__":
    a = sys.argv[1:]
    cmd = a[0]
    if cmd == "batches":
        bs = build_batches()
        print(len(bs), "batches,", sum(len(b["folios"]) for b in bs), "pages;", sum(1 for b in bs if b["source"] ==
              "this pass"), "to send")
    elif cmd == "prompt":
        b = next(x for x in batches() if x["key"] == a[1])
        sys.stdout.write(api_prompt(b))
    elif cmd == "import-comparison":
        import_comparison()
    elif cmd == "run-opus":
        run_opus(float(a[a.index("--credit") + 1]),
                 int(a[a.index("--max-requests") + 1]) if "--max-requests" in a else 60,
                 int(a[a.index("--max-batches") + 1]) if "--max-batches" in a else 10 ** 6)
    elif cmd == "run-sol":
        run_sol(float(a[a.index("--credit") + 1]),
                int(a[a.index("--group") + 1]) if "--group" in a else 25,
                int(a[a.index("--max-groups") + 1]) if "--max-groups" in a else 10 ** 6)
    elif cmd == "run-sol-window":
        run_sol_window(float(a[a.index("--credit") + 1]),
                       int(a[a.index("--window") + 1]) if "--window" in a else 40,
                       int(a[a.index("--chunk") + 1]) if "--chunk" in a else 50,
                       int(a[a.index("--max-tries") + 1]) if "--max-tries" in a else 3,
                       float(a[a.index("--queued-limit") + 1]) if "--queued-limit" in a else None,
                       float(a[a.index("--retry-wait") + 1]) if "--retry-wait" in a else None,
                       "--vary-key" in a)
    elif cmd == "status":
        status()
