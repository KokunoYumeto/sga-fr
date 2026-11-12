"""Raw OCR (no dictionary) of the strips of pages 21-25, and a word comparison with the TeX.

usage: python -I ocr_diff.py BATCH_DIR OUT_DIR
Writes OUT_DIR/ocr_NNN.txt and prints, per page, the OCR words of 4+ letters that are one or two letters away from
a TeX word of the same length but not equal to any TeX word (hints only: OCR noise is expected).
"""
import pathlib
import re
import subprocess
import sys
import unicodedata

sys.stdout.reconfigure(encoding="utf-8")
TESS = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
batch = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])


def plain(s):
    s = unicodedata.normalize("NFD", s)
    return "".join(ch for ch in s if unicodedata.category(ch) != "Mn").lower()


def tex_words(t):
    t = re.sub(r"%[^\n]*", " ", t)
    t = re.sub(r"\$[^$]*\$", " ", t)
    t = re.sub(r"\\begin\{equation\}.*?\\end\{equation\}", " ", t, flags=re.S)
    t = re.sub(r"\\\[.*?\\\]", " ", t, flags=re.S)
    t = re.sub(r"\\[a-zA-Z]+\*?", " ", t)
    return set(plain(w) for w in re.findall(r"[A-Za-zÀ-ÿ]+", t))


for n in range(21, 26):
    texw = tex_words((batch / f"page_{n:03d}.tex").read_text(encoding="utf-8"))
    words = []
    lines = []
    for s in range(1, 5):
        png = batch / f"page_{n:03d}_s{s}.png"
        r = subprocess.run([TESS, str(png), "stdout", "--psm", "6", "-c", "load_system_dawg=0",
                            "-c", "load_freq_dawg=0"], capture_output=True, text=True, encoding="utf-8")
        lines.append(r.stdout)
        words += re.findall(r"[A-Za-zÀ-ÿ]+", r.stdout)
    (out / f"ocr_{n:03d}.txt").write_text("\n".join(lines), encoding="utf-8")
    print(f"== page {n}")
    seen = set()
    for w in words:
        p = plain(w)
        if len(p) < 4 or p in texw or p in seen:
            continue
        seen.add(p)
        near = [t for t in texw if len(t) == len(p) and sum(a != b for a, b in zip(t, p)) <= 2]
        if near:
            print(f"  {w!r:22} ~ {near}")
