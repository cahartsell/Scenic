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
    for x in data['world']:
        all_models = all_models + model_template.render(model_name=x['name']) + '\n\n'
    with open('example.sdf', 'w+') as write_file:
        write_file.write(world_template.render(world_name='world', model=all_models))