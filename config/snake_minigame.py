import pew
import random


 ##
 #   @name  Snake
 #   @type  class
 #
 #   @usage text
##
class Snake:

    def __init__(self, keyboard, win_length=6, color=3):
        self._keyboard = keyboard
        self._win_length = win_length
        self._color = color
        self._snake = [(2, 4)]
        self._x_delta, self._y_delta = 1, 0
        self._game_speed = 4


    def snake_down(self):
        if self._y_delta == 0:
            self._x_delta, self._y_delta = 0, 1


    def snake_up(self):
        if self._y_delta == 0:
            self._x_delta, self._y_delta = 0, -1


    def snake_right(self):
        if self._x_delta == 0:
            self._x_delta, self._y_delta = 1, 0


    def snake_left(self):
        if self._x_delta == 0:
            self._x_delta, self._y_delta = -1, 0


    def paint(self, screen):
        if len(self._snake) > 1:
            screen.pixel(self._snake[-2][0], self._snake[-2][1], self._color)
        screen.pixel(self._snake[-1][0], self._snake[-1][1], self._color)


    def rub_out(self, screen, position):
        x_location, y_location = self._snake.pop(position)
        screen.pixel(x_location, y_location, 0)

    def run(self):
        screen = pew.Pix()
        apple = Apple(self._snake)
        apple.paint(screen)

        while True:
            self.paint(screen)
            pew.show(screen)
            pew.tick(1 / self._game_speed)

            self._keyboard.update(pew.keys())
            x = (self._snake[-1][0] + self._x_delta) % 8
            y = (self._snake[-1][1] + self._y_delta) % 8

            if (x, y) in self._snake:
                return False
            
            if len(self._snake) >= self._win_length:
                return True

            self._snake.append((x, y))

            if x == apple.x_location and y == apple.y_location:
                apple.rub_out(screen)
                apple = Apple(self._snake)
                apple.paint(screen)
                self._game_speed += 0.2
            else:
                self.rub_out(screen, 0)

## end Snake


 ##
 #   @name  Apple
 #   @type  class
 #
 #   @usage text
##
class Apple:

    def __init__(self, snake, color=2):
        self._x_location, self._y_location = snake[0]
        while (self._x_location, self._y_location) in snake:
            self._x_location = random.getrandbits(3)
            self._y_location = random.getrandbits(3)
        self._color = color


    @property
    def x_location(self):
        return self._x_location


    @property
    def y_location(self):
        return self._y_location


    def paint(self, screen):
        screen.pixel(self._x_location, self._y_location, self._color)


    def rub_out(self, screen):
        screen.pixel(self._x_location, self._y_location, 0)

## end Apple
