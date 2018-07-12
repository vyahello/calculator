from abc import ABC, ABCMeta, abstractmethod
from calculator.operations import Operation


class Converter(ABC):
    """Represent abstraction for a converter."""

    __metaclass__: type = ABCMeta

    @abstractmethod
    def perform(self) -> float:
        pass


class ToFloat(Converter):
    """Represent float converter."""

    def __init__(self, operation: Operation) -> None:
        self._operation = operation

    def perform(self) -> float:
        return float('{:0.3f}'.format(self._operation.perform()))
