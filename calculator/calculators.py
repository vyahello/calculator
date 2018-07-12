import logging
from abc import ABC, ABCMeta, abstractmethod
from typing import Union, Iterable
from calculator.converters import ToFloat, Converter
from calculator.operations import Add, Subtract, Multiply, Divide
from logger.logger import logger, obj_log

_log: logging.Logger = logger()



class Calculator(ABC):
    """Represent abstraction for specific calculator object."""

    __metaclass__: type = ABCMeta

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
    def divide(self) -> Union[int, float]:
        pass


class BasicCalculator(Calculator):
    """Represent basic calculator object."""

    def __init__(self, numbers: Iterable[float]) -> None:
        self._add: Converter = ToFloat(Add(numbers))
        self._subtract: Converter = ToFloat(Subtract(numbers))
        self._multiply: Converter = ToFloat(Multiply(numbers))
        self._divide: Converter = ToFloat(Divide(numbers))

    @obj_log(_log)
    def add(self) -> float:
        return self._add.perform()

    @obj_log(_log)
    def subtract(self) -> float:
        return self._subtract.perform()

    @obj_log(_log)
    def multiply(self) -> float:
        return self._multiply.perform()

    @obj_log(_log)
    def divide(self)-> float:
        return self._divide.perform()
