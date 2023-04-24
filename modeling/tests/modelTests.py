import unittest
from model import Model

class TestModel(unittest.TestCase):
    def test_nameIsSet(self):
        model = Model('тестовое имя')
        self.assertEqual(model.name, 'тестовое имя')

# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()