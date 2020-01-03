# Maze Runner #
(an object oriented python game for the [PewPew Platform](https://github.com/pewpew-game))

&nbsp;

## Introduction ##
This repository contains the Maze Runner project. It is a small game written in Python for the [PewPew Platform](https://github.com/pewpew-game).

First of all it has to mention that this is my first Python project for which I had to script more than two lines of Python code. So it should not serve as a reference for well written Python code. As the focus was rather on a clear functional structure, I decided to take an object-oriented approach.

&nbsp;

## Project Structure ##
This repository has the following structure:

```bash
    |- Projekt
        |- config/
        |- doc/
        |- lib/
        |- maze_runner.py
        |- README.md
        |- README_de.md
```

* _config_: This folder contains the demo configuration including all game levels (i.e. stages) and a README file with a description of how to design and implement your own configurations.

* _doc_: This folder contains a single OpenOffice Calc file. You can use this file as a template for your own maze configurations.

* _lib_: This folder contains the all the Python scripts used for the Maze Runner game logic as well as one README file per Python module with some explanations about the classes.

* _maze\_runner.py_: This is the main module that is executed by the PewPew code. A GameController instance is created (c.f. 'lib' README) that loads a given configuration (c.f. 'config' README) and updates its state in a loop.

* _README_: This file contains an overview of this repository and an installation / deployment description for the Maze Runner game. It is available in english and german.

&nbsp;

## Installation and Deployment ##
Basically, you have two options to install and deploy the Maze Runner game:

1. _PewPew Board_: To execute the code on a PewPew Board, you first have to connect your board with your computer over USB. Then copy the two folders 'lib' and 'config' as well as the main module 'maze\_runner.py' to the automatically mounted PewPew board and (re)power the board. ** Attention - not tested yet! **

2. _PewPew Emulator_: The Maze Runner game can also be executed using the [PewPew Emulator](https://github.com/pewpew-game/pew-pygame). To do so, you have to install 'python3' and the Python3 package manager 'pip' on the development machine and follow the installation instructions of the PewPew Emulator README. After a successful installation, the two folders 'config' and 'lib' as well as the main module 'maze\_runner.py' have to be copied into the 'Pew Pygame' folder and the game can be deployed by executing the 'python3 maze_runner.py' command in a console. Under Linux with root privileges (`sudo` or `su`) run the following commands in a terminal:

```bash
    $ sudo apt-get update
    $ sudo apt-get install git
    $ sudo apt-get install python3
    $ sudo apt-get install python3-pip
    # without root privileges
    $ git clone https://github.com/pewpew-game/pew-pygame.git
    $ cd pew-pygame
    $ python3 -m pip install -r requirements.txt
    # copy 'lib', 'config' and maze_runner.py in the current folder
    $ python3 maze_runner.py
```

It is recommended to use the PewPew Emulator for the further development and the implementation of your own configurations, because it then is possible to debug the Python scripts for the PewPew board with the python method `print( ... )`.

&nbsp;

