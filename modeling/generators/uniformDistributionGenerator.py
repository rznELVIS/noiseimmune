import random
from randomGenerator import RandomGenerator

class UniformDistributionGenerator(RandomGenerator):
    def generate(self):
        value: float = random.random()

        if value > 0.5:
            return 1

        return 0
