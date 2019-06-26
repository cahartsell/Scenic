# all classes are derived from the Scenic 'Object' base class
# each defined class must add additional fields to fill model template (field names must match template placeholders)


constructor Cube:
    model_name: 'cube'
    static: 'false'
    x: self.position[0]  # isolate x coordinate of position, default value = 0
    y: self.position[1]  # isolate y coordinate of position, default value = 0
    z: 0
    roll: 0
    pitch: 0
    yaw: self.heading  # default heading = 0
    shape_type: 'box'  # SDF built-in shape type
    height: 1
    width: 1
    depth: 1
    size: '<size>' + str(self.height) + ' ' + str(self.width) + ' ' + str(self.depth) + '</size>'
    uri: 'model://scenic/simulators/gazebo/models/cube'

constructor Cylinder:
    model_name: 'cylinder'
    static: 'false'
    x: self.position[0]
    y: self.position[1]
    z: 0
    roll: 0
    pitch: 0
    yaw: self.heading
    shape_type: 'cylinder'
    radius: 1
    length: 3
    size: '<radius>' + str(self.radius) + '</radius>' + '\n' + '                            <length>' + str(self.length) + '</length>'
    uri: 'model://scenic/simulators/gazebo/models/cylinder'
