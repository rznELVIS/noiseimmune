class Options:
	def __init__(self):
		self.__count = 1

	@property
	def count(self):
		return self.__count

	@count.setter
	def count(self, value):
		self.__count = value