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
