# Maze Runner #
(ein objekt-orientiert gescriptetes Python Spiel für die [PewPew Plattform](https://github.com/pewpew-game))

&nbsp;

## Vorbemerkung ##
Dieses Repository umfasst das Maze Runner Projekt - ein kleines, in Python geschriebenes Spiel für die  [PewPew Plattform](https://github.com/pewpew-game).

Vorab muss ich erwähnen, dass dies mein erstes Python Projekt ist, für welches ich mehr als zwei Zeilen Python Code scripten musste. Es sollte somit nicht als Referenz für gut geschriebenen Python Code dienen. Der Fokus lag vielmehr auf einer klaren funktionalen Struktur, weshalb ich mich für einen objekt-orientierten Ansatz entschieden habe.

&nbsp;

## Projektstruktur ##
Das Repository ist folgendermassen strukturiert:

```bash
    |- Projekt
        |- config/
        |- doc/
        |- lib/
        |- maze_runner.py
        |- README.md
        |- README_de.md
```

* _config_: Dieser Ordner enthält die Demo Konfiguration und die einzelnen Spiellevel (sog. stages) sowie eine README Datei mit einer Beschreibung, wie eine eigenen Konfiguration erstellt werden kann.

* _doc_: Dieser Ordner enthält eine einzelne OpenOffice Calc Datei, welche als Vorlage für eigenen Labyrinthe dienen kann.

* _lib_: Dieser Ordner enthält die Python Scripts für das Spiel selbst und einer  README Datei pro Python Modul mit Erklärungen zu den einzelnen Klassen.

* _maze\_runner.py_: Diese Datei entspricht dem Hauptmodul, welches vom PewPew aufgerufen wird. Dazu wird ein GameController (vgl. 'lib' README) erstellt, eine Konfiguration (vgl. 'config' README) geladen und in einer Schlaufe ausgeführt.

* _README_: Diese Datei enthält eine Übersicht über das Repository, eine Beschreibung für die Ausführung dieses Spiels und ist sowohl in englisch als auch deutsch verfügbar.

&nbsp;

## Spiel Ausprobieren ##
Das Spiel kann grundsätzlich auf zwei verschiedene Arten ausprobiert werden:

1. _PewPew Board_: Das Spiel kann auf einem PewPew Board ausprobiert werden, indem das Board über USB mit dem Computer verbunden wird und die beiden Ordner 'config' und 'lib' sowie das Hauptmodul 'maze\_runner.py' auf das automatisch als Speicher geladenen PewPew kopiert werden. Sodann muss nur noch das Board aus- und wieder eingeschaltet werden. ** Achtung - dies konnte noch nicht getestet werden! **

2. _PewPew Emulator_: Das Spiel kann auch mit dem [PewPew Emulator](https://github.com/pewpew-game/pew-pygame) ausprobiert werden. Dazu muss auf dem Entwicklungsrechner 'python3' und das Python3 Paketverwaltungstool 'pip' installiert sowie die Installationsanleitung des Emulators befolgt werden. Danach müssen die beiden Ordner 'config' und 'lib' sowie das Hauptmodul 'maze\_runner.py' in den 'Pew Pygame' Ordner kopiert und das Spiel mit dem Konsolenbefehl `python3 maze_runner.py` ausgeführt werden. Unter Linux mit root Rechten (`sudo` oder `su`) müssen dazu die folgenden Befehle in einem Terminal ausgeführt werden:

```bash
    $ sudo apt-get update
    $ sudo apt-get install git
    $ sudo apt-get install python3
    $ sudo apt-get install python3-pip
    # ohne root Rechte
    $ git clone https://github.com/pewpew-game/pew-pygame.git
    $ cd pew-pygame
    $ python3 -m pip install -r requirements.txt
    # 'lib', 'config' und maze_runner.py in den aktuellen Ordner kopieren
    $ python3 maze_runner.py
```

Für das Weiterentwickeln und das Erstellen eigener Konfigurationen empfehle ich, den Simulator zu verwenden, da mit der Python Methode `print( ... )` die einzelnen PewPew Module relativ einfach auf Fehler untersucht werden können.

&nbsp;

## Lizenz ##
Alle Dateien dieses Repositorys gelten als freie Software und können entsprechend der WTFPL Lizenz (c.f. [http://www.wtfpl.net](http://www.wtfpl.net)) verwendet werden. Dieser Code soll der Allgemeinheit nützlich sein, bedingt jedoch SÄMTLICHE HAFTUNGSANSPRÜCHE UND GARANTIEN in vollem Umfang weg.

&nbsp;

