"""Rough word diff between the OCR of a page and its TeX (text words only), to catch missing or extra words."""
import difflib
import re
import sys

base = r"C:\Users\user\Documents\sga_scan_check_20261105"
for p in sys.argv[1:]:
    ocr = open(rf"{base}\ocr_6\page_{p}.txt", encoding="utf-8").read()
    tex = open(rf"{base}\run_6\b231_235\page_{p}.tex", encoding="utf-8").read()
    tex = "\n".join(l for l in tex.splitlines() if not l.startswith("%"))
    tex = re.sub(r"\\\(.*?\\\)", " ", tex, flags=re.S)
    tex = re.sub(r"\\\[.*?\\\]", " ", tex, flags=re.S)
    tex = re.sub(r"\\[A-Za-z]+\*?", " ", tex)
    tex = re.sub(r"[{}\[\]]", " ", tex)

    def words(s):
        return [w.lower() for w in re.findall(r"[A-Za-zÀ-ÿ']{3,}", s)]

    a, b = words(ocr), words(tex)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    print("== page", p)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            print(op, "OCR:", " ".join(a[i1:i2])[:150], "| TEX:", " ".join(b[j1:j2])[:150])
