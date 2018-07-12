from abc import ABC, abstractmethod
from argparse import Namespace
from typing import Callable, List
from calculator.calculators import BasicCalculator, Calculator


class Calculation(ABC):
    """Represent abstraction of calculation."""

    @abstractmethod
    def start(self) -> None:
        pass


class BasicCalculation(Calculation):
    """Represent object that performs basic calculation like `add`, `subtract`, `multiply` and `divide`."""

    def __init__(self, operation: Namespace) -> None:
        self._operation = operation
        self._calculate: Callable[[List[float]], Calculator] = lambda operations: BasicCalculator(operations)

    def start(self) -> None:
        if self._operation.add:
            self._calculate(self._operation.add).add()
        elif self._operation.subtract:
            self._calculate(self._operation.subtract).subtract()
        elif self._operation.multiply:
            self._calculate(self._operation.multiply).multiply()
        elif self._operation.divide:
            self._calculate(self._operation.divide).divide()
