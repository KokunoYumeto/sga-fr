"""Render scan index 495 (printed page 484) of SGA5.pdf at 300 dpi and cut it into four overlapping strips."""
import sys
import pathlib
import pypdfium2 as pdfium

pdf_path = pathlib.Path(sys.argv[1])
out_dir = pathlib.Path(sys.argv[2])
idx = int(sys.argv[3])
folio = int(sys.argv[4])

pdf = pdfium.PdfDocument(str(pdf_path))
print("pages in pdf:", len(pdf))
page = pdf[idx]
w_pt, h_pt = page.get_size()
print("page size (pt):", w_pt, h_pt)
img = page.render(scale=300 / 72).to_pil().convert("L")
print("rendered:", img.size)
img.save(out_dir / f"page_{folio:03d}_full.png")
W, H = img.size
n = 4
overlap = 60
step = H / n
for k in range(n):
    top = max(0, int(k * step) - overlap)
    bot = min(H, int((k + 1) * step) + overlap)
    img.crop((0, top, W, bot)).save(out_dir / f"page_{folio:03d}_s{k + 1}.png")
    print("strip", k + 1, top, bot)
