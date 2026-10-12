# Jackbox auf Deutsch – Support-Center

Das Wiki wird mit MkDocs Material gebaut. Die Navigation steht vollständig in
`mkdocs.yml`; zusammengeführte Artikel bleiben über Weiterleitungen erreichbar.

## Lokal arbeiten

```sh
python -m pip install -r requirements.txt
python -m mkdocs serve
```

Unter Windows kann eine virtuelle Umgebung mit `python -m venv .venv` angelegt
und anschließend `.venv/Scripts/python.exe` statt `python` verwendet werden.
Virtuelle Umgebungen gehören außerhalb von `docs`; `docs/venv` und `docs/.venv`
werden zusätzlich ausdrücklich vom Build ausgeschlossen.

## Vor einer Veröffentlichung prüfen

```sh
python -m mkdocs build --strict
python scripts/check_site.py
```

Die Prüfung kontrolliert interne Links und Dateien, doppelte IDs, die einmalige
Zuordnung jeder Seite in der Navigation, Inhalte des Suchindex, geschlossene
Spoiler und die wichtigsten Wege ab der Startseite (höchstens zwei Klicks über
Artikelverweise). `tests/legacy-anchors.json` sichert die 21 bestehenden URLs und
125 Überschriftenanker vor dem Umbau, auch über Weiterleitungen. Diesen Bestand nicht neu generieren, um
einen fehlgeschlagenen Kompatibilitätstest zu umgehen.

In der Browservorschau zusätzlich Desktop und Handy prüfen: Navigation öffnen,
Tastaturfokus und Sprunglink verwenden, Hell-/Dunkelmodus wechseln, WinZip- und
Terminal-Abschnitte auswählen, YDKJ-Spoiler öffnen und alte Direktlinks testen.
Suchbegriffe: Steam Deck, Mac, englisch, Update, deinstallieren,
HandshakeException und VCRUNTIME.

Nach Prüfung der Vorschau veröffentlicht der bestehende GitHub-Actions-Workflow
bei einem Push auf `main` oder `master` über `mkdocs gh-deploy`. Der strenge Build
und die Linkprüfung laufen zuvor. `docs/CNAME` erhält die Custom Domain im
generierten Ergebnis. Eine Rücknahme erfolgt durch Revert des Inhaltscommits und
erneutes Deployment über denselben Workflow.

## Inhalte pflegen

- Jede Seite bekommt genau einen Hauptplatz in der Navigation; Querverweise sind
  ausdrücklich erwünscht. „Installieren & Spielen“ führt direkt zu Jackbox Utility.
  Die manuellen Anleitungen werden dort unten als Alternative verlinkt.
- Bestehende Dateien nicht für eine neue Kategorie umbenennen. Bei geänderten
  Überschriften den bisherigen Anker mit `{ #alter-anker }` erhalten oder direkt
  beim passenden Abschnitt ein `<span id="alter-anker"></span>` setzen.
- Kurze, zusammengehörige Anleitungen auf einer Seite untereinander darstellen.
  Die Deinstallation bleibt auf einer Inhaltsseite. „Probleme lösen“ führt über
  eine kurze Übersicht zu eigenen Unterseiten für die einzelnen Problemthemen.
  Bei Zusammenführungen die alten Pfade unter `redirects.redirect_maps` in
  `mkdocs.yml` eintragen und ihre Überschriftenanker auf der Zielseite erhalten.
  Weiterleitungsziele ohne Fragment angeben, damit bestehende Sprungmarken
  erhalten bleiben; interne Links direkt auf den passenden neuen Abschnitt setzen.
- Anleitung: Anliegen und Geltungsbereich, Voraussetzungen, Schritte, Ergebnis,
  weiterführende Hilfe. Windows-Pfade nicht als plattformübergreifend beschreiben.
- Verfügbare Spiele und Downloads bleiben auf jackboxpatch.de; keine zweite Liste
  im Wiki anlegen. Den macOS-Download direkt auf das vorhandene DMG verlinken.
  TMP3-Skripte sind zentral im Spieleartikel erklärt.
- Bei Utility-, Patch- oder Plattformänderungen die zugehörigen Installations-,
  Update-, Fehlerhilfe- und Deinstallationsseiten gemeinsam prüfen.
- Artikel auf die nötigen Schritte und hilfreiche Verweise beschränken. Quellen-
  und Prüfnotizen gehören in die Wartungsdokumentation, nicht in Artikelfooter.

## Quellenabgleich des Umbaus (12. Oktober 2026)

- Die GitHub-Release-API meldete Utility 1.5.3 als aktuelles stabiles Release, mit
  Windows- und Linux-Assets. Das Release 1.5.1 enthält `JackboxUtility-MacOs.dmg`.
  Deshalb ist der macOS-Download versionsgebunden; der frühere `latest`-Link
  wurde ersetzt. Quellen: [1.5.3](https://github.com/JackboxUtility/JackboxUtility/releases/tag/1.5.3),
  [1.5.1](https://github.com/JackboxUtility/JackboxUtility/releases/tag/1.5.1),
  [Updater](https://github.com/JackboxUtility/JackboxUtilityUpdater/releases).
- Der Utility-Quellstand `5a1dcd0ad1b1f1efeb2c67021c275208f7499310` bestätigt
  `Logs/log.txt` unter dem Anwendungsdatenordner, die Windows-Namen
  `JackboxUtility/JackboxUtility` und den Aufruf `steam://validate/…` beim Reset.
  Quellen: [Dateipfade](https://github.com/JackboxUtility/JackboxUtility/blob/5a1dcd0ad1b1f1efeb2c67021c275208f7499310/jackbox_patcher/lib/services/files/folder_service.dart),
  [Windows-Metadaten](https://github.com/JackboxUtility/JackboxUtility/blob/5a1dcd0ad1b1f1efeb2c67021c275208f7499310/jackbox_patcher/windows/runner/Runner.rc),
  [Reset](https://github.com/JackboxUtility/JackboxUtility/blob/5a1dcd0ad1b1f1efeb2c67021c275208f7499310/jackbox_patcher/lib/components/dialogs/reset_pack_dialog.dart).
- [Epic beschreibt die Dateiprüfung](https://www.epicgames.com/help/c-32735058/c-36403860/a17813569?lang=en-US)
  als Überprüfung und Reparatur von Spieldateien. Daraus folgt keine Zusage, dass
  zusätzlich installierte Patchdateien entfernt werden.
- Spiel-/Store-Kompatibilität wird über die Download-Seite referenziert und nicht
  pauschal zugesichert. Nicht bestätigte frühere Aussagen zu Safari, dem macOS-
  Entpackprogramm und dem YDKJ-Deinstallationsworkaround wurden entfernt.
- TMP3-Schritte stammen aus den vorhandenen Anleitungen. Die Skripte sind nicht
  Teil dieses Repositories. Spielinstallationen, macOS und Steam Deck wurden bei
  diesem Umbau nicht praktisch getestet.
