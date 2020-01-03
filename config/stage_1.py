from lib.maze      import MazeRunner, Obstacle
from lib.utilities import KeyBoard, TextPrinter


 ##
 #   @name  stage_1
 #   @type  maze instance
 #
 #   @usage The second stage of the demo config is
 #          a simple 8x8 maze with two additional
 #          obstacles - a locked door and a key
 #          to open the door. This example should
 #          demonstrate the configuration for a
 #          (combined) obstacle.
##
s1_maze = [[1, 1, 1, 1, 1, 1, 1, 1],
           [0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 0, 1, 0, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 0, 0, 0, 0, 1],
           [1, 0, 1, 0, 1, 1, 1, 1],
           [1, 0, 1, 0, 0, 0, 0, 0],
           [1, 1, 1, 1, 1, 1, 1, 1]]


s1_runner = MazeRunner(0, 1)


s1_keyboard = KeyBoard()
s1_keyboard.register(KeyBoard.KEY_ID_DOWN, s1_runner.walk_down)
s1_keyboard.register(KeyBoard.KEY_ID_UP, s1_runner.walk_up)
s1_keyboard.register(KeyBoard.KEY_ID_RIGHT, s1_runner.walk_right)
s1_keyboard.register(KeyBoard.KEY_ID_LEFT, s1_runner.walk_left)


o0s1_entry = Obstacle(0, 1)
o0s1_entry.register(Obstacle.maze_entry)

def s1_key_found(caller):
    TextPrinter.print("Key Found")
    caller.fullfill()

o1s1_key = Obstacle(1, 5)
o1s1_key.register(s1_key_found)

def s1_locked_door(caller):
    TextPrinter.print("Locked Door")
    if o1s1_key.fullfilled:
        TextPrinter.print("Opened with Key")
        caller.fullfill()
    else:
        TextPrinter.print("Key Missing")

o2s1_door = Obstacle(5, 1)
o2s1_door.register(s1_locked_door)

o3s1_exit = Obstacle(7, 6)
o3s1_exit.register(Obstacle.maze_exit)

s1_obstacles = [o0s1_entry, o1s1_key, o2s1_door, o3s1_exit]


