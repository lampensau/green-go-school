

# User Konfiguration

## Kanalkonfiguration

- [Kanalbelegung & -wechsel](https://manual.greengoconnect.com/en/getting-started/software/#channel-configuration)
- [Gleichzeitiges Bearbeiten mehrer Elemente](https://manual.greengoconnect.com/en/getting-started/software/#editing-in-bulk)
- Konfiguration von Kanalerweiterungen
- Löschen gesetzer Einstellungen (transparente Einstellungen)
- [Listen Override](https://manual.greengoconnect.com/en/software/properties/channels/#channel-assignment)
- Talk Modi
- [Channel Modi](https://manual.greengoconnect.com/en/software/properties/channels/#channel-mode) (Autotalk, Auto Reply, GPIO Control, Flex List)
- [Listen Modi](https://manual.greengoconnect.com/en/software/properties/channels/#listen-mode) (Listen on Talk, Isolate)
- Call & Cue Modi
- Lautstärken & Kanalprioritäten (Level, Priority)
- Signalrouting / Ausgänge (Outputs)
- Tabellenkonfiguration (sichtbare Spalten)

## [Usereinstellungen](https://manual.greengoconnect.com/en/software/properties/user_settings/)

- Farben
- Active Time (Dauer der Aktivitätsanzeige)
- Reply Modi (Active, Last)
- Priority Dim
- Cue time-out

## [Räume (Rooms)](https://manual.greengoconnect.com/en/software/tree/rooms/)

- Dient zur besseren Strukturierung anhand lokaler Örtlichkeiten
- Room Dim für Audiosignale aus dem gleichen Raum

## [Spezialkanäle](https://manual.greengoconnect.com/en/software/properties/special_channels/)

- Programmton
- Ansagenkanal (Priorität > `High`)
- Notfallkanal (Priorität > Ansagenkanal)
- Direkte (temporäre) Kommunikationen

## [Flex Liste](https://manual.greengoconnect.com/en/software/properties/flexlist/)

- Ermöglicht den Wechsel eines Kanalziels
- Erweitert den direkten Zugriff bei begrenzter Benutzeroberfläche
- Bis zu 20 Ziele möglich

## [Sicherheitseinstellungen](https://manual.greengoconnect.com/en/software/properties/security/)

- User-Pincode (4-stellig) verhindert unbefugtes Laden
- Individuelle Zugriffskonfiguration erfordert Tech-Pincode

## Geräteprofile

- Live Preview erleichtert Kanalbelegung
- Tastenbelegung und UI Konfiguration
- Audioeinstellungen
- Gerätespezifische Konfigurationen (z.B. GPIO, Line In/Out, etc.)

# [Templates](https://manual.greengoconnect.com/en/software/tree/templates/)

- Speichern / Laden von Templates erleichtern die Konfiguration
- Transparente Templates halten keine dauerhafte Verbindung

# [Geräteverwaltung](https://manual.greengoconnect.com/en/software/tree/devices/)

- Einstellungen werden **nicht** in der Konfigurationsdatei gespeichert, sondern nur im Gerätespeicher abgelegt.
- [Synchronisation abweichender Konfigurationen](https://manual.greengoconnect.com/en/software/tree/devices/#devices-out-of-sync)

# [Scripting Engine](https://manual.greengoconnect.com/en/scripting/language/) (braucht warscheinlich einen eigenen Tag)

- Ein kompiliertes Script kann von jedem Gerät über das Setup Menü geladen werden
- Ein Script kann erst nach erfolgreicher Kompilierung ausgeführt werden
- Eine fehlerhafte Kompilierung wird lediglich mit einem roten Indikator in der Zeile mit dem (ersten) Fehler angezeigt
- Scripte können nur bearbeitet werden, wenn diese in Textform (Quellcode) im Dateiformat `*.gg5t` vorliegen
- Ein Script kann in beiden Varianten (Quellcode/Kompiliert) exportiert oder importiert werden