# 🎩 Layla unser Zahlenheld

Ein deutschsprachiges Lernspiel für den Übergang von der **1. in die 2. Klasse**.
Neun kurze Bühnen-Nummern wechseln sich ab und trainieren Rechnen, Farben, Formen,
Muster, Konzentration und Merkfähigkeit – als Zeit-Challenge mit Punkten, Rängen,
Bestenliste und echten Preisen: **Fernsehminuten und Süßigkeiten-Stücke**.

Optik und Musik sind eine Hommage an die Popbühne der 80er: schwarze Bühne,
goldener Fedora, Scheinwerfer, Leuchtboden und ein Funk-Groove mit 117 bpm.

Das ganze Spiel steckt in **einer einzigen Datei**: `layla-zahlenheld.html` (ca. 82 KB).
Kein Server, kein Internet, keine Installation, keine Werbung, kein Tracking.

---

## Zwei Wege aufs iPhone

Es gibt das Spiel in zwei Fassungen. Beide laufen offline, aber nur eine bekommt ein
Icon auf dem Home-Bildschirm.

| | **Web-App** (`docs/`) | **Einzeldatei** (`layla-zahlenheld.html`) |
|---|---|---|
| Icon auf dem Home-Bildschirm | ✅ ja | ❌ nein |
| Vollbild ohne Safari-Leisten | ✅ ja | ❌ nein |
| Offline spielbar | ✅ nach dem ersten Laden | ✅ sofort |
| Braucht Internet | einmalig zum Installieren | nie |
| Weitergabe | Link öffnen | AirDrop |

> **Warum kein Icon bei der Einzeldatei?** Safari bietet **„Zum Home-Bildschirm" nur für
> Web-Adressen** an (`http`/`https`), nicht für lokale Dateien (`file://`) – genau wie bei
> `data:`-Adressen. Das ist eine Einschränkung von iOS, kein Fehler des Spiels.

### A) Web-App mit Icon (empfohlen)

Einmalige Einrichtung auf GitHub:

1. Repo-Einstellungen → **Settings → General → Danger Zone → Change visibility → Public**.
2. **Settings → Pages** → *Source:* `Deploy from a branch`,
   *Branch:* `claude/educational-game-kids-x0xyc3`, *Folder:* `/docs` → **Save**.
3. Nach ein bis zwei Minuten ist das Spiel erreichbar unter
   **https://mmathlouthi.github.io/Test-environment_Martin/**

Danach auf jedem iPhone: Adresse in **Safari** öffnen → **Teilen → Zum Home-Bildschirm**.
Ab dann startet das Spiel im Vollbild mit Fedora-Icon und läuft **auch im Flugmodus**,
weil ein Service Worker alles auf dem Gerät behält.

Zum Weitergeben an ein anderes iPhone genügt der Link – kein AirDrop, keine Datei.

### B) Einzeldatei ganz ohne Internet

1. `layla-zahlenheld.html` per **AirDrop**, iCloud Drive oder E-Mail aufs iPhone bringen.
2. In der App **Dateien** antippen. Erscheint nur eine Vorschau: oben rechts
   **In Safari öffnen** wählen.
3. Tipp: In der Dateien-App lange auf die Datei tippen → **Favorit**, dann ist sie
   in zwei Tipps erreichbar.

Diese Fassung lädt **nichts** aus dem Netz – Formen sind SVG, das Icon ein eingebettetes
PNG, die Töne werden im Browser synthetisiert. Geprüft mit blockiertem Netzwerk:
**null externe Anfragen**.

> **Wichtig:** Punkte, Preise und Bestenlisten liegen immer nur auf dem jeweiligen Gerät –
> und getrennt je Fassung. Beim Wechsel oder Übertragen wandert das Preis-Konto **nicht**
> mit; dort wird bei Null gestartet.

### Datenschutz-Hinweis zur Web-App

Mit `Public` ist der Inhalt des Repos – und damit auch der Name im Spiel – **öffentlich
im Internet lesbar**. Zwei Dinge dämpfen das: `docs/robots.txt` und ein
`noindex`-Hinweis in der Seite halten Suchmaschinen ab, sodass die Seite nicht über eine
Namenssuche auffindbar ist. Wer das Test-Repo privat halten will, kann `docs/` alternativ
in ein eigenes, öffentliches Repo legen und nur dort Pages aktivieren.

### Geprüfte Geräte
| Gerät | Status |
|---|---|
| iPhone 14 / 14 Pro Max (iOS 16+) | ✅ getestet, kein Scrollen, kein Überlauf |
| iPhone 17 | ✅ getestet |
| iPhone SE (kleines Display) | ✅ getestet |
| Querformat | ✅ getestet |
| Safari auf dem Mac | ✅ getestet (1024×640 und 1280×800) |

Es werden bewusst nur Web-Funktionen genutzt, die iOS 16 sicher beherrscht –
kein `:has()`, keine optionalen Verkettungen, `100dvh` mit `100vh`-Rückfall,
`webkitAudioContext` als Rückfall für Web Audio.

---

## Die neun Bühnen-Nummern

| Nummer | Was geübt wird |
|---|---|
| **Rechen-Blitz** | Plus und Minus bis 100, mit Zehnerübergang |
| **Lücken-Jäger** | Lücken- und Umkehraufgaben (`7 + ? = 15`, `52 − ? = 20`) |
| **Mal-Monster** | Erstes Einmaleins (1er, 2er, 5er, 10er) mit Bildern zum Bündeln, ab Stufe 4 auch `? × 5 = 30` |
| **Zahlen-Reihe** | Reihen in 1er-, 2er-, 3er-, 5er- und 10er-Schritten, vorwärts und rückwärts |
| **Größer-Kleiner** | `<`, `=`, `>` vergleichen – ab Stufe 3 auch Rechenterme gegeneinander |
| **Farb-Falle** | Konzentration und Impulskontrolle: Schriftfarbe gegen Wortbedeutung |
| **Formen-Finder** | Formen und Farben unterscheiden und zählen |
| **Muster-Meister** | Muster erkennen und fortsetzen |
| **Merk-Blitz** | Kurzzeitgedächtnis: Dinge einprägen und wiedererkennen |

## Zwei Modi

- **⚡️ Blitz · 90 s** – Zeit-Challenge. Richtig = Punkte **+2 Sekunden**, falsch = **−2 Sekunden**.
  Punkte steigen mit der Stufe, eine Serie (🔥) gibt Bonuspunkte.
- **🌙 Ruhig · 20 Aufgaben** – ohne Uhr, ohne Druck. Zum Üben und für den Abend.

Jeder Modus hat seine eigene Bestenliste (Top 5).

## Preise: Fernsehminuten und Süßigkeiten

Nach jeder Runde gibt es einen **Preis-Gutschein**. Er wächst in zwei Richtungen:
mit den Punkten (Rang) und mit der Platzierung in der Bestenliste.

| Rang | ab Punkten | Grundpreis |
|---|---|---|
| 🎤 Bühnen-Debüt | 0 | 📺 5 min · 🍬 1 |
| 🪩 Tanzfläche | 150 | 📺 10 min · 🍬 2 |
| 🧦 Goldene Socken | 300 | 📺 15 min · 🍬 3 |
| ✨ Glitzer-Handschuh | 450 | 📺 20 min · 🍬 4 |
| 🌙 Moonwalkerin | 600 | 📺 25 min · 🍬 5 |
| 🌟 Superstar | 800 | 📺 30 min · 🍬 6 |

**Platz-Bonus** in der eigenen Bestenliste: Platz 1 → +5 min / +2 Stück,
Platz 2 → +3 / +1, Platz 3 → +2 / +1, Platz 4 und 5 → +1 / +0.

Höchstmöglich pro Runde: **📺 35 Minuten und 🍬 8 Stück** – das setzt eine sehr starke
Runde auf Platz 1 voraus. Das **Preis-Konto** auf der Startseite sammelt alles, bis
Erwachsene unter *Für Erwachsene* auf **„Preise eingelöst"** tippen (zweimal, gegen
versehentliches Löschen). Die Gesamtsumme aller je verdienten Preise bleibt sichtbar.

## Klang

Alles wird zur Laufzeit synthetisiert – **kein fremdes Tonmaterial, keine Aufnahmen,
keine Stimmen-Imitation**:

- durchlaufender Funk-Groove: Bassdrum, Snare, Hi-Hat und eine Bassfigur in
  F♯-Moll-Pentatonik bei 117 bpm
- richtig: Funk-Akkord plus Fingerschnippen · falsch: kurzer Abwärts-Sweep
- Stufenaufstieg: Orchester-Schlag · Rundenende: kleine Fanfare
- die Musik senkt sich automatisch, während die Aufgabe vorgelesen wird

Drei getrennte Schalter: **🎵 Musik**, **🥁 Effekte**, **🗣️ Vorlesen**.

> Hinweis: Der Look ist eine eigenständige Gestaltung im Stil der 80er-Popbühne.
> Es werden bewusst keine Fotos, Namensrechte, Logos oder Musikaufnahmen realer
> Künstler verwendet.

## Wie die Schwierigkeit wächst

**Alle 6 richtigen Antworten eine Stufe höher**, bis Stufe 5. Zahlenraum, Objektanzahl,
Musterlänge und Merkanforderungen wachsen mit. Nach jeder Runde zeigt eine Übersicht,
welche Nummer gut lief und welche noch wackelt.

Bei einer falschen Antwort wird die **richtige Lösung grün markiert** und bleibt etwas
länger stehen – dort passiert das Lernen.

## Bedienung und Barrierefreiheit

- Große Tipp-Flächen (mindestens 64 px), erreichbar mit dem Daumen, feste Position.
- Deutsche Sprachausgabe liest jede Aufgabe vor – hilft, wenn Lesen noch anstrengend ist.
- Hoch- und Querformat, `safe-area-inset` für die Notch, kein Scrollen im Spiel.
- `prefers-reduced-motion` schaltet Scheinwerfer-, Boden- und Glitzer-Animation ab.
- Läuft das Spiel in den Hintergrund (Anruf, Homescreen), pausieren Uhr und Musik.

## Datenschutz

Es werden **keine Daten übertragen**. Punkte, Preise, Bestenlisten und Einstellungen
liegen ausschließlich im `localStorage` des jeweiligen Browsers.
Ist Speichern gesperrt, weicht das Spiel automatisch auf `sessionStorage` und dann auf
den Arbeitsspeicher aus und weist im Eltern-Bereich darauf hin.
Löschen der Website-Daten setzt alles zurück; „Alles zurücksetzen" tut dasselbe im Spiel.

## Für Entwickler

### Dateien

| Datei | Rolle |
|---|---|
| `layla-zahlenheld.html` | **Quelle der Wahrheit** – das komplette Spiel in einer Datei |
| `build-docs.py` | erzeugt `docs/index.html` daraus (Manifest, Service Worker, Datei-Icons, `noindex`) |
| `build-icons.py` | erzeugt die App-Icons als PNG, ohne externe Bibliotheken |
| `docs/` | die Web-App für GitHub Pages: `index.html`, `sw.js`, `manifest.webmanifest`, Icons, `robots.txt` |

Nach jeder Änderung am Spiel:

```bash
python3 build-docs.py        # docs/index.html neu erzeugen
```

`docs/index.html` wird generiert und sollte **nicht** direkt bearbeitet werden.
Wird an den Dateien in `docs/` etwas geändert, in `docs/sw.js` die Zeile
`const CACHE = "zahlenheld-v1"` hochzählen – sonst liefert der Service Worker
weiter die alte Fassung aus.

### Aufbau

`layla-zahlenheld.html` ist bewusst eine Datei mit inline CSS und Vanilla JavaScript –
keine Abhängigkeiten, kein Build-Schritt für das Spiel selbst.

Ein neues Mini-Spiel besteht aus einer Funktion, die eine Aufgaben-Spezifikation liefert:

```js
function gameBeispiel(lv) {          // lv = Stufe 1..5
  return {
    prompt: "Was fragen wir?",       // Anweisung
    question: "3 + 4 = ?",           // große Anzeige (HTML erlaubt)
    visualHTML: "",                  // optionale Bilder/Formen
    options: [{ html: "7", val: 7 }],// Antwort-Buttons
    correct: 7,                      // muss zu einem val passen
    cols: 2,                         // Spalten im Antwort-Raster (2/3/4)
    speak: "3 plus 4",               // Text für die Sprachausgabe
    // preview: { html, ms, text }   // optionale Merkphase vor der Frage
  };
}
```

Danach in die Liste `GAMES` eintragen (`w` steuert, wie häufig die Nummer gezogen wird).
Die Generatoren sind reine Funktionen ohne DOM-Zugriff und lassen sich damit direkt in
Node testen – so wurden alle Stufen mit je 20 000 Aufgaben pro Nummer geprüft.
