from lib.maze      import MazeRunner, Obstacle
from lib.utilities import KeyBoard, TextPrinter

from config.snake_minigame import Snake


 ##
 #   @name  stage_4
 #   @type  maze instance
 #
 #   @usage The final stage of the demo config
 #          is a 16x16 maze with a few additional
 #          obstacles to demonstrate, first, an
 #          alternative way to reposition a maze
 #          runner inside a maze (i.e. 'teleport'
 #          obstacles) and, second, the call of
 #          a 'mini game' to clear out an obstacle.
##
s4_maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
           [1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
           [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
           [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
           [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1],
           [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


s4_runner = MazeRunner(0, 1)


s4_keyboard = KeyBoard()
s4_keyboard.register(KeyBoard.KEY_ID_DOWN, s4_runner.walk_down)
s4_keyboard.register(KeyBoard.KEY_ID_UP, s4_runner.walk_up)
s4_keyboard.register(KeyBoard.KEY_ID_RIGHT, s4_runner.walk_right)
s4_keyboard.register(KeyBoard.KEY_ID_LEFT, s4_runner.walk_left)


o0s4_entry = Obstacle(0, 1)
o0s4_entry.register(Obstacle.maze_entry)

def o1s4_key_found(caller):
    TextPrinter.print("Key Found")
    caller.fullfill()

o1s4_key = Obstacle(1, 14)
o1s4_key.register(o1s4_key_found)

def o2s4_locked_door(caller):
    TextPrinter.print("Locked Door")
    if o1s4_key.fullfilled:
        TextPrinter.print("Opened with Key")
        caller.fullfill()
    else:
        TextPrinter.print("Key Missing")

o2s4_door = Obstacle(14, 1)
o2s4_door.register(o2s4_locked_door)

def o3s4_teleporter(caller):
    TextPrinter.print("Teleport")
    s4_runner.walk_to(5, 5, False, True)

o3s4_tp = Obstacle(14, 14)
o3s4_tp.register(o3s4_teleporter)

def o4s4_teleporter(caller):
    TextPrinter.print("Teleport")
    s4_runner.walk_to(14, 14, False, True)

o4s4_tp = Obstacle(5, 5)
o4s4_tp.register(o4s4_teleporter)

def o5s4_key_found(caller):
    TextPrinter.print("Key Found")
    caller.fullfill()

o5s4_key = Obstacle(10, 5)
o5s4_key.register(o5s4_key_found)

def o6s4_snake(caller):
    TextPrinter.print("Mini Challenge")
    minigame = Snake(s4_keyboard, 8)
    s4_keyboard.register(KeyBoard.KEY_ID_DOWN, minigame.snake_down)
    s4_keyboard.register(KeyBoard.KEY_ID_UP, minigame.snake_up)
    s4_keyboard.register(KeyBoard.KEY_ID_RIGHT, minigame.snake_right)
    s4_keyboard.register(KeyBoard.KEY_ID_LEFT, minigame.snake_left)

    if minigame.run():
        TextPrinter.print("You Win")
        caller.fullfill()
    else:
        TextPrinter.print("You Lose")

    s4_keyboard.register(KeyBoard.KEY_ID_DOWN, s4_runner.walk_down)
    s4_keyboard.register(KeyBoard.KEY_ID_UP, s4_runner.walk_up)
    s4_keyboard.register(KeyBoard.KEY_ID_RIGHT, s4_runner.walk_right)
    s4_keyboard.register(KeyBoard.KEY_ID_LEFT, s4_runner.walk_left)

o6s4_minigame = Obstacle(5, 10)
o6s4_minigame.register(o6s4_snake)

def o7s4_teleporter(caller):
    TextPrinter.print("Teleport")
    s4_runner.walk_to(3, 3, False, True)

o7s4_tp = Obstacle(10, 10)
o7s4_tp.register(o7s4_teleporter)

def o8s4_teleporter(caller):
    TextPrinter.print("Teleport")
    s4_runner.walk_to(10, 10, False, True)

o8s4_tp = Obstacle(3, 3)
o8s4_tp.register(o8s4_teleporter)

def o9s4_snake(caller):
    TextPrinter.print("Mini Challenge")
    minigame = Snake(s4_keyboard, 12)
    s4_keyboard.register(KeyBoard.KEY_ID_DOWN, minigame.snake_down)
    s4_keyboard.register(KeyBoard.KEY_ID_UP, minigame.snake_up)
    s4_keyboard.register(KeyBoard.KEY_ID_RIGHT, minigame.snake_right)
    s4_keyboard.register(KeyBoard.KEY_ID_LEFT, minigame.snake_left)

    if minigame.run():
        TextPrinter.print("You Win")
        caller.fullfill()
    else:
        TextPrinter.print("You Lose")

    s4_keyboard.register(KeyBoard.KEY_ID_DOWN, s4_runner.walk_down)
    s4_keyboard.register(KeyBoard.KEY_ID_UP, s4_runner.walk_up)
    s4_keyboard.register(KeyBoard.KEY_ID_RIGHT, s4_runner.walk_right)
    s4_keyboard.register(KeyBoard.KEY_ID_LEFT, s4_runner.walk_left)

o9s4_minigame = Obstacle(3, 12)
o9s4_minigame.register(o9s4_snake)

def o10s4_locked_door(caller):
    TextPrinter.print("Locked Door")
    if o5s4_key.fullfilled:
        TextPrinter.print("Opened with Key")
        caller.fullfill()
    else:
        TextPrinter.print("Key Missing")

o10s4_door = Obstacle(12, 12)
o10s4_door.register(o10s4_locked_door)

def o11s4_teleporter(caller):
    TextPrinter.print("Teleport")
    s4_runner.walk_to(7, 7, False, True)

o11s4_tp = Obstacle(12, 3)
o11s4_tp.register(o11s4_teleporter)

def o12s4_teleporter(caller):
    TextPrinter.print("Teleport")
    s4_runner.walk_to(12, 3, False, True)

o12s4_tp = Obstacle(7, 7)
o12s4_tp.register(o12s4_teleporter)

o13s4_exit = Obstacle(8, 8)
o13s4_exit.register(Obstacle.maze_exit)

s4_obstacles = [o0s4_entry, o1s4_key, o2s4_door, o3s4_tp, o4s4_tp, o5s4_key, o6s4_minigame, o7s4_tp, o8s4_tp, o9s4_minigame, o10s4_door, o11s4_tp, o12s4_tp, o13s4_exit]

