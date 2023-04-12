class Model:
	def __init__(self, name):
		self.__name = name

	def Go(self):
		print(f'Go modeling')

	@property
	def name(self):
		return self.__name