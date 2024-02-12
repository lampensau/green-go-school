---
title: Eine Green-GO Featureübersicht
description: Ein Überblick über die wichtigsten Eigenschaften und Features eines digitalen Green-GO Interkom Systems
icon: material/clipboard-list
social:
  cards_layout_options:
    background_color: '#105723be'
    background_image: layouts/features.png
---
# Green-GO Eigenschaften und Featureübersicht

**Handbuch:** [Link](https://manual.greengoconnect.com/en/features/)

## Zentrale Eigenschaften

- Green-GO ist ein _dezentrales_ & digitales Kummunikationssystem und flexibel im Einsatz.
- Green-GO läuft auf ganz _normaler Netzwerkinfrastruktur_ + PoE ([IEEE 802.3af](https://de.wikipedia.org/wiki/Power_over_Ethernet#IEEE-Spezifikationen)) - für die Spannungsversorgung der einzelnen Geräte.
    - Layer 3 Multicast mit einer dedizierten Multicast-Adresse pro System.
    - Green-GO Geräte sind sparsam und benötigen maximal 6 Watt Leistung.
    - Prinzipiell erfolgt eine sternenförmige Verkabelung von den Switches zum Endgerät.
    - Einzelne Geräte (MCX(D), 19“ Interfaces) ermöglichen eine _optionale_ 12 V Spannungsversorgung (externes Netzteil) und Daisy-Chaining der Netzwerkverbindung.
    - Mehr Informationen zum Netzwerk können [hier](https://manual.greengoconnect.com/en/guides/network/) gefunden werden.
- Green-GO Systeme beginnen bereits ab zwei Beltpacks und können jederzeit _bedarfsgerecht_ erweitert werden.
- Green-GO ist ein _lineares Investement_.
    - Geräte können bedarfsgerecht zugemietet oder käuflich erworben werden.
    - DryHire-Kontakte auf Anfrage bei mail@castinfo.de erhältlich.

## Wichtige Eigenschaften

- **Keine zentrale Steuereineheit** wird benötigt (z.B. Master Station oder Matrix Frame).
    - Jedes Gerät speichert die aktive Konfiguration im lokalen Speicher und kann als Startpunkt für ein eigenständiges System dienen.
- Standalone Einsatz ohne Software _problemlos möglich_.
    - Für einen Einsatz ohne die v5 Software muss die Konfiguration zuerst im _Binärformat_ auf den Geräten [abgespeichert](https://manual.greengoconnect.com/en/getting-started/software/#save-the-configuration-to-the-devices) werden.
- Neue (_kostenlose_) [Software](https://manual.greengoconnect.com/en/release-notes/software/) (und [Firmware](https://manual.greengoconnect.com/en/release-notes/firmware/)) bietet zahlreiche Konzepte um ein System _besser und schneller_ einzurichten oder zu überwachen.
- [Drahtlose Kommunikation im System (DECT)](https://manual.greengoconnect.com/en/guides/wirelessx/).
    - Roaming wird unterstützt ([X-Pool](https://manual.greengoconnect.com/en/guides/wirelessx/#x-pool-pairings)) jedoch **ohne** nahtlosen Antennenwechsel.
- Eine neue Scripting Engine erweitert die Möglichkeiten eines Systems und bietet nicht nur Zugriff auf _jede_ interne Funktion, sondern auch externe Anbindungen an fremde Systeme.
    - Beispiele finden sich in der `School Resources.gg5` Konfiguration welche als [Download](../downloads/index.md) zur Verfügung steht.
    - Alternativ gibt es auch noch ein [GitHub Repository](https://github.com/ELClighting/green-go-scripts) oder das [User-Forum](https://greengoconnect.com/index.php?p=/categories/green-go-scripting) mit weiteren Beispielen.
- 32 _individuelle_ Kanäle mit zahlreichen Features auf _jedem_ Gerät.
    - Eigenständige Kanalbelegung und -konfiguration.
    - Mögliche Kommunikationsziele sind User (private Gespräche) oder Gruppen (Konferenzschaltung oder Party-Line)
- 4 _extra_ Kanäle für Sonderanwendungen wie Ansagen ([Announcements](https://manual.greengoconnect.com/en/glossary/#announcement-channel) und [Emergencies](https://manual.greengoconnect.com/en/glossary/#emergency-channel)), [Programmton](https://manual.greengoconnect.com/en/glossary/#program-audio) oder [_temporäre_ direkte Kommunikation](https://manual.greengoconnect.com/en/glossary/#direct-channel).
- Bis zu 3000 [_User_](https://manual.greengoconnect.com/en/glossary/#user) und 400 [_Gruppen_](https://manual.greengoconnect.com/en/glossary/#group) in einem System.
    - Ein User stellt einer [Green-GO Engine](https://manual.greengoconnect.com/en/glossary/#green-go-engine) oder Gerät die Konfiguration zur Verfügung.
        - Gerät oder Engine werden mit Hilfe des Users im System angesprochen.
        - Ein User kann beliebig vielen Engines oder Geräten zugewiesen werden.
    - Eine Gruppe dient hauptsächlich zur Kommunikation mit mehreren Usern.
        - Bei Nutzung der Sonderkanäle ([Programmton](https://manual.greengoconnect.com/en/glossary/#program-audio), [Announcements](https://manual.greengoconnect.com/en/glossary/#announcement-channel), [Emergency](https://manual.greengoconnect.com/en/glossary/#emergency-channel)) muss eine Gruppe für jede Signalquelle verwendet werden.
- Maximale eingehende _aktive_ Gespräche pro Gerät:
    - 16 kHz: ca. 300 Streams/Gerät
    - 32 kHz: ca. 150 Streams/Gerät
    - 48 kHz: ca. 100 Streams/Gerät
- _Lippensynchrone_ Kommunikation mit 10 ms Latenz vom Mikrofon zum Kopfhörer (_kabelgebunden_).
    - ca. 20 ms bei drahtloser Verbindung via [DECT](https://manual.greengoconnect.com/en/glossary/#dect).
- Hohe [Audioqualität](https://manual.greengoconnect.com/en/glossary/#audio-quality) mit _bis zu_ 48 kHz Abtastrate (mono) und moderatem Datenverbrauch (max. 800 kbps/Stream).
    - 16 kHz: ca. 320 KBit/s
    - 32 kHz: ca. 650 KBit/s
    - 48 kHz: ca. 900 KBit/s
- Zweistufiges Rufzeichen 
    - Drei verschiedene Alarmtöne für jeden Teilnehmer individuell konfigurierbar.
    - Konfiguration ist für jeden Kanal einzeln möglich.
- Dreistufige Lichtzeichen für nonverbale Kommunikation.
