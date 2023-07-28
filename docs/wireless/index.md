---
icon: material/wifi-cog
---
# Wireless mit Green-GO v5

**Handbuch:** [Link](https://manual.greengoconnect.com/en/guides/wirelessx/)

## Allgemeines

- Lizenzfreie drahtlose Kommunikation via DECT:
    - EU: `1880 - 1900 MHz` (10 Trägerfrequenzen)
    - USA/Canada: `1920 - 1930 MHz` (5 Trägerfrequenzen)
    - Japan: `1893 - 1906 MHz` (3 Trägerfrequenzen)
- Reichweite von bis zu 300 Metern.
- Bis zu vier Beltpacks können mit einer Antenne verbunden werden.
- Roaming mit bis zu 7 Antennen (X-Pools) ist _immer_ mit einer Unterbrechung von ca. 4 - 7 Sekunden verbunden.

## Pairing Methoden

- Mischbetrieb von OTA und X-Pools is seit v5 nicht mehr möglich.
- OTA Pairings:
    - One-Shot-Verfahren. Keine nachträgliche Änderung möglich.
    - Kein Roaming möglich.
    - Ausschließlich Monitoring via Software.
- X-Pools:
    - Konfiguration via Software.
    - Roaming mit bis zu 7 Antennen möglich.
    - Hinzufügen und Entfernen von Beltpacks mit USB-Verbindung möglich.
    - Ein drahtloses Beltpack kann immer nur mit einem X-Pool verbunden sein.

### OTA Pools

- Der Pairing-Speicher von Antennen und Beltpacks sollte vor Beginn des Pairing-Setups [zurück gesetzt](https://manual.greengoconnect.com/en/guides/wirelessx/#device-preparations) werden.
- Das [Pairing-Setup](https://manual.greengoconnect.com/en/guides/wirelessx/#ad-hock-over-the-air-pairings) erfolgt direkt an den Geräten. Ein direkter Zugriff auf die Geräte ist notwendig.
- Ein Bearbeiten der Pairings ist nicht möglich. Die Software ermöglicht nur das Monitoring.
- Es gibt keine Möglichkeit des Roamings.

### X-Pool Programmierung

- Das Pairing-Setup ist ausschließlich über die Green-GO Control Software möglich.
- Ein Abbrechen des Wizards ist nach dem zweiten Schritt nicht mehr möglich.
- WAA Antennen müssen Mitglied der Konfiguration (Adopted) und über das Netzwerk mit der Software verbunden sein bevor diese im Wizard zur Verfügung stehen.
- Drahtlose Beltpacks werden via USB mit Hilfe der Software programmiert.
- Bei Beltpacks wird ein Pairing direkt nach dem Hinzufügen oder Entfernen programmiert.
- Die Programmierung der Beltpacks kann nacheinander erfolgen.
- WAA Antennen werden erst nach dem Beenden des Wizards programmiert.
- Löschen eines X-Pools ist nur möglich, nachdem alle Beltpacks und Antennen entfernt wurden.
- Ein X-Pool kann jederzeit editiert und angepasst werden.