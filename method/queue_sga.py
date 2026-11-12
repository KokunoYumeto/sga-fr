"""Queue of the SGA scan-check batches (five printed pages each).

usage: python -I queue_sga.py init                 build QUEUE.json (all volumes; existing states are kept)
       python -I queue_sga.py next N [VOL]          take the next N waiting batches: prepare them (prep_sga.py) and
                                                    print one line per batch (vol first last folder outfile)
       python -I queue_sga.py done VOL FIRST LAST   mark a batch as checked and applied
       python -I queue_sga.py status
"""
import json
import pathlib
import subprocess
import sys

W = pathlib.Path(r"C:\Users\user\Documents\sga_scan_check_20261105")
Q = W / "QUEUE.json"
RANGES = {"7I": (1, 528), "7II": (1, 438), "5": (1, 484), "6": (1, 700)}
ORDER = ["7I", "7II", "6", "5"]


def load():
    return json.loads(Q.read_text(encoding="utf-8")) if Q.exists() else []


def save(q):
    Q.write_text(json.dumps(q, indent=1), encoding="utf-8")


cmd = sys.argv[1]
q = load()
if cmd == "init":
    have = {(b["vol"], b["first"]) for b in q}
    for vol in ORDER:
        a, z = RANGES[vol]
        for first in range(a, z + 1, 5):
            if (vol, first) not in have:
                q.append(dict(vol=vol, first=first, last=min(first + 4, z), state="waiting"))
    save(q)
    print(len(q), "batches")
elif cmd == "next":
    n = int(sys.argv[2])
    vol = sys.argv[3] if len(sys.argv) > 3 else None
    taken = 0
    for b in q:
        if taken >= n:
            break
        if b["state"] != "waiting" or (vol and b["vol"] != vol):
            continue
        folder = W / f"run_{b['vol']}" / f"b{b['first']:03d}_{b['last']:03d}"
        out = W / f"run_{b['vol']}" / f"findings_{b['first']:03d}_{b['last']:03d}.json"
        r = subprocess.run([sys.executable, "-I", str(W / "prep_sga.py"), b["vol"], str(b["first"]), str(b["last"]),
                            str(folder)], capture_output=True, text=True)
        b["state"] = "started"
        save(q)
        taken += 1
        print(b["vol"], b["first"], b["last"], folder, out, "|", r.stdout.strip() or r.stderr.strip()[-200:])
elif cmd == "done":
    vol, first, last = sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    for b in q:
        if b["vol"] == vol and b["first"] == first and b["last"] == last:
            b["state"] = "done"
    save(q)
elif cmd == "status":
    from collections import Counter
    c = Counter((b["vol"], b["state"]) for b in q)
    for vol in ORDER:
        print(vol, {s: c[(vol, s)] for s in ("waiting", "started", "done") if c[(vol, s)]})
