from options import Options


'''
Стандартная модель передачи цифровых данных
'''


class Model:
	def __init__(self, name: str):
		self.__name = name

	def go(self, options: Options):
		print(f'Go modeling')

		i = 0
		while i < options.count:
			self.__doIteration(i)
			i += 1

	def __doIteration(self, i: int):
		print(f'Do {i}')

	@property
	def name(self):
		return self.__name