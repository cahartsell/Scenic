# Scenic

[![Documentation Status](https://readthedocs.org/projects/scenic-lang/badge/?version=latest)](https://scenic-lang.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

A compiler and scene generator for the Scenic scenario description language.
Please see the [documentation](https://scenic-lang.readthedocs.io/) for installation instructions, as well as tutorials and other information about the Scenic language, its implementation, and its interfaces to various simulators.

For a description of the language and some of its applications, see [our PLDI 2019 paper](https://arxiv.org/abs/1809.09310).
Scenic was designed and implemented by Daniel J. Fremont, Tommaso Dreossi, Shromona Ghosh, Xiangyu Yue, Alberto L. Sangiovanni-Vincentelli, and Sanjit A. Seshia.

If you have any problems using Scenic, please submit an issue to [our GitHub repository](https://github.com/BerkeleyLearnVerify/Scenic) or contact Daniel at <dfremont@ucsc.edu>.

The repository is organized as follows:

* the _src/scenic_ directory contains the package proper;
* the _examples_ directory has many examples of Scenic programs;
* the _docs_ directory contains the sources for the documentation;
* the _tests_ directory contains tests for the Scenic compiler.


## Gazebo Simulator Interface

Modifications for interfacing Scenic to Gazebo are located in src/scenic/simulators/gazebo. 

Models that can be used in Gazebo simulations are found in gazebo_models.sc. These classes are all derived from the Scenic 'Object' base class. 

Models for the UUV simulation specifically can be found in uuv_models.sc. These classes are derived from the base classes defined in gazebo_models.sc. Additionally, this file contains 
a function buildPipeline, which is used to connect pipe segments and vary the pipe heading within a specified angle range. The first pipe in the segment must be placed manually, and the function 
takes this pipe as an argument. The function also takes the number of pipe segments to add and the maximum angle variation in radians as arguments. For an example of how to use buildPipeline, see
examples/gazebo/uuv.sc. 

To add new objects to use with Scenic, new classes can be defined in the same manner as classes are defined in the uuv_models.sc file. These objects must also have corresponding Gazebo model 
files (model.config and model.sdf) to work with Gazebo. These model files must be located in src/scenic/simulators/gazebo/models. The model files can be created manually or automatically. 
Functionality for creating model files automatically is found in the master branch of yuul/Scenic in the interface.py file. 

The code for creating a Gazebo world file from a Scenic scene is primarily located in the interface.py file. The fill_world function in this file takes a scene and the name of the world to use as arguments. 
Scenes are generated using the built-in Scenic functionality. The world_name parameter must be the name of a template located in the world_templates directory. The fill_world function 
will parse the scene and add all objects into the world template. Objects are added in the form of an include block with a uri to the model files (model.config and model.sdf).
