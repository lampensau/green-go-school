---
title: Green-GO Bedienung
description: Eine Einführung in die grundlegende Bedienung von Green-GO Sprechstellen
icon: material/gesture-double-tap
social:
  cards_layout_options:
    background_color: '#105723be'
    background_image: layouts/features.png
---
# Benutzung einer Green-GO Station

**Handbuch:** [Link](https://manual.greengoconnect.com/en/getting-started/usage/)

## Benutzeroberfläche

### Statusfarben

Ein Green-GO Gerät informiert den Anwender über den Geräte-, System- und Kanalstatus mit Hilfe von Farben.

Mit der _Default-Konfiguration_ `Factory Default` werden folgende Farben für den Kanalstatus verwendet:

| Farbe {width=5%}| Verhalten {width=12%}| Status {width=20%}| Beschreibung {width=63%}|
|:-:|:-|:-|:-|
| <span class="status-dot blue"></span> | Statisch | Free | Dem Kanal ist kein Kommunikationsziel [zugewiesen](https://manual.greengoconnect.com/en/getting-started/software/#channel-assignments). Der Kanal ist nicht belegt. |
| <span class="status-dot blue"></span> | Statisch | No Member | Es gibt kein Green-GO Gerät welches auf diesem Kanal empfängt. |
| <span class="status-dot blue"></span> | Statisch | Idle | Der Kanal ist belegt, es gibt empfangende Geräte und der Kanal ist inaktiv. |
| <span class="status-dot blue"></span> | Statisch | Active | Ein Green-GO Gerät oder User hat den Kanal für eine Übertragung [geöffnet](https://manual.greengoconnect.com/en/getting-started/usage/#talking) - es wird aber noch kein Audio übertragen. |
| <span class="status-dot yellow"></span> | Statisch | Active VOX | Der Kanal _empfängt_ [Audio Kommunikation](https://manual.greengoconnect.com/en/getting-started/usage/#receiving-voice-communication). |
| <span class="status-dot blink__blue-yellow"></span> | Blinkend | Active Muted | Der Kanal ist [_stumm geschaltet_](https://manual.greengoconnect.com/en/getting-started/usage/#muting-a-channel) und empfängt Audio Kommunikation. |
| <span class="status-dot green"></span> | Statisch | Talk | Der Kanal ist für eine Übertragung [_geöffnet_](#talking) und wird den aktiven Input übertragen. |
| <span class="status-dot green"></span> | Statisch | Autotalk | Der Kanal wurde _automatisch_ durch den Kanalmodus `Autotalk` für eine Übertragung geöffnet. |
| <span class="status-dot red"></span> | Statisch | Call | Auf dem Kanal wird ein Rufzeichen (Call) gesendet. |
| <span class="status-dot blink__white-red"></span> | Blinkend | Alert Call | Auf dem Kanal wird ein Alarm-Rufzeichen gesendet. |
| <span class="status-dot blink__red-yellow"></span> | Blinkend | Cue Attention | Der Kanal empfängt oder sendet die erste Stufe (Attention) des Lichtzeichens (Cue). |
| <span class="status-dot orange"></span> | Statisch | Cue GO | Der Kanal empfängt oder sendet die zweite Stufe (Ready) des Lichtzeichens. |
| <span class="status-dot green"></span> | Statisch | Cue GO | Der Kanal empfängt oder sendet die dritte Stufe (GO) des Lichtzeichens. |

!!! tip ""
    :material-lightbulb-outline: **Tip:** Es ist möglich die Statusfarben eines Green-GO Systems [anzupassen](https://manual.greengoconnect.com/en/software/views/config/#config-colors)!

### Kanal-UI

Jede Green-GO Sprechstelle verfügt über mindestens einen Display welcher Kanalinformationen darstellt.

Die Anzahl der Kanäle im direkten Zugriff variiert je nach Gerätetyp oder -konfiguration. Grundsätzlich bleibt die Struktur aber über alle Möglichkeiten gleich:

<div class="svg-container svg-center width-80" data-filename="../assets/images/mcx-display-ui-channel_new"></div>

Channel Status
:  Das rote `X` zeigt an, dass die lokale [Green-GO Engine](../glossary.md#green-go-engine) kein Gerät oder User als für den Kanal finden kann.

Channel ID
:  Dies zeigt die ID des Kanals an. Grundsätzlich hat ein Green-GO User Zugriff auf die Kanäle 1 bis 32.

Display Name
:  Der Name oder Anzeigename des Kanalziels ([User](../glossary.md#user) oder [Gruppe](../glossary.md#group)).

Channel Color
:  Die Kanalfarbe kann verwendet werden, um zwischen Kommunikationszielen zu unterscheiden. Die Farbe wird durch das Kanalziel selbst ([User](../glossary.md#user) oder [Gruppe](../glossary.md#group)) definiert.

Channel Volume
:  Die aktuelle Lautstärke des Kanals. Ein nicht gefüllter balken repräsentiert einen stumm geschalteten Kanal.

!!! tip ""
    :material-lightbulb-outline: **Tip:** Die Benutzeroberfläche einer Sprechstelle kann konfiguriert werden. Bitte lese die [Geräte-Dokumentation](https://manual.greengoconnect.com/en/devices/) der entsprechenden Sprechstelle, um mehr zu erfahren.

## Kanal Bedienung

### Kanal Ansprechen (Talk)

Um einen Kanal anzusprechen, muss die entsprechende ++button++ gedrückt werden. Dies aktiviert das Mikrofon für den Kanal und ändert den Kanalstatus auf Talk.

Ein _offener_ Kanal wird von der Status-LED durch ein <span class="status-dot green"></span> grünes leuchten signalisiert.

=== "BPX & WBPX belt packs"

    <div class="svg-container svg-center width-60" data-filename="../assets/images/bpx-use-talk"></div>

=== "MCX, MCXD & WPX stations"

    <div class="svg-container svg-center width-70" data-filename="../assets/images/mcx-use-talk"></div>

Mit den _werkseitigen Standardeinstellungen_, sind zwei [Funktionen] (`Latch/Momentary`) mit einer ++button++ verknüpft:

1. **Press and hold:** Will act as _push-to-talk_ and will close the channel on button release. ([`Momentary`](../glossary.md#momentary))
2. **Short button press:** Will _latch_ the channel to open on the first press. The second button press will close the channel. ([`Latch`](../glossary.md#latch))

The function of the button-press can be configured in the channel settings, either on the [device itself](devices.md#channel-assignments-configuration) or with the help of the [Green-GO Control](../software/tree/

### Audio Empfangen (VOX)

If voice communication is received, the channel status will change to <span class="status-dot yellow"></span> yellow. The device will transmit audio with the set channel volume to the active audio output.

=== "BPX & WBPX belt packs"

    <div class="svg-container svg-center width-60" data-filename="../assets/images/bpx-use-listen">
      <noscript>
        <p>Bitte schalte Javascript ein um das Bild zu laden.</p>
        <p>BPX: Wie man Audio empfängt.</p>
      </noscript>
    </div>

=== "MCX, MCXD & WPX stations"

    <div class="svg-container svg-center width-70" data-filename="../assets/images/mcx-use-listen"></div>

A channel will stay <span class="status-dot yellow"></span> active for 5 seconds after the last audio signal was received to give the user time to identify the receiving channel and use the [answer function](#answering-communications). This behavior can be configured by adjusting the property [`Active Time`](../devices/mcx.md#active-time) in the user's settings.

<div class="svg-container svg-inline width-20" data-filename="../assets/images/bpx-popup-direct"></div>

Should a user receive direct communication from another user that isn't configured on any of the 32 channels, the communication will be transmitted on an **extra 33rd channel**. A [configurable pop-up](../devices/mcx.md#popup) will inform the user about the sender's information.

### Gespräche Beantworten

Green-GO allows the user to answer any incoming <span class="status-dot yellow"></span> voice communication with the press of one button. By default, the answer function will reply to the channel that received a communication **last**. However, the answer function can be configured to respond to **all currently active** incoming <span class="status-dot yellow"></span> voice communications.

!!! tip ""
    :material-lightbulb-outline: **Tip:** The property [`Active Time`](../devices/mcx.md#active-time) will influence the duration of a channel staying active and being available for the answer function after communication has been received.

=== "BPX & WBPX belt packs"

    <div class="svg-container svg-inline width-25" data-filename="../assets/images/bpx_click2"></div>
    The _click action_ of the ++bpx-enc1++ and ++bpx-enc2++ is assigned to the answer/reply function. Pulling one of the encoders up towards the display while receiving any communication will reply to the last active channel.

    <div class="svg-container svg-inline-right width-20" data-filename="../assets/images/bpx-status-answer"></div>
    When one of the encoders is pulled, the [status screen](#) of the device displays the channel(s) that are currently activated by the answer function.

=== "MCX & MCXD stations"

    <div class="svg-container svg-inline width-50" data-filename="../assets/images/mcx-functions-answerreply"></div>
    The answer function must be [assigned](../devices/mcx.md#configuring-the-user-interface) to the user interface to be available. When available, the ++button++ of the answer function will allow a [reply](../glossary.md#reply) to the active channel(s), the ++touchscreen++ section will clear the current answer cue.
    
    When the function is inactive, it will display the local user of the device.

=== "WPX wall panels"

    <div class="svg-container svg-inline width-50" data-filename="../assets/images/wpx-functions-answerreply_2"></div>
    The answer function must be [assigned](../devices/mcx.md#configuring-the-user-interface) to the user interface to be available. When available, the ++button++ of the answer function will allow a [reply](../glossary.md#reply) to the active channel(s), the ++touchscreen++ section will clear the current answer cue.
    
    When the function is inactive, it will display the local user of the device.

### Kanal Lautstärke

It's possible to adjust the volume for each channel, creating your perfect channel mix.

!!! note ""
    :material-chat-alert-outline: **Notice:** The visual level indicator of a channel's volume isn't linear. The lower parts of the available range will show no visual difference - this gives the user a better visual feedback in the level range that actually matters.

=== "BPX & WBPX belt packs"

    A Green-GO belt pack provides direct access to the first 2 - 4 channels of the linked user, depending on the configured [UI mode](../devices/bpx.md#ui-modes).
    
    <div class="svg-container svg-center width-60" data-filename="../assets/images/bpx-use-volume-channel"></div>
    The volume for these channels can be easily adjusted by pressing one of the channel ++bpx-btns++ together with rotating either the ++bpx-enc1++ or ++bpx-enc2++.

    The volume meter below a channel's name will display the current volume setting.

    !!! warning ""
        :material-alert-outline: **Warning:** Adjusting the channel volume in direct access will always open the channel for voice communication.

    !!! tip ""
        :material-lightbulb-outline: **Tip:** The rest of the channels can be accessed and adjusted through the [extended channel view](../devices/bpx.md#extended-channel-view)

=== "MCX, MCXD & WPX stations"

    <div class="svg-container svg-center width-70" data-filename="../assets/images/mcx-use-volume-channel"></div>
    The [listen screen mode](../devices/mcx.md#operation-mode-switches) must be activated to adjust a channel's volume on an MCX, MCXD, or WPX station. When active, the ++touchscreen++ section for the channel and the ++encoder++ rotation will raise or lower the channel volume. The _volume meter_ on top of the [channel UI](#user-interface) will display the current volume setting.

#### Kanal Stumm Schalten

=== "BPX & WBPX belt packs"

    <div class="svg-container svg-center width-60" data-filename="../assets/images/bpx-use-mute"></div>

    <div class="svg-container svg-inline-right width-25" data-filename="../assets/images/bpx_click1"></div>
    To mute one of the first 2 - 4 channels of a user, the user needs to press one of the available channel ++bpx-btns++ and pull either the ++bpx-enc1++ or ++bpx-enc2++ towards the display.

    !!! warning ""
        :material-alert-outline: **Warning:** Adjusting the channel volume in direct access will always open the channel for voice communication.

    !!! tip ""
        :material-lightbulb-outline: **Tip:** The rest of the channels can be accessed and adjusted through the [Extended Channel View](#)<!-- Link needs to be set when device manual is ready -->.

=== "MCX, MCXD & WPX stations"

    <div class="svg-container svg-center width-70" data-filename="../assets/images/mcx-functions-mode-listen"></div>
    With the [listen screen mode](../devices/mcx.md#operation-mode-switches) enabled, a channel's ++touchscreen++ section can be tapped to mute or unmute the channel.

The volume meter on top of the [channel UI](#user-interface) will become hollow as soon as the channel is muted and return to the previous set volume when unmuted. The previous set channel volume will be stored and recalled upon muting or unmuting, respectively.

### Kanal Rufen (Call)

Green-GO supports call signs with an alert signal on each of the 32 user channels. Each channel can be configured to enable or disable the sending and receiving of call signals.

Should a channel receive or send a call signal, the channel status will change to <span class="status-dot red"></span> red and, after a short while, to blinking <span class="status-dot blink__white-red"></span> red and white, signaling the [alert call](../glossary.md#alert-call).

=== "BPX & WBPX belt packs"

    Green-GO belt packs feature several [user interface presets](#) that influence how a call sign can be sent to a channel. To find more about the available user interface presets, check out the corresponding device manual.

    | 2-Channel Mode {: .three-col} | 3-Channel Mode {: .three-col} | Extended Channel View {: .three-col} |
    |:-|:-|:-|
    | <div class="svg-container svg-center" data-filename="../assets/images/bpx_call-2ch"></div> | <div class="svg-container svg-center" data-filename="../assets/images/bpx_call-3ch"></div> | <div class="svg-container svg-center" data-filename="../assets/images/bpx_call-ext"></div> |
    | A belt pack using the [2-channel UI-mode](../devices/bpx.md#ui-modes) will feature direct access to call signs on channels 1 and 2 on <br>++bpx-btn3++ or ++bpx-btn4++, respectively. | The [3-channel UI-mode](../devices/bpx.md#ui-modes) features access to the call function on ++bpx-btn4++ as soon as any of the three first channels are open. | The [Extended Channel View](../devices/bpx.md#extended-channel-view) allows access to all 32 user channels. A call sign can be sent to the selected channel by pressing ++bpx-btn2++. |

=== "MCX, MCXD & WPX stations"

     <div class="svg-container svg-center width-60" data-filename="../assets/images/mcx-functions-mode-call"></div>
    The [call screen mode](../devices/mcx.md#operation-mode-switches) needs to be active on the device to enable the **sending** of call signals. When activated, the touch on a channel's ++touchscreen++ section will send a call sign to the assigned target(s).

    !!! tip ""
        :material-lightbulb-outline: **Tip:** It is possible to send a call sign with the press of a channel's ++button++. The property [`Button`](../devices/mcx.md#button) defines if the buttons should change their function to the active [screen mode](../devices/mcx.md#screen-function) or always open a channel for voice communication.

### Kanal Lichtzeichen (Cue)

 <div class="svg-container svg-inline-right width-50" data-filename="../assets/images/mcx-functions-mode-cue"></div>
A cue signal is sent by tapping the channel's ++touchscreen++ section while using the [cue screen mode](../devices/mcx.md#operation-mode-switches) on an MCX rack or MCXD desktop station. The first tap will initiate an <span class="status-dot blink__red-yellow"></span> attention cue. A second tap on the ++touchscreen++ will directly send the <span class="status-dot green"></span> GO cue and clear the channel after the local [`Cue Timeout`](../devices/mcx.md#cue-timeout) reaches 0.

!!! tip ""
    :material-lightbulb-outline: **Tip:** It is possible to send a cue sign with the press of the channel's ++button++. The option [`Button`](../devices/mcx.md#button) defines if the buttons function should follow the active screen mode ([listen](../glossary.md#listen), [call](../glossary.md#call), [cue](../glossary.md#cue)) or always open a channel for voice communication.

### Receiving and answering a cue sign

Incoming cue signs will be displayed with a pop-up on the screen. Additionally, the channel status will change its [color](#status-colors) according to the cue stage.<!-- The pop-ups can be easily cleared by pressing any ++button++ on the device.-->

=== "BPX & WBPX belt packs"

     <div class="svg-container svg-inline width-25" data-filename="../assets/images/bpx_click2"></div>
    Answering an incoming <span class="status-dot blink__red-yellow"></span> attention cue is the same as [answering any communication](#answering-communications): Pulling one of the encoders up towards the display. 
    
    <!--The pop-ups showing the status and sender information of the signal can be cleared by pressing any of the four ++bpx-btns++ on the front of the device.-->

=== "MCX & MCXD stations"

    | Answer incoming Attention Cue {: .two-col} | Incoming Hold or Go Cues {: .two-col} |
    | --- | --- |
    | <div class="svg-container svg-center" data-filename="../assets/images/mcx_functions_cue-rcv_attention"></div> | <div class="svg-container svg-center" data-filename="../assets/images/mcx_functions_cue-rcv_hold_go"></div> |
    | An incoming `Attention` cue will be displayed with its sender information in a pop-up on the third touchscreen. The Setup or Shift buttons can be pressed to answer incoming `Attention` cues. | An incoming `Ready` or `GO` cue will be displayed in a pop-up together with the sender's information on the third touchscreen. <!--The pop-up can be cleared by pressing any ++button++ of the device.--> |

<!-- === "WPX wall panel"

    {==I'm honestly lost on how the answer function works on the WPX. Was it pushing the encoder while receiving a communication?==} -->

## Setup Menü

The setup menu allows for persistent changes on the device and user configuration that can be [synced back](../software/tree/devices.md#devices-out-of-sync) to the main configuration with the help of the Green-GO Control software. The setup menu can be accessed on each device and provides access to almost all settings and options.

### User stations

=== "BPX & WBPX belt packs"

    The [BPX](../devices/bpx.md) and [WBPX](../devices/wbpx.md) belt packs feature two methods to access the setup menu:

    | Method A {: .two-col} | Method B {: .two-col} |
    | :- | :- |
    | <div class="svg-container svg-center" data-filename="../assets/images/bpx_setup1"></div> | <div class="svg-container svg-center" data-filename="../assets/images/bpx-setup-method_b"></div> |
    | Pull the ++bpx-enc1+bpx-enc2++ up towards the display. | Press ++bpx-btn1+bpx-btn3++ after pulling and holding either the ++bpx-enc1++ or ++bpx-enc2++ up towards the display. |

=== "MCX & MCXD stations"

     <div class="svg-container svg-inline width-50" data-filename="../assets/images/mcx_setup"></div>
    The [MCX rack](../devices/mcx.md) and [MCXD desktop](../devices/mcxd.md) stations provide easy access to the setup menu using a dedicated ++setup++ button and navigated with the help of the encoder right next to it.

=== "WPX wall panel"

     <div class="svg-container svg-inline width-50" data-filename="../assets/images/wpx_setup"></div>
    The setup menu on the [WPX wall panel](../devices/wpx.md) is hidden behind the press of the ++encoder++. When pressed, the 6th ++touchscreen++ section on the bottom right will provide access to the setup menu if tapped.

<!-- === "MCXEXT & MCXDEXT extensions"

     <div class="svg-container svg-center width-40" data-filename="../assets/images/mcxext_setup"></div>
    The setup menu on the [MCXEXT rack](../devices/mcxext.md) or [MCXDEXT desktop](../devices/mcxext.md) channel extensions is only available if **not connected** to a master [MCX rack](../devices/mcx.md) or [MCXD desktop](../devices/mcxd.md) station. It can be accessed with the last ++button++ on the bottom-right of the 4th display.<br>
    The two buttons above can be used to navigate the setup menu. -->

### Interfaces

=== "19" Rack-Interfaces"

     <div class="svg-container svg-inline width-50" data-filename="../assets/images/interface_tft-setup"></div>
    Pressing the ++encoder++ will bring up the setup menu on all 19" rack Green-GO interfaces like the [audio InterfaceX](../devices/interfacex.md), [Q4WR quad 4-wire interface](../devices/q4wr.md),  and many more.<br>
    The setup menu is navigated by scrolling or clicking the ++encoder++.

=== "1CH Interfaces"

     <div class="svg-container svg-inline width-50" data-filename="../assets/images/1ch_setup"></div>
    Pressing ++bpx-btn1+bpx-btn2++ at the same time brings up the setup menu on one-channel interfaces like the [RDX radio interface](../devices/rdx.md) or [SI4WR 4-wire interface](../devices/si4wr.md).
    
    In the setup menu, ++bpx-btn3++ and ++bpx-btn4++ go up and down. ++bpx-btn1++ affirms a selection, and ++bpx-btn2++ exits the current menu or selection.

#### Accessories

The limited user interface on accessories like the WAA wireless antenna or the BCN beacon light only allows for little functionality.

Please refer to the device documentation for a complete description of the provided functionality.