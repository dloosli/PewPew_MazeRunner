from lib.maze      import MazeRunner, Obstacle
from lib.utilities import KeyBoard


 ##
 #   @name  stage_0
 #   @type  maze instance
 #
 #   @usage The first stage of the demo config is a
 #          simple 8x8 maze without any additional
 #          obstactles (i.e. only the mandatory
 #          maze entry and exit obstacles). This
 #          example should demonstrate the 'walk'
 #          method with the up/down/left/right
 #          keys on the PewPew board.
##
s0_maze = [[1, 1, 1, 1, 1, 1, 1, 1],
           [0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 1, 0, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 0, 0, 0, 0, 1],
           [1, 0, 1, 0, 1, 1, 1, 1],
           [1, 0, 1, 0, 0, 0, 0, 0],
           [1, 1, 1, 1, 1, 1, 1, 1]]


s0_runner = MazeRunner(0, 1)


s0_keyboard = KeyBoard()
s0_keyboard.register(KeyBoard.KEY_ID_DOWN, s0_runner.walk_down)
s0_keyboard.register(KeyBoard.KEY_ID_UP, s0_runner.walk_up)
s0_keyboard.register(KeyBoard.KEY_ID_RIGHT, s0_runner.walk_right)
s0_keyboard.register(KeyBoard.KEY_ID_LEFT, s0_runner.walk_left)


o0s0_entry = Obstacle(0, 1)
o0s0_entry.register(Obstacle.maze_entry)

o1s0_exit = Obstacle(7, 6)
o1s0_exit.register(Obstacle.maze_exit)

s0_obstacles = [o0s0_entry, o1s0_exit]


