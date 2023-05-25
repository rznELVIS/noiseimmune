class Options:
	def __init__(self):
		self.__count = 0

	@property
	def count(self) -> int:
		return self.__count

	@count.setter
	def count(self, value: int):
		self.__count = value
