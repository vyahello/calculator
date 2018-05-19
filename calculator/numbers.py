from abc import ABC, ABCMeta, abstractmethod
from typing import Iterable


class Numbers(ABC):
    """Represent abstraction for specific numbers."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def value(self) -> Iterable[int]:
        pass


class NumbersError(Exception):
    """Represent numbers error object."""
    pass


class SafeNumbers(Numbers):
    """Represent safe value of given numbers."""

    def __init__(self, numbers: Iterable[float]) -> None:
        self._numbers = numbers

    def value(self) -> Iterable[float]:
        for num in self._numbers:
            if num.__class__ != float:
                raise NumbersError('{} type is not supported'.format(num.__class__))
        return self._numbers
