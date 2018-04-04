from abc import ABC, ABCMeta, abstractmethod
from functools import reduce
from typing import Union, Iterable
from calculator.numbers import SafeNumbers
from logger.logger import logger

_log = logger()


class Operation(ABC):
    """Represent abstraction for specific operation."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def perform(self) -> Union[int, float]:
        pass


class Add(Operation):
    """Represent add operation."""

    def __init__(self, numbers: Iterable[int]) -> None:
        self._numbers = SafeNumbers(numbers)

    def perform(self) -> Union[int, float]:
        _log.info('Performing adding operation of %s', ' + '.join(map(str, self._numbers.value())))
        result = reduce(lambda x, y: x + y, self._numbers.value())
        _log.info('Result of adding equals to %s', result)
        return result


class Subtract(Operation):
    """Represent subtract operation."""

    def __init__(self, numbers: Iterable[int]) -> None:
        self._numbers = SafeNumbers(numbers)

    def perform(self) -> Union[int, float]:
        _log.info('Performing subtracting operation of %s', ' - '.join(map(str, self._numbers.value())))
        result = reduce(lambda x, y: x - y, self._numbers.value())
        _log.info('Result of subtraction equals to %s', result)
        return result


class Multiply(Operation):
    """Represent multiply operation."""

    def __init__(self, numbers: Iterable[int]) -> None:
        self._numbers = SafeNumbers(numbers)

    def perform(self) -> Union[int, float]:
        _log.info('Performing multiplying operation of %s', ' * '.join(map(str, self._numbers.value())))
        result = reduce(lambda x, y: x * y, self._numbers.value())
        _log.info('Result of multiplication equals to %s', result)
        return result


class Divide(Operation):
    """Represent multiply operation."""

    def __init__(self, numbers: Iterable[int]) -> None:
        self._numbers = SafeNumbers(numbers)

    def perform(self) -> Union[int, float]:
        _log.info('Performing division operation of %s', ' - '.join(map(str, self._numbers.value())))
        result = float('{:0.3f}'.format(reduce(lambda x, y: x / y, self._numbers.value())))
        _log.info('Result of division equals to %s', result)
        return result
