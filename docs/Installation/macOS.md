---
title: macOS
description: In diesem Artikel erklären wir dir Schritt für Schritt, wie du die Deutsch-Patches auf macOS-Systemen installieren kannst.
tags:
  - macOS
---

# Installation auf Mac OS

In diesem Artikel erklären wir dir Schritt für Schritt, wie du die Deutsch-Patches auf macOS-Systemen installieren kannst.

Zum aktuellen Zeitpunkt ist unser Installer Jackbox Utility leider noch nicht für macOS verfügbar. Daher ist es derzeit nötig, die Patches manuell zu installieren.

!!! warning ""
    Bitte befolge diese Anleitung ganz genau und überspringe keinen Schritt. Andernfalls kann es zu Fehlern wie Blackscreens in den Spielen kommen.

## :blue_book: Anleitung

Es gibt zwei Möglichkeiten, wie du die Deutsch-Patches für die Spiele von Jackbox Games installieren kannst.
Methode 1 erfordert die Installation von **WinZip**. Dieses Programm bietet eine mehr als 30-tägige kostenlose Testversion, ist danach aber kostenpflichtig. Methode 2 erfordert die Verwendung des **Terminals** (Kommandozeile).

Wenn du noch keine Erfahrung mit der Kommandozeile hast, empfehlen wir die **WinZip**-Methode.

=== "WinZip"
    1. Lade dir [**WinZip**](https://www.winzip.com/en/mac/) herunter und installiere das Programm (30 tägige, kostenlose Testphase)
    2. Lade dir die ZIP-Datei für das entsprechende Party Pack [**hier**](https://jackboxpatch.de/Manual-Download.html#download) herunter.
    3. Öffne in einem zweiten Fenster den Ordner mit deinem Spiel im Finder.
    !!! info "So findest du den Ordner über Steam"
        1. Rechtsklicke auf das Party Pack Spiel in deiner Steam-Bibliothek und klicke auf "Verwalten"  
        2. Klicke dann auf "Lokale Dateien durchsuchen". Es öffnet sich der Dateipfad im Finder  
    4. Rechtsklick auf die App und "**Paketinhalt anzeigen**" auswählen
    5. Dort in den Ordner `Contents/Resources/macos` navigieren, die ZIP-Datei vom Patch mit **WinZip** öffnen, und alle Dateien in den Ordner des Spieleverzeichnis via Drag and Drop ziehen.

    !!! tip "Video-Tutorial"
        Die spanische Jackbox-Community hat [hier](https://youtu.be/RTb0_aFtLLY) ein ausführliches Video hochgeladen, welches diese Installations-Methode genauer behandelt.

=== "Terminal"
    1. Lade dir die ZIP-Datei für das entsprechende Party Pack [**hier**](https://jackboxpatch.de/Manual-Download.html#download) herunter und extrahiere es in den Downloads-Ordner. Stelle sicher, dass es in einem Ordner mit demselben Namen wie der Patch extrahiert wurde.
    2. Greife mit dem Terminal auf das Verzeichnis zu, in dem sich die Packs befinden
    ```
    cd /Users/<username>/Library/Application Support/Steam/steamapps/common/<package name>
    ```
    3. Greife auf die Ordner des zu übersetzenden Spiels zu (Beispielsweise Party Pack 3)
    ```
    cd The Jackbox Party Pack 3/The Jackbox Party Pack 3.app/Contents/MacOS
    ```

    4. Installiere die Patches mit dem `ditto` Befehl. Wenn die Dateien der Übersetzungen sich im "Downloads" Ordner befinden, muss folgender Befehl verwendet werden:
    ```
    ditto ~/Downloads/The-Jackbox-Party-Pack-3-German-macOS
    ```
    (Der genaue Ordnername kann abweichen)

    !!! tip "Video-Tutorial"
        Die spanische Jackbox-Community hat [hier](https://drive.google.com/file/d/1cqZ2mi9CKJwuc3pitR59f3jDASlKAvRF/view) ein ausführliches Video hochgeladen, welches diese Installations-Methode genauer behandelt.

!!! warning "Bekannter Fehler"
    Derzeit erreichen uns Meldungen, dass einige Patches nicht für alle macOS-Systeme funktionieren. Da andere macOS-Nutzer keine Probleme feststellen konnten, vermuten wir, dass es bei unterschiedlichen Modellen zu verschiedenen Ergebnissen führt. Wir sind gerade noch dabei, weitere Informationen zu sammeln. Falls du bei den Tests und der Entwicklung beitragen möchtest, trete doch gerne unserem [Discord-Server](https://discord.gg/vGcu9HWde4) bei.