import json

from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader('templates', 'sdf_templates'),
    autoescape=select_autoescape(['html', 'xml'])
)

print('<sdf version="1.5">\n    <world name="Example Car World">\n')

template = env.get_template('model_template')

with open('world_data.json') as json_file:
    data = json.load(json_file)
    for x in data['world']:
        print(template.render(model_name=x['name']), '\n')

print('    </world>\n</sdf>')