from scenic.simulators.gazebo.uuv_models import *


uuv_location = 5 @ 5
ego = UUV at uuv_location

pipe1 = Pipe left of uuv_location by 3

buildPipeline(pipe1, 10, 0.7853981634)
