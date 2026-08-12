# ⚡️ Zahlen-Blitz

Ein deutschsprachiges Lernspiel für Kinder am Übergang von der **1. in die 2. Klasse**.
Neun kurze Mini-Spiele wechseln sich ab und trainieren Rechnen, Farben, Formen, Muster,
Konzentration und Merkfähigkeit – als Zeit-Challenge mit Punkten, Rekorden und
freischaltbaren Tieren.

Das ganze Spiel steckt in **einer einzigen Datei**: `zahlen-blitz.html`.
Kein Server, kein Internet, keine Installation, keine Werbung, kein Tracking.

---

## Schnellstart

### Auf dem Mac (Safari)
1. `zahlen-blitz.html` herunterladen.
2. Doppelklick – die Datei öffnet sich in Safari. Fertig.

### Auf dem iPhone (iOS 17+, iPhone 17 & Safari)
1. Die Datei per **AirDrop** vom Mac aufs iPhone schicken (oder in iCloud Drive ablegen).
2. In der App **Dateien** auf `zahlen-blitz.html` tippen → das Spiel öffnet sich in Safari.
3. Empfehlung: **Teilen → Zum Home-Bildschirm** hinzufügen.
   Dann startet Zahlen-Blitz wie eine App im Vollbild, ohne Safari-Leisten.

Alternativ kann die Datei auf einem beliebigen Webspace liegen und per Link geöffnet werden –
sie braucht keinerlei Backend.

---

## Die neun Mini-Spiele

| Spiel | Was geübt wird |
|---|---|
| **Rechen-Blitz** | Plus und Minus bis 100, mit Zehnerübergang |
| **Lücken-Jäger** | Lücken- und Umkehraufgaben (`7 + ? = 15`, `52 − ? = 20`) |
| **Mal-Monster** | Erstes Einmaleins (1er, 2er, 5er, 10er) – mit Bildern zum Bündeln, ab Stufe 4 auch umgekehrt (`? × 5 = 30`) |
| **Zahlen-Reihe** | Zahlenreihen in 1er-, 2er-, 3er-, 5er- und 10er-Schritten, vorwärts und rückwärts |
| **Größer-Kleiner** | `<`, `=`, `>` vergleichen – ab Stufe 3 auch Rechenterme gegeneinander |
| **Farb-Falle** | Konzentration und Impulskontrolle: Farbe der Schrift gegen Wortbedeutung |
| **Formen-Finder** | Formen und Farben unterscheiden und zählen |
| **Muster-Meister** | Muster erkennen und fortsetzen |
| **Merk-Blitz** | Kurzzeitgedächtnis: Dinge einprägen und wiedererkennen |

## Zwei Modi

- **⚡️ Blitz (90 Sekunden)** – Zeit-Challenge. Jede richtige Antwort bringt Punkte
  und **+2 Sekunden**, jede falsche kostet **2 Sekunden**. Punkte steigen mit der Stufe,
  eine Serie (🔥) gibt Bonuspunkte.
- **🌙 Ruhig (20 Aufgaben)** – ohne Uhr, ohne Druck. Gut zum Üben und für den Abend.

## Wie die Schwierigkeit wächst

Die Stufe steigt automatisch: **alle 6 richtigen Antworten eine Stufe höher**, bis Stufe 5.
Der Zahlenraum, die Anzahl der Objekte, die Muster-Länge und die Merk-Anforderungen
wachsen mit. Nach jeder Runde zeigt eine Übersicht, welches Mini-Spiel gut lief und
welches noch wackelt.

Bei einer falschen Antwort wird immer die **richtige Lösung grün markiert** – dort passiert
das Lernen, deshalb bleibt sie etwas länger stehen.

## Bedienung und Barrierefreiheit

- Alle Antworten sind **große Tipp-Flächen** (mindestens 64 px hoch), erreichbar mit dem Daumen.
- **Töne** und **deutsche Sprachausgabe** lassen sich auf der Startseite einzeln abschalten.
  Die Aufgaben werden vorgelesen – hilfreich, wenn das Lesen noch anstrengend ist.
- Layout passt sich an Hoch- und Querformat an, respektiert die iPhone-Notch
  (`safe-area-inset`) und kommt ohne Scrollen aus.
- `prefers-reduced-motion` schaltet die Hintergrund-Animation ab.

## Datenschutz

Es werden **keine Daten übertragen**. Rekorde, Sterne und die Ton-Einstellungen liegen
ausschließlich im `localStorage` des jeweiligen Browsers auf dem Gerät.
Löschen der Website-Daten setzt alles zurück.

## Für Entwickler

`zahlen-blitz.html` ist bewusst eine Datei mit inline CSS und Vanilla JavaScript –
keine Abhängigkeiten, kein Build-Schritt.

Ein neues Mini-Spiel besteht aus einer Funktion, die eine Aufgaben-Spezifikation liefert:

```js
function gameBeispiel(lv) {          // lv = Stufe 1..5
  return {
    prompt: "Was fragen wir?",       // Anweisung
    question: "3 + 4 = ?",           // große Anzeige (HTML erlaubt)
    visualHTML: "",                  // optionale Bilder/Formen
    options: [{ html: "7", val: 7 }] // Antwort-Buttons
    correct: 7,                      // muss zu einem val passen
    cols: 2,                         // Spalten im Antwort-Raster (2/3/4)
    speak: "3 plus 4",               // Text für die Sprachausgabe
    // preview: { html, ms, text }   // optionale Merkphase vor der Frage
  };
}
```

Danach in die Liste `GAMES` eintragen (`w` steuert, wie häufig das Spiel gezogen wird).
Die Spiel-Generatoren sind reine Funktionen ohne DOM-Zugriff und lassen sich damit
direkt in Node testen.
