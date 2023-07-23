---
description: Empfehlungen und Tips zur Netzwerkinfrastruktur und -setup
icon: material/ip-network
social:
    cards_layout: network
---
# Das Netzwerk Setup

**Handbuch:** [Link](https://manual.greengoconnect.com/en/guides/network/)

## Verkabelung

- Ein ungeschirmtes Netzwerkkabel ([UTP](https://de.wikipedia.org/wiki/Twisted-Pair-Kabel#UTP)) wird vom Hersteller für eine Verkabelung empfohlen.
- Der Standard [TIA/EIA-568B.1](https://www.csd.uoc.gr/~hy435/material/TIA-EIA-568-B.1.pdf) definieret die maximale Länge eines Ethernet Kabels auf 100 Meter. Die eigentliche Reichweite kann aber abhängig von der Kabelqualität abweichen.
- Geräte mit zwei Neutrik EtherCON Anschlüssen verfügen über einen internen (unmanaged) Netzwerk Switch. Pakete werden nicht-diskriminierend weitergeleitet.
    - PoE Spannungsversorgung wird **nicht** mit durchgeschliffen.

## Switches

Green-GO ist kompatibel mit einem handelsüblichen Layer 3 Netzwerkswitch. Es gibt jedoch ein paar Dinge beim Kauf zu beachten.

### Unmanaged

- Green-GO ist standardmäßig **nicht kompatibel** mit _unmanaged_ Switches welche eine IGMP Konfiguration verwenden. Ein solcher Switch erfodert zusätzliche Hardware welche als IGMP-Querier oder -Router fungiert.
- [Energy Efficient Ethernet](https://de.wikipedia.org/wiki/Energy_Efficient_Ethernet) ([IEEE 802.3az](https://standards.ieee.org/ieee/802.3az/4270/)) sollte deaktivierbar sein.
- [PoE](https://de.wikipedia.org/wiki/Power_over_Ethernet) Support (min. [IEEE 802.3af](https://standards.ieee.org/ieee/802.3af/1090/), 48 V)

### Managed

- Support für QoS via [CoS](https://de.wikipedia.org/wiki/IEEE_802.1p) / [DSCP](https://de.wikipedia.org/wiki/DiffServ)
- Support für VLANs ([IEEE 802.1Q](https://standards.ieee.org/ieee/802.1Q/6844/))
- Support für IGMP Snooping
- [PoE](https://de.wikipedia.org/wiki/Power_over_Ethernet) Support (min. [IEEE 802.3af](https://standards.ieee.org/ieee/802.3af/1090/), 48 V)

## Spannungsversorgung

- Green-GO Geräte erfordern mindestens den PoE Standard IEEE 802.3af (15.4W, 48V).
- Es werden beide PoE Varianten utnerstützt. PoE Typ `A` (spare lines) und `B` (data lines).
- Verbrauch liegt zwichen 2 - 6 Watt, abhängig vom Gerät und der Konfiguration.

## IP Addressierung

- Es müssen _lokale_ IP-Adressbereiche (z.B. `192.168.0.0/24`) bei einer _manuellen Netzwerkkonfiguration_ verwendet werden ([RFC1918](https://datatracker.ietf.org/doc/html/rfc1918)).
- Die dynamische Netzwerkkonfiguration folgt [RFC3927](https://datatracker.ietf.org/doc/html/rfc3927) und benutzt den IP-Addressbereich `169.254.0.0/16`. Dieser Bereich wird gerne auch als _link-local_, _bonjour_, or _zeroconf_ bezeichnet. 
- Green-GO Geräte sind kompatibel mit allen standard DHCPv4 Servern.
- Es gibt derzeit **keinen** IPv6 Support für _alle_ Green-GO Geräte.

## Bandbreiten

- Die meisten Green-GO Geräte verfügen über einen `10/100 Mbps` Netzwerkanschluss.
- Die Statuskommunikation zwischen den Green-GO Geräten beträgt ca. `500 Bit/s` pro Gerät.
- Die Statuskommunikation zwischen Green-GO Gerät und Software beträgt ca. `255 Bit/s` pro Gerät

| Sample Rate | Bandbreite ([Engine](https://manual.greengoconnect.com/en/glossary/#green-go-engine)) | Aktive Streams (max) |
| :-- | :-- | :-- |
| 16 kHz | 319 KBit/s | ~ 300 Streams/Gerät |
| 32 kHz | 636 KBit/s | ~ 150 Streams/Gerät |
| 48 kHz | 892 KBit/s | ~ 105 Streams/Gerät |

## UDP Ports

| Port | Typ | Beschreibung |
| :-- | :-- | :-- |
| 6464 | UDP | Firmware Updates & State Broadcast |
| 5810 | UDP | Geräte Konfiguration & Kommunikation |
| 2001 | TCP | Software Datenverbindung |
| 2002 | TCP | Support Datenverbindung |
| 9221 | TCP | Remote Control App |

## Jitter und Latenzen

Green-GO ist eine Echtzeit-Audio-Anwendung und erwartet einen stetigen Paketfluss mit miminalen zeitlichen Variationen zwischen einzelnen Paketen (Jitter). Die eigentliche Paketlatenz ist grundsätzlich weniger entscheidend.

In der Regel wird es bei Green-GO bei einem Jitter von über 2 ms / 1 s problematisch. Auftretende Symptome könnten z.B. verterrtes Audio oder abgehackte Kommunikationen sein.

## VLAN Setups

- VLANs werden nach IEEE 802.1Q unterstützt und werden für komplexe Netzwerkinfrastrukturen empfohlen.
- Die Einrichtung und Konfiguration eines VLAN hängt vom Hersteller und Modell des Netzwerkswitches ab.
- Ein Green-GO Gerät sollte an einem _untagged_ Switchport angeschlossen sein.
- Die Green-GO Control Software ist derzeit nicht zuverlässig lauffähig mit _trunked_ bzw. _tagged_ Switchports.

### IGMP Snooping Setup

- Nur mit VLAN-Konfiguration empfohlen.
- Es gibt eine [Multicast Adresse](https://manual.greengoconnect.com/en/software/views/config/#config-settings) pro Konfiguration.

### QoS Konfiguration

- In Netzwerken mit viel Datenfluss (Bandbreite oder Paketanzahl) kann es erforderlich sein Green-GO Datenverkehr zu priorisieren.
- Green-GO Audiodaten können mit Hilfe des [DSCP Werts](https://de.wikipedia.org/wiki/DiffServ) `46` (VoIP) und [PCP Wert](https://de.wikipedia.org/wiki/IEEE_802.1p) `5` priorisiert werden.

### Paket Klassifizierung

| DSCP Feld | DSCP Wert | Beschreibung |
| :-: | :-: | :-- |
| EF | 46 | Priorisieren von Paketen für die Kommunikation und den Statusaustausch zwischen Geräten. |
| CS0 | 0 | Der allgemeine Status-Broadcast wird mit dem `CS0` versand und benötigt keine Priorisierung. |