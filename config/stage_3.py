from lib.maze      import MazeRunner, Obstacle
from lib.utilities import KeyBoard, TextPrinter


 ##
 #   @name  stage_3
 #   @type  maze instance
 #
 #   @usage The fourth stage of the demo config
 #          is a 16x16 maze with four additional
 #          obstacles - two locked door and a key
 #          each to open the door. This example
 #          should demonstrate the configuration
 #          for (combined) obstacles in a maze with
 #          a size greater than the 8x8 display on
 #          the PewPew.
##
s3_maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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


s3_runner = MazeRunner(0, 1)


s3_keyboard = KeyBoard()
s3_keyboard.register(KeyBoard.KEY_ID_DOWN, s3_runner.walk_down)
s3_keyboard.register(KeyBoard.KEY_ID_UP, s3_runner.walk_up)
s3_keyboard.register(KeyBoard.KEY_ID_RIGHT, s3_runner.walk_right)
s3_keyboard.register(KeyBoard.KEY_ID_LEFT, s3_runner.walk_left)


o0s3_entry = Obstacle(0, 1)
o0s3_entry.register(Obstacle.maze_entry)

def o1s3_key_found(caller):
    TextPrinter.print("Key Found")
    caller.fullfill()

o1s3_key = Obstacle(1, 14)
o1s3_key.register(o1s3_key_found)

def o2s3_locked_door(caller):
    TextPrinter.print("Locked Door")
    if o1s3_key.fullfilled:
        TextPrinter.print("Opened with Key")
        caller.fullfill()
    else:
        TextPrinter.print("Key Missing")

o2s3_door = Obstacle(13, 6)
o2s3_door.register(o2s3_locked_door)

def o3s3_key_found(caller):
    TextPrinter.print("Key Found")
    caller.fullfill()

o3s3_key = Obstacle(14, 1)
o3s3_key.register(o3s3_key_found)

def o4s3_locked_door(caller):
    TextPrinter.print("Locked Door")
    if o3s3_key.fullfilled:
        TextPrinter.print("Opened with Key")
        caller.fullfill()
    else:
        TextPrinter.print("Key Missing")

o4s3_door = Obstacle(12, 12)
o4s3_door.register(o4s3_locked_door)

o5s3_exit = Obstacle(15, 14)
o5s3_exit.register(Obstacle.maze_exit)

s3_obstacles = [o0s3_entry, o1s3_key, o2s3_door, o3s3_key, o4s3_door, o5s3_exit]


