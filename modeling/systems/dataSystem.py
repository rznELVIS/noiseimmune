from abc import ABC, abstractmethod

from generators.randomGenerator import RandomGenerator
from infrastructure.options import Options
from infrastructure.results import Results

"""
Базовый класс стандартная модели передачи цифровых данных
"""


class DataSystem(ABC):

    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def _getGenerator(self) -> RandomGenerator:
        pass

    @abstractmethod
    def _doIteration(self, i: int):
        pass

    def go(self, options: Options) -> Results:
        result: Results = Results()

        for i in range(0, options.count):
            self._doIteration(i)
            result.addResultToCollection()

        return result
