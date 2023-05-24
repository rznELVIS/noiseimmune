from abc import ABC, abstractmethod


"""
Базовый класс генераторов случайных слов.
"""


class RandomGenerator(ABC):
    """
    Генерация одного значения 0 или 1
    """
    @abstractmethod
    def generate(self):
        pass

    """
    Генерация слова, указанной длинны, состоящего из значений 0 или 1.
    """
    def generateMessage(self, length: int):
        message: list[int] = []

        for i in range(0,  length):
            value = self.generate()
            message.append(value)

        return message
