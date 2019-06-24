from jinja2 import Environment, PackageLoader, select_autoescape


class Gazebo:
    # parses object into model for world file
    @staticmethod
    def parse(obj):
        # load the model template from the environment
        env = Environment(
            loader=PackageLoader('templates', 'sdf_templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        model_template = env.get_template('model_template')

        # return the filled model template as a string
        return model_template.render(obj.__dict__)

    # fills world file with all models
    @staticmethod
    def config(scene):
        # parse all objects in the scenario
        all_models = ''
        for obj in scene.objects:
            all_models = all_models + Gazebo.parse(obj) + '\n\n'

        # load the world template from the environment
        env = Environment(
            loader=PackageLoader('templates', 'sdf_templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        world_template = env.get_template('world_template')

        # return the filled world template as a string
        return world_template.render(world_name='Example World', models=all_models)
