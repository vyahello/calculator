import pytest
from calculator.numbers import SafeNumbers, NumbersError


@pytest.mark.parametrize("numbers, result", [
    ((1.0, 2.0), (1.0, 2.0)),
    ((1.0, 2.0, 3.0), (1.0, 2.0, 3.0)),
    ((1.0, 2.0, 3.0, 4.0), (1.0, 2.0, 3.0, 4.0))
])
def test_safe_numbers(numbers: str, result: str) -> None:
    assert SafeNumbers(numbers).value() == result


@pytest.mark.parametrize("numbers, result", [
    ((1, '2'), 1),
    ((1, 2, '3'), 2),
    ((1, 2, 3, '4'), 3)
])
def test_safe_numbers_error(numbers: str, result: str) -> None:
    with pytest.raises(NumbersError):
        assert SafeNumbers(numbers).value() == result
