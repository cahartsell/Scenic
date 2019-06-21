from scenic.simulators.gazebo.interface import *
from scenic.simulators.gazebo.gazebo_models import *

x = Cube()
y = Cube()

test_scenario = (x, y)

print(Gazebo.config(test_scenario))
