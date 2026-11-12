"""Crop several boxes (in displayed 2000-px-wide coordinates of the strip) and scale them; usage:
python -I mcrop.py STRIP out1:x0,y0,x1,y1[:scale] out2:... ; boxes are in the displayed coordinates (factor W/2000)."""
import sys
from PIL import Image
src = sys.argv[1]
im = Image.open(src)
k = im.width / 2000.0
for spec in sys.argv[2:]:
    parts = spec.split(":")
    out, box = parts[0], [float(v) for v in parts[1].split(",")]
    scale = float(parts[2]) if len(parts) > 2 else 2.0
    b = tuple(int(round(v * k)) for v in box)
    c = im.crop(b)
    c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
    c.save(out)
    print(out, b, c.size)
