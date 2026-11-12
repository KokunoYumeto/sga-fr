"""Keep the 20 exposé files of both layers of the SGA 4 working copy, as copied from the corpus (hashes checked against
../sga4/SOURCE.json), in pristine/{diplomatic,current}/<NN>/<NN>.tex. merge_pass.py places the models' findings in
these pristine texts (the TeX the models saw), and apply_pass.py builds the working copy from them, so that the agreed
fixes can be applied again from scratch when more answers come in (no fix applied twice, positions always valid).

usage: python -I snapshot_pristine.py      (refuses to overwrite an existing snapshot)
"""
import hashlib
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
W = HERE.parent
FILES = ["01", "02", "03", "04", "05", "05bis", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
         "18", "19"]
src = json.loads((W / "sga4" / "SOURCE.json").read_text(encoding="utf-8"))
out = HERE / "pristine"
if out.exists():
    raise SystemExit("pristine/ exists already")
todo = []
for layer in ("diplomatic", "current"):
    for fn in FILES:
        rel = f"{fn}/{fn}.tex"
        data = (W / "sga4" / layer / fn / f"{fn}.tex").read_bytes()
        want = src[layer][rel]["sha256"]
        got = hashlib.sha256(data).hexdigest().upper()
        if got != want:
            raise SystemExit(f"{layer}/{rel}: the working copy no longer equals the corpus copy ({got[:12]} != "
                             f"{want[:12]}): not a pristine text")
        todo.append((out / layer / fn / f"{fn}.tex", data))
for p, data in todo:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data)
print(f"pristine snapshot: {len(todo)} files, hashes equal to ../sga4/SOURCE.json")
sys.exit(0)
