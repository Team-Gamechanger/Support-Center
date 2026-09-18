---
title: Deinstallation (Steam)
description: In diesem Artikel erklären wir dir Schritt für Schritt, wie du die Deutsch-Patches auf Steam deinstallieren kannst.
tags:
  - Windows
  - Linux / Steam Deck
  - macOS
---

# Deinstallation der Deutsch-Patches auf Steam

In diesem Artikel erklären wir dir Schritt für Schritt, wie du die Deutsch-Patches auf Steam deinstallieren kannst.

!!! info ""
    Für ein über Epic Games installiertes Spiel findest du hier die [**Anleitung**](../Deinstallation/EpicGames.md).

## :blue_book: Anleitung

!!! warning "Sonderfall: Trivia Murder Party 3"
    Bei **Trivia Murder Party 3** reicht die Steam-Dateiprüfung allein nicht aus. Steam stellt zwar veränderte Originaldateien wieder her, entfernt aber nicht alle Dateien, die durch den Deutsch-Patch neu hinzugefügt wurden.

    1. Beende **Trivia Murder Party 3** vollständig.
    2. Öffne den Ordner des Spiels.
    3. Starte die mitgelieferte Datei `Deutschpatch-deinstallieren.cmd`.
    4. Bestätige die Deinstallation mit **J**.

    Das Skript entfernt die zusätzlichen Patchdateien und startet danach automatisch die Steam-Dateiprüfung. Nach erfolgreicher Deinstallation löscht sich das Skript selbst. Die folgenden Schritte musst du für **Trivia Murder Party 3** daher nicht zusätzlich ausführen.

So deinstallierst du die Deutsch-Patches auf Steam:

1. Rechtsklicke auf das entsprechende Spiel in deiner Steam-Bibliothek.
2. Klicke auf **Eigenschaften**.
3. Klicke unter dem Tab **Lokale Dateien** auf “**Spieldateien auf Fehler überprüfen …**”.

!!! success ""
    Steam wird anschließend alle modifizierten Dateien entfernen und die Originaldateien neu herunterladen.

## :clipboard: Weitere Informationen

In unserem Support-Center erfährst du mehr über die Funktionen und Features von Jackbox Utility.
