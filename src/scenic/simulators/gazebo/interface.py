from jinja2 import Environment, PackageLoader, select_autoescape

class Gazebo:
    # fills world template with all objects in a scenario
    @staticmethod
    def config(scenario):
        for obj in scenario:  # TODO: separate object types into lists
            all_models = ''
            all_models = all_models + obj.parse()

        env = Environment(
            loader=PackageLoader('templates', 'sdf_templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )

        world_template = env.get_template('world_template')
        return world_template.render(world_name='Example World', models=all_models)
