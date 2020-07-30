import time
from scenic.simulators.gazebo.interface import Gazebo
import scenic.syntax.translator as translator

"""
Calls on a file and writes the generated scenario to an sdf file
"""

# Input and output file name
scenarioFile = "examples/gazebo/uuv.sc"
outFile = "examples/gazebo/outputs/uuv_sim.world"
worldName = "empty_underwater"

# Load scenario from file
print('Beginning scenario construction...')
startTime = time.time()
scenario = translator.scenarioFromFile(scenarioFile)
totalTime = time.time() - startTime
print(f'Scenario constructed in {totalTime:.2f} seconds.')

# Generate a scene from scenario file, then fill out a gazebo world file from scene
startTime = time.time()
scene, iterations = scenario.generate(verbosity=3)
totalTime = time.time() - startTime
print(f'  Generated scene in {iterations} iterations, {totalTime:.4g} seconds.')
output = Gazebo.fill_world(scene, worldName)

# Write generated world to file
with open(outFile, 'w+') as fileObj:
    fileObj.write(output)
