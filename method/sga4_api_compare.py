"""SGA 4 over the API, compared with the in-app subagent check (10 Nov 2026).

The six SGA 4 spot-check batches of run_4 (30 printed pages; the reference is the findings of the Claude Opus 5.5
subagents, run_4/findings_FFF_LLL.json) are checked again over the API with the same inputs (each page's TeX and its
four strips; for Expose XVII also the four witness strips) and the same checker prompt (run_4/prompt_FFF_LLL.txt, as
rendered by render_sga4_prompt.py), adapted only where it speaks of tools, as sga_api_batch.py does for SGA 7: the
strips come attached (greyscale JPEG, quality 90, full resolution), the files a subagent could look up are named as not
attached, and the JSON comes back in the answer instead of being written to a file. Nothing is applied to any TeX.

Configurations (one request per batch, six requests each; one run at a time):
  fable52-medium  Claude Fable 5.2 (claude-fable-5-2), effort medium, Message Batches API
  opus55-high     Claude Opus 5.5 (claude-opus-5-5), effort high, Message Batches API
  sol61-high      GPT-6.1 Sol (gpt-6.1-sol), reasoning effort high, OpenAI Responses API, Flex tier, background
  sol61-max       GPT-6.1 Sol, reasoning effort max (the highest value the API accepts: none, minimal, low, medium,
                  high, xhigh, max), Flex tier, background

Before each run, what the earlier runs of this comparison cost plus the new run's worst case (its input tokens at the
run's price plus six times the output cap of 128,000 tokens) must stay within the budget (default $30). Each run is
logged in run_4/api_compare/RUNS.jsonl and in C:\\Users\\user\\Documents\\compute_cost_ledger\\LEDGER.jsonl.
Answers: run_4/api_compare/<config>/findings_FFF_LLL.json (the findings list), _coordinator.md, _raw.txt.

usage:
  python -I sga4_api_compare.py prompts               write run_4/api_compare/prompts/api_prompt_FFF_LLL.txt, no API call
  (KEY_NOTE = the note with the Anthropic key)  python -I ..\\claude_tools\\run_with_note_key.py sga4_api_compare.py run fable52-medium
  python -I sga4_api_compare.py run sol61-high        (the OpenAI key is read by enr_pilot from the user's note)
  add --budget N to change the budget; "collect CONFIG" resumes waiting for a run that was submitted
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
from datetime import datetime, timezone

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(__file__).resolve().parent
R = W / "run_4"
OUT = R / "api_compare"
RUNS = OUT / "RUNS.jsonl"
LEDGER = pathlib.Path(r"C:\Users\user\Documents\compute_cost_ledger\LEDGER.jsonl")
BATCHES = [(41, 45), (51, 55), (101, 105), (361, 365), (386, 390), (401, 405)]
PAGES = 30
MAX_OUT = 128000
CONFIGS = {  # price: what the run is billed per million tokens (batch or Flex price); list: the list price
    "fable52-medium": {"provider": "anthropic", "model": "claude-fable-5-2", "effort": "medium", "price": (4.0, 20.0),
                       "list": (8.0, 40.0), "name": "Claude Fable 5.2, effort medium, Message Batches API"},
    "opus55-high": {"provider": "anthropic", "model": "claude-opus-5-5", "effort": "high", "price": (2.0, 10.0),
                    "list": (4.0, 20.0), "name": "Claude Opus 5.5, effort high, Message Batches API"},
    "sol61-high": {"provider": "openai", "model": "gpt-6.1-sol", "effort": "high", "price": (1.0, 5.0),
                   "list": (2.0, 10.0), "name": "GPT-6.1 Sol, reasoning effort high, Flex tier"},
    "sol61-max": {"provider": "openai", "model": "gpt-6.1-sol", "effort": "max", "price": (1.0, 5.0),
                  "list": (2.0, 10.0), "name": "GPT-6.1 Sol, reasoning effort max, Flex tier"},
}


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    argv, sys.argv = sys.argv, [str(path)]
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.argv = argv
    return mod


SAB = _load("sga_api_batch", W / "sga_api_batch.py")          # API_SENTENCE and API_OUT of the SGA 7 adaptation
R4 = _load("render_sga4_prompt", W / "render_sga4_prompt.py")  # the subagent prompt of each SGA 4 batch

# The tool passages of the SGA 4 subagent prompt and their API counterparts. The strips sentence of the current
# template also says how to read a page with the Read tool ("Work page by page ..."), which the SGA 7 adaptation of
# sga_api_batch.py predates; its method (one page at a time, TeX and strips together) is kept.
STRIPS_TOOL = ("page_NNN_s1.png ... page_NNN_s4.png: the page as four horizontal strips, top to bottom, at the scan's "
               "full resolution (strips overlap slightly). Read each strip once with the Read tool; they are sharp "
               "enough for subscripts, primes and accents. Work page by page, and read a page's page_NNN.tex and its "
               "four strips together, in one message with five Read calls (one model turn instead of five), before you "
               "compare. Make a crop only where one spot is genuinely unreadable; write crops and any helper script "
               "into a folder crops_<your first page>_<your last page> inside the run folder.")
STRIPS_API = ("Four images: the page as four horizontal strips, top to bottom, at the scan's full resolution (strips "
              "overlap slightly). " + SAB.API_SENTENCE + " Work page by page: take a page's TeX and its four strips "
              "together before you compare.")
REPLACE = [
    ("- page_NNN.tex: the LaTeX for that page, cut from", "- Its TeX: the LaTeX for that page, cut from"),
    ("(read only: labels, \\bibitem entries and the neighbouring pages can be looked up there)",
     "(not attached: labels, \\bibitem entries and the neighbouring pages cannot be looked up)"),
    ("the definitions are in the edition's macros.tex, named below, if one must be looked up",
     "the definitions are in the edition's macros.tex, which is not attached"),
    ("If page_NNN.tex lacks text", "If the page's TeX lacks text"),
    ('"<exact substring of page_NNN.tex>"', '"<exact substring of the page\'s TeX>"'),
]
WITNESS = [
    ("- page_NNN_w1.png ... page_NNN_w4.png: the same page in a second scan",
     "- Four more images, attached after the page's four strips: the same page in a second scan"),
    ("read the witness strip before deciding; do not read the witness strips otherwise.",
     "look at the witness strip before deciding; otherwise go by the main strips."),
]
LEFTOVERS = ("page_NNN", "Read tool", "Read call", "crop", "Folder:", "Write JSON", "looked up there", "named below",
             "run folder", ".png", "Do not edit", "Final message")


def api_prompt(a, z):
    """The subagent prompt of batch a-z, adapted for the API (each passage replaced exactly once)."""
    t = (R / ("prompt_%03d_%03d.txt" % (a, z))).read_text(encoding="utf-8")
    assert t == R4.render(a, z), "prompt file differs from render_sga4_prompt.py"
    folder = re.findall(r"^Folder: [^\n]*\n", t, flags=re.M)
    assert len(folder) == 1
    t = t.replace(folder[0], "")
    pairs = [(STRIPS_TOOL, STRIPS_API)] + REPLACE + (WITNESS if "page_NNN_w1.png" in t else [])
    for old, new in pairs:
        assert t.count(old) == 1, "passage not found exactly once in %d-%d: %s" % (a, z, old[:70])
        t = t.replace(old, new)
    macros = re.findall(r"the edition's macros are defined in macros\.tex and numerotation\.tex in [^\n]*?"
                        r"fichiers-configuration-latex\.", t)
    assert len(macros) == 1
    t = t.replace(macros[0], "the edition's macros are defined in its macros.tex and numerotation.tex (not attached).")
    assert t.count("Write JSON to ") == 1
    t = t[:t.index("Write JSON to ")] + SAB.API_OUT + "\n"
    left = [w for w in LEFTOVERS if w in t]
    assert not left, "tool wording left in %d-%d: %s" % (a, z, left)
    return t


def jpeg_b64(p):
    im = Image.open(p).convert("L")
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=90)
    return base64.b64encode(buf.getvalue()).decode()


def user_content(a, z, provider):
    """The user message: the pages in order, each with its TeX, its four strips and (Expose XVII) its witness strips."""
    folder = R / ("b%03d_%03d" % (a, z))

    def text(s):
        return {"type": "text", "text": s} if provider == "anthropic" else {"type": "input_text", "text": s}

    def image(p):
        d = jpeg_b64(p)
        if provider == "anthropic":
            return {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": d}}
        return {"type": "input_image", "detail": "high", "image_url": "data:image/jpeg;base64," + d}

    content = [text("Your pages: %s." % ", ".join(str(n) for n in range(a, z + 1)))]
    for n in range(a, z + 1):
        tex = (folder / ("page_%03d.tex" % n)).read_text(encoding="utf-8")
        content.append(text("Page %d. Its TeX:\n```latex\n%s\n```\nIts scan, four strips, top to bottom:" % (n, tex)))
        content += [image(folder / ("page_%03d_s%d.png" % (n, s))) for s in range(1, 5)]
        wit = [folder / ("page_%03d_w%d.png" % (n, s)) for s in range(1, 5)]
        if all(p.exists() for p in wit):
            content.append(text("The same page in the second scan (the witness), four strips, top to bottom:"))
            content += [image(p) for p in wit]
    content.append(text("Check these pages."))
    return content


# ---------------------------------------------------------------- bookkeeping

def now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def runs():
    if not RUNS.exists():
        return []
    return [json.loads(x) for x in RUNS.read_text(encoding="utf-8").splitlines() if x.strip()]


def log_run(rec):
    OUT.mkdir(parents=True, exist_ok=True)
    with open(RUNS, "a", encoding="utf-8") as f:
        f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def committed():
    """Dollars spent by finished runs plus the worst case of runs still open (submitted, not collected)."""
    rs = runs()
    done = {r["run"]: r for r in rs if r["event"] == "done"}
    total = sum(r["billed_usd"] for r in done.values())
    total += sum(r["worst_case_usd"] for r in rs if r["event"] == "submitted" and r["run"] not in done)
    return total


def save_answer(cfg_name, key, text, extra):
    """Write the answer's findings list, coordinator message and raw text; check each fix's old against the page."""
    d = OUT / cfg_name
    d.mkdir(parents=True, exist_ok=True)
    (d / ("findings_%s_raw.txt" % key)).write_text(text, encoding="utf-8")
    a, z = (int(x) for x in key.split("_"))
    res = {"batch": key, "parsed": False, "findings": None, **extra}
    try:
        obj = json.loads(text[text.index("{"):text.rindex("}") + 1])
        fl = obj.get("findings", [])
        (d / ("findings_%s.json" % key)).write_text(json.dumps(fl, ensure_ascii=False, indent=1), encoding="utf-8")
        (d / ("findings_%s_coordinator.md" % key)).write_text(str(obj.get("coordinator", "")) + "\n", encoding="utf-8")
        tex = {n: (R / ("b%03d_%03d" % (a, z)) / ("page_%03d.tex" % n)).read_text(encoding="utf-8")
               for n in range(a, z + 1)}
        fixes = [f for f in fl if isinstance(f.get("fix"), dict)]
        bad = [f for f in fixes if tex.get(int(f.get("page", 0) or 0), "").count(f["fix"].get("old", "\0")) != 1]
        res.update(parsed=True, findings=len(fl), fixes=len(fixes),
                   misprints=sum(1 for f in fl if f.get("kind") == "misprint_in_print"), fix_old_not_unique=len(bad))
    except Exception as e:  # noqa: BLE001
        res["parse_error"] = str(e)[:200]
    return res


def ledger_row(cfg_name, cfg, rec):
    in_t, out_t = rec["input_tokens"], rec["output_tokens"]
    lp = (in_t * cfg["list"][0] + out_t * cfg["list"][1]) / 1e6
    found = sum(r.get("findings") or 0 for r in rec["requests"])
    fixes = sum(r.get("fixes") or 0 for r in rec["requests"])
    mis = sum(r.get("misprints") or 0 for r in rec["requests"])
    row = {"id": "sga4-apicmp-" + cfg_name, "date": rec["ended"][:10], "project": "SGA 4 scan check: API comparison",
           "work": "SGA 4 spot check, 6 batches of five printed pages (30 pages, run_4), the subagents' prompt adapted "
                   "for the API",
           "method": ("Message Batches API" if cfg["provider"] == "anthropic" else "Responses API, Flex tier, background")
           + ", sga4_api_compare.py",
           "model": cfg["model"] if cfg["provider"] == "anthropic" else "GPT-6.1 Sol (OpenAI)", "effort": cfg["effort"],
           "requests": len(rec["requests"]), "pages": PAGES, "input_tokens": in_t, "output_tokens": out_t,
           "usd_batch_price": round(rec["billed_usd"], 2), "list_price_usd": round(lp, 2),
           "per_page_billed_usd": round(rec["billed_usd"] / PAGES, 4),
           "key": "account B ($200 key, Untitled 1939.md)" if cfg["provider"] == "anthropic"
           else "OpenAI project key (Untitled 1936.md)",
           "basis": "measured: usage of each answer; price %s/%s per million (%s)" % (
               cfg["price"][0], cfg["price"][1], "batch" if cfg["provider"] == "anthropic" else "Flex"),
           "wall_minutes": rec["wall_minutes"],
           "result": "%d findings (%d fixes, %d misprints of the print); scored in "
                     "sga_scan_check_20261105/SGA4_API_COMPARISON_20261110.md" % (found, fixes, mis)}
    if rec.get("batch"):
        row["batch"] = rec["batch"]
    with open(LEDGER, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


# ---------------------------------------------------------------- Anthropic (Message Batches)

def a_api(method, url, body=None):
    h = {"x-api-key": os.environ.get("ANTHROPIC_API_KEY", ""), "anthropic-version": "2023-06-01",
         "content-type": "application/json"}
    data = json.dumps(body).encode("utf-8") if body is not None else None
    try:
        with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=h, method=method), timeout=1800) as r:
            return r.status, r.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", "replace")


def anthropic_run(cfg_name, cfg, budget):
    assert os.environ.get("ANTHROPIC_API_KEY"), "run through run_with_note_key.py"
    reqs, in_tokens = [], 0
    for a, z in BATCHES:
        params = {"model": cfg["model"], "max_tokens": MAX_OUT, "thinking": {"type": "adaptive"},
                  "output_config": {"effort": cfg["effort"]}, "system": api_prompt(a, z),
                  "messages": [{"role": "user", "content": user_content(a, z, "anthropic")}]}
        code, r = a_api("POST", "https://api.anthropic.com/v1/messages/count_tokens",
                        {k: params[k] for k in ("model", "system", "messages", "thinking")})
        if code != 200:
            raise SystemExit("count_tokens %d: %s" % (code, r[:300]))
        in_tokens += json.loads(r)["input_tokens"]
        reqs.append({"custom_id": "b%03d_%03d" % (a, z), "params": params})
    worst = in_tokens * cfg["price"][0] / 1e6 + len(reqs) * MAX_OUT * cfg["price"][1] / 1e6
    spent = committed()
    print("%s: %d requests, input %d tokens (counted), worst case $%.2f; spent so far $%.2f; budget $%.2f"
          % (cfg_name, len(reqs), in_tokens, worst, spent, budget), flush=True)
    if spent + worst > budget:
        raise SystemExit("worst case over the budget: not submitted")
    code, r = a_api("POST", "https://api.anthropic.com/v1/messages/batches", {"requests": reqs})
    if code != 200:
        raise SystemExit("batch submit %d: %s" % (code, r[:500]))
    bt = json.loads(r)
    log_run({"event": "submitted", "run": cfg_name, "provider": "anthropic", "model": cfg["model"],
             "effort": cfg["effort"], "batch": bt["id"], "created": bt.get("created_at"), "submitted": now(),
             "input_tokens_counted": in_tokens, "worst_case_usd": round(worst, 2), "spent_before_usd": round(spent, 2),
             "budget_usd": budget})
    print("batch", bt["id"], flush=True)
    anthropic_collect(cfg_name, cfg, bt["id"])


def anthropic_collect(cfg_name, cfg, bid):
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
    reqs, tin, tout = [], 0, 0
    for line in body.splitlines():
        if not line.strip():
            continue
        x = json.loads(line)
        key = x["custom_id"][1:]
        if x["result"]["type"] != "succeeded":
            reqs.append({"batch": key, "result": x["result"]["type"], "detail": json.dumps(x["result"])[:300]})
            print(key, x["result"]["type"], flush=True)
            continue
        m = x["result"]["message"]
        u = m.get("usage") or {}
        i_t = (u.get("input_tokens") or 0) + (u.get("cache_creation_input_tokens") or 0) + (u.get("cache_read_input_tokens") or 0)
        tin += i_t
        tout += u.get("output_tokens") or 0
        text = "".join(c.get("text", "") for c in m["content"] if c.get("type") == "text")
        res = save_answer(cfg_name, key, text, {"result": "succeeded", "stop_reason": m.get("stop_reason"),
                                                "input_tokens": i_t, "output_tokens": u.get("output_tokens"),
                                                "model": m.get("model")})
        reqs.append(res)
        print(key, m.get("stop_reason"), "findings", res.get("findings"), "out", u.get("output_tokens"), flush=True)
    billed = tin * cfg["price"][0] / 1e6 + tout * cfg["price"][1] / 1e6
    t0 = datetime.fromisoformat(s["created_at"].replace("Z", "+00:00"))
    t1 = datetime.fromisoformat(s["ended_at"].replace("Z", "+00:00"))
    rec = {"event": "done", "run": cfg_name, "provider": "anthropic", "model": cfg["model"], "effort": cfg["effort"],
           "batch": bid, "ended": s["ended_at"], "wall_minutes": round((t1 - t0).total_seconds() / 60, 1),
           "input_tokens": tin, "output_tokens": tout, "billed_usd": round(billed, 4), "requests": sorted(
               reqs, key=lambda r: r["batch"])}
    log_run(rec)
    ledger_row(cfg_name, cfg, rec)
    print("%s: tokens in %d, out %d, $%.2f at batch price, %.1f min" % (cfg_name, tin, tout, billed, rec["wall_minutes"]),
          flush=True)


# ---------------------------------------------------------------- OpenAI (Responses API, Flex tier)

def openai_mod():
    sys.path.insert(0, r"C:\Users\user\Documents\enriques_api_pilot_20261106")
    import enr_pilot  # noqa: E402  (key(): the user's note, read at each call, never printed)
    return enr_pilot


def openai_run(cfg_name, cfg, budget):
    P = openai_mod()
    bodies, est = {}, 0
    for a, z in BATCHES:
        content = user_content(a, z, "openai")
        prompt = api_prompt(a, z)
        est += len(prompt) // 3 + sum(len(c.get("text", "")) // 3 for c in content) + 2500 * sum(
            1 for c in content if c["type"] == "input_image")
        bodies["%03d_%03d" % (a, z)] = {"model": cfg["model"], "instructions": prompt,
                                        "input": [{"role": "user", "content": content}],
                                        "reasoning": {"effort": cfg["effort"]}, "max_output_tokens": MAX_OUT,
                                        "background": True, "service_tier": "flex"}
    worst = est * cfg["price"][0] / 1e6 + len(bodies) * MAX_OUT * cfg["price"][1] / 1e6
    spent = committed()
    print("%s: %d requests, input about %d tokens (estimated, 2,500 per image), worst case $%.2f; spent so far $%.2f; "
          "budget $%.2f" % (cfg_name, len(bodies), est, worst, spent, budget), flush=True)
    if spent + worst > budget:
        raise SystemExit("worst case over the budget: not submitted")
    log_run({"event": "submitted", "run": cfg_name, "provider": "openai", "model": cfg["model"], "effort": cfg["effort"],
             "submitted": now(), "input_tokens_estimated": est, "worst_case_usd": round(worst, 2),
             "spent_before_usd": round(spent, 2), "budget_usd": budget})
    state = {}
    t_start = time.time()
    for key, body in bodies.items():
        state[key] = {"tries": 0}
        _submit_one(P, key, body, state)
    flying = {k for k, v in state.items() if v.get("id")}
    while flying:
        time.sleep(30)
        for key in sorted(flying):
            code, r = P.call("GET", "%s/%s" % (P.API, state[key]["id"]))
            st = r.get("status")
            if st in ("queued", "in_progress") or code >= 500:
                continue
            flying.discard(key)
            state[key]["t1"] = time.time()
            if st == "failed" and state[key]["tries"] < 3:
                print(key, "failed", json.dumps(r.get("error"))[:200], "- resubmitting", flush=True)
                state[key]["failed_" + str(state[key]["tries"])] = r.get("error")
                _submit_one(P, key, bodies[key], state)
                if state[key].get("id"):
                    flying.add(key)
                continue
            state[key]["response"] = r
            print(key, st, "service_tier", r.get("service_tier"), json.dumps(r.get("usage") or {})[:200], flush=True)
    openai_finish(cfg_name, cfg, state, t_start)


def _submit_one(P, key, body, state):
    for attempt in range(8):
        state[key]["tries"] += 1
        code, r = P.call("POST", P.API, body)
        if code < 300 and r.get("id"):
            state[key].update(id=r["id"], t0=time.time())
            print(key, "submitted", r["id"], r.get("status"), flush=True)
            return
        print(key, "submit failed", code, json.dumps(r.get("error"))[:300], flush=True)
        if code == 400:
            raise SystemExit("request rejected: " + json.dumps(r.get("error"))[:300])
        time.sleep(60)
    raise SystemExit("could not submit " + key)


def openai_finish(cfg_name, cfg, state, t_start):
    reqs, tin, tout = [], 0, 0
    for key in sorted(state):
        r = state[key].get("response") or {}
        u = r.get("usage") or {}
        tin += u.get("input_tokens") or 0
        tout += u.get("output_tokens") or 0
        text = "".join(c.get("text", "") for o in r.get("output", []) if o.get("type") == "message"
                       for c in o.get("content", []))
        res = save_answer(cfg_name, key, text, {
            "result": r.get("status"), "incomplete": r.get("incomplete_details"), "service_tier": r.get("service_tier"),
            "input_tokens": u.get("input_tokens"), "output_tokens": u.get("output_tokens"),
            "reasoning_tokens": (u.get("output_tokens_details") or {}).get("reasoning_tokens"),
            "cached_tokens": (u.get("input_tokens_details") or {}).get("cached_tokens"), "response_id": r.get("id"),
            "minutes": round((state[key].get("t1", time.time()) - state[key].get("t0", t_start)) / 60, 1),
            "tries": state[key]["tries"]})
        reqs.append(res)
        (OUT / cfg_name / ("findings_%s_response.json" % key)).write_text(
            json.dumps({k: v for k, v in r.items() if k != "instructions"}, ensure_ascii=False, indent=1)[:2000000],
            encoding="utf-8")
    billed = (tin * cfg["price"][0] + tout * cfg["price"][1]) / 1e6
    rec = {"event": "done", "run": cfg_name, "provider": "openai", "model": cfg["model"], "effort": cfg["effort"],
           "ended": now(), "wall_minutes": round((time.time() - t_start) / 60, 1), "input_tokens": tin,
           "output_tokens": tout, "billed_usd": round(billed, 4), "requests": reqs}
    log_run(rec)
    ledger_row(cfg_name, cfg, rec)
    print("%s: tokens in %d, out %d, $%.2f at the Flex price, %.1f min" % (cfg_name, tin, tout, billed,
                                                                         rec["wall_minutes"]), flush=True)


if __name__ == "__main__":
    args = sys.argv[1:]
    budget = float(args[args.index("--budget") + 1]) if "--budget" in args else 30.0
    if args[0] == "prompts":
        (OUT / "prompts").mkdir(parents=True, exist_ok=True)
        for a, z in BATCHES:
            p = OUT / "prompts" / ("api_prompt_%03d_%03d.txt" % (a, z))
            p.write_text(api_prompt(a, z), encoding="utf-8", newline="\n")
            print(p)
    elif args[0] == "prompt":
        sys.stdout.write(api_prompt(int(args[1]), int(args[2])))
    elif args[0] == "run":
        name = args[1]
        cfg = CONFIGS[name]
        if any(r["run"] == name and r["event"] == "done" for r in runs()):
            raise SystemExit(name + " has already run")
        (anthropic_run if cfg["provider"] == "anthropic" else openai_run)(name, cfg, budget)
    elif args[0] == "collect":
        name = args[1]
        sub = [r for r in runs() if r["run"] == name and r["event"] == "submitted"]
        anthropic_collect(name, CONFIGS[name], sub[-1]["batch"])
