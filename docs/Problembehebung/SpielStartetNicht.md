---
title: Das Spiel startet nicht
description: In diesem Artikel erklären wir dir, was die Ursache dafür sein kann, dass das Spiel nicht startet.
tags:
  - Windows
  - Linux / Steam Deck
  - macOS
---

Dieser Fehler tritt häufig auf, wenn die Version vom Spiel nicht mit der Version vom Patch übereinstimmt. Bitte aktualisiere das Spiel auf Steam, indem du dir die neusten Updates herunterlädst und versuche dann erneut den Patch zu installieren.

### So überprüfst du, ob der Patch mit dem Spiel kompatibel ist:
1. Starte das Jackbox Party Pack deiner Wahl. In einer der Ecken im Hauptmenü steht eine **Build-Nummer**.
2. Vergleiche die Build-Nummer mit der Version vom Patch. Die Version vom aktuellen Patch wird dir in Jackbox Utility angezeigt, oder auf unserer [Startseite](https://jackboxpatch.de/startseite) in der Übersicht.

!!! info "Aufbau der Build-Nummer vom Patch"
    Die Buildnummer vom Patch ist wie folgt aufgebaut: **[Build vom Spiel].[Build vom Patch]-DE**.

Falls du weiterhin Probleme bei der Installation haben solltest, melde dich bei der Community auf unserem [Discord-Server](https://discord.gg/vGcu9HWde4).

### So kannst du die Erstellung von Log-Dateien auf Steam aktivieren
Log Dateien können uns helfen, das Problem genauer zu untersuchen.

1. **Rechtsklicke das Spiel** in deiner Steam-Bibliothek und klicke auf **Eigenschaften**.
2. Füge folgende Parameter bei den Startoptionen ein:
```
-jbg.config debug=true logging=true dev-console=true logFile=log.txt
```

Im Anschluss findest du im Spielverzeichnis eine log.txt Datei. Diese kannst du auf unserem [Discord-Server](https://discord.gg/vGcu9HWde4) mit dem Team teilen, um weitere Unterstützung zu bekommen.