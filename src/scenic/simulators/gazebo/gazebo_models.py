from scenic.core.object_types import *
from jinja2 import Environment, PackageLoader, select_autoescape


class Cube(Object):
    height = 5
    width = 5
    depth = 5

    # fills model template with Cube attributes
    def parse(self):
        env = Environment(
            loader=PackageLoader('templates', 'sdf_templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        model_template = env.get_template('model_template')
        return model_template.render(model_name='Cube')  # TODO: fill template with other fields
