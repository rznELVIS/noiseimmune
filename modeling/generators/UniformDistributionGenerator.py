import random
from generators.RandomGenerator import RandomGenerator

class UniformDistributionGenerator(RandomGenerator):
    def Generate(self):
        value: float = random.random()

        if value > 0.5:
            return 1

        return 0;
