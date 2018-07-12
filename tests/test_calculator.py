import pytest
from calculator.calculators import BasicCalculator


@pytest.mark.parametrize("numbers, result", [
    ((1.0, 2.0), 3.0),
    ((1.0, 2.0, 3.0), 6.0),
    ((1.0, 2.0, 3.0, 4.0), 10.0)
])
def test_add(numbers: str, result: str) -> None:
    assert BasicCalculator(numbers).add() == result


@pytest.mark.parametrize("numbers, result", [
    ((1.0, 2.0), -1.0),
    ((1.0, 2.0, 3.0), -4.0),
    ((1.0, 2.0, 3.0, 4.0), -8.0)
])
def test_subtract(numbers: str, result: str) -> None:
    assert BasicCalculator(numbers).subtract() == result


@pytest.mark.parametrize("numbers, result", [
    ((1.0, 2.0), 2.0),
    ((1.0, 2.0, 3.0), 6.0),
    ((1.0, 2.0, 3.0, 4.0), 24.0)
])
def test_multiply(numbers: str, result: str) -> None:
    assert BasicCalculator(numbers).multiply() == result


@pytest.mark.parametrize("numbers, result", [
    ((1.0, 2.0), 0.5),
    ((1.0, 2.0, 3.0), 0.167),
    ((1.0, 2.0, 3.0, 4.0), 0.042)
])
def test_divide(numbers: str, result: str) -> None:
    assert BasicCalculator(numbers).divide() == result
