import unittest
from generators.UniformDistributionGenerator import UniformDistributionGenerator


class TestUniformDistributionGenerator(unittest.TestCase):
    def test_message_length_is_set_correctly(self):
        # arrange
        message_length: int = 10

        # act
        generator: UniformDistributionGenerator = UniformDistributionGenerator()
        message = generator.GenerateMethod(message_length)

        # assert
        self.assertEqual(len(message),
                         message_length,
                         'Сгененированное сообщение в {name}.py имеет не корректную длинну.'
                                    .format(name=UniformDistributionGenerator.__name__))

    def test_message_contains_only_0_or_1(self):
        # arrange
        message_length: int = 15

        # act
        generator: UniformDistributionGenerator = UniformDistributionGenerator()
        message = generator.GenerateMethod(message_length)

        # assert
        for value in message:
            self.assertTrue(value == 1 or value == 0,
                'Сгененированное сообщение в {name}.py содержит не только 0 или 1.'
                            .format(name=UniformDistributionGenerator.__name__))


if __name__ == "__main__":
    unittest.main()