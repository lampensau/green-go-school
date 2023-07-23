---
---

# Einrichtung eines Audio Interfaces

## Konfiguration eines Programmtons

- Mit verschiedenen Geräten möglich: MCX(D), Si4WR, INTX, Q4WR, DNTI
- Wird immer über eine Gruppe im Green-GO System übertragen
- Zwei unterschiedliche Konfigurationsmöglichkeiten mit 4-Draht Interfaces: Line In/Out, User

## Line In/Out

- Einziger Modus verfügbar auf MCX(D) Sprechstellen
- Ermöglicht simple in/out Konfiguration von Audiosignalen
- Funktioniert nur mit Gruppen
- Keine weiteren Funktionen wie Rufzeichen, GPIO, Scripting, etc.

## User Modus

- Ermöglicht Übertragung auf bis zu 32 Kanälen zu beliebigen Zielen (User oder Gruppe)
- Vollwertige Green-GO Engine mit Zugriff auf alle Funktionen
- Mindestens ein Kanal muss mit dem `Channel Mode: Autotalk` konfiguriert werden, ansonsten wird kein externes Audiosignal zum Green-GO System übertragen

## Anbindung an ein 2-Draht System

- Reihenfolge beim Setup beachten:
    1. 2-Draht System komplett errichten und auf Funktion testen
    2. Mikrofone aller 2-Draht Sprechstellen deaktivieren um Feedback-Loops zu vermeiden
    3. Auf dem Green-GO 2-Draht Interface die `Autonull` Prozedur ausführen
    4. Prüfen das min. ein Kanal des aktiven Users mit `Channel Mode: Autotalk` konfiguriert ist
    5. Verbindung prüfen und ggf. die Werte für `From 2-Wire` und `To 2-Wire` anpassen.
- Verbindung und Setup anfällig für Änderungen wie z.B. Leitungimpedanz
- Bei zu hohem Grundrauschen im 2-Draht System kann der `Gate Threshold` des Interfaces angepasst werden
- Rufzeichen werden unterstützt. Konfiguration ist abhängig von Hersteller und Modell