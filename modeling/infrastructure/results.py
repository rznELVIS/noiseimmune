class Results:

    def __init__(self):
        self.__count = 0

    @property
    def count(self) -> int:
        return self.__count

    def addResultToCollection(self):
        self.__count = self.__count + 1

