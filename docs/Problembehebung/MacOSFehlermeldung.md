---
title: Das Spiel funktioniert auf macOS nicht richtig
tags:
  - macOS
---

# Das Spiel funktioniert auf macOS nicht richtig

Prüfe zuerst, ob du den richtigen Patch für dein Spiel, deinen Store und macOS verwendet hast. Die Dateistruktur kann von Windows und Linux abweichen. Beende das Spiel vor Änderungen an seiner Installation.

Nutze die [Utility-Anleitung für macOS](../Installation/JackboxUtility.md#macos) oder die [manuelle Anleitung](../Installation/macOS.md).

## Bekannte Fehlerursachen

### Verwendung vom vorinstallierten Standardprogramm zum Entpacken des Patches

Achte darauf, dass beim Kopieren die benötigten Unterordner zusammengeführt werden und keine vorhandenen Spielordner versehentlich vollständig ersetzt werden. Die [manuelle Anleitung](../Installation/macOS.md) beschreibt die Methoden mit WinZip und dem Terminal-Befehl `ditto`.

### Entpacken des Patches in das falsche Unterverzeichnis

Die Ordnerstruktur des Patchinhalts muss mit der des Spiels übereinstimmen. Bei den in der manuellen Anleitung beschriebenen Party Packs liegt das Ziel innerhalb des App-Pakets unter `Contents/Resources/macos`. Prüfe beispielsweise, dass der `games`-Ordner auf beiden Ebenen zusammenpasst.

### Die Windows-Version wurde heruntergeladen

Manche Patches benötigen eine eigene macOS-Ausgabe. Prüfe auf der [Download-Seite](https://jackboxpatch.de/downloads), welches Paket für dein System vorgesehen ist. Verwende nicht ersatzweise einen Windows-Patch.

### Der Patch wurde mit Safari heruntergeladen

Prüfe, ob du nach dem Download die ZIP-Datei oder bereits einen entpackten Ordner vor dir hast. Wenn Safari das Archiv automatisch geöffnet hat, passe die weiteren Schritte daran an. Lade die ZIP-Datei bei Bedarf erneut herunter, ohne sie automatisch öffnen zu lassen.

## Erneut versuchen oder Hilfe bekommen

[Setze das Spiel zurück](../Deinstallation/index.md), bevor du eine beschädigte Installation erneut patchst. Beachte dabei die Hinweise zu zusätzlichen Patchdateien.

Wenn es weiterhin nicht funktioniert, [melde uns](../Wissenswertes/BugReport.md) bitte dein Mac-Modell, die macOS-Version, Spiel, Store, Installationsmethode und die genaue Fehlermeldung. So können wir auch mögliche Unterschiede zwischen Geräten untersuchen.
