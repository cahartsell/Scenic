import time

from interface import Gazebo
import scenic.syntax.translator as translator

"""
Calls on a file and writes the generated scenario to an sdf file
"""

# Input and output file name
fileName = "examples/gazebo/simpleBox.sc"
worldName = "basic_world"
outFile = "examples/gazebo/outputs/test2.world"

# Load scenario from file
print('Beginning scenario construction...')
startTime = time.time()
scenario = translator.scenarioFromFile(fileName)
totalTime = time.time() - startTime
print(f'Scenario constructed in {totalTime:.2f} seconds.')

def generateScene():
    startTime = time.time()
    scene, iterations = scenario.generate(verbosity=3)
    totalTime = time.time() - startTime
    print(f'  Generated scene in {iterations} iterations, {totalTime:.4g} seconds.')
    return scene, iterations

scene, _ = generateScene()
output = Gazebo.config(scene, worldName)

with open(outFile, 'w+') as fileObj:
    fileObj.write(output)
