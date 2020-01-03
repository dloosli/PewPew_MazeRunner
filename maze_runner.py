import pew

from config.demo_config import configuration
from lib.game           import GameController


 ##
 #   @name  -
 #   @type  main
##
pew.init()
screen = pew.Pix()

controller = GameController(configuration)

while True:
    controller.update(screen, pew.keys())
    pew.show(screen)    
    pew.tick(1 / 12)

# end main

