---
title: Das Spiel startet nicht
tags:
  - Windows
  - macOS
  - Linux / Steam Deck
---

# Das Spiel startet nicht

Wenn ein Spiel nach der Patchinstallation nicht mehr startet, können Spielversion und Patch nicht zusammenpassen oder Dateien unvollständig installiert worden sein. Für die ersten Schritte musst du das Spiel nicht öffnen können.

## Erste Schritte

1. Beende Spiel und Jackbox Utility vollständig.
2. Installiere verfügbare Spielupdates in Steam beziehungsweise Epic Games.
3. Prüfe, ob du den [passenden Patch für System und Store](https://jackboxpatch.de/downloads) verwendet hast.
4. Installiere den [aktuellen Patch](../Installation/aktualisieren.md) und warte auf den Abschluss.
5. Starte das Spiel erneut.

Unter macOS findest du zusätzliche Hinweise in der [macOS-Fehlerhilfe](MacOSFehlermeldung.md). Bei Trivia Murder Party 3 beachte die [besonderen Einrichtungsschritte](../Spiele/trivia-murder-party-3.md).

## So überprüfst du, ob der Patch mit dem Spiel kompatibel ist:

**Nur wenn du das Hauptmenü noch erreichst:** Vergleiche die angezeigte Build-Nummer mit der angebotenen Version für dasselbe Spiel. Die [Anleitung zum Versionsvergleich](../Installation/aktualisieren.md#build-nummer) erklärt das Schema **[Build des Spiels].[Build des Patches]-DE**.

Wenn das Spiel überhaupt nicht startet, überspringe diesen Schritt.

## Ohne Patch testen

[Setze das Spiel über deinen Store zurück](../Deinstallation/index.md) und beachte besondere Hinweise zu zusätzlich installierten Dateien. Teste anschließend das Spiel, bevor du einen Patch erneut installierst. Notiere für eine Fehlermeldung, ob es auch ohne Patch nicht startet.

## So kannst du die Erstellung von Log-Dateien auf Steam aktivieren

Log-Dateien können uns helfen, das Problem genauer zu untersuchen. Bei Spielen, die diese Jackbox-Startparameter unterstützen:

1. Rechtsklicke das Spiel in deiner Steam-Bibliothek und öffne **Eigenschaften**.
2. Ergänze unter **Allgemein → Startoptionen** folgende Parameter. Bewahre vorhandene Startoptionen auf.

```text
-jbg.config debug=true logging=true dev-console=true logFile=log.txt
```

Versuche das Spiel erneut zu starten. Wenn eine `log.txt` im Spielverzeichnis erstellt wird, kannst du sie deiner [Fehlermeldung](../Wissenswertes/BugReport.md) beifügen. Entsteht keine Datei, melde das Problem trotzdem. Entferne die ergänzten Parameter nach der Diagnose wieder.
