import pytest
from calculator.numbers import SafeNumbers, NumbersError


@pytest.mark.parametrize("numbers, result", [
    ((1, 2), (1, 2)),
    ((1, 2, 3), (1, 2, 3)),
    ((1, 2, 3, 4), (1, 2, 3, 4))
])
def test_safe_numbers(numbers, result):
    assert SafeNumbers(tuple(map(float, numbers))).value() == result


@pytest.mark.parametrize("numbers, result", [
    ((1, '2'), 1),
    ((1, 2, '3'), 2),
    ((1, 2, 3, '4'), 3)
])
def test_safe_numbers_error(numbers, result):
    with pytest.raises(NumbersError):
        assert SafeNumbers(numbers).value() == result
