from jinja2 import Environment, PackageLoader, select_autoescape


class Gazebo:
    # fills world file with all models as an include block
    @staticmethod
    def config(scene, world_name):
        # load the include block template
        env = Environment(
            loader=PackageLoader('templates', 'model_templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        include_template = env.get_template('include_template')

        # iterate through all objects in the scene and add to string
        all_models = ''
        for obj in scene.objects:
            all_models += include_template.render(obj.__dict__) + '\n\n'

        # load the world template
        env = Environment(
            loader=PackageLoader('templates', 'world_templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        world_template = env.get_template(world_name)

        # return the filled world template as a string
        return world_template.render(models=all_models)
