from lib.game import Configuration

from config.stage_0 import *
from config.stage_1 import *
from config.stage_2 import *
from config.stage_3 import *
from config.stage_4 import *


 ##
 #   @name  demo_config
 #   @type  config instance
##
configuration = Configuration()
configuration.add(s0_maze, s0_runner, s0_obstacles, s0_keyboard)
configuration.add(s1_maze, s1_runner, s1_obstacles, s1_keyboard)
configuration.add(s2_maze, s2_runner, s2_obstacles, s2_keyboard)
configuration.add(s3_maze, s3_runner, s3_obstacles, s3_keyboard)
configuration.add(s4_maze, s4_runner, s4_obstacles, s4_keyboard)

# end simple_config
