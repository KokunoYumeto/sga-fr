"""Compile every exposé of an SGA 4 layer standalone with LuaLaTeX (as Codex's smoke tests did), writing nothing into
the layer: the output goes to OUTDIR/<label>/<NN>/. Records per exposé the exit code, the page count and the number of
'!' error lines in COMPILE_<label>.json in this folder, so that the state before and after the fixes can be compared.

usage: python -I compile_check.py LAYER_DIR LABEL OUTDIR [--jobs N] [--only 01,05]
"""
import json
import pathlib
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
layer, label, outdir = pathlib.Path(sys.argv[1]), sys.argv[2], pathlib.Path(sys.argv[3])
jobs = int(sys.argv[sys.argv.index("--jobs") + 1]) if "--jobs" in sys.argv else 4
only = sys.argv[sys.argv.index("--only") + 1].split(",") if "--only" in sys.argv else None
FILES = ["01", "02", "03", "04", "05", "05bis", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
         "18", "19"]


def one(fn):
    od = outdir / label / fn
    od.mkdir(parents=True, exist_ok=True)
    res = {"file": fn}
    for run in (1, 2):  # two runs, so that references settle
        try:
            p = subprocess.run(["lualatex", "-interaction=nonstopmode", f"-output-directory={od}", f"{fn}.tex"],
                               cwd=layer / fn, capture_output=True, timeout=1800)
            res["exit"] = p.returncode
        except subprocess.TimeoutExpired:
            res["exit"] = "timeout"
            break
    log = (od / f"{fn}.log").read_text(encoding="utf-8", errors="replace") if (od / f"{fn}.log").exists() else ""
    m = re.search(r"Output written on .*?\((\d+) pages?", log.replace("\n", ""))
    res["pages"] = int(m.group(1)) if m else None
    res["errors"] = len(re.findall(r"^! ", log, flags=re.M))
    res["first_errors"] = re.findall(r"^! .*", log, flags=re.M)[:5]
    res["undefined_refs"] = len(re.findall(r"Reference `[^']*' on page \d+ undefined", log))
    return res


if __name__ == "__main__":
    todo = [f for f in FILES if not only or f in only]
    with ThreadPoolExecutor(jobs) as ex:
        out = list(ex.map(one, todo))
    path = HERE / f"COMPILE_{label}.json"
    prev = json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
    keep = [r for r in prev if r["file"] not in todo]
    path.write_text(json.dumps(sorted(keep + out, key=lambda r: FILES.index(r["file"])), ensure_ascii=False, indent=1),
                    encoding="utf-8")
    for r in out:
        print(r["file"], "exit", r["exit"], "pages", r["pages"], "errors", r["errors"], "undef refs",
              r["undefined_refs"])
