import pytest
from calculator.operations import Add, Subtract, Multiply, Divide


@pytest.mark.parametrize("numbers, result", [
    ((1.0, 2.0), 3.0),
    ((1.0, 2.0, 3.0), 6.0),
    ((1.0, 2.0, 3.0, 4.0), 10.0)
])
def test_add(numbers, result):
    assert Add(numbers).perform() == result


@pytest.mark.parametrize("numbers, result", [
    ((1.0, 2.0), -1.0),
    ((1.0, 2.0, 3.0), -4.0),
    ((1.0, 2.0, 3.0, 4.0), -8.0)
])
def test_subtract(numbers, result):
    assert Subtract(numbers).perform() == result


@pytest.mark.parametrize("numbers, result", [
    ((1.0, 2.0), 2.0),
    ((1.0, 2.0, 3.0), 6.0),
    ((1.0, 2.0, 3.0, 4.0), 24.0)
])
def test_multiply(numbers, result):
    assert Multiply(numbers).perform() == result


@pytest.mark.parametrize("numbers, result", [
    ((1.0, 2.0), 0.5),
    ((1.0, 2.0, 3.0), 0.167),
    ((1.0, 2.0, 3.0, 4.0), 0.042)
])
def test_divide(numbers, result):
    assert float('{:0.3f}'.format(Divide(numbers).perform())) == result
