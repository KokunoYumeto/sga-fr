"""Prepare the SGA 4 spot-check batches listed in run_4/BATCHES.json, in the format of prep_sga.py: for every printed
page F of a batch, run_4/bFFF_LLL/page_FFF.tex (the TeX of that page: one comment line naming the source file and the
line range, then exactly those whole lines of the corpus file) and four strips page_FFF_s1..s4.png of the scan at its
native resolution (300 dpi), cropped to the ink and cut into overlapping horizontal strips. Where the volume has a
second witness for the page (Number4.pdf for Tome 3, pp. 250-587), its strips are written as page_FFF_w1..w4.png.
The corpus is only read. A small manifest (run_4/PREP_MANIFEST.json) records the source files' SHA-256 and the spans.

usage: python -I prep_sga4.py [FIRST ...] [--tex-only]     (no FIRST: all batches)
"""
import hashlib
import json
import pathlib
import subprocess
import sys

from PIL import Image

W = pathlib.Path(__file__).resolve().parent
R = W / "run_4"
spec = json.loads((R / "BATCHES.json").read_text(encoding="utf-8"))
root = pathlib.Path(spec["corpus_root"])
args = [a for a in sys.argv[1:] if not a.startswith("--")]
tex_only = "--tex-only" in sys.argv
want = {int(a) for a in args}


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


def header(b, p, vol):
    a, z = p["lines"]
    notes = []
    if p.get("first_shared"):
        notes.append(f"its first line also holds the last words of p. {p['folio'] - 1}, which end before the word "
                     f"just before the page marker")
    if p.get("last_shared"):
        notes.append(f"its last line also holds the first words of p. {p['folio'] + 1}, from the word just before "
                     f"the page marker on")
    extra = ("; " + "; ".join(notes)) if notes else ""
    return (f"% from {b['tex']}, lines {a}-{z} (SGA 4 Tome {b['tome']}, LNM {vol['lnm']}, printed page {p['folio']}"
            f" = typescript page {p['ts']}{extra})\n")


manifest = {"sources": {}, "batches": []}
for b in spec["batches"]:
    if want and b["first"] not in want:
        continue
    vol = spec["volumes"][b["tome"]]
    out = R / f"b{b['first']:03d}_{b['last']:03d}"
    out.mkdir(parents=True, exist_ok=True)
    src = root / b["tex"]
    raw = src.read_bytes()
    assert b"\r" not in raw, "expected LF line endings"
    manifest["sources"][b["tex"]] = {"bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest().upper()}
    lines = raw.decode("utf-8").split("\n")
    rec = {"batch": out.name, "tome": b["tome"], "lnm": vol["lnm"], "expose": b["expose"], "tex": b["tex"],
           "scan": vol["scan"], "dpi": vol["dpi"], "pages": []}
    for p in b["pages"]:
        f = p["folio"]
        a, z = p["lines"]
        assert 1 <= a <= z <= len(lines), (f, a, z)
        body = "\n".join(lines[a - 1:z]) + "\n"
        (out / f"page_{f:03d}.tex").write_text(header(b, p, vol) + body, encoding="utf-8", newline="")
        idx = f + b["idx_minus_folio"]
        prec = {"folio": f, "typescript": p["ts"], "lines": [a, z], "first_shared": bool(p.get("first_shared")),
                "last_shared": bool(p.get("last_shared")), "scan_pdf_page": idx + 1}
        wit = vol.get("witness")
        has_wit = bool(wit) and vol["witness_covers"][0] <= f <= vol["witness_covers"][1]
        if has_wit:
            widx = f + vol["witness_idx_minus_folio"]
            prec["witness"] = wit
            prec["witness_pdf_page"] = widx + 1
        if not tex_only:
            strips(vol["scan"], idx, vol["dpi"], out, f"page_{f:03d}_s")
            if has_wit:
                strips(wit, widx, 300, out, f"page_{f:03d}_w")
        rec["pages"].append(prec)
    manifest["batches"].append(rec)
    print("prepared", out.name, [p["folio"] for p in b["pages"]])
mp = R / "PREP_MANIFEST.json"
old = json.loads(mp.read_text(encoding="utf-8")) if mp.exists() else {"sources": {}, "batches": []}
old["sources"].update(manifest["sources"])
names = {r["batch"] for r in manifest["batches"]}
old["batches"] = [r for r in old["batches"] if r["batch"] not in names] + manifest["batches"]
old["batches"].sort(key=lambda r: (r["tome"], int(r["batch"][1:4])))
mp.write_text(json.dumps(old, ensure_ascii=False, indent=1), encoding="utf-8")
