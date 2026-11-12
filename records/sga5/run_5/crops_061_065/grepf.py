"""Print earlier findings of this run whose JSON text matches any of the given literal substrings.
usage: python -I grepf.py SUBSTR [SUBSTR ...]"""
import glob, json, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
run = pathlib.Path(__file__).resolve().parent.parent
for f in sorted(glob.glob(str(run / "findings_*.json"))):
    for x in json.load(open(f, encoding="utf-8")):
        s = json.dumps(x, ensure_ascii=False)
        if any(a in s for a in sys.argv[1:]):
            print(pathlib.Path(f).name, s[:900]); print()
