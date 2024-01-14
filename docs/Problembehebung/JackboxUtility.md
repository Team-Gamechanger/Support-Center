---
title: Jackbox Utility Problembehebung
description: In diesem Artikel erklären wir dir, was die häufigsten Probleme mit Jackbox Utility sind, und wie du sie beheben kannst.
tags:
  - Windows
  - Linux / Steam Deck
---

In diesem Artikel erklären wir dir, was die häufigsten Probleme mit Jackbox Utility sind, und wie du sie beheben kannst.

## Ich sehe keinen Button, um die Patches zu installieren
Den blauen Button **Patche ein Spiel** findest du im Hauptmenü von Jackbox Utility.
!!! info ""
    Auf Wunsch startet Jackbox Utility bei einigen Nutzern immer direkt im **Suche ein Spiel**-Menü. Von dort erreicht man das Hauptmenü durch Klicken auf den Pfeil oben links.

Wenn dir dieser Button nicht angezeigt wird, befindest du dich mit hoher Wahrscheinlichkeit noch auf dem englischen Server. So wechselst du deinen Server:

1. Klicke auf **Settings**
2. Klicke links auf **Server Information**
3. Klicke auf **Change Server**
4. Wähle **Jackbox auf Deutsch**

!!! success "Toll gemacht!"
    Nun hast du dich mit dem deutschsprachigen Server verbunden. Unter **Patche ein Spiel** kannst du nun Übersetzungen für alle deine Spiele herunterladen und installieren.

!!! info "Warum automatisch der englische Server eingestellt ist"
    Jackbox Utility verfügt über ein automatisches Erkennungssystem, welches den Server beim ersten Start basierend auf deiner Sprache auswählt. Dieses System ist zum aktuellen Zeitpunkt noch nicht auf Linux verfügbar, sodass dort aktuell noch standardmäßig der englische Server ausgewählt ist.


## Ein Spiel wird mir in Jackbox Utility nicht angezeigt
Jackbox Utility überprüft beim Start automatisch, welche Spiele sich in deinem Besitz befinden. Wenn du ein Spiel frisch gekauft hast, musst du die automatische Erkennung erneut auslösen. Dazu kannst du:

- Jackbox Utility **neu starten**
- In den **Optionen** auf **Installierte Spiele automatisch erkennen** klicken

Falls die Spiele nicht automatisch erkannt werden, kannst du sie auch manuell hinzufügen.

!!! warning ""
    Wir sind streng gegen die Installation und Verbreitung von Raubkopien oder illegal installierter Spiele. Jackbox Utility erkennt nur legitim über Steam und Epic Games erworbene Spiele.

## Wenn ich Jackbox Utility starte, erscheint der Fehler *VCRUNTIME140_1.dll kann nicht gefunden werden*.
Bitte installiere [**Microsoft Visual C++ Redistributable**](https://learn.microsoft.com/de-de/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022)