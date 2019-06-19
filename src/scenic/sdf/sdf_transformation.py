import json

from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('templates', 'sdf_templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

world_template = env.get_template('world_template')
model_template = env.get_template('model_template')

with open('world_data.json') as json_file:
    data = json.load(json_file)
    all_models = ''
    for m in data['world']:
        # define characteristics for expected objects in the world
        if m['name'] == 'car':
            shape = 'box'
            size = '<size> ' + m['width'] + ' ' + m['height'] + ' ' + m['depth'] + ' </size>'
        else:
            shape = 'box'
            size = '<size> ' + m['width'] + ' ' + m['height'] + ' ' + m['depth'] + ' </size>'

        # fill model template
        all_models = all_models + model_template.render(model_name=m['name']+m['id'], x=m['x'], y=m['y'], z=m['z'], roll='0',
                                                        pitch='0', yaw=m['heading'], shape_type=shape,
                                                        size=size, color=m['color']) + '\n\n'
    with open('example.sdf', 'w+') as write_file:
        # fill world template with models
        write_file.write(world_template.render(world_name='Example World', models=all_models))