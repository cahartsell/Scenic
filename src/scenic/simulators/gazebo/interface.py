import time
import os
from jinja2 import Environment, PackageLoader, FileSystemLoader, select_autoescape
import scenic.syntax.translator as translator


class Gazebo:
    # creates a dictionary of all objects in a scenario that do not yet have model files
    @staticmethod
    def parse(scenario):
        models = {}
        for obj in scenario.objects:
            path = 'src/scenic/simulators/gazebo/models/' + str(obj.model_name)
            if os.path.exists(path):
                pass  # do not add repeated object types
            else:
                # add to list
                models[obj.model_name] = obj
        return models

    # writes to model files
    @staticmethod
    def write(scenario):
        # parse the scenario
        models = Gazebo.parse(scenario)

        # load the template environment
        env = Environment(
            loader=FileSystemLoader('src/scenic/simulators/gazebo/templates/model_templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )

        # iterate through models and write to model.sdf and model.config files
        for model in models:
            # write to .sdf file
            sdf_template = env.get_template(models[model].template_name)
            sdf = sdf_template.render(models[model].__dict__)
            os.mkdir('src/scenic/simulators/gazebo/models/' + str(models[model].model_name))
            sdf_path = 'src/scenic/simulators/gazebo/models/' + str(models[model].model_name) + '/model.sdf'
            with open(sdf_path, 'w+') as write_file:
                write_file.write(sdf)

            # write to .config file
            config_template = env.get_template('config_template')
            config = config_template.render(models[model].__dict__)
            config_path = 'src/scenic/simulators/gazebo/models/' + str(models[model].model_name) + '/model.config'
            with open(config_path, 'w+') as write_file:
                write_file.write(config)

    # fills world file with all models as an include block
    @staticmethod
    def fill_world(scene, world_name):
        # load the include block template
        env = Environment(
            loader=FileSystemLoader('src/scenic/simulators/gazebo/templates/model_templates'),
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
        env = Environment(
            loader=FileSystemLoader('src/scenic/simulators/gazebo/templates/world_templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        world_template = env.get_template(world_name)

        # return the filled world template as a string
        return world_template.render(models=all_models)

    @staticmethod
    def config(scenic_code, world_name):
        # create scenic file
        with open('examples/gazebo/uuv.sc', 'w+') as write_file:
            write_file.write(scenic_code)

        # load scenario from file
        print('Beginning scenario construction...')
        startTime = time.time()
        scenario = translator.scenarioFromFile('examples/gazebo/uuv.sc')
        totalTime = time.time() - startTime
        print(f'Scenario constructed in {totalTime:.2f} seconds.')

        # generate scene from loaded scenario
        startTime = time.time()
        scene, iterations = scenario.generate(verbosity=3)
        totalTime = time.time() - startTime
        print(f'  Generated scene in {iterations} iterations, {totalTime:.4g} seconds.')

        return Gazebo.fill_world(scene, world_name)
