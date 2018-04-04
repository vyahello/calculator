from abc import ABC, ABCMeta, abstractmethod
from functools import reduce
from typing import Union, Iterable
from calculator.numbers import SafeNumbers
from logger.logger import logger, obj_log

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

    @obj_log(_log)
    def perform(self) -> Union[int, float]:
        operation = ' + '.join(map(str, self._numbers.value()))
        _log.info('Calculating %s', operation)
        result = reduce(lambda x, y: x + y, self._numbers.value())
        _log.info('Result of %s equals to %s', operation, result)
        return result


class Subtract(Operation):
    """Represent subtract operation."""

    def __init__(self, numbers: Iterable[int]) -> None:
        self._numbers = SafeNumbers(numbers)

    @obj_log(_log)
    def perform(self) -> Union[int, float]:
        operation = ' - '.join(map(str, self._numbers.value()))
        _log.info('Calculating %s', operation)
        result = reduce(lambda x, y: x - y, self._numbers.value())
        _log.info('Result of %s equals to %s', operation, result)
        return result


class Multiply(Operation):
    """Represent multiply operation."""

    def __init__(self, numbers: Iterable[int]) -> None:
        self._numbers = SafeNumbers(numbers)

    @obj_log(_log)
    def perform(self) -> Union[int, float]:
        operation = ' * '.join(map(str, self._numbers.value()))
        _log.info('Calculating %s', operation)
        result = reduce(lambda x, y: x * y, self._numbers.value())
        _log.info('Result of %s equals to %s', operation, result)
        return result


class Divide(Operation):
    """Represent multiply operation."""

    def __init__(self, numbers: Iterable[int]) -> None:
        self._numbers = SafeNumbers(numbers)

    @obj_log(_log)
    def perform(self) -> Union[int, float]:
        operation = ' / '.join(map(str, self._numbers.value()))
        _log.info('Calculating %s', operation)
        result = float('{:0.3f}'.format(reduce(lambda x, y: x / y, self._numbers.value())))
        _log.info('Result of %s equals to %s', operation, result)
        return result
