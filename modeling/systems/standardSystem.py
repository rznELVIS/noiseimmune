from ..generators.randomGenerator import RandomGenerator
from ..generators.uniformDistributionGenerator import UniformDistributionGenerator
from ..systems.dataSystem import DataSystem

'''
Стандартная модель передачи цифровых данных
'''

class StandardSystem(DataSystem):
	def __init__(self, name: str):
		super(StandardSystem, self).__init__(name)

	def _doIteration(self, i: int):
		pass

	def _getGenerator(self) -> RandomGenerator:
		generator: UniformDistributionGenerator = UniformDistributionGenerator()
		return generator
