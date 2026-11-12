"""Prepare the SGA 4 1/2 spot-check batches listed in run_45/BATCHES.json, in the format of prep_sga.py and
prep_sga4.py: for every printed page F of a batch, run_45/bFFF_LLL/page_FFF.tex (one comment line naming the source
file and the line range, then exactly those whole lines of the corpus file, with the source's CRLF line ends written
as LF) and four strips page_FFF_s1..s4.png of the scan at its native resolution (300 dpi), cropped to the ink and cut
into overlapping horizontal strips. The inherited TeX has no page markers: the spans were found by aligning the scan's
text layer with the TeX and checked by eye. The scan holds the Rapport (pp. 76-109) twice; the first copy is used.
The corpus is only read. run_45/PREP_MANIFEST.json records the source files' SHA-256 and the spans.

usage: python -I prep_sga45.py [FIRST ...] [--tex-only]     (no FIRST: all batches)
"""
import hashlib
import json
import pathlib
import subprocess
import sys

from PIL import Image

W = pathlib.Path(__file__).resolve().parent
R = W / "run_45"
spec = json.loads((R / "BATCHES.json").read_text(encoding="utf-8"))
root = pathlib.Path(spec["corpus_root"])
scan = pathlib.Path(spec["scan"]["path"])
args = [a for a in sys.argv[1:] if not a.startswith("--")]
tex_only = "--tex-only" in sys.argv
want = {int(a) for a in args}


def idx_of(folio):
    return folio + 4 if folio <= 109 else folio + 38


def strips(pdf, idx, dpi, out, prefix):
    """Render PDF page idx (0-based) in grey at dpi, crop to the ink, write four overlapping strips."""
    full = out / f"{prefix}_full"
    subprocess.run(["pdftoppm", "-png", "-gray", "-r", str(dpi), "-f", str(idx + 1), "-l", str(idx + 1),
                    "-singlefile", str(pdf), str(full)], check=True)
    im = Image.open(str(full) + ".png").convert("L")
    w, h = im.size
    ink = im.point(lambda x: 255 if x < 150 else 0)
    box = ink.getbbox() or (0, 0, w, h)
    left, right = max(0, box[0] - 20), min(w, box[2] + 20)
    top, bottom = max(0, box[1] - 20), min(h, box[3] + 20)
    step = (bottom - top) / 4
    for i in range(4):
        y0 = int(top + i * step) - (40 if i else 0)
        y1 = int(top + (i + 1) * step) + (40 if i < 3 else 0)
        im.crop((left, max(top, y0), right, min(bottom, y1))).save(out / f"{prefix}{i + 1}.png", optimize=True)
    im.close()
    pathlib.Path(str(full) + ".png").unlink()


def header(b, p):
    a, z = p["lines"]
    notes = []
    if p.get("first_prev_end"):
        notes.append(f"its first line starts with the end of p. {p['folio'] - 1}, through \"{p['first_prev_end']}\"")
    if p.get("last_end"):
        notes.append(f"its last line holds this page through \"{p['last_end']}\", then the start of p. {p['folio'] + 1}")
    extra = ("; " + "; ".join(notes)) if notes else ""
    return (f"% from {b['tex']}, lines {a}-{z} (SGA 4½, LNM 569, printed page {p['folio']} = running head "
            f"{p['ts']}{extra})\n")


manifest = {"edition": spec["edition"], "scan": spec["scan"], "sources": {}, "batches": []}
for b in spec["batches"]:
    if want and b["first"] not in want:
        continue
    out = R / f"b{b['first']:03d}_{b['last']:03d}"
    out.mkdir(parents=True, exist_ok=True)
    raw = (root / b["tex"]).read_bytes()
    lines = raw.split(b"\n")
    manifest["sources"][b["tex"]] = {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest().upper(),
                                     "line_ends": "CRLF" if b"\r\n" in raw else "LF"}
    rec = {"batch": out.name, "part": b["part"], "tex": b["tex"], "pages": []}
    for p in b["pages"]:
        f = p["folio"]
        a, z = p["lines"]
        assert 1 <= a <= z <= len(lines), (f, a, z)
        span = lines[a - 1:z]
        assert all(x.endswith(b"\r") for x in span), "expected CRLF lines in %s %d-%d" % (b["tex"], a, z)
        body = b"\n".join(x[:-1] for x in span).decode("utf-8") + "\n"
        (out / f"page_{f:03d}.tex").write_text(header(b, p) + body, encoding="utf-8", newline="")
        idx = idx_of(f)
        rec["pages"].append({"folio": f, "running_head": p["ts"], "lines": [a, z],
                             "span_sha256_crlf": hashlib.sha256(b"\n".join(span) + b"\n").hexdigest().upper(),
                             "first_prev_end": p.get("first_prev_end"), "last_end": p.get("last_end"),
                             "scan_pdf_page": idx + 1})
        if not tex_only:
            strips(scan, idx, spec["scan"]["dpi"], out, f"page_{f:03d}_s")
    manifest["batches"].append(rec)
    print("prepared", out.name, [p["folio"] for p in b["pages"]])
mp = R / "PREP_MANIFEST.json"
old = json.loads(mp.read_text(encoding="utf-8")) if mp.exists() else {"sources": {}, "batches": []}
old.update({"edition": manifest["edition"], "scan": manifest["scan"]})
old["sources"].update(manifest["sources"])
names = {r["batch"] for r in manifest["batches"]}
old["batches"] = sorted([r for r in old["batches"] if r["batch"] not in names] + manifest["batches"],
                        key=lambda r: int(r["batch"][1:4]))
mp.write_text(json.dumps(old, ensure_ascii=False, indent=1), encoding="utf-8")
