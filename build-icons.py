#!/usr/bin/env python3
"""Erzeugt die App-Icons für Layla unser Zahlenheld ohne externe Bibliotheken.

Gezeichnet wird ein goldener Fedora auf dunkler Bühne mit drei Funkeln.
Aufruf: python3 build-icons.py
"""
import zlib, struct, math, base64, os

GOLD, GOLD_D, WHITE = (247, 208, 70), (176, 128, 30), (255, 255, 255)

def blend(a, b, t):
    t = max(0.0, min(1.0, t))
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

def render(size, art=1.0):
    """art < 1 verkleinert das Motiv (für maskierbare Icons mit Rand)."""
    px = bytearray()
    u = size / 180.0                      # Einheit des 180er-Entwurfs
    cx, cy = size / 2.0, size / 2.0

    def to_art(x, y):
        """Bildpunkt in Entwurfskoordinaten umrechnen."""
        return ((x - cx) / (u * art) + 90.0, (y - cy) / (u * art) + 90.0)

    def crown(x, y):
        if not (52 <= y <= 106): return False
        t = (y - 52) / 54.0
        half = 27 + 7 * t
        dx = abs(x - 90)
        if dx > half: return False
        if y < 62:                        # obere Ecken abrunden
            r = 10.0
            k = half - r
            if dx > k: return (dx - k) ** 2 + (62 - y - r) ** 2 <= r * r
        return True

    def brim(x, y):
        dx, dy = (x - 90) / 78.0, (y - 110) / 18.0
        return dx * dx + dy * dy <= 1.0

    def band(x, y):
        return 90 <= y <= 103 and crown(x, y)

    def sparkle(x, y, sx, sy, r):
        dx, dy = abs(x - sx), abs(y - sy)
        return (dx * dx / (r * r) + dy * dy / (r * r * 0.06) <= 1) or \
               (dy * dy / (r * r) + dx * dx / (r * r * 0.06) <= 1)

    for iy in range(size):
        px.append(0)                      # Filter-Byte je Zeile
        for ix in range(size):
            # Bühnenhintergrund immer randlos, damit Masken nicht schneiden
            d = math.hypot((ix - size / 2.0) / (size * 0.61), (iy - size * 0.17) / (size * 0.83))
            c = blend((38, 33, 44), (8, 8, 12), d)
            x, y = to_art(ix, iy)
            if brim(x, y) and not crown(x, y):
                c = blend(GOLD, GOLD_D, (y - 94) / 32.0 if y > 94 else 0)
            elif band(x, y):
                c = (26, 24, 30)
            elif crown(x, y):
                c = blend(GOLD, GOLD_D, (y - 52) / 54.0)
            else:
                for (sx, sy, sr) in ((36, 60, 13), (146, 92, 10), (124, 40, 8)):
                    if sparkle(x, y, sx, sy, sr):
                        c = WHITE
                        break
            px += bytes(c)

    def chunk(tag, data):
        return (struct.pack(">I", len(data)) + tag + data +
                struct.pack(">I", zlib.crc32(tag + data) & 0xffffffff))

    return (b"\x89PNG\r\n\x1a\n" +
            chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 2, 0, 0, 0)) +
            chunk(b"IDAT", zlib.compress(bytes(px), 9)) +
            chunk(b"IEND", b""))

TARGETS = [
    ("docs/icon-180.png", 180, 1.0),      # apple-touch-icon
    ("docs/icon-192.png", 192, 1.0),
    ("docs/icon-512.png", 512, 1.0),
    ("docs/icon-maskable-512.png", 512, 0.62),  # Rand für runde/eckige Masken
]

if __name__ == "__main__":
    for path, size, art in TARGETS:
        data = render(size, art)
        with open(path, "wb") as f:
            f.write(data)
        print("%-32s %4dx%-4d %6d Bytes" % (path, size, size, len(data)))
    # Das Einzeldatei-Spiel trägt sein Icon als data-URI in sich.
    with open("icon-inline.b64", "w") as f:
        f.write(base64.b64encode(render(180, 1.0)).decode())
    print("icon-inline.b64 für die Einzeldatei geschrieben")
