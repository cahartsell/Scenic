from scenic.simulators.gazebo.uuv_models import *

num_pipe_segments = 15

uuv_location = 5 @ 5
ego = UUV at uuv_location

pipes = []
pipe0 = Pipe offset by (-30, 30) @ (-10, 10),
    facing (-20 deg, 20 deg) relative to ego.heading
pipes.append(pipe0)

for i in range(1, num_pipe_segments):
    pipe = Pipe ahead of pipes[i-1] by pipes[i-1].length,
        facing (-20 deg, 20 deg) relative to pipes[i-1].heading
    pipes.append(pipe)