---
title: "Trivia Murder Party 3 – Besonderheiten"
description: "Richte deutsche Quizfragen ein und entferne den Deutsch-Patch für Trivia Murder Party 3 vollständig."
tags:
  - Windows
---

# Trivia Murder Party 3 – Besonderheiten

Bei diesem Spiel werden die übersetzten Quizfragen über unseren deutschen Online-Content-Service geladen. Die folgenden Skript-Schritte gelten für den **Windows-Patch**. Beende das Spiel vollständig, bevor du ein Skript ausführst.

## Installation { #installation }

Wir empfehlen die [Installation mit Jackbox Utility](../Installation/JackboxUtility.md#windows). Prüfe zuvor, ob der [passende Patch für deinen Store](https://jackboxpatch.de/downloads) angeboten wird.

Bei der **manuellen Installation unter Windows**:

1. Entpacke den Patch wie in der [Windows-Anleitung](../Installation/Windows.md) beschrieben in den Spielordner.
2. Öffne diesen Ordner und starte die mitgelieferte Datei `Deutschpatch-installieren.cmd`.
3. Warte auf den Abschluss und starte das Spiel erneut.

Das Skript richtet die Verbindung mit unserem deutschen Online-Content-Service ein. Ohne diesen Schritt können die Quizfragen trotz deutscher Menüs auf Englisch bleiben.

## Die Quizfragen sind auf Englisch { #englische-quizfragen }

Wenn Menüs und Untertitel auf Deutsch sind, aber die Quizfragen auf Englisch erscheinen, führe die mitgelieferte `Deutschpatch-installieren.cmd` bei beendetem Spiel aus. Verwende die Datei aus deinem aktuellen Patch, nicht aus einem älteren Download.

Zeigt das Skript einen Fehler an, aktualisiere zuerst das Spiel und installiere anschließend den aktuellen passenden Deutsch-Patch erneut. Bleibt der Fehler bestehen, [melde uns die genaue Ausgabe](../Wissenswertes/BugReport.md).

## Nach einem Spielupdate { #nach-einem-update }

Ein Update kann die Einrichtung überschreiben. Wenn die Quizfragen danach wieder auf Englisch erscheinen, beende das Spiel und führe `Deutschpatch-installieren.cmd` erneut aus. Prüfe außerdem, ob ein [Patchupdate](../Installation/aktualisieren.md) angeboten wird.

## Deinstallation unter Windows / Steam { #deinstallation }

Die Steam-Dateiprüfung allein entfernt nicht alle zusätzlich installierten Patchdateien.

1. Beende **Trivia Murder Party 3** vollständig.
2. Öffne den Spielordner und starte `Deutschpatch-deinstallieren.cmd`.
3. Bestätige mit **J**.
4. Warte, bis das Skript und die automatisch gestartete Steam-Dateiprüfung abgeschlossen sind.

Das mitgelieferte Skript entfernt die zusätzlichen Patchdateien und löscht sich nach erfolgreicher Deinstallation selbst. Eine weitere manuelle Steam-Dateiprüfung ist dann nicht nötig. Fehlt das Skript oder meldet es einen Fehler, [frage bei uns nach](../Wissenswertes/BugReport.md).
