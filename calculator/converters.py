from abc import ABC, ABCMeta, abstractmethod
from calculator.operations import Operation


class Converter(ABC):
    """Represent abstraction for a converter."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def prepare(self) -> float:
        pass


class ToFloat(Converter):
    """Represent float converter."""

    def __init__(self, operation: Operation) -> None:
        self._operation = operation

    def prepare(self) -> float:
        return float('{:0.3f}'.format(self._operation.perform()))
