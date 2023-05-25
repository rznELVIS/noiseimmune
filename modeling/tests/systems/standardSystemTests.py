import unittest
from systems.standardSystem import StandardSystem


class StandardSystemTests(unittest.TestCase):
    def test_name_is_set_as_in_constructor(self):
        model: StandardSystem = StandardSystem('тестовое имя')
        self.assertEqual(model.name, 'тестовое имя')


# Executing the tests in the above test case class
if __name__ == "__main__":
    unittest.main()