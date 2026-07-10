from src.pilingup15.util import can_stack


def test_can_stack_true():
    cubes = [4, 3, 2, 1, 3, 4]
    assert can_stack(cubes) is True


def test_can_stack_false():
    cubes = [1, 3, 2]
    assert can_stack(cubes) is False


def test_can_stack_single_cube():
    cubes = [5]
    assert can_stack(cubes) is True


def test_can_stack_two_cubes():
    cubes = [2, 1]
    assert can_stack(cubes) is True


def test_can_stack_all_equal():
    cubes = [3, 3, 3, 3]
    assert can_stack(cubes) is True