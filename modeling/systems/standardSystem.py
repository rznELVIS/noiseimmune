from options import Options
from systems.dataSystem import DataSystem


'''
Стандартная модель передачи цифровых данных
'''


class StandardSystem(DataSystem):
	def __init__(self, name: str):
		super(StandardSystem, self).__init__(name)

	def go(self, options: Options):
		print(f'Go modeling')

		i = 0
		while i < options.count:
			self.__doIteration(i)
			i += 1

	def _doIteration(self, i: int):
		pass
