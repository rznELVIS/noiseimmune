from abc import ABC, abstractmethod

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
