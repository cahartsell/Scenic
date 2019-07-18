from scenic.simulators.gazebo.gazebo_models import *


constructor Pipe(Cylinder):
    model_name: 'pipe'
    z: 1
    roll: 1.5707963268
    radius: 0.50000
    length: 10
    template_name: 'cylinder_template'
    description: 'Pipe.'
    uri: 'model://pipe'

constructor UUV(Box):
    model_name: 'uuv'
    static: 'false'
    height: 2
    width: 2
    depth: 2
    template_name: 'box_template'
    description: 'UUV.'
    uri: 'model://uuv'

constructor Joint(Sphere):
    model_name: 'joint'
    z: 1
    radius: 0.5
    template_name: 'sphere_template'
    description: 'A joint to connect pipe segments.'
    uri: 'model://joint'

def buildPipeline(pipe1, num_pipes, max_angle):
    for x in range(0, num_pipes):
        # calculate the endpoint of pipe1
        x = cos(pipe1.heading-4.7123889804)*(pipe1.length/2)
        y = sin(pipe1.heading-4.7123889804)*(pipe1.length/2)
        endpoint = Point at x @ y relative to pipe1.position

        # calculate relative location of new pipe and place at endpoint of pipe1
        angle1 = 6.2831853072-max_angle
        angle2 = 6.2831853072+max_angle
        angle_range = (angle1, angle2)
        new_angle = resample(angle_range)
        x2 = cos(new_angle-4.7123889804)*(pipe1.length/2)
        y2 = sin(new_angle-4.7123889804)*(pipe1.length/2)
        Joint at endpoint
        pipe1 = Pipe at x2 @ y2 relative to endpoint, facing new_angle
