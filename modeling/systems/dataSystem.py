from abc import ABC, abstractmethod
from infrastructure.options import Options

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
    def _doIteration(self, i: int):
        pass

    def go(self, options: Options):
        for i in range(0, options.count):
            self._doIteration(i)
