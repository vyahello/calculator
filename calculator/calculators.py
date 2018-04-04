from abc import ABC, ABCMeta, abstractmethod
from typing import Union, Iterable
from calculator.operations import Add, Subtract, Multiply, Divide


class Calculator(ABC):
    """Represent abstraction for specific calculator object."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def add(self) -> Union[int, float]:
        pass

    @abstractmethod
    def subtract(self) -> Union[int, float]:
        pass

    @abstractmethod
    def multiply(self) -> Union[int, float]:
        pass

    @abstractmethod
    def divide(self) -> str:
        pass


class BasicCalculator(Calculator):
    """Represent basic calculator object."""

    def __init__(self, numbers: Iterable[int]) -> None:
        self._add = Add(numbers)
        self._subtract = Subtract(numbers)
        self._multiply = Multiply(numbers)
        self._divide = Divide(numbers)

    def add(self) -> Union[int, float]:
        return self._add.perform()

    def subtract(self) -> Union[int, float]:
        return self._subtract.perform()

    def multiply(self) -> Union[int, float]:
        return self._multiply.perform()

    def divide(self)-> float:
        return self._divide.perform()
