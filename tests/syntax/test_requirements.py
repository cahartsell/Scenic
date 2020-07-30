
import pytest

import scenic
from scenic import scenarioFromString as compileScenic
from scenic.syntax.translator import InterpreterParseError, InvalidScenarioError
from tests.utils import sampleEgo

## Basic

def test_requirement():
    scenario = compileScenic(
        'ego = Object at (-10, 10) @ 0\n'
        'require ego.position.x >= 0'
    )
    xs = [sampleEgo(scenario, maxIterations=60).position.x for i in range(60)]
    assert all(0 <= x <= 10 for x in xs)

def test_soft_requirement():
    scenario = compileScenic(
        'ego = Object at (-10, 10) @ 0\n'
        'require[0.9] ego.position.x >= 0'
    )
    xs = [sampleEgo(scenario, maxIterations=60).position.x for i in range(350)]
    count = sum(x >= 0 for x in xs)
    assert 255 <= count < 350

## Forbidden operations inside requirements

def test_object_in_requirement():
    scenario = compileScenic('require Object\n' 'ego = Object')
    with pytest.raises(InterpreterParseError):
        scenario.generate(maxIterations=1)

def test_param_in_requirement():
    scenario = compileScenic('require param x = 4\n' 'ego = Object')
    with pytest.raises(InterpreterParseError):
        scenario.generate(maxIterations=1)

def test_mutate_in_requirement():
    scenario = compileScenic('require mutate\n' 'ego = Object')
    with pytest.raises(InterpreterParseError):
        scenario.generate(maxIterations=1)

def test_require_in_requirement():
    scenario = compileScenic('require (require True)\n' 'ego = Object')
    with pytest.raises(InterpreterParseError):
        scenario.generate(maxIterations=1)

## Error handling

def test_runtime_parse_error_in_requirement():
    scenario = compileScenic('require visible 4\n' 'ego = Object')
    with pytest.raises(InterpreterParseError):
        scenario.generate(maxIterations=1)

## Static violations of built-in requirements

def test_static_containment_violation():
    with pytest.raises(InvalidScenarioError):
        compileScenic(
            'foo = RectangularRegion(0@0, 0, 5, 5)\n'
            'ego = Object at 10@10, with regionContainedIn foo'
        )

def test_static_visibility_violation():
    with pytest.raises(InvalidScenarioError):
        compileScenic(
            'ego = Object at 10@0, facing -90 deg, with viewAngle 90 deg\n'
            'Object at 0@10'
        )

def test_static_intersection_violation():
    with pytest.raises(InvalidScenarioError):
        compileScenic(
            'ego = Object at 0@0\n'
            'Object at 1@0'
        )
