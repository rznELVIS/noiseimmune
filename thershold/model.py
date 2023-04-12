from options import Options

class Model:
	def __init__(self, name: str):
		self.__name = name

	def Go(self, options: Options):
		print(f'Go modeling')

	@property
	def name(self):
		return self.__name