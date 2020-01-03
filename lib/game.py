from lib.maze      import Maze
from lib.utilities import TextPrinter


 ##
 #   @name  GameController
 #   @type  class
 #
 #   @usage text
##
class GameController:

    def __init__(self, config):
        self._config = config
        self._stage  = -1
        self.next_stage()


    def next_stage(self):
        self._stage += 1
        try:
            self._maze = self._config.stages[self._stage]
            self._keyboard = self._config.stages[self._stage].keyboard
            TextPrinter.print("Stage " + str(self._stage))
        except IndexError:
            TextPrinter.print("You Win!")
            exit()


    def update(self, screen, keys):
        self._maze.paint(screen)
        self._keyboard.update(keys)

        if self._config.stages[self._stage].obstacles[-1].fullfilled:
            self.next_stage()

# end GameController


 ##
 #   @name  Configuration
 #   @type  class
 #
 #   @usage text
##
class Configuration:

    def __init__(self):
        self._stages = []


    @property
    def stages(self):
        return self._stages


    def add(self, maze, runner, obstacles, keyboard):
        self._stages.append(Maze(maze, runner, obstacles, keyboard))

# end Configuration

