import pytest
from calculator.operations import Add, Subtract, Multiply, Divide


@pytest.mark.parametrize("numbers, result", [
    ((1, 2), 3),
    ((1, 2, 3), 6),
    ((1, 2, 3, 4), 10)
])
def test_add(numbers, result):
    assert Add(numbers).perform() == result


@pytest.mark.parametrize("numbers, result", [
    ((1, 2), -1),
    ((1, 2, 3), -4),
    ((1, 2, 3, 4), -8)
])
def test_subtract(numbers, result):
    assert Subtract(numbers).perform() == result


@pytest.mark.parametrize("numbers, result", [
    ((1, 2), 2),
    ((1, 2, 3), 6),
    ((1, 2, 3, 4), 24)
])
def test_multiply(numbers, result):
    assert Multiply(numbers).perform() == result


@pytest.mark.parametrize("numbers, result", [
    ((1, 2), 0.5),
    ((1, 2, 3), 0.167),
    ((1, 2, 3, 4), 0.042)
])
def test_divide(numbers, result):
    assert Divide(numbers).perform() == result