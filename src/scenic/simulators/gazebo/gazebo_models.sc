

# all classes are derived from the Scenic 'Object' base class
# each defined class must add additional fields to fill model template (field names must match template placeholders)
# necessary fields include: model_name, x, y, z, roll, pitch, yaw, shape_type, size, color

constructor Cube:
    model_name: 'Cube'  # TODO: how to create unique name for each instantiation?
    x: self.position[0]  # isolate x coordinate of position, default value = 0
    y: self.position[1]  # isolate y coordinate of position, default value = 0
    z: 0  # for now, objects will be represented in 2D
    roll: 0
    pitch: 0
    yaw: self.heading  # default heading = 0
    shape_type: 'box'  # SDF built-in shape type
    # override default dimensions of 1 x 1 x 1
    height: 5
    width: 5
    depth: 5
    size: '<size>' + str(self.height) + ' ' + str(self.width) + ' ' + str(self.depth) + '</size>'
    color: '1 0 0 1'  # color in R G B Opacity format
