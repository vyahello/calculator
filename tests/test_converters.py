import pytest
from calculator.converters import ToFloat
from calculator.operations import Add


@pytest.mark.parametrize("numbers, result", [
    ((1.0, 2.0), 3.0),
    ((1.0, 2.0, 3.0), 6.0),
    ((1.0, 2.0, 3.0, 4.0), 10.0)
])
def test_to_float(numbers: str, result: str) -> None:
    assert ToFloat(Add(numbers)).perform() == result
