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
    def GenerateMethod(self, length: int):
        message: list[int] = []

        for i in range(0,  length):
            value = self.Generate()
            message.append(value)

        return message