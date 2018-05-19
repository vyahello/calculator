import pytest
from calculator.converters import ToFloat
from calculator.operations import Add


@pytest.mark.parametrize("numbers, result", [
    ((1, 2), 3),
    ((1, 2, 3), 6),
    ((1, 2, 3, 4), 10)
])
def test_to_float(numbers, result):
    assert ToFloat(Add(tuple(map(float, numbers)))).prepare() == result
