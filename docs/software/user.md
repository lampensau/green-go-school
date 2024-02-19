

# User Konfiguration

## Kanalkonfiguration

- [Kanalbelegung & -wechsel](https://manual.greengoconnect.com/en/getting-started/software/#channel-configuration "Weitere Informationen im offiziellen Green-GO Handbuch")
- [Gleichzeitiges Bearbeiten mehrer Elemente](https://manual.greengoconnect.com/en/getting-started/software/#editing-in-bulk "Weitere Informationen im offiziellen Green-GO Handbuch")
- Konfiguration von Kanalerweiterungen
- Löschen gesetzer Einstellungen (transparente Einstellungen)
- [Listen Override](https://manual.greengoconnect.com/en/software/properties/channels/#channel-assignment "Weitere Informationen im offiziellen Green-GO Handbuch")
- Talk Modi
- [Channel Modi](https://manual.greengoconnect.com/en/software/properties/channels/#channel-mode "Weitere Informationen im offiziellen Green-GO Handbuch") (Autotalk, Auto Reply, GPIO Control, Flex List)
- [Listen Modi](https://manual.greengoconnect.com/en/software/properties/channels/#listen-mode "Weitere Informationen im offiziellen Green-GO Handbuch") (Listen on Talk, Isolate)
- Call & Cue Modi
- Lautstärken & Kanalprioritäten (Level, Priority)
- Signalrouting / Ausgänge (Outputs)
- Tabellenkonfiguration (sichtbare Spalten)

## Spezialkanäle

**Handbuch:** [Link](https://manual.greengoconnect.com/en/software/properties/channels/#special-channels "Weitere Informationen im offiziellen Green-GO Handbuch")

- Programmton
- Ansagenkanal (Priorität > `High`)
- Notfallkanal (Priorität > Ansagenkanal)
- Direkte (temporäre) Kommunikationen

## Usereinstellungen

**Handbuch:** [Link](https://manual.greengoconnect.com/en/software/properties/user_settings/ "Weitere Informationen im offiziellen Green-GO Handbuch")

- Farben
- Active Time (Dauer der Aktivitätsanzeige)
- Reply Modi (Active, Last)
- Priority Dim
- Cue time-out

## Räume (Rooms)

**Handbuch:** [Link](https://manual.greengoconnect.com/en/software/tree/rooms/ "Weitere Informationen im offiziellen Green-GO Handbuch")

- Dient zur besseren Strukturierung anhand lokaler Örtlichkeiten
- Room Dim für Audiosignale aus dem gleichen Raum

## Flex Liste

**Handbuch:** [Link](https://manual.greengoconnect.com/en/software/properties/channels/#flex-list "Weitere Informationen im offiziellen Green-GO Handbuch")

- Ermöglicht den Wechsel eines Kanalziels
- Erweitert den direkten Zugriff bei begrenzter Benutzeroberfläche
- Bis zu 20 Ziele möglich

## Sicherheitseinstellungen

**Handbuch:** [Link](https://manual.greengoconnect.com/en/software/properties/security/ "Weitere Informationen im offiziellen Green-GO Handbuch")

- User-Pincode (4-stellig) verhindert unbefugtes Laden
- Individuelle Zugriffskonfiguration erfordert Tech-Pincode

## Geräteprofile

- Live Preview erleichtert Kanalbelegung
- Tastenbelegung und UI Konfiguration
- Audioeinstellungen
- Gerätespezifische Konfigurationen (z.B. GPIO, Line In/Out, etc.)

# Templates

**Handbuch:** [Link](https://manual.greengoconnect.com/en/software/tree/templates/ "Weitere Informationen im offiziellen Green-GO Handbuch")

- Speichern / Laden von Templates erleichtern die Konfiguration
- Transparente Templates halten keine dauerhafte Verbindung

# Geräteverwaltung

**Handbuch:** [Link](https://manual.greengoconnect.com/en/software/tree/devices/ "Weitere Informationen im offiziellen Green-GO Handbuch")

- Einstellungen werden **nicht** in der Konfigurationsdatei gespeichert, sondern nur im Gerätespeicher abgelegt.
- [Synchronisation abweichender Konfigurationen](https://manual.greengoconnect.com/en/software/tree/devices/#devices-out-of-sync "Weitere Informationen im offiziellen Green-GO Handbuch")

# Scripting Engine

**Handbuch:** [Link](https://manual.greengoconnect.com/en/software/tree/scripts/ "Weitere Informationen im offiziellen Green-GO Handbuch")

- Ein kompiliertes Script kann von jedem Gerät über das Setup Menü geladen werden
- Ein Script kann erst nach erfolgreicher Kompilierung ausgeführt werden
- Eine fehlerhafte Kompilierung wird lediglich mit einem roten Indikator in der Zeile mit dem (ersten) Fehler angezeigt
- Scripte können nur bearbeitet werden, wenn diese in Textform (Quellcode) im Dateiformat `*.gg5t` vorliegen
- Ein Script kann in beiden Varianten (Quellcode/Kompiliert) exportiert oder importiert werden