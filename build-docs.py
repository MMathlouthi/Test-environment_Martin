#!/usr/bin/env python3
"""Erzeugt docs/index.html aus der Einzeldatei layla-zahlenheld.html.

Die Einzeldatei ist die Quelle der Wahrheit (offline per AirDrop nutzbar).
Die Web-Fassung unter docs/ ergänzt lediglich:
  - Web-App-Manifest, damit Safari "Zum Home-Bildschirm" anbietet
  - Service Worker, damit die Seite nach dem ersten Laden offline läuft
  - Icons als echte Dateien statt als data-URI
  - noindex, damit die Seite nicht in Suchmaschinen auftaucht

Aufruf: python3 build-docs.py
"""
import re, sys, pathlib

SRC = pathlib.Path("layla-zahlenheld.html")
DST = pathlib.Path("docs/index.html")

html = SRC.read_text(encoding="utf-8")

# 1. Icons: data-URI durch echte Dateien ersetzen (kleinere Seite, zuverlässiger für A2HS)
html, n_icon = re.subn(
    r'<link rel="apple-touch-icon" href="data:image/png;base64,[^"]*">',
    '<link rel="apple-touch-icon" href="./icon-180.png">', html)
html, n_fav = re.subn(
    r'<link rel="icon" href="data:image/png;base64,[^"]*">',
    '<link rel="icon" href="./icon-192.png">', html)

# 2. Manifest, noindex und Hinweis auf die generierte Datei einfügen
head_extra = (
    '<link rel="manifest" href="./manifest.webmanifest">\n'
    '<meta name="robots" content="noindex, nofollow">\n'
    '<!-- Erzeugt aus layla-zahlenheld.html von build-docs.py – nicht direkt bearbeiten. -->\n'
)
marker = "<title>Layla unser Zahlenheld</title>\n"
if marker not in html:
    sys.exit("FEHLER: <title> nicht gefunden – Quelle geändert?")
html = html.replace(marker, marker + head_extra, 1)

# 3. Service Worker registrieren
sw_snippet = """<script>
/* Service Worker: macht das Spiel nach dem ersten Laden offline verfügbar.
   Ohne Service Worker (z. B. bei file://) läuft das Spiel unverändert weiter. */
if ("serviceWorker" in navigator) {
  window.addEventListener("load", function () {
    navigator.serviceWorker.register("./sw.js")["catch"](function () {});
  });
}
</script>
</body>"""
if "</body>" not in html:
    sys.exit("FEHLER: </body> nicht gefunden")
html = html.replace("</body>", sw_snippet, 1)

DST.write_text(html, encoding="utf-8")
print("%s geschrieben (%d Bytes)" % (DST, len(html)))
print("  Icon-Verweise ersetzt: apple-touch-icon=%d, icon=%d" % (n_icon, n_fav))
if n_icon != 1 or n_fav != 1:
    sys.exit("FEHLER: Icon-Verweise nicht wie erwartet ersetzt")
