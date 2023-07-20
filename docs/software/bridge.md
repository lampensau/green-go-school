

# Anbindung entfernter Netzwerke oder Endgeräte

- Nur mit der Green-GO BridgeX empfohlen und Supporttechnisch unterstützt
- Die Green-GO BridgeX ist ein Multicast-Unicast Router der eine mit AES256 verschlüsselte Verbindung mit einem Green-GO Endgerät oder Applikation aufbauen kann
- Frei konfigurierbare Buffergrößen für ein- und ausgehende Verbindungen
- Es gibt zwei Verbindungsmodi: User, Group
- Selbstbau via VPN oder ähnliche Konzepte ist möglich, jedoch muss die Verbindung vor Jitter geschützt werden

## Verbindung via User Modus herstellen

- Verbindet einzelne Green-GO Geräte oder Engines mit vollem Funktionsumfang
- Anbindung erfolgt immer über einen User und integriert sich wie ein lokales Green-GO Gerät
- Erhöhte Latenz ist zu erwarten aber abhängig vom Übertragungsweg

## Verbindung via Group Modus herstellen

- Verbindet immer zwei oder mehr Green-GO BridgeX miteinander
- Ideal um ganze Systeme über Fremdnetzwerke miteinander zu verbinden
- Verbindung wird immer über eine Gruppe übertragen
- Konfigurationen einzelner Green-GO BridgeX Verbindungspunkte können abweichen
- Lokale Kommunikation bleibt Lippensynchron, einzig die Kommunikation über die entsprechende Gruppe wird mit abweichender Latenz übermittelt

## Verbindungsmodi

### Direct IP

- Verbindet sich direkt zu einer IP Adresse und definierten UDP Port
- Erfordert evtl. eine Portweiterleitung (NAT)

### Auto IP

- Verbindet sich automatisch zu einer lokalen IP Adresse (UDP Port wird nicht benötigt)
- Funktioniert nur im lokalen Subnetz

### Cloud Connection

- Verbindung über Server von Green-GO mittels ID und Passwort
- Keine Portweiterleitung erforderlich. Verbindungen benutzen das _Hole-Punching_ Prinzip