---
title: Die Green-GO Control Software
description: Eine Einführung in die Bedienung der Software und die Verwaltung einer Green-GO Systemkonfiguration
icon: material/application
---
# Green-GO Control Software

## Installation

- [Software Installation (EN)](https://manual.greengoconnect.com/en/getting-started/upgrade/#software-installation)
- [Firmware Upgrade (EN)](https://manual.greengoconnect.com/en/getting-started/upgrade/#upgrade-your-devices)

## Ein Erster Überblick

- Starten der Software: Der Splashscreen
- [Erstellen einer ersten Konfiguration mit dem Quickstart Wizard](https://manual.greengoconnect.com/en/getting-started/software/#create-a-configuration-using-the-wizard)
    - Konfigurationsname und automatische konfiguration für Sonderkanäle
    - Bis zu 10 User und Gruppen können erstellt und individuell benannt werden
    - Einträge ohne einen Namen werden nach dem Prinzip `{User|Group} #ID` benannt
    - Kommunikationsziele (ausschließlich Gruppen) können auf Userkanäle verteilt werden
    - Klickreihenfolge definiert die Kanalreihenfolge in der Kanalmatrix
    - Geräte einer Konfiguraiton hinzufügen
    - Userzuweisung mittels Drag&Drop im letzten Schritt möglich
- [Neue Oberfläche](https://manual.greengoconnect.com/en/software/interface/)
    - Ansichten (Dashboard, Konfiguration, Netzwerk, Drahtlos)
    - Tools (Save to Devices, Assistenten, Support, File, Settings, Handbuch)
    - Statusleiste (Listen In (noch nicht veröffentlicht), Konfigurationsname, Gerätestatus, Warnungen)
    - Index-Tree (Konfigurationsindex mit Suchfunktion)
    - Navigationsleiste (Sektionsnavigation und -funktionen)
    - Inhaltsansicht der aktiven Elemente
- [Dashboard(s)](https://manual.greengoconnect.com/en/software/views/dashboard/)
    - Beliebig viele Dashboards möglich
    - Frei konfigurierbares 3x3 Grid
    - Karten können konfiguriert werden

## Konfigurations- und Systemverwaltung

### [Connection View](https://manual.greengoconnect.com/en/software/views/connection/)

- [Firmware Updates von Geräten via Netzwerk oder USB](https://manual.greengoconnect.com/en/guides/firmware/)
- Änderung der Netzwerk- und Verbindungseinstellungen sind im `Network Tab` verfügbar
- Änderung der Regionseinstellungen sind im `USB Tab` möglich
- Anzeige von verbundenen Applikationen ist im `Application Tab` verfügbar
- Adoptieren von Geräten ist ausschließlich im `Network Tab` möglich
    - Vorgang speichert aktuelle Version der Konfiguration auf dem Endgerät
    - Adoptierte Geräte verlieren Userzuordnung und sind erst nach erneuter Zuordnung einsatzbereit!
- Einer Konfiguration via eines Geräts oder entfernter Softwareinstanz beitreten

### Konfigurations- bzw. Systemeinstellungen

- Konfigurationen laden via dem File-Menü in der Toolbar
    - Mit diesem Tool können auch v4 Konfigurationen geladen und auf v5 geupdated werden (nicht über den Splash-Screen möglich!)
- Konfigurationen mergen via dem File-Menü in der Toolbar
- Es gibt keine Abhängigkeit zwischen Konfigurationsname vs. Dateiname
- Die Konfigurations ID (Config ID) entscheidet über eine Zugehörigkeit einer Konfiguration
- Die Audioqualität wird mit v5 nun Systemweit für alle Teilnehmer und Kanäle definiert (**Warnung:** Ein Wechsel der `Sample-Rate` ändert die `Config ID`!)
    - Die Audioqualität von drahtlosen Green-GO Endgeräten wird von dieser Einstellung nicht beeinflusst!
    - Die Audioqualität für drahtlose Verbindung wird individuell für jedes Endgerät konfiguriert.
- Manuelle Multicast-Adresse ist weiterhin möglich. Ansonsten errechnet die Software beim Erstellen einer neuen Konfiguration eine zufällige Multicast-Adresse<br>(**Warnung:** Ändert die `Config ID`!)
  - Es benötigt eine exklusive Multicast-Adresse pro System. Eine Überschneidung kann zu ungewollten Problemen führen.
- Benutzerdefinierte Statusfarben können im `Config View` angepasst werden
- Passwortschutz für Monitoring (config) und Administration
- Geräte PIN Code ermöglicht Zugriff zu gesperrten Funktionen und Menüs

### Save to Devices

- Unterbricht für ca. 1 - 2 Sekunden die Kommunikation auf **allen** Geräten.
- Wird nur für einen _standalone_ Einsatz ohne die Software benötigt.
- Nicht gespeicherte Änderungen werden mit einem Indikator auf dem Symbol angezeigt.
- Letzter Zeitpunkt der Übertragung wird in der Konfigurationsverwaltung angezeigt.
- Geräte speichern **keine** "überflüssigen" Daten:
    - Script-Quellcode (nur die compilierte Binary wird gespeichert)
    - Templates
    - Aufgezeichnete "Metadata" verschiedener Ansichten.

## Konfigurations Wizards

- IFB Wizard (Kommandokanal)
- One to Many (Kommandokanal _light_)
- Partyline (interaktiver Gruppen Wizard)

## Support Connection

- Ermöglicht einen Ad-Hock Zugriff auf das System und die Konfiguration wenn aktiv
- Nicht für permanente Verbindungen vorgesehen
- Kein Screen-Share, die Verbindung teilt einzig die Konfiguration und Statusinformationen eines Systems
- Funktion für dauerhaften entfernten Zugriff ist in Arbeit