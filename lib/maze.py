import pew

from lib.utilities import TextPrinter


 ##
 #   @name  Maze
 #   @type  class
 #
 #   @usage text
##
class Maze:

    def __init__(self, maze, runner, obstacles, keyboard):
        self._maze = maze
        self._keyboard = keyboard

        self._obstacles = []
        for o in obstacles:
            if self.is_path(o.x_location, o.y_location):
                o.parent_maze(self)
                self._obstacles.append(o)
                self._maze[o.y_location][o.x_location] = 2

        self._runner = runner
        self._runner.parent_maze(self)
        if (not self.is_inside(self._runner.x_location, self._runner.y_location)) or \
            self.is_wall(self._runner.x_location, self._runner.y_location):
                self._runner.walk_to(self.obstacles[0].x_location,
                                     self.obstacles[0].y_location)

        self._x_offset = self._y_offset = 0
        self.update(True)


    @property
    def maze(self):
        return self._maze


    @property
    def keyboard(self):
        return self._keyboard


    @property
    def runner(self):
        return self._runner


    @property
    def obstacles(self):
        return self._obstacles


    def is_path(self, x, y):
        return self._maze[y][x] == 0


    def is_wall(self, x, y):
        return self._maze[y][x] == 1


    def is_obstacle(self, x, y):
        return self._maze[y][x] == 2


    def is_inside(self, x, y):
        return 0 <= x < len(self._maze[0]) and 0 <= y < len(self._maze)


    def assign_challenge(self, x_location, y_location):
        for o in self._obstacles:
            if (o.x_location == x_location) and (o.y_location == y_location):
                if not o.fullfilled:
                    o.challenge(o)
                return o.fullfilled


    def update(self, centered=False):
        if centered:
            self._x_offset = 3 + int(2 * self._runner.x_location / len(self._maze[0])) \
                               - self._runner.x_location
            self._y_offset = 3 + int(2 * self._runner.y_location / len(self._maze)) \
                               - self._runner.y_location

            while self._x_offset > 0:
                self._x_offset -= 1

            while self._x_offset < (8 - len(self._maze[0])):
                self._x_offset += 1


            while self._y_offset > 0:
                self._y_offset -= 1

            while self._y_offset < (8 - len(self._maze)):
                self._y_offset += 1   
        else:
            while (8 - len(self._maze[0])) < self._x_offset and \
                  (self._runner.x_location + self._x_offset) > 6:
                self._x_offset -= 1

            while  self._x_offset < 0 and \
                  (self._runner.x_location + self._x_offset) < 1:
                self._x_offset += 1

            while (8 - len(self._maze)) < self._y_offset and \
                  (self._runner.y_location + self._y_offset) > 6:
                    self._y_offset -= 1

            while  self._y_offset < 0 and \
                  (self._runner.y_location + self._y_offset) < 1:
                    self._y_offset += 1


    def paint(self, screen):
        screen.blit(pew.Pix.from_iter(self._maze), self._x_offset, self._y_offset)

        for o in self._obstacles:
            o.paint(screen, self._x_offset, self._y_offset)

        self._runner.paint(screen, self._x_offset, self._y_offset)

## end Maze


 ##
 #   @name  MazeRunner
 #   @type  class
 #
 #   @usage text
##
class MazeRunner:

    def __init__(self, x_location, y_location, color=3):
        self._parent_maze = None
        self._x_location = x_location
        self._y_location = y_location
        self._color = color
        self._ticker = 0


    @property
    def x_location(self):
        return self._x_location


    @property
    def y_location(self):
        return self._y_location


    def parent_maze(self, maze):
        self._parent_maze = maze


    def walk_down(self):
        self.walk_to(self._x_location, (self._y_location + 1))


    def walk_up(self):
        self.walk_to(self._x_location, (self._y_location - 1))


    def walk_right(self):
        self.walk_to((self._x_location + 1), self._y_location)


    def walk_left(self):
        self.walk_to((self._x_location - 1), self._y_location)


    def walk_to(self, x_location_new, y_location_new, trigger_challenge=True, centered=False):
        if self._parent_maze.is_inside(x_location_new, y_location_new):

            if self._parent_maze.is_path(x_location_new, y_location_new):
                self._x_location = x_location_new
                self._y_location = y_location_new
                self._parent_maze.update(centered)

            if self._parent_maze.is_obstacle(x_location_new, y_location_new):
                if trigger_challenge:
                    if self._parent_maze.assign_challenge(x_location_new, y_location_new):
                        self._x_location = x_location_new
                        self._y_location = y_location_new
                        self._parent_maze.update(centered)
                else:
                    self._x_location = x_location_new
                    self._y_location = y_location_new
                    self._parent_maze.update(centered)


    def update(self):
        self._ticker = (self._ticker + 1) % 6
        if self._ticker == 0:
            self._color = (self._color + 3) % 6


    def paint(self, screen, x_offset, y_offset):
        self.update()
        screen.pixel((self._x_location + x_offset),
                     (self._y_location + y_offset),
                      self._color)

# end MazeRunner


 ##
 #   @name  Obstacle
 #   @type  class
 #
 #   @usage text
##
class Obstacle:

    def __init__(self, x_location, y_location, color=0):
        self._parent_maze = None
        self._x_location = x_location
        self._y_location = y_location
        self._challenge  = self.no_challenge
        self._fullfilled = False
        self._color = color
        self._ticker = 0
        self._ticker_up = True


    @property
    def x_location(self):
        return self._x_location


    @property
    def y_location(self):
        return self._y_location

    @property
    def fullfilled(self):
        return self._fullfilled


    @property
    def challenge(self):
        return self._challenge


    def parent_maze(self, maze):
        self._parent_maze = maze


    def register(self, challenge):
        self._challenge = challenge


    def fullfill(self):
        self._fullfilled = True


    def update(self):
        if self._ticker == 31:
            self._ticker_up = False
            self._ticker = (self._ticker - 7)
        
        if self._ticker == 0:
            self._ticker_up = True
            self._ticker = (self._ticker + 7)

        self._ticker = (self._ticker + 1) if self._ticker_up else (self._ticker - 1)
        self.color = self._ticker // 8


    def paint(self, screen, x_offset, y_offset):
        if self.fullfilled:
            screen.pixel((self._x_location + x_offset),
                         (self._y_location + y_offset), 0)
        else:
            self.update()
            screen.pixel((self._x_location + x_offset),
                         (self._y_location + y_offset), self.color)


    @staticmethod
    def no_challenge(caller):
        print("no function registered")


    @staticmethod
    def maze_entry(caller):
        TextPrinter.print("Maze Entry")


    @staticmethod
    def maze_exit(caller):
        TextPrinter.print("Maze Exit")
        caller.fullfill()

# end Obstacle

