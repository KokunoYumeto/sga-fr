from PIL import Image
import numpy as np
src = r'C:/Users/user/Documents/sga_scan_check_20261105/run_7I/b266_270/page_270_s2.png'
out = r'C:/Users/user/Documents/sga_scan_check_20261105/run_7I/crops_266_270/'
im = np.array(Image.open(src).convert('L')).astype(float)
y0, y1 = 778, 810
def g(x0, x1, pad=3):
    a = im[y0:y1, x0-pad:x1+pad]
    lo, hi = np.percentile(a, 1), np.percentile(a, 99)
    a = (a - lo) / (hi - lo) * 255
    return a.clip(0, 255)
parts = [g(1077,1095), g(1032,1048), g(1662,1681)]
# synthetic overlay: min of s and e (darker wins)
s = im[y0:y1, 1032-3:1048+3+2]
e = im[y0:y1, 1662-3:1681+3]
w = min(s.shape[1], e.shape[1])
ov = np.minimum(s[:, :w], e[:, :w])
lo, hi = np.percentile(ov, 1), np.percentile(ov, 99)
ov = ((ov - lo) / (hi - lo) * 255).clip(0, 255)
parts.append(ov)
H = y1 - y0
W = sum(p.shape[1] for p in parts) + 8 * len(parts)
m = np.full((H, W), 255.0); x = 0
for p in parts:
    m[:, x:x+p.shape[1]] = p; x += p.shape[1] + 8
Image.fromarray(m.astype('uint8')).resize((W*12, H*12), Image.LANCZOS).save(out + 'p270_glyph_overlay.png')
