---
title: Das Spiel funktioniert auf macOS nicht richtig
description: In diesem Artikel erklären wir dir, was die Ursache dafür sein kann, dass Spiele auf macOS-Systemen nicht richtig funktionieren.
tags:
  - macOS
---

# Das Spiel funktioniert auf macOS nicht richtig

Die macOS-Version von Jackbox-Spielen stellt für das Übersetzerteam eine besondere Herausforderung dar, da sich die Dateisysteme teilweise sehr stark von den Windows- und Linux-Versionen unterscheiden. Dazu kommt, dass im Team niemand mit einem Mac ausgestattet ist. Wir können zwar probieren, die Übersetzungen mit dem Mac-Dateisystem kompatibel zu machen, jedoch haben wir kaum Möglichkeiten, diese Patches zu testen.

Trotzdessen sind wir davon überzeugt, dass wir mittlerweile stabile macOS-Versionen unserer Übersetzungen veröffentlicht haben.

Da unser hauseigener Installer, [**Jackbox Utility**](../Installation/JackboxUtility.md), derzeit noch nicht für macOS verfügbar ist, müssen die Patches noch manuell heruntergeladen und installiert werden. Eine vollständige Anleitung dazu findest du [**hier**](../Installation/macOS.md). Es ist wichtig, dass diese Anleitung **exakt** befolgt wird. Dies sind die häufigsten Fehlerursachen:

## Bekannte Fehlerursachen
### Verwendung vom vorinstallierten Standardprogramm zum Entpacken des Patches
Das Standardprogramm kann unsere Patches nicht korrekt entpacken. Viele Dateien werden beim Entpacken mit dem Standardprogramm beschädigt oder gehen gar verloren. Wir haben viele Alternativprogramme ausprobiert und konnten nur mit dem Programm [**WinZip**](https://www.winzip.com/en/mac/) zufriedenstellende Ergebnisse feststellen.
### Entpacken des Patches in das falsche Unterverzeichnis
Um zu gewährleisten, dass der Patch korrekt installiert wird, muss **die Ordnerstruktur** vom Archiv-Inhalt mit der des Spielverzeichnisses **übereinstimmen**. Achte beispielsweise darauf, dass der `games`-Order sowohl auf Patch- als auch auf Spielebene gleich ist.
### Die Windows-Version wurde heruntergeladen
Für einige Party Packs ist eine spezielle **macOS-Version** erforderlich, da sich das Dateisystem unterscheidet. Stelle sicher, dass du auf unserer [**Download-Seite**](https://jackboxpatch.de/downloads) den macOS-Patch herunterlädst. 
### Der Patch wurde mit Safari heruntergeladen
Wir empfehlen die Verwendung von **Mozilla Firefox oder Google Chrome**, um die Patches herunterzuladen. Safari komprimiert die ZIP-Datei beim Downloadvorgang, was unter Umständen dazu führen kann, dass der Patch fehlerhaft installiert wird.

---

Denke daran, den beschädigten Patch zu [**deinstallieren**](../Deinstallation/Steam.md), bevor du die Installation erneut versuchst.

!!! info ""
    Falls du weiterhin Probleme bei der Installation mit deinem Mac haben solltest, melde dich bei der Community auf unserem [Discord-Server](https://discord.gg/vGcu9HWde4).