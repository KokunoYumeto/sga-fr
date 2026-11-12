"""Extract the text layer (the scans' own OCR) of every page of the SGA 4 scans, one JSON per scan:
ocr/<name>.json = list of page texts (index 0 = PDF page 1). Used only to place pages (printed page -> PDF page, and
where each printed page begins in the TeX); the models never see it.

usage: python -I ocr_extract.py
"""
import json
import pathlib
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
SCANS = {
    "t1": r"C:\Users\user\Documents\sga4_scans_20261110\rochester_artin-SGA4-1.pdf",
    "t2": r"C:\Users\user\Downloads\artin-SGA4-2.pdf",
    "t3": r"C:\Users\user\Documents\Papors\OS\Théorie des topos et cohomologie étale des schemas  [SGA 4] ( etc.).pdf",
    "w3": r"C:\Users\user\Downloads\Number4.pdf",
}


def pages_of(pdf):
    out = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True, encoding="utf-8", errors="replace").stdout
    return int(next(l.split()[1] for l in out.splitlines() if l.startswith("Pages:")))


(HERE / "ocr").mkdir(exist_ok=True)
for name, pdf in SCANS.items():
    n = pages_of(pdf)
    out = subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", pdf, "-"], capture_output=True).stdout
    texts = out.decode("utf-8", "replace").split("\f")
    if len(texts) == n + 1 and not texts[-1].strip():
        texts = texts[:-1]
    print(name, "pages", n, "texts", len(texts))
    (HERE / "ocr" / f"{name}.json").write_text(json.dumps(texts, ensure_ascii=False), encoding="utf-8")
