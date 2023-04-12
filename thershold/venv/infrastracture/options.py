class options:
	def __init__(self):
		self.__count = 1

	@propery
	def count(self):
		return self.__count

	@count.setter
	def name(self, value):
		self.__count = value