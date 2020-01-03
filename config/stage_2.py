from lib.maze      import MazeRunner, Obstacle
from lib.utilities import KeyBoard


 ##
 #   @name  stage_2
 #   @type  maze instance
 #
 #   @usage The third stage of the demo config is
 #          a 16x16 maze without any additional
 #          obstactles (i.e. only the mandatory
 #          maze entry and exit obstacles). This
 #          example should demonstrate the 'walk'
 #          method in a maze with a size greater
 #          than the 8x8 display on the PewPew.
##
s2_maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
           [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
           [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
           [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
           [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
           [1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1],
           [1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
           [1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
           [1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
           [1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


s2_runner = MazeRunner(0, 1)


s2_keyboard = KeyBoard()
s2_keyboard.register(KeyBoard.KEY_ID_DOWN, s2_runner.walk_down)
s2_keyboard.register(KeyBoard.KEY_ID_UP, s2_runner.walk_up)
s2_keyboard.register(KeyBoard.KEY_ID_RIGHT, s2_runner.walk_right)
s2_keyboard.register(KeyBoard.KEY_ID_LEFT, s2_runner.walk_left)


o0s2_entry = Obstacle(0, 1)
o0s2_entry.register(Obstacle.maze_entry)

o1s2_exit = Obstacle(15, 14)
o1s2_exit.register(Obstacle.maze_exit)

s2_obstacles = [o0s2_entry, o1s2_exit]


