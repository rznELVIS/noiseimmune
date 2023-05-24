from abc import ABC, abstractmethod
"""
Базовый класс генераторов случайных слов.
"""
class RandomGenerator(ABC):
    """
    Генерация одного значения 0 или 1
    """
    @abstractmethod
    def Generate(self):
        pass

    """
    Генерация слова, указанной длинны, состоящего из значений 0 или 1.
    """
    @abstractmethod
    def GenerateMethod(self, i: int):
        pass