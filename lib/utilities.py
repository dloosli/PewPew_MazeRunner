import pew


 ##
 #   @name  KeyBoard
 #   @type  class
 #
 #   @usage text
##
class KeyBoard:

    KEY_ID_X     = 0
    KEY_ID_DOWN  = 1
    KEY_ID_LEFT  = 2
    KEY_ID_RIGHT = 3
    KEY_ID_UP    = 4
    KEY_ID_O     = 5

    KEY_MAP = {pew.K_X:KEY_ID_X,
               pew.K_O:KEY_ID_O,
               pew.K_LEFT:KEY_ID_LEFT,
               pew.K_RIGHT:KEY_ID_RIGHT,
               pew.K_UP:KEY_ID_UP,
               pew.K_DOWN:KEY_ID_DOWN}


    def __init__(self, key_pressed=-1):
        self._key_pressed = key_pressed
        self._function_reg = [self.no_operation,
					 		  self.no_operation,
					 		  self.no_operation,
							  self.no_operation,
							  self.no_operation,
							  self.no_operation]


    def register(self, key_id, function):
        self._function_reg[key_id] = function


    def update(self, bit_array):
        if bit_array > 0:
            if (bit_array in self.KEY_MAP) and (self._key_pressed == -1):
                self._key_pressed = self.KEY_MAP[bit_array]
                self._function_reg[self._key_pressed]()
        else:
            self._key_pressed = -1


    @staticmethod
    def no_operation():
        print("no function registered")

## end KeyBoard


 ##
 #   @name  TextPrinter
 #   @type  class
 #
 #   @usage text
##
class TextPrinter:

    @staticmethod
    def print(string):
        _screen = pew.Pix()
        _text   = pew.Pix.from_text(string, 3, 0)

        for dx in range(-8, _text.width):
            _screen.blit(_text, -dx, 1)
            pew.show(_screen)
            pew.tick(1 / 8)

## end TextPrinter

