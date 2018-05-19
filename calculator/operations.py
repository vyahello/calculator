from abc import ABC, ABCMeta, abstractmethod
from functools import reduce
from typing import Iterable
from calculator.numbers import SafeNumbers


class Operation(ABC):
    """Represent abstraction for specific operation."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def perform(self) -> float:
        pass


class Add(Operation):
    """Represent add operation."""

    def __init__(self, numbers: Iterable[float]) -> None:
        self._numbers = SafeNumbers(numbers)

    def perform(self) -> float:
        return reduce(lambda x, y: x + y, self._numbers.value())


class Subtract(Operation):
    """Represent subtract operation."""

    def __init__(self, numbers: Iterable[float]) -> None:
        self._numbers = SafeNumbers(numbers)

    def perform(self) -> float:
        return reduce(lambda x, y: x - y, self._numbers.value())


class Multiply(Operation):
    """Represent multiply operation."""

    def __init__(self, numbers: Iterable[float]) -> None:
        self._numbers = SafeNumbers(numbers)

    def perform(self) -> float:
        return reduce(lambda x, y: x * y, self._numbers.value())


class Divide(Operation):
    """Represent multiply operation."""

    def __init__(self, numbers: Iterable[float]) -> None:
        self._numbers = SafeNumbers(numbers)

    def perform(self) -> float:
        return reduce(lambda x, y: x / y, self._numbers.value())
