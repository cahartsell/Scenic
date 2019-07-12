# all classes are derived from the Scenic 'Object' base class


constructor Box:
    model_name: 'box'
    static: 'true'
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
    template_name: 'box_template'
    description: 'A simple Box.'
    uri: 'model://box'

constructor Cylinder:
    model_name: 'cylinder'
    static: 'true'
    x: self.position[0]
    y: self.position[1]
    z: 0
    roll: 0
    pitch: 0
    yaw: self.heading
    shape_type: 'cylinder'
    radius: 1
    length: 1
    template_name: 'cylinder_template'
    description: 'A simple Cylinder.'
    uri: 'model://cylinder'

constructor Sphere:
    model_name: 'sphere'
    static: 'true'
    x: self.position[0]
    y: self.position[1]
    z: 0
    roll: 0
    pitch: 0
    yaw: self.heading
    shape_type: 'sphere'
    radius: 1
    template_name: 'sphere_template'
    description: 'A simple Sphere.'
    uri: 'model://sphere'
