---
title: Probleme mit Jackbox Utility
tags:
  - Windows
  - macOS
  - Linux / Steam Deck
---

# Probleme mit Jackbox Utility

## Ich sehe keinen Button, um die Patches zu installieren

Den Button **Patche ein Spiel** findest du im Hauptmenü. Startet Utility direkt in **Suche ein Spiel**, klicke auf den Pfeil oben links.

Fehlt der Button weiterhin, prüfe den Server:

1. Klicke auf **Settings**.
2. Öffne **Server Information → Change Server**.
3. Wähle **Jackbox auf Deutsch**.

Danach sollten die für den deutschen Server angebotenen Patches sichtbar sein. Verlasse dich insbesondere unter Linux nicht darauf, dass die Serverauswahl automatisch erfolgt.

## Ein Spiel wird mir in Jackbox Utility nicht angezeigt

Installiere das gekaufte Spiel zuerst über deinen Store. Starte anschließend Utility neu oder klicke in den **Optionen** auf **Installierte Spiele automatisch erkennen**. Falls die Erkennung scheitert, kannst du das installierte Spiel in Utility manuell hinzufügen.

Ein erkanntes Spiel hat nicht automatisch einen passenden Deutsch-Patch. Prüfe auch [Store und Patchverfügbarkeit](https://jackboxpatch.de/downloads). Wir unterstützen keine Raubkopien.

<span id="verbindung"></span>

## Jackbox Utility kann sich nicht mit dem deutschsprachigen Server verbinden.

1. Prüfe, ob du die [für dein System angebotene Utility-Version](../Installation/JackboxUtility.md) verwendest.
2. Starte Utility neu und kontrolliere die Serverauswahl.
3. Versuche ein anderes Netzwerk, beispielsweise einen Handy-Hotspot. Funktioniert es dort, liegt die Ursache möglicherweise im bisherigen Netzwerk, VPN, Proxy oder HTTPS-Filter.
4. Sichere die [Log-Datei](#wo-finde-ich-die-log-datei-von-jackbox-utility), bevor du Einstellungen zurücksetzt.

Bleibt das Problem bestehen, [melde uns den Fehler](../Wissenswertes/BugReport.md). Ein Datenreset ist ein weiterer Schritt für Windows, aber keine Voraussetzung für eine Meldung.

<span id="handshake"></span>

## Der Fehler "HandshakeException: Connection terminated during handshake" wird angezeigt

Die HTTPS-Verbindung wird beendet, bevor der Verbindungsaufbau abgeschlossen ist. Teste Utility über ein anderes Netzwerk, etwa einen Handy-Hotspot. Funktioniert es dort, prüfe die Einstellungen deines Netzwerks, VPNs, Proxys oder Sicherheitsprogramms. Teile bei einer [Fehlermeldung](../Wissenswertes/BugReport.md) die genaue Ausgabe und das Ergebnis dieses Tests mit.

<span id="startprobleme"></span>

## Jackbox Utility startet nicht.

- **Windows:** Starte `JackboxUtility.exe` direkt aus dem entpackten Ordner statt über eine Verknüpfung. Falls vorhanden, kannst du auch `app/jackbox_patcher.exe` direkt starten.
- **Linux / Steam Deck:** Prüfe die [Ausführungsberechtigung](../Installation/JackboxUtility.md#linux-steam-deck).
- **macOS:** Nutze die [macOS-Fehlerhilfe](MacOSFehlermeldung.md).

Wenn der Updater das Problem ist, kannst du für Windows oder Linux die [eigenständige Utility-Version](https://github.com/JackboxUtility/JackboxUtility/releases/latest) verwenden. Diese musst du selbst aktualisieren. Lade nur das Paket für dein Betriebssystem herunter.

## Wenn ich Jackbox Utility starte, erscheint der Fehler *VCRUNTIME140_1.dll kann nicht gefunden werden*.

Installiere unter Windows die passende [Microsoft Visual C++ Redistributable](https://learn.microsoft.com/de-de/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022) von Microsoft und starte Utility erneut.

## Wo finde ich die Log-Datei von Jackbox Utility?

Öffne unter Windows mit **Windows + R** den folgenden Pfad und sichere die Datei `log.txt`:

```text
%AppData%\JackboxUtility\JackboxUtility\Logs
```

<span id="wie-setze-ich-meine-jackbox-utility-speicherdaten-zuruck"></span>

## Wie setze ich meine Jackbox Utility Speicherdaten unter Windows zurück?

Ein Reset setzt Utility-Einstellungen und gespeicherte Zuordnungen zurück. Er deinstalliert keine Patches aus deinen Spielen.

1. Beende Utility vollständig und sichere die Log-Datei.
2. Öffne mit **Windows + R** `%AppData%\JackboxUtility`.
3. Benenne den darin enthaltenen Ordner `JackboxUtility` in `JackboxUtility-Sicherung` um. Verwende einen anderen Sicherungsnamen, falls dieser bereits existiert.
4. Starte Utility und wähle den deutschen Server erneut. Lass die Spiele neu erkennen.

Durch das Umbenennen behältst du eine Sicherung. Wenn der Ordner nicht existiert, lösche keine ähnlich benannten Ordner, sondern [frage bei uns nach](../Wissenswertes/BugReport.md).
