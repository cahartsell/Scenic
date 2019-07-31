from jinja2 import Environment, select_autoescape, FileSystemLoader
import os

package_directory = os.path.dirname(os.path.abspath(__file__))


class Gazebo:
    # fills world file with all models as an include block
    @staticmethod
    def fill_world(scene, world_name):
        # load the include block template
        env = Environment(
            loader=FileSystemLoader(os.path.join(package_directory, 'templates/model_templates')),
            autoescape=select_autoescape(['html', 'xml'])
        )
        include_template = env.get_template('include_template')

        # iterate through all objects in the scene and add to string
        all_models = ''
        obj_num = 0
        for obj in scene.objects:
            all_models += include_template.render(obj.__dict__, object_id=obj.model_name+'_'+str(obj_num)) + '\n\n'
            obj_num += 1

        # load the world template
        env2 = Environment(
            loader=FileSystemLoader(os.path.join(package_directory, 'templates/world_templates')),
            autoescape=select_autoescape(['html', 'xml'])
        )
        world_template = env2.get_template(world_name)

        # return the filled world template as a string
        return world_template.render(models=all_models)
